const { createServer } = require("./a2a-server");

const port = Number(process.env.PORT || process.env.A2A_PORT || 5510);
const host = process.env.HOST || "127.0.0.1";

const server = createServer();

server.listen(port, host, () => {
  console.log(`Coding.Tools A2A runtime listening on http://${host}:${port}/a2a`);
  console.log(`Coding.Tools MCP runtime listening on http://${host}:${port}/mcp`);
});

process.on("SIGTERM", () => {
  server.close(() => process.exit(0));
});

process.on("SIGINT", () => {
  server.close(() => process.exit(0));
});
