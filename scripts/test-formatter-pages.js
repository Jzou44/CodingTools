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

  try {
    for (const [slug, input, check] of cases) {
      await open(slug);
      if (slug === "sql-formatter") await get("sql-dialect").selectOption("sqlite");
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
