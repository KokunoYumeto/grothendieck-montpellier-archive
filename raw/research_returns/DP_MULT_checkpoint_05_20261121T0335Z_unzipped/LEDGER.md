# DP_MULT research ledger

Run: DP_MULT_20261121. User-facing date: 21 November 2026 (Europe/Berlin).
First recorded clock: 20 November 2026 23:51:41 UTC (21 November 00:51:41 CET).
Working start is conservatively taken as 23:50 UTC for checkpoint scheduling.
First checkpoint due approximately 21 November 00:35 UTC; later checkpoints every 45 minutes of ongoing work only. No checkpoint was created at initialization.
Three-hour progress review due approximately 02:50 UTC; hourly thereafter if still working. Two consecutive reviews without movement trigger the user-specified stop rule.

## Scope and source convention

The attached prompt is the controlling task. The archive was unpacked exactly once into `sources/`. The supplied Alpöge RH and Dirichlet-GRH results are taken as cited theorems as requested; this run does not re-audit or recompile them. The supplied Lean files expose final declarations, not the internal local-height or theta-lift proofs. Archive files are transcriptions, not manuscript photographs. Algebraically forced corrections will be marked second-pass candidates, not visually verified transcriptions.

All proofs claimed in the final paper must receive a complete proof reading recorded in CHECK_EVENTS.tsv. Models: GPT-6 Astra Pro (root and inherited agents). Effort parameter: not exposed by runtime; no numerical effort setting or formal certificate will be invented.

## Initial gates (00:52 CET)

| Row | State | Strongest gate / next step |
|---|---|---|
| Q1 finite-height bound | In progress | Correct Fable's unsupported normal form; prove a height-only estimate with explicit constants. |
| Q2 step 2 | In progress | Match height-two local exponent; check theta integrality, tangent normalization, and exact source/Lean provenance. |
| Q3 higher height | In progress | Separate one-dimensional formal summands from total height, then test whether local valuation entails theta-lift multiplicity. |
| Q4 archive | In progress | Read cote54 scans5–7 and cote4; distinguish restricted Lie power, Cartier duality and crystalline structures. |
| Q5 binomial/homotopy | In progress | Precisely formulate identity Frobenius lifts and homotopy theorem; distinguish finite differences from derivations. |

## Movement at 00:57 CET

- Q1: two independent derivations prove the scale-by-π logarithm estimate, with π^(p^h−1)=p. It gives an explicit factorial-minus-floor bound and equality at every p-power order. Coefficientwise operator composition then proves the stronger floor sum over indices not divisible by h.
- Q1: a further translation-operator relation is being checked. It predicts the uniform bound v_p(D^n f) ≥ ceil(n(1/(p−1)−1/(p^h−1))−(h−1)); this would remove the logarithmic loss. The proposed constant is forced by n=p^h−1 and f=t^n. This is not yet promoted to a final checked finding in this ledger.
- Q2: the note's step2 coefficient is p/(p²−1); Katz's exact stronger trace-zero theorem located, with its extra hypothesis. The supplied Lean map gives no exact local lemma identifier.
- Q3: total height is insufficient (product of multiplicative formal groups); local derivative valuations do not force generic-fibre vanishing (integral unit). A global comparison theorem would be needed for a shorter theta chain.
- Q4: cote54 zero p-power concerns the vector-group kernel, not the supersingularity of A. Oda Corollary5.11 supplies the historical de Rham/Dieudonné answer independently of RH.
- Q5: Horel's binomial-cochain reconstruction theorem located; a precise finite-difference/associated-graded divided-power bridge is being written.

## Approaches and checks retained

The `research/` directory holds agent reports, literature extracts and computations. Final statuses, exact statement IDs, check events, gaps and next steps will be reconciled before delivery. No citation located only from memory is promoted to an asserted theorem.

## Movement at 01:33 CET

