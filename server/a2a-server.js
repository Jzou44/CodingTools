const http = require("http");
const crypto = require("crypto");
const a2aAgentCard = require("../src/_data/a2aAgentCard");
const a2aCapabilities = require("../src/_data/a2aCapabilities");
const { executeTool, supportedToolIds, ToolInputError } = require("./a2a-tools");
const { handleMcpHttpRequest } = require("./mcp-server");

const MAX_BODY_BYTES = 1024 * 1024;
const TASK_LIMIT = 1000;
const TASK_TTL_MS = Number(process.env.A2A_TASK_TTL_MS || 15 * 60 * 1000);
const MAX_STORED_TEXT_CHARS = Number(process.env.A2A_MAX_STORED_TEXT_CHARS || 50000);
const tasks = new Map();

function now() {
  return new Date().toISOString();
}

function makeId(prefix) {
  return `${prefix}-${crypto.randomUUID()}`;
}

function sendJson(res, statusCode, value, headers = {}) {
  const body = JSON.stringify(value, null, 2);
  res.writeHead(statusCode, Object.assign({
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    "x-content-type-options": "nosniff",
    "referrer-policy": "no-referrer",
    "access-control-allow-origin": "*",
    "access-control-allow-methods": "GET,POST,OPTIONS",
    "access-control-allow-headers": "content-type,a2a-version"
  }, headers));
  res.end(body);
}

function sendA2aJson(res, statusCode, value) {
  sendJson(res, statusCode, value, { "content-type": "application/a2a+json; charset=utf-8" });
}

function sendProblemJson(res, statusCode, type, title, detail) {
  sendJson(res, statusCode, {
    type,
    title,
    status: statusCode,
    detail
  }, { "content-type": "application/problem+json; charset=utf-8" });
}

function validateA2aVersion(req, url, res) {
  const requestedVersion = req.headers["a2a-version"] || url.searchParams.get("A2A-Version") || "0.3";
  if (requestedVersion === "1.0") return true;
  sendProblemJson(
    res,
    400,
    "https://a2a-protocol.org/problems/unsupported-version",
    "Unsupported A2A protocol version",
    "Coding.Tools A2A runtime supports A2A-Version 1.0."
  );
  return false;
}

function sendError(res, statusCode, reason, message, metadata = {}) {
  sendJson(res, statusCode, {
    error: {
      code: statusCode,
      status: reason,
      message,
      details: [
        {
          "@type": "type.googleapis.com/google.rpc.ErrorInfo",
          reason,
          domain: "coding.tools",
          metadata: Object.assign({ timestamp: now() }, metadata)
        }
      ]
    }
  });
}

function stripBasePath(pathname) {
  if (pathname === "/a2a") return "/";
  if (pathname.startsWith("/a2a/")) return pathname.slice(4);
  return pathname;
}

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on("data", (chunk) => {
      size += chunk.length;
      if (size > MAX_BODY_BYTES) {
        reject(new ToolInputError("Request body is too large."));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on("end", () => {
      try {
        const raw = Buffer.concat(chunks).toString("utf8");
        resolve(raw ? JSON.parse(raw) : {});
      } catch (error) {
        reject(new ToolInputError("Request body must be valid JSON."));
      }
    });
    req.on("error", reject);
  });
}

function contentTypeIsJson(req) {
  const contentType = req.headers["content-type"] || "";
  return contentType.includes("application/json") || contentType.includes("application/a2a+json");
}

function getPartText(part) {
  if (!part || typeof part !== "object") return "";
  if (typeof part.text === "string") return part.text;
  if (part.data !== undefined) return JSON.stringify(part.data);
  return "";
}

function extractInvocation(body) {
  const message = body.message || body;
  const parts = Array.isArray(message.parts) ? message.parts : [];
  const metadata = Object.assign({}, body.metadata || {}, message.metadata || {});
  const dataPart = parts.find((part) => part && part.data && typeof part.data === "object" && !Array.isArray(part.data));
  const data = dataPart ? dataPart.data : {};
  const textPart = parts.find((part) => part && typeof part.text === "string");

  const toolId = body.toolId || metadata.toolId || metadata.skillId || data.toolId || data.skillId;
  const input = body.input !== undefined
    ? body.input
    : data.input !== undefined
      ? data.input
      : data.text !== undefined
        ? data.text
        : textPart
          ? textPart.text
          : "";
  const options = Object.assign({}, body.options || {}, metadata.options || {}, data.options || {});

  if (!toolId) {
    throw new ToolInputError("A toolId is required. Provide message.metadata.toolId or a data part with toolId.");
  }

  return {
    message,
    toolId,
    input,
    options,
    acceptedOutputModes: body.acceptedOutputModes || message.acceptedOutputModes || []
  };
}

