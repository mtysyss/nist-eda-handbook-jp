# NIST EDA 1.3.3.22.Probability Plot####
# Date: 20260412
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33m.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/probplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/RANDWEIB.DAT
# 説明 ####
# 分布関数と引数を指定して確率プロットを出力する。。
# 分布名	        関数名 (q_func)	主な引数 (パラメータ)
# 正規分布	      qnorm	          mean (平均), sd (標準偏差)
# ワイブル分布    qweibull	      shape (形状), scale (尺度) デフォルトの場合は位置母数はない
# 指数分布	      qexp	          rate (レート = 1/平均)
# ガンマ分布	    qgamma	        shape (形状), rate または scale
# 対数正規分布    qlnorm	        meanlog (対数の平均), sdlog (対数の標準偏差)
# t分布	          qt	            df (自由度)
# F分布	          qf	            df1, df2 (自由度)
# カイ二乗分布    qchisq	        df (自由度)
# ベータ分布	    qbeta	          shape1, shape2
# 一様分布	      qunif	          min (最小), max (最大)
# ロジスティック分布	qlogis	    location, scale
# コーシー分布	  qcauchy	        location, scale

# プロット関数定義####
plot_prob_dist <- function(data, q_func, params = list(), main_title = "Probability Plot") {
  # 1. データの準備
  sorted_data <- sort(data)
  n <- length(data)
  p <- ppoints(n)
  
  # 2. 理論的クォンタイルの計算
  # do.callを使って、指定された関数にパラメータリストを渡す
  theoretical_quantiles <- do.call(q_func, c(list(p), params))
  
  # 3. プロットの実行
  plot(theoretical_quantiles, sorted_data,
       main = main_title,
       xlab = "理論分位点",
       ylab = "順序応答（データ）",
       pch = 20, cex = 0.8, col = "blue")
  
  # 理想的な直線（45度線）を赤の破線で引く
  abline(0, 1, col = "red", lty = 2)
  
  #grid() # グリッド線を追加
}

# データの読込####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/RANDWEIB.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Y")

# 分布条件設定####
shape_param <- 2
scale_param <- 1
location_param <- 0 # デフォルトのqwuibull()は引数として持たない

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2,1), 
    mgp = c(1.8,0.5,0.0), 
    xaxs = "r", yaxs = "r",
    las = 1,
    tck = 0.01)

# 描画####
plot_prob_dist(data$Y, 
               qweibull, 
               list(shape = shape_param, scale = scale_param), 
               "Weibull 確率プロット")

# 描画条件戻し####
on.exit(par(original_par))