# KTOWER research ledger

Session start: 2026-11-21 15:30:46 UTC (16:30:46 Europe/Berlin).
Model: GPT-6 Astra Pro; effort setting not exposed.
Input archive extracted exactly once into `input/`.
Snapshot: 2026-11-21, 18:13 UTC. Research remains active.

## Current questions and strongest gates

| ID | State | Result or strongest current gate |
|---|---|---|
| KT-Q1A-U3 | Proved for every positive even e | Total dimension is an explicit cubic quasipolynomial; endoscopic dimension is floor((e−1)/3), stable dimension is its complement, and both Hecke polynomials are determined by integral factorization. |
| KT-Q1A-GL2 | Proved, independently checked | Dimension floor((2e−2)/3), CM dimension 1 exactly when 3 divides e, explicit integral basis and uniform determinant. |
| KT-Q1B | Open, strictly reduced | Source coverage and the closed OneChar implication are discharged. Remaining arithmetic gate: exclude common residual prime support of complete trace determinants, with rational reflection and auxiliary data allowed. A quartic full-order bound is proved; it is not vanishing. |
| KT-Q1C | Open | All-weight trace-unit or equivalent arithmetic prime elimination. No proof of Vandiver. |
| KT-Q1D-26 | Proved: KT-K52-K56-K60-VANISH | Both E=−3 full matrices and GL2 data are verified; two residual E=−7 U3 unit certificates complete, with fresh full replay for the formerly pending large modulus. |
| KT-Q1D-28 | Proved: KT-K52-K56-K60-VANISH | Both residual unit tests and full initial-field independent replay passed; complete arithmetic proof checked. |
| KT-Q1D-30 | Proved: KT-K52-K56-K60-VANISH | All complete initial-field, classical and alternate-field unit reports passed; updated whole arithmetic proof independently checked. |
| KT-Q2 | Proved, checked | Independent character calculation gives 157899; coverage audited against exact source and published local-global statements. An independent endoscopic identification also gives the eigenvalue. |
| KT-Q3 | Proved under stipulated archive convention | Literal nine-arrow application extracted and all nine discharges traced to closed declarations; 706 source files match pinned Git blobs. No Lean build was run. |
| KT-Q4 | Proved with explicit general-source correction | Explicit C7=10^(10^3500), exact Soulé constants transcribed. A counterexample to Soulé's general-field Lemma9 and a safe replacement cutoff are proved; Q-specialization is unaffected. Stronger checked log-order bound <e^4/4 (KT-QUARTIC-QUARTER). |
| KT-Q5 | Open | Actual arithmetic Triple-NV, or a positive-rank substitute, remains missing. All-weight K vanishing would settle this via carried K17-VANDIVER-KERNEL. |
| KT-Q6A | Refuted, checked | Proper genus-two curve over F2 has no F2-point, but its full arithmetic fundamental-group extension splits because Zhat is projective. |
| KT-Q6B | Refuted in unrestricted maximal geometric prime-to-p form; positive refinement proved | Explicit proper hyperbolic polycurve and affine Artin-tower counterexamples; point-separating curve maps yield the valid positive statement, including product embeddings. |
| KT-Q6C | Completed targeted proof/literature review | Marked recognition and unmarked obstruction survive full proof reading at their stated scope. No universal section-surjectivity assertion. |
| KT-Q6D | Proved comparison, checked | Torsion-line family verifies the homotopy injection and gives an instance of F149-RELATIVE, with normal/conormal sign recorded. |
| KT-Q7 | Open, geometric formulation reduced | Pointing over Fbar2 adds no condition; the remaining gate is meeting every primitive doubling orbit in the Raynaud theta divisor for some odd-order torsion point. O5 RM does not yet supply it. |
| KT-Q8 | Completed checked crosswalk | Exact integral/rational motivic dictionary, Faltings letter, Esquisse and cote/scan/run locators recorded and independently reviewed. |

## New proved results relevant to the main gate

