# The first repeated-four canonical block

## R-045. The complete \((4,4)\) tail, with all inner-degree endpoints

Let \(a\ge3\), \(n\ge4\), and \(\dim V\ge3\). Put
\[
\lambda=(an-8,4,4),\qquad r_t=\min(4,\max(0,t-2)).
\]
All these displayed weights are partitions. The exact
target and actual canonical-image multiplicities are
\[
\boxed{
a_{a,n}^{\lambda}=r_a,\qquad
\operatorname{mult}_\lambda\operatorname{im}h_{n,a}
=\min(r_a,r_n).}
\tag{DF.1}
\]
In particular the actual map is surjective in every
\(\lambda\)-multiplicity for all \(n\ge a\ge3\) for which
this weight is a partition.

For inner degree three the valid parameters are \(a\ge4\),
and the complete answer is
\[
\boxed{
a_{a,3}^{(3a-8,4,4)}=1+\mathbf1_{a\ge6},\qquad
\operatorname{mult}_{(3a-8,4,4)}
\operatorname{im}h_{3,a}=1.}
\tag{DF.2}
\]
For inner degree two, \(a\ge6\), the target multiplicity
of \((2a-8,4,4)\) is one and its canonical-image
multiplicity is zero.

The proof supplies the entire four-by-four matrix,
its exact determinant and inverse, all finite-dimensional
relations and endpoint minors, and the complete cubic
extension space. Its maps use the scalar-one tensor
pairing SR.5–SR.6 throughout. No historical novelty
claim is made.

## 1. Four highest polynomials and an invariant upper bound

Write the centered rows as \(z_i=(z_{i1},z_{i2})\), put
\([z_i,z_j]=z_{i1}z_{j2}-z_{i2}z_{j1}\), and define
\[
M_{pq}=\sum_i z_{i1}^p z_{i2}^q,\qquad
S=\begin{pmatrix}M_{20}&M_{11}\\M_{11}&M_{02}\end{pmatrix}.
\]
Use the following ordered generators:
\[
\begin{aligned}
Q_0&=(\det S)^2,\\
Q_1&=\sum_i(z_i^t\operatorname{adj}(S)z_i)^2,\\
Q_2&=\sum_{i,j}[z_i,z_j]^2
                  z_i^t\operatorname{adj}(S)z_j,\\
Q_3&=\sum_{i,j}[z_i,z_j]^4.
\end{aligned}
\tag{DF.3}
\]
Every index sum in the last two lines is ordered.

The determinant identity
\(\det S=\sum_{i<j}[z_i,z_j]^2\) and the exact equality
\[
z_i^t\operatorname{adj}(S)z_j
=\sum_k[z_i,z_k][z_j,z_k]
\]
express each \(Q_j\) as a sum of products of four brackets.
They are consequently \(GL_2\) highest tensors of weight
\((4,4)\), with determinant character \((\det)^4\), and
are invariant under row permutations and common translations.

Set \(z_i=w_i-\bar w\). For any fixed original row \(w_r\),
the leading terms of \(z_i,z_j\) in that row are scalar
multiples of the same vector. Their quadratic bracket
term is zero. Thus each bracket is separately linear
in every original row, and every \(Q_j\) has separate
row degree at most four. Hence
\[
\widehat Q_{j;a,n}
=\left(\prod_i x_i\right)^n Q_j(y_i/x_i)
\tag{DF.4}
\]
is a polynomial highest vector of weight \(\lambda\)
for every \(n\ge4\).

The transpose tail is \((2,2,2,2)\). Apply the exact
surjection (SF.4), whose finite-row proof is HO.3.
In its even exterior-degree part, exterior degree zero
gives three copies: the additional determinant exponents
are \(0,1,2\), with paired shapes respectively
\((2,2,2,2),(1,1,1,1),(0,0,0,0)\).
Exterior degree two is
\((\det T)\otimes\Lambda^2T\); it gives exactly one
additional copy, from \(\Lambda^2T\) and the vertical
strip in rows three and four after the determinant shift.
The strip in rows one and two violates the paired
partition inequality. Exterior degree four has a
determinant-cube factor and cannot have fourth part two.
Odd exterior degrees have odd total degree. The actual
Pieri Young projections therefore prove
\[
\dim(S_{(4,4)}\mathfrak h_a)^{S_a}\le4.
\tag{DF.5}
\]

