import argparse
import html as html_lib
import http.server
import re
import shutil
import socketserver
import threading
import time
import unicodedata
import urllib.parse
import webbrowser
from pathlib import Path
import markdown

# メイン記事用のHTMLテンプレート
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ja"{no_sidebar_attr}>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #ffffff;
      --surface: #f6f8fa;
      --border: #d0d7de;
      --text: #24292f;
      --muted: #57606a;
      --accent: #0969da;
      --accent-bg: #ddf4ff;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
      line-height: 1.75;
      margin: 0;
      padding: 0;
      color: var(--text);
      background: var(--bg);
    }}

    /* === 1. スティッキー上部ヘッダー（1行固定・省略表示対応） === */
    .top-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(246, 248, 250, 0.96);
      backdrop-filter: blur(6px);
      border-bottom: 1px solid var(--border);
      padding: 8px 16px;
    }}
    .top-nav-inner {{
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      min-height: 32px;
    }}

    /* 左寄せ：操作ボタン群 ＋ # ページ見出し */
    .header-left {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex: 1 1 auto;
      min-width: 0;
    }}
    .ctrl-btn {{
      font-size: 12px;
      padding: 4px 9px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: #ffffff;
      color: var(--text);
      cursor: pointer;
      white-space: nowrap;
      flex-shrink: 0;
    }}
    .ctrl-btn:hover {{ background: #eef1f4; }}
    .mobile-toc-btn {{ display: none; font-weight: 600; }}

    .header-page-title {{
      margin: 0 0 0 6px;
      font-size: 15px;
      font-weight: 700;
      color: var(--text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      min-width: 0;
    }}

    /* 右寄せ：⬅️ ⬆️ ➡️ リンク */
    .header-right {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-shrink: 0;
      font-size: 14px;
    }}
    .header-right a {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 3px 10px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: #ffffff;
      color: var(--text);
      text-decoration: none;
      white-space: nowrap;
      line-height: 1.3;
    }}
    .header-right a:hover {{
      background: var(--accent-bg);
      border-color: var(--accent);
    }}

    /* === メインコンテナ === */
    .page-container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 20px 20px 64px;
      display: grid;
      grid-template-columns: 270px minmax(0, 1fr);
      gap: 28px;
      align-items: start;
    }}
    html[data-no-sidebar="true"] .page-container {{
      grid-template-columns: minmax(0, 960px);
      justify-content: center;
    }}
    html[data-no-sidebar="true"] .toc-sidebar {{ display: none; }}

    /* === 左固定サイドバー / モバイル目次ダイアログ === */
    .toc-sidebar {{
      position: sticky;
      top: 62px;
      max-height: calc(100vh - 80px);
      overflow-y: auto;
      padding: 12px 14px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      font-size: 13px;
    }}
    .drawer-section {{
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border);
    }}
    .drawer-section:last-child {{
      margin-bottom: 0;
      padding-bottom: 0;
      border-bottom: none;
    }}
    .toc-title {{
      font-weight: 700;
      font-size: 11.5px;
      color: var(--muted);
      letter-spacing: 0.04em;
      margin: 0 0 6px;
    }}

    /* モバイル時のみダイアログ内に表示する「前へ・上へ・次へ」ナビ */
    .drawer-prev-next {{
      display: flex;
      gap: 6px;
    }}
    .drawer-prev-next a {{
      flex: 1;
      text-align: center;
      padding: 6px 6px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: #ffffff;
      color: var(--accent);
      text-decoration: none;
      font-size: 12.5px;
      font-weight: 600;
      white-space: nowrap;
    }}
    .drawer-prev-next a:hover {{ background: var(--accent-bg); }}

    /* 章の階層リンクツリー表示（元の番号保持） */
    .chapter-tree {{
      list-style: none;
      margin: 0;
      padding: 0;
      line-height: 1.5;
    }}
    .chapter-tree li {{
      position: relative;
      padding: 2px 0;
      display: flex;
      align-items: baseline;
    }}
    .chapter-tree .tree-branch {{
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 11px;
      margin-right: 4px;
      flex-shrink: 0;
      user-select: none;
    }}
    .chapter-tree .tree-num {{
      color: var(--muted);
      font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
      font-size: 12px;
      font-weight: 600;
      margin-right: 5px;
      flex-shrink: 0;
    }}
    .chapter-tree a {{
      color: var(--accent);
      text-decoration: none;
      padding: 1px 4px;
      border-radius: 4px;
    }}
    .chapter-tree a:hover {{
      text-decoration: underline;
      background: #eaeef2;
    }}
    .chapter-tree .tree-current {{
      font-weight: 700;
      color: var(--text);
      padding: 1px 4px;
    }}

    /* ページ内見出し（h4 / h5）目次 */
    .toc-list {{
      list-style: none;
      margin: 0;
      padding: 0;
    }}
    .toc-list li {{ margin: 2px 0; }}
    .toc-list a {{
      display: block;
      padding: 4px 8px;
      border-radius: 5px;
      color: var(--text);
      text-decoration: none;
      line-height: 1.4;
      border-left: 2px solid transparent;
    }}
    .toc-list a:hover {{ background: #eaeef2; }}
    .toc-list a.active {{
      background: var(--accent-bg);
      color: var(--accent);
      font-weight: 600;
      border-left-color: var(--accent);
    }}
    .toc-list li.toc-h5 a {{
      padding-left: 20px;
      font-size: 12px;
      color: var(--muted);
    }}
    .toc-list li.toc-h5 a.active {{ color: var(--accent); }}

    /* 原典リンク・閲覧日時・著作権表示メタ情報 */
    .source-meta {{
      font-size: 11.5px;
      color: var(--muted);
      line-height: 1.65;
    }}
    .source-meta a {{
      color: var(--accent);
      text-decoration: none;
    }}
    .source-meta a:hover {{ text-decoration: underline; }}

    /* === 本文エリア === */
    .article-body {{ min-width: 0; }}
    .article-body > h1:first-of-type {{
      position: absolute;
      width: 1px;
      height: 1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
    }}
    h1, h2, h3, h4, h5 {{ scroll-margin-top: 64px; }}

    /* === ハイブリッド：h4 セクション折りたたみ === */
    details.sec-block {{
      margin: 14px 0;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: #ffffff;
    }}
    details.sec-block:first-of-type {{ margin-top: 0; }}
    details.sec-block > summary {{
      list-style: none;
      cursor: pointer;
      padding: 10px 16px;
      background: var(--surface);
      border-radius: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
      user-select: none;
    }}
    details.sec-block[open] > summary {{
      border-bottom: 1px solid var(--border);
      border-radius: 8px 8px 0 0;
    }}
    details.sec-block > summary::-webkit-details-marker {{ display: none; }}
    details.sec-block > summary::before {{
      content: "▶";
      font-size: 11px;
      color: var(--muted);
      transition: transform 0.15s ease;
      flex-shrink: 0;
    }}
    details.sec-block[open] > summary::before {{
      transform: rotate(90deg);
    }}
    details.sec-block > summary h4 {{
      margin: 0;
      font-size: 1.08rem;
      line-height: 1.4;
    }}
    .sec-content {{
      padding: 14px 18px;
    }}
    .sec-content h5 {{
      font-size: 1rem;
      margin: 18px 0 8px;
      padding-left: 10px;
      border-left: 3px solid var(--accent);
    }}

    /* === テーブル体裁（すべて中央揃え + 属性クラス対応） === */
    .table-wrap {{
      width: 100%;
      overflow-x: auto;
      margin: 16px 0;
    }}
    table {{
      border-collapse: collapse;
      width: auto;
      max-width: 100%;
      margin: 0 auto;
    }}
    th, td {{
      border: 1px solid var(--border);
      padding: 8px 12px;
      vertical-align: top;
      word-break: normal;
      overflow-wrap: break-word;
    }}
    th:not([align]), td:not([align]) {{
      text-align: left;
    }}
    th {{ background-color: var(--surface); }}

    /* {{; .no-border-table}} ：罫線なし */
    table.no-border-table,
    table.no-border-table th,
    table.no-border-table td {{
      border: none !important;
      background-color: transparent !important;
    }}

    /* {{:. no-header-table}} ：Markdownヘッダ非表示 + 罫線なし */
    table.no-header-table thead {{
      display: none !important;
    }}
    table.no-header-table,
    table.no-header-table th,
    table.no-header-table td {{
      border: none !important;
      background-color: transparent !important;
    }}

    /* 事例研究節内（子見出しリンクあり＆2つ目の---以下）の2列等幅テーブル */
    table.equal-two-col {{
      table-layout: fixed;
      width: 100%;
    }}
    table.equal-two-col th:nth-child(1),
    table.equal-two-col td:nth-child(1),
    table.equal-two-col th:nth-child(2),
    table.equal-two-col td:nth-child(2) {{
      width: 50%;
    }}

    /* 画像・コード・数式 */
    img {{ display: block; max-width: min(620px, 100%); height: auto; margin: 16px auto; }}
    pre {{ background-color: var(--surface); padding: 12px; border-radius: 6px; overflow-x: auto; }}
    mjx-container[display="true"] {{ overflow-x: auto; overflow-y: hidden; padding: 4px 0; }}

    /* トップへ戻るボタン */
    .back-to-top {{
      position: fixed;
      right: 20px;
      bottom: 20px;
      z-index: 90;
      padding: 8px 12px;
      font-size: 13px;
      border: 1px solid var(--border);
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.95);
      color: var(--text);
      text-decoration: none;
      box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }}
    .back-to-top:hover {{ background: var(--surface); }}

    /* === 幅が狭い時（860px以下）：戻る・上へ・進むリンクを隠し、目次ダイアログへ格納 === */
    @media (max-width: 860px) {{
      .header-right {{ display: none; }}
      html:not([data-no-sidebar="true"]) .mobile-toc-btn {{ display: inline-block; }}
      .drawer-prev-next-wrap {{ display: block; }}

      .page-container {{
        grid-template-columns: minmax(0, 1fr);
        padding: 14px 14px 64px;
        gap: 0;
      }}
      .toc-sidebar {{
        display: none;
        position: fixed;
        top: 52px;
        left: 12px;
        right: 12px;
        max-height: 75vh;
        z-index: 120;
        background: #ffffff;
        box-shadow: 0 10px 28px rgba(0, 0, 0, 0.2);
      }}
      .toc-sidebar.open {{ display: block; }}
      .sec-content {{ padding: 12px 12px; }}
    }}
    @media (min-width: 861px) {{
      .drawer-prev-next-wrap {{ display: none; }}
    }}
  </style>
  <script>
    window.MathJax = {{
      tex: {{ inlineMath: [['$', '$']], displayMath: [['$$', '$$']], processEscapes: true }}
    }};
  </script>
  <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body id="page-top">
  {header_nav}
  <div class="page-container">
    <aside class="toc-sidebar" id="toc-sidebar" aria-label="ナビゲーション・目次">
      {drawer_prev_next_block}
      {chapter_tree_block}
      <div class="drawer-section" id="page-toc-section">
        <div class="toc-title">ページ内セクション</div>
        <ul class="toc-list" id="toc-list"></ul>
      </div>
      {source_meta_block}
    </aside>
    <main class="article-body" id="article-body">
      {body}
    </main>
  </div>
  <a href="#page-top" class="back-to-top" title="ページの先頭へ">↑ 先頭へ</a>

  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      const article = document.getElementById('article-body');
      const tocList = document.getElementById('toc-list');
      const tocSection = document.getElementById('page-toc-section');
      const tocSidebar = document.getElementById('toc-sidebar');
      const mobileTocBtn = document.getElementById('mobile-toc-btn');
      const headings = Array.from(article.querySelectorAll('h4[id], h5[id]'));

      // 1. h4 / h5 からページ内目次を自動生成
      if (headings.length === 0) {{
        if (tocSection) tocSection.style.display = 'none';
      }} else {{
        headings.forEach(h => {{
          const li = document.createElement('li');
          li.className = h.tagName.toLowerCase() === 'h5' ? 'toc-h5' : 'toc-h4';
          const a = document.createElement('a');
          a.href = '#' + h.id;
          a.textContent = h.textContent;
          a.dataset.targetId = h.id;
          a.addEventListener('click', () => {{
            const parentDetails = h.closest('details.sec-block');
            if (parentDetails && !parentDetails.open) {{
              parentDetails.open = true;
            }}
            tocSidebar.classList.remove('open');
          }});
          li.appendChild(a);
          tocList.appendChild(li);
        }});
      }}

      // 2. モバイル用目次ボタンの開閉
      if (mobileTocBtn) {{
        mobileTocBtn.addEventListener('click', (e) => {{
          e.stopPropagation();
          tocSidebar.classList.toggle('open');
        }});
        document.addEventListener('click', (e) => {{
          if (!tocSidebar.contains(e.target) && e.target !== mobileTocBtn) {{
            tocSidebar.classList.remove('open');
          }}
        }});
      }}

      // 3. スクロール位置に応じた目次ハイライト
      const tocLinks = Array.from(tocList.querySelectorAll('a'));
      if (tocLinks.length > 0 && 'IntersectionObserver' in window) {{
        const observer = new IntersectionObserver((entries) => {{
          entries.forEach(entry => {{
            if (entry.isIntersecting) {{
              const id = entry.target.id;
              tocLinks.forEach(link => {{
                link.classList.toggle('active', link.dataset.targetId === id);
              }});
            }}
          }});
        }}, {{ rootMargin: '-68px 0px -70% 0px', threshold: 0 }});

        headings.forEach(h => observer.observe(h));
      }}

      // 4. URLハッシュ直リンク時の自動展開
      if (location.hash) {{
        const target = document.getElementById(location.hash.slice(1));
        if (target) {{
          const parentDetails = target.closest('details.sec-block');
          if (parentDetails) parentDetails.open = true;
        }}
      }}
    }});

    // 全セクションの一括展開・折りたたみ
    function toggleAllSections(openState) {{
      document.querySelectorAll('details.sec-block').forEach(d => {{
        d.open = openState;
      }});
    }}
  </script>
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

