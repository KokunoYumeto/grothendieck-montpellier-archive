# Nonstandard branch: exact results and open gates

Authoring model: GPT-6 Astra Pro. Effort setting is not exposed. Dates: 2026-11-21--22 UTC.

The main conclusion is N-009: the full integral rank-four order is not locally free at (2,v−1), and consequently has no Z[v±]-basis of any kind. A finite mixed-characteristic image requires 126 generators although the generic rank is 114. The parent independently verified this with new Hecke arithmetic and a different module-cardinality algorithm, then read the complete proof. The exact definition and targeted literature audit is in `N009_definition_literature_audit.md`. The main proof file is `nonstandard_results.tex`; `integral_nonfreeness.tex` contains the complete N-009 proof separately. The branch is self-contained for computational replay: its `dependencies/` contains unchanged copies of five small supplied arithmetic/data files, with provenance below. Python 3 and Sympy are required; the new polynomial-order construction and replay also use python-flint 0.9.0. No numerical floating-point positivity test is used.

## Results

| ID | Result | Status and exact scope |
|---|---|---|
| N-009 | No integral basis exists: the full rank-four order is not locally free at (2,v−1). | Exact finite all-degree obstruction, independently verified. R=(Z/1024)[η]/η⁸ image has log₂ sizes 3690 and 3564 for M and mM, so μ(M)=126>114. |
| N-010 | The full rank-four Q(D)-form is split; explicit rational GT path vectors and all nine generator triples are constructed. | Exact symbolic Hecke/tensor/projector checks and rank-114 modular certificate; all branching is multiplicity-free. This is a GT basis, not VIII's minimum-degree E(4). |
| N-011 | The outer Laurent signs of F57, INT-NSRH-4 and F67 follow from an explicit binomial transfer. | Exact full D-polynomials and coefficient lists; distinguishes negative outermost coefficients from F67's negative next coefficients. No universal edge-negativity theorem is claimed. |
| N-012 | VIII's printed external variable-scaling minimum is unbounded below. | Exact rank-one counterexample and full rank-four minimal-GT-line proof, independently reviewed against the complete source. A bar-fixed variant remains a separate possible repair. |
| N-013 | Unique minima in an explicitly bar-fixed rational variant descend to the actual Q[D] order; odd half-integral scalings cannot minimize. | Whole proof independently reviewed by root. Existence and uniqueness are conditional, and the modified domain is explicit. |
| N-014 | VIII’s highest-weight rule does not define the asserted label partial order. | Exact rank-four dual multiplicity space has two incomparable maxima, also in faithful dimensions; distinct labels can have equal weights. Primary sources and entire proof independently reviewed. |
| N-015 | Explicit basis of the full unsaturated Q[D] order, with exact all-degree closure. | 148 words through length10,114 triangular rows,34026-node compact certificate; separate arithmetic replay passes all342 basis-generator products. Generic dimension114 and the rational-D form are now independently certified within the branch; root independently read the complete proof/verifier and replayed the full certificate. |
| N-016 | Explicit finite global decision procedure for each stage of the bar-fixed variant. | Uniform GT denominators give finite V/(S t); a computable degree cutoff reduces existence and full-domain uniqueness to finite rational affine systems. Whole proof independently reviewed by root and plethysm; the exact-linear implementation addendum was also separately reviewed. No full repaired basis is yet claimed. |
| N-017 | Actual four-element minimal block globalized for a product-path repair; a total refinement fails. | Root whole-proof/source-code reading and full reconstruction PASS. Product-order minima have exponents −8,−8,−7,−6. All64 block multiplication constants pass the signed q-unimodality test, but an ambient coefficient forces residual (q+q⁻¹)/2, disproving structural-coefficient unimodality for this explicit repair. |
| N-018 | The product-path bar-fixed repair has no minimum at the fifth position in the other minimal block. | Complete proof and exact constructor saved; separate certificate-only replay passes actual intersections and matrix-rank degree tests. First four minima unique, fifth exhaustive space dimension7, shared failure witness at (3241,4321). Root whole-proof reading and independent certificate replay PASS. Rational GT-line rescaling cannot repair the failure. |
| N-019 | A changed maximal-scaling rule gives a full balanced triple and the actual114-element Q[D] Hermite basis. | Entire proof independently reviewed by root and plethysm. Full12996-product table independently replayed by root:204876 nonzero constants, maximum degree8. Exact coefficient D−9/2 disproves the requested signed positivity for this alternative. It is not VIII's E(4). Separate proof input: maximal_scaling_globalization.tex. |
| N-020 | The abstract D=0 fibre has dimension114 and radical109, with split quotient Q⊕Mat2(Q) and an explicit corrected parabolic matrix section. | Root whole-proof/code reading and exact replay PASS; plethysm whole mathematical proof reading PASS. Ambient image55, kernel59; ambient Gram rank42 differs from regular Gram rank5. The corrected cell has C3/C6/D3 slot symmetries, but the same weighted cyclic label rule cannot extend to a full basis containing the unit and the cell. |
| N-021 | Total cancelling-pair minimization admits an explicit all-degree finite reduction for every integral Laurent trace table. | Fixed monomial matchings and an integer-minor argument give exponent bound B(d0+1)4^B at budgetB, preserving bar/label symmetries and unit/zero slots. Rank-three bounds:43656·4^7276 in general,9327 for symmetric unimodal tables. Whole mathematical proof independently reviewed by plethysm; root review in progress. No optimum or canonical choice computed. |
| N-001 | The q=−1 cyclic pairing on the inert cell cannot extend to the full ten-label rank-three table with nonzero weights. | Algebraic proof, using μe=e and e²=16e; exact table replay. This concerns the same labelwise symmetry, not cyclicity of τ(xyz). |
| N-002 | P12132 has four bad C⊗C coordinates; it is a shortest negative P-word. | All 121 words of length ≤4 checked exactly. Its two coordinate polynomials change sign on v>1, excluding the specified signed/factored form for this word. |
| N-003 | 114 explicit bar-invariant positive integral combinations of P-words of degree ≤10 form a Q(v)-basis. | Full exact positivity replay through a second multiplication path; nonzero modular rank certificate. The A-lattice they span is provably proper, by the v=2 coordinate −10656875/4608. |
| N-004 | A bare positive A-basis of the full order exists iff that order is A-free. | All-degree proof, conditional exactly on freeness; uses the certified positive full-support element z with augmentation 1 and a standard cancellation theorem. Unconditionally, there is a positive Q[v±]-basis. The freeness premise is disproved by N-009; the rational-coefficient conclusion remains valid. |
| N-005 | Two smaller rank-three composing dimension rings: 7276 cancelling pairs, or 9040 with all dimension polynomials unimodal. | Explicit formulas and algebraic proof; 132 source constants compared and all 1000 associativity triples checked twice per table. Both old search-window minima fail globally. New global minima are not claimed. |
| N-006 | Constant lisse/Weil sheaf π*C(1) on A¹ realizes the fixed-parameter F46 coefficient spaces with stalk weight −2 and Hc²=C. | Literal item 8 solved for the exact F19/F21 tensor action and F46 coefficient objects: End/Hom identities and Hc² recover the actual objects. The additional extension-retuning condition is obstructed for one fixed space by F26/F42. |
| N-007 | Q(D)-rational structure constants need not be finite Tate Laurent polynomials. | Elementary rank-two example b=P/D², b²=b/D; pole at q=−1. Rational descent itself is unaffected. |
| N-008 | At v=i the specialized ambient image has rank 55 and trace Gram rank 42 for r=4; ranks 7 and 6 for r=3. | Exact closure/rank certificate. This is not the abstract integral fiber and not an E(4) table. |

