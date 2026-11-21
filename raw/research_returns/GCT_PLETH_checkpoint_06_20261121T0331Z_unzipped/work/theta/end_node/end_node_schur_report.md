# Arbitrary outer Schur functors on the equal-middle-row family

This report extends T-024–T-026 by identifying the full balanced permutation module. All statements below are unconditional over characteristic zero, and every coefficient is accompanied by an explicit algebra or lattice-point morphism. Author/checker: GPT-6 Astra Pro, run `GCT_PLETH-20261121-theta`; effort setting is not exposed.

## T-027. Exact reflection-representation model and positive tableau formula

Let \(m\ge3\), \(\mu\vdash m\), \(n\ge0\), and
\[
\lambda=(\alpha,\beta^{m-2},\gamma)\vdash mn,
\qquad \alpha\ge\beta\ge\gamma\ge0.
\]
Write
\[
p_{\mu,(n)}^\lambda=[S_\lambda V:S_\mu(\operatorname{Sym}^nV)],
\qquad
S=\min(\alpha-\beta,\beta-\gamma).
\tag{S.1}
\]
Let \(\mathfrak h_m\) be the \((m-1)\)-dimensional standard representation of \(S_m\), realized as the quotient of its permutation representation by the trivial line. Set
\[
\nu=\begin{cases}\mu,&\beta\text{ even},\\ \mu',&\beta\text{ odd}.\end{cases}
\tag{S.2}
\]
For a standard Young tableau \(T\) with entries \(1,\ldots,m\), define
\[
\operatorname{Des}(T)=\{i: i+1\text{ lies in a lower row than }i\},
\qquad
\operatorname{comaj}(T)=\sum_{i\in\operatorname{Des}(T)}(m-i).
\tag{S.3}
\]
Then the exact formulas are
\[
\boxed{
(S_\lambda\mathbf Q^m)_{(n^m)}
\simeq\operatorname{sgn}^{\beta}\otimes
\operatorname{Sym}^{S}(\mathfrak h_m)
\quad\text{as }S_m\text{-modules},}
\tag{S.4}
\]
and
\[
\boxed{
p_{\mu,(n)}^\lambda
=\sum_{T\in\operatorname{SYT}(\nu)}
\#\left\{(c_2,\ldots,c_m)\in\mathbf Z_{\ge0}^{m-1}:
\sum_{i=2}^m i c_i=S-\operatorname{comaj}(T)\right\}.}
\tag{S.5}
\]
Negative right sides contribute zero. The sum is finite and entirely explicit. T-028 below realizes it as the lattice-point count of one polytope with a polynomial-size description.

### Proof of the module isomorphism, including its character twist

Use the exact balanced incidence algebra from T-024:
\[
B_{\mathrm{ends}}
=\mathbf Q[u,v,z,t_1,\ldots,t_m]
/(\sum_i t_i,\ uv-\prod_i t_i),
\tag{S.6}
\]
with the right weights and literal permutation action in (E.12)–(E.13) of `end_node_report.md`. Put
\[
k=n-\beta,\quad k_+=\max(k,0),\quad L=\max(-k,0).
\]
Before imposing \(\sum_i t_i=0\), every monomial has a unique normal form with at most one of \(u,v\) present, using \(uv=\prod_i t_i\). Distinct such normal monomials have distinct exponent vectors in the original \(x_i,y_i,z\), as proved in T-024. In the component of degree \((n,\lambda)\), the normal form is necessarily
\[
u^{k_+}v^L z^\gamma f(t_1,\ldots,t_m),
\qquad \deg f=\beta-\gamma-mL.
\tag{S.7}
\]
This follows directly by subtracting the degree and middle-row equations (E.22), which gives the fixed difference \(a-b=k\); eliminating every factor \(uv\) increases the \(t\)-degree by \(m\). The equation \(\sum_i t_i=0\) does not change that difference. Its part in this component is exactly the same factor in (S.7) times a multiple of \(\sum_i t_i\). Thus multiplication in (S.7) gives a vector-space isomorphism
\[
\left(\mathbf Q[t_1,\ldots,t_m]/(\sum_i t_i)\right)_S
\longrightarrow (B_{\mathrm{ends}})_{n,\lambda}.
\tag{S.8}
\]
Here the degree equals \(S\), since
\[
(\alpha-\beta)-(\beta-\gamma)=m(n-\beta)=mk
\]
implies
\[
\beta-\gamma-m\max(0,\beta-n)
=\min(\alpha-\beta,\beta-\gamma).
\tag{S.9}
\]
This also proves its nonnegativity under the stated partition inequalities.

