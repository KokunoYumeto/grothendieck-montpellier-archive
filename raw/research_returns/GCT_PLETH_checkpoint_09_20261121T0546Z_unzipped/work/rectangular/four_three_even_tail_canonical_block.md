# The remaining mixed width-four block

## R-043. The tails \((4,3,2^{m-2})\)

Let \(m\ge2\), \(a\ge m+2\), \(n\ge4\), and \(\dim V\ge m+1\).
Set
\[
\lambda=(an-2m-3,4,3,2^{m-2}),\qquad
s_t=\min(2,\max(0,t-m-1)).
\tag{ME.1}
\]
Then
\[
\boxed{
a_{a,n}^{\lambda}=s_a,\qquad
\operatorname{mult}_{\lambda}\operatorname{im}h_{n,a}
=\min(s_a,s_n).}
\tag{ME.2}
\]
For inner degree three, the valid partitions in the same tail family
have target multiplicity one for \(a\ge m+3\), zero for
\(a\le m+2\), and canonical-image multiplicity zero throughout.
For inner degree two the target multiplicity is zero.
The proof gives the actual two-by-two matrix, its inverse, the finite
unit endpoint, and the exact cubic extension vector. No historical
novelty assertion is made.

## 1. The two highest tensors and the invariant bound

For centered rows \(z_i=w_i-\bar w\in\mathbb Q^m\), put
\[
S=\sum_i z_i z_i^t,\quad
(C_p)_{ij}=\sum_lz_{lp}z_{li}z_{lj},\quad
(D_{pq})_{ij}=\sum_lz_{lp}z_{lq}z_{li}z_{lj},
\quad f_p=\operatorname{tr}(\operatorname{adj}(S)C_p).
\]
Define the symmetric bilinear polynomial
\[
\mathcal B_S(X,Y)=[uv]\det(S+uX+vY).
\]
For invertible \(S\), \(G=S^{-1}\), it equals
\[
\mathcal B_S(X,Y)=\det(S)
\left(\operatorname{tr}(GX)\operatorname{tr}(GY)
-\operatorname{tr}(GXGY)\right).
\tag{ME.3}
\]
Coefficient extraction defines it at singular \(S\), and the
determinant derivative proves (ME.3).
The required polynomials are
\[
\Phi_1=S_{11}f_2-S_{12}f_1,\qquad
\Phi_2=\mathcal B_S(D_{11},C_2)-\mathcal B_S(D_{12},C_1).
\tag{ME.4}
\]
Both are symmetric in the rows and translation invariant.
Their tensor transformation is determinant-square times a
three-covariant-index hook. The two terms have free labels
\(1,1,2\), with the first two labels in their symmetric pair.
The raising operator \(E_{12}\) sends each of their two terms
to the same component with labels \(1,1,1\), so their difference
vanishes. All other raising operators kill the components.
Their diagonal weight is exactly \((4,3,2^{m-2})\).
Adjugate congruence and the complementary-minor form of (ME.3)
prove these transformation assertions as polynomial identities.

The tail transpose is \(\gamma=(m,m,2,1)\).
In HO.3's exact four-column invariant-algebra surjection,
only odd exterior degrees of \(\Lambda(\Lambda^3T)\) occur.
Exterior degree three has a determinant-square factor and hence
fourth part at least two; it misses \(\gamma\).
Exterior degree one contributes exactly twice. Using the
paired-shape decomposition HO.5, its vertical three-strip
comes from \((m-1,m-1,1,1)\) with no \(\Lambda^4T\) factor,
or from \((m-2,m-2,0,0)\) with one determinant factor.
In each case the added rows are one, two and three.
All other choices are excluded by the equal first two parts
and the final parts \(2,1\). The actual exterior Pieri projections
have multiplicity one. Consequently
\[
\dim(S_{(4,3,2^{m-2})}\mathfrak h_a)^{S_a}\le2.
\tag{ME.5}
\]

## 2. Affine Gram maps and row degree at most four

