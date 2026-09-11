---
name: google-seo-architect
description: Google SEO 深度收录与高排名内容生产引擎。基于 E-E-A-T、信息增量（Information Gain）与机器级硬门禁，生成不被 Google 降权、自带结构化数据与对比表的工业级高质量文章。
---

# Google SEO Architect (深度收录与抗 AI 降权内容引擎)

> **专为 Shopify / 独立站出海量身打造的高质量 Google SEO 内容流水线。**
> 彻底击碎 Google 核心算法更新中的“已发现未编入索引（Discovered - currently not indexed）”困境。
> 强制注入真实实体参数、独家对比表与 Schema.org 结构化数据，严密过滤 AI 模板废话。

---

## 触发关键词 (Triggers)

- 写SEO文章、SEO内容、谷歌收录、写博客、博客规划、Google SEO、EEAT、E-E-A-T
- Schema生成、结构化数据、JSON-LD、提交收录、Google Indexing API、IndexNow
- Programmatic SEO、信息增量、Information Gain、Anti-AI、防AI降权

---

## 六大子指令敏捷路由 (Sub-Commands)

### 1. `/google-seo-architect write <关键词/主题>`
* **功能**：自动检索或提取专车参数、独家痛点与长尾词，生成符合 Google 顶尖索引标准的深度指南；
* **刚性要求**：
  - 采用 **BLUF (Bottom Line Up Front)** 结构，开篇 50 字内给出直接答案；
  - 必须包含至少 1 个结构化对比数据表（`|...|` Markdown 表格）；
  - 必须包含合法的 JSON-LD（`FAQPage` + `BreadcrumbList`）Schema 代码块；
  - 包含规范 Frontmatter 元数据与带锚点的目录导航（TOC）；
  - 自动调用后台 `scripts/lint_article.py` 自检，**未通过门禁物理禁止向用户交付**！

### 2. `/google-seo-architect lint <文件路径>`
* **功能**：运行机器级代码断言脚本，对指定 Markdown/HTML 文章进行全维度质量审计；
* **校验项**：词数规模、60+ 个 AI 模板黑名单词扫描、表格存在性、JSON-LD 语法合法性、Frontmatter 字符数、TOC 锚点。

### 3. `/google-seo-architect blueprint <车型名称> [--width W] [--depth D] [--radius R]`
* **功能**：调用 `scripts/generate_blueprint_svg.py` 自动生成工业级深色技术线框图（SVG 矢量），提供极高权重的 Google 图片搜索资产与独家实测证据。

### 4. `/google-seo-architect export-shopify <Markdown文件>`
* **功能**：调用 `scripts/compile_shopify_blog.py`，一键编译为自带内联样式、响应式表格与双 Schema 的 Shopify 兼容 HTML，并生成带有全局 SEO Metafields 的 Admin API JSON 载荷。

### 5. `/google-seo-architect schema <faq|howto|product|breadcrumb>`
* **功能**：根据输入的产品信息或问答对，生成完全符合 Schema.org 标准的 JSON-LD 代码块。

### 6. `/google-seo-architect index <URL列表>`
* **功能**：调用 `scripts/submit_google_indexing.py`，向 Google Indexing API（100条自动批处理）或 IndexNow 提交新发布页面，带 200 配额熔断守卫。

---

## 核心刚性门禁 (The 4 Hard Gates)

```text
════════════════════════════════════════════════════════════════════════════════
【Google SEO Architect 机器级硬门禁】
Gate 1: 绝对零 AI 模板词 (Zero Banned Words - 严格遵循 ai_fluff_blacklist.md)
Gate 2: 绝对信息增量 (Information Gain - 必须包含多维实测对比数据表与SVG线框图)
Gate 3: 实体结构化标记 (Valid JSON-LD Schema - 必须包含可解析的 FAQ/Breadcrumb)
Gate 4: 交付前静默自检 (Pre-Delivery Self-Lint - 必须经 lint_article.py 返回 PASS)
════════════════════════════════════════════════════════════════════════════════
```

---

## 谷歌官方需求验证四阶标准 (Google Verification Standards)

> 详见底层完整标准文档：`references/google_verification_standards.md`

每篇交付的文章必须满足以下**四阶段完整闭环验证**：
1. **阶段一（本地硬门禁）**：运行 `lint_article.py`，确保 Meta 字符数（Title 45-65, Desc 120-165）、TOC 锚点、表格、Schema、零 AI 八股词 100% PASS；
2. **阶段二（谷歌官方测试）**：通过 **Google Rich Results Test**（`search.google.com/test/rich-results`），成功点亮 `FAQ` 与 `Breadcrumbs` 绿色有效卡片；
3. **阶段三（GSC 实盘抓取）**：在 Google Search Console 通过 Live URL 测试，最终收录状态必须直接进入 **`Indexed (已编入索引)`**，坚决破除 `Crawled - currently not indexed` 魔咒；
4. **阶段四（SERP 真实回测）**：上线 72 小时后，通过 `site:` 指令与主词搜索，验证搜索结果下方是否成功展现展开式问答折叠栏与 SiteLinks 子链。

---

## 交付前强制自检工作流 (Mandatory Pre-Delivery Loop)

每次为用户撰写完任何 SEO 文章后，**严禁直接交卷！必须执行以下自闭环闭环动作**：
1. 将文章存盘为 `.md` 文件；
2. 执行校验：`python C:\Users\hanzhe1\.claude\skills\google-seo-architect\scripts\lint_article.py <文件路径>`；
3. **若返回 FAIL**：立即在当前轮次就地重写违规段落，直到返回 `PASS`；
4. **交付成果**：向用户输出完整文章，并附带后台机器门禁审计卡片！
