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

## Checkpoint 02 — 2026-11-21 02:19:31 UTC

The second scheduled checkpoint was saved as `THETA3_checkpoint_02.zip`, 6,999,965 bytes, 100 members. SHA256: `e5ef06dfa6e76a9bc86778a1f77fdda01dc538a187f5d62ff6f46ae76567705e`. Persistent file id: `libfile_bd3601f5597081918e81facc62d66440`. It contains no earlier checkpoint. The next checkpoint is due at03:04:30 UTC. This is not a formal progress review.

## Substantive movements — 02:31–02:45 UTC

- Q1 analytic gate closed in an exact corrected form: B17 realizes the actual A7 wedge as the literal double theta lift V3→P2→V3 through the adjoint kernel, with one positive inverse Q⁻¹ common to every character for fixed spaces/kernel/levels. The universal LastLaw/SeeLast then gives its actual definite-U2 Bessel identity. A5 recovers the whole mixed pairing from finitely many such coefficients. The upper space is explicitly rank4, signature(3,1) everywhere; the arithmetic totally-definite MainX comparison is still separate. Both root and theta agent checked the full proof and conventions.
- Q1 reverse coherence gate reduced by B16 to a precise standard-L-function pole with local signature hypotheses; the conclusion constructs coherent finite forms. The pole is not asserted for an uncomputed canonical packet.
- Q4 canonical-jet gate reduced by A8: the 032 completed Taylor series is the matched Appell–Humbert reading. A direct exponential-adjoint argument extends chart independence to every jointly harmonic polynomial, including the actual different-type product determinant. Tangent/tensor conjugation and factorials are explicit. On a CM elliptic factor the conjugate quadratic ambiguity is zero.
- Q4 artificial-coordinate gate removed by C19: the actual good-reduction CM formal group has the sharp strong integral-function derivative bound without a polynomial multiplication coordinate. A deRham CM eigensplitting proves e2* integral and supplies the weak bound for actual reduced theta tensors; equal-degree tame ratios retain the strong slope. Full independent proof/source checks passed.
- Q3 source gate enlarged by C20 in final proof checking: a genus-two Jacobian with geometric endomorphism ring Z is a quotient of a ball-cover Albanese of degree≤1764. Independent arithmetic implementations reproduce its two reductions overF37 and F37². This is a simple non-CM source of dimension2; the exceptional Weil-cycle extraction gate itself remains.

The first scheduled formal progress review is still due at03:49:30 UTC.

### 02:58–03:00 UTC: further main-gate movement

- Q2: Q11 proves a direct lower bound for the geometric ball norm from definite period squares with explicit chart/mass/frame constant, eliminating the unknown ball Gram upper bound. The full proof passed root and independent definite-agent checks.
- Q1: B18 reduces alternate definite rank2 realizations to a three-entry real deletion table and exact local packet data. Under the stated unitary base-change hypotheses, a cuspidal GL2 source gives a unique character and inner form; the endoscopic case leaves at most three global character candidates. The equal-rank alternative has a precise central-value test.
- Q4: C21 proves the actual split/inert higher-dimensional CM formal decomposition and strong mixed bounds for integral canonical theta ratios. C22 settles the stronger single-section extension negatively: actual normalized theta sections atp7 andp5 have exact valuation subsequences attaining the weak slope. The arbitrary raw strong extension is no longer an undecided gate. No claim about an unmatched archive theorem is made.
- C20 full independent proof and two arithmetic certificate checks passed. Its endomorphism ringZ and coverdegree1764 are now checked findings, not pending proposals.

These are research events; the first formal review remains due03:49:30 UTC.
