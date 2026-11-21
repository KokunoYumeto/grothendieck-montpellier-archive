# A positive formula on an unbounded-order wall chamber

## T-054. Every order in the chamber \(b\ge3k-2\)

Let \(k\ge3\), \(x,b,d\ge0\),
\(b\ge3k-2\), and \(2b+x\ge5k\). Set
\[
\begin{aligned}
n&=d+b+x-k,\\
\lambda&=(d+3b+2x-5k,d+b+x,d+b+x,d+x,d).
\end{aligned}
\tag{VW.1}
\]
For every \(\mu\vdash5\), the coefficient
\(p_{\mu,(n)}^\lambda\) has the explicit positive formula
(VW.14). It uses at most 46 bounded integer polytopes, each with
at most nine variables, after selecting three residues modulo60.
The fixed phase polynomials and every rational inequality proving
positivity are given in the accompanying finite certificate.
There is no input-dependent representation or elimination oracle.

This chamber permits every \(x\ge0\) and unbounded \(k\).
Its complete support is the thirteen effective-label exceptions
in §6, together with the declared determinant parity. No historical
novelty claim is made for the coefficient family or its ingredients.

Write
\[
a=b+x,\qquad X=x,\qquad B=b-3k+2,\qquad K=k-3.
\tag{VW.2}
\]
Thus \(X,B,K\ge0\). The partition condition is
\(K+2B+X\ge1\): the sole excluded parameter is
\((X,B,K)=(0,0,0)\). A formal zero value at that point is
proved below and is retained in the fixed Newton constants.

## 1. The actual restriction complex and its two surviving terms

Let \(E=\mathfrak h_5\), \(F=\mathbf Q^2\), and
\(J_k=\bigcap_{i=1}^5(\ell_i\otimes F)^k\).
T-049's all-degree substitution, the rank-adaptive Cauchy map,
and the balanced flag chart give the actual module
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}\otimes M_{a,b,k},
\qquad
M_{a,b,k}=\operatorname{Hom}_{GL(F)}
(S_{(a,b)}F,(J_k)_{a+b}).
\tag{VW.3}
\]
The quotient substitution sends the \(i\)-th independent
block to \(\ell_i\otimes F\); its inverse balanced chart
is \(u^{-k}F(v(X))\). G-027's normal-order calculation is
the polynomial extension criterion. The determinant in (VW.3)
is \(\lambda_2=d+a\), so its finite character is retained.

Put \(T_k(V)=\bigoplus_{t=0}^{k-1}\operatorname{Sym}^tV\).
The selected-subset term of G-027 for a subset of size \(s\)
is Cauchy extraction from
\(T_k(F)^{\otimes s}\otimes
\operatorname{Sym}(\mathfrak h_{5-s}\otimes F)\),
with the actual orientation line of that subset. Its differential
is the signed polynomial quotient map. Since \(a+b\ge5k\),
the cited complex is exact in this degree.

All terms with \(s\ge4\) vanish: four independent blocks
truncated below \(k\) have total degree at most \(4(k-1)\).
For \(s=3\), the complementary standard space is a line.
The skew Schur factor can be nonzero only when
\((a,b)/\rho\) is a horizontal strip, which requires
\(\rho_1\ge b\). The normal factors have
\(\rho_1\le|\rho|\le3(k-1)<b\). Hence that entire
module vanishes as well. We obtain the actual exact sequence
\[
0\longrightarrow M_{a,b,k}\longrightarrow
S_{(a,b)}E\longrightarrow C_1\longrightarrow C_2
\longrightarrow0.
\tag{VW.4}
\]
The maps are the specified restriction maps followed by rational
Young idempotents; the following identifications describe their
source and target modules explicitly.

### 1.1. Singleton module and the exact straightening cancellation

