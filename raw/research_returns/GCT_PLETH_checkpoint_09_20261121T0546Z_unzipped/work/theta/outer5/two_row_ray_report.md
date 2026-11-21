# Every two-row quotient on the five-point quadratic ray

## T-044. Exact realization and independent positive certificate

Let \(x,b,k,d\ge0\), write \(a=b+x\), and set
\[
n=d+b+x+k,\qquad
\lambda=(d+3b+2x+3k,d+b+x+2k,d+b+x,d+x,d).
\tag{R.1}
\]
For every \(\mu\vdash5\), the plethysm coefficient
\(p_{\mu,(n)}^\lambda\) is given by the positive count (R.11).
After selecting three residues modulo 60, there are at most 55
contributing polytopes, each with at most ten integer variables.
All constants have a fixed finite arithmetic specification. The
independent exact certificate checks all 120,960,000 constants in the
rectangular range of difference orders, including the 25 orders that
vanish identically. This is the \(t=0\) specialization of G-021;
the separable-product calculation here independently verifies that
specialization. No claim of historical novelty is made.

## 1. The actual representation map

Let \(E=\mathfrak h_5\), let \(Z\) be the five canonical frame points
\([\ell_i]\) in \(\mathbf P(E)\), with
\(\ell_i=e_i-\frac15\sum_j e_j\), and let \(\mathcal I\) be their
ideal sheaf. Put \(L=\mathcal O(-1)\subset E\) and \(Q=E/L\).
Define the actual section module
\[
M_{x,b,k}=H^0\bigl(\mathbf P(E),
       \mathcal I^k(2k)\otimes S_{(b+x,b)}Q\bigr).
\tag{R.2}
\]
The normal-coordinate map of G-015 and its inverse balanced
homogenization give
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
 \simeq\epsilon^{d+b+x}\otimes M_{x,b,k},}
\qquad\epsilon=\operatorname{sgn}_{S_5}.
\tag{R.3}
\]
Here every twist can be checked directly. After removing the full
determinant power \(d\), the relative quotient-flag weight on \(Q^*\)
is \((a,x,0)\), and the first-line weight is \(a+2k\).
Exterior-column contraction gives the perfect Schur pairing
\[
S_{(a,x)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,b)}Q.
\]
The identity \(\det Q^*=\det E^*\otimes\mathcal O(-1)\)
leaves line twist \(2k\) and sign \(\epsilon^{d+a}\).
The point order is \(\lambda_2-n=k\). The inverse map is exactly
\(F\mapsto u^{-k}F(v(X))\). G-015's independent transverse ratios
prove that its polynomial extension condition is membership in
\(\mathcal I^k\). Thus (R.3) identifies the specified modules, with
their group actions and extension condition.

## 2. The exact Schur complex and all cohomology

The actual differential is fixed as follows. Put \(N=a+b\), take
\([L\to E]^{\otimes N}\), with \(L\) in degree \(-1\), and use the
Koszul-signed permutation action. For line positions \(J\), replace
position \(r\in J\) by the tautological inclusion with sign
\((-1)^{|J\cap\{1,\ldots,r-1\}|}\). Apply the primitive Young
idempotent \(c_Tr_T/h_{a,b}\) for the row-filled tableau of shape
\((a,b)\). The differential commutes with this idempotent. Exterior
Pieri, obtained by multiplying the Schur alternant by an elementary
symmetric function, identifies its three terms as
\[
0\to L^2S_{(a-1,b-1)}E
\to L\bigl(S_{(a-1,b)}E\oplus S_{(a,b-1)}E\bigr)
\to S_{(a,b)}E\to S_{(a,b)}Q\to0.
\tag{R.4}
\]
Only valid partition terms are retained. The rational polytabloid,
sign-projector and Frobenius-reciprocity prescriptions in
`work/archive/GENERAL_TWO_ROW_SCHUR_COMPLEX.md`, (S.1)–(S.5), specify
the comparison matrices and all their scalars; conjugating the
displayed tensor differential by them fixes the maps in (R.4).
That complete proof has been read and checked independently here.

For completeness, the exactness argument survives the ideal tensor:
locally split \(E=L\oplus Q\), contract the tensor complex onto
\(Q^{\otimes N}\), average the contraction over \(S_N\), and restrict
to the idempotent image. This is an \(\mathcal O\)-linear homotopy.
It remains a homotopy after tensoring by \(\mathcal I^k(2k)\).
The resulting augmented complex is therefore exact even though the
ideal need not be locally free.

