(function () {
  const API_URL = "https://www.pccpmdev.jp/api/vote.php";
  const pagePath = window.location.pathname;
  const storageKey = "nist_jp_voted_" + pagePath;

  let container = document.getElementById("nist-vote-widget");
  if (!container) {
    container = document.createElement("div");
    container.id = "nist-vote-widget";
    document.body.appendChild(container);
  }

  // 添付画像風の白抜き線画SVG（選択時はCSSで塗りつぶし）
  const thumbUpSvg = `
    <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M14 9V5a3 3 0 0 0-3-3l-4 9v11h11.28a2 2 0 0 0 2-1.7l1.38-9a2 2 0 0 0-2-2.3zM7 22H4a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h3"></path>
    </svg>`;

  const thumbDownSvg = `
    <svg viewBox="0 0 24 24" width="22" height="22" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
      <path d="M10 15v4a3 3 0 0 0 3 3l4-9V2H5.72a2 2 0 0 0-2 1.7l-1.38 9a2 2 0 0 0 2 2.3zm7-13h2.67A2.31 2.31 0 0 1 22 4v7a2.31 2.31 0 0 1-2.33 2H17"></path>
    </svg>`;

  container.innerHTML = `
    <style>
      #nist-vote-box {
        margin: 2.5rem auto 1.5rem;
        padding: 1rem 1.2rem;
        max-width: 640px;
        border-top: 1px solid #d0d7de;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        text-align: center;
      }
      .nist-vote-btns {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 1.2rem;
      }
      .nist-vote-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        padding: 0.45rem 0.75rem;
        border: none;
        border-radius: 999px;
        background: transparent;
        color: #57606a;
        font-size: 0.9rem;
        cursor: pointer;
        transition: background-color 0.15s, color 0.15s, transform 0.1s;
      }
      .nist-vote-btn:hover {
        background-color: #f3f4f6;
        color: #24292f;
      }
      .nist-vote-btn:active {
        transform: scale(0.95);
      }
      /* 選択状態：設定されていたアクセントカラー(#0969da)と塗りつぶし */
      .nist-vote-btn.selected {
        color: #0969da;
        background-color: #ddf4ff;
        font-weight: 600;
      }
      .nist-vote-btn.selected svg {
        fill: #0969da;
        stroke: #0969da;
      }
      #nist-vote-msg {
        margin-top: 0.5rem;
        font-size: 0.85rem;
        color: #1a7f37;
        min-height: 1.2em;
      }
      #nist-comment-area {
        display: none;
        margin-top: 0.8rem;
        text-align: left;
      }
      #nist-comment-area textarea {
        width: 100%;
        box-sizing: border-box;
        padding: 0.6rem;
        border: 1px solid #d0d7de;
        border-radius: 6px;
        font-size: 0.85rem;
        resize: vertical;
      }
      #nist-comment-submit {
        margin-top: 0.5rem;
        padding: 0.4rem 1rem;
        font-size: 0.85rem;
        color: #ffffff;
        background: #0969da;
        border: none;
        border-radius: 6px;
        cursor: pointer;
      }
      #nist-comment-submit:disabled {
        opacity: 0.6;
        cursor: default;
      }
    </style>
    <div id="nist-vote-box">
      <div class="nist-vote-btns">
        <button type="button" class="nist-vote-btn" id="btn-good" aria-label="役に立った" title="役に立った">
          ${thumbUpSvg}
          <span id="count-good">-</span>
        </button>
        <button type="button" class="nist-vote-btn" id="btn-bad" aria-label="改善が必要" title="改善が必要">
          ${thumbDownSvg}
          <span id="count-bad">-</span>
        </button>
      </div>
      <div id="nist-vote-msg"></div>
      <div id="nist-comment-area">
        <textarea id="nist-comment-text" rows="3" maxlength="500" placeholder="よろしければ理由や改善点をお知らせください（任意・500文字以内）"></textarea>
        <div style="text-align: right;">
          <button type="button" id="nist-comment-submit">コメントを送信</button>
        </div>
      </div>
    </div>
  `;

  const btnGood = document.getElementById("btn-good");
  const btnBad = document.getElementById("btn-bad");
  const countGood = document.getElementById("count-good");
  const countBad = document.getElementById("count-bad");
  const commentArea = document.getElementById("nist-comment-area");
  const commentText = document.getElementById("nist-comment-text");
  const commentSubmit = document.getElementById("nist-comment-submit");
  const voteMsg = document.getElementById("nist-vote-msg");

  let currentVote = localStorage.getItem(storageKey); // 'good' | 'bad' | null
  let isProcessing = false;

  function renderVoteState() {
    btnGood.classList.toggle("selected", currentVote === "good");
    btnBad.classList.toggle("selected", currentVote === "bad");
    if (currentVote) {
      voteMsg.textContent = "ご評価ありがとうございます（投票済み）";
    } else {
      voteMsg.textContent = "";
      commentArea.style.display = "none";
    }
  }

  // 初期表示時のカウント取得
  fetch(`${API_URL}?path=${encodeURIComponent(pagePath)}`)
    .then((res) => res.json())
    .then((data) => {
      if (data.status === "ok") {
        countGood.textContent = data.good;
        countBad.textContent = data.bad;
      }
    })
    .catch(() => {});

  // 保存済みの評価があれば画面に反映
  renderVoteState();

  // 投票・変更・取り消し処理
  function handleVote(clickedType) {
    if (isProcessing) return;
    isProcessing = true;

    const prevVote = currentVote;
    let nextVote = null;

    if (prevVote === clickedType) {
      // 同じボタンを再クリック → 取り消し
      nextVote = null;
    } else {
      // 新規投票 または 反対側へ切り替え
      nextVote = clickedType;
    }

    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "vote",
        path: pagePath,
        prev_type: prevVote,
        type: nextVote,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.status === "ok") {
          countGood.textContent = data.good;
          countBad.textContent = data.bad;
          currentVote = nextVote;

          if (currentVote) {
            localStorage.setItem(storageKey, currentVote);
            renderVoteState();
            commentArea.style.display = "block";
          } else {
            localStorage.removeItem(storageKey);
            renderVoteState();
            voteMsg.textContent = "評価を取り消しました";
          }
        }
      })
      .catch(() => {
        voteMsg.textContent = "通信エラーが発生しました。";
      })
      .finally(() => {
        isProcessing = false;
      });
  }

  btnGood.addEventListener("click", () => handleVote("good"));
  btnBad.addEventListener("click", () => handleVote("bad"));

  // コメント送信処理
  commentSubmit.addEventListener("click", () => {
    const text = commentText.value.trim();
    if (!text || !currentVote) return;
    commentSubmit.disabled = true;

    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "comment",
        path: pagePath,
        type: currentVote,
        comment: text,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.status === "ok") {
          commentArea.style.display = "none";
          commentText.value = "";
          commentSubmit.disabled = false;
          voteMsg.textContent = "ご評価ありがとうございます（投票済み）・コメントを送信しました";
        }
      })
      .catch(() => {
        commentSubmit.disabled = false;
        voteMsg.textContent = "コメントの送信に失敗しました。";
      });
  });
})();