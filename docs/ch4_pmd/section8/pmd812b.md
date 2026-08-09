[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pmd/section8/pmd812b.htm)  
閲覧(UTC)：2026-07-26 14:08:44  
[⬅️](pmd812a.md)[➡️](../../../README.md)  

4. [工程のモデル化](../pmd.md)  
4.8. [工程のモデル化に役立ついくつかの関数](pmd8.md)  
4.8.1. [単変数関数](pmd81.md)  
4.8.1.2. [有理関数](pmd812.md)  

---

# 4.8.1.2.11. 有理関数のモデルにおける m および n の決定

#### 一般的な質問
有理関数モデルに関する一般的な質問は次の通り。

    有理関数を当てはめたいデータがある。
    分子と分母には、それぞれどの次数 $`n`$ と $`m`$ を用いればよいか。

#### 4つの質問
上記の広範な問いに答えるためには、以下の4つの具体的な問いに答える必要がある。

1. 関数は $`x=\infty`$ の点でどのような<u>値</u>をとるべきか。
具体的には、その値はゼロか定数か、それとも正もしくは負の無限大か。
2. 関数は $`x=\infty`$ でどのような<u>傾き</u>を持つべきか。
具体的には、関数の導関数はゼロか定数か、それとも正もしくは負の無限大か。
3. 有限の $`x`$ において、関数がゼロ（すなわち $`f(x)=0`$）となる回数は何回であるべきか。
4. 有限の $`x`$ において<u>傾き</u>がゼロになる（すなわち $`f'(x)=0`$）回数は何回であるべきか。

これらの問いに対しては、分析者がデータを検討し、研究対象の現象に関する理論的考察に基づいて回答する。 

以下では、これらの各問について個別に検討する。 

#### 質問 1：関数は $`x=\infty`$ でどのような値をとるべきか。
次の有理関数

$$R(x) = \frac{P_n(x)} {P_m(x)} $$

または

$$ y = \frac{a_{n}x^{n} + a_{n-1}x^{n-1} + \dots + a_{2}x^{2} + a_{1}x + a_{0}} {b_{m}x^{m} + b_{m-1}x^{m-1} + ... + b_{2}x^{2} + b_{1}x + b_{0}}$$

とすると、漸近的に次式となる。

$$R(x) \approx \left(\frac{a_n}{b_m}\right)x^{n-m} $$

ここから、以下のことが導かれる。

* $`n \lt m`$ のとき $`R(\infty)=0`$
* $`n = m`$ のとき $`R(\infty) = a_n/b_m`$
* $`n \gt m`$ のとき $`R(\infty) = \pm \infty`$ となる。

逆に、近似関数 $`f(x)`$ が以下の場合、

* $`f(\infty) = 0`$ である場合、これは $`n \lt m`$ を意味する。
* $`f(\infty) = \text{定数}`$ である場合、これは $`n = m`$ を意味する。
* $`f(\infty) = \pm \infty`$ である場合、これは $`n \gt m`$ を意味する。

#### 質問 2：この関数は $`x=\infty`$ でどのような傾きを持つべきか。
傾きは、関数の導関数によって決まる。
有理関数の導関数は次式となる。

$$R'(x) = \frac{P_m(x)P'_n(x) - P_n(x)P'_m(x)} {[P_m(x)]^2}$$

であり、

$$\begin{eqnarray}
P_n(x) &=& a_0 + a_1x + ... + a_nx^n \\
&=& \\
P'_n(x) &=& a_1 + 2a_2x + ... + na_nx^{n-1} \\
&=& \\
P_m(x) &=& b_0 + b_1x + ... + b_mx^m \\
&=& \\
P'_m(x) &=& b_1 + 2b_2x + ... + mb_mx^{m-1} \, .\\
\end{eqnarray} $$

漸近的に次式となる。

$$R'(x) \approx (n - m)\left(\frac{a_n} {b_m}\right)x^{n-m-1}$$


ここから、 いかが導かれる。

* $`n < m`$ のとき $`R'(\infty)=0`$ となり、
* $`n = m`$ のとき $`R'(\infty) = 0`$、
* $`n = m + 1`$ のとき $`R'(\infty) = a_n/b_n`$ となり
* $`n > m + 1`$ のとき $`R'(\infty) = \pm \infty`$ となる。

逆に、近似関数 $`f(x)`$ が以下の場合、

* $`f'(\infty) = 0`$ である場合、これは $`n \le m`$ を意味する。
* $`f'(\infty) = \text{定数}`$ である場合、これは $`n = m + 1`$ を意味する。
* $`f'(\infty) = \pm \infty`$ である場合、これは $`n > m + 1`$ を意味する。

#### 質問 3：有限の $`x`$ に対して、関数は何回ゼロになるべきか。
有限な $`x`$ について、$`R(x)=0`$ となるのは、分子の多項式 $`P_n`$ がゼロに等しい場合に限られる。

