# Parts B/C status at 2026-11-19 08:43 UTC

All results marked proved below have independent root audit recorded in CHECK_EVENTS.tsv.

## Part B
- B-RD1–3: explicit odd-prime counterexamples; explicit p=3 e=2 curve; ordinary full-p assertion proved.
- B-RD4–6: Lead B′ refuted by the logarithmic cyclotomic extension; height-one index is 0; all-prime finite-level character counterexamples.
- B-RD7–11: complete first-level elliptic ramification ranges, including wild defect 12 at p=3, and precise cyclotomic-field answer.
- B-RD12–13: exact all-level tame elliptic ranges and least forcing level for potentially good elliptics (all p>=5; tame defects at p=3).
- B-RD14–16: all-dimensional cyclotomic bound; literal unrestricted least forcing level is vacuous; explicit lower bounds for general-height character determination.
- B-RD17: an explicit finite universal upper bound for character determination exists for every prime and height, directly for the manuscript filtration condition; no potential semistability of the whole representation is assumed.
- B-RD18: formal Honda height-two constructions give nonzero lower bounds for every admissible absolute ramification and every height at least two, including p=2. Height one has sharp index zero for every prime. The quadratic p=2 full-character detour was rejected and is not asserted.
- B-RD19: additive reduction with full rational odd-prime torsion is necessarily potentially good, clarifying the two parts of the higher-level question.
- B-RD20: at p=3 the maximum primitive formal torsion valuation is divisible by 3 for a wild defect. This gives a sharper necessary higher-level wild range and the exact minimum absolute index 2*3^(2n-2) over all additive full-3^n examples. Independent parent and obstructions/crystals audits passed.
- B-RD21: the fixed-e p=3 largest additive full-torsion level is reduced to at most two adjacent integers, with an exact arithmetic characterization of the exceptional band. Its four full9 exceptions are resolved by B-RD23; B-RD26/27 now realize the upper endpoint in every exceptional band.
- B-RD22: at p=2,e=1 and every height at least2, even M[4] does not determine the odd-order inertia character. Explicit elliptic E versus split good BT group; both independent audits and exact finite certificate passed. Thus the least B4 index is at least2 in this smallest ramification case.

- B-RD23: complete full9 additive range at p3 is 6|e and e>=18. All examples occur over explicitly constructed finite local fields; the formerly unresolved e=24,30,42,48 examples all have defect12. Both independent audits and exact symbolic certificate passed.

- B-RD24: explicit finite Witt-coordinate algebraic decision test for the entire elliptic additive full-p^n existence question, with bounded minimality and exact Hensel lifting; parent proof/source audit and independent exact polynomial rerun passed. The test has not been evaluated at (3,216,3); the complete numerical range is instead proved independently by B-RD26/27.

- B-RD25: a ramification-nine base change of an e24 full9 additive example cannot yield full27; proof and exact certificate independently passed. This closes that construction route, not direct existence.
- B-RD26/27: every wild p3 bound is sharp, for all n and defects3,6,12. Exact trace invariant, regular weighted chart and faithful descent prove existence; the all-elliptic least potentially-good level is N_w+1. In particular e216/full27 exists. Parent complete proof/source/certificate audits passed.

- B-RD28: stronger p3 character lower bound N_w in every height>=2; parent audit passed.
- B-RD29: explicit B9 versus Tate9 comparison proves leastnu>=2 already p3,e2, and every e=2mod4; parent complete proof/source/code audit passed.

Remaining B gates: the optional potentially good dimension >1 least level; general-height B4 exact threshold (finite existence now proved); The corrected Fontaine dictionary is now primary-source-complete and audited; Lead B′ as stated remains false.

## Part C
- C-RD1: proper schematically dominant BT Hom descent proved; original non-noetherian rigidity overstatement corrected by C-RD2.
- C-RD3–5: exact p-nilpotent reduction criterion; nonreduced positive example and explicit mixed-characteristic dual-number negative example.
- C-RD6: normal noetherian extension theorem, without excellence.
- C-RD7–9: local-system effectivity on reduced geometrically unibranch bases, on reduced bases with local finite surjective geometrically unibranch covers, and invariance of effectivity for a specified local system under nilpotent reduction.
- C-RD10: explicit countable noetherian reduced infinite-node counterexample to unrestricted local-system effectivity; nonreduced counterexample by adjoining a square-zero variable. Thus C4 normal YES, arbitrary reduced NO, arbitrary NO; finite-cover hypothesis (a) gives YES.
- C-RD11: full C2 reduced assertion REFUTED, even for a reduced geometrically unibranch one-dimensional local domain satisfying (a),(b), ordinary elliptic generic fibre and split BT group. The obstruction is visible modulo 5. Normalization is not finite. All ring and finite algebra claims proved explicitly.

- C-RD12: exact relative essential-image criterion across a specified nilpotent thickening once a reduced realization is given, using the actual completed lift and its punctured overlap. Parent proof and primary-source audits passed.

- C-RD13: exact absolute essential-image criterion on every locally noetherian base via a closed-locus abelian seed, its canonical Serre--Tate tower, actual models on completions, actual BT-compatible punctured overlaps, and compatible quasi-affine atlases. Necessary and sufficient data do not quantify the original S-realization. Parent proof and original-source audits passed.
- C-RD14: elliptic specialization removes the formal-algebraization and atlas gates using the canonical degree-three line bundle and proper formal existence. Parent proof and original-source audits passed.

No remaining Part C gate. Automatic effectivity is not asserted: the exact criterion retains explicit completion and overlap conditions, and C2 is refuted even for a reduced geometrically unibranch base satisfying (a),(b).

## Manuscript documentation
F_BC_manuscript_quotes.tex records short French quotations for B1–B4 and C1–C4 with cote:scan and manuscript page references, explicitly checked against supplied transcriptions rather than fresh original scans.

C_absolute_image.tex supplies the audited C-RD13/C-RD14 criteria. Original EGAIII1 5.4.1/5.4.5 and Moret-Bailly1.1/1.2 were read by both this agent and the parent.

## Later B4 sharpening (19 November 2026, 09:58 UTC)

- B-RD30 PROVED: universal sufficient manuscript index2h² floor(log_p(peD/(p−1))) via original Bondarko A/B and audited B17 refinement.
- B-RD31 PROVED:2≤ν_min(3,2,2)≤4. At levels27 and81 every possible character mismatch must compare two whole potentially supersingular groups; filtered height-one comparisons are excluded at27 by the new rational-formal-torsion bound. Parent and OC complete independent proof audits passed.
- B-RD32 CANDIDATE: the81 test further reduces to inertia orders(12,3) or(12,6), joint image36; the27 test requires norm-one distinct tame quotient orders and joint image>9. Independent audits requested.
- The exact least B4 index in height≥2 remains open; no finite-elimination computation has been claimed to decide it.

- B-RD32 now PROVED: parent and obstructions-crystals full proof audits passed. The level-81 test reduces exactly to type12 versus3/6 with joint36; finite auxiliary certificate PASS0.050076540999725694s. Exact least index remains open.
