[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366c.htm)  
閲覧(UTC)：2026-03-05 09:04:23  
[⬅️](eda366b.md)[➡️](eda366d.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.12. 二重指数分布

#### 確率密度関数
二重指数分布の[確率密度関数](eda362.md#確率密度関数)の一般式は次式である。 

$$f(x) = \frac{e^{-\left| \frac{x-\mu}{\beta} \right| }} {2\beta}$$   

ここで、 $`μ`$ は[位置母数](eda364.md)、$`β`$ は[尺度母数](eda364.md)である。
$`μ=0`$ および $`β=1`$ の場合を標準**二重指数分布**と呼ぶ。
標準二重指数分布の式は次の通りである。

$$f(x) = \frac{e^{-|x|}}{2}$$   

確率関数の一般形は[標準分布を用いて表現](eda364.md#標準形に基づく位置と尺度の式)できるため、本節以降の式はすべて関数の標準形について示す。

なお、二重指数分布はラプラス分布とも呼ばれる。
 
以下は二重指数確率密度関数のグラフである。  
 
![plot of the double exponential probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/dexpdf.gif)  

#### 累積分布関数
二重指数分布の[累積分布関数](eda362.md#累積分布関数)の式は次式である。

$$
F(x) = \begin{array}{ll} 
\frac{e^{x}} {2} & \mbox{$x < 0$ の場合} \\
1 - \frac{e^{-x}} {2} & \mbox{$x \ge 0$ の場合} 
\end{array}
$$   

以下は二重指数累積分布関数のグラフである。  

![plot of the double exponential cumulative distribution function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/dexcdf.gif)  

#### パーセント点関数
二重指数分布の[パーセント点関数](eda362.md#パーセント点関数)の式は次式である。   

$$
G(P) = \begin{array}{ll} 
\log(2p) & \mbox{$p \le 0.5$ の場合} \\
-\log(2(1 - p)) & \mbox{$p > 0.5$ の場合} 
\end{array}
$$   

以下は二重指数パーセント点関数のグラフである。  

![plot of the double exponential percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/dexppf.gif)  

#### ハザード関数
二重指数分布の[ハザード関数](eda362.md#ハザード関数)の式は次式である。   

$$
h(x) = \begin{array}{ll} 
\frac{e^{x}} {2 - e^{x}} &\mbox{for $x < 0$} \\ 
1 & \mbox{for $x \ge 0$} 
\end{array}
$$   

以下は二重指数ハザード関数のグラフである。  

![plot of the double exponential hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/dexhaz.gif)  

#### 累積ハザード関数
二重指数分布の[累積ハザード関数](eda362.md#累積ハザード関数)の式は次式である。 

$$H(x) = \begin{array}{ll} 
-log{(1 - \frac{e^{x}} {2})} &\mbox{for $x < 0$} \\ 
x + \log{(2)} & \mbox{for $x \ge 0$} 
\end{array}$$   

以下は二重指数累積ハザード関数のグラフである。  

![plot of the double exponential cumulative hazard function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/dexcha.gif)  

#### 生存関数
二重指数分布の[生存関数](eda362.md#生存関数)の式は次式である。  

$$S(x) = \begin{array}{ll} 1 - \frac{e^{x}} {2} & \mbox{for $x < 0$} \\\frac{e^{-x}} {2} & \mbox{for $x \ge 0$} \end{array}$$   

以下は二重指数生存関数のグラフである。  

![plot of the double exponential survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/dexsurv.gif)  

#### 逆生存関数
二重指数分布の[逆生存関数](eda362.md#INVERSESURVIVAL)の式は次式である。  

$$Z(P) = \begin{array}{ll} \log(2(1-p)) & \mbox{$p \le 0.5$ の場合} \\-\log(2p) & \mbox{$p > 0.5$ の場合} \end{array}$$   

以下は二重指数逆生存関数のグラフである。  

![plot of the double exponential inverse survival function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/dexisurv.gif)  

#### 共通統計量 　
平均値　　　　　$`μ`$  
中央値　　　　　$`μ`$  
最頻値　　　　　$`μ`$  
範囲　　　　　　$`-\infty \mbox{ から } \infty`$  
標準偏差　　　　$`\sqrt{2}\beta`$  
歪度　　　　　　0  
尖度　　　　　　6  
変動係数　　　　$`\sqrt{2}(\frac{\beta} {\mu})`$  

#### 母数推定
二重指数分布の位置と尺度の母数の最尤推定量は次式である。 

$$\hat{\mu} = \tilde{X}$$   

$$\hat{\beta} = \frac{\sum_{i=1}^{N}|X_{i} - \tilde{X}|} {N}$$   

ここで $`\tilde{X}`$ は標本中央値である。 

#### ソフトウェア
いくつかの汎用統計ソフトウェア・プログラムは、二重指数分布の確率関数の一部を実装している。
