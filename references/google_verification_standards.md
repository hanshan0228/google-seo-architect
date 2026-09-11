# Google Verification Standards & Acceptance Criteria (谷歌需求符合度验证与终审验收标准)

> 本标准为 `google-seo-architect` 生成内容的最高验收准绳。
> 任何交付的内容必须能够顺利通过以下四阶段的严格检验，确保不仅“机器代码合规”，更能真正进入 Google 核心索引并触发富媒体排名。

---

## 第一阶段：本地代码级自动化硬门禁（上线前，0成本机器拦截）

所有文章在发布前，必须在本地通过 `python scripts/lint_article.py <文件路径>` 自动化审查，达到 **100% PASS**：

1. **零 AI 模板词 (Anti-AI Cliché Gate)**：
   - 严禁出现 `In conclusion`, `Delve into`, `Navigating the landscape`, `A testament to` 等 60+ 个被 Google 算法标记的高频八股词；
   - 采用 **BLUF (Bottom Line Up Front)** 结构，开篇 50 字内直接给出搜索疑问的结论。
2. **绝对信息增量 (Information Gain Gate)**：
   - 必须包含至少 1 个专有物理数据对比表（如座套长宽深、厚度、实测降温数据）；
   - 严禁全篇只有空泛文字叙述。
3. **SERP 字符数精准卡尺 (Meta Dimensions Gate)**：
   - `meta_title`：严格控制在 **45–65 字符**（超出在 Google SERP 搜索结果中会被强行截断，过短权重不足）；
   - `meta_description`：严格控制在 **120–165 字符**（确保移动端与桌面端摘要完整展示主词）。
4. **SiteLinks 结构规范 (TOC Anchor Gate)**：
   - 必须包含带跳转锚点 `[...](#...)` 的 Table of Contents，为 Google 搜索结果生成子链（SiteLinks）铺平道路。
5. **结构化数据有效性 (Schema Syntax Gate)**：
   - 嵌入的 JSON-LD 代码必须通过 `json.loads` 深度语法树解析，100% 杜绝漏括号、多逗号等解析错误。

---

## 第二阶段：谷歌官方工具链真机验证（上线前终审验收）

本地代码审查通过后，必须通过谷歌官方提供的免费验证工具进行测试：

### 1. Google 官方富媒体测试 (Google Rich Results Test)
* **官方测试网址**：`https://search.google.com/test/rich-results`
* **测试方法**：
  - 点击“代码 (Code)”标签，粘贴文章生成的完整 HTML 源码（或直接输入已上线的 URL）；
  - 选择“Googlebot 智能手机”抓取模式；
* **验收通过标准**：
  - 页面状态栏显示绿色对勾：**`检测到有效项 (Valid items detected)`**；
  - 必须成功点亮两大卡片：
    - ✅ **`FAQ`（常见问题解答）**：识别出文章末尾的问答对，允许在搜索结果中展开折叠面板；
    - ✅ **`Breadcrumbs`（面包屑导航）**：识别出站点层级，允许在搜索结果网址上方展示清晰路径；
  - 存在 0 个“严重问题 (Critical issues)”。

### 2. Schema.org 国际标准校验 (Schema Markup Validator)
* **官方测试网址**：`https://validator.schema.org/`
* **验收通过标准**：
  - 语法树中 `FAQPage` 与 `BreadcrumbList` 属性解析完整，0 Errors，0 Warnings。

---

## 第三阶段：上线后 Google Search Console (GSC) 实盘状态验证

文章上线并推送到 Googlebot 后，在 GSC 后台进行抓取状态审计：

### 1. 实时网址检查 (Live URL Inspection)
在 GSC 顶部搜索框输入目标文章 URL，点击“测试实际网址”：
* **抓取状态**：必须返回 **`网址可编入 Google 索引 (URL is available to Google)`**；
* **移动设备易用性**：必须通过（我们的自适应表格 `.table-wrapper` 具备 `overflow-x: auto`，杜绝手机端横向拉伸撑破页面）；
* **用户声明的规范网址 (User-declared Canonical)** 与 **Google 选定的规范网址 (Google-selected Canonical)** 必须一致。

### 2. 收录终局判定（破除“已抓取未收录”魔咒）
* ❌ **未通过标准**：状态落入 **“已抓取 - 尚未编入索引 (Crawled - currently not indexed)”** —— 意味着被 Google 算法识别为缺乏独特价值或低质洗稿；
* ✅ **通过标准**：状态直接进入 **“已编入索引 (Indexed)”** —— 证明文章的专车参数与独特数据增量已被 Google 数据库完全采纳。

---

## 第四阶段：SERP 真实搜索结果回测（商业终极大考）

在页面上线 48–72 小时后进行实际效果核验：

1. **基础收录回测**：
   - 搜索指令：`site:yoursite.com/guides/evolution-d5-seat-covers-guide`
   - 确认标题完整、摘要清晰、无乱码。
2. **富媒体与排位表现**：
   - 在无痕窗口搜索目标长尾词（如 `evolution d5 seat covers fitment`）；
   - 观察搜索结果条目下方是否展现：
     - **展开式 FAQ 常见问答下拉菜单**；
     - **面包屑分类路径**；
     - **SiteLinks 快速跳转子链接**；
   - 只要触发以上富媒体元素，即代表文章已完美契合 Google 搜索引擎的一切技术与内容深度需求！
