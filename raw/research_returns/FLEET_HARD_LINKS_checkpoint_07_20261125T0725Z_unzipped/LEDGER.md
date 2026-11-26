# Research ledger

Started 2026-11-25 02:01 UTC (03:01 Europe/Berlin). Parts are researched in order A, B, C. Original archive extracted once and held outside the return. First scheduled checkpoint is approximately 02:46 UTC, then every 45 minutes. First formal progress review is due approximately 05:01 UTC.

## Initial gates

- A: Decide LS(6) ≤ 10 or produce a dimension-11 level space; ultimately decide existence of a uniform linear bound. Current methods do not exclude dimensions 11–17 at n=6.
- B: Four missing quadratic witnesses, and circuits of degree at most two on each bipartition. Research not begun.
- C: Height-two versus height-at-least-three criterion for the specified smooth construction; exact height complexity. Research not begun.

## Events

- 02:08 UTC: Workspace filesystem was nearly full. New work and extracted inputs moved to temporary capacity, with original paths preserved by symlinks. Checkpoints will provide durability. No original attachment deleted.
- 02:10 UTC: Two separate readers found the claimed torus-deformation implication unsupported: the specified symmetry group is finite. This corrects the route; it does not change the main dimension gate.

- 02:29 UTC: Exact Klein pure and mixed quartic formulas, 24 flex lines, and the dimension-two mixed bound have separate same-model re-proofs. The no-pure-line-extension claim has an exact modular calculation; independent re-proof remains pending.
- 02:31 UTC: The full six-cycle-invariant bound ten and the nontrivial scalar-symmetry bound ten are proved with separate same-model re-proofs. Thus a hypothetical dimension-eleven example must avoid both classes. Hook inclusion-maximality excludes all extensions of the usual nine-dimensional construction. No unrestricted dimension bound improved.
- 02:35 UTC: Two independent coefficient-matrix constructions prove the order-four graded-ideal stabilizer is scalar. The projection-annihilator rank condition does not settle LS(4): an explicit six-plane satisfies quadratic and zero-rectangle tests but fails mixed cubic vanishing. The torus and first-order-isolation routes are therefore narrowed to specified missing steps.
- 02:36 UTC: Part B main research begins after the named Part A routes have been examined. Remaining Part A calculations and independent checks continue. Part B starts with exactly four missing witnesses and degree at most two in each bipartition; the granted at-most-three and one-sided theorems are not being reproved.

- 02:46 UTC: First scheduled45-minute checkpoint. All three paper projects compile; research remains in progress. Most new exact results concern PartA; PartB main attacks and unrestricted affine43gate search are running. PartC remains at its opening draft. No source files or earlier archives are included.

## 2026-11-25 03:31 UTC — scheduled checkpoint 02

- A: unrestricted uniform bound and LS(6) remain open; six-cycle/scalar symmetry bounds and exact Klein slice are in the paper.
- B: four missing induced edges require four deleted products; the optimal six-deletion profile is excluded, with a same-model separate reproof. New two-cut certificates further narrow the optimal seven-deletion profile; final integration audit pending. Restricted shared bilinear two-level circuits now normalize without growth under the universal-row condition. General degree (2,2), PG3/AG3 and completion additivity remain open. New pruned searches at63/43 gates both timed out without a conclusion.
- C: source-verified logarithm proof gives the exact height-two test. Replica orbit count gives an explicit formula; all-prime gadgets yield Mod_pP completeness at height two on the Hasse-zero promise. Independent reproof of the general gadget is in progress; raw coefficient examples are checked by two different algorithms. Exact higher height classification remains under study; an explicit terminating bound and upper algorithms are being documented.
- This is the second scheduled snapshot, not the three-hour progress review. The first formal review remains due at approximately05:01UTC.

## 2026-11-25 04:15 UTC — research snapshot, not a scheduled review

C now has the all-prime exact height-two replica/orbit criterion and promised Mod_pP completeness; exact-S-only dependence is refuted in every characteristic. A characteristic-two height-three gadget is independently verified and gives promised parity completeness. The coefficient rule terminates using a cohomological bound, and an existing zeta algorithm gives FEXPTIME for full exact height including infinity; matching full-function complexity remains open. Point-count tests include a genuine p2 mod8 precision obstruction. C2-C6 have the precise character/first-variation correction, model-specific bounded-rank trace obstruction, fixed-orbit degree stabilization, class-group-minor counterexample, exact DIV local identities, and odd-theta affine classification. All open rows are updated in QUESTIONS.tsv.

