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

checkLanguageSets();
checkTranslationShape("homepage", homepage);
checkTranslationShape("t", t);
checkToolDataFiles();
checkHomepageToolTitles();
checkCategories();
checkToolPages();

if (errors.length) {
  console.error(`Structure check failed with ${errors.length} issue(s):`);
  errors.forEach((error) => console.error(`- ${error}`));
  process.exit(1);
}

console.log("Structure check passed.");
