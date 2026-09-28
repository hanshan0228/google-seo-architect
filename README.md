# Google SEO Architect (深度收录与抗 AI 降权内容引擎)

> 解决独立站出海 SEO 核心痛点：让 AI 写的深度文章真正被 Google 爬虫快速收录、获得高权威评级，并在 SERP 中触发富媒体（Rich Snippets）。

---

## 核心功能

1. **Anti-AI 质量门禁系统 (`scripts/lint_article.py`)**：
   - 自动扫描 60+ 个常见 AI 废话词（如 *In conclusion*, *Delve into*, *A testament to*, *综上所述* 等）；
   - 强制核验结构化对比数据表（杜绝空洞大话，注入独家信息增量）；
   - 强制校验 JSON-LD Schema 代码的 JSON 语法与有效性；
   - 校验段落节奏与层级标题。

2. **快速收录推流通道路由 (`scripts/submit_google_indexing.py`)**：
   - 支持 Google Indexing API 批量提交（Batch Request）；
   - 支持 IndexNow 协议（一键触达 Bing, Yandex）；
   - 支持无秘钥测试模拟（Dry-Run）。

3. **标准知识库 (`references/`)**：
   - `google_verification_standards.md`：谷歌需求符合度四阶验收标准（本地硬门禁、Rich Results Test、GSC 实盘、SERP 回测）；
   - `ai_fluff_blacklist.md`：AI 八股黑名单；
   - `schema_templates.md`：FAQPage, BreadcrumbList, HowTo, Product 规范结构化数据模板；
   - `silo_linking_blueprint.md`：Silo 拓扑内链设计蓝图。

---

## 快速使用

### 1. 质量门禁审计
```bash
python scripts/lint_article.py path/to/article.md
```

### 2. 模拟收录提交 (Dry-Run)
```bash
python scripts/submit_google_indexing.py --urls https://yoursite.com/guides/evolution-d5-guide --dry-run
```

---

## 生产级实战案例 / Production References

本套收录门禁与 Silo 拓扑模型已在以下开源与出海知识库项目中落地实践：

- **[Just My Socks Guide (跨境网络知识库与 SEO 拓扑实践)](https://github.com/justmysocks-guide)**
  - 核心主站：[justmysocks-guide/.github](https://github.com/justmysocks-guide/.github) (一级组织根域名借权，双语 E-E-A-T 实体落地页与结构化痛点解答)
  - 测速诊断工具：[jms-speedtest](https://github.com/justmysocks-guide/jms-speedtest) (Engineering-as-Marketing 实战，网络延迟与 AI 解锁体检)
  - 智能分流规则集：[clash-rules](https://github.com/justmysocks-guide/clash-rules) (Clash / Sing-box 精准分流规则提供者)

