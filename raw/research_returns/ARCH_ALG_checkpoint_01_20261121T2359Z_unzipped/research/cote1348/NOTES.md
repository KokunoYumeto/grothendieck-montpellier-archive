# Cote 134-8 research notes

## 2026-11-22 — route record

The inherited F-SM44 comparison is b_n: ⊕ L_n φ(X_s) → L_n φ(⊕ X_s), monic in every degree and invertible in degrees 0 and 1. A full tensor counterexample can be built by square-zero unitization of F-SM34 rather than trying to tensor F-SM34 itself.

### Routes considered before the construction

1. Shift with the interval exact sequence 0→X→J⊗X→Q⊗X→0. Even when interval tensor preserves coproducts, this shifts the comparison obstruction to a higher degree; it does not reduce it to b_1. No proof of surjectivity resulted.
2. Split the evaluated interval on coinduced modules. Bare tensor purity gives pure scalar monomorphisms, not scalar splittings; the inherited finite pure-injective dimension obstruction remains.
3. Try to tensor the F-SM34 category directly. F-SM36–38 already exclude straightforward componentwise and exact scalar approaches. The new construction embeds it as an ideal in a larger monoidal category with a different tensor unit.
4. Search for a contemporary theorem settling the full abstract setup. Hubert, arXiv:2602.09674v1, Theorem 5.14, concerns abelian presheaves on test categories with a strong Whitehead condition. It does not cover arbitrary non-AB4 categories in the sheet. This is literature context only, not a mathematical input.

### New construction to check

Let N and κ_N be F-SM34, over a field k. Let A have objects (V,X,h:κ_NV→X). Product tensor has first component V⊗W and second the pushout (V⊙Y) ⊔_{κ_N(V⊗W)} (W⊙X), where ⊙ is the canonical scalar copower in N. The common maps are obtained from h,g. Unit=(k,κ_Nk,id). The m-fold tensor has the colimit of m terms, one N component at a time, with all common scalar-unit images identified; this gives coherence.

φ_A(V,X,h)=φ_N(X), κ_A(U)=(U,κ_NU,id), ψ_A(V,X,h)=V. κ_A(U) is projective for every vector space. The embedding i(X)=(0,X,0) is exact, preserves coproducts, and carries N-projectives to A-projectives.

For M=Ch_{≥0}(A), the usual homological tensor has unit κ_A(k)[0] and interval D_1(unit). Its tensor is cone(id), hence degreewise monic from every X and fully derived-acyclic. All original hypotheses hold. For X_n=iκ_N(k)[0], b_2 is 0→E(k^{(N)})≠0. The map iκ_N(k)→κ_A(k) is a weak equivalence, but its countable coproduct is not. Nevertheless the ordinary localization is D_{≥0}(k), because Lφ_A has the exact right adjoint κ_A and the counit is an isomorphism on all scalar complexes.

No claim yet that the raw ordinary-G counit question is settled: this category has no compact-projective-generator claim, and the ringoid SM25.2 question is separate.

## Raw ordinary-G counit: subsequent routes and exact limits

5. **Finite scalar resolution through geometric completions — succeeds in a new explicit range.** Nakamura–Yoshino 2018, Theorem 9.2 and Remark 9.3, pp.432–433, provides a uniform length dim(k) exact sequence of pure-injectives for every flat or finitely generated module over commutative noetherian finite-dimensional k. Applying the inherited F-SM24 retraction argument and finite dimension shifting proves ARCH-134-04. Objectwise purity/scalar compatibility is retained explicitly. No scalar cardinality bound is used. This is a new application, not a new pure-dimension theorem.

6. **Infinite pure-injective coresolution — exact failure point.** For Z=∏C_x(Q), an infinite scalar coresolution yields 0→Z→I^0→I^1→… with all Lφ(I^r)=0. Successive short exact sequences give L_jφ(Z)≅L_{j+m}φ(Z_m), where Z_m is the m-th cosyzygy. The homological degree increases, so connectivity gives no vanishing. A finite uniform bound on the resolution length closes the argument; without it, no valid infinite-totalization convergence argument was obtained. Infinite resolution length alone is not evidence of a counit counterexample.

7. **Truncate the acyclic projective target by disks — product comparison remains.** Write P=∏_{n≥1}D_n(Q_n), with finite partial products P_{≤N}. Even if every finite GP_{≤N} is derived-acyclic, GP is their inverse limit. The left adjoint Λ need not commute with this product/inverse limit. The issue is exactly B_j⊗_R∏C_x(Q) versus ∏(B_j⊗_R C_x(Q)), not exactness of products themselves. Finite presentation of the relevant resolution terms is the inherited F-SM27 sufficient condition, and was not reintroduced as automatic.

8. **Use the known underlying localization and Brown's lemma — insufficient.** F-SM29 supplies a Quillen equivalence for an injective-type model structure, but the raw coinduced-projective targets need not be fibrant. Replacing G(C) by G(C^fib) gives the already known derived inverse and leaves the literal counit undecided. No inference from an invertible derived counit to an invertible unreplaced counit is made.

9. **Transfer the new tensor counterexample to a small ringoid — blocked.** ARCH-134-01 embeds F-SM34 as an ideal in a larger monoidal category. The surviving non-AB4 defect shows that this category is not an ordinary module category of a small ringoid. Replacing its projectives by a small tensor-closed subcategory and taking all presheaves changes coproducts and the scalar functor. Over a field every raw counit is already in BR-13404's positive range; no raw counterexample results. Outer chain categories over a locally scalar-projective ringoid are likewise already covered by F-SM39.

10. **Descent to a countable coefficient subring — does not preserve the test.** A Tor cycle uses finitely many tensor entries, but each coinduced entry is a scalar-linear map defined on an entire potentially huge morphism module. Its coordinate values may require unboundedly many scalar coefficients. Encoding these values as generators over a smaller ring generally destroys projectivity of the coefficient module or local scalar projectivity of the ringoid, and changing scalar adjoints changes normalization. Thus finite support in the tensor expression is not a valid countable-ring descent argument.

11. **Direct non-split pure interval counterexample — not constructed.** Pointwise purity does not imply scalar splitting (the supplied Z→∏Z_p example already witnesses the general error), so F-SM42 cannot be invoked. Conversely no actual symmetric tensor, canonical normalization, and full acyclic interval were constructed with a nonzero SM25.2 Tor class. General pure-dimension examples alone do not supply these predicates.

### Status at redirect

- Universal higher coproduct surjectivity: refuted by ARCH-134-02, parent full-proof check passed.
- Localization in that counterexample: proved by ARCH-134-03, parent check passed.
- Bare abstract Thm(?): remains open; higher coproduct compatibility is now known not to follow from the axioms, so a proof must bypass it.
- Raw G: ARCH-134-04 establishes the explicit noetherian finite-dimensional scalar range under the visible scalar-compatibility hypothesis; arbitrary scalar ring remains unresolved by the routes above.
