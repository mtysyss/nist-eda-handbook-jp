# NIST EDA 1.3.3.28.Standard Deviation Plot####
# Date: 20260414
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33t.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/starplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/AUTO79.DAT
# 説明 ####
# 
# データの読込####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/AUTO79.DAT"
## クリップボードから####
# 7行目に欠損値があり、うまく読み込むには手の込んだ処理にする必要があるため
# 一度テキストファイルにペーストして、欠損を0として、クリップボードから披露
# Windowsなら "clipboard"、Macなら pipe("pbpaste") を使用します
con <- if(Sys.info()["sysname"] == "Windows") "clipboard" else pipe("pbpaste")
raw_data <- read.table(con, header = FALSE, stringsAsFactors = FALSE)

# データ修整####
## 列名の設定####
colnames(raw_data) <- c("Maker", "Model", "Price", "MPG", "Rep78", "Rep77", 
                        "Hroom", "RSeat", "Trunk", "Weight", "Length", "Turn", "Displ", "Grat")

## 車名を統合し行名に####
rownames(raw_data) <- paste(raw_data$Maker, raw_data$Model)

## 指定された9項目の抽出
selected_cols <- c("Price", "MPG", "Rep78", "Rep77", "Hroom", 
                   "RSeat", "Trunk", "Weight", "Length")
df_plot <- raw_data[, selected_cols]

# 4. データを0-5の範囲に規格化（スケーリング）する関数
rescale_0_5 <- function(x) {
  # 全て同じ値や欠損（-1など）がある場合を考慮し、最小値を一旦NAに置換して計算
  x[x <= -1] <- NA 
  min_val <- min(x, na.rm = TRUE)
  max_val <- max(x, na.rm = TRUE)
  # 最小0、最大5に変換
  return(((x - min_val) / (max_val - min_val)) * 5)
}

# 各列に適用
df_scaled <- as.data.frame(lapply(df_plot, rescale_0_5))
rownames(df_scaled) <- rownames(raw_data)

# 欠損値（NA）を0として扱う（描画エラー回避）
df_scaled[is.na(df_scaled)] <- 0

# 5. スタープロットの描画
stars(df_scaled, 
      len = 0.8, 
      key.loc = c(15, 1.5), 
      main = "1979 自動車分析 (Clipped Data)",
      draw.segments = TRUE, 
      col.segments = rainbow(9))