For an odd permutation, the factor \(v^Lz^\gamma\) contributes the sign \((-1)^{mL+\gamma}\). The degree-\(S\) polynomial in the \(t_i\) contributes an additional \((-1)^S\) under their signed permutation action. Since \(S+mL+\gamma=\beta\), the total twist is exactly \(\operatorname{sgn}^{\beta}\). The quotient by \(\sum_i t_i\) is the symmetric algebra on \(\mathfrak h_m\). Finally the polynomial Cauchy identification (E.4) identifies the right-hand side of (S.8), with all actions retained, with \((S_\lambda\mathbf Q^m)_{(n^m)}\). This proves (S.4).

The refined balanced Howe identity T-003 gives
\[
p_{\mu,(n)}^\lambda
=\dim\operatorname{Hom}_{S_m}([\mu],(S_\lambda\mathbf Q^m)_{(n^m)}).
\tag{S.10}
\]
The exact sign-twist identity \([\mu]\otimes\operatorname{sgn}\simeq[\mu']\) identifies this with the multiplicity of \([\nu]\) in \(\operatorname{Sym}^{S}\mathfrak h_m\). One character verification of this identity is as follows: the symmetric-function involution \(p_i\mapsto(-1)^{i-1}p_i\) sends \(s_\mu\) to \(s_{\mu'}\); under the Frobenius formula it multiplies the coefficient on a cycle type \(\rho\) by \((-1)^{m-\ell(\rho)}\), exactly the permutation sign. Equality of the resulting characters gives the module isomorphism in characteristic zero.

### Cycle traces and a full standardization proof

For a permutation with cycle lengths \(\rho_1,\ldots,\rho_\ell\), the permutation representation has characteristic determinant
\[
\det(1-q\sigma)=\prod_{j=1}^\ell(1-q^{\rho_j}).
\]
Removing the trivial line gives
\[
\sum_{d\ge0}\operatorname{tr}(\sigma;\operatorname{Sym}^d\mathfrak h_m)q^d
=\frac{1-q}{\prod_j(1-q^{\rho_j})}.
\tag{S.11}
\]
Take its inner product with the character \(\chi^\nu\). The Frobenius character formula, evaluated at the alphabet \(1,q,q^2,\ldots\), gives
\[
\begin{aligned}
\sum_{d\ge0}[\,[\nu]:\operatorname{Sym}^d\mathfrak h_m\,]q^d
&=(1-q)\sum_{\rho\vdash m}\frac{\chi^\nu(\rho)}{z_\rho}
\prod_j\frac1{1-q^{\rho_j}}\\
&=(1-q)s_\nu(1,q,q^2,\ldots).
\end{aligned}
\tag{S.12}
\]
The equality uses precisely \(p_i(1,q,q^2,\ldots)=(1-q^i)^{-1}\). It is a formal power-series equality, so no analytic specialization is needed.

We now derive the positive numerator without assuming a coinvariant-ring decomposition. Semistandard tableaux of shape \(\nu\), with weak rows and strict columns, enumerate \(s_\nu(1,q,q^2,\ldots)\), with weight \(q^{\sum_c(Q(c)-1)}\). Standardize a semistandard tableau by ordering cells by increasing entry and breaking ties from left to right. Equal entries cannot occupy the same column; their left-to-right order runs weakly upward in row number, by the column-strict and row-weak conditions. The result is a standard tableau \(T\), together with integers
\[
0\le a_1\le\cdots\le a_m,
\qquad a_i<a_{i+1}\text{ for every }i\in\operatorname{Des}(T),
\tag{S.13}
\]
where \(a_i+1\) is the original entry in the cell labelled \(i\).

Conversely, fill the cell labelled \(i\) in \(T\) by \(a_i+1\). The rows are weak because \(T\) increases across rows. For two cells in one column with labels \(p<q\), the row number increases from the cell of \(p\) to the cell of \(q\), so some consecutive step \(i\to i+1\), \(p\le i<q\), goes to a lower row. At that step (S.13) is strict, and hence the column entries are strict. Within an equality block of the sequence \(a_i\), the row numbers can never increase. A later cell in a higher row must then be farther right: otherwise it would lie weakly northwest of the earlier cell, contradicting the increasing row and column labels of \(T\). Thus standardizing the filled tableau recovers exactly \(T\). This proves the bijection.

