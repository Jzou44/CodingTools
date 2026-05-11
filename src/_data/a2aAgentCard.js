const site = require("./site");
const a2aCapabilities = require("./a2aCapabilities");
const { isRuntimeTool } = require("./a2aRuntimeTools");

const runtimeSkills = a2aCapabilities.tools
  .filter((tool) => isRuntimeTool(tool.id))
  .map((tool) => ({
    id: tool.id,
    name: tool.name,
    description: tool.description,
    tags: tool.tags,
    examples: tool.examples,
    inputModes: tool.inputModes,
    outputModes: tool.outputModes
  }));

module.exports = {
  name: site.siteName,
  description: "A2A runtime for deterministic Coding.Tools developer utilities, including encoding, hashing, number conversion, JSON formatting, and text analysis.",
  supportedInterfaces: [
    {
      url: `${site.baseUrl}/a2a`,
      protocolBinding: "HTTP+JSON",
      protocolVersion: "1.0"
    }
  ],
  provider: {
    organization: site.siteName,
    url: site.baseUrl
  },
  version: "1.0.0",
  capabilities: {
    streaming: false,
    pushNotifications: false,
    extendedAgentCard: false
  },
  defaultInputModes: ["text/plain", "application/json"],
  defaultOutputModes: ["text/plain", "application/json"],
  skills: runtimeSkills,
  iconUrl: site.absoluteUrl(site.ogImage)
};
