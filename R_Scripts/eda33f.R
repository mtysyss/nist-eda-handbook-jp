# NIST EDA 1.3.3.15.Lag plot####
# Date: 20260408
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# base page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33f.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/lagplot.htm
# Data URL:
#   --
# 説明 ####
# NIST Statistic Handbook 1.3.3.15.遅延プロット
# 1.3.3.15の遅延プロットと関連ページの描画条件を含んでいます。
# statsパッケージのlag.plot()は軸範囲が指定できず、1つずらしたデータを作成し
# plot()でプロットしています。
# テキストの表記のうち、縦軸、横軸が表示、説明文と実際のデータが入れ替わって
# います。

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,4,2,1), 
    mgp = c(1.8,0.5,0.0), 
    xaxs = "i", yaxs = "i",
    las = 1, 
    tck = 0.01)

# データの読み込み ####
## 33f####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/MAVRO.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Y")
xy_range <- c(2.0010,2.0030)
par(mar = c(3,4.5,2,1.5))
ylab_line <- 3
## 33f1####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/NORMAL2.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xy_range <- c(-4,3)
#par(mar = c(3,3,2,1))
#ylab_line <- 1.5
## 33f2####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/FLICKER.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xy_range <- c(-0.02,0.02)
#par(mar = c(3,3,2,1))
#ylab_line <- 2
## 33f3####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/RANDWALK.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xy_range <- c(-2,8)
#par(mar = c(3,3,2,1))
#ylab_line <- 1.8
## 33f4####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/LEW.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xy_range <- c(-675,375)
#par(mar = c(3,4,2,1))
#ylab_line <- 2.5

# データ処理####
n <- length(data$Y)
y_im1 <- data$Y[1:(n-1)]
y_i <- data$Y[2:n]

# 描画####
plot(y_im1, y_i, 
     xlim = xy_range, 
     ylim = xy_range, 
     pch = 16,
     col = "black",
     ann = FALSE, 
     axes = TRUE  
)
# タイトル、ラベル表示####
# 目盛ラベルの桁数の関係でmtext()で表示
mtext("遅延プロット", side = 3, line = 0.8, cex = 1.2)
mtext(expression(Y[i-1]), side = 1, line = 2)
mtext(expression(Y[i]), side = 2, line = ylab_line, las = 3)