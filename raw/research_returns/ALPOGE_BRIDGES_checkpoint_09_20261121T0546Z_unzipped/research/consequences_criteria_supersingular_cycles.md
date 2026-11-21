# Geometrically Tate Chow motives and supersingular K3 cycle certificates

**Scope.** The geometric input below is an established theorem about actual rational Chow motives. The finite-field deductions retain the Galois action through Artin motives. They require neither a general Tate conjecture nor the added all-abelian Tate input used elsewhere in the programme.

## CC-XC20 — Descent of a geometric Tate decomposition

Let \(X/\mathbf F_q\) be smooth projective of pure dimension \(d\), and suppose that in rational Chow motives

\[
 h(X_{\bar{\mathbf F}_q})
       \simeq\bigoplus_{i=0}^{d}\mathbf 1(-i)^{b_{2i}}.
\tag{CC-XC.T1}
\]

Then there are rational Artin motives \(A_i\), factoring through one finite cyclic Galois group, such that

\[
                  h(X)\simeq\bigoplus_{i=0}^{d} A_i(-i).
\tag{CC-XC.T2}
\]

Their finite-image rational Galois representations are
\(\mathrm{CH}^i(X_{\bar{\mathbf F}_q})_{\mathbf Q}\); their dimensions are \(b_{2i}\). For every \(\ell\ne p\), the realization of \(A_i\) is \(H^{2i}(X_{\bar{\mathbf F}_q},\mathbf Q_\ell(i))\), and all odd cohomology vanishes. The finite-order Frobenius representations determine the \(A_i\) up to rational Artin-motive isomorphism.

Every finite product of varieties satisfying (CC-XC.T1), over every finite extension of \(\mathbf F_q\), has the following properties:

1. Its rational Chow motive is Artin--Tate and hence belongs to the abelian--Artin category of CC-XC16.
2. Rational, \(\ell\)-adic homological and numerical equivalence agree in every codimension.
3. The rational cycle-class map, after tensoring with \(\mathbf Q_\ell\), is an isomorphism onto the Frobenius-invariant part of the corresponding Tate-twisted even cohomology.
4. The fixed-target forward-cycle search in CC-XC15 terminates.

