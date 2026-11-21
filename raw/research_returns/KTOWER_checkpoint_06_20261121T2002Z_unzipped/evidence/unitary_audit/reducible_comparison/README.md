# Residually reducible comparison audit

This directory is new work after the fourth checkpoint. Earlier integrated unitary sections are unchanged.

## Result and limit

The work now contains genuine conditional arithmetic exclusions. `KT-ORDINARY-RANK2-UNIT-EXCLUSION` proves that the corresponding auxiliary Bernoulli unit excludes an ordinary irreducible rank-two source, without a weight bound and at split or inert primes. The exact source corollary `KT-AUXILIARY-UNIT-NO-TYPEII` excludes actual Type II specializations when the exponent-2e auxiliary unit holds. Both independent reviewers and parent have passed the full proof and pinned-source application. `KT-ADJOINT-BRANCH-UNIT-EXCLUSION` extends the exponent-e exclusion to the whole specified normalized adjoint branch, recovering and removing its residual quadratic scalar character. Parent and `lean_chain` have read and passed this full proof; its hypotheses retain the exact determinant normalization and ordered adjoint inertia flag.

No inspected R=T comparison theorem itself supplies the missing upper bound for the actual odd off-diagonal module. The closest result is Berger–Klosin's three-character ordinary unitary preprint, arXiv:2611.19007v1 (13 November 2026). Its characteristic-zero weight range and ordered flags differ from ours, and its residual cyclicity condition concerns exactly the negative Tate-character group. The new theorem `KT-RESIDUAL-CYCLICITY-SCOPE` proves that, in the qualifying split ordinary congruence branches, this cyclicity would already force the original rational strict Selmer group to vanish.

The separate theorem `KT-POLARIZED-EXTENSION-GRAPH-OBSTRUCTION` gives an **abstract profinite group**, not a number-field or automorphic counterexample. All three auxiliary twisted-negative cohomology groups, and both rational positive-root groups, vanish in that example, even with divisible coefficients. The remaining positive twisted root and negative rational root still generate an absolutely irreducible polarized rank-three representation. This disproves the proposed purely GMA inference from those vanishings. It does not disprove any arithmetic theorem using additional global input.

## Deliverables

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

## Independent checks

The sibling `lean_chain` whole-read the comparison draft, the complete new GMA and cyclicity proofs, and the precise primary source scopes. Its final report is `evidence/lean_chain/REDUCIBLE_COMPARISON_REVIEW.md`. The checked comparison-section SHA256 is `f4a4f6d1fe43b58bc367acf8fae0a01e1b805a8c685ac93cffa37bd0a39012e2`.

Parent whole-read the comparison proof and confirmed the mathematics, subject to that primary-source review. The inert prime 697446897311 is explicitly excluded from the split-prime preprint application; the cyclicity theorem is scoped to qualifying split branches.

The local-family and ordinary-rank-two reviews are `evidence/lean_chain/LOCAL_MIXED_PATHS_REVIEW.md` and `evidence/lean_chain/ORDINARY_RANK2_REVIEW.md`, with a second full ordinary review at `evidence/main_gate/ordinary_rank2_review/REVIEW.md`. The ordinary section's independently reviewed mathematical version has hash `dbf0385112c0ad125e3372b1ac10bb45051fd6c1a7e2d40f0925cd3a745d7d0d`; parent subsequently removed only math-mode wrappers around pure path identifiers for layout, giving hash `bef7284efe069539219cc8e97bb8dd1ee75acd0d8850e0eebb28de9b4e3c0b27`.

The final adjoint section hash is `d4973ee9a019c8d619e91ab637e5aaff5ec8fa55faf1db748d9be7d7d9b6c08a`. Its final statement explicitly places the residual triple on the restriction to G_E, and its order argument uses the stated condition (p−1) not dividing 2e rather than assuming the full source GD predicate.

The general strict Selmer vanishing problem remains open. The new rank-two and specified-adjoint source exclusions are conditional on the corresponding auxiliary units and exact source data; they are not new R=T or saturation theorems. Stable rank-three sources outside the specified normalized adjoint family have not been removed.
