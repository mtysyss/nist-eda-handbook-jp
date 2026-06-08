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
par(mfrow = c(2, 1),
    mar = c(3,3,2,1), 
    mgp = c(1.6,0.5,0.0), 
    las = 1, 
    tck = 0.02)

# データの読み込み ####
url <- "https://www.itl.nist.gov/div898/handbook/datasets/LEW.DAT"
data <- read.table(url, skip=25)
colnames(data) <- c("Deflection")

y <- data$Deflection
n <- length(y)
t <- 1:n

#スペクトル密度の計算####
spec_res <- spec.pgram(y, log = "no", detrend = TRUE, taper = 0, fast = FALSE, spans = c(3,3), plot = FALSE)
## 複素復調計算の初期値####
# initial_freqを定数にするとテキストの鋸状プロットが再現できます。
# スペクトル解析で周波数を特定しているため、ある程度最適な初期値になっています。
# 最適周波数から一定値以上外れると近似ができなくなり、修正後が水平になりません。
#initial_freq <- spec_res$freq[which.max(spec_res$spec)] 
initial_freq <- 0.3015
#複素復調 (Complex Demodulation)####
z <- y * exp(complex(imaginary = -2 * pi * initial_freq * t))

## 平滑化窓設定####
window_size <- 20
z_smooth <- complex(
  real = as.numeric(stats::filter(Re(z), rep(1/window_size, window_size), sides = 2)),
  imaginary = as.numeric(stats::filter(Im(z), rep(1/window_size, window_size), sides = 2))
)

## 位相の抽出とラッピング (±pi/2)と近似####
# NISTのテキスト通り atan(Im/Re) に相当する ±pi/2 の範囲
# (Arg(z) は ±pi なので、piで割った余りを利用して ±pi/2 に変換)
phase_raw <- ((Arg(z_smooth) + pi/2) %% pi) - pi/2

# 回帰分析用には unwrap した連続位相（傾きを正しく出すため）
is_valid <- !is.na(Arg(z_smooth))
phase_continuous <- signal::unwrap(Arg(z_smooth)[is_valid])
fit <- lm(phase_continuous ~ t[is_valid])

# 傾きから周波数を修正
slope <- coef(fit)[2]
intercept <- coef(fit)[1]
f_final <- initial_freq + (slope / (2 * pi))

# 周波数修正後の再計算####
z_final <- y * exp(complex(imaginary = -2 * pi * f_final * t))
z_smooth_final <- complex(
  real = as.numeric(stats::filter(Re(z_final), rep(1/window_size, window_size), sides = 2)),
  imaginary = as.numeric(stats::filter(Im(z_final), rep(1/window_size, window_size), sides = 2))
)
## 修正後 ±pi/2 でラッピング####
phase_final <- ((Arg(z_smooth_final) + pi/2) %% pi) - pi/2

# プロット####
## 上段：初期周波数####
plot(t, phase_raw, type = "p", col = "red", cex = 0.5,
     ylim = c(-2, 2),
     main = paste("初期位相プロット\n (f =", round(initial_freq, 4), ")"),cex.main=0.8,
     ylab = "位相 (±π/2)", xlab = "")

## 下段：修正後周波数####
plot(t, phase_final, type = "p", col = "darkgreen", cex = 0.5,
     ylim = c(-2, 2),
     main = paste("修正位相プロット\n (f =", round(f_final, 5), ")"),cex.main=0.8,
     ylab = "位相 (±π/2)", xlab = "時刻")

par(original_par)

# テキストのグラフ####
# NIST Dataplot Loop Reproduction ####
# 0.28から0.3176まで 0.0025刻みで複素復調位相プロットを表示

# 描画設定：4x4のタイル状に配置
original_par <- par(no.readonly = TRUE)
par(mfrow = c(4, 4), 
    mar = c(2, 2, 1.5, 0.5), # 各グラフの余白を小さく
    mgp = c(1.2, 0.3, 0), 
    tck = 0.02, 
    cex.main = 0.8, 
    las = 1)

# ループの設定 (Dataplotの loop for k = .28 .0025 .3176 に相当)
freq_list <- seq(0.28, 0.3176, by = 0.025 / 10) # 0.0025だと16個にならないため調整
# ※NISTの刻み幅0.0025だと (0.3176-0.28)/0.0025 = 約15回なので、16分割に最適化
freq_list <- seq(0.28, 0.3175, length.out = 16)

window_size <- 20

for (k in freq_list) {
  # 1. 複素復調 (Mixing)
  z <- y * exp(complex(imaginary = -2 * pi * k * t))
  
  # 2. 低域通過フィルタ (Smoothing)
  z_smooth <- complex(
    real = as.numeric(stats::filter(Re(z), rep(1/window_size, window_size), sides = 2)),
    imaginary = as.numeric(stats::filter(Im(z), rep(1/window_size, window_size), sides = 2))
  )
  
  # 3. NIST仕様の位相計算 (±pi/2 制限)
  # atan(Im/Re) 相当のラッピング
  phase_nist <- ((Arg(z_smooth) + pi/2) %% pi) - pi/2
  
  # 4. プロット
  plot(t, phase_nist, type = "p", pch = 16, cex = 0.3, col = "black",
       ylim = c(-pi/2, pi/2), 
       xlab = "", ylab = "", 
       main = paste("F =", round(k, 4)))
}

# 設定を元に戻す
par(original_par)