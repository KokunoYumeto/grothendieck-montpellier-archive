# Stable line defects: exact higher cohomology and a positive correction count

## T-047. The stable-defect isomorphism

Let \(s\ge2\), \(k\ge3s-1\), \(a=b+x\), \(b,x\ge0\), and
\(c=2k-s\). Retain the five-point ideal \(\mathcal I\subset
\mathbf P(E)\), \(E=\mathfrak h_5\), and its tautological quotient
\(Q\). For one pair of points put \(P=\operatorname{span}(\ell_i,\ell_j)\)
and \(W=E/P\simeq\mathfrak h_3\). The pair stabilizer is
\(S_2\times S_3\); it permutes the basis of \(P\), acts standardly
on \(W\), and acts trivially on the other factor in each case.

There is an actual equivariant isomorphism
\[
\boxed{H^1(\mathcal I^k(c)S_{(a,b)}Q)
\simeq\operatorname{Ind}_{S_2\times S_3}^{S_5}\mathcal C_{x,b,s},}
\tag{D.1}
\]
where the positive direct sum is
\[
\boxed{\mathcal C_{x,b,s}=
\bigoplus_{\substack{j,u,v\ge0;\ u\le x,\ v\le b\\j+u+v\le s-2}}
(\det P)^{u+v+1}\operatorname{Sym}^{s-j-u-v-2}P
\otimes\operatorname{Sym}^jW^*
\otimes S_{(a-u,b-v)}W.}
\tag{D.2}
\]
Every higher cohomology group in degree at least two vanishes.
The isomorphism is induced by finite normal restriction, the explicit
substitution (D.6), and the unipotent bundle automorphism (D.7).
The multiplicity of any fixed \([\nu]\), \(\nu\vdash5\), in
(D.1) has a positive count in at most twelve bounded rational
polytopes with nine integer variables, stated in §6.

This theorem determines the higher-cohomology correction for every
defect in the displayed stable range. It does not assert positivity
of a signed zeroth-cohomology expression without a further positive
formula for that expression. At \(s=2\), it specializes to the
actual correction and full positive plethysm formula of T-046.

## 1. Directional jet interpolation with a proved bound

At each of the five frame points the four pair-line directions form
a projective frame in \(\mathbf P^2\). Put \(r=s-1\). In
coordinates with frame points \(e_1,e_2,e_3,[1,1,1]\), their ideal is
the complete intersection
\[
J=(f,g)=(z_1z_2-z_1z_3,\ z_1z_2-z_2z_3).
\tag{D.3}
\]
Its projective zero set is exactly those four points; the two gradients
are independent at each. There is no common curve component, so
\(f,g\) is a regular sequence. The ideal power has the exact resolution
\[
0\to S(-2r-2)^r\longrightarrow S(-2r)^{r+1}
\longrightarrow J^r\to0,
\tag{D.4}
\]
where the last basis maps to \(f^{r-i}g^i\), \(0\le i\le r\),
and the preceding columns are \(g e_{i-1}-f e_i\).
To check every syzygy, reduce a relation modulo \(f\): regularity
of \(g\) gives divisibility of the last coefficient by \(f\).
Subtract its adjacent displayed syzygy, then divide the remaining
relation by \(f\) and continue inductively. Injection of the first
map follows successively from its first, second and later coordinates.
This proves the resolution with its actual maps.

After sheafifying and twisting by \(d\ge2r\), the left line bundles
have twists at least \(-2\). Projective-plane cohomology therefore
gives \(H^1(\widetilde{J^r}(d))=0\). Consequently evaluation onto
the order-\(r\) jets at the four directions is onto in every degree
\(d\ge2r\). The map is literal polynomial evaluation in affine
direction charts; a right inverse can be specified by row reduction
of this full-row-rank rational evaluation matrix. Thus no interpolation
rank is being assumed.

## 2. Exact finite normal quotients and their substitutions

For a pair \(e\), use the canonical stabilizer splitting
\(E=P_e\oplus W_e\), where \(W_e\) is the zero-sum subspace on
the other three letters. Let \(X,Y\) be the dual coordinates of the
ordered pair basis, and let \(w\in W_e\) denote the normal vector.
The open set \(\mathbf P(E)\setminus\mathbf P(W_e)\) projects onto
\(\mathbf P(P_e)\), and is the total space of
\(W_e\otimes\mathcal O(1)\). Its normal Taylor expansion is unique.

