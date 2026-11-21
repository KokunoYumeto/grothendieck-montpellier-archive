# F-SM-30: the interval theorem without an exact realization

**Model:** GPT-6 Astra Pro  
**Effort:** not exposed  
**Run:** /root/source_and_masullo  
**Date:** 2026-11-21 UTC  
**Complete proof:** source_cote1348_grothendieck.tex

## Result

Let M be a k-linear Grothendieck abelian category with enough projectives. Let κ:Mod(k)→M be exact and preserve coproducts, with left adjoint φ. Assume the canonical counit Lφ(κk)→k is an equivalence, and each object X embeds in an object A_X with Lφ(A_X)=0 in every degree, including degree zero. The original full tensor interval gives A_X=J⊗X.

Then localization at maps inverted by Lφ is equivalent to D≥0(k), at the level of infinity-categories and hence of ordinary homotopy categories.

This removes the exact chain-valued realization Λ from F-SM-29. It also removes any finite-presentation assumption on projective generators and any scalar projectivity assumption on their Hom modules. The remaining **extra hypothesis relative to the bare handwritten (a)–(d)** is that M is Grothendieck: exact filtered colimits and a generator. Enough projectives is already an original hypothesis. We do not infer AB5 or a generator from the recovered handwriting.

## Proof architecture

1. A projective epimorphism onto a generator gives a projective generator and functorial projective resolutions. For a filtered indexing category I, resolve a diagram in M^I by free diagrams i_!P. Evaluation and colimit take these projective diagrams to projectives. AB5 and the colimit preservation of φ then prove that every L_jφ commutes with filtered colimits. The analogous coproduct calculation also holds.

2. The graded derived functor is accessible, so the inverse image of isomorphisms is an accessible weak-equivalence class. Beke's generating-monomorphism and Smith recognition theorems now apply directly to Lφ. A monomorphism is weakly equivalent precisely when its cokernel is Lφ-acyclic. A map with the right lifting property against all monomorphisms is split epic with injective kernel; that kernel splits off its assumed acyclic overobject. This establishes all recognition conditions. Every object is cofibrant.

3. The coherent functor is obtained from the genuine derived infinity-functor Lφ:D≥0(M)→D≥0(k), not from a functor known only on homotopy categories. It and the exact derived κ preserve pushouts and coproducts, and therefore all colimits by HTT 4.4.2.7. Canonical normalization consequently extends from k to every scalar module using projective resolutions and Dold–Kan realization.

4. Relative localization gives a coherent F:M[W−1]→D≥0(k). It preserves coproducts. Every homotopy pushout is represented by a cofibrant monic span, whose ordinary pushout gives a short exact sequence. Applying the genuine derived φ proves pushout preservation with the correct comparison maps. The same primary colimit-generation theorem gives preservation of all colimits.

5. Define L(C)=hocolim κΓ(C). Then FL≃id. A projective resolution P•X→X gives a natural span X←hocolim Γ(P•X)→L(φP•X). The right map comes from the adjunction units on projectives, which are weak equivalences by normalization. The left map is the actual augmentation; its F-image is the derived φ-image of the projective-resolution augmentation, hence an equivalence. This proves LF≃id with coherent natural comparisons.

The totalization/realization calculation is fully proved in F-SM-29. Its extension here uses precisely exact sums, AB5, Dold–Kan, finite free normalized simplex chains, and finite-diagonal total complexes; the proof identifies these dependencies explicitly.

## Primary source inspection

- Beke, T. (2000). *Sheafifiable homotopy model categories*. Mathematical Proceedings of the Cambridge Philosophical Society, 129(3), 447–475. https://doi.org/10.1017/S0305004100004722 . Author copy: https://faculty.uml.edu/tbeke/sheafi.pdf . Directly checked Proposition 3.10, author pp.24–25; Proposition 1.12, p.11; and the previously inspected Theorem 1.7 and Propositions 1.15/1.18. Local source: research/source_1348_model/Beke2000.pdf.
- Lurie, J. (2009). *Higher topos theory*. Princeton University Press. https://www.math.ias.edu/~lurie/papers/HTT.pdf . Proposition 4.4.2.7, printed p.297, directly checked including the preceding skeletal construction proof. Web references: turn120636065search5, turn657234564view2, turn573386416view1.
- Lurie, J. (2017, September 18). *Higher algebra*. https://people.math.harvard.edu/~lurie/papers/HA.pdf . Directly checked Example 1.3.3.4 p.98, Theorem 1.3.4.4 and Proposition 1.3.4.6 p.109, Proposition 1.3.4.22 p.118, and Propositions 1.3.4.24–25 p.119. Theorem 1.3.4.4 is the ordinary-chain-category localization statement; Proposition 1.3.4.6 alone concerns the dg nerve. Web references: turn657234564view0, turn657234564view1, turn573386416view2, turn646213216view0. Full copyrighted texts are not part of the new deliverable.
- The Stacks Project Authors. (2026). Dold–Kan, Theorem 14.24.3, Tag019G. https://stacks.math.columbia.edu/tag/019G . Known input already directly inspected.

## Actual checks

The author read the complete saved proof, checking each of the five stages and both natural inverse comparisons. A short clarification then supplied the chain-level representative of the derived counit, and the parent-requested citation correction added HA Theorem 1.3.4.4; these additions were inspected in context. Author whole-proof check: **PASS**, completed 01:59:24 UTC. This is an author proof reading, not an independent reproof.

The parent separately reported a complete independent whole-proof reading with primary sources checked and no mathematical gap. Its actual event is logged by the parent; the author's own ledger does not substitute for that event.

## Failed extensions and exact remaining scope

Neither arbitrary abelian categories nor nonexact filtered colimits are covered by this proof. The filtered projective-diagram argument uses AB5 in an essential place. A bare exact double-dual quotient endofunctor does not supply AB5 for its square-zero module category. The intake's three-sort counterexample remains unreconstructed as a full symmetric tensor/interval construction; we do not assert that its unprovided coherence certificate was checked.

No assertion about every ordinary right-adjoint counit follows here. The specified raw G test remains separate whenever an exact chain-valued adjunction is independently chosen.