- Q1 closed: DP1-DP4 prove the optimal finite-height affine slope and constant, complementary exact floor sum, both endpoints and normalization. Complete independent proof readings and224 exact-arithmetic checks passed.
- Q2 source gate closed:52 targeted modules match the original author archive byte for byte. The exact normalized theta, B0-B4, inverse-log, minor and period/path interfaces are located. No Lean compilation or RH audit was performed.
- Q3 narrowed: DP19 extends bounds under full lifted unramified CM action over ramified bases; DP20 gives a genuine linear-slope counterexample without it. DP22 constructs an actual height3 CM factor. DP21 andDP23 refute the unchanged-log and dual-product recipes; DP17-DP18 prove limits of pure coefficient replacement.
- Remaining Q3 gate: construct genuinely different admissible multivariate theta/period data and controlled-nonvanishing/denominator inputs, then prove a net cost reduction. Specific failed recipes are closed; unrestricted shorter-chain existence is not refuted.
- Q4/Q5 closed within stated source scope: DP10 recovers the classical restricted-Lie answer; DP11-DP14 give the precise binomial homotopy statement and failed naive identifications. Five transcription candidates are verified against exact source lines; original manuscript pixels absent.
- New DP19-DP24 proofs are integrated; their independent review records and exact remaining classical-background locators are being finalized. ThePDF build is undergoing layout verification. No three-hour review is due yet.

## Checkpoint01 packaged at 2026-11-21T00:35:05.353898+00:00

The first45-minute checkpoint contains all current report/audit files, complete mathematical research notes, computations and source recovery/verification metadata. No earlier checkpoint is nested. Source PDFs/archive parts and build caches are recoverable inputs/intermediates. Persistent-save confirmation follows in the continuing ledger.

## Checkpoint01 save confirmation

The persistent save succeeded for `DP_MULT_checkpoint_01.zip` (225,738 bytes, SHA-256 `711402b5aa254b3eeb466fe6eb8600a5acdcf1bae1a4276f9642db4787a63be5`). The completed transfer metadata was applied to the local file. It has not been overwritten, renamed or deleted. The next checkpoint is due at01:20UTC only if work is still ongoing.

## Further main-question movement at 2026-11-21T00:44:46.161554+00:00

The fresh finite-saving and host-type pass has located an earlier structural gate: `CMObj.typeP/typeM` impose types induced from the fixed quadratic CM field, and `IsTen` explicitly describes the Serre tensor with a CM elliptic curve. At inert primes those types alternate, giving slope1/2 even when the full CM field is enlarged. A distinct CM type is therefore required before a higher-height line can enter this construction. A second source constraint, `Ranks.m_even`, rules out deleting exactly one lift while retaining the existing rank type. These findings are being written and independently checked as DP25–DP27. A finite numerical ramp example nevertheless shows why a parity-compatible saving is not refuted by the coefficient estimates alone.

In parallel, a genuine q-typical logarithm/generalized-kernel route is being tested to determine whether the analytic estimate can be generalized separately from geometric realization. No shorter chain is claimed. The three-hour progress review is not yet due, and no no-movement stop rule has been invoked.


## Main-question movement at 2026-11-21T01:08:27.217185+00:00

