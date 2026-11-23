# C44_POS final research package

## Final status — research stopped 22 November 2026

Scheduled Review 9 was recorded at **10:14:05.058251 UTC**. Reviews 8 and 9 both recorded **NO additional movement**, so the governing two-consecutive-NO rule requires stopping research and delivering this final record. The quaternion developments were counted once at Review 5, and the canonical ramified-lifting developments once at Review 7; their later refinements were not used as staged clock resets. Stopping does not turn an unresolved question into a theorem.

**The universal fixed-axis sign is not proved or refuted. No wrong-sign algebraic axis class was found. Unrestricted lifting of primitive axis classes and the Fermat scalar Abel–Jacobi injection remain open.**

| Original objective | Final state |
|---|---|
| Fixed-axis sign, JAC1964 QH9-axis | Open beyond the checked residual-one, extending orthogonal/totally-real, and actual quaternion correspondence criteria. Explicit closed families in every characteristic satisfy the required sign. |
| Lifting primitive axis classes | Selected sufficiently ample prescribed-centre examples exclude every abstract model with e≤5 at p=3 and e≤3p at the constructed primes p≥7, p≡3 mod4. The p=5 result e≤10 requires a separately supplied nonliftable centre. Arbitrary ramification remains open. |
| Special covers | The stated generic splitting/conductor strata and the geometric lifting problem are handled. Arbitrary closed special covers with new algebraic trace-kernel classes remain open. |
| Fermat AJ5 and full arithmetic height positivity | Open at C44-F07: actual finite generation of the specified projected discrete étale-motivic group. Rank-one completion, the F25 descent identification, and the square-zero CM radical do not prove injectivity. |
| Cote 16 scans 049–050 beyond abelian varieties | Corrected conditions and positivity are verified on the stated explicit families. The requested historical initially-unknown-I status is not certified. |
| Characteristic-p Theorem W | Proved with the corrected signature and integral-lattice hypotheses, conditional on the explicitly stated unrefereed 032/Milne2026 inputs. The effective-cycle degree bound is unconditional. |
| Extended Th. 4 | The stated inherited incidence factors, relative-injection and finite-cover cases are proved in their recorded scopes. New special incidence directions and the unrestricted abelian-type transfer remain open or explicitly conditional. |
| Final Th. 5 | Checked synthesis C44-T05 retains Schur corrections, the injective case, the Albanese-primitive cover domain and the unresolved general axis term. |

The strongest supplied-support orders are ceil(e/3) at p=3, ceil(e/10) at p=5, and ceil(e/(3p)) at p≥7. Existence of the initial support is not assumed automatic. A31t treats the exact characteristic-three e=5 case and does not assert a ceil(e/5) theorem.

The final higher-Cartier research leaves two specific controls unproved: a fixed-axis primitive period restriction modulo closed-function periods, and mixed-characteristic ambient correction preserving the detector. A31v proves finite-dimensionality and a sufficient axis-dependent test, not that the chosen axis passes the test. The quantitative conormal and constrained-test notes are preserved as unpromoted research with explicit gaps and whole-note reading scopes.

## Contents and verification

C44_POS.tex is standalone. QUESTIONS.tsv gives all 75 treated questions with their final states. LEDGER.md includes the complete scheduled reviews; CHECK_EVENTS.tsv distinguishes whole-proof readings, narrower source checks and computations; IMPLICATIONS.md maps results to Grothendieck's texts and predecessor statement IDs. The work directory preserves contribution fragments, scripts, certificates, source locators, audits, rejected inferences and the final research notes. The supplied source archive is not duplicated.

All promoted proofs have the recorded complete-proof readings. Final research-note readings do not promote their unproved integrated applications. Assembly hashes, identifier coverage and LaTeX compilation are reproducibility checks, not mathematical proof checks. Every use of 032 or Milne2026 retains the explicit unrefereed-preprint qualification. The separate Milne2022 transfer assertion is retained where needed.

The entries below are historical checkpoint notes. Their former bounds and pending statuses are superseded by this final summary and QUESTIONS.tsv. All earlier checkpoint ZIPs remain unchanged and none is nested in this package.

---

# C44_POS working package

