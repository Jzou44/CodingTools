// Run against npm run dev, or point COMPRESSION_TEST_URL at a static build.
const assert = require("node:assert/strict");
const fs = require("node:fs/promises");
const { chromium } = require("playwright-core");
const JSZip = require("../src/js/jszip.min");
const site = require("../src/_data/site");

async function makeFixtures(page) {
  const encoded = await page.evaluate(() => {
    const canvas = document.createElement("canvas");
    canvas.width = 720;
    canvas.height = 480;
    const ctx = canvas.getContext("2d");
    const pixels = ctx.createImageData(canvas.width, canvas.height);
    let seed = 7919;
    for (let i = 0; i < pixels.data.length; i++) {
      seed = (Math.imul(seed, 1664525) + 1013904223) >>> 0;
      pixels.data[i] = i % 4 === 3 ? 255 : seed >>> 24;
    }
    ctx.putImageData(pixels, 0, 0);
    ctx.fillStyle = "#cc3322";
    ctx.fillRect(0, 0, 90, 60);
    const noisy = canvas.toDataURL("image/jpeg", 0.99).split(",")[1];
    canvas.width = 32;
    canvas.height = 64;
    ctx.fillStyle = "#2244cc";
    ctx.fillRect(0, 0, 32, 64);
    const small = canvas.toDataURL("image/jpeg").split(",")[1];
    function transparentPng(width, height, color) {
      canvas.width = width;
      canvas.height = height;
      ctx.fillStyle = color;
      ctx.fillRect(0, 0, width / 2, height);
      ctx.globalAlpha = 0.5;
      ctx.fillRect(width / 2, 0, width / 4, height);
      return canvas.toDataURL("image/png").split(",")[1];
    }
    return {
      noisy, small,
      wide: transparentPng(320, 180, "#cc3322"),
      tall: transparentPng(96, 176, "#2244cc")
    };
  });
  return Object.fromEntries(Object.entries(encoded).map(([key, value]) => [key, Buffer.from(value, "base64")]));
}

// Compare decoded pixels, including alpha, independently of compression and metadata.
async function inspect(page, bytes) {
  return page.evaluate(async base64 => {
    const bytes = Uint8Array.from(atob(base64), c => c.charCodeAt(0));
    const bitmap = await createImageBitmap(new Blob([bytes]));
    const canvas = document.createElement("canvas");
    canvas.width = bitmap.width;
    canvas.height = bitmap.height;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(bitmap, 0, 0);
    bitmap.close();
    const { data } = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const digest = Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", data)));
    const pixel = (x, y) => {
      const pos = (y * canvas.width + x) * 4;
      return [...data.slice(pos, pos + 4)];
    };
    return {
      width: canvas.width, height: canvas.height, digest,
      marker: pixel(Math.floor(canvas.width / 16), Math.floor(canvas.height / 16)),
      alpha: [1 / 4, 5 / 8, 7 / 8].map(x => pixel(Math.floor(canvas.width * x), 0)[3])
    };
  }, bytes.toString("base64"));
}

function file(type, buffer) {
  return { name: type === "jpeg" ? "sample.jpg" : "sample.png", mimeType: "image/" + type, buffer };
}

async function download(page, button) {
  const [transfer] = await Promise.all([page.waitForEvent("download"), button.click()]);
  return { name: transfer.suggestedFilename(), bytes: await fs.readFile(await transfer.path()) };
}

function checkJpegMarker(image, original) {
  // JPEG quantization can shift RGB values in our solid-color corner patch.
  original.marker.slice(0, 3).forEach((c, i) => assert.ok(Math.abs(image.marker[i] - c) < 25));
}

async function checkBatch(page, type, inputs, originals) {
  const input = page.locator("#file-input");
  const links = page.locator("#file-list a[download]");
  const all = page.locator("#btn-download-all");
  const ext = type === "jpeg" ? "jpg" : "png";
  await input.setInputFiles(file(type, inputs[0]));
  const single = await download(page, links.first());
  assert.equal(single.name, "sample-compressed." + ext);
  assert.ok(single.bytes.length < inputs[0].length, type + " should shrink the compressible fixture");
  assert.deepEqual(await download(page, all), single);
  await input.setInputFiles(file(type, inputs[1]));
  await links.nth(1).waitFor();
  const archive = await download(page, all);
  assert.equal(archive.name, "compressed-" + type + ".zip");
  const zip = await JSZip.loadAsync(archive.bytes, { checkCRC32: true });
  const names = ["sample-compressed." + ext, "sample-compressed-2." + ext];
  assert.deepEqual(Object.keys(zip.files).sort(), names.slice().sort());
  for (const [i, name] of names.entries()) {
    const bytes = await zip.file(name).async("nodebuffer");
    if (i === 0) assert.deepEqual(bytes, single.bytes);
    const image = await inspect(page, bytes);
    assert.equal(image.width, originals[i].width);
    assert.equal(image.height, originals[i].height);
    if (type === "png") assert.deepEqual(image.digest, originals[i].digest);
    else checkJpegMarker(image, originals[i]);
  }
  return single.bytes;
}

