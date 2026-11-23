[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pmd/section8/pmd812a.htm)  
閲覧(UTC)：2026-07-26 14:08:41  
[⬅️](pmd8129.md)[➡️](pmd812b.md)  

4. [工程のモデル化](../pmd.md)  
4.8. [工程のモデル化に役立ついくつかの関数](pmd8.md)  
4.8.1. [単変数関数](pmd81.md)  
4.8.1.2. [有理関数](pmd812.md)  

---

# 4.8.1.2.10. 3次／3次有理関数

![examples of cubic/cubic rational functions](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/r33p1.r.gif)

|||  
| :--- | :--------- |  
| **関数：** | $`\displaystyle f(x) = \frac{\beta_0 + \beta_1x + \beta_2x^2 + \beta_3x^3} {1 + \beta_4x + \beta_5x^2 + \beta_6x^3}, \ \ \beta_3 \neq 0, \ \beta_6 \neq 0`$ |  
| **関数族:** | 有理 |  
| **統計の種類** | 非線形 |  
| **定義域** | $`\displaystyle (-\infty, \infty)`$<br>未定義点が次式の平方根にある。<br><br>$`\displaystyle 1 + \beta_4x + \beta_5x^2 + \beta_6x^3`$<br><br>特定の係数値に応じて、1、2、3 の根が存在する。3次多項式の根に対する明示的な解は複雑であり、ここでは示されていない。多くの数学および統計学のソフトウェア・プログラムは、多項式方程式の根を数値的に求めることができ、これらの根がどこにあるかを知る必要がある場合は、これらのプログラムのいずれかを使用することを推奨する。|  
| **値域** |  $`\displaystyle (-\infty, \infty)`$<br>$`\displaystyle y = \beta_3/\beta_6`$ が除外される例外を除き |  
| **特別な特徴** | 水平漸近線: <br>$`\displaystyle y = \beta_3 / \beta_6`$<br>垂直漸近線は次式の平方根にある。<br><br>$`\displaystyle 1 + \beta_4x + \beta_5x^2 + \beta_6x^3`$<br><br>特定の係数値に応じて、1、2、3 の根が存在する。3次多項式の根に対する明示的な解は複雑であり、ここでは示されていない。多くの数学および統計学のソフトウェア・プログラムは、多項式方程式の根を数値的に求めることができ、これらの根がどこにあるかを知る必要がある場合は、これらのプログラムのいずれかを使用することを推奨する。|  
| **追加例** | |  

![cubic/cubic rational function example 1](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/r33p2.r.gif)

![cubic/cubic rational function example 2](https://www.itl.nist.gov/div898/handbook/pmd/section8/plots/r33p3.r.gif)

---
#### 訳註
* ページ中の図およびデータのリンク先は ソースページを維持し、NISTへのリンクになっています。