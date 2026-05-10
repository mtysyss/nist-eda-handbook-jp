[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm)  
閲覧(UTC)：2026-04-21 09:37:59  
[⬅️](eda366i.md)[➡️](eda367.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)

---

# 1.3.6.6.19. Poisson 分布

#### 確率質量関数
Poisson 分布は、特定の時間間隔内に発生する事象数をモデル化するために用いられる。

Poisson 確率質量関数の式は次の通りである。

$$p(x;\lambda) = \frac{e^{-\lambda}\lambda^{x}} {x!} \mbox{ただし、 } x = 0, 1, 2, \cdots$$  

$`λ`$ は形状母数であり、特定の時間間隔における事象の平均回数を示する。

以下は、4つの $`λ`$ の値に対する Poisson 確率密度関数のプロットである。

![plot of the Poisson probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/poipdf4.gif)  

#### 累積分布関数
Poisson 累積確率関数の式は次式である。  

$$F(x;\lambda) = \sum_{i=0}^{x}{\frac{e^{-\lambda}\lambda^{i}} {i!}}$$  

以下は、上記の確率密度関数のグラフと同じ $`λ`$ の値を用いた Poisson 累積分布関数のグラフである。

![plot of the Poisson cumulative distribution function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/poicdf4.gif)  

#### パーセント点関数
Poisson 分布のパーセント点関数は、単純な閉形式では存在しない。
数値的に計算される。
これは $`x`$ が整数の場合にのみ定義される離散分布であるため、連続分布におけるパーセント点関数のように滑らかではないことを留意する。

以下は、上記の確率密度関数のプロットと同じ $`λ`$ の値を用いた Poisson 分布のパーセント点関数のプロットである。

![plot of the Poisson percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/poippf4.gif)  

#### 共通統計量
平均値　　　　　$`λ`$  
最頻値　　　　　$`λ`$ が整数でない場合、$`λ`$ より小さい最大の整数  
　　　　　　　　$`λ`$ が整数の場合、$`x=λ`$ および $`x=λ-1`$ の両方が最頻値となる。  
範囲　　　　　　0 から $`\infty`$  
標準偏差　　　　$`\sqrt{\lambda}`$  
変動係数　　　　$`\frac{1} {\sqrt{\lambda}}`$  
歪度　　　　　　$`\frac{1} {\sqrt{\lambda}}`$  
尖度　　　　　　$`3 + \frac{1} {\lambda}`$  

#### 母数推定
λの最尤推定量は次式である。  

$$\tilde{\lambda} = \bar{X}$$  

ここで、$`\bar{X}`$は標本平均である。 

#### ソフトウェア
ほとんどの一般的な統計ソフトウェアプログラムは、Poisson 分布に関する確率関数のいくつかを実装している。


---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  


