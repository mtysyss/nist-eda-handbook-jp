# NIST EDA 1.3.3.14.Histogram####
# Date: 20260407
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# base page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33e.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/histogra.htm
# Data URL:
#   --
# 説明 ####
# NIST Statistic Handbook 1.3.3.14.ヒストグラム
# 1.3.3.14のヒストグラムと関連ページの描画条件を含んでいます。

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2,1), 
    mgp = c(1.6,0.5,0.0), 
    xaxs = "i", yaxs = "i",
    las = 1, 
    tck = 0.02)

# データの読み込み ####
## 33e####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/MICHELSO.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y","X1","X2","X3","X4")
#xlimits <- c(299.4,300.2)

## 33e1####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/ZARR13.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlimits <- c(9.1,9.4)

## 33e2####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/TUKLAMB.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlimits <- c(-4,4)

## 33e3####
# データURLが間違っている様な気がする
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/DZIUBA1.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("MONTH", "DAY", "YEAR", "Y")
#xlimits <- c(27.5,28.5)

## 33e4####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/LEW.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlimits <- c(-2000,2000)

## 33e5####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/ZARR14.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlimits <- c(8.9,9.5)

## 33e6####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/SUNSPOT.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y", "MONTH", "YEAR", "AVERAGWE")
#xlimits <- c(-200,300)

## 33e7####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/MORALES.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y", "RES2", "RES3", "FACTOR")
#xlimits <- c(22.5,23.1)


## 33e8####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/ZARR13.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlimits <- c(9,9.5)
#data <- rbind(data, 9.45, 9.45, 9.45, 9.45)

# 階級数設定####
n_break <- 25

# 最大カウント取得####
h1 <- hist(data$Y, breaks = n_break, plot=FALSE)
max_y <- max(h1$counts)
hist(data$Y, breaks = n_break, 
     xlim = xlimits, ylim = c(0, max_y * 1.05),
     col = "lightblue",
     main = "ヒストグラム",
     xlab = "Y", ylab = "カウント")
box()
