# JAC1964 dated ledger

Run: JAC1964-20261121. Model: GPT-6 Astra Pro; effort setting not exposed.
Started UTC: 2026-11-21T00:51:37Z (21 November 2026, 01:51 Europe/Berlin).

## Rules and provenance

The attached prompt is the task specification. The archive was unpacked once.
Attached 032, van Hoften–Sempliner, Milne, and Alpöge statements are accepted as cited inputs, as requested; their complete proofs and Lean dependency archive are not independently certified in this run.
New deductions require complete proofs and recorded whole-proof checks. Missing gates remain explicit.
Checkpoint interval: 45 minutes; first due 01:36:37 UTC. First movement review due 03:51:37 UTC, then hourly. No checkpoint is created before its due interval.

## Open questions at intake

| ID | State | Current gate | Assigned |
|---|---|---|---|
| Q34 | Open | Construct primitive signed incidence duality and prove its ampleness using 032 Cor. 8.4 on products of abelian varieties; identify the intended quotient | root |
| QH9a | Open | Admissible extensions and exact function-field height normalization including singular fibres | h9_height |
| QH9b | Open | Identification of cycle quotient, height pairing, and injectivity modulo trace | h9_height |
| Q35 | Open | Algebraically trivial height comparison; justified analytic sign and applicability of Alpöge steps 5,13 | arithmetic_sign |
| QPROG | Open | Exact status of Th.1–7 and next theorem | programme_audit |

## Events

- 2026-11-21 00:51 UTC: Intake, extraction, three parallel mathematical investigations.
- 2026-11-21 00:53 UTC: Source check establishes that cote 44 scan 8 explicitly requires primitive decomposition; scan 4 assumes algebraic triviality, stronger than H9 homological triviality.

- 2026-11-21 01:06 UTC: Q34 reduced to a complete drafted curve-test proof (JAC-T4.1–3), awaiting full independent reading. H9(a) refuted by a split quadric pencil; both singular-fibre corrections calculated. Th6 critical fixed-part equality has a cycle-spread/blowup proof drafted by programme agent.

- 2026-11-21T01:34:01+00:00: Whole-proof review completed for JAC-P00–06, H9-T4/T5 and the new all-primes monodromy argument H9-L1/L2/T6. The variable sign gate closes under explicit generic monodromy hypotheses; combined with fixed-part positivity, this extends primitive Th4 to generic ample sections of abelian varieties.
- Arithmetic gate movement: AR-1 removes all primitive grades >=2 from the sign problem; AR-2 splits off an actual positive Picard Chow summand for CM varieties. AR-7 places an explicit nonzero Fermat-quartic Ceresa class in a rank-two complementary motive. AR-8 is being checked and computes its height through Gross–Schoen local invariants.
- No three-hour review has yet fallen due. Work continues; checkpoint creation is scheduled for01:36:37UTC.

- 2026-11-21T01:36:37+00:00: Scheduled45-minute checkpoint01 created. Research continues. Next checkpoint due02:21:37UTC.


## Checkpoint 02 update (2026-11-21 02:21:37 UTC)
New checked results since checkpoint 01: JAC-T4.4 actual primitive algebraic representative of an abelian threefold; JAC-T4.5 arbitrary-field descent; H9-T6a automatic variable monodromy; JAC-P07 automatic condition A for abelian pencils; H9-T7 full geometric-height decomposition; H9-T8 full semipositivity for abelian fourfold pencils; JAC-P09 geometric-generic degree-at-least-three axes; H9-T9 algebraically trivial incidence height and trace radical; H9-T10 actual algebraic representative of the generic threefold; JAC-P10 exact Fermat Faltings-height difference log(2)/4; AR-11 unconditional positive Fermat L-derivative; AR-12 exact theta reduction; AR-13 independently reviewed IEEE/Arb certificate proving the specified Fermat Ceresa height greater than 1/100. Full positivity on all CH(N) remains unproved. AR-13 is a reproducible numerical certificate under stated arithmetic assumptions, not formal verification. The latest individual proof fragments and per-agent check logs are authoritative for additions not yet integrated into the manuscript. The manuscript assembly will be refreshed immediately after this scheduled checkpoint. No stale compiled PDF is included.