The moment expressions of (DF.3), useful for checking
every normalization, are
\[
\begin{aligned}
Q_0={}&(M_{20}M_{02}-M_{11}^2)^2,\\
Q_1={}&M_{02}^2M_{40}-4M_{02}M_{11}M_{31}
 +(2M_{20}M_{02}+4M_{11}^2)M_{22}\\
 &-4M_{20}M_{11}M_{13}+M_{20}^2M_{04},\\
Q_2={}&2\{M_{02}(M_{30}M_{12}-M_{21}^2)
 -M_{11}(M_{30}M_{03}-M_{21}M_{12})\\
 &\hspace{20mm}+M_{20}(M_{21}M_{03}-M_{12}^2)\},\\
Q_3={}&2(M_{40}M_{04}-4M_{31}M_{13}+3M_{22}^2).
\end{aligned}
\tag{DF.6}
\]
These follow by expanding the two-by-two bracket, so
they are exact polynomial identities, including factors
two and the ordered-pair convention.

## 2. The injective independent-row map

Let \(A_D=\mathbb Q[w_1,w_2]_{\le D}\), and identify
row-symmetric polynomials in \(a\) rows of separate
degree at most \(D\) with \(\operatorname{Sym}^a A_D\).
The diagonal evaluation morphism is
\[
\mathcal E_a(f)(L)=L^{\otimes a}(f),
\qquad L\in A_D^*.
\tag{DF.7}
\]
It is injective: the rational polarization identity
recovers every symmetric multilinear evaluation from
the diagonal polynomial. Equivalently, its monomial
coefficients are the nonzero multinomial multiples
of the row-orbit coefficients of \(f\).

On the subspace of common-translation-invariant polynomials,
restriction of (DF.7) to
\[
L(1)=1,\qquad L(w_1)=L(w_2)=0
\tag{DF.8}
\]
remains injective. Indeed, for an arbitrary normalized \(L\)
let \(v=(L(w_1),L(w_2))\) and define
\(L_0(p)=L(p(w-v))\). Then \(L_0\) satisfies (DF.8), and
translation invariance gives
\(L^{\otimes a}f=L_0^{\otimes a}f\).
For \(L(1)\ne0\), normalize \(L\) first and multiply by
\(L(1)^a\). This proves vanishing on a dense open set
of all functionals, hence everywhere; polarization then
gives \(f=0\).

The same argument proves the exact filtration identity
\[
f\in\operatorname{Sym}^a A_q
\quad\Longleftrightarrow\quad
\mathcal E_a(f)\text{ on (DF.8) contains no moment of
degree greater than }q
\tag{DF.9}
\]
for translation-invariant \(f\in\operatorname{Sym}^a A_D\).
For the reverse inclusion, the normalized expression on
(DF.8) depends only on moments through degree \(q\).
Translation back expresses every centered moment of
degree at most \(q\) using raw moments through degree
\(q\). Homogeneity then makes the full polynomial
\(\mathcal E_a(f)\) independent of all higher functional
coordinates. Its coefficient/polarization identification
in (DF.7) places \(f\) in \(\operatorname{Sym}^a A_q\).
This gives an actual equality of the indicated finite
polynomial subspaces, not merely a dimension comparison.

## 3. Complete moment matrix by equality partitions