def heading_slugify(value: str, separator: str = "-") -> str:
    """日本語・英数字を保持しつつ、見出し用の安全なアンカーIDを生成する"""
    value = unicodedata.normalize("NFKC", value)
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"[-\s]+", separator, value).strip(separator)
    return value.lower()

def md_url_to_html(url: str) -> str:
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', url):
        return url
    return re.sub(r'\.md(?=$|[?#])', '.html', url)

def rewrite_yakuchu_links(html_after_yakuchu: str) -> str:
    """#### 訳註 以降のHTML内にある R_Figures / R_Scripts リンクを変換"""
    def replace_href(match):
        prefix = match.group(1)
        url = match.group(2)
        quote = match.group(3)

        gh_blob_match = re.match(
            r'^https?://github\.com/mtysyss/nist-eda-handbook-jp/blob/main/(R_Fig(?:ures|sures)|R_Sc?ripts)(/.*)$',
            url
        )
        if gh_blob_match:
            folder = gh_blob_match.group(1)
            rest = gh_blob_match.group(2)
            url = f"https://mtysyss.github.io/nist-eda-handbook-jp/{folder}{rest}"

        if re.search(r'(?:^|/)(?:R_Sc?ripts)/[^"\'#?]+\.R(?:$|[?#])', url, flags=re.IGNORECASE):
            new_url = re.sub(r'(\.R)(?=$|[?#])', r'\1.html', url, flags=re.IGNORECASE)
            return f'{prefix}{new_url}{quote} target="_blank" rel="noopener"'

        if re.search(r'(?:^|/)(?:R_Fig(?:ures|sures))/', url, flags=re.IGNORECASE):
            return f'{prefix}{url}{quote} target="_blank" rel="noopener"'

        return match.group(0)

    return re.sub(r'(<a\s+[^>]*href=["\'])([^"\']+)(["\'])', replace_href, html_after_yakuchu)

