# The five-point Cox ring and the Segre cubic, with the exact group action

## A-028. Source identification and actual algebra map

Let \(E=\mathfrak h_5\), let \(Z=\{[\ell_i]\}_{i=1}^5\subset\mathbf P(E)\), and let \(X=\operatorname{Bl}_Z\mathbf P(E)\). Write \(H\) for the pullback of the hyperplane class and \(E_i\) for its five exceptional divisors. Choose the canonical exceptional sections \(e_i\), with their literal permutation action. The following explicit map identifies the Cox ring with the Plücker coordinate ring of \(\operatorname{Gr}(2,6)\):
\[
\boxed{
p_{i6}\longmapsto e_i,\qquad
p_{ij}\longmapsto
\frac{q_i-q_j}{\prod_{k\notin\{i,j\}}e_k}
\quad(1\le i<j\le5).
}
\tag{Cox.1}
\]
Here \(\sum_iq_i=0\), and \(p_{ji}=-p_{ij}\). Its Picard grading is
\[
\deg p_{i6}=E_i,\qquad
\deg p_{ij}=H-\sum_{k\notin\{i,j\}}E_k.
\tag{Cox.2}
\]
The \(S_5\) action permutes the first five Plücker indices and fixes the sixth. It is equivariant under (Cox.1), including the signs arising when an ordered pair is reversed.

