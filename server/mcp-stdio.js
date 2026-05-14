const readline = require("readline");
const { handleMcpMessage, jsonRpcInternalError } = require("./mcp-server");

const rl = readline.createInterface({
  input: process.stdin,
  crlfDelay: Infinity
});

rl.on("line", async (line) => {
  if (!line.trim()) return;
  let message;
  try {
    message = JSON.parse(line);
  } catch (error) {
    process.stdout.write(`${JSON.stringify({
      jsonrpc: "2.0",
      id: null,
      error: {
        code: -32700,
        message: "Parse error"
      }
    })}\n`);
    return;
  }

  let response;
  try {
    response = await handleMcpMessage(message);
  } catch (error) {
    console.error("Unhandled MCP stdio error:", error);
    response = jsonRpcInternalError(message && message.id);
  }
  if (response) {
    process.stdout.write(`${JSON.stringify(response)}\n`);
  }
});

rl.on("close", () => {
  process.exit(0);
});
