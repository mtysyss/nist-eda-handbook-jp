import argparse
import datetime
import html as html_lib
import http.server
import json
import os
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

# 公開サイトのベースURL（末尾スラッシュなし）
SITE_BASE_URL = "https://mtysyss.github.io/nist-eda-handbook-jp"
SITE_NAME = "NIST/SEMATECH 工学統計ハンドブック（非公式日本語版）"
DEFAULT_DESCRIPTION = (
    "米国国立標準技術研究所（NIST）とSEMATECHによる工学統計ハンドブック"
    "（Engineering Statistics Handbook）の非公式日本語翻訳版です。探索的データ解析、"
    "測定プロセス解析、工程管理、実験計画法、信頼性工学などの統計手法を網羅しています。"
)

# メイン記事用のHTMLテンプレート
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="ja"{no_sidebar_attr}>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full_title}</title>
  <meta name="description" content="{meta_description}">
  <link rel="canonical" href="{canonical_url}">
  <meta property="og:type" content="article">
  <meta property="og:site_name" content="{site_name}">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{meta_description}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:locale" content="ja_JP">
  <meta name="twitter:card" content="summary">
  {json_ld_block}
  <link rel="stylesheet" href="{root_rel_prefix}pagefind/pagefind-ui.css">
  <style>
    :root {{
      --bg: #ffffff;
      --surface: #f6f8fa;
      --border: #d0d7de;
      --text: #24292f;
      --muted: #57606a;
      --accent: #0969da;
      --accent-bg: #ddf4ff;
      --pagefind-ui-scale: 0.9;
      --pagefind-ui-primary: #0969da;
      --pagefind-ui-text: #24292f;
      --pagefind-ui-background: #ffffff;
      --pagefind-ui-border: #d0d7de;
      --pagefind-ui-tag: #f6f8fa;
      --pagefind-ui-border-width: 1px;
      --pagefind-ui-border-radius: 6px;
      --pagefind-ui-font: -apple-system, BlinkMacSystemFont, "Segoe UI", "Hiragino Kaku Gothic ProN", "Noto Sans JP", sans-serif;
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
    .search-open-btn {{ font-weight: 600; }}

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

    /* 右寄せ：🏠 ⬅️ ⬆️ ➡️ リンク */
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

    /* === Pagefind 検索モーダル === */
    .search-modal-backdrop {{
      display: none;
      position: fixed;
      inset: 0;
      z-index: 300;
      background: rgba(27, 31, 36, 0.55);
      padding: 44px 16px 24px;
      align-items: flex-start;
      justify-content: center;
    }}
    .search-modal-backdrop.open {{ display: flex; }}
    .search-modal-box {{
      width: 100%;
      max-width: 760px;
      max-height: 84vh;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 10px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.25);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .search-modal-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      font-size: 13px;
      font-weight: 700;
      color: var(--text);
    }}
    .search-modal-body {{
      padding: 14px;
      overflow-y: auto;
    }}
    .search-fallback-msg {{
      font-size: 13px;
      color: var(--muted);
      padding: 8px 4px;
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

    /* モバイル時のみダイアログ内に表示する「ホーム・前へ・上へ・次へ」ナビ */
    .drawer-prev-next {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}
    .drawer-prev-next a {{
      flex: 1 1 auto;
      text-align: center;
      padding: 6px 6px;
      border: 1px solid var(--border);
      border-radius: 6px;
      background: #ffffff;
      color: var(--accent);
      text-decoration: none;
      font-size: 12px;
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
      font-size: 1.35rem;
      line-height: 1.4;
      margin: 0 0 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
      color: var(--text);
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

    /* === 幅が狭い時（860px以下）：ホーム・戻る・上へ・進むリンクを隠し、目次ダイアログへ格納 === */
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
    <main class="article-body" id="article-body" data-pagefind-body>
      {body}
    </main>
  </div>
  <a href="#page-top" class="back-to-top" title="ページの先頭へ">↑ 先頭へ</a>

  <!-- Pagefind サイト内検索モーダル -->
  <div class="search-modal-backdrop" id="search-modal" aria-hidden="true">
    <div class="search-modal-box" role="dialog" aria-modal="true" aria-label="サイト内全文検索">
      <div class="search-modal-header">
        <span>サイト内全文検索（{site_name}）</span>
        <button type="button" class="ctrl-btn" id="search-close-btn">閉じる (Esc)</button>
      </div>
      <div class="search-modal-body">
        <div id="pagefind-search-container"></div>
      </div>
    </div>
  </div>

  <script src="{root_rel_prefix}pagefind/pagefind-ui.js"></script>
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

      // 5. Pagefind 検索モーダルの初期化と開閉制御
      const searchModal = document.getElementById('search-modal');
      const searchOpenBtn = document.getElementById('search-open-btn');
      const searchCloseBtn = document.getElementById('search-close-btn');
      let pagefindInitialized = false;

      function openSearchModal() {{
        searchModal.classList.add('open');
        searchModal.setAttribute('aria-hidden', 'false');
        if (!pagefindInitialized) {{
          pagefindInitialized = true;
          if (typeof PagefindUI !== 'undefined') {{
            const resolvedBundlePath = new URL('{root_rel_prefix}pagefind/', window.location.href).pathname;
            new PagefindUI({{
              element: '#pagefind-search-container',
              bundlePath: resolvedBundlePath,
              showSubResults: true,
              showImages: false,
              resetStyles: false,
              translations: {{
                placeholder: 'キーワードを入力（例: ワイブル, 工程能力指数, Box-Cox, 管理図）',
                zero_results: '「[SEARCH_TERM]」に一致するページは見つかりませんでした',
                many_results: '[COUNT] 件のページが見つかりました',
                one_result: '1 件のページが見つかりました',
                searching: '「[SEARCH_TERM]」を検索中...',
                load_more: 'さらに表示'
              }}
            }});
          }} else {{
            document.getElementById('pagefind-search-container').innerHTML =
              '<p class="search-fallback-msg">検索インデックスが未生成です（ローカル検証時は <code>npx pagefind --site trialhtml</code> を実行してください）。</p>';
          }}
        }}
        setTimeout(() => {{
          const input = searchModal.querySelector('input');
          if (input) input.focus();
        }}, 50);
      }}

      function closeSearchModal() {{
        searchModal.classList.remove('open');
        searchModal.setAttribute('aria-hidden', 'true');
      }}

      if (searchOpenBtn) searchOpenBtn.addEventListener('click', openSearchModal);
      if (searchCloseBtn) searchCloseBtn.addEventListener('click', closeSearchModal);
      if (searchModal) {{
        searchModal.addEventListener('click', (e) => {{
          if (e.target === searchModal) closeSearchModal();
        }});
      }}
      document.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape' && searchModal.classList.contains('open')) {{
          closeSearchModal();
        }} else if (
          e.key === '/' &&
          !searchModal.classList.contains('open') &&
          !['INPUT', 'TEXTAREA', 'SELECT'].includes((document.activeElement || {{}}).tagName)
        ) {{
          e.preventDefault();
          openSearchModal();
        }}
      }});
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
  <title>{filename} | {site_name}</title>
  <meta name="robots" content="noindex">
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
            url = f"{SITE_BASE_URL}/{folder}{rest}"

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
    """<h4> から次の <h4> までを <details class="sec-block" open> で囲む（訳註セクションは検索ノイズ除外）"""
    h4_matches = list(re.finditer(r'(<h4\b[^>]*>.*?</h4>)', body_html, flags=re.DOTALL))
    if not h4_matches:
        return body_html

    parts = [body_html[:h4_matches[0].start()]]
    for i, m in enumerate(h4_matches):
        h4_tag = m.group(1)
        h4_plain = re.sub(r'<[^>]+>', '', h4_tag).strip()
        ignore_attr = ' data-pagefind-ignore' if h4_plain == '訳註' else ''
        content_start = m.end()
        content_end = h4_matches[i + 1].start() if i + 1 < len(h4_matches) else len(body_html)
        section_inner = body_html[content_start:content_end].strip()

        wrapped = (
            f'<details class="sec-block" open{ignore_attr}>\n'
            f'  <summary>{h4_tag}</summary>\n'
            f'  <div class="sec-content">\n{section_inner}\n  </div>\n'
            f'</details>'
        )
        parts.append(wrapped)

    return "\n".join(parts)

