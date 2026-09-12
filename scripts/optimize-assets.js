const fs = require("node:fs/promises");
const path = require("node:path");
const { createHash } = require("node:crypto");
const { transform } = require("esbuild");

async function listFiles(directory) {
  const entries = await fs.readdir(directory, { withFileTypes: true });
  const files = await Promise.all(entries.map((entry) => {
    const filename = path.join(directory, entry.name);
    return entry.isDirectory() ? listFiles(filename) : [filename];
  }));
  return files.flat();
}

async function optimizeAssets(outputDirectory) {
  const files = await listFiles(outputDirectory);
  const manifest = {};
  let before = 0;
  let after = 0;
  for (const filename of files) {
    const relative = path.relative(outputDirectory, filename).split(path.sep).join("/");
    if (!/^(css|js)\/.*\.(css|js)$/.test(relative) || /\.[a-f0-9]{16}\.(css|js)$/.test(relative)) continue;
    const source = await fs.readFile(filename, "utf8");
    const extension = path.extname(filename);
    const result = await transform(source, {
      loader: extension.slice(1),
      minify: true,
      // Preserve browser globals used by inline tool scripts and library licenses.
      legalComments: "inline",
      target: extension === ".js" ? "es2020" : ["chrome90", "firefox88", "safari14"],
    });
    const hash = createHash("sha256").update(result.code).digest("hex").slice(0, 16);
    const versioned = relative.slice(0, -extension.length) + "." + hash + extension;
    await fs.writeFile(path.join(outputDirectory, versioned), result.code);
    // Keep stable URLs available for dynamic loaders and external integrations.
    await fs.writeFile(filename, result.code);
    manifest["/" + relative] = "/" + versioned;
    before += Buffer.byteLength(source);
    after += Buffer.byteLength(result.code);
  }
  for (const filename of files.filter((file) => file.endsWith(".html"))) {
    const html = await fs.readFile(filename, "utf8");
    const optimized = html.replace(/\b(src|href)=(['"])(\/(?:css|js)\/[^'"?#]+)(?:\?[^'"#]*)?\2/g,
      (match, attribute, quote, url) => manifest[url]
        ? `${attribute}=${quote}${manifest[url]}${quote}` : match);
    if (optimized !== html) await fs.writeFile(filename, optimized);
  }
  await fs.writeFile(path.join(outputDirectory, "asset-manifest.json"), JSON.stringify(manifest, null, 2) + "\n");
  return { before, after, assets: Object.keys(manifest).length };
}

if (require.main === module) {
  optimizeAssets(path.resolve(__dirname, "../dist")).then(({ before, after, assets }) => {
    console.log(`Optimized ${assets} CSS/JS assets: ${before} -> ${after} bytes (${Math.round((1 - after / before) * 100)}% smaller).`);
  }).catch((error) => { console.error(error); process.exitCode = 1; });
}

module.exports = { optimizeAssets };