- DP25–DP27 now prove the induced-type obstruction, a parity-compatible finite numerical saving, and the precise failure of literal chain truncation. Their complete proofs have been independently read against the actual source definitions.
- The scalar analytic gate has changed status. DP28 refutes the direct higher-height intermediate LemmaS with a full-hypothesis example; DP29 proves a valid replacement and a sharp nonzero example. DP31 proves the full c_h scalar estimate over W(k) by integral biextension trivialization. The inverse-limit, uniqueness and torus-normalization steps have received a complete root proof reading and are under an additional independent integrated review.
- DP30 computes the restricted Lie algebra of the actual dual: its p-map has rank h−2, so some primitive direction has a unit p-th derivative for h>2. It refutes assigning the line estimate to every dual direction. A fresh h3 actual-dual logarithm/derivative-sequence attempt is underway to test the asymptotic pairing gate; the order-p observation alone is not treated as an asymptotic no-gain theorem.
- The remaining main gate is now the genuine 1-by-(h−1) dual kernel with mixed CM type, its specified theta/minor/period data, and the global cost comparison. The two-scalar q-logarithm question is no longer open.
- Source identity was expanded to105 targeted files; all105 match the author archive. Byte comparison does not imply proof reading or Lean compilation.
- Public original pages for all five correction candidates were recovered and read. The autograph itself has the first four disputed readings; these are mathematical emendations of faithful transcription. The general exponent remains visually qualified. Earlier no-pixels log entries remain historical observations.
- Public recovery supplies exact binomial operations in cote153 PDFp3/archivep2 and extra PD-base data in cote136 PDFpp4–6/archivepp3–5. Twelve listed pages were read, not whole dossiers. No precise B7 transfer is supplied or proved.

The next scheduled checkpoint remains01:20UTC. The three-hour review is not yet due; no no-movement stop condition has been invoked.


## Actual-dual gate reduced at 2026-11-21T01:20:34.452623+00:00

DP32 now constructs the actual Cartier dual of the Honda line at every finite height h≥2, with an explicit integral logarithm. Finite freeness, F/V cancellation over F_p and the exact Lubin–Tate uniqueness theorem establish the model before any estimate is used. Its primitive directional slopes are p^i/(p^h−1), i=1,…,h−1; each is sharp and their sum is c_h. DP33 strengthens the height3 dual to optimal affine loss1 in both directions. Complete root proof readings passed, and independent whole-proof reviews are recorded or being merged.

This is further main-question movement: the actual dual's integral model and directional asymptotics are no longer missing. The remaining local gate is the primitive Poincare/theta cocycle and its prescribed frame/period/jet normalization. A concrete Zink-biextension construction and a source-specific theta-frame tracing attempt are now underway. No shorter global chain is claimed.


## Checkpoint02 packaged at 2026-11-21T01:20:53.367379+00:00

The second45-minute checkpoint captures all current authored deliverables, full research proofs and check/source-recovery metadata. Earlier checkpoint ZIPs are excluded and unchanged. The compiled PDF is a working build awaiting final cross-reference/layout QA. Persistent-save confirmation will follow in the continuing ledger.


## Checkpoint02 save confirmation

The scheduled checkpoint was created at2026-11-21T01:20:53.367379Z and saved successfully as `DP_MULT_checkpoint_02.zip` (1,046,616 bytes;94 entries; SHA256 `bdfa78c7e44587c2559e6d330d85811d0231647794bde7cb8351a89866d9a2fc`). Completed transfer metadata was applied to the local file. Checkpoint01 and checkpoint02 remain immutable. The next scheduled checkpoint is02:05UTC if work continues.

## Further main-question movement, 2026-11-21 02:03 UTC

- DP34 closes the all-height optimal affine-error problem for the actual dual: error1 in every displayed primitive direction, with a common sharp witness.
- DP35 proves bounded-denominator rigidity for compatible splittings, positive linear growth for a nonintegral splitting, and the precise primitive-initial-form multiplier criterion. The actual primitive Poincare class is constructed using the display pairing and compatible integral frames.
- DP36 proves a sufficient genuine-pair kernel estimate; DP37 determines the exact true dual torus action and constructs an invariant integral frame and rational logarithmic splitting. The existence of a primitive local kernel satisfying those analytic hypotheses is no longer a missing gate.
- DP38 computes both first primitive coefficients and unit mixed jets, with an exact invariant-splitting last-axis jet for h>2 and an integral local unit multiplier. Its full display proof has been read independently. A review caught an integration-only Witt-negation assertion at p2; the text now uses the correct Witt vector components and retains the corrected review history.
- The source trace identifies the actual normalized expression, integral exponential-conjugated connection, canonical-gauge independence, and J^e ordered-column theorem as supplied results. DP39 proves that full-series nonintegrality alone does not obstruct harmonic values, but the exact summed harmonic conditions also do not transfer the whole bare integral-function gain. Both overly broad shortcuts are closed by complete examples.
- Source inventory now contains526 modules, all byte-identical to the original14-part archive in a fresh sweep completed01:53:25UTC. The targeted reading scope is much smaller and is separately recorded. No Lean execution or RH audit is claimed.

