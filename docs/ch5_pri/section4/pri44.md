[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pri/section4/pri44.htm)  
閲覧(UTC)：2026-08-09 15:49:57  
[⬅️](pri43.md)[➡️](pri45.md)  

5. [工程の改善](../pri.md)  
5.4. [DOEデータの分析](pri4.md)  

---

# 5.4.4. DOEモデルの検定と修正方法

#### モデルの検定、修正、および選択のツール
最終的なDOEモデルの検定、修正、および選定に必要なすべてのツールと手順については、本ハンドブックの各節で解説している。
以下の概要では、最も一般的で有用な技法の多くを紹介し、詳細説明へのリンクも掲載する。

**モデルの検定と修正の概要：ツールと手順**

#### 概要
概要（リンク付き）には、DOEモデルの検定と修正に役立つツールや手順のほとんどを網羅している。

* モデル検定のための可視化指標（残差の利用）
    * [応答値対予測値](../../ch1_eda/section3/eda33q.md)
    * [残差対予測値](../../ch1_eda/section3/eda33q.md)
    * [残差対独立変数](../../ch1_eda/section3/eda33q.md)
    * [残差の遅延プロット](../../ch1_eda/section3/eda33f.md)
    * [残差のヒストグラム](../../ch1_eda/section3/eda33e.md)
    * [残差の正規確率プロット](../../ch1_eda/section3/eda33l.md)
* モデルおよびモデル項の検証に関する総合的な数値指標
    * R二乗と調整済みR二乗値
    * [モデルの適合度不足の検定](pmd44.md)
    * 分散分析（ANOVA）表（[3章](../../ch3_ppc/section2/ppc23.md)または[7章](../../ch7_prc/section4/prc43.md)を参照）
    * [*p*-値](../../ch7_prc/section1/prc131.md)
* モデル選択ツールや手順
    * ANOVA表（[3章](../../ch3_ppc/section2/ppc23.md)または[7章](../../ch7_prc/section4/prc43.md)章を参照）
    * [*p*-値](../../ch7_prc/section1/prc131.md)
    * [残差分析](pmd44.md#resdef)
    * [モデルの不適合検定](pmd44.md)
    * [正規性](../../ch1_eda/section3/eda336.md)および[線形性](../../ch1_eda/section3/eda335.md)のためのデータ変換
    * 段階的回帰の手順
    * 効果の[正規](../../ch1_eda/section3/eda33l.md)プロットまたは半正規プロット（主に2水準の完全および一部実施要因実験用）
    * [Youden プロット](../../ch1_eda/section3/eda33v.md)
    * [その他の手法](../section6/pri615.md)

---
#### 訳註
* [原典](https://www.itl.nist.gov/div898/handbook/pri/section4/pri44.htm)では、「分散分析」に関するリンク（3章: section2/ppc222、7章: section4/prc42）は、リンク先がないかもしくは違うページにリンクされています。(2026-08-20確認)該当ページ節と考えられるリンクに変更しています。
