// Run against npm run dev, or set HASH_TEST_URL to a served build.
const assert = require("node:assert/strict");
const { createHash } = require("node:crypto");
const { chromium } = require("playwright-core");
const { languageIds } = require("../src/_data/site");
const origin = new URL(process.env.HASH_TEST_URL || "http://localhost:5500").origin;
const algorithms = ["md5", "sha1", "sha256", "sha384", "sha512"];
const binary = Buffer.from([0xff, 0, 65, 13, 10, 226, 128, 168]);
const sample = "Hello 世界 🌍\r\n";
const sum = (algorithm, value) => createHash(algorithm).update(value).digest("hex");

async function verifyLanguage(browser, lang) {
  const page = await browser.newPage();
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  page.on("response", response => {
    if (response.url().startsWith(origin + "/") && response.request().resourceType() === "script" && !response.ok()) {
      errors.push(response.status() + " " + response.url());
    }
  });
  page.on("requestfailed", request => {
    if (request.url().startsWith(origin + "/") && request.resourceType() === "script") {
      errors.push(request.url() + " " + request.failure()?.errorText);
    }
  });
  await page.route("**/*", route => new URL(route.request().url()).origin === origin ? route.continue() : route.abort());
  page.setDefaultTimeout(6000);
  const get = id => page.locator("#" + id);
  const click = id => get(id).click();
  const fileMode = page.locator('input[name="single-input-source"][value="file"]');
  const textMode = page.locator('input[name="single-input-source"][value="text"]');
  const messages = require("../src/_data/t/" + lang + ".json").ui.hashCompare;
  const expectStatus = async target => assert.equal(await get("hash-comparison-status").textContent(), target);
  const expectDigest = target => page.waitForFunction(hash => document.getElementById("output-editor").value === hash, target);
  async function selectFile(name, bytes) {
    await fileMode.locator("..").click();
    await get("single-file-input").setInputFiles({ name, mimeType: "application/octet-stream", buffer: bytes });
    await page.locator("#single-file-status.is-loaded").waitFor();
  }
  try {
    for (const algorithm of algorithms) {
      const path = (lang === "en" ? "/" : "/" + lang + "/") + algorithm + "-generator.html";
      assert.equal((await page.goto(origin + path)).status(), 200);
      // This attribute is set by the first render, after the comparison listeners are installed.
      await page.locator('#expected-hash[aria-invalid="false"]').waitFor();
      const expected = get("expected-hash");
      assert.equal(await get("single-file-input").getAttribute("accept"), null);
      const textDigest = sum(algorithm, sample.replace("\r\n", "\n"));
      await get("input-editor").fill(sample);
      await expected.fill("  " + textDigest.toUpperCase() + "  ");
      await expectStatus(messages.pending);
      await click("btn-generate");
      await expectDigest(textDigest);
      await expectStatus(messages.match);
      await expected.fill("0".repeat(textDigest.length));
      await expectStatus(messages.mismatch);
      await expected.fill("g".repeat(textDigest.length));
      await expectStatus(messages.format.replace("{length}", textDigest.length));
      assert.equal(await expected.getAttribute("aria-invalid"), "true");
      await expected.fill(textDigest);
      await get("input-editor").fill("changed");
      await expectStatus(messages.pending);
      assert.ok(await get("btn-copy").isDisabled());
      await selectFile("binary.bin", binary);
      const fileDigest = sum(algorithm, binary);
      await expected.fill(fileDigest);
      await click("btn-generate");
      await expectDigest(fileDigest);
      await expectStatus(messages.match);
      await selectFile("empty.txt", Buffer.alloc(0));
      await expectStatus(messages.pending);
      await click("btn-generate");
      await expectDigest(sum(algorithm, ""));
      await expectStatus(messages.mismatch);
      await textMode.locator("..").click();
      await expectStatus(messages.pending);
      await click("btn-clear");
      await expectStatus("");
      assert.equal(await expected.inputValue(), "");
      await click("btn-generate");
      await expectDigest(sum(algorithm, ""));

      await click("batch-tab-batch");
      assert.ok(await expected.isHidden());
      await page.locator('[name="batch-input-mode"][value="files"]').locator("..").click();
      await get("batch-file-input").setInputFiles({ name: "verify.bin", mimeType: "application/octet-stream", buffer: binary });
      await click("batch-run");
      await page.locator(".batch-status-ok").waitFor();
      assert.equal(await page.locator(".batch-output").textContent(), fileDigest);
    }
    if (lang === "en") {
      await click("batch-tab-single");
      await selectFile("windows.txt", Buffer.from("A\r\nB"));
      await click("btn-generate");
      await expectDigest(sum("sha512", "A\r\nB"));
      await get("input-editor").fill("A\nB!");
      assert.ok(await textMode.isChecked());
      await click("btn-generate");
      await expectDigest(sum("sha512", "A\nB!"));

      await fileMode.locator("..").click();
      assert.ok(await get("btn-generate").isDisabled());
      await get("single-file-input").setInputFiles({ name: "large", mimeType: "application/octet-stream", buffer: Buffer.alloc(5 * 1024 * 1024 + 1) });
      await page.locator("#single-file-status.is-error").waitFor();
      assert.ok(await get("btn-generate").isDisabled());
      await textMode.locator("..").click();
      // Resolve a running digest after the user has cleared it.
      await page.evaluate(() => {
        const original = ToolCommon.hashBytes;
        ToolCommon.hashBytes = (...args) => new Promise(resolve => {
          window.finishDigest = async () => resolve(await original(...args));
        });
      });
      await click("btn-generate");
      await click("btn-clear");
      await page.evaluate(() => window.finishDigest());
      await expectDigest("");
      assert.ok(await get("btn-download").isDisabled());
    }
    assert.deepEqual(errors, []);
    console.log(lang + ": five hash generators verified");
  } catch (error) {
    throw new Error(page.url() + " (" + errors.join(", ") + "): " + error.message, { cause: error });
  } finally {
    await page.close();
  }
}
(async () => {
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    for (let offset = 0; offset < languageIds.length; offset += 3) {
      await Promise.all(languageIds.slice(offset, offset + 3).map(lang => verifyLanguage(browser, lang)));
    }
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
