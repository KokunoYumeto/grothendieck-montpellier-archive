# A second higher-row width-four family

## R-040. The tails \((4,3,2^{m-3},1)\)

Let \(m\ge3\), \(a\ge m+2\), \(n\ge3\), and
\(\dim V\ge m+1\). Set
\[
\nu=(4,3,2^{m-3},1),\qquad
\lambda=(an-2m-2,4,3,2^{m-3},1).
\tag{HC.1}
\]
The first part is at least \(m+4\), so this is a partition.
The exact target and canonical-image multiplicities are
\[
\boxed{
a_{a,n}^{\lambda}=1,\qquad
\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}
=\begin{cases}1,&n\ge m+2,\\0,&3\le n\le m+1.\end{cases}}
\tag{HC.2}
\]
The proof supplies the actual normalized scalar and its inverse.
All parameter ranges here are unconditional; no historical
novelty claim is made.

## 1. The invariant unit bound and the finite exceptional row count

Use R-039's explicit surjection
\[
\operatorname{Sym}(\Lambda^2T\oplus\Lambda^4T)
\otimes\Lambda(\Lambda^3T)
\twoheadrightarrow(\Lambda(\mathfrak h_a\otimes T))^{S_a},
\qquad \dim T=4.
\tag{HC.3}
\]
Its row power-sum generators, signed equality-partition
spanning argument, and the skew-Cauchy Young projectors
are given in HO.3–HO.5. The transpose of the present tail
is \(\gamma=(m,m-1,2,1)\).

Only even exterior degrees of \(\Lambda(\Lambda^3T)\)
can contribute. Exterior degree zero contributes only
paired-row shapes \((p+l,p+l,q+l,q+l)\), by the exact
Pfaffian decomposition HO.5, and therefore misses
\(\gamma\). Exterior degree four is \((\det T)^3\),
so its fourth part is at least three and it also misses
\(\gamma\). The actual exterior contraction map gives
\[
\Lambda^2(\Lambda^3T)=(\det T)\otimes\Lambda^2T.
\tag{HC.4}
\]
Thus exterior degree two reduces to a vertical two-strip
from
\((p+l+1,p+l+1,q+l+1,q+l+1)\).
The final fourth part one forces \(q=l=0\).
The unequal first two parts force \(p=m-2\), with one
box in row one; the other box must be in row three.
This is the unique strip. The exterior Pieri maps
are the column inclusions followed by rational Young
projections, each with multiplicity one. Consequently
\[
\dim(S_\nu\mathfrak h_a)^{S_a}\le1
\quad\text{for every }a.
\tag{HC.5}
\]

One finite row count is needed for the zero endpoint.
When \(a=m+1\), the space \(W=\mathfrak h_a\) has
dimension \(m\). The complementary-column pairing in
the rectangle \((4^m)\) gives the actual isomorphism
\[
S_\nu W=(\det W)^4\otimes
S_{(3,2^{m-3},1,0)}W^*.
\tag{HC.6}
\]
This is induced by the perfect pairings
\(\Lambda^rW\otimes\Lambda^{m-r}W\to\det W\),
one for each of the four columns, followed by the
corresponding Young projectors. The fourth determinant
power is trivial on \(S_a\); the invariant dot product
on \(W\) identifies its dual with \(W\).
The three-column invariant-algebra surjection CT.4
and its explicitly decomposed source CT.5–CT.6 have
only tails \((2^j)\) and \((3,2^j)\). They exclude
\((3,2^{m-3},1)\). Thus the invariant space in (HC.6)
is zero. This proves the exact finite-row vanishing
without deducing it from a vanishing candidate vector.

## 2. The centered tensor and its highest weight

For centered rows \(z_i=w_i-\bar w\in\mathbb Q^m\), put
\[
S=\sum_i z_i z_i^t,\qquad
C_{pqr}=\sum_i(z_i)_p(z_i)_q(z_i)_r.
\]
For invertible \(S\), write \(G=S^{-1}\) and define
\[
A_{ij,kl}=\det(S)(G_{ik}G_{jl}-G_{il}G_{jk}).
\tag{HC.7}
\]
These expressions are the complementary minors of order
\(m-2\), with their alternating cofactor signs.
They therefore define polynomials at every \(S\).
Equivalently this follows by expanding the coefficient
of a two-entry perturbation of \(\det S\).
Set
\[
\mathcal F_{pqr}^{\,s}
=\sum_{i,j,k}C_{pqi}C_{rjk}A_{ij,ks},
\qquad
F_{a,m}=\mathcal F_{112}^{\,m}-\mathcal F_{121}^{\,m}.
\tag{HC.8}
\]

