# NIST EDA 1.3.3.21.~ 21.4 Normal Probability Plot####
# Date: 20260410
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
# 21.   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33l.htm
# 21.1  https://www.itl.nist.gov/div898/handbook/eda/section3/eda33l1.htm
# 21.2  https://www.itl.nist.gov/div898/handbook/eda/section3/eda33l2.htm
# 21.3  https://www.itl.nist.gov/div898/handbook/eda/section3/eda33l3.htm
# 21.4  https://www.itl.nist.gov/div898/handbook/eda/section3/eda33l4.htm
#
# 21    https://www.itl.nist.gov/div898/handbook/eda/section3/normprpl.htm
# 21.1  https://www.itl.nist.gov/div898/handbook/eda/section3/normprpl1.htm
# 21.2  https://www.itl.nist.gov/div898/handbook/eda/section3/normprpl2.htm
# 21.3  https://www.itl.nist.gov/div898/handbook/eda/section3/normprpl3.htm
# 21.4  https://www.itl.nist.gov/div898/handbook/eda/section3/normprpl4.htm
# Data URL:
# 21    https://www.itl.nist.gov/div898/handbook/datasets/NORMAL.DAT
# 21.1  https://www.itl.nist.gov/div898/handbook/datasets/ZARR13.DAT
# 21.2  https://www.itl.nist.gov/div898/handbook/datasets/TUKLAMB.DAT
# 21.3  https://www.itl.nist.gov/div898/handbook/datasets/RANDDEX.DAT
# 21.4  https://www.itl.nist.gov/div898/handbook/datasets/SUNSPOT.DAT
#
# 説明 ####
# qqnorm()で描画します。
# reference_line
#   1: 線形回帰、2: 最大値と最小値間
# 1.3.3.21.4 の基準線だけが描画条件が異なります。

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(4,3,2,1), 
    mgp = c(1.8,0.5,0.0), 
    xaxs = "r", yaxs = "r",
    las = 1,
    tck = 0.01)

# データの読み込み ####
# 21. ####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/NORMAL.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlabel <- "正規分布 N(0,1) の順序統計量の中央値"
#ylabel <- "順序応答値"
#title <- "正規確率プロット"
#ylab_line <- 1.5
#reference_line <- 1

# 21.1 ####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/ZARR13.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y") # Calibration Factor
#xlabel <- "理論値"
#ylabel <- "データ"
#title <- "熱流量計データ"
#par(mar = c(4,3.5,2,1))
#ylab_line <- 2.5
#reference_line <- 1

# 21.2 ####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/TUKLAMB.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlabel <- "理論値"
#ylabel <- "データ"
#title <- "Tukey-Lambda 乱数 (λ = 1.1)"
#ylab_line <- 2
#reference_line <- 1

# 21.3 ####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/RANDDEX.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y")
#xlabel <- "理論値"
#ylabel <- "データ"
#title <- "二重指数乱数"
#ylab_line <- 1.5
#reference_line <- 1

# 21.4 ####
#url <- "https://www.itl.nist.gov/div898/handbook/datasets/SUNSPOT.DAT"
#data <- read.table(url, skip=25)
#colnames(data) <- c("Y", "Month", "Year", "Monthly Average")
#xlabel <- "理論値"
#ylabel <- "データ"
#title <- "黒点データ"
#ylab_line <- 2
#reference_line <- 2

# 描画####
qq_res <- qqnorm(data$Y, 
                 pch = 16, cex = 0.8, col = "blue",
                 xlab = xlabel,
                 ylab = "",
                 main = title)
mtext(ylabel, side = 2, line = ylab_line, las =3)
## 係数解析####
correlation <- cor(qq_res$x, qq_res$y)
fit <- lm(qq_res$y ~ qq_res$x)
intercept <- coef(fit)[1]
slope <- coef(fit)[2]

## サブタイトル描画####
sub_text <- paste0(
  "相関係数: ", round(correlation, 3), 
  ", 切片: ", round(intercept, 3), 
  ", 傾き: ", round(slope, 3)
)
title(sub = sub_text, col.sub = "blue")

## 基準線####
if (reference_line == 1) {
  abline(intercept, slope, col = "red", lwd = 1, lty = 2)
} else if (reference_line == 2) {
  idx_min <- which.min(qq_res$y)
  idx_max <- which.max(qq_res$y)
  lines(c(qq_res$x[idx_min],qq_res$x[idx_max]),c(qq_res$y[idx_min],qq_res$y[idx_max]) ,
        col = "red", lwd = 1, lty = 2)
}

# 描画条件戻し####
on.exit(par(original_par))