[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section1/eda17.htm)  
閲覧(UTC)：2026-03-03 02:19:19

[1. 探索的データ解析](../eda.md)  
[1.1. EDA入門](eda1.md)

---

# 1.1.7. 一般的な問題の分類

#### 問題の分類区分

以下の表は、EDA問題を分類するための便利な方法である。

#### 単変量と管理

|||
|:---|:---|
|単量変<br><br>データ：<br>&emsp;単一列の数字、Y</br>モデル：</br>&emsp;$y = 定数 + 誤差$<br>出力:<br> &emsp; 1 .数（モデル内の推定定数）<br>&emsp; 2. 定数に対する不確かさの推定値<br>&emsp; 3. 誤差の分布の推定値<br>技法:<br>&emsp;• [4-プロット](../section3/4plot.htm)<br>&emsp;• [確率プロット](../section3/probplot.htm) <br>&emsp;• [PPCC プロット]()|管理<br><br>データ：<br>&emsp;単一列数値、Y<br>モデル:<br>&emsp;$y = 定数 + 誤差$<br>出力:<br>&emsp;「システムは管理外れか？」という質問に対する「はい」または「いいえ」の回答。<br>技法:<br>&emsp;・ [管理図](../../ch6_pmc/section3/pmc3.md) 

#### 比較とスクリーニング

|||
|:---|:---|
|比較<br><br> データ:<br>&emsp;単一の応答変数とk個の独立変数 $(Y,X_1,X_2,...,X_k)$ 、主たる焦点はこれらの独立変数の一つ（主因子）に置かれる。<br>モデル:<br>&emsp;y = f(x_1,x_2,...,x_k) + 誤差<br>出力:<br>&emsp;「主因子は有意か？」という問いに対する「はい」または「いいえ」の判定。<br>技法:<br>&emsp;・[ブロック・プロット](../section3/blockplo.md)<br>&emsp;・[散布図](../section3/scatterp.md)<br>&emsp;・[箱ひげ図](../section3/boxplot.md) |スクリーニング<br><br>データ:<br>&emsp;単一の応答変数と k 個の独立変数$(Y,X_1,X_2,...,X_k)$。<br>モデル:<br>&emsp;$y = f(x_1,x_2,...,x_k) + 誤差$<br>出力:<br>&emsp;1. 因子群の重要度順リスト（最も重要から最も重要でない順）。<br>&emsp;2. 各要因の最適設定値。<br>&emsp;3. Yと因子を関連付ける適切なモデル/予測式。<br>技法:<br>&emsp;・[ブロック・プロット](../section3/blockplo.md)<br>&emsp;・[確率プロット](../section3/probplot.md)<br>&emsp;・[二元ヒストグラム](../section3/bihistog.md)| 

#### 最適化と回帰
|||
|:---|:---|
|最適化<br><br>データ:<br>&emsp;単一の応答変数と k 個の独立変数$(Y,X_1,X_2,...,X_k)$。<br>モデル:<br>&emsp;$y = f(x_1,x_2,...,x_k) + 誤差$<br>出力:<br>&emsp;因子変数に対する最適設定。<br>技法:<br>&emsp;・[ブロック・プロット](../section3/blockplo.md)<br>&emsp;・[最小二乗法近似](../../ch4_pmd/section1/pmd141.md)<br>&emsp;・[等高線図](../section3/contour.md)|回帰<br><br>データ:<br>&emsp;単一の応答変数と k 個の独立変数$(Y,X_1, X_2,...,X_k)$。独立変数は連続変数でもよい。<br>モデル:<br>&emsp;$y = f(x_1,x_2,...,x_k) + 誤差$<br>出力:<br>&emsp;Yと因子を関連付ける適切なモデル/予測式。<br>技法:<br>&emsp;・[最小二乗法近似](../../ch4_pmd/section1/pmd141.md)<br>&emsp;・[散布図](../section3/scatterp.md)<br>&emsp;・[6-プロット](../section3/6plot.md)| 

#### 時系列と多変量

|||
|:---|:---|
|時系列<br><br>データ:<br>&emsp;時間依存の数値列、Y。加えて、時間は独立変数である。時間変数は明示的または暗黙的のいずれかである。データが等間隔でない場合、時間変数は明示的に提供されるべきである。<br>モデル:<br>&emsp;$y = f(t) + 誤差$<br>&emsp;モデルは時間領域ベースまたは周波数領域ベースのいずれかである。<br>出力:<br>&emsp;Y と過去の Y 値を関連付ける適切なモデル／予測式。<br>技法:<br>&emsp;・[自己相関プロット](../section3/autocopl.md)<br>&emsp;・[スペクトル](../section3/spectrum.md)<br>&emsp;・[複素復調振幅プロット](../section3/compdeam.md)<br>&emsp;・[複素復調位相プロット](../section3/compdeph.md)<br>&emsp;・[ARIMAモデル](../../ch6_pmc/section4/pmc4.md)|多変量<br><br>データ:<br>&emsp;k個の因子変数$(X_1,X_2,...,X_k)$。<br>モデル:<br>&emsp;モデルは明示されていない。<br>出力:<br>&emsp;データ内の潜在的な相関構造を特定する。<br>技法:<br>&emsp;・[スタープロット](../section3/starplot.md)<br>&emsp;・[散布図行列](..//section3/scatterb.md)<br>&emsp;・[条件化プロット](..//section3/scatterc.md)<br>&emsp;・プロファイル・プロット<br>&emsp;・[主成分分析](../../ch6_pmc/section5/pmc55.md)<br>&emsp;・層別<br>&emsp;・判別/分類<br><br>なお、多変量解析については本ハンドブックでは軽く触れる。 |