function normalizeUserMessage(message) {
  return {
    messageId: message.messageId || makeId("msg"),
    role: message.role || "ROLE_USER",
    parts: Array.isArray(message.parts) && message.parts.length ? message.parts : [{ text: "" }],
    contextId: message.contextId || makeId("ctx")
  };
}

function makeAgentMessage(contextId, text, data) {
  const parts = [{ text }];
  if (data !== undefined) {
    parts.push({
      data,
      mediaType: "application/json"
    });
  }
  return {
    messageId: makeId("msg"),
    role: "ROLE_AGENT",
    parts,
    contextId
  };
}

function rememberTask(task) {
  pruneExpiredTasks();
  const storedTask = trimStoredText(task);
  tasks.set(storedTask.id, storedTask);
  while (tasks.size > TASK_LIMIT) {
    const firstKey = tasks.keys().next().value;
    tasks.delete(firstKey);
  }
}

function pruneExpiredTasks() {
  if (!TASK_TTL_MS || TASK_TTL_MS < 0) return;
  const expiresBefore = Date.now() - TASK_TTL_MS;
  for (const [taskId, task] of tasks) {
    const timestamp = Date.parse(task.status && task.status.timestamp);
    if (!Number.isFinite(timestamp) || timestamp < expiresBefore) {
      tasks.delete(taskId);
    }
  }
}

function truncateText(value) {
  if (typeof value !== "string" || value.length <= MAX_STORED_TEXT_CHARS) return value;
  return `${value.slice(0, MAX_STORED_TEXT_CHARS)}\n[truncated ${value.length - MAX_STORED_TEXT_CHARS} characters]`;
}

function trimStoredPart(part) {
  if (!part || typeof part !== "object") return;
  if (typeof part.text === "string") part.text = truncateText(part.text);
  if (part.data !== undefined) {
    const serialized = JSON.stringify(part.data);
    if (serialized.length > MAX_STORED_TEXT_CHARS) {
      part.data = {
        truncated: true,
        originalBytes: Buffer.byteLength(serialized),
        preview: truncateText(serialized)
      };
    }
  }
}

function trimStoredMessage(message) {
  if (!message || !Array.isArray(message.parts)) return;
  message.parts.forEach(trimStoredPart);
}

function trimStoredText(task) {
  if (!MAX_STORED_TEXT_CHARS || MAX_STORED_TEXT_CHARS < 0) return task;
  const storedTask = JSON.parse(JSON.stringify(task));
  if (storedTask.status && storedTask.status.message) trimStoredMessage(storedTask.status.message);
  if (Array.isArray(storedTask.history)) storedTask.history.forEach(trimStoredMessage);
  if (Array.isArray(storedTask.artifacts)) {
    storedTask.artifacts.forEach((artifact) => {
      if (Array.isArray(artifact.parts)) artifact.parts.forEach(trimStoredPart);
    });
  }
  return storedTask;
}

function makeCompletedTask(userMessage, toolId, result) {
  const contextId = userMessage.contextId || makeId("ctx");
  const agentMessage = makeAgentMessage(contextId, result.text, {
    toolId,
    result: result.data !== undefined ? result.data : result.text
  });
  const task = {
    id: makeId("task"),
    contextId,
    status: {
      state: "TASK_STATE_COMPLETED",
      timestamp: now(),
      message: agentMessage
    },
    artifacts: [
      {
        artifactId: makeId("artifact"),
        name: `${toolId} result`,
        parts: agentMessage.parts
      }
    ],
    history: [userMessage, agentMessage],
    metadata: {
      toolId,
      completedSynchronously: true
    }
  };
  rememberTask(task);
  return task;
}

function makeFailedTask(userMessage, toolId, error) {
  const contextId = userMessage.contextId || makeId("ctx");
  const agentMessage = makeAgentMessage(contextId, error.message, { toolId, error: error.message });
  const task = {
    id: makeId("task"),
    contextId,
    status: {
      state: "TASK_STATE_FAILED",
      timestamp: now(),
      message: agentMessage
    },
    history: [userMessage, agentMessage],
    metadata: {
      toolId,
      error: error.message
    }
  };
  rememberTask(task);
  return task;
}

