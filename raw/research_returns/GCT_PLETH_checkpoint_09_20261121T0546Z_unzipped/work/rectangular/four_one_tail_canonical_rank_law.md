# A higher-row width-four family with an exact canonical scalar

## R-039. The tails \((4,2^{m-2},1)\)

Let \(m\ge2\), \(a\ge m+1\), \(n\ge3\), and
\(\dim V\ge m+1\). Set

\[
\nu=(4,2^{m-2},1),\qquad
\lambda=(an-2m-1,4,2^{m-2},1).
\tag{HO.1}
\]

These are partitions: the first part is at least
\(3(m+1)-2m-1=m+2\ge4\). The exact target and canonical
image multiplicities are

\[
\boxed{
a_{a,n}^{\lambda}=1,\qquad
\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}
=\begin{cases}
1,&n\ge m+1,\\
0,&3\le n\le m.
\end{cases}}
\tag{HO.2}
\]

The proof gives a polynomial highest vector, an exact scalar
for the actual normalized canonical map, and a rational
preimage in every nonzero case. The family has \(m+1\) rows,
and its second row has size four. The claim makes no historical
novelty assertion.

## 1. An actual invariant-algebra map and the unit bound

Put \(E=\mathbb Q^a\), \(W=\mathfrak h_a\), and let
\(P:E\to W\) be the sum-zero orthogonal projector. For an
auxiliary four-dimensional space \(T\), the following is a
surjective \(GL(T)\)-equivariant graded-algebra morphism:

\[
\operatorname{Sym}(\Lambda^2T\oplus\Lambda^4T)
\otimes\Lambda(\Lambda^3T)
\longrightarrow
\bigl(\Lambda(W\otimes T)\bigr)^{S_a}.
\tag{HO.3}
\]

Its degree-\(d\) generator, \(d=2,3,4\), sends
\(t_1\wedge\cdots\wedge t_d\) to
\(\sum_i(Pe_i\otimes t_1)\wedge\cdots\wedge(Pe_i\otimes t_d)\).
The even generators commute and the odd generators
anticommute, so these prescriptions give the displayed
algebra map.

Here is the complete finite-row spanning argument. In
\(\Lambda(E\otimes T)\), label the four Grassmann letters in
each row by \(1,2,3,4\). A row type is a nonempty subset of
these labels. The product of the corresponding row power sums
expands by the equality partition of its occupied row indices.
The discrete equality partition is exactly the injective
row-assignment sum for the chosen types. All other terms
merge at least two row types and use fewer occupied rows;
overlapping types give zero, and disjoint types give their
literal exterior sign. Induction on the number of occupied
rows expresses every injective assignment sum in the power
sums. Every nonzero invariant orbit average is a nonzero
rational multiple of one of these sums. Two equal odd row
types give zero average, since their interchange has sign
minus one; the other stabilizers only give nonzero factorial
factors. This proves spanning including all finite \(a\).
The equivariant projection \(E\to W\) is surjective on
exterior algebras and on invariants, by the equivariant
inclusion \(W\hookrightarrow E\). It kills the singleton
power sums. The remaining generators are precisely (HO.3).

The rational skew-Cauchy Young projectors give the actual
decomposition

\[
\bigl(\Lambda(W\otimes T)\bigr)^{S_a}
=\bigoplus_{\eta_1\le4}
(S_\eta W)^{S_a}\otimes S_{\eta^t}T.
\tag{HO.4}
\]

We determine the multiplicity of
\(\gamma=\nu^t=(m,m-1,1,1)\) in the source of (HO.3).
We use the following explicit description:

\[
\operatorname{Sym}^d(\Lambda^2T)
\simeq
\bigoplus_{q=0}^{\lfloor d/2\rfloor}
S_{(d-q,d-q,q,q)}T.
\tag{HO.5}
\]

For completeness, its polynomial maps are obtained as
follows. In the six variables \(X_{ij}\), \(1\le i<j\le4\),
the Pfaffian
\(Q=X_{12}X_{34}-X_{13}X_{24}+X_{14}X_{23}\)
is a \(GL(T)\) determinant vector. Map \(X_{ij}\) to the
\(ij\) minor of a generic two-by-four matrix. The kernel is
\((Q)\): on the chart \(X_{12}\ne0\) the Plücker equation
solves for \(X_{34}\), and every remaining coordinate choice
is realized by a matrix with its first two columns independent.
The quadric \(Q\) is irreducible (its associated bilinear
matrix has rank six), so this chart is dense in the prime
quadric and gives the kernel everywhere.

