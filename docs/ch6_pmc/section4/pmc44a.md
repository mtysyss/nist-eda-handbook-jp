[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a.htm)  
閲覧(UTC)：2026-10-17 02:19:27  
[⬅️](pmc449.md)[➡️](pmc45.md)  

6. [工程や製品の監視と管理](../pmc.md)  
6.4. [時系列解析入門](pmc4.md)  
6.4.4. [単変量時系列モデル](pmc44.md)  

---

# 6.4.4.10. 季節性データのBox-Jenkins分析

#### 系列 G
この例では、[Box, Jenkins, and Reinsel (1994)](../section7/pmc7.md#Box,%20G.E.P.;%20G.M.) に掲載されている[系列G データ集合](https://www.itl.nist.gov/div898/handbook/datasets/G_SERIES.DAT)を用いた、季節性データに対する Box-Jenkins時系列分析を示している。
144個の観測値のプロットを以下に示す。

![Plot of Series G Data](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a_r01.gif)

分散の変動は、自然対数変換を行うことで除去できる。

![Plot of natural log of series G](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a_r02.gif)

次に、1次差分をとることで、時系列からトレンドを除去する。
その結果得られた時系列を以下に示す。

![Plot of first differences of the natural log of series G](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a_r03.gif)

#### 季節性の自己相関プロットの分析
適切なモデルを同定するために、時系列のACFをプロットする。

![ACF plot of first differenced natural log series G](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a_r04.gif)

もし、*n* 期間間隔のラグ、例えばラグ12 や 24で非常に大きな自己相関が観測される場合、それは周期性の証拠である。
識別段階の目的は全体を通して自己相関を低減することであるため、その影響は除去する必要がある。
したがって、単純な差分処理では不十分な場合は、4、6、12などの選択した周期で季節差分処理を試みる。
この例では、季節周期は12である。

自然対数変換、1次差分、および季節差分処理を施した系列Gのプロットを以下に示す。

![Seasonal and first differenced natural log of series G](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a_r05.gif)

季節項の数が 1を超えることはめったにない。
予測関数の形状が分かっている場合、あるいは予測関数に特定の形状を割り当てたい場合は、季節ARモデルまたは季節MAモデルに適した項の数を選択する。

BoxとJenkinsの著書『*Time Series Analysis Forecastingand Control*』（改訂版はBox, Jenkins, Reinsel, 1994）の326～328ページに、これらの予測関数に関する解説がある。
繰り返しになるが、漠然としたイメージしかない場合でも、差分処理を行う前に上昇傾向があったことが分かっているのであれば、季節性MA項を選んで、診断結果がどう出るか確認してみること。

時系列Gの自然対数値に対する季節成分および1次差分後のACFプロットを以下に示す。

![Autocorrelation plot after taking seasonal difference](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a_r06.gif)

プロットにはいくつかのスパイクが見られるが、ほとんどの自己相関はゼロ近くであり、季節MA(1)モデルが適切であることを示している。 

#### モデル適合
データに対して季節性MA(1)モデルを適合した。

$$ X_t - \delta = A_t + \theta_1  A_{t-1} + \psi_1  A_{t-12}+ \theta_1  \psi_1  A_{t-13}  , $$

ここで、$`\theta_1`$ はMA(1)母数を、$`\psi_1`$ は季節母数を表す。
モデル適合の結果を以下に示す。

```
                            Seasonal
Estimate            MA(1)     MA(1)
--------          -------    -------
Parameter         -0.4018    -0.5569
Standard Error     0.0896     0.0731

Residual standard deviation = 0.0367  
Log likelihood = 244.7
AIC = -483.4
```

Box-Ljung検定を用いて、最大 30ラグまでの残差の無作為性を検定する。
なお、棄却域の自由度は、推定された 2母数を考慮して調整する必要がある。

```
H0:  The residuals are random.
Ha:  The residuals are not random.  

Test statistic:  Q = 29.4935
Significance level:  α = 0.05
Degrees of freedom:  h = 30 - 2 = 28
Critical value:  Χ 21-α,h = 41.3371 
Critical region: Reject H0 if Q > 41.3371
```

Box-Ljung検定の帰無仮説は棄却されなかったため、推定モデルは適切であると結論付ける。

#### 予測
季節性MA(1)モデルを用いて、12期間先までの予測値を計算し、90 %信頼区間を計算した。

```
              Lower                   Upper
    Period    Limit      Forecast     Limit
    ------   --------    --------    --------
      145    424.0234    450.7261    478.4649
      146    396.7861    426.0042    456.7577
      147    442.5731    479.3298    518.4399
      148    451.3902    492.7365    537.1454
      149    463.3034    509.3982    559.3245
      150    527.3754    583.7383    645.2544
      151    601.9371    670.4625    745.7830
      152    595.7602    667.5274    746.9323
      153    495.7137    558.5657    628.5389
      154    439.1900    497.5430    562.8899
      155    377.7598    430.1618    489.1730
      156    417.3149    477.5643    545.7760
```

![Plot of forecasted values with 90 % confidence limits](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a_r07.gif)

このページに掲載されているすべての分析結果は、[Rコード](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44a.r)を使用して作成することができる。

---
#### 訳註
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。
