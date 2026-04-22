[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366h.htm)  
閲覧(UTC)：2026-04-22 02:50:48  
[⬅️](eda366g.md)[➡️](eda366i.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.17. ベータ分布

#### 確率密度関数
ベータ分布の[確率密度関数の](eda362.md#確率密度関数)一般式は次式である。

$$f(x) = \frac{(x-a)^{p-1}(b-x)^{q-1}}{B(p,q) (b-a)^{p+q-1}}\hspace{.3in} a \le x \le b; p, q > 0$$  

ここで、$`p`$ および $`q`$ は[形状母数](eda363.md)、$`a`$ および $`b`$ はそれぞれ分布の下限および上限、$`B(p,q)`$ はベータ関数である。
ベータ関数の式は次式である。  

$$B(\alpha,\beta) = \int\_{0}^{1} {t^{\alpha-1}(1-t)^{\beta-1}dt}$$  

$`a=0`$ および $`b=1`$ の場合を**標準ベータ分布**と呼ぶ。
標準ベータ分布の式は次式である。    

$$f(x) = \frac{x^{p-1}(1-x)^{q-1}}{B(p,q)} \hspace{.3in}0 \le x \le 1; p, q > 0$$  

通常、分布の一般形は位置母数と尺度母数を用いて定義される。
ベータ分布は、下限と上限を用いて一般分布を定義するという点で異なる。
しかし、位置母数と尺度母数は、以下のように下限と上限を用いて定義することができる。  

　　位置 = $`a`$    
　　尺度 = $`b-a`$    

確率関数の一般形は[標準分布を用いた表現](eda364.md#標準形に基づく位置と尺度の式)ができるため、本節の以降のすべての式は、関数の標準形について示す。

以下は、4つの異なる形状母数の値に対するベータ確率密度関数のプロットである。

![plot of the Beta probability density function for 4 different values of the shape parameters](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/betpdf4.gif)  

#### 累積分布関数
ベータ分布の[累積分布関数](eda362.md#累積分布関数)の式は、不完全ベータ関数比（一般に $`Ix`$と表記される）とも呼ばれ、次に定義される。  

$$F(x) = I\_{x}(p,q) = \frac{\int\_{0}^{x}{t^{p-1}(1-t)^{q-1}dt}}{B(p,q)}\hspace{.2in} 0 \le x \le 1; p, q > 0$$  

ここで、$`B`$ は上記で定義されたベータ関数である。 

以下は、上記の確率密度関数のプロットと同じ形状母数の値を用いたベータ累積分布関数のプロットである。

![plot of the Beta cumulative distribution function with the same values of the shape parameters as the pdf plots above](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/betcdf4.gif)  

#### パーセント点関数
ベータ分布の[パーセント点関数](eda362.md#パーセント点関数)の式は、単純な閉形式では存在せず、数値的に計算される。

以下は、上記の確率密度関数のプロットと同じ形状母数値を用いたベータ分布のパーセント点関数のプロットである。

![plot of the beta percent point function with the same values of the shape parameters as the pdf plots above](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/betppf4.gif)  

#### 他の確率関数
ベータ分布は通常、信頼性解析には用いられないため、ハザード関数、累積ハザード関数、生存関数、および逆生存確率関数に関する数式やグラフは省略する。

#### 一般的な統計
以下の式は、下限が 0、上限が 1 の場合である。  
平均値　　　　$`\frac {p}{p + q}`$      
最頻値　　　　$`\frac {p-1}{p+q-2} \hspace{.3in} p, q > 1`$      
範囲　　　　　0 から 1  
標準偏差　　　$`\sqrt{\frac{pq}{(p+q)^{2}(p+q+1)}}`$      
変動係数　　　$`\sqrt{\frac{q}{p(p+q+1)}}`$      
歪度　　　　　$`\frac {2(q-p)\sqrt{p+q+1}} {(p+q+2)\sqrt{pq}}`$      

#### 母数推定
まず、$`a`$ と $`b`$ が既知であると仮定する場合について考える。
この場合、モーメント法推定値は次式となる。

$$p = \bar{x}(\frac{\bar{x}(1 - \bar{x})}{s^2} - 1)$$  

$$q = (1 - \bar{x})(\frac{\bar{x}(1 - \bar{x})}{s^2} - 1)$$   

ここで、$`\bar{x}`$ は標本平均、$`s^2`$ は標本分散である。
$`a`$ と$`b`$ がそれぞれ 0 と 1 でない場合、上記の式において、$`\bar{x}`$ を $`\frac{\bar{x} - a}{b-a}`$ に置き換え、$`s^2`$ を$`\frac{s^2}{(b-a)^2}`$ に置き換える。

$`a`$ と $`b`$ が既知の場合、最大尤度推定量は、以下の連立方程式を解くことで得られる。

$$\psi(\hat{p}) - \psi(\hat{p} + \hat{q}) = \frac{1}{n}\sum_{i=1}^{n}{\log(\frac{Y_i - a}{b - a})}$$  

$$\psi(\hat{q}) - \psi(\hat{p} + \hat{q}) = \frac{1}{n}\sum_{i=1}^{n}{\log(\frac{b - Y_i}{b - a})}$$   

$`a`$ と $`b`$ が未知である場合の最尤推定は、問題となることがある。
[Bury](../section4/eda43.md#Bury) の第14章では、この場合におけるモーメント推定と最尤推定の両方について論じている。 

#### ソフトウェア
ほとんどの一般的な統計ソフトウェアは、ベータ分布に関する確率関数のいくつかを実装している。

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  
