# Schema.org Structured Data Templates (Google 友好型结构化数据模板)

> Google 爬虫通过 JSON-LD 解析实体属性。
> 每篇 SEO 文章落地页底端**必须包含至少一种结构化数据**，以触发 SERP 富媒体结果（Rich Snippets）。

---

## 1. FAQPage Schema（适用于常见问答、选型答疑，出单与点击率极高）

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Do Evolution D5 seat covers fit older Club Car or EZGO models?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. The Evolution D5 features a proprietary sculpted high-back bucket seat contour with integrated armrest cutouts measuring 41.5 inches across, whereas standard Club Car DS cushions are flat and 39.5 inches wide. Universal covers will bunch up and fail to secure properly."
      }
    },
    {
      "@type": "Question",
      "name": "What is the best seat cover material for Florida heat and humidity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "3D Breathable Honeycomb Mesh is ideal for extreme sun and humidity. In our thermal imaging tests, honeycomb mesh maintained seat surface temperatures at 84°F under direct midday sunlight, compared to 112°F on factory marine-grade vinyl."
      }
    }
  ]
}
</script>
```

---

## 2. HowTo Schema（适用于安装教程、尺寸测量指南）

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to Measure and Install Custom Golf Cart Seat Covers in 4 Steps",
  "description": "A complete step-by-step guide to measuring your cart cushion and fastening custom slip-on seat covers without power tools.",
  "totalTime": "PT15M",
  "supply": [
    {
      "@type": "HowToSupply",
      "name": "Custom Fit Seat Cover Set"
    }
  ],
  "tool": [
    {
      "@type": "HowToTool",
      "name": "Tape Measure (Imperial Inches)"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Measure Cushion Dimensions",
      "text": "Measure total width from left outer edge to right outer edge across the widest point of the bottom cushion. Note whether front corners are rounded (3-inch radius) or square.",
      "url": "https://yourdomain.com/guides/installation#step1"
    },
    {
      "@type": "HowToStep",
      "name": "Slip Over Backrest First",
      "text": "Slide the backrest cover from the top down. Ensure the rear hook-and-loop velcro aligns with the factory mounting brackets.",
      "url": "https://yourdomain.com/guides/installation#step2"
    },
    {
      "@type": "HowToStep",
      "name": "Secure Bottom Cushion Straps",
      "text": "Thread the quick-release nylon buckle straps under the seat pan. Pull evenly from side to side until fabric sits completely wrinkle-free.",
      "url": "https://yourdomain.com/guides/installation#step3"
    }
  ]
}
</script>
```

---

## 3. Product & AggregateRating Schema（适用于单品推荐与合集导购）

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Custom Fit Breathable Golf Cart Seat Covers for Evolution D5",
  "image": [
    "https://yourdomain.com/images/evolution-d5-seat-cover-front.webp"
  ],
  "description": "Marine-grade 3D honeycomb mesh seat covers engineered specifically for Evolution D5 Maverick and Forester 4-passenger carts.",
  "sku": "EVO-D5-SC-01",
  "brand": {
    "@type": "Brand",
    "name": "CartArmor Pro"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://yourdomain.com/products/evolution-d5-seat-covers",
    "priceCurrency": "USD",
    "price": "89.00",
    "priceValidUntil": "2027-12-31",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "128"
  }
}
</script>
```
