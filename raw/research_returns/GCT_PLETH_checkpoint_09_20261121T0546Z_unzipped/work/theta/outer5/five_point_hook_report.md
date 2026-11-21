# A five-point hook-bundle family

## T-041. Statement and exact flag comparison

For \(a\ge1\), \(d\ge0\), put
\[
n=d+a+1,\qquad
\lambda=(d+2a+4,d+a+2,d+a,d+a-1,d).
\tag{5H.1}
\]
Let \(E=\mathfrak h_5\), \(U=[3,2]\), and
\(\epsilon=\operatorname{sgn}\). There is an actual equivariant isomorphism
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes U\otimes S_{(a,1)}E.}
\tag{5H.2}
\]
Every outer \(\mu\vdash5\) has the positive formula below with at most
90 fixed polytopes of dimension at most four. For symmetric outer power,
\[
\boxed{p_{(5),(n)}^\lambda>0\quad\Longleftrightarrow\quad a\ge2.}
\tag{5H.3}
\]

Indeed \(\lambda_2-n=1\), \(\lambda_2-\lambda_3=2\), and
\((\lambda_3-\lambda_5,\lambda_3-\lambda_4)=(a,1)\).
The actual chart and extension map of G-015 therefore identifies the
left side of (5H.2) with
\[
\epsilon^{d+a}\otimes
H^0(\mathbf P(E),\mathcal I_Z(2)\otimes S_{(a,1)}Q),
\tag{5H.4}
\]
where \(Q=E/\mathcal O(-1)\) and \(Z\) is the five canonical frame
points. To check every determinant, the relative quotient-flag weight
after removing the full determinant shift is \((a,a-1,0)\).
Complementary exterior-column pairings in the rank-three quotient give
\[
S_{(a,a-1)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,1)}Q.
\]
This is the restriction of the perfect wedge pairings of complementary
columns in the height-three, width-\(a\) rectangle to their Schur
summands. The first-line twist is \(a+2\); the identity
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\) leaves
\(\mathcal O(2)\). The full determinant contributes \(\epsilon^d\),
so the total character is \(\epsilon^{d+a}\), as claimed.
The inverse flag chart is \(F\mapsto u^{-1}F(v(X))\); G-015 proves
that (5H.4)'s ideal condition is exactly its polynomial extension
condition. Thus no determinant or extension condition is suppressed.

## 1. An exact hook resolution

For a vector space \(V\), write
\[
H_a(V)=\ker(V\otimes\operatorname{Sym}^aV
                    \longrightarrow\operatorname{Sym}^{a+1}V).
\tag{5H.5}
\]
Multiplication has its equivariant polarization section divided by
\(a+1\). The kernel is \(S_{(a,1)}V\): it contains the highest vector
\(v_1\otimes v_1^{a-1}v_2-v_2\otimes v_1^a\), and the irreducible
highest-weight summand it generates has the kernel's dimension by the
Weyl dimension formula. This specifies the hook functor used here.

The line inclusion \(L=\mathcal O(-1)\subset E\otimes\mathcal O\)
gives the exact locally free resolution
\[
0\to L^2\otimes\operatorname{Sym}^{a-1}E
\mathrel{\mathop{\longrightarrow}^{d_2}}
L\otimes E\otimes\operatorname{Sym}^{a-1}E
\mathrel{\mathop{\longrightarrow}^{d_1}}
H_a(E)\otimes\mathcal O\to H_a(Q)\to0,
\tag{5H.6}
\]
with actual maps
\[
d_2(l^2\otimes v)=l\otimes l\otimes v,\qquad
d_1(l\otimes e\otimes v)=e\otimes(lv)-l\otimes(ev).
\tag{5H.7}
\]
Their composition is zero. For exactness choose a local splitting
\(E=L\oplus W\). In \(d_1\), the first tensor factors in \(W\)
record \(e\otimes lv\). Multiplication by \(l\) is injective, so
\(\ker d_1\) is exactly the subspace with \(e\in L\), the image of
\(d_2\). The map \(H_a(E)\to H_a(Q)\) is onto by the splitting.
An element of its kernel has the form
\(\sum e_i\otimes lv_i+l\otimes w\), with \(e_i\in W\).
The zero-product condition says \(w=-\sum e_iv_i\), so this element
is \(d_1(l\otimes\sum e_i\otimes v_i)\). This proves exactness at
every term of (5H.6).