B's D7 five-product/two-addition profile has an independent statement-only reduction being checked against the certified templates. A and the unrestricted B conjecture remain open. This is not the three-hour review: the first formal movement review remains due around05:01UTC. Checkpoint03 is due about04:19UTC,45minutes after the preceding durable save.

## 2026-11-25 04:25 UTC — checkpoint 03 and packaging correction

Checkpoint 03 was saved at approximately04:24UTC, later than the intended04:19 time because the context transition and final B7 integration intervened. Its SHA-256 is7e50930509d171e8079a23cb841eb646a4d2d6ee6a18aebd206a2c4ee33a94c2. The next45-minute checkpoint is due approximately05:09UTC. The archive inadvertently included one external-source extraction, research/c_main_referee/lauder_wan_published_extract.txt. This violates the no-source-copy requirement and the manifest's generic assertion for that checkpoint. The file was moved outside the workbench as soon as detected; package.py now rejects plain-text extracts and PDFs outside the three paper outputs. The earlier checkpoint remains unchanged under the no-overwrite requirement. The user was informed. No source text is intended for any subsequent ZIP.

## 2026-11-25 05:04 UTC — first formal three-hour progress review

The review is against the initial main gates and every currently open row. Movement is present; the consecutive no-movement count is zero. The next formal review is due approximately06:04UTC.

- **A main gate strictly smaller:** the unrestricted order-six upper bound decreased from17 to15 through the proved weighted cubic bound 3dimL≤n²+2n−1, independently rederived from its statement. The uniform linear bound and LS6≤10 are still open. The new general bound does not settle either one.
- **B main gate strictly smaller:** the optimal D6,e0 gain-four profile is excluded; the optimal D7,e0 profile is reduced to four products and three additions. Its three-visible-cut branch now has an independent structural reproof, encoder audit, and independently checked RUP certificates. One-visible and two-visible original-circuit embeddings are being checked; their completion is not counted prematurely. The unrestricted conjecture, lower cover gains and general bidegree(2,2) remain open.
- **C main rows changed:** exact height-two criterion, formula-dependent replica/orbit interpretation, and all-prime promised Mod_pP completeness are proved; count-only dependence is refuted. A terminating exact coefficient rule and FEXPTIME upper bound are proved. Full-function matching complexity remains open.
- The full expert A read corrected the displayed Klein basis from E01 to E02. Independent reconstruction checked all384 exact coefficients and a separate matching-DP computation checked the two mod29 sextic obstructions. This correction is evidence of checking, not an additional main-gate movement.

### Every open or partially open row at this review

