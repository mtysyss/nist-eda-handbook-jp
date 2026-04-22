[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366i.htm)  
閲覧(UTC)：2026-04-21 09:37:36  
[⬅️](eda366h.md)[➡️](eda366j.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)

---

# 1.3.6.6.18. 二項分布

#### 確率質量関数
二項分布は、ある試行において、互いに排他的な結果がちょうど2つある場合に用いられる。  
これらの結果は、それぞれ「成功」と「失敗」と呼ばれる。
二項分布は、1回の試行における成功確率を $`p`$ と表し、*N* 回の試行のうち *x* 回の成功が観測される確率を求めるために用いられる。
二項分布では、$`p`$ がすべての試行において一定であると仮定する。

二項確率質量関数の式は次式である。  

$$P(x;p,n) = \left(\begin{array}{c} n \\ x \end{array} \right)(p)^{x}(1 - p)^{(n-x)} \qquad \mbox{$x = 0, 1, 2, \cdots , n$ の場合}$$   

$$
\left ( \begin{array}{c} n \\ x \end{array} \right )
$$  

ここで 

$$\left(\begin{array}{c} n \\ x \end{array} \right) = \frac{n!}{x!(n-x)! }$$  

以下は、$`p`$ の 4 つの値および $`n=100`$ に対する二項分布の確率密度関数のプロットである。

![plot of the binomial probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/binpdf4.gif)  

#### 累積分布関数
二項累積確率関数の式は次式である。  

$$F(x;p,n) = \sum\_{i=0}^{x}{\left( \begin{array}{c} n \\ i \end{array}\right) (p)^{i}(1 - p)^{(n-i)}} $$  

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた二項累積分布関数のプロットである。

![plot of the binomial cumulative distribution function ](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/bincdf4.gif)  

#### パーセント点関数
二項分布のパーセント点関数は、単純な閉形式では存在しない。
これは数値的に計算される。
なお、これは $`x`$ が整数の値をとる場合にのみ定義される離散分布であるため、連続分布におけるパーセント点関数のように滑らかではないことを留意する。

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた、二項分布のパーセント点関数のプロットである。

![plot of the binomial percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/binppf4.gif)  

#### 共通統計量
平均　　　　　$`np`$  
最頻値　　　　$`p(n+1)-1≤x≤p(n+1)`$  
範囲　　　　　0 から $`n`$  
標準偏差　　　$`\sqrt{np(1 - p)}`$  
変動係数　　　$`\sqrt{\frac{(1-p)} {np}}`$  
歪度　　　　　$`\frac{(1-2p)} {\sqrt{np(1 - p)}}`$  
尖度　　　　　$`3 - \frac{6} {n} + \frac{1} {np(1 - p)}`$  

#### 解説  
二項分布は、おそらく最も一般的に用いられる離散分布である。

#### 母数推定
（*n* が固定の場合）$`p`$ の最尤推定量は次式である。  

 $`\tilde{p} = \frac{x} {n}`$   

#### ソフトウェア
ほとんどの一般的な統計ソフトウェア・プログラムは、二項分布に関する確率関数のうちのいくつかを実装している。

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  