The standalone manuscript is C44_POS.tex. QUESTIONS.tsv is the per-question state register, LEDGER.md records work and scheduled reviews, CHECK_EVENTS.tsv records actual checks, and IMPLICATIONS.md maps findings back to Grothendieck and the predecessor runs.

The work directory contains the editable contribution fragments, complete proof-check records, exact arithmetic/Gram scripts and their outputs, assembly script, research notes, and an assembly hash manifest. The attached source archive was extracted exactly once into sources/ in the original workspace. That input archive is not duplicated here; it remains one of the supplied attachments.

Start time: 2026-11-22 00:13:48 Europe/Berlin (2026-11-21 23:13:48 UTC). Checkpoints are due every 45 minutes from that time, under new sequential names and without earlier ZIPs nested. First three-hour gate review: 03:13:48 Europe/Berlin; hourly afterward. Two successive reviews without the prompt’s defined movement trigger stopping. Do not claim a scheduled review before the actual time.

To resume, read the governing prompt at work/input_prompt.md, then LEDGER.md, QUESTIONS.tsv and the latest work/assembly_manifest.json. Review any new agent fragments before promoting them into the checked part. The cover boundary and all-conductor proofs have full review markers. The general axis sign and the Fermat AJ injection are unresolved.

Run work/assemble.py from the restored workspace to rebuild the paper and merge current per-agent check events. The script places unchecked cover candidates separately unless the whole-proof pass marker exists. Preserve all explicit unrefereed-input qualifications.

## State approaching checkpoint 07, 22 November 2026, 04:21 UTC

Reviews 1, 2 and 3 recorded genuine movement. Review 3 was executed at 04:16:00 UTC against its scheduled time of 04:13:48 UTC. Review 4 is due at 05:13:48 UTC; no stopping condition has been met. Read work/scheduled_reviews.json for the exact prior row snapshots and work/review_assessments.json for explicit assessments. Review 3 counts only the strict reduction of the original primitive-class lifting gate; the universal sign criterion did not broaden in that interval. Later reviews require an explicit comparison; never infer movement from new file counts or direct corollaries.

The checked fixed-axis criteria now include actual rational orthogonal blocks and extending totally real fields (A19/A24), with affine S3 and D5 applications and an unbounded prime-dihedral extension across dimensions (A20/A21/A23/A25/A26). They do not settle every axis. A27 identifies the integral canonical PD obstruction and excludes lifting the nonzero primitive A14/A18 class along every unramified embedded model. A29 and A30 have passed whole-proof checks: A29 covers all unramified abstract models; A30 proves product-polarized I, B, D and strong Tate on all powers of one selected axis. Exact hashes and audit scope are recorded.

A28/A28a/A28b are checked: actual selected nonabelian axes have product-polarized I on their squares, strong Tate in every degree and over every finite extension, B and D, scan049 positive-adjoint semisimplicity, and all corrected SN-C04 conditions. A primary-source locator error was corrected transparently: the exact Kleiman1994 scan uses Proposition5-1 p17 and Theorem5-6(1) with its proof p19. The mathematical application is unchanged; old erroneous locator events are superseded by explicit correction events.

The checked A31 finite initial ramification theorem now excludes the constructed primitive class on every abstract model with ramification index e<p−1. For larger e, a model lifting that class must prevent the specified surface from lifting through R/pi^n0, where n0=floor(e/(p−1))+1. No claim that this initial lift always exists is made. A14b extends the actual nonliftable-centre construction to every prime p congruent to 3 modulo 4. A31a explicitly computes a surviving canonical divided-power term at the boundary e=p−1, so a square-zero argument alone cannot remove the remaining gate.

A30a gives all ample polarizations on the selected fourfold itself; A30 on higher powers retains its positive-product-polarization scope. A32/A32a exclude uniform abelian realization of the entire variable local system in an explicit full-monodromy family; individual special-fibre correspondences remain possible. Both additions have whole-proof checks and do not separately reset the progress clock.