| Question | Status | Current gate |
|---|---|---|
| A1-uniform | OPEN | Whether sup_n LS(n)/n is finite; no uniform bound or superlinear family |
| A1-six | OPEN | Unconditional9<=LS6<=15; dimension11example must avoid full6cycle invariance, nontrivial scalar symmetry and hook containment |
| A1-connected | PARTLY_PROVED | Exact c5,c6 contractions proved and independently checked numerically over rationals; growing-order Kneser inequality not proved |
| A1-zeta | PROVED_FORMULATION_ONLY | Zeta coefficient equation is exactly the original homogeneous level equations |
| A2-four | OPEN | 5<=LS4<=6 per dated graph; quadratic/projection constraints admit nonlevel6planes |
| A2-four-by-five | OPEN | Known6dimensional hook is inclusion-maximal; existence of7dimensional level space unresolved |
| A3-Klein-mixed | PARTLY_PROVED | Exact S2 and S4; dimension<=2; pureflex cannot extend; transverse mixedplanes undecided |
| A3-general-G | OPEN_CLASSIFICATION | Invariant ideal generated by restricted layers contracts exactly by Reynolds operator; no uniform generator classification |
| A5-hyperpermanent | OPEN | Rootunity block reduction exact; claimed induction still needs a dimension inequality |
| A5-cycle-defect | PARTLY_PROVED | General cyclic/abelian invariant bounds proved; n6 bound10+5r; no unrestricted linear bound |
| B1-unrestricted | OPEN | Atleast4missing quadratic witnesses and mixed variables on both sides required |
| B1-four-missing | OPEN | d2:(5,0); d3:(5,0),(5,1),(6,0); d4:(6,1),(7,0); D7,e0 onlyfourproducts/threeadditions withatmost2visiblecuts; onevisibleCNFbound independently proved, originalembedding beingchecked |
| B1-degree-two | PARTLY_PROVED | Exact bound for shared two-level bilinear architectures with at most one universal row in each unsafe bottom rectangle; general (2,2) remains open |
| B1-two-AND-levels | PARTLY_PROVED | Restricted shared bilinear architecture normalized without growth; general two-level class remains open |
| B2-affine | OPEN | Unrestricted43gate pruned encoding UNKNOWN after300s; explicit44gate star calibration verified |
| B2-infinity-additivity | OPEN | Literal projective line-star deletion gives47 atq3, not44; naive20gate deletion step fails |
| B2-PG23 | OPEN | Unrestricted63gate pruned encoding UNKNOWN after300s; no witness or certified lower bound |
| B3-negation | PARTLY_PROVED | Correct BNT bound and nearlinear endpoint proved at ceil(log2(q²)) NOTs; exact intermediate budgets open |
| B4-root39 | OPEN | 38gate synthesis UNKNOWN after300s; target upper39 unchanged |
| B4-root59 | OPEN | 58gate synthesis UNKNOWN after300s; target upper59 unchanged |
| B4-hyperovals | PARTLY_PROVED | 714/715 conditional threshold proved; PG(2,4) threshold functional exactly14; 168 hyperovals enumerated |
| B5-component | PARTLY_PROVED | Lower bihomogeneous component extracted without growth for P in Sup(G); additional missing-edge charge remains open |
| C1-complexity | PARTLY_PROVED | Every fixed height in Mod_pP; height1/2 complete allp, height3 complete p2; full height Mod_pP-hard and in FEXPTIME |
| C2-polynomial-rank | MODEL_DEPENDENT | Succinct Artin schemes rank<=1 and richer known-rank<=2 projector syntax yield NP=RP consequence; expanded matrix trace easy |

Rows recorded as proved or refuted remain in QUESTIONS.tsv with their precise scopes. No result has been promoted from a timed-out search to an impossibility statement. The four graph synthesis attempts remain UNKNOWN.

## 2026-11-25 05:08 UTC — seven-deletion profile excluded

After the formal review, the last two visibility branches passed their independent checks. The one-visible branch has a statement-only structural reproof and an independent exhaustive enumeration of850500 six-gate DAGs giving atmost12CNFclauses,13withcontext,below the matching requirement16. The two-visible branch has a fresh statement-only reduction, complete encoder audit, byte-identical regeneration ofall six relevantCNFs, and binding to the alreadyindependentlyreplayed RUP-onlyrefutations. Consequently D7,e0,d4 is excluded. The gain-four gate is now strictly smaller: only D6,e1,necessarilyfourproducts/twoadds,remains. Lower cover-gain rows and the unrestricted conjecture remain open. This is new movement after the05:04review, to be evaluated at the next scheduledreview.

## 2026-11-25 05:10 UTC — checkpoint 04

Saved checkpoint04, SHA256 66a69bd581f6e458a03bd0ea2809eb33ed5ecc27b36c1d08617c42c8be499f3f, 73,714,554 bytes. No earlier checkpoint changed. Next checkpoint due approximately05:55UTC.

## 2026-11-25 05:20–05:50 UTC — further main-gate movement

B: the final gain-four profile D6,e1 is excluded by a statement-only independently rederived full-context/affected-star argument. Thus every gain-four case for exactly four missing quadratic witnesses is settled. Lower cover-gain rows remain open. Two smaller graph configurations in the D5,e0 gain-three row are being checked and are not counted as proved yet.

C: a uniform promised height-two oracle recovers exact satisfying counts through polynomially many nonadaptive prime/residue queries; its FP oracle class equals FP^#P under promise-respecting calls. This gives #P-hardness for the full exact-height function with varying input prime. Independently, the full exact-height function, including infinity and binary input prime, belongs to FPSPACE by polynomial-depth access to finite p-adic trace calculations and balanced exact Frobenius-coefficient reconstruction. Each theorem has a fresh statement-only same-model re-proof and a post-freeze comparison. The full complexity classification remains open.

A: all27 final PDF pages were inspected and the full expert/newcomer reads completed. This is quality assurance, not movement. The next formal review remains06:04UTC.

## 2026-11-25 05:55 UTC — checkpoint 05

