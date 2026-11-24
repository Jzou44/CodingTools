// Run against npm run dev, or set PROGRESSIVE_JPEG_TEST_URL to a local build.
const assert = require("node:assert/strict");
const fs = require("node:fs/promises");
const path = require("node:path");
const { chromium } = require("playwright-core");
const JSZip = require("../src/js/jszip.min");
const site = require("../src/_data/site");

// Walk segments and entropy-coded scans, skipping stuffed bytes and restart
// markers. A thumbnail inside APP1 must never count as the main frame.
function inspectJpeg(bytes) {
  assert.equal(bytes.readUInt16BE(0), 0xffd8);
  const frames = [];
  let scans = 0;
  let pos = 2;
  while (pos < bytes.length) {
    assert.equal(bytes[pos++], 0xff);
    while (bytes[pos] === 0xff) pos++;
    const marker = bytes[pos++];
    if (marker === 0xd9) return { frames, scans };
    const length = bytes.readUInt16BE(pos);
    assert.ok(length >= 2 && pos + length <= bytes.length);
    if (marker >= 0xc0 && marker <= 0xcf && ![0xc4, 0xc8, 0xcc].includes(marker)) frames.push(marker);
    pos += length;
    if (marker === 0xda) {
      scans++;
      for (;;) {
        pos = bytes.indexOf(0xff, pos);
        assert.notEqual(pos, -1, "Truncated scan");
        while (bytes[pos + 1] === 0xff) pos++;
        const next = bytes[pos + 1];
        if (next !== 0 && !(next >= 0xd0 && next <= 0xd7)) break;
        pos += 2;
      }
    }
  }
  assert.fail("Missing end of image");
}

async function download(page, button) {
  const [file] = await Promise.all([page.waitForEvent("download"), button.click()]);
  return { name: file.suggestedFilename(), bytes: await fs.readFile(await file.path()) };
}

async function checkImage(page, bytes, width, height) {
  const { frames, scans } = inspectJpeg(bytes);
  assert.deepEqual(frames, [0xc2], "Expected the main JPEG frame to be SOF2");
  assert.ok(scans > 1, "Expected multiple scans");
  const size = await page.evaluate(async (base64) => {
    const bytes = Uint8Array.from(atob(base64), c => c.charCodeAt(0));
    const bitmap = await createImageBitmap(new Blob([bytes], { type: "image/jpeg" }));
    const dimensions = [bitmap.width, bitmap.height];
    bitmap.close();
    return dimensions;
  }, bytes.toString("base64"));
  assert.deepEqual(size, [width, height]);
}

async function main() {
  const origin = new URL(process.env.PROGRESSIVE_JPEG_TEST_URL || "http://127.0.0.1:5500").origin;
  const fixture = await fs.readFile(path.join(__dirname, "../src/assets/examples/landscape-gps.jpg"));
  assert.deepEqual(inspectJpeg(fixture).frames, [0xc0]);
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    const page = await browser.newPage();
    const pageErrors = [];
    page.on("pageerror", error => pageErrors.push(error.message));
    await page.route(/^https?:\/\//, route =>
      new URL(route.request().url()).origin === origin ? route.continue() : route.abort());
    const portrait = await page.evaluate(() => {
      const canvas = document.createElement("canvas");
      canvas.width = 37;
      canvas.height = 61;
      const ctx = canvas.getContext("2d");
      ctx.fillStyle = "#468";
      ctx.fillRect(0, 0, 37, 61);
      return canvas.toDataURL("image/jpeg").split(",")[1];
    });
    for (const lang of site.languageIds) {
      const url = site.pathFor(lang, "progressive-jpeg");
      const response = await page.goto(origin + url);
      assert.equal(response.status(), 200, url);
      const input = page.locator("#file-input");
      const all = page.locator("#btn-download-all");
      const rows = page.locator("#file-list a[download]");
      await input.setInputFiles({ name: "photo.jpg", mimeType: "image/jpeg", buffer: fixture });
      const single = await download(page, rows.first());
      assert.equal(single.name, "photo-progressive.jpg");
      await checkImage(page, single.bytes, 1200, 800);
      const only = await download(page, all);
      assert.equal(only.name, single.name);
      assert.deepEqual(only.bytes, single.bytes);
      await input.setInputFiles({ name: "photo.jpeg", mimeType: "image/jpeg", buffer: Buffer.from(portrait, "base64") });
      await rows.nth(1).waitFor();
      const archive = await download(page, all);
      assert.equal(archive.name, "progressive-jpeg.zip");
      const zip = await JSZip.loadAsync(archive.bytes);
      assert.deepEqual(Object.keys(zip.files), ["photo-progressive.jpg", "photo-progressive-2.jpg"]);
      await checkImage(page, await zip.file("photo-progressive.jpg").async("nodebuffer"), 1200, 800);
      await checkImage(page, await zip.file("photo-progressive-2.jpg").async("nodebuffer"), 37, 61);
      console.log(lang + ": single JPEG, single Download All and both ZIP entries passed (FFC2, multiple scans, decoded dimensions)");
    }
    // Failed rows remain visible, but only active, queued or successful files
    // occupy one of the 20 download slots.
    await page.locator("#btn-clear").click();
    const valid = { name: "valid.jpg", mimeType: "image/jpeg", buffer: fixture };
    const invalid = Array.from({ length: 19 }, (_, i) => ({
      name: "bad-" + i + ".jpg", mimeType: "image/jpeg", buffer: Buffer.from("invalid")
    }));
    const input = page.locator("#file-input");
    await input.setInputFiles([valid, ...invalid]);
    await page.waitForFunction(() => !document.getElementById("btn-download-all").disabled);
    await input.setInputFiles(valid);
    await page.locator("#file-list a[download]").nth(1).waitFor();
    assert.equal(await page.locator("#file-list .file-item").count(), 21);
    assert.deepEqual(pageErrors, []);
    console.log("Verified all nine locales in Chrome " + browser.version());
  } finally {
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
