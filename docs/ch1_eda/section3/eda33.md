[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda33.htm)  
閲覧(UTC)：2026-03-26 09:17:58  
[⬅️](eda32.md)[➡️](eda331.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)

---

# 1.3.3. 図表現技法：アルファベット順  

この節では、いくつかの有用な図表現技法のギャラリーを提供する。
技法をアルファベット順に並べられていが、順番通りに読むことを意図していない。
本章の[事例研究](../section4/eda4.md)において、これらの図表現技法の大部分の使用が示されている。
これらの図表現技法のいくつかは、後の章で実演されている。  

|   |   |   |   |  
|:---:|:---:|:---:|:---:|   
| ![Autocorrelation Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/autocopl.gif)<br>[自己相関プロット: 1.3.3.1](eda331.md) | ![Bihistogram](https://www.itl.nist.gov/div898/handbook/eda/gif100/bihistog.gif)<br>[対比ヒストグラム: 1.3.3.2](eda332.md) | ![Block Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/blockplo.gif)<br>[ブロック・プロット: 1.3.3.3](eda333.md) | ![Bootstrap Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/bootstra.gif)<br>[ブートストラップ・プロット: 1.3.3.4](eda334.md) |  
| ![Box-Cox Linearity Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/boxcoxli.gif)<br>[Box-Cox 線形性プロット: 1.3.3.5](eda335.md) | ![ox-Cox Normality Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/boxcox.gif)<br>[Box-Cox 正規性プロット: 1.3.3.6](eda336.md) | ![Box Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/boxplot.gif)<br>[箱ひげ図: 1.3.3.7](eda337.md) | ![Demodulation Amplitude Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/cdampplo.gif)<br>[複素復調振幅プロット: 1.3.3.8](eda338.md) |  
| ![Complex Demodulation Phase Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/cdphasep.gif)<br>[複素復調フェーズ・プロット: 1.3.3.9](eda339.md) | ![Contour Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/contourp.gif)<br>[等高線図: 1.3.3.10](eda33a.md) | ![DOE Scatter Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/dexscatp.gif)<br>[DOE 散布図: 1.3.3.11](eda33b.md) | ![DOE Mean Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/dexmeanp.gif)<br>[DOE 平均プロット: 1.3.3.12](eda33c.md) |  
| ![DOE Standard Deviation Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/dexsdplo.gif)<br>[DOE 標準偏差プロット: 1.3.3.13](eda33d.md) | ![Histogram]( https://www.itl.nist.gov/div898/handbook/eda/gif100/histogra.gif)<br>[ヒストグラム: 1.3.3.14](eda33e.md) | ![Lag Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/lagplot.gif)<br>[遅延プロット: 1.3.3.15](eda33f.md) | ![Linear Correlation Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/lincorrp.gif)<br>[線形相関プロット: 1.3.3.16](eda33g.md) |  
| ![Linear Intercept Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/linintpl.gif)<br>[線形切片プロット 1.3.3.17](eda33h.md) | ![Linear Slope Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/linslopl.gif)<br>[線形傾きプロット: 1.3.3.18](eda33i.md) | ![Linear Residual Standard Deviation Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/linrsdpl.gif)<br>[線形残差標準偏差プロット: 1.3.3.19](eda33j.md) | ![Mean Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/meanplot.gif)<br>[平均プロット: 1.3.3.20](eda33k.md) |  
| ![Normal Probability Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/normprpl.gif)<br>[正規確率プロット: 1.3.3.21](eda33l.md) | ![Probability Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/probplot.gif)<br>[確率プロット: 1.3.3.22](eda33m.md) | ![Probability Plot Correlation Coefficient Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/ppccplot.gif)<br>[確率プロット相関係数プロット: 1.3.3.23](eda33n.md) | ![Quantile-Quantile Plot](https://www.itl.nist.gov/div898/handbook/eda/section3/gif100/qqplot.gif)<br>[分位数-分位数プロット: 1.3.3.24](eda33o.md) |  
| ![Run Sequence Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/runseqpl.gif)<br>[実行順序プロット: 1.3.3.25](eda33p.md) | ![Scatter Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/scatterp.gif)<br>[散布図: 1.3.3.26](eda33q.md) | ![Spectrum]( https://www.itl.nist.gov/div898/handbook/eda/gif100/spectrum.gif)<br>[スペクトル図: 1.3.3.27](eda33r.md) | ![Standard Deviation Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/sdplot.gif)<br>[標準偏差プロット: 1.3.3.28](eda33s.md) |   
| ![Star Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/starplot.gif)<br>[星図: 1.3.3.29](eda33t.md) | ![Weibull Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/weibullp.gif)<br>[Weibullプロット: 1.3.3.30](eda33u.md) | ![Youden Plot]( https://www.itl.nist.gov/div898/handbook/eda/gif100/youdenpl.gif)<br>[Youden プロット: 1.3.3.31](eda33v.md) | ![4-Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/4plot.gif)<br>[4-プロット: 1.3.3.32](eda33w.md) |  
| ![6-Plot](https://www.itl.nist.gov/div898/handbook/eda/gif100/6plot.gif)<br>[6-プロット: 1.3.3.33](eda33x.md) | | | |  

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。
* 原典の各プロットへのリンクは節番号ではなくプロット名を基準に設定されています。mdファイルでは節番号にリンクを変更しております。（REMARKS.md参照）