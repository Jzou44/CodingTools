// Run against a built or development site. Blocks external resources in every case.
const assert = require("node:assert/strict");
const { createHash } = require("node:crypto");
const { chromium } = require("playwright-core");
const site = require("../src/_data/site");

const origin = new URL(process.env.TEXT_TOOL_TEST_URL || "http://127.0.0.1:5500").origin;
const formatSamples = {
  "json-minifier": '{"a": 1}', "json-to-xml": '{"a": 1}', "xml-to-json": "<a>1</a>",
  "xml-formatter": "<r><a/></r>", "xml-minifier": "<r><a/></r>",
  "javascript-beautifier": "let a = 1;", "javascript-minifier": "let a = 1;",
  "css-beautifier": "p { color: red; }", "css-minifier": "p { color: red; }",
  "html-beautifier": "<p>Hello</p>", "html-minifier": "<p>Hello</p>",
  "sql-formatter": "SELECT a FROM t;", "sql-minifier": "SELECT a FROM t;",
  "base64-encode": "Hello", "base64-decode": "SGVsbG8="
};

async function checkLanguage(browser, lang) {
  const page = await browser.newPage();
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  page.on("requestfailed", request => {
    if (request.url().startsWith(origin + "/") && request.resourceType() === "script") {
      errors.push(request.url() + " " + request.failure()?.errorText);
    }
  });
  await page.route("**/*", route => new URL(route.request().url()).origin === origin
    ? route.continue() : route.abort());
  async function open(slug) {
    const response = await page.goto(origin + site.pathFor(lang, slug));
    assert.equal(response.status(), 200);
  }
  async function checkFile(bytes, action, expected) {
    await page.locator('label:has(input[name="single-input-source"][value="file"])').click();
    await page.locator("#single-file-input").setInputFiles({
      name: "sample.txt", mimeType: "text/plain", buffer: bytes
    });
    await page.locator("#single-file-status.is-loaded").waitFor();
    await page.click(action);
    await page.waitForFunction(value => document.querySelector("#output-editor").value === value, expected);
  }
  async function checkEditedFile(action, expected) {
    await page.locator("#input-editor").press("Control+End");
    await page.locator("#input-editor").press("Tab");
    assert.equal(await page.inputValue("#input-editor"), "A\nB  ");
    await page.click(action);
    await page.waitForFunction(value => document.querySelector("#output-editor").value === value, expected);
  }
  async function checkBatchFiles(files, expected) {
    await page.click("#batch-tab-batch");
    await page.locator('label:has(input[name="batch-input-mode"][value="files"])').click();
    await page.locator("#batch-file-input").setInputFiles(files.map((buffer, i) => ({
      name: "sample-" + i + ".txt", mimeType: "text/plain", buffer
    })));
    await page.click("#batch-run");
    await page.locator("#batch-results-body .batch-output").first().waitFor();
    assert.deepEqual(await page.locator("#batch-results-body .batch-output").allTextContents(), expected);
  }
  try {
    for (const [slug, sample] of Object.entries(formatSamples)) {
      await open(slug);
      const action = slug.startsWith("base64-") ? "#btn-" + slug.slice(7) : "#btn-generate";
      await page.fill("#input-editor", sample);
      await page.click(action);
      assert.ok(await page.inputValue("#output-editor"), slug + " " + await page.textContent("#status-text"));
      await page.fill("#input-editor", "");
      await page.click(action);
      assert.equal(await page.inputValue("#output-editor"), "", slug);
    }

    const files = [Buffer.from("A\r\nB"), Buffer.from([0xef, 0xbb, 0xbf, 0xff, 0])];
    for (const algorithm of ["md5", "sha1", "sha256", "sha384", "sha512"]) {
      await open(algorithm + "-generator");
      const digest = value => createHash(algorithm).update(value).digest("hex");
      await checkFile(files[0], "#btn-generate", digest(files[0]));
      await checkEditedFile("#btn-generate", digest("A\nB  "));
      await checkFile(files[1], "#btn-generate", digest(files[1]));
      await page.fill("#input-editor", "");
      await page.click("#btn-generate");
      await page.waitForFunction(expected => document.querySelector("#output-editor").value === expected, digest(""));
      await checkBatchFiles(files, files.map(digest));
    }
    await open("base64-encode");
    await checkFile(files[0], "#btn-encode", files[0].toString("base64"));
    await checkEditedFile("#btn-encode", Buffer.from("A\nB  ").toString("base64"));
    await checkFile(files[1], "#btn-encode", files[1].toString("base64"));
    await checkBatchFiles(files, files.map(file => file.toString("base64")));

    await open("password-generator");
    await page.click("#btn-generate");
    assert.equal((await page.locator(".CodeMirror").evaluate(el => el.CodeMirror.getValue())).length, 16);

    for (const slug of ["regex-tester", "regex-replace"]) {
      await open(slug);
      await page.fill("#regex-input", "a");
      if (slug === "regex-replace") await page.fill("#replace-input", "X");
      for (const global of [false, true]) {
        await page.locator(".CodeMirror").evaluate(el => el.CodeMirror.setValue("aaa"));
        if (await page.isChecked("#flag-g") !== global) await page.locator("label:has(#flag-g)").click();
        assert.equal(await page.locator("#match-output mark").count(), global ? 3 : 1);
        if (slug === "regex-replace") {
          await page.click("#btn-replace");
          assert.equal(await page.locator(".CodeMirror").evaluate(el => el.CodeMirror.getValue()), global ? "XXX" : "Xaa");
        }
      }
    }
    await open("reverse-text");
    await page.fill("#input-editor", "A😀e\u0301B");
    await page.click("#btn-reverse");
    assert.equal(await page.inputValue("#input-editor"), "Be\u0301😀A");
    await open("case-converter");
    await page.fill("#input-editor", "école ouverte");
    await page.click("#btn-title");
    assert.equal(await page.inputValue("#input-editor"), "École Ouverte");

    await open("word-counter");
    await page.fill("#input-editor", "你好。世界！");
    assert.equal(await page.textContent("#stat-sentences"), "2");
    assert.equal(await page.textContent("#stat-words"), "2");
    const wordExample = await page.textContent("#example-code");
    await page.fill("#input-editor", wordExample.split("---")[2].trim());
    assert.equal(await page.textContent("#stat-chars-spaces"), "115");
    assert.equal(await page.textContent("#stat-paragraphs"), "2");
    assert.match(wordExample, /Paragraphs: 2/);
    await open("character-count");
    const charExample = await page.textContent("#example-code");
    await page.fill("#input-editor", charExample.split("---")[2].trim());
    assert.equal(await page.textContent("#stat-words"), "3");
    assert.equal(await page.textContent("#stat-lines"), "1");
    assert.match(charExample, /Words: 3\nLines: 1/);
    await open("text-editor");
    await page.locator(".CodeMirror").click();
    await page.keyboard.type("A");
    await page.keyboard.press("Tab");
    assert.equal(await page.locator(".CodeMirror").evaluate(el => el.CodeMirror.getValue()), "A  ");
    await page.locator(".CodeMirror").evaluate(el => {
      el.CodeMirror.setValue("one\ntwo");
      el.CodeMirror.execCommand("selectAll");
    });
    await page.keyboard.press("Tab");
    assert.equal(await page.locator(".CodeMirror").evaluate(el => el.CodeMirror.getValue()), "  one\n  two");

    await open("number-to-words");
    for (const value of ["1e2", "0x10", "4.5", "9007199254740993"]) {
      await page.fill("#input-number", "42");
      await page.locator("#status-message.valid").waitFor();
      await page.fill("#input-number", value);
      await page.locator("#status-message.invalid").waitFor();
      for (const id of ["result-word", "result-ordinal-word", "result-ordinal-number"]) {
        assert.doesNotMatch(await page.locator("#" + id).evaluate(el => el.value || el.textContent), /forty|42/);
      }
    }
    assert.deepEqual(errors, []);
    console.log("Text tool pages passed:", lang);
  } catch (error) {
    throw new Error([page.url(), error.message, ...errors].join(" "), { cause: error });
  } finally {
    await page.close();
  }
}

async function main() {
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    const ids = site.languages.map(language => language.id);
    for (let i = 0; i < ids.length; i += 3) {
      await Promise.all(ids.slice(i, i + 3).map(id => checkLanguage(browser, id)));
    }
  } finally {
    await browser.close();
  }
}
main().catch(error => { console.error(error); process.exitCode = 1; });