Saved checkpoint05 (snapshot05:55UTC), 74,149,622 bytes, SHA2567dcc77aeab94e69dcdd96a88893320b96853cdcca74b55e34aa3e2653b105b1d. The snapshot contains current A/B/C PDFs and source, including C's FPSPACE theorem and exact-counting reduction. The lowergain B audit concluded just after the snapshot; its accepted paper section was integrated afterward. Next checkpoint due approximately06:40UTC. No previous archive changed.

## 2026-11-25 05:57 UTC — two lowergain shapes excluded

The gain-three, five-deletion, optimal-frame profile is excluded when the four missing edges form a three-edge path plus a disjoint edge or a triangle plus a disjoint edge. A fresh statement-only structural reduction, followed by a complete encoder/coverage audit and regeneration/hash binding of all six RUP-certified instances, passed. The path case applies to girth-at-least-five graphs; the triangle case concerns the broader C4-free class. The result is in the paper with its full reduction and certificate semantics. Other shapes and profiles remain open.

## 2026-11-25 06:04 UTC — second formal hourly progress review

Movement is present since05:04UTC. The consecutive no-movement count remains zero. The next formal review is due07:04UTC. This review concerns mathematical gates, not writing, source searches or packaging.

- A: no further main-gate change since the weighted bound. The current unconditional order-six range remains9<=LS6<=15; the uniform linear conjecture and LS6<=10 remain open. The completed two readings and27-page inspection are quality assurance, not movement.
- B: the complete gain-four row is now excluded, removing both D7,e0 and D6,e1. In gain3,D5,e0, missing graphs P4 disjoint K2 and K3 disjoint K2 are excluded by full structural proofs and six RUP-certified templates with fresh independent rederivation and source binding. A further elementary pure-product-cut theorem, independently derived by the root before reading its author's proof, gives D>=2^d−1 when exactly one addition is deleted; this removes that branch from all remaining gain-three profiles. The full four-missing question, gain-two row, and other gain-three branches remain open. A new D6 path-plus-edge candidate is under examination and is not counted as accepted.
- C: full exact height has improved from FEXPTIME to FPSPACE for binary prime inputs, including infinity. Uniform promised height-two decisions are oracle-equivalent to exact counting, giving #P-hardness for full exact height by nonadaptive polynomial-time oracle calls. Both have fresh statement-only same-model reproofs. The gap between exact-counting hardness and polynomial-space membership remains open. A newly located published/preprint matrix method via quasi-F-splitting may simplify and sharpen the resource analysis; its pending analysis is not counted as a new classification.

### Every open or partially open row