def preprocess_markdown_tables(md_text: str) -> str:
    """Markdown変換前にテーブル関連の記述を正規化し、変換崩れを防ぐ"""
    md_text = re.sub(
        r'\n[ \t]*\{\s*[;:]\s*\.(no-border-table|no-header-table)\s*\}[ \t]*(?=\n|$)',
        lambda m: f'\n\n<!-- TABLE_ATTR:{m.group(1).lower()} -->\n',
        md_text,
        flags=re.IGNORECASE
    )

    def pad_raw_table(m):
        return f"\n\n{m.group(0).strip()}\n\n"

    md_text = re.sub(
        r'<table\b[^>]*>.*?</table>',
        pad_raw_table,
        md_text,
        flags=re.DOTALL | re.IGNORECASE
    )
    return md_text

def add_class_to_table_tag(table_html: str, new_class: str) -> str:
    """<table ...> タグにクラス名を重複なく追加する"""
    def repl(m):
        attrs = m.group(1)
        class_match = re.search(r'\bclass=(["\'])(.*?)\1', attrs, flags=re.IGNORECASE)
        if class_match:
            quote = class_match.group(1)
            existing = class_match.group(2).split()
            if new_class not in existing:
                existing.append(new_class)
            updated_attrs = (
                attrs[:class_match.start()]
                + f'class={quote}{" ".join(existing)}{quote}'
                + attrs[class_match.end():]
            )
            return f'<table{updated_attrs}>'
        return f'<table{attrs} class="{new_class}">'

    return re.sub(r'^<table\b([^>]*)>', repl, table_html, count=1, flags=re.IGNORECASE)

