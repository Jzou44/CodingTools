// Auto-merged from src/_data/toolData/*.json — edit per-tool files instead of this.
const fs = require('fs');
const path = require('path');
const dir = path.join(__dirname, 'toolData');
const result = {};
fs.readdirSync(dir).filter(f => f.endsWith('.json')).forEach(f => {
  const toolData = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  for (const lang of Object.keys(toolData)) {
    if (!result[lang]) result[lang] = {};
    const slug = f.replace('.json', '');
    result[lang][slug] = toolData[lang];
  }
});
module.exports = result;
