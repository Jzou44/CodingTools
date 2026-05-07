// Auto-merged from src/_data/toolData/*.json — edit per-tool files instead of this.
const fs = require('fs');
const path = require('path');
const dir = path.join(__dirname, 'toolData');
const result = {};

function stripHtml(value) {
  return String(value || '').replace(/<[^>]+>/g, '').trim();
}

function inferButtonLabel(data) {
  if (!data || data.buttonLabel) return data;

  const steps = Array.isArray(data.steps) ? data.steps : [];
  for (const step of steps) {
    const match = String(step || '').match(/<strong>(.*?)<\/strong>/i);
    if (match && stripHtml(match[1])) {
      return Object.assign({}, data, { buttonLabel: stripHtml(match[1]) });
    }
  }

  return Object.assign({}, data, { buttonLabel: data.toolTitle || data.title || '' });
}

fs.readdirSync(dir).filter(f => f.endsWith('.json')).forEach(f => {
  const toolData = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  for (const lang of Object.keys(toolData)) {
    if (!result[lang]) result[lang] = {};
    const slug = f.replace('.json', '');
    result[lang][slug] = inferButtonLabel(toolData[lang]);
  }
});
module.exports = result;
