// Run against a local build. All DNS replies are deterministic fixtures.
const assert = require("node:assert/strict");
const { chromium } = require("playwright-core");
const site = require("../src/_data/site");
const builtIn = require("../src/_data/toolData/nslookup.json");

const origin = new URL(process.env.DNS_TEST_URL || "http://127.0.0.1:5500").origin;
const languages = site.languages;
const domain = "example.com";
const record = { name: "example.com.", type: 1, TTL: 45, data: "192.0.2.1" };

async function run() {
  const browser = await chromium.launch({ channel: "chrome" });
  try {
    const context = await browser.newContext();
    let reply = { Status: 0, Answer: [record] };
    let handler;
    const queries = [];
    await context.route("**/*", async route => {
      const url = new URL(route.request().url());
      if (url.origin === origin) return route.continue();
      if (url.origin !== "https://dns.google" || url.pathname !== "/resolve") return route.abort();
      queries.push([url.searchParams.get("name"), url.searchParams.get("type")]);
      if (handler) return handler(route);
      return route.fulfill({ json: reply, headers: { "access-control-allow-origin": "*" } });
    });
    const page = await context.newPage();
    const errors = [];
    page.on("pageerror", error => errors.push(error.message));
    const name = page.locator("#dns-name");
    const form = page.locator("#dns-form");
    const status = page.locator("#dns-status");
    const answer = page.locator("#dns-answers tr");
    const type = page.locator("#dns-type");
    async function query(input, typeName = "A") {
      await name.fill(input);
      await type.selectOption(typeName);
      await form.getByRole("button").click();
    }
    async function hasStatus(message) {
      await status.getByText(message, { exact: true }).waitFor();
    }
    const sitemap = await (await context.request.get(origin + "/sitemap.xml")).text();
    for (const { id, htmlLang } of languages) {
      const path = site.pathFor(id, "nslookup");
      const text = builtIn[id];
      const response = await page.goto(origin + path);
      assert.equal(response.status(), 200, path);
      assert.equal(await page.locator("html").getAttribute("lang"), htmlLang);
      assert.equal(await page.title(), text.title);
      assert.equal(await page.locator("h1").innerText(), text.toolTitle);
      assert.equal(await form.getByRole("button").innerText(), text.dns.submit);
      assert.equal(await page.locator("link[rel=canonical]").getAttribute("href"), site.absoluteUrl(path));
      assert.equal(await page.locator("link[hreflang]").count(), languages.length + 1);
      assert.equal(await page.locator(".language-options a").count(), languages.length);
      assert.ok(sitemap.includes("<loc>" + site.absoluteUrl(path) + "</loc>"), path);
      const structured = JSON.parse(await page.locator("script[type='application/ld+json']").textContent())["@graph"];
      assert.equal(structured.find(x => x["@type"] === "WebApplication").name, text.toolTitle);
      assert.deepEqual(structured.find(x => x["@type"] === "HowTo").step.map(s => s.text), text.steps);
      assert.ok(await name.isVisible(), path);
      await query(domain);
      await hasStatus(text.dns.complete);
      assert.deepEqual(await answer.locator("td").allTextContents(), [record.name, "A", "45", record.data]);
      assert.deepEqual(queries.at(-1), [domain, "A"]);
    }

    await page.goto(origin + "/nslookup.html");
    const messages = builtIn.en.dns;
    const before = queries.length;
    await query("https://example.com/path");
    await hasStatus(messages.invalid);
    assert.equal(queries.length, before);
    reply = { Status: 0, Answer: [{ name: "_dmarc.example.com.", type: 16, TTL: 1, data: "<em>text</em>" }] };
    await query("_dmarc.example.com", "TXT");
    await hasStatus(messages.complete);
    assert.equal(await answer.locator("td").last().innerText(), "<em>text</em>");
    assert.equal(await answer.locator("em").count(), 0);
    reply = { Status: 3 };
    await query("bücher.example.", "AAAA");
    await hasStatus(messages.nxdomain);
    assert.deepEqual(queries.at(-1), ["xn--bcher-kva.example", "AAAA"]);
    assert.equal(await answer.count(), 0);
    reply = { Status: 0 };
    await query("*.example.com", "TXT");
    await hasStatus(messages.empty);
    assert.deepEqual(queries.at(-1), ["*.example.com", "TXT"]);
    await query("sub.*.example.com", "TXT");
    await hasStatus(messages.invalid);
    await query("192.0.2.1", "PTR");
    await hasStatus(messages.empty);
    assert.deepEqual(queries.at(-1), ["1.2.0.192.in-addr.arpa", "PTR"]);
    await query("2001:db8::1", "PTR");
    await hasStatus(messages.empty);
    assert.equal(queries.at(-1)[0], [..."20010db8000000000000000000000001"].reverse().join(".") + ".ip6.arpa");
    reply = { Status: 2 };
    await query(domain);
    await hasStatus(messages.rcode + " SERVFAIL");
    handler = route => route.fulfill({ status: 503, body: "Unavailable" });
    await query(domain);
    await hasStatus(messages.failed);

    let release;
    handler = async route => {
      await new Promise(resolve => { release = resolve; });
      await route.fulfill({ json: { Status: 0, Answer: [record] } }).catch(() => {});
    };
    const first = page.waitForRequest(r => r.url().includes("name=first.example"));
    await query("first.example");
    await first;
    const oldRequest = page.waitForEvent("requestfailed", { predicate: r => r.url().includes("name=first.example") });
    await name.fill("second.example");
    await oldRequest;
    handler = undefined;
    reply = { Status: 3 };
    await form.getByRole("button").click();
    await hasStatus(messages.nxdomain);
    release();
    assert.equal(await answer.count(), 0);

    await page.clock.install();
    handler = route => new Promise(resolve => {
      release = async () => { await route.abort().catch(() => {}); resolve(); };
    });
    const pending = page.waitForRequest(r => r.url().includes("name=timeout.example"));
    await query("timeout.example");
    await pending;
    await page.clock.fastForward(11000);
    await hasStatus(messages.failed);
    await release();
    assert.deepEqual(errors, []);
    console.log("DNS lookup, nine localized pages, search metadata, invalid input, DNS errors, timeout and cancellation passed.");
  } finally {
    await browser.close();
  }
}
run().catch(error => { console.error(error); process.exitCode = 1; });
