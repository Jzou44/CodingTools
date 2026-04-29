// Auto-merged from src/_data/t/*.json — edit per-language files instead of this.
const fs = require('fs');
const path = require('path');
const dir = path.join(__dirname, 't');
const result = {};
fs.readdirSync(dir).filter(f => f.endsWith('.json')).forEach(f => {
  const lang = f.replace('.json', '');
  result[lang] = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
});
module.exports = result;
