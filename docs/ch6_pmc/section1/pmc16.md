[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)  
閲覧(UTC)：2026-10-17 02:06:29  
[⬅️](pmc15.md)[➡️]()  

6. [工程や製品の監視と管理](../pmc.md)  
6.1. [はじめに](pmc1.md)  

---

# 6.1.6. 工程能力とは
工程能力は、<u>管理下</u>にあるの工程の出力を<u>能力指標</u>を用いて仕様限界と比較する。
比較は、工程仕様（仕様「幅」）と工程値のばらつきの比率を 6工程標準偏差単位（工程「幅」）で測定し行う。

**工程能力指数**

#### 工程ばらつきと工程仕様の両方を用い、工程が「能力」を満たしているかの判断に用いられる工程能力指数
安定した工程出力を工程仕様と比較し、工程が仕様をどの程度満たしているかについて評価を行うことがしばしば求められる。
これを行うには、安定した工程の固有ばらつきを工程仕様の限界値と比較する。

測定値のほぼすべてが仕様限界内に収まっている工程は、<u>能力</u>のある工程である。
これは、以下に図示することができる。

![Diagram demonstrating a capable process](https://www.itl.nist.gov/div898/handbook/pmc/section1/gifs/cpi1.gif)

工程の能力を測定するために使用できる統計量には、*C*<sub>*p*</sub>、*C*<sub>*pk*</sub>、および *C*<sub>*pm*</sub> などがある。

 ほとんどの能力指数推定値は、使用される標本規模が「十分に大きい」場合にのみ有効である。
十分に大きいとは、一般に約50個の独立したデータ値の場合と考えられる。

*C*<sub>*p*</sub>、*C*<sub>*pk*</sub>、および *C*<sub>*pm*</sub> の各統計量は、データ値の母集団が正規分布に従うことを仮定している。
両側仕様を仮定し、*μ* と *σ* をそれぞれ正規データの平均と標準偏差とし、USL、LSL、および *T* をそれぞれ上側、下側の仕様限界および目標値とする場合、母集団能力指数は次のように定義される。 

#### 各種工程能力指数の定義
$$\begin{gather}
 C_p = \frac{\text{USL} - \text{LSL}} {6\sigma} \\
 C_{pk} = \min{\left[ \frac{\text{USL} - \mu} {3\sigma}, \frac{\mu - \text{LSL}} {3\sigma}\right]} \\ 
 C_{pm} = \frac{\text{USL} - \text{LSL}} {6\sqrt{\sigma^2 + (\mu - T)^2}} 
\end{gather} $$ 

#### 能力指数の推定値の例
これらの指標の<u>推定量の例</u>を以下に示す。
（推定量は「ハット」記号で示されている）。

$$ \begin{gather}
\hat{C}_p = \frac{\text{USL} - \text{LSL}} {6s} \\
\hat{C}_{pk} = \min{\left[ \frac{\text{USL} - \bar{x}} {3s}, \frac{\bar{x} - \text{LSL}} {3s}\right]} \\
\hat{C}_{pm} = \frac{\text{USL} - \text{LSL}} {6\sqrt{s^2 + (\bar{x} - T)^2}} 
\end{gather} $$

*C*<sub>*pk*</sub> の推定量は、$`C_{pk} = C_p(1-k)`$ と表すこともできる。
ここで、*k* は仕様範囲の中点 *m* と工程平均 *μ* との間の尺度調整された距離である。

仕様範囲の中点を $`m = (\text{USL} + \text{LSL})/2`$ と表す。
工程平均 *μ* と最適値である *m* との距離は $`\mu - m`$ であり、ここで $`m \le \mu \le \text{LSL}`$ である。
尺度調整された距離は

$$ k = \frac{|m - \mu|} {(\text{USL} - \text{LSL})/2} , \qquad 0 \le k \le 1 \, .$$

（絶対値記号は、$`\text{LSL} \le \mu \le m`$）の場合をカバーしている）。
推定値 $`\hat{k}`$ を決定するために、*μ* を $`\bar{x}`$ で推定する。
なお、$`\bar{x} \le \text{USL}`$ であることに注意されたい。

*k* 因子によって調整された *C*<sub>*p*</sub> 指数の推定量は、

$$ \hat{C}_{pk} = \hat{C}_p(1 - \hat{k}) \quad . $$

$` 0 \le k \le 1 `$ であるため、$` \hat{C}_{pk} \le \hat{C}_p `$ となる。 

#### 工程幅の変化と *C*<sub>*p*</sub> のグラフ
工程幅が変化した場合の *C*<sub>*p*</sub> 統計量の値の目安を知るために、次の図を参照してください。

![ 4 plots showing the value of Cp for varying process widths](https://www.itl.nist.gov/div898/handbook/pmc/section1/gifs/plotcp_r.gif)

これは以下の表に数値的に表現している。 

#### 能力を「棄却」に変換

| | | | | |  
| :----- | :--- | :--- | :--- | :--- |    
| USL - LSL | 6*σ* | 8*σ* | 10*σ* | 12*σ* |  
| *C*<sub>*p*</sub> | 1.00 | 1.33 | 1.66 | 2.00 |  
| 棄却 | 0.27 % | 64 ppm | 0.6 ppm | 2 ppb |  
| 仕様使用率（%） | 100 | 75 | 60 | 50 |  
{: .no-header-table} 

ここで、ppm は 100 万分の 1、ppb は 10 億分の 1 を表す。
なお、不適合率は分布が *μ* を中心としているという仮定に基づいていることに注意されたい。

これまでは、2つの規格限界、すなわち USLとLSLがある場合について検討してきた。
これは<u>双側（bilateral）</u>または両側の場合として知られている。
下限仕様のみ、あるいは上限仕様のみが用いられるケースも多くある。
1つの仕様限界を用いることを<u>片側</u>または一側と呼びます。
これに対応する能力指標は以下の通りである。 

#### 片側仕様と対応する能力指標

$$ C_{pu} = \frac{\text{許容上限ばらつき}} {\text{実際の上限ばらつき}} = \frac{\text{USL} - \mu} {3\sigma} $$

および

$$ C_{pl} = \frac{\text{許容下限幅}} {\text{実際の下限幅}} = \frac{\mu - \text{LSL}} {3\sigma} \, , $$

ここで、*μ* および *σ* はそれぞれ工程の平均および標準偏差である。

*C*<sub>*pu*</sub> および *C*<sub>*pl*</sub> の推定量は、*μ* と *σ* をそれぞれ $`\bar{x}`$ と *s* に置き換えることで得られる。
以下の関係が成り立つ。

$$ C_p = \frac{C_{pu} + C_{pl}}{2} \, . $$

これは図示すると次になる。

![Graph demonstrating upper actual and allowable upper spread](https://www.itl.nist.gov/div898/handbook/pmc/section1/gifs/cpi3.gif){: .text-center}

なお、次のように書くこともできる： 

$$ C_{pk} = \text{min}(C_{pl}, C_{pu}) . $$ 

**能力指数の信頼限界**

#### 指数の信頼区間
工程データが正規分布に従うと仮定すると、標本値 $`\hat{C}_p`$ の分布はカイ二乗分布に従い、$`\hat{C}_{pu}`$ および $`\hat{C}_{pl}`$ の分布は 非心 *t* 分布に関連する。
幸いなことに、正規分布に関連する近似的な信頼限界が導出されている。
$`\hat{C}_{pk}`$ の分布に対する様々な近似が提案されており、その中には Bissell (1990) によるものも含まれるが、ここでは正規近似を用いる。

その結果得られる 100(1-*α*)% 信頼区間の式を以下に示す。

*C*<sub>*p*</sub> の信頼限界は 

$$ Pr\\{\hat{C}_p(L_1) \le C_p \le \hat{C}_p(L_2)\\} = 1 - \alpha \quad ,$$

であり、ここで

$$ \begin{eqnarray}
L_1 & = & \sqrt{\frac{\chi^2_{\alpha/2, \nu}}{\nu}} \quad , \\
    & & \\
L_2 & = & \sqrt{\frac{\chi^2_{1-\alpha/2, \nu}}{\nu}} \quad ,
\end{eqnarray}$$

ここで、$`\nu = \text{自由度}`$ である。 

#### *C*<sub>*pu*</sub> および *C*<sub>*pl*</sub> の信頼区間
標本規模 *n* における *C*<sub>*pu*</sub> の 近似 100(1-*α*) % 信頼区間は

$$ C_{pu}(lower) = \hat{C}_{pu} - z_{1-\beta}\sqrt{\frac{1}{9n} + \frac{\hat{C}_{pu}^2}{2(n-1)}} $$

また、 

$$ C_{pu}(lower) = \hat{C}_{pu} - z_{1-\alpha}\sqrt{\frac{1}{9n} + \frac{\hat{C}_{pu}^2}{2(n-1)}} \, $$

ここで、*z* は標準正規分布のパーセント点関数を表す。
*β* が未知の場合は、*α* に設定する。

*C*<sub>*pl*</sub> の極限は、$`\hat{C}_{pu}`$ を $`\hat{C}_{pl}`$ に置き換えることで得られる。 

#### *C*<sub>*pk*</sub> の信頼区間
[Zhangら（1990）](../section7/pmc7.md#Zhang1990)は、$`C_{pk}`$ の推定量の正確な分散および *n* が大きい場合の近似値を導出した。
参考文献は、Zhang、Stenback、Wardrop（1990）の「工程能力指数の区間推定（Interval Estimation of the process capability index）」、『*Communicationsin Statistics: Theory and Methods*』、19(21)、4455-4470 である。

分散は以下で求まる。

まず、以下とする。

$$ \begin{gather}
c = \sqrt{n}\left[\mu - (\text{USL} + \text{LSL})/2\right]\sigma \\
d = (\text{USL} - \text{LSL})/\sigma \\
\Phi(-c) = \int\_{-inf}^{-c}{\frac{1}{\sqrt{2\pi}}\exp{-5z^2}dz} \, .
\end{gather}$$

すると

$$ \begin{align}
\text{Var}(\hat{C}_{pk}) &= (d^2/36)(n-1)(n-3) \\
                  &\quad -(d/9\sqrt{n})(n-1)(n-3) \\{\sqrt{2\pi}\exp{(-c^2/2)} + c[1 - 2\Phi(-c)]\\} \\
                  &\quad +[(1/9)(n-1)/(n(n-3))](1 + c^2) \\                  
                  &\quad -[(n-1)/(72n)]\\{\frac{\Gamma((n-2)/2)}{\Gamma((n-1)/2)}\\}^2 \\
                  &\quad * \\{d\sqrt{n} - 2\sqrt{2\pi}\exp{(-c^2/2)} - 2c[1 - 2\Phi(-c)]\\}^2 \, .
                  \end{align}$$

その近似式は以下に与えられる。

$$ Var(\hat{C}_{pk}) = \frac{n-1}{n-3} - 0.5\{\frac{\Gamma((n-2)/2)}{\Gamma((n-1)/2)}\}^2 \, , $$

ここで

$$ n \ge 25, \qquad 0.75 \le C_{pk} \le 4, \qquad |c| \le 100, \qquad \text{ かつ } \qquad d \le 24 \, .$$

実務では、以下の近似式が一般的に用いられる。

$$ C_{pk} = \hat{C}_{pk} \pm z_{1-\alpha/2}\sqrt{\frac{1}{9n} + \frac{\hat{C}_{pk}^2}{2(n-1)}} \, . $$

これらの近似式が有効となるためには、標本規模が少なくとも 25以上である必要があることに留意することが重要である。
ただし、一般に、能力調査を行うには $`n \ge 100`$ が求められる。
また、能力指数の無作為性により、ばらつきが無視できない点にも注意が必要である。 

#### 例
ある工程について、USL = 20 であり、LSL = 8 である。
観測された工程の平均は $`\bar{x} \ge 16`$、標準偏差は $`s = 2`$ である。
これより、以下の式が得られる。

$$ \hat{C}_p = \frac{\text{USL} - \text{LSL}} {6s} = \frac{20 - 8} {6(2)} = 1.0 \, . $$

これは、工程が中点 $`m = (\text{USL} + \text{LSL})/2 = 14`$ に位置している限り、その工程は網力があることを意味する。

しかし、$`\bar{x} \ge 16`$ であるため、そうではない。
$`\hat{k}`$ 係数は次式で求められる。

$$ \hat{k} = \frac{|m - \bar{x}|} {(\text{USL} - \text{LSL})/2} = \frac{2} {6} = 0.3333 $$

であり、

$$ \hat{C}_{pk} = \hat{C}_{p}(1-\hat{k}) = 0.6667 \, .$$

$`\hat{C}_{pk}`$ は少なくとも 1.0であることが望ましいため、これは良好な工程とは言えない。
可能であれば、変動を低減するか、あるいは工程を中心に揃えるようにする。
また、以下の2式を用いて $` \hat{C}_{pu} `$ および $` \hat{C}_{pl} `$ を計算する。

$$ \hat{C}_{pu} = \frac{\text{USL} - \bar{x}} {3s} = \frac{20 - 16} {3(2)} = 0.6667 $$
 
および
 
$$ \hat{C}_{pl} = \frac{\bar{x} - \text{LSL}} {3s} = \frac{16 - 8} {3(2)} = 1.3333 \, . $$
 
ここから、上記の指標の中で最小である $`\hat{C}_{pu}`$ が 0.6667 であることが判る。
なお、式 $`\hat{C}_{pk} = \hat{C}_{p}(1 - \hat{k})`$ は、定義 $` \text{min}(\hat{C}_{pu}, \hat{C}_{pl})`$ と代数的に同等であることに注意されたい。 

**工程が近似的に正規分布に従わない場合に何が起きるか**

#### 異常値を含むデータでできること
これまで検討してきた指標は、工程分布が正規分布に基づいている。
これは、工程分布が正規分布でない場合に問題となる。
詳細には立ち入らず、いくつかの対処法を挙げる。

1. データが近似的に正規分布になるよう変換する。
よく用いられる変換として、[Box-Cox 変換](../section5/pmc52.md#Box-Cox)がある 
2. 非正規分布に適用可能な別の指標の組を採用または開発する。
非パラメトリック版（[Pearn, Tai, Hsiao, and Ao (2014)](../section7/pmc7.md#Pearn) および [Chen and Ding (2001)](../section7/pmc7.md#Chen)）の *C*<sub>*p*</sub>, *C*<sub>*pk*</sub>, *C*<sub>*pm*</sub> 能力指標の非パラメトリック版は、それぞれ *C*<sub>*np*</sub>, *C*<sub>*npk*</sub>, *C*<sub>*npm*</sub> と表記される。
これらの非パラメトリック能力指数の推定量は、以下の式によって計算される。
<br>
$$ \begin{align}
\hat{C}_{np} &= \frac{\text{USL} - \text{LSL}} {p(0.99865) - p(0.00135)} \\
\hat{C}_{npk} &= \frac{\text{min}\left[ \text{USL} - median, median - \text{LSL} \right]} {(p(0.99865) - p(0.00135))/2 } \\
\hat{C}_{npm} &= \frac{\text{USL} - \text{LSL}} {6 \sqrt{\left( \frac{p(0.99865) - p(0.00135)}{6} \right) ^2     + (中央値 - \text{T})^2}} 
\end{align} $$
<br>
ここで、*p*(0.99855) はデータの 99.865 百分数位、*p*(0.00135) はデータの 0.135 百分位数である。
これらの百分位数を用いるのは、正規分布における ±3標準偏差の包含を模倣するためである。
なお、99%の包含率を用いる文献もあることに留意されたい。
例えば、*C*<sub>*npk*</sub> 統計量は次式で表されることがある。
<br>
$$ \hat{C}_{npk} = \text{min}\left[\frac{\text{USL} - \text{中央値}} {p(0.995) - \text{中央値}}, \frac{\text{中央値} - \text{LSL}}{\text{中央値} - p(0.005)} \right] $$ 
<br><br>
ここで、*p*(0.995) はデータの 99.5 百分位数、*p*(0.005) はデータの 0.5 百分位数である。
非正規分布に関する詳細については、[Johnson and Kotz (1993)](../section7/pmc7.md#Kotz, S and)を参照のこと。

もちろん、非正規分布の場合については、他にも多くのことが言える。
しかし、Box-Cox変換をうまく適用できるのであれば、それを利用することが推奨される。 
