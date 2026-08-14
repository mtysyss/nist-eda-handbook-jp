[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/mpc/section4/mpc44.htm)  
閲覧(UTC)：2026-06-06 15:24:44  
[⬅️](mpc433.md)[➡️](mpc441.md)  

2. [測定工程の特徴付け](../mpc.md)  
2.4. [ゲージR&R研究](mpc4.md)  

---

# 2.4.4. ばらつきの分析

#### 枝分かれ設計のばらつき分析
本節の目的は、3段階枝分かれ設計の各階層の標準偏差を用いて、測定工程のばらつきに及ぼす各階層の時間依存性効果を示すことである。

* [階層1 - 繰り返し性／短期精度](mpc441.md)  
* [階層2 - 再現性／日間](mpc442.md)  
* [階層3 - 安定性／実行間](mpc443.md)

以下のグラフは、概念を説明するために、2段階設計（短期反復と日）における考えられるシナリオを示している。

#### 6日間に渡る短期ばらつきが同程度の2つの測定工程の図解[^1]
工程1 は日間のばらつきが大きく、工程2 は日間のばらつきがわずかである。

| Process 1<br>Large between-day variability | Process 2<br>Small between-day variability |
| :---: | :---:|
| ![process 1:large between-day variability](https://www.itl.nist.gov/div898/handbook/mpc/section4/mpc44j.gif) | ![process 2:small between-day variability](https://www.itl.nist.gov/div898/handbook/mpc/section4/mpc44k.gif) |

6日間に渡る短期測定値の分布中心線からの距離は、日間のばらつきを示す。

#### 表を用いた分析方法に関するヒント
簡単な始め方は、繰り返し性／再現性測定の *J* 列 *K* 行の[2階層表](../section6/mpc632.md)を用いて、次のように進めることである。

1. 各行の平均を計算し、それを *J* + 1 列に入力する。
2. 各行について階層1（繰り返し性）の標準偏差を計算し、*J* + 2 列に記入する。
3. *J* + 1 列目のデータから、全体平均と階層2 の標準偏差を計算する。
4. *L* 回の実行それぞれについて、この表を繰り返す。
5. *L* 個の全体平均値から階層3 の標準偏差を計算する。

#### 階層1：データから計算される *LK* 繰り返し性標準偏差
枝分かれ設計による測定値は、以下で表す。

$$Y_{lkj}(l = 1, \ldots, L,\quad k=1,\ldots, K,\quad j=1,\ldots, J)$$

表形式の解析に対応する式を以下に示す。
階層1の[繰り返し性標準偏差](mpc441.md) $`{\large s}_{1lk}`$ 、は、*K* 日間、*L* 回の実行を組み入れる。
それぞれ (*J*- 1) の自由度を持つ個々の標準偏差は、*J* 回の反復から次式で計算する。
 
$$s_{1lk} = \sqrt{\frac{1}{J-1} \sum_{j=1}^{J}{(Y_{lkj} - \overline{Y}_{lk{\small \bullet}})^2}}$$

ここで

$$\overline{Y}_{lk{\small \bullet}} = \frac{1}{J}\sum_{j=1}^{J}{\overline{Y}_{lkj}}$$

#### 階層2：データから計算される *L* 再現性標準偏差
*L* 回の実行について、[階層2の標準偏差 $`{\large s}_{2l}`$に組み入れる](mpc442.md)。
自由度 (*K*- 1) を持つ個々の標準偏差は、*K* 日の平均値から次式で計算する。

$${\large s}_{2l} = \sqrt{\frac{1}{K-1} \sum_{k=1}^{K}{\left( Y_{lk{\small \bullet}} - \overline{Y}_{l{\small \bullet \bullet}} \right)^2}} $$

ここで

$$\overline{Y}_{l{\small \bullet \bullet}} = \frac{1}{K}\sum_{k=1}^{K}{\overline{Y}_{lk {\small \bullet}}}$$

#### 階層3：*L* 回実行平均値から計算される1全標準偏差
自由度 (*L*- 1) を持つ階層3の標準偏差は、*L回の*実行の平均値から次式で計算する。

$$ {\large s}_{3} = \sqrt{\frac{1}{L-1} \sum_{l=1}^{L}{\left( Y_{l{\small \bullet \bullet}} - \overline{Y}_{{\small \bullet \bullet \bullet}} \right)^2}} $$

ここで

$$ \overline{Y}_{{\small \bullet \bullet \bullet}} = \frac{1}{L}\sum_{l=1}^{L}{\overline{Y}_{l {\small \bullet \bullet}}}$$

#### [試験対象の不確かさ](../section5/mpc56.md)との関連性
試験対象の 1回測定における不確かさを定義する標準偏差は、次式で与えられる。

$${\large s}_R = \sqrt{ {\large s}_{runs}^2 + {\large s}_{days}^2 + {\large s}_1^2}= srqt{ {\\large s}_3^2 + \frac{K-1}{K} {\large s}_2^2 + \frac{J-1}{J} {\large s}_1^2}$$

ここで、組み入れた値 $`{\large s}_1`$ および $`{\large s}_2`$ は、通常、

$${\large s}_1 = \sqrt{\frac{\sum_{l=1}^{L}{\sum_{k=1}^{K}{{\large s}_{1lk}^{2}}}}{LK}}$$

および

$${\large s}_2 = \sqrt{\frac{1}{L} \sum_{l=1}^{L}{{\large s}_{2l}^{2}}}$$

となり、時間依存成分は、以下のように個別に計算する。

$${\large s}_{runs} = \sqrt{ {\large s}_3^2 - \frac{1}{K} {\large s_2^2}}$$

$${\large s}_{days} = \sqrt{ {\large s}_2^2 - \frac{1}{J} {\large s_1^2}}$$

測定工程には他の不確かさ源が存在することがあり、それらを正式な[不確かさの解析](../section5/mpc5.md)において考慮しなければならない。

---
#### 訳註
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。

[^1]: 可読性を改善するために、見出しの一部を本文に移動した。