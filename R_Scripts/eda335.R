# NIST EDA 1335 Box-Cox Linearity Plot ####
# Date: 20260401
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda335.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/boxcoxli.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/JONES.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.5のBox-Cox線形性プロット
# 元データでの近似直線を加えた図（左上）Box-Cox線形性プロット(右上)から
# λ値を求め、変換後の近似直線とともにプロット
# 左上：生データ散布図にlm()で近似した線を引く
# 右上：x値（温度）を変換し、相関係数を取得し、λでプロット
# 左下：|λ|で変換した温度とy値（比重)の値をプロットし、lm()で近似した線を引く

# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.6,0.2,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/JONES.DAT"
data <- read.table(url,skip=25)
# 列名の割り当て
colnames(data) <- c("Density","Temperature")

# プロットエリアの設定####
par(mfrow = c(2,2))
## データの生成 ####

## 線形回帰モデルの計算####
fit <- lm( data$Density ~ data$Temperature)
res_sd <- summary(fit)$sigma  # 残差標準偏差を取得

# 元データ散布図プロット####
plot(data$Temperature, data$Density, 
     pch = 16,                # 点の形）
     cex = 0.8,               # 点の大きさ
     xlim = c(0, max(data$Temperature)*1.05), # X軸の範囲
     ylim = c(991, 1002), # Y軸の範囲
     xaxt = "n", #yaxt = "n",  # デフォルトの軸を非表示に
     xlab = "", ylab = "",    # 軸ラベルを一旦空に
     main = "元データの線形近似") # タイトル

## 軸の調整####
# ① 5刻みで「目盛（線）」だけを描く (labels = FALSE)
axis(1, at = seq(0, 40, by = 5), labels = FALSE)
# ② 10刻みで「目盛ラベル（数字）」を描く
axis(1, at = seq(0, 40, by = 10), labels = seq(0, 40, by = 10), tick = FALSE)
axis(2, at = seq(992, 1002, by = 1), labels = FALSE)
axis(2, at = seq(992, 1002, by = 2), labels = seq(992, 1002, by = 2), tick = FALSE)

## 回帰線の追加####
# データの範囲（xの最小から最大まで）で線を引く
lines(data$Temperature, fitted(fit), lwd = 1, col="blue")

## 残差標準偏差の表示####
mtext(paste0("残差標準偏差= ",round(res_sd,3)),side=1, line=1.5, cex=0.9)
 
# Box-Cox線形性プロット####
## lambdaの範囲を設定####
lambdas <- seq(-2, 2, by = 0.1)

## 各lambdaで変換後のyとxの相関係数を計算####
cor_values <- sapply(lambdas, function(l) {
  # Box-Cox変換の定義式
  if (l == 0) {
    yt <- log(data$Temperature)
  } else {
    yt <- (data$Temperature^l - 1) / l
  }
  return(cor(data$Density, yt)) # 相関係数 (r) を計算
})

## プロット####
plot(lambdas, cor_values, type = "l", col = "blue", lwd = 1,
     xlab = "", 
     ylab = "相関係数",
     main = "Box-Cox 線形性プロット")
mtext(expression(lambda),side = 1,line=1)

### 相関係数絶対値が大きいλを取得####
max_abs_idx <- which.max(abs(cor_values))
### λ値を取得し表示####
mtext(paste0("最大λ値 = ",lambdas[max_abs_idx]),side=1, line=2,cex=0.9)

# 変換後線形近似####
# 上記のプロットとは別に、データを与え、計算してラムダを求めてプロット

## 最適なlambdaでデータを変換####
#Box-Cox変換関数の定義
boxcox_trans <- function(y, lambda) {
  if (abs(lambda) < 1e-7) {
    return(log(y))
  } else {
    return((y^lambda - 1) / lambda)
  }
}

xt <- boxcox_trans(data$Temperature, lambdas[max_abs_idx])

## 線形モデルの作成####
model <- lm(data$Density ~ xt)
res_sd <- summary(model)$sigma # 残差標準偏差を取得

# 変換後データのプロット####
plot(xt, data$Density, 
     pch = 16, cex = 0.8,         # 白抜きの点
     xlab = "", ylab = "",        # 軸ラベルを空に
     main = "変換データの線形近似")

#
axis(1, at = seq(0, 800, by = 100), labels = FALSE)
axis(1, at = seq(0, 800, by = 200), labels = seq(0, 800, by = 200), tick = FALSE)
axis(2, at = seq(992, 1002, by = 1), labels = FALSE)
axis(2, at = seq(992, 1002, by = 2), labels = seq(992, 1002, by = 2), tick = FALSE)

## 回帰線の追加####
# xtの最小値と最大値を取得
xt_endpoints <- range(xt, na.rm = TRUE)

# 2点の y の予測値をモデルから計算し描画
y_pred <- predict(model, newdata = data.frame(xt = xt_endpoints))
lines(xt_endpoints, y_pred, col = "blue", lwd = 1)

## 残差標準偏差を表示####
mtext(paste("残差標準偏差 =", round(res_sd, 3)), 
      side = 1, line = 1.5, cex = 0.9)



