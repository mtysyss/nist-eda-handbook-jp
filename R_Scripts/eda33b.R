# NIST EDA 1.3.3.11.DOE Scatter Plot####
# Date: 20260406
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33b.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/dexsplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/BOXBIKE2.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.11.DOE 散布図
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
# パッケージの読み込み####
library(lattice)

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/BOXBIKE2.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Y","X1","X2","X3","X4","X5","X6","X7")

# データを縦長に変換####
long_data = reshape(data, 
               direction = "long", 
               varying = 2:8, 
               v.names = "Level", 
               timevar = "Factor", 
               times = colnames(data)[2:8])

# stripplot：Y軸ID####
print(lattice::stripplot(Y ~ Level | Factor, 
          data = long_data,
          layout = c(7, 1), 
          pch = 16, 
          col = "dodgerblue", 
          strip = strip.custom(bg = "lightblue"), 
          main = "DOE 散布図",
          xlab = "因子水準",
          ylab = "Y (ID)",
          xlim = c(-1.8, 1.8),
          scales = list(x = list(at = c(-1, 0, 1), # X軸目盛を-1, 1 に固定
                                 alternating = 1), # X軸目盛表示を下側に統一
                        tck = c(-0.5,-0.5)) # 目盛を内向きに

        )
  )
# stripplot：Y軸応答値####
print(xyplot(Y ~ Level | Factor, # 
       data = long_data,
       layout = c(7, 1), 
       #tck = 1,
       pch = 16, 
       col = "dodgerblue", 
       strip = strip.custom(bg = "lightblue"), 
       main = "DOE 散布図",
       xlab = "因子水準",
       ylab = "Y (応答値)",
       xlim = c(-1.8, 1.8),
       scales = list(x = list(at = c(-1, 0, 1), # X軸目盛を-1, 1 に固定
                              alternating = 1), # X軸目盛表示を下側に統一
                     tck = c(-0.5,-0.5)), # 目盛を内向きに
       # パネル関数を用いて平均線を描く
       panel = function(...) {
         panel.stripplot(...) # 本体のプロットを描画
         panel.abline(h = mean(long_data$Y), lty = 2, col = "red") # 総平均の水平線
       })
      )
par((original_par))