Let \(L\) satisfy (DF.8), and write \(\mu_{pq}=L(w_1^pw_2^q)\).
Let \(F_0,\ldots,F_3\) be exactly the four expressions
(DF.6), with \(M_{pq}\) replaced by \(\mu_{pq}\).
Then
\[
\boxed{\mathcal E_a(Q)=(a)_3\,C_a F,}
\tag{DF.10}
\]
where \(Q,F\) are columns in the order \(0,1,2,3\).
A compact complete specification of the matrix is
\[
C_a=\operatorname{diag}(a^{-2},a^{-3},a^{-3},a^{-4})
       \,[\,A_a\mid B_a\,],
\tag{DF.11}
\]
with
\[
A_a=
\begin{pmatrix}
(a-3)(a^2-4a+8)&a^2-4a+6\\
8(a-3)(2a-5)&(a-2)(a^2-4a+15)\\
8(a-3)(a-2)&-2(a^2-4a+6)\\
48(a-3)&6(a-2)(2a-3)
\end{pmatrix},
\]
\[
B_a=
\begin{pmatrix}
-2a&(a-2)/2\\
-4a(a-1)&a^2-4a+5\\
a(a^2-3a+4)&-(a-2)\\
-12a(a-2)&a^3-6a^2+12a-6
\end{pmatrix}.
\]

Here is a complete finite algebraic derivation rule for
all sixteen entries, without interpolation.
Put \(W_{pq}=\sum_iw_{i1}^pw_{i2}^q\), \(W_{00}=a\).
The central-to-raw substitution is
\[
M_{pq}=\sum_{i=0}^p\sum_{j=0}^q
 \binom pi\binom qj
 \left(-\frac{W_{10}}a\right)^{p-i}
 \left(-\frac{W_{01}}a\right)^{q-j}W_{ij}.
\tag{DF.12}
\]
For every product of raw sums, expansion by its actual
equality partition of row indices gives
\[
L^{\otimes a}\prod_{j=1}^eW_{\alpha_j}
 =
 \sum_{\pi\in\Pi([e])}
 (a)_{|\pi|}
 \prod_{B\in\pi}\mu_{\sum_{j\in B}\alpha_j}.
\tag{DF.13}
\]
Each set partition chooses its distinct occupied rows
in \((a)_{|\pi|}\) ways. A singleton coordinate moment
is zero by (DF.8). Thus (DF.13) includes every term
with its literal integer multiplicity.

Substitution of (DF.12) into the four lines of (DF.6)
gives respectively \(15,52,34,47\) raw monomials.
Apply (DF.13) to each. All moments of degree greater
than four cancel, as the bracket degree proof also
requires. The coefficients on the following four
moment monomials recover the four columns of
\((a)_3C_a\):
\[
\begin{array}{c|c}
\text{monomial}&\text{coefficient within its }F_j\\ \hline
\mu_{11}^4&1\\
\mu_{02}^2\mu_{40}&1\\
\mu_{02}\mu_{30}\mu_{12}&2\\
\mu_{40}\mu_{04}&2 .
\end{array}
\tag{DF.14}
\]
All remaining coefficients agree with the corresponding
linear combination of (DF.6). The exact symbolic script
`derive_double_four_moment_matrix.py` executes precisely
(DF.12)–(DF.14), reconstructs every moment monomial, and
checks that all four residual polynomials are identically
zero over \(\mathbb Q(a)\). Its formulas and result are
saved in `DOUBLE_FOUR_MOMENT_MATRIX.json`.
Thus the finite certificate checks the entire identity,
including the moments that cancel; it is not a fitted
matrix from selected numeric samples.

The exact determinant is
\[
\boxed{\det C_a=
 \frac{(a-5)(a-4)^2(a-3)^3}{a^6}.}
\tag{DF.15}
\]
The four formal \(F_j\)'s are independent: their moment
degree patterns are respectively \(2+2+2+2\), \(2+2+4\),
\(2+3+3\), and \(4+4\), and each displayed polynomial
is nonzero. Therefore (DF.15) proves independence of
all four \(Q_j\)'s at \(a\ge6\).

The finite-row zero-padding/orthogonal-projection
morphisms QE.8–QE.9 restrict each centered moment
polynomial with scalar one. Their surjectivity on the
Young-projector invariant component follows from the
row power sums in (SF.4). Since the four generators
span at every row count at least six by (DF.5), their
images span the invariant component at every smaller
row count.