def count_table_columns(table_html: str) -> int:
    """テーブル内の最初の行（tr）から列数をカウントする"""
    first_tr = re.search(r'<tr\b[^>]*>(.*?)</tr>', table_html, flags=re.DOTALL | re.IGNORECASE)
    if not first_tr:
        return 0
    cells = re.findall(r'<(?:th|td)\b[^>]*>', first_tr.group(1), flags=re.IGNORECASE)
    return len(cells)

def process_body_tables(body_html: str) -> str:
    """本文内の全テーブルに対して属性付与・2列等幅化・中央揃えラッパーを適用する"""
    attr_pattern = re.compile(
        r'(<table\b[^>]*>.*?</table>)\s*(?:<p>\s*)?(?:<!--\s*TABLE_ATTR:(no-border-table|no-header-table)\s*-->|\{\s*[;:]\s*\.(no-border-table|no-header-table)\s*\})(?:\s*</p>)?',
        flags=re.DOTALL | re.IGNORECASE
    )

    def apply_table_attr(match):
        t_html = match.group(1)
        cls_name = (match.group(2) or match.group(3)).lower()
        return add_class_to_table_tag(t_html, cls_name)

    body_html = attr_pattern.sub(apply_table_attr, body_html)

    first_h4 = re.search(r'<h4\b[^>]*>(.*?)</h4>', body_html, flags=re.DOTALL | re.IGNORECASE)
    has_linked_h4 = bool(first_h4 and re.search(r'<a\b[^>]*href=', first_h4.group(1), flags=re.IGNORECASE))

    second_hr = re.search(r'<hr\s*/?>', body_html, flags=re.IGNORECASE)

    if has_linked_h4 and second_hr:
        before_hr = body_html[:second_hr.end()]
        after_hr = body_html[second_hr.end():]

        def make_two_col_equal(t_match):
            t_html = t_match.group(0)
            if count_table_columns(t_html) == 2:
                return add_class_to_table_tag(t_html, "equal-two-col")
            return t_html

        after_hr = re.sub(r'<table\b[^>]*>.*?</table>', make_two_col_equal, after_hr, flags=re.DOTALL | re.IGNORECASE)
        body_html = before_hr + after_hr

    body_html = re.sub(
        r'(<table\b[^>]*>.*?</table>)',
        r'<div class="table-wrap">\1</div>',
        body_html,
        flags=re.DOTALL | re.IGNORECASE
    )
    return body_html

