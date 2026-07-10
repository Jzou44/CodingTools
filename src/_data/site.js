function normalizeBaseUrl(value) {
  const candidate = (value || "https://coding.tools").replace(/\/+$/, "");
  return /^https?:\/\//.test(candidate) ? candidate : "https://coding.tools";
}

const baseUrl = normalizeBaseUrl(process.env.SITE_BASE_URL);

const languages = [
  { id: "en", htmlLang: "en", label: "English" },
  { id: "cn", htmlLang: "zh-CN", label: "中文" },
  { id: "tw", htmlLang: "zh-TW", label: "繁體" },
  { id: "jp", htmlLang: "ja", label: "日本語" },
  { id: "kr", htmlLang: "ko", label: "한국어" },
  { id: "fr", htmlLang: "fr", label: "Français" },
  { id: "de", htmlLang: "de", label: "Deutsch" },
  { id: "es", htmlLang: "es", label: "Español" },
  { id: "pt", htmlLang: "pt", label: "Português" }
];

function htmlLang(lang) {
  const match = languages.find((item) => item.id === (lang || "en"));
  return match ? match.htmlLang : "en";
}

function pathFor(lang, slug) {
  const currentLang = lang || "en";
  if (slug) {
    return currentLang === "en" ? `/${slug}.html` : `/${currentLang}/${slug}.html`;
  }
  return currentLang === "en" ? "/index.html" : `/${currentLang}/index.html`;
}

function absoluteUrl(path) {
  return `${baseUrl}${path || "/index.html"}`;
}

module.exports = {
  baseUrl,
  siteName: "Coding.Tools",
  assetVersion: "20260710-1",
  ogImage: "/assets/favicons/favicon-512x512.png",
  languages,
  languageIds: languages.map((item) => item.id),
  localizedLanguageIds: languages.filter((item) => item.id !== "en").map((item) => item.id),
  htmlLang,
  pathFor,
  absoluteUrl
};