For a fixed \(T\), write
\[
b_1=a_1,\qquad b_{i+1}=a_{i+1}-a_i-\mathbf1_{i\in\operatorname{Des}(T)}\ge0.
\]
Then
\[
\sum_{i=1}^m a_i
=\operatorname{comaj}(T)+\sum_{j=1}^m(m-j+1)b_j.
\tag{S.14}
\]
It follows that
\[
s_\nu(1,q,q^2,\ldots)
=\frac{\sum_{T\in\operatorname{SYT}(\nu)}q^{\operatorname{comaj}(T)}}
{\prod_{i=1}^m(1-q^i)}.
\tag{S.15}
\]
Substitution into (S.12) cancels exactly the factor \(1-q\), proving
\[
\sum_{d\ge0}[\,[\nu]:\operatorname{Sym}^d\mathfrak h_m\,]q^d
=\frac{\sum_{T\in\operatorname{SYT}(\nu)}q^{\operatorname{comaj}(T)}}
{\prod_{i=2}^m(1-q^i)}.
\tag{S.16}
\]
Taking the coefficient of \(q^S\) proves (S.5). For \(\mu=(m)\), the shape \(\nu\) is either a row with comajor index 0 or a column with comajor index \(\binom m2\), recovering exactly T-025.

## T-028. A single polynomial-size polytope and a support criterion

### The explicit polytope

