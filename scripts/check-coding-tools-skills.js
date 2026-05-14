#!/usr/bin/env node

const fs = require("fs");
const path = require("path");
const { listMcpTools } = require("../server/mcp-tools");

const repoRoot = path.resolve(__dirname, "..");
const skillsRoot = path.join(repoRoot, "skills", "coding-tools");
const packageJson = require("../package.json");
const MAX_SKILL_NAME_LENGTH = 64;

let failures = 0;

function fail(message) {
  failures += 1;
  console.error(message);
}

function read(file) {
  return fs.readFileSync(file, "utf8");
}

function normalizeLineEndings(value) {
  return String(value).replace(/\r\n/g, "\n").replace(/\r/g, "\n");
}

function parseFrontmatter(markdown, skillName) {
  const match = normalizeLineEndings(markdown).match(/^---\n([\s\S]*?)\n---/);
  if (!match) {
    fail(`${skillName} has invalid YAML frontmatter delimiters.`);
    return {};
  }

  const frontmatter = {};
  for (const line of match[1].split(/\r?\n/)) {
    const separator = line.indexOf(":");
    if (separator === -1) {
      fail(`${skillName} has invalid frontmatter line: ${line}`);
      continue;
    }
    const key = line.slice(0, separator).trim();
    let value = line.slice(separator + 1).trim();
    if (value.startsWith('"') && value.endsWith('"')) {
      try {
        value = JSON.parse(value);
      } catch (error) {
        fail(`${skillName} has invalid quoted frontmatter value for ${key}.`);
      }
    }
    frontmatter[key] = value;
  }
  return frontmatter;
}

function listGeneratedSkillNames() {
  if (!fs.existsSync(skillsRoot)) return [];
  return fs
    .readdirSync(skillsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();
}

function hasNoArgumentSchema(schema) {
  return schema
    && schema.properties
    && Object.keys(schema.properties).length === 0;
}

function validateExample(tool, skillName) {
  const examples = tool.inputSchema && tool.inputSchema.examples;
  if (!Array.isArray(examples) || examples.length !== 1) {
    fail(`${skillName} input schema must expose exactly one example.`);
    return;
  }

  const example = examples[0];
  const noArgument = hasNoArgumentSchema(tool.inputSchema);
  const isEmptyObject = example
    && typeof example === "object"
    && !Array.isArray(example)
    && Object.keys(example).length === 0;

  if (noArgument && !isEmptyObject) {
    fail(`${skillName} should use an empty example object because it has no arguments.`);
  }
  if (!noArgument && isEmptyObject) {
    fail(`${skillName} needs a non-empty demo argument object.`);
  }

  const serialized = JSON.stringify(example);
  if (/(token|secret|api[_-]?key|private key)/i.test(serialized)) {
    fail(`${skillName} demo arguments should not look like secrets or credentials.`);
  }
  if (/\b\d{3}-\d{3}-\d{4}\b/.test(serialized)) {
    fail(`${skillName} demo arguments should not look like a phone number.`);
  }
}

function main() {
  const tools = listMcpTools();
  const expectedNames = tools.map((tool) => `coding-tools-${tool.name}`).sort();
  const actualNames = listGeneratedSkillNames();

  if (JSON.stringify(expectedNames) !== JSON.stringify(actualNames)) {
    fail(`Expected ${expectedNames.length} generated skill folders, found ${actualNames.length}. Run npm run skills:generate.`);
  }

  const manifestPath = path.join(skillsRoot, "manifest.json");
  if (!fs.existsSync(manifestPath)) {
    fail("skills/coding-tools/manifest.json is missing.");
  } else {
    const manifest = JSON.parse(read(manifestPath));
    if (manifest.language !== "en") fail("Skill manifest language must be en.");
    if (manifest.skillCount !== tools.length) fail("Skill manifest count does not match tools/list.");
    if (!Array.isArray(manifest.skills) || manifest.skills.length !== tools.length) {
      fail("Skill manifest skills array does not match tools/list.");
    }
  }

  for (const tool of tools) {
    const skillName = `coding-tools-${tool.name}`;
    const skillDir = path.join(skillsRoot, skillName);
    const skillPath = path.join(skillDir, "SKILL.md");
    const openaiPath = path.join(skillDir, "agents", "openai.yaml");
    validateExample(tool, skillName);

    if (!fs.existsSync(skillPath)) {
      fail(`${skillName} is missing SKILL.md.`);
      continue;
    }

    const markdown = normalizeLineEndings(read(skillPath));
    const frontmatter = parseFrontmatter(markdown, skillName);
    const keys = Object.keys(frontmatter).sort();
    if (JSON.stringify(keys) !== JSON.stringify(["description", "name"])) {
      fail(`${skillName} frontmatter should contain only name and description.`);
    }
    if (frontmatter.name !== skillName) {
      fail(`${skillName} has invalid SKILL.md frontmatter name.`);
    }
    if (!/^[a-z0-9-]+$/.test(skillName) || skillName.startsWith("-") || skillName.endsWith("-") || skillName.includes("--")) {
      fail(`${skillName} must be lowercase hyphen-case.`);
    }
    if (skillName.length > MAX_SKILL_NAME_LENGTH) {
      fail(`${skillName} exceeds ${MAX_SKILL_NAME_LENGTH} characters.`);
    }
    if (!frontmatter.description || typeof frontmatter.description !== "string") {
      fail(`${skillName} frontmatter description is missing.`);
    } else {
      if (frontmatter.description.length > 1024) fail(`${skillName} frontmatter description is too long.`);
      if (frontmatter.description.includes("<") || frontmatter.description.includes(">")) {
        fail(`${skillName} frontmatter description must not contain angle brackets.`);
      }
    }
    [
      `MCP tool \`${tool.name}\``,
      "## Call Shape",
      "## Input Schema",
      "## Argument Guidance",
      "## Output Schema",
      "## Example Arguments",
      "tools/list",
      "tools/call",
      "result.structuredContent"
    ].forEach((needle) => {
      if (!markdown.includes(needle)) fail(`${skillName} SKILL.md is missing "${needle}".`);
    });

    if (!markdown.includes(JSON.stringify(tool.inputSchema, null, 2))) {
      fail(`${skillName} SKILL.md input schema is stale. Run npm run skills:generate.`);
    }
    if (!markdown.includes(JSON.stringify(tool.outputSchema, null, 2))) {
      fail(`${skillName} SKILL.md output schema is stale. Run npm run skills:generate.`);
    }

    if (!fs.existsSync(openaiPath)) {
      fail(`${skillName} is missing agents/openai.yaml.`);
    } else {
      const openai = read(openaiPath);
      if (!openai.includes(`Use $${skillName}`)) {
        fail(`${skillName} agents/openai.yaml default prompt should mention $${skillName}.`);
      }
    }
  }

  if (!packageJson.bin || packageJson.bin["install-coding-tools-skills"] !== "./scripts/install-coding-tools-skills.js") {
    fail("package.json must expose the install-coding-tools-skills npx bin.");
  }

  if (failures) {
    console.error(`Coding.Tools skill check failed with ${failures} issue(s).`);
    process.exit(1);
  }

  console.log(`Coding.Tools skill check passed for ${tools.length} English skills.`);
}

main();