Let \(k=m+1\), let \(R\) have rows \((1,w_i)\), and write
\(f_I=\det R_I^2\). For a subset \(I\), define centered sums
\(T_{I,p}=\sum_{i\in I}z_{ip}\) and
\(U_{I,pq}=\sum_{i\in I}z_{ip}z_{iq}\).
The cubic-minor identity CT.9, in centered coordinates, gives
\[
a f_p=\sum_{|I|=k}T_{I,p}f_I.
\tag{ME.6}
\]
Its weighted-Cauchy–Binet proof applies to every component \(p\).
Thus
\[
a\Phi_1=\sum_I(S_{11}T_{I,2}-S_{12}T_{I,1})f_I.
\tag{ME.7}
\]
There is a second exact polynomial identity:
\[
\boxed{
\sum_I(U_{I,11}T_{I,2}-U_{I,12}T_{I,1})f_I
=a\Phi_2+\Phi_1.}
\tag{ME.8}
\]

To prove (ME.8), insert row weights \(1+u z_{i1}^2+v z_{i2}\)
in \(R^tR\), and subtract the mixed determinant coefficient
for weights \(1+u z_{i1}z_{i2}+v z_{i1}\).
The same-row product cancels identically, so weighted
Cauchy–Binet gives exactly the left side.
The centered base matrix is \(\operatorname{diag}(a,S)\).
Its mixed coefficient is \(a\Phi_2+\Phi_1\):
the lower-block mixed coefficient is \(a\Phi_2\);
the top-left quadratic variation gives
\(S_{11}f_2-S_{12}f_1\);
and the two off-diagonal Schur-complement contributions
are both \(-2\det(S)C_{112}\), so they cancel in the difference.
These statements also follow by multiplying the two-by-two
block inverse in the determinant's mixed derivative.
This proves the identity, including its coefficient one.

Both weight polynomials in (ME.7) and (ME.8) have degree
at most two in each fixed original row.
Indeed, under \(w_r\mapsto tv\), every centered row has
leading term \(\alpha_i tv\). The leading degree-three
term in either weight is a scalar times
\(v_1^2v_2-v_1v_2v_1=0\).
As \(f_I\) has degree at most two in each row, (ME.7)–(ME.8)
prove that \(\Phi_1,\Phi_2\) have row degree at most four.
Their separate homogenizations
\[
\widehat\Phi_{j;a,n,m}
=\left(\prod_i x_i\right)^n\Phi_j(y_i/x_i)
\tag{ME.9}
\]
are therefore polynomial highest vectors for \(n\ge4\).

## 3. The complete independent-row matrix

Let a formal row functional have first moments zero.
Use \(U,C_p^0,D_{pq}^0\) for its second, third and fourth
moments, and let \(F_1,F_2\) be the expressions (ME.4)
in these moments. Set \(l=a-k\).
Then the exact independent-row identity is
\[
\boxed{
\begin{pmatrix}L^{\otimes a}\Phi_1\\L^{\otimes a}\Phi_2\end{pmatrix}
=(a)_k\,\mathcal E_{a,m}
\begin{pmatrix}F_1\\F_2\end{pmatrix},\qquad
\mathcal E_{a,m}=
\begin{pmatrix}
l^2/a^2&l/a^2\\
kl/a^3&(a-1)l/a^3
\end{pmatrix}.}
\tag{ME.10}
\]
Here is a derivation by literal raw row sums, including all
centering terms.

