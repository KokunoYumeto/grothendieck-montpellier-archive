# A complete three-dimensional higher-row canonical block

## R-041. The tails \((4,2^{m-1})\)

Let \(m\ge2\), \(a\ge m+1\), \(n\ge4\), and \(\dim V\ge m+1\).
Define
\[
\lambda=(an-2m-2,4,2^{m-1}),\qquad
r_t=\min(3,\max(0,t-m)).
\tag{QE.1}
\]
The first part is at least \(2m+2\ge4\).
The exact target and canonical-image multiplicities are
\[
\boxed{
a_{a,n}^{\lambda}=r_a,\qquad
\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}
=\min(r_a,r_n).}
\tag{QE.2}
\]
In particular, the full three-dimensional target component is reached
for every \(a,n\ge m+3\). The proof gives its explicit three-by-three
canonical matrix and inverse, as well as all one- and two-dimensional
endpoint ranks. No historical novelty assertion is made.

## 1. Three centered highest polynomials and their row degrees

Use centered rows \(z_i=w_i-\bar w\in\mathbb Q^m\), and put
\[
S=\sum_i z_i z_i^t,\quad
C=(\sum_i z_{i1}z_{ip}z_{iq})_{pq},\quad
D=(\sum_i z_{i1}^2z_{ip}z_{iq})_{pq}.
\]
Define
\[
P_1=S_{11}\det S,\qquad
P_2=\operatorname{tr}(\operatorname{adj}(S)D),\qquad
P_3=[t^2]\det(S+tC).
\tag{QE.3}
\]
These are polynomials also at singular \(S\).
At invertible \(S\), with \(G=S^{-1}\), the last is
\[
P_3=\frac{\det S}{2}
\left((\operatorname{tr}(GC))^2-\operatorname{tr}(GCGC)\right).
\tag{QE.4}
\]
The determinant's second derivative, or its two-permutation expansion,
proves this formula and its factor.

All three are row-symmetric and translation invariant. They are highest
polynomials of lower weight \((4,2^{m-1})\): each has determinant-square
weight \((2^m)\), with two additional covariant indices equal to one.
For \(P_2\) these are the two uncontracted indices of the fourth tensor;
for \(P_3\) they are the two uncontracted indices of its third-tensor
slices. Adjugate congruence and the complementary-minor version of
(QE.4) give the exact tensor transformations. All raising operators
therefore kill these components.

