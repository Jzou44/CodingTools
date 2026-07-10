# Semantic-Safe Minifiers and JSON/XML Preservation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the semantics-corrupting minifiers and data-losing JSON/XML converters with one dependency-free implementation shared by browser tools, batch processing, and the MCP runtime.

**Architecture:** Add a UMD module at `src/js/text-transformers.js` containing conservative lexical minifiers plus a small well-formed XML tokenizer/parser and JSON/XML mapping. Keep `html-minifier-compat.js` as a thin adapter for the localized templates, delegate batch and MCP execution to the same module, and prove behavior with direct fixture tests plus integration checks.

**Tech Stack:** Vanilla ES2018 JavaScript, Node.js `assert`/`vm`, Eleventy v3, Nunjucks, existing MCP runtime.

## Global Constraints

- Add no browser bundling pipeline and no server runtime dependency.
- Preserve JavaScript, CSS, SQL, HTML, and XML semantics before optimizing output size.
- Keep all transformations deterministic, side-effect free, and entirely local.
- Emit exactly one XML document element for every supported JSON input.
- Preserve XML qualified-name case, attributes, non-formatting text, repeated siblings, and mixed-content order.
- Reject malformed or unsupported input explicitly; never return a partial conversion.
- Keep all nine localized tool pages working without adding localized metadata frontmatter.
- Do not change translations or visual styling.

---

## File map

- Create `src/js/text-transformers.js`: only source of minification and JSON/XML transformation behavior; exports CommonJS and `window.CodingToolsTextTransforms`.
- Create `scripts/test-text-transformers.js`: direct behavioral fixtures for the shared module and its browser UMD export.
- Modify `package.json`: add `test:transforms` and include it in `npm run check`.
- Modify `src/js/html-minifier-compat.js`: retain legacy `htmlminifier`/`JXON` globals while delegating all work.
- Modify `src/_includes/tool-layout.njk`: load the shared module before the compatibility adapter and batch consumer.
- Modify `src/js/batch-tools.js`: remove independent SQL and JSON/XML transforms and call the shared module.
- Modify `src/tools/{sql-minifier,cn/sql-minifier,tw/sql-minifier,jp/sql-minifier,kr/sql-minifier,fr/sql-minifier,de/sql-minifier,es/sql-minifier,pt/sql-minifier}.njk`: route single-page SQL minification to the shared module.
- Modify `src/tools/{xml-minifier,cn/xml-minifier,tw/xml-minifier,jp/xml-minifier,kr/xml-minifier,fr/xml-minifier,de/xml-minifier,es/xml-minifier,pt/xml-minifier}.njk`: route strict single-page XML minification to the shared module.
- Modify `scripts/check-batch-tools.js`: enforce script ordering and absence of duplicate transformer implementations.
- Modify `server/mcp-tools.js`: remove regex/recursive transformer copies and delegate to the shared module.
- Modify `scripts/test-mcp-runtime.js`: verify MCP parity and structured failures.

---

### Task 1: Shared semantics-safe minifiers

**Files:**
- Create: `src/js/text-transformers.js`
- Create: `scripts/test-text-transformers.js`
- Modify: `package.json:6-10`

**Interfaces:**
- Consumes: string input only.
- Produces: `minifyJavaScript(source: string): string`, `minifyCss(source: string): string`, `minifySql(source: string): string`, `minifyHtml(source: string): string`, and `minifyXml(source: string): string` on both CommonJS exports and `window.CodingToolsTextTransforms`.

- [ ] **Step 1: Add the minifier regression harness before the module exists**

Create `scripts/test-text-transformers.js` with a tiny named-test runner and these exact assertions:

```js
const assert = require("assert");
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const transforms = require("../src/js/text-transformers");

const tests = [];
function test(name, callback) {
  tests.push({ name, callback });
}

test("JavaScript literals and ASI-sensitive newlines survive minification", () => {
  const source = [
    "function value() {",
    "  return",
    "  { text: \"a  b //keep /*keep*/ </script>\" };",
    "}",
    "const regex = /https?:\\/\\/[^/]+\\/\\*keep\\*\\//g;",
    "const template = `left  //keep ${value()}  right`; // remove"
  ].join("\n");
  const output = transforms.minifyJavaScript(source);
  assert.ok(output.includes("\"a  b //keep /*keep*/ </script>\""));
  assert.ok(output.includes("return\n"));
  assert.ok(output.includes("/https?:\\/\\/[^/]+\\/\\*keep\\*\\//g"));
  assert.ok(output.includes("`left  //keep ${value()}  right`"));
  assert.ok(!output.includes("// remove"));
});

