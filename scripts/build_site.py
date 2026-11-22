import re
import shutil
from pathlib import Path
import markdown

SRC_DIR = Path("docs")
OUT_DIR = Path("_site")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; line-height: 1.7; max-width: 1100px; margin: 0 auto; padding: 24px; color: #24292f; }}
    table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
    th, td {{ border: 1px solid #d0d7de; padding: 8px 12px; text-align: left; }}
    th {{ background-color: #f6f8fa; }}
    img {{ max-width: 100%; height: auto; }}
  </style>
  <script>
    window.MathJax = {{
      tex: {{ inlineMath: [['$', '$']], displayMath: [['$$', '$$']], processEscapes: true }}
    }};
  </script>
  <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
{body}
</body>
</html>
"""

def md_url_to_html(url: str) -> str:
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url):
        return url
    return re.sub(r'\.md(?=$|[?#])', '.html', url)

def convert_md_to_html(md_text: str) -> str:
    math_blocks = []

    def push_math(tex_str: str) -> str:
        math_blocks.append(tex_str)
        return f"@@MATH_{len(math_blocks)-1}@@"

    # 1. ブロック数式 $$...$$ とインライン数式 $`...`$ をHTML変換前に退避
    protected = re.sub(r'\$\$.*?\$\$', lambda m: push_math(m.group(0)), md_text, flags=re.DOTALL)
    protected = re.sub(r'\$`([^`]+)`\$', lambda m: push_math(f"${m.group(1)}$"), protected)

    # 2. Markdown → HTML 変換
    html = markdown.markdown(protected, extensions=['tables', 'fenced_code'])

    # 3. 退避した数式を復元
    for idx, math_str in enumerate(math_blocks):
        html = html.replace(f"@@MATH_{idx}@@", math_str)

    # 4. <table>内の [text](url) や .md リンクを <a> タグ & .html に変換
    def replace_md_link(match):
        text = match.group(1)
        url = md_url_to_html(match.group(2))
        return f'<a href="{url}">{text}</a>'

    def fix_table_links(table_match):
        t_html = table_match.group(0)
        return re.sub(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)\)', replace_md_link, t_html)

    html = re.sub(r'<table.*?>.*?</table>', fix_table_links, html, flags=re.DOTALL)
    # 通常の <a> タグ内の相対 .md リンクも .html に統一
    html = re.sub(r'(<a\s+[^>]*href=["\'])(?![a-zA-Z]+:)([^"\']+?)\.md([#?\'"])', r'\1\2.html\3', html)

    return html

def build():
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    for src_path in SRC_DIR.rglob("*"):
        rel_path = src_path.relative_to(SRC_DIR)
        if src_path.is_dir():
            (OUT_DIR / rel_path).mkdir(parents=True, exist_ok=True)
        elif src_path.suffix.lower() == ".md":
            dst_path = (OUT_DIR / rel_path).with_suffix(".html")
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            md_text = src_path.read_text(encoding="utf-8")
            body_html = convert_md_to_html(md_text)
            full_html = HTML_TEMPLATE.format(title=src_path.stem, body=body_html)
            dst_path.write_text(full_html, encoding="utf-8")
        else:
            dst_path = OUT_DIR / rel_path
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_path, dst_path)

if __name__ == "__main__":
    build()