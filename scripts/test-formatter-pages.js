// Run against npm run dev, or point FORMATTER_TEST_URL at a served static build.
const assert = require("node:assert/strict");
const { chromium } = require("playwright-core");
const { languageIds } = require("../src/_data/site");

const origin = process.env.FORMATTER_TEST_URL || "http://localhost:5500";
const exact = '{"n":9007199254740993,"m":1e400}';
const preserved = '<r xml:space="preserve"><a/> <b/></r>';
const sql = "SELECT '\\' AS s;";
const xml = "<root>\n  <name>John</name>\n  <age>30</age>\n</root>";
const compact = "<root><name>John</name><age>30</age></root>";

const cases = [
  ["json-minifier", exact, value => assert.equal(value, exact)],
  ["json-to-xml", exact, value => assert.match(value, /<n>9007199254740993<\/n>\s*<m>1e400<\/m>/)],
  ["javascript-beautifier", "function f(){return\n[1];}", value => assert.match(value, /return\s*[\r\n]\s*\[1\]/)],
  ["javascript-minifier", 'if (true) /[/*]/.test("x");', value => assert.ok(value.includes("/[/*]/"))],
  ["css-minifier", "div :first-child { color: red; }", value => assert.equal(value, "div :first-child{color:red}")],
  ["html-minifier", "<textarea><!--hello--></textarea>", value => assert.equal(value, "<textarea><!--hello--></textarea>")],
  ["xml-formatter", preserved, value => assert.equal(value, preserved)],
  ["xml-to-json", '<r xml:space="preserve"> </r>', value => assert.equal(JSON.parse(value).r["#text"], " ")],
  ["xml-minifier", xml, value => assert.equal(value, compact)],
  ["sql-minifier", sql, value => assert.equal(value, sql)],
  ["sql-formatter", sql, value => assert.match(value, /SELECT\s+'\\'\s+AS\s+s;/i)],
  ["url-decode", "https://example.test/a?debug", value => assert.equal(value.split("\n")[0], "https://example.test/a?debug")],
  ["url-encode", "x y", value => assert.equal(value, "x%20y")]
];

async function checkJsonWorkbench(page) {
  const input = page.locator("#input-editor");
  const output = page.locator("#output-editor");
  const colors = page.locator(".json-colors");
  const sample = { 'name"': '<b>中文 & JSON</b>', path: 'a\\b', list: [true, null, 3] };
  const expected = JSON.stringify(sample, null, 2);
  const originalViewport = page.viewportSize();

  for (const width of [390, 1440]) {
    await page.setViewportSize({ width, height: 900 });
    await input.fill(JSON.stringify(sample));
    await page.locator(".tool-editor-input #btn-generate").click();
    assert.equal(await output.inputValue(), expected);
    assert.equal(await colors.textContent(), expected);
    assert.equal(await colors.locator(".json-key").count(), 3);
    assert.equal(await colors.locator(".json-string").count(), 2);
    assert.equal(await colors.locator("b").count(), 0);
    const left = await input.boundingBox();
    const right = await output.boundingBox();
    if (width === 390) assert.ok(right.y > left.y + left.height);
    else assert.ok(right.x >= left.x + left.width);
    await page.locator(".tool-editor-output #btn-copy").click();
    assert.equal(await page.evaluate(() => navigator.clipboard.readText()), expected);
    await page.locator("#batch-tab-batch").click();
    assert.ok(await page.locator(".single-input-mode-row").isHidden());
    await page.locator("#batch-tab-single").click();
    assert.ok(await page.locator(".single-input-mode-row").isVisible());
    assert.equal(await output.inputValue(), expected);
  }
  await page.setViewportSize(originalViewport);

  const large = JSON.stringify("x".repeat(70000));
  await input.fill(large);
  await page.locator("#btn-generate").click();
  assert.equal(await output.inputValue(), large);
  assert.ok(await colors.isHidden());
  await input.fill("{");
  await page.locator("#btn-generate").click();
  assert.equal(await output.inputValue(), "");
  assert.equal(await colors.textContent(), "");
}