## Live gate update 2026-11-21T02:50:58.188641+00:00

Q7-finite CLOSED by JAC-P15: accepted032 Tate plus Kahn2003 gives rational Chow=numerical, hence numerical=tau, for every geometric abelian-type variety over finite fields/Fbarp. Root and arithmetic whole-proof checks passed. This is an actual open-row status change.

Q35-full strictly reduced by AR-15 to the complementary Griffiths quotient for semipositivity, with its algebraically trivial subgroup proved to lie in the radical. Strict positivity also requires that subgroup zero. JAC-P11–14 identify a positive Q(i)-line and prove its entire abelian-endomorphism orbit cannot enlarge it. AR-18 gives the exact effective sum/difference surface-height comparison; the comparison remains open.

H9-T11/12/13 are checked: elliptic-product reduction, finite-base-change orthogonal decomposition, and generic-last-section odd complete intersections. New separable norm-zero cycles and the arbitrary fixed-axis form remain open. Castella standing conductor restriction caught and corrected; no unsupported Selmer-rank claim remains.

No scheduled three-hour movement review has yet fallen due. Current status of every treated question is in QUESTIONS.tsv. Next checkpoint03 due03:06:37UTC; first review03:51:37UTC.

## Gate closures 2026-11-21T03:04:19.716548+00:00

H9-T14 closes the constant finite-field full homological-domain height question and customary numerical=tau after arbitrary extension of those constants. JAC-P16 proves B(X) for geometric abelian-type varieties and extendsTh6. AR-19 proves the specific Katz nonvanishing by exact mod5 arithmetic; H9-T15 gives the conductor-correct Selmer rank-one implication. Root whole-proof checks are recorded. The next arithmetic gate is scalar-extended Abel–Jacobi injectivity or a direct real-height argument on the remaining Griffiths quotient. No Chow-rank conclusion is inferred from Selmer dimension.

- 2026-11-21T03:06:37Z: Scheduled checkpoint03 created immutably and persisted (Library ID libfile_230551e3f750819193e5a83ba81fa79e). ZIP SHA256 2eed39ee76cdf1d10307bdd79f6391542a1898d8472a63139203a2a42a1b6f16. Contains109-page paper and all current authored proof/check/calculation documentation. Next checkpoint04 and first movement review both due03:51:37UTC.

## Exact-field and primitive-scope update 2026-11-21T03:31:16.681418+00:00

JAC-P17 and AR-16a resolve the Fermat fields and reduce the sufficient full-Chow gate to scalar-extended Abel–Jacobi injectivity overQ; the equivalent Q(i) statement has no hidden field assumption. AR-15a isolates a possible algebraic-radical obstruction in grade-zero CH2 on B times J. AR-20 refutes finite-fibre detection: every good finite specialization ofN vanishes. Vial's Murre theorem was source-checked and does not close these gates.

H9-T8a closes every fixed axis in characteristic zero by classical Hodge–Riemann. H9-T16 proves survival and rational operational-Chow gluing in a corrected semistable degeneration, but refutes lifting by the proposed fixed-elliptic parameter under its explicit generic-monodromy hypotheses. The higher fixed-axis gate remains in positive characteristic.

AR-21 reduces every rational odd class, over its original number field, to a scalar multiple of the Ceresa class of one geometrically integral curve. AR-22 supplies a complete symmetric divisor-Hodge-index bound on that curve test; it does not orient the needed sum/difference comparison. These new full-proof readings are logged. No scheduled movement review has yet fallen due.

## Finite-cover counterexample and regulator image 2026-11-21T03:37:07.222199+00:00