- KT-U3-DIM: explicit all-weight total dimension, with the coefficient/Harish–Chandra shift made precise.
- KT-U3-SECOND: independent Reynolds-character computation of 157899, with all 57 cosets accounted for.
- KT-U3-SPECTRUM: all-weight exact finite power-sum/Newton algorithm for the whole characteristic polynomial.
- KT-TRACE-MULTIPLICITY: pairwise nonisomorphic source representations inject into full automorphic systems, so coincident single-prime eigenvalues are counted with sufficient multiplicity.
- KT-QUARTIC-BOUND: |K_(2e)(Z)| divides |N_(e,7)|^2 and log|K_(2e)(Z)| < (2/5)e^4 for positive even e, using the stipulated archive, carried K17 arithmetic comparison, and explicitly the 2-primary input. This does not show N_(e,7) is a unit.
- K17-S17-JOINT rechecked as KT-GLOBAL-RESIDUAL; KT-MULTI-HECKE clarifies the carried joint-operator criterion. These are independent rechecks of an existing gate, not new mathematical progress.
- KT-U3-ENDO-EXACT and KT-U3-SPECTRAL-SPLIT: the endoscopic dimension is proved for every positive even e, and the rank-three source can be restricted to the stable polynomial. Both full proof readings passed; all30 degree–prime factorization checks through e30 at7 and13 pass, including independent character traces.
- KT-K52-K56-K60-VANISH: the requested Q2-HIGHER4 row is fully closed; together with carried K17, all k<=15 vanish. KT-COMPONENT-EXTENSION enlarges periodic character representatives to[-16,15] and proves full-domain Soulé surjectivity in weights27,29,31.
- KT-C7-EXPLICIT: all constants in the seventh-power bound replaced by the displayed finite expression, bounded by 10^(10^3500).

- KT-U3-SYM2-INJECT, KT-U3-SYM2-POLYNOMIAL and KT-U3-SYM2-EISENSTEIN: constructed stable symmetric-square dimension floor((e−2)/6), exact integral factorization, and all-good-prime residual congruences for every prime of the three smaller moduli. The remaining stable factors are units at7 and13; no large-modulus primality is used. KT-ORDINARY-SYM2-ADM3 now verifies actual admissibility; every sigma has a nonunit difference along three infinite progressions whose rational K-components vanish. KT-ADJOINT-ACTUAL-HOST-POINT now proves realization as actual TypeI and TwoPt points on the chosen local component, over an allowed finite coefficient extension.
- KT-STABLE-PROPAGATION and KT-STABLE-LARGE-PRIME: Brauer-character multiplicities force stable congruences in unbounded weights at the fixed prime8361790201; rational reflection kills every corresponding K-component. This rules out uniform ambient stable-unit exclusion without retaining reflection.
- KT-QUARTIC-QUARTER: the exact stable degree improves the bound to log|K_(2e)(Z)|<e^4/4. This remains an order bound, not vanishing.

- KT-ORDINARY-SYM2-GD and KT-ORDINARY-SYM2-EXPLICIT-LARGE: fixed prime697446897311 is independently proved prime and exceeds2^31; all e=26+(ell−1)t satisfy GD, actual Adm3U_s and the full residual congruence, while the corresponding K-component vanishes. This does not force membership in OneChar's existentially selected set.

## Approaches and outcomes

1. Direct source dependency tracing: successful; replaced syntactic closure inference by actual applications.
2. Independent compact-unitary character calculation: successful; a normalization shift was corrected.
3. Full-spectrum multiplicity bound: successful; improved log-order estimate to fourth power without assuming global temperedness of all forms.
4. Fixed-field, two-prime complete Hecke computations: e=26,28,30 complete and arithmetic vanishings proved; all three e32,e34,e36 full7,13 producers and exhaustive two-modulus supports are complete; independent replays are running.
5. Alternate-field residual-ring computation: all six e32,e34,e36 harmonic models and classical unit certificates are complete. Both e32 unitary moduli have complete native full-row unit certificates; the other four are running or queued. Exact initial-field support reduction has now proved the two moduli exhaustive in each degree, subject to completion of the independent full initial-field replays. Native whole-code review, mathematical proof and full e26 control have passed; the original complete Python e32 runs continue separately. No large-modulus primality is assumed. Earlier failed launches are retained.
6. Full stable/endoscopic dimension formula: proved for positive even e. A local full-stabilizer converse and generic multiplicity signs exclude the possible outer-character and three-character parameters. The parity restriction is essential; no opposite-parity formula is claimed.
7. Universal two-field generalized-Bernoulli coprimality: explicit simultaneous obstruction at e=268, ell=661 found; rational reflection removes that instance. The explicit theorem and its checks are complete; the infinite-weight extension at the same prime is also checked (KT-TWOFIELD-FAMILY), and reflection kills every resulting rational component.
8. Geometric section surjectivity and unrestricted higher-dimensional separation: explicit counterexamples found, with narrower valid refinements.

