[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366f.htm)  
閲覧(UTC)：2026-03-05 09:08:29  
[⬅️](eda366e.md)[➡️](eda366g.md)  

1. [探索的データ解析](../eda.md)  
1.3. [EDA技法](eda3.md)  
1.3.6. [確率分布](eda36.md)  
1.3.6.6. [分布ギャラリー](eda366.md)  

---

# 1.3.6.6.15. Tukey-Lambda 分布

#### 確率密度関数
Tukey-Lambda分布の密度関数は単純な閉形式を持たない。
数値的に計算される。  

Tukey-Lambda 分布は[形状母数](eda363.md) $`λ`$ を持つ。
他の確率分布と同様に、Tukey-Lambda 分布は[位置母数](eda364.md) $`μ`$ と[尺度母数](eda364.md) $`σ`$ を用いて変換可能である。
確率関数の一般形は[標準分布を用いて表現](eda364.md#標準形に基づく位置と尺度の式)できるため、本節以降の式はすべて関数の標準形について示す。

以下は、$`λ`$ の4つの値に対する Tukey-Lambda 確率密度関数のプロットである。  
 
![plot of the Tukey-Lambda probability density function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/lampdf4.gif)  

#### 累積分布関数
Tukey-Lambda 分布は単純な閉形式を持たない。
数値的に計算される。

以下は、上記の確率密度関数のプロットと同じ *λ* の値を用いたテューキー・ラムダ累積分布関数のプロットである。 
  
![plot of the Tukey-Lambda cumulative distribution function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/lamcdf4.gif)  

#### パーセント点関数
標準形　Tukey-Lambda 分布の[パーセント点関数](eda362.md#PPF)の式は次式である。 

$$G(p;\lambda) = \frac{p^{\lambda} - (1 - p)^{\lambda}} {\lambda}$$ 

以下は、上記の確率密度関数のプロットと同じ $`λ`$ の値を用いた Tukey-Lambda パーセント点関数のプロットである。  

![plot of the Tukey-Lambda percent point function](https://www.itl.nist.gov/div898/handbook/eda/section3/gif/lamppf4.gif)  

#### 他の確率関数
Tukey-Lambda 分布は通常、適切な分布を特定するために用いられ（下記の解説参照）、統計モデルに直接使用されるものではない。
このため、ハザード関数、累積ハザード関数、生存関数、逆生存関数に関する公式およびプロットは省略する。
また、一般的な統計量および母数推定の項も省略する。

#### 解説  
Tukey-Lambda 分布は実際には分布族であり、多くの一般的な分布を近似できる。
例えば、  
$`λ=-1`$　　近似的にCauchy分布  
$`λ=0`$　　　厳密にロジスティック分布  
$`λ=0.14`$　ほぼ正規分布  
$`λ=0.5`$　　U字型  
$`λ=1`$　　完全均一分布（-1から+1まで）  

この分布の最も一般的な用途は、データ集合の Tukey-Lambda [PPCCプロット](eda33n.md)を作成することである。
PPCCプロットに基づき、データに適したモデルが示唆される。
例えば、最大相関が $`λ`$ 値 0.14 付近である場合、データは正規分布でモデル化できる。
$`λ`$ 値がこれより小さい場合、重い裾の分布（-1では Cauchy 分布に近似）を示唆する。
つまり、最適λ値が 0.14 から -1 へ移行するにつれ、裾部が次第に重くなる。
同様に、最適 $`λ`$ 値が 0.14 より大きくなるほど、裾部は短くなる。  

Tukey-Lambda 分布は対称分布であるため、Tukey-Lambda PPCCプロットを用いてデータをモデル化する適切な分布を決定する手法は、対称分布にのみ適用可能である。
データの[ヒストグラム](eda33e.md)は、そのデータが対称分布で合理的にモデル化可能か否かの判断材料を提供する。 

#### ソフトウェア
ほとんどの汎用統計ソフトウェアは、Tukey-Lambda分布の確率関数を実装していない。

---
#### 訳註  
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。  
* 原典の各プロットへのリンクはセクション番号ではなくプロット名を基準に設定されて箇所があります。mdファイルのリンク先はセクション番号だけを表示するmdファイルになっています。 
