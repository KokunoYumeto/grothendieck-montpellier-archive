# Reflection-free source barrier

`bireflection_section.tex` contains full proofs D-BI-01–07.

The new remaining gate, for the eight non-Eisenstein class-number-one fields, is a dominant nonsplit finite-cover source with exact character field K, coefficient degree at least fifteen, reflection-free image, and no inducing complex representation of dimension one, two or three. This is an exclusion of smaller sources, not a claimed construction or an algebraicity theorem for the remaining determinant classes.

The proofs include the actual intermediate-cover period factorization for two- and three-dimensional blocks, the published primitive bireflection classification with every scalar/tensor case handled, all low-degree imprimitive block budgets, and the final rank-seven real-normalizer exclusion. The intermediate inducing field is not silently identified with K.

Run the exact certificate with:

```
python check_bireflection.py
```

It checks retained U5(2) generator/form data and the arithmetic budget tables in under one second. The written proofs supply the universal statements. See `SOURCES.md` and `CHECK_EVENTS.tsv` for exact premises, provenance, review scope, and source-access limitations. The full external papers are kept under `sources/` or the central research source directory, rather than included as authored deliverables.

## Scalar alternating and symmetric inducing blocks

`scalar_standard_section.tex` contains the separately reviewed full proof D-BI-08. It excludes dominant nonsplit sources induced from any deleted standard representation whose image satisfies A_n ⊂ J ⊂ C* S_n, n ≥ 4, with arbitrary scalar image. No direct-product assumption or initial equality of the inducing cyclotomic field with K is made. The proof identifies an actual cyclic Prym variation, controls its rational multiplicity, and verifies the actual polarization.

Root completed a whole-proof audit and separately checked the generalized scalar alternating extension, including scalar projection, point-stabilizer surjectivity, multiplicity one, and the larger inducing-field issue. The original D-BI-01–07 section remains a separate reviewed integration unit. Imprimitive independently completed whole-proof audits of D-BI-01–08, including the generalized scalar alternating case.

## Essentially self-dual inducing blocks

`essential_selfdual_section.tex` contains full proofs D-BI-09–10. If an inducing representation is primitive and essentially self-dual, degree at least nine forces degree at least twenty-four for a dominant nonsplit sixfold source, even when the inducing character field is larger than K. This includes scalar-real and symplectic-similitude representations. The proof includes all factorwise projective tensor cases and does not assume that the inducing image itself is reflection-free. For an original primitive exact-K representation, uniqueness of the bilinear multiplier also forces even degree outside Q(i) and Q(omega).

Root read both entire proofs and recorded PASS. `python check_essential_selfdual.py` checks every degree9–23 budget and every tensor factorization, the exceptional symplectic budget, and the first degrees not ruled out by the inequalities. It certifies only these arithmetic statements; the full universal proof is in the TeX, and satisfying a budget is not asserted to construct a source.

`NIELSEN_PEER_AUDIT.md` records our separate whole-proof audit of the imprimitive agent's exact per-Nielsen algorithm. Its independent finite example is retained as `nielsen_peer_example.json`; the unbounded model enumeration was not executed.

## Four-dimensional inducing blocks

`rank_four_inducing_section.tex` is the reviewed D-BI-11. It excludes inducing dimension four for K=Q(sqrt−7), Q(sqrt−11), Q(sqrt−19), Q(sqrt−43), Q(sqrt−67), Q(sqrt−163), in arbitrary original coefficient degree. For the remaining non-Eisenstein class-number-one fields Qi and Q(sqrt−2), the inducing character field must be a specified biquadratic field strictly larger than K. Every remaining intermediate branch profile is ten reflections and two rank-two inertias outside the reflection normal closure. Root and imprimitive completed whole-proof audits; root also independently reread the exact Cohen statements and reran the field checker.

`check_rank_four_fields.py` and its JSON give31 exact cyclotomic cases in five model fields. Every quadratic-field inclusion is checked by an exact polynomial square witness modulo a primitive element's minimal polynomial. The written proof supplies exhaustiveness; the script is not a classification or a group enumeration.

`rank_four_real_boundary_section.tex` is the separately reviewed D-BI-12. Root and imprimitive completed whole-proof audits; imprimitive also read the exact published Lewis–Reiner statements and the complete pair-extraction corollary proof. The new graph-monodromy argument removes the real rank-four reflection groups even when L is larger than K, by producing a maximal isotropic space over the original K. Among the eight non-Eisenstein class-number-one fields, only G29/G31/G32 with the specified larger cyclotomic fields remain. It is kept separate from D-BI-11 as its own reviewed integration unit.

