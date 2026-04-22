[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366a.htm)  
閲覧(UTC)：2026-03-05 08:59:37  
[⬅️](eda3669.md)[➡️](eda366b.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.10. Birnbaum-Saunders（疲労寿命）分布

#### 確率密度関数
Birnbaum-Saunders 分布は、疲労寿命分布としても広く知られている。
文献には Birnbaum-Saunders 分布のいくつか代替の式がある。

Birnbaum-Saunders 分布の[確率密度関数](eda362.md#確率密度関数)の一般式は次式である。

$$f(x) = \left (\frac{\sqrt{\frac{x-\mu} {\beta}} + \sqrt{\frac{\beta}{x-\mu}}} {2\gamma (x-\mu)} \right)\phi \left( \frac{\sqrt{\frac{x-\mu} {\beta}} -\sqrt{\frac{\beta} {x-\mu}}} {\gamma} \right)\hspace{.2in} x > \mu; \gamma, \beta > 0$$ 

ここで、$`γ`$ は[形状母数](eda363.md)、$`μ`$ は[位置母数](eda364.md)、$`β`$ は[尺度母数](eda364.md)、$`\phi`$ は[標準正規](eda3661.md)分布の確率密度関数、$`\Phi`$ は[標準正規](eda3661.md)分布の累積分布関数である。
$`μ=0`$ および $`β=1`$ の場合を標準 Birnbaum-Saunders 分布と呼ばれる。
標準 Birnbaum-Saunders 分布は次式に簡略化される 

$$f(x) = \left (\frac{\sqrt{x} + \sqrt{\frac{1} {x}}} {2\gamma x} \right)\phi \left (\frac{\sqrt{x} - \sqrt{\frac{1} {x}}} {\gamma} \right)\hspace{.2in} x > 0; \gamma > 0$$   

確率関数の一般形は[標準分布を用いて表現](eda364.md#標準形に基づく位置と尺度の式)できるため、本節以降の式はすべて関数の標準形で示す。

以下は Birnbaum-Saunders 確率密度関数のプロットである。  

![plot of the Birnbaum-Saunders probability density function for 4 values of gamma](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/flpdf4.gif)  

#### 累積分布関数
Birnbaum-Saunders 分布の[累積分布関数](eda362.md#累積分布関数)の式は次式である

$$F(x) = \Phi(\frac{\sqrt{x} - \sqrt{\frac{1} {x}}} {\gamma})\hspace{.2in} x > 0; \gamma > 0$$   

ここで $`\Phi`$ は[標準正規](eda3661.md)分布の累積分布関数である。

以下は、上記の確率密度関数プロットと同じ $`γ`$ の値を用いた Birnbaum-Saunders 累積分布関数のプロットである。

![plots of the Birnbaum-Saunders cumulative distribution function for 4 values of gamma](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/flcdf4.gif)  

#### パーセント点関数
Birnbaum-Saunders 分布の[パーセント点関数](eda362.md#パーセント点関数)の式は次式である。
 
$$G(p) = \frac{1} {4} \left[\gamma \Phi^{-1}(p) + \sqrt{4 +(\gamma \Phi^{-1}(p))^{2}}\right]^{2}$$   
 
ここで $`\Phi^{-1}`$ は[標準正規](eda3661.md)分布のパーセント点関数である。

以下は、上記の確率密度関数のプロットと同じ $`γ`$ の値を用いた Birnbaum-Saunders 分布のパーセント点関数のプロットである。  

![plot of the Birnbaum-Saunders percent point function for 4 values of gamma](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/flppf4.gif)  

#### ハザード関数
Birnbaum-Saunders の[ハザード関数](eda362.md#ハザード関数)は、 Birnbaum-Saunders の確率密度関数および累積分布関数から計算することができる。
 
以下は、上記の確率密度関数のプロットと同じ $`γ`$ の値を用いた Birnbaum-Saunders 危険率関数のプロットである。 
 
![plot of the Birnbaum-Saunders hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/flhaz4.gif)  

#### 累積ハザード関数
Birnbaum-Saunders [累積ハザード関数](eda362.md#累積ハザード関数)は、 Birnbaum-Saunders 累積分布関数から計算できる。
 
以下は、上記の確率密度関数のプロットと同じ $`γ`$ 値を用いた Birnbaum-Saunders 累積ハザード関数のプロットである。  
 
![plot of the Birnbaum-Saunders cumulative hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/flcha4.gif)  

#### 生存関数
Birnbaum-Saunders [生存関数](eda362.md#存関数)は Birnbaum-Saunders 累積分布関数から計算できる。
 
以下は、上記の確率密度関数のプロットと同じ $`γ`$ 値を用いた Birnbaum-Saunders 生存関数のプロットである。  
 
![plot of the Birnbaum-Saunders survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/flsur4.gif)  

#### 逆生存関数
Birnbaum-Saunders [逆生存関数](eda362.md#生存関数)は、 Birnbaum-Saunders  パーセント点関数から計算することができる。
 
以下は、上記の確率密度関数のプロットと同じ $`γ`$ 値を用いたガンマ逆生存関数のプロットである。  
 
![plot of the Birnbaum-Saunders inverse survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/flisur4.gif)  

#### 共通統計量 　
以下の式は、位置母数がゼロ、尺度母数が 1 である。

平均値　　　　　$`1 + \frac{\gamma^{2}} {2}`$  
範囲　　　　　　0から$`\infty`$  
標準偏差　　　　$`\gamma\sqrt{1 + \frac{5\gamma^{2}} {4}}`$  
変動係数　　　　$`\frac{2 + \gamma^{2}} {\gamma\sqrt{1 + 5\gamma^{2}}}`$  

#### 母数推定
[Birnbaum-Saunders 分布の最尤推定](../../apr/section4/apr413#疲労寿命)は、[信頼性](../../apr/apr.md)の章で議論されている。

#### 解説   
Birnbaum-Saunders 分布は、[信頼性](../../apr/apr.md)の応用において故障時間をモデル化するために広く用いられている。

#### ソフトウェア
[Dataplot](../section4/eda44.md#FLDIST)を含む一部の汎用統計ソフトウェア・プログラムは、 Birnbaum-Saunders 分布の確率関数の少なくともいくつかを実装している。
信頼性用途を重視する統計プログラムでは、この分布を実装していることがある。  

「bs」パッケージは R パッケージ向けに Birnbaum-Saunders 分布を実装している。  

<blockquote>
詳細はLeiva, V., Hernandez, H., and Riquelme, M. (2006). A New Package for the Birnbaum-Saunders Distribution. *Rnews*, 6/4, 35-40.(<http://www.r-project.org>) 
</blockquote>

---
#### 訳註  
* 2026-04-22時点で、「bs」パッケージは、維持されていない状態で、本ハンドブック付属の r スクリプトは機能しません。
* [CRAN Task View: Probability Distributions](https://cran.r-project.org/web/views/Distributions.html#miscellaneous)に、次の記載があります。 "Birnbaum-Saunders distribution: provided in bsgof, extraDistr, VGAM." (2026-04-22 閲覧)
