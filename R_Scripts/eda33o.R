# NIST EDA 1.3.3.24.Quantile-Quantile Plot####
# Date: 20260413
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33o.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/qqplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/JAHANMI2.DAT
# 説明 ####
# 
# データの読込####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/JAHANMI2.DAT"
data <- read.table(url, skip=50)
colnames(data) <- c("Id","Lab","Num","Test","Y","X1","X2","X3","X4","Trt","Set","Llab","Rep","Bat","Sblab","Set2")

# QQプロットの描画関数####
draw_batch_qq <- function(x_batch, y_batch, x_label = "Batch 2", y_label = "Batch 1") {
  
  # 桁数に応じた余白の計算
  max_digits <- nchar(as.character(max(abs(y_batch), na.rm = TRUE)))
  
  # デフォルト環境の保存と調整####
  old_par <- par(no.readonly = TRUE)
  on.exit(par(old_par)) # 終了時に設定を戻す
  # 余白設定####
  par(mgp = c(1.5,0.5,0.0), 
      las = 1,
      tck = 0.01)
  par(mar = c(3, max_digits*0.5 , 2, 1)) 
 
  # 範囲設定####
  x_range <- range(x_batch, na.rm = TRUE)
  y_range <- range(y_batch, na.rm = TRUE)
  y_limits <- range(c(y_range, x_range), na.rm = TRUE)
  
  # プロット####
  qqplot(x_batch, y_batch, 
         xlab = "", ylab = "", 
         ylim = y_limits,  # ここで範囲を固定
         main = "Q-Q Plot", 
         pch = 16, col = "blue", cex = 0.8,
         las = 1)
  
  # 基準線描画####
  segments(x0 = x_range[1], y0 = x_range[1], 
           x1 = x_range[2], y1 = x_range[2], 
           col = "red", lty = 2)
  
  # ラベル描画####
  mtext(x_label, side = 1, line = 1.8)
  mtext(y_label, side = 2, line = max_digits*0.3+0.2, las = 3)
}

# データの読み込み####
batches <- with(data, split(Y[Bat %in% 1:2], Bat[Bat %in% 1:2]))
# プロット####
draw_batch_qq(batches$`2`, batches$`1`)