## 2. All cohomology used in the formula

Put \(B_a=H_a(Q)\). The scalar projective-space calculation of Stacks
Project, Lemma 30.8.1, applied to (5H.6) gives
\[
H^0(B_a)=H_a(E),\quad H^{i>0}(B_a)=0,
\qquad H^i(B_a(-1))=0\quad\text{for all }i.
\tag{5H.8}
\]
The negative twists involved are respectively \(-2,-1\) and
\(-3,-2,-1\), all acyclic on \(\mathbf P^3\).

For \(B_a(-3)\), the three terms of (5H.6) have twists
\(-5,-4,-3\). The only possible cohomology is the map
\[
H^3(\mathcal O(-5))\otimes\operatorname{Sym}^{a-1}E
\longrightarrow H^3(\mathcal O(-4))\otimes E
                                      \otimes\operatorname{Sym}^{a-1}E.
\tag{5H.9}
\]
It is the identity under the natural identifications. The ordered Čech
generator indexed by \(i\) in the source is
\(1/(x_1x_2x_3x_4x_i)\). Multiplication by the \(j\)-th coordinate
of the line inclusion gives the top class \(1/(x_1x_2x_3x_4)\) for
\(j=i\); for \(j\ne i\), one exponent is zero, so the top class
vanishes. Thus the matrix is exactly \(\delta_{ij}\). Both spaces
carry the same factor \(\det E=H^3(\mathcal O(-4))\), so this is
also the correct equivariant map. The two short exact sequences of
(5H.6) consequently prove
\[
\boxed{H^i(B_a(-3))=0\quad\text{for all }i,\ a\ge1.}
\tag{5H.10}
\]
This includes the boundary \(a=1\), where the hook is \(\Lambda^2Q\).

Now tensor T-038's actual five-point resolution by \(B_a(2)\):
\[
0\to\epsilon B_a(-3)\to\epsilon U\otimes B_a(-1)
\to U\otimes B_a\to\mathcal I_Z(2)\otimes B_a\to0.
\tag{5H.11}
\]
Tensoring is exact because \(B_a\) is locally free. Both left terms
are acyclic by (5H.8) and (5H.10), hence multiplication gives the actual
isomorphism
\[
U\otimes H_a(E)\longrightarrow
H^0(\mathcal I_Z(2)\otimes B_a).
\tag{5H.12}
\]
It multiplies the five specified quadrics by constant hook sections and
then applies the quotient \(E\to Q\). Together with (5H.4), this
proves (5H.2). Its dimension is \(5a(a+2)(a+3)/2\).

## 3. The complete fixed positive formula

For positive weights \(W\), let
\[
C_W(R)=\#\{x\in\mathbf Z_{\ge0}^{|W|}:\sum_{w\in W}wx_w=R\}.
\tag{5H.13}
\]
This is a bounded rational-polytope count, zero for \(R<0\). Use
\(C_4=C_{(2,3,4,5)}\) and \(C_3=C_{(2,3,5)}\).
The multiplicity \(L_\rho(a)\) of \([\rho]\) in \(H_a(E)\) is
\(\sum_{r\in A_\rho}C_4(a-r)+\sum_{r\in B_\rho}C_3(a-r)\),
with all shifts listed below. Repetitions are separate tags.

| \(\rho\) | \(A_\rho\) | \(B_\rho\) |
|---|---|---|
| \((5)\) | \(4,6,13\) | \(5,6,7\) |
| \((4,1)\) | \(2,3,3,4,4,4,5,5,5,6,6,7\) | empty |
| \((3,2)\) | \(2,3,3,4,4,4,5,5,5,6,6,6,7,7,8\) | empty |
| \((3,1,1)\) | \(1,2,3,3,4,4,5,5,5,6,6,6,7,7,7,8,8,9\) | empty |
| \((2,2,1)\) | \(2,3,4,4,5,5,5,6,6,6,7,7,8,8,9\) | empty |
| \((2,1,1,1)\) | \(3,4,4,5,5,6,6,7,7,8,9,10\) | empty |
| \((1^5)\) | \(6,7,8\) | empty |

