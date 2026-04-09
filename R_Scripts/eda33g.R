# NIST EDA 1.3.3.16.~19. Linear XXX Plot####
# Date: 20260409
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
# 16:   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33g.htm
# 17:  https://www.itl.nist.gov/div898/handbook/eda/section3/eda33h.htm
# 18:  https://www.itl.nist.gov/div898/handbook/eda/section3/eda33i.htm
# 19:  https://www.itl.nist.gov/div898/handbook/eda/section3/eda33j.htm
#
# 16:  https://www.itl.nist.gov/div898/handbook/eda/section3/linecorr.htm
# 17:  https://www.itl.nist.gov/div898/handbook/eda/section3/lineinte.htm
# 18:  https://www.itl.nist.gov/div898/handbook/eda/section3/lineslop.htm
# 19:  https://www.itl.nist.gov/div898/handbook/eda/section3/linressd.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/HSU12.DAT
# 説明 ####

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,5,2,1), 
    mgp = c(1.8,0.5,0.0), 
    xaxs = "r", yaxs = "r",
    las = 1, 
    tck = 0.01)

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/HSU12.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Y","X", "Batch") # c("時刻","距離", "バッチ")

# 線形解析####
## 全データ解析####
all_fit <- lm(Y ~ X, data = data)
all_sum <- summary(all_fit)
### 全データ係数####
all_stats <- c(
  all_sum$r.squared,   # 相関係数(R2)
  coef(all_fit)[1],    # 切片
  coef(all_fit)[2],    # 傾き
  all_sum$sigma        # RESSD
)

## バッチ解析####
out = by(data,data$Batch,function(x) lm(Y~X,data=x))
outs = sapply(out,summary)
outc = sapply(out,coef)
id = c(1:length(out))
## 線形相関 1.3.3.16#### 
r2 = matrix(outs[8,], ncol = 1, dimnames = list(NULL, "相関"))
## 線形切片 1.3.3.17####
b0 = matrix(outc[1,], ncol = 1, dimnames = list(NULL, "切片")) 
## 線形傾き 1.3.3.18####
b1 = matrix(outc[2,], ncol = 1, dimnames = list(NULL, "傾き")) 
## 線形残差標準偏差 1.3.3.19####
fitse = matrix(outs[6,], ncol = 1, dimnames = list(NULL, "RESSD"))

plot_data <- cbind(r2, b0, b1, fitse)

# 描画####
xax2 = "バッチ番号"
for (i in 1:ncol(plot_data)) {
  # 全データと基準線を合わせた範囲を計算
  y_range <- range(c(plot_data[, i], all_stats[i]), na.rm = TRUE)
  
  plot(id, plot_data[, i], 
       xlab = xax2,
       ylab = "",
       ylim = y_range,
       main = paste0("線形",colnames(plot_data)[i],"プロット"), # タイトルもつけると分かりやすい
       type = "o", pch = 16, cex = 1,col = "blue", lty = 2,
       xaxt = "n"
       )
  # X軸を1刻みで描画
  axis(side = 1, at = id, labels = id)
  # Y軸ラベルを描画
  mtext(paste(colnames(plot_data)[i],"(Y,X)"), side = 2, line = 3.5, las = 3)
  # 基準線描画
  lines(c(1,max(id)) , c(all_stats[i],all_stats[i]), col = "red", lty = 2 )
}

# 描画設定の戻し####
par(original_par)