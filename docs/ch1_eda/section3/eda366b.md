[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366b.htm)  
閲覧(UTC)：2026-03-05 09:03:39  
[⬅️](eda366a.md)[➡️](eda366c.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.11. ガンマ分布

#### 確率密度関数
ガンマ分布の[確率密度関数の](eda362.md#確率密度関数)一般式は次式である。 

$$f(x) = \frac{(\frac{x-\mu}{\beta})^{\gamma - 1}\exp{(-\frac{x-\mu}{\beta}})} {\beta\Gamma(\gamma)} \hspace{.2in} x \ge \mu; \gamma,\beta > 0$$   

ここで、$`γ`$ は[形状係数](eda363.md)、$`μ`$ は[位置母数](eda364.md)、$`β`$ は[尺度母数](eda364.md)、$`Γ`$ はガンマ関数であり、その式は以下である。 

$$\Gamma(a) = \int\_{0}^{\infty} {t^{a-1}e^{-t}dt}$$   

$`μ=0`$ および $`β=1`$ の場合を**標準ガンマ分布**と呼ぶ。
標準ガンマ分布は次式に簡略化される。 

$$f(x) = \frac{x^{\gamma - 1}e^{-x}} {\Gamma(\gamma)} \hspace{.2in}x \ge 0; \gamma > 0$$   

確率関数の一般形は[標準分布を用いて表現](eda364.md#標準形に基づく位置と尺度の式)できるため、本節以降の式はすべて関数の標準形について示す。

 以下はガンマ確率密度関数のプロットである。 
 
![plot of the gamma probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/gampdf4.gif)  

#### 累積分布関数
ガンマ分布の[累積分布関数](eda362.md#累積分布関数)の式は次式である。

$$F(x) = \frac{\Gamma\_{x}(\gamma)} {\Gamma(\gamma)} \hspace{.2in}x \ge 0; \gamma > 0$$   

ここで $`Γ`$ は上記で定義したガンマ関数であり、$`\Gamma\_{x}(a)`$ は不完全ガンマ関数である。
不完全ガンマ関数の式は次式である。

$$\Gamma\_{x}(a) = \int\_{0}^{x} {t^{a-1}e^{-t}dt}$$   

以下は、上記の確率密度関数プロットと同じ $`γ`$ 値を用いたガンマ累積分布関数のプロットである。 

![plot of the gamma cumulative distribution function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/gamcdf4.gif)  

#### パーセント点関数
ガンマ分布の[パーセント点関数](eda362.md#パーセント点関数)の式は、単純な閉形式では存在しない。
数値的に計算される。

以下は、上記の確率密度関数のプロットと同じ $`γ`$ 値を用いたガンマ分布のパーセント点関数のグラフである。
   
![plot of the gamma percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/gamppf4.gif)  

#### ハザード関数
ガンマ分布の[ハザード関数](eda362.md#ハザード関数)の式は次式である。

$$h(x) = \frac{x^{\gamma - 1}e^{-x}} {\Gamma(\gamma) -\Gamma\_{x}(\gamma)} \hspace{.2in} x \ge 0; \gamma > 0$$   

以下は、上記の確率密度関数のプロットと同じ $`γ`$ 値を用いたガンマ・ハザード関数のプロットである。 

![plot of the gamma hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/gamhaz4.gif)  

#### 累積ハザード関数
ガンマ分布の[累積ハザード関数](eda362.md#累積ハザード関数)の式は次式である。

$$H(x) = -\log{(1 - \frac{\Gamma\_{x}(\gamma)} {\Gamma(\gamma)})}\hspace{.2in} x \ge 0; \gamma > 0$$   

ここで $`Γ`$ は上記で定義したガンマ関数、$`\Gamma\_{x}(a)`$ は上記で定義した不完全ガンマ関数である。

以下は、上記の確率密度関数のプロットと同じ $`γ`$ の値を用いたガンマ累積ハザード関数のプロットである。 
 
![plot of the gamma cumulative hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/gamcha4.gif)  

#### 生存関数
ガンマ分布の[生存関数](eda362.md#生存関数)の式は次式である。

$$S(x) = 1 - \frac{\Gamma\_{x}(\gamma)} {\Gamma(\gamma)} \hspace{.2in}x \ge 0; \gamma > 0$$   

ここで $`Γ`$ は上記で定義したガンマ関数であり、$`\Gamma\_{x}(a)`$ は上記で定義した不完全ガンマ関数である。

以下は、上記の確率密度関数のプロットと同じ $`γ`$ の値を用いたガンマ生存関数のプロットである。 
 
![plot of the gamma survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/gamsurv4.gif)  

#### 逆生存関数
ガンマ[逆生存関数](eda362.md#逆生存関数)は単純な閉形式では存在しない。
数値的に計算される。

以下は、上記の確率密度関数のプロットと同じ $`γ`$ の値を用いたガンマ逆生存率関数のプロットである。 
 
![plot of the gamma inverse survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/gamisur4.gif)  

#### 共通統計量 　
以下の式は、位置係数がゼロ、尺度係数が 1 である。

平均値　　　　$`γ`$  
中央値　　　　$`γ-1 \quad γ≥1`$  
範囲　　　　　0 から $`\infty`$  
標準偏差　　　$`\sqrt{\gamma}`$  
歪度　　　　　$`\frac{2} {\sqrt{\gamma}}`$  
尖度　　　　　$`3 + \frac{6} {\gamma}`$  
変動係数　　　$`\frac{1} {\sqrt{\gamma}}`$   

#### 母数推定
2 係数ガンマ分布のモーメント法推定量は次式である。 

$$\hat{\gamma} = (\frac{\bar{x}} {s})^{2}$$   
$$\hat{\beta} = \frac{s^{2}} {\bar{x}}$$   

ここで $`\bar{x}`$ および $`$`s\`$) はそれぞれ標本平均と標本標準偏差である。

2 係数ガンマ分布の最大尤度推定量は、以下の連立方程式の解である。
 
$$\hat{\beta} - \frac{\bar{x}}{\hat{\gamma}} = 0$$   
$$\hat{\beta} - \frac{\bar{x}}{\hat{\gamma}} = 0$$   
$$\log{\hat{\gamma}} - \psi(\hat{\gamma}) - \log \left( \frac{\bar{x}}{ \left( \prod\_{i=1}^{n}{x\_i} \right) ^{1/n} } \right) = 0$$   
 
ここで $`ψ`$ はディガンマ関数を表す。
これらの連立方程式は数値的に解く必要があり、通常は統計ソフトウェア・パッケージを用いて実行される。 

#### ソフトウェア
汎用統計ソフトウェア・プログラムのいくつかは、ガンマ分布の確率関数の一部を実装している。