The main Q3 gate is strictly smaller: identify the prescribed mixed-type theta expression, actual H_h/psi lattice, selected polynomial/minor module and geometric path with quantitative bounds; then construct the mixed-type global correspondence and prove a net integer lift saving. Basic actual-dual, primitive-kernel and integral-connection existence are no longer listed as missing. Concrete next attempts address the optimal primitive exponential weights and the combined CM-type directional budget. The latter is provisionally DP40 and is not yet asserted as proved.

The next scheduled checkpoint is02:05UTC. The three-hour review remains due02:50UTC; no no-movement review or stop has occurred.


## Checkpoint03 packaged at 2026-11-21T02:05:26.758950+00:00

Scheduled immutable full-report checkpoint. Current authored deliverables, mathematical research notes, proof snapshots, source identity/reading metadata and reproduction scripts are included. The PDF is a working build pending final layout QA. Raw recoverable third-party source PDFs, full archive parts, extracted Lean input files and build caches are not redistributed. No earlier ZIP is included. Persistent-save confirmation follows in the continuing ledger.


## Checkpoint03 save confirmation

The scheduled immutable checkpoint was saved successfully as `DP_MULT_checkpoint_03.zip` (1,467,052 bytes;147 entries; SHA256 `3965c53cb0321b3c085c981b1bc53b286a84db72322c03a3897ceef3254db094`). The returned transfer metadata was applied. Checkpoints01–03 remain unchanged. The next scheduled checkpoint is02:50UTC.

## Exact-source correction after checkpoint03

An independent whole-proof challenge of DP38 directly checked Zink's (196), p232, and (211), p236. His hex map uses the negative Artin–Hasse convention. The earlier positive convention gave reversed exact signs. The corrected primitive coefficients are (−1/p,+1/p), its first form is (−S^pY1+SYd^p)/p, and DP39(b)'s selected value is −(p−1)!/2. All asserted valuations and unit conclusions survive. The componentwise Witt-negation wording at p2 had also been repaired by using the vector w=−xi and only w0=−xi0. The corrected complete draft and integrated DP38 proof were reread and passed; the historical error-discovery and earlier snapshots remain preserved. Checkpoint03 predates the hex correction and is a working checkpoint, not the final paper.


## Main-question movement at 2026-11-21T02:32:51.709510+00:00

- DP40 is proved and independently whole-read: arbitrary-unit integral cyclic displays and actual duals have sharp directional slopes; the equally weighted type-plus-dual sum is maximal exactly for alternating type.
- DP41 is proved and independently whole-read: the entire primitive logarithm, exact uniform exponential inflation threshold p, and resistance to every nonzero bounded prefactor are established.
- DP42 is proved and independently whole-read: every primitive mixed logarithmic line in the unramified actual pair has exact factorial slope 1/((p−1)(p^k+1)), governed by restricted-p nilpotency length; the maximum rho2 does not increase with h. Exact logarithmic congruences and nonzero prefactors are covered.
- DP43 is proved with author and root complete readings; an additional independent review is in progress. It gives the optimal codimension affine error and periodic floor sum in every cyclic eigendirection, with one common sharp monomial.
- Main paper now contains all four full proofs. The integrated fragments receive separate preservation reviews; no source identity check is called Lean verification.