The primary general Cox-ring locator is A.-M. Castravet and J. Tevelev, *Hilbert's 14th problem and Cox rings*, **Compositio Math. 142** (2006), 1479–1498, **Remark 3.9, p. 1487**. I opened and read the [author's published PDF](https://people.math.umass.edu/~tevelev/14problem.pdf). Its \(s=1,n=3\) instance identifies this Cox ring with the Plücker ring of \(\operatorname{Gr}(2,6)\). The exact map and action above are verified below rather than inferred from an abstract ring isomorphism.

For the Segre map and the representation convention, I opened and read I. Dolgachev, B. Farb and E. Looijenga, *Geometry of the Wiman–Edge pencil, I: algebro-geometric aspects*, [author PDF](https://www.math.uchicago.edu/~farb/papers/wiman.pdf), **§2.3, Table 1, p. 10**, and **Remark 2.4, p. 13**. Table 1 gives the five-dimensional representation with transposition trace 1; Remark 2.4 describes the equivariant quadratic map through the five frame points and identifies the ambient \(S_6\) representation as \([(3,3)]\). The printed remark contains a dimension typo \(\mathbf P^4=\mathbf P(V)\): the \(V\) fixed in §2.3 has dimension four and its projectivization is \(\mathbf P^3\). The quadratic map and target dimension in the surrounding discussion specify the intended spaces.

## 1. Proof of the Cox map through one additive-group action

Take the polynomial ring
\(P=\mathbf Q[x_1,\ldots,x_5,y_1,\ldots,y_5]\)
and the action of \(\mathbf G_a\) given by \(y_i\mapsto y_i+t x_i\), with \(x_i\) fixed. The invariant polynomials include
\[
x_i,\qquad p_{ij}=x_i y_j-x_jy_i.
\]
The invariant algebra is the Plücker ring of \(\operatorname{Gr}(2,6)\), with \(p_{i6}=x_i\). Here is a direct comparison map. Regard \((x_i,y_i)^T\) as the first five columns of a \(2\times6\) matrix and set the sixth column equal to \((0,1)^T\). Its stabilizer in \(SL_2\) is exactly the displayed additive group. An invariant function of the first five columns extends uniquely to an \(SL_2\)-invariant regular function on the open set where the sixth column is nonzero: choose locally an \(SL_2\) element sending that column to \((0,1)^T\), and use additive invariance to make the value independent of the choice. The two standard coordinate charts of the nonzero sixth column give regular choices. The complement has codimension two in affine matrix space, so the function extends across it by the intersection property of polynomial-ring localizations. Restriction and extension are inverse ring maps.

Finally, the \(SL_2\) invariant algebra of six column vectors is the image algebra of their \(2\times2\) minors. This can be seen directly from the Cauchy decomposition: its degree \(2d\) part is \(S_{(d,d)}\mathbf Q^6\), and products of the minors contain a nonzero highest vector in every such summand. Their span is \(GL_6\)-stable, so it contains the whole summand. This is precisely the Plücker coordinate ring. The construction commutes with permutation of the first five columns.

To identify this invariant algebra with the Cox ring using the specified grading, put
\[
u=\prod_i x_i,\qquad r_i=y_i/x_i,\qquad
q_i=u\left(\frac15\sum_jr_j-r_i\right).
\tag{Cox.3}
\]
These \(q_i\) are polynomial invariants, have sum zero, and transform by the standard representation. On \(u\ne0\), the differences of the \(r_i\) are coordinates for the additive quotient. Thus the localized invariant ring is exactly
\(\mathbf Q[x_i^{\pm1},q_1,\ldots,q_5]/(\sum q_i)\).
Sending \(x_i\) to \(e_i\) gives
\[
x_i y_j-x_j y_i
=\frac{q_i-q_j}{\prod_{k\notin\{i,j\}}x_k},
\]
which proves the formula for each generator in (Cox.1).

Assign \(\deg x_i=E_i\) and
\(\deg y_i=H-\sum_{j\ne i}E_j\).
Then \(q_i\) has degree \(H\), and every homogeneous element of the localized invariant ring is a polynomial \(f(q)\) of some degree \(c\), multiplied by \(\prod_i x_i^{a_i}\). Its degree is \(cH+\sum_i a_iE_i\).

It remains to check which such elements are polynomial before localization. Along \(x_i=0\), the vector \(q\) in (Cox.3) becomes the nonzero scalar
\(-y_i\prod_{j\ne i}x_j\) times \(\ell_i\) on the generic locus. The normalized transverse coordinates have leading terms \(x_i(r_j-r_l)/y_i\), with \(j,l\ne i\); their three independent differences vary freely. The same lowest-term calculation as G-015 therefore proves
\[
\operatorname{ord}_{x_i}f(q(X,Y))
=\operatorname{mult}_{[\ell_i]}f.
\]
The scalar trivializing the homogeneous degree-\(c\) factor is a unit there. Since the \(x_i\) are distinct primes, the Laurent expression is polynomial exactly when
\(\operatorname{mult}_{[\ell_i]}f+a_i\ge0\) for every \(i\).

These are exactly the section conditions for
\(\mathcal O_X(cH+\sum_i a_iE_i)\). They follow directly on the affine blow-up charts from divisibility by the required order of the point ideal. Positive exceptional coefficients permit their canonical sections but no additional poles downstairs: the removed points have codimension three, and a pole divisor cannot be supported on them. The criterion therefore identifies each Picard-graded piece, and multiplication is the same multiplication of Laurent polynomials. This proves the full ring isomorphism (Cox.1) with its exact action.

## 2. The quadratic subalgebra as an actual Cox component

Put \(D=2H-\sum_iE_i\). Under (Cox.1), the space
\(H^0(X,\mathcal O_X(D))\) is the space \(U\) of quadrics through the five points. Its Plücker multidegree is \((1,1,1,1,1,1)\), and its Plücker degree is three.

To verify the degree conversion explicitly, let \(b_{ij}\) count a factor \(p_{ij}\) with \(i,j\le5\), and let \(a_i\) count \(p_{i6}\). If its Cox degree is \(cH-k\sum E_i\), then
\[
\sum_{i<j}b_{ij}=c,\qquad
a_i+\sum_{j\ne i}b_{ij}=c-k.
\]
Hence its six column weights are
\[
(c-k,c-k,c-k,c-k,c-k,3c-5k),
\]
and its total Plücker degree is \(4c-5k\). Substituting \(c=2,k=1\) gives the asserted degree three and six equal weights.

The multilinear \(SL_2\) invariants of six columns are the Specht module \([(3,3)]\). This follows from the tensor Schur–Weyl decomposition, with the \(SL_2\)-invariant determinant power \(S_{(3,3)}\mathbf Q^2\). Restriction from the literal \(S_6\) column permutation action to the stabilizer of column six removes the unique removable box from \((3,3)\), giving \([(3,2)]\). Thus the extension of the quadratic \(S_5\) action to \(S_6\) is fixed by this actual column model; no choice of a projective lift determines it implicitly.

The same degree conversion sends every \(H^0(X,kD)\) to column weights \((k^6)\). Permuting all six columns preserves this diagonal component and therefore gives an \(S_6\) action on the whole \(D\)-section ring. It preserves the original \(S_5\) action on the first five indices. Permutations involving the sixth index act on this diagonal ring regardless of their action on the other Picard degrees.

By A-027 the algebra generated by \(U\) has the exact presentation
\[
\mathbf Q[A,B,C,D,E]/
\bigl(AD(E-B-C)-BC(E-A-D)\bigr).
\]
By A-029 the ordinary and saturated ideal powers agree in degree \(2k\) for every \(k\). Consequently multiplication of the quadrics maps this algebra isomorphically onto
\(\bigoplus_{k\ge0}H^0(X,kD)\).
This identifies the full section ring along the displayed Cox degree with the cubic algebra, including every graded piece and its action.

The cubic has sign character under \(S_5\), as the direct transposition calculation in A-027 shows. T-038 separately constructs its six linear forms and the actual exceptional six-element permutation action; that explicit intertwiner compares its usual six-coordinate Segre equation with the quadratic coordinates above. The present Cox calculation fixes the geometric \(S_6\) extension as \([(3,3)]\) in degree one.

## 3. The exact maps to ordinary and sheaf powers

There is an injective bigraded map
\[
\mathcal R(I)=\bigoplus_{k\ge0}I^k t^k
\longrightarrow\operatorname{Cox}(X),\qquad
f(q)t^k\longmapsto f(q)\left(\prod_i e_i\right)^{-k}.
\]
Its degree-\((c,k)\) image is \((I^k)_c\) in the Cox component
\(H^0(X,cH-k\sum E_i)\), which is the corresponding saturated fat-point section space. The component map is the usual inclusion of ordinary ideal powers into their sheaf sections. A-029 proves it is onto for \(c\ge2k\). Thus the quadratic cubic algebra, the ordinary Rees algebra, and the Cox section spaces are related here by specified inclusions and the stated equalities of graded components.

The full flag problem G-015 additionally tensors by its specified flag line bundle. The proofs here determine the point-ideal algebra and its action and provide the exact cohomology inputs recorded in A-029. They make no assertion that an alternating resolution alone has already evaluated every \(S_5\)-covariant flag-section multiplicity.
