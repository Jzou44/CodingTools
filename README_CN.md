<div align="center">

# Coding.Tools

### 开发者工具箱

**63 个免费、基于浏览器运行、重视隐私的开发者工具。**

无需注册。无需追踪。数据不会发送到服务器。所有工具都在浏览器中运行。

[![访问网站](https://img.shields.io/badge/访问-coding.tools-blue?style=for-the-badge)](https://coding.tools)
[![开源协议](https://img.shields.io/badge/协议-MIT-green?style=for-the-badge)](#开源协议)
[![多语言](https://img.shields.io/badge/语言-9-orange?style=for-the-badge)](#多语言支持)

<br/>

[English](README.md) | **中文**

</div>

---

## 为什么选择 Coding.Tools？

- **隐私优先**：工具全部在浏览器本地运行。
- **静态输出**：生产环境产物是纯 HTML、CSS、JavaScript 和静态资源。
- **多语言**：英文加 8 套本地化语言页面。
- **无前端框架运行时**：Eleventy 负责生成页面，工具逻辑使用原生 JavaScript。
- **翻译可校验**：`npm run check` 会检查页面覆盖、翻译结构、分类数量和本地化模板常见回归。

---

## 工具一览

| 分类 | 数量 | 功能 |
|------|-----:|------|
| 哈希与加密 | 8 | Base64、MD5、SHA-1/256/384/512、密码生成 |
| 数字转换 | 26 | 十六进制、十进制、二进制、八进制、ASCII、罗马数字、RGB/RGBA、分数、百分比 |
| 字符串与文本工具 | 8 | 文本编辑、正则测试/替换、单词与字符统计、大小写转换 |
| 格式化与压缩 | 14 | JSON、XML、HTML、CSS、JavaScript、SQL 格式化与压缩、JSON/XML 转换 |
| 图片工具 | 7 | PNG/JPEG 压缩、渐进式 JPEG、Photo2Pixel、图片转 Base64、EXIF 查看/移除 |

**63 个工具**，涵盖 **5 个分类**，支持 **9 种语言**。

---

## 快速开始

```bash
npm install
npm run dev
```

Eleventy 开发服务器运行在 [http://localhost:5500](http://localhost:5500)。

## 常用命令

```bash
npm run check          # 校验结构、i18n 覆盖、分类和本地化模板
npm run build          # 先运行 check，再构建静态站点到 dist/
npm run dev            # 在 localhost:5500 启动 Eleventy 开发服务器
npm run debug          # 带 debug 日志的 Eleventy 开发服务器
npm run docker:build   # 构建基于 nginx 的静态站点 Docker 镜像
npm run docker:run     # 在 localhost:8080 运行 Docker 镜像
npm run docker:stop    # 停止并删除本地 Docker 测试容器
npm run docker:test    # 构建并运行 Docker 镜像
```

仓库中没有 Node 生产服务器。部署时直接服务生成的 `dist/` 静态目录。

---

## 项目结构

```text
coding-tools/
├── .eleventy.js                 # Eleventy 配置
├── Dockerfile                   # 用于 dist/ 的静态 nginx 容器
├── package.json                 # npm 脚本和依赖
├── scripts/
│   └── check-structure.js       # 结构和 i18n 校验
├── src/
│   ├── index.njk                # 英文首页
│   ├── localized-index.njk      # 本地化首页生成器
│   ├── sitemap.xml.njk          # 覆盖所有语言和工具的 sitemap
│   ├── robots.txt.njk
│   ├── _includes/               # 布局、局部模板和宏
│   ├── _data/
│   │   ├── site.js              # 站点元数据和语言列表
│   │   ├── tools.json           # 工具元数据
│   │   ├── categoryDefinitions.json
│   │   ├── categories.js
│   │   ├── homepage.json        # 首页翻译
│   │   ├── t/                   # 按语言拆分的 UI 翻译
│   │   ├── t.js                 # 加载 t/*.json
│   │   ├── toolData/            # 按工具拆分的多语言内容
│   │   └── toolData.js          # 加载 toolData/*.json
│   ├── css/
│   │   ├── style.css
│   │   └── tool.css
│   ├── js/                      # 共享客户端工具和内置库
│   ├── assets/                  # favicon、图片、Photo2Pixel ONNX 模型
│   └── tools/
│       ├── *.njk                # 英文工具页面
│       ├── cn/ tw/ jp/ kr/      # CJK 本地化工具页面
│       └── fr/ de/ es/ pt/      # 欧洲语言本地化工具页面
└── dist/                        # 构建输出，git 忽略
```

**技术栈：** Eleventy v3、Nunjucks、自定义 CSS、原生 JavaScript。

---

## 多语言支持

支持语言：

| 语言 | 代码 | HTML lang |
|------|------|-----------|
| 英语 | `en` | `en` |
| 简体中文 | `cn` | `zh-CN` |
| 繁体中文 | `tw` | `zh-TW` |
| 日语 | `jp` | `ja` |
| 韩语 | `kr` | `ko` |
| 法语 | `fr` | `fr` |
| 德语 | `de` | `de` |
| 西班牙语 | `es` | `es` |
| 葡萄牙语 | `pt` | `pt` |

本地化工具页面在 frontmatter 中设置 `lang` 和 `toolId`，页面内容通过 `{{ t.ui.* }}` 和 `{{ toolData.* }}` 渲染。标题、描述、工具标题和分类名由 `src/_data/makeToolLangData.js` 从 `toolData` 计算。

不要在本地化页面中添加 `title`、`description`、`toolTitle`、`toolDescription`、`categoryName` 这类 frontmatter；它们会覆盖翻译数据，并会被 `npm run check` 拒绝。

---

## 校验

`npm run check` 会校验：

- `site.js` 中的每种语言都存在首页和 UI 翻译数据
- `tools.json` 中的每个工具都有对应的 `src/_data/toolData/<slug>.json`
- 每个 toolData 文件都有 9 种语言，且键和数组长度与英文基准一致
- 英文基准非空的本地化字段不能是空字符串
- 分类数量与实际工具数一致
- 英文和本地化工具模板都存在
- 本地化模板的 `lang`、`toolId` 和 permalink 正确
- 本地化模板不使用元数据 frontmatter 覆盖，也不包含已知硬编码英文 UI

`npm run build` 会通过 `prebuild` 自动先运行该校验。

---

## 添加或更新工具

1. 在 `src/_data/tools.json` 中添加或更新工具元数据。
2. 在 `src/_data/toolData/<slug>.json` 中添加或更新各语言内容。
3. 如需共享 UI 文案，在每个 `src/_data/t/<lang>.json` 中添加对应字段。
4. 在 `src/tools/<slug>.njk` 中创建或更新英文模板。
5. 在每个语言目录中创建或更新本地化模板。
6. 运行 `npm run check` 和 `npm run build`。

---

## 开源协议

MIT License。

---

<div align="center">

[访问 coding.tools](https://coding.tools)

</div>