The degree-\(d\) quotient has the standard two-row tableau
basis for \(S_{(d,d)}T\). To see this in the same coordinates,
order each two-entry minor column increasingly. Among the
two-subsets of \([4]\), the only incomparable pair is
\((1,4),(2,3)\). The replacement
\(X_{14}X_{23}=X_{13}X_{24}-X_{12}X_{34}\) decreases
both offending exponents and introduces neither of them,
so repeated replacement terminates. Comparable
products correspond to semistandard tableaux of shape
\((d,d)\). Their diagonal matrix monomials are distinct,
so these products are independent. The multiplication map
from tensor columns is equivariant and sends the highest
column tensor \((e_1\wedge e_2)^{\otimes d}\) to
\(X_{12}^d\ne0\). Its cyclic highest submodule is a copy
of \(S_{(d,d)}T\), equivalently the image of its rational
Young projector. The semistandard tableau count is the
dimension of this same Schur module. The resulting
nonzero Schur map is therefore an isomorphism onto the
degree-\(d\) quotient.
Consequently multiplication by \(Q\) gives the exact
degree sequence with quotient \(S_{(d,d)}T\).
Complete reducibility splits it; iteration, retaining
the determinant character of each \(Q\), proves (HO.5)
with precisely the displayed multiplicities.

In addition,
\(\Lambda^3T=(\det T)\otimes T^*\), by exterior
contraction. The exterior powers of this four-dimensional
module give, in particular,

\[
\Lambda^1(\Lambda^3T)=\Lambda^3T,\qquad
\Lambda^3(\Lambda^3T)=(\det T)^2\otimes T.
\tag{HO.6}
\]

The total degree \(|\gamma|=2m+1\) is odd. Thus only
exterior degrees one and three can occur in (HO.3).
Exterior degree three has a determinant-square factor,
so all resulting fourth parts are at least two; it
cannot contribute to \(\gamma_4=1\).

For exterior degree one, let \(l\) be the number of
\(\Lambda^4T\) generators. The other factor, by (HO.5),
has shape \((p+l,p+l,q+l,q+l)\), \(p\ge q\ge0\).
Tensoring with \(\Lambda^3T\) adds a vertical three-strip.
This is the actual exterior Pieri map obtained by column
antisymmetrization and the rational Young projector;
each admissible strip has multiplicity one. Since
\(\gamma_4=1\), one has \(l\le1\). At \(l=1\),
subtracting its determinant leaves
\((m-1,m-2,0,0)\); a vertical three-strip cannot lie
in this two-row shape. At \(l=0\), the unique possibility
is

\[
(p,p,q,q)=(m-1,m-1,0,0),\qquad
\text{added rows }1,3,4.
\tag{HO.7}
\]

Indeed the unequal first two parts force the addition in
row one only, and the equal last two parts equal to one
then force their two additions. This gives one copy
also at \(m=2\). Equations (HO.3)–(HO.7) prove

\[
\dim(S_\nu\mathfrak h_a)^{S_a}\le1
\quad\text{for every }a.
\tag{HO.8}
\]

## 2. The centered highest vector and its affine-minor identity

Take \(a\) row vectors \(w_i\in\mathbb Q^m\), and put
\[
\bar w=\frac1a\sum_iw_i,\quad z_i=w_i-\bar w,\quad
S=\sum_i z_i z_i^t,\quad
C_{pqr}=\sum_i(z_i)_p(z_i)_q(z_i)_r.
\]
Define

\[
H_{a,m}=\sum_{i=1}^m C_{11i}\operatorname{adj}(S)_{im}.
\tag{HO.9}
\]

This polynomial is invariant under permutations of the
rows and under common translations. Its complete tensor
\(\sum_iC_{pqi}\operatorname{adj}(S)_{ir}\) transforms
as \((\det\mathbb Q^m)^2\otimes
\operatorname{Sym}^2(\mathbb Q^m)\otimes(\mathbb Q^m)^*\).
The formula follows by substituting \(S\mapsto gSg^t\),
\(C\mapsto g^{\otimes3}C\), and the identity
\(\operatorname{adj}(gSg^t)
=(\det g)^2g^{-t}\operatorname{adj}(S)g^{-1}\).
The latter follows for invertible \(S\) by multiplication,
and then for every \(S\) by polynomial continuation.

The component \(p=q=1,r=m\) is killed by all raising
operators \(\sum_i(w_i)_p\partial_{(w_i)_q}\), \(p<q\):
the two covariant indices are already one, and the dual
index is already \(m\). Its diagonal weight is
\((4,2,\ldots,2,1)=\nu\). This is the literal highest
component inside the indicated tensor module.

Let \(R\) and \(B\) be the \(a\)-by-\((m+1)\) matrices
whose \(i\)-th rows are
\[
r_i=(1,(w_i)_1,\ldots,(w_i)_m),\qquad
b_i=(1,(w_i)_1,\ldots,(w_i)_{m-1},(w_i)_1^2).
\]
Then