For a fixed subset \(I\), use uncentered \(T_p=\sum_{i\in I}w_{ip}\),
\(U_{pq}^I=\sum_{i\in I}w_{ip}w_{iq}\),
\(W_p=\sum_iw_{ip}\), and \(U_{pq}^{\rm all}=\sum_iw_{ip}w_{iq}\).
Set
\[
\begin{aligned}
X&=U_{11}^{\rm all}T_2-U_{12}^{\rm all}T_1,\\
Y&=U_{11}^{\rm all}W_2-U_{12}^{\rm all}W_1,\\
Z&=W_1^2T_2-W_1W_2T_1.
\end{aligned}
\]
After expanding the centering in (ME.7), its contribution to
\(a^2\Phi_1\) is \((aX-kY-Z)f_I\).
Divide all expectations in the following equations by \(k!\):
\[
L(Xf_I)=F_2+(l+1)F_1,\quad
L(Yf_I)=F_2+(l+1)F_1,\quad
L(Zf_I)=lF_1.
\tag{ME.11}
\]
For the inside part of \(X\), the mixed moment-matrix derivative
in §2, now with top-left entry one, gives \(F_2+F_1\).
Its outside quadratic terms give \(lF_1\).
The additional outside first moments in \(Y-X\) vanish;
its same-row cubic difference vanishes identically.
In \(Z\), the completely inside terms cancel, the outside
linear terms have zero expectation, and the two outside
second moments leave \(lF_1\). These are all equality patterns.

For (ME.8), the centered inside weight expands exactly to
\[
J-\frac{k}{a}(W_2U_{11}^I-W_1U_{12}^I)
-\frac1a(W_1T_1T_2-W_2T_1^2),\quad
J=U_{11}^I T_2-U_{12}^I T_1.
\tag{ME.12}
\]
The expectations of the first two displayed raw differences
are both \(k!(F_1+F_2)\); the last has expectation zero.
Hence its expectation is \(k!l(F_1+F_2)/a\).
Combine this with (ME.11), the \(\binom a{k}\) subsets,
and (ME.8) to obtain every entry of (ME.10).

The determinant is
\[
\boxed{\det\mathcal E_{a,m}=l^2(l-1)/a^4.}
\tag{ME.13}
\]
Indeed its remaining numerator is
\(l(a-1)-k=a(l-1)\).
The formal \(F_1,F_2\) are independent for \(m\ge2\):
take \(U=I\) and only the third tensor \(C_{222}=1\).
Then \(F_1=1\); varying the symmetric fourth entry
\(D_{1111}\) varies \(F_2\) independently.
Thus (ME.13) proves independence of \(\Phi_1,\Phi_2\)
at every \(a\ge m+3\). With (ME.5), they form the entire
invariant basis.

The zero-padding/orthogonal-projection maps QE.8–QE.9
apply to these centered moment tensors as well:
restriction of zero-padded centered rows changes none of
\(S,C_p,D_{pq}\), so it sends each \(\Phi_j\) to the same
finite-row polynomial with scalar one.
The invariant-algebra surjection therefore proves that
their finite-row images span every smaller invariant space.

## 4. Exact finite-row relations

At \(a=m+2=k+1\), every subset is \(I=[a]\setminus\{i\}\).
Centering gives
\(T_{I,p}=-z_{ip}\) and \(U_{I,pq}=S_{pq}-z_{ip}z_{iq}\).
The weight in (ME.8) becomes
\(-(S_{11}z_{i2}-S_{12}z_{i1})\).
The right side of (ME.7), divided by \(a\), uses exactly
\(1/a\) times that weight. Hence
\[
\Phi_2=(a-1)\Phi_1/a.
\tag{ME.14}
\]
The first row of (ME.10) is nonzero at \(l=1\), and the
formal \(F_1,F_2\) are independent, so \(\Phi_1\ne0\).
The invariant dimension is one.

At \(a=m+1\), the only subset is the full set and its
centered first sums are zero. Equations (ME.6)–(ME.8)
give both \(\Phi_j=0\).
At \(a\le m\), their subset sums are empty and again
both vanish. Their proved spanning gives zero dimension.
The invariant dimension at every row count is therefore
exactly \(s_a\). Since all vectors extend for \(n\ge4\),
dehomogenization and (ME.9) prove the target formula in (ME.2).

## 5. The split-form matrix and actual ranks

