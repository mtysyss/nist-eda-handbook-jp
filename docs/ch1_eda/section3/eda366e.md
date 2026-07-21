[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366e.htm)  
閲覧(UTC)：2026-03-05 09:12:22  
[⬅️](eda366d.md)[➡️](eda366f.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.14. 冪乗対数正規分布

#### 確率密度関数
標準形冪乗対数正規分布の[確率密度関数](eda362.md#確率密度関数)の式は次式である。

$$f(x;p,\sigma) = (\frac{p} {x\sigma})\phi(\frac{\log x} {\sigma})(\Phi(\frac{-\log x} {\sigma}))^{p-1} \hspace{.2in} x, p, \sigma > 0$$   

ここで、$`p`$（指数母数とも呼ばれる）と $`σ`$ は[形状母数](eda363.md)であり、$`\Phi`$ は[標準正規](eda3661.md)分布の累積分布関数、$`\phi`$ は[標準正規](eda3661.md)分布の確率密度関数である。

他の確率分布と同様に、冪乗対数正規分布は[位置母数](eda364.md) $`μ`$ と [尺度母数](eda364.md) $`B`$ を用いて変換可能である。
冪乗対数正規分布の一般形の式は省略する。

確率関数の一般形は[標準分布を用いて表現](eda364.md#標準形に基づく位置と尺度の式)できるため、本節以降の式はすべて関数の標準形について示す。

以下は、$`p`$ と $`σ`$ の値を 1 に設定した冪乗対数正規確率密度関数のプロットである。
 
![plot of the power lognormal probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/plnpdf4.gif)  

#### 累積分布関数
冪乗対数正規分布の[累積分布関数](eda362.md#累積分布関数)の式は次式である。

$$F(x;p,\sigma) = 1 - (\Phi(\frac{-\log x} {\sigma}))^{p}\hspace{.2in} x, p, \sigma > 0$$   

ここで $`\Phi`$ は標準[正規](eda3661.md)分布の累積分布関数である。

 以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗対数正規累積分布関数のプロットである。
 
![plot of the power lognormal cumulative distribution function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/plncdf4.gif)  

#### パーセント点関数
冪乗対数正規分布の[パーセント点関数](eda362.md#パーセント点関数)の式は次式である。

$$G(f;p,\sigma) = \exp{(\Phi^{-1}(1 - (1 - f)^{1/p})\sigma)}\hspace{.2in} 0 < p < 1; p, \sigma > 0$$   

ここで $`\phi^{-1}`$ は標準[正規](eda3661.md)分布のパーセント点関数である。

以下は、上記の確率密度関数プロットと同じ $`p`$ の値を用いた冪乗対数正規パーセント点関数のプロットである。
 
![plot of the power lognormal percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/plnppf4.gif)  

#### ハザード関数
冪乗対数正規分布の[ハザード関数](eda362.md#ハザード関数)の式は次式である。

$$h(x,p,\sigma) = \frac{p(\frac{1} {x\sigma})\phi(\frac{\log x}{\sigma})} {\Phi(\frac{-\log x} {\sigma})} \hspace{.2in}x, p, \sigma > 0$$   

ここで $`\Phi`$ は標準正規分布の累積分布関数、$`\phi`$ は標準正規分布の確率密度関数である。

 これは対数正規ハザード関数の単なる倍数（*p*）であることに注意せよ。
 
 以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗対数正規ハザード関数のプロットである。
 
![plot of the power lognormal hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/plnhaz4.gif)  

#### 累積ハザード関数
冪乗対数正規分布の[累積ハザード関数](eda362.md#累積ハザード関数)の式は次式である。 

$$H(x;p,\sigma) = -\log{((\Phi(\frac{-\log x} {\sigma}))^{p})}\hspace{.2in} x, p, \sigma > 0$$   

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗対数正規累積ハザード関数のプロットである。

![plot of the power lognormal cumulative hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/plncha4.gif)  

#### 生存関数
冪乗対数正規分布の[生存関数](eda362.md#生存関数)の式は次式である。

$$S(x;p,\sigma) = (\Phi(\frac{-\log x} {\sigma}))^{p}\hspace{.2in} x, p, \sigma > 0$$   

以下は、上記の確率密度関数のプロットと同じ $`p`$ の値を用いた冪乗対数正規生存関数のプロットである。

![plot of the power lognormal survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/plnsurv4.gif)  

#### 逆生存関数
冪乗対数正規分布の[逆生存関数](eda362.md#逆生存関数)の式は次式である。

$$Z(f;p,\sigma) = \exp{(\Phi^{-1}(1 - f^{1/p})\sigma)} \hspace{.2in} 0 < p < 1; p, \sigma > 0$$   

以下は、上記の確率密度関数プロットと同じ $`p`$ の値を用いた冪乗対数正規逆生存関数のプロットである。

![plot of the power lognormal inverse survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/plnisur4.gif)  

#### 共通統計量 　
冪乗対数正規分布の統計量は複雑であり、表が必要である。
[Nelson](../section4/eda43.htm#Nelson2)は冪乗対数正規分布の平均値、中央値、最頻値、標準偏差について論じ、適切な表への参照を提供している。

#### 母数推定
[Nelson](../section4/eda43.md#Nelson2)は、冪乗対数正規分布の最尤推定について論じている。
これらの推定はコンピュータ・ソフトウェアを用いて行う必要がある。
冪乗対数正規分布の母数の最尤推定用ソフトウェアは、指数分布、Weibull 分布、対数正規分布といった他の信頼性分布用ソフトウェアほど容易に入手できない。

#### ソフトウェア
ほとんどの汎用統計ソフトウェアは、冪乗対数正規分布の確率関数を実装していない。

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  
* 原典の各プロットへのリンクは節番号ではなくプロット名を基準に設定されて箇所があります。mdファイルのリンク先は節番号だけを表示するmdファイルになっています。 