QH9-finite-sep changes from OPEN to REFUTED without primitive qualification. H9-T17 constructs a smooth elliptic double-cover model of an E4 pencil, unramified above every critical value, and an exact norm-zero cycle z=hD with height−12d³. The repaired threefold group splits orthogonally into the Albanese-primitive domain (semipositive in characteristic zero by Zhang) and the negative Picard Lefschetz part modulo trace. Root whole-read and primary source checks passed. This is actual main-question movement.

AR-23 proves the known positive eta realizes the full one-dimensional Selmer target overQ, and eta,Teta realize the two-dimensional target overQ(i). The remaining arithmetic sufficient gate is the kernel of the explicitly split scalar-extended regulator. The splitting is overQ5 only and gives no unproved rational or real-height decomposition.

## Further exact reductions 2026-11-21T03:47:03.118027+00:00

H9-T18 strictly reduces the positive-characteristic threefold-cover sign to the algebraic variable middle subspace ker(k_*) of the smooth incidence fourfold. Every fixed term and the algebraic cohomological primitive correction are proved; both directions of the reduction are checked. AR-25 gives the full Fermat sign as16 explicit normalized triple intersections attached to a tensor projector, with exact positive factor1/(16DM²). Its sign is a stated instance of the still-additional Zhang tensor positivity conjecture. P18 confines the algebraic-radical obstruction to a curve-times-J fourfold component. Root complete-proof readings are recorded.

## Scheduled movement review 01 — due 2026-11-21T03:51:37Z

Recorded at 2026-11-21T03:54:58.466181+00:00. This is the first review, against the intake gates and all subsequent proved reductions. **Movement: YES. Consecutive reviews without movement: 0.** Next review due 2026-11-21T04:51:37Z.

Counted movement: Q34 closed by JAC-T4.1–5; QH9a/b refuted in their original scope, with corrected height theorems; QH9-full4 and the characteristic-zero fixed-axis row closed; QH9-finite-sep refuted by the all-characteristic H9-T17 counterexample; H9-T18 strictly reduces the primitive positive-characteristic cover problem to its variable algebraic middle form; Q35 is reduced to grade one and its complementary Griffiths quotient, with the Fermat instance further reduced to an explicitly split regulator kernel over Q (AR-16a/23) or the exact tensor form (AR-25); Q7-finite and Q7-constant closed; Th6 extended to geometric abelian type. Packaging, numerical re-runs and source-audit restatements are not counted as movement.

### Main gates at this review

- **Th4 / Q34:** proved on the primitive incidence quotient for abelian varieties over arbitrary fields in every characteristic. The unqualified common-sign whole-middle statement is refuted (P03).
- **H9(a),(b):** original claims refuted; repaired admissible height and incidence statements proved in the explicitly listed scopes. Remaining fixed-axis gate: signed primitive algebraic middle form in positive characteristic, axis dimension at least four. Remaining primitive threefold-cover gate: nonnegativity on Alg2(X) intersect ker(k_*), by the checked equivalence T18. Unrestricted cover positivity is false by T17.
- **Arithmetic sibling:** the algebraically trivial incidence sign is known under the cited comparison hypotheses. Full primitive positivity still requires the complementary Griffiths sign; the Fermat sufficient gate is scalar-extended Abel–Jacobi injectivity over Q, whose target and image are both exactly known. Direct sign gate: the projected Gross–Schoen / sixteen-tensor intersection form in AR24–25. Possible algebraic radical is detected on the P18 curve-times-J fourfold component. Bost still needs the actual comparison map and norm bound.
- **Seven-theorem programme:** precise incidence versions of Th1–3; primitive Th4; corrected/scope-limited Th5; Th6 under B(X), now including geometric abelian type; customary Th7 false in general but proved over finite constants in the stated scopes. Next work attacks the primitive-cover variable form and the full arithmetic complementary motive.

### Every unresolved or conditional row at review

