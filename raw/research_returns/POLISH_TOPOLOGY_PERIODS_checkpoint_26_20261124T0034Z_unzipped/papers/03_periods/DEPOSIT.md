# Deposit sheet

## Bibliographic information

**Title:** A counterexample and a dimension formula for Grothendieck's strong transcendence conjecture

**Author line:** Intentionally blank. The method statement identifies GPT-6 Astra in ChatGPT Pro mode; no human has checked the mathematics or text. No more specific effort setting is asserted.

**Date:** 23 November 2026.

**Suggested categories:** Algebraic Geometry; Number Theory. Suggested MSC 2020: 14C30, 11J81, 14K22, 14F20.

**Keywords:** Grothendieck period conjecture; motivated motives; complex conjugation; Hodge splitting; Hodge–Tate filtration; Cartier operator; integral Betti comparison.

**Licence:** CC0 1.0 for the text and accompanying original programs. Third-party works are cited and are not included in the source package.

## Abstract

Grothendieck's Montpellier notes propose a strong transcendence conjecture for the comparison between Betti, de Rham and Hodge realizations. We show that five of its predicted degrees are too large for a non-CM elliptic curve defined over the rationals. For a pure motivated motive and its complex conjugate, we compute the six algebraic image dimensions of the comparison triangle. One normal subgroup of their joint motivic Galois group measures the missing freedom. These dimensions are unconditional upper bounds for the corresponding transcendence degrees, and become equalities under the period conjecture for the joint motive. An explicit elliptic analysis describes the splitting parameter, its CM examples, its zero locus and its extremal growth normalization. We also explain three limitations of comparison data: ordinary Hodge–Tate filtrations do not detect complex multiplication of elliptic curves, polarizable rational Hodge structures with a real involution need not be geometric, and rational or locally integral comparisons need not assemble to an integral comparison. The mathematics and text were produced and checked by GPT-6 Astra in ChatGPT Pro mode; no human has checked them.

## Contribution and qualifications

The main unconditional result is the six-dimensional image table `(g,u,b+v,u,u+v,g+v)`, together with the uniform relative bounds and the explicit real elliptic counterexample. The equality statement is visibly conditional on period genericity for the joint motive. The paper supplies proofs for its stated reductions and constructions and identifies the classical theorem inputs. It proves full faithfulness and the Artin–Tate classification for real abelian absolute-Hodge motives using Deligne’s theorem and real descent; the corresponding homological statements retain the exact Hodge-conjecture hypothesis. It does not claim priority for the assembled result or its ingredients.

The auxiliary examples are included for their precise implications for realization arguments. Howe's ordinary splitting, Cartier's identity, Schneider's period-ratio theorem, CM reciprocity, Hodge rigidity, and computability of periods are credited. The nonreal elliptic example shows that an isomorphism to the conjugate motive is broader than real descent.

The expanded release has 84 pages. Its exact source crosswalk has 186 rows: 133 are represented in the paper (one only partially), one published-correction item is excluded by instruction, and 52 remain outside this incorporation. This release does not claim complete coverage of SA07.

The elliptic zero classification is credited to Sebbar–Besrour Lemma8.1; its proof is reproduced with exact Fourier estimates. The CM period-field consequence uses Nesterenko's exact theorem. Additional cycle normalization, integral Lefschetz, semilinear descent and nodal-normalization examples are included with proofs and named comparison inputs.

All sixteen local-comparison source rows are now incorporated. Section8 distinguishes arbitrary generic-fibre p-divisible groups from good-reduction objects and gives the exact known crystalline, semistable, derived and prismatic inputs. Under both global centralizations and modified-section compatibility, Proposition8.2 proves the equalizer is normal; a separate unconstrained example shows why the hypotheses matter. Proposition8.3 gives an inverse Artin–Tate system satisfying all those identities whose image is not p-adic analytic. The arithmetic classifications are known imports with exact primary locators.

The further expansion proves the tensor twist of real Betti realization, the relative-frame quotient and its dimension, simultaneous local genericity in compact-open adelic cosets, and the precise all-frame openness equivalence. The known elliptic open-image and strong-approximation theorems are credited with their exact hypotheses. The actual comparison-cocycle closure equals the period locus; a genuine CM example shows that generated-subgroup closure can be larger. Its varying-elliptic augmentation has minimum field degree one in the effective degree-one category but makes no full-group assertion. A Tate-square example refutes universal openness of the combined image, while non-CM elliptic openness remains equivalent to the unresolved period genericity assertion.

