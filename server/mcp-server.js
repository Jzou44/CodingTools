const { listMcpTools, callMcpTool } = require("./mcp-tools");

const MCP_PROTOCOL_VERSION = "2025-06-18";
const SUPPORTED_PROTOCOL_VERSIONS = new Set(["2025-06-18", "2025-03-26"]);
const MAX_BODY_BYTES = 1024 * 1024;

function jsonRpcResult(id, result) {
  return { jsonrpc: "2.0", id, result };
}

function jsonRpcError(id, code, message, data) {
  const error = { code, message };
  if (data !== undefined) error.data = data;
  return { jsonrpc: "2.0", id: id === undefined ? null : id, error };
}

function isJsonRpcRequest(message) {
  return message && typeof message === "object" && !Array.isArray(message) && message.jsonrpc === "2.0" && typeof message.method === "string";
}

function initializeResult(params = {}) {
  const requested = params.protocolVersion;
  const protocolVersion = SUPPORTED_PROTOCOL_VERSIONS.has(requested) ? requested : MCP_PROTOCOL_VERSION;
  return {
    protocolVersion,
    capabilities: {
      tools: {
        listChanged: false
      }
    },
    serverInfo: {
      name: "coding-tools",
      title: "Coding.Tools MCP Runtime",
      version: "2.0.0"
    },
    instructions: "Use tools/list to discover every Coding.Tools utility. Each tool includes inputSchema, outputSchema, and examples. Use tools/call with the tool name and arguments. Read content[0].text for display text and structuredContent for machine parsing; tool-level failures set isError=true."
  };
}

async function handleMcpMessage(message) {
  if (!isJsonRpcRequest(message)) {
    return jsonRpcError(message && message.id, -32600, "Invalid JSON-RPC request.");
  }

  const hasId = Object.prototype.hasOwnProperty.call(message, "id");
  const id = message.id;
  const params = message.params || {};

  if (!hasId) {
    return null;
  }

  switch (message.method) {
    case "initialize":
      return jsonRpcResult(id, initializeResult(params));
    case "ping":
      return jsonRpcResult(id, {});
    case "tools/list":
      return jsonRpcResult(id, {
        tools: listMcpTools(),
        nextCursor: null
      });
    case "tools/call": {
      if (!params || typeof params.name !== "string") {
        return jsonRpcError(id, -32602, "tools/call requires params.name.");
      }
      return jsonRpcResult(id, await callMcpTool(params.name, params.arguments || {}));
    }
    default:
      return jsonRpcError(id, -32601, `Method not found: ${message.method}`);
  }
}

function sendHttpJson(res, statusCode, value, headers = {}) {
  const body = value === undefined ? "" : JSON.stringify(value);
  res.writeHead(statusCode, Object.assign({
    "content-type": "application/json; charset=utf-8",
    "cache-control": "no-store",
    "x-content-type-options": "nosniff",
    "referrer-policy": "no-referrer",
    "access-control-allow-origin": "*",
    "access-control-allow-methods": "POST,OPTIONS",
    "access-control-allow-headers": "content-type,accept,mcp-protocol-version"
  }, headers));
  res.end(body);
}

function readJsonBody(req) {
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on("data", (chunk) => {
      size += chunk.length;
      if (size > MAX_BODY_BYTES) {
        reject(new Error("Request body is too large."));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on("end", () => {
      const raw = Buffer.concat(chunks).toString("utf8");
      try {
        resolve(raw ? JSON.parse(raw) : {});
      } catch (error) {
        reject(new Error("Request body must be valid JSON."));
      }
    });
    req.on("error", reject);
  });
}

function acceptsJson(req) {
  const accept = req.headers.accept || "";
  return !accept || accept.includes("application/json") || accept.includes("*/*");
}

function contentTypeIsJson(req) {
  const contentType = req.headers["content-type"] || "";
  return contentType.includes("application/json");
}

function validateProtocolHeader(req) {
  const value = req.headers["mcp-protocol-version"];
  return !value || SUPPORTED_PROTOCOL_VERSIONS.has(value);
}

async function handleMcpHttpRequest(req, res) {
  const url = new URL(req.url, "http://localhost");
  if (url.pathname !== "/mcp") {
    sendHttpJson(res, 404, jsonRpcError(null, -32601, "MCP endpoint not found."));
    return;
  }

  if (req.method === "OPTIONS") {
    sendHttpJson(res, 202, undefined);
    return;
  }

  if (req.method !== "POST") {
    sendHttpJson(res, 405, jsonRpcError(null, -32601, "MCP Streamable HTTP endpoint accepts POST requests."), {
      allow: "POST, OPTIONS"
    });
    return;
  }

  if (!validateProtocolHeader(req)) {
    sendHttpJson(res, 400, jsonRpcError(null, -32602, "Unsupported MCP-Protocol-Version header.", {
      supported: Array.from(SUPPORTED_PROTOCOL_VERSIONS)
    }));
    return;
  }

  if (!acceptsJson(req)) {
    sendHttpJson(res, 406, jsonRpcError(null, -32602, "Accept header must allow application/json."));
    return;
  }

  if (!contentTypeIsJson(req)) {
    sendHttpJson(res, 415, jsonRpcError(null, -32602, "Content-Type must be application/json."));
    return;
  }

  let message;
  try {
    message = await readJsonBody(req);
  } catch (error) {
    sendHttpJson(res, 400, jsonRpcError(null, -32700, error.message));
    return;
  }

  if (Array.isArray(message)) {
    sendHttpJson(res, 400, jsonRpcError(null, -32600, "MCP HTTP transport expects a single JSON-RPC message."));
    return;
  }

  const response = await handleMcpMessage(message);
  if (!response) {
    sendHttpJson(res, 202, undefined);
    return;
  }
  sendHttpJson(res, 200, response);
}

module.exports = {
  MCP_PROTOCOL_VERSION,
  handleMcpMessage,
  handleMcpHttpRequest
};
