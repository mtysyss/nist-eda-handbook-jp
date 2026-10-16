[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pri/section6/pri62b.htm)  
閲覧(UTC)：2026-09-05 02:56:32  
[⬅️](pri62a.md)[➡️]()  

5. [工程の改善](../pri.md)  
5.6. [事例研究](pri6.md)  
5.6.2. [音響発光光強度の事例研究](pri62.md)  

---

# 5.6.2.11. 自分で解いてみる

#### [事例研究の Dataplot マクロを表示](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpm62.htm)

このページでは、これまでのページの事例研究説明で概説された分析を[Dataplot](http://www.itl.nist.gov/div898/handbook/dataplot.htm)を使用して再現することができます。
Dataplot をすでに[ダウンロードしてインストール](http://www.itl.nist.gov/div898/software/dataplot/ftp/homepage.htm)し、Dataplot を実行できるように[ブラウザを設定済み](http://www.itl.nist.gov/div898/handbook/dpbrows.htm)であることが必要である。
以下の各分析手順での出力は、1つ以上の Dataplot ウィンドウに表示される。
主なウィンドウは、出力ウィンドウ、グラフィックス・ウィンドウ、コマンド履歴ウィンドウ、およびデータシート・ウィンドウの4つである。
各メイン・ウィンドウの上部には、Dataplot のコマンドを実行するためのメニューがある。
下部には、コマンドを入力できるコマンド入力ウィンドウがある。

---
#### 訳註：
* Dataplot関係はNISTのサイトへリンクになっております。
* ***データ分析の手順列はdpプログラムがダウンロードされます。***
* 結果と結論列は、翻訳版mdファイルへのリンクになっています。

---

| データ分析の手順 |  結果と結論 |  
| :--- | :--- |  
| 以下のリンクをクリックして、Dataplotを起動し、この事例研究を実際に実行してください。各手順では、前の手順の結果が使用される場合がありますので、しばらくお待ちください。
ソフトウェアが現在の手順の完了を確認するまで待ってから、次の手順をクリックしてください。 | この欄にあるリンクをクリックすると、事例研究の説明に記載されている各分析手順に関するより詳細な情報に飛びます。 |  
| 1. 設定し開始する。 | |  
| [1. データを読み込む。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/data.dp) | [1. 変数 Y, X1, X2, X3, X4, X5, X6, X7の8行の数値行を DataPlot に読み込む 。](pri621.md#data) |  
| 2. 主効果をプロットする。 ||  
| [1. 順序付きデータ・プロット。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/order.dp)<br><br>[2. DOEの散布図。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/dexsct.dp)<br><br>[3. DOEの平均値のプロット。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/dexmea.dp) | [1. 順序付きデータ・プロットは 2点ハズレを示している。重要な因子候補は X1, X2, X3,および X7である](pri622.md#order)<br><br>[2. DOE散布図は、X1, X2,    X3, および X7 が重要因子であることを示している。](pri622.md#dexscatter)<br><br>[3. DOE平均プロットは X1, X2, X3, および X7 が重要因子であることを示している。](pri622.md#dexmean) |  
| 3. 相互作用効果のプロット ||  
| [1. DOEの相互作用効果プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/dexeff.dp) | [1. DOE交互作用効果プロットは、いくつかの重要な交互作用効果を示している。](pri623.md#dexinte) |  
| 4. 主効果および交互作用効果のブロック・プロット ||  
[1. ブロック・プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/blockp.dp) | [1. ブロック・プロットは、この事例で特に有用であるというわけではない。](pri624.md#blockplot) |  
| 5. 重要な要因を特定するための Youden プロット ||  
| [1. Youden プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/youden.dp) | [1. Youden プロットは、X1, X2, X3, および X7 が重要因子であることを示している。また、重要な交互作用のいくつかも特定している、(X1*X3, X1*X2, X2*X3).](pri625.md#youdenplot) |  
| 6. |効果| プロットを作成して重要な要因を特定する ||  
| [1. |効果| プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/effect.dp) | [1. |効果|プロットは、X2, X7, X1*X3, X1, X3, X2*X3, および X1*X2 が重要な因子および交互作用として特定している。](pri626.md#effectsplot) |  
| 7. 重要な要因を特定するための半正規確率プロット ||  
| [1. 半正規確率プロットを作成する。]() | [1. 半確率プロットは、X2, X7, X1*X3, X1, X3, X2*X3, および X1*X2 を重要な因子および交互作用として特定している。](pri627.md#halfnormalplot) |  
| 8. 累積残差標準偏差プロット ||  
| [1. 累積残差標準偏差プロットを作成する。}() |[1. 累積残差標準偏差プロットから、4主効果および 3 2因子交互作用のモデルが得られる。](pri628.md#cumressdplot) |  
| 9. DOE等高線図 ||  
| [1. 因子2および7を用いて、DOE等高線図を作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/inn/dpmacros/dexcon.dp) | [1. DOE等高線図は、X2 = -1 および X7 = -1 が最適設定であることを示している。](pri629.md#dexcon) |  
