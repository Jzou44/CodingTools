const fs = require("fs");
const path = require("path");

const repoRoot = path.resolve(__dirname, "..");
const distPath = path.resolve(repoRoot, "dist");

if (path.basename(distPath) !== "dist" || path.dirname(distPath) !== repoRoot) {
  throw new Error(`Refusing to remove unexpected path: ${distPath}`);
}

fs.rmSync(distPath, { recursive: true, force: true });
