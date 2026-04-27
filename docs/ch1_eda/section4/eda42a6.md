[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section4/eda42a6.htm)  
閲覧(UTC)：2026-04-24 16:55:19  
[⬅️](eda42a5.md)[➡️]()  

1. [探索的データ解析](../eda.md)  
1.4. [EDA事例研究](eda4.md)  
1.4.2. [事例研究](eda42.md)  
1.4.2.10. [セラミックの強度](eda42a.md)  

---

# 1.4.2.10.6. 例題を解いてみる

#### [事例研究の Dataplot マクロを表示](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/jahanmi2.htm)

このページでは、ここまでの事例研究で概説された分析を [Dataplot](../../../dataplot.md) を使用して再現する。
Dataplot を実行するには、あらかじめ Dataplot を[ダウンロードしてインストール](http://www.itl.nist.gov/div898/software/dataplot/ftp/homepage.htm)し、[ブラウザの設定](../../../dpbrows.md)を完了している必要がある。
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
| 1.Dataplot を呼び出してデータを読み込む。 |  |
| [1. データを読み込む。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/data.dp) | [1. 数字の列が1つ読まれたら Dataplot に、変数 Y を入力する。](eda42a1.md) |
| 2. 応答変数をプロットする。 |  |
| [1.Y の数値要約を計算する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/summary.dp) | [1. 要約は平均強度が 650.08、強度の標準偏差は 74.64 を示している。](eda42a2.md#数値要約) |
| [2. Yの4-プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/4plot.dp) | [2. 4-プロットは位置と尺度には偏位がなく、双峰分布を示している。](eda42a2.md#4-プロット) |
| 3.バッチ効果があるかを判断する。 |  |
| [1. 2バッチに基づき、対比ヒストグラムを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/bihistog.dp) | [1. 対比ヒストグラムは、約75単位のバッチ間効果を示している。](eda42a3.md#対比ヒストグラム) |
| [2. q-q プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/qqplot.dp) | [2. q-qプロットは、バッチ1とバッチ2は共通した分布からのものではないことを示している。](eda42a3.md#分位数分位数プロット) |
| [3. 箱ひげ図を作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/boxplot.dp) | [3. 箱ひげ図は、約75 から 100 のバッチ効果を示し、いくつかの外れ値があることを示している。](eda42a3.md#箱ひげ図) |
| [4. ブロック・プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/blockpl1.dp) | [4. ブロック・プロットは、バッチ効果が主因子に対し試験所間と水準で一定であることを示している。](eda42a3.md#ブロック・プロット) |
| [5. 平均値が等しいかの2標本*t*-検定を行う。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/ttest.dp) | [5. t-検定は、それぞれの平均値に関してバッチ効果を検証している。](eda42a3.md#2標本t-検定) |
| [6. 標準偏差が等しいかの F-検定を行う。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/ftest.dp) | [6. Fテストは、各標準偏差に対しい有意なバッチ効果を示していない。](eda42a3.md#F検定) |
| 4. 試験所効果があるかを判断しする。 |  |
| [1. 2バッチを合わせ、試験所の箱ひげ図を作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/boxplotl.dp) | [1. 箱ひげ図は、有意な試験所効果を示していない。](eda42a4.md#箱ひげ図) |
| [2. バッチ1のみの試験所の箱ひげ図を作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/boxpltl1.dp) | [2. 箱ひげ図は、バッチ1 に対して有意な試験所効果を示していない。](eda42a4.md#バッチ1-の箱ひげ図) |
| [3. バッチ2のみの試験所の箱ひげ図を作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/boxpltl2.dp) | [3. 箱ひげ図は、バッチ2 に対して有意な試験所効果を示していない。](eda42a4.md#バッチ2-の箱ひげ図) |
| 5.主因子を分析する。 |  |
| [1. バッチ1のDOE散布図を作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexscat1.dp) | [1. DOE散布図は、打点の範囲と外れ値の存在を示している。](eda42a5.md#バッチ1-のDOE散布図) |
| [2. バッチ1 のDOE平均プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexmean1.dp) | [2. DOE平均プロットは、バッチ1 に対してテーブル速度が最も有意な因子であることを示している。](eda42a5.md#バッチ1-のDOE平均プロット) |
| [3. バッチ1 のDOE SD プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexsd1.dp) | [3. DOE sdプロットは、バッチ1 に対し、テーブル速度が最もばらつきが大きいことを示している。](eda42a5.md#バッチ1-のDOE-SDプロット) |
| [4. バッチ2 のDOE散布図を作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexscat2.dp) | [4. DOE散布図は、打点の範囲と外れ値の存在を示している。](eda42a5.md#バッチ2-のDOE散布図) |
| [5. バッチ2 のDOE平均プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexmean2.dp) | [5. DOE平均プロットは、バッチ2 では供給速度と砥石の粒度が最も有意な因子であることを示している。](eda42a5.md#バッチ2-のDOE平均プロット) |
| [6. バッチ2 のDOE SD プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexsd2.dp) | [6. DOE sdプロットは、バッチ2のばらつきについてすべての３因子は等しいことを示している。](eda42a5.md#バッチ2-のDOE-SDプロット) |
| [7. バッチ1 のDOE交互作用効果行列プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexint1.dp) | [7. DOE交互作用効果行列プロットは、順位付けられた推定効果因子一覧を示す。](eda42a5.md#バッチ1-のDOE交互作用プロット) |
| [8. バッチ2 のDOE交互作用効果行列プロットを作成する。](https://www.itl.nist.gov/div898/handbook/eda/section4/jahanmi2/dpmacros/dexint2.dp) | [8. DOE交互作用効果行列プロットは、順位付けられた推定効果因子一覧を示す。](eda42a5.md#バッチ2-
のDOE交互作用プロット) |

