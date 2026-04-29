module.exports = function (eleventyConfig) {
  // Copy static assets to output
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/js");
  eleventyConfig.addWatchTarget("src/_data/");

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
