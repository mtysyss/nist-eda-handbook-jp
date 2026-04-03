# NIST EDA 1.3.3.27.1.Spectral Plot: Random Data ####
# Date: 20260403
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33r1.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/spectrum1.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/NORMAL2.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.27のスペクトル・プロット：乱数データ
# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.6,0.2,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更
    
# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/NORMAL2.DAT"
data <- read.table(url,skip=25)
# 列名の割り当て
colnames(data) <- c("Y")

y <- data$Y

# スペクトル密度の計算とプロット####
# spec.pgram 関数を使用
# detrend=TRUE: トレンドを除去
# log="no": Y軸を対数スケールにしない）
spec_res <- spec.pgram(y, #xaxs = "i", yaxs = "i", 
                       log = "no", 
                       detrend = TRUE,  # トレンド除去
                       taper = 0,       # データの端の加工（テーパリング）を0にする
                       fast = FALSE,     # データ数を2の累乗に調整
                       spans = c(5,5),  # 平滑化の設定
                       main = "スペクトル", 
                       sub = "", # コメントアウトするとバンド幅がX軸ラベルの下に表示される
                       xlab = "周波数(観測あたりのサイクル)", 
                       ylab = "スペクトル強度",
                       col = "blue", lwd = 2)

# mtext("スペクトル強度", side = 2, line = 4, las = 3)
# ピーク周波数の確認####
# 最もスペクトル密度が高い周波数を特定
max_freq <- spec_res$freq[which.max(spec_res$spec)]

par(original_par)

