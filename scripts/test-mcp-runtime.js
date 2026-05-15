const assert = require("assert");
const { spawn } = require("child_process");
const { EventEmitter } = require("events");
const http = require("http");
const https = require("https");
const { PassThrough } = require("stream");
const { createServer } = require("../server/a2a-server");
const { executeMcpTool } = require("../server/mcp-tools");
const tools = require("../src/_data/tools.json");
const mcpExamples = require("../src/_data/mcpExamples");

const browserOnlyToolIds = new Set([
  "photo2pixel",
  "image-resize",
  "image-crop",
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
  "image-resize": { input: "browser-only" },
  "image-crop": { input: "browser-only" },
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
    const jsonDiffTool = listed.data.result.tools.find((tool) => tool.name === "json-diff");
    assert.ok(jsonDiffTool.inputSchema.properties.options.properties.sortKeys);

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

    const jsonKeyOrderDiff = await rpc(baseUrl, "tools/call", {
      name: "json-diff",
      arguments: {
        input: "{\"obj\":{\"b\":2,\"a\":1}}",
        options: {
          compareTo: "{\"obj\":{\"a\":1,\"b\":2}}",
          sortKeys: false
        }
      }
    }, 33);
    assert.strictEqual(jsonKeyOrderDiff.data.result.isError, false);
    assert.ok(jsonKeyOrderDiff.data.result.content[0].text.includes("Changed: 1"));
    assert.ok(jsonKeyOrderDiff.data.result.content[0].text.includes("[changed] $.obj"));

    const jsonSortedKeysDiff = await rpc(baseUrl, "tools/call", {
      name: "json-diff",
      arguments: {
        input: "{\"obj\":{\"b\":2,\"a\":1}}",
        options: {
          compareTo: "{\"obj\":{\"a\":1,\"b\":2}}",
          sortKeys: true
        }
      }
    }, 34);
    assert.strictEqual(jsonSortedKeysDiff.data.result.isError, false);
    assert.ok(jsonSortedKeysDiff.data.result.content[0].text.includes("Changed: 0"));

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

async function runSecurityUnitTests() {
  const dnsPromises = require("dns").promises;
  const originalLookup = dnsPromises.lookup;
  const originalFetch = global.fetch;
  const originalHttpRequest = http.request;
  const originalHttpsRequest = https.request;

  function mockRequest(handler) {
    return (options, callback) => {
      const request = new EventEmitter();
      request.end = () => {
        Promise.resolve()
          .then(() => handler(options))
          .then((mockResponse) => {
            const response = new PassThrough();
            response.statusCode = mockResponse.status || 200;
            response.headers = mockResponse.headers || {};
            callback(response);
            const chunks = mockResponse.chunks || [mockResponse.body || ""];
            chunks.forEach((chunk) => response.write(chunk));
            response.end();
          })
          .catch((error) => request.emit("error", error));
      };
      request.destroy = () => {};
      return request;
    };
  }

  function blockUnexpectedRequest(options) {
    throw new Error(`Network request should not be called for ${options.hostname}${options.path || ""}`);
  }

  async function withNetworkMocks({ lookup, request }, callback) {
    try {
      dnsPromises.lookup = lookup || originalLookup;
      global.fetch = () => {
        throw new Error("image-to-base64 URL fetch must not use global fetch.");
      };
      http.request = request || mockRequest(blockUnexpectedRequest);
      https.request = request || mockRequest(blockUnexpectedRequest);
      await callback();
    } finally {
      dnsPromises.lookup = originalLookup;
      global.fetch = originalFetch;
      http.request = originalHttpRequest;
      https.request = originalHttpsRequest;
    }
  }

  async function expectImageUrlRejected(url, message, lookup, request) {
    await withNetworkMocks({ lookup, request }, async () => {
      try {
        const result = await executeMcpTool("image-to-base64", {
          input: { url }
        });
        assert.fail(`Expected image URL to fail, got ${result.text}`);
      } catch (error) {
        assert.ok(
          error.message.includes(message),
          `Expected "${error.message}" to include "${message}"`
        );
      }
    });
  }

  async function fetchImageUrl(url, lookup, request) {
    let result;
    await withNetworkMocks({ lookup, request }, async () => {
      result = await executeMcpTool("image-to-base64", {
        input: { url }
      });
    });
    return result;
  }

  const privateNetworkMessage = "Private network image URLs are not allowed";
  const blockedUrls = [
    "http://0.0.0.0/image.png",
    "http://100.64.0.1/image.png",
    "http://192.0.2.1/image.png",
    "http://198.18.0.1/image.png",
    "http://203.0.113.1/image.png",
    "http://224.0.0.1/image.png",
    "http://240.0.0.1/image.png",
    "http://[::1]/image.png",
    "http://[fc00::1]/image.png",
    "http://[fe80::1]/image.png",
    "http://[2001:db8::1]/image.png",
    "http://[::ffff:127.0.0.1]/image.png"
  ];

  for (const url of blockedUrls) {
    await expectImageUrlRejected(url, privateNetworkMessage);
  }

  await expectImageUrlRejected(
    "http://public.example/image.png",
    privateNetworkMessage,
    async () => [{ address: "169.254.169.254" }]
  );

  const publicAddress = "93.184.216.34";
  let redirectRequests = 0;
  await expectImageUrlRejected(
    "http://public.example/image.png",
    privateNetworkMessage,
    async () => [{ address: publicAddress }],
    mockRequest(() => {
      redirectRequests += 1;
      return {
        status: 302,
        headers: {
          location: "http://127.0.0.1/private.png"
        }
      };
    })
  );
  assert.strictEqual(redirectRequests, 1);

  let lookupCount = 0;
  const pinnedRequests = [];
  const pinnedResult = await fetchImageUrl(
    "http://rebind.example/image.png",
    async () => {
      lookupCount += 1;
      return [{ address: lookupCount === 1 ? publicAddress : "10.0.0.1" }];
    },
    mockRequest((options) => {
      pinnedRequests.push(options);
      return {
        status: 200,
        headers: {
          "content-type": "image/png"
        },
        body: "abc"
      };
    })
  );
  assert.strictEqual(pinnedResult.text, "data:image/png;base64,YWJj");
  assert.strictEqual(lookupCount, 1);
  assert.strictEqual(pinnedRequests.length, 1);
  assert.strictEqual(pinnedRequests[0].hostname, publicAddress);
  assert.strictEqual(pinnedRequests[0].headers.Host, "rebind.example");
  assert.strictEqual(pinnedRequests[0].path, "/image.png");

  const httpsRequests = [];
  await fetchImageUrl(
    "https://secure.example:8443/image.png?size=1",
    async () => [{ address: publicAddress, family: 4 }],
    mockRequest((options) => {
      httpsRequests.push(options);
      return {
        status: 200,
        headers: {
          "content-type": "image/png"
        },
        body: "abc"
      };
    })
  );
  assert.strictEqual(httpsRequests.length, 1);
  assert.strictEqual(httpsRequests[0].hostname, publicAddress);
  assert.strictEqual(httpsRequests[0].servername, "secure.example");
  assert.strictEqual(httpsRequests[0].headers.Host, "secure.example:8443");
  assert.strictEqual(httpsRequests[0].path, "/image.png?size=1");

  let aborted = false;
  await expectImageUrlRejected(
    "http://large.example/image.png",
    "Image is too large. Maximum size is 5 MB.",
    async () => [{ address: publicAddress }],
    mockRequest((options) => {
      options.signal.addEventListener("abort", () => {
        aborted = true;
      });
      return {
        status: 200,
        headers: {
          "content-type": "image/png"
        },
        chunks: Array.from({ length: 6 }, () => Buffer.alloc(1024 * 1024))
      };
    })
  );
  assert.strictEqual(aborted, true);

  console.log("MCP security unit tests passed.");
}

async function main() {
  await runSecurityUnitTests();
  await runHttpTests();
  await runStdioTest();
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