| ID | State | Exact current gate |
|---|---|---|
| QH9-axis | OPEN | H9-T7: signed primitive algebraic intersection form on the fixed axis in positive characteristic, m>2; H9-T8a closes every characteristic-zero axis. |
| QH9-products | PROVED CONDITIONAL REDUCTION | H9-T11: curve-correspondence proof gives positivity modulo numerical equivalence; D needed separately for cohomological strictness |
| Q35-full | OPEN | AR-1 grade-one reduction; AR-2 actual orthogonal Picard Chow summand; AR-15 reduces complementary semipositivity to its Griffiths quotient; strictness also needs algebraic radical zero |
| Q35-GRH | PROVED CONDITIONAL IMPLICATION | AR-4/5: real self-dual analytic sign plus applicable height identity with correct positive constants and local terms; Dirichlet GRH alone is insufficient |
| Q35-Bost | OPEN | AR-6/10 give exact height line and slope criterion; comparison map and norm bound missing. AR-18/21 reduce the threefold sign to effective sum/difference surfaces of one integral curve; AR-22 divisor-Hodge-index bounds are symmetric and do not orient the comparison. |
| QFermat-tautological | REDUCED; GENERATION OPEN | JAC-P12: Teta outside ordinary tautological ring; JAC-P14: entire endomorphism orbit remains exactly the known CM plane |
| QFermat-full | OPEN | AR-15: semipositivity reduces to Griff2(N). P17 reduces the full Q(i) height to V_Q. AR-16a supplies a sufficient single remaining injectivity gate overQ; strictness still needs the algebraic radical zero if pursued directly. |
| QFermat-Selmer | OPEN | AR-19, H9-T15 and P17 give exact dimensions1 overQ and2 overQ(i). AR-16a reduces the remaining sufficient gate to scalar-extended Abel–Jacobi injectivity overQ; injectivity is equivalent overQ(i). |
| Qnext-Newton | PROVED CONDITIONAL CRITERION | H9-T5: a slope outside [m-1,m] forces variable incidence zero under irreducibility; existence of a witness remains unproved |
| QFermat-AJ | OPEN | AR-16a/23: the regulator V_Q tensorQ5 onto the one-dimensional Selmer line has explicit section eta; remaining gate is kerAJ=0, equivalently overQ(i); no known real-height factorization through this kernel. |
| QFermat-algradical | OPEN | AR-15a and P18: a nonzero class gives a homologically trivial nonzero degree-four component on the fourfold C timesJ; componentwise cycle-class injectivity/MurreD there would suffice. Equivalent Jacobian-product grade-zero obstruction retained. |
| Q35-divisor-index | PROVED BOUND; SIGN UNRESOLVED | AR-22: full one-parameter family gives a symmetric absolute bound on the height; it is invariant under reversing the cubic sign and does not imply the required orientation |
| QH9-cover-primitivep | OPEN | H9-T18: equivalent to semipositivity of the intersection form on Alg2(X) intersectker(k_*:H4(X)→H6(A4 timesC)); all fixed terms and the cohomological primitive correction are proved in every characteristic. |
| QFermat-fourfold | PROVED CONDITIONAL REDUCTION | P18: a nonzero algebraically trivial N-class gives a nonzero homologically trivial cycle in (pi1C tensorpiN)CH2(C timesJ), fixed bypi4; injectivity on this component/MurreD for these fourfolds would kill it |

A conditional reduction is distinguished from a proof of its hypothesis. The original unrestricted questions already refuted are not silently reopened. Work continues on the repaired questions.

## 2026-11-21T04:25:26.835759+00:00 — New cover gates and canonical-point reduction

H9-T19/T19a establish the exact norm-height identity on moving tame cyclic covers and the full geometric-generic rational-map space in degree prime to the characteristic. T20 treats positive-genus Kummer covers, including every generic hyperelliptic genus in characteristic not2, with both fixed and variable cohomology accounted for. T21 closes every rational degree in every characteristic through an Artin–Schreier Fourier calculation and actual lisse-kernel tower. T22 treats the simple-pole wild genus strata and uses a full rank-two algebra parameter space to close every generic hyperelliptic genus in characteristic2. Thus the remaining primitive-cover variable form is restricted to special covers and other scopes not covered by these vanishing theorems. These are strict scope reductions, not a claim that specialization is surjective on algebraic cycles. Root and independent agent whole-proof checks are recorded.

