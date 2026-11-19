# Independent checks and computation limits

Run SA15-20261119/cotes6_7; GPT-6 Astra Pro, effort not exposed. Code: code/computations.py. Exact output: outputs/computations.json. These checks concern recorded claims, not development of the ranked research directions. Finite symbolic samples never replace the infinite or geometric arguments below. No manuscript reading is changed.

## 1. The ordinary cusp does not give the proposed counterexample

**P67-C045; P67-I050; P67-P021.** The natural reading of cote7/024 is an ordinary cusp. Its abbreviated singularity word remains a scan question.

Let \(A=\mathbf C[x,y]/(y^2-x^3)\), with the **full** exterior Kähler complex, including its nonzero second term. Give \(x,dx\) weight2 and \(y,dy\) weight3. The relation is homogeneous of weight6. The Euler derivation \(E=2x\partial_x+3y\partial_y\) preserves the ideal, hence contraction \(i_E\) exists on the quotient differential algebra. Cartan's identity holds on the generators and respects the relations:
\[
d i_E+i_Ed=L_E.
\]
On weight \(w>0\), \(L_E=w\), so \(h=i_E/w\) contracts that subcomplex. Each form is a finite sum of homogeneous forms. Weight zero is exactly \(\mathbf C\) in degree0. Thus
\[
H^0(\Omega^\bullet_A)=\mathbf C,\qquad H^i(\Omega^\bullet_A)=0\quad(i>0).
\]
The analytic normalization \(t\mapsto(t^2,t^3)\) is a finite, hence proper, bijection from \(\mathbf C\) to the cusp. A proper continuous bijection between locally compact Hausdorff spaces is a homeomorphism. Singular \(H^1\) also vanishes. Both sides of the alleged mismatch are checked.

The tempting incorrect calculation discards \(\Omega^2\) because the curve has dimension1. In fact
\[
\Omega^2_A=A/(x^2,y)\,dx\wedge dy\ne0.
\]
The torsion one-form \(\tau=3y\,dx-2x\,dy\) is not closed: \(d\tau=-5\,dx\wedge dy\). The code checks this sign and the homogeneous calculation. The quotient \(\Omega^1/dA\) alone is not \(H^1\) of the full complex.

The general criticism remains P67-C046. Arapura–Kang2011 Proposition4.2/Example4.4 gives the non-quasihomogeneous curve \(x^5+y^5+x^2y^2=0\), with \(\mu=11,\tau=10\), and excess analytic Kähler–de Rham \(H^1\). These local numbers are an **opened published result**, not this run's independent Gröbner certificate.

An extra algebraic/analytic bridge is needed for that replacement example. Here is the explicitly reconstructed argument. Normalize the reduced affine algebraic curve. Its normalization is smooth affine, where algebraic de Rham comparison holds. The kernel and cokernel of the map from the singular Kähler complex to the normalization complex have finite support at the singularities, including the torsion in \(\Omega^1\) and all higher exterior terms. Their finite-dimensional local algebraic and analytic pieces agree. The resulting comparison diagram transfers analytic failure to the algebraic full Kähler complex. The citation is not silently presented as having stated this bridge in exactly that form. The independent ordinary-cusp refutation does not depend on it.

## 2. Isogenous to a mixed elliptic product does not mean isomorphic

**P67-C013; P67-I012; P67-P008.** This checks the natural abelian-surface reconstruction of the unsure phrase on6/049.

Over \(k=\overline{\mathbf F}_7\), take the smooth projective model of
\[
C:\quad y^2=(x^2-1)(x^2-2)(x^2-5).
\]
There are six distinct branch roots and characteristic is not2, so its genus is2. The code checks the polynomial gcd with its derivative. Degree-two quotient maps are
\[
(u,v)=(x^2,y),\qquad (u,w)=(x^2,xy),
\]
to
\[
E_1:v^2=(u-1)(u-2)(u-5),\qquad
E_2:w^2=u(u-1)(u-2)(u-5).
\]
Both targets have smooth genus-one projective models and rational points. The quartic has two points at infinity, both included in the count. Exact enumeration gives8 and12 points over \(\mathbf F_7\), hence traces0 and−4. The first elliptic curve is supersingular and the second ordinary, so they are not geometrically isogenous.

