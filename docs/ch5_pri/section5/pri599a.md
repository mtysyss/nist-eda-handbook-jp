[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pri/section5/pri599a.htm)  
閲覧(UTC)：2026-09-05 02:52:38  
[⬅️](pri5999.md)[➡️](pri599b.md)  

5. [工程の改善](../pri.md)  
5.5. [応用題目](pri5.md)  
5.5.9. [実験計画法におけるEDA手法](pri59.md)  
5.5.9.9. [累積残差標準偏差のプロット](pri599.md)  

---

# 5.5.9.9.10. 動機：モデルを用いた補間方法

#### 元データ単位での計画表
補間そのものの仕組みについては、前述の *k* = 2 の因子実験の続きを考える。
温度 *T* が 300 から 350 の範囲で、時間 *t* が 20 から 30 の範囲であり、解析者が *n* = 4 実験を実施できると仮定する。
2<sup>2</sup>の完全要因計画を実行する。
温度の符号化値を *X*<sub>1</sub>、時間の符号化値を *X*<sub>2</sub> とすると、以下のになる。

| 温度 | 時間  | *X*<sub>1</sub> | *X*<sub>2</sub> | *Y* |  
| :---: | :---: | :---: | :---: | :---: |  
| 300 | 20 | - | - | 2 |  
| 350 | 20 | + | - | 4 |  
| 300 | 30 | - | + | 6 |  
| 350 | 30 | + | + | 8 |  
{: .no-border-table}

#### 図解
図による計画とデータは以下の通り。

![Diagram of design and response data in orignal data units](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des2.gif){: .text-center}

#### よくある補間に関する質問
前回と同様、データから予測式は次式になる。

$$ \hat{Y} = 5 + 2 X_2 + X_1 $$

ここで、次のような典型的な補間問題を考える。

このモデルから、例えば 温度 ＝ 310、時間 ＝ 26 の時点における予測応答はいくらになるか。

要するに：

$$ \hat{Y}(T = 310, t = 26) = \text{?} $$

この問題を解くために、まず *k* = 2 の実験計画とデータをグラフ上で確認し、求める(*T* = 310, *t* = 26) の補間点がどこにあるかを（「X」で）示す。

![Diagram of design and response data with interpolation point in orignal data units](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des3.gif){: .text-center}

#### 補間点における応答の予測
次の重要な手順は、生データ（元の因子 *T* および *t* 単位）の補間点を、符号化された（*X*<sub>1</sub> および *X*<sub>2</sub>を単位とする）補間点に変換する。
グラフやその他の情報から、*T* と *X*<sub>1</sub> の間、および *t* と *X*<sub>2</sub> の間の線形変換により、以下の関係が得られる。

*T* = 300 => *X*<sub>1</sub> = -1  
*T* = 350 => *X*<sub>1</sub> = +1

したがって

*X*<sub>1</sub> = 0 は *T* = 325 にある。

```
        |-------------|-------------|
       -1     ?       0            +1
       300   310     325           350
```


これが、

*T* = 310 => *X*<sub>1</sub> = -0.6

同様に、

*t* = 20 => *X*<sub>2</sub> = -1  
*t* = 30 => *X*<sub>2</sub> = +1

したがって、

*X*<sub>2</sub> = 0 となるのは *t* = 25 のときである。

```
        |-------------|-------------|
       -1             0   ?        +1
       20             25 26        30
```


したがって
*t* = 26 => *X*<sub>2</sub>= +0.2

*X*<sub>1</sub> = -0.6 および *X*<sub>2</sub> = +0.2 を予測式

$$ \hat{Y} = 5 + 2 X_2 + X_1 $$

に代入すると予測値は 4.8 となる。

#### 補間されたデータ点の応答値のグラフ表示
したがって

![Diagram of design and response data with response for interpolated point in orignal data units](https://www.itl.nist.gov/div898/handbook/pri/section5/dpmacros/2x2des4.gif){: .text-center}


---
#### 訳註
* ページ中の図はソースページを維持し、NISTへのリンクになっています。