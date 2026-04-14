# NIST EDA 1.3.3.28.Standard Deviation Plot####
# Date: 20260414
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33s.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/sdplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/PBF11.DAT
# 説明 ####
# 
# データの読込####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/PBF11.DAT"
header_row <- read.table(url, skip = 48, nrows = 1, stringsAsFactors = FALSE)
data <- read.table(url, skip=50)
colnames(data) <- c("YEAR","DAY","Sumple Bottle", "SD", "FREON","FLAG","WV","CO2") #as.character(header_row)

# デフォルト環境の保存と調整####
old_par <- par(no.readonly = TRUE)
on.exit(par(old_par)) # 終了時に設定を戻す

# 前処理####
# Day of Year から日付を計算
dates <- as.Date(data$DAY - 1, origin = paste0(data$YEAR, "-01-01"))
data$MONTH <- as.numeric(format(dates, "%m"))

## 標準偏差（SD）の計算####
# 月ごとのSD (1〜12月)
# tapplyを使ってMONTHごとにWVのsdを計算
monthly_sd <- tapply(data$WV, data$MONTH, sd)
# 全体のSD
total_sd <- sd(data$WV)

# 描画####
## 設定####
x_label <- "月"
y_label <- "標準偏差(WATER VAPOR)"

## Y軸桁数確認####
max_digits <- nchar(as.character(max(abs(round(monthly_sd,4)), na.rm = TRUE)))

## 余白設定####
par(mar = c(3, max_digits*0.8 , 2, 1),
    mgp = c(1.5,0.5,0.0), 
    las = 1,
    tck = 0.01)

## 1〜12月の範囲で描画####
plot(1:12, monthly_sd, type = "p", pch = 19, col = "blue", cex = 0.8,
     xlab = "", xaxt = "n",
     ylab = "",
     main = "標準偏差プロット",
     ylim = c(0, max(c(monthly_sd, total_sd), na.rm = TRUE) * 1.2))

## ラベル描画####
axis(side = 1, at = 1:12, labels = 1:12)
mtext("月", side = 1, line = 1.8)
mtext(y_label, side = 2, line = max_digits*0.5 + 0.2, las = 3)

## 全体SDを水平線で表示
lines(c(1,12),c(total_sd,total_sd), col = "red", lty = 2, lwd = 1)