def wrap_h4_sections(body_html: str) -> str:
    """<h4> から次の <h4> までを <details class="sec-block" open> で囲む"""
    h4_matches = list(re.finditer(r'(<h4\b[^>]*>.*?</h4>)', body_html, flags=re.DOTALL))
    if not h4_matches:
        return body_html

    parts = [body_html[:h4_matches[0].start()]]
    for i, m in enumerate(h4_matches):
        h4_tag = m.group(1)
        content_start = m.end()
        content_end = h4_matches[i + 1].start() if i + 1 < len(h4_matches) else len(body_html)
        section_inner = body_html[content_start:content_end].strip()

        wrapped = (
            f'<details class="sec-block" open>\n'
            f'  <summary>{h4_tag}</summary>\n'
            f'  <div class="sec-content">\n{section_inner}\n  </div>\n'
            f'</details>'
        )
        parts.append(wrapped)

    return "\n".join(parts)

def parse_top_navigation(nav_raw: str, nav_items_raw: list[tuple[str, str, str]], page_title: str) -> tuple[str, str, str, str]:
    """1つ目の <hr> より上のナビゲーション情報を解析する"""
    if not nav_raw and not nav_items_raw:
        return "", "", "", ""

    all_links = re.findall(r'<a\s+[^>]*href=["\'][^"\']+["\'][^>]*>.*?</a>', nav_raw, flags=re.DOTALL)
    arrow_slots = {"prev": None, "up": None, "next": None}
    drawer_slots = {"prev": None, "up": None, "next": None}

    for a_tag in all_links:
        label = re.sub(r'<[^>]+>', '', a_tag).strip()
        if '⬅' in label:
            arrow_slots["prev"] = a_tag
            drawer_slots["prev"] = re.sub(r'>.*?</a>', '>⬅️ 前へ</a>', a_tag, flags=re.DOTALL)
        elif '⬆' in label:
            arrow_slots["up"] = a_tag
            drawer_slots["up"] = re.sub(r'>.*?</a>', '>⬆️ 上へ</a>', a_tag, flags=re.DOTALL)
        elif '➡' in label:
            arrow_slots["next"] = a_tag
            drawer_slots["next"] = re.sub(r'>.*?</a>', '>次へ ➡️</a>', a_tag, flags=re.DOTALL)

    header_prev_next_html = "\n".join(v for v in arrow_slots.values() if v)
    drawer_prev_next_html = "\n".join(v for v in drawer_slots.values() if v)

    # 原典リンク・閲覧(UTC)日時・著作権表示および免責事項リンクの組み立て
    orig_link_match = re.search(
        r'<a\s+[^>]*href=["\']https?://[^"\']+["\'][^>]*>.*?</a>',
        nav_raw,
        flags=re.DOTALL | re.IGNORECASE
    )
    utc_match = re.search(r'閲覧\(UTC\)[：:]\s*([0-9\-:\s]+)', nav_raw)

    meta_lines = []
    if orig_link_match:
        orig_tag = orig_link_match.group(0)
        if 'target=' not in orig_tag:
            orig_tag = orig_tag.replace('<a ', '<a target="_blank" rel="noopener" ', 1)
        meta_lines.append(orig_tag)
    if utc_match:
        meta_lines.append(f"閲覧(UTC)：{html_lib.escape(utc_match.group(1).strip())}")

    # 原典・閲覧の次の行に「著作権表示および免責事項」へのリンクを追加
    meta_lines.append(
        '<a href="https://mtysyss.github.io/nist-eda-handbook-jp/NOTICE.html" target="_blank" rel="noopener">著作権表示および免責事項</a>'
    )

    source_meta_block = (
        '<div class="drawer-section source-meta">'
        f'{"<br>".join(meta_lines)}'
        '</div>'
    )

    chapter_tree_block = ""
    if nav_items_raw:
        tree_lis = []
        for depth, (num_str, link_text, raw_url) in enumerate(nav_items_raw):
            indent_px = depth * 14
            branch = "└ " if depth > 0 else ""
            html_url = md_url_to_html(raw_url)
            tree_lis.append(
                f'<li style="padding-left: {indent_px}px;">'
                f'<span class="tree-branch">{branch}</span>'
                f'<span class="tree-num">{html_lib.escape(num_str)}</span>'
                f'<a href="{html_lib.escape(html_url)}">{html_lib.escape(link_text)}</a>'
                f'</li>'
            )

        if page_title:
            current_indent = len(nav_items_raw) * 14
            tree_lis.append(
                f'<li style="padding-left: {current_indent}px;">'
                f'<span class="tree-branch">└ </span>'
                f'<span class="tree-current">{html_lib.escape(page_title)}</span>'
                f'</li>'
            )

        chapter_tree_block = (
            '<div class="drawer-section">'
            '<div class="toc-title">章の階層</div>'
            f'<ul class="chapter-tree">{"".join(tree_lis)}</ul>'
            '</div>'
        )

    return header_prev_next_html, drawer_prev_next_html, chapter_tree_block, source_meta_block

