[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pri/section6/pri61c.htm)  
閲覧(UTC)：2026-09-05 02:55:28  
[⬅️](pri61b.md)[➡️](pri62.md)  

5. [工程の改善](../pri.md)  
5.6. [事例研究](pri6.md)  
5.6.1. [渦電流探針感度の事例研究](pri61.md)  

---

# 5.6.1.12. 自分で解いてみる

#### [事例研究の Dataplot マクロを表示](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpm61.htm)

このページでは、ここまでのページの事例研究説明で概説された分析を[Dataplot](http://www.itl.nist.gov/div898/handbook/dataplot.md) を使用して再現することができる。
Dataplot をすでに[ダウンロードしてインストール](http://www.itl.nist.gov/div898/software/dataplot/ftp/homepage.htm)し、Dataplot を実行できるように[ブラウザを設定済み](http://www.itl.nist.gov/div898/handbook/dpbrows.htm)であることが必要である。
以下の各解析手順での出力は、1つ以上の Dataplot ウィンドウに表示される。
主なウィンドウは、出力ウィンドウ、グラフィックス・ウィンドウ、コマンド履歴ウィンドウ、およびデータシート・ウィンドウの4つである。
各メイン・ウィンドウの上部には、Dataplot のコマンドを実行するためのメニューがある。
下部には、コマンドを入力できるコマンド入力ウィンドウがある。

---
#### 訳註：
* Dataplot関係はNISTのサイトへリンクになっております。
* ***データ分析の手順列はdpプログラムがダウンロードされます。***
* 結果と結論列は、翻訳版mdファイルへのリンクになっています。

---

| データ分析の手順 | 結果と結論 |  
| :--- | :--- |  
| 以下のリンクをクリックして、Dataplot を起動し、この事例研究を実際に実行してください。各手順では、前の手順の結果が使用される場合がありますので、しばらくお待ちください。
ソフトウェアが現在のステップの完了を確認するまで待ってから、次のステップをクリックしてください。 | この列のリンクをクリックすると、事例研究の説明に記載されている各分析手順のより詳細な情報に飛びます。 |  
| 1. 設定し開始する。 | |  
| [1. データを読み込む。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/data.dp) | [1. 変数 Y, X1, X2, X3の4行の数値行を DataPlot に読み込む 。](pri611.md#data) |  
| 2. 主効果をプロットする。 ||  
| [1. 順序付きデータ・プロット](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/order.dp)<br><br>[2. DOEの散布図](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/dexsct.dp)<br><br>[3. DOE平均プロット](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/dexmea.dp) | [1. 順序付きデータ・データプロットは、因子1は明らかに重要、因子2はやや重要であることを示している。](pri612.md#order)<br><br>[2. DOE散布図は、因子1と因子にについて有意差を示している。](pri612.md#dexscatter)<br><br>[3. DOE平均プロットは、因子1と因子2の平均において有意差を示している。](pri612.md#dexmean) |  
| 3. 交互作用効果プロット ||  
| [1. DOE交互作用効果行列プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/dexeff.dp) | [1. DOE交互作用効果行列プロットは、重要な交互作用効果があることをを示していない。](pri613.md#dexinte) |  
| 4. 主効果および交互作用効果のブロック・プロット ||  
| [1. ブロック・プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/blockp.dp) |  [1. ブロック・プロットは、因子1および因子2の効果がその他の因子の組合せ全てに渡り一貫していることを示している。](pri614.md#blockplot) |  
| 5. 主効果および交互作用効果を推定する ||  
| [1. Yates 法を用いて、主効果および交互作用効果を推定する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/yates.dp) | [1. Yates 分析は、因子1および因子2 主効果が有意であり、因子2と因子3の交互作用が統計的有意の教会にあることを示している。](pri615.md#yates) |  
| 6. モデルの選択 ||  
| [1. 効果の半正規確率プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/normpr.dp)<br><br>[2. 効果の Youden プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/youden.dp) | [1. 確率プロットは、モデルが因子1と因子2の主効果を含むべきであることを示している。](pri618.md#normprob)<br><br>[2. Youden プロットは、もでるが因子1と因子2の主効果を含むべきであることを示している。](pri618.md#youden) |  
| 7. モデルの検証 ||  
| [1. イェーツ分析によって提案された部分モデルから、残差と予測値を計算する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/fitpart.dp)<br><br>[2. モデル妥当性確認のために残差プロットを作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/part.dp) | [1. 残差と予測値の値をリンクをクリックして確認する。](pri619.md#partmodel)[2. 残差プロットは、因子1と因子2の主効果を入れたモデルに対していかなる大きな問題も示していない。](pri619.md#resplots) |  
| 8. DOEの等高線図 ||  
| [1. 因子1および2を用いて、DOEの等高線図を作成する。](https://www.itl.nist.gov/div898/handbook/pri/section6/splett3/dpmacros/dexcon.dp) | [1. DOE等高線図は、 X1 = -1 および X2 = +1 が最適設定であることを示している](pri61a.md#dexcontour) |  