The cells of \(\nu\) form a set \(C\) of size \(m\); write \(r(c)\) for the row number of a cell. Introduce variables
\[
X_{c,j}\quad(c\in C,\ 1\le j\le m),\qquad
\delta_j\quad(1\le j<m),\qquad
c_i\quad(2\le i\le m).
\]
There are \(m^2+2m-2\) variables. Impose
\[
0\le X_{c,j}\le1,\quad0\le\delta_j\le1,\quad c_i\ge0;
\qquad
\sum_jX_{c,j}=1\ (c\in C),\quad
\sum_cX_{c,j}=1\ (1\le j\le m).
\tag{S.17}
\]
Define the following linear forms, which introduce no new variables:
\[
\ell_c=\sum_{j=1}^m jX_{c,j},\qquad
r_j=\sum_{c\in C}r(c)X_{c,j}.
\tag{S.18}
\]
For each adjacent pair of cells in a row or column, with \(c'\) immediately right of or below \(c\), require
\[
\ell_c+1\le\ell_{c'}.
\tag{S.19}
\]
For every \(1\le j<m\), require
\[
1-m(1-\delta_j)\le r_{j+1}-r_j\le m\delta_j.
\tag{S.20}
\]
Finally require
\[
\sum_{i=2}^m i c_i+\sum_{j=1}^{m-1}(m-j)\delta_j=S.
\tag{S.21}
\]

At every integral point, (S.17) makes \(X\) a permutation assignment of the labels \(1,\ldots,m\) to the cells of \(\nu\). Equation (S.19) is exactly the standard-tableau condition. Since \(1\le r_j\le m\), (S.20) uniquely forces \(\delta_j=1\) when \(r_{j+1}>r_j\), and \(\delta_j=0\) otherwise. Thus its weighted sum in (S.21) is exactly \(\operatorname{comaj}(T)\). The remaining variables count the partitions in (S.5), without any multiplicity from the encoding. Conversely every pair counted in (S.5) gives exactly one integral point. Therefore
\[
\boxed{p_{\mu,(n)}^\lambda=\#(\mathcal P_{\mu,\lambda}\cap\mathbf Z^{m^2+2m-2}),}
\tag{S.22}
\]
where \(\mathcal P_{\mu,\lambda}\) is the explicitly displayed polytope (S.17)–(S.21). It is bounded: the \(X,\delta\) variables lie in \([0,1]\), and \(0\le c_i\le S/i\) follows from (S.21). Its number of variables, constraints, and nonzero matrix entries is polynomial in \(m\). Its coefficients have bit length \(O(\log(m(n+1)+1))\). This gives a direct \(\#P\) verifier in ordinary explicit partition encoding, with no algebra precomputation. As in T-025, a nonzero \(\beta\) supplies at least \(m-1\) explicitly listed parts of \(\lambda\); for \(\beta=0\), the answer is directly 1 for \(\mu=(m)\) and 0 for the other outer shapes.

### The exact nonvanishing criterion

Define
\[
b(\nu)=\sum_{r\ge1}(r-1)\nu_r,
\qquad d(\nu)=\#\{r:\nu_r>\nu_{r+1}\},
\qquad Q=S-b(\nu).
\tag{S.23}
\]
Here \(d(\nu)\) is the number of removable corners, equivalently the number of distinct positive part sizes. Then
\[
\boxed{
p_{\mu,(n)}^\lambda>0
\Longleftrightarrow
\left[Q=0\right]\ \text{or}\ \left[Q\ge2\right]\ \text{or}\
\left[Q=1\text{ and }d(\nu)\ge2\right].}
\tag{S.24}
\]

To prove this, the smallest exponent in the semistandard generating function \(s_\nu(1,q,q^2,\ldots)\) is \(b(\nu)\), occurring once: in row \(r\), column strictness forces every entry to be at least \(r\), and filling that row entirely by \(r\) attains the bound. A semistandard tableau of weight \(b(\nu)+1\) must increase exactly one cell of this minimum tableau by 1. Row weakness permits this only at the rightmost cell of a row; column strictness permits it only when no cell lies below it. These are exactly the \(d(\nu)\) removable corners, and all such increases are valid. Thus
\[
s_\nu(1,q,q^2,\ldots)=q^{b(\nu)}(1+d(\nu)q+O(q^2)).
\]
Multiplication by \(\prod_{i=1}^m(1-q^i)=1-q+O(q^2)\) in (S.15) gives
\[
\sum_Tq^{\operatorname{comaj}(T)}
=q^{b(\nu)}(1+(d(\nu)-1)q+O(q^2)).
\tag{S.25}
\]
It follows that the minimum comajor index is \(b(\nu)\), attained once, and the number of tableaux with comajor index \(b(\nu)+1\) is \(d(\nu)-1\). No sum of parts \(2,\ldots,m\) is 1, whereas every integer at least 2 is such a sum because \(m\ge3\). Formula (S.5) now proves every case of (S.24): the unique minimum tableau gives all \(Q=0\) and \(Q\ge2\), and at \(Q=1\) only the tableaux counted by \(d(\nu)-1\) can contribute.

This is an integer-arithmetic polynomial-time support test. When \(\beta\) is odd, the statistic can be computed directly on \(\mu\), since
\[
b(\mu')=\sum_i\binom{\mu_i}{2},\qquad d(\mu')=d(\mu).
\tag{S.26}
\]
The first identity counts pairs of cells in the same row; the second follows by exchanging the horizontal and vertical boundary corners of the Ferrers diagram. Thus a long transpose need not be explicitly expanded to test support. Compressed strings of repeated parts can also be handled by arithmetic sums over their blocks for this support test; the \(O(m^2)\) tableau polytope itself uses the ordinary explicit size convention stated above.

## Exact input identities and validation

The only representation-theoretic inputs are polynomial Cauchy/Howe duality, the refined balanced-weight identity T-003, and the Frobenius character identity from Schur–Weyl duality. Their action on the relevant module is specified in (S.4), (S.8), and (S.10). The exact primary locator supplied with the task for the balanced-weight realization is Landsberg, *Geometric Complexity Theory: an introduction for geometers*, subsection “A duality theorem for weight zero spaces and plethysms,” theorem `gaythm`, source lines 766–798. The Frobenius evaluation used in (S.12) is displayed explicitly, and (S.13)–(S.15) give a complete proof of the needed principal-specialization tableau identity. No generic coefficient oracle, coinvariant decomposition, or unproved positivity assertion enters the argument.

The cycle-trace averaging in (S.11)–(S.12) is the character-valued Molien formula: R. P. Stanley, *Invariants of finite groups and their applications to combinatorics*, Bull. Amer. Math. Soc. **1** (1979), 475–511, Theorem 2.1 and its complete proof on printed pp. 479–480. The primary author-hosted text was read in this run: https://math.mit.edu/~rstan/pubs/pubfiles/38.pdf. The tableau numerator is a classical representation-theoretic object; the report proves its precise comajor convention directly, rather than importing a statistic with a different tableau convention.

The author and the rectangular agent have each read the complete T-027 and T-028 proofs; their actual events are recorded separately in the respective `CHECK_EVENTS.tsv` files. The independent reader checked both directions of standardization, the comajor convention, the exact module twist, all polytope constraints, and the support argument. The same agent independently expanded the outer Schur power-sum cycle index and used Murnaghan–Nakayama to test all 231 coefficients, and their support, for every outer \(\mu\) and every admissible end shape with \(m=3,n=0,\ldots,4\) and \(m=4,n=0,\ldots,3\). Every comparison passed. Code: `work/rectangular/verify_endsector_schur.py`; receipt: `work/rectangular/ENDSECTOR_SCHUR_INDEPENDENT_CHECK.tsv`. These computations are additional checks, not replacements for the proof readings.
