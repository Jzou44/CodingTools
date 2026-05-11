const site = require("./src/_data/site");
const toolDataAll = require("./src/_data/toolData");

function stripHtml(value) {
  return String(value || "").replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
}

function jsonForHtml(value) {
  return JSON.stringify(value).replace(/</g, "\\u003c").replace(/>/g, "\\u003e").replace(/&/g, "\\u0026");
}

function findCategory(categories, categoryId) {
  return (categories || []).find((category) => category.id === categoryId) || {};
}

function makeToolJsonLd(lang, slug, title, description, toolTitle, categoryName, categoryId, categories) {
  const currentLang = lang || "en";
  const pagePath = site.pathFor(currentLang, slug);
  const pageUrl = site.absoluteUrl(pagePath);
  const homeUrl = site.absoluteUrl(site.pathFor(currentLang));
  const category = findCategory(categories, categoryId);
  const td = (toolDataAll[currentLang] && toolDataAll[currentLang][slug]) || (toolDataAll.en && toolDataAll.en[slug]) || {};
  const displayTitle = toolTitle || td.toolTitle || title;
  const displayDescription = description || td.description || td.toolDescription;
  const displayCategory = categoryName || td.categoryName || category.name || "";
  const graph = [
    {
      "@type": "BreadcrumbList",
      itemListElement: [
        {
          "@type": "ListItem",
          position: 1,
          name: currentLang === "en" ? "Home" : "Coding.Tools",
          item: homeUrl
        },
        {
          "@type": "ListItem",
          position: 2,
          name: displayCategory,
          item: `${homeUrl}#${categoryId || ""}`
        },
        {
          "@type": "ListItem",
          position: 3,
          name: displayTitle,
          item: pageUrl
        }
      ]
    },
    {
      "@type": "WebApplication",
      name: displayTitle,
      description: displayDescription,
      url: pageUrl,
      applicationCategory: displayCategory || "DeveloperApplication",
      operatingSystem: "Any",
      browserRequirements: "Requires JavaScript",
      offers: {
        "@type": "Offer",
        price: "0",
        priceCurrency: "USD"
      }
    }
  ];

  const steps = Array.isArray(td.steps) ? td.steps : [];
  if (steps.length > 0) {
    graph.push({
      "@type": "HowTo",
      name: td.howToUse ? `${stripHtml(td.howToUse)}: ${displayTitle}` : `How to use ${displayTitle}`,
      description: displayDescription,
      step: steps.map((step, index) => ({
        "@type": "HowToStep",
        position: index + 1,
        text: stripHtml(step)
      }))
    });
  }

  return {
    "@context": "https://schema.org",
    "@graph": graph
  };
}

function makeHomeJsonLd(lang, title, description) {
  const currentLang = lang || "en";
  const pageUrl = site.absoluteUrl(site.pathFor(currentLang));
  return {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "Organization",
        name: site.siteName,
        url: site.baseUrl,
        logo: site.absoluteUrl(site.ogImage)
      },
      {
        "@type": "WebSite",
        name: site.siteName,
        url: pageUrl,
        inLanguage: site.htmlLang(currentLang),
        description: description || title
      }
    ]
  };
}

module.exports = function (eleventyConfig) {
  // Copy static assets to output
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/js");
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy({ "src/assets/favicons/favicon.ico": "favicon.ico" });
  eleventyConfig.addWatchTarget("src/_data/");

  eleventyConfig.addFilter("htmlLang", function (lang) {
    return site.htmlLang(lang);
  });

  eleventyConfig.addFilter("pathFor", function (lang, slug) {
    return site.pathFor(lang, slug);
  });

  eleventyConfig.addFilter("absoluteUrl", function (path) {
    return site.absoluteUrl(path);
  });

  eleventyConfig.addFilter("json", function (value) {
    return JSON.stringify(value, null, 2);
  });

  eleventyConfig.addShortcode("seoJsonLd", function (pageType, lang, slug, title, description, toolTitle, categoryName, categoryId, categories) {
    const data = pageType === "tool"
      ? makeToolJsonLd(lang, slug, title, description, toolTitle, categoryName, categoryId, categories)
      : makeHomeJsonLd(lang, title, description);
    return `<script type="application/ld+json">${jsonForHtml(data)}</script>`;
  });

  // Global data available in all templates
  eleventyConfig.addGlobalData("currentYear", function () {
    return new Date().getFullYear();
  });

  return {
    dir: {
      input: "src",
      output: "dist",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["njk", "html"],
    htmlTemplateEngine: "njk",
    dataTemplateEngine: "njk"
  };
};