Fermat arithmetic AJ5 remains at the exact F07 projected etale-motivic finite-generation gate. F23 proves projected geometric 5-primary torsion vanishing and bounded geometric 5-divisibility of the known nonzero class, while its exact sequence retains a nonzero completed geometric Chow term. These conclusions do not settle F07. All negative route audits are retained. Current work concentrates on actual crystalline descent invariants for the axis sign and on the initial ramified support-lifting gate.

work/checks/check_coverage.py verifies identifier coverage and assembly hashes only. Compilation and arithmetic scripts are not mathematical proof checks. The paper's raw contribution fragments, candidate notes and all check events remain available for continuation.

A31b and F24 have also passed complete author/root proof readings. A31b is an explicit ramified support-lifting shortcut counterexample outside A_B; its rational cycle class actually lifts. F24 is a formal arithmetic module diagnostic, not a motive counterexample. Neither changes an original gate.

## Update at 04:45 UTC

A33/A33a/A33b have passed complete author, root and independent proof readings and are now in the checked part. Their crystalline quadratic-invariant formula requires a full central-cycle certificate before it identifies the algebraic form. No actual new axis sign case is certified. F25 has passed complete author/root readings: it identifies the actual integral Chow descent defect with a precise projected H2(K2) tame-symbol kernel and records its mod5 and completion consequences. It proves no vanishing and leaves F07 open. These additions do not reset the progress clock.

Current checkpoint08 status: scheduled review4 records NO movement, streak1. A31c, A33, F25, F07-SA1 and the W09 source audit have completed whole-proof readings. A34/A34a quaternion sign candidate is preserved separately as awaiting final root audit; A35 actual C3 construction remains active work. Universal fixed-axis sign, larger-ramification lifting, and Fermat AJ5 remain open.

## Checkpoint09 preparation — 22 November2026, 05:57UTC

Review4 remains NO with streak1. Review5 is due06:13:48UTC. Since review4, the quaternion criterion A34/A34a and actual family A35 have completed author, root and independent whole-proof readings; together they are a genuine strict reduction of the main sign gate. A36–A39 are extensions of this same developing argument, not independent staged clock resets. A38 is now checked; A40 actual characteristic-three C4 family is in its final independent audit. The universal sign, larger-ramification class lifting, and Fermat AJ5 gates remain open. Continue research; no final package or two-NO stop is yet authorized by the scheduled rule.

Final Checkpoint09 audit update: A40 also passed its independent complete-proof review and is now in the checked part, at final SHA256575e4df3b751126b866f00c7f3314c314b5eed03f6315e5510be6e9ffb0ff9ad. A34 through A40 form one developing quaternion advance.

Checkpoint09 build: standaloneTeX compiles successfully to276pages. One layout-only proof-heading fix changes A40 currentSHA to b52882a8ee426eb4b459128da7071dd88cc3f4a9670b723cd5b0401c841df42e; its whole mathematical text is unchanged from the independently read575e4df3 version. Compilation is not mathematical verification.

## Current state — 2026-11-22T06:31:50.842502+00:00

Review5 at06:14:10UTC recorded movement, counting A34/A35 once; streak0. All A36–A42b extensions and consequences are explicitly the same advance and cannot be staged as a Review6 reset. Review6 is due07:13:48UTC, checkpoint10 due06:43:48UTC. A31d, A41/A41a/A41b, A42/A42a/A42b and F07-SA2 have passed their specified whole-proof readings and are promoted. The dyadic formula uses the full even lattice and nonprimitive correction. The elliptic-power families now have unconditional full original-pencil heights modulo H0. Universal axis sign, the finite initial ramified-support gate, and Fermat F07 remain open. Continue; no stopping condition has been met.

Checkpoint10 preparation: A36b also completed author/root/independent whole-proof review. The current standalone manuscript compiles to301pages. Primary-source page images used locally for reading are omitted from the ZIP; their exact page locators and reading events are retained. Review6 remains due07:13:48UTC, with the same quaternion advance already counted at Review5.

## Current state — 2026-11-22T07:26:42.375327+00:00

