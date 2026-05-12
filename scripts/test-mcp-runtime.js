const assert = require("assert");
const { spawn } = require("child_process");
const { createServer } = require("../server/a2a-server");
const tools = require("../src/_data/tools.json");
const mcpExamples = require("../src/_data/mcpExamples");

const browserOnlyToolIds = new Set([
  "photo2pixel",
  "compress-png",
  "compress-jpeg",
  "progressive-jpeg",
  "exif-viewer",
  "exif-remover"
]);

const toolSamples = {
  "base64-encode": { input: "Hello" },
  "base64-decode": { input: "SGVsbG8=" },
  "md5-generator": { input: "abc" },
  "sha1-generator": { input: "abc" },
  "sha256-generator": { input: "abc" },
  "sha384-generator": { input: "abc" },
  "sha512-generator": { input: "abc" },
  "password-generator": { options: { length: 12, symbols: false } },
  "hex-to-decimal": { input: "FF" },
  "decimal-to-hex": { input: "255" },
  "octal-to-decimal": { input: "10" },
  "decimal-to-octal": { input: "8" },
  "binary-to-decimal": { input: "1010" },
  "decimal-to-binary": { input: "10" },
  "binary-to-hex": { input: "11111111" },
  "hex-to-binary": { input: "FF" },
  "ascii-table": {},
  "hex-to-ascii": { input: "48 69" },
  "ascii-to-hex": { input: "Hi" },
  "binary-to-text": { input: "01001000 01101001" },
  "text-to-binary": { input: "Hi" },
  "fraction-to-decimal": { input: "3/4" },
  "decimal-to-fraction": { input: "0.75" },
  "percent-to-decimal": { input: "25%" },
  "decimal-to-percent": { input: "0.25" },
  "percent-to-fraction": { input: "25%" },
  "fraction-to-percent": { input: "1/4" },
  "hex-to-rgb": { input: "#ff00aa" },
  "rgb-to-hex": { input: { r: 255, g: 0, b: 170 } },
  "hex-to-rgba": { input: "#ff00aa", options: { alpha: 0.5 } },
  "rgba-to-hex": { input: { r: 255, g: 0, b: 170, a: 0.5 } },
  "roman-numerals-chart": {},
  "roman-numerals-to-numbers": { input: "XLII" },
  "numbers-to-roman-numerals": { input: "42" },
  "text-editor": { input: "hello\nworld" },
  "regex-tester": { input: "abc 123 abc", options: { pattern: "abc", flags: "g" } },
  "regex-replace": { input: "abc 123 abc", options: { pattern: "abc", replacement: "xyz", flags: "g" } },
  "url-encode": { input: "hello world & tea=green", options: { mode: "component" } },
  "url-decode": { input: "https://example.com/search?q=hello+world&redirect=https%3A%2F%2Fcoding.tools%2F" },
  "text-compare": { input: "status: draft\nowner: alice", options: { compareTo: "status: published\nowner: alice" } },
  "word-counter": { input: "Hello world." },
  "character-count": { input: "Hi world" },
  "case-converter": { input: "hello world", options: { mode: "title" } },
  "reverse-text": { input: "abc" },
  "number-to-words": { input: "42" },
  "json-formatter": { input: "{\"a\":1}" },
  "json-diff": { input: "{\"user\":{\"name\":\"Alice\",\"role\":\"admin\"}}", options: { compareTo: "{\"user\":{\"name\":\"Alice\",\"role\":\"editor\"}}" } },
  "json-minifier": { input: "{\n  \"a\": 1\n}" },
  "xml-formatter": { input: "<root><a>1</a></root>" },
  "xml-minifier": { input: "<root>\n  <a>1</a>\n</root>" },
  "json-to-xml": { input: "{\"a\":1}", options: { rootName: "root" } },
  "xml-to-json": { input: "<root><a>1</a></root>" },
  "html-beautifier": { input: "<div><span>Hi</span></div>" },
  "html-minifier": { input: "<div>\n  <span>Hi</span>\n</div>" },
  "javascript-beautifier": { input: "function x(){return 1;}" },
  "javascript-minifier": { input: "function x() { return 1; }" },
  "css-beautifier": { input: "body{color:red;}" },
  "css-minifier": { input: "body { color: red; }" },
  "sql-formatter": { input: "select * from users where id = 1" },
  "sql-minifier": { input: "select *\nfrom users\nwhere id = 1" },
  "photo2pixel": { input: "browser-only" },
  "compress-png": { input: "browser-only" },
  "compress-jpeg": { input: "browser-only" },
  "progressive-jpeg": { input: "browser-only" },
  "image-to-base64": { input: "aGVsbG8=", options: { mimeType: "image/png" } },
  "exif-viewer": { input: "browser-only" },
  "exif-remover": { input: "browser-only" }
};

