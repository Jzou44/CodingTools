// Auto-merged from src/_data/t/*.json. Edit per-language files instead.
const path = require("path");
const { loadJsonMap } = require("./loadJsonDirectory");

module.exports = loadJsonMap(path.join(__dirname, "t"));