def build_layout_parts(
    html: str,
    has_nav: bool,
    nav_items_raw: list[tuple[str, str, str]],
    fallback_title: str
) -> tuple[str, str, str, str, str, str, bool]:
    """index.md 以外のページは最初の <hr> で上部ナビゲーションと本文を分離する"""
    if has_nav:
        hr_match = re.search(r'<hr\s*/?>', html, flags=re.IGNORECASE)
        if hr_match:
            nav_raw = html[:hr_match.start()].strip()
            body_raw = html[hr_match.end():].strip()
        else:
            nav_raw = ""
            body_raw = html
    else:
        nav_raw = ""
        body_raw = html

    h1_match = re.search(r'<h1\b[^>]*>(.*?)</h1>', body_raw, flags=re.DOTALL)
    if h1_match:
        page_title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
    else:
        page_title = fallback_title

    header_prev_next, drawer_prev_next, chapter_tree_block, source_meta_block = parse_top_navigation(
        nav_raw, nav_items_raw, page_title
    )

    has_h4 = bool(re.search(r'<h4\b', body_raw))
    has_h5 = bool(re.search(r'<h5\b', body_raw))
    has_sidebar = bool(chapter_tree_block or source_meta_block or has_h4 or has_h5)

    accordion_buttons = (
        '<button type="button" class="ctrl-btn" onclick="toggleAllSections(true)">すべて展開</button>'
        '<button type="button" class="ctrl-btn" onclick="toggleAllSections(false)">すべて折りたたむ</button>'
        if has_h4 else ""
    )

    header_right_html = f'<div class="header-right">{header_prev_next}</div>' if header_prev_next else ""

    header_html = f"""
    <header class="top-nav">
      <div class="top-nav-inner">
        <div class="header-left">
          <button type="button" class="ctrl-btn mobile-toc-btn" id="mobile-toc-btn">☰ 目次</button>
          {accordion_buttons}
          <h1 class="header-page-title" title="{html_lib.escape(page_title)}">{html_lib.escape(page_title)}</h1>
        </div>
        {header_right_html}
      </div>
    </header>
    """

    drawer_prev_next_block = ""
    if drawer_prev_next:
        drawer_prev_next_block = (
            '<div class="drawer-section drawer-prev-next-wrap">'
            '<div class="toc-title">ページ移動</div>'
            f'<div class="drawer-prev-next">{drawer_prev_next}</div>'
            '</div>'
        )

    body_html = process_body_tables(body_raw)
    body_html = wrap_h4_sections(body_html)
    return page_title, header_html, drawer_prev_next_block, chapter_tree_block, source_meta_block, body_html, has_sidebar

