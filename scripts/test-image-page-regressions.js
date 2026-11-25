// Run against a local build served through HTTP.
const assert = require("node:assert/strict");
const fs = require("node:fs/promises");
const { chromium } = require("playwright-core");
const site = require("../src/_data/site");
const pixel = require("../src/_data/toolData/photo2pixel.json");
const jszip = require("../src/js/jszip.min");

const origin = new URL(process.env.IMAGE_TEST_URL || "http://127.0.0.1:5500").origin;
const portrait = "src/assets/examples/portrait.png";
// 1x1, single-channel TIFF written by Pillow, with the Make IFD set to Acme.
const tiff = Buffer.from("SUkqAAgAAAAKAAABBAABAAAAAQAAAAEBBAABAAAAAQAAAAIBAwABAAAACAAAAAMBAwABAAAAAQAAAAYBAwABAAAAAQAAAA8BAgAFAAAAhgAAABEBBAABAAAAjAAAABYBBAABAAAAAQAAABcBBAABAAAAAQAAABwBAwABAAAAAQAAAAAAAABBY21lAAAq", "base64");
// Pillow EXIF payload with N 31°30'30", W 122°30'30" and no altitude.
const exif = Buffer.from("RXhpZgAATU0AKgAAAAgAAgEPAAIAAAAFAAAAJoglAAQAAAABAAAALAAAAABBY21lAAAABAABAAIAAAACTgAAAAACAAUAAAADAAAAYgADAAIAAAACVwAAAAAEAAUAAAADAAAAegAAAAAAAAAfAAAAAQAAAB4AAAABAAAAHgAAAAEAAAB6AAAAAQAAAB4AAAABAAAAHgAAAAE=", "base64");
// Use a non-unit denominator to distinguish rational values from their numerators.
exif.writeUInt32BE(120, 6 + 98 + 16);
exif.writeUInt32BE(4, 6 + 98 + 20);

function app1(payload) {
  const header = Buffer.from([0xff, 0xe1, 0, 0]);
  header.writeUInt16BE(payload.length + 2, 2);
  return Buffer.concat([header, payload]);
}

async function download(page, selector) {
  const [file] = await Promise.all([page.waitForEvent("download"), page.locator(selector).click()]);
  return { name: file.suggestedFilename(), bytes: await fs.readFile(await file.path()) };
}

async function checkExif(page, jpeg) {
  const input = page.locator("#file-input");
  const segments = [app1(exif)];
  for (const withXmp of [false, true]) {
    if (withXmp) segments.unshift(app1(Buffer.from("http://ns.adobe.com/xap/1.0/\0<x:xmpmeta/>")));
    const bytes = Buffer.concat([jpeg.subarray(0, 2), ...segments, jpeg.subarray(2)]);
    await input.setInputFiles({ name: "gps.jpg", mimeType: "image/jpeg", buffer: bytes });
    await page.locator("#status-message.valid").waitFor();
    const rows = await page.locator(".exif-table tbody tr").allTextContents();
    assert.ok(rows.includes("GPSLatitude31.508333"), rows.join(", "));
    assert.ok(rows.includes("GPSLongitude-122.508333"), rows.join(", "));
    assert.ok(rows.every(row => !row.startsWith("GPSAltitude")));
  }
  await input.setInputFiles({ name: "camera.tif", mimeType: "image/tiff", buffer: tiff });
  await page.locator("#status-message.valid").waitFor();
  assert.ok((await page.locator(".exif-table tbody tr").allTextContents()).includes("MakeAcme"));
}

async function dropOversize(page) {
  // Build the file in the browser so the automation transport needn't transfer 10 MiB.
  await page.evaluate(() => {
    const files = new DataTransfer();
    files.items.add(new File([new Uint8Array(10 * 1024 * 1024 + 1)], "large.jpg", { type: "image/jpeg" }));
    document.querySelector("#dropzone").dispatchEvent(new DragEvent("drop", { dataTransfer: files, bubbles: true }));
  });
  await page.locator("#status-message.invalid").waitFor();
  assert.match(await page.locator("#status-text").innerText(), /10/);
}

async function holdNextCanvasExport(page) {
  await page.evaluate(() => {
    const original = HTMLCanvasElement.prototype.toBlob;
    HTMLCanvasElement.prototype.toBlob = function (callback, ...options) {
      HTMLCanvasElement.prototype.toBlob = original;
      original.call(this, blob => { window.releaseOldExport = () => callback(blob); }, ...options);
    };
  });
}