## Timing and durable checkpoints

Checkpoint 01 was created at 16:15:58 UTC and successfully saved; its immutable hash and receipt are in CHECKPOINTS.json. Checkpoint02 was created exactly17:00:46UTC and successfully saved; 1089files, SHA25617113ffbf814df870c52233598aec2c7ddc9fbd205a9250cfdef2e78ae1f6b60. Checkpoint03 was created at17:45:46.072135UTC and successfully saved:1305files,207388776bytes,SHA256934d92019683c733c5bd90361fc551a993ba3b9a5ff79bd198afea1c5e6f6527. Checkpoint04 is due18:30:46UTC; subsequent checkpoints remain at45-minute intervals.
First progress review is due about 18:30:46 UTC; hourly thereafter.
The first progress review occurred at 2026-11-21T18:30:46.000175+00:00. The rediscovery of K17-S17-JOINT is explicitly excluded from new movement. Side-result packaging is not counted as gate movement.
No final status or stop decision has been taken.

## Active work

- Root: full finite computation orchestration, classical uniform model, Soulé comparison, exact motivic dictionary, paper and registers.
- lean_chain: ordinary predicate chain completed; complete native alternate-field certificates and exact cyclic-polynomial audit.
- unitary_audit: actual Type-I host theorem completed; equivariant normalization and strict-Selmer eigensummand length comparison under investigation.
- geometry_tower: field-character reduction and literature scopes completed; renewed O5 route-two incidence work.

## Post-checkpoint02 active gates

- KT-HOST-TANGENT-SIGN, KT-ORDINARY-ON-BASE-COMPONENT and KT-ADJOINT-ACTUAL-HOST-POINT have passed full mathematical proof readings by root and geometry_tower. The proof uses any finite coefficient DVR, generic nonvanishing of the saturator rather than nonvanishing at the base point, a congruently split lattice after ramification, the exact Kill condition and source normalization. Actual CoversPt sets necessarily contain the resulting class. The remaining sign-sensitive length comparison is not proved.
- KT-FIELD-CHARACTER-REDUCTION is proved and independently checked: the exact field-selection gate is simultaneous nonvanishing of B1(chi_D), B1(chi_D omega^e), and B1(chi_D omega^(2e)) at the same D. Wiles, Bruinier and Burungale–Sun were checked at their precise scopes; none of these reviewed statements supplies the required joint assertion. Necessary ordinary congruence exclusion and generic stable exclusion remain separate.
- Hsieh2014 Theorem7.18/Corollary7.20 gives the inclusion direction for constructing congruences from a nonunit special value. The opposite unit-exclusion direction is not supplied by those statements.
- New complete native alternate-field evaluator has passed whole-code review and full e26-small comparison; full independent Python e32 runs continue. This improves computation time without changing the arithmetic criterion.

- KT-CYCLIC-CHARPOLY gives an exact modular-Krylov plus integer-Horner alternative to full Faddeev recursion. Full frozen model checks remain enabled in its replay wrapper. Small controls passed, with incorrect-polynomial rejection and explicit inconclusive behavior for a noncyclic matrix; higher full replays are running.

- Auxiliary two-family attempt: reviewed the Ono–Skinner single-form theorem and the Castella–Liu–Wan addendum correcting almost-all tower nonvanishing. A checked two-variable example (KT-FIELD-SPECIALIZATION-LIMIT) shows why height-one avoidance does not imply integral units at every specialization. No new all-weight arithmetic conclusion follows.


## Post-checkpoint03 checked changes (18:13 UTC)