Let \(\mathcal B_{e,k}^r(c)\) be the image of
\(\mathcal I^k(c)\) in its quotient by the \(r\)-th power of the
pair-line ideal. In normal degree \(j<r\), its coefficient is a
binary polynomial section of degree \(c-j\) vanishing to order
\(k-j\) at both endpoints. Indeed membership in a point maximal
ideal power is exactly total Taylor order at least \(k\).
Here \(k>r\), so these orders are positive. Thus, as a sheaf on
the base line, this actual image is the direct sum
\[
\bigoplus_{j=0}^{r-1}\operatorname{Sym}^j W_e^*\otimes
(XY)^{k-j}\mathcal O(c-j-2(k-j)).
\tag{D.5}
\]
The three other frame points are off the line and impose no local
condition on this finite normal sheaf.

Make the homogeneous substitution
\[
\boxed{w=XYv,\qquad F\longmapsto (XY)^{-k}F(X,Y,XYv).}
\tag{D.6}
\]
It is regular on the displayed image: the factor in each summand of
(D.5) cancels exactly. Its inverse multiplies the normal coefficient
of degree \(j\) by \((XY)^{k-j}\). Consequently it is an actual
isomorphism to
\(\mathcal O(-s)\otimes\bigoplus_{j<r}\operatorname{Sym}^jW_e^*
\mathcal O(j)\), with the action of an original normal coordinate
given by multiplication by \(XYv\). The vector \(v\) is the
tautological normal vector on \(\operatorname{Tot}(W_e\otimes
\mathcal O(-1))\), truncated at degree \(r\). The same construction
at twist \(c-1\) has base line bundle \(\mathcal O(-s-1)\).

The original tautological line after substitution is generated by
\(p+XYv\), where \(p=X\ell_i+Y\ell_j\). Define
\[
\boxed{T=I-\tfrac12\bigl((Yv)\otimes X^*+(Xv)\otimes Y^*\bigr).}
\tag{D.7}
\]
Here \(X^*,Y^*\in E^*\) are the constant coordinate functionals
vanishing on \(W_e\); the products \(Xv,Yv\) have homogeneous
degree zero and are regular on this total-space chart. Its correction
has square zero, because those functionals vanish on \(W_e\), so
the inverse changes the minus sign to plus. Direct substitution gives
\(T(p+XYv)=p\). The formula is symmetric in the two endpoints
and equivariant under the other three letters. It therefore gives an
actual stabilizer-equivariant isomorphism
\[
Q\longrightarrow\pi^*\bigl((P_e/\mathcal O(-1))\oplus W_e\bigr)
=\pi^*((\det P_e)\mathcal O(1)\oplus W_e)
\tag{D.8}
\]
on the finite normal module after (D.6). In particular the normal
coupling in the original Schur differential is conjugated by an
explicit automorphism; it is not discarded on an associated graded.

## 3. Scalar restriction is onto, and its target is an isomorphism

The scalar restriction maps are
\(H^1\mathcal I^k(C)\to\bigoplus_eH^1\mathcal B_{e,k}^r(C)\),
for \(C=c,c-1\). Their cokernel descriptions are obtained from
ordinary point-jet evaluation, as in (L.6).

Fix a normal monomial \(w^\beta\), \(|\beta|=j<r\). Its binary
coefficient has degree \(C-j\); the retained endpoint jets have
orders \(t<k-j\). Their overlap functionals are the differences
of the two coefficients with binary exponents
\(t\) and \(C-j-t\). They vanish on every global polynomial and
form a basis of the dual line-normal cohomology in (D.5). The possible
exponents range from \(C-k+1\) to \(k-j-1\).

At one endpoint, the total tangent Taylor degree of such a coefficient
is \(t+j\). For the source twist \(C=c-1\), all these degrees are
at least \(k-s\), and for the target they are at least \(k-s+1\).
Our bound gives
\(k-s\ge2s-1\ge2r\). At a fixed total degree, these normal
coefficients are precisely directional Taylor-jet functionals of
orders at most \(r-1\) at the four direction points. For a homogeneous
Taylor polynomial of degree \(d\), expansion at a direction in local
projective coordinates has coefficients of the monomials
\(t^{d-j}w^\beta\). This describes the leading map exactly.
Changing the point or line chart is triangular in the total Taylor
degree, with an invertible leading coordinate change.

