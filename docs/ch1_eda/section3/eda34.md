[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda34.htm)  
閲覧(UTC)：2026-03-05 09:15:56

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  

---

# 1.3.4. 図表現技法：問題区分別

#### 単変量<br>$`y=c+e`$
|   |   |   |  
|:---:|:---:|:---:|  
| ![Run Sequence Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/runseqpl.gif)<br>[実行順序プロット: 1.3.3.25](eda33p.md) | ![Lag Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/lagplot.gif)<br>[遅延プロット: 1.3.3.15](eda33f.md) | ![Histogram]( https://www.itl.nist.gov/div898/handbook/eda/gif100/histogra.gif)<br>[ヒストグラム: 1.3.3.14](eda33e.md) |  
| ![Normal Probability Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/normprpl.gif)<br>[正規確率プロット: 1.3.3.21](eda33l.md) | ![4-Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/4plot.gif)<br>[4-プロット: 1.3.3.32](eda33w.md) | ![Probability Plot Correlation Coefficient Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/ppccplot.gif)<br>[確率プロット相関係数プロット: 1.3.3.23](eda33n.md) |  
| ![Weibull Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/weibullp.gif)<br>[Weibullプロット: 1.3.3.30](eda33u.md) | ![Probability Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/probplot.gif)<br>[確率プロット: 1.3.3.22](eda33m.md) | ![Box-Cox Linearity Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/boxcoxli.gif)<br>[Box-Cox 線形性プロット: 1.3.3.5](eda335.md) |  
| ![Box-Cox Normality Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/boxcox.gif)<br>[Box-Cox 正規性プロット: 1.3.3.6](eda336.md) | ![Bootstrap Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/bootstra.gif)<br>[ブートストラップ・プロット: 1.3.3.4](eda334.md) | |  

---
#### 時系列<br>$`y=f(t)+e`$
|   |   |   |  
|:---:|:---:|:---:|  
| ![Run Sequence Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/runseqpl.gif)<br>[実行順序プロット: 1.3.3.25](eda33p.md) | ![Spectrum]( https://www.itl.nist.gov/div898/handbook/eda/gif100/spectrum.gif)<br>[スペクトル図: 1.3.3.27](eda33r.md) | ![Autocorrelation Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/autocopl.gif)<br>[自己相関プロット: 1.3.3.1](eda331.md) |  

| ![Demodulation Amplitude Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/cdampplo.gif)<br>[複素復調振幅プロット: 1.3.3.8](eda338.md) | ![Complex Demodulation Phase Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/cdphasep.gif)<br>[複素復調フェーズ・プロット: 1.3.3.9](eda339.md) |  |

---
#### 1因子<br>$`y=f(x)+e`$

![Scatter Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/scatterp.gif)  
[散布図: 1.3.3.26](eda33q.md)  

![Block Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/blockplo.gif)  
[ブロック・プロット: 1.3.3.3](eda333.md)  

![Bihistogram](https://www.itl.nist.gov/div898/handbook/eda/gif100/bihistog.gif)  
[対比ヒストグラム: 1.3.3.2](eda332.md) 

![Quantile-Quantile Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/qqplot.gif)  
[分位数-分位数プロット: 1.3.3.24](eda33o.md)  

![Mean Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/meanplot.gif)  
[平均プロット: 1.3.3.20](eda33k.md)  

![Standard Deviation Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/sdplot.gif)  
[標準偏差プロット: 1.3.3.28](eda33s.md)  

---
#### 多因子/比較<br>$`y=f(x_p, x_1,x_2,...,x_k)+e`$

![Block Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/blockplo.gif)  
[ブロック・プロット: 1.3.3.3](eda333.md)  

---
#### 多因子/スクリーニング<br>$`y=f(x_1,x_2,x_3,...,x_k)+e`$

|   |   |   |  
| --- | --- | --- |  
| ![DOE Scatter Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/dexscatp.gif)<br>[DOE 散布図: 1.3.3.11](eda33b.md) | ![DOE Mean Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/dexmeanp.gif)<br>[DOE 平均プロット: 1.3.3.12](eda33c.md) | ![DOE Standard Deviation Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/dexsdplo.gif)<br>[DOE 標準偏差プロット: 1.3.3.13](eda33d.md) |  
| ![Contour Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/contourp.gif)<br>[等高線図: 1.3.3.10](eda33a.md) |  |  |  

---
#### 回帰<br>$`y=f(x_1,x_2,x_3,...,x_k)+e`$

![Scatter Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/scatterp.gif)  
[散布図: 1.3.3.26](eda33q.md)  

![6-Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/6plot.gif)  
[6-プロット: 1.3.3.33](eda33x.md)

![Linear Correlation Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/lincorrp.gif)  
[線形相関プロット: 1.3.3.16](eda33g.md)  

![Linear Intercept Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/linintpl.gif)  
[線形切片プロット 1.3.3.17](eda33h.md)  

![Linear Slope Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/linslopl.gif)  
[線形傾きプロット: 1.3.3.18](eda33i.md)

![Linear Residual Standard Deviation Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/linrsdpl.gif)  
[線形残差標準偏差プロット: 1.3.3.19](eda33j.md)  

---
#### 試験所間<br>$`(y_1,y_2)=f(x)+e`$

![Youden Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/youdenpl.gif)  
[Youden プロット: 1.3.3.31](eda33v.md)  

---
#### 多変量<br>$`(y_1,y_2,...,y_p)`$

![Star Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/starplot.gif)  
[星図: 1.3.3.29](eda33t.md) 