- KT-K64-VANISH and KT-COMPONENT-EXTENSION-16 are proved and whole-proof checked by root and lean_chain. Both full E−3 replay methods (cyclic and explicit integer Faddeev), both complete E−7 native comparisons, the exact support identity, and all classical data pass. All k<=16 are now proved. The safe periodic interval is[-16,16], with full-domain kappa33 onto. The negative endpoint has not been extended.
- The exact projector and local ordinary component proofs are checked. KT-ODD-CONORMAL-SELMER-EQUIVALENCE proves the actual odd conormal is the Matlis dual of the original strict Selmer group, with equal length. This corrects the earlier proposed sign-sensitive gate: it is an exact reformulation, not arithmetic movement. The finite weight-zero algebra and finite normal module with its surjection are constructed, but flatness and full generic normal support remain unproved.
- KT-RM-FROB-AVOID and KT-RM-FROB-NONDETERMINATION are checked. Arbitrary finite Frobenius data do not force the desired theta incidence for any fixed finite prime support. The all-odd-order route-two gate is unchanged; this side obstruction does not count as arithmetic movement.
- e34: small alternate modulus complete; large determinant and initial full replays running. e36: small alternate modulus complete (all1944 rows); large modulus full rows running, with initial full replays continuing. All nine full classical replays have completed. Running cases are not recorded as certificates.
- New exact conormal framework locator: EGA IV4 Definition16.1.2, independently identified by Stacks01R1; affine formula Stacks01R3, base-change lemma Stacks0473. The Stacks statements and short proofs were read. The original49MB Numdam PDF could not be fetched by the web renderer, so no new primary EGA-page reading is claimed.

The first timed review remains due18:30:46UTC. This update is not that review. Completed K64 is an open-row closure; conormal reformulation, source-boundary audits, numerical acceleration and geometric finite-support obstructions are not counted as all-weight arithmetic movement.


### Subsequent checked closure before review01

At18:21UTC, KT-K68-VANISH and KT-COMPONENT-EXTENSION-17 passed root's entire proof reading and fresh displayed-support/unit arithmetic, following lean_chain's complete review. Both full initial-field replay variants agree and both alternate-field native reports are complete. Thus all k<=17 vanish, the safe interval is[-16,17], and kappa35 is onto. This is an actual open-row closure. The e36 combined gate remains pending.

Root stopped two confirmed-running redundant replays (sessions43090 and97209) after two full reports in each degree had already passed; both exited130 and neither interruption is counted as a passed replay. Logs and the interruption receipt are retained. The required e36 jobs continue.


### Additional checked scope before review01

KT-STABLE-HECKE-SELFDUAL-LOCALIZATION, KT-TRACE-INVISIBLE-SELMER-TANGENT and KT-RESIDUAL-TRACE-DISCRIMINANT passed complete root and independent readings and the six exact Bezout replay. They give an integral Hecke identity and precise missing extension data, not a smaller strict Selmer gate. The Hida–Tilouine/Zhang residual-image hypotheses fail on the actual reducible residual branch.

KT-EXPLICIT-TWO-UNIT-FAMILY passed the complete root and independent proof/source readings, with primitive-character Euler-factor precision retained. For ell≡3mod4 and e≡(ell−3)/2, two explicit quadratic fields give the first two units and either ell-splitting behavior. The third unit and the source exclusions remain open. This partial auxiliary-field theorem does not close the all-weight row; the definite movement for the first review remains the completed finite K-group rows.


## Progress review 01 — 2026-11-21T18:30:46.000175+00:00

Movement: YES. Checked open rows closed: KT-Q1D-26, KT-Q1D-28, KT-Q1D-30, KT-Q1C-NEXT-32, KT-Q1C-NEXT-34. The first review has no preceding no-movement review; streak=0.

The all-weight Vandiver target remains open. The odd-conormal equivalence, finite-normal-module audit, finite-support geometric obstruction, numerical acceleration and packaging are explicitly excluded from movement.