The pulled-back differentials are \(2x\,dx/y\) and \(2\,dx/y\), spanning \(H^0(C,\Omega^1)\). The induced product-to-Jacobian map is an isogeny; the complementary involutions give a \((2,2)\)-isogeny.

If the underlying surface \(J(C)\) were isomorphic to \(F_1\times F_2\), its two isogeny factors would again be one ordinary and one supersingular elliptic curve. Cross Hom groups vanish. Every polarization is then diagonal, and every principal polarization is a product of degree-one elliptic polarizations, with reducible theta divisor. The canonical principal polarization of a smooth genus-two Jacobian has irreducible theta divisor, a translate of \(C\). Pullback across the alleged product isomorphism is impossible. Thus even as an unpolarized abelian variety the Jacobian is not a product.

The program certifies the polynomial and finite point counts. The isogeny and polarization arguments are the independent geometric proof, not output of the program.

## 3. Barsotti's p-rank-zero question

**P67-C010–C012.** The author defines “hypersingulier” by absence of geometric points of order \(p\), meaning p-rank zero.

Lenstra–Oort1974 §2, printedpp48–51, constructs **geometrically simple** abelian varieties of the exact types used here. For each prime \(p\), choose \(A_3\) of type \(G_{21}+G_{12}\), \(A_4\) of type \(G_{21}+G_{12}+G_{11}\), and a supersingular elliptic \(E\), all over \(\overline{\mathbf F}_p\). Then \(A_4\) and \(A_3\times E\) have dimension4 and p-rank zero, and their formal groups are isogenous with the same slope blocks \(1/3,2/3,1/2\). They are not isogenous as abelian varieties, because simplicity is invariant under isogeny. This uses a construction theorem actually read, not an existence assertion inferred from an arbitrary Newton polygon.

For an abelian surface, polarization pairs \(\lambda\) with \(1-\lambda\). A reduced denominator \(b\) divides the multiplicity of that slope. A non-half pair with \(b\ge3\) would require height at least6, impossible in height4. With slopes0,1 absent, all slopes must be1/2. The supersingular isogeny theorem therefore gives the positive dimension-two answer. The slope argument is independent; the supersingular theorem is background from the opened references.

## 4. A finite-field formal twist and its residual

**P67-C015–C016.** Choose a supersingular elliptic curve over a finite square field where all its geometric endomorphisms are defined and Frobenius is scalar. Choose \(u\in1+p\mathbf Z_p\) transcendental over \(\mathbf Q\), using \(1+4\mathbf Z_2\) for \(p=2\). Such units exist by uncountability.

The map \(\widehat{\mathbf Z}\to1+p\mathbf Z_p\), \(z\mapsto u^{z_p}\), is continuous by p-adic exponential/logarithm. On each \(G[p^n]\), a sufficiently deep congruence subgroup acts trivially. Effective finite-level descent, compatibly in \(n\), therefore gives a height-two, dimension-one p-divisible group over the finite field. This supplies the continuity suppressed in an “any unit” assertion.

Twisted Frobenius has eigenvalue \(u\lambda\), or \(u^{-1}\lambda\) under the opposite convention, with nonzero algebraic \(\lambda\). Every positive power remains transcendental. A formal p-divisible subgroup of an abelian variety over a finite field would produce a Frobenius-stable subobject/quotient of its isocrystal, whose Frobenius eigenvalues are algebraic. This contradiction persists over every finite extension.

The argument does **not** certify the arbitrary finitely generated extension clause. Spreading out an embedding compatibly at all p-power levels and specializing without losing injectivity is a further step. It is retained as a residual proof obligation, not declared an open problem of modern literature.

## 5. The two Hodge–Tate representation questions