async function checkLanguage(browser, lang) {
  const context = await browser.newContext();
  await context.grantPermissions(["clipboard-read", "clipboard-write"], { origin: new URL(origin).origin });
  await context.route("**/*", route => {
    if (new URL(route.request().url()).origin === new URL(origin).origin) return route.continue();
    return route.abort();
  });
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  const open = slug => page.goto(origin + (lang === "en" ? "/" : "/" + lang + "/") + slug + ".html");
  const get = id => page.locator("#" + id);
  async function run(input) {
    await get("input-editor").fill(input);
    await get("btn-generate").click();
    return get("output-editor").inputValue();
  }
  async function emptyResult() {
    assert.equal(await get("output-editor").inputValue(), "");
    assert.ok(await get("btn-copy").isDisabled());
    assert.ok(await get("btn-download").isDisabled());
  }

  async function openSqlWithSlowLibrary() {
    const library = /\/js\/sqlformatter(?:\.[a-f0-9]+)?\.js(?:\?.*)?$/;
    const url = origin + (lang === "en" ? "/" : "/" + lang + "/") + "sql-formatter.html";
    const { promise: download, resolve: finishDownload } = Promise.withResolvers();
    await page.route(library, async route => {
      await download;
      await route.continue();
    });
    try {
      await page.goto(url, { waitUntil: "commit" });
      await get("input-editor").fill(sql);
      assert.ok(await get("btn-generate").isDisabled());
      assert.ok(await get("batch-run").isDisabled());
    } finally {
      finishDownload();
    }
    await page.waitForLoadState("domcontentloaded");
    assert.equal(await get("input-editor").inputValue(), sql);
    assert.ok(await get("btn-generate").isEnabled());
    assert.ok(await get("batch-run").isEnabled());
    await page.unroute(library);
  }

  try {
    if (lang === "cn") {
      await open("json-formatter");
      await checkJsonWorkbench(page);
    }
    for (const [slug, input, check] of cases) {
      if (slug === "sql-formatter") {
        await openSqlWithSlowLibrary();
        await get("sql-dialect").selectOption("sqlite");
      } else {
        await open(slug);
      }
      check(await run(input));
      if (["xml-formatter", "xml-minifier", "xml-to-json", "json-to-xml"].includes(slug)) {
        const expected = require("../src/_data/toolData/" + slug + ".json")[lang].exampleCode;
        assert.equal(await get("example-code").textContent(), expected);
        await get("example-copy").click();
        await page.waitForFunction(async text => await navigator.clipboard.readText() === text, expected);
      }
      if (slug === "xml-minifier") {
        await get("remove-xml-indent").uncheck();
        assert.equal(await run(xml), xml);
        assert.equal(await run(preserved), preserved);
      }
      if (slug === "sql-minifier") {
        await get("sql-dialect").selectOption("mysql");
        assert.equal(await run("SELECT /*! STRAIGHT_JOIN */ 1--2; # comment"), "SELECT /*! STRAIGHT_JOIN */ 1--2;");
      }
      if (slug === "url-decode") assert.equal(await run("https://example.test/a=b"), "https://example.test/a=b");
      if (slug.startsWith("url-")) {
        await run("");
        await emptyResult();
      }
      await get("batch-tab-batch").click();
      if (slug === "sql-formatter") await get("batch-sql-dialect").selectOption("sqlite");
      await page.locator('[name="batch-input-mode"][value="files"]').check();
      await get("batch-file-input").setInputFiles({ name: "example.txt", mimeType: "text/plain", buffer: Buffer.from(input) });
      await get("batch-run").click();
      await page.locator(".batch-status-ok").waitFor({ timeout: 3500 });
      check(await page.locator(".batch-output").textContent());
    }

    await open("json-diff");
    await get("left-editor").fill('{"n":9007199254740992}');
    await get("right-editor").fill('{"n":9007199254740993}');
    await get("btn-generate").click();
    assert.equal(await get("summary-changed").textContent(), "1");
    assert.match(await get("output-editor").inputValue(), /\$\.n[\s\S]*9007199254740992[\s\S]*9007199254740993/);
    await get("left-editor").fill("");
    await get("btn-generate").click();
    await emptyResult();
    assert.equal(await get("summary-changed").textContent(), "0");

    await open("text-compare");
    await get("right-editor").fill("hello");
    await get("btn-generate").click();
    assert.equal(await get("summary-added").textContent(), "1");
    assert.equal(await get("summary-changed").textContent(), "0");
    assert.deepEqual(errors, []);
    console.log(lang + " formatter, converter and diff page checks passed.");
  } catch (error) {
    const status = await page.locator("#status-message").textContent().catch(() => "");
    throw new Error(page.url() + " (" + status + ", " + errors.join(", ") + "): " + error.message, { cause: error });
  } finally {
    await context.close();
  }
}

(async () => {
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    for (const lang of languageIds) await checkLanguage(browser, lang);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