def convert_md_to_html(md_text: str, fallback_title: str, has_nav: bool = True) -> tuple[str, str, str, str, str, str, bool]:
    math_blocks = []
    nav_items_raw: list[tuple[str, str, str]] = []

    def push_math(tex_str: str) -> str:
        math_blocks.append(tex_str)
        return f"@@MATH_{len(math_blocks)-1}@@"

    if has_nav:
        hr_md_match = re.search(r'^\s*---+\s*$', md_text, flags=re.MULTILINE)
        if hr_md_match:
            top_md = md_text[:hr_md_match.start()]
            rest_md = md_text[hr_md_match.start():]

            def capture_nav_item(m):
                num_str = m.group(1)
                link_text = m.group(2)
                raw_url = m.group(3)
                nav_items_raw.append((num_str, link_text, raw_url))
                return ""

            top_md = re.sub(
                r'^\s*(\d+(?:\.\d+)*\.)\s*\[([^\]]+)\]\(([^)\s]+)\)[ \t]*$',
                capture_nav_item,
                top_md,
                flags=re.MULTILINE
            )
            working_md = top_md + rest_md
        else:
            working_md = md_text
    else:
        working_md = md_text

    # #### 訳註 の直前にある --- をMarkdown段階で除去
    working_md = re.sub(
        r'\n[ \t]*---+[ \t]*\n+(?=\s*####\s*訳註\b)',
        '\n\n',
        working_md
    )

    # テーブル直後の属性記法・生<table>前後の空行を正規化
    working_md = preprocess_markdown_tables(working_md)

    # ブロック数式 $$...$$ とインライン数式 $`...`$ をHTML変換前に退避
    protected = re.sub(r'\$\$.*?\$\$', lambda m: push_math(m.group(0)), working_md, flags=re.DOTALL)
    protected = re.sub(r'\$`([^`]+)`\$', lambda m: push_math(f"${m.group(1)}$"), protected)

    html = markdown.markdown(
        protected,
        extensions=['tables', 'fenced_code', 'toc'],
        extension_configs={
            'toc': {
                'toc_depth': '1-5',
                'slugify': heading_slugify,
            }
        }
    )

    # 退避した数式を復元
    for idx, math_str in enumerate(math_blocks):
        html = html.replace(f"@@MATH_{idx}@@", math_str)

    # HTML変換後も <h4>訳註</h4> 直前に <hr> が残っていれば除去
    html = re.sub(r'<hr\s*/?>\s*(?=<h4[^>]*>\s*訳註\s*</h4>)', '', html, flags=re.IGNORECASE)

    # <table>内の [text](url) や .md リンクを <a> タグ & .html に変換
    def replace_md_link(match):
        text = match.group(1)
        url = md_url_to_html(match.group(2))
        return f'<a href="{url}">{text}</a>'

    def fix_table_links(table_match):
        t_html = table_match.group(0)
        return re.sub(r'(?<!!)\[([^\]]+)\]\(([^)\s]+)\)', replace_md_link, t_html)

    html = re.sub(r'<table.*?>.*?</table>', fix_table_links, html, flags=re.DOTALL)
    html = re.sub(r'(<a\s+[^>]*href=["\'])(?![a-zA-Z]+:)([^"\']+?)\.md([#?\'"])', r'\1\2.html\3', html)

    yakuchu_match = re.search(r'<h4[^>]*>\s*訳註\s*</h4>', html)
    if yakuchu_match:
        split_pos = yakuchu_match.start()
        before = html[:split_pos]
        after = html[split_pos:]
        html = before + rewrite_yakuchu_links(after)

    return build_layout_parts(html, has_nav, nav_items_raw, fallback_title)

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

def extract_local_asset_paths(html_content: str, src_md_path: Path, root_dir: Path) -> set[Path]:
    """生成されたHTML内の href / src 属性から、リポジトリ内のローカル参照ファイル（非.md/.html）を抽出する"""
    assets: set[Path] = set()
    urls = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', html_content, flags=re.IGNORECASE)

    for raw_url in urls:
        if raw_url.startswith(('#', 'mailto:', 'tel:', 'javascript:', 'data:')):
            continue

        clean_url = urllib.parse.unquote(raw_url.split('#')[0].split('?')[0]).strip()
        if not clean_url:
            continue

        gh_pages_prefix = "https://mtysyss.github.io/nist-eda-handbook-jp/"
        if clean_url.startswith(gh_pages_prefix):
            rel_str = clean_url[len(gh_pages_prefix):]
            target_path = (root_dir / rel_str).resolve()
        elif re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', clean_url):
            continue
        elif clean_url.startswith('/'):
            target_path = (root_dir / clean_url.lstrip('/')).resolve()
        else:
            target_path = (src_md_path.parent / clean_url).resolve()

        try:
            target_path.relative_to(root_dir)
        except ValueError:
            continue

        if target_path.name.lower().endswith(".r.html"):
            target_path = target_path.with_name(target_path.name[:-5])
        elif target_path.suffix.lower() in (".html", ".md"):
            continue

        if target_path.is_file():
            assets.add(target_path)

    return assets

def copy_referenced_assets(asset_paths: set[Path], root_dir: Path, out_dir: Path):
    """mdファイル内から参照されているローカルファイルのみを出力先へコピー（.Rは閲覧用HTMLも生成）"""
    for src_asset in sorted(asset_paths):
        rel_path = src_asset.relative_to(root_dir)
        dst_asset = out_dir / rel_path
        if src_asset.suffix.lower() == ".r":
            render_r_script_file(src_asset, dst_asset)
        else:
            dst_asset.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_asset, dst_asset)