| Question | Status | Current gate |
|---|---|---|
| A1-uniform | OPEN | Whether sup_n LS(n)/n is finite; no uniform bound or superlinear family |
| A1-six | OPEN | Unconditional9<=LS6<=15; dimension11example must avoid full6cycle invariance, nontrivial scalar symmetry and hook containment |
| A1-connected | PARTLY_PROVED | Exact c5,c6 contractions proved and independently checked numerically over rationals; growing-order Kneser inequality not proved |
| A1-zeta | PROVED_FORMULATION_ONLY | Zeta coefficient equation is exactly the original homogeneous level equations |
| A2-four | OPEN | 5<=LS4<=6 per dated graph; quadratic/projection constraints admit nonlevel6planes |
| A2-four-by-five | OPEN | Known6dimensional hook is inclusion-maximal; existence of7dimensional level space unresolved |
| A3-Klein-mixed | PARTLY_PROVED | Exact S2 and S4; dimension<=2; pureflex cannot extend; transverse mixedplanes undecided |
| A3-general-G | OPEN_CLASSIFICATION | Invariant ideal generated by restricted layers contracts exactly by Reynolds operator; no uniform generator classification |
| A5-hyperpermanent | OPEN | Rootunity block reduction exact; claimed induction still needs a dimension inequality |
| A5-cycle-defect | PARTLY_PROVED | General cyclic/abelian invariant bounds proved; n6 bound10+5r; no unrestricted linear bound |
| B1-unrestricted | OPEN | Atleast4missing quadratic witnesses and mixed variables on both sides required |
| B1-four-missing | OPEN | All gain4 cases excluded; remaining gain2:(D,e)=(5,0), gain3:(5,0),(5,1),(6,0); in gain3,D5,e0 the missing graphs P4 disjoint K2 and K3 disjoint K2 are excluded; exactly one deleted addition requires D>=2^d−1, excluding that branch throughout gain3,D5/6 |
| B1-degree-two | PARTLY_PROVED | Exact bound for shared two-level bilinear architectures with at most one universal row in each unsafe bottom rectangle; general (2,2) remains open |
| B1-two-AND-levels | PARTLY_PROVED | Restricted shared bilinear architecture normalized without growth; general two-level class remains open |
| B2-affine | OPEN | Unrestricted43gate pruned encoding UNKNOWN after300s; explicit44gate star calibration verified |
| B2-infinity-additivity | OPEN | Literal projective line-star deletion gives47 atq3, not44; naive20gate deletion step fails |
| B2-PG23 | OPEN | Unrestricted63gate pruned encoding UNKNOWN after300s; no witness or certified lower bound |
| B3-negation | PARTLY_PROVED | Correct BNT bound and nearlinear endpoint proved at ceil(log2(q²)) NOTs; exact intermediate budgets open |
| B4-root39 | OPEN | 38gate synthesis UNKNOWN after300s; target upper39 unchanged |
| B4-root59 | OPEN | 58gate synthesis UNKNOWN after300s; target upper59 unchanged |
| B4-hyperovals | PARTLY_PROVED | 714/715 conditional threshold proved; PG(2,4) threshold functional exactly14; 168 hyperovals enumerated |
| B5-component | PARTLY_PROVED | Lower bihomogeneous component extracted without growth for P in Sup(G); additional missing-edge charge remains open |
| C1-complexity | PARTLY_PROVED | Every fixed height in Mod_pP; height1/2 complete allp, height3 complete p2; uniform promisedheight2 oracle FP-equivalent to #P; fullheight #P-hard under nonadaptive polynomial-time oracle reductions and in FPSPACE |
| C2-polynomial-rank | MODEL_DEPENDENT | Succinct Artin schemes rank<=1 and richer known-rank<=2 projector syntax yield NP=RP consequence; expanded matrix trace easy |

All proved and refuted rows remain in QUESTIONS.tsv with their scopes. No timed-out graph search is promoted to UNSAT, and no candidate matrix or circuit reduction is counted before its required proof checks.

06:07UTC: The general single-addition theorem is integrated with full proof. For every H-cover the remaining induced graph is a matching; 2^d<=D+1 follows by counting its prime CNF clauses. At girth at least five the missing-edge graph itself must be a matching. No quadratic optimality is assumed. This accepted movement was included in the06:04review after the independent derivation and author comparison passed.

## 2026-11-25T06:38:35.229758+00:00 — accepted matrix resource and unary-height refinements

The existing quasi-F-split matrix algorithm is now explicitly credited to Kawakami–Takamatsu–Yoshikawa and Batubara–Garzella–Pan, with Yobuko's comparison theorem. A separate statement-only same-model derivation verifies FPSPACE, a matrix-dimension cutoff and the sharper dense time 2^{O(d log p)}poly(s,d,logp). The older independent finite-trace proof remains as an alternative appendix. A second statement-only derivation, frozen before the author's proof was opened, verifies fixed-prime/unary-height Mod_pP completeness and unary-prime/unary-height exact-counting oracle equivalence. Both results are integrated with full proofs. The unrestricted exact-height complexity row stays open with a smaller parameter gate.

A's 27-page PDF and B's 34-page PDF have completed expert/newcomer and all-page visual checks at their recorded hashes. C has a clean changed build; the entire changed PDF still needs final visual inspection. The new B six-deletion path-plus-edge candidate has passed seven finite-class bindings; its extra auxiliary singleton-union lemma is pending a separate statement-only reproof and is not yet in the paper.

This is a research update, not the scheduled hourly review. The next formal review remains 07:04 UTC and the consecutive no-movement count remains zero.

## 2026-11-25 06:40 UTC — checkpoint06

Saved FLEET_HARD_LINKS_checkpoint_06.zip, 75,354,979 bytes, 685 archive entries, SHA-256 5c4216417b906c5156d1026de7674b4dc470f6c0cf24cdd1892867a87ff8dbae. Includes all current paper projects, full unary-height and matrix resource proofs, original records and certificates; excludes external sources and earlier checkpoints. The exact-byte source scan compared 620 source files with 686 workbench files and found no matches; its limitations are recorded. C clean PDF hash664b11cd9bccd76cd7f2833fadda84972af3f855417d53ce413a8385bf749bcd has zero overfull boxes/unresolved references; full visual review is pending. Next checkpoint due07:25UTC.

