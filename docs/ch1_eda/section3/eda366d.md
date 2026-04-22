[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366d.htm)  
閲覧(UTC)：2026-03-05 09:09:59  
[⬅️](eda366c.md)[➡️](eda366e.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.13. 冪乗正規分布

#### 確率密度関数
冪乗正規分布の標準形の[確率密度関数](eda362.md#確率密度関数)の式は式である。  

$$f(x;p) = p \phi(x) (\Phi(-x))^{p-1} \hspace{.3in} x, p > 0$$  

ここで、$`p`$ は[形状母数](eda363.md)（指数母数とも呼ばれる）、$`\Phi`$ は[標準正規](eda3661.md)分布の累積分布関数、$`\phi`$ は[標準正規](eda3661.md)分布の確率密度関数である。

他の確率分布と同様に、冪乗正規分布は[位置母数](eda364.md) $`μ`$ と[尺度母数](eda364.md) $`σ`$ によって変換可能である。
冪乗正規分布の一般形の式は省略する。
確率関数の一般形は[標準分布を用いて表現](eda364.md#標準形に基づく位置と尺度の式)できるため、本節以降の式はすべて関数の標準形について示す。

以下は、4つの $`p`$ 値における冪乗正規確率密度関数のプロットである。  
 
![plot of the power normal probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/pnrpdf4.gif)  

#### 累積分布関数
冪乗正規分布の[累積分布関数](eda362.md#累積分布関数)の式は次式である。  

$$F(x;p) = 1 - (\Phi(-x))^{p} \hspace{.3in} x, p > 0$$  

ここで $`\Phi`$ は標準[正規](eda3661.md)分布の累積分布関数である。

以下は、上記の確率密度関数のプロットと同じ値の $`p`$ を用いた冪乗正規分布の累積分布関数のプロットである。  
 
![plot of the power normal cumulative distribution function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/pnrcdf4.gif)  

#### パーセント点関数
冪乗正規分布の[パーセント点関数](eda362.md#パーセント点関数)の式は次式である。  

$$G(f) = \Phi^{-1}(1 - (1 - f)^{1/p}) \hspace{.3in} 0 < f < 1; p > 0$$  

ここで $`\phi^{-1}`$ は標準[正規](eda3661.md)分布のパーセント点関数である。

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗正規パーセント点関数のプロットである。  
 
![plot of the power normal percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/pnrppf4.gif)  

#### ハザード関数
冪乗正規分布の[ハザード関数](eda362.md#ハザード関数)の式は次式である。

$$h(x;p) = \frac{p\phi(x)} {\Phi(-x)} \hspace{.3in} x, p > 0$$  

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗正規ハザード関数のプロットである。  

![plot of the power normal hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/pnrhaz4.gif)  

#### 累積ハザード関数
冪乗正規分布の[累積ハザード関数](eda362.md#累積ハザード関数)の式は次式である。 

$$H(x,p) = -\log{((\Phi(-x))^{p})} \hspace{.3in} x, p > 0$$  

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗正規累積ハザード関数のプロットである。 
 
![plot of the power normal cumulative hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/pnrcha4.gif)  

#### 生存関数
冪乗正規分布の[生存関数](eda362.md#生存関数)の式は次式である。 

$$S(x;p) = (\Phi(-x))^{p} \hspace{.3in} x, p > 0$$  

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗正規生存関数のプロットである。  

![plot of the power normal survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/pnrsurv4.gif)  

#### 逆生存関数
冪乗正規分布の[逆生存関数](eda362.md#逆生存関数)の式は次式である。  

$$Z(f) = \Phi^{-1}(1 - f^{1/p}) \hspace{.3in} 0 < f < 1; p > 0$$  

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗正規逆生存関数のプロットである。  

![plot of the power normal inverse survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/pnrisur4.gif)  

#### 共通統計量 　
冪乗正規分布の統計量は複雑であり、表が必要である。
[Nelson](../section4/eda43.md#Nelson2)は冪乗正規分布の平均値、中央値、最頻値、標準偏差について論じ、適切な表への参照を提供している。

#### ソフトウェア
ほとんどの汎用統計ソフトウェアは、冪乗正規分布の確率関数を実装していない。

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  
* 原典の各プロットへのリンクはセクション番号ではなくプロット名を基準に設定されて箇所があります。mdファイルのリンク先はセクション番号だけを表示するmdファイルになっています。 