def extract_meta_description(body_html: str) -> str:
    """本文HTMLの冒頭段落・リストから数式やタグを除去した概要文（最大140文字）を自動生成する"""
    main_part = re.split(r'<h4[^>]*>\s*訳註\s*</h4>', body_html, maxsplit=1)[0]
    main_part = re.sub(r'<h1\b[^>]*>.*?</h1>', '', main_part, count=1, flags=re.DOTALL | re.IGNORECASE)

    blocks = re.findall(r'<(?:p|li)\b[^>]*>(.*?)</(?:p|li)>', main_part, flags=re.DOTALL | re.IGNORECASE)
    cleaned_chunks = []
    for blk in blocks:
        txt = re.sub(r'\$\$.*?\$\$', ' ', blk, flags=re.DOTALL)
        txt = re.sub(r'\$[^$]+\$', ' ', txt)
        txt = re.sub(r'<[^>]+>', ' ', txt)
        txt = html_lib.unescape(txt)
        txt = re.sub(r'\s+', ' ', txt).strip()
        if len(txt) >= 12:
            cleaned_chunks.append(txt)
        if sum(len(c) for c in cleaned_chunks) >= 180:
            break

    summary = " ".join(cleaned_chunks).strip()
    if not summary:
        return DEFAULT_DESCRIPTION
    if len(summary) > 140:
        summary = summary[:139].rstrip() + "…"
    return summary

