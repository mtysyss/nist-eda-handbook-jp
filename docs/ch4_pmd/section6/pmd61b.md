[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pmd/section6/pmd61b.htm)  
閲覧(UTC)：2026-07-26 14:04:38  
[⬅️](pmd61a.md)[➡️](pmd62.md)  

4. [工程のモデル化](../pmd.md)  
4.6. [工程モデル化の事例研究](pmd6.md)  
4.6.1. [ロードセルの校正](pmd61.md)  

---

# 4.6.1.11. 自分で解いてみる

#### [事例研究の Dataplot マクロを表示](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpm61.htm)

このページでは、DataPlot を[ダウンロードしインストール](https://www.itl.nist.gov/div898/software/dataplot/ftp/homepage.htm)してあるならば、ここまでの事例研究で概説された分析を [Dataplot](https://www.itl.nist.gov/div898/software/dataplot/homepage.htm) を使用して再現する。
以下の各解析手順での出力は、1つ以上の Dataplot ウィンドウに表示される。
主なウィンドウは、出力ウィンドウ、グラフィックス・ウィンドウ、コマンド履歴ウィンドウ、およびデータシート・ウィンドウの 4つである。
各メイン・ウィンドウの上部には、Dataplot コマンドを実行するためのメニューが配置されている。
下部には、コマンドを入力できるコマンド入力ウィンドウがある。

---
#### 訳註：
* Dataplot関係はNISTのサイトへリンクになっております。
* ***データ分析の手順列はdpプログラムがダウンロードされます。***
* 結果と結論列は、翻訳版mdファイルへのリンクになっています。

---

| データ分析の手順 | 結果と結論 |  
| :--- | :--- |  
| 以下のリンクをクリックしてDataplotを開始し、この例題を実行してください。各手順は前の手順の結果を使用する場合があります。ソフトウェアが処理中の手順が完了していることを確認するまで、次の手順をクリックするのをお待ちください。 | この列のリンクは、事例研究の解説各分析手順に関する詳細情報へのリンクです。 |  
| 1. 設定し開始する。 | |  
| [1. データを読み込む。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/data.dp) | [1. 撓みと荷重の変数の2行の数値行を DataPlot に読み込む 。](pmd611.md#data) |  
| 2. 初期モデルの当てはめと妥当性の確認。 ||  
| [1. 撓み と 荷重のプロット](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/initmd.dp)<br><br>[2. データに直線モデルを当てはめる](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/mfit1.dp)<br><br>[3. モデルの予測値をプロットし、データを載せる](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra1a.dp)<br><br>[4. 残差と荷重のプロット](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra1b.dp)<br><br>[5. 残差と予測値のプロット](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra1c.dp) <br><br>[6. 残差の4-プロット](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra1d.dp) <br><br>[7. 適合の数値出力を確認](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/nmv1.dp)  | [1. プロットに基づくと、直線モデルはデータを適切に筈。](pmd612.md#ip)<br><br>[2. 直線適合を実施する。数値出力解釈の前に、残差のブラフ分析を行う。](pmd613.md#dpo)<br><br>[3. 予測値の重ね合せと観測値はモデルがOKであることを示唆している。](pmd614.md#dfp)<br><br>[4. 直線が適切でない時、残差は無作為ではない。](pmd614.md#rl) <br><br>[5. このプロットは前のプロットと同じ情報を示している。](pmd614.md#rpv) <br><br>[6. 全ての4-プロットはモデルの問題を示している。](pmd614.md#f4p) <br><br>[7. 大きい不適合 F統計量(>214)から、直線モデルが不適切であると確認できる。](pmd615.md#dpo) |  
| 3. 精緻化モデルへの当てはめと妥当性の確認。 ||  
| [1. 残差と荷重のプロットを参照する。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/mrfn1.dp)<br><br>[2. データに2次モデルを当てはめる。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/mfit2.dp)<br><br>[3. モデルからの予測値をプロットし、データを載せる。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra2a.dp) <br><br>[4. 残差と荷重のプロット。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra2b.dp) <br><br>[5. 残差と予測値のプロット。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra2c.dp) <br><br>[6. 残差の4-プロット。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/gra2d.dp) <br><br>[7. 適合の数値出力を確認。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/nmv2.dp) | [1. プロットの構造は2次モデルがデータをよく表していることを示している。](pmd616.md#rl)<br><br>[2. 2次当てはめを行う。数値出力の解釈を試みるまえに残差のグラフ分析を行う。](pmd617.md#dpo)<br><br>[3. 予測値と観測値の重ね合せもモデルがOKであることを示唆している。](pmd618.md#dfp)<br><br>[4. 残差は無作為に見えることから2次モデルはOKであることを示唆している。](pmd618.md#rl)<br><br>[5. 残差と予測値のプロットも2次モデルがOKであることを示唆している。](pmd618.md#rpv)<br><br>[6. これらプロットはなんらモデルに問題がないことを示している。](pmd618.md#f4p)<br><br>[7. 小さな不適合 F統計量（<1）から、2次モデルがデータに適合していることが確認される。](pmd619.md#dpo) |  
| 4. モデルを用いて測定の校正を行う。 ||  
| [1. 新しい撓み値を観測する。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/clbints1.dp)<br><br>[2. 関連した加重を決定する。](https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/clbints2.dp) <br><br>[3. 加重推定値の不確かさを計算する。]https://www.itl.nist.gov/div898/handbook/pmd/section6/ldcll/dpmacros/clbints3.dp) | [1. 新しい撓みは測定されていない未知の荷重に関連付けられている。](pmd61a.md#nd)<br><br>[2. 校正方程式を解き、未観測で荷重値を得る。](pmd61a.md#nl)<br><br>[3. 測定ノイズが工程に影響を与えることは既知であることから、荷重値の信頼区間を計算し、妥当な加重値の範囲を判定する。](pmd61a.md#ci) |　　  