Its three scalar twists are \(2k,2k-1,2k-2\). The last two terms
have no \(H^2\) or \(H^3\): the point quotient has finite support
and these twists are at least \(-2\). The first scalar ideal has no
positive cohomology. For \(k\ge2\), this is the fully applied linear
power result A-029; for \(k=1\), evaluation of quadrics onto the five
points is onto; for \(k=0\), it is the scalar projective calculation.
In the cohomology spectral sequence of the three-term complex, the
remaining possible \(H^1\)'s are in total degrees zero and minus one.
Consequently
\[
H^{i>0}(\mathcal I^k(2k)S_{(a,b)}Q)=0.
\tag{R.5}
\]
This includes \(a=b\), \(b=0\), \(a=b=0\), and both \(k=0,1\)
endpoints. In particular no map between the exceptional first
cohomology groups at \(k=1\) has been silently assumed onto.

## 3. Seven elementary traces and their exact degree bound

Use the class order
\(1^5,21^3,2^21,31^2,32,41,5\), with sizes
\(1,10,15,20,20,30,24\). Let \(f_g\) be the fixed-letter count.
The traces \(h_g(j)=\operatorname{tr}(g\mid\operatorname{Sym}^jE)\)
are the coefficients of
\((1-z)/\prod_{\ell\in\operatorname{cyc}(g)}(1-z^\ell)\).
Explicitly, for \(j\ge0\), they are
\[
\begin{array}{c|c}
g&h_g(j)\\\hline
1^5&\binom{j+3}{3}\\
21^3&(j^2+4j+4-(j\bmod2))/4\\
2^21&(j+2)/2\text{ for even }j,\ 0\text{ otherwise}\\
31^2&\lfloor j/3\rfloor+1\\
32&(1,-1,1,0,0,0)_{j\bmod6}\\
41&\mathbf1_{j\equiv0\pmod4}\\
5&(1,-1,0,0,0)_{j\bmod5}.
\end{array}
\tag{R.6}
\]
Their residue-polynomial extensions also vanish at \(-1,-2\), so
they agree with the required convention there. The certificate checks
each formula against its cycle recurrence through every used index.

For \(a=b+x\), put
\[
\begin{aligned}
A_g&=h_g(a)h_g(b)-h_g(a+1)h_g(b-1),\\
B_g&=h_g(a-1)h_g(b)-h_g(a+1)h_g(b-2),\\
C_g&=h_g(a-1)h_g(b-1)-h_g(a)h_g(b-2),\\
J_g(k)&=f_gh_g(k-1).
\end{aligned}
\]
These are respectively the three Schur terms in (R.4), with the
middle two summed; the formulas automatically implement all omitted
boundary terms. The canonical affine point charts identify the jet
trace with \(J_g(k)\), as proved by their evaluation maps in T-042.
Taking the Euler trace of (R.4), justified by (R.5), gives the actual
character
\[
\boxed{P_g(x,b,k)=A_g(h_g(2k)-J_g(k))
 -B_g(h_g(2k-1)-J_g(k))+C_g(h_g(2k-2)-J_g(k)).}
\tag{R.7}
\]
This is a sum of three separable products, which is the calculation
used in the independent certificate.

On every residue class modulo 60 it is a polynomial of separate
degrees at most \((3,4,3)\). At the identity its dimension is exactly
\[
\frac{(x+1)(b+x+2)(b+1)}{12}
\bigl[(2k+1)(b+2k+2)(b+x+2k+3)-5k(k+1)(k+2)\bigr].
\tag{R.8}
\]
All ordinary coefficients are positive and its total degree is six.
For the transposition and double-transposition classes, substitution
of (R.6) on each of the eight parity phases gives total degree at
most three; for the three-cycle class the 27 phase polynomials have
degree at most one. These are exact symbolic polynomial identities,
retained in the certificate, not a finite sample of large parameters.
The remaining classes are periodic. The formulas remain valid at
every initial point because every negative index that occurs is
\(-1\) or \(-2\), already accounted for above.

## 4. Fixed positive constants and their verification

The fixed irreducible character rows, in the class order of (R.6), are
\[
\begin{array}{c|rrrrrrr}
5&1&1&1&1&1&1&1\\
41&4&2&0&1&-1&0&-1\\
32&5&1&1&-1&1&-1&0\\
311&6&0&-2&0&0&0&1\\
221&5&-1&1&-1&-1&1&0\\
2111&4&-2&0&1&1&0&-1\\
11111&1&-1&1&1&-1&-1&1.
\end{array}
\]
Let \(m_\nu(x,b,k)=\frac1{120}\sum_g|g^{S_5}|\chi_\nu(g)P_g(x,b,k)\).
For residues \(r\in\{0,\ldots,59\}^3\) and
\(\alpha=(i,j,l)\in\{0,\ldots,3\}\times\{0,\ldots,4\}
\times\{0,\ldots,3\}\), define
\[
C_{\nu,r;\alpha}=\sum_{u=0}^i\sum_{v=0}^j\sum_{w=0}^l
(-1)^{i+j+l-u-v-w}\binom iu\binom jv\binom lw
m_\nu(r_1+60u,r_2+60v,r_3+60w).
\tag{R.9}
\]
This is a completely specified finite integer constant: every
argument is below 300, and (R.6)–(R.7) contain only fixed elementary
arithmetic. It requires no unknown representation coefficient.