AR26 proves the complete canonical Hermitian-divisor constraint symmetry; this rules out the specified larger divisor-index route but does not orient the height. AR27a/b supplies a new exact restriction of the full Fermat testing problem: it suffices to use curves with an actual rational canonical marked point mapping to zero. A ramified double cover preserves the original number field; projected modified diagonals pull back with factor1/4 and their heights with factor1/2. The remaining projector and arithmetic sign are retained.

The scheduled next movement review remains04:51:37UTC. The above new generic-cover closures and canonical-point reduction will be assessed against the first-review baseline; this unscheduled mathematical update does not reset the review clock.

## 2026-11-21T04:32:41.414911+00:00 — Cubic families and the canonical diagonal metric

H9-T23 proves the exact norm-height formula for explicit cubic cover families of every genus at least2 in every characteristic. T23a composes with the rational-cover towers to obtain degree2M in every positive genus and degree3M in every genus at least2. These are actual family statements; no irreducibility assertion for full Hurwitz spaces has been substituted. Root whole-proof checks passed.

AR28 gives the exact canonical-metric nef cone δ1δ2>=g²t² and its Jacobian PSD plus base-line representation. The specified Vojta big metrics outside this range remain non-nef after every base shift; complex curvature detects the obstruction. Exact point-metric constants are retained. This closes the proposed substitution of shifted bigness for nefness; the larger Jacobian mixed terms remain to be tested and are not identified with the already symmetric E3 cone. Root and programme whole-proof/source checks passed.

## 2026-11-21T04:37:19.099355+00:00 — Scheduled checkpoint05 persisted

Created exactly04:36:37.008313UTC, the fifth45-minute boundary. JAC1964_checkpoint_05.zip includes all six required root deliverables, the170-page compiled manuscript, authored proofs and documentation;173 content files plus two manifests,17,490,746bytes. SHA256 c3fffbd49e4b6c6347e11b12a0cba8c6eeb7c2900a8695111105e5c5003bd630. Persisted as libfile_7bb5f2bf2d0c8191953942087401c10e. Earlier checkpoints were neither overwritten nor nested. Next checkpoint05:21:37UTC; next movement review04:51:37UTC.

## Hourly movement review 2 — due 2026-11-21T04:51:37+00:00

Recorded 2026-11-21T04:51:37.000991+00:00. Movement: **YES**. Consecutive reviews without movement: **0**.

### Mathematical judgment

The previously open positive-characteristic primitive-cover gate QH9-cover-primitivep is strictly narrower: H9-T19–T22 eliminate all new algebraic middle classes for every geometric-generic rational-cover degree and every generic hyperelliptic genus in every characteristic; H9-T24 closes the full generic triple-cover space for every genus at least2. The remaining sign problem is confined to special covers and other parameter scopes. These are exact norm-height and radical theorems, not a restatement of the same variable-form reduction. AR-27 also proves an equivalent full Fermat test restricted to parametrized curves with a literal canonical marked point. The additional obstruction/source/layout checks are not counted as movement.

A text difference, an added side result, proof checking, and packaging are not themselves movement. The stated mathematical reason is the criterion used.

### Main questions and strongest current gates