Let
\[
u_n=\frac{n(n-1)}{(n-2)(n-3)},\qquad
\mathcal H_{n,m}=
\begin{pmatrix}1&0\\(m+1)u_n&-6u_n\end{pmatrix}.
\]
The exact centered split-form moments give
\[
\begin{pmatrix}F_1\\F_2\end{pmatrix}
=\frac{2(-1)^m}{n^{m+1}(n-1)^{m+1}(n-2)}
\mathcal H_{n,m}
\begin{pmatrix}\Phi_{1;n}\\\Phi_{2;n}\end{pmatrix}.
\tag{ME.15}
\]
For the first row, each term has \(m\) second moments and
one third moment. For the second row, use the fourth-moment
numerators
\[
D_{11}^0:\ S_{11}S+2(Se_1)(Se_1)^t-6D_{11},
\]
\[
D_{12}^0:\ S_{12}S+(Se_1)(Se_2)^t+(Se_2)(Se_1)^t-6D_{12}.
\]
The mixed determinant satisfies
\(\mathcal B_S(S,C_p)=(m-1)f_p\).
The two rank-one parts add \(2(S_{11}f_2-S_{12}f_1)\);
their \(-2\det(S)C_{112}\) terms cancel.
The resulting numerator is
\((m+1)\Phi_1-6\Phi_2\).
Its denominator ratio to the first row is
\(N_2^2/N_4=u_n\).
This verifies every coefficient and sign in (ME.15).

The actual normalized canonical identities are
\[
\boxed{
\begin{pmatrix}
h_{a,n}\widehat\Phi_{1;a,n,m}\\
h_{a,n}\widehat\Phi_{2;a,n,m}
\end{pmatrix}
=c_{a,n,m}\mathcal E_{a,m}\mathcal H_{n,m}
\begin{pmatrix}
\widehat\Phi_{1;n,a,m}\\
\widehat\Phi_{2;n,a,m}
\end{pmatrix},\quad
c_{a,n,m}=
\frac{2(-1)^m(a)_{m+1}}
{n^{m+1}(n-1)^{m+1}(n-2)}.}
\tag{ME.16}
\]
This is the scalar-one pairing SR.5–SR.6.
First-coordinate homogeneity extends it from the affine chart
to the polynomial identity everywhere.

For \(a,n\ge m+3\), both bases have size two, and
\(\det\mathcal E\ne0\), \(\det\mathcal H=-6u_n\ne0\).
In column coordinates its matrix is
\(c_{a,n,m}(\mathcal E_{a,m}\mathcal H_{n,m})^t\).
Under \(h_{n,a}\), an actual preimage of target coordinate
column \(v\) has source coordinates
\[
c_{n,a,m}^{-1}
(\mathcal E_{n,m}^{-1})^t(\mathcal H_{a,m}^{-1})^t v.
\tag{ME.17}
\]
All entries are explicit rational functions, or adjugate over
the displayed nonzero determinants.

For mixed one- and two-dimensional blocks, the matrix with
the larger source row count is invertible before restriction
to the finite target span. In the reverse direction, the
nonzero first row of \(\mathcal E\), followed by invertible
\(\mathcal H\), remains nonzero in the two-dimensional target.
Thus their rank is one.
The last unit square is \(a=n=m+2\).
After substituting (ME.14), the scalar of
\(\mathcal E_{a,m}\mathcal H_{n,m}\), omitting the
nonzero common factor \(c\), is
\[
\frac{m^2-3m-2}{(m+2)m(m-1)}.
\tag{ME.18}
\]
Direct substitution gives this fraction.
Its numerator is \(-4,-2,2\) at \(m=2,3,4\), and its
increment from \(m\) to \(m+1\) is \(2m-2>0\).
It is therefore nonzero for every integer \(m\ge2\).
For \(n\le m+1\), both target generators vanish by §4.
This proves rank \(\min(s_a,s_n)\) for \(h_{a,n}\);
scalar-one transposition proves (ME.2).

## 6. The whole cubic extension and its zero canonical image

There is a particularly simple degree-three combination:
\[
\Psi=a\Phi_2-(a-1)\Phi_1.
\]
For a subset \(J\), put
\(J_J(z)=U_{J,11}T_{J,2}-U_{J,12}T_{J,1}\).
Equations (ME.7)–(ME.8) and the zero total centered first sums
give the exact identity
\[
\boxed{\Psi=\sum_{|I|=m+1}J_{I^c}(z)\,f_I.}
\tag{ME.19}
\]
Indeed (ME.8) minus \(a\Phi_1\) replaces the inside second
sums by minus the outside second sums, and
\(T_{I,p}=-T_{I^c,p}\) supplies the remaining sign.

