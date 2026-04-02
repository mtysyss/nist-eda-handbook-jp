# NIST EDA 1336 Box-Cox Normality Plot ####
# Date: 20260402
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda336.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/boxcoxno.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/AUTO83B.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.6のBox-Cox正規性プロット
# 元データでの近似直線を加えた図（左上）Box-Cox正規性プロット(右上)から
# λ値を求め、変換後の近似直線とともにプロット
# ヒストグラムは、Y軸調整のため、頻度を計算してから描画しています。
# 左上：生データヒストグラム
# 右上：x値（温度）を変換し、相関係数を取得し、λでプロット
# 左下：|λ|で変換した値のヒストグラム
# 右下：変換データの正規確率プロット

# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.6,0.2,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/AUTO83B.DAT"
data <- read.table(url,skip=25)
# 列名の割り当て
colnames(data) <- c("U.S.","Japan")

y <- data$U.S.

# プロットエリアの設定####
par(mfrow = c(2,2))

# 左上：生データヒストグラム####
breaks = 20
h1 <- hist(y, breaks = breaks, plot= FALSE)
max_y1 <- max(h1$counts) * 1.1
hist(y,breaks = breaks, 
     xlim = c(-25,65),
     ylim = c(0, max_y1), yaxs = "i",
     main="生データヒストグラム",xlab="",ylab="",
     col = "lightblue")
box()

# 右上：Box-Cox正規性プロット####
## 変換の関数を定義####
box_cox_trans <- function(x, lambda) {
  if (lambda == 0) {
    return(log(x))
  } else {
    return((x^lambda - 1) / lambda)
  }
}

## lambdaの範囲を設定####
### 各lambdaでの正規確率プロットの相関係数を計算####
lambda_seq <- seq(-2, 2, by = 0.1)
cor_values <- sapply(lambda_seq, function(l) {
  y_trans <- box_cox_trans(y, l)
  # 正規確率プロットの理論上の値との相関を計算
  qq <- qqnorm(y_trans, plot.it = FALSE)
  return(cor(qq$x, qq$y))
})

## プロット####
plot(lambda_seq, cor_values, type = "l",
     main = "Box-Cox 正規性プロット",
     xlab = "",
     ylab = "",
     col = "blue")

## 最大値（最適なlambda）の特定と表示####
max_idx <- which.max(cor_values)
opt_lambda <- lambda_seq[max_idx]
abline(v = opt_lambda, col = "red", lty = 2)

mtext(paste("最大λ値 =", opt_lambda), side = 1, line = 2, col = "red")
mtext("相関係数", side = 2, line = 2, las = 3, cex = 0.8)

# 左下：変換後データヒストグラム####
## 最適なlambdaでデータを変換####
# Box-Cox変換関数の定義
boxcox_trans <- function(y, lambda) {
  if (abs(lambda) < 1e-7) {
    return(log(y))
  } else {
    return((y^lambda - 1) / lambda)
  }
}

# 変換データの作成####
yt <- boxcox_trans(y, opt_lambda)
breaks = 20
h2 <- hist(yt, breaks = breaks, plot= FALSE)
max_y2 <- max(h2$counts) * 1.1

## プロット####
hist(yt,breaks = breaks, 
     xlim = c(0.75,3.25),
     ylim = c(0, max_y2), yaxs = "i",
     main="変換後データ",xlab="",ylab="",
     col = "lightblue")
box()

# 右下：正規確率プロット####
# プロットの作成
qqnorm(yt, 
       main = "正規確率プロット", # タイトル
       xlab = "",   # X軸ラベル
       ylab = "",   # Y軸ラベル
       pch = 16,     # 点の形
       cex = 0.5,
       col = "blue")   # 点の大きさ

par(original_par)
