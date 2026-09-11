#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/compile_shopify_blog.py - Markdown to Shopify Blog Compiler & Packager
Transforms an SEO markdown article with YAML frontmatter into:
1. Clean, responsive Shopify-compatible HTML (with inlined styles, callouts, tables).
2. Ready-to-publish Shopify Admin API Article JSON payload (with SEO Metafields).
3. Ready for 1-click publishing or manual paste.
"""

import sys
import os
import re
import json
import argparse
import html
import io

# Ensure UTF-8 output on Windows
if sys.platform == "win32":
    if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

def markdown_to_shopify_html(md_body):
    """Converts common Markdown elements to styled Shopify blog HTML."""
    lines = md_body.split("\n")
    html_lines = []
    in_table = False
    table_lines = []

    def flush_table(tbl_lines):
        if not tbl_lines:
            return ""
        out = ['<div class="table-wrapper" style="overflow-x: auto; margin: 1.5rem 0;">']
        out.append('<table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; border: 1px solid #e2e8f0;">')
        header_parsed = False
        for line in tbl_lines:
            if re.match(r"^\|[- :|]+\|$", line.strip()):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not header_parsed:
                out.append('  <thead style="background-color: #f8fafc; border-bottom: 2px solid #cbd5e1;"><tr>')
                for c in cells:
                    out.append(f'    <th style="padding: 10px 14px; font-weight: 700; color: #1e293b;">{c}</th>')
                out.append('  </tr></thead><tbody>')
                header_parsed = True
            else:
                out.append('  <tr style="border-bottom: 1px solid #e2e8f0;">')
                for c in cells:
                    out.append(f'    <td style="padding: 10px 14px; color: #334155;">{c}</td>')
                out.append('  </tr>')
        out.append('</tbody></table></div>')
        return "\n".join(out)

    for line in lines:
        stripped = line.strip()
        # Table detection
        if stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            table_lines.append(stripped)
            continue
        elif in_table:
            html_lines.append(flush_table(table_lines))
            table_lines = []
            in_table = False

        # Headings
        if stripped.startswith("### "):
            html_lines.append(f'<h3 style="font-size: 1.25rem; font-weight: 700; color: #0f172a; margin-top: 1.5rem; margin-bottom: 0.5rem;">{stripped[4:]}</h3>')
        elif stripped.startswith("## "):
            html_lines.append(f'<h2 style="font-size: 1.5rem; font-weight: 700; color: #0f172a; margin-top: 2rem; margin-bottom: 0.75rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.3rem;">{stripped[3:]}</h2>')
        elif stripped.startswith("# "):
            html_lines.append(f'<h1 style="font-size: 2rem; font-weight: 800; color: #0f172a; margin-bottom: 1rem;">{stripped[2:]}</h1>')
        # Callout blockquote
        elif stripped.startswith("> "):
            callout = stripped[2:]
            html_lines.append(f'<div style="background-color: #f0fdf4; border-left: 4px solid #22c55e; padding: 12px 16px; margin: 1.5rem 0; border-radius: 0 6px 6px 0; color: #166534; font-size: 14px;"><strong>Note:</strong> {callout}</div>')
        # Lists
        elif stripped.startswith("- ") or stripped.startswith("* "):
            html_lines.append(f'<li style="margin-bottom: 6px; color: #334155;">{stripped[2:]}</li>')
        # Horizontal rule
        elif stripped in ["---", "***"]:
            html_lines.append('<hr style="border: 0; height: 1px; background: #e2e8f0; margin: 2rem 0;" />')
        # Paragraphs or empty
        elif stripped:
            # Inline bold/links
            text = stripped
            text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
            text = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2" style="color: #0284c7; text-decoration: underline;">\1</a>', text)
            html_lines.append(f'<p style="line-height: 1.7; color: #334155; margin-bottom: 1rem;">{text}</p>')

    if in_table:
        html_lines.append(flush_table(table_lines))

    return "\n".join(html_lines)

def compile_article(md_filepath, output_dir=None):
    if not os.path.exists(md_filepath):
        print(f"❌ File not found: {md_filepath}")
        return False

    with open(md_filepath, "r", encoding="utf-8", errors="ignore") as f:
        raw_text = f.read()

    # Parse YAML frontmatter
    fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n(.*)", raw_text, re.DOTALL)
    metadata = {}
    if fm_match:
        fm_text = fm_match.group(1)
        body_text = fm_match.group(2)
        for line in fm_text.split("\n"):
            if ":" in line:
                key, val = line.split(":", 1)
                metadata[key.strip()] = val.strip().strip("'\"")
    else:
        body_text = raw_text

    # Extract JSON-LD script blocks to preserve intact
    schemas = re.findall(r'(<script\s+type=["\']application/ld\+json["\']>.*?</script>)', body_text, re.DOTALL | re.IGNORECASE)
    cleaned_body = re.sub(r'<script\s+type=["\']application/ld\+json["\']>.*?</script>', '', body_text, flags=re.DOTALL | re.IGNORECASE)

    # Convert body to styled HTML
    converted_html = markdown_to_shopify_html(cleaned_body)

    # Append schemas at the end
    if schemas:
        converted_html += "\n\n<!-- Schema.org Rich Snippets -->\n" + "\n\n".join(schemas)

    base_name = os.path.splitext(os.path.basename(md_filepath))[0]
    out_dir = output_dir or os.path.dirname(md_filepath)

    # 1. Output compiled HTML
    html_out_path = os.path.join(out_dir, f"{base_name}_shopify.html")
    with open(html_out_path, "w", encoding="utf-8") as f:
        f.write(converted_html)

    # 2. Output Shopify Admin API JSON Payload
    shopify_payload = {
        "article": {
            "title": metadata.get("meta_title", base_name.replace("-", " ").title()),
            "author": metadata.get("author", "Editorial Team"),
            "tags": metadata.get("primary_keyword", ""),
            "body_html": converted_html,
            "summary_html": metadata.get("meta_description", ""),
            "metafields": [
                {
                    "key": "title_tag",
                    "value": metadata.get("meta_title", ""),
                    "type": "single_line_text_field",
                    "namespace": "global"
                },
                {
                    "key": "description_tag",
                    "value": metadata.get("meta_description", ""),
                    "type": "single_line_text_field",
                    "namespace": "global"
                }
            ]
        }
    }

    json_out_path = os.path.join(out_dir, f"{base_name}_shopify_payload.json")
    with open(json_out_path, "w", encoding="utf-8") as f:
        json.dump(shopify_payload, f, indent=2, ensure_ascii=False)

    print("=" * 75)
    print("🎉 Shopify Blog Compilation & Packaging Complete!")
    print(f"📄 Target HTML:    {html_out_path}")
    print(f"📦 API Payload:    {json_out_path}")
    print("=" * 75)
    return True

def main():
    parser = argparse.ArgumentParser(description="Compile SEO Markdown to Shopify-compatible Blog HTML and API JSON payload.")
    parser.add_argument("file", help="Path to markdown article")
    parser.add_argument("--out-dir", help="Output directory (defaults to article dir)")
    args = parser.parse_args()

    compile_article(args.file, args.out_dir)

if __name__ == "__main__":
    main()
