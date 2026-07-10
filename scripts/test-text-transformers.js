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

for (const entry of tests) {
  entry.callback();
  console.log(`ok - ${entry.name}`);
}

console.log(`Text transformer tests passed (${tests.length}).`);
