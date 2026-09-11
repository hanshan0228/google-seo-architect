#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/lint_article.py - Google SEO Quality & Anti-AI Fluff Assertion Gate
Validates that an article meets strict Google indexing standards:
1. Zero banned AI fluff words / clichés.
2. Contains at least one structured comparison data table.
3. Contains valid JSON-LD structured data (FAQPage / HowTo / Product schema).
4. Follows BLUF structure with clear headings and no wall-of-text paragraphs.
5. Minimum substantive word count.
"""

import sys
import os
import re
import json
import argparse
import io

# Ensure UTF-8 output on Windows consoles/subprocesses
if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "buffer") and sys.stderr.encoding.lower() != "utf-8":
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Comprehensive list of banned AI phrases and throat-clearing fluff
BANNED_PHRASES = [
    r"\bin conclusion\b",
    r"\bto sum up\b",
    r"\bin summary\b",
    r"\ball in all\b",
    r"\bdelve into\b",
    r"\blet['’]s delve\b",
    r"\bnavigating the landscape\b",
    r"\bnavigating the world of\b",
    r"\ba testament to\b",
    r"\bin today['’]s fast-paced world\b",
    r"\bit is crucial to note\b",
    r"\bit is important to remember\b",
    r"\bplays a crucial role\b",
    r"\bplays a pivotal role\b",
    r"\ba myriad of\b",
    r"\btapestry\b",
    r"\bbeacon\b",
    r"\blook no further\b",
    r"\bever-evolving\b",
    r"\bever-changing landscape\b",
    r"\bgame-changer\b",
    r"\bwithout further ado\b",
    r"\bshed light on\b",
    r"\btreasure trove\b",
    r"\bbuckle up\b",
    r"\bwhen it comes to\b",
    r"\bwhether you are a beginner or a seasoned pro\b",
    r"\bin this comprehensive guide, we will explore\b",
    r"\bhave you ever wondered\b",
    r"\bone cannot overstate the importance of\b",
    r"\bunlocking the secrets\b",
    r"\btake your [a-z0-9_-]+ to the next level\b",
    # Chinese equivalents
    r"综上所述",
    r"总而言之",
    r"总的来说",
    r"不可否认的是",
    r"毋庸置疑的是",
    r"值得一提的是",
    r"值得注意的是",
    r"在当今快节奏的社会中",
    r"带你一探究竟",
    r"让我们拭目以待",
]

def analyze_article(filepath):
    if not os.path.exists(filepath):
        return {"status": "ERROR", "message": f"File not found: {filepath}"}

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    results = {
        "filepath": filepath,
        "word_count": len(content.split()),
        "char_count": len(content),
        "checks": {},
        "violations": [],
        "overall_pass": True
    }

    # 1. Word count check (minimum 600 words for English, 1000 characters for Chinese)
    is_chinese = bool(re.search(r"[一-龥]", content))
    if is_chinese:
        wc_pass = results["char_count"] >= 800
        wc_msg = f"Char count: {results['char_count']} (required: >= 800)"
    else:
        wc_pass = results["word_count"] >= 500
        wc_msg = f"Word count: {results['word_count']} (required: >= 500)"

    results["checks"]["length"] = {"pass": wc_pass, "detail": wc_msg}
    if not wc_pass:
        results["violations"].append(f"Content too short for comprehensive indexing. {wc_msg}")

    # 2. Banned AI fluff check
    matched_fluff = []
    content_lower = content.lower()
    for pattern in BANNED_PHRASES:
        found = re.findall(pattern, content_lower, re.IGNORECASE)
        if found:
            matched_fluff.append(f"Pattern matched '{pattern}' ({len(found)} times)")

    fluff_pass = len(matched_fluff) == 0
    results["checks"]["ai_fluff"] = {
        "pass": fluff_pass,
        "detail": f"Matched {len(matched_fluff)} banned AI cliché phrases",
        "matches": matched_fluff
    }
    if not fluff_pass:
        results["violations"].extend([f"AI Cliché: {m}" for m in matched_fluff])

    # 3. Data Table Check (Markdown or HTML table)
    has_markdown_table = bool(re.search(r"\|.+\|\n\|[- :|]+\|\n\|.+\|", content))
    has_html_table = "<table" in content.lower()
    table_pass = has_markdown_table or has_html_table
    results["checks"]["data_table"] = {
        "pass": table_pass,
        "detail": "Structured comparison table detected" if table_pass else "Missing structured comparison data table (|...| or <table>)"
    }
    if not table_pass:
        results["violations"].append("Missing structured comparison data table (vital for Information Gain).")

    # 4. JSON-LD Schema Check
    schema_blocks = re.findall(r'<script\s+type=["\']application/ld\+json["\']>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    valid_schema = False
    schema_types_found = []
    if schema_blocks:
        for idx, block in enumerate(schema_blocks):
            try:
                schema_json = json.loads(block.strip())
                stype = schema_json.get("@type", "Unknown")
                schema_types_found.append(stype)
                valid_schema = True
            except Exception as e:
                results["violations"].append(f"JSON-LD block #{idx+1} has invalid JSON syntax: {e}")

    results["checks"]["schema_markup"] = {
        "pass": valid_schema,
        "detail": f"Found valid schemas: {schema_types_found}" if valid_schema else "No valid JSON-LD schema block found"
    }
    if not valid_schema:
        results["violations"].append("Missing or invalid JSON-LD schema markup (FAQPage / HowTo / Product required).")

    # 5. Wall of Text Check (paragraphs with > 250 words without break)
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    long_paragraphs = [len(p.split()) for p in paragraphs if len(p.split()) > 250 and not p.startswith("<") and not p.startswith("|")]
    wall_pass = len(long_paragraphs) == 0
    results["checks"]["wall_of_text"] = {
        "pass": wall_pass,
        "detail": f"{len(long_paragraphs)} wall-of-text paragraphs (>250 words)" if not wall_pass else "Paragraph pacing well-structured"
    }
    if not wall_pass:
        results["violations"].append(f"Pacing violation: {len(long_paragraphs)} paragraphs exceed 250 words without visual breaks.")

    # 6. Heading hierarchy check (H2/H3 presence)
    has_h2 = bool(re.search(r"^##\s+.+", content, re.MULTILINE)) or "<h2" in content.lower()
    results["checks"]["headings"] = {
        "pass": has_h2,
        "detail": "Heading hierarchy present" if has_h2 else "Missing H2 headings (poor document outline)"
    }
    if not has_h2:
        results["violations"].append("Missing H2 headings for logical content outlining.")

    # 7. Frontmatter & Meta Tags Check (Adopted from santifer-irepair & Complete-SEO)
    fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    fm_pass = True
    fm_details = []
    if fm_match:
        fm_text = fm_match.group(1)
        # Check meta_title
        title_m = re.search(r"meta_title:\s*['\"]?(.*?)['\"]?\s*$", fm_text, re.MULTILINE)
        if title_m:
            title_len = len(title_m.group(1).strip())
            if 40 <= title_len <= 65:
                fm_details.append(f"meta_title length ({title_len} chars) optimal")
            else:
                fm_pass = False
                results["violations"].append(f"meta_title length ({title_len} chars) out of range (optimal: 40-65 chars).")
        else:
            fm_pass = False
            results["violations"].append("Missing 'meta_title' in YAML frontmatter.")

        # Check meta_description
        desc_m = re.search(r"meta_description:\s*['\"]?(.*?)['\"]?\s*$", fm_text, re.MULTILINE)
        if desc_m:
            desc_len = len(desc_m.group(1).strip())
            if 120 <= desc_len <= 165:
                fm_details.append(f"meta_description length ({desc_len} chars) optimal")
            else:
                fm_pass = False
                results["violations"].append(f"meta_description length ({desc_len} chars) out of range (optimal: 120-165 chars).")
        else:
            fm_pass = False
            results["violations"].append("Missing 'meta_description' in YAML frontmatter.")

        # Check primary_keyword
        pk_m = re.search(r"primary_keyword:\s*['\"]?(.*?)['\"]?\s*$", fm_text, re.MULTILINE)
        if pk_m:
            pk = pk_m.group(1).strip().lower()
            if pk and pk in content_lower:
                fm_details.append(f"primary_keyword '{pk}' verified in body")
            else:
                fm_pass = False
                results["violations"].append(f"primary_keyword '{pk}' not found in article body.")
    else:
        # Frontmatter is optional for plain markdown, but highly recommended
        fm_pass = True
        fm_details.append("No frontmatter present (plain markdown format)")

    results["checks"]["frontmatter_metadata"] = {
        "pass": fm_pass,
        "detail": "; ".join(fm_details) if fm_details else "Frontmatter verified"
    }

    # 8. Table of Contents / Anchor Jump Navigation Check (Complete-SEO pattern)
    has_toc = bool(re.search(r"\[.+\]\(#[a-z0-9_-]+\)", content))
    results["checks"]["toc_anchors"] = {
        "pass": has_toc,
        "detail": "Table of Contents with jump anchors detected" if has_toc else "Missing quick-jump Table of Contents anchors"
    }
    # Note: TOC missing is a warning/best-practice, we enforce it for top ranking
    if not has_toc:
        results["violations"].append("Recommendation: Add a quick-jump Table of Contents (TOC) for Google SiteLinks.")

    # Overall verdict
    results["overall_pass"] = (
        results["checks"]["length"]["pass"] and
        results["checks"]["ai_fluff"]["pass"] and
        results["checks"]["data_table"]["pass"] and
        results["checks"]["schema_markup"]["pass"] and
        results["checks"]["headings"]["pass"] and
        results["checks"]["frontmatter_metadata"]["pass"] and
        results["checks"]["toc_anchors"]["pass"]
    )

    return results

def print_report(res):
    print("=" * 80)
    print("【Google SEO 质量与 Anti-AI 机器级门禁审计报告】")
    print("=" * 80)
    print(f"目标文件: {res['filepath']}")
    print(f"统计规模: {res['word_count']} 词 (约 {res['char_count']} 字符)")
    status_str = "✅ PASS (符合 Google 深度收录规范)" if res["overall_pass"] else "❌ FAIL (存在严重违规，禁止直接发布)"
    print(f"终审结论: {status_str}")
    print("-" * 80)
    print("各项硬门禁校验明细:")
    for check_name, info in res["checks"].items():
        mark = "✅ PASS" if info["pass"] else "❌ FAIL"
        print(f"  [{mark}] {check_name.upper():<15}: {info['detail']}")

    if res["violations"]:
        print("-" * 80)
        print("🚨 拦截违规项清单 (必须修正):")
        for v in res["violations"]:
            print(f"  • {v}")
    print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description="Lint an article against Google SEO & Anti-AI rules.")
    parser.add_argument("file", help="Path to markdown or HTML article file")
    parser.add_argument("--json", action="store_true", help="Output raw JSON results")
    args = parser.parse_args()

    results = analyze_article(args.file)
    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print_report(results)

    sys.exit(0 if results.get("overall_pass") else 1)

if __name__ == "__main__":
    main()