Suppose a relation among the overlap functionals existed. At one
point take its largest total Taylor degree with a nonzero coefficient.
The leading relation lies among a subset of the order-\(r\) direction
jet functionals, which are independent by (D.3)–(D.4). Every
coefficient at that degree vanishes. Descend in Taylor degree and do
this at each point. All coefficients of the alleged relation vanish.
No two overlaps for the same edge and normal monomial use the same
endpoint coefficient, so this eliminates each overlap coefficient
individually. Thus both scalar restriction maps are onto.

The target dimension can be computed exactly from A-028's Cox map.
Its six binary weights are \((k-s)^5,k-3s\). For \(k\ge3s\),
the binary weight difference gives
\[
\begin{aligned}
h^0\mathcal I^k(c)
&=[z^c]\frac{(1-z^{k-s+1})^5}{(1-z)^4}\\
&=\binom{c+3}{3}-5\binom{k+2}{3}+10\binom{s+1}{3}.
\end{aligned}
\tag{D.9}
\]
Numerator terms of order at least three have negative residual degree
in the displayed range. At \(k=3s-1\) the sixth weight is \(-1\),
so the Cox component is zero. The same coefficient is zero because
the binary weights \(-1\) and 1 have equal multiplicity. Thus (D.9)
holds at that endpoint as well.

The point quotient length is \(5\binom{k+2}{3}\), and higher scalar
cohomology in degrees two and three vanishes. Therefore
\(h^1\mathcal I^k(c)=10\binom{s+1}{3}\).
On each normal quotient the scalar first cohomology dimension is
\[
\sum_{j=0}^{s-2}(j+1)(s-j-1)=\binom{s+1}{3}.
\]
Consequently the already onto target restriction is an isomorphism:
\[
H^1\mathcal I^k(c)\simeq
\bigoplus_eH^1\mathcal B_{e,k}^{s-1}(c).
\tag{D.10}
\]
The source restriction at \(c-1\) remains onto; no dimension
assertion about that source is required.

## 4. Exact global Schur comparison and evaluation

Tensor the actual locally split three-term Schur complex with
\(\mathcal I^k(c)\), as in T-046. All its scalar twists are
positive, so \(H^2,H^3\) of every term vanish. Its two image
sequences identify the target first cohomology with the cokernel of
the map from the first cohomology of the middle term to that of the
last term; all target cohomology of degree at least two vanishes.

Apply normal restriction to those two terms. The last-term map is
an isomorphism by (D.10), and the middle-term map is onto by §3.
The differentials commute with restriction. Tensoring the locally
split Schur complex by each normal quotient preserves its exactness,
so its analogous cokernel computes the first cohomology of that
actual finite normal quotient tensored with the Schur bundle. The
commuting cokernel diagram therefore gives an isomorphism from the
global first cohomology to the sum of these finite normal first
cohomology groups. This is the same exact diagram as (L.15)–(L.17),
with the specified finite normal modules in place of reduced lines.

Under (D.6)–(D.8), each group is the first cohomology of
\[
\bigoplus_{j=0}^{s-2}\operatorname{Sym}^jW^*\otimes
\mathcal O(-s+j)\otimes
S_{(a,b)}((\det P)\mathcal O(1)\oplus W).
\tag{D.11}
\]
The decomposition with one line factor is obtained by removing a
horizontal strip from \((a,b)\). Write its two removed row lengths
as \(u,v\). They satisfy \(0\le u\le a-b=x\),
\(0\le v\le b\), and the line exponent is \(u+v\). Its
actual summand is
\((\det P)^{u+v}\mathcal O(u+v)\otimes S_{(a-u,b-v)}W\).
One can obtain the maps by the same primitive-projector and
multiplicity-one branching prescription used for the Schur complex;
the horizontal-strip identity also follows by the usual tableau
decomposition according to the entries from the one-dimensional
summand.

Only \(j+u+v\le s-2\) contributes to first cohomology.
The line Čech pairing gives
\(H^1\mathcal O(-s+j+u+v)=
\operatorname{Sym}^{s-j-u-v-2}P\otimes\det P\).
Substitution in (D.11) proves exactly (D.2). The formulas are
equivariant under the pair stabilizer, and the ten pair summands
are permuted transitively by \(S_5\), proving (D.1).

