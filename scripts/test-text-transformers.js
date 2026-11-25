const assert = require("assert");
const fs = require("fs");
const path = require("path");
const vm = require("vm");

const transforms = require("../src/js/text-transformers");

const tests = [];

test("JSON formatting preserves original tokens and changes only whitespace", () => {
  const input = String.raw`{"id":9007199254740993,"n":1e400,"n":-0,"1":"a , : [ ] \\ \" \u0041","v":[{},[],1.00]}`;
  const formatted = transforms.formatJson(input);
  assert.ok(formatted.includes('  "id": 9007199254740993,'));
  assert.strictEqual(transforms.formatJson(formatted, 0), input);
  for (const scalar of ["1E+20", "true", "null", '" "']) {
    assert.strictEqual(transforms.formatJson(" \t" + scalar + "\r\n"), scalar);
  }
  assert.strictEqual(transforms.formatJson("[[],{}]", 1), "[\n [],\n {}\n]");
});

test("JSON formatting rejects invalid syntax and identifies the location", () => {
  const invalid = [
    ["", 1, 1], ["{\r\n name: 1}", 2, 2], ['{"x":1,\n}', 2, 1],
    ["[1,,2]", 1, 4], ["01", 1, 2], ["true false", 1, 6],
    ['{"x":}', 1, 6], ["null\u00a0", 1, 5], ['"bad\\q"', 1, 1],
    ["{", 1, 2], ["/*x*/1", 1, 1], ['{"x": [1}', 1, 9]
  ];
  for (const [source, line, column] of invalid) {
    assert.throws(() => transforms.formatJson(source), error => error.line === line && error.column === column, source);
  }
});

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

test("JSON conversion and comparison preserve exact numeric values and scalar types", () => {
  const source = '{"n":9007199254740993,"m":1e400,"id":"001","v":-0}';
  assert.equal(transforms.stringifyExactJson(transforms.parseExactJson(source)), source);
  assert.equal(transforms.jsonToXml(source), "<root><n>9007199254740993</n><m>1e400</m><id>001</id><v>-0</v></root>");
  const comparable = text => transforms.stringifyExactJson(transforms.parseExactJson(text), true, true);
  assert.notEqual(comparable("9007199254740992"), comparable("9007199254740993"));
  assert.notEqual(comparable('"1"'), comparable("1"));
  assert.equal(comparable('{"a":[0.0100,0,-2e500]}'), comparable('{"a":[1E-2,-0,-200e498]}'));
  assert.notEqual(comparable('{"__proto__":1}'), comparable("{}"));
});

test("JavaScript transformations preserve restricted newlines and regex after a condition", () => {
  const beautify = require("../src/js/beautify").js_beautify;
  for (const expression of ["[1]", "(1)", "{value:1}", "1"]) {
    const source = "(function () {return\n" + expression + "})()";
    assert.equal(vm.runInNewContext(beautify(source)), vm.runInNewContext(source));
  }
  for (const source of [
    'if ((true)) /[/*]/.test("/");',
    'let x = 2; while (x-- > 1) /[/*]/.test("*"); x;',
    'const o = {if(){return 12}}; o.if() / 3;',
    'if /* before */ (true) /* after */ /[/*]/.test("x");'
  ]) {
    assert.equal(vm.runInNewContext(transforms.minifyJavaScript(source)), vm.runInNewContext(source));
  }
});

test("CSS descendant pseudo-classes and HTML text areas retain their meaning", () => {
  assert.equal(transforms.minifyCss("div :first-child { color: red; }"), "div :first-child{color:red}");
  assert.equal(transforms.minifyCss("div:first-child { color: red; }"), "div:first-child{color:red}");
  assert.equal(transforms.minifyCss("div/*comment*/:first-child {color:red}"), "div/**/:first-child{color:red}");
  const raw = "<TEXTAREA><!--hello--></textarea-extra><!--world--></textarea>";
  assert.equal(transforms.minifyHtml(raw + "<!--remove-->"), raw);
});

test("XML indentation respects mixed text and inherited xml:space", () => {
  const preserved = '<p xml:space="preserve"><a/> <b><c/> <d/></b></p>';
  assert.equal(transforms.formatXml(preserved), preserved);
  assert.equal(transforms.minifyXml(preserved, true), preserved);
  const example = "<root>\n  <name>John</name>\n  <age>30</age>\n</root>";
  const compact = "<root><name>John</name><age>30</age></root>";
  assert.equal(transforms.minifyXml(example, false), example);
  assert.equal(transforms.minifyXml(example, true), compact);
  assert.equal(transforms.formatXml(compact), example);
  assert.equal(transforms.formatXml('<p>Hello <b>world</b>!</p>'), '<p>Hello <b>world</b>!</p>');
  const data = transforms.xmlToJson('<r xml:space="preserve"><a> </a><b xml:space="default"> </b></r>').r;
  assert.equal(data.a, " ");
  assert.deepEqual(data.b, {"@attributes": {"xml:space": "default"}});
  assert.equal(transforms.xmlToJson('<r xml:space="preserve"> </r>').r["#text"], " ");
});

test("SQL string quoting follows the chosen dialect", () => {
  const sql = "SELECT '\\' AS s;";
  assert.equal(transforms.minifySql(sql), sql);
  assert.equal(transforms.minifySql(sql, "sqlite"), sql);
  assert.equal(transforms.minifySql("SELECT 1 /* SQLite stops at the first /* closing delimiter */ + 2", "sqlite"), "SELECT 1 + 2");
  assert.equal(transforms.minifySql("SELECT 'it\\'s' -- keep string\nFROM t", "mysql"), "SELECT 'it\\'s' FROM t");
  assert.equal(transforms.minifySql("SELECT 1--2; # remove", "mysql"), "SELECT 1--2;");
  assert.equal(transforms.minifySql("SELECT /*! STRAIGHT_JOIN */ /*+ HINT */ a FROM t -- remove", "mysql"),
    "SELECT /*! STRAIGHT_JOIN */ /*+ HINT */ a FROM t");
  assert.equal(transforms.minifySql("SELECT 'it''s' -- keep string\nFROM t", "sqlite"), "SELECT 'it''s' FROM t");
});

test("URL decoding preserves query flags and only parses the query portion", () => {
  for (const input of ["https://example.test/a?debug", "https://example.test/a=b", "https://example.test/a?#x"]) {
    assert.equal(transforms.decodeUrl(input, true), input);
  }
  assert.deepEqual(transforms.queryParameters("https://example.test/a=b#?x", true), []);
  assert.deepEqual(transforms.queryParameters("https://example.test/a?debug&x=a+b#end", true), [
    { index: 1, key: "debug", value: "" }, { index: 2, key: "x", value: "a b" }
  ]);
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
