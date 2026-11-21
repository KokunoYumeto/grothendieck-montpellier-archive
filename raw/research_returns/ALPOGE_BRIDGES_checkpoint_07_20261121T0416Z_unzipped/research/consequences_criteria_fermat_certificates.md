# Geometric constructions that force the finite certificate search to terminate

**Scope and inputs.** Fix a finite field \(k=\mathbf F_q\) of characteristic \(p\). Call a smooth projective \(k\)-scheme **certified** if it satisfies the equivalent conditions of CC-XC06: there are rational algebraic correspondences giving its cohomological motive as a direct summand of a finite sum of Tate twists of abelian varieties and finite étale schemes. The same correspondences can be chosen to give the splitting for every \(\ell\ne p\), and also in the rational numerical category. Empty schemes and finite disjoint unions are allowed.

This section uses the abelian-sector fullness and numerical--homological comparison already isolated in AQ.15 and CC-AG01, and the proved rational certificate theorem CC-XC05--07. It does not assume the Tate conjecture for an arbitrary variety. The geometric input for Fermat varieties is the classical construction of Shioda and Katsura (1979, Lemmas 1.1--1.3, pp. 98--100; Lemma 2.1, p. 103). The statements below are applications and complete deductions from these inputs, with no novelty claim. Literature cutoff: 20 November 2026; checks: 21 November 2026 UTC.

## CC-XC08 — Closure operations, including descent of membership

The following assertions hold.