\[
\boxed{
A_{a,m}:=aH_{a,m}
=\sum_{\substack{I\subseteq[a]\\ |I|=m+1}}
\det R_I\,\det B_I.}
\tag{HO.10}
\]

To prove this equality, apply the determinant-one
translation column operation to \(R\). Apply it to
the linear columns of \(B\), and replace its last
column by \(w_1^2-2\bar w_1w_1+\bar w_1^2=z_1^2\).
This column operation is available because \(m\ge2\)
and \(B\) contains its \(w_1\) column. The determinant
of \(R^tB\) is unchanged. Its first column is now
\((a,0,\ldots,0)^t\); its lower-right block has the
first \(m-1\) columns of \(S\), followed by the column
\((C_{i11})_i\). Expanding first in the first column
and then in the last column gives \(aH_{a,m}\), with
no cofactor sign left over. Cauchy–Binet for
\(R^tB\) gives exactly the right side of (HO.10).

Each row has degree at most one in \(\det R_I\)
and at most two in \(\det B_I\). Thus \(A_{a,m}\)
has degree at most three in every row. It is nonzero
for every \(a\ge m+1\): use centered rows

\[
e_1,e_2,\ldots,e_m,-e_1-\cdots-e_m,
\quad a-m-1\text{ zero rows}.
\tag{HO.11}
\]

Here \(S=I+\mathbf1\mathbf1^t\), so
\(\operatorname{adj}(S)=(m+1)I-\mathbf1\mathbf1^t\),
and \((C_{11i})_i=(0,-1,\ldots,-1)^t\).
The last component of their product is \(-2\).
Therefore \(H_{a,m}=-2\) and \(A_{a,m}=-2a\).

For slots \((x_i,y_i)\), \(u=\prod_i x_i\), define
\[
F_{a,n,m}=u^n A_{a,m}(y_i/x_i).
\tag{HO.12}
\]
This is a polynomial for every \(n\ge3\). More explicitly,
let \(X_I\) have rows \((x_i,y_{i1},\ldots,y_{im})\),
and let \(Y_I\) have rows
\((x_i^2,x_iy_{i1},\ldots,x_iy_{i,m-1},y_{i1}^2)\).
Then

\[
F_{a,n,m}=u^{n-3}\!
\sum_{|I|=m+1}
\left(\prod_{i\notin I}x_i\right)^3
\det X_I\,\det Y_I.
\tag{HO.13}
\]

Every slot has degree exactly \(n\). The two determinant
signs cancel under row permutations. Translation
invariance gives the raising equations from the first
coordinate, and the lower-coordinate calculation gives
all other raising equations. Its highest weight is
therefore the partition \(\lambda\) in (HO.1).
Specializing \(x_i=1\) recovers \(A_{a,m}\), so it
is nonzero.

The exact dehomogenization map evaluates all \(x_i=1\).
Separate homogeneity makes it injective on the fixed
slot degrees. The first-coordinate raising equations
become common-translation invariance, and the remaining
ones give the highest lower weight \(\nu\).
Taking the sum-zero representatives \(z_i=w_i-\bar w\)
is the inverse linear coordinate map on that translation
quotient. The ordinary Cauchy Young projectors on
the polynomial algebra of \(W\otimes\mathbb Q^m\)
identify its highest-\(\nu\) invariant space with
\((S_\nu\mathfrak h_a)^{S_a}\).
This proves the claimed embedding directly; it is the
localized map used in T-032. Its inverse on the present
vector is (HO.12), and (HO.13) proves its finite-degree
extension even when \(n=3<\nu_1\).
Thus (HO.8) and the
nonzero vector prove the target multiplicity one
in (HO.2) for every declared parameter.

## 3. Independent-slot determinant pairing

Let \(L\) be a formal row functional, of total degrees
at most three, with \(L(1)=1\), \(L(w_p)=0\).
Denote its second and third moments by
\(\mu_{pq}=L(w_pw_q)\) and
\(\mu_{pqr}=L(w_pw_qw_r)\).
Apply \(L\) independently to each row of (HO.10).
For each subset \(I\) of size \(m+1\), expanding both
determinants gives
\[
L^{\otimes(m+1)}(\det R_I\det B_I)
=(m+1)!\det M,\qquad M_{pq}=L(r_p b_q).
\tag{HO.14}
\]
Indeed fix the first determinant permutation; changing
the second relative to it gives the determinant of
the pairing matrix, with identical sign. There are
exactly \((m+1)!\) first permutations. This proves
both the matrix and its full factor.

The first column of \(M\) is \((1,0,\ldots,0)^t\).
Its lower-right block is the \(m\)-by-\(m\) matrix
with entries
\[
M'_{pq}=\mu_{pq}\quad(q<m),\qquad
M'_{pm}=\mu_{p11}.
\]
There are \(\binom a{m+1}\) subsets, so

