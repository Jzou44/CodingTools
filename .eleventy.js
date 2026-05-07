module.exports = function (eleventyConfig) {
  // Copy static assets to output
  eleventyConfig.addPassthroughCopy("src/css");
  eleventyConfig.addPassthroughCopy("src/js");
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy({ "src/assets/favicons/favicon.ico": "favicon.ico" });
  eleventyConfig.addWatchTarget("src/_data/");

  eleventyConfig.addTransform("removeBrokenCdnScripts", function (content, outputPath) {
    if (!outputPath || !outputPath.endsWith(".html")) return content;
    return content.replace(
      /\s*<script src="https:\/\/cdn\.jsdelivr\.net\/npm\/(?:html-minifier@4\.0\.0\/dist\/htmlminifier\.min\.js|jxon@2\.0\.0\/dist\/jxon\.min\.js)"><\/script>/g,
      ""
    );
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
