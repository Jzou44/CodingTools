const categoryDefinitions = require("./categoryDefinitions.json");
const tools = require("./tools.json");

const counts = Object.values(tools).reduce((acc, tool) => {
  if (tool && tool.category) {
    acc[tool.category] = (acc[tool.category] || 0) + 1;
  }
  return acc;
}, {});

module.exports = categoryDefinitions.map((category) =>
  Object.assign({}, category, { count: counts[category.id] || 0 })
);