test("CSS strings and required value whitespace survive minification", () => {
  const output = transforms.minifyCss('a::before { content: "/*keep*/  //keep"; width: calc(100% - 1px); } /* remove */');
  assert.ok(output.includes('"/*keep*/  //keep"'));
  assert.ok(output.includes("calc(100% - 1px)"));
  assert.ok(!output.includes("/* remove */"));
});

test("SQL quoted regions survive while external comments are removed", () => {
  const source = [
    "select '--keep', \"--identifier\", [/*identifier*/], `--backtick`, $tag$--keep /*keep*/$tag$",
    "from users -- remove",
    "where note = 'a  b /*keep*/'; /* remove */"
  ].join("\n");
  const output = transforms.minifySql(source);
  assert.ok(output.includes("'--keep'"));
  assert.ok(output.includes("\"--identifier\""));
  assert.ok(output.includes("[/*identifier*/]"));
  assert.ok(output.includes("`--backtick`"));
  assert.ok(output.includes("$tag$--keep /*keep*/$tag$"));
  assert.ok(output.includes("'a  b /*keep*/'"));
  assert.ok(!output.includes("-- remove"));
  assert.ok(!output.includes("/* remove */"));
});

test("HTML text, preformatted text, and raw element contents are preserved", () => {
  const source = '<div><span>A</span> <span>B</span><pre> a  b\n c </pre><script>const x = "/*keep*/  //keep";</script><!--remove--></div>';
  const output = transforms.minifyHtml(source);
  assert.ok(output.includes("</span> <span>"));
  assert.ok(output.includes("<pre> a  b\n c </pre>"));
  assert.ok(output.includes('<script>const x = "/*keep*/  //keep";</script>'));
  assert.ok(!output.includes("<!--remove-->"));
});

test("XML text and CDATA whitespace are preserved", () => {
  const source = '<Root note="a  b"><Text> a  b </Text><![CDATA[x  <!--keep-->  y]]><!--remove--></Root>';
  const output = transforms.minifyXml(source);
  assert.ok(output.includes('note="a  b"'));
  assert.ok(output.includes("<Text> a  b </Text>"));
  assert.ok(output.includes("<![CDATA[x  <!--keep-->  y]]>"));
  assert.ok(!output.includes("<!--remove-->"));
});

test("UMD build exposes the same browser API", () => {
  const source = fs.readFileSync(path.join(__dirname, "..", "src", "js", "text-transformers.js"), "utf8");
  const sandbox = { window: {} };
  sandbox.globalThis = sandbox.window;
  vm.runInNewContext(source, sandbox, { filename: "text-transformers.js" });
  assert.strictEqual(typeof sandbox.window.CodingToolsTextTransforms.minifyJavaScript, "function");
  assert.strictEqual(
    sandbox.window.CodingToolsTextTransforms.minifySql("select '--keep' --remove\nfrom t"),
    transforms.minifySql("select '--keep' --remove\nfrom t")
  );
});