def render_md_file(src_path: Path, dst_path: Path, root_dir: Path) -> set[Path]:
    """1つのmdファイルをHTML変換して書き出し、そのページが参照しているローカルファイル集合を返す"""
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    md_text = src_path.read_text(encoding="utf-8")

    is_root_index = (
        src_path.resolve().parent == root_dir.resolve()
        and src_path.name.lower() in ("index.md", "readme.md")
    )

    page_title, header_nav, drawer_prev_next, chapter_tree, source_meta, body_html, has_sidebar = convert_md_to_html(
        md_text, fallback_title=src_path.stem, has_nav=not is_root_index
    )
    no_sidebar_attr = '' if has_sidebar else ' data-no-sidebar="true"'
    full_html = HTML_TEMPLATE.format(
        no_sidebar_attr=no_sidebar_attr,
        title=html_lib.escape(page_title),
        header_nav=header_nav,
        drawer_prev_next_block=drawer_prev_next,
        chapter_tree_block=chapter_tree,
        source_meta_block=source_meta,
        body=body_html,
    )
    dst_path.write_text(full_html, encoding="utf-8")

    return extract_local_asset_paths(full_html, src_path, root_dir)

def build_single_file(target_md: str, root_dir: Path, out_dir: Path):
    """指定された1つの .md ファイルと、その中のリンク対象ファイルだけを出力先へ変換する"""
    candidate = Path(target_md)
    if candidate.exists():
        src_path = candidate.resolve()
    else:
        src_path = (root_dir / target_md).resolve()

    if not src_path.exists() or src_path.suffix.lower() != ".md":
        raise FileNotFoundError(f"対象のMarkdownファイルが見つかりません: {target_md}")

    rel_path = src_path.relative_to(root_dir)
    dst_path = (out_dir / rel_path).with_suffix(".html")
    assets = render_md_file(src_path, dst_path, root_dir)

    if src_path.name.lower() in ("readme.md", "index.md") and src_path.parent == root_dir:
        render_md_file(src_path, out_dir / "index.html", root_dir)

    copy_referenced_assets(assets, root_dir, out_dir)
    print(f"単一ファイルビルド完了: {rel_path} -> {dst_path} （関連ファイル {len(assets)} 件コピー）")
    return dst_path

def build_all(root_dir: Path, out_dir: Path):
    """プロジェクトルート直下の .md、docs/ 配下の .md、およびそれらからリンクされたファイルのみビルドする"""
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    referenced_assets: set[Path] = set()
    md_count = 0

    root_mds = list(root_dir.glob("*.md"))
    has_root_index = any(f.name.lower() == "index.md" for f in root_mds)

    for md_file in root_mds:
        dst_path = out_dir / md_file.with_suffix(".html").name
        referenced_assets |= render_md_file(md_file, dst_path, root_dir)
        md_count += 1
        if md_file.name.lower() == "readme.md" and not has_root_index:
            render_md_file(md_file, out_dir / "index.html", root_dir)

    docs_dir = root_dir / "docs"
    if docs_dir.exists():
        for md_file in docs_dir.rglob("*.md"):
            rel_path = md_file.relative_to(root_dir)
            dst_path = (out_dir / rel_path).with_suffix(".html")
            referenced_assets |= render_md_file(md_file, dst_path, root_dir)
            md_count += 1
            if md_file.name.lower() == "readme.md":
                render_md_file(md_file, dst_path.parent / "index.html", root_dir)

    copy_referenced_assets(referenced_assets, root_dir, out_dir)

    print(f"全体ビルド完了: {out_dir} （HTML {md_count} ページ / リンク対象ファイル {len(referenced_assets)} 件）")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Markdown to HTML static site builder")
    parser.add_argument(
        "--trial",
        action="store_true",
        help="ローカル検証モード（py実行フォルダの1つ上 .. をルートとし、../trialhtml へ出力）"
    )
    parser.add_argument(
        "-f", "--file",
        help="単体テスト用に1ファイルだけビルドする場合のパス"
    )
    parser.add_argument(
        "-s", "--serve",
        action="store_true",
        help="ビルド後にローカルサーバーを起動してブラウザでプレビューする"
    )
    args = parser.parse_args()

    if args.trial or args.file:
        root_dir = Path("..").resolve()
        out_dir = root_dir / "trialhtml"
    else:
        root_dir = Path(".").resolve()
        out_dir = root_dir / "_site"

    if args.file:
        dst_html = build_single_file(args.file, root_dir, out_dir)
    else:
        build_all(root_dir, out_dir)
        dst_html = out_dir / "index.html"

    if args.serve:
        rel_url = dst_html.relative_to(out_dir).as_posix()
        port = 8000
        url = f"http://localhost:{port}/{rel_url}"

        class Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *h_args, **h_kwargs):
                super().__init__(*h_args, directory=str(out_dir), **h_kwargs)

        def open_browser():
            time.sleep(0.8)
            webbrowser.open(url)

        threading.Thread(target=open_browser, daemon=True).start()
        print(f"プレビューサーバー起動中: {url} （停止は Ctrl+C）")
        with socketserver.TCPServer(("", port), Handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nサーバーを停止しました。")