The weight \(J_J\) depends only linearly on a common translation.
Explicitly, translating by \((M_1,M_2)\) gives
\[
J_J(w-M)=J_J(w)
-|J|(M_2U_{J,11}-M_1U_{J,12})
-M_1T_{J,1}T_{J,2}+M_2T_{J,1}^2.
\]
For a row in \(I\), its occurrence in \(J_{I^c}(z)\)
is only through this common mean, hence is linear.
The minor square adds degree at most two.
For a row outside \(I\), the determinant is independent
of that row and the weight has degree at most three.
Thus \(\Psi\) has row degree at most three.

For \(a\ge m+3\), \(\Psi\ne0\) because the two \(\Phi_j\)'s
are independent. The other direction really has degree four:
the first row of (ME.10) has nonzero coefficient
\((a)_k l/a^2\) on \(F_2\), which has genuine fourth-moment
dependence at fixed second and third moments.
A row-degree-three polynomial has no such dependence under
independent-row evaluation. Therefore \(\Phi_1\) cannot extend
to slot degree three. The full cubic extension is exactly
the line spanned by \(\Psi\).
At \(a=m+2\), (ME.14) makes \(\Psi=0\), and the same
fourth-moment argument excludes the sole invariant line.
At smaller \(a\) there are no invariants.

The actual cubic map is zero. Combining the two rows of
(ME.10) gives
\[
L^{\otimes a}\Psi=-(a)_{m+1}\frac{l(l-1)}a F_1.
\tag{ME.20}
\]
The fourth moments cancel before specialization.
For three split factors, \(F_1\) is a scalar multiple of
\(\Phi_{1;3}\), and this polynomial is zero because
\(3\le m+1\), by §4.
Consequently \(h_{a,3}\widehat\Psi=0\), and transposition
gives the asserted zero rank of \(h_{3,a}\).

For inner degree two, every polynomial highest weight in
\(\operatorname{Sym}^a(\operatorname{Sym}^2V)\) has even
parts: the exact symmetric-matrix LDL chart of QD.11–QD.12
restricts a highest polynomial to a monomial in diagonal
entries, each of torus weight twice a coordinate.
The present weight has a part equal to three, so its
highest space is zero. This proves the remaining target
statement without relying on a candidate polynomial's vanishing.

All these maps are rational and have the same multiplicity
matrices in every declared rank.
Their coordinate-ring and frame-torsor transports are the
actual morphisms R-037 EP.3–EP.5 and R-036 §5.

## 7. Executed checks

The script `verify_four_three_even_tail_block.py` expands the
determinant-square permutations and every raw row weight in
(ME.11)–(ME.12), and pairs monomials against the actual split
form with exact multinomial denominators. It groups only
literal equal determinant monomials and uses a finite
nilpotent-variable product to sum the row assignments.
It does not call the proposed moment matrix on that side.
An independent fifth-moment extension check confirms the
degree-four cancellation at the smallest endpoint.

Population configurations have the full separately computed
generator rank \(s_n\), with nonunit first coordinates.
The exact matrix checks cover \(m=2,3\), \(n=4,5,6\),
and \((m,n)=(4,5),(4,6),(4,7)\), with three source row
counts beginning at \(m+2\).
The receipt is `FOUR_THREE_EVEN_TAIL_CANONICAL_CHECK.tsv`.
All 78 literal generator pairings pass.

A separate cycle-index/Murnaghan–Nakayama calculation verifies
the target and source coefficients for \(4\le a\le8\),
\(n=3,4,5\), \(2\le m\le a-1\), retaining valid partitions.
The receipt is `FOUR_THREE_EVEN_TAIL_MN_CHECK.tsv`.
All 59 target coefficients and all 59 source coefficients pass.
The complete unbounded ranks are proved by the matrix and
endpoint arguments above.