Here are polynomial maps proving the separate degree bound.
Let \(R\) have rows \((1,w_i)\), let \(k=m+1\), and write
\(f_I=\det R_I^2\). Put \(s_i=z_{i1}\), and define
\[
\begin{aligned}
A&=(\sum_i s_i^2)\sum_{|I|=k}f_I,\\
B&=\sum_{|I|=k}(\sum_{i\in I}s_i^2)f_I,\\
C'&=\sum_{|I|=k}e_2((s_i)_{i\in I})f_I.
\end{aligned}
\]
Then
\[
\boxed{A=aP_1,\qquad B=P_1+aP_2,\qquad C'=aP_3-P_1.}
\tag{QE.5}
\]
For the first equality, centered Cauchy–Binet gives
\(\det(R^tR)=a\det S=\sum_I f_I\).
For the second, insert row weights \(1+t s_i^2\).
The first determinant derivative has top-left contribution
\(S_{11}\det S\), and lower-block contribution
\(a\operatorname{tr}(\operatorname{adj}(S)D)\).
Weighted Cauchy–Binet gives exactly \(B\).
For the third, insert weights \(1+t s_i\). Its centered Gram matrix is
\[
\begin{pmatrix}a&t(Se_1)^t\\tSe_1&S+tC\end{pmatrix}.
\]
The Schur-complement determinant, through degree two, is
\(a\det(S+tC)-t^2\det S\,S_{11}\).
Weighted Cauchy–Binet gives \(C'\) as the coefficient of \(t^2\).
This proves (QE.5), with its signs. The invertible-matrix calculation
extends polynomially to singular matrices.

Each \(f_I\) has degree at most two in each row. Each displayed weight
has degree at most two in every row, even after expanding the common
mean. Thus \(A,B,C'\), and hence all \(P_j\), have row degree at most four.

For slots \((x_i,y_i)\), let \(u=\prod_i x_i\) and
\[
\widehat P_{j;a,n,m}=u^nP_j(y_i/x_i).
\tag{QE.6}
\]
These are polynomial highest vectors of weight \(\lambda\) for
\(n\ge4\). Dehomogenization gives the literal inverse on their span
and is injective on the whole fixed-degree highest space.

## 2. The invariant bound and exact finite-row restriction

In the four-column invariant algebra HO.3, the transpose of the present
tail is \(\gamma=(m,m,1,1)\). Exterior degree zero contributes twice:
in the paired shape \((p+l,p+l,q+l,q+l)\), take
\((l,q,p)=(0,1,m)\) or \((1,0,m-1)\).
Exterior degree two uses
\(\Lambda^2(\Lambda^3T)=(\det T)\otimes\Lambda^2T\).
The fourth part one forces \(q=l=0\), and the unique vertical
two-strip adds rows one and two to \((m-1,m-1,1,1)\).
Equivalently \(p=m-2\) in the paired shape before the determinant
factor. Exterior degree four has fourth part at least three.
These exhaustive exterior/Pieri maps, with HO.5's exact Pfaffian
decomposition, prove
\[
\dim(S_{(4,2^{m-1})}\mathfrak h_a)^{S_a}\le3.
\tag{QE.7}
\]

We also need actual surjectivity when reducing the number of rows.
For \(A_0\ge a\), let
\(\iota:\mathfrak h_a\hookrightarrow\mathfrak h_{A_0}\)
pad a vector by zeros, and let \(q=\iota^t\) for the ordinary invariant
dot products. Explicitly
\[
q(P_{A_0}e_i)=
\begin{cases}P_a e_i,&i\le a,\\0,&i>a.\end{cases}
\tag{QE.8}
\]
The exterior map \(\Lambda(q\otimes1_T)\) therefore sends every row
power-sum generator in HO.3 with \(A_0\) rows to its generator with
\(a\) rows. Those generators span the entire finite-row invariant
algebra, by HO.3's signed equality-partition proof.
Thus the map sends the \(S_{A_0}\)-invariant algebra onto the
\(S_a\)-invariant algebra. It is \(GL(T)\)-equivariant.
Taking the actual skew-Cauchy Young summand of weight \(\gamma\)
gives the corresponding surjection on \(S_\nu\)-invariants.

Under the invariant dot products, its polynomial realization is
restriction to \(\iota(\mathfrak h_a)\). There the rows sum to zero,
so padding zeros changes neither \(S,C,D\). Consequently
\[
P_{j;A_0}|_{\iota(\mathfrak h_a)}=P_{j;a}\quad(j=1,2,3)
\tag{QE.9}
\]
with scalar one. This exact map will establish spanning at every
finite row count.

## 3. The exact independent-row matrix

Let \(L\) have first moments zero, with arbitrary second, third and
fourth moments. Denote its second matrix by \(U\), its first-coordinate
third slice by \(C_0\), and its twice-first-coordinate fourth slice by
\(D_0\). Write
\[
Q=U_{11}\det U,\quad
R=\operatorname{tr}(\operatorname{adj}(U)D_0),\quad
T=[t^2]\det(U+tC_0).
\]
For each fixed \(I\) of size \(k=m+1\), put
\(T_I=\sum_{i\in I}w_{i1}\), \(U_I=\sum_{i\in I}w_{i1}^2\),
and use \(T_{\rm all},U_{\rm all}\) for the entire row set.
Let \(l=a-k\). The following expectation table is divided by \(k!\):

| Polynomial paired with \(f_I\) | Value after division by \(k!\) |
|---|---|
| \(1\) | \(\det U\) |
| \(U_I\) | \(Q+R\) |
| \(T_I^2\) | \(R+2T-Q\) |
| \(U_{\rm all}\) | \(R+(l+1)Q\) |
| \(T_{\rm all}^2\) | \(R+2T+(l-1)Q\) |
| \(T_{\rm all}T_I\) | \(R+2T-Q\) |

The first entry is the exact two-determinant pairing HO.14.
For \(U_I\), take the first derivative of its moment matrix with row
weight \(w_1^2\); the top-left entry is \(U_{11}\), and the lower block
is \(D_0\). For \(e_2(w_I)\), take the second coefficient of its moment
matrix with weight \(w_1\). The Gram block calculation of §1, now
with top-left entry one, gives \(T-Q\).
Since \(T_I^2=U_I+2e_2(w_I)\), this proves the third entry.
The remaining entries follow by independent outside rows:
their first moments vanish and their total squared first coordinate
has expectation \(lU_{11}\). This proves the full table.

Before pairing, the weights of \(A,B,C'\) in (QE.5) are respectively
\[
\begin{aligned}
&U_{\rm all}-T_{\rm all}^2/a,\\
&U_I-2T_{\rm all}T_I/a+kT_{\rm all}^2/a^2,\\
&(T_I^2-U_I)/2-(k-1)T_{\rm all}T_I/a
 +k(k-1)T_{\rm all}^2/(2a^2).
\end{aligned}
\]
There are \(\binom a{k}\) subsets, so the common factor is \((a)_k\).
Substitute the table and use (QE.5) to return to \(P_1,P_2,P_3\).
The result is
\[
\boxed{
\begin{pmatrix}L^{\otimes a}P_1\\L^{\otimes a}P_2\\L^{\otimes a}P_3\end{pmatrix}
=(a)_{m+1}\mathcal C_{a,m}
\begin{pmatrix}Q\\R\\T\end{pmatrix},}
\tag{QE.10}
\]
where
\[
\mathcal C_{a,m}=
{\setlength{\arraycolsep}{3pt}\begin{pmatrix}
\dfrac{a^2-am-a+m+2}{a^2}&\dfrac{a-1}{a^2}&-\dfrac2{a^2}\\[3pt]
\dfrac{(m+2)(2a-m-2)}{a^3}&\dfrac{a^2-3a+m+2}{a^3}
&-\dfrac{2(2a-m-2)}{a^3}\\[3pt]
\dfrac{(m-1)(m+2)(a-m-2)}{2a^3}
&-\dfrac{(m-1)(2a-m-2)}{2a^3}
&\dfrac{a^2-2am+m^2+m-2}{a^3}
\end{pmatrix}}.
\tag{QE.11}
\]
Direct determinant expansion gives
\[
\boxed{\det\mathcal C_{a,m}
=\frac{(a-m-2)(a-m-1)^2}{a^5}.}
\tag{QE.12}
\]
Every entry comes from the displayed finite table.
The determinant can also be checked after multiplying the rows
by \(a^2,a^3,2a^3\), respectively.

The formal polynomials \(Q,R,T\) are independent for \(m\ge2\).
Set \(U=I\). Zero third and fourth tensors give \(Q=1,R=T=0\);
varying the symmetric fourth entry \(D_{1111}\) varies \(R\)
independently. Finally take third entries \(C_{111}=C_{122}=1\),
with all other entries not forced by symmetry zero.
Its slice has two diagonal ones, so \(T=1\).
Thus (QE.12) proves independence of the actual \(P_1,P_2,P_3\)
whenever \(a\ge m+3\). With (QE.7), they form the entire invariant
basis. Equations (QE.8)–(QE.9) then prove that their finite-row
images span for every smaller row count as well.

## 4. Finite-row relations and target multiplicities

At \(a=m+1\), the sole subset \(I\) is the full row set.
In centered coordinates \(B=A\) and \(C'=-A/2\). Hence
\[
P_2=\frac{a-1}{a}P_1,\qquad
P_3=\frac{2-a}{2a}P_1.
\tag{QE.13}
\]
The centered simplex \(e_1,\ldots,e_m,-\mathbf1\) has
\(P_1=2(m+1)\ne0\). The invariant dimension is one.

At \(a=m+2\), write \(I=[a]\setminus\{i\}\).
The centered identities \(T_I=-w_{i1}\) and
\(U_I=U_{\rm all}-w_{i1}^2\) give \(B+C'=A/2\). Thus
\[
P_2+P_3=P_1/2.
\tag{QE.14}
\]
The minor in rows one and two, columns one and two of
\(\mathcal C_{m+2,m}\) equals \((m-1)/(m+2)^3\ne0\).
The independence argument of §3 shows that \(P_1,P_2\) are
independent, so the invariant dimension is two.

For \(a\le m\), every subset sum in (QE.5) is empty.
All \(P_j\) vanish, and their proved spanning gives invariant
dimension zero. With §3, the dimension at every positive row count
is exactly \(r_a\).

For \(n\ge4\), every \(P_j\) extends by (QE.6).
Dehomogenization injects the highest multiplicity space into this
invariant space, with inverse (QE.6) on its spanning generators.
The target multiplicity is therefore exactly \(r_a\), proving
the first assertion of (QE.2).

## 5. The actual normalized canonical matrix

Let \(N_2=n(n-1)\), \(N_3=n(n-1)(n-2)\),
\(N_4=n(n-1)(n-2)(n-3)\).
For centered split factors, the normalized moments are
\[
U=-S_n/N_2,\qquad C_0=2C_n/N_3,
\]
and
\[
(D_0)_{ij}=
\{(S_n)_{11}(S_n)_{ij}
+2(S_n)_{1i}(S_n)_{1j}-6(D_n)_{ij}\}/N_4.
\tag{QE.15}
\]
The fourth numerator is the inclusion–exclusion sum over the three
two-pair partitions and the six four-equal permutations; singleton
blocks vanish by centering. This includes repeated coordinate labels
with their exact ordered-index factors.

It follows that
\[
\begin{pmatrix}Q\\R\\T\end{pmatrix}
=\frac{(-1)^{m-1}}{N_2^{m+1}}\mathcal D_{n,m}
\begin{pmatrix}P_{1;n}\\P_{2;n}\\P_{3;n}\end{pmatrix},
\tag{QE.16}
\]
where
\[
\mathcal D_{n,m}=
\begin{pmatrix}
1&0&0\\
(m+2)u_n&-6u_n&0\\
0&0&-4v_n
\end{pmatrix},\quad
u_n=\frac{n(n-1)}{(n-2)(n-3)},\quad
v_n=\frac{n(n-1)}{(n-2)^2}.
\tag{QE.17}
\]
The middle row uses
\(\operatorname{tr}(\operatorname{adj}S\,S)=m\det S\) and
\((Se_1)^t\operatorname{adj}S(Se_1)=S_{11}\det S\).
The last uses degree \(m-2\) in \(S\) and degree two in the third
slice in (QE.4). Thus all signs and denominators are fixed.

Combining (QE.10) and (QE.16) proves the normalized canonical identity
\[
\boxed{
\begin{pmatrix}
h_{a,n}\widehat P_{1;a,n,m}\\
h_{a,n}\widehat P_{2;a,n,m}\\
h_{a,n}\widehat P_{3;a,n,m}
\end{pmatrix}
=c_{a,n,m}\mathcal C_{a,m}\mathcal D_{n,m}
\begin{pmatrix}
\widehat P_{1;n,a,m}\\
\widehat P_{2;n,a,m}\\
\widehat P_{3;n,a,m}
\end{pmatrix},\quad
c_{a,n,m}=\frac{(-1)^{m-1}(a)_{m+1}}{N_2^{m+1}}.}
\tag{QE.18}
\]
This display uses rows for images of source generators.
The ordinary column-coordinate matrix is its transpose.

When \(a=3\), the individual expressions on the right can be rational
homogeneous functions; their displayed linear combinations are
precisely the actual polynomial images on the left.
The identity is first the dehomogenized pairing, so this endpoint
introduces no unproved extension. For \(a\ge4\), all entries
on both sides are polynomial by (QE.6).
The exact split-form evaluation is SR.5–SR.6 with the same
normalization. First-coordinate scaling gives the identity on the
dense nonzero open set, and polynomial equality extends it everywhere.

## 6. Full rank and every finite endpoint

For \(a,n\ge m+3\), both bases have size three.
The matrix determinant is nonzero because
\(\det\mathcal D_{n,m}=24u_nv_n\ne0\) and (QE.12) is nonzero.
In column coordinates the matrix is
\[
\mathcal M_{a,n,m}
=c_{a,n,m}(\mathcal C_{a,m}\mathcal D_{n,m})^t.
\tag{QE.19}
\]
An actual preimage under \(h_{n,a}\) of a target coordinate column
\(v\) is the source combination with coordinate column
\(\mathcal M_{n,a,m}^{-1}v\), where
\[
\mathcal M_{n,a,m}^{-1}
=c_{n,a,m}^{-1}
(\mathcal C_{n,m}^{-1})^t(\mathcal D_{a,m}^{-1})^t.
\tag{QE.20}
\]
The inverses can equivalently be read as adjugate over the explicit
determinants. This gives every preimage by a fixed rational
three-by-three formula.

For endpoints, retain the first generator as basis at row count
\(m+1\), and the first two at row count \(m+2\), using
(QE.13)–(QE.14). At row counts at least \(m+3\), use all three.
For \(n\le m\), the right side of (QE.18) vanishes.
When exactly one of \(a,n\) is at least \(m+3\), the invertible
factor in that parameter and the finite-row independent basis give
rank equal to the smaller dimension. The remaining blocks have
the following literal reductions of
\(\mathcal C_{a,m}\mathcal D_{n,m}\); the nonzero common scalar
\(c_{a,n,m}\) is omitted:

| Parameters | Exact nonzero coefficient or determinant |
|---|---|
| \(a=n=m+1,\ m\ge3\) | \((m-2)/(m-1)\) |
| \(a=n=m+2\) | \(-2(m+1)(3m+2)/(m^3(m+2))\) |
| \(a=m+1,\ n=m+2\) | coefficient of the second target basis vector is \(-2(m+2)^2(3m-2)/(m^2(m-1)(m+1))\) |

The second entry is the two-by-two determinant after replacing
\(P_3\) by \(P_1/2-P_2\). The first replaces \(P_2,P_3\)
using (QE.13). The third replaces only the target \(P_3\)
using (QE.14). Substitution in (QE.11) and (QE.17) gives every
printed fraction. Reverse the off-diagonal pair by the exact
scalar-one transposition of canonical maps SR.5.
The square \(m=2,a=n=3\) lies outside \(n\ge4\).

For precision, when the larger row count occurs on the target side
of (QE.18), its three generators are independent, and the indicated
one or two rows of \(\mathcal C\) have full rank.
When it occurs on the source side, \(\mathcal C\mathcal D\) is
invertible and maps onto the span of the finite target generators.
This proves the mixed-size assertion by the actual matrix.
Thus \(h_{a,n}\) has rank \(\min(r_a,r_n)\); scalar-one
transposition gives (QE.2).

All identifications are rational tensor, column, Young, determinant
and affine-chart maps. Their multiplicity matrices are the same in
every dimension at least \(m+1\). Their Chow pullback is
R-037 EP.3–EP.5; frame-torsor and representation-\(K_0\) transport
uses the SGA/EGA/cote locators in R-036 §5.

## 7. Executed checks

The script verify_four_even_tail_block.py expands the determinant
squares, their raw row weights, and the actual split form.
It sums literal monomial pairings with exact multinomial
denominators and compares all three generators with (QE.18).
It does not call the moment table on the literal side.
Population configurations are selected to give the full separately
computed generator rank \(r_n\); nonunit first coordinates are retained.

Its ranges are \(m=2,3\), \(n=4,5,6\), together with
\((m,n)=(4,5),(4,6),(4,7)\), and \(m+1\le a\le7\).
All 246 literal generator pairings pass, including every one- and
two-dimensional endpoint and several three-dimensional matrices.

An independent cycle-index/Murnaghan–Nakayama calculation checks
the target multiplicities for \(3\le a\le8\), \(n=4,5\),
\(2\le m\le a-1\).
The receipts are `FOUR_EVEN_TAIL_CANONICAL_MATRIX_CHECK.tsv` and
`FOUR_EVEN_TAIL_MN_CHECK.tsv`.
The unbounded rank law follows from the complete matrix proof.