**P67-C003–C004.** Over \(\mathbf Q_3\), put
\[
\psi(g)=\exp\bigl(\tfrac12\log\langle\chi_{\mathrm{cyc}}(g)\rangle\bigr).
\]
The pro-3 part of the cyclotomic character makes this a continuous one-dimensional \(\mathbf Q_3\)-representation, hence irreducible. The defining local logarithm formula in Brinon–Conrad Theorem15.1.7 gives Sen eigenvalue \(1/2\). A nonzero equivariant map to \(C_p(i)\) becomes a one-dimensional semilinear isomorphism after scalar extension, forcing an integral Sen eigenvalue. This contradiction answers the broad first question negatively.

For the second question, take a weakly admissible two-dimensional filtered Frobenius module over \(\mathbf Q_p\) with characteristic polynomial \(X^2+p\) and filtration weights0,1. The polynomial is irreducible; Newton and Hodge numbers are both1; no proper Frobenius-stable rational subspace remains to test. Brinon–Conrad Theorem8.3.6 gives an irreducible crystalline representation \(V\). Each nonzero Hodge–Tate component projection restricts to a nonzero map on \(V\); its rational kernel is a subrepresentation, hence zero. Twisting appropriately gives \(M\) and \(M(i)\), \(i\ne0\), both in \(C_p\). This is a deduction from an opened theorem, not a re-proof of the comparison equivalence.

## 6. Ordinary polarized local rings