## 5. Exact consequence for plethysm coefficients

For \(d\ge0\), define
\[
n=d+b+x+k-s,
\quad\lambda=(d+3b+2x+3k-4s,d+b+x+2k-s,d+b+x,d+x,d).
\tag{D.12}
\]
Require \(2b+x+k\ge3s\); this is exactly the remaining partition
inequality. The G-015 chart and complementary-column pairing give
the actual isomorphism
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+b+x}
H^0(\mathcal I^k(2k-s)S_{(b+x,b)}Q).
\tag{D.13}
\]
The first-line weight before complement is \(b+x+2k-s\); the
relative quotient weight is \((b+x,x,0)\). Removing its determinant
via \(\det Q^*=\det E^*\mathcal O(-1)\) leaves twist \(2k-s\).
The point order is \(\lambda_2-n=k\), and the inverse map remains
\(F\mapsto u^{-k}F(v(X))\). This fixes every determinant and
extension condition in (D.13).

Let \(P_g(x,b,k;c)\) be the explicit three-term Schur/Euler trace
in (R.7). Equations (D.1) and the higher vanishing give the exact
character identity
\[
\boxed{\operatorname{tr}\left(g\mid H^0(\mathcal I^k(c)S_{(a,b)}Q)\right)
=P_g(x,b,k;c)+
\operatorname{tr}\left(g\mid\operatorname{Ind}_{S_2\times S_3}^{S_5}
\mathcal C_{x,b,s}\right).}
\tag{D.14}
\]
Both terms are explicitly evaluated here: the first by seven
elementary closed traces, the second by the positive module (D.2).
No uncomputed cohomology rank remains in this region. The formula
is an exact arithmetic evaluation of the zeroth-cohomology coefficient;
the positive polytopes below count its cohomology correction.

## 6. At most twelve positive polytopes for the correction

Identify \(W^*\) with \(W\) by the invariant nondegenerate dot
product on the zero-sum three-letter subspace. Rank-two Schur
duality gives
\(S_{(a-u,b-v)}W=(\det W)^{b-v}
\operatorname{Sym}^{x-u+v}W\).
For two symmetric powers, the actual Clebsch–Gordan summands are
generated by the highest vectors
\((p_1q_2-p_2q_1)^h p_1^{j-h}q_1^{x-u+v-h}\),
\(0\le h\le\min(j,x-u+v)\). Applying the lowering operator gives
their explicit equivariant embeddings. Their distinct highest
weights and dimension sum prove the direct-sum equality
\[
\operatorname{Sym}^jW\operatorname{Sym}^{x-u+v}W
=\bigoplus_h(\det W)^h\operatorname{Sym}^{j+x-u+v-2h}W.
\tag{D.15}
\]
On \(P\), use the eigenbasis \(\ell_i+\ell_j,\ell_i-\ell_j\).
A monomial with \(p\) factors of the second vector has endpoint
sign \((-1)^p\), with \(0\le p\le s-j-u-v-2\).

Let \(\sigma,\tau\in\{0,1\}\), and \(\rho\vdash3\).
Retain this fixed tag only when \(\nu/\rho\) is a horizontal
two-strip for \(\sigma=0\), or a vertical two-strip for
\(\sigma=1\). This is exactly the restriction multiplicity of
\([\rho]\otimes\operatorname{sgn}_{S_2}^{\sigma}\) in \([\nu]\),
by the ordinary/exterior Pieri identity. It is either zero or one.

The three symmetric-power multiplicity series for \(W=\mathfrak h_3\)
are
\[
\frac1{(1-t^2)(1-t^3)},\quad
\frac{t+t^2}{(1-t^2)(1-t^3)},\quad
\frac{t^3}{(1-t^2)(1-t^3)}
\tag{D.16}
\]
for labels \((3),(2,1),(1^3)\). They follow by taking the three
character inner products of \((1-t)^{-2},(1-t^2)^{-1},
(1+t+t^2)^{-1}\); multiplication of the denominators verifies
the three rational identities exactly. Thus their fixed shift lists
are \(\{0\},\{1,2\},\{3\}\).