| Open row | State | Strongest current gate |
|---|---|---|
| KT-Q1B | OPEN | All-weight common residual support elimination remains open. Actual ordinary adjoint host counterfamilies persist; odd conormal is exactly the strict Selmer dual, so unit minor is equivalent, not a strict reduction. Actual finite normal module exists, but flatness, full generic support and unit determinant remain unproved; auxiliary-field three-unit condition and necessary exclusions remain open. For ell≡3mod4 and e≡(ell−3)/2, explicit D± supply first two field units with either local splitting; the third unit remains unproved. Trace coordinates are insensitive to the actual Selmer tangent. |
| KT-Q1C | OPEN | All-weight arithmetic prime elimination |
| KT-Q5 | OPEN | Actual arithmetic Triple-NV or a positive-rank substitute |
| KT-Q7 | OPEN_REDUCED | Raynaud-theta incidence with every primitive doubling orbit remains open. Arbitrary finite Frobenius data coexist with avoidance at every exponent of any fixed odd prime support; this is not a counterexample for all odd orders. |
| KT-Q1C-NEXT-36 | OPEN_COMPUTATIONS_RUNNING | Exact two-modulus support and all classical replays complete; small-modulus alternate unitary full report complete; large-modulus full rows and full initial-field replays remain running |

All question rows, including closed rows, are frozen in PROGRESS_REVIEWS.json. Continue; next timed review is19:30:46UTC.

## Checkpoint04 persistence receipt — 2026-11-21T18:34:29.838407+00:00

The immutable checkpoint begun at18:30:46UTC contains1396 files plus its manifest,220022407 bytes. All manifest members were freshly rehashed; every required deliverable is present and no earlier ZIP is included. SHA256: `ea0a83f55d214117fd379db88fe9ae5deb2bd9e682b05b57d9b4a197da62f83a`. Persistence succeeded as `libfile_e8b552fb81dc81918621c8b4c36eac0b`. The next prescribed checkpoint is19:15:46UTC; next progress review19:30:46UTC. This receipt and post-package visual check are retained for the next package; checkpoint04 is unchanged.

###18:36UTC: auxiliary-field finite normalization check

Root whole-read the prefix identity and entire exact code, then freshly recomputed all2270 fields at1135 primes through20000, reconciling the entire saved JSON byte for byte. The exact bounded third-unit conclusion is checked. Since this range is below the already carried2^31 verification, this audit does not reduce the all-weight main gate and is not counted as movement.

###18:37UTC: finite continuation and completed-replay discipline

The complete e36 sum-first initial-field replay passed at18:30:45.701UTC; the alternate large-modulus determinant is still pending, so K72 remains open. A redundant native-Faddeev initial-field attempt was observed running and interrupted with exit130; its log is retained, no complete report claimed. The original-transform cyclic replay continues. Initial native discovery and level-three classical computations have begun for e38 and40; these are open K76/K80 rows, not results.

### 2026-11-21T18:43:30.579589+00:00: K72 whole proof and exact arithmetic checked

KT-Q1C-NEXT-36 is now PROVED by KT-K72-VANISH and KT-COMPONENT-EXTENSION-18. Root whole-read the proof and freshly checked the displayed support identity, every small-prime factor and every determinant/denominator gcd, then reran the complete report reconciliation. The finite range is1<=k<=18, safe periodic interval[-16,18], full-domain kappa37 onto. This open-row closure occurred after review1 and can count at review2. K76/K80 remain open. The third-unit character and p-rational-compositum obstruction proofs also passed root whole-reading and a fresh p59 calculation; these delineate failed approaches without moving the all-weight gate.

### 2026-11-21T18:46:28.000197+00:00: additional full initial-field replay observed

The original-transform cyclic e36 report had completed at18:40:53.824788UTC and was subsequently observed with exit0 and full PASS metadata. It supplies an additional complete initial-field replay beyond the sum-first report used in the frozen K72 proof. SHA256:a2065331a467a77de6b7da37c07b658143af71769db20a1f8eb6f22befdc86cb. The attempted terminal signal after completion did not interrupt it; it is correctly recorded as completed. No new arithmetic row is counted for this redundant verification.


## Auxiliary components and comparison scope — 2026-11-21T18:54:07.864871+00:00

The complete auxiliary Selmer bridge kills only the E-negative components named in AB.6. Its rational positive-root supplement has its own ordinary Bernoulli-unit hypothesis. Root whole-read both proofs. The complete reducible-comparison proofs and the abstract polarized extension-graph proof also pass root and independent readings. A fresh exact graph replay passes. These identify limitations of proposed routes and do not close the rational negative strict-Selmer gate or count as main movement. Both new finite unitary discovery jobs remain running.