The remaining Q3 gate excludes these now settled local families. It requires the actual mixed-type theta/connection/selected-operator/path identification and a global net lift-cost inequality. Concrete next routes are the geometric Jacobian cyclic model, the exact smaller-rank/source interface, and whether the primitive path theorem transports to general unramified CM forms. The three-hour review remains due02:50UTC; no review or stop is claimed early.


## Scheduled three-hour progress review — 2026-11-21T02:50:47.371408+00:00

Conservative work start23:50UTC on20November; this is the first actual review at approximately three hours. It is not a retrospective or simulated elapsed-time claim.

### Main questions and strongest current gates

| Main question | Current state | Strongest proved reduction |
|---|---|---|
| Q1 formal-group bound | Proved | DP1–DP4: coefficientwise optimal affine slope and constant h−1, complementary exact floor sum, h1 and infinite-height endpoints. DP43 further gives codimension error for cyclic CM displays. |
| Q2 step2 | Proved with exact scope | Height2 gives the scalar coefficient; the actual source theta/gauge/period/path/denominator comparisons are identified. It is not a height-only theorem about an arbitrary normalized theta expression. |
| Q3 higher height and fewer lifts | Local theorems proved; global saving open | DP40–DP48 settle general cyclic directional sums/errors, primitive mixed-line radii with arbitrary unit arrows, polarized trace-one normalization and quadratic gauge. DP44 rebuilds smaller even rank/HC/host/Spaces inputs; new endpoint periods, selected local data and the net global inequality remain. |
| Q4 archive/Cartier/crystals | Proved within stated source scope | Boxed zero is the universal extension's vector kernel; Oda/Cartier give the classical comparison. Scalar valuation estimates do not by themselves supply crystal descent/connection. Autograph corrections distinguished from transcription errors. |
| Q5 binomial/homotopy | Precise mathematical statement proved; one source/prior-run comparison row open | Torsion-free identity Frobenius/binomial equivalence, numerical-polynomial divided-power graded algebra, and Horel's derived nilpotent finite-type reconstruction are established/cited exactly. The extra historical/B7 comparison is separated below. |

### Every currently open question row

| Row | Status | Current gate |
|---|---|---|
| Q3e | current gate | Actual cyclic CM models, optimal directional/codimension bounds, arbitrary-unit primitive mixed-line slopes, and the polarized trace-one hyperbolic pullback are proved. Rational quadratic gauges cannot improve those line slopes. The old rank/HC/host and generic Spaces data can be rebuilt at any smaller even m>=2; a new endpoint period and its integral ties are the next nonautomatic fields. For a mixed CM family, construct its actual selected theta/connection/minor/path data, controlled nonvanishing and global links, then compare actual gain and full costs. Equal-direction sums and primitive ordinary lines are settled local families; arbitrary harmonic selections and the net integer lift saving remain open. |
| Q5e | source mapping partly proved; comparison remains a current gate | Exact binomial/plethystic and PD-base locators recovered by bounded visual reading. No precise B7 comparison was supplied or established. Specific plethysm passage in133 and relevant theorem in137 remain unlocated in inspected pages; not all cotes date to1976. |

### Movement assessment

**Movement: YES. Consecutive no-movement reviews: 0.** Relative to the initial ledger, Q1/Q2/Q4 and the precise mathematical Q5 statements changed from open to proved/refuted. Q3 reduced from an unspecified higher-height formal/kernel mechanism to explicit integral models, exact primitive radii and gauge formulas, plus concrete endpoint/selected-data/cost interfaces. This meets the user's movement definition independently of packaging or side observations.

Concrete work continuing: DP49 is a local polarized Jacobian/nonzero-path application under proof review; the nonunit theta tensor parameter is being investigated; the actual selected harmonic/global endpoint comparison remains active. A renewed targeted autograph search is assigned for the unresolved cote133/137 locators. No missing B7 statement is invented.