def build_json_ld_block(
    page_title: str,
    canonical_url: str,
    meta_description: str,
    nav_items_raw: list[tuple[str, str, str]],
    src_md_path: Path,
    root_dir: Path,
    orig_url: str | None,
    lastmod_iso: str | None
) -> str:
    """SEO用の構造化データ（BreadcrumbList + TechArticle）を個別のJSON-LDタグとして生成する"""
    schemas = []

    breadcrumb_items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "ホーム",
            "item": f"{SITE_BASE_URL}/index.html"
        }
    ]
    for idx, (num_str, link_text, raw_url) in enumerate(nav_items_raw, start=2):
        html_rel = md_url_to_html(raw_url)
        if re.match(r'^https?://', html_rel, flags=re.IGNORECASE):
            item_url = html_rel
        else:
            target_abs = (src_md_path.parent / html_rel).resolve()
            try:
                rel_from_root = target_abs.relative_to(root_dir).as_posix()
                item_url = f"{SITE_BASE_URL}/{rel_from_root}"
            except ValueError:
                item_url = canonical_url

        breadcrumb_items.append({
            "@type": "ListItem",
            "position": idx,
            "name": f"{num_str} {link_text}".strip(),
            "item": item_url
        })

    if canonical_url != f"{SITE_BASE_URL}/index.html":
        breadcrumb_items.append({
            "@type": "ListItem",
            "position": len(breadcrumb_items) + 1,
            "name": page_title,
            "item": canonical_url
        })

    if len(breadcrumb_items) >= 2:
        schemas.append({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumb_items
        })

    article_schema = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": page_title,
        "description": meta_description,
        "inLanguage": "ja",
        "mainEntityOfPage": canonical_url,
        "isPartOf": {
            "@type": "WebSite",
            "name": SITE_NAME,
            "url": f"{SITE_BASE_URL}/index.html"
        }
    }
    if orig_url:
        article_schema["isBasedOn"] = orig_url
    if lastmod_iso:
        article_schema["dateModified"] = lastmod_iso

    schemas.append(article_schema)

    script_tags = []
    for schema in schemas:
        json_str = json.dumps(schema, ensure_ascii=False, indent=2)
        script_tags.append(f'<script type="application/ld+json">\n{json_str}\n  </script>')
    return "\n  ".join(script_tags)

