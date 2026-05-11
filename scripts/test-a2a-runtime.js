const assert = require("assert");
const { createServer } = require("../server/a2a-server");
const { executeTool, supportedToolIds, ToolInputError } = require("../server/a2a-tools");

function assertTool(toolId, input, expectedText, options) {
  const result = executeTool(toolId, input, options || {});
  assert.strictEqual(result.text, expectedText, `${toolId} output mismatch`);
}

function assertToolData(toolId, input, expectedData, options) {
  const result = executeTool(toolId, input, options || {});
  assert.deepStrictEqual(result.data, expectedData, `${toolId} data mismatch`);
}

function assertToolFails(toolId, input, options) {
  assert.throws(() => executeTool(toolId, input, options || {}), ToolInputError, `${toolId} should reject invalid input`);
}

function runToolUnitTests() {
  assertTool("base64-encode", "Hello", "SGVsbG8=");
  assertTool("base64-decode", "SGVsbG8=", "Hello");
  assertTool("md5-generator", "abc", "900150983cd24fb0d6963f7d28e17f72");
  assertTool("sha1-generator", "abc", "a9993e364706816aba3e25717850c26c9cd0d89d");
  assertTool("sha256-generator", "abc", "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");
  assertTool("sha384-generator", "abc", "cb00753f45a35e8bb5a03d699ac65007272c32ab0eded1631a8b605a43ff5bed8086072ba1e7cc2358baeca134c825a7");
  assertTool("sha512-generator", "abc", "ddaf35a193617abacc417349ae20413112e6fa4e89a97ea20a9eeee64b55d39a2192992a274fc1a836ba3c23a3feebbd454d4423643ce80e2a9ac94fa54ca49f");
  assert.strictEqual(executeTool("password-generator", "", { length: 12, symbols: false }).text.length, 12);

  assertTool("hex-to-decimal", "0xFF", "255");
  assertTool("decimal-to-hex", "255", "FF");
  assertTool("octal-to-decimal", "10", "8");
  assertTool("decimal-to-octal", "8", "10");
  assertTool("binary-to-decimal", "1010", "10");
  assertTool("decimal-to-binary", "10", "1010");
  assertTool("binary-to-hex", "11111111", "FF");
  assertTool("hex-to-binary", "FF", "11111111");

  assertTool("ascii-to-hex", "Hi", "48 69");
  assertTool("ascii-to-hex", "", "");
  assertTool("hex-to-ascii", "48 69", "Hi");
  assertTool("binary-to-text", "01001000 01101001", "Hi");
  assertTool("text-to-binary", "Hi", "01001000 01101001");

  assertTool("fraction-to-decimal", "3/4", "0.75");
  assertTool("decimal-to-fraction", "0.75", "3/4");
  assertTool("percent-to-decimal", "25%", "0.25");
  assertTool("decimal-to-percent", "0.25", "25%");
  assertTool("percent-to-fraction", "25%", "1/4");
  assertTool("fraction-to-percent", "1/4", "25%");

  assertToolData("hex-to-rgb", "#ff00aa", { r: 255, g: 0, b: 170 });
  assertToolData("hex-to-rgba", "#ff00aa", { r: 255, g: 0, b: 170, a: 0.5 }, { alpha: 0.5 });
  assertTool("rgb-to-hex", "rgb(255, 0, 170)", "#FF00AA");
  assertTool("rgba-to-hex", "rgba(255, 0, 170, 0.5)", "#FF00AA80");

  assertTool("roman-numerals-to-numbers", "XLII", "42");
  assertTool("numbers-to-roman-numerals", "42", "XLII");
  assertTool("json-formatter", "{\"a\":1}", "{\n  \"a\": 1\n}");
  assertTool("json-minifier", "{\n  \"a\": 1\n}", "{\"a\":1}");
  assertTool("reverse-text", "abc", "cba");
  assertToolData("case-converter", "hello world", { mode: "title", result: "Hello World" }, { mode: "title" });
  assertToolData("word-counter", "Hello world.\n\nAgain.", {
    words: 3,
    characters: 20,
    charactersNoSpaces: 17,
    lines: 3,
    sentences: 2,
    paragraphs: 2
  });
  assertToolData("character-count", "Hi 世界", {
    characters: 5,
    charactersNoSpaces: 4,
    bytesUtf8: 9,
    words: 2,
    lines: 1
  });

  assertToolFails("json-formatter", "{bad json");
  assertToolFails("base64-decode", "not base64");
  assertToolFails("roman-numerals-to-numbers", "IIII");
  assertToolFails("base64-encode", "a".repeat(200001));
  assertToolFails("decimal-to-hex", "1".repeat(4097));
  assert.strictEqual(supportedToolIds.length, 38);
}

function listen(server) {
  return new Promise((resolve) => {
    server.listen(0, "127.0.0.1", () => {
      const address = server.address();
      resolve(`http://127.0.0.1:${address.port}`);
    });
  });
}

