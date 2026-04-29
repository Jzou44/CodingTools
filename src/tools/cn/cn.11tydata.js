var tData = require('../../_data/t');
var toolDataAll = require('../../_data/toolData');

module.exports = function () {
  var lang = 'cn';
  var t = tData[lang] || tData.en;
  var tdLang = toolDataAll[lang] || toolDataAll.en;

  var sidebarTitles = {};
  if (tdLang) {
    Object.keys(tdLang).forEach(function (slug) {
      if (tdLang[slug] && tdLang[slug].toolTitle) {
        sidebarTitles[slug] = tdLang[slug].toolTitle;
      }
    });
  }

  return {
    lang: lang,
    t: t,
    toolDataLookup: tdLang,
    sidebarToolTitles: sidebarTitles,
    eleventyComputed: {
      toolData: function (data) {
        return (data.toolDataLookup && data.toolId) ? (data.toolDataLookup[data.toolId] || {}) : {};
      },
      title: function (data) {
        var td = (data.toolDataLookup && data.toolId) ? (data.toolDataLookup[data.toolId] || {}) : {};
        return td.title || '';
      },
      description: function (data) {
        var td = (data.toolDataLookup && data.toolId) ? (data.toolDataLookup[data.toolId] || {}) : {};
        return td.description || '';
      },
      toolTitle: function (data) {
        var td = (data.toolDataLookup && data.toolId) ? (data.toolDataLookup[data.toolId] || {}) : {};
        return td.toolTitle || '';
      },
      toolDescription: function (data) {
        var td = (data.toolDataLookup && data.toolId) ? (data.toolDataLookup[data.toolId] || {}) : {};
        return td.toolDescription || '';
      },
      categoryName: function (data) {
        var td = (data.toolDataLookup && data.toolId) ? (data.toolDataLookup[data.toolId] || {}) : {};
        return td.categoryName || '';
      }
    }
  };
};
