(function () {
  const API_URL = "https://www.pccpmdev.jp/api/vote.php";
  const pagePath = window.location.pathname;
  const storageKey = "nist_jp_voted_" + pagePath;

  // ウィジェット挿入先の取得（なければbody末尾に追加）
  let container = document.getElementById("nist-vote-widget");
  if (!container) {
    container = document.createElement("div");
    container.id = "nist-vote-widget";
    document.body.appendChild(container);
  }

  // スタイルとHTMLの構築
  container.innerHTML = `
    <style>
      #nist-vote-box {
        margin: 2.5rem auto 1.5rem;
        padding: 1.2rem 1.5rem;
        max-width: 640px;
        border: 1px solid #d0d7de;
        border-radius: 8px;
        background-color: #f6f8fa;
        font-family: sans-serif;
        text-align: center;
      }
      #nist-vote-box p.title {
        margin: 0 0 0.8rem;
        font-size: 0.95rem;
        font-weight: bold;
        color: #24292f;
      }
      .nist-vote-btns {
        display: flex;
        justify-content: center;
        gap: 1rem;
      }
      .nist-vote-btn {
        padding: 0.5rem 1.2rem;
        font-size: 0.9rem;
        border: 1px solid #afb8c1;
        border-radius: 6px;
        background: #ffffff;
        cursor: pointer;
        transition: background 0.15s;
      }
      .nist-vote-btn:hover:not(:disabled) {
        background: #eaeef2;
      }
      .nist-vote-btn:disabled {
        opacity: 0.65;
        cursor: default;
      }
      .nist-vote-btn.selected {
        border-color: #0969da;
        background: #ddf4ff;
        font-weight: bold;
      }
      #nist-comment-area {
        display: none;
        margin-top: 1rem;
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
      #nist-vote-msg {
        margin-top: 0.6rem;
        font-size: 0.85rem;
        color: #1a7f37;
      }
    </style>
    <div id="nist-vote-box">
      <p class="title">このページの内容は役に立ちましたか？</p>
      <div class="nist-vote-btns">
        <button type="button" class="nist-vote-btn" id="btn-good">👍 いいね (<span id="count-good">-</span>)</button>
        <button type="button" class="nist-vote-btn" id="btn-bad">👎 ダメね (<span id="count-bad">-</span>)</button>
      </div>
      <div id="nist-comment-area">
        <textarea id="nist-comment-text" rows="3" maxlength="500" placeholder="よろしければ理由や改善点をお知らせください（任意・500文字以内）"></textarea>
        <div style="text-align: right;">
          <button type="button" id="nist-comment-submit">コメントを送信</button>
        </div>
      </div>
      <div id="nist-vote-msg"></div>
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

  let selectedType = localStorage.getItem(storageKey);

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

  // すでに投票済みの場合の表示制御
  if (selectedType) {
    btnGood.disabled = true;
    btnBad.disabled = true;
    if (selectedType === "good") btnGood.classList.add("selected");
    if (selectedType === "bad") btnBad.classList.add("selected");
    voteMsg.textContent = "ご評価ありがとうございます（投票済み）";
  }

  // 投票ボタン押下時の処理
  function handleVote(type) {
    if (selectedType) return;
    selectedType = type;
    btnGood.disabled = true;
    btnBad.disabled = true;
    if (type === "good") btnGood.classList.add("selected");
    if (type === "bad") btnBad.classList.add("selected");

    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ action: "vote", path: pagePath, type: type }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.status === "ok") {
          countGood.textContent = data.good;
          countBad.textContent = data.bad;
          localStorage.setItem(storageKey, type);
          voteMsg.textContent = "評価を記録しました！";
          commentArea.style.display = "block"; // コメント欄を展開
        }
      })
      .catch(() => {
        voteMsg.textContent = "通信エラーが発生しました。";
      });
  }

  btnGood.addEventListener("click", () => handleVote("good"));
  btnBad.addEventListener("click", () => handleVote("bad"));

  // コメント送信処理
  commentSubmit.addEventListener("click", () => {
    const text = commentText.value.trim();
    if (!text) return;
    commentSubmit.disabled = true;

    fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        action: "comment",
        path: pagePath,
        type: selectedType,
        comment: text,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.status === "ok") {
          commentArea.style.display = "none";
          voteMsg.textContent = "コメントを送信しました。貴重なご意見ありがとうございます！";
        }
      })
      .catch(() => {
        commentSubmit.disabled = false;
        voteMsg.textContent = "コメントの送信に失敗しました。";
      });
  });
})();