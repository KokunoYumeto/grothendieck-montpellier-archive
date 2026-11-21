# Independent review of G-015 and G-016

## Status

**PASS, complete proof read.** The general projective-frame section model and the full quadratic ideal calculation are correct in their stated characteristic-zero scope. The original \(S_m\) action and determinant line are retained throughout. The proof gives the actual comparison map and the ordinary sheaf ideal powers; it proves the needed equality of orders without assuming a higher-cohomology vanishing statement.

I separately opened the original primary source [P. Magyar, *A Borel–Weil Construction for Schur Modules*, arXiv:alg-geom/9411014v1](https://arxiv.org/pdf/alg-geom/9411014) and read Proposition 1, printed pp. 5–6, the Plücker determinant bundle convention on p. 7, and Proposition 4\(a\)–\(c\), printed p. 10. These give the dual Schur convention and the precise full-flag pullback used in GF.2 and GF.7. All maps in this specialization are defined over \(\mathbf Q\). The source's algebraically closed field convention in §2 causes no rational-field gap: global sections commute with field extension, as follows from an affine-cover equalizer and flatness, and a map becoming an isomorphism after the faithfully flat extension \(\mathbf Q\subset\overline{\mathbf Q}\) was already an isomorphism.

## 1. The exact general chart and its linearization

The chart T-032 takes a smaller flag polynomial \(F\) to
\[
u^{n-\lambda_2}F(v(X)),\qquad
v_{j,I}=\left(\prod_{i\notin I}x_i\right)p_{j,I},
\quad u=\prod_i x_i.
\]
The map \(w\mapsto\mathbf1\wedge w\) identifies the smaller exterior coordinates with the displayed minors. Row permutations fix \(\mathbf1,u\), commute with centering, and act on every exterior power by its literal permutation matrix. Thus the chart preserves the exact \(S_m\) action. The full-height smaller flag factor is \(\det E\); its sign character is the last factor of \(\mathcal L_\tau\), not a separate omitted twist.

The highest-weight and row-weight calculation in C.12–C.13 gives precisely \(\lambda_2\) factors of height at least two and the common residual exponent \(n\) for every \(x_i\). The inverse dense chart C.14 recovers any prescribed smaller matrix and any nonzero \(u\). Consequently polynomial extension is exactly divisibility by \(u^k\), as asserted in GF.8. The invariant form on \(E\) is nondegenerate and equivariant over \(\mathbf Q\), so its Schur functor gives the specified map from the section convention \(S_\tau E^*\) to \(S_\tau E\).

## 2. Every higher flag frame is independent of the leading normal directions

At \(x_m=\varepsilon\), with \(s_m=S\ne0\), the first-line coordinates are exactly
\[
a_j=\varepsilon\frac{r_j-r_1}{S-\varepsilon r_1},
\qquad 2\le j\le m-1.
\]
The (m-2) coordinates are a regular parameter system at \([\ell_m]\) in \(\mathbf P(E)\). Pullback along the flag bundle gives a regular parameter system transverse to its whole fiber.

The subfamily \(X_{mj}=0\) for \(j\ge3\) is sufficient to test the possible leading-coefficient cancellation. At \(\varepsilon=0\), a nonzero minor must contain row \(m\); expansion along that row uses only the entry \(S\) in column two. After factoring out the \(x_i\), every remaining minor is an exterior coordinate in the columns
\[
\mathbf1,\quad (X_{i3}/x_i)_{i<m},\quad\ldots,
(X_{im}/x_i)_{i<m}.
\]
No such coordinate depends on the \(r_j\). The quotient \(E/\mathbf Q\ell_m\) is exactly \(\mathbf Q^{m-1}/\mathbf Q\mathbf1\): restricting the first (m-1) coordinates is surjective onto that quotient, with kernel \(\mathbf Q\ell_m\). The remaining ratio columns are arbitrary, so their classes realize every generic flag and every choice of nonzero successive frame scalings in the quotient. Varying \(S\prod_{i<m}x_i\) supplies the first-line frame; successive column scalings supply all higher exterior frames. The last one is nonzero whenever those quotient columns form a basis, so the determinant factor also has valuation zero.

Meanwhile the (m-2) differences \(r_j-r_1\) vary freely with all those image flag and frame coordinates fixed. This proves the required algebraic independence over the image fiber's function field. It is stronger than independence of only the first line: it includes every higher coordinate which can occur in \(F\).

## 3. Equality of orders and the ordinary ideal powers

Choose local nonzero Plücker coordinates at the generic fiber point. On the exhibited family each has valuation zero, so the local trivialization of \(\mathcal L_\tau\) introduces no extra factor of \(\varepsilon\). A section with lowest nonzero transverse term of degree \(h\) has leading coefficient equal to that nonzero polynomial evaluated at the independent \((r_j-r_1)/S\). It cannot vanish. The opposite inequality follows because every transverse parameter is divisible by \(\varepsilon\). This proves exact equality of the original coordinate-divisor valuation and the fiber-ideal order.

The special subfamily used here need not dominate the entire original divisor: the lower-order divisibility is valid on its full open chart, and nonvanishing on this subfamily proves nonvanishing of the universal leading coefficient. Its independence statement is exactly what is needed for the reverse inequality.

The generic order detects the ordinary sheaf power everywhere on the fiber. Indeed the fiber is a regular embedding and its graded normal quotients are locally free over an integral flag variety. A section of such a quotient which is zero at the generic point is zero globally. Induction through the first \(k\) graded pieces therefore gives membership in \(\mathcal I_i^k\) at every point, not just symbolic membership at one generic point.

The original \(x_i\) are pairwise nonassociate primes. Hence the \(m\) valuations are equivalent to divisibility by \(\prod_i x_i^k\). The fibers are disjoint, so their powers are pairwise comaximal and intersection equals product. Flatness of the flag projection identifies that product with \(\pi^*\mathcal I_{Z_m}^k\). Applying the actual chart map proves GF.4, and the specified Specht covariant functor proves GF.5.

The cases \(k=0\), \(n=0\), and \(m=3\) cause no change in the argument. For \(m=3\), the quotient flag fiber is a point, the transverse system has one parameter, and the same independence test still applies.

## 4. The full quadratic ideal and its action

Set \(r=m-1\ge3\) and use the \(r\) coordinate points plus \([1:\cdots:1]\). In degree two, vanishing at the coordinate points removes every square, while vanishing at the last point imposes exactly one sum-zero relation on the mixed coefficients. This gives the listed differences \(z_i z_j-z_1z_2\).

In their quotient, write \(z=z_1z_2\). For distinct (i,j), choose \(a\notin\{i,j\}\); then
\[
z_i z=z_i(z_jz_a)=z_j(z_i z_a)=z_jz.
\]
Every mixed degree-\(C\) monomial contains a cross-product, and this identity replaces every remaining factor by \(z_1\). Thus the pure powers \(z_i^C\) and the single mixed class \(zz_1^{C-2}\) span. Evaluation at the coordinate points isolates the coefficients of the pure powers, and evaluation at the last point then isolates the mixed coefficient. They are independent. This proves the asserted basis in every degree, including the low degrees separately.

The resulting graded map to the product of line coordinate rings is injective. Its kernel before quotienting is exactly the intersection of the homogeneous linear prime ideals of those lines. Hence the generated ideal is radical and saturated as well as the full projective ideal. The dimension of its quadratic piece is \(m(m-3)/2\).

Returning to the exact affine representatives \(\ell_i\), evaluation is equivariant without a scaling character. The two eigenvalues for the matrix of the values of \(q_i^2\) are \((m-2)/m\) and \((m-1)/m\); for \(q_i^3\) they are \(1-3/m+3/m^2\) and \((m-1)(m-2)/m^2\). These are nonzero for the stated \(m\). The invariant quadratic has the same nonzero value at each point and propagates surjectivity by two degrees. The established dimensions make evaluation an isomorphism onto \(\operatorname{Perm}_m\) for every \(C\ge2\). Degrees zero and one give its constant and standard submodules. All the actions in GF.15 are therefore literal evaluation maps.

For \(m=3\), the three differences \(q_i-q_j\) are distinct line equations on \(E\), each vanishing at one frame point. Their product gives exactly the reduced degree-three divisor ideal and changes by sign under permutations. This is the stated separate cubic formula.

## 5. Independent check supplied for the next \(m=5\) computation

The subsequent cubic and full resolution are being written by the theta agent in T-038. I supplied an independent verification of its quadratic-subalgebra kernel; the full resolution was not audited in this event.

For the five quadrics
\[
A=z_1z_3-z_1z_2,\ B=z_1z_4-z_1z_2,\
C=z_2z_3-z_1z_2,\ D=z_2z_4-z_1z_2,\ E=z_3z_4-z_1z_2,
\]
the nonzero cubic
\[
F=AD(E-B-C)-BC(E-A-D)
\]
maps to zero; exact symbolic expansion confirms it. Put \(x=z_1z_2\). In the image fraction field,
\[
x=\frac{AD}{E-A-D},\qquad
z_1^2=\frac{x(x+A)}{x+C}.
\]
All six pair products follow from \(x,A,B,C,D,E\), and all \(z_i\) follow from them and \(z_1\). Thus \(\mathbf Q(z_1,z_2,z_3,z_4)\) is algebraic of degree two over the image field, so that field has transcendence degree four. The cubic is primitive linear in \(E\): its coefficient \(AD-BC\) is irreducible, and does not divide its constant term, as the substitution \((A,B,C,D)=(1,2,3,6)\) gives constant 12. Gauss's lemma proves irreducibility. The kernel is consequently the height-one prime \((F)\).

Under the actual coordinate transposition \(z_1\leftrightarrow z_2\), the quadrics transform by \(A\leftrightarrow C\), \(B\leftrightarrow D\), and \(E\mapsto E\), so \(F\mapsto-F\). The degree-three kernel is one-dimensional and stable under \(S_5\), and a one-dimensional character of \(S_5\) is determined by a transposition. Hence this relation has sign character, agreeing with theta's independent calculation. This is an explicit algebra map and relation, not a dimension-only comparison.