- **Q34 — PROVED:** JAC-T4.1–3; T4.5 arbitrary-field descent; 032 Cor8.4
- **QH9-axis — OPEN:** H9-T7: signed primitive algebraic intersection form on the fixed axis in positive characteristic, m>2; H9-T8a closes every characteristic-zero axis.
- **QH9-cover-primitivep — OPEN:** H9-T18: equivalent to semipositivity on Alg2(X) intersectker(k_*:H4(X)→H6(A4 timesC)); T19–T24 kill this new algebraic space for every generic rational degree, every generic hyperelliptic genus, full generic triple covers g>=2 in every characteristic, and specified cyclic/composite families. Special-cover and other parameter-scope variable classes remain.
- **Q35-full — OPEN:** AR-1 grade-one reduction; AR-2 actual orthogonal Picard Chow summand; AR-15 reduces complementary semipositivity to its Griffiths quotient; strictness also needs algebraic radical zero
- **Q35-Bost — OPEN:** AR-6/10 give exact height line and slope criterion; comparison map and norm bound missing. AR-18/21 reduce the threefold sign to one curve. AR-22/26 prove the canonical Hermitian-divisor constraints are sign-symmetric; AR-28 rules out replacing nefness by shifted Vojta bigness. Full-Jacobian diagonal mixed identities remain a separate test.
- **QFermat-full — OPEN:** AR-15/P17: semipositivity reduces to the rational complementary Griffiths quotient. AR-25/27 give an equivalent projected-diagonal sign test on parametrized curves with a literal canonical marked point. AR-16a/23 alternatively reduce sufficiency to kerAJ5=0 overQ; the algebraic radical remains for strictness if pursued directly.
- **QFermat-AJ — OPEN:** AR-16a/23: the regulator V_Q tensorQ5 onto the one-dimensional Selmer line has explicit section eta; remaining gate is kerAJ=0, equivalently overQ(i); no known real-height factorization through this kernel.
- **QFermat-algradical — OPEN:** AR-15a and P18: a nonzero class gives a homologically trivial nonzero degree-four component on the fourfold C timesJ; componentwise cycle-class injectivity/MurreD there would suffice. Equivalent Jacobian-product grade-zero obstruction retained.
- **Q6 — PROVED UNDER B(X):** JAC-P00–02 underB(X); P08 for specified products; P16 for every geometric abelian-type variety, in every characteristic.
- **Q7 — REFUTED IN GENERAL:** JAC-P05: CM Fermat-quartic Jacobian in characteristic0, using Bloch Th4.1; true for divisors and zero-cycles

### Every unresolved or conditional row at review

