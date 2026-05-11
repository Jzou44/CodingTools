#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { listMcpTools } = require("../server/mcp-tools");

const repoRoot = path.resolve(__dirname, "..");
const skillsRoot = path.join(repoRoot, "skills", "coding-tools");
const defaultEndpoint = "https://coding.tools/mcp";

function mkdirp(dir) {
  fs.mkdirSync(dir, { recursive: true });
}

function toJson(value) {
  return `${JSON.stringify(value, null, 2)}\n`;
}

function yamlQuote(value) {
  return JSON.stringify(String(value));
}

function truncate(value, maxLength) {
  const text = String(value);
  return text.length <= maxLength ? text : `${text.slice(0, maxLength - 3)}...`;
}

function makeDescription(tool) {
  return [
    `Use when Codex needs to run the Coding.Tools ${tool.title} MCP tool`,
    `(${tool.name}) through tools/list and tools/call for ${tool.description.replace(/\s*Web UI:.*/, "")}`
  ].join(" ");
}

function hasNoArgumentSchema(tool) {
  return tool.inputSchema
    && tool.inputSchema.properties
    && Object.keys(tool.inputSchema.properties).length === 0;
}

function makeArgumentGuidance(tool, exampleArguments, browserOnly) {
  if (browserOnly) {
    return `This tool is exposed in MCP so clients can discover it, but server-side MCP calls do not process image bytes for this browser-only workflow. Use an empty arguments object \`{}\`; the call intentionally returns \`isError: true\` plus a \`resource_link\` to the web UI.`;
  }

  if (hasNoArgumentSchema(tool)) {
    return `This is a fixed reference tool and does not need user input. Use an empty arguments object \`{}\`; the returned \`structuredContent\` contains the reference rows.`;
  }

  const hasOptions = Boolean(exampleArguments && Object.prototype.hasOwnProperty.call(exampleArguments, "options"));
  const hasInput = Boolean(tool.inputSchema
    && tool.inputSchema.properties
    && Object.prototype.hasOwnProperty.call(tool.inputSchema.properties, "input"));
  return [
    "Pass only the JSON object shown in Example Arguments as `tools/call.params.arguments`; do not include the outer JSON-RPC envelope inside `arguments`.",
    hasInput
      ? "Use `input` for the value being converted, formatted, counted, hashed, or tested."
      : "This tool is controlled by `options`; omit `input` unless a future `tools/list` schema adds it.",
    hasOptions
      ? "Use `options` for tool settings such as regex patterns, indentation, alpha values, or generation settings."
      : "Omit `options` unless the discovered `inputSchema` lists a setting you need.",
    "The demo values are synthetic and safe for testing the remote endpoint; replace them with user data only after the privacy check above is satisfied."
  ].join("\n\n");
}