async function handleSendMessage(req, res) {
  if (!contentTypeIsJson(req)) {
    sendError(res, 415, "CONTENT_TYPE_NOT_SUPPORTED", "Use application/json for A2A requests.");
    return;
  }

  let body;
  try {
    body = await readJsonBody(req);
  } catch (error) {
    sendError(res, 400, "INVALID_ARGUMENT", error.message);
    return;
  }

  let invocation;
  try {
    invocation = extractInvocation(body);
  } catch (error) {
    sendError(res, 400, "INVALID_ARGUMENT", error.message, { supportedToolIds: supportedToolIds.join(",") });
    return;
  }

  const userMessage = normalizeUserMessage(invocation.message);
  try {
    const result = executeTool(invocation.toolId, invocation.input, invocation.options);
    sendA2aJson(res, 200, { task: makeCompletedTask(userMessage, invocation.toolId, result) });
  } catch (error) {
    if (error instanceof ToolInputError) {
      sendA2aJson(res, 200, { task: makeFailedTask(userMessage, invocation.toolId, error) });
      return;
    }
    sendError(res, 500, "INTERNAL", "Tool execution failed.");
  }
}

function handleTaskGet(pathname, res) {
  pruneExpiredTasks();
  const match = pathname.match(/^\/tasks\/([^/]+)$/);
  if (!match) return false;
  const task = tasks.get(decodeURIComponent(match[1]));
  if (!task) {
    sendError(res, 404, "TASK_NOT_FOUND", "Task not found.");
    return true;
  }
  sendA2aJson(res, 200, task);
  return true;
}

function handleTaskCancel(pathname, res) {
  const match = pathname.match(/^\/tasks\/([^/]+):cancel$/);
  if (!match) return false;
  const task = tasks.get(decodeURIComponent(match[1]));
  if (!task) {
    sendError(res, 404, "TASK_NOT_FOUND", "Task not found.");
    return true;
  }
  sendError(res, 400, "TASK_NOT_CANCELABLE", "Coding.Tools A2A tasks complete synchronously and cannot be canceled.");
  return true;
}

async function handleRequest(req, res) {
  const url = new URL(req.url, "http://localhost");

  if (url.pathname === "/mcp" || url.pathname.startsWith("/mcp/")) {
    await handleMcpHttpRequest(req, res);
    return;
  }

  const pathname = stripBasePath(url.pathname);

  if (req.method === "OPTIONS") {
    sendJson(res, 204, {});
    return;
  }

  if (req.method === "GET" && (pathname === "/healthz" || pathname === "/")) {
    sendJson(res, 200, {
      ok: true,
      service: "coding-tools-a2a",
      protocolVersion: "1.0",
      supportedToolCount: supportedToolIds.length
    });
    return;
  }

  if (req.method === "GET" && pathname === "/.well-known/agent-card.json") {
    sendJson(res, 200, a2aAgentCard, { "cache-control": "public, max-age=300" });
    return;
  }

  if (req.method === "GET" && pathname === "/capabilities.json") {
    sendJson(res, 200, a2aCapabilities, { "cache-control": "public, max-age=300" });
    return;
  }

  if (req.method === "POST" && pathname === "/message:send") {
    if (!validateA2aVersion(req, url, res)) return;
    await handleSendMessage(req, res);
    return;
  }

  if (req.method === "POST" && (pathname === "/message:stream" || pathname.endsWith(":subscribe"))) {
    if (!validateA2aVersion(req, url, res)) return;
    sendError(res, 400, "UNSUPPORTED_OPERATION", "Streaming is not enabled for this A2A runtime.");
    return;
  }

  if (req.method === "GET" && pathname === "/tasks") {
    if (!validateA2aVersion(req, url, res)) return;
    sendProblemJson(
      res,
      403,
      "https://coding.tools/problems/task-listing-disabled",
      "Task listing is disabled",
      "Coding.Tools keeps completed tasks retrievable by id only. Public task enumeration is disabled to avoid exposing prior request data."
    );
    return;
  }

  if (req.method === "GET" && /^\/tasks\/[^/]+$/.test(pathname)) {
    if (!validateA2aVersion(req, url, res)) return;
    if (handleTaskGet(pathname, res)) return;
  }
  if (req.method === "POST" && /^\/tasks\/[^/]+:cancel$/.test(pathname)) {
    if (!validateA2aVersion(req, url, res)) return;
    if (handleTaskCancel(pathname, res)) return;
  }

  if (pathname.includes("pushNotification")) {
    if (!validateA2aVersion(req, url, res)) return;
    sendError(res, 400, "UNSUPPORTED_OPERATION", "Push notifications are not enabled for this A2A runtime.");
    return;
  }

  sendError(res, 404, "NOT_FOUND", "Endpoint not found.");
}

function createServer() {
  const server = http.createServer((req, res) => {
    handleRequest(req, res).catch(() => {
      sendError(res, 500, "INTERNAL", "Unhandled runtime error.");
    });
  });
  server.requestTimeout = 10000;
  server.headersTimeout = 11000;
  server.keepAliveTimeout = 5000;
  return server;
}

module.exports = {
  createServer,
  handleRequest
};
