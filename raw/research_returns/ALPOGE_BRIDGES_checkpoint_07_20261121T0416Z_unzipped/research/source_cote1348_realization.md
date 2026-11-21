# F-SM-29 — the full underlying connective localization over every coefficient ring

**Run:** /root/source_and_masullo  
**Model:** GPT-6 Astra Pro  
**Effort:** not exposed  
**Author whole-proof rereading completed:** 2026-11-21 01:28:27 UTC  
**Complete proof:** source_cote1348_realization.tex, 476 lines  
**Checked TeX SHA256:** efb3bcc031b45e63c9c15ed8d0109fa5952829d7a893a7d30861a4490a215994

## Outcome and precise scope

The underlying localization conclusion is now proved over **every commutative scalar ring k** in the module-category setting of the original corollary, once BR-13405 supplies its exact adjunction. The theorem retains the canonical normalization and the full interval hypotheses, including degree zero. It requires neither finite scalar injective dimension nor finite scalar pure-injective dimension; it requires neither finitely generated scalar morphism modules nor FP-infinity for the coefficient module D.

The proof establishes the equivalence induced by Λ=Lφ:
  
W^{-1}M ≃ D_{≥0}(k).

The inverse uses a homotopy colimit. The ordinary right adjoint G need not be this inverse before deriving it; the proof does not establish that G preserves all quasi-isomorphisms. The ordinary all-counits assertion remains the exact BR-13403 test on acyclic projective chain objects. The derived right adjoint, computed after target fibrant replacement, is a quasi-inverse.

Thus the original **underlying corollary-level localization question** is settled in the stated range, while the stronger ordinary-adjoint assertion remains separately identified. The unrestricted handwritten theorem for arbitrary abelian M without the module/presentability setting has not been asserted here.

## Proof architecture

### Canonical normalization for every scalar module

The canonical maps Λκ(U)→U[0] are quasi-isomorphisms for projective U by coproducts and retracts of the unit normalization. An arbitrary module U is resolved by projective scalar modules. Applying the exact functor Λκ yields a first-quadrant bicomplex whose augmented rows are exact, while the already established canonical maps are quasi-isomorphisms in each resolution degree. Finite diagonals prove normalization for every U. The proof uses the actual counit map, so the later unit calculation is canonical.

### A model structure with all monomorphisms as cofibrations

The set of inclusions U↪R(-,x), for every submodule of every representable, generates all monomorphisms. A complete element-by-element transfinite proof is included: at each stage adjoin one element of the target using its representable, and identify the pushout with the sum of the preceding submodule and the cyclic image.

The weak equivalences are accessible because H_*Λ preserves filtered colimits and isomorphisms form an accessible class. Beke's exact inverse-image and solution-set propositions supply Smith's final set condition.

Two-out-of-three and retract closure are immediate from quasi-isomorphisms. For a monomorphism, weak equivalence is equivalent to acyclicity of the cokernel's Λ-image, so pushouts preserve trivial cofibrations. Exact filtered colimits handle transfinite composition.

A map lifting against all monomorphisms is a split epimorphism with injective kernel. The interval embeds that kernel into an object with zero derived image; injectivity splits this embedding, so the kernel also has zero image. This verifies the required inclusion of injective-trivial-fibrations into weak equivalences.

The same argument constructs the needed model structure on nonnegative scalar complexes directly. It does not improperly restrict an unbounded injective model structure. The functor Λ is left Quillen because it is exact and detects the chosen weak equivalences.

### Homotopy colimits as normalized total complexes

The necessary formula for a simplicial chain complex Y is proved completely:

hocolim Y ≃ Tot N_simp Y.

The proof uses a projective-diagram cofibrant replacement QY. On a free representable diagram based at [m], normalized totalization is N(k[Δ[m]])⊗C, which contracts onto C by prepending vertex 0. The natural comparison to ordinary colimit is therefore a quasi-isomorphism on free diagrams. Pushout cells preserve it by a cokernel argument; transfinite colimits and retracts then give it for all projectively cofibrant diagrams. Finally a levelwise quasi-isomorphism induces a quasi-isomorphism of normalized totalizations by the first-quadrant filtration.

This establishes both naturality and compatibility with augmentations. The proof does not rely on an unproved assertion that ordinary colimit of every Reedy-cofibrant simplicial diagram is its homotopy colimit.

Left Quillen preservation of homotopy colimits is checked using projective model structures on diagrams and the actual colimit adjunction. No simplicial enrichment of M is assumed.

### The two natural inverse comparisons

Define L(C)=hocolim κΓ(C), where Γ is the Dold–Kan inverse. The normalization for every scalar module gives ΛL(C)≃C naturally. This also proves that L sends quasi-isomorphisms to W; it does not assume that κΓ does so degree by degree.

