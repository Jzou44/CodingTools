const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs/promises");
const path = require("node:path");
const os = require("node:os");
const vm = require("node:vm");
const { optimizeAssets } = require("./optimize-assets");

test("build assets preserve globals, rewrite localized pages, and invalidate changed content", async () => {
  const directory = await fs.mkdtemp(path.join(os.tmpdir(), "coding-tools-assets-"));
  try {
    await Promise.all(["js", "css", "cn"].map((name) => fs.mkdir(path.join(directory, name))));
    const script = "/*! Example license */\nfunction formatTool(value) { return value.trim(); }\n";
    const html = '<link href="/css/style.css?v=old" rel="stylesheet"><script src="/js/tool.js?v=old"></script><script>window.result = formatTool(" ok ");</script><script src="https://example.com/external.js"></script>';
    await fs.writeFile(path.join(directory, "js/tool.js"), script);
    await fs.writeFile(path.join(directory, "css/style.css"), "/* comment */\nbody { color: red; }\n");
    await fs.writeFile(path.join(directory, "cn/index.html"), html);
    const result = await optimizeAssets(directory);
    assert.equal(result.assets, 2);
    assert.ok(result.after < result.before);
    const manifest = JSON.parse(await fs.readFile(path.join(directory, "asset-manifest.json")));
    const output = await fs.readFile(path.join(directory, "cn/index.html"), "utf8");
    for (const url of Object.values(manifest)) {
      assert.match(url, /\.[a-f0-9]{16}\.(js|css)$/);
      assert.ok(output.includes(url));
      await fs.access(path.join(directory, url));
    }
    assert.ok(output.includes('src="https://example.com/external.js"'));
    const context = { window: {} };
    vm.createContext(context);
    const optimizedJs = await fs.readFile(path.join(directory, manifest["/js/tool.js"]), "utf8");
    assert.ok(optimizedJs.includes("Example license"));
    vm.runInContext(optimizedJs + '; window.result = formatTool(" ok ");', context);
    assert.equal(context.window.result, "ok");
    // Changing a source changes only that asset's URL.
    await fs.writeFile(path.join(directory, "js/tool.js"), script + "var addedGlobal = true;\n");
    await fs.writeFile(path.join(directory, "cn/index.html"), html);
    await optimizeAssets(directory);
    const updated = JSON.parse(await fs.readFile(path.join(directory, "asset-manifest.json")));
    assert.notEqual(updated["/js/tool.js"], manifest["/js/tool.js"]);
    assert.equal(updated["/css/style.css"], manifest["/css/style.css"]);
  } finally {
    await fs.rm(directory, { recursive: true, force: true });
  }
});
