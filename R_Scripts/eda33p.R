# NIST EDA 1.3.3.25.Run-Sequence Plot####
# Date: 20260413
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33p.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/runseqpl.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/MAVRO.DAT
# 説明 ####
# 
# データの読込####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/MAVRO.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Y")

# デフォルト環境の保存と調整####
old_par <- par(no.readonly = TRUE)
on.exit(par(old_par)) # 終了時に設定を戻す

y_label <- "透過率"
y_lim_expand <- 0.2
r <- range(data$Y, na.rm = TRUE)
y_limits <- r + c(-y_lim_expand, y_lim_expand) * diff(r)

# Y軸桁数確認####
max_digits <- nchar(as.character(max(abs(data$Y), na.rm = TRUE)))

# 余白設定####
par(mar = c(3, max_digits*0.8 , 2, 1),
    mgp = c(1.5,0.5,0.0), 
    las = 1,
    tck = 0.01)

# プロット####
plot(data$Y,
     xlab = "インデックス", ylab = "", 
     ylim = y_limits,  
     main = "プロットY",
     pch = 16, col = "blue", cex = 0.8,
     las = 1)
# ラベル描画####
mtext(y_label, side = 2, line = max_digits*0.5 + 0.2, las = 3)