## Main replay commands

Run from any working directory by supplying the full script path if necessary:

```bash
python mixed_jet_freeness.py --p 2 --k 10 --length 8
python verify_mixed_jet_certificate.py
python rational_gt_rank4.py
python edge_coefficients.py
python polynomial_order_rank4_flint.py
python verify_polynomial_order_rank4.py
python verify_local_obstructions.py
python verify_positive_basis.py
python lattice_specialization.py
python verify_dimension_improvements.py
python sign_specialization.py
HN=3 python sign_specialization.py
python verify_gt_hermite_multiplication.py
python verify_sign_fibre.py
python dimension_exponent_compression.py
```

`verify_positive_basis.py` reconstructs each of the 114 elements by standard-T multiplication, converts to the dual-KL basis, checks all integer Laurent coefficients, and verifies rank at v=2 modulo 1000003. Its path differs from `cone_search.py`, which uses the direct dual-KL right action.

`lattice_specialization.py` computes exact Fraction coordinates at v=2. Its counterexample is in the full P-generated order, and a coefficient outside Z[1/2] proves it is outside the proposed lattice. This is a necessary integral test with a decisive failure, not an attempt to infer lattice equality from a successful specialization.

`verify_dimension_improvements.py` checks the actual table against the supplied 132-row JSON. For each new table it runs the supplied symbolic associativity check and a separate asserting integer-polynomial-list check on all 1000 triples, as well as coefficientwise domination/parity and the exact pair score. The script's output JSON contains both entire tables.

`sign_specialization.py` stores the full exact integer basis and trace Gram matrix. Its breadth-first closure proves that its reported image span is closed under every generator; it does not infer dimension from a mere degree cutoff.

## The nonfreeness verifier

`mixed_jet_freeness.py` constructs the full specialized image, using exact additive row reduction over Z/1024 and closure under all P_i and η. The certificate JSON lists 128 words; the compressed companion file stores full triangular module bases. The largest word length is 9, but the proof uses exact algebra closure and therefore applies to the full order in every degree.

`verify_mixed_jet_certificate.py` reconstructs those words as full Laurent polynomials before substituting v=1+η. It verifies the stored triangular certificate and independently computes additive cardinalities using iterative unit elimination and division by 2. The parent verifier `../root/verify_mixed_jet.py` imports none of the branch code, implements the standard Hecke formula directly, and uses global minimum-valuation local Smith elimination. Its independently read output is `../../reviews/mixed_jet_p2_independent_verification.json`.

