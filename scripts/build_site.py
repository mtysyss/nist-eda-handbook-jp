import html as html_lib
import re
import shutil
from pathlib import Path
import markdown

ROOT_DIR = Path(".")
OUT_DIR = Path("_site")

# ビルド対象とするルート直下のフォルダ（綴り揺れも含めて対応）
TARGET_DIRS = ["docs", "R_Figures", "R_Scripts", "R_Fisures", "R_Sripts"]

# メイン記事用のHTMLテンプレート
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
    pre {{ background-color: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; }}
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

# .R スクリプト閲覧用のHTMLテンプレート（シンタックスハイライト・コピーボタン付き）
R_SCRIPT_TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{filename}</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/r.min.js"></script>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; max-width: 1100px; margin: 0 auto; padding: 24px; color: #24292f; background-color: #ffffff; }}
    .toolbar {{ display: flex; justify-content: space-between; align-items: center; background: #f6f8fa; border: 1px solid #d0d7de; border-bottom: none; border-radius: 6px 6px 0 0; padding: 10px 16px; }}
    .filename {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-weight: 600; font-size: 14px; }}
    .actions {{ display: flex; gap: 8px; }}
    .btn {{ font-size: 13px; padding: 5px 12px; border: 1px solid #d0d7de; border-radius: 6px; background: #ffffff; color: #24292f; cursor: pointer; text-decoration: none; }}
    .btn:hover {{ background: #f3f4f6; }}
    pre {{ margin: 0; border: 1px solid #d0d7de; border-radius: 0 0 6px 6px; overflow-x: auto; }}
    code.hljs {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13.5px; line-height: 1.55; padding: 16px; }}
  </style>
</head>
<body>
  <div class="toolbar">
    <span class="filename">{filename}</span>
    <div class="actions">
      <button class="btn" id="copy-btn" onclick="copyCode()">コードをコピー</button>
      <a class="btn" href="{raw_filename}" download>ダウンロード (.R)</a>
    </div>
  </div>
  <pre><code class="language-r" id="r-code">{escaped_code}</code></pre>
  <script>
    hljs.highlightAll();
    function copyCode() {{
      const code = document.getElementById('r-code').innerText;
      navigator.clipboard.writeText(code).then(() => {{
        const btn = document.getElementById('copy-btn');
        btn.textContent = 'コピーしました';
        setTimeout(() => {{ btn.textContent = 'コードをコピー'; }}, 2000);
      }});
    }}
  </script>
</body>
</html>
"""

def md_url_to_html(url: str) -> str:
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url):
        return url
    return re.sub(r'\.md(?=$|[?#])', '.html', url)

def rewrite_yakuchu_links(html_after_yakuchu: str) -> str:
    """#### 訳註 以降のHTML内にある R_Figures / R_Scripts リンクを変換"""
    def replace_href(match):
        prefix = match.group(1)   # <a ... href="
        url = match.group(2)      # リンク先URL
        quote = match.group(3)    # " または '

        # すでにGitHubのblob URLで書かれている R_Figures / R_Scripts を github.io の相対・直接リンクへ正規化
        gh_blob_match = re.match(
            r'^https?://github\.com/mtysyss/nist-eda-handbook-jp/blob/main/(R_Fig(?:ures|sures)|R_Sc?ripts)(/.*)$',
            url
        )
        if gh_blob_match:
            folder = gh_blob_match.group(1)
            rest = gh_blob_match.group(2)
            url = f"https://mtysyss.github.io/nist-eda-handbook-jp/{folder}{rest}"

        # R_Scripts 内の .R リンクは閲覧用HTML (.R.html) へ向け、別タブで開く
        if re.search(r'(?:^|/)(?:R_Sc?ripts)/[^"\'#?]+\.R(?:$|[?#])', url, flags=re.IGNORECASE):
            new_url = re.sub(r'(\.R)(?=$|[?#])', r'\1.html', url, flags=re.IGNORECASE)
            return f'{prefix}{new_url}{quote} target="_blank" rel="noopener"'

        # R_Figures 内のファイルリンクは画像ファイルそのものを別タブで開く
        if re.search(r'(?:^|/)(?:R_Fig(?:ures|sures))/', url, flags=re.IGNORECASE):
            return f'{prefix}{url}{quote} target="_blank" rel="noopener"'

        return match.group(0)

    return re.sub(r'(<a\s+[^>]*href=["\'])([^"\']+)(["\'])', replace_href, html_after_yakuchu)

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

    # 5. 通常の <a> タグ内の相対 .md リンクも .html に統一
    html = re.sub(r'(<a\s+[^>]*href=["\'])(?![a-zA-Z]+:)([^"\']+?)\.md([#?\'"])', r'\1\2.html\3', html)

    # 6. <h4>訳註</h4> 以降のセクションに限定して R_Figures / R_Scripts リンクを変換
    yakuchu_match = re.search(r'<h4[^>]*>\s*訳註\s*</h4>', html)
    if yakuchu_match:
        split_pos = yakuchu_match.start()
        before = html[:split_pos]
        after = html[split_pos:]
        html = before + rewrite_yakuchu_links(after)

    return html

def render_md_file(src_path: Path, dst_path: Path):
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    md_text = src_path.read_text(encoding="utf-8")
    body_html = convert_md_to_html(md_text)
    full_html = HTML_TEMPLATE.format(title=src_path.stem, body=body_html)
    dst_path.write_text(full_html, encoding="utf-8")

def render_r_script_file(src_path: Path, dst_raw_path: Path):
    """元の .R ファイルをコピーしつつ、閲覧用の .R.html を生成する"""
    dst_raw_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_path, dst_raw_path)

    code_text = src_path.read_text(encoding="utf-8", errors="replace")
    viewer_html = R_SCRIPT_TEMPLATE.format(
        filename=src_path.name,
        raw_filename=src_path.name,
        escaped_code=html_lib.escape(code_text)
    )
    viewer_path = dst_raw_path.with_name(dst_raw_path.name + ".html")
    viewer_path.write_text(viewer_html, encoding="utf-8")

def build():
    if OUT_DIR.exists():
        shutil.rmtree(OUT_DIR)
    OUT_DIR.mkdir(parents=True)

    # 1. ルート直下の .md ファイルを変換
    for md_file in ROOT_DIR.glob("*.md"):
        dst_path = OUT_DIR / md_file.with_suffix(".html").name
        render_md_file(md_file, dst_path)
        if md_file.name.lower() == "readme.md":
            render_md_file(md_file, OUT_DIR / "index.html")

    # 2. docs, R_Figures, R_Scripts フォルダ配下を構造維持したまま処理
    for dir_name in TARGET_DIRS:
        src_dir = ROOT_DIR / dir_name
        if not src_dir.exists():
            continue

        for src_path in src_dir.rglob("*"):
            rel_path = src_path.relative_to(ROOT_DIR)
            if src_path.is_dir():
                (OUT_DIR / rel_path).mkdir(parents=True, exist_ok=True)
            elif src_path.suffix.lower() == ".md":
                dst_path = (OUT_DIR / rel_path).with_suffix(".html")
                render_md_file(src_path, dst_path)
                if src_path.name.lower() == "readme.md":
                    render_md_file(src_path, dst_path.parent / "index.html")
            elif src_path.suffix.lower() == ".r" and dir_name in ("R_Scripts", "R_Sripts"):
                render_r_script_file(src_path, OUT_DIR / rel_path)
            else:
                dst_path = OUT_DIR / rel_path
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_path, dst_path)

if __name__ == "__main__":
    build()