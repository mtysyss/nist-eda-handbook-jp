# NIST EDA 1.3.3.9.Complex Demodulation Phase Plot####
# Date: 20260403
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda339.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/compdeph.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/LEW.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.9の複素復調位相プロット
# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2,1), 
    mgp = c(1.6,0.5,0.0), 
    las = 1, 
    tck = 0.02)

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/LEW.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Deflection")

y <- data$Deflection
t <- 1:length(y)
## 複素復調計算の初期値####
k <- 0.3075 # 描画周波数の設定

#複素復調 (Complex Demodulation)####
# swdftパッケージを利用####
if(!require(swdft)) install.packages("swdft")

nist_phase_plot_swdft <- function(y, k,smooth_param = "butterworth" ,window_size = 5) {
  
  # 1. 複素復調の実行
  z_smooth <- swdft::complex_demod(y, f0 = k, smooth_param, order=window_size)
  
  # 2. NIST仕様の位相計算 (±pi/2 制限)
  phase_nist <- ((Arg(z_smooth$demod$y_smooth) + pi/2) %% pi) - pi/2
  
  # 3. プロット (NAを除外して x と y の長さを合わせる)
  t_axis <- 1:length(y)
  valid_idx <- which(!is.na(phase_nist))
  
  plot(t_axis[valid_idx], phase_nist[valid_idx], 
       type = "p", pch = 16, cex = 0.5, col = "blue",
       ylim = c(-2, 2), 
       xlab = "時刻", ylab = "位相の推定値", 
       main = paste("複素復調位相 swdft: F =", round(k, 4), ifelse(smooth_param == "butterworth", "", paste(", 平滑化窓：", window_size))))
 }

nist_phase_plot_swdft(y, k, "ma", 10)
# nist_phase_plot_swdft(y, k)
# 設定を元に戻す
par(original_par)