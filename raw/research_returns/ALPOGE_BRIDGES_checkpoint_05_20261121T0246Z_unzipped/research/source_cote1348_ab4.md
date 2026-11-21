# F-SM-32 — The interval localization theorem under AB4

**Status:** Complete deduction written in `source_cote1348_ab4.tex`; author and peer checking are recorded separately in the check ledgers. This is a new application of existing cofibration localization and derived-category theorems, not a reproof of those background theorems.

**Model:** GPT-6 Astra Pro. **Effort:** not exposed. **Run:** `/root/source_and_masullo`. **Date:** 2026-11-21 UTC.

## Exact result

Let M be a k-linear abelian category with enough projectives and small coproducts. Let φ be left adjoint to an exact, coproduct-preserving scalar functor κ. Write F(X)=Lφ(X[0]) and W=F⁻¹(equivalences). Assume the canonical counit Fκ(k)→k is an equivalence, every X admits a monomorphism into an F-acyclic object (including H₀), and the canonical comparison ⊕F(Xᵢ)→F(⊕Xᵢ) is an equivalence for every small family. Then M[W⁻¹]∞≃D≥0(k)∞.

AB4 (exact coproducts) implies the stated compatibility: coproducts of projective resolutions remain projective resolutions and φ preserves their coproducts. No AB5, generator, presentability, exact chain-valued realization, or functorial choice of projective resolutions is needed. The result thus includes the non-AB5, nonpresentable category in F-SM-31.

## Proof route and the two points requiring care

1. All monomorphisms are cofibrations. The interval gives an explicit factorization X→A_X⊕Y→Y of every f:X→Y, with a monic first map and a weak equivalence second map. Derived exact triangles give the pushout axioms. The coproduct assumption makes W stable under coproducts.
2. The finite cofibration localization theorem and the coproduct theorem provide all colimits in the localization. They do **not** require exact filtered colimits or a sequential-colimit axiom. F descends as a coherent functor that preserves those colimits.
3. The left-fraction description proves that this descended functor is conservative. This conclusion is not inferred from the bare definition of W.
4. HA Theorem 1.3.3.8 extends γκ on projective scalar modules to L:D≥0(k)→M[W⁻¹], and γ on projectives of M to T:D≥0(M)→M[W⁻¹]. Projective normalization gives FL≃id; the adjunction units on projectives give T≃L Lφ.
5. The potentially nonfunctorial resolution choices are avoided by extending P↦(γP,P,id) into the comma infinity-category (id↓γ). Its geometric realizations are componentwise, even though γ need not preserve ordinary realizations. This supplies a coherent augmentation T→γH₀. After applying F, the universal property identifies it with Lφ(C)→Lφ(H₀C[0]). It is therefore an equivalence on the heart, by conservativity. This yields LF≃id after relative localization.

The saved TeX proves the componentwise comma-colimit assertion by the mapping-space pullback formula and checks the actual arrow-valued augmentation, rather than comparing its two objects abstractly.

## Original scope

Fresh visual inspection of the supplied official scans, cote 134-8 footers 46–48, shows the bilinear symmetric tensor convention and the scalar functor's adjoints/exactness. No explicit AB4 assertion or exactness of arbitrary scalar copowers on every object was located there. Thus AB4 remains an explicitly additional sufficient condition, and the weaker derived coproduct condition is the exact residual gate isolated by this result. This module does not certify the bare abstract handwritten assertion without that condition. The ordinary raw right-adjoint counit remains a separate question.

## Primary sources and exact locators

- Cisinski, D.-C. (2019). *Higher categories and homotopical algebra*. Cambridge University Press. [Author PDF, dated 30 July 2026](https://cisinski.app.uni-regensburg.de/CatLR.pdf). Proposition 7.5.6, printed pp. 372–373; Proposition 7.7.1, p. 396; Definition 7.7.2 and Proposition 7.7.4, p. 397. The latter dual all-colimit form confirms that no sequential ordinary-colimit hypothesis is hidden. Directly inspected web references: `turn723359040view0`, `turn199616872view1`, `turn545355257view0`.
- Ramzi, M., Sosnilo, V., & Winges, C. (2025). *Every motive is the motive of a stable infinity-category* (arXiv:2503.11338v1). https://arxiv.org/abs/2503.11338 . Definition 2.5 and Theorem 2.6(1),(4), pp. 5–6; Remark 2.3 and Example 2.4, p. 4. Direct primary statement and proof inspection: `turn629095888view1`, `turn629095888view2`, `turn545355257view1`. CC independently located and inspected the same input; their note is `consequences_criteria_cofibration_sources.md`.
- Lurie, J. (2017, September 18). *Higher algebra*. https://people.math.harvard.edu/~lurie/papers/HA.pdf . Theorem 1.3.3.8, p. 101; Lemma 1.3.3.11(2), pp. 103–104; Proposition 1.3.3.16 and Lemma 1.3.3.17, pp. 106–107; Theorem 1.3.4.4, p. 109. Direct primary inspection: `turn936814072view1`, `turn936814072view2`, `turn521233747view0`, `turn521233747view1`. The theorem concerns functor infinity-categories and consequently controls natural transformations, which is essential in Step 5.
- Lurie, J. (2009). *Higher topos theory* (Annals of Mathematics Studies, Vol. 170). Princeton University Press. https://www.math.ias.edu/~lurie/papers/HTT.pdf . Propositions 4.4.2.6–7, pp. 296–297; exact primary statement read during F-SM-30 and used here without an altered hypothesis.
- Grothendieck, A. (n.d.). *Cote 134-8* [Unpublished manuscript], footers 46–48. Archives Grothendieck, Université de Montpellier. https://grothendieck.umontpellier.fr/134-8.pdf . Fresh visual source files: `root_sources/1348_pre-47.png`, `root_sources/1348_pre-48.png`, `root_sources/1348_48_thm_crop.png`.

No complete third-party book or article is copied into this module.
