# Residually reducible comparison audit

This directory is new work after the fourth checkpoint. Earlier integrated unitary sections are unchanged.

## Current checked result

The initial normalized adjoint exclusion has been extended. A separately checked scalar-normalization lemma removes the prescribed determinant hypothesis for projectively odd origins, and the selfdual automorphic descent proves that every actual selfdual TypeI source has such an origin. Thus the exponent-e auxiliary unit excludes every actual selfdual source.

With the class-number unit, the exact determinant and inertia arguments reduce essential selfduality to selfduality. Consequently the three units at exponents 0, e and 2e leave only actual TypeI systems that are not essentially self-dual. A separate elementary ordinary lemma excludes monomial systems and finite projective image. These reductions have passed parent and sibling whole-proof reviews, with exact primary and pinned-source checks for the imported interfaces. They do not assert that the remaining source class is empty.

The quadratic mixed-cup calculation and its ordinary correction have also passed whole reviews. They construct only a characteristic-p Artin family conditional on a strict negative class. The subsequent explicit cubic criterion has passed both whole reviews: its remaining relative obstruction has dimension given by the rational cyclotomic class component of character omega^(1-e). Neither calculation is an arithmetic vanishing theorem.

## Historical comparison scope

The work now contains genuine conditional arithmetic exclusions. `KT-ORDINARY-RANK2-UNIT-EXCLUSION` proves that the corresponding auxiliary Bernoulli unit excludes an ordinary irreducible rank-two source, without a weight bound and at split or inert primes. The exact source corollary `KT-AUXILIARY-UNIT-NO-TYPEII` excludes actual Type II specializations when the exponent-2e auxiliary unit holds. Both independent reviewers and parent have passed the full proof and pinned-source application. `KT-ADJOINT-BRANCH-UNIT-EXCLUSION` extends the exponent-e exclusion to the whole specified normalized adjoint branch, recovering and removing its residual quadratic scalar character. Parent and `lean_chain` have read and passed this full proof; its hypotheses retain the exact determinant normalization and ordered adjoint inertia flag.

No inspected R=T comparison theorem itself supplies the missing upper bound for the actual odd off-diagonal module. The closest result is Berger–Klosin's three-character ordinary unitary preprint, arXiv:2611.19007v1 (13 November 2026). Its characteristic-zero weight range and ordered flags differ from ours, and its residual cyclicity condition concerns exactly the negative Tate-character group. The new theorem `KT-RESIDUAL-CYCLICITY-SCOPE` proves that, in the qualifying split ordinary congruence branches, this cyclicity would already force the original rational strict Selmer group to vanish.

The separate theorem `KT-POLARIZED-EXTENSION-GRAPH-OBSTRUCTION` gives an **abstract profinite group**, not a number-field or automorphic counterexample. All three auxiliary twisted-negative cohomology groups, and both rational positive-root groups, vanish in that example, even with divisible coefficients. The remaining positive twisted root and negative rational root still generate an absolutely irreducible polarized rank-three representation. This disproves the proposed purely GMA inference from those vanishings. It does not disprove any arithmetic theorem using additional global input.

## Deliverables

- selfdual_source_exclusion.tex: checked descent of every actual selfdual source to a projectively odd rational rank-two origin, and its exclusion under the exponent-e unit.
- essential_selfdual_reduction.tex: exact determinant-one and essential-selfduality reduction, followed by the actual three-unit source restriction.
- SCALAR_NORMALIZATION_REVIEW.md: independent whole proof and local class-field-theory source review of the sibling's scalar-normalization lemma.
- global_mixed_cup.tex and global_mixed_cup_check.py/json: checked global quadratic obstruction and ordinary correction, with eight exact matrix identities; no higher lift or source point.
- source_to_cubic_jet.tex: reviewed formal-ring counterexample and conditional sparse valuative extraction; actual source declarations do not supply its extra depth/support hypotheses.
- cubic_shuffle_comparison.tex and cubic_shuffle_check.py/json: exact endpoint/consecutive comparison and relative-local transport; appended Fp Bockstein/norm identification now uses the explicitly repaired matched-system argument, with eleven exact cochain identities. No norm-ideal value or source exclusion is proved.
- cubic_massey_condition.tex and cubic_massey_check.py/json: checked explicit normalized cubic lifting criterion and fifteen exact symbolic identities; no actual source-to-independent-jet implication is asserted.
- `reducible_comparison_results.tex`: exact applicability audit, polarized Cayley–Hamilton scope example, and the complete cyclicity obstruction proof.
- `polarized_extension_graph.tex`: exact root/sign table and the complete profinite-group obstruction proof.
- `extension_graph_check.py` and `.json`: standard-library exact matrix and finite-character checks. These do not prove the profinite or arithmetic assertions; the written proof supplies the profinite argument.
- `local_mixed_paths.tex`: actual local Galois calculation showing that the mixed directions fit a crystalline upper family and a near-identity conjugation on the chosen ordinary component. Independently reviewed; no global existence is inferred.
- `ordinary_rank2_exclusion.tex`: complete ordinary exclusion, residual restriction/twist variant, and exact actual Type II source corollary.
- `adjoint_unit_exclusion.tex`: checked extension to the entire specified normalized adjoint branch, recovering and removing its unknown residual quadratic scalar twist. No classification of all stable rank-three sources is asserted.
- `PRIMARY_SCOPE.tsv`: exact source versions, locators, and read depth.
- `CHECK_EVENTS.tsv`: truthful self-check and review records; no kernel check is claimed.
- `manifest.json`: current file hashes and source URLs, produced by `refresh_manifest.py`.