The transformation of (HC.7) under \(S\mapsto gSg^t\)
is \((\det g)^2\) times four contravariant indices.
Contracting it with the two third tensors leaves
three covariant indices and one contravariant index.
The difference in (HC.8) has free covariant labels
\(1,1,2\), and its dual label is \(m\).
The raising operator \(E_{12}\) sends each displayed
summand to \(\mathcal F_{111}^{\,m}\), so it kills
their difference. Every other raising operator kills
both terms: there is no covariant label above two
and the dual label is already \(m\).
Its diagonal weight is
\[
(2,\ldots,2)+2e_1+e_2-e_m
=(4,3,2^{m-3},1)=\nu.
\tag{HC.9}
\]
This proves the exact highest-weight equations.
The tensor is also row-symmetric and translation invariant
by its definition in centered row sums.

## 3. A weighted affine-minor identity and its degree-three cancellation

Let \(R\) have rows
\((1,w_{i1},\ldots,w_{im})\).
Let \(B_1\) and \(B_2\) have rows
\[
(1,w_{i1},\ldots,w_{i,m-1},w_{i1}^2),
\qquad
(1,w_{i1},\ldots,w_{i,m-1},w_{i1}w_{i2}),
\]
respectively. The assumption \(m\ge3\) ensures that
both linear columns \(w_1,w_2\) occur in each \(B\).
For \(|I|=m+1\), define
\[
L_{I,p}=(a-m-1)\sum_{i\in I}w_{ip}
-(m+1)\sum_{i\notin I}w_{ip}.
\]
The polynomial
\[
\boxed{
D_{a,m}:=-a^2F_{a,m}
=\sum_{|I|=m+1}\det R_I
\bigl(L_{I,2}\det(B_1)_I-L_{I,1}\det(B_2)_I\bigr)}
\tag{HC.10}
\]
is the exact affine-minor form of the tensor.

Here is a proof including its sign and scalar. After translating
the columns, write \(C_1=(C_{1ij})\), \(C_2=(C_{2ij})\),
\(v_1=(C_{11i})_i\), and \(v_2=(C_{12i})_i\).
The lower-right block of \(R^tB_t\) is formed from
the first \(m-1\) columns of \(S\), followed by \(v_t\);
its first column is \((a,0,\ldots,0)^t\).

Insert row weights \(1+\epsilon z_{i2}\) into
\(R^tB_1\), and weights \(1+\epsilon z_{i1}\)
into \(R^tB_2\), and subtract the determinant derivatives.
The two fourth-moment last columns are identical and
cancel. The extra Schur-complement columns are multiples
of column two or column one of \(S\), respectively,
so their determinants vanish by repeated columns.
The remaining derivative is exactly
\[
a\left(v_1^t(d\,\operatorname{adj}_S[C_2])e_m
       -v_2^t(d\,\operatorname{adj}_S[C_1])e_m\right)
=-aF_{a,m}.
\tag{HC.11}
\]
To verify the last equality directly at invertible \(S\),
\[
d\,\operatorname{adj}_S[M]
=\det(S)\{\operatorname{tr}(GM)G-GMG\}.
\]
Substitution is precisely minus the two cofactor sums
in (HC.8). Both sides are polynomial, so the identity
holds also at singular \(S\).

Weighted Cauchy–Binet computes the same derivative as
\[
\sum_I\det R_I
\left((\sum_{i\in I}z_{i2})\det(B_1)_I
      -(\sum_{i\in I}z_{i1})\det(B_2)_I\right).
\]
The determinants do not change on translating their
columns: the quadratic corrections use only \(1,w_1,w_2\),
which are present. Substituting \(z=w-\bar w\) and
multiplying by \(a\) gives exactly (HC.10).