**Complete proof.** Choose an isomorphism in (CC-XC.T1) and its inverse. A cycle is a finite sum of integral subschemes, and a rational-equivalence relation has finitely many subvarieties and rational functions as witnesses. Thus both correspondences and the two identities between their compositions descend to one finite extension \(k'=\mathbf F_{q^m}\). We obtain an actual Chow isomorphism

\[
                     h(X_{k'})\simeq
                         \bigoplus_i\mathbf1_{k'}(-i)^{b_{2i}}.
\tag{CC-XC.T3}
\]

Use the induction of Chow correspondences proved in CC-XC16: regard a \(k'\)-scheme as a \(k\)-scheme, and extend a correspondence by zero from the open-and-closed component defined by the \(k'\)-fibre product. Its composition law is block diagonal after a separable splitting extension, and rational restriction--corestriction makes this an identity over \(k\). Applying induction to (CC-XC.T3) gives

\[
 h(X_{k'}\text{ as a }k\text{-scheme})
      \simeq\bigoplus_i h(\operatorname{Spec}k')(-i)^{b_{2i}}.
\tag{CC-XC.T4}
\]

The projection \(\tau:X_{k'}\to X\) satisfies
\(\tau_*\tau^*=m\,\mathrm{id}\) as a Chow correspondence. Dividing the transfer by \(m\) exhibits \(h(X)\) as a direct summand of the right-hand side of (CC-XC.T4). No numerical or homological replacement of the Chow identity is used.

For finite étale \(k\)-schemes \(U,V\), the groups of Chow correspondences between \(h(U)(-i)\) and \(h(V)(-j)\) vanish when \(i\ne j\), since the product has dimension zero and has nonzero Chow groups only in codimension zero. Consequently the idempotent cutting out \(h(X)\) is block diagonal in the twist index \(i\), and its \(i\)-th block defines the Artin motive \(A_i\). This proves (CC-XC.T2).

For completeness, the category of rational Artin motives split by \(k'\) identifies with finite-dimensional rational representations of the cyclic group \(G=\operatorname{Gal}(k'/k)\). The motive of a finite étale scheme gives its permutation representation. Correspondences are rational matrices constant on \(G\)-orbits of pairs of geometric points, exactly the equivariant maps between these permutation representations. Taking direct sums and idempotent images gives all finite-dimensional representations: every such representation is a summand of a finite sum of regular representations by Maschke's averaging argument. This also proves faithfulness of the Artin realization. Finite-order rational operators are semisimple, and their cyclotomic characteristic-polynomial multiplicities determine their rational representations.

Over \(\bar k\), maps from a Tate summand to a different Tate summand vanish, and its degree-\(2i\) cycle class is an isomorphism. Applying this to (CC-XC.T1) proves

\[
 \mathrm{CH}^i(X_{\bar k})_{\mathbf Q}\otimes\mathbf Q_\ell
       \simeq H^{2i}(X_{\bar k},\mathbf Q_\ell(i)).
\tag{CC-XC.T5}
\]

The identification is Galois equivariant, so it identifies \(A_i\) as asserted. In particular its action has finite image: a basis of the finite-dimensional rational Chow group is defined over a common finite extension.

The condition (CC-XC.T1) is preserved by products and finite extensions. It remains to justify the cycle assertions for any one such product \(Y/k\). Rational restriction to \(\bar k\) is injective. Indeed, an equality of cycles modulo rational equivalence over \(\bar k\) descends to a finite extension, where restriction followed by corestriction is multiplication by its degree.

Moreover,

\[
 \mathrm{CH}^j(Y)_{\mathbf Q}
    =\mathrm{CH}^j(Y_{\bar k})_{\mathbf Q}^{\operatorname{Gal}(\bar k/k)}.
\tag{CC-XC.T6}
\]

To check surjectivity, represent an invariant geometric class over a finite Galois extension \(k''/k\). Its invariance holds already in \(\mathrm{CH}^j(Y_{k''})_{\mathbf Q}\), by the injectivity just proved. The corestriction divided by \([k'':k]\) restricts to that class. The actions on the finite-dimensional geometric Chow groups factor through a finite group, so taking invariants commutes with extension of scalars to \(\mathbf Q_\ell\). Formula (CC-XC.T5), applied to \(Y\), now proves the asserted cycle-class isomorphism onto invariants.

The intersection pairing on the geometric rational Chow groups in complementary codimensions is perfect: (CC-XC.T5) identifies its scalar extension with Poincaré duality, and its matrix has rational entries. It remains perfect on invariants. In fact, if a nonzero invariant vector pairs nontrivially with some vector, averaging the latter over the finite acting group preserves that nonzero pairing and produces an invariant vector. By (CC-XC.T6), this is the numerical pairing over \(k\). Its kernel is zero, proving rational equals numerical; the usual rational--homological--numerical implications then give the middle equality as well.

Finally Artin--Tate motives are contained in the abelian--Artin category, and all the isomorphisms used above are given by rational cycles. Thus the forward-cycle existence condition of CC-XC15 is satisfied for \(Y\), and that search terminates. No a priori bound for its termination time is asserted. \(\square\)

## CC-XC21 — Supersingular K3 surfaces, their Hilbert schemes and residual projectors

Let \(S/\mathbf F_q\) be a smooth projective geometrically connected K3 surface which is geometrically supersingular. One can use the definition
\(\rho(S_{\bar{\mathbf F}_q})=22\); equivalence with the formal-Brauer or slope-one definition is the established supersingular Tate theorem, recorded in Fu--Li (2021, pp. 148 and 169).

The published motivic input is Fu--Li (2021, Theorem 1.3(iii), pp. 152--153; proof in §4.5, p. 179). It implies

\[
 h(S_{\bar k})\simeq
       \mathbf1\oplus\mathbf1(-1)^{22}\oplus\mathbf1(-2).
\tag{CC-XC.T7}
\]

The same theorem gives a Tate Chow motive for a moduli space \(M_H(S_{\bar k},v)\), where \(v=(r,c,s)\) is a **primitive** Mukai vector, \(r>0\), \(v^2\ge0\), \(H\) is general for \(v\), and
\[
             p\nmid r\quad\text{or}\quad
             p\nmid s\quad\text{or}\quad
             p\nmid(c\cdot\mathrm{NS}(S_{\bar k})).
\tag{CC-XC.T8}
\]
Here “general” means that every semistable sheaf in question is stable; the last expression means that at least one intersection \(c\cdot D\) is not divisible by \(p\). These are the source's Definitions 4.3 and 4.7, pp. 171 and 173. We include primitivity explicitly from its standing moduli-space convention. A finite-field form of such a smooth projective moduli space is allowed.

In particular, for every \(n\ge1\), the Hilbert scheme \(S^{[n]}\) has geometric Tate Chow motive. Indeed it is the rank-one ideal-sheaf case \(v=(1,0,1-n)\): this vector is primitive, satisfies (CC-XC.T8), has \(v^2=2n-2\), and its rank-one ideal sheaves are stable for every ample polarization. This agrees with the Hilbert-scheme step of the published proof, p. 179.

**Complete finite-field deduction.** Apply CC-XC20 to each of these varieties. Thus their actual rational Chow motives over \(\mathbf F_q\) are Artin--Tate, all of their finite products satisfy the cycle comparisons and Tate-surjectivity statements of CC-XC20, and their fixed-target forward-cycle searches terminate. This applies in every positive characteristic; no assumption of unirationality is made.

For \(S\) itself, the degree-zero and top-degree Artin factors are trivial by geometric connectedness and the degree map. The middle factor is exactly the rational Néron--Severi representation. If \(A_{\mathrm{NS}}\) denotes its rational Artin motive, then

\[
                h(S)\simeq
                  \mathbf1\oplus A_{\mathrm{NS}}(-1)
                              \oplus\mathbf1(-2).
\tag{CC-XC.T9}
\]

After a finite extension defining all divisor classes, this becomes the Tate decomposition (CC-XC.T7) over that finite field. This conclusion is a Chow-motive isomorphism, not merely equality of characteristic polynomials.

For the even-dimensional quadric fibration over a surface in CC-XC18, suppose that its supplied residual surface \(Z\) is a supersingular K3 surface, or that its specified projector summand \((Z,e)\) is known by Chow correspondences to be a summand of a finite sum of twisted motives of the varieties just considered. Then \((Z,e)\) is Artin--Tate. The residual-projector gate in CC-XC18 is discharged, and the total space has Chow abelian--Artin membership exactly when its base does; the analogous statement holds for homological certification. If the base is itself geometrically Tate, then the total space is Artin--Tate and the stronger all-products assertions of CC-XC20 apply to it. This conditional identification of a residual projector does not assert that the auxiliary surface of every even-dimensional quadric fibration is K3. \(\square\)

## Primary-source scope and dependency record

The K3 input is a theorem about rational Chow motives, not just the algebraicity of \(H^2\). The proof in Fu--Li, §4.5, uses twisted derived equivalences to reduce Artin invariant and therefore does not rely on general supersingular unirationality. The corresponding current Bragg--Lieblich locator is Proposition 5.2.5, p. 95, in arXiv:1804.07282v6 (9 February 2019), in its \(p\ge3\) range. Fu--Li's printed proof uses an older locator “Proposition 5.15”; we do not copy that locator as a reference to v6. The characteristic-two case is the separate known unirational case discussed on their p. 148. Fu--Vial (2021, Theorem 1, p. 3) supplies actual rational Chow isomorphisms for twisted-derived-equivalent K3 surfaces over an arbitrary field. These are inspected published or preprint inputs; their full foundational proofs are not claimed to have been reconstructed here.

No conclusion is drawn for a general finite-height K3 surface from its Tate theorem for divisors or from a theorem about its self-product alone. No unirationality conclusion for Artin invariant ten is asserted. The new finite-field deductions above use the precise geometric Chow input that is stated.

## Primary bibliography

- Fu, L., & Li, Z. (2021). Supersingular irreducible symplectic varieties. In G. Farkas, G. van der Geer, M. Shen, & L. Taelman (Eds.), *Rationality of varieties* (Progress in Mathematics, Vol. 342, pp. 147--200). Birkhäuser. https://doi.org/10.1007/978-3-030-75421-1_7 . Author-hosted published PDF: https://irma.math.unistra.fr/~lfu/articles/Supersingular%20ISV.pdf . Exact locators: Theorem 1.3(iii), pp. 152--153; Definitions 4.3 and 4.7, pp. 171 and 173; §4.5, full concluding proof, p. 179; supersingularity conventions, pp. 148 and 169.
- Fu, L., & Vial, C. (2021). A motivic global Torelli theorem for isogenous K3 surfaces. *Advances in Mathematics, 383*, 107674. https://doi.org/10.1016/j.aim.2021.107674 . Published PDF: https://irma.math.unistra.fr/~lfu/articles/DerivedEqK3.pdf . Exact locator: Theorem 1, p. 3, over any field.
- Bragg, D., & Lieblich, M. (2019). *Twistor spaces for supersingular K3 surfaces* (arXiv:1804.07282v6). https://arxiv.org/abs/1804.07282v6 . Exact locator: Proposition 5.2.5, p. 95; standing \(p\ge3\) range in §1.1 and §3. This is the 9 February 2019 version, whose notice removes the earlier material claiming general unirationality.
- Vial, C. (2017). Remarks on motives of abelian type. *Tohoku Mathematical Journal, Second Series, 69*(2), 195--220. https://doi.org/10.2748/tmj/1498269623 . Lemma 1.2, p. 200, and the finite-field induction proof of CC-XC16 justify the rational Chow descent used above.
