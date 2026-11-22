[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/glossary.htm)  
閲覧(UTC)：2026-11-18 03:28:00  
[⬆️️](toolaids.md)

---

# 用語集

注：この用語集は、Advanced Micro Devices の Bill Heavlin から寄付いただいた用語集を元に改編されたものである。
現在、ハンドブックで使用されていない用語が含まれていることがある。

---

ハイパーテキスト辞書へようこそ。
これは工学統計から選択された用語を含んでいる。
現在のテーマ領域には、[実験計画](#SDE)、[計測学](#metrology)、[調査](#survey)、アンケート、[統計的工程管理](#SPC)、そして[コンピュータ実験](#computer-expreiment)が含まれている。

---

[A](#A) [B](#B) [C](#C) [D](#D) [E](#E) [F](#F) [G](#G) [H](#H) [I](#I) [J](#J) [K](#K) [L](#L) [M](#M) [N](#N) [O](#O) [P](#P) [Q](#Q) [R](#R) [S](#S) [T](#T) [U](#U) [V](#V) [W](#W) [X](#X) [Y](#Y) [Z](#Z)

---

<div id="A"></div>

## [A]


<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">

<tr>

  <td class="headword" style="width: 15%; vertical-align: top;">

   <span id="accuracy" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">accuracy</span>
   <span id="精確さ" class="term-jp">精確さ</span>
 
  </td>
 
  <td class="definition">

[計測学](#metrology)において、総[測定](#MCA)[変動](#variation)には、[精度](#precision)（[再現性](#reproducibility)）だけでなく、測定値の平均と真値との系統的なオフセットも含まれる。

  </td>
</tr>

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">

   <span id="additive-effect" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">additive effect</span>
   <span id="加法効果" class="term-jp">加法効果</span>

  </td>
  <td class="definition">

特定の入力[因子](#factor)の変更による平均または期待される変化が、他の入力[因子](#factor)の値に依存しない物理[過程](#process)を記述する[モデル](#model)の性質。
加法[効果](#effect)には関連する[交互作用](#interaction)がない。

  </td>
</tr>


<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">

   <span id="affine-calibration" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">affine calibration</span>
   <span id="アフィン校正" class="term-jp">アフィン校正</span>

  </td>
  <td class="definition">

特に[コンピュータ実験](#computer-experiment)においては、予測値と経験的[応答](#response)との一致をシミュレータの入力[要素](#factor)のうち1つまたは複数を線形変換によって変更することにより向上させる方法である。
[全体校正](#global-calibration)と区別される。
  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">
    <span id="AMV" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">analysis of manufacturing variance (AMV)</span>
    
   <span id="製造分散の分析" class="term-jp">製造分散の分析</span>
  </td>
  <td class="definition">

特に[コンピュータ実験](#computer-experiment)の分析において、製造における工程の予測分布を複数の[要因](#factor)それぞれに起因する構成要素、あるいは因子[交互作用](#interaction)の組合せに分解すること。</p>
AMV が各[因子](#factor)について（通常は[ガウス](#Gaussian)分布）を仮定することに依存しているため、[分散分析](#ANOVA)と区別される。
AMV は、通常[コンピュータ実験](#computer-experiment)に適用されるため、分散成分とは区別される。
  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">

<span id="ANOVA" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">analysis of variance</span>
<span id="分散分析" class="term-jp">分散分析<sup> [2]</sup></span>

  </td>
  <td class="definition">

特定[因子](#factor)の[効果](#effect)の有意性に関する計算を提示する方法であり、特に複数の[因子](#factor)の影響が同時に考慮されているデータにおいて重要である。
分散分析は、平均から平方[残差](#residual)の和を各因子、すなわち因子相互作用の組合せに起因する非負成分に分解する。

<p>

通常、固定[効果](#effect)とランダム[効果](#effect)を区別することは有用です。
無作為効果のみの場合、しばしば「[分散成分](#variance-components)」という用語が好まれる。

</p>
  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">

<span id="assignable-cause" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">assignable cause</span>
<span id="突き止められる原因" class="term-jp">突き止められる原因<sup> [1]</sup></span>

  </td>
  <td class="definition">

[特別な原因](#special-cause)の同義語である。</td>
  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">

<span id="attenuation" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">attenuation</span>
<span id="減衰" class="term-jp">減衰<sup>[1]</sup></span>

  </td>
  <td class="definition">

1. [曖昧な概念](#fuzzy-concepts)として、[変動](#variation)の存在に起因する信号の減少。</p>
2. [計測学](#metrology)において、特に[校正](#calibration)標準における[変動](#variation)や測定[不確かさ](#uncertainty)の影響により、信号の[感度](#sensitivity)の[偏り](#bias)をゼロにする傾向がある。
  
  </td>
</tr>  

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="audit" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">audit</span>
<span id="監査" class="term-jp">監査</span>
</td>
<td class="definition">
文書化された要求事項への適合性を検証するために実施される活動の定期的な観察。</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="AOQ" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">average outgoing quality  (AOQ)</span>
<span id="平均出検品質" class="term-jp">平均出検品質</span>
</td>
<td class="definition">

[検査](#inspection)および是正による利益を考慮した結果、[顧客](#customers)に納品される不良品の平均水準。
通常、ppmで報告される。
[ハーン推定量](#Hahn-Estimate)も参照のこと。

</td></tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="B"></div>

## [B]  

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">

<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="bar-chart" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">bar chart</span>
<span id="棒グラフ" class="term-jp">棒グラフ</span>

</td>
<td class="definition">

ゼロから各値まで棒を引き、複数の値を報告するグラフ。
各棒には適切にラベルが付けられている。
優れたグラフィック・デザインの批評家は、縦棒グラフと横棒グラフをさらに区別する。
縦棒グラフは、時に「列図（column charts）」とも呼ばれ、*y*軸に対して値を、*x*軸に沿ってラベルを描画しているグラフで、データを時間順に報告する場合に推奨される。
水平棒グラフは、*x*軸に沿って値を、*y*軸に沿ってラベルをプロットする。
時系列ではないデータの報告に推奨される。
水平棒グラフでは、ラベルは自然に横向きに配置され、縦棒グラフよりも読みやすくなることにご留意する。
最後に、推奨される実践として、軸を意味のある順序に配置することが推奨される。
ラベル内の自然配列を使用するか、プロットされた値を順位付けするかのいずれかである。
[パレート図](#Pareto)も参照。

</td>

</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="bias" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">bias</span>
<span id="偏り" class="term-jp">偏り<br>バイアス</span>

</td>
<td class="definition">

[分布](#distribution)の平均値（期待値）と真の値との差。
[計量学](#metrology)において、[精度](#precision)と[精確さ](#accuracy)の違いは、[精度](#precision)の測定は偏りの影響を受けないのに対し、[精度](#accuracy)の測定は偏りが大きくなると低下する点である。
</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="binomial-distribution" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[binomial distribution](docs/ch1_eda/section3/eda366i.md)

</span>
<span id="二項分布" class="term-jp">

[二項分布](docs/ch1_eda/section3/eda366i.md)

</span>
</td>
<td class="definition">

離散事象、特に不良事象の数を[モデル](#model)するために用いられる重要な理論[分布](#distribution)。
二項分布は *n* と *p* の二つの母数に依存する。
*n* は試行の総回数であり、各試行において、対象事象を観測できる確率は *p*、観測しない確率は 1‐*p* である。
二項分布は、各試行の結果が他の試行と独立していると仮定し、観測された事象の総和を[モデル](#model)にしている。
[Poisson(ポアソン)分布](#Poisson-distribution) とは異なり、二項分布は観測可能な[標本規模](#samplesize)である事象（イベント）の最大数 *n* を設定する。
[超幾何](#hypergeometric-distribution)分布とは異なり、二項分布は計数事象が独立であると仮定する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="blocking" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">blocking</span>
<span id="ブロック化" class="term-jp">ブロック化</span>

</td>
<td class="definition">

[実験](#SDE)を規模、時間、または空間が制限された副群に分割すること。
優れた[実験計画](#SDE)の実践では、すべての[因子](#factor)がブロック内で変化し、ブロック内の単位割当てが[無作為化](#randomization)され、ブロックの順序と割当てが[無作為化](#randomization)される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Box-Benkhen" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Box-Benkhen experiment</span>
<span id="ボックス・ベンヘン実験" class="term-jp">ボックス・ベンヘン実験</span>

</td>
<td class="definition">

各[因子](#factor)に対して3つの[水準](#factor-level)を持つ[実験計画](#SDE)で、[交互作用](#interaction)を含む完全な 2次[モデル](#model)の推定を可能にする。
Box-Benkhen 計画は 2つの部分から構成されている。</p>

1. [中心点](#centerpoint)、そして
2. [中心点](#centerpoint)から等距離にある球面上の点

<p>

後者の点は、小さな[2水準完全実施要因](#two-level-designs)で構成され、いくつかの因子は中心値に固定されている。
[回転可能性](#rotatable)を確立するために、[中心点](#centerpoint)数が選択される。
[中心複合設計](#CCD)と比較のこと。
</p></td>

</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="box-plot" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[box plot](docs/ch1_eda/section3/eda337.md)

</span>
<span id="箱ひげ図" class="term-jp">

[箱ひげ図](docs/ch1_eda/section3/eda337.md)

</span>
</td>
<td class="definition">

各群が多数の観測値を有する複数群の比較を容易にするための、分布の単変量グラフ表示。
各群は箱で表される。
箱の端は25百分位数（パーセンタイル）と75百分位数を示し、中央線は中央値を示す。
さらに、箱の端から外側へ、（a）分布の最大値と最小値、または（b）[外れ値](#outliers)と看做されない最大値と最小値のいずれかに2本の線が描かれる。
後者の慣例では、[外れ値](#outliers)と看做される個々の値は特定の点としてプロットされる。
一部のソフトウェアは平均値もプロットする。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="brushing" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">brushing</span>
<span id="ブラッシング" class="term-jp">ブラッシング</span>

</td>
<td class="definition">

観測の小群に焦点を当てる手法で、特に[散布図行列](#scatter-plot-matrix)において、時には[ヒストグラム](#histogram)やその他のグラフ表示でも行われる。
[散布図行列](#scatter-plot-matrix)において、ブラッシングは多変量データの可視化に役立つ。
典型的なコンピュータ実装では、利用者がリアルタイムで小群を再定義できるようになります。

</td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)
</td></tr>


</tbody></table>

---

<div id="C"></div>

## [C]

<table width="540" cellspacing="20">

<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="calibration" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">calibration</span>
<span id="校正" class="term-jp">較正</span>

</td>
<td class="definition">

[計量学](#metrology)において、実際の測定値を既知の値と比較する[過程](#process)または方法、そして両者の一致を改善するために適切な調整を行う方法。</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="constraint" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">constraint</span>

<span id="制約" class="term-jp">制約</span>

</td>
<td class="definition">

[実験](#SDE)であれ生産[工程](#process)であれ、物理的に実行不可能であるか、極めて望ましくない[要因範囲](#factor-range)または[要因](#factor)の組合せにおける制限。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="capability" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">capability</span>
<span id="能力" class="term-jp">能力</span>

</td>
<td class="definition">

[共通原因](#common-cause)による[過程](#process)の自然な[変動](#variation)

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Cpk" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">capability index, Cpk</span>

<span id="能力指数、Cpk" class="term-jp">能力指数、Cpk</span>

</td>
<td class="definition">

[安定](#stability)[過程](#process)の自然[変動](#variation)を仕様限界の近接度と比較した指標。
[工程](#process)が[安定](#stability)かつ正規分布の場合、Cpkから製品の仕様外の割合を推定することが可能である。
<p>LSL を下限仕様上限とし、USL を上限仕様上限とする。
AVG を[分布](#distribution)の平均またはそれに類似した典型値とし、SIGMA を総[共通原因](#common-cause)[変動](#variation)の推定値とする。
すると、Cpk は [ AVG - LSL ]/3 \* SIGMA と [ USL - AVG ]/3 \* SIGMA のうち小さい方として定義される。</p>
<p>場合によっては、下位の仕様のみ、または上位の仕様のみが適切である。
下限については、Cpl（[ AVG - LSL ]/3 \* SIGMA と定義される）という片側能力指数を代わりに使用できる。
上限については、[ USL - AVG ]/3 \* SIGMA と定義された Cpu を使用できる。
それらの類似性により、Cpkは、片面および両面の仕様の両方を含む一般的な用語として時折使用される。</p>

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Cpk25" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">capability index, Cpk with 25 percent precision and 95 percent confidence</span>
<span id="能力指数、25%の精度と95%の信頼性を持つCpk" class="term-jp">能力指数、25%の精度と95%の信頼性を持つCpk</span>

</td>
<td class="definition">

[工程](#process)が少なくとも33回の異なる反復で繰り返される場合、[USL-LSL]/6 \* SIGMA と定義される Cp は、推定 Cp 値の約 ± 25% の 95% 信頼区間を持つ。
この同じ原理は、Cpk の信頼区間について概ね成り立つ。
<p>AMD技術報告書320に詳細が記載されている。</p>
<p>代替手法は、特定の条件下で[標本規模](#samplesize)を小さくし、同等の[精度](#precision)を実現するために利用可能である。
AMDの技術報告書326を参照のこと。</p>

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="capability-study" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">capability study</span>
<span id="能力調査" class="term-jp">能力調査</span>

</td>
<td class="definition">

[工程](#process)の[共通原因](#common-cause)変動に関するあらゆる研究。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="capable-process" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">capable process</span>
<span id="工程能力のある工程" class="term-jp">工程能力のある工程</span>

</td>
<td class="definition">

1. 仕様範囲に十分な許容範囲があり、原則として管理外れ状況を検知し、生産材料を危険にさらすことなく是正措置を講じることができる工程。</p>
2. 能力指数[Cpk](#Cpk)が1.0を超える[工程](#process)（[Cpk](#Cpk)の他の基準は時々推奨される）。
これらには1.33、1.5、2.0が含まれるが、後者の値は通常「生産可能」という標示に割り当てられる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="CEdiagram" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">cause-effect diagram</span>
<span id="特性要因図" class="term-jp">特性要因図</span>

</td>
<td class="definition">

CE図、石川図、魚骨図とも呼ばれる。
石川薫が最初に提示した、特定の関心の質に関する様々な要因と[変動](#variation)源を記述した図。
関心の質は通常、水平矢印の先端の右側に配置される。
主な原因区分は、この主矢から分岐し、広げた魚の骨を思わせる様式で展開する。
他の符号化慣例では、原因の影響が定量化された場合は原因表示の周囲に枠を描画し、その原因が重要と考えられるが、まだ[効果](#effect)が定量化されていない場合は標示に下線を付ける。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="census" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">census</span>
<span id="全数調査" class="term-jp">全数調査</span>
</td>
<td class="definition">

[抽出枠](#sample-frame)内のすべての単位、すなわち[母集団](#population)を評価するデータ収集手法。
[標本](#sample)の対義語。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="centerpoint" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">centerpoint</span>
<span id="中心点" class="term-jp">中心点</span>

</td>
<td class="definition">

定量的[因子](#factor)を用いた[実験](#SDE)において、すべての[因子](#factor)に対応する実験条件は、それらの高値と低値の中間点に設定される。
中心点は曲率の有無を検定し、二次[効果](#effect)に関する情報を提供する。
繰り返した場合、中心点は実験誤差の大きさの推定値も提供する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="CCD" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">CCD</span>
<span id="中心複合設計" class="term-jp">中心複合設計</span>

</td>
<td class="definition">

Box-Wilson または 星型複合計画としても知られています。3部構成の[実験計画](#SDE)：</p>

1. [2水準完全または一部実施要因計画](#twol-evel-designs);</p>
2. 「星型」または各[因子](#factor)が高低[水準](#factor-level)に変動し、他のすべての因子が一定に保たれる軸点；</p>
3. [中心点](#centerpoint)。</p>

星点の配置は変動を与える。
[2水準計画](#two-level-designs)部分を -1 と +1 で符号化すると、元の Box‐Wilson 提案では星点を 1 より大きい特定の値で変化させる。
[回転性](#rotatable)を確保するために、正確な値が選択される。
別の代替案として、星点を ±1 に制限することが考えられる。
<p>中心複合計画は、反復実験や[ブロック化](#blocking)に対応できる点で、さらに魅力がある。
[Box-Benkhen 計画](#Box-Benkhen-design)と比較のこと。</p>

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="characteristic" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">characteristic</span>
<span id="特徴" class="term-jp">特徴</span>

</td>
<td class="definition">

変数や属性のデータを収集できる、[工程](#process)やその出力の特徴的な要素。
工程の[応答](#response)。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="characterization" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">characterization</span>
<span id="特徴付け" class="term-jp">特徴付け</span>

</td>
<td class="definition">

[工程](#process)またはその測定可能な出力の記述で、性能の予測に役立つ。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="checklist" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">checklist</span>
<span id="チェックリスト" class="term-jp">チェックリスト</span>

</td>
<td class="definition">

測定尺度が区分けされた行に分割される、データ記録またはデータ分析の方法。
特定の区間に値が収まることを観測した場合、垂直線を記録する。
各5番目の垂直線は、前の4つに横方向に描かれます。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Clifford" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Clifford's method</span>
<span id="クリフォードの方法" class="term-jp">クリフォードの方法</span>

</td>
<td class="definition">

[個別管理図](#individuals-chart)に対する[管理限界](#control-limits)の[頑健](#robust)な計算。
中心線は中央値で計算され、上限（下限）の[管理限界](#control-limits)は中心線の ±3.15倍の中央値移動範囲にある。
Clifford は、手計算を削減するためにこの手法を最初に提案した。
また、自動制御限界再計算にも優れた特性を有する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="close-ended-question" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">close-ended question</span>
<span id="制限回答式質問" class="term-jp">制限回答式質問</span>

</td>
<td class="definition">

[調査](#survey)において、質問形式を提示し、回答を「はい・いいえ」や1から10までの尺度で構成しようとする質問形式。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="common-cause" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">common cause</span>
<span id="共通原因" class="term-jp">共通原因</span>

</td>
<td class="definition">

研究対象の[工程](#process)出力のすべての個別値に影響を与える自然な[変動](#variation)の源。
一般的に、一般的な原因は多数あり、個々の要因は総[変動](#variation)にほとんど寄与しないが（総[変動](#variation)は依然として大きいこともある）、排除が困難である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="computer-experiment" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">computer experiment</span>
<span id="コンピュータ実験" class="term-jp">コンピュータ実験</span>

</td>
<td class="definition">

1つ以上のコンピュータ・シミュレータを用いて、基本的な物理[過程](#process)を研究する。
経験的実験と同様に、入力変数（[因子](#factor)）はシミュレータの出力（[応答](#response)）への影響を評価するために体系的に変更される。
実証的実験とは異なり、シミュレータの[応答](#response)は[決定論的](#deterministic)であり、影響がある。
コンピュータ実験は適切に中間水準の因子を持つことができ、特に実行回数の範囲はより野心的になることがある。
さらに、[補間器](#interpolator)（特に[クリギング](#kriging")）に基づく[モデル化](#model)手法は、実行可能な手法として挙げられる。
適切な実践として、コンピュータ実験に[ラテン超方格](#LHC)を使用し、データ解析段階では[クリギング](#kriging)、[ニューラルネットワーク](#neural-network)、多変量適応回帰スプライン（MARS）などの高度なノンパラメトリック[モデル](#model)化手法を用いることが推奨される。
コンピュータ実験手法の重要な応用は、[工程](#process)最適性を決定することと、[工程](#process)許容差を評価することである。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="confidence-interval" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[confidence interval](docs/ch1_eda/section3/eda352.md)

</span>
<span id="信頼区間" class="term-jp">

[信頼区間](eda/section3/eda352.md)

</span>

</td>
<td class="definition">

1. 未知のパラメータが、ある確率で二つの値の間にあるというすべての陳述。
例えば、theta の 95%信頼区間が 1.1 から 10.3 であると言う場合、これは Pr{ 1.1 &lt;= theta &lt;=3D 10.3 }=3D0.95 という確率命題に対応する。</p>
2. 特定のデータ集合の観測に基づき、未知係数の妥当な値の範囲で、そのデータの観測と一致する。
例えば、theta の 95%信頼区間が 1.1 から 10.3 であると言う場合、これは観測されたデータに基づき、Theta が 1.1 から 10.3 の間である確率が 95% であると言うことと同等である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="confidentiality" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">confidentiality</span>
<span id="機密性" class="term-jp">機密性</span>

</td>
<td class="definition">

調査において、回答者の身元が公衆や他の回答者、特に[調査](#survey)計画者、面接官、管理者に対してどの程度知られていないか。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="control" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">control</span>

<span id="制御" class="term-jp">制御</span>

</td>
<td class="definition">

フィードバックに基づく是正措置。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="control-chart" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">control chart</span>
<span id="管理図" class="term-jp">管理図</span>

</td>
<td class="definition">

工程特性の図表現。
[統計](#statistic)または個別測定のプロットされた値を示す時系列チャートで、中心線と1つ以上の統計的に導出された[管理限界](#control-limits)を含む。</p>
管理図の典型的な例としては、X--R管理図、バッチ平均（「個別」）管理図、ウェハ内[範囲](#range)および[標準偏差](#sigma)管理図、ウェハ間および標準偏差管理図、累積和管理図、指数加重移動平均管理図、平均分析管理図、累積計数管理図が挙げられる。</p>

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="control-factor" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">control factor</span>
<span id="制御因子" class="term-jp">制御因子</span>

</td>
<td class="definition">

特に[実験](#SDE)においては、制御しやすい[因子](#factor)や工程入力は、[応答](#response)の典型的な値に強い[影響](#effect)を与え、その変動の大きさには小さな[効果](#effect)しない。
通常、[誤差因子](#noise-factor)とは区別される。

</td></tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="control-group" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">control group</span>
<span id="対照群" class="term-jp">対照群</span>

</td>
<td class="definition">

[実験](#SDE)または[前向き](#prospective)研究における観測の集合で、[実験](#SDE)の処理を受けないもの。
これらの観測は、（a）各実験処理の規模と重要性を評価する比較点として、（b）現在の観測と過去の観測履歴を比較するための現実確認として、（c）自然実験誤差を確立するためのデータ源として機能する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="control-limits" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">control limits</span>
<span id="管理限界" class="term-jp">管理限界</span>

</td>
<td class="definition">

[共通原因](#common-cause)のみによる[工程](#process)特性の許容可能な最大[変動](#variation)管理限界を超える変動は、[異常原因](#special-cause)が[工程](#process)に影響を与えている可能性があることの証拠である。
管理限界は[工程](#process)データから計算される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="convenience-sample" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">convenience sample</span>
<span id="便宜標本" class="term-jp">便宜標本</span>

</td>
<td class="definition">

[調査](#survey)において、調査員または面接官の都合に合わせて観察単位を選定すること。
科学的[無作為化](#randomization)と区別される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="correlation" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">correlation</span>
<span id="相関" class="term-jp">相関</span>

</td>
<td class="definition">

相関は、二つの変数間の（通常は線形的な）関係の強さを測る指標。
通常の相関係数（ピアソン相関係数と呼ばれる）は、-1から1の範囲である。
+1 の値は、二つの変数が増加関係によって完全に関連している場合に対応し、-1 の値は完全であるが減少する関係に対応する。
ピアソン相関係数の場合、+1（-1）という値は、その関係が<span class="underline">線形</span>であり、増加（減少）していることを意味する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="coverage-error" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">coverage error</span>
<span id="網羅誤差" class="term-jp">網羅誤差</span>

</td>
<td class="definition">

調査において、回答候補者群（[標本枠](#sample-frame)）が一般化したい[対象](#population)と一致しない場合に生じる誤差。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="critical-parameters" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">critical parameters</span>
<span id="重要係数" class="term-jp">重要係数</span>

</td>
<td class="definition">

重要係数とは、材料、[工程](#process)、装置、[測定](#MCA)機器、施設、または製品の測定可能な特性であり、製品、[工程](#process)、またはサービスの使用適合性に直接的または間接的に関連する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="critical-process-module" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">critical process module</span>
<span id="重要工程モジュール" class="term-jp">重要工程モジュール</span>

</td>
<td class="definition">

[工程](#process)フローにおけるノードで、その出力が全体[工程](#process)に重大な影響を与える。
時には、重要工程ステップとも呼ばれることがある。</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="cross-validation" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">cross-validation</span>
<span id="交差検証" class="term-jp">交差検証</span>

</td>
<td class="definition">

予測誤差の最も[偏りのない](#bias)検証は、初期予測[モデル](#model)の構築に使用されなかったデータに適用することであるという考えに基づく手法群。
一般的な応用例は、データ集合を二つの部分に分割し、1つ目に[モデル](#model)を適合させ、他方にその[モデル](#model)予測能力を評価することが挙げられる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="cusum" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">cusum chart</span>
<span id="累積和管理図" class="term-jp">累積和管理図</span>

</td>
<td class="definition">

累積和に基づく[管理図](#control-chart)で、時には「cumsum」チャートとも呼ばれる。
時刻 <i>t</i> に測定された値が <i>X</i>(<i>t</i>) の場合、累積和管理図では値 SUM{ <i>X</i>(<i>u</i>)</i>-target:<i>u</i>=1,2,...,<i>t </i>} をプロットする。
累積和管理図は偏位に敏感であり、目標の上または下で系統的に実行される過程にも敏感である。
これらは調整可能な過程に最も適しており、実際に大量に実行されている処方が1つだけの場合などである。
これらの特性により、[EWMA管理図](#EWMA)に似ている。
<p>累積和 [管理限界](#control-limits)は、後方向きの V マスクの形を取る。
すべてのプロットされた点がこの Vマスク内にあるとき、工程は[管理下](#in-control)にある。</p>

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="customers" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">customers</span>
<span id="顧客" class="term-jp">顧客</span>
</td>
<td class="definition">

事業の製品、情報、またはサービスを利用する組織。<p>

</td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td>
</tr>

</tbody></table>

---

<div id="D"></div>

## [D]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">

<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="data-driven" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[data-driven](docs/ch1_eda/section1/eda12.md)

</span>
<span id="データ駆動型" class="term-jp">

[データ駆動型](docs/ch1_eda/section1/eda12.md)

</span>
</td>

<td class="definition">

データや事実を要求する性質だが、主観的な意見は要求しない。
[意見駆動型](#opinion-driven)の対義語。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="data-reduction" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">data reduction</span>
<span id="データ削減" class="term-jp">データ削減</span>

</td>
<td class="definition">

複数の数から1つ以下の数を計算する過程。
例として、ウェハ上で9つの読取りを行う場合がある。
一般的なデータ削減として、平均と[標準偏差](#sigma)（2つのみの数）を使用する。
データ削減の利点は、通常、単純さ、解釈の容易さ、関心のある課題へのより大きな焦点、そして小さなデータ・ファイルである。

</td>
</tr>



<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="demographics" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">demographics</span>
<span id="人口統計" class="term-jp">人口統計</span>

</td>
<td class="definition">

調査では、年齢、性別、居住地、年収などの情報を特に回答者を特定のグループの一員として特定することで、回答を明らかにするために使用する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="detection" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">detection</span>
<span id="検出" class="term-jp">検出

</span>
</td>
<td class="definition">

製造品が仕様に適合しているかを判定するために設計された工程是正監視の区分。
[処分](#disposition)もご参照のこと。
[予防](#prevention)の対義語。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="deterministic" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">deterministic</span>
<span id="決定論的" class="term-jp">決定論的</span>

</td>
<td class="definition">

完全に再現可能で、実験的または観測的誤差がない性質。
通常、[コンピュータ実験](#computer-experiment)でのみ実現可能。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="diagnostic" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[diagnostic](docs/ch1_eda/section2/eda23.md)

</span>
<span id="診断" class="term-jp">

[診断](docs/ch1_eda/section2/eda23.md)

</span>

</td>
<td class="definition">

[モデル](#model)に関する1つ以上の前提を検証するための計算またはグラフ。
</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="digidot-chart" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">digidot chart</span>
<span id="幹葉図付き時系列プロット" class="term-jp">幹葉図付き時系列プロット</span>

</td>
<td class="definition">

葉が左側を向き、右側が時間傾向プロットとなっている、Y軸に茎と葉のチャートからなる複合チャート。
どちらの場合も、プロットされた値は観測値の最下位桁である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="disposition" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">disposition</span>
<span id="処分" class="term-jp">処分</span>

</td>
<td class="definition">

仕様外で製造された生産品に対して何をすべきかを評価する製品決定の区分。
[検出](#detection)も参照のこと。
[予防](#prevention)の対義語。

</td>
</tr>



<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="distribution" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[distribution](docs/ch1_eda/section3/eda366.md) 

</span>
<span id="分布" class="term-jp">

[分布](docs/ch1_eda/section3/eda366.md)

</span>

</td>
<td class="definition">

変数、特に[応答](#response)値の出現頻度を表す表現。

</td>
</tr>



<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="dot-plot" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">dot plot</span>
<span id="点図" class="term-jp">点図</span>

</td>
<td class="definition">

特定の範囲内の値を持つ観測を同じ範囲内の前の点より固定間隔の点としてプロットする[ヒストグラム](#histogram)の形態。
観測回数が少ない場合に有用である。<p>

</td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td>
</tr>

</tbody></table>

---

<div id="E"></div>

## [E]  

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="effect" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">effect</span>
<span id="効果" class="term-jp">効果/影響</span>

</td>
<td class="definition">

与えられた[応答](#response)の平均値または期待値が、特定の[因子](#factor)の変化によって変化すること。
与えられた[因子](#factor)の変化は、通常、実験的に試された値の最小値から最大値へと変化し、効果の単位は通常、[応答](#response)と同じ単位である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="efficiency" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">efficiency</span>
<span id="効率" class="term-jp">効率</span>

</td>
<td class="definition">

与えられた推定手法と[標本規模](#sample-size)によって実現できる[精度](#precision)に関する[曖昧な概念](#fuzzy-concepts)。
効率的な手法は、最も短い[信頼区間](#confidence-interval)で[母集団](#population)を推定する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="EVOP" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">EVOP, Evolutionary Operation</span>
<span id="EVOP、進化的操作" class="term-jp">EVOP、進化的操作</span>

</td>
<td class="definition">

「進化的操作」の略称。
EVOPは、いくつかの特徴的な機能を備えた特別な種類の稼働中[実験](#SDE)である。</p>

1. 実験品は、[顧客](#customers)に納品されることを目的とした生産品である。
2. 各[実験](#SDE)サイクルにおいて、標準の生産処方が変更される。
3. 実験因子水準は、従来の稼働中[実験](#SDE)に比べて極端ではない。
4. この[実験](#SDE)は、従来の稼働中[実験](#SDE)よりも多くの材料を用い、長期的に実施される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="EWMA" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">EWMA chart</span>
<span id="EWMA管理図" class="term-jp">EWMA管理図</span>

</td>
<td class="definition">

1. 指数加重移動平均に基づく任意の[管理図](#control-chart)。
EWMA管理図は、現在の観測値と以前にプロットされた点の加重平均をプロットし、現在の観測値の重みは<i>λ</i>で表される。
<i>λ</i>の値は一般的に0.3から0.7が推奨される；0.7の値は「ばらつきが多い」工程に適している。
<i>λ</i> = 0.4は、すべての8[Western Electric 規則](#Western-Electric-rules)が有効な状態で約1の<i>λ</i>と等しい挙動を示す。
<p>EWMA管理図は偏位に敏感であり、系統的に中心値がズレている時に実行される工程にも敏感である。
対象が多数実行されている工程が1つだけである場合に最も有用である。
これらの機能は[累積和管理図](#cusum-chart)と共通である。</p>
2. AMDでは、EWMA管理図でも最適な<i>λ</i>値の計算が可能である。
AMDの実装は、現在の監視点の平均をプロットし、この平均を指定された[管理限界](#control-limits)と比較する。
この点に関しては、[個別管理図](#individuals-chart)に似ている。
EWMA 部は、[Western Electric 規則](#Western-Electric-rules)の代わりに使用される傾向パターンの組として実装されている。</p>
3. J Stuart Hunter が最初に提案したように、EWMA 管理図は、以前にプロットされた点とともに現在の観測値の指数加重平均をプロットする。
これらは適切な[管理限界](#control-limits)と比較される。
さらに、現在の観測値もプロットされ、適切な（例：[個別管理図](#individuals-chart)）[管理限界](#control-limits)と比較される。

</tr>

<tr><td></td><td>

[ページの先頭へ戻る](glossary.htm)

</td>
</tr></tbody></table>

---

<div id="F"></div>

## [F]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">

<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="facetoface" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">facetoface</span>
<span id="対面調査" class="term-jp">対面調査</span>

</td>
<td class="definition">

回答者が実際に現場にいる者によってインタビューされる[調査](#survey)の実施方法。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="factor" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">factor</span>
<span id="要因" class="term-jp">要因/因子</span>

</td>
<td class="definition">

[工程](#process)、特に[実験](#SDE)の入力変数。
実験因子とは、特に[実験](#SDE)中に意図的に操作される変数のこと。
実験因子はさらに[制御因子](#control-factor)と[誤差因子](#noise-factor)に分類できる。
制御因子とは、制御しやすく、通常、[応答](#response)に強い影響を与える要因のこと。
（典型的な例として、証言録取[手続き](#process)に要する時間がある。）
誤差因子は、制御が困難であるか、しづらい因子のこと。
制御が難しい[誤差因子](#noise-factor)は、炉管周囲の空気流が相当する。
制御しにくい[誤差因子](#noise-factor)として、最近の濡れた清潔なシンクの使用履歴が挙げられる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="factor-level" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">factor level</span>
<span id="因子水準" class="term-jp">因子水準</span>

</td>
<td class="definition">

実験計画において、入力変数または[因子](#factor)が取り得る値。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="factor-range" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">factor range</span>
<span id="因子範囲" class="term-jp">因子範囲</span>

</td>
<td class="definition">

実験計画の、特に定量的[因子](#factor)においては、[因子](#factor)が取る最高値と最低値との差。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="factorial-experiment" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">factorial experiment</span>
<span id="要因実験" class="term-jp">要因実験</span>

</td>
<td class="definition">

各[因子](#factor)の値を他のすべての因子の値と組み合わせて使用する[実験](#SDE)。
一部実施要因実験は、組合せすべての適切な部分集合を以下の目的を念頭に置いて実施する。</p>
1. 実験の総が少ない。
2. 実験空間が十分に網羅されている。
3. 因子の部分集合（例えば規模が2、3、もしくは 4）については、実験組合総数を大きくしておく。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="focus-groups" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">focus groups</span>
<span id="フォーカス・グループ" class="term-jp">フォーカス・グループ</span>

</td>
<td class="definition">

個別にではなく、少人数のグループで人々にインタビューする方法。
この方法は、正式なアンケート[調査](#survey)の前段階としてしばしば好まれる。
グループは通常、何らかの形で比較できるよう構成されている（収入、年齢など）。
欠点には、費やした労力に対し[標本規模](#sample-size)が小さいこと、他の回答者の見解を聞くことによる潜在的な[偏り](#bias)、そして結果を統合する構造が欠如していることが挙げられる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="fuzzy-concepts" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">fuzzy concepts</span>
<span id="曖昧な概念" class="term-jp">曖昧な概念</span>

</td>
<td class="definition">

抽象度が高いことにより、一般化と代替手法の両方を認める概念。
例えば、平均は通常、数値集合の典型的な値を推定するために計算される。
平均は特定の概念であり、一方「典型値」は曖昧な概念である。

</td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td>
</tr></tbody></table>


---

<div id="G"></div>

## [G]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody>
<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="gauge-study" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">gauge study</span>
<span id="ゲージ研究" class="term-jp">ゲージ研究</span>

</td>
<td class="definition">

[計測学](#metrology)の研究の同義語。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Gaussiandistribution" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[Gaussian distribution](docs/ch1_eda/section3/eda3661.md)

</span>
<span id="ガウス分布" class="term-jp">

[ガウス分布](docs/ch1_eda/section3/eda3661.md)

</span>

</td>
<td class="definition">

[正規](#normal)分布を参照のこと。

</td>
</tr>



<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="global-calibration" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">global calibration</span>
<span id="全体校正" class="term-jp">全体校正</span>

</td>
<td class="definition">

[コンピュータ実験](#computer-experiment)において、シミュレーション結果と経験値の読取りの間で良好な一致を達成するために、生のシミュレーション[応答](#response)を変換する関数を開発する作業。
[アフィン校正](#affine-calibration)と区別される。
[校正](#calibration)を参照のこと。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="goodness-of-fit" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[goodness of fit](docs/ch1_eda/section3/eda35f.md)

</span>
<span id="適合性" class="term-jp">

[適合性](docs/ch1_eda/section3/eda35f.md)

</span>

</td>
<td class="definition">

1. [曖昧な概念](#fuzzy-concepts)として、[適合の欠如](#lack-of-fit)の対義。
2. 観測された[分布](#distribution)の頻度を確率[モデル](#model)がどれほど近く再現するかを示すすべての指標。
3. [R二乗](#R-squared)などの指標で、統計[モデル](#model)が観測値をどれだけ正確に予測するかを示す指標。

</tr>  

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="H"></div>

## [H]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Hahn-Estimator" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Hahn Estimator</span>
<span id="ハーン推定量" class="term-jp">ハーン推定量</span>

</td>
<td class="definition">

[二項分布](#binomial-distribution)に基づく[平均出検品質](#AOQ)のノンパラメトリック推定と、[二項分布](#binomial-distribution)の母数 <i>p </i>に対する観測されていない[分布](#distribution)の仮定。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="histogram" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[histogram](docs/ch1_eda/section3/eda33e.md)

</span>
<span id="ヒストグラム" class="term-jp">

[ヒストグラム](docs/ch1_eda/section3/eda33e.md)

</span>

</td>
<td class="definition">

統計[分布](#distribution)のグラフ表示；棒グラフの形態。
1軸（通常は x）は観測された値の尺度であり、2軸（通常はy）はその値とともに観測が行われる頻度である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="hypergeometric-distribution" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">hypergeometric distribution</span>
<span id="超幾何分布" class="term-jp">超幾何分布</span>

</td>
<td class="definition">

離散事象を[モデル](#model)化するために使用される重要な[分布](#distribution)であり、特に置換なしで標本抽出する時の不良品数は特に重要である。
超幾何分布は、<i>N</i>、<i>n</i>、<i>D </i>の3つの母数に依存する。
<i>N </i>は既知の有限[母集団](#population)規模、<i>n </i>は既知の[標本規模](#sample-size)（<i>N </i>以下に制限された）、<i>D </i>は不明な欠陥数である。
[二項分布](#binomial-distribution)とは異なり、超幾何分布は標本化が置換されないと仮定し、その母数はすべて整数値であるとする。

</td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="I"></div>

## [I]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="imputation" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">imputation</span>
<span id="代入" class="term-jp">代入</span>

</td>
<td class="definition">

未知で測定されていない、または欠損データを特定の値に置き換えること。
代入の最も簡単な形態は、欠損しているすべての値をその変数の平均に置き換えることである。
より高度な代入手法は、観測された変数間の[相関](#correlation)構造を使用する。
代入は人間集団の[調査](#survey)で最も一般的である。
特定の[コンピュータ実験](#computer-experiment)の用途でも使用される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="in-control" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">in control</span>
<span id="管理下" class="term-jp">管理下</span>

</td>
<td class="definition">

[管理外れ](#out-of-control)になることの反対

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="individuals-chart" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">individuals chart</span>
<span id="個別管理図" class="term-jp">個別管理図</span>
</td>
<td class="definition">

1. [合理的群](#rational-subgroup)の規模が1である変数データの[管理図](#control-chart)。
[X管理図](#X-chart)の同義語。</p>
2. [合理的群](#rational-subgroup)の複数測定値を単一の数値（通常は平均）に縮小し、さらに[合理的群](#rational-subgroup)の規模が1であるかのように極限を算出する変数データ[管理図](#control-chart)のアルゴリズムである。
3. [Clifford の手法](#Clifford)も参照のこと。
   
   </td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="inspection" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">inspection</span>
<span id="検査" class="term-jp">検査</span>

</td>
<td class="definition">

特性の[測定](#MCA)と標準との比較。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="interaction" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">interaction</span>
<span id="交互作用" class="term-jp">交互作用</span>

</td>
<td class="definition">

物理的[過程](#process)（そのような[過程](#process)を記述する[モデル](#model)）の性質において、特定の入力[因子](#factor)を変更することによる[応答](#response)の平均（または予測平均）の変化が、他の入力因子の値に依存すること。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="interpolator" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">interpolator</span>
<span id="補間器" class="term-jp">補間器</span>

</td>
<td class="definition">

[モデル](#model)構築に使用される観測を常に完全に再現する予測アルゴリズム。
[コンピュータ実験](#computer-experiment)に有用である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="interview-survey" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">interview survey</span>
<span id="面接調査" class="term-jp">面接調査</span>

</td>
<td class="definition">

回答者に口頭でインタビューを行い、回答を回答者が記録する[調査](#survey)の実施方法。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="interviewererror" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">interviewererror</span>
<span id="調査員誤差" class="term-jp">面接官のエラー</span>

</td>
<td class="definition">

調査において、回答者がインタビュアーの行動、非言語的手がかり、または口頭の発言に応じて回答を修正することによって生じる[測定誤差](#measurement-error)の構成要素。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="item-stem-and-leaf-plot" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">item stem and leaf plot</span>
<span id="幹葉図" class="term-jp">幹葉図</span>

</td>
<td class="definition">

アンケートでは、共通の[リッカート尺度](#Likert-scale)を用いて複数の質問の平均結果を示す方法。
各質問は概ね平均値でプロットされ、質問番号でラベル付けされている。
この形式は質問平均の[ヒストグラム](#histogram)に似ており、質問ラベルは観測された平均の相対頻度を示すために使用される。 
 
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="J"></div>

## [J]


---

<div id="K"></div>

## [K]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="kriging" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">kriging</span>
<span id="クリギング" class="term-jp">クリギング</span>

</td>
<td class="definition">

観測点の任意の配置や複数の次元に容易に一般化できる[補完器](#interpolator)。
それでも、クリギングは最小二乗に類似している。
クリギング予測が求められる点は、観測空間においてより近い観測点とより「相関」していると考えられている。
さらに、この点が実際に観測されている別の点に近づくにつれて、[相関](#correlation)は1.0に近づく。
これらの考えから、予測手法であるクリギングを形式化することができる。
n 個の観測の実験では、クリギングは n × n 行列の逆行列を必要とし、n を大まかに使用するのは扱いにくい。

</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="L"></div>

## [L]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="lack-of-fit" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">lack of fit</span>
<span id="不適合性" class="term-jp">不適合性</span>

</td>
<td class="definition">

観測の集合に関する[モデル](#model)の性質。
不適合性（適合の欠如）とは、[モデル](#model)が観測結果を予測または適合しない程度を指す。
適合性の欠如は、観測結果を取得する[過程](#process)における[実験](#SDE)誤差や[不確かさ](#uncertainty)が原因である可能性があるか、あるいは[モデル](#model)の欠陥が原因である可能性がある。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="LHC" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Latin hypercube design</span>
<span id="ラテン超方格計画" class="term-jp">ラテン超方格計画</span>

</td>
<td class="definition">

n 回の試行から構成される実験計画で、各[因子](#factor)は n 個の異なる水準を持つ。
通常、因子水準は等間隔で配置されている。
最高のラテン超方格計画は[直交配列](#orthogonal-array)に基づく。
ラテン超方格計画は、特に[コンピュータ実験](#computer-experiment)に有用である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="LHS" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Latin hypercube sampling</span>
<span id="ラテン超方格抜取り" class="term-jp">ラテン超方格抜取り</span>

</td>
<td class="definition">

[ラテン超方格](#LHC)計画を用いてシミュレータ出力の[分布](#distribution)を推定する[コンピュータ実験](#computer-experiment)手法。
[ラテン超方格](#LHC)計画の使用により、ラテン超方格抜取りは[モンテカルロ](#Monte-Carlo-sampling)法よりもはるかに精度が高くなることが可能である。
入力[因子](#factor)の[分布](#distribution)は、[因子水準](#factor-level)の間隔で表される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="LDL" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">LDL, lower detection limit</span>
<span id="LDL、下側検出限界" class="term-jp">LDL、下側検出限界</span>

</td>
<td class="definition">

[測定](#metrology)システムが背景[標準偏差](#sigma)を効果的に区別しなくなる水準。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Likert-scale" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Likert scale</span>
<span id="リッカート尺度" class="term-jp">リッカート尺度</span>

</td>
<td class="definition">

アンケートでの回答形式として、回答者が尺度に沿っていくつかの値のうちの一つを選ぶことが求められることがある。
5点と9点は一般的なリッカート尺度である。
リッカート尺度の両端は対向であり、中央の値はその間の度を表す。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="linearity" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">linearity</span>
<span id="線形性" class="term-jp">線形性</span>

</td>
<td class="definition">

[計測学](#metrology)において、測定対象機器の範囲全体にわたる[偏り](#bias)の差。
この定義は、y軸の測定結果とx軸の真の値との関係を観測すれば、最もよく理解できる。
理想的な線形性は、傾きが1.0の直線である。
（純粋な[偏り](#bias)は切片=0.0に相当する。）
線形性はやや誤称である。
これは、傾きが1.0の直線との差を指すためであり、非線形関係がある場合と、傾きが1.0以外の線形関係を持つ場合の両方で起こり得る。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="logistic-function" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">logistic function</span>
<span id="ロジスティック関数" class="term-jp">ロジスティック関数</span>

</td>
<td class="definition">

関数 1/(1+exp(-x))。
ロジスティック関数は、logistic(x)=0.5-logistic(-x) であるため、約ゼロで歪対称である。
応用例として、処理量応答曲線のモデル化、裾が厚い分布、そして[ニューラルネットワーク・モデル化](#neural-network)における「スカッシュ」関数としての活用が挙げられる。

</td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="M"></div>

## [M]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">

<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="mail-survey" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">mail survey</span>
<span id="メール調査" class="term-jp">メール調査</span>

</td>
<td class="definition">

回答者にメールで連絡する調査の実施方法。
Salant と Dillman（1994）は、メール調査の回答率を向上させるための一連の戦略を提示している。
これらには、興味深いカバー・デザイン、加速するリマインダーのポストカードや手紙、そして最終連絡（認証書留郵便）が含まれる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="matching" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">matching</span>
<span id="マッチング" class="term-jp">マッチング</span>

</td>
<td class="definition">

[後ろ向き](#retrospective)研究において、比較対象群を特定する方法。
観測単位のマッチング・ペア：関心特性Aと迷惑効果B、C、...の両方を有する各ユニットと、関心特性Aを欠く別のユニットがあるが、B、C、...を共有する。低利回りのロット（関心対象は[収量](#yield)です）は、ほぼ同時期に開始された同じ製品の収量のあるロットと比較して、このようになっている。
このようにマッチは、すべての利用可能なロットから「マッチ」を取る場合よりも、主要な因果差異（例えば、使用された特定の装備セットにおいて）に対してより[敏感](#sensitive)である。
マッチングは、共通性研究を実施する方法である。
マッチングは、遡及的研究における一種の[ブロック](#block)化である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="MCA" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">MCA</span>
<span id="MCA" class="term-jp">MCA</span>

</td>
<td class="definition">

測定能力の評価、あるいは測定能力の分析。[メトロロジー](#metrology)の[特性評価](#characterization)。
Sematech での定義は (a) [繰り返し性](#repeatability)、(b) [再現性](#reproducibility)に焦点を当てている。
より広い定義では、（c）測定対象の現象の変化に対する[感度](#sensitivity)（そのような[感度](#sensitivity)が望ましい）と（d）測定対象の現象以外の特徴に対する[感度](#sensitivity)（そのような[感度](#sensitivity)は好ましくない）を評価する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="MTBF" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">mean time between failures (MTBF)</span>
<span id="平均故障間隔時間（MTBF）" class="term-jp">平均故障間隔時間（MTBF）</span>

</td>
<td class="definition">

システムの1つまたは集合について、システムの1つの障害と次の障害との間の平均時間。
この平均時間は、修理待ち時間、修理に費やした時間、再認定に費やした時間などを除外しており、システムが利用可能で稼働している時間のみを測定することを意図している。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="measurement-error" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">measurement error</span>
<span id="測定誤差" class="term-jp">測定誤差</span>

</td>
<td class="definition">

1. [計測学](#metrology)または[測定](#MCA)システムに起因すると看做される観測された変動。
測定誤差は、[感度](#sensitivity)、[繰り返し性](#repeatability)、[再現性](#reproducibility)にさらに分解できる。</p>
2.[調査](#survey)において、回答者の回答が不正確、不正確、または他の回答者と比較して容易でない場合に生じる誤差。
Salant と Dillman（1994）は、そのような測定誤差を手法、質問票、インタビュアー、および回答者の誤差に分けている。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="meta-analysis" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">meta analysis</span>
<span id="メタ分析" class="term-jp">メタ分析</span>

</td>
<td class="definition">

個々の調査結果を定量的に統合し、全体的な有意性の単一の記述にまとめた統計手法群。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="metamodel-calibration" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">metamodel calibration</span>
<span id="メタモデルの校正" class="term-jp">メタモデルの校正</span>

</td>
<td class="definition">

モデルの未知の係数を以下の手順で決定する方法：</p>
1. 未知の係数を変化させ、期待される[応答](#response)を記録して[コンピュータ実験](#computer-experiment)を実行する。
2. [コンピュータ実験](#computer-experiment)の[応答](#response)を入力、[因子](#factor)を出力として、特に[ニューラルネットワーク](neural-network)の一般的な形態の[モデル](#model)を適合させる。
3. 入力を経験的に観測された値とした場合、この[モデル](#model)から得られる未知係数を出力として抽出する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="method-error" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">method error</span>
<span id="方法誤差" class="term-jp">方法誤差</span>

</td>
<td class="definition">

[測定誤差](#measurement-error)のうち、[測定](#MCA)[工程](#process)の詳細に起因する部分。
[調査](#survey)では、例えば、[対面](#face-to-face)、郵送、[電話](#telephone)などでアンケートを実施する。
これらの異なる手法は異なる結果をもたらすと認識されており、その程度において、これは方法誤差の例である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="metrology" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">metrology study</span>
<span id="計測学研究" class="term-jp">計測学研究</span>

</td>
<td class="definition">

時には、[ゲージ](#gauge-study)能力調査、または[測定](#MCA)能力評価と呼ばれる。
このような研究は、[測定](#MCA)機器の能力と限界を定量化し、しばしばその[繰り返し性性](#repeatability)、[再現性](#reproducibility)、そして時には[感度](#sensitivity)を推定する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="mixture-experiment" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">mixture experiment</span>
<span id="配合計画" class="term-jp">配合計画</span>

</td>
<td class="definition">

各実験の実行が制約され、[因子](#factor)を横断的に合計した際に[因子水準](#factor-level)が一定に総和されるように制約される[実験計画](#SDE)。
典型的な応用は、[要素](#factor)が液体、あるいは時には気体である化学実験を含む。
そのような場合、重要なのは各液体成分の比率であり、重量や体積ではない。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="model" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">model</span>
<span id="モデル" class="term-jp">モデル</span>

</td>
<td class="definition">

変数間の関係に関する数学的記述。
モデルは2つの基本的な種類に分けられるか、2つの基本部分から構成される：統計モデルは測定された量を予測し、確率モデルは異なる無作為な結果の相対頻度を予測する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="monitor-variable" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">monitor variable</span>
<span id="監視変数" class="term-jp">監視変数</span>

</td>
<td class="definition">

[工程](#process)の測定可能な特性で、[工程管理](#SPC)の目的に特に関連性が高く、情報量も有する。
[製品受入](#SQC)のより関連性の高い[重要係数](#critical-parameters)とは区別される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Monte-Carlo-sampling" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Monte Carlo sampling</span>
<span id="モンテカルロ標本抽出法" class="term-jp">モンテカルロ標本抽出法</span>

</td>
<td class="definition">

シミュレータの出力の[分布](#distribution)を推定するために、[乱](#randomization)数を使用する[コンピュータ実験](#computer-experiment)手法。

</td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="N"></div>

## [N]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="neural-nets" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">neural nets</span>
<span id="ニューラルネット" class="term-jp">ニューラルネット</span>

</td>
<td class="definition">

[ニューラルネットワーク](#neural-network)モデルを参照のこと。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="neural-network" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">neural network model</span>
<span id="ニューラル・ネットワーク・モデル" class="term-jp">ニューラル ネットワーク モデル</span>

</td>
<td class="definition">

観測されていない変数の層を1つ以上仮定する、
非常に柔軟な[モデル](#model)化手法である。
各観測されていない変数は、前層の変数の線形関数であり（第一層は因子、すなわちモデル入力である）。
次層への出力として、観測されていない各変数の出力は、ほぼ常に非線形関数、すなわち[ロジスティック関数](#logistic)によって変換される。
ニューラル・ネットワークは、特に[実験](#SDE)規模が[クリギング](#kriging")を実務上不可能にする場合に、[コンピュータ実験](#computer-experiment)の解析に時折使用される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="noise-factor" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">noise factor</span>
<span id="誤差因子" class="term-jp">誤差因子</span>

</td>
<td class="definition">

特に[実験](#SDE)においては、制御が困難であるか、しづらい[因子](#factor)や工程入力。
誤差因子には、製品の使用条件（温度、試験条件、環境）も含まれる。
通常、[制御因子](#controlfactor)とは区別される。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="NSRratio" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">noise-to-signal ratio</span>
<span id="ノイズ対信号比" class="term-jp">ノイズ対信号比</span>

</td>
<td class="definition">

[測定](#metrology)システムの[精度](#precision)と平均測定値の比率；信号対雑音比の逆数。
ノイズ対信号比は、測定精度の大きさを百分率尺度で表現する。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="nonresponse" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">nonresponse</span>
<span id="無回答" class="term-jp">無回答</span>

</td>
<td class="definition">

[実験](#SDE)、[調査](#survey)、または観察研究のときに、[応答](#response)（関心のある結果）が測定できず、完全に記録できない事象。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="nonresponseerror" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">nonresponseerror</span>
<span id="無回答誤差" class="term-jp">無回答誤差</span>

</td>
<td class="definition">

[調査](#survey)において、標本回答者が質問票への回答を拒否した場合に生じる誤差は、特に全体としての回答者が、研究にとって重要な回答の仕方で回答する回答者と異なるように見える場合である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="normal-distribution" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[normal distribution](docs/ch1_eda/section3/eda3661.htm)

</span>
<span id="正規分布" class="term-jp">

[正規分布](docs/ch1_eda/section3/eda3661.htm)

</span>

</td>
<td class="definition">

高い点またはモードが1つある対称[分布](#distribution)で、時には釣鐘型曲線とも呼ばれる。
平均は、たとえごく少量のデータであっても、正規分布に類似した[分布](#distribution)を持つことが多い多くの統計計算の一つ。
産業において、正規分布には4つの重要な特性がある。</p>

1. それは対称である。
2. ±1 の[標準偏差](#sigma)の範囲内では、分布の約68パーセントが囲まれている。
3. ±2標準偏差範囲内は、95%である。
4. ±3標準偏差範囲内は、99.7%である。

  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="O"></div>

## [O]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="objective-methods" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">objective methods</span>
<span id="客観的手法" class="term-jp">客観的手法</span>

</td>
<td class="definition">

データ収集の手法、特にデータ分析の手法は、個人固有の意見や知識に依存しないという点が特徴である。
客観的手法は、科学的観点から再現可能であり、原則としてソフトウェア・アルゴリズムに変換可能である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="off-line-SPC" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">off-line SPC</span>
<span id="オフライン SPC" class="term-jp">オフライン SPC</span>

</td>
<td class="definition">

[ヒストグラム](#histogram)、[チェックリスト](#checklist)、[パレート](#Pareto-analysis")図、[能力](#capability)指標、および[実験計画](#SDE)など、[工程](#process)の選択された特性を特徴付けることを目的とした手法で、[異常原因](#special-cause)を調査または補正するために制御アルゴリズムの起動すべき時期を必ずしも決定しない。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="on-line-SPC" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">on-line SPC</span>
<span id="オンラインSPC" class="term-jp">オンラインSPC</span>
</td>
<td class="definition">

[管理図](#control-chart)のような手法で、[工程](#process)を自然[変動](#variation)に対して監視し、[異常原因](#special-cause)を調査または補正するために制御アルゴリズムの呼び出し時期を特定しようとする。
[EVOP](#EVOP)などの特定の統計手法は、[工程](#process)の動的最適化を追求する。
これらはオンラインの SPC 手法でもある。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="open-ended-question" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">open-ended question</span>
<span id="自由解答式質問" class="term-jp">自由解答式質問</span>

</td>
<td class="definition">

[調査](#survey)において、質問を提示するが、回答を構成（はい・いいえ、1から10までの尺度など）しようとしない質問形式。
むしろ、回答者は口頭または書面で、本人の言葉で回答することが求められる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="opinion-driven" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">opinion driven</span>
<span id="意見駆動型" class="term-jp">意見駆動型</span>

</td>
<td class="definition">

個人的な意見や恣意的な補正[要因](#factor)、あるいは客観的根拠のないその他の選択に依存する性質。
[データ駆動型](#data-driven)の対義語。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="optimal-design" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">optimal design</span>
<span id="最適設計" class="term-jp">最適設計</span>
</td>
<td class="definition">

目的関数を最大化するコンピュータ・アルゴリズムを用いて[実験計画](#SDE)を作成する手法。
最も一般的な目的関数は係数の分散‐共分散行列の行列式であり、このような設計は D‐optimum と呼ばれる。
最適設計手法とは対照的に、[直交配列](#orthogonal-array)に基づく。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="optimum" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">optimum</span>
<span id="最適" class="term-jp">最適</span>
</td>
<td class="definition">

1. 特に[実験](#SDE)により決定された場合、関心のある[応答](#response)の最適均衡を実現する[因子](#factor)設定点の組合せ。
2. そのような[因子](#factor)設定点の集合において達成された平均[応答](#response)値。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="orthogonal-array" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">orthogonal array</span>
<span id="直交配列" class="term-jp">直交配列</span>
</td>
<td class="definition">

行と列から構成される表で、任意の列（[要因](#factor)）の対に対してすべての値（[水準](#factorlevel)）の組合せがあり、さらにすべての組合せが同じ回数出現するという特性を持つ。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="outliers" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">outliers</span>
<span id="外れ値" class="term-jp">外れ値</span>

</td>
<td class="definition">

値が極めて極端で、データ集合の他の部分と一致していないように見える観測。
工程監視では、外れ値が[突き止められる原因](#assignable)や[異常原因](#special-cause)が存在することを示す。
データ分析から特定の外れ値を削除することは、そうした一般的な原因が特定されたときに最も正当化しやすい。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="out-of-control" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">out of control</span>
<span id="管理外れ" class="term-jp">管理外れ</span>
</td>
<td class="definition">

平均や範囲などの[統計](#statistic)が[管理限界](#control-limits)を超える場合、または[管理限界](#control-limits)内であってもその[統計](#statistic)に有意な傾向やパターンが現れる場合、[工程](#process)は管理外れとなる。
管理外れであることは、[工程](#process)の本質的な性質ではなく、時間で範囲が設定された状態で定義される。
類推により、任意の時点で、作業者が事故（管理外れ）に巻き込まれることも、関与しないこともある。
[プロセスの](#process)本質的な性質は、作業者が安全な作業者であるか（管理外れ状態の頻度が過剰か）である。
後者を決定するには、本質的な安全性（[安定性](#stability)）は通常、長期間にわたる観察が必要であり。

  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="P"></div>

## [P]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tbody><tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Pareto" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">Pareto analysis</span>
<span id="パレート解析" class="term-jp">パレート解析</span>

</td>
<td class="definition">

すべての潜在的な問題領域や[変動](#variation)要因をそれぞれの寄与度に基づいて順位付けする問題解決手法。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="partially-open-question" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">partially open question</span>
<span id="部分的に開かれた質問" class="term-jp">部分的に開かれた質問</span>

</td>
<td class="definition">

[調査](#survey)において、質問形式は回答をある程度構成するだけでなく、回答者が口頭で回答することも認める。
[閉じた質問](#closeended)と[開かれた](#openended)質問のハイブリッドである。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="PDC" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">PDC, Passive data collection</span>
<span id="PDC" class="term-jp">受動的データ収集</span>

</td>
<td class="definition">

受動的データ収集は、時に「[前向き](#prospective)観察研究」と呼ばれる。
[工程](#process)を繰り返し測定し測定する技術[特性付け](#characterization)の初期段階であり、介入（調整、変更、処方変更）は回避される。
Sematech資格計画に関連している。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="Poisson-distribution" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[Poisson distribution](docs/ch1_eda/section3/eda366i.md)

</span>
<span id="ポアソン分布" class="term-jp">

[ポアソン分布](docs/ch1_eda/section3/eda366i.md)

</span>

</td>
<td class="definition">

離散的な事象を[モデル](#model)化するために用いられる重要な理論[分布](#distribution)であり、特に領域における欠陥の数をモデルにする。
ポアソン分布は、観測領域（または体積、時間間隔など）あたりの平均欠陥密度を表す変数である<i>λ</i>に依存する。
ポアソン分布は、重複しない二つの観測単位における欠陥の数が独立であると仮定している。
さらに、ポアソン分布は、欠陥数の分布が観測される領域のみに依存すると仮定している。
[二項分布](#binomial-distribution)とは異なり、原則としてポアソン分布は任意の領域で観測できる欠陥の数に上限を設けない。
半導体産業において特に注目すべきは、面積<i>A</i>の領域で欠陥がゼロであるポアソン確率（exp{-lambda<i> A</i>}）であり、これは[収量](#yield)[モデル](#model)化に有用である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="population" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

[population](docs/ech1_da/section3/eda35.md)

</span>
<span id="母集団" class="term-jp">

[母集団](docs/ech1_da/section3/eda35.md)

</span>

</td>
<td class="definition">

ウェハや人物などの知りたい性質に関する潜在的な観測の全集合。
[サンプル](#sample)の対義語。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="precision" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">precision</span>
<span id="精度" class="term-jp">精度</span>

</td>
<td class="definition">

1. [計測学](#metrology)において、[測定](#MCA)[工程](#process)の平均値に関する変動性。
精度は通常、[精確さ](#accuracy)と区別される。
精確性とは、測定[工程](#process)の真の値に対する変動性である。
精度は、短期的な[変動](#variation)（[繰り返し性](#repeatability)）と長期的な[変動](#variation)（[再現性）](#reproducibility)にさらに分解することができる。</p>
2. データが多いほど、知識がより多く、あるいは信頼区間が短くなるという一般的な概念を指す[曖昧な概念](#fuzzy-concepts)用語であり、すなわち、データが多いほど、回答や意思決定の精度が高くなる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="prevention" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">prevention</span>
<span id="予防" class="term-jp">予防</span>

</td>
<td class="definition">

生産資材が危険にさらされる前に実施される工程監視と是正措置の種類。</td>

</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">
<span id="probability-plot" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">

probability plot

</span>
<span id="確率プロット" class="term-jp">

[確率プロット](docs/ch1_eda/section3/probplot.md)

</span>

</td>
<td class="definition">

観測された分布が理論的分布、特に[正規分布](#normal-distribution)と一致する形状を持つかどうかを評価するために設計されたプロット。
観測された値は、理論分布から期待される順序統計量に対してプロットされる。
直線が見かけ上の場合、観測された分布と理論上の分布は同じ形であると言われる。
確率プロットは、観測された分布が多数の観測値で構成されている場合に特に有用であり、比較対象がごく少数の群に限られる場合に有用である。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="process" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">process</span>
<span id="工程" class="term-jp">工程/過程/プロセス</span>

</td>
<td class="definition">

特定の作業活動における人員、手順、機械、材料、[測定](#MCA)装置、および環境条件の組合せ。
測定可能な入力と出力を備えた、繰り返し可能な活動の一連の流れ。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="process-signature" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">process signature</span>
<span id="工程指紋" class="term-jp">工程指紋/工程固有の挙動パターン</span>

</td>
<td class="definition">

[工程](#process)[特性付け](#characterization)には、入力変数に対する[感度](#sensitivity)、自然[変動](#variation)の大きさ、流入材料の[変動](#variation)に対する[感度](#sensitivity)、そして動的および出力プロファイルを自然に動作する場合と異常に振る舞う場合の両方が含まれる。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="process-capability-study" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">process capability study</span>
<span id="工程能力調査" class="term-jp">工程能力調査</span>

</td>
<td class="definition">

[工程](#process)の[共通原因](#common-cause)変動を定量化する研究。
[能力調査](#capability-study)も参照のこと。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="proctor-survey" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">proctor survey</span>
<span id="監督付き調査" class="term-jp">監督付き調査</span>

</td>
<td class="definition">

[調査](#survey)を実施する方法として、回答者を監督者が出席する部屋に配置する。
監督者付き調査は回答者の回答の[機密性](#confidentiality)を保持しつつ、十分な行政体制を提供し、高い回答率を確保できるようにする。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="prospective" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">prospective</span>
<span id="前向き研究" class="term-jp">前向き研究</span>

</td>
<td class="definition">

[標本](#sample)選択および調査対象のすべての現象が、研究開始後に行われる非実験的研究の一種。
[PDC](#PDC)も参照のこと。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="proxy" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">proxy</span>
<span id="代理" class="term-jp">代理</span>

</td>
<td class="definition">

[特徴付け](#characterization)において、別の変数を置き換えるために使用される変数は、[応答](#response)の場合は[測定](#metrology)が容易であり、あるいは[因子](#factor)の場合は操作しやすい。

</td>
</tr>

<tr>
<td class="headword" style="width: 15%; vertical-align: top;">

<span id="PTratio" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">PT-ratio</span>
<span id="P/T比率" class="term-jp">P/T比率</span>

</td>
<td class="definition">

[計測学](#metrology)において、製造状況に適用した場合の「精度‐許容」比。[精度](#precision)要素は通常、[測定誤差](#measurement-error)（[精度](#precision)、[再現性](#reproducibility)）の3[標準偏差](#sigma)の大きさであり、許容要素は通常、対応する半許容値であるUSL-(USL+LSL)/2で、USL（L）はそれぞれ上限（下限）の仕様限界を示す。
新しい[計測学](#metrology)または工程開発プロジェクトの共通の目標は、P/T比を0.1にすることである。

  </td>
</tr>  
<tr><td></td><t
d>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="Q"></div>

## [Q]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="R"></div>

## [R]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="S"></div>

## [S]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="T"></div>

## [T]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="U"></div>

## [U]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="V"></div>

## [V]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">
  <span id="variation" class="term-en" style="display: block; margin-bottom: 6px; font-style: italic;">variation</span>
  <span id="変動" class="term-jp">変動</span>
  </td>
  <td class="definition">
  
  [工程](#accuracy)の個々の出力間の違い。変異の原因は、<a href="#common1">共通原因</a>と<a href="#specialcause">特殊原因</a>という二つの主要なクラスに分類できます。<a href="3D&quot;#common1&quot;">共通原因</a>の変動は、しばしば<a href="#variancecomponents">分散要素</a>に分解されます。
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="W"></div>

## [W]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="X"></div>

## [X]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="Y"></div>

## [Y]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">


  
  </td>
</tr>  

<tr>
  <td class="headword" style="width: 15%; vertical-align: top;">



  </td>
  <td class="definition">

  
  </td>
</tr>

<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>  

</table>

---

<div id="Z"></div>

## [Z]

<table class="glossary" style="width: 540px; border-collapse: separate; border-spacing: 20px;">
<tr><td></td><td>

[ページの先頭へ戻る](#top)

</td></td></tr>

</table>

---

#### 訳註

JIS Z 8110
<span id="1">[1]: JIS Z 8101-2</span>
<span id="2">[2]: JIS Z 8101-3</span>