\[
L^{\otimes a}(A_{a,m})
=(a)_{m+1}\det M'.
\tag{HO.15}
\]

Here \((a)_{m+1}=a(a-1)\cdots(a-m)\). This derivation
uses the actual row polynomial and does not require
probability or positivity assumptions on its moments.

## 4. The exact canonical scalar, inverse, and zero endpoints

Take the product \(Q=\prod_{k=1}^n(1,v_k)\), where
\(v_k\in\mathbb Q^m\). The normalized tensor pairing
of SR.5–SR.6 is the independent-slot functional on
(HO.12). Translation invariance permits centering
the \(v_k\). For \(\sum_kv_k=0\), the exact moments are

\[
\mu_{pq}=-\frac{\sum_k(v_k)_p(v_k)_q}{n(n-1)},
\qquad
\mu_{pqr}=
\frac{2\sum_k(v_k)_p(v_k)_q(v_k)_r}{n(n-1)(n-2)}.
\tag{HO.16}
\]

These identities follow by expanding the ordered
distinct-index sums. At order two, the full sum is
zero and removal of the equal-index terms gives the
minus sign. At order three, subtracting the three
pair coincidences and adding the triple coincidence
leaves two copies of the diagonal third sum. The
ordered sums have respectively \(n(n-1)\) and
\(n(n-1)(n-2)\) terms. This argument includes all
repeated coordinate labels in \(\mu_{11i}\).

Factor the first scalar in (HO.16) out of the first
\(m-1\) columns of \(M'\), and the second out of
its last column. The remaining determinant is
\(H_{n,m}=A_{n,m}/n\), by the last-column expansion
already proved. Consequently (HO.15) gives the
actual normalized polynomial identity

\[
\boxed{
h_{a,n}F_{a,n,m}
=c_{a,n,m}F_{n,a,m},\qquad
c_{a,n,m}=
\frac{2(-1)^{m-1}(a)_{m+1}}
{n^{m+1}(n-1)^m(n-2)}.}
\tag{HO.17}
\]

It holds for \(a\ge m+1,n\ge3\), including the zero
target endpoints. Equality at first coordinates one
extends by separate homogeneity to their dense
nonzero open set, and hence everywhere as a
polynomial identity. This proves (HO.17) for the
specified canonical morphism, with no uncomputed
change of bases.

For \(a,n\ge m+1\), both generator lines are nonzero
and the scalar is nonzero. An actual preimage of
\(F_{a,n,m}\) under \(h_{n,a}\) is

\[
\boxed{
\frac{(-1)^{m-1}a^{m+1}(a-1)^m(a-2)}
{2(n)_{m+1}}F_{n,a,m}.}
\tag{HO.18}
\]

For \(3\le n\le m\), the sum defining \(A_{n,m}\)
is empty. More precisely, the source
\(\operatorname{Sym}^n\operatorname{Sym}^aV\)
is a submodule of \((\operatorname{Sym}^aV)^{\otimes n}\).
Successive horizontal-strip Pieri inclusions have
at most \(n\) rows, while \(\lambda\) has \(m+1>n\)
rows. Its source multiplicity is zero. Its target
multiplicity remains one by §2. This proves the
zero-image line of (HO.2), and completes the exact
rank law.

All these constructions use rational tensor, Young,
and determinant maps. The same fixed multiplicity
maps occur in every dimension at least \(m+1\).
Applying the frame-torsor and exact representation
\(K_0\) constructions specified, with primary
SGA/EGA locators, in R-036 §5 transports (HO.17)
and its explicit inverse to the associated bundles.
The coordinate pullback is exactly R-037 EP.3–EP.5,
with its algebra morphism in EP.4;
thus the polynomial functions also give the stated
nonzero Chow coordinate-ring classes.

## 5. Executed finite verification

The script verify_four_one_tail_family.py expands the two
determinants in (HO.13), expands the product linear
form, and pairs every slot monomial with its exact
multinomial denominator. It uses two configurations,
with nonunit first coordinates, for every
\(3\le a,n\le6\), \(2\le m\le\min(a-1,4)\).
One configuration realizes (HO.11), so the stated
nonzero and zero endpoints are both checked. It
also compares the affine-minor sum directly with
the centered Cramer determinant in every case.

The same script independently computes the actual
source and target coefficients by cycle-index
expansion and Murnaghan–Nakayama for every
\(3\le a\le7\), \(3\le n\le5\), \(2\le m\le a-1\).
All 72 literal polynomial pairings and their affine/Cramer
comparisons pass. All 45 target and 45 source coefficients
agree with (HO.2). The receipts are
FOUR_ONE_TAIL_CANONICAL_SCALAR_CHECK.tsv and
FOUR_ONE_TAIL_MN_CHECK.tsv.
The exact scalar and multiplicity proofs above
establish the unbounded families.