For X, choose a functorial projective resolution P•X. Every term of Γ(P•X) is a finite sum of projective objects. Its adjunction unit into κφ is a weak equivalence, since positive homology vanishes on projectives and the zeroth-homology map is an isomorphism by the triangle identity and canonical scalar normalization. Homotopy colimit gives the comparison with L(φP•X).

The augmentation hocolim Γ(P•X)→X is a weak equivalence after applying Λ: its image is the finite-diagonal total complex of ΛP•X, whose augmented rows are exact. The already checked BR-13401 comparison gives natural quasi-isomorphisms φP•X←Tot ΛP•X→ΛX. Applying the proved homotopical functor L completes a natural zigzag from X to LΛX. This proves the second inverse isomorphism without a full-faithfulness shortcut.

## Exact primary sources and checks

### Beke

Beke, T. (2000). Sheafifiable homotopy model categories. *Mathematical Proceedings of the Cambridge Philosophical Society, 129*(3), 447–475. https://doi.org/10.1017/S0305004100004722

- Author primary PDF: https://faculty.uml.edu/tbeke/sheafi.pdf
- **Theorem 1.7**, author-PDF p. 8: Smith recognition with conditions c0–c3.
- **Proposition 1.15**, p. 12: accessible class satisfies solution-set condition.
- **Proposition 1.18**, p. 13: accessible inverse-image criterion.
- **Proposition 1.12**, p. 11: general monomorphism-generation statement, inspected but replaced by a complete explicit ringoid proof here.
- Diagram model construction and generating cofibrations discussed on author-PDF p. 20.
- All page numbers above are author-PDF pages; no unchecked conversion to published pagination.
- Exact web refs inspected: turn982547037view2, turn103272735view3, turn690323070view0.
- Publisher metadata and DOI: turn150511136search1.
- Frozen local reference: research/source_1348_model/Beke2000.pdf
- PDF SHA256: d9f176798c31d033fd961aebfacbdcc710366cdeb9b4b78bee7279d5a94c13c0.

### Dugger

Dugger, D. (2008). *A primer on homotopy colimits* [Unpublished notes; current author version retrieved November 21, 2026]. https://pages.uoregon.edu/ddugger/hocolim.pdf

- Current author PDF has **109 pages**.
- **Theorem 19.4**, p. 91: projective diagram model structure for every small indexing category and every cofibrantly generated model category.
- Discussion immediately following, p. 91: homotopy colimit as derived colimit, including non-simplicial model categories.
- **Proposition 19.9**, p. 93: the totalization formula. Our proof includes its needed instance, naturality and augmentation comparison independently.
- Earlier 80-page versions have different theorem numbers; do not cite 16.9 for the frozen current version.
- Author webpage lists the primer as 2008: turn150511136search13.
- Exact web refs inspected: turn690323070view1, turn150511136view0, turn103272735view1.
- Frozen local reference: research/source_1348_model/Dugger_hocolim_current.pdf
- PDF SHA256: ee8f8c125bc2e1bc4d84beb68afce452bf58b8bf3eca5c4878c84247bb30320c.

### Dold–Kan

The Stacks Project Authors. (2026). *Dold–Kan*. Theorem 14.24.3, Tag 019G; Section 14.24, Tag 019D.

https://stacks.math.columbia.edu/tag/019G  
https://stacks.math.columbia.edu/tag/019D

- Exact statement and explicit finite direct-sum inverse construction inspected.
- Web ref: turn478890701search0.
- The theorem is used as a known background equivalence for abelian categories; no claim is made to have independently re-proved Dold–Kan itself.

## Verification status

The original predicates were visually rechecked after the proof. Manuscript footer 47(a) supplies φ as the left adjoint of κ and explicitly identifies the right adjoint of κ with Hom(1,−), so κ is exact and preserves coproducts. Footer 46 independently labels κ exact. Footer 47(b) displays the derived adjunction, and (c) displays Lφ(κ(k))→k as an isomorphism: the normalization used here is that displayed adjunction’s canonical counit. The source uses Z/unit notation at this point; the theorem uses the scalar ring notation k. Footer 48 adds finitely presented projective generators and, in its right margin, projectivity over k of the morphism modules. The proof settles this module-category corollary, not the broader abstract conditions (a)–(d) without the corollary’s presentability/construction assumptions.

The full saved proof was read in three complete contiguous chunks. Every statement and equation was checked, including both adjunction directions, all model recognition conditions, exactness and accessibility, the singleton-element pushout calculation, the diagram-model cofibrant replacement convention, the simplex contraction and cell induction, the finite-diagonal homology arguments, the naturality of both inverse comparisons, and the distinction between G and its right derived functor.

Small explanatory additions then made explicit that nonnegative chain complexes are a module category, that the colimit/constant adjunction is Quillen, why the cell images are monomorphisms, and why normalization of ΛΓ(P) gives ΛP. These additions were checked in context. The author whole-proof check passed at 01:28:27 UTC. Independent parent reading was requested separately; no independent result is inferred from the author's own check.