async function checkJpegTargets(page, fixtures, original) {
  const mode = page.locator("#compression-mode");
  const input = page.locator("#file-input");
  const links = page.locator("#file-list a[download]");
  const custom = page.locator("#target-kb");
  await page.locator("#btn-clear").click();
  await mode.selectOption("200");
  await input.setInputFiles(file("jpeg", fixtures.noisy));
  let previous = fixtures.noisy.length;
  for (const limit of [200, 100, 32]) {
    if (limit === 100) await mode.selectOption("100");
    if (limit === 32) {
      await mode.selectOption("custom");
      await custom.fill(String(limit));
    }
    const { bytes } = await download(page, links.first());
    assert.ok(bytes.length <= limit * 1000 && bytes.length < previous, "JPEG target " + limit + " KB");
    previous = bytes.length;
    const image = await inspect(page, bytes);
    assert.deepEqual([image.width, image.height], [original.width, original.height]);
    checkJpegMarker(image, original);
  }

  await custom.fill("2");
  const unmet = await page.locator("#jpeg-options").getAttribute("data-unmet");
  assert.ok(unmet);
  await page.locator("#file-list .file-status").filter({ hasText: unmet }).waitFor();
  assert.equal(await links.count(), 0);
  assert.ok(await page.locator("#btn-download-all").isDisabled());
  await page.locator("#allow-resize").check();
  const resized = await download(page, links.first());
  assert.ok(resized.bytes.length <= 2000);
  const image = await inspect(page, resized.bytes);
  assert.ok(image.width < original.width && image.height < original.height);
  assert.ok(Math.abs(image.height - image.width * original.height / original.width) <= 1);

  await page.locator("#btn-clear").click();
  await mode.selectOption("100");
  await input.setInputFiles(file("jpeg", fixtures.small));
  assert.deepEqual((await download(page, links.first())).bytes, fixtures.small);
}

async function main() {
  const origin = new URL(process.env.COMPRESSION_TEST_URL || "http://127.0.0.1:5500").origin;
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    const page = await browser.newPage();
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    await page.route(/^https?:\/\//, route =>
      new URL(route.request().url()).origin === origin ? route.continue() : route.abort());
    await page.goto(origin + site.pathFor("en", "compress-jpeg"));
    const fixtures = await makeFixtures(page);
    assert.ok(fixtures.noisy.length > 200000);
    const jpegInputs = [fixtures.noisy, fixtures.small];
    const pngInputs = [fixtures.wide, fixtures.tall];
    const jpegOriginals = await Promise.all(jpegInputs.map(bytes => inspect(page, bytes)));
    const pngOriginals = await Promise.all(pngInputs.map(bytes => inspect(page, bytes)));
    for (const image of pngOriginals) {
      assert.equal(image.alpha[0], 255);
      assert.ok(image.alpha[1] === 127 || image.alpha[1] === 128);
      assert.equal(image.alpha[2], 0);
    }

    for (const lang of site.languageIds) {
      const jpeg = await page.goto(origin + site.pathFor(lang, "compress-jpeg"));
      assert.equal(jpeg.status(), 200);
      await checkBatch(page, "jpeg", jpegInputs, jpegOriginals);
      await checkJpegTargets(page, fixtures, jpegOriginals[0]);
      const png = await page.goto(origin + site.pathFor(lang, "compress-png"));
      assert.equal(png.status(), 200);
      const optimized = await checkBatch(page, "png", pngInputs, pngOriginals);
      await page.locator("#btn-clear").click();
      await page.locator("#file-input").setInputFiles(file("png", optimized));
      const again = await download(page, page.locator("#file-list a[download]").first());
      assert.ok(again.bytes.length <= optimized.length);
      if (again.bytes.length === optimized.length) assert.deepEqual(again.bytes, optimized);
      assert.deepEqual((await inspect(page, again.bytes)).digest, pngOriginals[0].digest);
      console.log(lang + " passed: JPEG size limits and resize, lossless PNG " +
        fixtures.wide.length + " → " + optimized.length + " B, duplicate-name ZIPs");
    }
    assert.deepEqual(errors, []);
    console.log("Verified all nine languages in Chrome " + browser.version());
  } finally {
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
