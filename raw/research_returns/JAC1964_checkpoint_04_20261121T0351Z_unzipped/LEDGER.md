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
