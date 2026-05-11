const readline = require("readline");
const { handleMcpMessage } = require("./mcp-server");

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

  const response = await handleMcpMessage(message);
  if (response) {
    process.stdout.write(`${JSON.stringify(response)}\n`);
  }
});

rl.on("close", () => {
  process.exit(0);
});