Review6 at07:14:08UTC recorded NO movement, streak1; its snapshot is unchanged. After that review A31f completed author/root/independent whole-proof checks. For selected actual characteristic-three axes and their nonzero primitive classes, every abstract model with ramification e<=2 is now excluded. The canonical bounded PD descent, rather than a chosen transport, is essential. Models of e>=3 and the universal sign remain open. A36c and all quaternion refinements remain part of the single previously counted advance. A31e, F26 and F27 are checked; the Fermat F07 arithmetic gate remains open. Next scheduled review08:13:48UTC; continue research.

Checkpoint11 preparation: the current standalone manuscript compiles successfully to317pages. The package retains exact source fragments, audit notes and events; successful compilation is separate from whole-proof verification. A31f is checked, while every unaddressed larger-ramification case remains open.

## Current state approaching checkpoint12 — 2026-11-22T08:12:42.344223+00:00

A31g and A31h are checked by complete proof readings. The primitive two-term jet theorem holds for fixed3<=M<4p; the first equality boundary excludes every abstract model with e<=p−1 for the selected nonzero A14b/A18 classes in each characteristic p=3 mod4. At e=(p−1)m an explicit S_m already suffices for exclusion. A31f/g/h are one developing lifting advance completed after Review6. Review7 is due08:13:48UTC; its prepared assessment counts this reduction once. A31i is a candidate beyond the PD boundary. Its larger-pole quotient lemma has author/root/independent whole-proof PASS, but the actual common comparison-frame construction and final integrated proof remain under review. Do not promote it from its unchecked status without those completed checks. A31-SA1 is a checked source boundary audit, not an additional exclusion. All quaternion refinements remain the single Review5 advance; FermatF07 and the original universal sign remain open.

## Current checkpoint13 state — 2026-11-22T08:58:40.989143+00:00

Review7 at08:13:51UTC recorded YES, counting the A31f onward lifting advance once. All ensuing A31g–q refinements are grouped into that same advance, with no staged reset. Review8 is due09:13:48.738457UTC. No stopping condition has been met. Checkpoint13 is due08:58:48.738457UTC and is the only permitted next checkpoint.

A31i/j/k/l/m/n/o are checked by complete author/root/independent readings. The strongest unconditional selected-class exclusion is e<=4 atp3 and e<=2p−1 atp>=5. The supplied smooth-support threshold isceil(e/3) atp3 andceil(e/(2p−1)) atp>=5. A31n detects a nonzero H1(Q_M) edge for every fixedfiniteM at sufficientlyhighaxisdegree; it retains a precise ambientclosedfunctionannihilator and doesnotclaimfulljetsurjectivityabove4p.

A31p uniformampleconormal proof is author/root whole-read PASS, awaiting additional independent whole read, and remains in the unchecked part until promoted. A31q extends to e<=3p−1 and suppliedthresholdceil(e/(3p−1)) forp>=7; author/fermat whole-read PASS, root whole read not yet completed, so it remains unchecked. Their complete current proofs and all audits are retained. The candidate ambient-removal lemma for precisionn<=p remains research work; no theorem is promoted from messages.

The universal fixed-axis sign, special-cover sign at arbitraryclosedpoints, FermatAJ5/F07, special-variableTh4 and the historicalprior-unknown-I requirement remain open. All quaternionrefinements remain the advancecountedReview5. Primary source scopes, original proof fragments and dated events are preserved. The assembly now correctly reads arithmeticdate_utc fields; all assembled events have dates. Build/coveragechecks are notproofchecks.

## Post-checkpoint13 update — 2026-11-22T09:03:48.118052+00:00

A31p and A31q have now completed author, root and independent whole-proof readings and are in the checked part. Checkpoint13 itself is unchanged. The strongest selected-class exclusion is e<=4 at p=3, e<=9 at p=5 when a nonliftable centre is given, and e<=3p−1 at p>=7. Actual A14b/A18 centres occur for p congruent to3mod4. The supplied-support thresholds are ceil(e/3), ceil(e/9), and ceil(e/(3p−1)), respectively. A31p supplies a single open for all finite quotient injections; A31n still has a separate degree threshold depending on M. The ambient closed-layer removal lemma A31r is being developed and is not yet proved. All this remains part of the advance counted at Review7. Review8 is due09:13:48.738457UTC; checkpoint14 is due09:43:48.738457UTC.