Pieri extraction from \(\operatorname{Sym}^{i+j}F\)
removes a horizontal strip from \((a,b)\). Thus
\[
C_1=\operatorname{Ind}_{S_4}^{S_5}
\bigoplus_{\substack{i,j\ge0\\i+j<k\\i\le x}}
S_{(a-i,b-j)}\mathfrak h_4.
\tag{VW.5}
\]
The conditions \(i\le x\) and \(j\le b\) are exactly
the interlacing conditions; the latter is automatic from
\(b\ge3k-2\) and \(i+j<k\). Each Pieri map is the
column inclusion and Schur projection of the Cauchy tensor.
This gives the displayed direct sum as an actual module.

For its character computation only, the restriction \(i\le x\)
can be dropped by an explicit involution. Use the two-row
Jacobi--Trudi expression
\(s_{(u,v)}=h_uh_v-h_{u+1}h_{v-1}\) also for unordered
integer pairs. Every pair with \(i>x\) is matched with
\[
(i',j')=(x+j+1,i-x-1).
\tag{VW.6}
\]
Both new entries are nonnegative, \(i'>x\), and
\(i'+j'=i+j<k\). Their two shapes are
\((a-i,b-j)\) and \((b-j-1,a-i+1)\), whose
Jacobi--Trudi determinants are negatives of one another.
The fixed points have determinant zero. Thus every additional
term cancels, and the full triangular determinant sum has exactly
the trace of (VW.5). All complete-function indices used in that
sum are nonnegative: the smallest is
\(b-j-1\ge2k-2\). This proves the enlargement to every
\(x\ge0\), including its boundary, by the stated map and
straightening relation.

### 1.2. Pair module, its dual comparison, and its finite action

For a pair let \(W=\mathfrak h_3\) be the complementary
two-dimensional standard representation. A normal Schur shape
\(\rho=(p,q)\) has \(p\le2(k-1)<b\). The exact
rank-two skew comparison is
\[
S_{(a,b)/(p,q)}W
\simeq (\det W)^b\otimes\operatorname{Sym}^xW
\otimes S_{(p,q)}W^*.
\tag{VW.7}
\]
Here is the actual representation comparison. In the two-row
Littlewood--Richardson extraction, use the perfect exterior
pairing for \(S_{(p,q)}W\) and its dual. Since
\(S_{(p,q)}W^*=(\det W)^{-p}\operatorname{Sym}^{p-q}W\),
the right side is
\((\det W)^{b-p}\operatorname{Sym}^xW
\otimes\operatorname{Sym}^{p-q}W\), a polynomial module.
The binary Clebsch--Gordan projections, given by contraction
with the alternating form and multiplication of the remaining
symmetric slots, identify its distinct irreducible summands with
the same Littlewood--Richardson column maps on the left. Each
map is nonzero on its highest column tensor and is normalized
there. The multiplicity-one binary decomposition makes their
direct sum a perfect isomorphism. Equivalently, expanding the
two-row determinant on two variables gives its character
\((uv)^{b-p}h_x(u,v)h_{p-q}(u,v)\); the preceding
column maps specify the isomorphism behind that equality.

Decompose \(T_k(F)^{\otimes2}\) by its Cauchy Young
projectors and apply (VW.7) to every summand. The same
projectors reconstruct \(T_k(W^*)^{\otimes2}\), with the
literal interchange of its two factors. Thus
\[
C_2\simeq\operatorname{Ind}_{S_2\times S_3}^{S_5}
\left(\operatorname{sgn}_2\otimes(\det W)^b
\otimes\operatorname{Sym}^xW\otimes T_k(W^*)^{\otimes2}\right).
\tag{VW.8}
\]
The first sign is the orientation line in (VW.4). The rational
dot product on the standard \(S_3\)-space identifies
\(W^*\) with \(W\) when computing its finite-group
traces. That comparison is equivariant and preserves the two
tensor-factor permutations.

The skew determinant and its containment convention were read
in the primary text: Macdonald, *Symmetric Functions and Hall
Polynomials*, second edition, Chapter I §5, (5.3)–(5.4),
printed p.70, and (5.7)–(5.8), p.71,
[primary PDF](https://math.berkeley.edu/~corteel/MATH249/macdonald.pdf).
The actual Cauchy, exterior and binary projections used here
are the same explicit maps fixed in T-047 and T-049.

## 2. A bounded formula for every class trace

For a cycle partition \(\gamma\) define
\[
h_\gamma(j)=[z^j]\frac{1-z}{\prod_{\ell\in\gamma}(1-z^\ell)}.
\tag{VW.9}
\]
This is the complete-character trace of the ordinary standard
representation of \(S_{|\gamma|}\). For \(g\in S_5\)
write \(\gamma(g)\) for its cycle partition and \(m_1(g)\)
for its number of fixed points. The trace in (VW.4) is the sum
of the following three completely specified terms:

* The ambient term is
  \(h_\gamma(a)h_\gamma(b)-h_\gamma(a+1)h_\gamma(b-1)\).
* Subtract \(m_1(g)\) times
  \(\sum_{i,j\ge0,\ i+j<k}
  [h_\delta(a-i)h_\delta(b-j)
  -h_\delta(a-i+1)h_\delta(b-j-1)]\),
  where \(\delta\) removes one fixed point from \(\gamma\).
  This term is absent when \(m_1(g)=0\).
* For every literal \(g\)-stable two-subset \(A\), add
  \(\operatorname{sgn}(g|A)\det(g|W)^b
  h_{\gamma(g|A^c)}(x)\) times
  \(U_{\gamma(g|A^c)}(k)^2\) when \(g|A\) is the
  identity, or \(U_{\gamma(g^2|A^c)}(k)\) when it is a
  transposition. Here \(U_\delta(k)=\sum_{t=0}^{k-1}h_\delta(t)\).

The square in the fixed-pair case and the squared permutation
in the swapped-pair case follow by the literal trace of an
operator on two tensor factors. For the three possible
complementary classes, the complete formulas are
\[
\begin{array}{c|c|c}
\delta&h_\delta(x)&U_\delta(k)\\\hline
1^3&x+1&k(k+1)/2\\
21&\mathbf1_{2\mid x}&\lceil k/2\rceil\\
3&(1,-1,0)_{x\bmod3}&\mathbf1_{k\equiv1\ (3)}.
\end{array}
\tag{VW.10}
\]
All induced traces above are sums over at most five fixed points
and ten two-subsets. Their signs are the actual ones of (VW.4).

At the formal origin of (VW.2), \(k=3\), \((a,b)=(7,7)\)
and \(N=14<15\). T-049 gives \((J_3)_{14}=0\).
The same trace formula is zero there: expand T-049's full tail
product by selecting truncated factors. Selected-four terms have
degree at most8. The full-selected term has degree at most12,
including the degree-two exterior factor. Both are below14;
the selected-three Schur term vanishes by \(b>3(k-1)\).
Thus the three displayed terms still compute the actual zero
ideal component at that point. This proves its value, without
assigning a plethysm coefficient to an invalid partition.

## 3. Exact phase polynomials, valid from the initial residue

Let \(L=\operatorname{lcm}(\gamma)\). The maximum pole
multiplicity of (VW.9) is
\(d+1=\max_{e\mid L}
(\#\{\ell\in\gamma:e\mid\ell\}-\mathbf1_{e=1})\).
Partial fractions express the coefficient sequence, on each
residue modulo \(L\), as a polynomial of degree at most
\(d\). The generating function is proper, so this assertion
holds from index zero. The polynomial is explicitly
\[
H_{\gamma,r}(z)=
\sum_{j=0}^d h_\gamma(r+Lj)
\prod_{\substack{0\le q\le d\\q\ne j}}
\frac{(z-r)/L-q}{j-q}.
\tag{VW.11}
\]
Only bounded initial coefficients of the fixed rational function
are used here.

For completeness the triangular singleton sum is also evaluated
by a fixed polynomial construction. Let \(L\le4\) be the
period of its complementary \(S_4\) class. Write
\(i=s+Lu\), \(j=t+Lv\), with \(0\le s,t<L\), and set
\(M=\lfloor(k-1-s-t)/L\rfloor\). On each phase of
\((a,b,k)\), this is an affine polynomial in \(k\).
Substitute (VW.11) in the summand. Its formal expression in
\(u,v\) has degree at most two in each variable; write it
uniquely as \(\sum_{p,q} e_{pq}\binom up\binom vq\).
Its triangular sum is exactly
\[
\sum_{p,q} e_{pq}\binom{M+2}{p+q+2},
\quad
\sum_{u,v\ge0,\ u+v\le M}\binom up\binom vq
=\binom{M+2}{p+q+2}.
\tag{VW.12}
\]
The identity follows by multiplying
\(z^p/(1-z)^{p+1}\), \(z^q/(1-z)^{q+1}\)
and \(1/(1-z)\). Since \(k\ge3\), \(L\le4\),
we always have \(M\ge-1\). At \(M=-1\), every displayed
binomial polynomial is zero, so the formula covers the empty
initial triangle as well. The formal polynomial extension used
to find the \(e_{pq}\)'s is only evaluated as a trace on the
actual triangle, where all complete-function indices were shown
nonnegative in §1.1.

Equations (VW.9)–(VW.12), the literal two-subset list and
(VW.10) define every class polynomial with no unbounded sum.
`chamber_polynomials.py` carries out exactly these rational
operations. In the class order
\(1^5,2111,221,311,32,41,5\), their total degrees are
\((5,3,2,1,0,0,0)\); the numbers of phases retained are
\((1,8,8,27,216,64,125)\). All phases are stored in
`VARIABLE_WALL_POLYNOMIALS.json`. This is a finite polynomial
certificate, independent of the varying input.

The identity polynomial \(P_1(X,B,K)\) has nonnegative
ordinary coefficients. To give all of them explicitly, the
following entry is the coefficient of \(X^iB^j\) in
\(12P_1\):

| \((i,j)\) | Coefficient as a polynomial in \(K\) |
|---|---|
| (0,0) | \(54K+90K^2+42K^3+6K^4\) |
| (0,1) | \(78+305K+177K^2+28K^3\) |
| (0,2) | \(305+219K+39K^2\) |
| (0,3) | \(36+12K\) |
| (0,4) | \(1\) |
| (1,0) | \(48+205K+177K^2+56K^3+6K^4\) |
| (1,1) | \(365+518K+216K^2+28K^3\) |
| (1,2) | \(358+237K+39K^2\) |
| (1,3) | \(38+12K\) |
| (1,4) | \(1\) |
| (2,0) | \(120+202K+96K^2+14K^3\) |
| (2,1) | \(304+219K+39K^2\) |
| (2,2) | \(54+18K\) |
| (2,3) | \(2\) |
| (3,0) | \(72+51K+9K^2\) |
| (3,1) | \(17+6K\) |
| (3,2) | \(1\) |

## 4. The analytic positivity certificate

Let \(\Delta^\delta\) be the mixed forward difference with
step60 in \((X,B,K)\). The complete possible orders form
the downward-closed set
\[
\mathcal A=
\{(0,j,l):j+l\le4\}
\cup\{(i,j,l):1\le i\le3,\ 0\le j\le4,
i+j+l\le5\}.
\tag{VW.13}
\]
It has46 elements. Every phase polynomial is supported on
monomials in this set; all differences outside it vanish.
For each nonzero \(\delta\) of total order at most three,
form the following explicit polynomial. From \(\Delta^\delta P_1\)
subtract, for every nonidentity conjugacy class, its size times
the coefficientwise maximum, over its finitely many phases, of
the absolute coefficients of \(\Delta^\delta P_g\).
Call the resulting polynomial \(M_\delta\).

All coefficients of these nineteen polynomials are nonnegative.
The following table gives the constant coefficient and the
minimum over their represented coefficients; the complete
polynomials and every phase used to construct them are in the
fixed certificate. The arithmetic is rational and exact.

| \(\delta\) | Constant coefficient | Minimum represented coefficient |
|---|---:|---:|
| (0,0,1) | 7224470 | 30 |
| (0,0,2) | 95238000 | 5400 |
| (0,0,3) | 237816000 | 1512000 |
| (0,1,0) | 1792265 | 10 |
| (0,1,1) | 92445000 | 1800 |
| (0,1,2) | 272052000 | 1404000 |
| (0,2,0) | 19146000 | 600 |
| (0,2,1) | 169884000 | 648000 |
| (0,3,0) | 42768000 | 216000 |
| (1,0,0) | 1288865 | 5 |
| (1,0,1) | 2103897000 | 3600 |
| (1,0,2) | 12628332000 | 972000 |
| (1,1,0) | 388302000 | 1200 |
| (1,1,1) | 9935064000 | 324000 |
| (1,2,0) | 2189628000 | 108000 |
| (2,0,0) | 7767000 | 1200 |
| (2,0,1) | 5857092000 | 648000 |
| (2,1,0) | 885204000 | 216000 |
| (3,0,0) | 7776000 | 108000 |

For the other26 nonzero orders in \(\mathcal A\), the
nonidentity differences vanish by their degree bounds. The
identity table proves nonnegative coefficients and a positive
constant for each remaining difference. Thus all45 positive
orders have a strictly positive domination polynomial; their
minimum constant is1288865.

Here is the implication for every outer label, including all
signs. A finite group representation admits an invariant positive
Hermitian form, so \(|\chi_\nu(g)|\le\dim[\nu]\).
On any valid phase and at nonnegative \(X,B,K\), the triangle
inequality and the coefficientwise bound therefore give
\[
\Delta^\delta f_\nu(X,B,K)
\ge\frac{\dim[\nu]}{120}M_\delta(X,B,K)>0
\quad(\delta\in\mathcal A\setminus\{0\}),
\]
where \(f_\nu\) is the character average of (VW.4).
Step60 preserves all phases. The order-zero values are
nonnegative because they are the actual multiplicities in
(VW.3), with the formal zero at the excluded origin already
proved. Hence every coefficient used in the next section is a
nonnegative integer. This establishes positivity by finitely
specified polynomial inequalities, without assuming positivity
of an unevaluated difference.

## 5. The positive formula and every constraint matrix

Let \(\nu=\mu\) when \(d+b+x\) is even and
\(\nu=\mu^t\) when it is odd. Write
\((X,B,K)=r+60q\), with \(0\le r_i<60\), and set
\[
D_{\nu,r,\delta}=
\sum_{0\le h\le\delta}
(-1)^{|\delta|-|h|}\binom{\delta}{h}
f_\nu(r+60h).
\]
These are fixed constants: all evaluation coordinates are
bounded by359, independently of the input. The exact polynomial
Newton identity gives
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{\delta\in\mathcal A}
D_{\nu,r,\delta}\prod_{i=1}^3\binom{q_i}{\delta_i}.}
\tag{VW.14}
\]
Their positivity was proved in §4. Every trace evaluation in the
constants is the bounded formula of §3, using the fixed
polynomial certificate. The evaluator therefore
has no input-dependent multiplicity oracle.

For each positive constant use integer variables \(q_1,q_2,q_3\),
a selector \(z\), and three increasing chains of lengths
\(\delta_i\). The complete constraints are
\[
\begin{gathered}
60q_i=Z_i-r_i,\quad q_i\ge0,\qquad
0\le z\le D_{\nu,r,\delta}-1,\\
0\le u_{i1}<\cdots<u_{i,\delta_i}<q_i
\quad(1\le i\le3),\qquad Z=(X,B,K).
\end{gathered}
\tag{VW.15}
\]
Replace strict inequalities by gaps of at least one. The selector
and the increasing subsets give a bijection with the corresponding
summand in (VW.14). Empty chains have one choice. These are bounded
rational polytopes, with at most \(3+1+|\delta|\le9\)
variables and46 disjoint order tags. The quotient coordinates
and chain entries have \(O(\log(x+b+k+1))\) bits; the
selector bound belongs to fixed data. The determinant parameter
only selects the specified outer-label parity.

`positive_wall_chamber.py` evaluates (VW.14), emits every
integer matrix in (VW.15), and lazily enumerates witnesses.
It uses only fixed rational polynomials, bounded finite
differences and binomials of order at most five.

## 6. Complete support and exact check scopes

The three first-order constants are strictly positive. Therefore
a zero in (VW.14) has \(q=(0,0,0)\). The complete fixed
residue enumeration, omitting the invalid origin, is:

| Effective label \(\nu\) | All zero triples \((X,B,K)\) |
|---|---|
| \((5)\) | \((0,0,2),(0,1,1),(1,0,0)\) |
| \((4,1)\) | none |
| \((3,2)\) | none |
| \((3,1,1)\) | \((0,0,1)\) |
| \((2,2,1)\) | none |
| \((2,1,1,1)\) | \((0,0,1),(1,0,0)\) |
| \((1^5)\) | \((0,0,2)\), \((0,1,0)\), \((0,1,1)\), \((0,2,0)\), \((1,0,0)\), \((1,0,1)\), \((2,0,0)\) |

Every other valid coefficient in the chamber is positive. Apply
the stated parity and (VW.2) to turn this into the original
partition and outer label.

`check_residue_support.py` checked all1512000 zeroth-order
constants, including the seven formal zeros at the excluded
origin. It used exact integer numerators of the class
polynomials and proved the maximum intermediate absolute bound
\(138514500600<2^{63}\) for those evaluations; the largest
weighted character-sum bound is69257572344. All classes, hashes,
extrema and the thirteen valid zeros are in
`VARIABLE_WALL_RESIDUE_RECEIPT.json`.

The separate `check_chamber_formula.py` compared the proposed
polynomials with434 full selected-subset restriction traces and
322 actual balanced cycle/Pieri coefficients, including orders
four and five and the added \(x<k-1\) region. It checked182
Newton continuation/parity cases and157 literal constraint
witnesses. The receipt is `VARIABLE_WALL_COMPARISON_RECEIPT.json`.
The rectangular agent independently verified140 actual
cycle-index/Murnaghan--Nakayama cases in the enlarged chamber,
including112 added cases outside the initial \(x\ge k-1\)
subchamber. Its receipt is
`work/rectangular/OUTER5_ZERO_TWIST_BULK_MN_CHECK.tsv`.
It separately read the complete enlarged proof (VW.1)–(VW.15)
and checked all actual maps, endpoints and positivity arguments;
that whole-proof review also passed.
The root independently derived the straightening enlargement,
reconstructed the transformed45 polynomial margins, and read
the complete proof (VW.1)–(VW.15); all checks passed. The archive
agent independently reconstructed all449 enlarged phase
polynomials from1627 unisolvent normal-subset character values,
recomputed all45 margins by literal step60 translation, and
replayed all1512000 zeroth-order constants with unbounded
integers. Every polynomial, margin, hash and support exception
matched. Its separate complete proof reading, printed-table
audit and evaluator checks of140 coefficients,6426 matrices
and2620 witnesses also passed. The exact records are
`work/archive/VARIABLE_WALL_REVIEW.md`,
`work/archive/VARIABLE_WALL_INDEPENDENT_RECEIPT.json` and
`work/archive/VARIABLE_WALL_EVALUATOR_RECEIPT.json`.
These distinct scopes are recorded separately; none is reported
as a proof-assistant certificate.