def parse_top_navigation(
    nav_raw: str,
    nav_items_raw: list[tuple[str, str, str]],
    page_title: str,
    home_rel_url: str | None = None
) -> tuple[str, str, str, str, str | None, str | None]:
    """1つ目の <hr> より上のナビゲーション情報を解析する"""
    if not nav_raw and not nav_items_raw and not home_rel_url:
        return "", "", "", "", None, None

    all_links = re.findall(r'<a\s+[^>]*href=["\'][^"\']+["\'][^>]*>.*?</a>', nav_raw, flags=re.DOTALL)
    arrow_slots = {"home": None, "prev": None, "up": None, "next": None}
    drawer_slots = {"home": None, "prev": None, "up": None, "next": None}

    if home_rel_url:
        esc_home = html_lib.escape(home_rel_url)
        arrow_slots["home"] = f'<a href="{esc_home}" title="ホーム (index.html)">🏠</a>'
        drawer_slots["home"] = f'<a href="{esc_home}">🏠 ホーム</a>'

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

    if not nav_raw and not nav_items_raw:
        return header_prev_next_html, drawer_prev_next_html, "", "", None, None

    orig_link_match = re.search(
        r'<a\s+[^>]*href=["\'](https?://[^"\']+)["\'][^>]*>.*?</a>',
        nav_raw,
        flags=re.DOTALL | re.IGNORECASE
    )
    utc_match = re.search(r'閲覧\(UTC\)[：:]\s*([0-9\-:\s]+)', nav_raw)

    orig_url = None
    lastmod_date = None
    meta_lines = []

    if orig_link_match:
        orig_url = orig_link_match.group(1)
        orig_tag = orig_link_match.group(0)
        if 'target=' not in orig_tag:
            orig_tag = orig_tag.replace('<a ', '<a target="_blank" rel="noopener" ', 1)
        meta_lines.append(orig_tag)

    if utc_match:
        utc_str = utc_match.group(1).strip()
        meta_lines.append(f"閲覧(UTC)：{html_lib.escape(utc_str)}")
        date_only = re.match(r'(\d{4}-\d{2}-\d{2})', utc_str)
        if date_only:
            lastmod_date = date_only.group(1)

    meta_lines.append(
        f'<a href="{SITE_BASE_URL}/NOTICE.html" target="_blank" rel="noopener">著作権表示および免責事項</a>'
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

    return header_prev_next_html, drawer_prev_next_html, chapter_tree_block, source_meta_block, orig_url, lastmod_date

def build_layout_parts(
    html: str,
    has_nav: bool,
    nav_items_raw: list[tuple[str, str, str]],
    fallback_title: str,
    home_rel_url: str | None = None
) -> tuple[str, str, str, str, str, str, bool, list[tuple[str, str, str]], str | None, str | None]:
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
        # Pagefind用のタイトルメタ属性をh1に付与
        body_raw = re.sub(
            r'<h1\b([^>]*)>',
            r'<h1\1 data-pagefind-meta="title">',
            body_raw,
            count=1,
            flags=re.IGNORECASE
        )
    else:
        page_title = fallback_title

    header_prev_next, drawer_prev_next, chapter_tree_block, source_meta_block, orig_url, lastmod_date = parse_top_navigation(
        nav_raw, nav_items_raw, page_title, home_rel_url=home_rel_url
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
          <button type="button" class="ctrl-btn search-open-btn" id="search-open-btn" title="サイト内検索 (/)">🔍 検索</button>
          {accordion_buttons}
          <span class="header-page-title" title="{html_lib.escape(page_title)}">{html_lib.escape(page_title)}</span>
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
    return (
        page_title,
        header_html,
        drawer_prev_next_block,
        chapter_tree_block,
        source_meta_block,
        body_html,
        has_sidebar,
        nav_items_raw,
        orig_url,
        lastmod_date,
    )

def convert_md_to_html(
    md_text: str,
    fallback_title: str,
    has_nav: bool = True,
    home_rel_url: str | None = None
) -> tuple[str, str, str, str, str, str, bool, list[tuple[str, str, str]], str | None, str | None]:
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

    working_md = re.sub(
        r'\n[ \t]*---+[ \t]*\n+(?=\s*####\s*訳註\b)',
        '\n\n',
        working_md
    )

    working_md = preprocess_markdown_tables(working_md)

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

    for idx, math_str in enumerate(math_blocks):
        html = html.replace(f"@@MATH_{idx}@@", math_str)

    html = re.sub(r'<hr\s*/?>\s*(?=<h4[^>]*>\s*訳註\s*</h4>)', '', html, flags=re.IGNORECASE)

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

    return build_layout_parts(html, has_nav, nav_items_raw, fallback_title, home_rel_url=home_rel_url)

def render_r_script_file(src_path: Path, dst_raw_path: Path):
    """元の .R ファイルをコピーしつつ、閲覧用の .R.html を生成する"""
    dst_raw_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_path, dst_raw_path)

    code_text = src_path.read_text(encoding="utf-8", errors="replace")
    viewer_html = R_SCRIPT_TEMPLATE.format(
        filename=src_path.name,
        site_name=html_lib.escape(SITE_NAME),
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

        gh_pages_prefix = f"{SITE_BASE_URL}/"
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

def render_md_file(
    src_path: Path,
    dst_path: Path,
    root_dir: Path,
    out_dir: Path
) -> tuple[set[Path], str, str]:
    """
    1つのmdファイルをHTML変換して書き出し、
    (参照ローカルファイル集合, 正規URL, 更新日YYYY-MM-DD) を返す。
    """
    dst_path.parent.mkdir(parents=True, exist_ok=True)
    md_text = src_path.read_text(encoding="utf-8")

    is_root_index = (
        src_path.resolve().parent == root_dir.resolve()
        and src_path.name.lower() in ("index.md", "readme.md")
    )

    # ルートディレクトリまでの相対パス接頭辞（例: "" または "../../"）
    # 変更前:
    # rel_to_root = os.path.relpath(root_dir.resolve(), src_path.resolve().parent)

    # 変更後（出力先HTMLとout_dirから確実に階層深さを計算する）:
    rel_out_parts = dst_path.resolve().relative_to(out_dir.resolve()).parts
    depth = len(rel_out_parts) - 1  # ルート直下(index.html)なら 0、docs/ch1/a.html なら 2
    root_rel_prefix = "../" * depth

    home_rel_url = None if is_root_index else f"{root_rel_prefix}index.html"

    (
        page_title,
        header_nav,
        drawer_prev_next,
        chapter_tree,
        source_meta,
        body_html,
        has_sidebar,
        nav_items_raw,
        orig_url,
        lastmod_date,
    ) = convert_md_to_html(
        md_text, fallback_title=src_path.stem, has_nav=not is_root_index, home_rel_url=home_rel_url
    )

    rel_out_posix = dst_path.resolve().relative_to(out_dir.resolve()).as_posix()
    canonical_url = f"{SITE_BASE_URL}/{rel_out_posix}"

    if is_root_index or page_title == SITE_NAME:
        full_title = SITE_NAME
    else:
        full_title = f"{page_title} | {SITE_NAME}"

    meta_description = extract_meta_description(body_html)

    if not lastmod_date:
        mtime = datetime.datetime.fromtimestamp(src_path.stat().st_mtime, tz=datetime.timezone.utc)
        lastmod_date = mtime.strftime("%Y-%m-%d")

    json_ld_block = build_json_ld_block(
        page_title=page_title,
        canonical_url=canonical_url,
        meta_description=meta_description,
        nav_items_raw=nav_items_raw,
        src_md_path=src_path.resolve(),
        root_dir=root_dir.resolve(),
        orig_url=orig_url,
        lastmod_iso=lastmod_date,
    )

    no_sidebar_attr = '' if has_sidebar else ' data-no-sidebar="true"'
    full_html = HTML_TEMPLATE.format(
        no_sidebar_attr=no_sidebar_attr,
        full_title=html_lib.escape(full_title),
        meta_description=html_lib.escape(meta_description),
        canonical_url=html_lib.escape(canonical_url),
        site_name=html_lib.escape(SITE_NAME),
        json_ld_block=json_ld_block,
        root_rel_prefix=html_lib.escape(root_rel_prefix),
        header_nav=header_nav,
        drawer_prev_next_block=drawer_prev_next,
        chapter_tree_block=chapter_tree,
        source_meta_block=source_meta,
        body=body_html,
    )
    dst_path.write_text(full_html, encoding="utf-8")

    return extract_local_asset_paths(full_html, src_path, root_dir), canonical_url, lastmod_date

def generate_sitemap_and_robots(out_dir: Path, sitemap_entries: list[tuple[str, str]]):
    """検索クローラ向けの sitemap.xml と robots.txt を出力ディレクトリ直下に生成する"""
    unique_entries: dict[str, str] = {}
    for loc, lastmod in sitemap_entries:
        unique_entries[loc] = lastmod

    url_blocks = []
    for loc in sorted(unique_entries.keys()):
        lastmod = unique_entries[loc]
        priority = "1.0" if loc.endswith("/index.html") and loc.count("/") == 4 else "0.8"
        url_blocks.append(
            "  <url>\n"
            f"    <loc>{html_lib.escape(loc)}</loc>\n"
            f"    <lastmod>{html_lib.escape(lastmod)}</lastmod>\n"
            f"    <priority>{priority}</priority>\n"
            "  </url>"
        )

    sitemap_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(url_blocks)
        + "\n</urlset>\n"
    )
    (out_dir / "sitemap.xml").write_text(sitemap_xml, encoding="utf-8")

    robots_txt = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE_BASE_URL}/sitemap.xml\n"
    )
    (out_dir / "robots.txt").write_text(robots_txt, encoding="utf-8")

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
    assets, _, _ = render_md_file(src_path, dst_path, root_dir, out_dir)

    if src_path.name.lower() in ("readme.md", "index.md") and src_path.parent == root_dir:
        render_md_file(src_path, out_dir / "index.html", root_dir, out_dir)

    copy_referenced_assets(assets, root_dir, out_dir)
    print(f"単一ファイルビルド完了: {rel_path} -> {dst_path} （関連ファイル {len(assets)} 件コピー）")
    return dst_path