`two_row_ray_certificate.py` verifies all
\(7\cdot60^3\cdot4\cdot5\cdot4=120960000\) constants exactly.
They are all nonnegative. Exactly 25 difference orders vanish
identically. The other 55 orders form the following downset \(D\):
\[
\begin{array}{c|c}
(i,j)&l\\\hline
(0,0),(1,0),(0,1),(2,0),(0,2),(1,1),(2,1),(1,2)&0\le l\le3\\
(3,0),(0,3),(3,1),(2,2),(1,3)&0\le l\le2\\
(0,4),(1,4),(2,3),(3,2)&0\le l\le1.
\end{array}
\tag{R.10}
\]
All nonconstant orders in \(D\) are strictly positive, with minimum
258. The maximum of all constants is 165476844000. The calculation
establishes each signed-64-bit intermediate bound using arbitrary
precision integers before constructing its array; the largest weighted
numerator bound is 19857224520000. Every division by 12 and by 120
is checked for exact divisibility. Thus the vectorized operations do
not introduce an overflow or rounding assumption.

`TWO_ROW_RAY_SUMMARY.json` records all minima and maxima, the exact
phase degrees, zero triples, intermediate bounds and per-label SHA256
hashes. The full table is streamed in the documented order rather
than saved. `TWO_ROW_RAY_CHECK.txt` is its concise receipt.

`two_row_positive.py` is the direct evaluator and full constraint-matrix
exporter for T-044/T-045. It constructs constants only at the fixed
bounded arguments in (R.9), caches them, and evaluates the positive
binomial products. It calls no representation library or elimination
routine. The shared `check_two_row_evaluator.py`, extended through
T-046, passed 1882 exact continuation, branch and fixed-coin
comparisons, plus 57 literal matrix witnesses.
The receipt is `TWO_ROW_EVALUATOR_CHECK.txt`.

## 5. The positive formula and the exact lattice bijection

Write \((x,b,k)=r+60q\), and put \(\nu=\mu\) for even
\(d+b+x\), or \(\nu=\mu^t\) for odd \(d+b+x\). The ordinary
multivariate Newton identity and the proved residue-polynomial bound
give the equality
\[
\boxed{p_{\mu,(n)}^\lambda
 =\sum_{\alpha\in D}C_{\nu,r;\alpha}
       \binom{q_1}{\alpha_1}\binom{q_2}{\alpha_2}
       \binom{q_3}{\alpha_3}.}
\tag{R.11}
\]
For each fixed residue and order introduce \(q_1,q_2,q_3,y\) and
three increasing chains of respective lengths \(\alpha_1,\alpha_2,
\alpha_3\). Impose
\[
60q_i=X_i-r_i,\quad q_i\ge0,\quad 0\le y<C_{\nu,r;\alpha},
\quad0\le z_{i,1}<\cdots<z_{i,\alpha_i}<q_i.
\tag{R.12}
\]
Empty chains are omitted; strict integral inequalities mean the
corresponding closed difference inequalities with gap one. Each
coordinate is bounded. A point is exactly a choice of \(y\) and
three subsets, with the inverse writing each subset in increasing
order. This proves that its lattice count is the summand of (R.11).
Since \(|\alpha|\le6\), there are at most ten integer variables.
There are \(60^3\cdot55=11880000\) fixed tags before selecting the
unique residue, and 55 after it. Fixed constants are below \(2^{38}\);
all other coordinates and right sides have logarithmic bit length in
\(2+x+b+k+d\). The arithmetic count uses a fixed number of operations
and binomial coefficients of bounded order.

Every first-order constant is positive, so all zeros occur inside the
residue cube. The 70 zero triples, grouped by effective label, are
listed exactly in `TWO_ROW_RAY_SUMMARY.json` (counts 9,3,3,6,6,12,31).
This is a complete support specification.

## Sources and verification scope

The scalar ideal-power input is the applied A-029 proof from
[Kustin–Polini–Ulrich, formula (6.1.4), p.1509, Lemma 6.3 and Corollary 6.4, p.1510](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf).
The exact ideal and all local hypotheses were verified in T-038 and
A-029. Scalar cohomology is
[Stacks Project, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS).
The relative Schur convention is
[Magyar, Propositions 1 and 4](https://arxiv.org/pdf/alg-geom/9411014),
transported by the displayed exterior-column pairing. The entire
signed tensor Schur construction and its ideal-tensored cohomology
were independently read in the archive appendix. G-021 proves the
larger \(c\ge2k\) family by a separate coefficient-domination
argument; the finite computation here is an independent exact check
of its full quadratic-ray specialization.