function makeSkillMarkdown(tool) {
  const skillName = `coding-tools-${tool.name}`;
  const exampleArguments = tool.inputSchema.examples && tool.inputSchema.examples.length ? tool.inputSchema.examples[0] : {};
  const browserOnly = tool.outputSchema.description && tool.outputSchema.description.includes("isError=true");
  const humanDescription = tool.description.replace(/\s*Web UI:.*/, "");
  const webUi = `https://coding.tools/${tool.name}.html`;
  const frontmatterDescription = makeDescription(tool);

  return `---
name: ${skillName}
description: ${yamlQuote(frontmatterDescription)}
---

# ${tool.title}

Use the Coding.Tools MCP tool \`${tool.name}\` when the user needs: ${humanDescription}

## Endpoint

Use \`${defaultEndpoint}\` for production. If the user is testing a local Docker container, use \`http://localhost:8080/mcp\`.

## Call Shape

For streamable HTTP, send JSON-RPC requests with \`Content-Type: application/json\`, \`Accept: application/json, text/event-stream\`, and \`MCP-Protocol-Version: 2025-06-18\`.

When an MCP client hides JSON-RPC details, configure the endpoint, select tool \`${tool.name}\`, and pass only the Example Arguments object as the tool arguments.

## Security And Privacy

The production endpoint is a public remote service. Do not send secrets, private keys, tokens, personal data, or proprietary source code unless the user explicitly confirms that remote processing is acceptable. For sensitive data, use a local Docker endpoint such as \`http://localhost:8080/mcp\`.

## Workflow

1. Connect to the MCP endpoint.
2. Call \`tools/list\`.
3. Find the tool whose \`name\` is \`${tool.name}\`.
4. Build \`tools/call.params.arguments\` from the discovered \`inputSchema\`. Start from the example below when the user does not provide a more specific value.
5. Call \`tools/call\` with \`params.name = "${tool.name}"\`.
6. If \`result.isError\` is \`false\`, read \`result.content[0].text\` for display and \`result.structuredContent\` for programmatic parsing.
7. If \`result.isError\` is \`true\`, report the error text and include the returned \`resource_link\` when present.

## Input Schema

\`\`\`json
${JSON.stringify(tool.inputSchema, null, 2)}
\`\`\`

## Argument Guidance

${makeArgumentGuidance(tool, exampleArguments, browserOnly)}

## Output Schema

\`\`\`json
${JSON.stringify(tool.outputSchema, null, 2)}
\`\`\`

## Example Arguments

\`\`\`json
${JSON.stringify(exampleArguments, null, 2)}
\`\`\`

## Example tools/call

\`\`\`json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "${tool.name}",
    "arguments": ${JSON.stringify(exampleArguments, null, 4).replace(/\n/g, "\n    ")}
  }
}
\`\`\`

## Notes

${browserOnly ? `This is a browser-only image tool in MCP. \`tools/call\` returns \`isError: true\` with a \`resource_link\` to ${webUi} instead of processing image bytes server-side.` : `This tool can run directly through MCP. Prefer \`result.structuredContent\` for downstream automation and \`result.content[0].text\` for human-readable output.`}

Web UI: ${webUi}
`;
}

function makeOpenAiYaml(tool) {
  const skillName = `coding-tools-${tool.name}`;
  const shortDescription = truncate(tool.description.replace(/\s*Web UI:.*/, ""), 64);
  return `interface:
  display_name: ${yamlQuote(`Coding.Tools ${tool.title}`)}
  short_description: ${yamlQuote(shortDescription)}
  default_prompt: ${yamlQuote(`Use $${skillName} to run ${tool.title} through Coding.Tools MCP.`)}
dependencies:
  tools:
    - type: "mcp"
      value: "coding-tools"
      description: ${yamlQuote(`Coding.Tools MCP endpoint for ${tool.title}.`)}
      transport: "streamable_http"
      url: "${defaultEndpoint}"
policy:
  allow_implicit_invocation: true
`;
}

function writeSkill(tool) {
  const skillName = `coding-tools-${tool.name}`;
  const dir = path.join(skillsRoot, skillName);
  mkdirp(path.join(dir, "agents"));
  fs.writeFileSync(path.join(dir, "SKILL.md"), makeSkillMarkdown(tool));
  fs.writeFileSync(path.join(dir, "agents", "openai.yaml"), makeOpenAiYaml(tool));
}

function main() {
  const tools = listMcpTools();
  mkdirp(skillsRoot);
  for (const tool of tools) {
    writeSkill(tool);
  }

  const manifest = {
    generatedFrom: "server/mcp-tools.js:listMcpTools",
    language: "en",
    endpoint: defaultEndpoint,
    skillCount: tools.length,
    skills: tools.map((tool) => ({
      name: `coding-tools-${tool.name}`,
      tool: tool.name,
      title: tool.title,
      webUi: `https://coding.tools/${tool.name}.html`
    }))
  };
  fs.writeFileSync(path.join(skillsRoot, "manifest.json"), toJson(manifest));
  console.log(`Generated ${tools.length} Coding.Tools skills in ${path.relative(repoRoot, skillsRoot)}`);
}

main();