The further elliptic expansion supplies Masser's exact formula and the modular coefficient normalization, the rank-three projector tensor, torsion Poincare translations and Gaussian cancellation, compact algebraic-point and restricted-Lie tests, Tang's rational density bound, and the precise Frobenius lifting criterion. It also gives explicit CM denominator and horizontal-integrality counterexamples, with the applicable published modular and differential-equation theorems cited exactly. It leaves algebraicity of the complex splitting parameter as distinct from the stronger crystalline and boundedness conditions; no converse-to-CM theorem is inferred.

The nine-result elliptic continuation proves the actual conjugate quotient and its differential scale, second-kind lattice and algebraic-model obstructions, symmetric-square and conjugate-extension identities, the precise quantitative restricted-Lie density application, ordinary isogeny denominator formulas, the conditional quotient-graph rank bound, actual period-product jet obstruction, and local size/positive-tau failure of the cited algebraicity criteria. The foundational subgroup, density, ordinary integral-structure and geometric-size theorems are credited to the exact primary sources. Quantitative gaps that were open in the frozen attempt were completed only after source comparison; the records preserve that distinction.

The four-result comparison/Hodge continuation proves the finite-diagram and entire finitely generated comparison theorem, both uncountable behaviours with examples over C itself, and a tensor-compatible nongeometric Hodge assignment over Q and over the entire complex motivated category. An arbitrary-index linear lift controls the uncountable category. The unchanged plain integral class and the merely chosen de Rham comparison remain explicit, so no unspecified essential-image claim is inferred. Wibmer’s complex-coefficient torsor result is credited as a known input.

The number-field continuation gives finite labelled tests for elliptic ring class subfields, generalized-dihedral fields, every totally real and CM field, and hence every cubic field. It proves the exact Artin transporter and its still unresolved universal-image formulation. A separate quartic example admits a simultaneous integral comparison on the entire specified CM/Artin diagram, preserving polarizations and ordinary Hodge structures but not geometric real Frobenius. Its integrality follows from the exact CM quasi-isogeny theorem and an explicit denominator argument. The finite fixed-field isogeny skeleton and the necessary projective Tate condition have their different domains and logical strengths stated explicitly.

## Where the required material appears

| Item | Location |
|---|---|
| Exact archival question and direct quotation | Section 1; cote 18, handwritten p. 10 / PDF p. 11 |
| Hypotheses and necessary definitions | Sections 1–2 |
| Main unconditional theorem | Theorem 1.1 and Sections 3–4 |
| Explicit counterexamples | Corollary 1.2; Sections4–13 |
| Complete proofs and named theorem inputs | Sections2–13; exact reference locators in text |
| Conditional and unresolved statements | Theorem 1.1 equality clause and Sections11,14 |
| Method, model, human-review status and licence | Abstract and Method and records |
| Code and records links | Method and records; macros in the preamble |

## Files and reproduction

`main.tex` is the entire standalone source, including bibliography. `main.pdf` is the rendered paper. `BUILD.md` gives the two-pass pdfLaTeX build and the standard-library Python certificate commands. No custom class, external bibliography, figure, or unpublished source is required. The checks, independent-dimension memo, exact 186-row incorporation crosswalk, literature version records and separate correction note accompany the paper in the notes directory.

**Repository destinations:**

* https://github.com/KokunoYumeto/algebraic-cycles-and-motives-workbench
* https://github.com/KokunoYumeto/mathematics-workbenches

The deposit sheet does not certify that a repository upload or public deposit has occurred. It records the supplied destinations and the complete local package.

## Review limits

No human review, external referee report, or formal proof certification is claimed. The earlier separate root derivation was blind for the initial orbit calculations and later clarified through discussion; its exact scope is recorded. A further previously unexposed worker has now frozen a complete statement-only reconstruction of Theorem 1.1 and Corollary 1.2, then compared it with the manuscript. Its full scope, named inputs, and later proof clarifications are recorded separately; this does not claim independent reproof of every other assertion or of imported foundational theorems. The finite computations test explicit cases and signs, while the all-prime proof is written in the paper. The Bhowmik–Pathak preprint issue is excluded from this paper and appears only in the separate correction note, with the unavailable journal-version comparison explicitly outstanding.