At \(a=3,4,5\), the complete relations are
\[
\begin{array}{c|l}
a&\text{relations}\\ \hline
3&Q_1=\tfrac43Q_0,\quad Q_2=-\tfrac23Q_0,\quad
       Q_3=\tfrac23Q_0\\
4&Q_2=2Q_0-2Q_1,\quad Q_3=\tfrac12Q_1\\
5&Q_3=-\tfrac45Q_0+\tfrac{13}{10}Q_1+\tfrac25Q_2 .
\end{array}
\tag{DF.16}
\]
Indeed these rows are exactly the left kernels of the
explicit \(C_a\), and injectivity (DF.7)–(DF.8) turns
them into polynomial identities. The first \(a-2\)
rows are independent: nonzero minors in columns
\((1)\), \((0,1)\), \((0,1,2)\) are respectively
\(1/3,\ 3/32,\ 48/3125\).
Thus the finite invariant dimension is exactly \(r_a\).
At \(a\le2\), \(\dim\mathfrak h_a\le1\), so the actual
two-row column antisymmetrizer is zero.
All invariants extend for \(n\ge4\) by (DF.4), proving
the target assertion in (DF.1).

## 4. Exact split-form substitution and the canonical matrix

For \(n\) centered split-factor rows, put
\[
N_j=(n)_j,\qquad
u_n=\frac{N_2^2}{N_4}
=\frac{n(n-1)}{(n-2)(n-3)},\qquad
v_n=\frac{N_2^3}{N_3^2}
=\frac{n(n-1)}{(n-2)^2}.
\]
The normalized actual monomial pairing gives
\[
\mu_2=-S/N_2,\qquad
\mu_3=2M_3/N_3,\qquad
\mu_4=(\operatorname{Wick}(S)-6M_4)/N_4.
\tag{DF.17}
\]
Here the five entries of the last numerator are
\[
(3M_{20}^2,\ 3M_{20}M_{11},\
 M_{20}M_{02}+2M_{11}^2,\
 3M_{11}M_{02},\ 3M_{02}^2)-6M_4.
\]
This is the distinct-factor pairing SR.5–SR.6, including
its repeated-index factorials; equivalently expansion
of the product linear form gives (DF.17).

Substitute these expressions into (DF.6). The result is
\[
\boxed{F=N_2^{-4}H_n Q_n,\qquad
H_n=
\begin{pmatrix}
1&0&0&0\\
8u_n&-6u_n&0&0\\
0&0&-4v_n&0\\
24u_n^2&-36u_n^2&0&36u_n^2
\end{pmatrix}.}
\tag{DF.18}
\]
For the second row, contraction of the Gaussian fourth
tensor with two adjugates is \(8(\det S)^2\).
This follows either from its five printed entries or
from
\((\operatorname{tr}(\operatorname{adj}(S)S))^2+
2\operatorname{tr}((\operatorname{adj}(S)S)^2)=8(\det S)^2\).
For the fourth row, direct expansion gives \(24Q_0\)
for its pure Wick part, \(6Q_1\) for the polarized
Wick/actual-fourth part, and \(Q_3\) for its pure actual
part. Substituting Wick minus six times the actual
tensor therefore gives \(24Q_0-36Q_1+36Q_3\).
The cubic row has scalar \((-1)\cdot2^2=-4\).
This proves every entry and sign. In particular
\[
\det H_n=864u_n^3v_n\ne0\qquad(n\ge4).
\tag{DF.19}
\]

Equations (DF.10), (DF.17) and the scalar-one grid pairing
give the actual canonical polynomial identity
\[
\boxed{
h_{a,n}\widehat Q_a
=c_{a,n}C_aH_n\,\widehat Q_n,\qquad
c_{a,n}=\frac{(a)_3}{[n(n-1)]^4}.}
\tag{DF.20}
\]
First-coordinate homogeneity extends the affine calculation
to a polynomial identity. At \(a=3\) the individual
right-hand homogenizations have row degree four and are
rational on the chart; their displayed combinations
extend polynomially because they are the actual left
side. Independence and rank may be checked on this dense
chart, so no individual extension is assumed there.

