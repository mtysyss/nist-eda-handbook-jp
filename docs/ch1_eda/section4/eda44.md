[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/eda/section4/eda44.htm)  
閲覧(UTC)：2026-04-28 02:35:50  
[⬅️](eda42a6.md)[➡️](../eda.md)  

1. [探索的データ解析](../eda.md)  
1.4. [EDA事例研究](eda4.md)  

---

# 1.4.4. EDA技法の Dataplot コマンド類

こージは、本章で議論されている図表現および分析技法に用いる Dataplot のコマンド類を収録している。
これは、適切なコマンドへ案内するだけのものである。
これらのコマンドに関する完全な解説は、[Dataplot リファレンス・マニュアル](http://www.itl.nist.gov/div898/software/dataplot/document.htm)を入手してください。

---

#### 1因子分散分析の Dataplot コマンド
一元配置分散分析を行う Dataplot コマンドは、以下の通り。

```
ANOVA Y X
```

ここで、Y は応答変数、X は群識別変数である。 

Dataplot は現在、バランス計画の場合（すなわち、各水準で観測値の数が同じである場合）に限定されており、交互作用効果の推定値は計算されない。

[一元分散分析のページに戻る](../section3/eda354.md) 

---

#### 多因子分散分析の Dataplot コマンド
多因子分散分析を生成する Dataplot コマンドは、以下の通り。

```
ANOVA Y X1  
ANOVA Y X1 X2  
ANOVA Y X1 X2 X3  
ANOVA Y X1 X2 X3 X4  
ANOVA Y X1 X2 X3 X4 X5  
```

ここで、Yは応答変数であり、X1、X2、X3、X4、および X5は因子変数である。
Dataplot では最大10個の因子変数まで指定可能である。 

Dataplot は現在、バランス計画の場合（すなわち、各水準で観測値の数が同じである場合）に限定されており、交互作用効果の推定値は計算されない。

[多因子分散分析のページに戻る](../section3/eda355.md)  

---

#### Anderson-Darling 検定の Dataplot コマンド
Anderson-Darling 検定の Dataplot コマンドは以下の通り。

```
ANDERSON DARLING NORMAL TEST Y  
ANDERSON DARLING LOGNORMAL TEST Y  
ANDERSON DARLING EXPONENTIAL TEST Y  
ANDERSON DARLING WEIBULL TEST Y  
ANDERSON DARLING EXTREME VALUE TYPE I TEST Y  
```

ここで、Y は応答変数である。

[Anderson-Darling 検定のページに戻る](../section3/eda35e.md)

---

#### 自己相関の Dataplot コマンド
Dataplot でラグ1 の自己相関値を計算するには、次のように入力する。

```
LET A = AUTOCORRELATION Y  
```

ここで、Yは応答変数である。 

Dataplot で、ラグ1 より大きい自己相関を生成する最も簡単な方法は次の通り。

```
AUTOCORRELATION PLOT Y  
LET AC = YPLOT  
LET LAG = XPLOT  
RETAIN AC LAG SUBSET TAGPLOT = 1  
```

AUTOCORRELATION PLOT コマンドは、ラグ0 から N/4 までの自己相関プロットを出力する。
また、自己相関の 95%および 99%信頼限界も出力する。 
Dataplot は、プロットの座標を内部変数 XPLOT、YPLOT、および TAGPLOT に格納する。
2つの LET コマンドと RETAIN コマンドは、自己相関の数値を抽出するために使用する。
変数 LAG はラグを識別し、AC の対応する行には自己相関値が格納される。

[自己相関のページに戻る](../section3/eda35c.md)  

---

#### 自己相関プロットの Dataplot コマンド
自己相関プロットを作成するコマンドは次の通り。

```
AUTOCORRELATION PLOT Y  
```

自己相関プロットの表示は、LINE、CHARACTER、および SPIKE コマンドを適切に設定し制御する。
Dataplot は、自己相関プロット上に以下の曲線を描画する。

1. 自己相関曲線  
2. 原点を通る基準線  
3. 95%信頼限界の上限にある基準線  
4. 95%信頼限界の下限にある基準線  
5. 99%信頼限界の上限にある基準線  
6. 99%信頼限界の下限にある基準線  

たとえば、自己相関をスパイクで、ゼロ基準線を実線で、95%の線を破線で、99%の線を点線で描画するには、次のコマンドを入力する。

```
LINE BLANK SOLID DASH DASH DOT DOT  
CHARACTER BLANK ALL  
SPIKE ON OFF OFF OFF OFF OFF  
SPIKE BASE 0  
```

デフォルトでは、信頼区間の幅は固定されている。
これはホワイト・ノイズ（すなわち、無作為性）の検定には適している。
Box-Jenkins モデル化では、幅可変の信頼区間の方が適している。
幅可変の信頼区間を設定するには、次のコマンドを入力する。

```
SET AUTOCORRELATION BAND BOX-JENKINS  
```

固定幅の信頼区間に戻すには、次のように入力する。

```
SET AUTOCORRELATION BAND WHITE-NOISE  
```

[自己相関プロットのページに戻る](../section3/eda331.md)   

---

#### Bartlett 検定の Dataplot コマンド
Bartlett 検定の Dataplot コマンドは次の通り。

```
BARTLETT TEST Y X  
```

ここで、Yは応答変数、Xは群ID変数である。 

上記は、Bartlett 検定の標準形式を計算する。
Bartlett 検定の Dixon-Massey 形式を計算するには、Dataplot コマンドで以下のいずれかを使用する（これらは同義語であり、別々のコマンドではない）。

```
DIXON BARTLETT TEST Y X  
DIXON MASSEY BARTLETT TEST Y X  
DM BARTLETT TEST Y X  
```

[Bartlett 検定のページに戻る](../section3/eda357.md)  

---

#### 対比ヒストグラムの Dataplot コマンド
対比ヒストグラムを描画する Dataplot コマンドは次の通り。

```
BIHISTOGRAM Y1 Y2  
```

標準のヒストグラムと同様に、階級幅、階級の下限、および階級の上限は、以下のコマンドで制御できる。

```
CLASS WIDTH <値>  
CLASS LOWER <値>  
CLASS UPPER <値>  
```

さらに、相対対比ヒストグラム、累積対比ヒストグラム、および相対累積対比ヒストグラムは、以下のコマンドで描画する。

```
RELATIVE BIHISTOGRAM Y1 Y2  
CUMULATIVE BIHISTOGRAM Y1 Y2  
RELATIVE CUMULATIVE BIHISTOGRAM Y1 Y2  
```

[対比ヒストグラムのページに戻る](../section3/eda332.md)  

---

#### 二項分布の確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して二項分布の確率関数を計算する。

```
cdf		LET Y = BINCDF(X,P,N)  
pdf		LET Y = BINPDF(X,P,N)  
ppf		Y = BINPPF(F,P,N)  
乱数		LET N = 値  
				LET P = 値  
				LET Y =BINOMINAL RANDOM NUMBEERS FOR I = 1 1 1000  
確率プロット	LET N = 値  
				LET P = 値  
				BINOMINAL PROBABILITY PLOT Y  
```

ここで、X は数値、母数、または変数である。
P および N は形状母数で、必須である。
これらは数値、母数、または変数である。
通常は数値または母数である。

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT BINPDF(X,0.5,100) FOR X = 0 1 100  
```

[二項分布のページに戻る](../section3/eda366i.md) [^1]  

---

#### ブロック・プロットの Dataplot コマンド
ブロック・プロットの Dataplot コマンドは次の通り。

```
BLOCK PLOT Y X1 X2 X3 など XP  
```

ここで

* Y は応答変数であり、
* X1、X2、X3 などは、1つ以上の交絡因子（＝二次因子）であり、
* XP は主要な関心のある因子である。

通常、ブロック・プロットの前に以下のコマンドを記述する。

```
CHARACTER 1 2  
LINE BLANK BLANK
```

これらのコマンドは、主要因の描画文字を設定する。
1 や 2 は有用な指標であるが、描画文字の選択は利用者の裁量に委ねられている。

[ブロック・プロットのページに戻る](../section3/eda333.md)  

---

#### ブートストラップ・プロットの Dataplot コマンド
ブートストラップ・プロットの Dataplot コマンドは次の通り。

```
BOOTSTRAP <STAT> PLOT Y  
```

ここで、<STAT> は以下のいずれかである。

```
MEAN
MIDMEAN
MIDRANGE
MEDIAN
TRIMMED MEAN
WINSORIZED MEAN
GEOMETRIC MEAN
HARMONIC MEAN
SUM
PRODUCT
MINIMUM
MAXIMUM

STANDARD DEVIATION
VARIANCE
STANDARD DEVIATION OF MEAN
VARIANCE OF MEAN
RELATIVE STANDARD DEVIATION
RELATIVE VARIANCE
AVERAGE ABSOLUTE DEVIATION
MEDIAN ABSOLUTE DEVIATION
LOWER QUARTILE
LOWER HINGE
UPPER QUARTILE
UPPER HINGE

FIRST DECILE
SECOND DECILE
THIRD DECILE
FOURTH DECILE
FIFTH DECILE
SIXTH DECILE
SEVENTH DECILE
EIGHTH DECILE
NINTH DECILE
PERCENTILE

SKEWNESS
KURTOSIS

AUTOCORRELATION
AUTOCOVARIANCE
SINE FREQUENCY
COSINE FREQUENCY

TAGUCHI SN0
TAGUCHI SN+
TAGUCHI SN-
TAGUCHI SN00
```

BOOTSTRAP PLOT コマンドの後に、[ヒストグラム](../section3/eda33e.md)やその他の分布プロットが続くことがほとんどである[^2]。

Dataplot は、BOOTSTRAP PLOT コマンドの実行後に、以下の内部母数を自動的に保存する。

BMEAN - プロットされたブートストラップ値の平均  
BSD   - プロットされたブートストラップ値の標準偏差  
B001  - プロットされたブートストラップ値の 0.1 百分位数  
B005  - プロットされたブートストラップ値の 0.5 百分位数  
B01   - プロットされたブートストラップ値の 1.0 百分位数  
B025  - プロットされたブートストラップ値の2.5 百分位数  
B05   - プロットされたブートストラップ値の5.0 百分位数  
B10   - プロットされたブートストラップ値の10 百分位数  
B20   - プロットされたブートストラップ値の20 百分位数  
B80   - プロットされたブートストラップ値の80 百分位数  
B90   - プロットされたブートストラップ値の90 百分位数  
B95   - プロットされたブートストラップ値の95 百分位数  
B975  - プロットされたブートストラップ値の97.5 百分位数  
B99   - プロットされたブートストラップ値の99 百分位数  
B995  - プロットされたブートストラップ値の99.5 百分位数  
B999  - プロットされたブートストラップ値の99.9百分位数  

これらの内部母数は信頼区間を計算するのに有用であり、出力（PRINT BMEAN）したり、他の利用者定義母数と同様に使用したりする（例：LET UCL = B95）。 

使用するブートストラップ部分標本の数を指定するには、次のコマンドを入力する。

```
BOOTSTRAP SAMPLE <N>
```

ここで <N> は希望するサンプル数である。
デフォルトは 500 である（古い実装では 100 の場合もある）。 

Dataplot では、直接サポートされていない統計量についてもブートストラップ推定値を計算できる。
以下の例は、500個の正規乱数の平均に対するブートストラップ計算を示している。
Dataplot では直接行うこともできるが、ここではサポートされていない統計量に必要な手順を示している。
部分標本はループを使用して作成する。
BOOTSTRAP INDEX および BOOTSTRAP SAMPLE コマンドは単一の部分標本を生成し、それを Y2 に格納する。
その後、Y2 に対して目的の統計量を計算し、その結果を配列に格納する。
ループ終了後、配列 XMEAN には 100 個の平均値を保持している。

```
LET Y = NORMAL RANDOM NUMBERS FOR I = 1 1 500 
LET N = SIZE Y 
LOOP FOR K = 1 1 500 
	LET IND = BOOTSTRAP INDEX FOR I = 1 1 N 
	LET Y2 = BOOTSTRAP SAMPLE Y IND 
	LET A = MEAN Y2 
	LET XMEAN(K) = A 
END OF LOOP  
HISTOGRAM XMEAN
```

[ブートストラップのページに戻る](../section3/eda334.md)  

---

#### Box-Cox 線形性プロットの Dataplot コマンド
Box-Cox 線形性プロットを描画する Dataplot コマンドは次の通り。

```
BOX-COX LINEARITY PLOT Y X
```

ここで、Y と X は応答変数である。

[Box-Cox 線形性プロットのページに戻る](../section3/eda335.md)  

---

#### Box-Cox 正規性プロットの Dataplot コマンド
Box-Cox 正規性プロットを描画する Dataplot コマンドは次の通り。

```
BOX-COX NORMALITY PLOT Y
```

ここで、Yは応答変数である。

[Box-Cox 正規性プロットのページに戻る](../section3/eda336.md)  

---

#### 箱ひげ図の Dataplot コマンド
箱ひげ図を作成する Dataplot コマンドは次の通り。

```
BOX PLOT Y X
```

BOX PLOT コマンドの前には、通常、以下のコマンドを記述する。

```
CHARACTER BOX PLOT 
LINE BOX PLOT 
```

これらのコマンドは、箱ひげ図のデフォルトの線と文字の設定を行いる。
必要に応じて、CHARACTER および LINE コマンドを使用して、独自の線や文字の設定を選択することもできる。 

外れ値を円として表示するには、次のコマンドを入力する。

```
FENCES ON 
```

[箱ひげ図のページに戻る](../section3/eda337.md)  

---

#### Cauchy 確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して Cauchy 分布の確率関数を計算する。

```
cdf		LET Y = CAUCDF(X,A,B)  
pdf		LET Y = CAUPDF(X,A,B)  
ppf		Y = CAUPPF(X,A,B)  
ハザード		LET Y = CAUHAZ(X,A,B)  
累積ハザード	LET Y = CAUCHAZ(X,A,B)  
生存		LET Y = 1 - CAUCDF(X,A,B)  
逆生存		LET Y = CAUPPF(1-X,A,B)  
乱数		LET Y = CAUCHY RANDOM 
				NUMBERS FOR I = 1 1 1000  
確率プロット	CAUCHY PROBABILITY PLOT Y  
```

ここで、X は数値、母数、または変数にする。
A および B は位置母数と尺度母数であり、これらは省略可能である
（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかにする。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT CAUPDF(X) FOR X = -5 0.01 5 
```

[Cauchy 分布のページに戻る](../section3/eda3663.md)

---  

#### カイ二乗確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用してカイ二乗分布の確率関数を計算する。

```
cdf		LET Y = CHSCDF(X,NU,NU2,A,B)
pdf		LET Y = CHSPDF(X,NU,A,B)
ppf		LET Y = CHSPPF(X,NU,A,B)
乱数		LET NU = 値
				LET Y = CHI-SQUARE RANDOM 
				NUMBERS FOR I = 1 1 1000
確率プロット	LET NU = 値
				CHI-SQUARE PROBABILITY PLOT Y
ppcc プロット	LET NU = 値
				CHI-SQUARE PPCC PLOT Y
```
ここで、X は数値、母数、または変数である。
NU は形状母数（自由度の数）である。
NU は数値、母数、または変数である。
ただし、通常は数値または母数のいずれかである。
A および B は位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数である。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT CHSPDF(X,5) FOR X = 0 0.01 5 
```

[カイ二乗分布のページに戻る](../section3/eda3666.md)  

---

#### カイ二乗適合度検定の Dataplot コマンド
カイ二乗適合度検定を行う Dataplot コマンドは以下の通り。

```
<dist> CHI-SQUARE GOODNESS OF FIT TEST Y 
<dist> CHI-SQUARE GOODNESS OF FIT TEST Y X 
<dist> CHI-SQUARE GOODNESS OF FIT TEST Y XL XU 
```

ここで、`<dist>` は 70 以上の組み込み分布のいずれかである。
Dataplot は、累積分布関数をサポートするすべての分布について、カイ二乗適合度検定をサポートしている。
サポートされている分布のリストを表示するには、コマンド LIST DISTRIBUTIONS を入力する。
具体的な例としては、

```
NORMAL CHI-SQUARE GOODNESS OF FIT TEST Y
LOGISTIC CHI-SQUARE GOODNESS OF FIT TEST Y
DOUBLE EXPONENTIAL CHI-SQUARE GOODNESS OF FIT TEST Y
```

（サポートされている任意の分布について）位置母数と尺度母数を指定するには、次のように入力する。

```
LET CHSLOC = 値 
LET CHSSCAL = 値 
```

形状母数が必要な分布については、1つ以上の形状母数の値を入力する必要がある。
例えば、ガンマ分布の形状母数 gamma を指定するには、以下のコマンドを入力する。

```
LET GAMMA = 値 
GAMMA CHI-SQUARE GOODNESS OF FIT TEST Y 
```

Dataplot では、階級幅、下限（すなわち、最初のビンの開始値）、および上限（すなわち、最後のビンの終了値）を制御することもできる。
これらのコマンドは以下の通り。

```
CLASS WIDTH 値 
CLASS LOWER 値 
CLASS UPPER 値 
```

ほとんどの場合、Dataplotのデフォルトの階級間隔で十分である。 

データがすでにビン分けされている場合は、以下のコマンドを入力する。

```
NORMAL CHI-SQUARE GOODNESS OF FIT TEST Y X 
NORMAL CHI-SQUARE GOODNESS OF FIT TEST Y XL XU 
```

上記の両方のコマンドにおいて、Y は頻度変数である。
X 変数が1つ指定する場合、Dataplot はそれを区間の中点と見なし、区間の幅は等しいと仮定する。
X 変数が2つ指定する場合、Dataplot はこれらを区間の端点と見なし、区間の幅は必ずしも等しくないものと仮定する。
ビン幅を不均一にするのは、通常、頻度の少ない階級を結合するために行われる。
これは、観測数が5未満の頻度階級がある場合、検定のためのカイ二乗近似が正確でない可能性があることによる。 

[カイ二乗適合度のページに戻る](../section3/eda35f.md)  

---

#### 標準偏差のカイ二乗検定の Dataplotコマンド
標準偏差のカイ二乗検定を行う Dataplot コマンドは以下の通り。

```
CHI-SQUARE TEST Y A
```

ここで、Y は応答変数、A は検定対象の値である。

[標準偏差のカイ二乗検定のページに戻る](../section3/eda358.md)  

---

#### 複素復調振幅プロットの Dataplot コマンド
複素復調振幅プロットを作成する Dataplot コマンドは以下の通り。

```
COMPLEX DEMODULATION AMPLITUDE PLOT Y
```

ここで、Y は応答変数である。

[複素復調振幅プロットのページに戻る](../section3/eda338.md)  

---

#### 複素復調位相プロットの Dataplot コマンド
複素復調位相プロットを作成する Dataplot コマンドは以下の通り。

```
DEMODULATION FREQUENCY <VALUE> 
COMPLEX DEMODULATION PHASE PLOT Y
```

ここで、Y は応答変数である。
DEMODULATION FREQUENCY は、COMPLEX DEMODULATION PLOT の対象とする周波数を指定するために使用する。
復調周波数の値は、通常、スペクトル図から取得する。

[複素復調位相プロットのページに戻る](../section3/eda339.md)

---
  
#### 条件付きプロットの Dataplot コマンド
条件付きプロットを作成する Dataplot コマンドは次の通り。

```
CONDITION PLOT Y X COND
```

Y は応答変数、X は独立変数、そして COND は条件変数である。
Dataplot で COND には離散的な値が個別に含まれていることが想定されている。
Dataplotには、連続変数から離散変数を作成するためのコマンドがいくつか用意されている。
例えば、X2 を 4つの領域に分割したい連続変数だとする。
X2 から離散変数を作成するには、次の一連のコマンドを入力する。

```
LET COND = X2 
LET COND = 1 SUBSET X2 = 0 TO 99.99 
LET COND = 2 SUBSET X2 = 100 TO 199.99 
LET COND = 3 SUBSET X2 = 200 TO 299.99 
LET COND = 4 SUBSET X2 = 300 TO 400  
```

SUBSET 機能は上記のように使用し、任意の範囲を作成する。
より簡単で自動化された方法として、Dataplot の CODE コマンドを使用する方法がある。
例えば、

```
LET COND = CODE4 X2  
```

とすると、データが四分位に分割され、X2 の対応する値がどの四分位にあるかに基づき、COND に 1 から 4 の値が割り当てられる。

プロットの表示は、CHARACTER および LINE コマンドと、それらの各種属性設定コマンドを適切に設定し制御する。

さらに、Dataplot には条件付きプロットの表示を制御するための多数の SET コマンドが用意されている。
詳細については、Dataplot で HELP CONDITION PLOT と入力する。 

[条件付きプロットのページに戻る](../section3/eda33qc.md)  

---

#### 信頼限界と1標本 *t*-検定の Pataplot コマンド
Dataplot では、以下のコマンドを使用し、それぞれ、平均値の信頼区間の計算や1標本*t*-検定を行う。

```
CONFIDENCE LIMITS Y 
T TEST Y U0
```

ここで、Y は応答変数、U0 は仮説値を定義する母数またはスカラー値である。

[平均値の信頼限界のページに戻る](../section3/eda352.md)  

---

#### 等高線図の Dataplot コマンド
等高線図を作成する Dataplot コマンドは次の通り。

```
CONTOUR PLOT Z X Y Z0
```

変数 X および Y はグリッドを定義し、変数 Z は応答変数、Z0 は希望する等高線水準を定義する。
現在、Dataplot は規則的なグリッド上の等高線図のみをサポートしている。
Dataplot は、不規則なデータから規則的なグリッドを形成するための2次元補間機能を提供している。
また、Dataplot は等高線へのラベル表示や、等高線間の塗りつぶしはサポートしていない。

[等高線図のページに戻る](../section3/eda33a.md)  

---

#### 管理図の Dataplot コマンド
管理図を作成する Dataplot コマンドは以下の通り。

```
XBAR CONTROL CHART Y X
R CONTROL CHART Y X
S CONTROL CHART Y X
C CONTROL CHART Y X
U CONTROL CHART Y X
P CONTROL CHART Y X
NP CONTROL CHART Y X
CUSUM CONTROL CHART Y X
EWMA CONTROL CHART Y X
MOVING AVERAGE CONTROL CHART Y
MOVING AVERAGE CONTROL CHART Y X
MOVING RANGE CONTROL CHART Y
MOVING RANGE CONTROL CHART Y X
MOVING SD CONTROL CHART Y
MOVING SD CONTROL CHART Y X
```

ここで、Y は応答変数、X は群識別変数である。 
Dataplot は管理限界を計算する。
場合によっては、管理限界として設定する値をあらかじめ決定していることもある（例：過去のデータに基づく）。
Dataplot では、管理図コマンドの前に以下のコマンドを入力し、これら限界を指定する。

```
LET TARGET = <値> 
LET LSL = <値> 
LET USL = <値> 
```

これらにより、それぞれ目標値、下限仕様値、および上限仕様値を指定する。 

プロットの表示は、LINE および CHARACTER コマンドを適切に設定し制御する。
具体的には、7つの設定がある。

1. 応答曲線
2. Dataplot によって決定された目標値における基準線
3. データプロットで決定された上限仕様限界における基準線
4. Dataplot によって決定された下限仕様限界における基準線
5. 利用者指定の目標値における基準線
6. 利用者が指定した上限仕様限界における基準線
7. 利用者が指定した下限仕様限界における基準線 

[管理図のページに戻る](../../pmc/section3/pmc31.md)  

---

#### DEX 等高線図の Dataplot コマンド
1次 DEX 等高線図を作成する Dataplot コマンドは、以下の通り。

```
DEX CONTOUR PLOT Y X1 X2 Y0
```
変数 X1 および X2 は 2 つの因子変数、Y は応答変数、Y0 は希望する等高線水準を定義する。

Dataplot には、2次 DEX 等高線図の作成機能は組み込まれていない。
ただし、マクロ DEXCONTQ.DP を使用すれば、2次DEX等高線図を作成できる。
詳細については、LIST DEXCONTQ.DP と入力する。

[DEX等高線図のページに戻る](../section3/eda33a1.md)   

---

#### DEX 交互作用効果プロットの Dataplot コマンド
DEX 平均交互作用効果のプロットを作成する Dataplot コマンドは以下の通り。

```
DEX MEAN INTERACTION EFFECTS PLOT Y X1 X2 X3 X4 X5
```

ここで、Y は応答変数であり、X1、X2、X3、X4、および X5 は因子変数である。
因子変数の数は変動可能であるが、少なくとも1つ指定する。 

Dataplot は、その他の位置統計量について、以下の追加プロットをサポートしている。

```
DEX MEDIAN INTERACTION EFFECTS PLOT Y X1 X2 X3 X4 X5
DEX MIDMEAN INTERACTION EFFECTS PLOT Y X1 X2 X3 X4 X5
DEX TRIMMED MEAN INTERACTION EFFECTS PLOT Y X1 X2 X3 X4 X5
DEX WINSORIZED MEAN INTERACTION EFFECTS PLOT Y X1 X2 X3 X4 X5
```

統計量ではなく生データをプロットしたい場合は、以下を入力する。

```
DEX INTERACTION EFFECTS PLOT Y X1 X2 X3 X4 X5
```

LINE および CHARACTER コマンドを使用して、プロットの表示を制御する。
例えば、典型的な一連のコマンドは以下である。

```
LINE SOLID SOLID 
CHARACTER CIRCLE BLANK 
CHARACTER FILL ON 
```

これにより、因子の各水準と全体平均の基準線との間の接続線が実線で描画される。
さらに、各水準の平均値は塗りつぶされた実線の円で描画される。 

このコマンドは、SCATTER PLOT MATRIX コマンドの派生である。
これらのプロットの表示を制御するためのオプションがいくつかある。
Dataplot で詳細を確認するためには HELP SCATTER PLOT MATRIX と入力する。 

[Dex平均プロットへ戻る](../section3/eda33c.md)  

---

#### DEX 平均プロットの Dataplot コマンド
DEX 平均プロットを作成する Dataplot コマンドは次の通り。

```
DEX MEAN PLOT Y X1 X2 X3 X4 X5
```

ここで、Y は応答変数であり、X1、X2、X3、X4、および X5 は因子変数である。
因子変数の数は変動可能であるが、少なくとも1つ指定する。 

Dataplot は、その他の位置統計量について、以下の追加プロットをサポートしている。

```
DEX MEDIAN PLOT Y X1 X2 X3 X4 X5  
DEX MIDMEAN PLOT Y X1 X2 X3 X4 X5 
DEX TRIMMED MEAN PLOT Y X1 X2 X3 X4 X5
DEX WINSORIZED MEAN PLOT Y X1 X2 X3 X4 X5  
```

LINE および CHARACTER コマンドを使用して、プロットの表示を制御する。
例えば、典型的なコマンドの並びは以下の通り。

```
LINE SOLID SOLID 
CHARACTER CIRCLE BLANK 
CHARACTER FILL ON 
```

これにより、因子の各水準と全体平均の基準線との間の接続線が実線で描画される。
さらに、各水準の平均値は、塗りつぶされた円として描画される。 

多くの場合、因子にアルファベットのラベルを付けることが望ましい。
例えば、時間と温度の 2つの因子がある場合、以下のコマンドを使用してアルファベットのラベルを定義する。

```
XLIMITS 1 2 
XTIC OFFSET 0.5 0.5 
MAJOR XTIC MARK NUMBER 2 
MINOR XTIC MARK NUMBER 0 
XTIC MARK LABEL FORMAT ALPHA 
XTIC MARK LABEL CONTENT TIME TEMPERATURE 
```

[Dex平均プロットへ戻る](../section3/eda33c.md)  

---

#### DEX 散布図の Dataplot コマンド
DEX 散布図を作成する Dataplot コマンドは次の通り。

```
DEX SCATTER PLOT Y X1 X2 X3 X4 X5
```

ここで、Y は応答変数であり、X1、X2、X3、X4、および X5 は因子変数である。
因子変数の数は変動可能であるが、少なくとも1つは必要である。

DEX SCATTER PLOT の前には、通常、以下のコマンドを記述する。

```
CHARACTER X BLANK 
LINE BLANK SOLID 
```

ただし、プロットの文字や線の設定は、適切と思われるものに変更可能である。 

多くの場合、因子にアルファベットのラベルを付けることが望ましい。
例えば、時間と温度の2つの因子がある場合、以下のコマンドを使用してアルファベットのラベルを定義する。

```
XLIMITS 1 2 
XTIC OFFSET 0.5 0.5 
MAJOR XTIC MARK NUMBER 2 
MINOR XTIC MARK NUMBER 0 
XTIC MARK LABEL FORMAT ALPHA 
XTIC MARK LABEL CONTENT TIME TEMPERATURE 
```

[Dex散布図のページに戻る](../section3/eda33b.md)  

---

#### DEX標準偏差プロットの Dataplot コマンド
DEX標準偏差のプロットを作成する Dataplot コマンドは以下の通り。

```
DEX STANDARD DEVIATION PLOT Y X1 X2 X3 X4 X5
```

ここで、Y は応答変数であり、X1、X2、X3、X4、および X5 は因子変数である。
因子変数の数は変動可能であるが、少なくとも1つ指定する。 

Dataplot は、その他の尺度統計量について、以下の追加プロットをサポートしている。

```
DEX VARIANCE PLOT Y X1 X2 X3 X4 X5
DEX MEDIAN ABSOLUTE VALUE PLOT Y X1 X2 X3 X4 X5
DEX AVERAGE ABSOLUTE VALUE PLOT Y X1 X2 X3 X4 X5
DEX RANGE VALUE PLOT Y X1 X2 X3 X4 X5
DEX MIDRANGE VALUE PLOT Y X1 X2 X3 X4 X5
DEX MINIMUM PLOT Y X1 X2 X3 X4 X5
DEX MAXIMUM PLOT Y X1 X2 X3 X4 X5 
```

LINE および CHARACTER コマンドを使用して、プロットの表示を制御する。
例えば、典型的なコマンドの並びは以下の通り。

```
LINE SOLID SOLID 
CHARACTER CIRCLE BLANK 
CHARACTER FILL ON 
```

これにより、因子の各水準と全体平均の基準線との間の接続線が実線で描画される。
さらに、各水準の平均値は、塗りつぶされた円として描画される。 

多くの場合、因子にアルファベットのラベルを付けることが望ましいである。
例えば、時間と温度の2つの因子がある場合、以下のコマンドを使用してアルファベットのラベルを定義する。

```
XLIMITS 1 2 
XTIC OFFSET 0.5 0.5 
MAJOR XTIC MARK NUMBER 2 
MINOR XTIC MARK NUMBER 0 
XTIC MARK LABEL FORMAT ALPHA 
XTIC MARK LABEL CONTENT TIME 
TEMPERATURE 
```

[Dex標準偏差プロットのページに戻る](../section3/eda33d.md)

---

#### 二重指数確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、二重指数分布の確率関数を計算する.

```

cdf		LET Y = DEXCDF(X,A,B)
pdf		LET Y = DEXPDF(X,A,B)
ppf		LET Y = DEXPPF(X,A,B)
ハザード		LET Y = DEXHAZ(X,A,B)/(1 - DEXCDF(X,A,B))
累積ハザード	LET Y = -LOG(1 - DEXCHAZ(X,A,B))
生存		LET Y = 1 - DEXCDF(X,A,B)
逆生存		LET Y = DEXPPF(1-X,A,B)
乱数		LET Y = DOUBLE EXPONENTIAL 
				RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	DOUBLE EXPONENTIAL PROBABILITY PLOT Y
最尤法		LET MU = MEDIAN Y
				LET BETA = MEDIAN ABSOLUTE DEVIATION Y
```

ここで、X は数値、母数、または変数にする。
A および B は位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、次の通り。

```
PLOT DEXPDF(X) FOR X = -5 0.01 5 
```

[二重指数分布のページに戻る](../section3/eda366c.md)  

---

#### 2つの比率の差に対する信頼区間の Dataplot コマンド
2つの比率の差に対する信頼区間を求める Dataplot コマンドは、次の通り。

```
DIFFERENCE OF PROPORTIONS CONFIDENCE
INTERVAL Y1 Y2
```

ここで、Y1 には標本1 のデータが、Y2 には標本2 のデータが含まれる。
標本規模が大きい場合、Dataplot は正規近似ではなく二項分布を使用する。 

次のコマンドは、応答変数における成功を定義する下限と上限を設定する。

```
ANOP LIMITS <下限> <上限> 
```

[2つの比率の差のページに戻る](../../prc/section3/prc33.md)  

---

#### Duane プロットの Dataplot コマンド
Duane プロットを作成する Dataplot コマンドは次の通り。

```
DUANE PLOT Y
```

ここで、Y は故障時間を含む応答変数である。

[Duane プロットのページに戻る](../../apr/section2/apr223.md)  

---

#### 有理関数モデルの初期値を設定する Dataplot コマンド
有理関数モデルの初期値は、元のデータの部分集合に正確な有理関数を適合させることで得ることができる。
この部分集合のデータ点数は、有理関数モデルで推定される母数数と一致している必要がある。
EXACT RATIONAL FIT を使用して、この部分集合モデルを適合させ、それによって有理関数モデルの初期値を与える。 
例えば、X および Y のデータに 2次/2次有理関数モデルを適合させるには、次の処理を行う。 

```
LET X2 = DATA 12 17 22 34 56
LET Y2 = DATA 7 9 6 19 23
EXACT 2/2 FIT Y2 X2 Y X
FIT Y = (A0 + A1*X + A2*X**2)/(1 + B1*X + B2*X**2)
```

DATA コマンドは部分集合変数を定義するために使用し、EXACT 2/2 FIT は正確な有理関数を適合させるために使用する。
「2/2」は、分子の次数を2、分母の次数を 2 であることを指定している。
これにより、A0、A1、A2、B1、および B2 の値が得られ、全データ集合に対する有理関数モデルの推定に使用する。 

ブラウザの「戻る」ボタンを推して元のページに戻ってください。

#### 指数確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、指数分布の確率関数を計算する。

```

cdf		LET Y = EXPCDF(X,A,B)
pdf		LET Y = EXPPDF(X,A,B)
ppf		LET Y = EXPPPF(X,A,B)
ハザード		LET Y = EXPHAZ(X,A,B)
累積ハザード	LET Y = EXPCHAZ(X,A,B)
生存		LET Y = 1 - EXPCDF(X,A,B)
逆生存		LET Y = EXPPPF(1-X,A,B)
乱数		LET Y = EXPONENTIAL RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	EXPONENTIAL PROBABILITY PLOT Y

母数推定		データに欠損がない場合は、以下のコマンドを入力する。
				SET CENSORING TYPE NONE  
				EXPONENTIAL MLE Y 
				
				データに固定時刻 t₀ での1型打切りがある場合は、以下のコマンドを入力する。
				LET TEND = 打切時刻 
				SET CENSORING TYPE 1  
				EXPONENTIAL MLE Y X 
				
				データに2型の打切りがある場合は、以下のコマンドを入力する。
				SET CENSORING TYPE 2  
				EXPONENTIAL MLE Y X 
```

Y は応答変数、X は打切変数であり、値が 1 の場合は故障時刻、0 の場合は打切時刻を示す。
点推定値に加え、母数の信頼区間も算出される。 

上記において、X は数値、母数、または変数にする。
A と B は位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A と B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかにする。
 
これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば以下の通り。

```
PLOT EXPPDF(X) FOR X = 0 0.01 4 
```

[指数分布のページに戻る](../section3/eda3667.md)  

---

#### 一般化 ESD 検定の Dataplot コマンド
一般化ESD（Extreme Studentized Deviate）検定の Dataplot コマンドは次の通り。

```
LET NOUTLIER = <値> 
EXTREME STUDENTIZED DEVIATE TEST Y  
```

ここで、Y は応答変数であり、NOUTLIER は検定対象となる外れ値の数の上限を指定する。

[一般化 ESD のページに戻る](../section3/eda35h3.md)  

---

#### 極値分布（I型、Gumbel 分布）の Dataplot コマンド
最小値に基づいてGumbel 分布の形式を指定するには、次のコマンドを入力する。

```
SET MINMAX 1
```

最大値に基づいて Gumbel 分布の形を指定するには、次のコマンドを入力する。

```
SET MINMAX 2
```

以下のコマンドを使用する前に、これらのコマンドのいずれかを入力する必要がある。

Dataplot では、以下のコマンドを使用して、極値 I型分布の確率関数を計算する。 

```
cdf		LET Y = EV1CDF(X,A,B)
pdf		LET Y = EV1PDF(X,A,B)
ppf		LET Y = EV1PPF(X,A,B)
ハザード		LET Y = EV1HAZ(X,A,B)
累積ハザード	LET Y = EV1CHAZ(X,A,B)
生存		LET Y = 1 - EV1CDF(X,A,B)
逆生存		LET Y = EV1PPF(1-X,A,B)
乱数		LET Y = EXTREME VALUE TYPE 1 RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	EXTREME VALUE TYPE 1 PROBABILITY PLOT Y
最尤法		EV1 MLE Y
				これは全標本の点推定値を返す。
				母数の信頼区間はなく、打切りデータは扱えない。

```

上記において、X は数値、母数、または変数にする。
A および B は位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、以下の通り。

```
SET MINMAX 1  
PLOT EV1PDF(X) FOR X = -4 0.01 4 
```

[極値 I型分布のページに戻る](../section3/eda366g.md)

---

#### F分布確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して F分布の確率関数を計算する。

```
cdf		LET Y = FCDF(X,NU1,NU2,A,B)
pdf		LET Y = FPDF(X,NU1,NU2,A,B)
ppf		LET Y = FPPF(X,NU1,NU2,A,B)
乱数		LET NU1 = 値
				LET NU2 = 値
				LET Y = F RANDOM NUMBERS
				FOR I = 1 1 1000
確率プロット	LET NU1 = 値
				LET NU2 = 値
				F PROBABILITY PLOT Y
```

ここで、X は数値、母数、または変数である。NU1 および NU2 は形状母数（＝自由度の数）である。
NU1 および NU2 は数値、母数、または変数である。 
ただし、これらは通常、数値または母数のいずれかである。
A および B は位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、これらは通常、数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、次の通り。

```
PLOT FPDF(X,10,10) FOR X = 0 0.01 5 
```

[F 分布のページに戻る](../section3/eda3665.md)  

---

#### 2標準偏差等式のF検定の Dataplot コマンド
標準偏差2つの等式を検定する F 検定の Datpalot コマンドは、以下の通り。

```
F TEST Y1 Y2
```

ここで、Y1 は標本1 のデータ、Y2 は標本2 のデータである。

[2標準偏差等式の F 検定のページに戻る](../section3/eda359.md)  

---

#### ヒストグラムの Dataplot コマンド
ヒストグラムを作成する Dataplot コマンドは次の通り。

```
HISTOGRAM Y
```

ここで、Y は応答変数である。
ヒストグラムのさまざまな派生を以下のコマンドで作成する。

```
RELATIVE HISTOGRAM Y 
CUMULATIVE HISTOGRAM Y 
RELATIVE CUMULATIVE HISTOGRAM Y 
```

階級幅、最初の階級の開始値、および最後の階級の終了値は、以下のコマンドで指定する。

```
CLASS WIDTH <値> 
CLASS LOWER <値> 
CLASS UPPER <値> 
```

デフォルトでは、Dataplot は階級幅として 0.3\*SD を使用する。
ここで SD はデータの標準偏差である。
階級の下限は標本平均から標本標準偏差の 6 倍を引いた値となる。
同様に、階級の上限は標本平均に標本標準偏差の 6 倍を加えた値になる。 

デフォルトでは、Dataplot は相対ヒストグラムに対して確率正規化を使用する。
相対カウントの合計が 1 になるようにしたい場合は、次のコマンドを入力する。

```
SET RELATIVE HISTOGRAM PERCENT
```

確率の解釈設定をリセットするには、次のコマンドを入力する。

```
SET RELATIVE HISTOGRAM AREA 
```

[ヒストグラムのページに戻る](../section3/eda33e.md)

---

#### 遅延プロットの Dataplot コマンド
遅延プロットを作成する Dataplot コマンドは次の通り。

```
LAG PLOT Y
```

遅延プロットの表示は、LINE および CHARACTER コマンドの適切な設定によって制御する。
これらのコマンドの一般的な設定は以下の通り。

```
LINE BLANK 
CHARACTER X 
```

遅延プロット上のデータ点に対して、自己回帰モデルが推奨される場合に線形近似を行うには、以下のコマンドを入力する。

```
LAG PLOT Y 
LINEAR FIT YPLOT XPLOT  
```

変数 YPLOT および XPLOT は、直近のプロットの座標を格納する内部変数である。

[遅延プロットのページに戻る](../section3/eda33f.md)

---

#### 疲労寿命確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、疲労寿命分布の確率関数を計算する。

```
cdf		LET Y = FLCDF(X,GAMMA,A,B)
pdf		LET Y = FLPDF(X,GAMMA,A,B)
ppf		LET Y = FLPPF(X,GAMMA,A,B)
ハザード		LET Y = FLHAZ(X,GAMMA,A,B)
累積ハザード	LET Y = FLCHAZ(X,GAMMA,A,B)
生存		LET Y = 1 - FLCDF(X,GAMMA,A,B)
逆生存		LET Y = FLPPF(1-X,GAMMA,A,B)
乱数		LET GAMMA = 値
				LET Y = FATIGUE LIFE RANDOM NUMBERS FOR I = 1 1 1000	
確率プロット	LET GAMMA = 値
				FATIGUE LIFE PROBABILITY PLOT Y
ppcc プロット	LET GAMMA = 値
				FATIGUE LIFE PPCC PLOT Y
```

ここで、X は数値、母数、または変数である。FLMA は形状母数であり、必須である。
これは数値、母数、または変数である。
通常は数値または母数である。
A および B は位置母数および尺度母数であり、これらはオプションである（省略された場合は、位置 0 および尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、次式の通り。

```
PLOT FLPDF(X,2) FOR X = 0.01 0.01 10 
```

[疲労寿命分布のページに戻る](../section3/eda366a.md)

---

#### 近似するための Dataplot コマンド
Dataplot では、線形および非線形をコマンドで近似する。 

たとえば、Y 対 X1、X2、および X3 の線形近似を実行するには、次のコマンドを使用する。

```
FIT Y X1 X2 X3
```

Y 対 X の 2次および 3次近似を実行するには、以下のコマンドを使用する。

```
QUADRATIC FIT Y X 
CUBIC FIT Y X  
```

非線形近似は、方程式を入力し実行する。
例えば、

```
FIT Y = A\*(EXP(-B\*X/10) - EXP(-X/10)) 
FIT Y = C/(1+C\*A\*X\*\*B) 
FIT Y = A - B\*X - ATAN(C/(X-D))/3.14159  
```

上記の式には、変数（X および Y）、母数（A、B、C、および D）、および定数（10 および 3.14159）が含まれている。
FIT コマンドは、母数の値を推定する。
推定したくない母数がある場合は、それを定数として、または「^」を付けて入力する。
（例：FIT Y = ^C/(1+^C\*A\*X\*\*B)。
「^」は、母数の値をコマンド内に代入する。 

関数を定義してから、その関数に近似する。
例えば、

```
LET FUNCTION F = C/(1+C\*A\*X\*\*B) 
FIT Y = F 
```

元の場所に戻るには、ブラウザの「戻る」ボタンを押す。

---

#### ガンマ確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用してガンマ分布の確率関数を計算する。

```
cdf		LET Y = GAMCDF(X,GAMMA,A,B)
pdf		LET Y = GAMPDF(X,GAMMA,A,B)
ppf		LET Y = GAMPPF(X,GAMMA,A,B)
ハザード		LET Y = GAMHAZ(X,GAMMA,A,B)
累積ハザード	LET Y = GAMCHAZ(X,GAMMA,A,B)
生存		LET Y = 1 - GAMCDF(X,GAMMA,A,B)
逆生存		LET Y = GAMPPF(1-X,GAMMA,A,B)
乱数		LET GAMMA = 値
				LET Y = Gamma RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	LET GAMMA = 値
				Gamma PROBABILITY PLOT Y
ppcc プロット	LET GAMMA = 値
				Gamma PPCC PLOT Y
最尤		GAMMA MLE Y
				これは全標本の場合の点推定値を返す。母数の信頼区間は処理されず、打切りデータは扱わない。
```

ここで、X は数値、母数、または変数である。
GAMMA は形状母数であり、必須である。
これは数値、母数、または変数である。
通常は数値または母数である。
A および B は位置母数と尺度母数であり、これらはオプションである（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT GAMPDF(X,2) FOR X = 0.01 0.01 10 
```

[ガンマ分布のページに戻る](../section3/eda366b.md)

---

#### Grubbs 検定の Dataplot コマンド
Grubbs 検定を行う Dataplot コマンドは次の通り。

```
GRUBBS <MINIMUM/MAXIMUM> TEST Y
```

ここで、Y は応答変数である。
Dataplot は一度に1つの外れ値を特定する。
MINIMUM または MAXIMUM キーワードは省略可能である。
省略した場合、最も極端な値で処理される（それが最小方向か最大方向かにかかわらず）。

[Grubbs 検定のページに戻る](../section3/eda35h1.md)  

---

#### ハザード・プロットの Dataplot コマンド
ハザード・プロットの Dataplot コマンドは以下の通り。

```
EXPONENTIAL HAZARD PLOT Y X 
NORMAL HAZARD PLOT Y X 
LOGNORMAL HAZARD PLOT Y X 
WEIBULL HAZARD PLOT Y X  
```

ここで、Y は故障時間を含む応答変数であり、X は打切り変数である（0 は故障時間を、1 は打切り時間を表す）。

[ハザード・プロットのページに戻る](../../apr/section2/apr222.md)  

---

#### Kruskal-Wallis 検定の Dataplot コマンド
Kruskal-Wallis 検定の Dataplot コマンドは次の通り。

```
KRUSKAL WALLIS TEST Y X
```

ここで、Y は応答変数、X は群識別変数である。

[Kruskal-Wallis 検定のページに戻る](../../prc/section4/prc4.md)

---

#### Kolmogorov-Smirnov の適合度検定
Kolmogorov-Smirnov の適合度検定を行うDataplotコマンドは、以下の通り。

```
<dist> KOLMOGOROV-SMIRNOV GOODNESS OF FIT TEST Y 
```

ここで、`<dist>` は 60 以上の組み込み分布のいずれかである。
K-S 適合度検定は、CDF（累積分布関数）をサポートするすべての Dataplot 内部の連続分布で利用可能である。
コマンド LIST DISTRIBUTIONS は、Dataplot で現在サポートされている分布を表示する。
具体的な例としては、

```
NORMAL KOLM-SMIR GOODNESS OF FIT Y 
LOGISTIC KOLM-SMIR GOODNESS OF FIT Y 
DOUBLE EXPONENTIAL KOLM-SMIR GOODNESS OF FIT Y 
```
位置および尺度母数は、以下のように入力して指定する。

```
LET KSLOC = 値 
LET KSSCALE = 値 
```

形状母数が必要な分布については、1つ以上の形状母数の値を入力する必要がある場合がある。
例えば、ガンマ分布の形状母数 gamma を指定するには、以下のコマンドを入力する。

```
LET GAMMA = 値
GAMMA KOLMOGOROV-SMIRNOV GOODNESS OF FIT TEST Y
```

K-S 検定の境界値は分布が完全に指定されていることを前提としているため、
K-S 検定の計算に使用するデータと同じデータをこれらの分布母数の推定に使用してはならないことに注意する。 

経験的累積分布関数 (CDF) は、次のコマンドでプロットする。

```
EMPIRICAL CDF PLOT Y 
```

[Kolmogorov-Smirnov 適合度検定のページに戻る](../section3/eda35g.md)  

#### 分布母数の最小二乗推定の Dataplot コマンド
次の例は、Dataplot を使用して、Weibull 分布から生成されたデータの最小二乗推定値を求める方法を示している。

```
. Weibull 分布のデータを生成する
SET MINMAX MIN  
LET GAMMA = 5 
LET Y = WEIBULL RAND NUMB FOR I = 1 1 1000 
. データをビン分けする 
SET RELATIVE HISTOGRAM AREA 
RELATIVE HISTOGRAM Y 
LET ZY = YPLOT 
LET ZX = XPLOT 
RETAIN ZY ZX SUBSET YPLOT > 0 
. 初期値を指定する
LET SHAPE = 3 
LET LOC = MINIMUM Y 
LET SCALE = 1 
. 最小 
二乗法による近似を実行する
FIT ZY = WEIPDF(ZX,SHAPE,LOC,SCALE)  
```

RELATIVE HISTOGRAM は[相対ヒストグラム](../section3/eda33e.md) [^2] を出力する。
SET RELATIVE HISTOGRAM コマンドは、ヒストグラム下の面積が 1 になるように（つまり、積分値が 1 になるように）相対ヒストグラムの作成を指定する。
これは、バーの合計が 1 になるのではなく、相対ヒストグラムを基礎となる密度関数の推定量として機能させる。 
Dataplot は、ヒストグラムの座標を内部変数 XPLOT および YPLOT に保存する。
SUBSET コマンドは、頻度ゼロのクラスを除外する。
その後、FIT コマンドが最小二乗法による近似を行う。 

この一般的な手順は、Dataplot に確率密度関数（pdf）関数が用意されている任意の分布について、最小二乗推定値を計算するために使用する。
最小二乗近似の主な難点は、初期値に非常に敏感になり得ることである。
形状母数を持たない分布の場合、[確率プロット](../section3/eda33m.md)[^2]を使用して位置母数と尺度母数の初期値を決定する。
単一の形状母数を持つ分布の場合、[ppccプロット](../section3/eda33n.md)[^2] を使用して形状母数の初期値を決定し、確率プロットを使用して位置母数と尺度母数の初期値を決定する。 

上記の手法は、非線形最小二乗法による近似機能と、確率密度関数を定義する機能（組み込みまたは利用者定義）を備えたあらゆる統計ソフトウェア・パッケージで
利用可能である。 

[最小二乗推定のページに戻る](../section3/eda3653.md) 

---

#### Levene 検定の Dataplot コマンド
Levene 検定の Dataplot コマンドは次の通り。

```
LEVENE TEST Y X
```

ここで、Y は応答変数、X は群ID変数である。

[Levene 検定のページに戻る](../section3/eda35a.md)

---

#### 線形相関プロットの Dataplot コマンド
線形相関プロットを作成する Dataplot コマンドは次の通り。

```
LINEAR CORRELATION PLOT Y X TAG
```

ここで、Y は応答変数、X は独立変数、TAG は群ID変数である。 

プロットの表示形式は、LINE および CHARACTER コマンドの適切な設定によって制御する。
典型的な設定は以下である。

```
CHARACTER X BLANK 
LINE BLANK SOLID 
```

[線形相関プロットのページの戻る](../section3/eda33g.md)  

---

#### 線形切片プロットの Dataplot コマンド
直線切片プロットを作成する Dataplot コマンドは次の通り。

```
LINEAR INTERCEPT PLOT Y X TAG
```

ここで、Y は応答変数、X は独立変数、TAGは 群ID変数である。 

プロットの表示形式は、LINE および CHARACTER コマンドの適切な設定によって制御する。
典型的な設定は以下である。

```
CHARACTER X BLANK 
LINE BLANK SOLID 
```

[線形切片プロットのページに戻る](../section3/eda33h.md)

---

#### 線形傾きプロットの Dataplot コマンド
線形勾配プロットを作成する Dataplot コマンドは次の通り。

```
LINEAR SLOPE PLOT Y X TAG
```

ここで、Y は応答変数、X は独立変数、TAG は群ID変数である。 

プロットの表示は、LINE および CHARACTER コマンドの適切な設定によって制御する。
典型的な設定は以下である。

```
CHARACTER X BLANK 
LINE BLANK SOLID 
```

[線形傾きプロットのページに戻る](../section3/eda33i.md)  

---

#### 線形残差標準偏差プロットの Dataplot コマンド
線形残差の標準偏差プロットを作成する Dataplot コマンドは次の通り。

```
LINEAR RESSD PLOT Y X TAG
```

ここで、Y は応答変数、X は独立変数、TAG は群ID変数である。 

プロットの表示は、LINE および CHARACTER コマンドの適切な設定によって制御する。
典型的な設定は以下の通り。

```
CHARACTER X BLANK 
LINE BLANK SOLID 
```

[線形残差標準偏差プロットのページに戻る](../section3/eda33j.md) 

---

#### 位置の測定値に対する Dataplot コマンド
Dataplot では、次のようにさまざまな位置の指標を計算する。

```
LET A = MEAN Y 
LET A = MEDIAN Y 
LET A = MIDMEAN Y 
 
LET P1 = 10 
LET P2 = 10 
LET A = TRIMMED MEAN Y 
 
LET P1 = 10 
LET P2 = 10 
LET A = WINSORIZED Y 
```

上記において、P1 および P2 は、刈り込みもしくはウィンザー化される値の割合を設定するために使用する。
P1 を使用して下側の裾の割合を、P2 を使用して上側の裾の割合を設定する。

[位置の尺度のページの戻る](../section3/eda351.md)  

---

#### 対数正規確率関数に関する Dataplot コマンド
Dataplot では、以下のコマンドを使用して対数正規分布の確率関数を計算する。

```
cdf		LET Y = LGNCDF(X,SD,A,B)
pdf		LET Y = LGNPDF(X,SD,A,B)
ppf		LET Y = LGNPPF(X,SD,A,B)
ハザード		LET Y = LGNHAZ(X,SD,A,B)
累積ハザード	LET Y = LGNCHAZ(X,SD,A,B)
生存		LET Y = 1 - LGNCDF(X,SD,A,B)
逆生存		LET Y = LGNPPF(1-X,SD,A,B)
乱数		LET SD = 値
				LET Y = LOGNORMAL RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	LET SD = 値
				LOGNORMAL PPCC PLOT Y
ppcc プロット	LET SD = 値  
母数推定		LOGNORMAL MLE Y
				形状および尺度の母数の点推定値を返す。打切りデータは扱えず、母数の信頼区間は計算されない。
			
```

ここで、X は数値、母数、または変数である。
SD は形状母数であり、省略可能である。
数値、母数、または変数である。
通常は数値または母数である。
A および B は位置母数と尺度母数であり、省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT LGNPDF(X,5) FOR X = 0.01 0.01 5 
```


[対数正規分布のページに戻る](../section3/eda3669.md)  

---

#### 分布の最尤推定の Dataplot コマンド
Dataplot は、以下の表に記載されている特定の分布について、最尤推定を行える。
特に指定がない限り、打切りデータはサポートされておらず、点推定値のみが計算される（つまり、母数の信頼区間は計算されない）。
打切りデータの場合、故障時刻には 1 を、打切時刻には 0 を割り当てる id変数を作成する。
I型 の打切りとは、固定時刻 $`t_0`$ での打切りを指す。
II型 の打切りとは、あらかじめ決められた数の部品が故障した後の打切りを指す。 

##### 正規正規分布
```
NORMAL MAXIMUM LIKELIHOOD Y
```

##### Y指数指数
```
EXPONENTIAL MAXIMUM LIKELIHOOD Y
```

母数に対して信頼区間が計算され、I型およびⅡ型の打切りの両方がサポートされている。 

I型の打切りについては、以下のコマンドを入力する。

```
SET CENSORING TYPE 1
LET TEND = 打切時刻
EXPONENTIAL MAXIMUM LIKELIHOOD Y ID
```

Ⅱ型打切りについては、以下のコマンドを入力する。

```
SET CENSORING TYPE 2 EXPONENTIAL MAXIMUM LIKELIHOOD Y ID 
```

##### Weibull

```
WEIBULL MAXIMUM LIKELIHOOD Y 
```

母数の信頼区間が計算され、Ⅰ型 およびⅡ型 の両方の打切りがサポートされている。 

型 の打切りについては、次のコマンドを入力する。

```
SET CENSORING TYPE 1 
LET TEND = 打切時刻 
WEIBULL MAXIMUM LIKELIHOOD Y ID 
```

II 型打切りについては、以下のコマンドを入力する。

```
SET CENSORING TYPE 2 
WEIBULL MAXIMUM LIKELIHOOD Y ID 
```

##### 対数正規

```
LOGNORMAL MAXIMUM LIKELIHOOD Y 
```

##### 二重指数

```
DOUBLE EXPONENTIAL MAXIMUM LIKELIHOOD Y
```

##### Pareto

```
PARETO MAXIMUM LIKELIHOOD Y
```

##### ガンマ

```
GAMMA MAXIMUM LIKELIHOOD Y
```

##### 逆ガウス

```
INVERSE GAUSSIAN MAXIMUM LIKELIHOOD Y
```

##### Gumbel

```
GUMBEL MAXIMUM LIKELIHOOD Y
```

##### 二項

```
BINOMIAL MAXIMUM LIKELIHOOD Y
```

##### Poisoon

```
POISSON MAXIMUM LIKELIHOOD Y
```

[最尤推定のページに戻る](../section3/eda3652.md)

---  

#### 平均プロットの Dataplot コマンド
平均プロットを作成する Dataplot コマンドは次の通り。

```
MEAN PLOT Y X
```

ここで、Y は応答変数、X は群ID変数である。 

Dataplot は、他にも多くの一般的な位置統計量に対してこのコマンドをサポートしている。
例えば、MEDIAN PLOT Y X や MID-RANGE PLOT Y X は、各群の平均値の代わりに中央値や中点値を計算する。 

[平均値プロットのページに戻る](../section3/eda33k.md)

---

#### 正規確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、正規分布のさまざまな確率関数を計算する。

```
cdf		LET Y = NORCDF(X,A,B)
pdf		LET Y = NORPDF(X,A,B)
ppf		LET Y = NORPPF(X,A,B)
ハザード		LET Y = NORHAZ(X,A,B)
累積ハザード	LET Y = NORCHAZ(X,A,B)
生存		LET Y = 1 - NORCDF(X,A,B)
逆生存		LET Y = NORPPF(1-X,A,B)
乱数		LET Y = NORMAL RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	NORMAL PROBABILITY PLOT Y
母数推定値	LET YSD = STANDARD DEVIATION Y
```

ここで、X は数値、母数、または変数にする。
A および B は位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT NORPDF(X) FOR X = -4 0.01 4 
```

[正規分布のページに戻る](../section3/eda3661.md)

---

#### 正規確率プロットの Dataplot コマンド
正規確率プロットを作成する Dataplot コマンドは次の通り。

```
NORMAL PROBABILITY PLOT Y
```

ここで、Y は応答変数である。 

データがすでに群化されている場合（つまり、Y に X で識別される群ごとの個数が含まれている場合）、Dataplot コマンドは以下になる。

```
NORMAL PROBABILITY PLOT Y X
```

Dataplot は、確率プロットを作成する際に、以下の内部母数を返す。

* PPCC - 確率プロット上の近似直線の相関係数。
これは、直線が確率プロットにどの程度適合しているかを示す指標である。
* PPA0 - 確率プロット上の近似直線の切片項。
これは位置母数の推定値である。
* PPA1 - 確率プロット上の近似直線の傾き項。
これは尺度母数の推定値である。
* SDPPA0 - 確率プロット上の近似直線の切片項の標準偏差。
* SDPPA1 - 確率プロット上の近似直線の傾き項の標準偏差。
* PPRESSD - 確率プロット上の近似直線の残差の標準偏差。
これは、近似直線の適合度の指標である。
* PPRESDF - 確率プロット上の近似直線の残差の自由度。 

[正規確率プロットのページへ戻る](../section3/eda33l.md)  

---

#### 正規分布に従う乱数を生成する Dataplot コマンド
位置 50、尺度 20の正規乱数を 1,000個生成する Dataplot コマンドは、以下の通り。

```
LET LOC = 50 
LET SCALE = 20 
LET Y = NORM RAND NUMBERS FOR I = 1 1 1000 
LET Y = LOC + SCALE\*Y 
```

乱数を自動的に生成するプログラムは、通常、シード（種）によって制御される。
シードは通常、整数値である。
シードの重要性は、乱数を再現できる点にある。
つまり、プログラムに同じシードを与えれば、同じ乱数の列が生成されるはずである。
乱数の集合を再現する能力が重要でない場合は、シードとして任意の有効な値を指定する。
 
Dataplot では、シードは奇数の整数であり、最小値（およびデフォルト値）は 305 である。
305 未満のシードは 305 と同じ列を生成し、偶数は直前の奇数と同じ列を出力する。
Dataplot でシード値を 401 に変更するには、次のコマンドを入力する。

```
SEED 401 
```

[正規乱数の事例研究（背景とデータ）のページに戻る](eda4211.md)

---

#### 偏自己相関プロットの Dataplot コマンド
偏自己相関プロットを作成するコマンドは次の通り。

```
PARTIAL AUTOCORRELATION PLOT Y
```

偏自己相関プロットの表示形式は、LINE、CHARACTER、および SPIKE コマンドを適切に設定し制御する。
Dataplot は、自己相関プロット上に以下の曲線を描画する。

1. 自己相関曲線。  
2. 原点を通る基準線。  
3. 95%信頼限界の上限にある基準線。  
4. 95%信頼限界の下限にある基準線。  
5. 99%信頼限界の上限にある基準線。  
6. 99%信頼限界の下限にある基準線。  

たとえば、偏自己相関をスパイクで、ゼロ基準線を実線で、95%の線を破線で、99%の線を点線で描画するには、次のコマンドを入力する。

```
LINE BLANK SOLID DASH DASH DOT DOT 
CHARACTER BLANK ALL 
SPIKE ON OFF OFF OFF OFF OFF 
SPIKE BASE 0 
```

[偏自己相関プロットのページに戻る](../../pmc/section4/pmc4463.md)

---  

#### Poisson 確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して Poisson 分布の確率関数を計算する。

```
cdf		LET Y = POICDF(X,LAMBDA)
pdf		LET Y = POIPDF(X,LAMBDA)
ppf		LET Y = POIPPF(X,LAMBDA)
乱数		LET Y = POISSON RANDOM 
				NUMBERS FOR I = 1 1 1000
確率プロット	LET LAMBDA = 値 
				POISSON PROBABILITY PLOT Y
ppcc プロット	POISSON PPCC PLOT Y
```

ここで、X は数値、母数、または変数にする。
LAMBDA は形状母数であり、必須である。
数値、母数、または変数にする。
通常は数値または母数である。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT POIPDF(X,15) FOR X = 0 1 50 
```

[Poisson 分布のページに戻る](../section3/eda366j.md)[^3]  

---

#### 冪乗対数正規分布の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、冪乗対数正規分布の確率関数を計算する。

```
cdf		LET Y = PLNCDF(X,P,SD,MU)
pdf		LET Y = PLNPDF(X,P,SD,MU)
ppf		LET Y = PLNPPF(X,P,SD,MU)
ハザード		LET Y = PLNHAZ(X,P,SD,MU)
累積ハザード	LET Y = PLNCHAZ(X,P,SD,MU)
生存		LET Y = 1 - PLNCDF(X,P,SD,MU)
逆生存		LET Y = PLNPPF(1-X,P,SD,MU)
確率プロット	LET P = 値
				LET SD = 値 (defaults to 1)
				POWER LOGNORMAL
				PROBABILITY PLOT Y
PPCCプロット	LET SD = 値
				POWER LOGNORMAL PPCC PLOT Y
```

上記において、X は数値、母数、または変数にする。
SD および MU は、それぞれ尺度母数および位置母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、SD および MU は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、次のコマンド

```
PLOT PLNPDF(X,5,1) FOR X = 0.01 0.01 5 
```

[冪乗対数正規分布のページに戻る](../section3/eda366e.md)

---

#### 冪乗正規確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、力正規分布の確率関数を計算する。

```
cdf		LET Y = PNRCDF(X,P,SD,MU)
pdf		LET Y = PNRPDF(X,P,SD,MU)
ppf		LET Y = PNRPPF(X,P,SD,MU)
ハザード		LET Y = PNRHAZ(X,P,SD,MU)
累積ハザード	LET Y = PNRCHAZ(X,P,SD,MU)
生存		LET Y = 1 - PNRCDF(X,P,SD,MU)
逆生存		LET Y = PNRPPF(1-X,P,SD,MU)
確率プロット	LET P = 値
				LET SD = 値 (defaults to 1)
				POWER NORMAL PROBABILITY PLOT Y
ppccプロット	POWER NORMAL PPCC PLOT Y
```

上記において、X は数値、母数、または変数にする。
SD および MU は、それぞれ尺度母数および位置母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、SD および MU は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT PNRPDF(X,10,1) FOR X = -5 0.01 5 
```

[冪乗正規確率分布のページに戻る](../section3/eda366d.md)

---

#### 確率プロットの Dataplot コマンド
確率プロットの Dataplot コマンドは次の通り。

```
<dist> PROBABILITY PLOT Y  
```

ここで、`<dist>` は特定の分布の名前である。
Dataplot は現在、70 種類以上の分布に対する確率プロットをサポートしている。
例えば、 

```
NORMAL PROBABILITY PLOT Y 
EXPONENTIAL PROBABILITY PLOT Y 
DOUBLE EXPONENTIAL PROBABILITY PLOT Y 
CAUCHY PROBABILITY PLOT Y 
```

分布によっては、1つ以上の[形状母数](../section3/eda363.md)を指定する。
例えば、ガンマ分布の形状母数を指定するには、次のコマンドを入力する。

```
LET GAMMA = 2 
GAMMA PROBABILITY PLOT Y 
```

コマンド LIST DISTRIBUTIONS を入力すると、Dataplot が確率プロットをサポートしている分布のリスト（および指定が必要な母数）を確認できる。 

Dataplot は、確率プロットを作成する際に、以下の内部母数を返す。

* PPCC - 確率プロット上の近似直線の相関係数。
これは、直線が確率プロットにどの程度よく適合しているかを示す指標である。
* PPA0 - 確率プロット上の近似直線の切片項。
これは位置母数の推定値である。
* PPA1 - 確率プロット上の近似直線の傾き。
これは尺度母数の推定値である。
* SDPPA0 - 確率プロット上の近似直線の切片項の標準偏差。
* SDPPA1 - 確率プロット上の近似直線の傾き項の標準偏差。
* PPRESSD - 確率プロット上の近似直線の残差の標準偏差。
これは、回帰直線の適合度の尺度である。
* PPRESDF - 確率プロット上の近似直線の残差の自由度。 

[正規確率プロットのページに戻る](../section3/eda33l.md)

---

#### PPCCプロットの Dataplot コマンド
ビン分けされていないデータのPPCCプロットを作成する Dataplot コマンドは、次の通り。

```
<dist> PPCC PLOT Y
```

ここで、`<dist>` は分布族を指定し、Y は応答変数である。 
ビン分けされたデータに対してPPCCプロットを作成する Dataplot コマンドは次の通り。

```
<dist> PPCC PLOT Y X
```

ここで、`<dist>` は分布族を指定し、Y はカウント変数、X はビン識別変数である。 

Dataplot は 25種類以上の分布についてPPCCプロットをサポートしている。
最も一般的なものには、WEIBULL、TUKEY LAMBDA、GAMMA、PARETO、および INVERSE GAUSSIAN がある。
サポートされている分布の一覧を表示するには、コマンド LIST DISTRIBUTIONS を入力する。 

Dataplot では、形状母数の範囲を指定する。
Dataplot は、形状母数の最小値から最大値まで、等間隔の区間において 50 個の確率プロットを出力する。
例えば、形状母数 γ の値が 2 から 4 までのWeibull  PPCC プロットを作成するには、以下のコマンドを入力する。

```
LET GAMMA1 = 2 
LET GAMMA2 = 4 
WEIBULL PPCC PLOT Y 
```

コマンド LIST DISTRIBUTIONS は、サポートされている分布の形状母数の名前を表示する。
接尾辞の「1」と「2」は、それぞれ形状母数の最小値と最大値である。 

DataplotがPPCCプロットを作成するたびに、以下の内部母数が保存される。

* MAXPPCC - PPCCプロットから得られた最大相関係数。
* SHAPE - 最大相関係数となる形状母数の値。 

[PPCCプロットのページに戻る](../section3/eda33n.md)  

---

#### 不良率信頼区間の Dataplotコマンド
不良率の信頼区間を求める Dataplot コマンドは、次の通り。

```
PROPORTION CONFIDENCE LIMITS Y
```

ここで、Y は応答変数である。
標本規模が大きい場合、Dataplot は正規近似ではなく、正確な二項分布の確率に基づいて信頼区間を計算することに注意する。 

以下のコマンドは、応答変数における「合格」を定義する下限と上限を設定する。

```
ANOP LIMITS <下限> <上限> 
```

[不良率のページに戻る](../../prc/section2/prc22.md)  

---

#### Q-Qプロットの Dataplot コマンド
q-qプロットを作成する Dataplot コマンドは次の通り。

```
QUANTILE-QUANTILE PLOT Y1 Y2
```

CHARACTER および LINE コマンドを使用して、Q-Q プロットの表示を制御する。
例えば、分位点を円、基準線を実線で描画するには、次のコマンドを入力する。

```
LINE BLANK SOLID 
CHARACTER CIRCLE BLANK 
```

[分位数-分位数プロットのページに戻る](../section3/eda33o.md)

---

#### ランダム・ウォーク数を生成する Dataplot コマンド
1,000点のランダム・ウォークを生成するには、以下の Dataplot コマンドを用いる。

```
LET Y = UNIFORM RANDOM NUMBERS FOR I = 1 1 1000
LET Y2 = Y - 0.5
LET RW = CUMULATIVE SUM Y2
```

[ランダム・ウォーク事例研究（背景とデータ）に戻る](eda4231.md)

---

#### 順位和検定の Dataplot コマンド
順位和検定（Wilcoxon 順位和、Mann-Whitney）を行う Dataplot コマンドは以下の通り。

```
RANK SUM TEST Y1 Y2 
RANK SUM TEST Y1 Y2 A  
```

ここで、Y1 には標本1 のデータが、Y2 には標本2 のデータが含まれ、A はスカラー値（数値または母数）である。
Y1 とY2 の観測値の数は同じである必要はない。 

最初の構文は、2つの標本平均が等しいという仮説を検定するために使用する。
2番目の構文は、2つの平均の差が指定された定数に等しいかを検定するために使用する。 

[符号検定のページに戻る](../../prc/section2/prc243.md) 

--- 

#### 実行順序プロットの Dataplot コマンド
実行順序プロットを作成する Dataplot コマンドは次の通り。

```
RUN SEQUENCE PLOT Y
```

同様に、次のように入力することもできる。

```
PLOT Y
```

プロットの表示は、LINE、CHARACTER、SPIKE、BAR コマンドおよびそれらに関連する属性設定コマンドを適切に設定し制御する。

[実行順序プロットのページに戻る](../section3/eda33p.md)

---

#### 連検定の Dataplot コマンド
連検定の Dataplot コマンドは次の通り。

```
RUNS TEST Y
```

ここで、Yは応答変数である。

[連検定のページに戻る](../section3/eda35d.md)  

---

#### 尺度の測定値に対する Dataplot コマンド
Dataplot では、以下のさまざまな尺度指標を次のように計算する。

```
LET A = VARIANCE Y
LET A = STANDARD DEVIATION Y
LET A = AVERAGE ABSOLUTE DEVIATION Y
LET A = MEDIAN ABSOLUTE DEVIATION Y
LET A = RANGE Y

LET A1 = LOWER QUARTILE Y
LET A2 = UPPER QUARTILE Y
LET IQRANGE = A2 - A1
```

[尺度の指標のページに戻る](../section3/eda356.md)  

---

#### 散布図の Dataplot コマンド
散布図を作成する Dataplot コマンドは次の通り。

```
PLOT Y X
```

プロットの表示は、CHARACTER コマンドや LINE コマンド、およびそれらの各種属性設定コマンドを適切に設定し制御する。

[散布図のページに戻る](../section3/eda33q.md)  

---

#### 散布図行列の Dataplot コマンド
散布図行列を作成する Dataplot コマンドは次の通り。

```
SCATTER PLOT MATRIX X1 X2 ... XK
```

プロットの表示は、CHARACTER コマンドや LINE コマンド、およびそれらの各種属性設定コマンドを適切に設定し制御する。

さらに、Dataplot には散布図行列の表示を制御するための多数の SET コマンドが用意されている。最も一般的なコマンドは以下の通り。

* SET MATRIX PLOT LOWER DIAGONAL <ON/OFF>  
このコマンドは、対角線より下のプロットの描画を制御する。
* SET MATRIX PLOT TAG <ON/OFF>  
ONの場合、SCATTER PLOT MATRIX  
コマンドの最後の変数は直接プロットされない。
代わりに、群ID変数として使用する。
CHARACTER および LINE コマンドを使用して、各群のプロット属性を設定する。
* SET MATRIX PLOT FRAME  
<DEFAULT/USER/CONNECTED>  
DEFAULTの場合、プロット枠を結合する（つまり、FRAME CORNER COORDINATES 0 0 100 100 を実行する）。
軸の目盛りとラベルは自動的に制御される。 
CONNECTED の場合、FRAME CORNER COORDINATES の現在の値が使用される点を除き、DEFAULTと同様である。
これは、プロット間にわずかな隙間を設ける場合に便利である（例：散布図行列を生成する前に、FRAME CORNER COORDINATES 3 3 97 97と入力する。）。 
USERの場合、Dataplot はプロット枠を結合しない。
目盛線とラベルは利用者が設定した通りになる。
* SET MATRIX PLOT FIT <NONE/LOWESS/LINEAR/QUADRATIC>  
これは、プロット点の上に LOWESS 近似、線形近似、2次近似線、あるいは近似線の重ね書きを制御する。
LOWESS 近似の場合、LOWESS 割合をかなり高い値に設定することが推奨される（例：LOWESS FRACTION 0.6）。

Dataplotで、このプロットの追加オプションについては、HELP SCATTER PLOT MATRIX と入力する。 

[散布図行列のページに戻る](../section3/eda33qb.md)  

---

#### 季節調整済み部分系列プロットに関する Dataplot コマンド
季節調整済み部分系列のプロットを作成する Dataplot コマンドは以下の通り。

```
LET PERIOD = <値> 
LET START = <値>  
SEASONAL SUBSERIES PLOT Y
```

PERIOD の値は季節周期の長さを定義する。（例：月次データの場合は 12）。
START は、系列がどの群から始まるかを指定する（例：3月から始まる月次データの場合、START を 3 に設定する）。
プロットの表示形式は、CHARACTER および LINE コマンド、ならびにそれらの各種属性設定コマンドを適切に設定し制御する。

[季節部分系列プロットのページに戻る](../../pmc/section4.pmc4431.md)  

---

#### 符号検定の Dataplot コマンド
符号検定を行う Dataplot コマンドは以下の通り。

```
SIGN TEST Y1 A 
SIGN TEST Y1 Y2 
SIGN TEST Y1 Y2 A  
```

ここで、Y1 には標本1 のデータが、Y2 には標本2 のデータが格納され、A はスカラー値（数値または母数）である。
Y1 と Y2 は、同じ観測値の数を持つ必要がある。 

最初の構文は、ある標本の平均が指定された定数に等しいという仮説を検定するために使用する。
2番目の構文は、2つの標本の平均が等しいという仮説を検定するために使用する。
3番目の構文は、2つの平均の差が指定された定数に等しいかを検定するために使用する。 

[符号検定のページに戻る](../../pmc/section2/pmc243.md)

---

#### 符号付き順位検定の Dataplot コマンド
符号付き順位（またはWilcoxon 符号付き順位）検定の Dataplot コマンドは以下の通り。

```
SIGNED RANK TEST Y1 A 
SIGNED RANK TEST Y1 Y2 
SIGNED RANK TEST Y1 Y2 A  
```

ここで、Y1 には標本1 のデータが、Y2 には標本2 のデータが含まれ、A はスカラー値（数値または母数）である。
Y1 と Y2 は、同じ観測値数を持つ必要がある。 

最初の構文は、ある標本の平均が指定された定数に等しいという仮説を検定するために使用する。
2番目の構文は、2つの標本の平均が等しいという仮説を検定するために使用する。
3番目の構文は、2つの平均の差が指定された定数に等しいかを検定するために使用する。 

[符号付き順位検定のページに戻る](../../pmc/section2/pmc243.md)

---

#### 歪度と尖度の Dataplot コマンド
歪度と尖度に関する Dataplot コマンドは以下の通り。

```
LET A = SKEWNESS Y 
LET A = KURTOSIS Y
```

ここで、Y は応答変数である。
Dataplot では、以下のコマンドを使用して、群化されたデータや単因子データに対する歪度および尖度のプロットを作成する。

```
SKEWNESS PLOT Y X 
KURTOSIS PLOT Y X 
```

ここで、Y は応答変数、X は群ID変数である。

[歪度と尖度のページに戻る](../section3/eda35b.md)

---

#### スペクトル図の Dataplot コマンド
スペクトル図を作成する Dataplot コマンドは次の通り。

```
SPECTRAL PLOT Y
```

[スペクトル図のページに戻る](../section3/eda33r.md)

---

#### 標準偏差プロットの Dataplot コマンド
標準偏差のプロットを作成する Dataplot コマンドは次の通り。

```
STANDARD DEVIATION PLOT Y X
```

ここで、Y は応答変数、X は群ID変数である。 
Dataplot は、他にも多くの一般的な尺度統計量に対してこのコマンドをサポートしている。
例えば、AAD PLOT Y X や MAD PLOT Y X は、各群の標準偏差の代わりに、それぞれ平均絶対偏差と中央絶対偏差を計算する。 

[標準偏差プロットのページに戻る](../section3/eda33s.md)

---

#### 星図の Dataplot コマンド
星図を作成する Dataplot コマンドは次の通り。

```
STAR PLOT X1 TO XP FOR I = 10 1 10
```

ここで、X1、X2、...、XP という *p* *個の*応答変数がある。
この構文では、1 つの星図、具体的には X1、X2、...、XP 変数の 10 行目がプロットされることに注意する。

通常、複数の星図が同じページに表示される。
例えば、最初の 25 行を同じページにプロットするには、次のコマンド列を入力する。

```
MULTIPLOT CORNER COORDINATES 0 0 100 100 
MULTIPLOT 5 5  
LOOP FOR K = 1 1 25 
  STAR PLOT X1 TO XP FOR I = K 1 K  
END OF LOOP 
```

[星図のページに戻る](../section3/eda33t.md)

---

#### 要約統計量の表を出力する Dataplot コマンド
要約統計量の表を出力する Dataplot コマンドは次の通り。

```
SUMMARY Y
```

ここで、Y は応答変数である。

[正規乱数事例研究（定量出力）のページに戻る](eda4213.md)

---

#### *t* 確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して*t* 分布の確率関数を計算する。

```
cdf		LET Y = TCDF(X,NU,A,B)
pdf		LET Y = TPDF(X,NU,A,B)
ppf		LET Y = TPPF(X,NU,A,B)
乱数		LET NU = 値
				LET Y = T RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	LET NU = 値
				T PROBABILITY PLOT Y
ppcc プロット	LET NU = 値
				T PPCC PLOT Y
```
上記において、X は数値、母数、または変数である。
NU は形状母数（＝自由度の数）である。
NU は数値、母数、または変数である。 
ただし、通常は数値または母数のいずれかである。
A と B はそれぞれ位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A と B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT TPDF(X) FOR X = -4 0.01 4 
```

[T 分布のページに戻る](../section3/eda3664.md)

---



#### Tietjen-Moore 検定の Dataplot コマンド
Tietjen-Moore 検定の Dataplot コマンドは次の通り。

```
LET NOUTLIER = <値> 
TIETJEN-MOORE <MINIMUM/MAXIMUM> TEST Y  
```

ここで、Y は応答変数であり、NOUTLIER は検査対象となる外れ値の数を指定する。
MINIMUM または MAXIMUM キーワードは省略可能である。
省略された場合、最小値側と最大値側の両方向で外れ値を確認する。

[Tietjen-Moore のページに戻る](../section3/eda35h2.md)  

---


#### 許容範囲の Dataplotコマンド
許容範囲を示す Dataplot コマンドは次の通り。

```
TOLERANCE Y
```

ここで、Y は応答変数である。
正規およびノンパラメトリックの許容区間を表示する。

[許容区間のページに戻る](../../prc/section2/prc242.md)

---

#### 二標本 *t*-検定の Dataplot コマンド
二標本 *t*-検定を実行する Dataplot コマンドは次の通り。

```
T TEST Y1 Y2
```

ここで、Y1 には標本1 のデータを Y2 には標本2 のデータを入力する。
Y1 と Y2 の観測値の数は同じである必要はない。

[二標本 *t*-検定のページに戻る](../section3/eda353.md)  

---

#### Tukey-Lambda 確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、Tukey-Lambda分布の確率関数を計算する。

```
cdf		LET Y = LAMCDF(X,LAMBDA,A,B)
pdf		LET Y = LAMPDF(X,LAMBDA,A,B)
ppf		LET Y = LAMPPF(X,LAMBDA,A,B)
乱数		LET LAMBDA = 値
				LET Y = TUKEY-LAMBDA RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	LET LAMBDA = 値
				TUKEY-LAMBDA PROBABILITY PLOT Y
ppcc プロット	TUKEY-LAMBDA PPCC PLOT Y
```
上記において、X は数値、母数、または変数にする。
LAMBDA は形状母数であり、必須である。
これは数値、母数、または変数にする。
通常は数値または母数である。
A および B はそれぞれ位置母数と尺度母数であり、これらは省略可能である（省略された場合は、位置 0、尺度 1 が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT LAMPDF(X,0.14) FOR X = -5 0.01 5 
```

[Tukey-Lambda 分布のページに戻る](../section3/eda366f.md)

---

#### 一様確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、一様分布の確率関数を計算する。

```

cdf		LET Y = UNICDF(X,A,B)
pdf		LET Y = UNIPDF(X,A,B)
ppf		LET Y = UNIPPF(X,A,B)
ハザード		LET Y = UNIHAZ(X,A,B)
累積 ハザード	LET Y = UNICHAZ(X,A,B)
生存		LET Y = 1 - UNICDF(X,A,B)
逆生存		LET Y = UNIPPF(1-X,A,B)
乱数		LET Y = UNIFORM RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	UNIFORM PROBABILITY PLOT Y
母数推定		モーメント推定量の方法は、以下のコマンドを入力する。
				LET YMEAN = MEAN Y
				LET YSD = STANDARD DEVIATION Y
				LET A = YMEAN - SQRT(3)*YSD
				LET B = YMEAN + SQRT(3)*YSD
				
				最尤推定量は、以下のコマンドを入力する。
				LET YRANGE = RANGE Y
				LET YMIDRANG = MID-RANGE Y
				LET A = YMIDRANG - 0.5*YRANGE
				LET B = YMIDRANG + 0.5*YRANGE
```

上記において、X は数値、母数、または変数である。
A および B は一様分布の下限および上限であり、これらは省略可能である（省略された場合、A は 0、B は 1 である）。
位置母数は A、尺度母数は (B - A) である。
指定する場合、A と B は数値、母数、または変数である。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。
例えば、

```
PLOT UNIPDF(X) FOR X = 0 0.1 1 
```

[一様分布のページに戻る](../section3/eda3662.md)

---

#### 一様乱数を生成する Dataplot コマンド
区間 (-100,100) 内で 1,000 個の一様乱数を生成する Dataplot コマンドは、以下の通り。

```
LET A = -100 
LET B = 100 
LET Y = UNIFORM RANDOM NUMBERS FOR I = 1 1 1000 
LET Y = A + (B-A)\*Y 
```

同様の技法は、標準的な一様乱数を生成できるあらゆるパッケージで使用できる。
単に尺度値（上限値から下限値を引いた値）を乗算し、位置値を足すだけである。 

乱数を自動的に生成するプログラムは、通常、シード（通常は整数値）によって制御する。
シードの重要性は、乱数を再現可能にする点にある。
つまり、プログラムに同じシードを与えれば、同じ乱数の列が生成されるはずである。
乱数のセットを再現する能力が重要でない場合は、シードとして任意の有効な値を指定する。 

Dataplot では、シードは奇数の整数であり、最小値（およびデフォルト値）は 305 である。
305未満のシードは305と同じ列を生成し、偶数は直前の奇数と同じ列を出力する。
Dataplotでシード値を401に変更するには、次のコマンドを入力する。

```
SEED 401 
```

[一様乱数の事例研究（背景とデータ）のページに戻る](../section4/eda4221.md)  

---

#### Weibull 確率関数の Dataplot コマンド
Dataplot では、以下のコマンドを使用して、Weibull 分布の確率関数を計算する。

```

cdf		LET Y = WEICDF(X,GAMMA,A,B)
pdf		LET Y = WEIPDF(X,GAMMA,A,B)
ppf		LET Y = WEIPPF(X,GAMMA,A,B)
ハザード		LET Y = WEIHAZ(X,GAMMA,A,B)
累積ハザード	LET Y = WEICHAZ(X,GAMMA,A,B)
生存		LET Y = 1 - WEICDF(X,GAMMA,A,B)
逆生存		LET Y = WEIPPF(1-X,GAMMA,A,B)
乱数		LET GAMMA = 値
				LET Y = WEIBULL RANDOM NUMBERS FOR I = 1 1 1000
確率プロット	LET GAMMA = 値
				WEIBULL PROBABILITY PLOT Y
ppcc プロット	LET GAMMA = 値
				WEIBULL PPCC PLOT Y
母数推定		データに打切りがない場合は、以下のコマンドを入力する。
				SET CENSORING TYPE NONE  
				WEIBULL MLE Y 
				データに固定時刻 t0での1型 打切りがある場合は、以下のコマンドを入力する。
				
				LET TEND = 打切時刻 
				SET CENSORING TYPE 1  
				WEIBULL MLE Y X 
				
				データに2型の打切りがある場合は、以下のコマンドを入力する。
				SET CENSORING TYPE 2  
				WEIBULL MLE Y X 
				
				Y は応答変数、X は打切り変数である。
				ここで、値1 は故障時刻を、値0 は打切時刻である。
				点推定値に加え、母数の信頼区間も計算される。 
```

上記において、Xは数値、母数、または変数にする。
GAMMA は形状母数であり、必須である。
これは数値、母数、または変数にする。
通常は数値または母数である。A と B はそれぞれ位置母数と尺度母数であり、これらはオプションである（省略された場合は、位置0、尺度1が使用される）。
指定する場合、A および B は数値、母数、または変数にする。
ただし、通常は数値または母数のいずれかである。 

これらの関数は、Dataplot の PLOT および FIT コマンドでも使用できる。例えば、

```
PLOT WEIPDF(X,2) FOR X = 0.01 0.01 5 
```

[Weibull 分布のページに戻る](../section3/eda3668.md)

---



#### Weibull プロットの Dataplotコマンド
Weibull 分布のプロットを作成する Dataplot コマンドは以下の通り。

```
WEIBULL PLOT Y 
WEIBULL PLOT Y X
```

ここで、Y は故障時間を含む応答変数であり、X はオプションの打切り変数である。
値が 1 の場合は、対象の故障モードによってアイテムが故障したことを示し、値が 0 の場合は、対象外の故障モードによってアイテムが故障したことを示す。 

プロットの表示は、LINE および CHARACTER コマンドの適切な設定によって制御する。
例えば、生データを「X」文字で表すと、2本の基準線を破線として描画するには、以下のコマンドを入力する。

```
LINE BLANK DASH DASH 
CHARACTER X BLANK BLANK 
WEIBULL PLOT Y X 
```

Dataplot は、Weibull プロットの実行後に以下の内部母数を保存する。

ETA - 推定特性寿命  
BETA - 推定形状母数  
SDETA - ETAの推定標準  
SDBETA - BETAの推定標準  
BPT1 - 0.1%故障点推定時刻  
BPT5 - 0.5%故障点推定時刻  
B1 - 1%故障点推定時刻  
B5 - 5%故障点推定時刻  
B10 - 10%故障点推定時刻  
B20 - 20%故障点推定時刻  
B50 - 50%故障点推定時刻  
B80 - 80%故障点推定時刻  
B90 - 90%故障点推定時刻  
B95 - 95%故障点推定時刻  
B99 - 99%故障点推定時刻  
B995 - 99.5%故障点推定時刻  
B999 - 99.9%故障点推定時刻  

[Weibull プロットのページに戻る](../section3/eda33u.md)  

---

#### Wilk-Shapiro 正規性検定の Dataplot コマンド
Wilk-Shapiro の正規性検定を行う Dataplot コマンドは次の通り。

```
WILK SHAPIRO TEST Y
```

ここで、Yは応答変数である。 

有意値は、データ点が 5,000点未満の場合にのみ有効である。 

[Wilk-Shapiro のページに戻る](../../prc/section2/prc213.md)

---

#### Yates の処理手順の Dataplot コマンド
Yates 分析を行う Dataplot コマンドは次の通り。

```
YATES Y
```

ここで、Y はYates 順序の応答変数である。

[Yates 分析のページに戻る](../section3/eda35i.md)

---

#### Youden プロットの Dataplot コマンド
Youden プロットを作成する Dataplot コマンドは次の通り。

```
YOUDEN PLOT Y1 Y2 LAB
```

ここで、Y1 と Y2 は応答変数であり、LAB は試験所（または実行番号）の識別子である。
LINE および CHARACTER コマンドを使用して、Youden プロットの表示を制御する。
例えば、実験室が 5 つある場合、典型的なコマンドの並びは以下になる。

```
LINE BLANK ALL 
CHARACTER 1 2 3 4 5 
YOUDEN PLOT Y X LAB  
```

[Youden プロットのページに戻る](../section3/eda33v.md)

---

#### 4-プロットの Dataplot コマンド
4-plotを作成する Dataplot コマンドは次の通り。

```
4-PLOT Y
```

ここで、Y は応答変数である。

[4-プロットのページに戻る](../section3/eda33w.md)

---


#### 6-Plotの Dataplot コマンド
6-プロットを作成する Dataplot コマンドは以下の通り。

```
FIT Y X 
6-PLOT Y X
```

ここで、Y は応答変数、X は独立変数である。

[6-プロットのページに戻る](../section3/eda33x.md)


---
#### 訳註：
* 原典リンクの間違いと思われるもの。

[^1]: 原点では二項分布ではなくベータ分布のリンクになっている。(2026-04-30)  
[^2]: リンクURLセクション指定の間違い。本来は、"/eda/section3/xxx"が "/eda/section4/xxx" になっている。 (2026-04-30)  
[^3]: 原典のリンク先は、Poisson分布ではなく、二項分布になっている。(2026-05-01)  
