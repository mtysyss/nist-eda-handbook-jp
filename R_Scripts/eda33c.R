# NIST EDA 1.3.3.12.DOE Mean Plot####
# Date: 20260406
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33c.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/dexmeanp.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/BOXBIKE2.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.12.DOE 平均プロット
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2,1), 
    mgp = c(1.6,0.5,0.0), 
    las = 1, 
    tck = 0.02)
# パッケージの読み込み####
library(lattice)

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/BOXBIKE2.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Y","X1","X2","X3","X4","X5","X6","X7")

long_data <- reshape(data, 
                     direction = "long", 
                     varying = 2:8, 
                     v.names = "Level", 
                     timevar = "Factor", 
                     times = colnames(data)[2:8])

# 平均値を計算####
mean_data <- aggregate(Y ~ Level + Factor, data = long_data, mean)
grand_mean <- mean(long_data$Y)

# 枠組み描画####
plot(NULL, xlim=c(0.5, 7.5), ylim=range(mean_data$Y), 
     xaxt="n", xlab="因子", ylab="感度", main="DOE 平均プロット")
#rect(par("usr")[1], par("usr")[3], par("usr")[2], par("usr")[4], col = "lightyellow") # 背景色
abline(h = grand_mean, lty = 2, col = "red") # 総平均

# 因子ごとに線と点を描画####
factors <- unique(mean_data$Factor)
for(i in 1:length(factors)){
  sub <- mean_data[mean_data$Factor == factors[i], ]
  points(i + sub$Level*0.2, sub$Y, pch=16, col = "blue") # 少し横にずらして描画
  lines(i + sub$Level*0.2, sub$Y, col = "blue")
}
axis(1, at=1:7, labels=factors)

par((original_par))
