// Auto-merged from src/_data/toolData/*.json. Edit per-tool files instead.
const path = require("path");
const { readJsonFiles } = require("./loadJsonDirectory");

const dir = path.join(__dirname, "toolData");
const result = {};

function stripHtml(value) {
  return String(value || "").replace(/<[^>]+>/g, "").trim();
}

function inferButtonLabel(data) {
  if (!data || data.buttonLabel) return data;

  const steps = Array.isArray(data.steps) ? data.steps : [];
  for (const step of steps) {
    const match = String(step || '').match(/<strong>(.*?)<\/strong>/i);
    if (match && stripHtml(match[1])) return Object.assign({}, data, { buttonLabel: stripHtml(match[1]) });
  }

  return Object.assign({}, data, { buttonLabel: data.toolTitle || data.title || "" });
}

readJsonFiles(dir).forEach(({ key: slug, data: toolData }) => {
  for (const lang of Object.keys(toolData)) {
    if (!result[lang]) result[lang] = {};
    result[lang][slug] = inferButtonLabel(toolData[lang]);
  }
});

module.exports = result;
