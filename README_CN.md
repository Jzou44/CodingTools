<div align="center">

# Coding.Tools

### 开发者工具箱

**62+ 免费、基于浏览器的开发者工具，保护您的隐私。**

无需注册。无需追踪。数据不会发送到服务器。一切在浏览器中运行。

[![访问网站](https://img.shields.io/badge/访问-coding.tools-blue?style=for-the-badge)](https://coding.tools)
[![开源协议](https://img.shields.io/badge/协议-MIT-green?style=for-the-badge)](#开源协议)
[![多语言](https://img.shields.io/badge/语言-9-orange?style=for-the-badge)](#-多语言支持)

<br/>

[English](README.md) | **中文**

</div>

---

## 为什么选择 Coding.Tools？

大多数在线开发者工具充斥着广告、要求注册，或将您的数据发送到远程服务器。Coding.Tools 与众不同：

- **隐私优先** — 所有工具 100% 在浏览器中运行。您的代码、密码和数据永远不会离开您的设备。
- **零门槛** — 无需注册、无需 API 密钥、无需等待。打开即用。
- **精美设计** — 简洁的界面，每个工具类别都有独特的配色方案。
- **真正的多语言** — 完整支持 9 种语言，不仅仅是翻译标签。
- **永久免费** — 开源项目，无付费层级，无隐藏费用。

---

## 工具一览

| 分类 | 数量 | 功能 |
|------|-----:|------|
| 哈希与加密 | 8 | Base64、MD5、SHA-1/256/384/512、密码生成器 |
| 数字转换 | 26 | 十六进制、十进制、二进制、八进制、ASCII、罗马数字、RGB、分数 |
| 字符串与文本 | 8 | 正则测试、字数统计、大小写转换、文本编辑器 |
| 格式化与压缩 | 14 | JSON、XML、HTML、CSS、JavaScript、SQL 格式化与压缩 |
| 图片工具 | 6 | PNG/JPEG 压缩、EXIF 查看/移除、图片转 Base64 |

**62 个工具**，涵盖 **5 个分类**，支持 **9 种语言**。

---

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/your-username/coding-tools.git
cd coding-tools

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

在浏览器中打开 [http://localhost:5500](http://localhost:5500)。

### 其他命令

```bash
npm run build          # 构建静态站点到 dist/ 目录
node server.js         # 生产环境服务器（在 5500 端口提供 dist/ 服务）
```

---

## 项目结构

```
coding.tools
├── .eleventy.js           # Eleventy 配置文件
├── server.js              # 生产环境静态文件服务器
├── src/
│   ├── index.njk          # 首页模板
│   ├── _includes/         # 布局和局部模板
│   │   ├── base.njk       # 基础 HTML 结构
│   │   ├── navbar.njk     # 导航栏
│   │   ├── sidebar.njk    # 工具侧边栏
│   │   └── tool-layout.njk # 工具页面布局
│   ├── _data/             # 工具数据和翻译
│   │   ├── tools.json     # 工具定义
│   │   ├── t.json         # UI 翻译
│   │   └── toolData.json  # 工具内容翻译
│   └── tools/             # 工具页面模板
│       ├── *.njk          # 英文工具
│       ├── cn/            # 简体中文
│       ├── jp/            # 日语
│       ├── kr/            # 韩语
│       └── ...            # 更多语言
├── css/                   # 样式表
├── js/                    # 客户端 JavaScript
└── dist/                  # 生成的输出
```

**技术栈：** Eleventy v3 + Nunjucks + 原生 JS — 无框架，无冗余。

---

## 多语言支持

Coding.Tools 支持您的语言：

| | 语言 | 代码 | | 语言 | 代码 |
|---|----------|------|---|----------|------|
| 🇺🇸 | 英语 | `en` | 🇫🇷 | 法语 | `fr` |
| 🇨🇳 | 简体中文 | `cn` | 🇩🇪 | 德语 | `de` |
| 🇹🇼 | 繁体中文 | `tw` | 🇪🇸 | 西班牙语 | `es` |
| 🇯🇵 | 日语 | `jp` | 🇧🇷 | 葡萄牙语 | `pt` |
| 🇰🇷 | 韩语 | `kr` | | | |

每种语言都有完整的工具描述、分步指南和 UI 元素翻译——不仅仅是标签。

---

## 工具详情

### 哈希与加密

生成哈希值、编码数据、创建安全密码——全部离线完成。

`Base64 编码` `Base64 解码` `MD5 生成器` `SHA1 生成器` `SHA256 生成器` `SHA384 生成器` `SHA512 生成器` `密码生成器`

### 数字转换

即时转换不同数字系统，实时显示结果。

`十六进制 ↔ 十进制` `八进制 ↔ 十进制` `二进制 ↔ 十进制` `二进制 ↔ 十六进制` `ASCII 表` `十六进制 ↔ ASCII` `二进制 ↔ 文本` `分数 ↔ 十进制` `百分比 ↔ 十进制` `十六进制 ↔ RGB` `罗马数字`

### 字符串与文本工具

为开发者和写作者提供的强大文本处理工具。

`文本编辑器` `正则测试器` `正则替换` `字数统计` `字符统计` `大小写转换` `文本反转` `数字转文字`

### 格式化与压缩

一键美化或压缩代码。

`JSON` `XML` `HTML` `CSS` `JavaScript` `SQL` — 每个都有格式化和压缩选项，还有 `JSON ↔ XML` 转换。

### 图片工具

直接在浏览器中处理图片。无需上传。

`PNG 压缩` `JPEG 压缩` `渐进式 JPEG` `图片转 Base64` `EXIF 查看器` `EXIF 移除器`

---

## 参与贡献

欢迎贡献！无论是添加新工具、修复 bug，还是改进翻译。

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-tool`)
3. 提交更改 (`git commit -m '添加新工具'`)
4. 推送到分支 (`git push origin feature/amazing-tool`)
5. 创建 Pull Request

### 添加新工具

1. 在 `src/_data/tools.json` 中添加工具元数据
2. 在 `src/tools/your-tool.njk` 中创建工具模板
3. 在 `src/_data/t.json` 和 `src/_data/toolData.json` 中添加翻译
4. 在各语言子目录中创建本地化版本

---

## 开源协议

MIT 协议 — 随意使用。

---

<div align="center">

**为重视隐私和简洁的开发者精心打造。**

[访问 coding.tools](https://coding.tools)

</div>