## Reflection-free inducing images and ramification bounds

`large_prime_inducing_section.tex` is the reviewed D-BI-13. For K=Q(sqrt(-p)), p=7,11,19,43,67,163, every inducing representation of a dominant nonsplit sixfold source is reflection-free, in every original degree and with arbitrary inducing character field. The p=7 case is included by the exact repeated-eigenvalue bound. Root and imprimitive completed whole-proof audits; imprimitive freshly checked the Cohen normalizer/classification and Malle model-field inputs.

`scalar_unramified_section.tex` is the reviewed D-BI-14. If an inducing image is contained in scalar multiples of a finite group defined over a number field unramified at p, its degree is at least 7(p-1). The model field need not be Galois. The general moving-rank-q bound is (5q-3)(p-1). For primitive tensor-indecomposable inducing images, `scalar_unramified_radical_section.tex` gives the stronger D-BI-14a bound (p-1)(25(p-1)-22)/4, namely 192,570,1926,10794,26862,163134. Root read both entire proofs and independently reopened the full published Guralnick–Saxl theorem and its exceptional-case reduction. These remain necessary lower bounds, not existence thresholds.

`python check_scalar_unramified.py` checks all displayed integer bounds, the p=7 reflection-containing contradiction, and every smaller possible q in the radical bound. The universal field and geometric arguments are proved in the TeX.

## Forced symmetry of larger-field induction

`inducing_symmetry_section.tex` is the reviewed D-BI-15. A nontrivial inducing-field conjugation realized in the subgroup normalizer gives a nontrivial automorphism of the rational intermediate base preserving its genuine branch divisor. For R branch points its period rank is at most floor(R/2)-1. This excludes normal inducing subgroups and unique imprimitivity systems in the remaining R=12 larger-field cases. Root read the entire proof, including the algebraic block-projector and Galois uniqueness argument, and recorded PASS. Nonnormal subgroups with nonunique systems are explicitly left open.

`E8_INDUCING_FIELDS_PEER_AUDIT.md` and `RANK_FIVE_PEER_AUDIT.md` record our independent whole-proof checks of the parent E8 larger-field reduction and the sibling G33 reduction. Their separate exact checkers rebuild all 112 E8 class words and eight scalar-phase cases, and independently check the G33 scalar-field and exponent calculations. Neither report claims a new dominant larger-field source.

## Six- and seven-dimensional inducing blocks

`rank_six_seven_section.tex` contains the fully reviewed D-BI-16–17. Among the eight non-Eisenstein class-number-one fields, degree six leaves only K=Q(i), L=Q(zeta12), and J=mu4 G34. Its eight necessary moving-rank profiles have twelve to fourteen genuine branch points. The proof supplies the exact outside rank-three and rank-four spectra and the necessary square-isogeny condition over the original K. The all-embedding signature restriction also forces the inside rank-two age to be one and outside rank-four age to be two in the twelve-branch (3,4) row. Degree seven is excluded. Root and imprimitive completed whole-proof audits; the exact checker passes all thirteen field cases, eight profiles and seven residual pairs.

## Character ratios and the normal core

`character_ratio_section.tex` proves D-BI-18 and D-BI-18a. A character bound c on a normal subgroup acting irreducibly gives the exact necessary inequality 12 ceil(e(1−c)/4) ≤ 2e+6 for a rank-nine sixfold source, allowing outer inertia. The published Lie-type bound in Duyan–Halasi–Podoski, Theorem4.1(2), p141, excludes every inducing degree at least ten when the defining field has size at least47. Scalar-only extensions are excluded altogether at field size at least29. An irreducible extraspecial core is excluded in every degree at least five. The essentially self-dual refinement excludes primitive nonsplit inducing degrees at least nine at Lie field size at least19. `check_character_ratio.py` independently records the exact ceiling arithmetic; it is not a group classification. Imprimitive completed a whole-proof and primary-source audit with an independent arithmetic reconstruction.

