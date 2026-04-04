# NIST EDA 1.3.3.10.Contour Plot####
# Date: 20260403
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33a.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/contour.htm
# Data URL:
#   NA
# 説明 ####
# NIST Statistic Handbook 1.3.3.10の等高線図
# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2,1), 
    mgp = c(1.6,0.5,0.0), 
    las = 1, 
    tck = 0.02)

# データの作成 ####
# 1から10までの範囲を定義
x <- seq(1, 10, length.out = 50)
y <- seq(1, 10, length.out = 50)

# 2変数の関数を定義 (中心 5.5, 5.5 の円形)
# z = (x - 5.5)^2 + (y - 5.5)^2
f <- function(x, y) {
  (x - 5.5)^2 + (y - 5.5)^2
}

# z行列の計算
z <- outer(x, y, f)

# プロットの作成####
# 等高線図の描画
contour(x, y, z, 
        nlevels = 10,        # 線の数
        drawlabels = FALSE,  # 線上の数値を非表示
        main = "等高線図", cex.main = 1,  # タイトル
        xlab = "X",          # X軸ラベル
        ylab = "Y",          # Y軸ラベル
        asp = 0.8)           # 縦横比
box()                        # 全体を枠で囲む

par(original_par)
