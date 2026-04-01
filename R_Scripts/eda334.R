# NIST EDA 1334 Bootstrap Plot ####
# Date: 20260401
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda334.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/bootplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/RANDU.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.4のブートストラップ・プロット
# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.8,0.5,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# 値生成のためのパッケージ読み込み ####
library(boot)

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/RANDU.DAT"
data0 <- read.table(url,skip=25)
data <- c(t(data0)) # 10列50行データを1列にする

# ブートストラップの計算 ####
# 1.4.2.2. 事例研究 一様無作為数の RCodeから抜粋
## Bootstrap and CI for mean.  d is a vector of integer indexes
samplemean <- function(x, d) {
  return(mean(x[d]))                   
}
b1 = boot(data, samplemean, R=500)   
z1 = boot.ci(b1, conf=0.9, type="basic")
meanci = paste("90% CI: ", "(", round(z1$basic[4],4), ", ", 
               round(z1$basic[5],4), ")", sep="" )

## Bootstrap and CI for median
samplemedian <- function(x, d) {
  return(median(x[d]))
}   

b2 = boot(data, samplemedian, R=500)
z2 = boot.ci(b2, conf=0.90, type="basic")
medci = paste("90% CI: ", "(", round(z2$basic[4],4), ", ", 
              round(z2$basic[5],4), ")", sep="" )

## Bootstrap and CI for midrange
samplemidran <- function(x, d) {
  return( (max(x[d])+min(x[d]))/2 )
}

b3 = boot(data, samplemidran, R=500)   
z3 = boot.ci(b3, conf=0.90, type="basic")
midci = paste("90% CI: ", "(", round(z3$basic[4],4), ", ", 
              round(z3$basic[5],4), ")", sep="" )


# プロット####
par(mfrow=c(2,3),par(yaxs="r"))
plot(b1$t,type="l",xlab="",ylab="",main=meanci)
plot(b2$t,type="l",xlab="",ylab="",main=medci)
plot(b3$t,type="l",xlab="",ylab="",main=midci)

# ヒストグラムは、描画を調整
par(yaxs="i")
h1 <- hist(b1$t,breaks = 25, plot = FALSE)
max_y1 <- max(h1$counts) * 1.1
hist(b1$t,breaks = 25, ylim = c(0, max_y1), main="Bootstrap Mean",xlab="",ylab="", xlim = c(0.45,0.55))
box()

h2 <- hist(b2$t,breaks = 25, plot = FALSE)
max_y2 <- max(h2$counts) * 1.1
hist(b2$t,breaks = 25, ylim = c(0, max_y2),main="Bootstrap Median",xlab="",ylab="", xlim = c(0.45,0.55))
box()

h3 <- hist(b3$t,breaks = 25, plot = FALSE)
max_y3 <- max(h3$counts) * 1.1
hist(b3$t,breaks = 25, ylim = c(0, max_y3),main="Bootstrap Midrange",xlab="",ylab="", xlim = c(0.45,0.55))
box()
par(original_par)