for (const entry of tests) {
  entry.callback();
  console.log(`ok - ${entry.name}`);
}
console.log(`Text transformer tests passed (${tests.length}).`);
```

Add the package script but do not add it to `check` until it can pass:

```json
"test:transforms": "node scripts/test-text-transformers.js"
```

- [ ] **Step 2: Run the test and verify the intended red state**

Run: `npm run test:transforms`

Expected: FAIL with `Cannot find module '../src/js/text-transformers'`. This proves the new suite is exercising the missing shared implementation.

- [ ] **Step 3: Implement the UMD shell and scanners**

Create `src/js/text-transformers.js` with this public shell:

```js
(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.CodingToolsTextTransforms = factory();
  }
})(typeof window !== "undefined" ? window : globalThis, function () {
  "use strict";

  function requireString(value, label) {
    if (typeof value !== "string") throw new TypeError((label || "Input") + " must be a string.");
    return value;
  }

  return {
    minifyJavaScript: minifyJavaScript,
    minifyCss: minifyCss,
    minifySql: minifySql,
    minifyHtml: minifyHtml,
    minifyXml: minifyXml
  };
});
```

Implement the scanners with these concrete state rules:

- JavaScript states are `code`, `single`, `double`, `template`, `regex`, `regexClass`, `lineComment`, and `blockComment`. Escapes consume the following character. Template `${` entries push a brace depth and return to `template` at depth zero. `/` opens a regex only after the start of input; one of `(`, `{`, `[`, `=`, `:`, `,`, `;`, `!`, `?`, `&`, `|`, `+`, `-`, `*`, `%`, `~`, `^`, `<`, `>`; or the exact keyword set `return`, `throw`, `case`, `delete`, `void`, `typeof`, `instanceof`, `in`, `of`, `new`, `yield`, and `await`. Line comments retain their terminating line break. Block comments containing a line break emit one line break; other removed comments emit a space when both neighboring characters could form one token. Unterminated protected states throw `SyntaxError`.
- JavaScript whitespace is normalized only in `code`: horizontal runs become one space, blank line runs become one newline, and newlines are never removed. Literal bytes are copied unchanged.
- CSS states are `code`, `single`, `double`, and `comment`. Removed comments emit a separator when surrounded by name characters. Outside strings, whitespace becomes one space; remove it around `{`, `}`, `:`, `;`, and `,` only. Preserve whitespace around `+` and `-` so `calc(100% - 1px)` stays valid. Unterminated strings/comments throw.
- SQL states are `code`, `single`, `double`, `backtick`, `bracket`, `dollar`, `lineComment`, and `blockComment`. Doubled quote/bracket closers and backslash escapes stay in their protected region. A dollar opener matches `\$[A-Za-z_][A-Za-z0-9_]*\$|\$\$` and closes only on the same delimiter. Outside protected regions, comments become a pending separator and all whitespace becomes one space. Unterminated regions throw.
- Markup scanning copies ordinary text, quoted attribute values, CDATA, processing instructions, declarations, and raw `script`/`style` blocks byte-for-byte. It removes complete ordinary comments and collapses whitespace inside an opening/closing tag only when outside quotes. XML mode maintains an exact-case element-name stack, rejects crossing/missing close tags, and rejects multiple roots. HTML mode does not apply XML nesting rules. Unterminated tags, comments, CDATA, declarations, or quotes throw.

Keep the implementation conservative: if a whitespace removal is not covered by a rule above, copy it as one equivalent whitespace character.

- [ ] **Step 4: Run the minifier suite until green**

Run: `npm run test:transforms`

Expected: six `ok -` lines followed by `Text transformer tests passed (6).`

- [ ] **Step 5: Make the suite a repository gate and run it again**

Change `package.json` to:

```json
"check": "npm run check:site && npm run check:batch && npm run test:transforms && npm run skills:check"
```

Run: `npm run test:transforms`

Expected: PASS with no warnings.

- [ ] **Step 6: Commit the shared minifier slice**

```bash
git add package.json scripts/test-text-transformers.js src/js/text-transformers.js
git commit -m "Fix semantics-safe text minification"
```

---

### Task 2: Structure-preserving JSON/XML conversion

**Files:**
- Modify: `src/js/text-transformers.js`
- Modify: `scripts/test-text-transformers.js`

**Interfaces:**
- Consumes: `jsonToXml(sourceOrValue, { rootName?: string, maxDepth?: number })` and `xmlToJson(source, { maxDepth?: number })`.
- Produces: one XML string from `jsonToXml`; one plain JavaScript object keyed by the exact root qualified name from `xmlToJson`.

- [ ] **Step 1: Append failing conversion fixtures**

Insert these tests before the runner loop in `scripts/test-text-transformers.js`:

```js
test("JSON objects and arrays always produce one complete XML root", () => {
  assert.strictEqual(transforms.jsonToXml('{"person":{"name":"Ada"}}'), "<person><name>Ada</name></person>");
  assert.strictEqual(transforms.jsonToXml('{"a":1,"b":2}'), "<root><a>1</a><b>2</b></root>");
  assert.strictEqual(transforms.jsonToXml('[1,2,3]'), "<root><item>1</item><item>2</item><item>3</item></root>");
  assert.strictEqual(
    transforms.jsonToXml('[1,2]', { rootName: "Rows" }),
    "<Rows><item>1</item><item>2</item></Rows>"
  );
});

test("XML conversion preserves case, attributes, entities, and repeated children", () => {
  const result = transforms.xmlToJson('<Root ID="7"><Item>A &amp; B</Item><Item><![CDATA[C < D]]></Item></Root>');
  assert.deepStrictEqual(result, {
    Root: {
      "@attributes": { ID: "7" },
      Item: ["A & B", "C < D"]
    }
  });
});

test("mixed XML content preserves source order", () => {
  const result = transforms.xmlToJson('<p class="lead">Hello <b>world</b>!</p>');
  assert.deepStrictEqual(result, {
    p: {
      "@attributes": { class: "lead" },
      "#content": ["Hello ", { b: "world" }, "!"]
    }
  });
  assert.strictEqual(transforms.jsonToXml(result), '<p class="lead">Hello <b>world</b>!</p>');
});

test("invalid JSON/XML structures fail instead of being rewritten", () => {
  assert.throws(() => transforms.jsonToXml('{"bad key":1}'), /Invalid XML name/);
  assert.throws(() => transforms.xmlToJson("<Root><A></Root>"), /Expected <\/A>/);
  assert.throws(() => transforms.xmlToJson("<A/><B/>"), /one root element/);
  assert.throws(() => transforms.xmlToJson('<!DOCTYPE x [<!ENTITY custom "value">]><x>&custom;</x>'), /DOCTYPE/);
  assert.throws(() => transforms.xmlToJson("<x>&unknown;</x>"), /Unknown XML entity/);
});
```

- [ ] **Step 2: Run the focused suite and verify red**

Run: `npm run test:transforms`

Expected: the six minifier tests pass, then FAIL because `transforms.jsonToXml is not a function`.

- [ ] **Step 3: Implement exact XML name/entity helpers**

Add these rules to `src/js/text-transformers.js`:

```js
var XML_NAME = /^[:_\p{L}][:_\p{L}\p{N}.\-\u00B7\u0300-\u036F\u203F-\u2040]*$/u;
var XML_ENTITIES = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'" };

function assertXmlName(name) {
  var value = String(name);
  if (!XML_NAME.test(value)) {
    throw new SyntaxError('Invalid XML name: "' + value + '".');
  }
  return value;
}

function escapeXmlText(value) {
  return String(value).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function escapeXmlAttribute(value) {
  return escapeXmlText(value).replace(/"/g, "&quot;").replace(/'/g, "&apos;");
}
```

Decode named entities from `XML_ENTITIES`, decimal numeric entities, and hexadecimal numeric entities. Reject invalid Unicode scalar values and every unknown named entity.

- [ ] **Step 4: Implement the XML tokenizer and tree builder**

Use plain nodes with the following exact shapes:

```js
{ type: "element", name: "Root", attributes: [{ name: "ID", value: "7" }], children: [] }
{ type: "text", value: "Hello " }
{ type: "cdata", value: "C < D" }
```

The tokenizer must:

1. Skip one optional XML declaration.
2. Reject every `<!DOCTYPE` construct with `SyntaxError("DOCTYPE is not supported.")`.
3. Skip comments but preserve separators through their surrounding text nodes.
4. Parse exact-case qualified names and quoted attributes; duplicate attribute names are errors.
5. Convert entity references in text and attributes exactly once.
6. Treat CDATA as text data without entity decoding.
7. Maintain a stack and throw `SyntaxError('Expected </' + openName + '> before </' + closeName + '>.')` on mismatches.
8. Require exactly one document element and reject non-whitespace text outside it.
9. Enforce `maxDepth`, defaulting to `100`.

- [ ] **Step 5: Implement XML-node to JSON mapping**

Use these exact mapping decisions:

```js
function elementToJson(element) {
  var attributes = attributesToObject(element.attributes);
  var significant = element.children.filter(function (child) {
    return child.type === "element" || child.value.trim() !== "";
  });
  var hasElements = significant.some(function (child) { return child.type === "element"; });
  var hasText = significant.some(function (child) { return child.type !== "element"; });

  if (!element.attributes.length && !hasElements) {
    return significant.map(function (child) { return child.value; }).join("");
  }

  var result = {};
  if (element.attributes.length) result["@attributes"] = attributes;
  if (hasElements && hasText) {
    result["#content"] = significant.map(function (child) {
      if (child.type !== "element") return child.value;
      var entry = {};
      entry[child.name] = elementToJson(child);
      return entry;
    });
    return result;
  }

  if (hasText) result["#text"] = significant.map(function (child) { return child.value; }).join("");
  significant.filter(function (child) { return child.type === "element"; }).forEach(function (child) {
    var value = elementToJson(child);
    if (Object.prototype.hasOwnProperty.call(result, child.name)) {
      if (!Array.isArray(result[child.name])) result[child.name] = [result[child.name]];
      result[child.name].push(value);
    } else {
      result[child.name] = value;
    }
  });
  return result;
}
```

Return `{ [root.name]: elementToJson(root) }` from `xmlToJson`.

- [ ] **Step 6: Implement JSON to one-root XML serialization**

Select the root with this exact logic:

```js
function jsonToXml(sourceOrValue, options) {
  var value = typeof sourceOrValue === "string" ? JSON.parse(sourceOrValue) : sourceOrValue;
  var settings = options || {};
  if (settings.rootName) return serializeElement(assertXmlName(settings.rootName), value, 0, settings);
  if (isPlainObject(value)) {
    var keys = Object.keys(value);
    if (keys.length === 1 && XML_NAME.test(keys[0])) {
      return serializeElement(assertXmlName(keys[0]), value[keys[0]], 0, settings);
    }
  }
  return serializeElement("root", value, 0, settings);
}
```

`serializeElement(name, value, depth, settings)` must:

- Emit array entries inside the current root as `<item>` children instead of repeating the root.
- Repeat a property tag for nested property arrays.
- Read `@attributes`, `#text`, and `#content` as reserved mapping keys.
- Require each `#content` element entry to be a plain single-key object.
- Escape values once and emit null/empty values as `<name></name>` consistently with the expected fixtures.
- Validate every emitted name and enforce `maxDepth`, defaulting to `100`.

Expose `jsonToXml` and `xmlToJson` in the returned API object.

- [ ] **Step 7: Run the suite until all conversion fixtures are green**

Run: `npm run test:transforms`

Expected: ten `ok -` lines followed by `Text transformer tests passed (10).`

- [ ] **Step 8: Commit the conversion slice**

```bash
git add scripts/test-text-transformers.js src/js/text-transformers.js
git commit -m "Preserve JSON and XML structure"
```

---

### Task 3: Browser compatibility and batch parity

**Files:**
- Modify: `src/js/html-minifier-compat.js`
- Modify: `src/_includes/tool-layout.njk:394-463`
- Modify: `src/js/batch-tools.js:255-315,626-674`
- Modify: `src/tools/sql-minifier.njk:62-130`
- Modify: `src/tools/cn/sql-minifier.njk:89-157`
- Modify: `src/tools/tw/sql-minifier.njk`
- Modify: `src/tools/jp/sql-minifier.njk`
- Modify: `src/tools/kr/sql-minifier.njk`
- Modify: `src/tools/fr/sql-minifier.njk`
- Modify: `src/tools/de/sql-minifier.njk`
- Modify: `src/tools/es/sql-minifier.njk`
- Modify: `src/tools/pt/sql-minifier.njk`
- Modify: `src/tools/xml-minifier.njk`
- Modify: `src/tools/cn/xml-minifier.njk`
- Modify: `src/tools/tw/xml-minifier.njk`
- Modify: `src/tools/jp/xml-minifier.njk`
- Modify: `src/tools/kr/xml-minifier.njk`
- Modify: `src/tools/fr/xml-minifier.njk`
- Modify: `src/tools/de/xml-minifier.njk`
- Modify: `src/tools/es/xml-minifier.njk`
- Modify: `src/tools/pt/xml-minifier.njk`
- Modify: `scripts/test-text-transformers.js`
- Modify: `scripts/check-batch-tools.js`

**Interfaces:**
- Consumes: `window.CodingToolsTextTransforms` from Tasks 1–2.
- Produces: legacy `window.htmlminifier.minify`, legacy `window.JXON`, and identical single/batch outputs without independent transformation algorithms.

- [ ] **Step 1: Add browser-adapter tests before changing the adapter**

Append this fixture before the runner loop in `scripts/test-text-transformers.js`:

```js
test("browser compatibility globals delegate without wrapper truncation", () => {
  const sharedSource = fs.readFileSync(path.join(__dirname, "..", "src", "js", "text-transformers.js"), "utf8");
  const compatSource = fs.readFileSync(path.join(__dirname, "..", "src", "js", "html-minifier-compat.js"), "utf8");
  const sandbox = { window: {} };
  sandbox.globalThis = sandbox.window;
  vm.runInNewContext(sharedSource, sandbox, { filename: "text-transformers.js" });
  vm.runInNewContext(compatSource, sandbox, { filename: "html-minifier-compat.js" });

  const wrappedJs = '<script>const text = "</script>  //keep"; //remove\n</script>';
  const minifiedJs = sandbox.window.htmlminifier.minify(wrappedJs, { minifyJS: true, removeComments: true });
  assert.ok(minifiedJs.includes('"</script>  //keep"'));

  const wrappedArray = sandbox.window.JXON.jsToXml({ RootDirectory: [1, 2] });
  const unwrappedArray = wrappedArray.replace(/<RootDirectory>/, "").replace(/<\/RootDirectory>[\s\S]*$/, "");
  assert.strictEqual(unwrappedArray, "<root><item>1</item><item>2</item></root>");

  const wrappedXml = sandbox.window.JXON.stringToXml('<RootDirectory><Actual ID="7"><Child>x</Child></Actual></RootDirectory>');
  assert.deepStrictEqual(
    JSON.parse(JSON.stringify(sandbox.window.JXON.xmlToJs(wrappedXml).rootdirectory)),
    { Actual: { "@attributes": { ID: "7" }, Child: "x" } }
  );
});
```

- [ ] **Step 2: Run the suite and verify the adapter test fails**

Run: `npm run test:transforms`

Expected: earlier tests pass; the new adapter test fails because the existing adapter lowercases names or truncates the wrapped array.

- [ ] **Step 3: Replace compatibility logic with delegation**

Rewrite `src/js/html-minifier-compat.js` as a thin IIFE. Require `window.CodingToolsTextTransforms`, then implement:

```js
function minify(source, options) {
  var text = String(source == null ? "" : source);
  var opts = options || {};
  if (opts.minifyJS && /^<script>/i.test(text) && /<\/script>$/i.test(text)) {
    return text.slice(0, text.indexOf(">") + 1) +
      transforms.minifyJavaScript(text.slice(text.indexOf(">") + 1, text.toLowerCase().lastIndexOf("</script>"))) +
      text.slice(text.toLowerCase().lastIndexOf("</script>"));
  }
  if (opts.minifyCSS && /^<style>/i.test(text) && /<\/style>$/i.test(text)) {
    return text.slice(0, text.indexOf(">") + 1) +
      transforms.minifyCss(text.slice(text.indexOf(">") + 1, text.toLowerCase().lastIndexOf("</style>"))) +
      text.slice(text.toLowerCase().lastIndexOf("</style>"));
  }
  return transforms.minifyHtml(text);
}
```

For `JXON`:

- `stringToXml(source)` returns `{ __codingToolsXmlSource: String(source) }`; it validates immediately by calling `xmlToJson`.
- `xmlToJs(document)` calls `xmlToJson(document.__codingToolsXmlSource)`. If the sole exact root is `RootDirectory`, return `{ rootdirectory: rootValue }` so existing localized templates continue to unwrap it without lowercasing actual names.
- `jsToXml(value)` special-cases `{ RootDirectory: payload }` as `<RootDirectory>` + `jsonToXml(payload)` + `</RootDirectory>`; other values use `jsonToXml(value)`.
- `jsToString` aliases `jsToXml`, and `xmlToString` returns strings unchanged or the stored source.

Do not retain regex minifiers, name-lowercasing, or tag-name rewriting in this file.

- [ ] **Step 4: Load the shared module before all browser consumers**

In `src/_includes/tool-layout.njk`, add `sql-minifier` to a transformer set and render scripts in this order:

```njk
{% set textTransformerTools = [
  "css-minifier",
  "html-minifier",
  "javascript-minifier",
  "json-to-xml",
  "sql-minifier",
  "xml-formatter",
  "xml-minifier",
  "xml-to-json"
] %}
{% if currentTool in textTransformerTools %}
<script src="/js/text-transformers.js?v={{ site.assetVersion }}"></script>
{% endif %}
{% if currentTool in htmlCompatTools %}
<script src="/js/html-minifier-compat.js?v={{ site.assetVersion }}"></script>
{% endif %}
```

The existing `tool_script` block and `batch-tools.js` tags remain after both scripts.

- [ ] **Step 5: Delegate batch transformations**

Delete the local `minifySql`, `jsonToXmlBatch`, and `xmlToJsonBatch` functions from `src/js/batch-tools.js`. Add one checked accessor:

```js
function textTransforms() {
  if (!window.CodingToolsTextTransforms) throw new Error(tr("invalidInput", "Invalid input"));
  return window.CodingToolsTextTransforms;
}
```

Use these exact branches in `transformText`:

```js
if (tool === "json-to-xml") return Promise.resolve(vkbeautify.xml(textTransforms().jsonToXml(value)));
if (tool === "xml-minifier") return Promise.resolve(textTransforms().minifyXml(value));
if (tool === "xml-to-json") return Promise.resolve(JSON.stringify(textTransforms().xmlToJson(value), null, 2));
if (tool === "html-minifier") return Promise.resolve(textTransforms().minifyHtml(value));
if (tool === "javascript-minifier") return Promise.resolve(textTransforms().minifyJavaScript(value));
if (tool === "css-minifier") return Promise.resolve(textTransforms().minifyCss(value));
if (tool === "sql-minifier") return Promise.resolve(textTransforms().minifySql(value));
```

For `xml-formatter`, pass the original `value` directly to `vkbeautify.xml`; do not use any minifier as a formatter pre-pass.

- [ ] **Step 6: Delegate all localized SQL and XML-minifier single pages**

In each of the nine SQL minifier templates, delete the local `minifySql` function and change the click handler to:

```js
var result = CodingToolsTextTransforms.minifySql(text);
outputEditor.value = result;
```

Preserve every localized status string and all existing editor wiring.

In each of the nine XML minifier templates, replace only the transformation expression in the click handler:

```js
outputEditor.value = CodingToolsTextTransforms.minifyXml(text);
```

Do not route XML minification through the HTML compatibility entry point, because strict nesting and single-root validation are part of the XML contract.

- [ ] **Step 7: Strengthen static wiring checks**

In `scripts/check-batch-tools.js`, read `src/js/html-minifier-compat.js`, every SQL minifier template, and the layout. Add assertions that:

```js
if (!layout.includes('/js/text-transformers.js?v={{ site.assetVersion }}')) {
  fail("tool-layout.njk does not load the shared text transformer");
}
if (layout.indexOf("/js/text-transformers.js") > layout.indexOf("/js/html-minifier-compat.js")) {
  fail("text-transformers.js must load before html-minifier-compat.js");
}
if (!batchScript.includes("CodingToolsTextTransforms")) {
  fail("batch-tools.js does not delegate to CodingToolsTextTransforms");
}
if (/function\s+(minifySql|jsonToXmlBatch|xmlToJsonBatch)\s*\(/.test(batchScript)) {
  fail("batch-tools.js still contains a duplicate text transformer");
}
```

For every `src/tools/**/sql-minifier.njk`, fail if it contains `function minifySql(` or lacks `CodingToolsTextTransforms.minifySql(text)`. For every `src/tools/**/xml-minifier.njk`, fail if it lacks `CodingToolsTextTransforms.minifyXml(text)`.

- [ ] **Step 8: Run browser-core and wiring tests**

Run: `npm run test:transforms && npm run check:batch`

Expected: eleven transformer tests pass and batch checks report the current enabled-tool count with no errors.

- [ ] **Step 9: Commit browser and batch integration**

```bash
git add src/js/html-minifier-compat.js src/js/batch-tools.js src/_includes/tool-layout.njk src/tools scripts/test-text-transformers.js scripts/check-batch-tools.js
git commit -m "Share safe transforms across browser tools"
```

---

### Task 4: MCP runtime parity

**Files:**
- Modify: `server/mcp-tools.js:1-35,1253-1397,1755-1779`
- Modify: `scripts/test-mcp-runtime.js`

**Interfaces:**
- Consumes: CommonJS `require("../src/js/text-transformers")`.
- Produces: unchanged MCP `{ text, data }` result shapes and `McpToolError` for shared validation failures.

- [ ] **Step 1: Add direct MCP regression tests before delegation**

Add this function above `main()` in `scripts/test-mcp-runtime.js` and call it before the network tests:

```js
async function runTextTransformerRegressionTests() {
  const js = await executeMcpTool("javascript-minifier", {
    input: 'const text = "a  b //keep /*keep*/"; //remove\ntext;'
  });
  assert.ok(js.text.includes('"a  b //keep /*keep*/"'));
  assert.ok(!js.text.includes("//remove"));

  const css = await executeMcpTool("css-minifier", {
    input: 'a::before { content: "/*keep*/"; width: calc(100% - 1px); }'
  });
  assert.ok(css.text.includes('"/*keep*/"'));
  assert.ok(css.text.includes("calc(100% - 1px)"));

  const sql = await executeMcpTool("sql-minifier", {
    input: "select '--keep', [/*keep*/], $$--keep$$ --remove\nfrom t"
  });
  assert.ok(sql.text.includes("'--keep'"));
  assert.ok(sql.text.includes("[/*keep*/]"));
  assert.ok(sql.text.includes("$$--keep$$"));
  assert.ok(!sql.text.includes("--remove"));

  const markup = await executeMcpTool("html-minifier", {
    input: "<span>A</span> <span>B</span><pre> a  b </pre>"
  });
  assert.ok(markup.text.includes("</span> <span>"));
  assert.ok(markup.text.includes("<pre> a  b </pre>"));

  const arrayXml = await executeMcpTool("json-to-xml", {
    input: "[1,2]",
    options: { rootName: "Rows" }
  });
  assert.strictEqual(arrayXml.text, "<Rows><item>1</item><item>2</item></Rows>");

  const parsed = await executeMcpTool("xml-to-json", {
    input: '<Root ID="7"><Item>A</Item><Item>B</Item></Root>'
  });
  assert.deepStrictEqual(parsed.data, {
    Root: { "@attributes": { ID: "7" }, Item: ["A", "B"] }
  });

  console.log("MCP text transformer regression tests passed.");
}
```

Add a `callMcpTool` assertion for malformed XML so the public MCP response remains structured:

```js
const invalidXml = await callMcpTool("xml-to-json", { input: "<Root><A></Root>" });
assert.strictEqual(invalidXml.isError, true);
assert.ok(invalidXml.content[0].text.includes("Expected </A>"));
```

Import `callMcpTool` alongside `executeMcpTool` at the top of the file.

- [ ] **Step 2: Run MCP tests and verify the reported failures**

Run: `npm run mcp:test`

Expected: FAIL in the new JavaScript literal, CSS literal, SQL quoted-comment, XML attribute, or top-level-array assertions against the current regex implementations.

- [ ] **Step 3: Delegate the MCP implementation**

At the top of `server/mcp-tools.js`, add:

```js
const textTransforms = require("../src/js/text-transformers");
```

Replace the old `minifyMarkup`, `minifyCss`, `minifyJavaScript`, `minifySql`, `jsonToXml`, `xmlNode`, `escapeXml`, `xmlToJson`, and `xmlChildren` implementation block with:

```js
function sharedTransform(callback) {
  try {
    return callback();
  } catch (error) {
    throw new McpToolError(error.message);
  }
}

function jsonToXml(input, options) {
  return sharedTransform(() => textTransforms.jsonToXml(input, {
    rootName: options.rootName,
    maxDepth: MAX_JSON_TO_XML_DEPTH
  }));
}

function xmlToJson(input) {
  const data = sharedTransform(() => textTransforms.xmlToJson(requireText(input)));
  return { text: JSON.stringify(data, null, 2), data };
}
```

Update switch branches to call `sharedTransform` around the five minifier functions:

```js
case "xml-minifier":
  return { text: sharedTransform(() => textTransforms.minifyXml(requireText(input))) };
case "html-minifier":
  return { text: sharedTransform(() => textTransforms.minifyHtml(requireText(input))) };
case "javascript-minifier":
  return { text: sharedTransform(() => textTransforms.minifyJavaScript(requireText(input))) };
case "css-minifier":
  return { text: sharedTransform(() => textTransforms.minifyCss(requireText(input))) };
case "sql-minifier":
  return { text: sharedTransform(() => textTransforms.minifySql(requireText(input))) };
```

Keep existing formatters unchanged. Remove no unrelated MCP code.

- [ ] **Step 4: Run direct and transport-level MCP tests until green**

Run: `npm run test:transforms && npm run mcp:test`

Expected: the direct transformer suite passes; MCP output includes `MCP text transformer regression tests passed.`, `MCP HTTP runtime tests passed.`, and `MCP stdio runtime test passed.`

- [ ] **Step 5: Commit MCP integration**

```bash
git add server/mcp-tools.js scripts/test-mcp-runtime.js
git commit -m "Align MCP text transformations"
```

---

### Task 5: Full build and rendered-browser verification

**Files:**
- Inspect: `dist/js/text-transformers.js`
- Inspect: representative generated pages in `dist/`
- Modify only if a verification failure identifies an in-scope defect.

**Interfaces:**
- Consumes: completed Tasks 1–4.
- Produces: verified static output and requirement-by-requirement evidence.

- [ ] **Step 1: Run all repository gates from a clean command invocation**

Run:

```bash
npm run test:transforms
npm run mcp:test
npm run check
npm run build
```

Expected: every command exits `0`; build creates `dist/js/text-transformers.js` and all language pages.

- [ ] **Step 2: Inspect generated script ordering and stale implementations**

Run:

```powershell
rg -n "text-transformers|html-minifier-compat|batch-tools" dist/javascript-minifier.html dist/cn/javascript-minifier.html dist/sql-minifier.html
rg -n "RootDirectory.*replace|function minifySql|replace\(/\\/\\\*\[\\s\\S\]" src/js src/tools server/mcp-tools.js
```

Expected: the shared script precedes compatibility and batch scripts; no active duplicate minifier or root-stripping implementation remains in the modified paths.

- [ ] **Step 3: Verify representative browser interactions**

Start the repository dev server with the custom debug workflow and verify these pages in the local browser:

- `/javascript-minifier.html`: input `const x = "a  b //keep /*keep*/ </script>"; //remove` retains the full string and removes only the final comment.
- `/cn/css-minifier.html`: input `a::before { content: "/*keep*/"; width: calc(100% - 1px); }` retains the string and required calculation spacing.
- `/sql-minifier.html`: quoted `--`, block markers, bracket identifiers, and dollar strings remain intact.
- `/json-to-xml.html`: `[1,2]` produces one `<root>` containing two `<item>` elements.
- `/xml-to-json.html`: `<Root ID="7"><Item>A</Item><Item>B</Item></Root>` retains `Root`, `ID`, and the two-item array.
- `/xml-minifier.html`: `<Root><Text> a  b </Text></Root>` retains the text spaces.

Expected: output matches direct tests and the browser console has no errors.

- [ ] **Step 4: Audit every acceptance criterion**

Record evidence in the final handoff:

- Literal/comment-marker preservation: direct transformer test names and browser cases.
- HTML/XML text preservation: direct tests and rendered page cases.
- Browser/batch/MCP parity: shared-module wiring check plus MCP regression output.
- One-root JSON/XML conversion: direct and MCP array assertions.
- XML attributes/case/repeated children: direct and MCP parsed-object assertions.
- Repository health: exact exit results of `test:transforms`, `mcp:test`, `check`, and `build`.

- [ ] **Step 5: Commit only if verification required a correction**

If an in-scope correction was necessary, stage only its files and commit:

```bash
git add -- package.json src/js/text-transformers.js src/js/html-minifier-compat.js src/js/batch-tools.js src/_includes/tool-layout.njk src/tools server/mcp-tools.js scripts/test-text-transformers.js scripts/check-batch-tools.js scripts/test-mcp-runtime.js
git commit -m "Fix transformer verification regression"
```

If no correction was necessary, do not create an empty commit.
