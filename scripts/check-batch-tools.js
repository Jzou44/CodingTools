const fs = require("fs");
const path = require("path");

const repoRoot = path.resolve(__dirname, "..");
const layoutPath = path.join(repoRoot, "src", "_includes", "tool-layout.njk");
const batchScriptPath = path.join(repoRoot, "src", "js", "batch-tools.js");
const singleScriptPath = path.join(repoRoot, "src", "js", "single-input-mode.js");

const layout = fs.readFileSync(layoutPath, "utf8");
const batchScript = fs.readFileSync(batchScriptPath, "utf8");
const singleScript = fs.readFileSync(singleScriptPath, "utf8");

const errors = [];

function fail(message) {
  errors.push(message);
}

function extractNunjucksArray(name) {
  const pattern = new RegExp(`\\{%-?\\s*set\\s+${name}\\s*=\\s*\\[(.*?)\\]\\s*-?%\\}`, "s");
  const match = layout.match(pattern);
  if (!match) {
    fail(`Could not find ${name} in tool-layout.njk`);
    return [];
  }
  return Array.from(match[1].matchAll(/"([^"]+)"/g), (item) => item[1]);
}

function extractObjectKeys(objectName) {
  const pattern = new RegExp(`var\\s+${objectName}\\s*=\\s*\\{([\\s\\S]*?)\\n\\s*\\};`);
  const match = batchScript.match(pattern);
  if (!match) {
    fail(`Could not find ${objectName} in batch-tools.js`);
    return [];
  }
  return Array.from(match[1].matchAll(/["']([^"']+)["']\s*:/g), (item) => item[1]);
}

const batchEnabledTools = extractNunjucksArray("batchEnabledTools");
const batchImageTools = new Set(extractNunjucksArray("batchImageTools"));
const outputExtensions = new Set(extractObjectKeys("outputExtensions"));
const imageProcessors = new Set(["image-resize", "image-to-base64"]);

batchEnabledTools.forEach((tool) => {
  if (batchImageTools.has(tool)) {
    if (!imageProcessors.has(tool)) {
      fail(`${tool} is marked as a batch image tool but has no image batch processor`);
    }
    return;
  }

  if (!batchScript.includes(`tool === "${tool}"`)) {
    fail(`${tool} is enabled for batch mode but is missing from transformText()`);
  }

  if (!outputExtensions.has(tool)) {
    fail(`${tool} is enabled for batch mode but is missing from outputExtensions`);
  }
});

imageProcessors.forEach((tool) => {
  if (!batchEnabledTools.includes(tool)) {
    fail(`${tool} has an image batch processor but is not enabled in tool-layout.njk`);
  }
});

const runtimeI18nMatch = layout.match(/window\.CodingToolsRuntimeI18n\s*=\s*\{\{([\s\S]*?)\}\};/);
if (!runtimeI18nMatch) {
  fail("Could not find CodingToolsRuntimeI18n in tool-layout.njk");
}

const runtimeI18nKeys = new Set(
  Array.from((runtimeI18nMatch ? runtimeI18nMatch[1] : "").matchAll(/\b([A-Za-z][A-Za-z0-9]*)\s*:\s*t\.ui\./g), (item) => item[1])
);
const usedRuntimeKeys = new Set(
  Array.from((batchScript + "\n" + singleScript).matchAll(/\btr\("([^"]+)"/g), (item) => item[1])
);

usedRuntimeKeys.forEach((key) => {
  if (!runtimeI18nKeys.has(key)) {
    fail(`Runtime i18n key "${key}" is used by JS but not exposed in tool-layout.njk`);
  }
});

[
  "Batch results will appear here. Each row",
  "Files mode:",
  "Lines mode:",
  "Unsupported batch tool",
  "No file selected. The file content"
].forEach((text) => {
  if ((batchScript + "\n" + singleScript).includes(text)) {
    fail(`Found stale hard-coded UI string: "${text}"`);
  }
});

[
  ["cdnjs.cloudflare.com/ajax/libs/jszip", "JSZip"],
  ["cdn.jsdelivr.net/npm/js-md5", "js-md5"],
  ["cdn.jsdelivr.net/npm/js-beautify", "js-beautify"]
].forEach(([needle, label]) => {
  const matches = [];
  [
    layoutPath,
    ...fs.readdirSync(path.join(repoRoot, "src", "tools"), { recursive: true })
      .filter((name) => name.endsWith(".njk"))
      .map((name) => path.join(repoRoot, "src", "tools", name))
  ].forEach((filePath) => {
    if (fs.readFileSync(filePath, "utf8").includes(needle)) {
      matches.push(path.relative(repoRoot, filePath));
    }
  });

  if (matches.length) {
    fail(`${label} still loads from a CDN in ${matches.join(", ")}`);
  }
});

if (errors.length) {
  console.error("Batch tool checks failed:");
  errors.forEach((error) => console.error(`- ${error}`));
  process.exit(1);
}

console.log(`Batch tool checks passed for ${batchEnabledTools.length} enabled tools.`);
