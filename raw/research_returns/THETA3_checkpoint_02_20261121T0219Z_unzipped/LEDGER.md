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

At the time of the preceding entries, no checkpoint or formal review had fallen due. The dated events below supersede that earlier working status. No result depending on Masullo has been used.

## Checkpoint 01 — 2026-11-21 01:34:40 UTC

The first scheduled checkpoint was created and saved under the new name `THETA3_checkpoint_01.zip`. SHA256: `6ff6fb8a1626ab8e56859698321869de6d442a5a1aaa1c1c416555b01667a68a`. It contains no earlier checkpoint. The next checkpoint is due at02:19:30 UTC. This event is not the three-hour formal progress review.

## Further substantive movement — 01:34–02:16 UTC

- Q1 narrowed from an unspecified global seesaw to the actual `MainX` family and its last two-lift law. Global Witt index zero forces the direct Bessel rank to zero; the abstract m=2 model permits one active ball signature and removes intermediate ValX/LocFin conditions. Its exact kernel/covolume matching, source representations and arithmetic links remain. A5 is now fully checked. A7 makes the independent wedge a genuine single theta lift through a finite-rank kernel and a Riesz representative; it also identifies exactly when that natural source is totally definite. Alternate compact local models under changed splitting data are being checked.
- Q1/Q2 all-rank gate closed: A6 proves direct balanced2n-factor CM cycles on an n-ball using Liu's exact componentwise theorem in every rank, full Gaussian spanning and divisor contractions. Q10 gives the n! determinant norm, all-rank finite grid and local Bessel constant1. Canonical node gaps remain1, so rank stabilization alone does not solve the separate concrete tower gate.
- Q2 arithmetic projector gate closed: Q9's resultant construction passed independent whole-proof checks. B14 identifies the exact coherent-power versus ordinary-cohomology distinction and the positive diagonal contraction when opposite Hodge factors are supplied.
- Q3 source gate materially enlarged: C12's degree500 non-CM period passed independent checks. C15/C16 now give dense torsion-branch hyperelliptic source families and infinitely many pairwise nonisogenous non-CM elliptic Albanese factors in finite covers of one fixed ball surface. An explicit new j-polynomial and a cover of degree≤36 are checked by exact arithmetic. Two-factor periods have positive integral degree≤2000.
- Q3 target gate narrowed: C13 gives an explicit algebraic projector onto a Weil space; one nonzero projected cycle spans the rational Weil space under its quadratic multiplication. C14 proves that the known curve-product factorizations miss this space in the generic divisor-rank1 case. C15 identifies a precise conditional source-universality reduction over Qbar and the countability limit over C; neither is represented as a solved exceptional Hodge case.
- Q4 integral-frame gate narrowed: C11 now has the sharp uniform constant1 via the Katz trace ideal and an actual normalized reduced-theta nonintegrality example. C18 proves integral tame theta quotients by cancellation of a common sigma factor, with an explicit algebraic prime-to-p isogeny pullback. The remaining raw-section connection is specified as Dq/q, rather than left unnamed. C17 states the actual horizontal-correspondence/specialization criterion with exact EGA/SGA source locators.

No three-hour review is due before03:49:30 UTC. None has been recorded. Current open rows remain in QUESTIONS.tsv; packaging is not counted as substantive movement.

### 02:17 UTC: further reduction of Q1

B15 passed an independent entire-proof and source check. The canonical local representations have compact rank2 neighbors with explicit splitting exponents; compatible infinity exponents globalize as Hecke characters with finite ramification. The exact adjacent-rank GQT criterion is nonzero local lifts at every place plus a holomorphic nonzero completed L-value at1. Universal lastLaw/seeLast statements provide the analytic last-step identity once its data exist. The remaining gate is now the prescribed canonical representation/vector in that two-lift image and the explicit ClsK.Core/ClsT kernel-covolume equations and arithmetic links. Reverse first-occurrence/pole criteria are being examined next.

### 02:19 UTC: integral theta gate moved again

C18 now proves a positive valuation slope for actual tame translated-sigma tensors of any integer degree: max(0,n/(p²−1)−s_p(n)/(p−1)). The degree-zero case retains the sharper C11 slope. The proof uses the explicit integral rational function D²logq, parity, Bell polynomials and invariant-derivation nilpotence, and passed two independent entire-proof checks. This does not identify the archive's covariant derivative with the stronger raw-frame estimate; it gives a concrete bound while leaving the exact connection match visible.