To prove the table, the polarization splitting in (5H.5) gives the
actual decomposition
\(E\otimes\operatorname{Sym}^aE=H_a(E)\oplus\operatorname{Sym}^{a+1}E\).
Writing \(H_g(t)=\det(1-tg\mid E)^{-1}\), one obtains
\[
\sum_{a\ge0}\chi_{H_a(E)}(g)t^a
=(\chi_E(g)-t^{-1})H_g(t)+t^{-1},\qquad H_0(E)=0.
\tag{5H.14}
\]
Take inner products using the seven fixed character rows of QP.16's
following table. T-027's tableau standardization gives the common
denominator \(D(t)=(1-t^2)(1-t^3)(1-t^4)(1-t^5)\).
For each nontrivial row, its numerator has exactly the nonnegative
coefficients recorded as \(A_\rho\). For the trivial row the exact
polynomial identity is
\[
\begin{aligned}
&t^4+t^5+2t^6+t^7-t^9-t^{10}-t^{11}+t^{13}\\
&\hspace{8mm}=t^4+t^6+t^{13}+(1-t^4)(t^5+t^6+t^7).
\end{aligned}
\tag{5H.15}
\]
After division by \(D(t)\), this is precisely its three four-variable
and three three-variable counts. Seven exact rational identities verify
the full table in every degree, including its zero initial terms.

For \(\mu\vdash5\), put \(\nu=\mu\) when \(d+a\) is even and
\(\nu=\mu^t\) when \(d+a\) is odd. Let \(K_{\rho\nu}\) be the
completely listed fixed \([3,2]\)-tensor table in §4 of T-039. Then
\[
\boxed{p_{\mu,(n)}^\lambda=\sum_{\rho\vdash5}K_{\rho\nu}L_\rho(a).}
\tag{5H.16}
\]
Each summand is tagged by a tensor copy, a table row and a shift. For
\(\rho\ne(5)\) there are exactly \(3\dim[\rho]\) tags; the trivial
row has three additional tags. Self-duality and the tensor dimension
identity give the total
\[
15\dim[\nu]+3\mathbf1_{\nu=(3,2)}\le90.
\tag{5H.17}
\]
Each tag has one displayed equality and nonnegative coordinates with
weights \((2,3,4,5)\) or \((2,3,5)\). Every witness has
\(O(\log(a+2))\) bits. All tables have fixed size.

For symmetric outer power, only row \((3,2)\) contributes in even
parity and only row \((2,2,1)\) in odd parity. Both have shifts two
and three and no smaller shift. Since their positive weights generate
\(\{0\}\cup\{r:r\ge2\}\), they are positive exactly for \(a\ge2\),
which proves (5H.3). The sign outer partition has the same threshold.
Every other outer partition receives row \((3,1,1)\), with shifts one
and two, and is positive for every \(a\ge1\).

## Checks and primary sources

`five_point_hook_positive.py` contains the entire fixed positive
evaluator. `check_five_point_hook.py` verifies all seven exact rational
identities, the tag bounds, and 560 finite coefficient/support cases.
Receipts: `FIVE_POINT_HOOK_CHECK.tsv` and `.txt`. The semigroup argument
proves support in every degree; the finite checks supplement it.

The scalar cohomology and explicit Čech classes are those of
[Stacks Project, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS),
whose full calculation was read. The relative Schur and exterior-column
convention uses [Magyar, Proposition 1 and Proposition 4](https://arxiv.org/pdf/alg-geom/9411014),
as specified in T-039. The hook resolution and all its maps are proved
here. The finite-group table was checked against
[Dolgachev–Farb–Looijenga, §2.3, Table 1](https://www.math.uchicago.edu/~farb/papers/wiman.pdf).

At \(a=1\) this meets the exterior-square quotient-bundle family at
point power one. For \(a>1\), it evaluates the actual rank-three hook
section space in (5H.4). No vanishing for arbitrary Schur quotient
bundles or higher point powers is assumed.
