[原文 (Original English)](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc45.htm)  
閲覧(UTC)：2026-10-17 02:19:34  
[⬅️](pmc44a.md)[➡️](pmc451.md)  

6. [工程や製品の監視と管理](../pmc.md)  

---
# 多変量時系列モデル

#### 各時系列の観測値が数値ベクトルである場合のBox-Jenkinsモデル 多変量形式を用いたモデル化
Box-Jenkinsの単変量モデルの多変量形式は、ARMAVモデルと呼ばれることがある。
これは、自己回帰移動平均ベクトルの略称であり、単にベクトルARMA過程とも呼ばれる。

平均ベクトルがゼロである定常多変量時系列に対するARMAVモデルは次式で表される。

$$ x_t = (x_{1t},  x_{2t},  \ldots,  x_{nt})^T,  -\infty < t < \infty $$

形は次式となる。

$$ \begin{eqnarray}
x_t & = & \phi_1 x_{t-1} + \phi_2 x_{t-2} + \cdots + \phi_p x_{t-p} + \\
& & a_t - \theta_1 a_{t-1} - \theta_2 a_{t-2} - \cdots - \theta_q a_{t-q}  ,
\end{eqnarray} $$

ここで
* $`x_t`$ および $`a_t`$ は $` n \times 1`$ の列ベクトルであり、$`a_t`$ は多変量白色雑音を表し、 
* $`\phi_k = \{\phi_{k.jj}\}, k = 1,  2, \ldots, p`$<br>
$`\theta_k = \{\theta_{k.jj}\},  k = 1,  2,  \ldots,  q`$<br>
は、自己回帰および移動平均母数を表す $`n \times n`$ の行列であり、 
* $`E[a_t]=0`$
* $`E[a_t a_{t-k}'] = 0,  k \ne 0`$<br>
$`E[a_t a_{t-k}'] = \Sigma_a,  k = 0`$<br>
ここで、$`\Sigma_a`$ は $`a_t`$ の分散行列または共分散行列である。

例として、$`n=2`$、$`p=2`$、$`q=1`$ の二変量時系列の場合、ARMAV(2,1) モデルは以下となる。

$$ \begin{eqnarray} \left( \begin{array}{c} x_{1t} \\ x_{2t} \end{array} \right) & = & \left( \begin{array}{cc} \phi_{1.11} & \phi_{1.12} \\ \phi_{1.21} & \phi_{1.22} \end{array} \right) \left( \begin{array}{c} x_{1t-1} \\ x_{2t-1} \end{array} \right) +\left( \begin{array}{cc} \phi_{2.11} & \phi_{2.12} \\ \phi_{2.21} & \phi_{2.22} \end{array} \right) \left( \begin{array}{c} x_{1t-2} \\ x_{2t-2} \end{array} \right) + \\& & \left( \begin{array}{c} a_{1t} \\ a_{2t} \end{array} \right) - \left( \begin{array}{cc} \phi_{1.11} & \phi_{1.12} \\ \phi_{1.21} & \phi_{1.22} \end{array} \right) \left( \begin{array}{c} a_{1t-1} \\ a_{2t-1} \end{array} \right)\end{eqnarray} $$

ここで、

$$ a_t = \left( \begin{array}{c} a_{1t} \\ a_{2t} \end{array} \right)  .$$ 

