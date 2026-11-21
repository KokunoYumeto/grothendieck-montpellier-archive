# THETA3 ledger

Run THETA3-20261121. Work began 21 November 2026 at approximately 01:49 Europe/Berlin (00:49 UTC).

This ledger records results actually reached; it does not count restatement or packaging as progress. Checkpoints are due at 45-minute intervals from this start. The first formal progress review is due after about three hours, then hourly.

## Initial gates

| Question | State | Strongest current gate |
|---|---|---|
| Q1: exact machine and sketch 1.7 | Open | Identify actual pairings and determine a matching theorem, including characters, inner forms, test vectors and measures. |
| Q2: explicit non-vanishing | Open | Fix all scalar normalizations; quantify the Gaussian and compact-variation construction, and test whether definite positivity supplies missing constants. |
| Q3: non-CM sources | Open | Identify the rational Hodge sources of the constructed degree-one forms and test a replacement outside the CM subcategory. |
| Q4: integral models | Open | Identify good-reduction specialization and exact local arithmetic intersection theorem; compare its hypotheses with the analytic construction. |

## Source boundary

The ZIP was unpacked once. It contains the papers and two short Lean entry files, a text scan and a secondary Lean map; it does not contain the full Lean source tree named by the map. No Lean build has been run. Grothendieck archive scans and text of record are not attached. Alpöge's stated RH and Dirichlet GRH are carried as cited background as instructed. Masullo's claims will be conditional if used.

## Events

- 01:49–01:56 Europe/Berlin: source inventory, PDF extraction, independent examination of 032, Alpöge and non-CM/integral routes.
- Source observation: 032 §§4.5–4.7 use Taylor tensors, Gaussian concentration and continuity; a Rallis or Bessel identity is not stated there. The literal version of 1.7 therefore requires a precise additional matching statement. This is a source observation, not a refutation of an unspecified possible comparison.

## Substantive movements before the first scheduled review

The following are research events, not the three-hour formal review. Times are Europe/Berlin; detailed proof events are kept separately.

- 01:56–02:08: Exact 032 and van Hoften–Sempliner character, signature, splitting, doubling and CM-extraction dictionary established. The rank-three ball group's totally definite inner-form comparison was reduced to explicit local signature/scalar-type constraints. A1 proves the signature-independent averaged zero-orbit identity; Q1–Q6 quantify compact variation, Gaussian tails, rational approximation and normalized extraction. These replace unqualified positivity with named constants.
- 02:08–02:14: Public mirror source recovery narrowed the archive gate. Entry files match the attachment hashes; no Lean build or complete primary-archive hash verification was performed. The actual local Bessel definition gives B9, normalized value1 on the canonical coefficient type of U(2,1). The initial global matching candidate has a different rank/signature range (B10), so it is not a direct rank-three specialization.
- 02:10–02:15: Q7 replaces the existential finite translate by an explicit finite unipotent grid and Gaussian-seminorm Lipschitz certificate. Q8 supplies a pointwise-to-global norm bound. Independent whole-proof checks passed. This genuinely reduces the quantitative gate: the remaining constants are specified input data, rather than an unspecified choice of translate.
- 02:12 onward: A new global route uses a totally definite U(2) subgroup inside the original U(2,1), preserving the original Hermitian space. B11 gives the restriction-theta seesaw; B12 gives a nonzero global Bessel coefficient and a finite-mass lower bound. A5 is being developed to recover the full ball pairing from finitely many such restrictions with a positive correction operator. Its algebraicity is not assumed.
- Source gate further reduced: the exact step12 mechanism has been located in the mirror's `Development/AbelianVarietyTheory/Definitions/LatticeFrames/ValLastX.lean`, including iterated up/down operators, normalized periods, and a relation-preservation statement uniform in the character tuple. Its applicability to the 032 data is under examination.
- Non-CM gate reduced: C01 identifies the obstruction at every standard congruence ball level. C03 constructs a genuine non-CM/CM mixed period on a common cover of Schoen's noncongruence surface and an appropriate 032 congruence surface. C04 isolates the remaining projector/rank requirement for a genuinely exceptional non-CM Hodge summand; C05 explains why this first example alone is not a new Hodge-conjecture case.
- Integral gate reduced: C06 gives an explicit negative derived intersection and C07 an exactly positive sector, so the relevant signs and lattice hypotheses are now explicit. C11 derives the exact height-two derivative slope appearing in Alpöge step2 from integral formal coordinates, improving the earlier reciprocal-quasi-canonical-index observation. Matching the raw theta normalization remains a named hypothesis.

No scheduled checkpoint or three-hour progress review has yet fallen due. No result depending on Masullo has been used.
