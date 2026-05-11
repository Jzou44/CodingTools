const site = require("./site");
const tools = require("./tools.json");
const toolDataAll = require("./toolData");
const categoryDefinitions = require("./categoryDefinitions.json");
const { isRuntimeTool } = require("./a2aRuntimeTools");

const CATALOG_VERSION = "1.0.0";
const A2A_PROTOCOL_VERSION = "1.0";

function stripHtml(value) {
  return String(value || "").replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
}

function wordsFrom(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, " ")
    .trim()
    .split(/\s+/)
    .filter(Boolean);
}

function unique(values) {
  return Array.from(new Set(values.filter(Boolean)));
}

function categoryMap() {
  return categoryDefinitions.reduce((result, category) => {
    result[category.id] = category;
    return result;
  }, {});
}

function modesForCategory(categoryId) {
  if (categoryId === "image-utilities") {
    return {
      inputModes: ["image/png", "image/jpeg", "image/webp", "application/json"],
      outputModes: ["image/png", "image/jpeg", "text/plain", "application/json"]
    };
  }

  return {
    inputModes: ["text/plain", "application/json"],
    outputModes: ["text/plain", "application/json"]
  };
}

function makeTags(slug, title, categoryId) {
  return unique([
    "developer-tool",
    "browser-tool",
    categoryId,
    ...wordsFrom(slug),
    ...wordsFrom(title)
  ]).slice(0, 12);
}

function makeExamples(toolName, data) {
  const examples = [];
  if (data.examplePara) examples.push(stripHtml(data.examplePara));
  if (Array.isArray(data.steps) && data.steps.length) examples.push(stripHtml(data.steps[0]));
  examples.push(`Open ${toolName} and process input in the browser.`);
  return unique(examples).slice(0, 3);
}

function makeLocalizedUrls(slug) {
  return site.languages.reduce((result, language) => {
    result[language.id] = site.absoluteUrl(site.pathFor(language.id, slug));
    return result;
  }, {});
}

function makeTools() {
  const categories = categoryMap();
  const englishToolData = toolDataAll.en || {};

  return Object.entries(tools).map(([slug, tool]) => {
    const data = englishToolData[slug] || {};
    const name = data.toolTitle || tool.title;
    const description = data.toolDescription || data.description || tool.description;
    const category = categories[tool.category] || {};
    const modes = modesForCategory(tool.category);

    return {
      id: slug,
      name,
      description,
      category: tool.category,
      categoryName: data.categoryName || category.name || tool.category,
      url: site.absoluteUrl(site.pathFor("en", slug)),
      localizedUrls: makeLocalizedUrls(slug),
      inputModes: modes.inputModes,
      outputModes: modes.outputModes,
      tags: makeTags(slug, name, tool.category),
      examples: makeExamples(name, data),
      privacy: isRuntimeTool(slug)
        ? "A2A requests are processed by the Coding.Tools runtime. The public website version still runs locally in the user's browser."
        : "Runs locally in the user's browser on the public website.",
      runtime: {
        available: isRuntimeTool(slug),
        endpoint: isRuntimeTool(slug) ? `${site.baseUrl}/a2a/message:send` : null,
        reason: isRuntimeTool(slug)
          ? "Send an A2A HTTP+JSON message with message.metadata.toolId or a data part containing toolId and input."
          : "This tool is browser-only for now and is not exposed through the A2A runtime."
      }
    };
  });
}

module.exports = {
  schemaVersion: CATALOG_VERSION,
  generatedFrom: ["src/_data/tools.json", "src/_data/toolData/*.json"],
  name: site.siteName,
  description: "Agent-readable catalog for Coding.Tools developer utilities.",
  baseUrl: site.baseUrl,
  a2a: {
    protocol: "A2A",
    protocolVersion: A2A_PROTOCOL_VERSION,
    runtimeAvailable: true,
    agentCardUrl: `${site.baseUrl}/.well-known/agent-card.json`,
    supportedInterfaces: [
      {
        url: `${site.baseUrl}/a2a`,
        protocolBinding: "HTTP+JSON",
        protocolVersion: A2A_PROTOCOL_VERSION
      }
    ],
    capabilities: {
      streaming: false,
      pushNotifications: false,
      extendedAgentCard: false
    },
    note: "The A2A runtime supports the subset of tools where runtime.available is true. Browser-only tools remain available through their public web pages."
  },
  defaultInputModes: ["text/plain", "application/json"],
  defaultOutputModes: ["text/plain", "application/json"],
  languages: site.languages,
  categories: categoryDefinitions.map((category) => ({
    id: category.id,
    name: category.name,
    description: category.description
  })),
  tools: makeTools()
};