Apply the injective independent-row morphism to the
right-hand dehomogenized expression. Its rank is exactly
\[
\operatorname{rank}(C_aH_nC_n).
\tag{DF.21}
\]
The omitted factors \(c_{a,n}\) and \((n)_3\) are nonzero.
If both row counts are at least six, both \(C\)'s and
\(H_n\) are invertible. If precisely one row count is
at least six, invertibility of that \(C\) and \(H_n\)
gives rank equal to the smaller finite dimension.
The same conclusion for a source row count three and
a target row count at least six follows from the full
row rank of \(C_3\).

The remaining finite ordered pairs and exact leading
nonzero minors of (DF.21) are
\[
\begin{array}{c|c|c}
(a,n)&\text{minor size}&\text{minor}\\ \hline
(3,4)&1&16\\
(3,5)&1&320/27\\
(4,4)&2&-27/4\\
(4,5)&2&-110/27\\
(5,5)&3&-32768/28125.
\end{array}
\tag{DF.22}
\]
These follow by substituting into the printed rational
matrices. Reverse pairs have the same rank under the
actual scalar-one transpose pairing. This proves
\(\min(r_a,r_n)\) throughout the asserted domain.

For \(a,n\ge6\), in column coordinates an actual preimage
under \(h_{n,a}\) of target coordinate column \(v\) is
\[
c_{n,a}^{-1}(C_n^{-1})^t(H_a^{-1})^t v.
\tag{DF.23}
\]
For finite endpoints (DF.16) and the minors (DF.22)
give the exact smaller linear systems. Alternatively,
on each surjective rational tensor component, the
canonical adjoint formula
\(h_{a,n}(h_{n,a}h_{a,n})^{-1}\) is a rational right
inverse: the standard positive tensor pairing identifies
the two maps as adjoints, so their composition on the
target is positive definite there. The full rank was
proved in (DF.21)–(DF.22), and its inverse is the
ordinary adjugate divided by its nonzero determinant.

## 5. The entire cubic extension and its exact image

Under (DF.9), the cubic extension is precisely the
space whose independent-row polynomial has no fourth
moments. In (DF.10) these are columns one and three
of \(C_a\), because \(F_1\) is linear and \(F_3\) is
quadratic in the independent fourth moments; the
two other \(F_j\)'s use only moments through degree three.
Their patterns are independent, so both coefficients
must vanish.

The relevant two-column matrix has rank one at \(a=3,4\)
and rank two at every \(a\ge5\). The latter follows from
the explicit leading two-by-two minor
\[
\frac{(a-4)(a-3)(a-1)}{2a^4}\ne0.
\tag{DF.24}
\]
Combining this with \(r_a\) proves extension dimension
one at \(a=4,5\), and two at every \(a\ge6\).

Explicit cubic vectors are
\[
\begin{aligned}
J_a&=aQ_2+2Q_0,\\
K_a&=2(a-2)(a^2-3a+6)Q_0
 -2a(a^2-3a+3)Q_1+a^2(a-1)Q_3 .
\end{aligned}
\tag{DF.25}
\]
Their two forbidden columns vanish identically.
For \(a\ge6\) they are independent since the \(Q_j\)'s
are independent and only \(J_a\) has a \(Q_2\) term.
At \(a=4\), \(K_a=4J_a\); at \(a=5\), \(K_a=8J_a\),
by (DF.16). The moment row of \(J_a\) is nonzero in
both cases. Thus (DF.25) spans the entire extension.
Its separate row degree at most three follows from
the exact filtration equality (DF.9), so homogenizing
with \(u^3\) is an actual polynomial map.