The correct quotient is M/(2M+ηM), with the maximal ideal acting inside the image module. It must not be replaced by intersection with the ambient maximal-ideal submodule. The exact lower bound 126 is for the abstract fiber of the full integral order; no claim that its dimension is exactly 126 is made.

## Search history and limits

- `cone_search.py` searched the normal forms with no adjacent repeated letter and no 31 through degree ten; its cumulative modular rank reaches the inherited generic dimension 114 in degree nine.
- `triangular_cone.py` attempted positive repairs using a more restrictive ordering and failed. The failed certificate is retained; failure of that restricted repair is not a cone nonexistence result.
- `mixed_cone.py` puts 77 independent positive words first and then repairs the remaining 37 independent words by earlier positive donors. It succeeds with individual donor increments at most five (collected coefficients at most six) and no positive power of D in the corrections.
- `dimension_expand.py` is an unsuccessful first enlarged search. `dimension_expand_fast.py` uses a larger, explicitly finite parameter window; its success establishes examples, not global optimization. Its exact window is printed in the script and certificate.

## Dependencies and source provenance

The following are copied unchanged into `dependencies/`:

- `e4lib.py`: supplied `OURS_E4_scripts/e4lib.py`, standard Hecke and KL arithmetic.
- `consult_a157422a_dimension_ring_verify.py`: supplied `OURS_counting_scripts/`, symbolic table and exhaustive checker.
- `consult_a157422a_dimension_ring_search.py`: supplied `OURS_counting_scripts/`, integer-polynomial arithmetic.
- `dimension_ring_minimal_pairs.py`: supplied `OURS_counting_scripts/`, reduction and score routines.
- `e3_constants.json`: supplied `OURS_counting_scripts/`, all actual rank-three constants.

The generic rank114 was initially inherited and is now independently certified by N015/N017. The rank-three presentation and prior sign-cell computation retain their supplied and primary source credits; exact locators appear in the proofs. The source search found no full rank-four canonical table in the supplied VII/VIII, and no basis identification is asserted. Abedelfatah (2010), Theorem1.3, is the external cancellation input to N004. Parent-agent whole-proof review is tracked separately in `deliverables/reviews/`; numerical replay is not labeled independent whole-proof reading.

## Delivery boundary

An integral A-basis is disproved for the specified full order by N009. The full GT tower has an explicit Q(D) realization in `rational_gt_rank4_verified.json`. The literal external prescription for E(4) fails by N012. Two explicit bar-fixed minimum-degree repairs fail by N017/N018. The changed maximal-scaling construction N019 succeeds on the entire actual rational order, with a full table, but fails signed positivity and is not identified with E(4). A canonical positive dimension ring from the Hecke category remains open. The fixed-q sheaf request is solved for the exact F19/F21/F46 objects and action. Extension-compatible quantum grading and F44's semilinear Frobenius comparison are additional conditions, not unfulfilled requirements of that literal construction.

## Explicitly repaired globalization

`bar_fixed_descent.tex` and `bar_fixed_finite_cutoff.tex` concern an added bar-fixed condition, K=Q(v), rational GT inputs, and a chosen genuine label order. The latter gives an explicit all-degree cutoff and a finite decision procedure at each inductive stage. `viii_label_order.tex` records why the source does not itself supply that order and gives distinct possible repairs. The actual polynomial basis and compact row-operation certificate make the finite module calculations concrete; N-017 executes the full four-element Sprime22 block, and N-018 proves that the same product-path repair fails at the fifth position in thetaSprime31. A different repair would require a fresh precise definition; rational rescaling of the same GT lines does not change this failure.

## Completed alternative and sign fibre

`maximal_scaling_globalization.tex` is a separate main-proof input, not repeated inside `nonstandard_results.tex`. Its114 Hermite vectors are stored in `polynomial_order_gt_hermite.json.gz`; all12996 products are in `gt_hermite_multiplication_table.json.gz`. The complete-table verifier uses the faithful nine-block representation and no triangular division. `N019_literature_scope.md` distinguishes the standard Hermite method from this application and from VIII's different selection rule.

`sign_fibre_structure.tex` specializes that actual free order at D=0. Its full specialized table, both trace forms and ambient matrix are in `sign_fibre_abstract_certificate.json.gz`; the explicit quotient and parabolic section are in `sign_fibre_quotient_certificate.json.gz`. The separate verifier checks all the identities used in the proof. `N020_literature_scope.md` credits the already-known ordinary-specialization radical and rank-three presentation. These files use python-flint; if it is absent from the default Python path, use `PYTHONPATH=/workspace/scratch/e1d2c905d8a8/runtime_nonstandard` for the installed task dependency.

`dimension_degree_cutoff.tex` removes the unspecified degree range from the total-pair minimization problem. Its proof handles all Laurent tables, beyond the earlier cell-parameter ansatz. `dimension_exponent_compression.py` checks the finite compression mechanism and extracts the exact source bounds; it does not run global optimization. The method and its bounded literature search are documented in `N021_literature_scope.md`. Canonical geometric selection and the numerical global minima remain open.