## Exact level and literature scope — 2026-11-21T18:56:58.497519+00:00

The all-level admissibility corollary passes root whole reading and an independent literal-source check. The new stable-congruence-cohomology and complex Rankin–Cohen routes retain respectively the unknown arithmetic K-factor and the missing fixed-prime unit condition. These are failed route checks, not main-gate reductions. Checkpoint05 remains scheduled for19:15:46UTC; no unscheduled ZIP has been created.


## Ordinary exclusion gate closed — 2026-11-21T19:09:03.516636+00:00

Whole root and independent proof/source readings establish KT-ORDINARY-RANK2-UNIT-EXCLUSION and KT-AUXILIARY-UNIT-NO-TYPEII. Given actual GD,N=2,psi=1 and the a=2e Bernoulli unit, the actual TypeII point is excluded with no prime-versus-weight bound; no modularity assumption is needed for finite coefficient descent. This removes the previously explicit ordinary necessary-direction requirement from the conditional field strategy. The simultaneous source-compatible field choice and genuine rank3 exclusion remain open. A parity correction is material: the previous explicit two-unit fields have even discriminant, whereas actual GD with evenN forces odd discriminant. An odd-discriminant alternative is under investigation, without a theorem yet. The separate local mixed-path construction leaves the global gate unchanged.


## Odd-discriminant source compatibility — 2026-11-21T19:15:40.102037+00:00

KT-ODD-DISCRIMINANT-TWO-UNIT-FAMILY and KT-ODD-DISCRIMINANT-GD pass complete author, root, and independent proof/source checks. The explicit odd fields now meet all twelve actual GD conditions while supplying the first two units, in the stated progression p=3 mod4. The third unit remains open. This supersedes the preceding under-investigation status.


## Checkpoint05 optional PDF defect — 2026-11-21T19:21:26.270255+00:00

All1544 snapshot members match the manifest and all requested deliverables are complete. The optional KTOWER.pdf was captured during a concurrent compile and is incomplete (2569bytes, no EOF); use standalone KTOWER.tex. The checkpoint remains immutable. The first verification process was interrupted after the malformed-PDF reader stalled, with no completion claimed; a new streaming verification completed every member. Later packaging now requires a completed visual-review manifest binding exact PDF and TeX hashes and checks the complete byte stream before including the optional PDF. This is a packaging defect, not a mathematical result or progress movement.


## Full normalized adjoint branch — 2026-11-21T19:22:12.733035+00:00

KT-ADJOINT-BRANCH-UNIT-EXCLUSION passes whole author, root, and independent checks. The first twisted auxiliary unit excludes all normalized GQ adjoint origins with the exact source hypotheses, including unknown residual quadratic scalar twists. General GQ descent/determinant normalization and genuinely rank3 sources remain separate.


## Checkpoint05 saved — 2026-11-21T19:22:47.697551+00:00

Immutable snapshot created19:15:46.125358UTC;1544manifest members;442207764bytes;SHA256 bf1fa5b7bea7d0bf30a55f6d7fb87a1bc3881a465dc291c59127fc448f605c42. All required deliverables and hashes verified. Saved as libfile_e535a82a2b7c8191b70c03c74d06997a. Optional PDF defect explicitly disclosed; TeX complete. Checkpoint06 scheduled20:00:46UTC; hourly review2 remains19:30:46UTC.


## Progress review 02 — 2026-11-21T19:30:46.000231+00:00

Movement: YES. Prior open rows now closed: KT-Q1C-NEXT-36. Consecutive reviews without movement:0. The all-weight target remains open. The conditional ordinary TypeII exclusion removes a previously explicit needed direction; reformulations, side obstructions and packaging do not count.

