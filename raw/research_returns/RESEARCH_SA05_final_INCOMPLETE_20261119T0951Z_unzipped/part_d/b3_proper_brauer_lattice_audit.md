# Independent audit: the proper singular-base Brauer lattice

**Date:** 19 November 2026. **Source route proposed by:** Part B. **Independent auditor:** Part D. This is a new refinement after checkpoint 04, conditional on the same surface-Tate assertion already isolated in B3.

## Statement and verdict

Assume divisor Tate for every smooth projective surface over finite extensions of F_p, and fix ℓ≠p. For every proper finite-type F_p-scheme S,

    H²_et(S,G_m) ⊗ Z_(ℓ)

is a finitely generated Z_(ℓ)-module. The proof passes. In particular its torsion is finite. This supplies the missing bound on saturation of the relative Picard-obstruction image for smooth proper curves over proper singular bases. The remaining base-image issue is confined to nonproper singular bases; this note does not claim the same full-H² finite generation there.

## 1. Perfection and the low-degree topology comparison

Let S_perf be the perfection. Étale topoi are invariant under universal homeomorphisms. Under this identification the transition on G_m induced by Frobenius is multiplication by p. Cohomology on the quasi-compact quasi-separated étale site commutes with the filtered colimit in each fixed degree. Therefore

    H^i_et(S_perf,G_m) = H^i_et(S,G_m)[1/p].

For the change of topology ε from the h-site (or v-site) of perfect schemes to the étale site, Bhatt–Scholze's vector-bundle descent theorem gives

    ε_*G_m = G_m,       R¹ε_*G_m = 0.

The first equality is descent for automorphisms of the trivial line. The second follows because every G_m-torsor for the finer topology is an actual line bundle by effective descent, and a line bundle becomes trivial on a Zariski cover. Equivalently, the presheaf U↦H¹_h(U,G_m)=Pic(U) has zero étale sheafification. No descent theorem for G_m-gerbes is asserted.

The low-degree Leray sequence consequently gives an injection

    H²_et(S_perf,G_m) ↪ H²_h(S_perf,G_m).

This is all that is needed. A quasi-isomorphism RΓ_et(G_m)≃RΓ_h(G_m) in arbitrary degree is neither claimed nor used.

## 2. The proper Čech kernel is a finite lattice

Choose a proper surjection q:T→S with T a finite disjoint union of smooth projective schemes, using a projective alteration of each reduced irreducible component. Let T_a be its Čech nerve. Perfection preserves the finite fibre products, and q_perf is an h-cover.

The descent spectral sequence is

    E₁^{a,b}=H^b_h((T_a)_perf,G_m) ⇒ H^{a+b}_h(S_perf,G_m).

The kernel K of restriction in degree two to T_perf has a two-step filtration whose graded pieces are E∞^{2,0} and E∞^{1,1}. They are subquotients of, respectively,

    Γ(T_2,O^*)[1/p],       Pic(T_1)[1/p].

Jaffe's Proposition 10.8 and Theorem 10.11 show these groups are finitely generated over Z[1/p], even when a Čech term is singular or nonreduced. Thus K⊗Z_(ℓ) is finitely generated. The argument uses actual h-cohomological descent only after the topology change; it does not apply proper base change directly to G_m on the original étale site.

## 3. The regular proper alteration has finite target

Each component of T is regular, so H²_et(T,G_m) is torsion. Under surface Tate, the previously proved all-smooth divisor-Tate reduction and Kummer argument give finite Br′(T)[ℓ∞]. Hence

    H²_et(T_perf,G_m) ⊗ Z_(ℓ)

is finite. In the commutative restriction square from étale to h-cohomology, both vertical maps are injective by §1. Therefore the kernel of the localized étale restriction map on S is a submodule of the finitely generated localized K, and its image lies in the finite localized étale target on T. This proves finite generation of the full localized H²_et(S,G_m).

No assertion about the entire H²_h(T_perf,G_m) is required: only the image of the known étale group on T occurs in the diagram.

## 4. The Brauer consequence and the nonproper limitation

For a relative curve, let D be the image of Pic_{X/S}(S) in full H²(S,G_m). The localized group H²(S,G_m)⊗Z_(ℓ) is noetherian. Its quotient by the localized D is finitely generated, so its ℓ-primary torsion is finite. The extra torsion obtained from a non-torsion base lift is therefore finite. Combined with the separate integral H¹(J) lattice and Picard-degree argument, this removes the singular proper-base obstruction in the relative Brauer quotient.

For a nonproper S, a regular proper alteration T→S is generally not proper over the finite field. Its ℓ-primary Brauer group can be divisible even under surface Tate; already a smooth open curve can exhibit this phenomenon. An extension of Q_ℓ/Z_ℓ by a finite-rank lattice can have an infinitely divisible saturation (the model Z⊂Z[1/ℓ] suffices). Thus the final finite-target step cannot be copied to nonproper S. No claim of a nonproper counterexample is made.

## Exact primary-source audit

- Bhatt, B., & Scholze, P. *Projectivity of the Witt vector affine Grassmannian*. Author PDF <https://people.mpim-bonn.mpg.de/scholze/Witt.pdf>. Independently read Theorem 1.2; Theorem 4.1(ii), Proposition 4.5, complete Lemma 4.6 and the n=1 proof of Theorem 4.1, author pp. 15–17. Web opens: `turn318788244view0`, `turn295260423view0/1`, `turn408406088view0/1`. The source explicitly establishes vector-bundle v-descent on perfect schemes. Its warning in Remark 4.3 against inferring unrelated descent properties is respected.
- Jaffe, D. B. *Coherent functors, with application to torsion in the Picard group*. Original arXiv:alg-geom/9410009v1, <https://arxiv.org/pdf/alg-geom/9410009>. Independently read Proposition 10.8, printed p. 42, and Theorem 10.11 with its full proof sketch, printed p. 43 (PDF indices 41–42). The theorem says Pic of a finite-type finite-field scheme is finitely generated up to a bounded p-primary direct-sum term, which disappears after inverting p. Web opens: `turn165620748view0/1/2`. Later publication numbering differs and is not substituted.

Part B is responsible for the main-text integration and bibliography. This note records the independent mathematical check and the precise remaining nonproper limitation.


## Subsequent resolution at 06:20 UTC

The nonproper base-image or genus-one saturation gate isolated above is now resolved, conditional on the same surface-divisor Tate conjecture. The full proof is `b3_all_bases_brauer_units.tex`, independently audited in full by root and Part B. On every finite-type finite-field scheme S, full H²_et(S,G_m) tensor Z_(ell), modulo its actual divisible unit-cup subgroup, is finitely generated. The proof combines the finite-generation cover kernel already established here with a smooth quasi-projective unit-cup finite-cokernel theorem, an unconditional finite-kernel residue argument on arbitrary double intersections, and rational descent of unit lattices. It therefore controls non-torsion base classes becoming torsion in Leray quotients without any replacement of full H² by Br. For morphisms with equal global units, the relative ell-Brauer cokernel is directly finite. The universal curve-family assertion is consequently equivalent to surface Tate over all finite constant fields. The earlier warning remains a valid description of the limitation of the earlier proof alone; the added unit-cup argument supplies its missing step.
