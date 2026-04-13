[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/scatter7.htm)  
閲覧(UTC)：2026-03-05 09:04:05

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.3. [図表現技法：アルファベット順](eda33.md)  
1.3.3.26. [散布図](eda33q.md)  

---

# 1.3.3.26.7. 散布図：正弦波関係（減衰）

#### 正弦波関係を示す散布図
![1.3.3.26.7.Scatter Plot: Sinusoidal Relationship (damped)](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/scatplo7.gif)  

#### 議論
[LUTHER.DATデータ集合](https://www.itl.nist.gov/div898/handbook/datasets/LUTHER.DAT)のこのプロットにおける$`X`$と$`Y`$の複雑な関係は基本的に振動的であるように見え、したがって次式の三角関数的な正弦波モデルを描いている。  

$$Y_i=C+\alpha\sin{(2\pi\omega t_i+\phi)}+E_i$$  

散布図を詳細に観察すると、振れ幅（モデルにおける振幅$`α`$）は一定ではなく、$`X`$が大きくなるにつれて減少（減衰）しているように観える。
したがって次の結論に至り、減衰正弦波関係であり、これに対応する最も単純なモデルは次式となる。

$$Y_i=C+(B_0+B_1*t_i)\sin{(2\pi\omega t_i+\phi)}+E_i$$  

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  
* 原典の各プロットへのリンクはセクション番号ではなくプロット名を基準に設定されて箇所があります。mdファイルのリンク先はセクション番号だけを表示するmdファイルになっています。 