`normal_core_section.tex` proves D-BI-19 directly over C. In the primitive factorwise tensor-indecomposable case, every nonscalar normal subgroup acts irreducibly. An abelian minimal normal quotient gives trace zero and is excluded in degree at least five. The remaining minimal normal quotient lifts to an irreducible central product of quasisimple groups, permuted transitively by the whole group, so the character bounds apply to the total inducing degree. The proof does not apply a finite-field maximal-group theorem outside its hypotheses. Tensor-factor permutations are retained. Root and imprimitive completed independent whole-proof audits; both PASS events are recorded separately from the author derivation.

The D-R5-04 appendix to `RANK_FIVE_PEER_AUDIT.md` records the complete geometric component audit, a fresh rerun of the original 51840-element group enumeration, and a genuinely independent eighty-class local-form calculation in `audit_g33_local.py`. The paired component is excluded; no universal Nielsen transitivity is asserted.


## Lie fields from29 through43

`lie_small_fields_section.tex` is the full D-BI-20 proof, with separate `lie_small_fields_bibitems.tex`. In a dominant nonsplit sixfold source, a primitive factorwise tensor-indecomposable inducing block of total degree at least10 with Lie-type core must have defining field size at most27. Published projective minima first reduce the six remaining fields to a single PSL2 factor; q37 is removed by exact degree/ceiling disjointness, q29/32 by full-cover inverse conjugacy, and q31 by the class-inverting diagonal automorphism and scalar-only normalizer bound. Larger inducing fields are allowed. `check_lie_small_fields.py` passes exact arithmetic; the full universal proof is in the TeX. Root completed a whole-proof and primary-source review and reran the exact certificate, all PASS. Imprimitive also completed a whole-proof/source audit and an independent arithmetic reconstruction, PASS.


`SPORADIC_CORE_PEER_AUDIT.md` records the independent whole-proof audit of D-SPOR01–03. `audit_sporadic_input.py` independently checks all38 published-table inputs and473972 nonscalar entries, using rational trace norms for row selection and Ramanujan sums for exceptional Fourier multiplicities. The full normalizer and tensor-permutation proofs pass.


`SPIN_CORE_PEER_AUDIT.md` records the full independent audit of root HD-SPIN01a/b. `audit_spin_inputs.py` checks the complete five small-cover inputs, local2.A6 character ratios, and the exact nonreal degree24 exception in2.A8. The corrected full certificate passes; its initial auxiliary expected-list error is logged explicitly.

## Full rank-one Lie-core exclusion

`a1_core_section.tex` contains the complete new D-BI-21a–c and D-BI-21. It excludes every PSL2(q) normal core for a primitive tensor-indecomposable inducing block of degree at least five in a dominant nonsplit Weil sixfold source. The original field is any imaginary quadratic field, and the inducing field may be larger. All compatible outer automorphisms and tensor-factor permutations are included. At small q, degree at least six is excluded without a determinant hypothesis. The only exceptional degree-five core reduces to the already reviewed deleted A6 representation theorem.

The finite input comprises 33 complete ATLAS character tables, with every character row, power map and core fusion retained under `a1/`. The author GAP scan and the independent Python Ramanujan reconstruction both pass: 654 selected rows and 18,922 nonscalar entries, four quarter-bound exceptions and no fifth-bound exception. The Python run independently selects the restriction rows and checks the complete table inventory and all19 fusions. Run `python check_a1_spectra.py`; rerun GAP from the workspace root with the retained `a1/export_and_scan.g`. The exact input SHA and source provenance are in the proof and source log. Root completed a whole-proof and primary-source audit. Imprimitive independently completed a whole-proof/source audit and reconstructed all33 tables,654 rows and18,922 spectra in a separate arithmetic implementation. Both reviews passed; their exact scopes are recorded separately.

## Suzuki and Ree cores

`twisted_lie_section.tex` contains the fully reviewed D-BI-22a/b and D-BI-22, with `twisted_lie_bibitems.tex`. Every irreducibly acting normal central product of Suzuki, small Ree, large Ree or Tits quasisimple factors is excluded from a rank-nine finite-cover sixfold source. Mixed factor types, all compatible outer automorphisms and tensor permutations are covered. No primitive, tensor-indecomposable, essentially self-dual, nonsplit-polarization or inducing-field-equality assumption is needed.