def build_all(root_dir: Path, out_dir: Path):
    """プロジェクトルート直下の .md、docs/ 配下の .md、リンク対象ファイル、sitemap.xml / robots.txt をビルドする"""
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)

    referenced_assets: set[Path] = set()
    sitemap_entries: list[tuple[str, str]] = []
    md_count = 0

    root_mds = list(root_dir.glob("*.md"))
    has_root_index = any(f.name.lower() == "index.md" for f in root_mds)

    for md_file in root_mds:
        if md_file.name.lower() == "readme.md" and has_root_index:
            dst_path = out_dir / md_file.with_suffix(".html").name
            assets, _, _ = render_md_file(md_file, dst_path, root_dir, out_dir)
            referenced_assets |= assets
            md_count += 1
            continue

        dst_path = out_dir / md_file.with_suffix(".html").name
        assets, canonical_url, lastmod = render_md_file(md_file, dst_path, root_dir, out_dir)
        referenced_assets |= assets
        sitemap_entries.append((canonical_url, lastmod))
        md_count += 1

        if md_file.name.lower() == "readme.md" and not has_root_index:
            idx_path = out_dir / "index.html"
            _, idx_url, idx_mod = render_md_file(md_file, idx_path, root_dir, out_dir)
            sitemap_entries.append((idx_url, idx_mod))

    docs_dir = root_dir / "docs"
    if docs_dir.exists():
        for md_file in docs_dir.rglob("*.md"):
            rel_path = md_file.relative_to(root_dir)
            dst_path = (out_dir / rel_path).with_suffix(".html")
            assets, canonical_url, lastmod = render_md_file(md_file, dst_path, root_dir, out_dir)
            referenced_assets |= assets
            sitemap_entries.append((canonical_url, lastmod))
            md_count += 1
            if md_file.name.lower() == "readme.md":
                render_md_file(md_file, dst_path.parent / "index.html", root_dir, out_dir)

    copy_referenced_assets(referenced_assets, root_dir, out_dir)
    generate_sitemap_and_robots(out_dir, sitemap_entries)

    print(
        f"全体ビルド完了: {out_dir} "
        f"（HTML {md_count} ページ / サイトマップ {len(sitemap_entries)} 件 / 関連ファイル {len(referenced_assets)} 件）"
    )

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