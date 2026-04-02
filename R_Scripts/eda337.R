# NIST EDA 1337 Box Plot ####
# Date: 20260402
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda337.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/boxplot.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/SPLETT2.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.7の箱ひげ図
# 
# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.6,0.2,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/SPLETT2.DAT"
data <- read.table(url,skip=25)
# 列名の割り当て
colnames(data) <- c("Energy","Machine")
y <- data$Energy
x <- data$Machine

# 箱ひげ図の描画####
boxplot(y~x,
        ylim = c(60,80),yaxs = "i",
        ylab="エネルギー",xlab="機械",
        boxwex = 0.5, # 箱の幅の調整
        col = "skyblue")
title("箱ひげ図")

# par設定の戻し####
par(original_par)