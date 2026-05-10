[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366g.htm)  
閲覧(UTC)：2026-03-05 09:06:31  
[⬅️](eda366f.md)[➡️](eda366h.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.16. 極値 I 型 分布 

#### 確率密度関数
極値分布の I 型には二つの形式がある。
一つは最小極値に基づき、もう一つは最大極値に基づく。
これらをそれぞれ最小値および最大値のケースと呼ぶ。
両ケースの式とグラフを示す。
極値分布 I 型は Gumbel 分布とも呼ばれる。

Gumbel（最小）分布の[確率密度関数](eda362.md#確率密度関数)の一般式は次式である。  
 
$$f(x) = \frac{1} {\beta} e^{\frac{x-\mu}{\beta}}e^{-e^{\frac{x-\mu}{\beta}}}$$   
 
ここで、$`μ`$ は[位置母数](eda364.md)、$`β`$は[尺度母数](eda364.md)である。
$`μ=0`$ および $`β=1`$ の場合を標準**Gumbel 分布**と呼ぶ。

標準 Gumbel 分布（最小）の式は次式に簡略化される。
$$f(x) = e^{x}e^{-e^{x}}$$   
 
以下は最小値ケースの Gumbel 確率密度関数のグラフである。  
 
![plot of the Gumbel probability density function for the minimum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1pdf.gif)  

Gumbel 分布（最大値）の[確率密度関数](eda362.md#確率密度関数)の一般式は次式である。 

$$f(x) = \frac{1}{\beta} e^{-\frac{x-\mu}{\beta}}e^{-e^{-\frac{x-\mu}{\beta}}}$$   

ここで、$`μ`$ は[位置母数](eda364.md)、$`β`$は[尺度母数](eda364.md)である。
$`μ=0`$ および $`β=1`$ の場合を標準**Gumbel 分布**と呼ぶ。

標準 Gumbel 分布（最大値）の式は次式に簡略化される。

$$f(x) = e^{-x}e^{-e^{-x}}$$   
 
以下は最大値ケースの Gumbel 確率密度関数のグラフである。  

![plot of the Gumbel probability density function for the maximum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1pdf2.gif)  

確率関数の一般形は[標準分布を用いて表現](eda364.md#標準形に基づく位置と尺度の式)できるため、本節以降の式はすべて関数の標準形について示す。 

#### 累積分布関数
Gumbel 分布（最小値）の[累積分布関数](eda362.htm#累積分布関数)の式は次式である。   

$$F(x) = 1 - e^{-e^{x}}$$   

以下は最小値ケースの Gumbel 累積分布関数のグラフである。  

![plot of the Gumbel cumulative distribution function for the minimum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1cdf.gif)  

Gumbel 分布（最大値）の[累積分布関数](eda362.htm#累積分布関数)の式は次式である。   

$$F(x) = e^{-e^{-x}}$$  

以下は最大値の場合の Gumbel 累積分布関数のグラフである。  

![plot of the Gumbel cumulative distribution function for the maximum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1cdf2.gif)  

#### パーセント点関数
Gumbel 分布（最小値）の[パーセント点関数](eda362.htm#パーセント点関数)の式は次式である。   

$$G(p) = \ln(\ln(\frac{1} {1 - p}))$$   

以下は最小値ケースの Gumbel 分布のパーセント点関数のグラフである。  

![plot of the Gumbel percent point function for the minimum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1ppf.gif)   

Gumbel 分布（最大値）の[パーセント点関数](eda362.htm#パーセント点関数)の式は次式である。   

$$G(p) = -\ln(\ln(\frac{1} {p}))$$   

以下は最大値の場合の Gumbel 分布パーセント点関数のグラフである。  

![plot of the Gumbel percent point function for the maximum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1ppf2.gif)  

#### ハザード関数
Gumbel 分布（最小値）の[ハザード関数](eda362.htm#ハザード関数)の式は次式である。   

$$h(x) = e^{x}$$   

以下は最小の場合における Gumbel 分布のハザード関数のグラフである。  

![plot of the Gumbel hazard function for the minimum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1haz.gif)  

Gumbel 分布（最大値）の[ハザード関数](eda362.htm#ハザード関数)の式は次式である。 
 
$$h(x) = \frac{e^{-x}} {e^{e^{-x}} - 1}$$   

以下は最大値の場合の Gumbel ハザード関数のグラフである。

![plot of the Gumbel hazard function for the maximum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1haz2.gif)  

#### 累積ハザード関数
Gumbel 分布（最小値）の[累積ハザード関数](eda362.htm#累積ハザード関数)の式は次式である。   

$$H(x) = e^{x}$$   

以下は最小値ケースのGumbel 累積ハザード関数のグラフである。  

![plot of the Gumbel cumulative hazard function for the minimum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1cha.gif)  

Gumbel 分布（最大値）の[累積ハザード関数](eda362.md#累積ハザード関数)の式は次式である。   

$$H(x) = -\ln(1 - e^{-e^{-x}})$$ 

以下は最大値ケースの Gumbel 累積ハザード関数のグラフである。  

![plot of the Gumbel cumulative hazard function for the maximum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1cha2.gif)  

#### 生存関数
Gumbel 分布（最小値）の[生存関数](eda362.md#生存関数)の式は次式である。   

$$S(x) = e^{-e^{x}}$$   

以下は最小値ケースの Gumbel 生存関数のグラフである。  

![plot of the Gumbel survival function for the minimum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1surv.gif)  

Gumbel 分布（最大値）の[生存関数](eda362.md#生存関数)の式は次式である。   

$$S(x) = 1 - e^{-e^{-x}}$$  

以下は最大値ケースの Gumbel 生存関数のグラフである。  

![plot of the Gumbel survival function for the maximum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1surv2.gif)  

#### 逆生存関数
Gumbel 分布（最小値）の[逆生存関数](eda362.md#逆生存関数)の式は次式である。   

$$Z(p) = \ln(\ln(\frac{1} {p}))$$   

以下は最小値ケースのGumbel 逆生存関数のグラフである。  

![plot of the Gumbel inverse survival function for the minimum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1isurv.gif)  

Gumbel 分布（最大値）の[逆生存関数](eda362.md#逆生存関数)の式は次式である。   

$$Z(p) = -\ln(\ln(\frac{1} {1-p}))$$   

以下は最大値ケースの Gumbel 逆生存関数のグラフである。  

![plot of the Gumbel inverse survival function for the maximum case](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/ev1isur2.gif)  

#### 共通統計量 　
以下の式は最大順序統計量の場合のもの。  
 平均値　　　　　$`\mu + 0.5772\beta`$  
 　　　　　　　　定数 0.5772はオイラー数である。  
 中央値　　　　　$`\mu - \beta\ln(\ln(2))`$  
 最頻値　　　　　$`μ`$  
 範囲　　　　　　$`-\infty \mbox{ から } \infty`$  
 標準偏差　　　　$`\frac{\beta\pi} {\sqrt{6}}`$  
 歪度　　　　　　1.13955  
 尖度　　　　　　5.4  
 変動係数　　　　$`\frac {\beta\pi} {\sqrt{6}(\mu + 0.5772\beta)}`$   

#### 母数推定
Gumbel （最大）分布のモーメント法推定量は以下となる。

$$\tilde{\beta} = \frac{s\sqrt{6}} {\pi}$$   

$$\tilde{\mu} = \bar{X} - 0.5772 \tilde{\beta} = \bar{X} - 0.45006 s$$     

ここで $`\bar{X}`$ および $`s`$ はそれぞれ標本平均と標準偏差である。

Gumbel （最小）分布のモーメント法推定量は以下となる。 
 
 $$\tilde{\beta} = \frac{s\sqrt{6}} {\pi}$$  
  
 $$\tilde{\mu} = \bar{X} + 0.5772 \tilde{\beta} = \bar{X} + 0.45006 s$$   
 
 ここで $`\bar{X}`$ および $`s`$ はそれぞれ標本平均と標準偏差である。
 
最大値ケースの最尤推定量は、以下の連立方程式の解である。 
 
$$\bar{x} - \frac{\sum_{i=1}^{n}{x_i \exp(-x_i/\hat{\beta})}}{\sum_{i=1}^{n}{\exp(-x_i/\hat{\beta})}} - \hat{\beta} = 0$$  

$$-\hat{\beta} \log \left( \frac{1}{n}\sum_{i=1}^{n}{\exp(-x_i/\hat{\beta})} \right) - \hat{\mu} = 0$$  
 
最小値ケースは、上記の式において $`-x_i`$ を $`x_i`$ に置き換える。

これらの式は数値的に解く必要があり、これは通常、統計ソフトウェア・パッケージを使用して行う。 

#### ソフトウェア
一部の汎用統計ソフトウェアは、極値分布 I 型の確率関数の一部を実装している。

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  