For each retained \((\sigma,\tau,\rho)\) and each shift \(e\)
in the list of \(\rho\) when \(\tau=0\), or of \(\rho^t\)
when \(\tau=1\), use nine nonnegative integer variables
\(j,u,v,h,p,A,B,z_2,z_3\), with
\[
\begin{gathered}
u\le x,\quad v\le b,\quad j+u+v+p\le s-2,\\
h\le j,\quad h\le x-u+v,\\
2A=u+v+1+p-\sigma,\qquad 2B=b-v+h-\tau,\\
2z_2+3z_3=j+x-u+v-2h-e.
\end{gathered}
\tag{D.17}
\]
The first equality records the endpoint sign, and the second records
the complementary determinant sign. The last equation is exactly
the coin count (D.16). Each variable is bounded by a linear function
of \(x+b+s+1\), so these are bounded rational polytopes with
logarithmic coordinate bounds. There are at most
\(2\cdot2\cdot(1+2+1)=16\) candidates before the fixed strip
test. After that test their exact counts are respectively
\(2,8,10,12,10,8,2\) for labels
\((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\).
Thus at most twelve tags occur for any label. These counts follow
by listing the horizontal and vertical two-strips in the three
partitions of three, with their displayed shift lists.

A point of (D.17) specifies the summand \((j,u,v)\) of (D.2), its
Clebsch–Gordan index \(h\), its endpoint monomial \(p\), and one
coin contribution to the required complementary irreducible label.
Conversely each such summand choice has uniquely determined parity
slacks \(A,B\) and gives the displayed lattice point. This proves
the claimed positive multiplicity count for (D.1), with no signed
terms or unspecified representation coefficients.

`stable_defect_correction.py` is the direct evaluator and complete
constraint-matrix exporter. `check_stable_defect_correction.py`
compares its positive count against literal induction over fixed
two-subsets, without using Clebsch–Gordan or Pieri on that comparison
side. All 896 comparisons passed, for every label, \(0\le x,b\le4\)
and \(2\le s\le6\), including 21 full matrix-count comparisons.
It enumerated and checked all 223 resulting lattice witnesses.
The receipt is `STABLE_DEFECT_CORRECTION_CHECK.txt`.

## Sources, scope and proof status

The scalar Cox component map and its action are the actual maps
proved in A-028; its primary locator is
[Castravet–Tevelev, Remark 3.9, p.1487](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/116C1106A59A410F79236A57C5477270/S0010437X06002284a.pdf/hilberts-14th-problem-and-cox-rings.pdf).
The projective-plane vanishing in (D.4) and the line Čech pairing are
[Stacks Project, Lemmas 30.8.1 and 30.8.2](https://stacks.math.columbia.edu/tag/01XS).
The full Schur complex and all its maps are the verified signed
tensor/projector construction in the archive appendix. Every other
comparison and rank assertion used here is proved by the displayed
maps, interpolation resolution and scalar dimension calculation.

The stable bound \(k\ge3s-1\) simultaneously ensures the scalar
dimension equality and the directional jet-surjectivity bounds.
No assertion outside it is used. T-046 supplies the first case
\(s=2\), including its independent full-proof reviews and actual
plethysm checks. The present complete proof has now been read and
checked independently by the root, rectangular and archive agents.
The rectangular agent independently compared 105 actual plethysm
coefficients, comprising every valid \(s=3,n\le7\) and
\(s=4,n\le8\) case and every outer label; its correction traces
were reconstructed from literal fixed two-subsets. The archive agent
independently checked 2744 correction multiplicities from the actual
twelve-element stabilizer matrices and two-by-two Jacobi–Trudi
characters, 42 restriction-character identities, 42 literal matrix
counts with 258 witnesses, and sixteen directional-jet ranks at
degrees \(2r-1,2r\) for \(1\le r\le8\).
The receipts are
`work/rectangular/OUTER5_STABLE_DEFECT_INDEPENDENT_CHECK.tsv` and
`work/archive/STABLE_DEFECT_INDEPENDENT_RECEIPT.json`.
The archive review explicitly identifies the finite normal module
as \(t_*\mathcal O(-s)\), for the truncated morphism
\(w=XYv\); projection formula and the displayed regular
automorphism then give the bundle comparison without inverting
\(XY\) at either endpoint.