The right side has degree at most three in each row.
For a row outside \(I\) the degree is at most one.
For a row in \(I\), all terms of degree four must
use its linear entry in \(R\), its quadratic entry
in \(B_t\), and its own entry in \(L_{I,p}\).
The cofactors of the last columns in \(B_1,B_2\)
are identical. The two row factors are
\(w_{i2}w_{i1}^2\) and \(w_{i1}(w_{i1}w_{i2})\);
they cancel term for term, with the same coefficient
\(a-m-1\). Every remaining term has degree at most
three. This verifies the finite extension directly.

## 4. A uniform nonzero specialization

Take centered rows
\[
e_1,\ldots,e_m,\quad v=e_1+2e_2,\quad
-u=-2e_1-3e_2-e_3-\cdots-e_m,
\quad a-m-2\text{ zeros}.
\tag{HC.12}
\]
Then \(u=\mathbf1+v\), \(S=I+vv^t+uu^t\), and
\[
\Delta=\det S=6m+8,\qquad
G=I-[v,u]
\begin{pmatrix}6&8\\8&m+12\end{pmatrix}^{-1}
[v,u]^t.
\tag{HC.13}
\]
Multiplication verifies this inverse, and the two-by-two
determinant gives \(\Delta\).
The third-moment slices and vectors are
\[
C_1=e_1e_1^t+vv^t-2uu^t,\quad
C_2=e_2e_2^t+2vv^t-3uu^t,\quad
v_1=e_1+v-4u,\quad v_2=2v-6u.
\]
For transparency, all scalar products needed in (HC.8)
reduce to the following six entries of (HC.13):

| Expression | Exact value |
|---|---|
| \(\operatorname{tr}(GC_1)\) | \((-2m-4)/\Delta\) |
| \(\operatorname{tr}(GC_2)\) | \((-6m-12)/\Delta\) |
| \((Gv_1)_m\) | \(-36/\Delta\) |
| \((Gv_2)_m\) | \(-52/\Delta\) |
| \((GC_2Gv_1)_m\) | \((336m+592)/\Delta^2\) |
| \((GC_1Gv_2)_m\) | \((344m+528)/\Delta^2\) |

The inverse formula gives every entry by ordinary matrix
multiplication. Substituting them into
\[
F_{a,m}=\Delta\bigl[
(GC_2Gv_1)_m-\operatorname{tr}(GC_2)(Gv_1)_m
-(GC_1Gv_2)_m+\operatorname{tr}(GC_1)(Gv_2)_m
\bigr]
\]
gives the numerator \(-120m-160=-20\Delta\).
Consequently
\[
F_{a,m}=-20,\qquad D_{a,m}=20a^2\ne0
\quad(a\ge m+2).
\tag{HC.14}
\]
The appended zero rows change neither \(S\) nor \(C\).

Put \(u_0=\prod_i x_i\), and define the homogeneous
highest polynomial
\[
\widehat D_{a,n,m}=u_0^nD_{a,m}(y_i/x_i).
\tag{HC.15}
\]
The degree-three cancellation in §3 proves that this
is polynomial for every \(n\ge3\). It has separate
degree \(n\), weight \(\lambda\), and is nonzero by
(HC.14). The first-coordinate raising equations are
its translation invariance, and the remaining equations
are (HC.9). Dehomogenization at \(x_i=1\) injects the
whole highest space into \((S_\nu\mathfrak h_a)^{S_a}\),
as explicitly proved in R-039 after HO.13.
Together with (HC.5), this proves the target multiplicity
one in (HC.2).

## 5. The normalized determinant derivative and canonical scalar

Let \(L\) be an independent-row formal functional
with first moments zero. Its second and third tensors
are denoted by \(U,C\). Extend it arbitrarily to degree
four for the following determinant derivatives; the
result will have no dependence on that extension.

