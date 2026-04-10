# NIST EDA 1.3.3.20.Mean Plot####
# Date: 20260410
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33k.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/meanplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/DRAFT69.DAT
# 説明 ####
# 

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2,1), 
    mgp = c(1.8,0.5,0.0), 
    xaxs = "r", yaxs = "r",
    tck = 0.01)

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/DRAFT69.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Rank"," Day_of_Year", "Month")

# 前処理####
## 全データ平均####
all_mean <- mean(data$Rank)
## 月次平均####
# MonthとRank列のリスト
monthly_avg <- aggregate(Rank ~ Month, data = data, FUN = mean, na.rm = TRUE)

# 描画####
plot(monthly_avg, 
     type = "o", pch = 16, cex = 0.8, col = "blue",
     xlab = "", xaxt = "n",
     ylab = "",
     main = "平均プロット"
     )
axis(side = 1, at = monthly_avg$Month, labels = monthly_avg$Month)
mtext("月", side = 1, line = 1.8)
mtext("平均ランク", side = 2, line = 2,las = 3)

lines(c(1, 12),c(all_mean,all_mean),col = "red", lty = 2)

# 描画設定戻し####
par(original_par)