The exact finite input comprises five complete published character tables. The exceptional Suzuki cover and its outer extension are retained in full; the other small groups use exact character trace bounds, which pass to every outer normalizer by the proved commutator inequality. The large-field bound and published minimum degrees finish all three infinite series. The complete GAP run and independent author Ramanujan reconstruction pass213 selected rows,1,330 Suzuki spectra and14,141 trace bounds. Root completed a whole-proof/source/code audit and an actual verifier rerun. Imprimitive completed a whole-proof/source audit and its own polynomial-Fourier reconstruction. All passed. Run `python check_twisted_lie.py`; data and GAP export are under `twisted_lie/`.

`SYMPLECTIC_WEIL_PEER_AUDIT.md` records the independent whole-proof and primary-source audit of the sibling D-SPW01–03. `ORDINARY_ALTERNATING_SMALL_PEER_AUDIT.md` records the independent whole-proof/input audit of root HD-ALT02, including all49,650 spectra. Their independent arithmetic programs and outputs are retained beside the reports.

`LOCAL_QUANTIZATION_PEER_AUDIT.md` records the complete SF-E819/E819R review, including the freshly read published Buchweitz–Flenner composition theorem and the independently computed full256-coordinate example. `ALTERNATING_STANDARD_TENSOR_PEER_AUDIT.md` records the complete D-AST01–03 review and independent seven-case endpoint arithmetic. Both pass; their precise source and computational scopes are recorded separately.

`ORDINARY_ALTERNATING_SHARP_PEER_AUDIT.md` records the whole HD-ALT03 proof audit, including split constituents and the all-degree content inequality. Its independent certificate checks8,788 partitions and390 exact commutators; the universal proof passes separately.

## Linear Weil normal cores

`linear_weil_section.tex` contains D-BI23a/b/23. Imprimitive completed a whole-proof/primary-source audit and an independent complete spectrum reconstruction; both passed. Root review is separately pending. It excludes every transitive normal core of general-linear Weil factor representations PSL_n(q), n≥3, for a rank-nine sixfold source, allowing all field sizes, compatible outer automorphisms, scalar phases, factor permutations and larger inducing fields. Either determinant is allowed. The proof uses explicit function-space trace bounds and the previously proved actual intermediate-cover budget. The only new finite endpoint is SL3(4)degree21; all six complete published tables pass24rows/1288spectra with moving rank at least8. Run `python check_linear_weil.py`. The initial metadata-only assertion failure is retained in the event log. No unitary or non-Weil linear-family claim is made.

`CURVILINEAR_QUANTIZATION_PEER_AUDIT.md` records the whole SF-E820 proof audit. Its independent exact program checks the universal formal mixed-wedge identity and the full256-coordinate rank32 balanced example. Both proof and computation pass; arbitrary Artinian modules remain outside scope.

`G2_TRIALITY_PEER_AUDIT.md` records the whole D-G2T01–03 review, fresh official source verification and a genuinely independent original-expression parser. All9,242 generic inequalities and11,502 small-group spectra pass; the report preserves the published classification-input boundary.

`ORDINARY_ALTERNATING_THREE_QUARTERS_PEER_AUDIT.md` records the complete HD-ALT04 review. Its independent symbolic and partition certificate passed28,121 partitions with27,425 eligible shapes; the all-degree proof is checked separately. The theorem requires transitivity and imaginary-field containment, and excludes all shapes with maximum row/column at most three quarters of n.

`ORDINARY_ALTERNATING_LONG_ROW_PEER_AUDIT.md` records the complete HD-ALT05 review and its independent exact symbolic/tail certificate. The universal proof and all332 finite tails passed.

## Unitary Weil normal cores

`unitary_weil_section.tex` contains D-BI24a/b/24. The author and imprimitive independent whole-proof/source audits passed; root review is separately pending. The exact all-characteristic source domains were freshly rechecked and explicitly annotated. The complete seven-table GAP scan and separate exact Python reconstruction passed17rows/754spectra. All transitive ordinary unitary Weil cores reduce to a single PSU4(2) factor of degree5 or6; the existing SPW04 result removes6 in the main non-Eisenstein nonsplit scope. No non-Weil or mixed-core assertion is made. Run `python check_unitary_weil.py`; full inputs/exporter are under `unitary_weil/`. The initial unsupported metadata call is retained honestly in the log.

EVEN_SYMPLECTIC_PEER_AUDIT.md records the whole D-ESC01–03 proof/source review and the independent complete4549-inequality/3442-spectrum reconstruction. COUPLED_SURFACE_PEER_AUDIT.md records the whole SF-E822 review and the independent first-jet/exterior certificate. Both pass with their stated source and geometric scopes.