故に、分子多項式$`R(x)`$ も、0 から $`n`$ までの実根を持つことがある。
したがって、与えられた $`n`$ に対して、$`R(x)`$ の実根の個数は $`n`$ 以下である。

逆に、近似関数 $`f(x)`$ が、有限の $`x`$ に対して $`f(x)=0`$ となる回数が $`k_3`$ であるような関数であるならば、$`n`$ は $`k_3`$ 以上である。 

#### 質問 4：有限の $`x`$ に対して、傾きがゼロになる回数は何回か。
有理関数の導関数 $`R'(x)`$ は、分子の多項式がゼロになるとき、ゼロになる。
多項式の実根の個数は、ゼロからその多項式の次数までの範囲にある。

$`n \ne m`$ の場合、$`R'(x)`$ の分子多項式の次数は $`n + m - 1`$ である。
$`n = m`$ に対しては、$`R'(x)`$ の分子多項式の次数は $`n + m - 2`$ である。

ここから、次のことが導かれる。

* $`n \ne m`$ のとき $`R'(x)`$ の実根の数 $`k_4`$ は $`n + m - 1`$ 以下である。
* $`n = m`$ のとき $`R'(x)`$ の実根の数 $`k_4`$ は $`n + m - 2`$ 以下である。

逆に、適合関数 $`f(x)`$ が、有限の $`x`$ および $`n \ne m`$ に対して $`f'(x) = 0`$ となる回数が $`k_4`$ であるような関数であるならば、$`n + m - 1`$ は $`\ge k_4`$ となる。
同様に、適合関数 $`f(x)`$ が有限の $`x`$ および $`n = m`$ に対して、$`f'(x) = 0`$ となる回数が $`k_4`$ である場合、$`n + m - 2 \ge k_4`$ となる。 

#### $`m`$ と $`n`$ の許容される組合せを決定するための表
要約すると、以下の4つの表を用いて $`n`$ 対 $`m`$ のグラフを作成し、$`n`$と$`m`$ の許容される組合せを特定する。
初期の有理関数モデルの次数については、最も単純な$`(n, m)`$ の組合せを選択する。

| 1. $`f(\infty)`$ の目的値 | $`n`$ と $`m`$の関係 |  
| :---- | :---- |  
| 0<br>定数<br>$`\infty`$ | $`n \lt m`$<br>$`n = m `$<br>$`n \gt m `$ |  

| 2. $`f'(\infty)`$ の求める値 | $`n`$と$`m`$ の関係 |  
| :---- | :---- |  
| 0<br>定数<br>$`\infty`$ | $`n \lt m + 1`$<br>$`n = m + 1`$<br>$`n \gt m + 1`$ |  

| 3. 有限な $`x`$ について、<br>$`f(x) = 0`$となる目標値 $`k_3`$ | $`n`$ と $`k_3`$の関係 |  
| :---- | :---- |  
| $`k_3`$ | $`n \ge k_3`$ |  

| 4. 有限な $`x`$ について、<br>$`f'(x) = 0`$となる回数の目標値$`k_4`$ | $`n`$ と $`k_4`$ および $`m`$
との関係 |  
| :---- | :---- |  
| $`k_4 (n \ne m)`$<br>$`k_4 \, (n = m)`$ | $`n \ge (1 + k_4) - m`$<br>$`n \ge (2 + k_4) - m`$ |  


#### $`m`$ および $`n`$ を決める例
目標は、標本データ集合から特定の有理関数へと導くことである。
以下のグラフは、有理関数が採り得る一般的な形状をまとめたもので、許容値と、$`n`$ および $`m`$ に関する最も単純なケースを示していり。
通常は、最も単純なケースから検討を始める。
モデルの妥当性確認の結果、モデルが不適切であると判断された場合は、許容領域内の他の有理関数を試してみる。

#### 形状 1
![plot showing admissiable n and m for shape 1](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape1.gif)

#### 形状 2
![plot showing admissiable n and m for shape 2](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape2.gif)

#### 形状 3
![plot showing admissiable n and m for shape 3](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape3.gif)

#### 形状 4
![plot showing admissiable n and m for shape 4](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape4.gif)

#### 形状 5
![plot showing admissiable n and m for shape 5](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape5.gif)

#### 形状 6
![plot showing admissiable n and m for shape 6](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape6.gif)

#### 形状 7
![plot showing admissiable n and m for shape 7](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape7.gif)

#### 形状 8
![plot showing admissiable n and m for shape 8](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape8.gif)

#### 形状 9
![plot showing admissiable n and m for shape 9](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shape9.gif)

#### 形状 10
![plot showing admissiable n and m for shape 10](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/shap10.gif)


---
#### 訳註
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。