function listen(server) {
  return new Promise((resolve) => {
    server.listen(0, "127.0.0.1", () => {
      const address = server.address();
      resolve(`http://127.0.0.1:${address.port}`);
    });
  });
}

async function rpc(baseUrl, method, params, id = 1, headers = {}) {
  const response = await fetch(`${baseUrl}/mcp`, {
    method: "POST",
    headers: Object.assign({
      "content-type": "application/json",
      "accept": "application/json, text/event-stream",
      "mcp-protocol-version": "2025-06-18"
    }, headers),
    body: JSON.stringify({ jsonrpc: "2.0", id, method, params })
  });
  const text = await response.text();
  return {
    response,
    data: text ? JSON.parse(text) : null
  };
}

function stdioRequest(child, message) {
  return new Promise((resolve, reject) => {
    const timeout = setTimeout(() => reject(new Error("Timed out waiting for MCP stdio response.")), 5000);
    const onData = (chunk) => {
      clearTimeout(timeout);
      child.stdout.off("data", onData);
      resolve(JSON.parse(chunk.toString("utf8")));
    };
    child.stdout.on("data", onData);
    child.stdin.write(`${JSON.stringify(message)}\n`);
  });
}

async function runHttpTests() {
  const server = createServer();
  const baseUrl = await listen(server);
  const toolIds = Object.keys(tools);

  try {
    const init = await rpc(baseUrl, "initialize", {
      protocolVersion: "2025-06-18",
      capabilities: {},
      clientInfo: { name: "coding-tools-test", version: "1.0.0" }
    });
    assert.strictEqual(init.response.status, 200);
    assert.strictEqual(init.data.result.protocolVersion, "2025-06-18");
    assert.ok(init.data.result.capabilities.tools);

    const listed = await rpc(baseUrl, "tools/list", {});
    assert.strictEqual(listed.response.status, 200);
    assert.strictEqual(listed.data.result.tools.length, toolIds.length);
    const listedNames = listed.data.result.tools.map((tool) => tool.name);
    assert.deepStrictEqual(listedNames, toolIds);
    assert.ok(listed.data.result.tools.every((tool) => tool.inputSchema && tool.inputSchema.type === "object"));
    assert.ok(listed.data.result.tools.every((tool) => tool.outputSchema && typeof tool.outputSchema === "object"));
    assert.deepStrictEqual(Object.keys(mcpExamples.arguments), toolIds);
    listed.data.result.tools.forEach((tool) => {
      assert.deepStrictEqual(tool.inputSchema.examples, [mcpExamples.arguments[tool.name]], `${tool.name} should expose the same example shown in docs`);
    });
    const passwordTool = listed.data.result.tools.find((tool) => tool.name === "password-generator");
    assert.ok(passwordTool.inputSchema.properties.options.properties.length);
    assert.ok(passwordTool.inputSchema.properties.options.properties.uppercase);
    assert.ok(passwordTool.inputSchema.properties.options.properties.lowercase);
    assert.ok(passwordTool.inputSchema.properties.options.properties.numbers);
    assert.ok(passwordTool.inputSchema.properties.options.properties.symbols);
    assert.deepStrictEqual(passwordTool.inputSchema.properties.options.properties.length.minimum, 8);
    assert.deepStrictEqual(passwordTool.inputSchema.properties.options.properties.length.maximum, 128);
    assert.deepStrictEqual(passwordTool.inputSchema.examples, [{ options: { length: 20, symbols: true } }]);
    assert.ok(passwordTool.outputSchema.properties.password);
    assert.ok(passwordTool.outputSchema.properties.generated);
    const rgbaTool = listed.data.result.tools.find((tool) => tool.name === "rgba-to-hex");
    assert.ok(rgbaTool.inputSchema.properties.input.oneOf);
    assert.ok(rgbaTool.outputSchema.properties.result);
    const regexTool = listed.data.result.tools.find((tool) => tool.name === "regex-replace");
    assert.deepStrictEqual(regexTool.inputSchema.properties.options.required, ["pattern"]);

    const hash = await rpc(baseUrl, "tools/call", {
      name: "sha256-generator",
      arguments: { input: "abc" }
    }, 2);
    assert.strictEqual(hash.response.status, 200);
    assert.strictEqual(hash.data.result.isError, false);
    assert.strictEqual(hash.data.result.content[0].text, "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
    assert.deepStrictEqual(hash.data.result.structuredContent, {
      result: "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    });

    const replace = await rpc(baseUrl, "tools/call", {
      name: "regex-replace",
      arguments: {
        input: "abc 123 abc",
        options: { pattern: "abc", replacement: "xyz", flags: "g" }
      }
    }, 3);
    assert.strictEqual(replace.data.result.isError, false);
    assert.strictEqual(replace.data.result.content[0].text, "xyz 123 xyz");

    const regexTooManyMatches = await rpc(baseUrl, "tools/call", {
      name: "regex-tester",
      arguments: {
        input: "a".repeat(1001),
        options: { pattern: "a", flags: "g" }
      }
    }, 31);
    assert.strictEqual(regexTooManyMatches.data.result.isError, true);
    assert.ok(regexTooManyMatches.data.result.content[0].text.includes("too many matches"));

    const regexTimeout = await rpc(baseUrl, "tools/call", {
      name: "regex-tester",
      arguments: {
        input: `${"a".repeat(19999)}!`,
        options: { pattern: "(a+)+$", flags: "" }
      }
    }, 32);
    assert.strictEqual(regexTimeout.data.result.isError, true);
    assert.ok(regexTimeout.data.result.content[0].text.includes("timed out"));

    const ascii = await rpc(baseUrl, "tools/call", {
      name: "ascii-table",
      arguments: {}
    }, 4);
    assert.strictEqual(ascii.data.result.isError, false);
    assert.strictEqual(ascii.data.result.structuredContent.length, 128);

    const browserOnly = await rpc(baseUrl, "tools/call", {
      name: "photo2pixel",
      arguments: { input: "unused" }
    }, 5);
    assert.strictEqual(browserOnly.data.result.isError, true);
    assert.ok(browserOnly.data.result.content.some((item) => item.type === "resource_link" && item.uri.endsWith("/photo2pixel.html")));

    assert.deepStrictEqual(Object.keys(toolSamples), toolIds);
    let id = 10;
    for (const toolId of toolIds) {
      const call = await rpc(baseUrl, "tools/call", {
        name: toolId,
        arguments: toolSamples[toolId]
      }, id);
      id += 1;
      assert.strictEqual(call.response.status, 200, `${toolId} MCP call should return HTTP 200`);
      assert.strictEqual(typeof call.data.result.isError, "boolean", `${toolId} should return an MCP tool result`);
      assert.strictEqual(call.data.result.isError, browserOnlyToolIds.has(toolId), `${toolId} isError mismatch`);
      assert.ok(call.data.result.content.length >= 1, `${toolId} should return content`);
      if (!browserOnlyToolIds.has(toolId)) {
        assert.ok(call.data.result.structuredContent !== undefined, `${toolId} should return structuredContent for machine parsing`);
      }
    }

    for (const toolId of toolIds) {
      if (browserOnlyToolIds.has(toolId) || toolId === "image-to-base64") continue;
      const call = await rpc(baseUrl, "tools/call", {
        name: toolId,
        arguments: mcpExamples.arguments[toolId]
      }, id);
      id += 1;
      assert.strictEqual(call.response.status, 200, `${toolId} documented MCP example should return HTTP 200`);
      assert.strictEqual(call.data.result.isError, false, `${toolId} documented MCP example should succeed`);
      assert.ok(call.data.result.structuredContent !== undefined, `${toolId} documented MCP example should include structuredContent`);
    }

    const getResponse = await fetch(`${baseUrl}/mcp`, {
      headers: { accept: "text/event-stream" }
    });
    assert.strictEqual(getResponse.status, 405);

    const badContentType = await fetch(`${baseUrl}/mcp`, {
      method: "POST",
      headers: {
        "content-type": "text/plain",
        "accept": "application/json",
        "mcp-protocol-version": "2025-06-18"
      },
      body: JSON.stringify({ jsonrpc: "2.0", id: 99, method: "tools/list", params: {} })
    });
    assert.strictEqual(badContentType.status, 415);

    const badVersion = await rpc(baseUrl, "tools/list", {}, 6, {
      "mcp-protocol-version": "2020-01-01"
    });
    assert.strictEqual(badVersion.response.status, 400);

    console.log("MCP HTTP runtime tests passed.");
  } finally {
    server.close();
  }
}

async function runStdioTest() {
  const child = spawn(process.execPath, ["server/mcp-stdio.js"], {
    cwd: process.cwd(),
    stdio: ["pipe", "pipe", "pipe"]
  });
  try {
    const response = await stdioRequest(child, {
      jsonrpc: "2.0",
      id: 1,
      method: "tools/call",
      params: {
        name: "base64-encode",
        arguments: { input: "Hello" }
      }
    });
    assert.strictEqual(response.result.isError, false);
    assert.strictEqual(response.result.content[0].text, "SGVsbG8=");
    console.log("MCP stdio runtime test passed.");
  } finally {
    child.kill();
  }
}

async function main() {
  await runHttpTests();
  await runStdioTest();
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