## Primary sources and version control

1. Bellaïche–Chenevier, *p-adic families of Galois representations and higher rank Selmer groups*, [arXiv:math/0602340v2](https://arxiv.org/pdf/math/0602340v2), 12 January 2007. The downloaded unversioned URL resolved to this version. The exact locators here are Prop. 1.5.1 pp. 32–34, Thms. 1.5.5–1.5.6 pp. 35–37, Remark 1.5.8 p. 38, not the final Astérisque pagination.
2. Urban, *Selmer Groups and the Eisenstein-Klingen Ideal*, [arXiv:math/9803171v1](https://arxiv.org/pdf/math/9803171v1), Theorem 1.1, author p. 6. We use the published theorem through this exact author version; the large surrounding automorphic proof is imported, not reconstructed.
3. Berger–Klosin, *On deformation rings of residually reducible Galois representations and R=T theorems*, [author PDF](https://kklosin.github.io/files/hd32.pdf), dated 10 February 2011. Assumption 5.1 p. 13; the divisible module W is explicit on p. 16 before Theorem 6.4; Theorems 8.5–8.6 p. 23.
4. Berger–Klosin, *On modularity of reducible residual Galois representations*, [author PDF](https://kklosin.github.io/files/bergerklosinonlifting21.pdf), dated 2 April 2013. Introduction pp. 1–3, Assumptions 2.6–2.7 p. 6, Assumption 4.2 and Lemma 4.4 p. 12.
5. Berger–Klosin, *On p-adic modularity of abelian threefolds with imaginary multiplication and rational p-isogeny*, [arXiv:2611.19007v1](https://arxiv.org/pdf/2611.19007v1). This is explicitly a recent preprint. The official arXiv and mirror PDF downloads are byte-identical, SHA256 `7daa95a88116c5ce389eb08bbde4b418da26d28f61bee9b23483a75dca799b2b`. General Prop. 2.12/Cor. 2.16 pp. 7–9, Definition 8.22 p. 48, §10 pp. 51–56.
6. Allen–Newton–Thorne II is separately audited with its primary PDF under `evidence/lean_chain/thorne_scope/`; `THORNE_SCOPE.md` records exact failures of conditions (iv) and (vii), not a missing Selmer hypothesis.
7. Laurent Berger, *An introduction to the theory of p-adic representations*, [author notes](https://perso.ens-lyon.fr/laurent.berger/autrestextes/barcelone.pdf), Section 5, Theorem 5.1, author p. 4; Section 16, author pp. 14–15. The local duality/Euler statement and complete crystalline-extension dimension derivation were read. The foundational period-ring and local-duality proofs remain imported inputs.

The actual source application uses the pinned commit `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4`. Exact statements, proof ranges, and finite-coefficient descent are listed in `PRIMARY_SCOPE.tsv` and the independent `ORDINARY_RANK2_REVIEW.md`. No new Lean kernel execution is claimed.

The source results are used as theorems. No full reconstruction of their automorphic lifting, main-conjecture, or congruence-module proofs is claimed.

Additional primary sources now used are Ramakrishnan's five-page 2014 author note (Theorem A, Corollary B, Proposition C(b), formula (6b), read in full), Arthur–Clozel Chapter III Theorems 3.1, 4.2(d), and 5.1 (exact statements/proofs reread from the sibling's primary copy), Milne's local class-field-theory notes (exact passages in SCALAR_NORMALIZATION_REVIEW.md), and Milne's Arithmetic Duality Theorems, second edition, Chapter I Sections 2, 4 and 5 (exact duality/Euler statements and their finite-S setup). Their precise read depths are recorded in PRIMARY_SCOPE.tsv. The independent Jacobi field-construction review is in the sibling directory ../jacobi_review; that theorem provides two units under its stated condition and does not supply all three units in one field.

## Independent checks

The sibling `lean_chain` whole-read the comparison draft, the complete new GMA and cyclicity proofs, and the precise primary source scopes. Its final report is `evidence/lean_chain/REDUCIBLE_COMPARISON_REVIEW.md`. The checked comparison-section SHA256 is `f4a4f6d1fe43b58bc367acf8fae0a01e1b805a8c685ac93cffa37bd0a39012e2`.

Parent whole-read the comparison proof and confirmed the mathematics, subject to that primary-source review. The inert prime 697446897311 is explicitly excluded from the split-prime preprint application; the cyclicity theorem is scoped to qualifying split branches.

The local-family and ordinary-rank-two reviews are `evidence/lean_chain/LOCAL_MIXED_PATHS_REVIEW.md` and `evidence/lean_chain/ORDINARY_RANK2_REVIEW.md`, with a second full ordinary review at `evidence/main_gate/ordinary_rank2_review/REVIEW.md`. The ordinary section's independently reviewed mathematical version has hash `dbf0385112c0ad125e3372b1ac10bb45051fd6c1a7e2d40f0925cd3a745d7d0d`; parent subsequently removed only math-mode wrappers around pure path identifiers for layout, giving hash `bef7284efe069539219cc8e97bb8dd1ee75acd0d8850e0eebb28de9b4e3c0b27`.

The final adjoint section hash is `d4973ee9a019c8d619e91ab637e5aaff5ec8fa55faf1db748d9be7d7d9b6c08a`. Its final statement explicitly places the residual triple on the restriction to G_E, and its order argument uses the stated condition (p−1) not dividing 2e rather than assuming the full source GD predicate.

The general strict Selmer vanishing problem remains open. The conditional rank-two and selfdual source exclusions are not R=T or saturation theorems. Under all three auxiliary units, the remaining sources are primitive, not essentially self-dual, and have infinite projective image. The mixed-cup and cubic calculations do not remove this remaining class.

## Later reviewed hashes

The selfdual section's whole-reviewed mathematical hash was 9f1ba655b6a45e70e1943d83909d1356e90706850563d5856ebbfe808f6636f6. Removing only obsolete pending-review language gave 336b60a3f3fd05d0b602a14cec9dda7580dd24bed98336e8bca32bf48a079dc4; the exact status-only diff and historical snapshot are retained. The essential-selfdual section's reviewed hash is 07e408de70dd8c88974b645fdb4548095780d52fef4d5fbb45f2d6510f7e76af.

The mixed-cup section passed both whole reviews at f3872ccd0441efea705fd42674ac4968523942a2bfd056ab19e5562f78918e35. A parent-requested explanation makes the automatic even-exponent noncritical condition explicit; its diff also passed both reviews. Three missing display closings were then restored, without mathematical changes. The current balanced-display hash is 6c4bb78b97c942a718c30c408f99fab991122c5fc6ca202a6f883a886b31711b. Both exact diffs and historical snapshots are retained.

## Norm-system scope repair and exact excision comparison

The historical checkpoint07 properness inference at cubic shuffle SHA0268d712 was incomplete; `NORM_MATCHING_REPAIR.md` records the gap, a counterexample to the blanket inference, the preserved snapshots, and the explicit repair. The new `cubic_excision_norm.tex` identifies the full relative obstruction with the rational class component and proves a matched norm-system lemma using zero absolute inflation. Its exact norm equality has no evaluated arithmetic value and supplies no new vanishing result. Current proof/check events supersede the earlier terminology-only properness scope.

## Quartic and quintic targets

`quartic_quintic_obstruction.tex` gives the exact three quartic BCH cochains and their ordinary local conditions. Three auxiliary units leave a positive quartic class in the even component eta*omega^(1-2e); the opposite auxiliary unit is sufficient to remove that group. The lower rational quintic target has dimension 1+d, with d the original strict rational negative dimension. It is not replaced by its raw odd mirror. Geometry independently whole-reviewed the proof and code and freshly replayed the symbolic check. No arithmetic value is obtained.

`finite_coefficient_norm.tex` separately proves the finite-field polarization reduction for the actual relative cubic norm class; both geometry and lean independently whole-reviewed the actual relative-primitives construction and passed it at SHA 0ff58707446a6198aa2058b31bd1bc34442d26c46bc791ed3473e7503712a3a3. No ideal-class value is evaluated.

- `actual_source_pairing_audit.tex`: author and independent whole-proof/source-scope PASS. The positive extension class is not the strict negative class's Cartier dual; exact matrix identities retain other extension products. This is a limitation audit, with no new arithmetic gate or vanishing.

- `hsieh_unitary_scope.tex`: precise direct-application exclusion for the inspected ordinary U(2,1) Eisenstein branch; author, parent and independent whole proof/source reviews passed. Its residual odd cyclotomic ratio does not match the all-even source triple. The congruence-ideal containment alone also supplies no unit exclusion.