## 2026-11-25 06:45 UTC — six-deletion path case accepted

The gain-three P4 disjoint K2 missing graph with an optimal quadratic frame now satisfies the full star lower bound: the prior five-deletion exclusion is joined by the complete six-deletion exclusion. Seven checked finite classes cover all profiles. The initial independent structural reduction froze before author access; a second independent statement-only proof separately closes the additional singleton-union lemma that was first encountered by the first referee after freezing. That distinction is recorded, not erased. Root read the full proof, both independent derivations and finite-class audit and accepted integration. The one-excess five-deletion case is still a candidate and is not counted as accepted.

## 2026-11-25 07:04 UTC — third scheduled progress review

Reviewed every open or partially open question against the strongest proved gate at06:04UTC. **Movement: yes. Consecutive no-movement reviews:0. Next formal review:08:04UTC.** This is the scheduled review, not a checkpoint or a decision to finish.

- **A main gate:** unchanged. The proved weighted bound still gives9<=LS(6)<=15, while LS(6)<=10 and a uniform linear bound remain open. Near-minimal Schur-square reasoning does not give a smaller gate: the necessary evaluation configuration has seven-column row/column dependencies and is not MDS, so the opened Vosper-type theorem does not apply. No numerical search is upgraded to a nonexistence proof.
- **B main gate:** strictly smaller. All optimal-frame counterexamples with missing graph P4 disjoint K2 and gain3 are excluded, by the newly accepted D6 theorem together with the prior D5 theorem. The seven finite classes, structural reproof and separately rederived singleton-union lemma have passed. This removes an actual branch of the four-missing gate. The excess-one D5 proof is frozen and independently under review, so it is expressly NOT counted at this review. The new P3-plus-two-edges experiments are also not counted.
- **C main gate:** strictly smaller. The growing unary-height parameter is now classified: fixed-prime exact-height decision is Mod_pP-complete, and with unary prime too its oracle is equivalent to exact counting. The full binary-prime function remains between nonadaptive#P-hardness and FPSPACE; the separate dense implementation now has time2^{O(d log p)}poly(s,d,logp). A known smooth perturbation mechanism was investigated for stronger hardness, but no controlled path to the detecting coefficient was obtained. The remaining complexity questions are binary-height/infinite-height decisions and a matching full-function class.

All other open rows retain their prior mathematical gate. Their complete current states follow; formatting, source updates, page inspections and checkpoint preparation are not counted as movement.

