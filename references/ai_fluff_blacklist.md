# AI Fluff & Buzzword Blacklist (物理禁用的 AI 套话与废话库)

> 本清单由 Google 核心算法反作弊更新与高质量人类内容编辑总结。
> 在任何 SEO 交付内容中，**严禁出现**以下词汇、短语与句式结构。
> `scripts/lint_article.py` 将对输出内容进行正则扫描，任何匹配均直接判定 `FAIL`！

---

## 1. 致命八股过渡与开头词（Throat-Clearing Openings & Transitions）
- `In conclusion`
- `To sum up` / `In summary` / `All in all`
- `Delve into` / `Let's delve`
- `Navigating the landscape` / `Navigating the world of`
- `A testament to`
- `In today's fast-paced world` / `In the fast-paced world`
- `It is crucial to note` / `It is important to remember`
- `Plays a crucial role` / `Plays a pivotal role`
- `A myriad of`
- `Tapestry` (如 a rich tapestry)
- `Beacon` / `Beacon of`
- `Look no further`
- `Ever-evolving` / `Ever-changing landscape`
- `Game-changer` / `Revolutionize` (滥用时)
- `Needless to say`
- `At the end of the day`
- `Without further ado`
- `Shed light on`
- `Treasure trove`
- `Buckle up`

---

## 2. 泛泛无物的空话套话（Hollow Claims & Generalities）
- `...is not just a..., it's a...` (Not just a cart, it's a lifestyle)
- `When it comes to [Topic]...`
- `Whether you are a beginner or a seasoned pro...`
- `In this comprehensive guide, we will explore...`
- `Have you ever wondered how to...`
- `One cannot overstate the importance of...`
- `Standing out in the crowded market...`
- `Unlocking the secrets of...`
- `Take your [item] to the next level...`
- `Embrace the future of...`

---

## 3. 中文对应禁用词（中文站写作红线）
- `综上所述` / `总而言之` / `总的来说`
- `不可否认的是` / `毋庸置疑的是`
- `值得一提的是` / `值得注意的是`
- `在当今快节奏的社会中`
- `不仅……更是……` (滥用排比套话)
- `画卷` / `浓墨重彩的一笔`
- `助力` / `赋能` (在技术评测/导购中泛滥使用)
- `带你一探究竟` / `让我们拭目以待`

---

## 4. 结构性禁用规范（Structural Dead Giveaways）
1. **禁止在文章开篇写 150 字以上的空洞背景介绍**：
   - 错误：从这项运动的历史、行业发展趋势开始扯起。
   - 正确：采用 **BLUF (Bottom Line Up Front)** 原则，第 1 句话直截了当解答用户的搜索疑问，直接摆出选型结论或对比表。
2. **禁止纯文字排版**：
   - 超过 300 单词的段落未设置分段、列表或加粗重点，直接判定违规。
   - 全文缺少对比数据表格（`<table>` 或 Markdown 表格）直接判定违规。
3. **禁止全篇无缺点吹捧**：
   - 任何产品推荐必须包含客观的“局限性（Limitations）”或“使用注意（Caveats）”，否则判定为虚假营销内容。