## 2026-11-22T09:19:35.283605+00:00 — A31r and A31s checked after Review 8

Author, root and independent whole-proof readings have passed A31r and A31s. A31r removes an ambient closed layer at a fixed pole bound and precision n<=min(p,e), while retaining the actual rational full class, an integral lower ordinary image, and the bounded finite supported representative. Its initialization uses all integral F3 tests. The global ambient source lift at larger precision remains unproved.

A31s proves the next exact boundaries and the entire intervening scaled intervals: e<=3p for p>=7, and e<=10 for p=5 with a nonliftable centre. The sufficient supplied-support orders are ceil(e/(3p)) and ceil(e/10), respectively. The characteristic-three bound remains e<=4 with supplied threshold ceil(e/3), pending the separate e=5 application. Actual A14b/A18 examples still require p congruent to 3 mod 4.

These are refinements of the single A31 advance counted at Review 7. Review 8, recorded at 09:16:40.361918 UTC, is NO with streak one. The next scheduled review is 10:13:48.738457 UTC; checkpoint 14 is due 09:43:48.738457 UTC. No original universal sign, special-cover, or Fermat scalar Abel-Jacobi question has been closed by these refinements.

## 2026-11-22T09:24:36.786282+00:00 — A31t checked: characteristic three through e=5

A31t has author, root and independent entire-proof PASS. It removes three genuine pole-nine closed boundaries, then applies A31r to the first ambient closed layer at precision two and pole bound eighteen. The actual ordinary lower class and its integral lattice are retained throughout. The unchanged Cartier edge forces S2; A31l gives S3 and A31 algebraizes, contradicting the intrinsic nonliftability of the chosen centre.

The selected characteristic-three classes are therefore excluded on every abstract model with e<=5. The arbitrary-e supplied threshold remains ceil(e/3); no scaled e=5m theorem is claimed. Together with A31s the current ranges are p=3: e<=5; p=5: e<=10 with a separately supplied nonliftable centre; p>=7: e<=3p. All remain the single Review 7 advance. Review 8 is NO, streak one, and Review 9 remains due 10:13:48.738457 UTC.

## Checkpoint 14 preparation — 2026-11-22T09:43:07.088760+00:00

Review 8 was recorded at 09:16:40.361918 UTC as NO, with one consecutive review without additional movement. Review 9 is due at 10:13:48.738457 UTC; a second consecutive NO will trigger the final package. All A31 refinements remain the single advance counted at Review 7, and all quaternion refinements remain the advance counted at Review 5. Checkpoint 14 is due at 09:43:48.738457 UTC.

A31r, A31s, A31t, A31u and A31v have completed author, root and independent whole-proof readings. The selected characteristic-three classes are excluded on every abstract model with e<=5. For p>=7 the checked range is e<=3p, with supplied-support threshold ceil(e/(3p)); at p=5 it is e<=10 and ceil(e/10), given a separately established nonliftable centre. At p=3 the arbitrary-e supplied threshold remains ceil(e/3). A14b/A18's actual centres occur for p congruent to 3 mod 4.

A31r removes an ambient closed layer only at precision n<=min(p,e), with an actual full ordinary class and an integral lower image. A31u detects higher Cartier normal edges on one ample-conormal open, but does not preserve them through arbitrary high-precision ambient removal. A31v gives a finite-dimensional colimit and a sufficient finite test depending on the fixed axis; it does not prove that the test holds there or that every finite quotient injects. The uniformity issue and the global ambient/Bockstein corrections remain open.

F07-SA3 is author/root whole-read, with independent verification still pending; retained in the unchecked part. Its CM radical calculation and recent source audits do not prove scalar AJ5 injectivity, F07 finite generation, or a uniform bound on F25's descent cokernel. The universal axis sign, arbitrary closed special-cover sign, special-variable Th4, and task 4's prior-unknown-I requirement also remain open. No checkpoint or source audit is counted as movement.

Checkpoint 14 status amendment at 2026-11-22T09:43:24.125170+00:00: F07-SA3 has now passed its independent entire-proof audit at the final citation-corrected hash and is in the checked part. The earlier preparation entry records the status at its own time. No Fermat gate movement follows.