The complete independent-row identities are
\[
\begin{aligned}
\mathcal E_a(J_a)
 &=(a)_3(a-3)(2F_0+F_2),\\
\mathcal E_a(K_a)
 &=(a)_3\{2(a-3)(a^3-9a^2+24a-12)F_0
            +4(a-3)^2F_2\}.
\end{aligned}
\tag{DF.26}
\]
They follow by the indicated row combinations of (DF.11).
For three split factors, the actual moments through
degree three give
\(F_0=Q_{0;3}/1296\) and \(F_2=-Q_{2;3}/54\).
The first line of (DF.16) says \(Q_{2;3}=-2Q_{0;3}/3\).
Consequently
\[
\boxed{
\begin{aligned}
h_{a,3}\widehat J_a
 &=\frac{(a)_3(a-3)}{72}\,\widehat Q_{0;3,a},\\
h_{a,3}\widehat K_a
 &=\frac{(a)_3(a-3)(a^3-9a^2+56a-108)}
         {648}\,\widehat Q_{0;3,a}.
\end{aligned}}
\tag{DF.27}
\]
Fourth moments cancel before this specialization; no
division by a zero \((3)_4\) occurs.
The first scalar is nonzero for all \(a\ge4\), and
\(Q_{0;3}\ne0\): the centered rows \(e_1,e_2,-e_1-e_2\)
give determinant three and \(Q_{0;3}=9\).
The source multiplicity under the transposed map is
one, by the finite \(a=3\) row space with inner degree
at least four. Thus the actual image rank is exactly
one, proving (DF.2).

## 6. Quadratic endpoint and transport

For \(n=2,a\ge6\), the generic symmetric three-by-three
matrix \(Z\) has the polynomial highest vector
\[
\Delta_1(Z)^{a-6}\Delta_3(Z)^2,
\tag{DF.28}
\]
where \(\Delta_i\) is its leading principal minor.
It has degree \(a\) and weight \((2a-8,4,4)\).
The exact LDL chart and normalized polarization map
QD.11–QD.12 prove that this highest space has dimension
one: on the dense chart \(Z=L\,\operatorname{diag}(d_i)L^t\),
unipotent invariance and the torus weight determine
the unique diagonal monomial, and (DF.28) extends it.
The source has outer degree two, so its three-row
column antisymmetrizer is zero. Its actual canonical
image is therefore zero.

All formulas are rational and natural tensor maps.
Their Young projections and multiplicity matrices
hold in every rank at least three; in smaller rank
the three-row Schur component is zero.
The exact coordinate-ring map is R-037 EP.3–EP.5,
and its frame-torsor/representation-\(K_0\) transport,
with the fixed SGA 6, SGA 3 and EGA II locators, is
R-036 §5. The actual rank statements are supplied by
(DF.20) and (DF.27), before any such transport.

## 7. Exact computational checks

The symbolic reconstruction script
`derive_double_four_moment_matrix.py` verifies every
coefficient of (DF.10) through the literal equality
partitions (DF.13), and factors (DF.15).
It does not interpolate in \(a\).

The separate verifier `verify_double_four_canonical_block.py`
uses actual product linear forms and exact multinomial
pairings. It expands the raw central expressions, then
sums the assignments of their labeled factors to rows
by a finite multivariate recurrence. This recurrence
does not use the moment-partition reconstruction or
the proposed matrix. Its population configurations have
the full independently checked finite generator rank,
and the first coordinates are nonunit.
The full-matrix and cubic receipts are
`DOUBLE_FOUR_CANONICAL_MATRIX_CHECK.tsv` and
`DOUBLE_FOUR_CUBIC_CANONICAL_CHECK.tsv`.
Changed arbitrary higher moments independently check
all required cancellation at the tested endpoints.
All 180 full-matrix generator pairings and all 20 cubic
generator pairings pass. The exact finite relations, five
canonical minors, split determinant and cubic identities
are separately certified by `check_double_four_endpoints.py`
in `DOUBLE_FOUR_ENDPOINT_CERTIFICATE.json`.

A separate literal cycle-index/Murnaghan–Nakayama
comparison checks the target and source multiplicities,
including the quadratic and cubic endpoints, in
`DOUBLE_FOUR_MN_CHECK.tsv`. These coefficient comparisons
pass all 21 target and all 21 source cases and
do not substitute for the actual matrix rank proof.