**P67-C019–C020.** Yoneda extensions give a map of extensions precisely when pushout along \(v\) and pullback along \(u\) have equal classes. Choices form a torsor under \(\operatorname{Hom}(M,N')\). Uniqueness requires rigidity in the framed infinitesimal p-divisible/abelian problem; it is false for arbitrary abelian extensions.

Katz1981 Theorem2.1 identifies ordinary framed deformations with a formal torus of character lattice \(L=T_pA\otimes T_pA^t\). A polarization imposes symmetry after its Tate-module map. That map is invertible over \(\mathbf Q_p\), giving a relation lattice of rank \(g(g-1)/2\) and quotient free rank \(g(g+1)/2\). Smith form over \(\mathbf Z_p\) reduces the character equations to \((1+z_j)^{p^{e_j}}=1\), after absorbing units in coordinates. In characteristic \(p\) they become \(z_j^{p^{e_j}}=0\).

These powers of distinct variables form a regular sequence. The quotient is a complete intersection, hence Cohen–Macaulay and Gorenstein; its reduction is a power-series ring. It is locally irreducible with smooth reduction. For prime-to-p polarization the Tate map is integral-invertible and the symmetry lattice saturated, so the ring is smooth. The code records the model and sample dimensions. This is not a claim about every coarse quotient or the cancelled mixed-characteristic flatness clause.

## 7. Frobenius conventions, fixed vectors and the missing shift

**P67-C021–C028.** The relation \(F[a]=[a^p]F\), checked over \(\mathbf F_2[t]\), explains why left and right skew actions differ. It does not prove arbitrary-base Ext-freeness.

For a rank-\(r\) module with invertible linearized Frobenius, the local fixed equations are \(A x^{[p]}-x=0\). Multiplication by \(A^{-1}\) makes them monic in the \(p\)-th powers. Their leading monomials \(x_i^p\) are pairwise relatively prime, giving a free quotient of rank \(p^r\). The Jacobian before that multiplication is \(-I\); the fixed scheme is finite étale. The saved characteristic3 rank-two calculation is one exact instance. The global equivalence and spanning after an étale cover are taken from Bhatt–Scholze Proposition3.4, not inferred solely from the instance.

Resolve \(\mathbf Z/p\) by the two-term free resolution. In cohomological grading, derived tensor with \(\mathbf F_p\) has degrees−1,0, while \(\operatorname{RHom}_{\mathbf Z}(\mathbf Z/p,\mathbf F_p)\) has degrees0,1. An unshifted equality fails in this test. With the finite dual convention fixed, the expected correction is tensor shifted by \([-1]\). The scan must decide whether a shift is absent or unread.

## 8. Affine-line de Rham pathologies and weak completion

**P67-C038, C042, C059–C061, C066.** In characteristic \(p\), \(d(t^n)=n t^{n-1}dt\), so
\[
H^0=k[t^p],\qquad H^1=k[t^p]t^{p-1}dt.
\]
The program lists finite ranges for \(p=2,3,5\); the formula proves all degrees. Over imperfect \(k\), use relative Frobenius rather than literal pth powers of all coefficients.

Let \(W\{t\}\) be restricted power series and \(K=W[1/p]\). The infinite sets \(J_m=\{2^m(2r+1):r\ge1\}\) are disjoint. Define
\[
f_m(t)=\sum_{j\in J_m}p^{\lfloor j/2\rfloor}t^{p^j-1}.
\]
Each is restricted. In any finite nonzero \(K\)-linear combination, the primitive coefficients on a support with coefficient \(c_m\ne0\) have valuations \(v_p(c_m)+\lfloor j/2\rfloor-j\to-\infty\). No primitive lies in \(K\{t\}\). Thus infinitely many independent classes survive after inverting \(p\), proving infinite rank.

For an integral form \(\sum a_nt^n dt\), the primitive coefficients are \(a_n/(n+1)\). Integral restrictedness requires both \(v_p(a_n)\ge v_p(n+1)\) for every \(n\) and that their differences tend to \(+\infty\). The polynomial \(t^{p-1}dt\) defeats a tail-only integral criterion.

The literal bound \(|a_n|\le C\rho^n\), \(\rho>1\), does not mean decay. Constant coefficients satisfy it, as do restricted subexponential coefficients \(p^{\lfloor\sqrt n\rfloor}\). Overconvergence requires a positive linear valuation bound, equivalently exponential decay such as \(C\rho^{-n}\). The transcription retains the original sign.

In the integral dagger algebra, \([t^{p^r-1}dt]\) has exact order \(p^r\): integrating its \(p^s\)-multiple forces coefficient \(p^{s-r}\). The unbounded p-torsion exponent rules out a finite \(W\)-module. Over \(K\), dividing by \(n+1\) loses only logarithmic valuation, so positive linear growth survives after a small radius shrink; rational dagger \(H^1(\mathbf A^1)\) vanishes.

Finally \((\varprojlim\mathbf Z/p^n)\otimes\mathbf Q_p=\mathbf Q_p\), while \(\varprojlim((\mathbf Z/p^n)\otimes\mathbf Q_p)=0\). This proves the claimed failure to commute limit and rationalization.

## 9. Closed ideals with the standard p-adic topology

**P67-C062.** Van der Put1986 Proposition2.2 gives noetherianity of the weak-completion algebra. The geometric series in \(pa\) belongs to the weak completion for every \(a\), so \(1-pa\) is invertible and \(p\) lies in the Jacobson radical. Krull intersection for the noetherian module \(A/I\) gives \(\bigcap_n p^n(A/I)=0\). Thus \(I=\bigcap_n(I+p^nA)\): every ideal is p-adically closed. This proof fixes the topology rather than asserting a result about every unspecified dagger topology.

## 10. Derived versus ordinary base change

**P67-C056–C057.** The perfect complex \(K^\bullet=[\mathbf Z\xrightarrow p\mathbf Z]\) in degrees0,1 has \(H^0=0\), but after derived tensor with \(\mathbf F_p\) its differential is zero and \(H^0=\mathbf F_p\). Derived compatibility alone therefore does not give ordinary compatibility of each cohomology module. This algebraic countermodel is not presented as a geometric family with every manuscript hypothesis.

For a separate geometric warning, Kothari2026 Theorem1.1 (opened preprint version2, dated22December2024) constructs smooth projective equal-characteristic-p DVR families, with geometrically connected fibres and arbitrary jumps in de Rham degrees1 through \(n\), in relative dimension \(n+1\). This is an opened existence theorem, not a construction redone here. Proper smooth characteristic-zero Gauss–Manin has local freeness, which supplies the needed Tor control.

## 11. Cartan homotopy and a fully specified elliptic p-curvature

**P67-C069–C071.** Cartan's formula is checked on functions and their differentials, then extended by graded Leibniz. Two lifts of a base derivation differ by a vertical vector field, so their Lie derivatives differ by \(d i_D+i_Dd\) and give the same cohomological action. The bracket identity gives integrability. Global descent is supplied by Katz–Oda1968 §§2–3, not by the polynomial sample.

Take \(R=\mathbf F_3[t,1/(t(1-t))]\) and the smooth proper elliptic completion of
\[
E:\ y^2=x(x-1)(x-t).
\]
Its discriminant \(16t^2(1-t)^2\) is a unit. For \(\omega=dx/y,\eta=x\,dx/y,\partial=d/dt\), exact reduction gives
\[
\nabla_\partial\omega=-\frac{\omega}{2(t-1)}+\frac{\eta}{2t(t-1)}.
\]
The second coefficient is a unit, proving that \((\omega,\nabla_\partial\omega)\) is a basis. The code verifies the exact differential in this reduction.

Katz1984 p183 gives
\[
t(1-t)\nabla_\partial^2\omega+(1-2t)\nabla_\partial\omega-\tfrac14\omega=0.
\]
The column connection matrix is
\[
A=\begin{pmatrix}0&1/(4t(1-t))\\1&-(1-2t)/(t(1-t))\end{pmatrix}.
\]
Set \(B_0=I,B_{n+1}=B'_n+AB_n\). Since \(\partial^3=0\) on \(R\), p-curvature is \(B_3\). Exact arithmetic yields
\[
\psi(\partial)=\frac1{t^2(t-1)^2}
\begin{pmatrix}t+1&1\\-t^2+t-1&-t-1\end{pmatrix}\ne0,\qquad
\psi(\partial)^2=0.
\]
The upper-right entry proves nonvanishing on this actual smooth base. Ordinary stratification would imply zero p-curvature, so it cannot induce this connection. Nonzero **nilpotent** p-curvature does not contradict a crystalline/PD structure. The saved certificate checks entries, trace, determinant and square.

## 12. Other checks and limits

For **P67-C052**, a supersingular elliptic curve over \(\overline{\mathbf F}_p\) has a four-dimensional quaternion division algebra at \(p\). A faithful two-dimensional \(\mathbf Q_p\)-valued Weil realization embeds it in \(M_2(\mathbf Q_p)\), also dimension4, hence would identify a division algebra with an algebra having nonzero zero-divisors. This checks the reconstructed axioms, not an obstruction to slope-zero or Witt-fraction theories.

For **P67-C051**, prime factorization proves that a rational number integral at every prime other than \(p\) lies in \(\mathbf Z[1/p]\). This does not itself prove rationality of cohomological characteristic polynomials.

For **P67-C054**, Artin–Schreier and Zariski cohomological dimension give \(H^i_{\mathrm{et}}(X,\mathbf F_p)=0\) above \(\dim X+1\) for a noetherian characteristic-p scheme. Induction gives constant p-primary coefficients; no assertion about all finite flat coefficients follows.

For **P67-C006**, choose a relatively compact identity neighbourhood \(U\). If \(q\) is a continuous seminorm on \(C_c(E)\), \(f\mapsto\sup_{g\in\bar U}q(gf)\) is continuous on each fixed-support normed subspace, since all translates have support in a common compact. It is therefore continuous for the locally convex inductive-limit topology. Together with orbit continuity on a fixed support, this proves joint continuity. On \(C_0(E)\), use density and isometric translation. The unfinished corollary is not supplied.

For **P67-C007–C008**, a finite polygonal contour inside the given holomorphy neighbourhood yields the Banach-valued Cauchy measure; its orientation accounts for the source's \(1/(z-t)\) kernel. The exterior formula uses vanishing at infinity. Separated compact supports bound the double kernel and justify Bochner-Fubini. Factor \(f(z)-\lambda\) at a spectral preimage for spectral mapping; use the resolvent identity and two Cauchy kernels for composition. The K/L inconsistency and missing typescript continuation remain textual questions despite the valid reconstructed lemmas.