1. Abelian varieties, finite étale schemes, and smooth projective curves are certified. Finite products and finite disjoint unions of certified schemes are certified.
2. If \(f:Y\to X\) is a proper, dominant, generically finite morphism between smooth projective geometrically integral schemes, and \(Y\) is certified, then \(X\) is certified. Separability is not needed for this assertion.
3. If \(P\) is smooth projective and \(Z\hookrightarrow P\) is a smooth closed subscheme of pure codimension two, then certification of \(P\) and \(Z\) implies certification of \(\operatorname{Bl}_ZP\).
4. For every finite extension \(k'/k\), a smooth projective \(X/k\) is certified if and only if \(X_{k'}\) is certified over \(k'\).

Assertion 4 concerns membership in the whole abelian--Artin category with a freely chosen target. It does not say that every specified rational object over \(k'\), or over \(\bar k\), descends to a specified object over \(k\). The orbit and Schur-index obstructions in CC-AG09--13 remain applicable to that different descent problem.

**Complete proof.**

**Finite sums and products.** For one auxiliary prime \(\ell\ne p\), write \(\mathcal H_{\ell,E}(k)\) for the homological category used in CC-XC01, with \(E=\overline{\mathbf Q}_\ell\). CC-XC06 identifies certification with membership in its fully embedded abelian--Artin subcategory \(\mathcal A_{q,E}\). This subcategory is closed under finite sums, tensor products, Tate twists, duals and direct summands. Künneth identifies a product with the tensor product, so products and disjoint unions preserve membership and hence certification. Abelian varieties and finite étale schemes are generators.

This use of tensor closure matters: a product of an abelian variety and a nontrivial finite étale scheme need not itself be an abelian variety. Membership in the tensor category followed by CC-XC06 supplies the permitted finite certificate target.

**Generically finite images.** Put \(\delta=[k(Y):k(X)]>0\). Pullback and proper pushforward are algebraic correspondences and satisfy

\[
 f_*f^*(a)=f_*(1)\smile a=\delta a
 \qquad(a\in H^*(X_{\bar k},E)).
 \tag{CC-XC.11}
\]

Indeed, \(f_*[Y]=\delta[X]\), and the displayed equality is the projection formula. Thus \(f^*\) and \(\delta^{-1}f_*\) split \(h_{\ell,E}(X)\) off \(h_{\ell,E}(Y)\). Since \(\mathcal A_{q,E}\) is closed under summands, \(X\) belongs to it. Apply CC-XC06. The identity depends on the full degree, including an inseparable degree if present; division by this positive integer is allowed with rational coefficients. This proves the required trace splitting directly from cycle pushforward and the projection formula.

**Codimension-two blowups.** Write

\[
 B=\operatorname{Bl}_ZP,\quad
 \beta:B\to P,\quad
 j:E_Z\hookrightarrow B,\quad
 \rho:E_Z=\mathbf P(N_{Z/P})\to Z.
\]

Here \(\mathbf P(N_{Z/P})\) parametrizes normal lines. Use \(\xi=c_1(\mathcal O_{E_Z}(1))\); the normal line of \(E_Z\) in \(B\) is \(\mathcal O_{E_Z}(-1)\). Consider the algebraic cohomological maps

\[
 \begin{aligned}
 \Phi:\ H^i(P)\oplus H^{i-2}(Z)(-1)&\longrightarrow H^i(B),
 &\Phi(u,v)&=\beta^*u+j_*\rho^*v,\\
 \Psi:\ H^i(B)&\longrightarrow H^i(P)\oplus H^{i-2}(Z)(-1),
 &\Psi(w)&=(\beta_*w,-\rho_*j^*w).
 \end{aligned}
 \tag{CC-XC.12}
\]

Every map here is induced by a graph, its transpose, or their composition. The twists in the second summand are the usual étale Tate twists.

We check \(\Psi\Phi=1\). First, \(\beta_*\beta^*=1\) by (CC-XC.11) with degree one. Next, \(\rho_*\rho^*=0\): the fibres of \(\rho\) have dimension one, so \(\rho_*1\in H^{-2}(Z)(-1)=0\), and the projection formula applies. If \(i_Z:Z\hookrightarrow P\), then \(\beta j=i_Z\rho\). It follows that

\[
 \beta_*j_*\rho^*=(i_Z)_*\rho_*\rho^*=0,\qquad
 \rho_*j^*\beta^*=\rho_*\rho^*i_Z^*=0.
\]

Finally, self-intersection of the divisor \(E_Z\) gives \(j^*j_*v=-\xi\smile v\), while integration over the projective-line fibres gives \(\rho_*(\xi\smile\rho^*v)=v\). Thus the lower-right entry of \(\Psi\Phi\) is also the identity, with the minus sign in \(\Psi\) cancelling the normal-bundle sign.

The blowup cohomology formula, Shioda--Katsura, Lemma 2.1, p. 103, equation (2.1), gives

\[
 \dim H^i(B)=\dim H^i(P)+\dim H^{i-2}(Z).
\]

Consequently the left inverse just verified is the inverse, in every degree. This proves the algebraic isomorphism

\[
 h_{\ell,E}(B)\simeq h_{\ell,E}(P)\oplus h_{\ell,E}(Z)(-1).
 \tag{CC-XC.13}
\]

It is Frobenius-equivariant because all the maps are defined over \(k\). Hence \(B\) is certified whenever \(P\) and \(Z\) are. Shioda--Katsura write their positive twist as tensoring with \(H^2(\mathbf P^1)\); their twist \((1)\) in this formula is therefore our \((-1)\). Disconnected smooth centres cause no change: both their cohomology and the formulas split by components.

**Finite-field descent.** The forward implication in assertion 4 follows by base change of the rational splitting cycles. For the converse, suppose \(X_{k'}\) is certified and put \(e=[k':k]\). By CC-XC06 it has a splitting into a finite sum

\[
 T'=\bigoplus_\nu h(Y_\nu)(n_\nu),
 \tag{CC-XC.14}
\]

with rational splitting correspondences, where each \(Y_\nu\) is an abelian variety or a finite étale scheme over \(k'\).

There is an additive induction operation on these homological correspondences: regard a smooth projective \(k'\)-scheme as a \(k\)-scheme, and extend a correspondence on \(U\times_{k'}V\) by zero along the open-and-closed immersion into \(U\times_kV\). It preserves identities and composition. To verify this directly, extend scalars to \(\bar k\). The resulting schemes are disjoint unions indexed by the embeddings \(k'\hookrightarrow\bar k\). An induced correspondence is block diagonal, with its conjugate in each matching block. Composition and identities are therefore block diagonal with exactly the asserted entries. This also proves that a zero cohomological action remains zero after induction. Thus the given splitting of \(X_{k'}\) induces a splitting of its underlying \(k\)-scheme into the induced summands of (CC-XC.14).

If \(Y_\nu\) is finite étale over \(k'\), its underlying \(k\)-scheme is finite étale. If \(Y_\nu=A\) is an abelian variety over \(k'\), let

\[
 B=\operatorname{Res}_{k'/k}A.
\]

Because the extension is finite separable, \(B\) is an abelian variety over \(k\), and

\[
 B_{k'}\simeq
 \prod_{\sigma\in\operatorname{Gal}(k'/k)} A^\sigma .
 \tag{CC-XC.15}
\]

These are the exact restriction-of-scalars properties recalled and justified by Milne (1972, §1, pp. 177--178). Projection onto the identity factor, and insertion into that factor with zero in all other factors, are \(k'\)-morphisms whose composite on \(A\) is the identity. Their graph correspondences show, after viewing the schemes over \(k\), that

\[
 h(A\text{ viewed over }k)
 \quad\text{is a summand of}\quad
 h(B_{k'}\text{ viewed over }k)
 =h(B)\otimes h(\operatorname{Spec}k').
 \tag{CC-XC.16}
\]

The object on the right is explicitly abelian **times Artin**. It belongs to the tensor-closed category \(\mathcal A_{q,E}\); we have not identified it with the motive of a single abelian variety. Tate twists preserve this conclusion. Therefore induction of every summand in (CC-XC.14), and then the underlying \(k\)-scheme of \(X_{k'}\), belong to \(\mathcal A_{q,E}\).

Finally the finite étale projection

\[
 \tau:X_{k'}\text{ viewed over }k\longrightarrow X
\]

has degree \(e\), and \(\tau_*\tau^*=e\,1\). Pullback and \(e^{-1}\) times trace split off \(h(X)\). Hence \(h_{\ell,E}(X)\) is in the abelian--Artin category, and CC-XC06 supplies a rational certificate with its specified allowed target over \(k\). This argument descends membership, without asserting descent of any prescribed simple summand.

**Curves.** By this finite-extension assertion, it suffices first to treat a smooth projective geometrically connected curve \(C/k\) with a rational point \(P\): every such curve acquires a point over a finite extension. Put \(g=\dim J(C)\). The point supplies algebraic projectors onto \(H^0(C)\) and \(H^2(C)\), whose motives are \(\mathbf Q\) and \(\mathbf Q(-1)\). If \(g=0\), these exhaust the cohomology, and the assertion follows directly.

For \(g>0\), the Abel--Jacobi map \(a:C\to J=J(C)\) induces an isomorphism

\[
 a^*:H^1(J_{\bar k},E)\xrightarrow{\sim}H^1(C_{\bar k},E).
 \tag{CC-XC.17}
\]

Milne (1986, Proposition 9.1, p. 195) states the stronger abelianized fundamental-group isomorphism over a separably closed field; the prime-to-\(p\) part needed here is proved on p. 196 using Lemmas 9.2--9.3. Apply it after base change to \(\bar k\). Because \(a\) is defined over \(k\), (CC-XC.17) is Frobenius-equivariant.

By Poincaré duality, its transpose is the algebraic pushforward isomorphism

\[
 a_*:H^1(C_{\bar k},E)
       \xrightarrow{\sim}H^{2g-1}(J_{\bar k},E)(g-1).
 \tag{CC-XC.18}
\]

Use the algebraic degree projectors on \(J\) from Katz--Messing, Theorem 2, or CC-XC05. Together with the point projectors, the graph of \(a\) therefore gives a morphism

\[
 h_{\ell,E}(C)\longrightarrow
 \mathbf Q\ \oplus\
 h^{2g-1}_{\ell,E}(J)(g-1)\
 \oplus\ \mathbf Q(-1)
 \tag{CC-XC.19}
\]

whose realization is an isomorphism. The target belongs to \(\mathcal A_{q,E}\). The algebraic-inverse construction in the proof of CC-XC02 applies to this target as well: transfer the Poincaré duality pairing to the target, lift that pairing using fullness inside the abelian sector, and transpose the given map. It produces the inverse without assuming Tate surjectivity for \(C\times J\). Thus \(C\) is certified by CC-XC06.

For an arbitrary smooth projective curve, a finite extension separates its finitely many geometric connected components and gives each a point. The proved finite-union and finite-extension assertions then apply. This completes all four assertions. \(\square\)

## CC-XC09 — Fermat and diagonal hypersurfaces in every dimension

Let \(m\ge2\), let \(p\nmid m\), and for \(r\ge0\) let

\[
 F_m^r:\quad x_0^m+\cdots+x_{r+1}^m=0
       \ \subset\ \mathbf P_k^{\,r+1}.
 \tag{CC-XC.20}
\]

Then \(F_m^r\) is certified. More generally, every diagonal hypersurface

\[
 D:\quad a_0x_0^m+\cdots+a_{r+1}x_{r+1}^m=0,
 \qquad a_i\in k^\times,
 \tag{CC-XC.21}
\]

is certified.

Consequently CC-XC07's finite search terminates for each of these explicit inputs. It returns rational algebraic splitting correspondences valid for every \(\ell\ne p\), and an actual object of the rational numerical abelian--Artin category isomorphic to its numerical motive. The Frobenius semisimplicity, Tate surjectivity, and numerical--homological consequences of CC-XC06 apply to their products, products with abelian varieties and finite étale schemes, and finite extensions of the base field.

**Complete proof.** The partial derivatives of the equations in (CC-XC.20)--(CC-XC.21) are nonzero scalar multiples of \(x_i^{m-1}\). They cannot vanish simultaneously at a projective point, so these hypersurfaces are smooth. In dimension zero they are finite étale. For \(r\ge1\), the Fermat hypersurface is geometrically integral: two distinct positive-degree hypersurface components in projective space of dimension at least two would meet, and their intersection would be singular in their union; a repeated component is likewise incompatible with smoothness.

Choose a finite extension \(k'/k\) containing an element \(\epsilon\) with \(\epsilon^m=-1\). This is possible because the polynomial has roots in the algebraic closure, each in a finite field. It is enough to prove certification over \(k'\), by CC-XC08(4). In characteristic two, \(-1=1\) and \(\epsilon=1\) is already available; no primitive \(2m\)-th root of unity is required.

Shioda--Katsura's construction can be used over this \(k'\). For positive integers \(u,v\), its rational map is

\[
 \begin{split}
 F_m^u\times F_m^v&\dashrightarrow F_m^{u+v},\\
 (x,y)&\longmapsto
 (x_0y_{v+1}:\cdots:x_uy_{v+1}:
   \epsilon x_{u+1}y_0:\cdots:\epsilon x_{u+1}y_v).
 \end{split}
 \tag{CC-XC.22}
\]

The displayed coordinates satisfy the Fermat equation: the first group of \(m\)-th powers sums to \(-x_{u+1}^m y_{v+1}^m\), and the second to \(+x_{u+1}^m y_{v+1}^m\). Its base scheme is

\[
 Z=F_m^{u-1}\times F_m^{v-1},
 \qquad x_{u+1}=y_{v+1}=0,
\]

a smooth codimension-two centre in \(F_m^u\times F_m^v\). Shioda--Katsura, Lemma 1.1, p. 98, proves that the map has degree \(m\); Lemma 1.2, p. 99, proves that the blowup of this centre resolves the map:

\[
 \psi:\operatorname{Bl}_{Z}(F_m^u\times F_m^v)
       \longrightarrow F_m^{u+v}.
 \tag{CC-XC.23}
\]

Lemma 1.3, p. 100, moreover gives a finite étale degree-\(m\) map on the specified dense open. Only its dominance and degree are needed here. These lemmas hold in arbitrary characteristic with \(p\nmid m\); all the displayed formulas, the centre, the blowup and the resolved morphism are defined over \(k'\).

Proceed by induction on \(r\). The case \(r=0\) is finite étale, and \(r=1\) is a smooth projective curve, so CC-XC08 applies. For \(r\ge2\), use \(u=r-1\) and \(v=1\). The source product

\[
 P=F_m^{r-1}\times F_m^1
 \quad\text{and its centre}\quad
 Z=F_m^{r-2}\times F_m^0
\]

are certified by induction and product closure. Hence their codimension-two blowup is certified. Its degree-\(m\) morphism (CC-XC.23) makes \(F_m^r\) a cohomological summand, by the explicit pullback/trace splitting (CC-XC.11). Thus \(F_m^r\) is certified over \(k'\), and finite-field descent proves the statement over \(k\).

For (CC-XC.21), choose a finite extension containing \(c_i\) with \(c_i^m=a_i\). The change of coordinates \(y_i=c_i x_i\) identifies \(D\) over this extension with \(F_m^r\). Finite-field descent again applies. This proves the theorem.

The assertions about search termination and simultaneous rational splitting are precisely CC-XC06--07 applied to the membership just proved. Products and further finite extensions remain certified by CC-XC08, so the corresponding consequences of CC-XC06 apply there too. No Chow-projector lifting or arbitrary-variety Tate assertion is being added. \(\square\)

**Exact status improvement.** For a specified smooth diagonal hypersurface with \(p\nmid m\), the existential cross-cycle gate in CC-XC02 has been discharged by the stated geometric construction and the existing abelian-sector inputs. The certificate search is therefore guaranteed to halt on this family. Its runtime and the degrees of the first certificate are not bounded here. The argument does not extend to a general smooth hypersurface merely from equality of dimension, degree, or zeta function.

## Primary source scope and bibliography

Shioda--Katsura work over an algebraically closed field in the cohomological discussion. Their defining formulas and the resolution in Lemmas 1.1--1.2 descend to a finite field containing \(\epsilon\), and their cohomological lemma is applied after geometric base change; the graph maps in this proof retain their finite-field Frobenius actions. Remark 1.8, p. 102, imposes a primitive \(2m\)-th root for the larger quotient diagram. We use only the map and blowup lemmas, and have not imposed that stronger condition in characteristic two.

Fu--Vial (2020, §5.3) discuss Fermat varieties of abelian type, but that section explicitly assumes the complex base field. It is not the source for the finite-field assertion proved here. The characteristic-independent geometric input used here is Shioda--Katsura.

- Katz, N. M., & Messing, W. (1974). Some consequences of the Riemann hypothesis for varieties over finite fields. *Inventiones Mathematicae, 23*, 73--77. https://doi.org/10.1007/BF01405203 . Exact locator: Theorem 2, p. 76. Author scan: https://web.math.princeton.edu/~nmk/old/katzmessing.pdf .
- Milne, J. S. (1972). On the arithmetic of abelian varieties. *Inventiones Mathematicae, 17*, 177--190. Exact locator: §1, pp. 177--178, restriction-of-scalars definition, existence, separable product decomposition and abelian-variety conclusion. https://www.jmilne.org/math/articles/1972a.pdf .
- Milne, J. S. (1986). Jacobian varieties. In G. Cornell & J. H. Silverman (Eds.), *Arithmetic geometry* (pp. 167--212). Springer. Exact locators: Proposition 9.1, p. 195; prime-to-characteristic part of the proof and Lemmas 9.2--9.3, p. 196. https://www.jmilne.org/math/articles/1986c.pdf . Author's errata page: https://www.jmilne.org/math/articles/1986c.html ; its listed corrections do not alter the cited statement.
- Shioda, T., & Katsura, T. (1979). On Fermat varieties. *Tohoku Mathematical Journal, Second Series, 31*(1), 97--115. https://doi.org/10.2748/tmj/1178229881 . Exact locators: Lemma 1.1, p. 98; Lemma 1.2, p. 99; Lemma 1.3, p. 100; Lemma 2.1 and equation (2.1), p. 103. Primary scan: https://www.jstage.jst.go.jp/article/tmj1949/31/1/31_1_97/_pdf .
- Fu, L., & Vial, C. (2020). Distinguished cycles on varieties with motive of abelian type and the section property. *Journal of Algebraic Geometry, 29*, 53--107. Used only for the literature-scope comparison, not as a finite-field theorem: conventions, p. 60, and §5.3, p. 92. Author manuscript: https://irma.math.unistra.fr/~lfu/articles/DistinguishedCycles.pdf .
