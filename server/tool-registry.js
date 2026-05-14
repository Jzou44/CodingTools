const tools = require("../src/_data/tools.json");
const { supportedToolIds, isRuntimeTool } = require("../src/_data/a2aRuntimeTools");

const toolIds = Object.keys(tools);

const browserOnlyToolIds = new Set([
  "photo2pixel",
  "image-resize",
  "image-crop",
  "compress-png",
  "compress-jpeg",
  "progressive-jpeg",
  "exif-viewer",
  "exif-remover"
]);

const noArgumentToolIds = new Set(["ascii-table", "roman-numerals-chart"]);

function getTool(toolId) {
  return tools[toolId] || null;
}

function isBrowserOnlyTool(toolId) {
  return browserOnlyToolIds.has(toolId);
}

function hasNoArguments(toolId) {
  return noArgumentToolIds.has(toolId);
}

module.exports = {
  tools,
  toolIds,
  supportedToolIds,
  browserOnlyToolIds,
  noArgumentToolIds,
  getTool,
  isRuntimeTool,
  isBrowserOnlyTool,
  hasNoArguments
};

