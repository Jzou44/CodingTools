const assert = require("assert");

const baseUrl = process.env.DOCKER_TEST_URL || "http://127.0.0.1:8080";

async function readJson(response) {
  const text = await response.text();
  try {
    return JSON.parse(text);
  } catch (error) {
    throw new Error(`Expected JSON from ${response.url}, got: ${text.slice(0, 200)}`);
  }
}

async function waitFor(url, attempts = 30) {
  let lastError;
  for (let index = 0; index < attempts; index += 1) {
    try {
      const response = await fetch(url);
      if (response.ok) return response;
      lastError = new Error(`${url} returned ${response.status}`);
    } catch (error) {
      lastError = error;
    }
    await new Promise((resolve) => setTimeout(resolve, 1000));
  }
  throw lastError;
}

async function main() {
  const home = await waitFor(`${baseUrl}/`);
  assert.strictEqual(home.status, 200);
  assert.strictEqual(home.headers.get("x-content-type-options"), "nosniff");
  assert.strictEqual(home.headers.get("x-frame-options"), "SAMEORIGIN");

  const cardResponse = await fetch(`${baseUrl}/.well-known/agent-card.json`);
  assert.strictEqual(cardResponse.status, 200);
  assert.ok((cardResponse.headers.get("cache-control") || "").includes("max-age=300"));
  const card = await readJson(cardResponse);
  assert.strictEqual(card.name, "Coding.Tools");
  assert.ok(card.skills.some((skill) => skill.id === "base64-encode"));

  const healthResponse = await fetch(`${baseUrl}/a2a/healthz`);
  assert.strictEqual(healthResponse.status, 200);
  const health = await readJson(healthResponse);
  assert.strictEqual(health.ok, true);

  const sendResponse = await fetch(`${baseUrl}/a2a/message:send`, {
    method: "POST",
    headers: {
      "content-type": "application/a2a+json",
      "a2a-version": "1.0"
    },
    body: JSON.stringify({
      message: {
        role: "ROLE_USER",
        messageId: "docker-smoke",
        metadata: { toolId: "base64-encode" },
        parts: [{ text: "hello docker" }]
      }
    })
  });
  assert.strictEqual(sendResponse.status, 200);
  assert.ok((sendResponse.headers.get("content-type") || "").includes("application/a2a+json"));
  const sent = await readJson(sendResponse);
  assert.strictEqual(sent.task.status.state, "TASK_STATE_COMPLETED");
  assert.strictEqual(sent.task.artifacts[0].parts[0].text, "aGVsbG8gZG9ja2Vy");

  const taskResponse = await fetch(`${baseUrl}/a2a/tasks/${sent.task.id}`, {
    headers: { "a2a-version": "1.0" }
  });
  assert.strictEqual(taskResponse.status, 200);
  const task = await readJson(taskResponse);
  assert.strictEqual(task.id, sent.task.id);

  const taskListResponse = await fetch(`${baseUrl}/a2a/tasks`, {
    headers: { "a2a-version": "1.0" }
  });
  assert.strictEqual(taskListResponse.status, 403);

  const mcpResponse = await fetch(`${baseUrl}/mcp`, {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "accept": "application/json, text/event-stream",
      "mcp-protocol-version": "2025-06-18"
    },
    body: JSON.stringify({
      jsonrpc: "2.0",
      id: 1,
      method: "tools/call",
      params: {
        name: "sha256-generator",
        arguments: { input: "abc" }
      }
    })
  });
  assert.strictEqual(mcpResponse.status, 200);
  assert.ok((mcpResponse.headers.get("x-content-type-options") || "").includes("nosniff"));
  const mcp = await readJson(mcpResponse);
  assert.strictEqual(mcp.result.isError, false);
  assert.strictEqual(mcp.result.content[0].text, "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad");

  const badMcpContentType = await fetch(`${baseUrl}/mcp`, {
    method: "POST",
    headers: {
      "content-type": "text/plain",
      "accept": "application/json",
      "mcp-protocol-version": "2025-06-18"
    },
    body: JSON.stringify({ jsonrpc: "2.0", id: 2, method: "tools/list", params: {} })
  });
  assert.strictEqual(badMcpContentType.status, 415);

  console.log("Docker container smoke tests passed.");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
