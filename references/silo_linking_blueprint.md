# Silo Linking & Topic Cluster Blueprint (Silo 结构与内部权重流转法则)

> 解决新站“收录难、收录慢”的根本方法，是建立闭环的站内拓扑网络。
> 严禁让任何一篇文章成为没有链接出入的“孤岛页面（Orphan Page）”。

---

## 1. 经典三层金字塔架构 (3-Tier Silo Hierarchy)

```text
              [ 顶级类目核心页 (Pillar / Collection) ]
           /collections/golf-cart-seat-covers (DA 聚集地)
                              ▲
                 ┌────────────┴────────────┐
                 │                         │
      [ 品牌细分聚合页 (Sub-Silo) ]   [ 品牌细分聚合页 (Sub-Silo) ]
 /collections/club-car-seat-covers   /collections/evolution-seat-covers
                 ▲                         ▲
        ┌────────┴────────┐       ┌────────┴────────┐
        │                 │       │                 │
   [ 博客指南 A ]   [ 博客指南 B ] [ 博客指南 C ]   [ 博客指南 D ]
   (长尾技术文章)   (买家实测文章) (安装排坑教程)   (尺寸测量指南)
```

---

## 2. 内部链接三大铁律 (The 3 Hard Rules of Internal Linking)

1. **同 Silo 内部横向互相支撑 (Cross-linking within cluster)**：
   - 讨论《Evolution D5 座套安装》的文章，必须在正文自然链接到《Evolution D5 与 D3 尺寸差异》文章；
   - 严禁在同一段落无关联地跳跃到无关 Silo（如突然插入 Jeep 备胎罩链接）。
2. **每篇博客必须包含 1–2 个指向父级商业页的高权重锚文本链接**：
   - 锚文本必须包含精确事务性购买词；
   - 示例：`"If you're ready to upgrade your ride, browse our verified [Evolution D5 custom seat covers collection] with free US shipping."`
3. **精准锚文本与上下文相关性（No Generic Anchor Text）**：
   - ❌ 严禁使用：“Click here”, “Read more”, “This link” 作为锚文本；
   - ✅ 必须使用包含核心实体的描述语：“marine-grade Club Car Onward seat covers”, “step-by-step enclosure installation guide”.

---

## 3. 面包屑导航与结构化关联 (Breadcrumbs)
所有页面头部必须启用 BreadcrumbList Schema：
`Home > Golf Cart Accessories > Golf Cart Seat Covers > Evolution D5 Installation Guide`
确保 Google 爬虫在初次爬取时就能精确理解站点的层级拓扑关系。
