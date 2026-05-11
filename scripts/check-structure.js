const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const srcDir = path.join(root, "src");
const toolsDir = path.join(srcDir, "tools");

const site = require(path.join(srcDir, "_data", "site.js"));
const tools = require(path.join(srcDir, "_data", "tools.json"));
const categories = require(path.join(srcDir, "_data", "categories.js"));
const categoryDefinitions = require(path.join(srcDir, "_data", "categoryDefinitions.json"));
const homepage = require(path.join(srcDir, "_data", "homepage.json"));
const t = require(path.join(srcDir, "_data", "t.js"));
const a2aCapabilities = require(path.join(srcDir, "_data", "a2aCapabilities.js"));
const a2aAgentCard = require(path.join(srcDir, "_data", "a2aAgentCard.js"));
const { supportedToolIds } = require(path.join(srcDir, "_data", "a2aRuntimeTools.js"));
const mcpExamples = require(path.join(srcDir, "_data", "mcpExamples.js"));

const errors = [];

function fail(message) {
  errors.push(message);
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function sorted(value) {
  return Array.from(value).sort();
}

function diff(expected, actual) {
  const actualSet = new Set(actual);
  return expected.filter((item) => !actualSet.has(item));
}

function unexpected(expected, actual) {
  const expectedSet = new Set(expected);
  return actual.filter((item) => !expectedSet.has(item));
}

function collectPaths(value, prefix = "") {
  if (!value || typeof value !== "object" || Array.isArray(value)) {
    return [prefix];
  }

  return Object.keys(value).flatMap((key) => collectPaths(value[key], prefix ? `${prefix}.${key}` : key));
}

function hasPath(value, dottedPath) {
  return dottedPath.split(".").every((part) => {
    if (!value || typeof value !== "object" || !Object.prototype.hasOwnProperty.call(value, part)) {
      return false;
    }
    value = value[part];
    return true;
  });
}

function parseFrontMatter(filePath) {
  const content = fs.readFileSync(filePath, "utf8");
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return {};

  return match[1].split(/\r?\n/).reduce((data, line) => {
    const pair = line.match(/^([A-Za-z0-9_-]+):\s*(.*)$/);
    if (!pair) return data;

    const rawValue = pair[2].trim();
    data[pair[1]] = rawValue.replace(/^["']|["']$/g, "");
    return data;
  }, {});
}

function checkLanguageSets() {
  const languageIds = site.languageIds;
  const homepageLangs = Object.keys(homepage);
  const tLangs = Object.keys(t);
  const homepageMissing = diff(languageIds, homepageLangs);
  const tMissing = diff(languageIds, tLangs);

  homepageMissing.forEach((lang) => fail(`homepage.json is missing language "${lang}"`));
  tMissing.forEach((lang) => fail(`t/${lang}.json is missing`));
  unexpected(languageIds, homepageLangs).forEach((lang) => fail(`homepage.json has unknown language "${lang}"`));
  unexpected(languageIds, tLangs).forEach((lang) => fail(`t/${lang}.json has unknown language "${lang}"`));
}

function checkTranslationShape(name, data) {
  const baseline = data.en;
  if (!baseline) {
    fail(`${name} is missing en baseline data`);
    return;
  }

  const requiredPaths = collectPaths(baseline).filter(Boolean);
  site.languageIds.forEach((lang) => {
    const value = data[lang];
    if (!value) return;

    requiredPaths.forEach((requiredPath) => {
      if (!hasPath(value, requiredPath)) {
        fail(`${name}.${lang} is missing required key "${requiredPath}"`);
      }
    });
  });
}

function checkDataShapeAgainstBaseline(name, baseline, value, prefix) {
  if (Array.isArray(baseline)) {
    if (!Array.isArray(value)) {
      fail(`${name}.${prefix} should be an array`);
      return;
    }
    if (value.length !== baseline.length) {
      fail(`${name}.${prefix} has ${value.length} item(s), expected ${baseline.length}`);
      return;
    }
    baseline.forEach((item, index) => {
      checkDataShapeAgainstBaseline(name, item, value[index], `${prefix}[${index}]`);
    });
    return;
  }

  if (baseline && typeof baseline === "object") {
    if (!value || typeof value !== "object" || Array.isArray(value)) {
      fail(`${name}.${prefix} should be an object`);
      return;
    }
    Object.keys(baseline).forEach((key) => {
      const nextPrefix = prefix ? `${prefix}.${key}` : key;
      if (!Object.prototype.hasOwnProperty.call(value, key)) {
        fail(`${name}.${nextPrefix} is missing`);
        return;
      }
      checkDataShapeAgainstBaseline(name, baseline[key], value[key], nextPrefix);
    });
    return;
  }

  if (typeof baseline === "string") {
    if (typeof value !== "string") {
      fail(`${name}.${prefix} should be a string`);
      return;
    }
    if (baseline.trim() && !value.trim()) {
      fail(`${name}.${prefix} is empty but the English baseline is not`);
    }
  }
}

function checkToolDataFiles() {
  const dataDir = path.join(srcDir, "_data", "toolData");
  const slugs = Object.keys(tools);
  const dataFiles = fs.readdirSync(dataDir).filter((file) => file.endsWith(".json"));
  const dataSlugs = dataFiles.map((file) => path.basename(file, ".json"));

  diff(slugs, dataSlugs).forEach((slug) => fail(`tools.json slug "${slug}" has no _data/toolData/${slug}.json`));
  diff(dataSlugs, slugs).forEach((slug) => fail(`_data/toolData/${slug}.json has no matching tools.json entry`));

  dataFiles.forEach((file) => {
    const slug = path.basename(file, ".json");
    const data = readJson(path.join(dataDir, file));
    const languages = Object.keys(data);
    diff(site.languageIds, languages).forEach((lang) => fail(`_data/toolData/${slug}.json is missing language "${lang}"`));
    unexpected(site.languageIds, languages).forEach((lang) => fail(`_data/toolData/${slug}.json has unknown language "${lang}"`));

    if (data.en) {
      site.localizedLanguageIds.forEach((lang) => {
        if (data[lang]) {
          checkDataShapeAgainstBaseline(`_data/toolData/${slug}.json.${lang}`, data.en, data[lang], "");
        }
      });
    }
  });
}

function checkHomepageToolTitles() {
  const slugs = Object.keys(tools);
  site.languageIds.forEach((lang) => {
    const data = homepage[lang];
    if (!data) return;

    const toolTitles = data.toolTitles || {};
    diff(slugs, Object.keys(toolTitles)).forEach((slug) => {
      fail(`homepage.${lang}.toolTitles is missing tool "${slug}"`);
    });
    unexpected(slugs, Object.keys(toolTitles)).forEach((slug) => {
      fail(`homepage.${lang}.toolTitles references unknown tool "${slug}"`);
    });
  });
}

function checkCategories() {
  const categoryIds = new Set(categoryDefinitions.map((category) => category.id));
  const categoryIdList = Array.from(categoryIds);
  Object.entries(tools).forEach(([slug, tool]) => {
    if (!categoryIds.has(tool.category)) {
      fail(`tools.json slug "${slug}" references unknown category "${tool.category}"`);
    }
  });

  const expectedCounts = Object.values(tools).reduce((acc, tool) => {
    acc[tool.category] = (acc[tool.category] || 0) + 1;
    return acc;
  }, {});

  categories.forEach((category) => {
    const expected = expectedCounts[category.id] || 0;
    if (category.count !== expected) {
      fail(`category "${category.id}" count is ${category.count}, expected ${expected}`);
    }
  });

  site.languageIds.forEach((lang) => {
    const data = homepage[lang];
    if (!data) return;

    const categoryTitles = data.categories || {};
    const categoryDescs = data.categoryDescs || {};
    diff(categoryIdList, Object.keys(categoryTitles)).forEach((categoryId) => {
      fail(`homepage.${lang}.categories is missing category "${categoryId}"`);
    });
    unexpected(categoryIdList, Object.keys(categoryTitles)).forEach((categoryId) => {
      fail(`homepage.${lang}.categories references unknown category "${categoryId}"`);
    });
    diff(categoryIdList, Object.keys(categoryDescs)).forEach((categoryId) => {
      fail(`homepage.${lang}.categoryDescs is missing category "${categoryId}"`);
    });
    unexpected(categoryIdList, Object.keys(categoryDescs)).forEach((categoryId) => {
      fail(`homepage.${lang}.categoryDescs references unknown category "${categoryId}"`);
    });
  });
}

function checkToolPages() {
  const slugs = sorted(Object.keys(tools));
  const localizedMetadataOverrides = ["title", "description", "toolTitle", "toolDescription", "categoryName"];
  const localizedEnglishLiterals = [
    />Regex Pattern</,
    />Test Text</,
    />Replace With</,
    />Match Results</,
    />Match Preview</,
    />Fraction</,
    />Example:/,
    />ASCII Input</,
    />Hex Input</,
    />Hex Output</,
    />ASCII Output</,
    />Binary Output</,
    /Cannot divide by zero/,
    /placeholder="Enter regex pattern/,
    /placeholder="Replacement string/,
    /placeholder="Enter or paste text/
  ];

  slugs.forEach((slug) => {
    const enPath = path.join(toolsDir, `${slug}.njk`);
    if (!fs.existsSync(enPath)) {
      fail(`English tool template is missing for "${slug}"`);
      return;
    }

    const data = parseFrontMatter(enPath);
    const expected = site.pathFor("en", slug);
    if (data.permalink && data.permalink !== expected) {
      fail(`${path.relative(root, enPath)} permalink is "${data.permalink}", expected "${expected}"`);
    }
  });

  site.localizedLanguageIds.forEach((lang) => {
    slugs.forEach((slug) => {
      const filePath = path.join(toolsDir, lang, `${slug}.njk`);
      if (!fs.existsSync(filePath)) {
        fail(`${lang} tool template is missing for "${slug}"`);
        return;
      }

      const data = parseFrontMatter(filePath);
      localizedMetadataOverrides.forEach((key) => {
        if (Object.prototype.hasOwnProperty.call(data, key)) {
          fail(`${path.relative(root, filePath)} should use translated data instead of localized frontmatter "${key}"`);
        }
      });

      const content = fs.readFileSync(filePath, "utf8");
      localizedEnglishLiterals.forEach((pattern) => {
        if (pattern.test(content)) {
          fail(`${path.relative(root, filePath)} contains hard-coded English UI matching ${pattern}`);
        }
      });

      const expectedPermalink = site.pathFor(lang, slug);
      if (data.permalink && data.permalink !== expectedPermalink) {
        fail(`${path.relative(root, filePath)} permalink is "${data.permalink}", expected "${expectedPermalink}"`);
      }
      if (data.toolId && data.toolId !== slug) {
        fail(`${path.relative(root, filePath)} toolId is "${data.toolId}", expected "${slug}"`);
      }
    });
  });
}

function checkA2aCapabilities() {
  const slugs = sorted(Object.keys(tools));
  const catalogTools = Array.isArray(a2aCapabilities.tools) ? a2aCapabilities.tools : [];
  const catalogSlugs = sorted(catalogTools.map((tool) => tool.id));
  const runtimeSlugs = sorted(supportedToolIds);

  if (a2aCapabilities.a2a && a2aCapabilities.a2a.runtimeAvailable !== true) {
    fail("a2aCapabilities.a2a.runtimeAvailable should be true when the A2A runtime is implemented");
  }

  if (!a2aCapabilities.a2a || !Array.isArray(a2aCapabilities.a2a.supportedInterfaces) || !a2aCapabilities.a2a.supportedInterfaces.length) {
    fail("a2aCapabilities.a2a.supportedInterfaces should declare the live A2A runtime");
  }

  diff(slugs, catalogSlugs).forEach((slug) => fail(`a2aCapabilities.tools is missing tool "${slug}"`));
  unexpected(slugs, catalogSlugs).forEach((slug) => fail(`a2aCapabilities.tools has unknown tool "${slug}"`));
  unexpected(slugs, runtimeSlugs).forEach((slug) => fail(`a2aRuntimeTools references unknown tool "${slug}"`));

  catalogTools.forEach((entry) => {
    const slug = entry.id;
    const source = tools[slug];
    if (!source) return;

    if (!entry.name || !entry.description) {
      fail(`a2aCapabilities.tools.${slug} should have name and description`);
    }

    if (entry.category !== source.category) {
      fail(`a2aCapabilities.tools.${slug}.category is "${entry.category}", expected "${source.category}"`);
    }

    const expectedUrl = site.absoluteUrl(site.pathFor("en", slug));
    if (entry.url !== expectedUrl) {
      fail(`a2aCapabilities.tools.${slug}.url is "${entry.url}", expected "${expectedUrl}"`);
    }

    site.languageIds.forEach((lang) => {
      const expectedLocalizedUrl = site.absoluteUrl(site.pathFor(lang, slug));
      if (!entry.localizedUrls || entry.localizedUrls[lang] !== expectedLocalizedUrl) {
        fail(`a2aCapabilities.tools.${slug}.localizedUrls.${lang} is missing or incorrect`);
      }
    });

    if (!Array.isArray(entry.tags) || !entry.tags.length) {
      fail(`a2aCapabilities.tools.${slug}.tags should be a non-empty array`);
    }

    if (!Array.isArray(entry.inputModes) || !entry.inputModes.length) {
      fail(`a2aCapabilities.tools.${slug}.inputModes should be a non-empty array`);
    }

    if (!Array.isArray(entry.outputModes) || !entry.outputModes.length) {
      fail(`a2aCapabilities.tools.${slug}.outputModes should be a non-empty array`);
    }

    const shouldBeRuntimeAvailable = supportedToolIds.includes(slug);
    if (!entry.runtime || entry.runtime.available !== shouldBeRuntimeAvailable) {
      fail(`a2aCapabilities.tools.${slug}.runtime.available should be ${shouldBeRuntimeAvailable}`);
    }
  });
}

function checkA2aAgentCard() {
  const skills = Array.isArray(a2aAgentCard.skills) ? a2aAgentCard.skills : [];
  const skillIds = sorted(skills.map((skill) => skill.id));
  const runtimeSlugs = sorted(supportedToolIds);

  ["name", "description", "version"].forEach((key) => {
    if (!a2aAgentCard[key]) fail(`a2aAgentCard.${key} is required`);
  });

  if (!Array.isArray(a2aAgentCard.supportedInterfaces) || !a2aAgentCard.supportedInterfaces.length) {
    fail("a2aAgentCard.supportedInterfaces should declare at least one interface");
  }

  if (!a2aAgentCard.capabilities || a2aAgentCard.capabilities.streaming !== false || a2aAgentCard.capabilities.pushNotifications !== false) {
    fail("a2aAgentCard.capabilities should explicitly disable streaming and pushNotifications");
  }

  diff(runtimeSlugs, skillIds).forEach((slug) => fail(`a2aAgentCard.skills is missing runtime tool "${slug}"`));
  unexpected(runtimeSlugs, skillIds).forEach((slug) => fail(`a2aAgentCard.skills has unknown runtime tool "${slug}"`));

  skills.forEach((skill) => {
    if (!skill.name || !skill.description) {
      fail(`a2aAgentCard.skills.${skill.id} should have name and description`);
    }
    if (!Array.isArray(skill.tags) || !skill.tags.length) {
      fail(`a2aAgentCard.skills.${skill.id}.tags should be a non-empty array`);
    }
  });
}

function checkMcpDocumentation() {
  const requiredUiKeys = [
    "mcpIntegrationTitle",
    "mcpIntegrationIntro",
    "mcpToolNameLabel",
    "mcpEndpointLabel",
    "mcpCurlIntro",
    "mcpArgumentsNote",
    "mcpDiscoveryNote",
    "mcpOutputNote",
    "mcpBrowserOnlyNote",
    "mcpImageInputNote"
  ];
  const layoutPath = path.join(srcDir, "_includes", "tool-layout.njk");
  const mcpSectionPath = path.join(srcDir, "_includes", "mcp-integration-section.njk");
  const layout = fs.existsSync(layoutPath) ? fs.readFileSync(layoutPath, "utf8") : "";
  const mcpSection = fs.existsSync(mcpSectionPath) ? fs.readFileSync(mcpSectionPath, "utf8") : "";
  const validExtends = [
    '{% extends "tool-layout.njk" %}',
    '{% extends "photo2pixel-page.njk" %}'
  ];

  if (!layout.includes('{% include "mcp-integration-section.njk" %}')) {
    fail("tool-layout.njk should include the MCP integration documentation section");
  }

  if (!mcpSection) {
    fail("mcp-integration-section.njk is missing");
  } else {
    ["tools/list", "tools/call", "MCP-Protocol-Version", "mcpToolName", "structuredContent", "isError"].forEach((needle) => {
      if (!mcpSection.includes(needle)) {
        fail(`mcp-integration-section.njk should mention "${needle}"`);
      }
    });
    if (mcpSection.includes('mcpExampleInput = "Hello"') || mcpSection.includes('"input":"{{ mcpExampleInput }}"')) {
      fail("mcp-integration-section.njk should use per-tool MCP examples instead of a hard-coded Hello input");
    }
  }

  const mcpArgumentExamples = mcpExamples.arguments || {};
  const mcpArgumentJson = mcpExamples.argumentsJson || {};
  const slugs = Object.keys(tools);
  diff(slugs, Object.keys(mcpArgumentExamples)).forEach((slug) => {
    fail(`mcpExamples.arguments is missing tool "${slug}"`);
  });
  unexpected(slugs, Object.keys(mcpArgumentExamples)).forEach((slug) => {
    fail(`mcpExamples.arguments has unknown tool "${slug}"`);
  });
  slugs.forEach((slug) => {
    const example = mcpArgumentExamples[slug];
    if (!example || typeof example !== "object" || Array.isArray(example)) {
      fail(`mcpExamples.arguments.${slug} should be an arguments object`);
      return;
    }
    const serialized = JSON.stringify(example);
    if (serialized.includes('"input":"Hello"')) {
      fail(`mcpExamples.arguments.${slug} should not use the generic Hello input`);
    }
    if (mcpArgumentJson[slug] !== serialized) {
      fail(`mcpExamples.argumentsJson.${slug} should match the compact JSON form of arguments.${slug}`);
    }
  });

  site.languageIds.forEach((lang) => {
    requiredUiKeys.forEach((key) => {
      const value = t[lang] && t[lang].ui && t[lang].ui[key];
      if (typeof value !== "string" || !value.trim()) {
        fail(`t.${lang}.ui.${key} is required for MCP documentation`);
      }
    });
  });

  Object.keys(tools).forEach((slug) => {
    site.languageIds.forEach((lang) => {
      const filePath = lang === "en"
        ? path.join(toolsDir, `${slug}.njk`)
        : path.join(toolsDir, lang, `${slug}.njk`);
      if (!fs.existsSync(filePath)) return;

      const content = fs.readFileSync(filePath, "utf8");
      if (!validExtends.some((line) => content.includes(line))) {
        fail(`${path.relative(root, filePath)} should extend tool-layout.njk or photo2pixel-page.njk so MCP documentation is rendered`);
      }
    });
  });
}

checkLanguageSets();
checkTranslationShape("homepage", homepage);
checkTranslationShape("t", t);
checkToolDataFiles();
checkHomepageToolTitles();
checkCategories();
checkToolPages();
checkA2aCapabilities();
checkA2aAgentCard();
checkMcpDocumentation();

if (errors.length) {
  console.error(`Structure check failed with ${errors.length} issue(s):`);
  errors.forEach((error) => console.error(`- ${error}`));
  process.exit(1);
}

console.log("Structure check passed.");
