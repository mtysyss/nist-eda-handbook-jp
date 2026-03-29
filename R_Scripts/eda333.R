# NIST EDA 1333 BlockPlot ####
# Date: 20260329
# Created by MATSUYOSHI Yasushi PCCPMDEV.JP
# Source: 
# page URL: 
#   https://www.itl.nist.gov/div898/handbook/eda/section3/eda333.htm
#   https://www.itl.nist.gov/div898/handbook/eda/section3/blockplo.htm
# Data URL:
#   https://www.itl.nist.gov/div898/handbook/datasets/SHEESLE2.DAT
# 説明 ####
# NIST Statistic Handbook 1.3.3.3のブロック・プロット
# データなしのプロットエリアを描画しておき、rect()でボックスを描画する
# ボックスのグルーピングはマニュアルで調整が必要です。
# 

# デフォルト環境の保存と調整 ####
original_par <- par(no.readonly = TRUE)
par(mar = c(3,3,2.5,1), # プロットエリア外周余白の調整
    mgp = c(1.8,0.5,0.0), # 軸ラベル、目盛ラベル、目盛描画位置の調整
    las = 1, # 目盛ラベル記載向きを水平に変更
    tck = 0.02) # 目盛線を内向きに変更

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/SHEESLE2.DAT"
data <- read.table(url,skip=25)

## データの生成 ####
# 列名の割り当て
colnames(data) <- c("Defects","Weld","Plant","Speed","Shift","Tag(2*3*4)")

### データの準備 ####
blocks <- interaction(data$Shift, data$Speed, data$Plant) # 順番を変えるとグループ化が変わります
n_blocks <- nlevels(blocks)

###  間隔の調整 ####
# ボックス同士の間隔を 0.5 (元の半分) に設定
# グループ内の位置を 0, 0.5, 1.0 ... とし、グループ間にはさらに 1.0 空ける計算
group_size <- nlevels(factor(data$Shift))# blocks interactionの引数順番を変えたら、ここも変える
step <- 0.5  # ボックスの間隔（1.0から0.5に変更）
gap  <- 0.5  # グループ間の空きスペース

### 各ボックスの描画位置 (x座標) を計算 ####
# (i-1) %% group_size でグループ内順序、floor() で何グループ目かを判定
x_pos <- numeric(n_blocks) 
for(i in 1:n_blocks) {
  g_idx <- floor((i-1) / group_size) # 何グループ目か (0, 1, 2...)
  b_idx <- (i-1) %% group_size        # グループ内の何番目か (0, 1, 2)
  x_pos[i] <- (g_idx * (group_size * step + gap)) + (b_idx * step) + 1
}

# 描画 ####
## プロットエリアの初期化 ####
plot(1, type="n", 
     xlim=c(min(x_pos)-0.5, max(x_pos)+0.5), 
     ylim=c(10, 45),
     xaxt="n", 
     xlab="工場 (2) x 速度 (2) x シフト (3)", # blocks interactionの引数順番を変えたら、ここも変える
     ylab="時間あたりの平均欠陥数", 
     main="ボックス・プロット")

## 各ブロックの描画 ####
for(i in 1:n_blocks) {
  sub_data <- data[blocks == levels(blocks)[i], ]
  val1 <- sub_data$Defects[sub_data$Weld == 1]
  val2 <- sub_data$Defects[sub_data$Weld == 2]
  
  current_x <- x_pos[i] # X軸位置を設定
  
  ## 長方形を描画 (幅も少し細く 0.15 に調整) ####
  rect(current_x - 0.15, min(val1, val2), current_x + 0.15, max(val1, val2))
  
  ## 水準番号の描画 ####
  text(current_x, val1, "1", pos=ifelse(val1 > val2, 3, 1), offset=0.2, cex=0.8)
  text(current_x, val2, "2", pos=ifelse(val2 > val1, 3, 1), offset=0.2, cex=0.8)
}
text(x = 0.5, y = 45, labels = "プロット文字 = 溶接法 (2)", font = 1, adj = 0)
# 環境の呼び戻し ####
on.exit(par(original_par))
