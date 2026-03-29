# NIST EDA 1332 Bihistogram ####
# Date: 20260329
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda332.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/bihistog.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/JAHANMI2.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.2の対比ヒストグラム
# R Hmiscパッケージにhistbackback()で対比ヒストグラムが描画できますが、
# テキストの描画に対し反時計回りに90°回転したグラフになります。
# 本スクリプトはR標準ライブラリでのスクリプトをベースに2つのヒストグ
# ラムを描画して調整しています。

# 必要なパッケージの読み込み####
library(Hmisc)

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.8,0.5,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/JAHANMI2.DAT"
data <- read.table(url,skip=50)

## データの生成 ####
# 列名の割り当て
colnames(data) <- c("Id","Lab","Num","Test","Y","X1","X2","X3","X4","Trt","Set","Llab","Rep","Bat","Sblab","Set2")

## バッチ番号に基づいてデータをフィルタリング ####
# Batch列の値が 1 の行から Strength を抽出
batch1 <- data$Y[data$Bat == 1] #split(data, data$Bat)[[1]]$Y

## Batch列の値が 2 の行から Y:Strength を抽出####
batch2 <- data$Y[data$Bat == 2] #split(data, data$Bat)[[2]]$Y

## ヒストグラムの計算 (描画はせず、統計量のみ取得)####
# 両方のデータが含まれるようにブレイクポイント（区切り）を共通化
breaks <- seq(200, 1100, by = 25)
h1 <- hist(batch1, breaks = breaks, plot = FALSE)
h2 <- hist(batch2, breaks = breaks, plot = FALSE)

# 描画設定####
## batch 1 (上向き) の描画####
# yaxs="i" で軸の無駄な余白を消し、ylimで上下の範囲を指定
bp1 <- barplot(h1$counts, 
               space = 0, 
               ylim = c(-60, 60), #<- 図を正しく描画するために範囲指定
               axes = FALSE, 
               col = "white",
               border = "black",
               main = "",
               ylab = "頻度",
               xlab = "セラミック強度")

## batch 2 (下向き) の描画####
# countsをマイナスにして重ね書き (add = TRUE)
barplot(-h2$counts, 
        space = 0,
        add = TRUE, 
        axes = FALSE, 
        col = "white", 
        border = "black")

# 軸と装飾の追加####
# X軸 (階級ラベル)
at_indices <- seq(1, length(breaks), by = 2) # 目盛50ごと
axis(1, at = bp1[at_indices], labels = breaks[at_indices])

## Y軸####
axis(2, at = seq(-60, 60, by = 10), labels = abs(seq(-60, 60, by = 10)), las = 1)
## プロットエリア枠 ####
box()

## テキストラベル####
text(x = 1, y = 50, labels = "batch 1", font = 2, adj = 0)
text(x = 1, y = -50, labels = "batch 2", font = 2, adj = 0)
#mtext("JAHANMI2.DAT", side = 1, line = 4, adj = 1, cex = 0.7)

## タイトルの作成 ####
title(main = "対比ヒストグラム", line = 1) #<- タイトル位置修正

# 環境の呼び戻し ####
on.exit(par(original_par))