| Question | Status | Current gate |
|---|---|---|
| A1-uniform | OPEN | Whether sup_n LS(n)/n is finite; no uniform bound or superlinear family |
| A1-six | OPEN | Unconditional9<=LS6<=15; dimension11example must avoid full6cycle invariance, nontrivial scalar symmetry and hook containment |
| A1-connected | PARTLY_PROVED | Exact c5,c6 contractions proved and independently checked numerically over rationals; growing-order Kneser inequality not proved |
| A1-zeta | PROVED_FORMULATION_ONLY | Zeta coefficient equation is exactly the original homogeneous level equations |
| A2-four | OPEN | 5<=LS4<=6 per dated graph; quadratic/projection constraints admit nonlevel6planes |
| A2-four-by-five | OPEN | Known6dimensional hook is inclusion-maximal; existence of7dimensional level space unresolved |
| A3-Klein-mixed | PARTLY_PROVED | Exact S2 and S4; dimension<=2; pureflex cannot extend; transverse mixedplanes undecided |
| A3-general-G | OPEN_CLASSIFICATION | Invariant ideal generated by restricted layers contracts exactly by Reynolds operator; no uniform generator classification |
| A5-hyperpermanent | OPEN | Rootunity block reduction exact; claimed induction still needs a dimension inequality |
| A5-cycle-defect | PARTLY_PROVED | General cyclic/abelian invariant bounds proved; n6 bound10+5r; no unrestricted linear bound |
| B1-unrestricted | OPEN | Atleast4missing quadratic witnesses and mixed variables on both sides required |
| B1-four-missing | OPEN | All gain4 cases excluded; remaining gain2:(D,e)=(5,0), gain3:(5,0),(5,1),(6,0); P4 disjoint K2 at gain3 is excluded for every optimal quadratic frame (D5,D6), and K3 disjoint K2 excluded for D5,e0; exactly one deleted addition requires D>=2^d−1 |
| B1-degree-two | PARTLY_PROVED | Exact bound for shared two-level bilinear architectures with at most one universal row in each unsafe bottom rectangle; general (2,2) remains open |
| B1-two-AND-levels | PARTLY_PROVED | Restricted shared bilinear architecture normalized without growth; general two-level class remains open |
| B2-affine | OPEN | Unrestricted43gate pruned encoding UNKNOWN after300s; explicit44gate star calibration verified |
| B2-infinity-additivity | OPEN | Literal projective line-star deletion gives47 atq3, not44; naive20gate deletion step fails |
| B2-PG23 | OPEN | Unrestricted63gate pruned encoding UNKNOWN after300s; no witness or certified lower bound |
| B3-negation | PARTLY_PROVED | Correct BNT bound and nearlinear endpoint proved at ceil(log2(q²)) NOTs; exact intermediate budgets open |
| B4-root39 | OPEN | 38gate synthesis UNKNOWN after300s; target upper39 unchanged |
| B4-root59 | OPEN | 58gate synthesis UNKNOWN after300s; target upper59 unchanged |
| B4-hyperovals | PARTLY_PROVED | 714/715 conditional threshold proved; PG(2,4) threshold functional exactly14; 168 hyperovals enumerated |
| B5-component | PARTLY_PROVED | Lower bihomogeneous component extracted without growth for P in Sup(G); additional missing-edge charge remains open |
| C1-height | PROVED_CRITERION | Finite exact rule from integral coefficients up to B_d, infinity detected; early coefficients are explicit replica counts |
| C1-complexity | PARTLY_PROVED | Fixedp/unaryr exact-height decision ModpPcomplete; unaryp/unaryr decision oracle-equivalent to#P; binaryp fullheight inFPSPACE and dense time2^{O(dlogp)}poly(s,d,logp), #P-hard via nonadaptive oracle reductions; matching full-function class open |
| C2-polynomial-rank | MODEL_DEPENDENT | Succinct Artin schemes rank<=1 and richer known-rank<=2 projector syntax yield NP=RP consequence; expanded matrix trace easy |
| C3-witness-degree | PROVED_FIXED_DATA | c_p=c_0 outside finitely many primes, including infinity, for fixed integral GL orbit data |
| C6-theta | PROVED_CLASSIFICATION | All maximal odd affine families have dimensiong-1; unique per isotropic(g-1)space; number(2^g-1)product_(j=2)^g(2^j+1) |

## 2026-11-25 07:08 UTC — C final reading and layout

PaperC now has a complete fresh expert read of all16TeX files (root) and a complete newcomer read of the same project (separate worker), including the alternative finite-trace appendix. Every page of the final46-page PDF was inspected individually, with raster matching used only to carry identical already-inspected pages across layout-only rebuilds. Final PDF SHA0281f0f6cd19341b1e6953a326db0d33fde8ea276059b0c6ad1798c0fec3deaf; zero overfull boxes and no unresolved references; author metadata blank. Program display names are mapped in PROGRAMS.md. New mathematical results would require incremental proof and layout review; no such result is currently being inserted into C. This QA update is not counted as research movement.

## 2026-11-25 07:24 UTC — preparation for checkpoint 07

The accepted six-deletion optimal P4 disjoint K2 result is now synchronized in the crosswalk, geometric dictionary, README and deposit sheet. Paper A remains the verified27-page version; Paper B is the clean37-page version; Paper C is the fully read and visually inspected46-page version. The final C method/source edits received an incremental expert check. A program-index misdescription was corrected: the replica verifier prints T3=47362 and odd-prime congruences; T3=1002460 belongs to the separate third-height program. No mathematical statement changed.

Two separate B candidates, P4 disjoint K2 with excess one and P3 disjoint2K2 with an optimal five-deletion frame, remain pending statement-only independent reproofs; their author files are included as research records, not accepted paper claims. Thirty original smooth-operator templates were evaluated exactly over F2; every vector orbit repeated with period6 without a scalar hit. These failed templates leave the C complexity gate unchanged. The source-byte scan compared621 source files with827 workbench files and found no unchanged source copy; this is not an excerpt detector. The next formal progress review remains08:04UTC.
