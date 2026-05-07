const tData = require("./t");
const toolDataAll = require("./toolData");

function dataForTool(data) {
  const toolId = data.toolId || data.activeTool || (data.page && data.page.fileSlug);
  const lang = data.lang || "en";
  const lookup = toolDataAll[lang] || toolDataAll.en || {};
  return toolId ? (lookup[toolId] || {}) : {};
}

function makeSidebarTitles(tdLang) {
  const sidebarTitles = {};

  if (tdLang) {
    Object.keys(tdLang).forEach((slug) => {
      if (tdLang[slug] && tdLang[slug].toolTitle) {
        sidebarTitles[slug] = tdLang[slug].toolTitle;
      }
    });
  }

  return sidebarTitles;
}

function makeToolLangData(lang) {
  return function () {
    const currentLang = lang || "en";
    const t = tData[currentLang] || tData.en;
    const tdLang = toolDataAll[currentLang] || toolDataAll.en;

    return {
      lang: currentLang,
      t,
      toolDataLookup: tdLang,
      sidebarToolTitles: makeSidebarTitles(tdLang),
      eleventyComputed: {
        toolId(data) {
          return data.toolId || data.activeTool || (data.page && data.page.fileSlug) || "";
        },
        activeTool(data) {
          return data.activeTool || data.toolId || (data.page && data.page.fileSlug) || "";
        },
        permalink(data) {
          const toolId = data.toolId || data.activeTool || (data.page && data.page.fileSlug);
          return toolId ? data.site.pathFor(currentLang, toolId) : data.permalink;
        },
        toolData(data) {
          return dataForTool(data);
        },
        title(data) {
          const td = dataForTool(data);
          return data.title || td.title || "";
        },
        description(data) {
          const td = dataForTool(data);
          return data.description || td.description || "";
        },
        toolTitle(data) {
          const td = dataForTool(data);
          return data.toolTitle || td.toolTitle || "";
        },
        toolDescription(data) {
          const td = dataForTool(data);
          return data.toolDescription || td.toolDescription || "";
        },
        categoryName(data) {
          const td = dataForTool(data);
          return data.categoryName || td.categoryName || "";
        }
      }
    };
  };
}

module.exports = makeToolLangData;