| Open row | State | Strongest current gate |
|---|---|---|
| KT-Q1B | OPEN | All-weight residual-prime elimination remains open. A genuine conditional branch exclusion is now proved: with actual GD,N=2,psi=1 and B1(eta omega^(2e)) a unit, no actual TypeII point exists; the a=e unit excludes the specified ordinary rank2 seeds, with no prime/weight bound. Remaining field route: simultaneous suitable units for an auxiliary field within actual GD, then control of the genuinely stable rank3 sources and mixed extension products. The original explicit D±=−4sf(p±2) supply two arithmetic units but fail GD odd-discriminant condition. Actual ordinary host counterfamilies, Selmer/conormal equivalence and lack of independent integral extension bound remain as documented. The new odd discriminants D±=−sf(p±4) repair this parity obstruction and supply two units plus actual GD in the specified progressions; their third unit and genuine rank3 exclusion remain open. The a=e unit now excludes the full specified normalized GQ adjoint branch, recovering and removing any residual quadratic scalar twist; unclassified adjoint origins and genuine rank3 remain outside this theorem. |
| KT-Q1C | OPEN | All-weight arithmetic prime elimination |
| KT-Q5 | OPEN | Actual arithmetic Triple-NV or a positive-rank substitute |
| KT-Q7 | OPEN_REDUCED | Raynaud-theta incidence with every primitive doubling orbit remains open. Arbitrary finite Frobenius data coexist with avoidance at every exponent of any fixed odd prime support; this is not a counterexample for all odd orders. |
| KT-Q1C-FURTHER-38 | OPEN_COMPUTATIONS_RUNNING | Initial discovery and exact two-modulus support complete; initial full sum-first replay running; both alternate native full-row jobs running; all three classical model replays complete. No arithmetic vanishing proof yet. |
| KT-Q1C-FURTHER-40 | OPEN_COMPUTATIONS_RUNNING | Initial discovery and exact two-modulus support complete; initial full sum-first replay running; alternate model preparations and classical calculations running. No completed unitary certificate or arithmetic vanishing proof yet. |

All question rows are frozen in PROGRESS_REVIEWS.json. Continue; next review20:30:46UTC.


## Self-dual source gate reduced — 2026-11-21T19:37:24.369696+00:00

Whole author, root and independent proof readings pass scalar normalization, self-dual automorphic descent, its unit exclusion, and the essential-selfduality reduction. The exact ordinary flag is read from the original source, not inferred merely from potential crystallinity. With actual GD,N2,psi1 and the three auxiliary units, only stable rank3 actual sources that are not essentially self-dual can remain. This removes a specified class from the conditional field strategy, while uniform simultaneous units and the remaining stable exclusion stay open. The odd-family rational-mirror scope proof also passes; that family already kills its rational component by carried quadratic reflection and is not counted as new component movement.


## Low-order component restriction — 2026-11-21T19:41:37.153967+00:00

The complete new application proof KT-SMALL-ORDER-COMPONENT-REDUCTION passes root reading after correction of the displayed quartic bounds to the exact non-strict primary inequalities. The known class-number theorems remove rational character orders1–4; remaining order is at least5. The class-number results themselves are cited and not claimed new. A secondary description of degree6 was not promoted without the primary theorem. The separate elementary monomial/finite-projective-image exclusion also passes whole root and independent reading; it adds source scope, not a new Selmer bound.


## First global mixed obstruction — 2026-11-21T19:46:44.015209+00:00

Whole author, root and independent proof/source readings pass KT-AUXILIARY-CLASS-UNIT-MIXED-CUP and KT-GLOBAL-QUADRATIC-MIXED-PERSISTENCE. The class-number unit removes the global mixed cup obstruction and supplies the ordinary correction through second order over a characteristic-p Artin algebra. A hypothetical nonzero strict negative class is not contradicted. No higher lift, characteristic-zero source or Selmer bound follows. This is a failed quadratic-obstruction route and does not count as main movement.


## Nonquadratic auxiliary fields constructed — 2026-11-21T19:51:45.606097+00:00

The final326-line Jacobi proof passes author, root and independent whole-proof/source review. The heat lift, odd-theta extraction and elliptic Sturm bound produce odd fundamental D prime to p with |D|<4p and two auxiliary units under the explicit rational Bernoulli seed. All actual GD clauses are checked. The automatic e=(p+1)/2 progression for p3mod4 has full-order odd mirror, so it is distinct from the previously controlled quadratic-mirror example. Applying the construction at2e+1 separately excludes actual TypeII in its own stated family. No same-discriminant pair of twisted units or remaining generic rank3 exclusion is claimed.
