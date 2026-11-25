// Run against a local Eleventy build. The same ONNX/WASM runtime as production is required.
const assert = require("node:assert/strict");
const { readFile } = require("node:fs/promises");
const { chromium } = require("playwright-core");
const site = require("../src/_data/site");

const origin = new URL(process.env.PHOTO2PIXEL_TEST_URL || "http://127.0.0.1:5500").origin;

async function waitForResult(page) {
  await page.waitForFunction(() =>
    !document.querySelector("#btn-download").disabled ||
    document.querySelector("#status-message").classList.contains("invalid"),
  null, { timeout: 90000 });
  assert.equal(await page.locator("#status-text").innerText(), "Pixel art generated");
}

async function eventCount(page, name, source) {
  return page.evaluate(({ name, source }) =>
    window.testEvents.filter(event => event.name === name && event.params.input_source === source).length,
  { name, source });
}

async function downloadPng(page) {
  const [download] = await Promise.all([page.waitForEvent("download"), page.locator("#btn-download").click()]);
  assert.equal(download.suggestedFilename(), "photo2pixel.png");
  const png = await readFile(await download.path());
  assert.equal(png.subarray(0, 8).toString("hex"), "89504e470d0a1a0a");
  const size = await page.locator("#result-canvas").evaluate(canvas => [canvas.width, canvas.height]);
  assert.deepEqual([png.readUInt32BE(16), png.readUInt32BE(20)], size);
}

async function comparePreview(page, id) {
  const meanError = await page.evaluate(async id => {
    const preview = document.querySelector('[data-example="' + id + '"]').closest("article").querySelectorAll("img")[1];
    await preview.decode();
    const canvas = document.createElement("canvas");
    canvas.width = preview.naturalWidth;
    canvas.height = preview.naturalHeight;
    const ctx = canvas.getContext("2d");
    const pixels = image => {
      ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
      return ctx.getImageData(0, 0, canvas.width, canvas.height).data;
    };
    const thumbnail = pixels(preview);
    const result = pixels(document.querySelector("#result-canvas"));
    let difference = 0;
    for (let i = 0; i < result.length; i++) difference += Math.abs(result[i] - thumbnail[i]);
    return difference / result.length;
  }, id);
  assert.ok(meanError < 6, id + " preview differs from its real model output: " + meanError);
}

async function main() {
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    await page.route(/^https?:\/\//, route => {
      const url = new URL(route.request().url());
      const runtime = url.origin === "https://cdn.jsdelivr.net" && url.pathname.startsWith("/npm/onnxruntime-web@");
      return (url.origin === origin || runtime) ? route.continue() : route.abort();
    });
    await page.goto(origin + site.pathFor("en", "photo2pixel"));
    await page.evaluate(() => {
      window.testEvents = [];
      window.gtag = (type, name, params) => {
        if (type === "event") window.testEvents.push({ name, params });
      };
    });
    const examples = page.locator("[data-example]");
    assert.equal(await examples.count(), 3);
    for (const id of ["cat", "mountains", "coffee"]) {
      await page.locator('[data-example="' + id + '"]').click();
      await waitForResult(page);
      await comparePreview(page, id);
    }
    assert.equal(await eventCount(page, "tool_success", "example"), 3);
    await page.locator('label[for="pixel-size-lg"]').click();
    await waitForResult(page);
    assert.equal(await eventCount(page, "tool_success", "example"), 3);
    await downloadPng(page);
    assert.equal(await eventCount(page, "tool_export", "example"), 1);

    // Hold one real canvas export until after the user has cleared the work area.
    await page.evaluate(() => {
      const toBlob = HTMLCanvasElement.prototype.toBlob;
      const canvas = document.querySelector("#result-canvas");
      canvas.toBlob = function (callback, type) {
        delete canvas.toBlob;
        toBlob.call(this, blob => { window.releaseOldExport = () => callback(blob); }, type);
      };
      document.querySelector('[data-example="cat"]').click();
    });
    await page.waitForFunction(() => typeof window.releaseOldExport === "function");
    await page.locator("#btn-clear").click();
    await page.evaluate(() => window.releaseOldExport());
    assert.equal(await page.locator("#btn-download").isDisabled(), true);
    assert.equal(await eventCount(page, "tool_success", "example"), 3);

    // A user upload must supersede an example, including a pending model run.
    await page.locator('[data-example="mountains"]').click();
    await page.locator("#file-input").setInputFiles("src/assets/img/photo2pixel/coffee.webp");
    await waitForResult(page);
    assert.equal(await eventCount(page, "tool_success", "upload"), 1);
    await downloadPng(page);
    assert.equal(await eventCount(page, "tool_export", "upload"), 1);
    for (const { name, params } of await page.evaluate(() => window.testEvents)) {
      assert.deepEqual(Object.keys(params).sort(), ["input_source", "operation", "tool_id", "tool_language"]);
      assert.equal(params.tool_id, "photo2pixel");
      assert.equal(params.tool_language, "en");
      assert.equal(params.operation, name === "tool_export" ? "download_png" : "photo_to_pixel");
    }
    for (const { id } of site.languages.filter(lang => lang.id !== "en")) {
      const res = await page.request.get(origin + site.pathFor(id, "photo2pixel"));
      assert.ok(res.ok());
      assert.doesNotMatch(await res.text(), /data-example="/);
    }
    await page.setViewportSize({ width: 1280, height: 800 });
    await page.goto(origin + site.pathFor("tw", "photo2pixel"));
    await page.locator("#file-input").setInputFiles("src/assets/img/photo2pixel/cat.webp");
    await page.waitForFunction(() => !document.querySelector("#btn-download").disabled, null, { timeout: 90000 });
    await downloadPng(page);
    assert.deepEqual(errors, []);
    console.log("Verified 3 model-generated previews, upload and export events, stale-result handling and the English-only pilot.");
  } finally {
    await browser.close();
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