async function postJson(url, body) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "a2a-version": "1.0"
    },
    body: JSON.stringify(body)
  });
  const data = await response.json();
  return { response, data };
}

async function postJsonWithHeaders(url, body, headers) {
  const response = await fetch(url, {
    method: "POST",
    headers: Object.assign({ "content-type": "application/json" }, headers || {}),
    body: JSON.stringify(body)
  });
  const data = await response.json();
  return { response, data };
}

async function getJson(url) {
  const response = await fetch(url, {
    headers: {
      "a2a-version": "1.0"
    }
  });
  const data = await response.json();
  return { response, data };
}

async function main() {
  runToolUnitTests();

  const server = createServer();
  const baseUrl = await listen(server);

  try {
    const card = await getJson(`${baseUrl}/.well-known/agent-card.json`);
    assert.strictEqual(card.response.status, 200);
    assert.strictEqual(card.data.name, "Coding.Tools");
    assert.ok(card.data.skills.some((skill) => skill.id === "base64-encode"));

    const sent = await postJson(`${baseUrl}/a2a/message:send`, {
      message: {
        role: "ROLE_USER",
        messageId: "msg-test-1",
        parts: [
          {
            data: {
              toolId: "base64-encode",
              input: "Hello, World!"
            },
            mediaType: "application/json"
          }
        ]
      }
    });
    assert.strictEqual(sent.response.status, 200);
    assert.ok(sent.response.headers.get("content-type").includes("application/a2a+json"));
    assert.strictEqual(sent.data.task.status.state, "TASK_STATE_COMPLETED");
    assert.strictEqual(sent.data.task.artifacts[0].parts[0].text, "SGVsbG8sIFdvcmxkIQ==");

    const binary = await postJson(`${baseUrl}/a2a/message:send`, {
      message: {
        role: "ROLE_USER",
        messageId: "msg-test-binary",
        metadata: { toolId: "binary-to-decimal" },
        parts: [{ text: "1010" }]
      }
    });
    assert.strictEqual(binary.response.status, 200);
    assert.strictEqual(binary.data.task.status.state, "TASK_STATE_COMPLETED");
    assert.strictEqual(binary.data.task.artifacts[0].parts[0].text, "10");

    const task = await getJson(`${baseUrl}/a2a/tasks/${sent.data.task.id}`);
    assert.strictEqual(task.response.status, 200);
    assert.ok(task.response.headers.get("content-type").includes("application/a2a+json"));
    assert.strictEqual(task.data.id, sent.data.task.id);

    const failed = await postJson(`${baseUrl}/a2a/message:send`, {
      message: {
        role: "ROLE_USER",
        messageId: "msg-test-2",
        metadata: { toolId: "json-formatter" },
        parts: [{ text: "{bad json" }]
      }
    });
    assert.strictEqual(failed.response.status, 200);
    assert.strictEqual(failed.data.task.status.state, "TASK_STATE_FAILED");

    const list = await getJson(`${baseUrl}/a2a/tasks`);
    assert.strictEqual(list.response.status, 403);
    assert.ok(list.response.headers.get("content-type").includes("application/problem+json"));
    assert.strictEqual(list.data.title, "Task listing is disabled");

    const badVersion = await postJsonWithHeaders(`${baseUrl}/a2a/message:send`, {
      message: {
        role: "ROLE_USER",
        messageId: "msg-bad-version",
        metadata: { toolId: "base64-encode" },
        parts: [{ text: "hello" }]
      }
    }, { "a2a-version": "0.5" });
    assert.strictEqual(badVersion.response.status, 400);
    assert.ok(badVersion.response.headers.get("content-type").includes("application/problem+json"));

    const missingVersion = await postJsonWithHeaders(`${baseUrl}/a2a/message:send`, {
      message: {
        role: "ROLE_USER",
        messageId: "msg-missing-version",
        metadata: { toolId: "base64-encode" },
        parts: [{ text: "hello" }]
      }
    });
    assert.strictEqual(missingVersion.response.status, 400);
    assert.ok(missingVersion.response.headers.get("content-type").includes("application/problem+json"));

    const missingTool = await postJson(`${baseUrl}/a2a/message:send`, {
      message: {
        role: "ROLE_USER",
        messageId: "msg-missing-tool",
        parts: [{ text: "hello" }]
      }
    });
    assert.strictEqual(missingTool.response.status, 400);

    const stream = await postJson(`${baseUrl}/a2a/message:stream`, {
      message: {
        role: "ROLE_USER",
        messageId: "msg-stream",
        metadata: { toolId: "base64-encode" },
        parts: [{ text: "hello" }]
      }
    });
    assert.strictEqual(stream.response.status, 400);

    console.log("A2A runtime tests passed.");
  } finally {
    server.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
