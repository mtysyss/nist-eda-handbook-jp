# NIST EDA 1.3.3.23.PProbability Plot Correlation Coefficient Plot####
# Date: 20260412
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# pages URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda33n.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/ppccplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/NORMAL.DAT
# 説明 ####
# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,4,2,1), 
    mgp = c(2.5,0.5,0.0), 
    #xaxs = "r", yaxs = "r",
    las = 1,
    tck = 0.01)

# データの読込####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/NORMAL.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Y")

# Tukey Lambda分布の分位関数定義####
# lambda が 0 の場合は Logistic 分布に近似
q_tukey <- function(p, lambda) {
  if (abs(lambda) < 1e-10) {
    return(log(p / (1 - p)))
  } else {
    return((p^lambda - (1 - p)^lambda) / lambda)
  }
}

# 形状パラメータ (lambda) の探索範囲設定####
# NISTの例では通常 -1 から 0.5 程度を探索
lambdas <- seq(-2, 2, length.out = 800) # 計算に供する点条件によりλ値は変わります

# 各lambda における PPCC (相関係数) を計算####
n <- length(data$Y)
p_points <- ppoints(n)  # (i - 0.5) / n 等の確率点
sorted_data <- sort(data$Y)

ppcc_values <- sapply(lambdas, function(l) {
  theoretical_quantiles <- q_tukey(p_points, l)
  return(cor(sorted_data, theoretical_quantiles))
})

# PPCCプロットの描画####
plot(lambdas, ppcc_values, type = "l", col = "blue",
     main = "(Tukey-Lambda)PPCC プロット",
     xlab = "",
     ylab = "相関係数")

# 最適形状係数の特定####
best_idx <- which.max(ppcc_values)
best_lambda <- lambdas[best_idx]
max_ppcc <- ppcc_values[best_idx]

# プロットに最適値を表示####
lines(c(best_lambda,best_lambda),c(0, ppcc_values[best_idx]), col = "red", lty = 2)
points(best_lambda, max_ppcc, col = "red", pch = 19)
mtext(paste("形状係数 λ" ,"；最適値 =", round(best_lambda, 3),"、相関係数 = ",round(max_ppcc,3)),
      side = 1, line = 1.8)
# 描画条件戻し####
on.exit(par(original_par))