| ID | State | Current gate |
|---|---|---|
| QH9-axis | OPEN | H9-T7: signed primitive algebraic intersection form on the fixed axis in positive characteristic, m>2; H9-T8a closes every characteristic-zero axis. |
| QH9-products | PROVED CONDITIONAL REDUCTION | H9-T11: curve-correspondence proof gives positivity modulo numerical equivalence; D needed separately for cohomological strictness |
| Q35-full | OPEN | AR-1 grade-one reduction; AR-2 actual orthogonal Picard Chow summand; AR-15 reduces complementary semipositivity to its Griffiths quotient; strictness also needs algebraic radical zero |
| Q35-GRH | PROVED CONDITIONAL IMPLICATION | AR-4/5: real self-dual analytic sign plus applicable height identity with correct positive constants and local terms; Dirichlet GRH alone is insufficient |
| Q35-Bost | OPEN | AR-6/10 give exact height line and slope criterion; comparison map and norm bound missing. AR-18/21 reduce the threefold sign to one curve. AR-22/26 prove the canonical Hermitian-divisor constraints are sign-symmetric; AR-28 rules out replacing nefness by shifted Vojta bigness. Full-Jacobian diagonal mixed identities remain a separate test. |
| QFermat-tautological | REDUCED; GENERATION OPEN | JAC-P12: Teta outside ordinary tautological ring; JAC-P14: entire endomorphism orbit remains exactly the known CM plane |
| QFermat-full | OPEN | AR-15/P17: semipositivity reduces to the rational complementary Griffiths quotient. AR-25/27 give an equivalent projected-diagonal sign test on parametrized curves with a literal canonical marked point. AR-16a/23 alternatively reduce sufficiency to kerAJ5=0 overQ; the algebraic radical remains for strictness if pursued directly. |
| QFermat-Selmer | OPEN | AR-19, H9-T15 and P17 give exact dimensions1 overQ and2 overQ(i). AR-16a reduces the remaining sufficient gate to scalar-extended Abel–Jacobi injectivity overQ; injectivity is equivalent overQ(i). |
| Qnext-Newton | PROVED CONDITIONAL CRITERION | H9-T5: a slope outside [m-1,m] forces variable incidence zero under irreducibility; existence of a witness remains unproved |
| QFermat-AJ | OPEN | AR-16a/23: the regulator V_Q tensorQ5 onto the one-dimensional Selmer line has explicit section eta; remaining gate is kerAJ=0, equivalently overQ(i); no known real-height factorization through this kernel. |
| QFermat-algradical | OPEN | AR-15a and P18: a nonzero class gives a homologically trivial nonzero degree-four component on the fourfold C timesJ; componentwise cycle-class injectivity/MurreD there would suffice. Equivalent Jacobian-product grade-zero obstruction retained. |
| Q35-divisor-index | PROVED BOUND; SIGN UNRESOLVED | AR-22: full one-parameter family gives a symmetric absolute bound on the height; it is invariant under reversing the cubic sign and does not imply the required orientation |
| QH9-cover-primitivep | OPEN | H9-T18: equivalent to semipositivity on Alg2(X) intersectker(k_*:H4(X)→H6(A4 timesC)); T19–T24 kill this new algebraic space for every generic rational degree, every generic hyperelliptic genus, full generic triple covers g>=2 in every characteristic, and specified cyclic/composite families. Special-cover and other parameter-scope variable classes remain. |
| QFermat-fourfold | PROVED CONDITIONAL REDUCTION | P18: a nonzero algebraically trivial N-class gives a nonzero homologically trivial cycle in (pi1C tensorpiN)CH2(C timesJ), fixed bypi4; injectivity on this component/MurreD for these fourfolds would kill it |

### Documentary comparison

Changed existing rows: Q35-Bost, QFermat-full, QH9-cover-primitivep.
New question rows: QH9-cover-cyclic-generic, QH9-cover-rational-generic, QH9-cover-positive-genus, QH9-cover-rational-all-degrees, Q35-hermitian-index, QH9-cover-wild-positive-genus, QFermat-canonical-point, Q35-canonical-diagonal-nef, QH9-cover-cubic-genus, QH9-cover-composite-genus, QH9-cover-triple-generic.
These lists are audit data, not an automatic movement test.

Next scheduled review: 2026-11-21T05:51:37+00:00.
The two-flat-review stopping threshold has not been reached.

## 2026-11-21T05:07:54.329813+00:00 — T25 and full-Jacobian arithmetic review

Whole-proof readings passed H9-T25, AR-29a–g and JAC-P19. T25 proves a strict further generic-cover scope reduction: full generic degree N>2g−2 covers with N even (allg>=1) or divisible by3 (g>=2), every characteristic. Exact old/norm-kernel height and radical identities hold. AR29 identifies surviving Picard data and a scoped selective sign symmetry; P19 excludes only abelian rational domination. Those obstruction checks are not independently counted as movement. Direct primary EGA, Deligne–Mumford and Stacks locators checked. Next mandatory review remains05:51:37UTC.

## 2026-11-21T05:21:19.596323+00:00 — elliptic triple covers and finite-field axis test

H9-T26 passed the root whole-proof read, with the global constant Radon split and rank-r twisted-coefficient nodal monodromy checked. It proves the full generic genus1 degree3 norm-height/radical theorem in every characteristic. H9-T8b passed root and programme readings: the remaining fixed-axis sign is equivalently tested on axes and cycles over finite fields by smooth proper specialization. P20 proves an actual abelian cohomology injection; its stronger positivity corollary remains explicitly conditional on Milne2022Proposition4.2, whose cited form-transfer justification was not re-established in this audit. Newly authored source files are included in the scheduled snapshot; integration into the next assembled paper is ongoing.