In the expectation of (HC.10), every outside-row
weight vanishes by its first moment. For a fixed
subset \(I\), the expectation of its inside weighted
determinant difference is the difference of derivatives
of the two moment matrices. The exact two-determinant
permutation expansion contributes \((m+1)!\), as
in HO.14. The first column of the unweighted moment
matrix is \((1,0,\ldots,0)^t\).
The same Schur-complement computation as (HC.11),
now with upper-left entry one, gives
\(-(m+1)!F(U,C)\). Its fourth-moment last columns
cancel, and its remaining extra columns repeat one
of the first \(m-1\) columns of \(U\).
There are \(\binom a{m+1}\) subsets and an inside
coefficient \(a-m-1\). Therefore
\[
\boxed{
L^{\otimes a}(D_{a,m})=-(a)_{m+2}F(U,C).}
\tag{HC.16}
\]
The complete cancellation of the arbitrary fourth
moments makes this computation valid for a functional
originally defined only through degree three.

For a normalized split form of degree \(n\ge3\),
the exact centered moments HO.16 give
\[
U=-S_n/[n(n-1)],\qquad
C=2C_n/[n(n-1)(n-2)].
\]
The cofactor in (HC.7) has degree \(m-2\) in \(S\),
and (HC.8) has degree two in \(C\). Hence
\[
F(U,C)=
\frac{4(-1)^{m-2}}
{n^m(n-1)^m(n-2)^2}F_{n,m}.
\]
Using \(D_{n,m}=-n^2F_{n,m}\), the actual canonical
pairing now yields
\[
\boxed{
h_{a,n}\widehat D_{a,n,m}
=\frac{4(-1)^{m-2}(a)_{m+2}}
{n^{m+2}(n-1)^m(n-2)^2}\widehat D_{n,a,m}.}
\tag{HC.17}
\]
This identity uses the scalar-one normalized grid map
SR.5–SR.6. Homogeneity extends the evaluation with
first coordinates one to the dense nonzero first-coordinate
open set and then to the polynomial identity everywhere.
In particular, no degree-four moment of a cubic split
form has been assigned by a zero-denominator formula.

For \(a,n\ge m+2\), the scalar and both vectors are
nonzero. An explicit preimage of \(\widehat D_{a,n,m}\)
under \(h_{n,a}\) is
\[
\boxed{
\frac{(-1)^{m-2}a^{m+2}(a-1)^m(a-2)^2}
{4(n)_{m+2}}\widehat D_{n,a,m}.}
\tag{HC.18}
\]
For \(3\le n\le m\), source length gives zero, since
the source outer degree is \(n\) and \(\lambda\) has
\(m+1\) rows. At \(n=m+1\), the exact complement
map (HC.6) and the invariant exclusion following it
give source multiplicity zero. These facts prove
every zero endpoint in (HC.2). They also agree with
(HC.10): the subset sum is empty below \(m+1\),
and both its inside and outside coefficients vanish
at exactly \(m+1\).

All tensor, complementary-column, determinant, and
Young maps are rational. They therefore have the same
multiplicity matrices in every declared ambient rank.
R-036 §5 gives the precise frame-torsor, SGA/EGA,
representation-\(K_0\), and cote133/028 transport
for these maps. The Chow coordinate-ring realization
is the exact pullback R-037 EP.3–EP.5, in particular
the algebra morphism EP.4.

## 6. Executed finite checks

The script verify_four_three_one_tail_family.py
expands the actual weighted determinant products and
the split linear forms, and pairs their monomials
with exact multinomial denominators. The degree-four
row terms are canceled directly by their identical
quadratic-column factors, before evaluating any
inner-degree-three pairing. It checks two configurations
with nonunit first coordinates at \(a=5,6\),
\(3\le n\le6\), \(3\le m\le\min(a-2,4)\).
All 24 literal scalar checks pass. In every case the
weighted minor sum also equals \(-n^2\) times the
separately computed centered complementary-minor
tensor, including every zero endpoint.

The same script independently computes all 45 target
and 45 source coefficients for \(4\le a\le8\),
\(3\le n\le5\), \(3\le m\le a-1\). They agree
with the unit ranges and the \(a=m+1\) and
\(n=m+1\) zero endpoints. The receipts are
FOUR_THREE_ONE_TAIL_CANONICAL_CHECK.tsv and
FOUR_THREE_ONE_TAIL_MN_CHECK.tsv.
These finite checks supplement the complete unbounded
map and multiplicity proof above.
