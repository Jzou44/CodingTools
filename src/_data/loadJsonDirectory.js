const fs = require("fs");
const path = require("path");

function readJsonFiles(dir) {
  return fs.readdirSync(dir)
    .filter((file) => file.endsWith(".json"))
    .sort()
    .map((file) => ({
      key: path.basename(file, ".json"),
      data: JSON.parse(fs.readFileSync(path.join(dir, file), "utf8"))
    }));
}

function loadJsonMap(dir) {
  return readJsonFiles(dir).reduce((result, item) => {
    result[item.key] = item.data;
    return result;
  }, {});
}

module.exports = {
  readJsonFiles,
  loadJsonMap
};
