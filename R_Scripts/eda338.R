# NIST EDA 1338 Complex Demodulation Amplitude Plot ####
# Date: 20260402
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda338.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/compdeam.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/LEW.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.8の複素復調振幅プロット
# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.6,0.2,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/LEW.DAT"
data <- read.table(url,skip=25)
# 列名の割り当て
colnames(data) <- c("Deflection")

y <- data$Deflection

# 複素復調振幅####
# swdftパッケージを利用####
if(!require(swdft)) install.packages("swdft")

nist_amplitude_plot_swdft <- function(y, k, smooth_param = "butterworth", window_size = 5) {
  
  # 1. 複素復調の実行
  z_smooth <- swdft::complex_demod(y, f0 = k, smooth_param, order = window_size)
  
  # 2. 振幅の計算 (Modで絶対値を取得し、実信号の振幅として2倍する)
  amp_nist <- 2 * Mod(z_smooth$demod$y_smooth)
  
  # 3. プロット
  t_axis <- 1:length(y)
  valid_idx <- which(!is.na(amp_nist))
  
  plot(t_axis[valid_idx], amp_nist[valid_idx], 
       type = "l", # 振幅の変化を見やすくするため線グラフ(l)を推奨
       col = "blue",
       ylim = c(0, max(amp_nist[valid_idx])*1.04),
       xlab = "時刻", ylab = "振幅の推定値", 
       main = paste("複素復調振幅 swdft: F =", round(k, 4), 
                    ifelse(smooth_param == "butterworth", "", paste(", 平滑化窓：", window_size))))
}

# 実行例
nist_amplitude_plot_swdft(y, k, "ma", 10)
#nist_amplitude_plot_swdft(y, k)
# par設定の戻し####
par(original_par)