The next progress review is due03:50UTC. The two-consecutive-no-movement stop condition has not occurred. The separate scheduled checkpoint04 is due now; next checkpoint05 will be03:35UTC if work continues.


## Checkpoint04 packaged at 2026-11-21T02:50:48.066527+00:00

Scheduled immutable full-report checkpoint. Current authored deliverables, mathematical research notes, proof snapshots, source identity/reading metadata and reproduction scripts are included. The PDF is a working build pending final layout QA. Raw recoverable third-party source PDFs, full archive parts, extracted Lean input files and build caches are not redistributed. No earlier ZIP is included. Persistent-save confirmation follows in the continuing ledger.

## Checkpoint04 persistent-save confirmation

The immutable checkpoint `/workspace/scratch/97b2cc84526f/DP_MULT_checkpoint_04.zip` was created at2026-11-21T02:50:48.066527+00:00 and successfully saved. Size2138898bytes;270entries;SHA256`57148d47f8d3722e6bdead18213c11c4cd17ecde2b844164f29265876d600e05`;Library identity`libfile_fde3_f-207bd97f7b848191b36792f3b5100547_3de54532f60c8191850458563edee173`. Returned Library identity metadata is attached to the local ZIP and was rechecked at02:54UTC. No checkpoint was overwritten. The next checkpoint is due03:35UTC; the next progress review is due03:50UTC.


## Post-review movement through DP51 — 2026-11-21T03:20:48.136807+00:00

DP49–DP51 are integrated with complete proofs and actual whole-proof checks. DP49 realizes the polarized theta germ on the actual genus-three Jacobian and proves nonzero restrictions in every primitive residue class. DP50 determines nonunit tensors and their exact source-level normalization loss. DP51 settles the sharp universal polynomial/harmonic rate, with a new complete corollary proof and separate final-version checks. The actual geometric section/weight data and net cost comparison remain open.

The historical source-search part of Q5e is proved: actual pixels now locate cote133 archive5 and26–28, and cote137 archive37–38. Q5e was split transparently: its historical question is closed, while the exact unsupplied B7 comparison is carried forward as Q5f. This split does not claim that the B7 comparison was proved or refuted.

Current merged records:267 check events and64 question rows. The open rows are Q3e and Q5f. Work continues on the actual endpoint-period construction, the full prime redistribution with unequal fixed derivative orders, and finite-jet realization by global algebraic theta sections. This is a work entry, not an early scheduled progress review, and does not change the consecutive-no-movement counter. Next checkpoint05 remains due03:35UTC; next progress review remains due03:50UTC.


## Post-review movement through DP53 — 2026-11-21T03:33:06.189735+00:00

DP52 and DP53 are integrated with complete proofs and actual author, root and independent whole-proof readings. DP52 constructs the previously open mixed-type finite-class endpoint period and Gram identity, narrows the remaining nonvanishing problem to the prescribed theta image, and proves the exact six-input induction and smaller-parameter transport. DP53 closes prime redistribution for globally fixed unequal derivative orders and integer floor certificates. This strictly narrows Q3e; it does not settle a net shorter lift chain.

Current records: 301 check events, 66 question rows,578 source modules. Open rows remain Q3e and the unsupplied B7 comparison Q5f. DP54 finite-jet globalization is undergoing independent review and is not yet a main-paper finding. This is a work entry, not an early scheduled progress review; consecutive no-movement reviews remain0. Next review03:50UTC, checkpoint05 due03:35UTC.


## Checkpoint05 packaged at 2026-11-21T03:35:00.064997+00:00

Scheduled immutable full-report checkpoint. Current authored deliverables, mathematical research notes, proof snapshots, source identity/reading metadata and reproduction scripts are included. The PDF is a working build pending final layout QA. Raw recoverable third-party source PDFs, full archive parts, extracted Lean input files and build caches are not redistributed. No earlier ZIP is included. Persistent-save confirmation follows in the continuing ledger.