#### 推定が難しい係数と共分散行列
行列係数および[共分散行列](../section5/pmc541.md#Mean%20vector%20and%20Covariance)の推定は複雑であり、コンピュータ・ソフトウェアなしでは非常に困難である。
特に、移動平均行列の推定は極めて骨の折れる作業となる。
もし移動平均（MA）成分を無視すれば、次のように表されるARVモデルが残る。

$$ x_{t} = \phi_{1}x_{t-1} + \phi_{2}x_{t-2} + \ldots + \phi_{p}x_{t-p} + a_{t}  , $$

ここで
* $`x_t`$ は観測値のベクトルであり、時刻 $`t`$ における $`x_{1t}, x_{2t}, \ldots, x_{nt}`$ を表し、   
* $`a_t`$ は白色雑音のベクトルであり、時刻 $`t`$ における $`a_{1t},  a_{2t},  \ldots,  a_{nt}`$ を表し、     
* $`\phi_k = \{\phi_{k.jj}\},  k = 1, 2, \ldots, p`$ は自己回帰母数の $`n \times n`$ 行列であり、 
* $`E[a_t] = 0`$  
* $`E[a_t a_{t-k}'] = 0, k \ne 0`$ <br>
$`E[a_t a_{t-k}'] = \Sigma_a,  k = 0`$ <br>
ここで、$`\Sigma_a`$ は分散行列または共分散行列である。

*p* 個の自己回帰行列母数を持つモデルは、ARV(*p*)モデルまたはベクトルARモデルと呼ばれる。

係数行列は多変量最小二乗法によって推定できるが、最尤推定法などの他の手法もある。 

#### 係数行列の興味深い性質
*φ* や AR係数行列には、いくつかの興味深い性質がある。
$`n=1`$、$`p=2`$、$`q=0`$ である 2変量時系列について、次の例を考える。
ARMAV(2,0) モデルは次式になる。

$$ \left( \begin{array}{c} x_{t} \\ y_{t} \end{array} \right) =\left( \begin{array}{cc} \phi_{1.11} & \phi_{1.12} \\\phi_{1.21} & \phi_{1.22} \end{array} \right) \left( \begin{array}{c} x_{t-1} \\y_{t-1} \end{array} \right) + \left( \begin{array}{cc} \phi_{2.11} & \phi_{2.12} \\\phi_{2.21} & \phi_{2.22} \end{array} \right) \left( \begin{array}{c} x_{t-2} \\y_{t-2} \end{array} \right) + \left( \begin{array}{c} a_{1t} \\ a_{2t} \end{array} \right)  .$$

一般性を失うことなく、*X* 系列が入力、*Y* 系列が出力であり、平均ベクトルが (0,0) であると仮定する。

したがって、観測値からそれぞれの平均を引くことで変換を行う。 

#### φ行列の対角要素  

<u>各 *Φ*行列の対角要素は、各系列に対するスカラー推定値であり、この場合は次となる</u>。

　入力系列 *X* に対する $`\phi_{1.11},  \phi_{2.11}`$
 
　出力系列 *Y* に対する $`\phi_{1.22},  \phi_{2.22}`$

#### 伝達機構

<u>対角線下の要素は、入力が出力に及ぼす影響を表している</u>。

これは、11章でBoxとJenkinsが論じた「伝達」機構、あるいは伝達関数モデルと呼ばれるものである。
ここでの$`\phi`$ 項は、彼らの $`\delta`$ 項に対応する。

<u>対角線外の上側の項は、出力が入力に及ぼす影響を表している</u>。 

#### フィードバック

これは「フィードバック」と呼ばれます。
フィードバックの存在は、残差の相関行列における係数の値が高いこととしても見ることができる。
フィードバックが存在しない場合、「真の」伝達モデルが存在する。

これは、行列形式をスカラー形式で表すことで確認できる。

$ \begin{eqnarray}
x_t & = & \phi_{1.11}x_{t-1} + \phi_{2.11}x_{t-2} +\phi_{1.12}y_{t-1} + \phi_{2.12}y_{t-2} + a_{1t} \\
& & \\
y_t & = & \phi_{1.22}y_{t-1} + \phi_{2.22}y_{t-2} +\phi_{1.21}x_{t-1} + \phi_{2.21}x_{t-2} + a_{2t}
\end{eqnarray} $$ 

#### 遅延
<u>最後に、遅延または「デッド」タイムは、下側の対角線外の要素を再度調べることで測定できる</u>。

例えば、$`\phi_{1.21}`$が有意でない場合、遅延は1周期となる。 