async function checkRemover(page) {
  const input = page.locator("#file-input");
  await holdNextCanvasExport(page);
  await input.setInputFiles(portrait);
  await page.waitForFunction(() => typeof window.releaseOldExport === "function");
  await page.locator("#btn-clear").click();
  await page.evaluate(() => window.releaseOldExport());
  assert.equal(await page.locator("#file-list").innerText(), "");
  assert.match(await page.locator("#file-count").innerText(), /^0/);
  assert.equal(await page.locator("#btn-download-all").isDisabled(), true);
  await dropOversize(page);
  assert.match(await page.locator("#file-list").innerText(), /10/);
  await input.setInputFiles(portrait);
  await page.locator("#file-list a[download]").first().waitFor();
  const one = await download(page, "#btn-download-all");
  assert.match(one.name, /\.png$/);
  assert.equal(one.bytes.readUInt32BE(0), 0x89504e47);
  await input.setInputFiles("src/assets/examples/landscape-gps.jpg");
  await page.locator("#file-list a[download]").nth(1).waitFor();
  const many = await download(page, "#btn-download-all");
  assert.match(many.name, /\.zip$/);
  assert.equal(Object.keys((await jszip.loadAsync(many.bytes)).files).length, 2);
}

async function checkDimensions(page, crop) {
  await page.locator("#file-input").setInputFiles(portrait);

  await page.waitForFunction(() => !document.querySelector("#btn-download").disabled);
  await holdNextCanvasExport(page);
  await page.locator("#width-input").fill("310");
  await page.waitForFunction(() => typeof window.releaseOldExport === "function");
  const disabled = await page.evaluate(crop => {
    function change(id, value) {
      const field = document.querySelector(id);
      field.value = value;
      field.dispatchEvent(new Event("input", { bubbles: true }));
    }
    change("#width-input", crop ? 1 : 300);
    if (crop) change("#height-input", 1);
    window.releaseOldExport();
    return document.querySelector("#btn-download").disabled;
  }, crop);
  assert.equal(disabled, true);
  await page.waitForFunction(() => !document.querySelector("#btn-download").disabled);
  const out = await download(page, "#btn-download");
  assert.deepEqual([out.bytes.readUInt32BE(16), out.bytes.readUInt32BE(20)], crop ? [1, 1] : [300, 450]);
}

async function run() {
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    const page = await browser.newPage();
    await page.route(/^https?:\/\//, route => {
      const url = new URL(route.request().url());
      const modelRuntime = url.origin === "https://cdn.jsdelivr.net" && url.pathname.startsWith("/npm/onnxruntime-web@");
      return url.origin === origin || modelRuntime ? route.continue() : route.abort();
    });
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    const jpeg = await fs.readFile("src/assets/examples/landscape-gps.jpg");
    for (const lang of site.languageIds) {
      const visit = slug => page.goto(origin + site.pathFor(lang, slug));
      await visit("exif-viewer");
      await checkExif(page, jpeg);
      await dropOversize(page);
      assert.equal(await page.locator(".exif-table tbody tr").count(), 0);
      await visit("exif-remover");
      await checkRemover(page);
      await visit("image-crop");
      await checkDimensions(page, true);
      await visit("image-resize");
      await checkDimensions(page, false);
      await visit("image-to-base64");
      const input = page.locator("#file-input");
      await input.setInputFiles(portrait);
      await page.locator("#status-message.valid").waitFor();
      await input.setInputFiles({ name: "sample.txt", mimeType: "text/plain", buffer: Buffer.from("abc") });
      await page.locator("#status-message.invalid").waitFor();
      const disguisedText = { name: "sample.jpg", mimeType: "image/jpeg", buffer: Buffer.from("abc") };
      await input.setInputFiles(disguisedText);
      await page.locator("#status-message.invalid").waitFor();
      assert.equal(await page.evaluate(() => document.querySelector(".CodeMirror").CodeMirror.getValue()), "");
      await page.click("#batch-tab-batch");
      await page.locator("#batch-file-input").setInputFiles(disguisedText);
      await page.click("#batch-run");
      await page.locator("#batch-results-body .batch-status-error").waitFor();
      assert.ok(await page.isDisabled("#batch-download"));
      await visit("photo2pixel");
      await page.locator("#file-input").setInputFiles("src/assets/img/photo2pixel/cat.webp");
      await page.locator("#status-message.valid").waitFor({ timeout: 90000 });
      assert.equal(await page.locator("#status-text").innerText(), pixel[lang].status.generated);
      await dropOversize(page);
      assert.equal(await page.locator("#status-text").innerText(), pixel[lang].status.tooLarge);
      console.log(lang + " passed EXIF, image cleanup and downloads, crop, resize, image Base64 and pixel-art checks");
    }
    assert.deepEqual(errors, []);
  } finally {
    await browser.close();
  }
}

run().catch(error => { console.error(error); process.exitCode = 1; });
