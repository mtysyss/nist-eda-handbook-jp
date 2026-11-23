[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pri/section4/pri4.htm)  
閲覧(UTC)：2026-08-09 15:49:31  
[⬅️](../section3/pri33a.md)[➡️](pri41.md)  

5. [工程の改善](../pri.md)  

---

# 5.4. DOEデータの分析

#### この節の内容
実験データに適合させたい初期モデルがあり、且つ実験が目的に合わせて適切に計画されているならば、ほとんどの DOEソフトウェア・パッケージで DOEデータの分析が可能である。
この節では、まず一般的な基本手順を概説し、その後ソフトウェアの具体例を示し、DOEの解析方法を解説する。
この節の内容は以下の通り。

* [DOE分析の手順](pri41.md)
* [DOEデータのプロット](pri42.md)
* [DOEデータのモデル化](pri43.md)
* [DOEモデルの検証と修正](pri44.md)
* [DOE結果の解釈](pri45.md)
* [DOE結果の検証](pri46.md)
* [DOEの例](pri47.md)
    * [完全実施要因計画の例](pri471.md)
    * [一部実施要因計画の例](pri472.md)
    * [応答曲面の例](pri473.md)

#### DOE分析に必要な統計ツールおよび概念
この節の例では、読者が以下の概念について理解していることを前提としている。

* ANOVA表（[3章](../../ch3_ppc/section2/ppc23.md)または[7章](../../ch7_prc/section4/prc42.md)を参照）
* [p値](../../ch7_prc/section1/prc131.md)
* [残差分析](../../ch4_pmd/section4/pmd44.md#resdef)
* [モデルの適合度検定](../../ch4_pmd/section4/pmd44.md)
* [正規性](../../ch1_eda/section3/eda336.md)へのデータ変換および[線形](../../ch1_eda/section3/eda335.md)