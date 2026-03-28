# NIST EDA 13311 Autocorreleation Plot: Random Data ####
# Date: 20260328
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda3311.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/autocop1.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/RANDN.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.1.1の自己相関プロット：無作為データ
# R標準ライブラリでのスクリプトをベースに描画調整しています。調整部分は
# "#<-で注意書きを記しています"
# テキストは信頼区間線分は2種類設定されていますが、R標準ライブラリでの
# デフォルト設置は１種類です。２種類線分を描く場合には別途追加する必要
# があります。

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.8,0.5,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/RANDN.DAT"
data0 <- read.table(url,skip=25)
data <- c(t(data0)) # 10列50行データを1列にする

# 自己相関プロットの作成 ####
# lag.max = 250 でラグの範囲を指定
# main, xlab, ylab でラベルを画像に合わせる
acf(data, 
    lag.max = 50, 
    main = "", #<- タイトル位置を近づけるために別関数で設定しています
    xlab = "ラグ", 
    ylab = "自己相関",
    col = "deepskyblue", #<- メインプロットの色設定
    ci = 0.95, #<- 信頼区間設定
    ci.col = "red" #<- 信頼区間線分の色設置絵
)

## タイトルの作成 ####
title(main = "自己相関プロット：無作為データ", line = 1) #<- タイトル位置修正

# 環境の呼び戻し ####
on.exit(par(original_par))

