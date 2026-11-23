# Research ledger

## Session opened: 2026-11-23 02:00 Europe/Berlin (01:00 UTC)

Task: audit the six attached research runs, reconstruct their result register,
resolve the named research gates, and write independently editable mathematical
papers with reproducible proof and literature records. The attached archive was
unpacked once into `source/`; no earlier conversation is used.

The archive contains 3,955 files, 54,444,826 uncompressed bytes, matching the
prompt's per-directory counts. It contains no `QUESTIONS.tsv` or `STATEMENTS.tsv`.
Result registration therefore starts from current TeX statements, current
reports, historical check events, and the intakes. Historical claims and checks
are evidence; they do not constitute checks in this session.

### Initial division of work

- Root: Paper 1, consolidated records, build/release controls, and independent
  checks of selected statements from the other papers.
- `papers_2_3`: Papers 2 and 3 and their registers; independent statement-only
  attacks on Paper 4.
- `paper_4`: Paper 4 and its register; independent statement-only attacks on
  Paper 1's vanishing, Picard invariance, and boundary theorem.
- `papers_5_6`: Papers 5 and 6 and their registers; independent statement-only
  attacks on Paper 1's arithmetic and mixed-characteristic counterexamples.

All workers use GPT-6 Astra with inherited reasoning settings. No human check
is asserted. A proof attack counts as an independent re-proof only if it
actually produces a complete argument before exposure to the source proof.

### Gates on opening

| Paper | Gate |
| --- | --- |
| 1 | Arithmetic quadratic-step construction, exhaustive certificate, source locators, literature; general finite-flat torsor purity; wild cohomology calculation. |
| 2 | Universal-section classification and characteristic-two root cover; a published proof/input for F11; F8/F10. |
| 3 | Exact functor axioms, counterexample and pro-modular representability, publication history after Murre. |
| 4 | Compare every claimed EGA error with original text and errata; validate nonlocal lifting and transfinite construction. |
| 5 | Integral torsion specialization lemma and exact scope of cycle/correspondence statements. |
| 6 | Global gerbe and inverse-limit cohomology calculations; determine whether the proposed note adds a statement beyond the literature. |

### Checkpoint and review schedule

First checkpoint is due at approximately 02:45 Europe/Berlin (01:45 UTC), then
every 45 minutes. No checkpoint is created before a scheduled time. Each is a
new complete ZIP of work products and records, excluding unchanged source files,
external literature, and earlier checkpoint ZIPs. The first mathematical
movement review is due at approximately 05:00 Europe/Berlin (04:00 UTC), then
hourly, using the stopping rule in the prompt.

### Initial findings

- Published general finite-flat torsor purity was located online; exact
  hypotheses and locators are being checked before closing the gate.
- The Paper 4 worker located EGA III/2's own erratum to III 4.3.6. This rules out
  presenting that correction as a new correction.
- The remote workbench format URL could not be opened by the search tool in the
  first attempt. No claim of exact format-1 compliance has yet been made.


## 2026-11-23 02:38 Europe/Berlin — substantive progress before checkpoint 01

- All six projects have compiling drafts; Paper 6 is expressly a comparison
  note because Milne's published results cover the proposed new theorem.
- Paper 1's original 111,784-assertion certificate reran successfully. A new
  permutation-action program made 37,889 checks by a different method.
  The ray-class step and limit-ring proof have been rechecked. General
  finite-flat torsor purity is located in Marrama (2026), Theorem 6, p.433,
  attributed to Moret-Bailly; this closes the named purity-input gate.
- Root rederived the characteristic-two surface construction from geometric
  data without its proof: the dimensions 210+186+160=556 come from filtration
  and Riemann–Roch, independently of the matrix certificates. The resulting
  invariants 562,1,565 and very ampleness agree. Universal polarization
  sections also have a separate quadratic-refinement/monodromy re-proof.
- EGA III 4.3.6's correction is already in EGA III/2 errata. Kleiman (1979),
  pp.203–204, already gives the two meromorphic-function examples. These are
  credited as known. The lifting assertion, nonlocal adic deformation and
  transfinite presentation are the active Paper 4 claims.
- The cycle torsion relation now has an independent core argument and a
  targeted check of its Albanese-spreading and Bloch-specialization bridges.
  The complete universal Lefschetz range and Jacobian bounds have separate
  derivations from statement/construction data and named published inputs.
- The cohomological-dimension conjecture is on cote31 archive sheet84,
  PDF page85. Archive sheet85 is a reversed unrelated draft page. Paper1's
  locator is corrected. Similar sheet/scan distinctions are recorded for
  cotes14,22,23,128,131 by the responsible readers.
- The global working register has 1,612 rows before report-alias reconciliation;
  that count is not asserted to be a count of distinct mathematical results.
  Historical checks have not been promoted to current checks.
- Remaining principal gates: current full F8/F10/F11 proof audit and published
  dependencies; separate complete re-proofs of representability/open-modularity
  and every-rank descent; separate full A16 proof; wild-affine separate re-proof;
  exact novelty comparisons for the arithmetic, polarization, root-cover,
  representability, and gcd deductions; report/register alias reconciliation.
- The remote format1 specification was fetched successfully. Permanent WB
  numbers and remote commits await the owner's filing step; none is invented.

This is an interim progress record, not the three-hour movement review.

### 2026-11-23 02:41 Europe/Berlin — a further literature decision

L6c is known: Ishii–Yoshida arXiv2410.15282v3, Corollary1.4,p3, proves
exactly the normal-source/regular-target first-direct-image vanishing, even
in every characteristic. Primary PDF opened and hashed. The paper now cites
that theorem instead of repeating the proof; our alternative positive-
characteristic proof is moved to the records. This is a change of literature
status, not a claim of a new mathematical result.

## Scheduled checkpoint 01 — 2026-11-23 02:45 Europe/Berlin

Snapshot name: POLISH_ALGEBRAIC_GEOMETRY_checkpoint_01.zip. The snapshot
contains all six compiling drafts (12,8,17,10,13,5 pages), editable sources,
deposit sheets, current records and computational artifacts. Paper1's PDF
incorporates the newly located Ishii–Yoshida attribution. The separate full
wild-affine re-proof, including the all-coefficient upper bound from
Gabber–Orgogozo Theorem6.1, was completed immediately before this snapshot.
The canonical Paper2/3 register was just reconciled and is included.

This is a checkpoint during active work, not a finished or deposited release.
The next scheduled checkpoint is03:30 Europe/Berlin (02:30 UTC). The
three-hour mathematical movement review remains05:00 Europe/Berlin.


## 2026-11-23 03:25 Europe/Berlin — mathematical movement before checkpoint02

Checkpoint01 was successfully saved at the scheduled time: ZIP SHA-256
fe47b7e98788776bd80b47737a065d860afa12d49279c964152a54902bc9d805,
manifest SHA-256 52e35e268beed24c0a6d306f3cdec1b25def3be618c2148f94cdfd5d3f96eb53.
It has not been overwritten, renamed, or included in a later archive.

- Paper1: the full separate wild-affine reproof and all-coefficient source
  checks are closed. The four boundary assertions now have a complete
  statement-only reconstruction; the author compared it and adopted its
  fixed-curve connectedness proof. SGA4 X Theorem2.2,p46 and Corollary4.4,p57
  close the arithmetic upper-bound source gate. The full arithmetic separate
  proof still needs extension beyond the already completed quadratic step.
  Li–Wang2026 Corollary4.6,p7 makes the Picard assertion a known consequence;
  it is now credited accordingly. Ishii–Yoshida vanishing remains known.
- Paper2: F8 has a full independent proof and reciprocal comparison, with
  published source gates closed. F10 and F11 have full separate derivations,
  author comparison and published inputs, replacing the preprint dependency.
  F11's independent proof uses a fixed unramified abelian cover and purity
  for prime-to-p coefficients, followed by finite-group counting.
- Paper3: the every-rank descent theorem has a complete separate proof and
  author comparison. All representability text received a full targeted
  adversarial check. A separate checker derived the four algebraic auxiliaries
  and is attacking actual local modularity through additional statement-only
  locus lemmas. This is still an independent-proof gate, not an asserted
  gap in the written proof. The henselized counterexample also awaits a full
  separate statement-only derivation; a fresh brief has been prepared.
- Paper4: nonlocal adic Cohen lifting has a full separate derivation and
  reciprocal comparison, including the pro-cotangent and inverse-limit steps.
  The final ten-page draft has explicit expert and newcomer full readings,
  source/PDF hashes and all-page visual review in FINAL_READS.md.
- Paper5: the premise-sharpness statement now has a complete separate proof.
  Exact prior overlap of the scalar correspondence lemma is credited to
  Scavia–Suzuki; the low-dimensional gcd bounds are presented as quantitative
  consequences of known geometric constructions. Voisin2024 and
  Beckmann–deGaayFortman2023 comparisons are recorded.
- Paper6: all proposed main assertions are known from Milne. In obedience to
  the instruction to write a sixth research paper only if it adds a result,
  the final release will have five admitted research papers and a Paper6
  disposition/comparison record. The current compiling comparison remains
  through checkpoint02; it will then be moved out of the papers directory.
- The SA05/SA06 canonical register now includes the previously missed labelled
  remarks:468 rows. Historical evidence comprises3274 deduplicated source
  check events and645 narrative intake entries, kept distinct from current
  checks. Paper2/3 canonical reconciliation remains540 rows, with148 unmatched
  report results explicitly marked as possible aliases, not distinct theorems.

This is an interim ledger entry. The scheduled three-hour movement review
remains05:00 Europe/Berlin (04:00 UTC); no no-movement review has yet occurred.


### Checkpoint02 preparation, 23November2026

The canonical consolidated register has1613 rows and95 current check events.
The148 unmatched report entries remain explicitly unresolved as possible
aliases; this is not a count of distinct certified theorems. Six falsely
classified supplemental question rows were removed after a status-word audit,
without removing their mathematical result rows. The current standalone
PDFs have12,17,17,10,14,6 pages respectively. The Paper6 comparison is retained
for this checkpoint only; its final research-paper disposition is known.


## Scheduled checkpoint02 — 2026-11-23 03:30 Europe/Berlin

Snapshot: POLISH_ALGEBRAIC_GEOMETRY_checkpoint_02.zip. This is the second
complete scheduled snapshot, with all six current compiling projects,
updated registers, exact source comparisons, independent proof records,
and computational certificates. It is not a final release. The next
checkpoint is04:15 Europe/Berlin (03:15 UTC), and the first mathematical
movement review remains05:00 Europe/Berlin (04:00 UTC).

## 2026-11-23 04:12 Europe/Berlin — movement before checkpoint03

Checkpoint02 was saved successfully at its scheduled time. Its ZIP SHA-256
is72fa33ef51aa9757797a9b0d326defa81d224b0cf225f28aeb4aade2e828e289;
its manifest SHA-256 is1e93fecee796d152aeb4e3e967800920ba6909a92fa585519c5882e788a94d82.
Neither earlier checkpoint has been overwritten, renamed, deleted or nested.

- The complete arithmetic counterexample now has a separate same-model
  reconstruction, including noetherianity of the infinite tower, every finite
  extension's two-primary Brauer vanishing, the all-coefficient dimension bound
  and persistent Picard growth. Reciprocal comparison passed. Popescu2022,
  section5,pp511–512 already gives the eventual-inertness Dedekind construction;
  the paper now credits it and identifies the extra dyadic and class-group
  controls used here. The Picard-scheme proof has also received a complete
  separate reconstruction; its known status from Li–Wang is unchanged.
- The modularity-locus theorem and Murre analogue have a complete independent
  reconstruction and reciprocal comparison. The henselized counterexample
  has a complete reconstruction of scalar descent, arbitrary fpqc descent,
  all eight axioms and nonrepresentability, with reciprocal comparison PASS.
  That reconstruction used separately requested scalar and auxiliary lemma
  statements; their proofs were reconstructed without reading the author's
  proof. This assistance is disclosed. An additional fresh, unaided attack
  from the main statement is being arranged; the assisted derivation is not
  relabelled as unaided. A different reader's earlier exposure to the proof
  is recorded and excludes that reader from a fresh blind claim.
- Paper5's full integral Albanese specialization theorem now has a complete
  separate derivation, including the whole-relation torsion lemma and the
  Albanese/cohomology bridge. The author's adversarial comparison passed.
- Paper4 has its two complete reads and all-page review on the final
  ten-page version. The input finite certificates were rerun successfully.
- The proposed sixth research paper has been moved to the records as an
  editable six-page comparison. Its assertions are known from Milne; there
  are five admitted research-paper projects.
- The canonical register now has1524 atomic result/question/documentary rows
  and114 current check events. These are inventory counts, not counts of new
  or currently certified theorems. All report aliases have been reconciled.
  The global question table is still being rebuilt from genuine source
  questions: the previous scrape includes headings and timing records, and
  three statements whose title contains 'open' have explicit proved status.
- Paper1's latest fresh-copy PDF has13 pages and no warnings or overfull
  boxes; its latest all-page review is in progress. Papers2/3 are receiving
  final source-credit and method-note updates, with corresponding fresh
  builds and renewed page review. Paper5's final read records are in progress.

This is an interim movement entry. The first scheduled mathematical movement
review is still05:00 Europe/Berlin (04:00 UTC); there have been no no-movement
reviews. Checkpoint03 is due04:15 Europe/Berlin (03:15 UTC).

## Scheduled checkpoint03 — 2026-11-23 04:15 Europe/Berlin

Snapshot: POLISH_ALGEBRAIC_GEOMETRY_checkpoint_03.zip. This third complete
scheduled snapshot contains the five current standalone research papers,
the editable known-gerbe comparison, the canonical register and newly
reconciled per-paper questions, independent derivations and reciprocal
comparisons, source retrieval records, and computational certificates.
The global question-table reconciliation and final reading records remain
active work. A fresh separate instance has started the strict unaided main-
statement-only counterexample attack and has seen only the two statement
briefs. This is a checkpoint, not a final release. The next checkpoint is
05:00 Europe/Berlin (04:00 UTC), also the first mathematical movement review.

## 2026-11-23 04:55 Europe/Berlin — preparation for first review

Checkpoint03 was saved successfully at its scheduled time. Its ZIP SHA-256
is e29e63be794dab620d6911a1601845c0dca1e1c6ab1b8d23632e33933590d98e;
its manifest SHA-256 is 498c1dd2fc76149d333400a8ce7a360d2fd8718087e7848d8c63b9a0cf9a0b9d.
No earlier checkpoint has been changed or included inside a later one.

The uniform tame-coefficient theorem now has a complete fresh unaided proof
from the main statement, frozen before manuscript access. Both comparisons
passed. The new proof uses leading logarithmic differentials and formal
functions; the manuscript uses the Frobenius cokernel and nearby cycles.
The counterexample's fresh scalar-descent attack remains active. The fresh
modularity/representability attempt proves formal and finite-chart steps,
but original-base global openness and assembly remain open in that attempt;
a second unaided approach is active. Earlier auxiliary-assisted full checks
remain accurately labelled and are not replaced by claims of fresh closure.
A further fresh arithmetic check now starts without the seed or auxiliary
lemma statements used by the earlier complete reconstruction.

The ordinary Igusa correction has a full root proof and exact primary-source
comparison, with original certificates rerun and a different matrix method.
It proves flatness of Pic-tau for the specified ordinary deformations and
the first-order Pic-var/Albanese-lifting obstruction. No supersingular claim
or miniversal-hull algebraization is certified. This dossier stays outside
the five papers.

All five current paper PDFs and the known-gerbe comparison have two complete
reads and all-page visual reviews. The record assembly now reconciles the
question aliases, restores the missing manuscript-date question, gives every
paper its statement/event/source tables, and supplies the mathematical
dictionary. These editorial and packaging changes are not mathematical
movement under the stopping rule. No formal hourly review has yet occurred.

## Formal mathematical movement review 01 — 2026-11-23 04:00:01 UTC

MOVEMENT since the opening ledger. The named general finite-flat purity gate is closed by the exact published theorem of Marrama, with the finite-torsor Picard deduction checked. The preprint-dependent abelian ramification step is replaced by the published Kato theorem in its Bright–Newton restatement and a complete derivation, closing that input gate. The ordinary Igusa flatness and first-order obstruction dossier is now fully checked in its stated ordinary scope. These are mathematical/input status changes; inventory reconciliation, PDF review, a second proof of an already checked result, and packaging are not counted. Consecutive no-movement reviews: 0. The next formal review is 2026-11-23 05:00 UTC / 06:00 Europe/Berlin.

The complete row-by-row review is in workbench/records/progress_reviews/review_01/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.

## Scheduled checkpoint04 — 2026-11-23 05:00 Europe/Berlin

Snapshot: POLISH_ALGEBRAIC_GEOMETRY_checkpoint_04.zip. This complete fourth scheduled snapshot contains the five current standalone papers, the known-gerbe comparison, 1526 canonical result rows, 428 canonical questions, 135 current check events, the first complete movement review, the main-theorem exposure matrix, and all newly completed proof and source-comparison records. The fresh unaided counterexample, representability and arithmetic attacks remain active. The next checkpoint is 05:45 Europe/Berlin (04:45 UTC). This snapshot is not a final release.

Checkpoint04 saved successfully at 04:00 UTC. ZIP SHA-256: ef742b286db96bbb2d98d73b39395fbcc915b9ffcef5c97bf66f8c969510576c. Manifest SHA-256: de3bff0c28519cc01c0e65e8ce36180a31814acfdca2cce7633538871d3d58c6. The saved ZIP is immutable; this receipt is recorded for the following snapshot.

## 2026-11-23 05:40 Europe/Berlin — current mathematical and checking changes

The exact open smooth-torsor exclusion SA14_SA19:A2Gs-cross is now closed. A smooth projective surface cannot contain a smooth ample curve D together with a line subbundle O(-D) of its tangent bundle tangent to D. The proof derives K.D=0 and c2=-D², then uses surface classification and an explicit ruled-surface intersection contradiction (and a connection argument in characteristic zero). Its finite-flat group-scheme torsor corollary is now Proposition6.1 and Corollary6.2 of Paper2. The full root proof, primary-source checks and new symbolic intersection program are returned. No matching source certificate for this new exclusion was found, and no unrelated certificate is substituted. The general Picard-group point kernel remains open. This exact open-row status change qualifies as mathematical movement at the next hourly review; formatting and additional proofs of already checked theorems do not.

The arithmetic main theorem now has a complete fresh existential-statement-only reconstruction, with no construction or auxiliary aids, and a full root comparison PASS. It uses Q(i), independent rank growth from several ramification primes, and an all-coefficient Leray proof. The pro-modular criterion likewise has a complete fresh main-statement-only proof and full root comparison PASS, with its own assembly argument. The separate ordinary-(7) proof has reported a potential complete reduction and is being written and frozen; it is not yet marked comparison-PASS. The arbitrary-base fpqc fresh reconstruction remains open, although excellent and certain nonnoetherian nilpotent-thickening cases are independently established. A genuinely fresh context worker now attacks the numerical existential surface theorem; the earlier construction-data reconstruction remains accurately labelled. A reused worker with uncertain compacted exposure was excluded before starting that task.

The new smoothness result and recent opened literature context are incorporated into the papers. Paper2 now has20pages, Paper3 has18, Paper4 remains10; all three changed projects were built from fresh copies with no overfull boxes or unresolved references, read completely in expert and newcomer modes, and visually inspected on every page. Papers1 and5 and the known comparison are unchanged from their already reviewed versions. The register contains1527 rows,142 current check events and428 canonical questions; these are inventory counts, not counts of certified theorems. Crosswalks now record current printed page/statement numbers and explicit check-file paths, including the new proposition and corollary. Every standalone version has a generated file manifest. No permanent tag, remote commit or deposit identity is invented.

A numerical error in the abelian-surface row of the opened Liedtke author version is documented only in CORRECTIONS_FOR_AUTHORS.md: coherent and etale Kunneth computations give chi(O)=0 and b2=6. The c2=0 entry used by our proof is correct. The published chapter's table was not separately inspected, so the correction is explicitly limited to the inspected author version. No author was contacted.

The next immutable checkpoint is05:45 Europe/Berlin (04:45UTC), and the next formal movement review remains06:00 Europe/Berlin (05:00UTC). The consecutive no-movement count is0.

## Scheduled checkpoint05 — 2026-11-23 05:45 Europe/Berlin

Snapshot: POLISH_ALGEBRAIC_GEOMETRY_checkpoint_05.zip. This complete fifth scheduled snapshot contains all five current standalone papers, the known-gerbe comparison, the new smooth-torsor obstruction and exact source correction, the current register and crosswalks, and all independent proof records. Immediately before the snapshot the ordinary-(7) fresh proof was frozen and passed a full root comparison; its exact record is ROOT_L1_FRESH_COMPARISON.md. The arithmetic, ordinary-modularity and pro-modular strict checks are now complete. The unrestricted fpqc and existential surface strict attempts remain active. There are1527 canonical rows,144 current check events,428 canonical questions, and54 numbered research-paper statements in the current crosswalk. The next checkpoint is06:30 Europe/Berlin (05:30UTC). The next formal movement review remains06:00 Europe/Berlin (05:00UTC). This is not a final release.

Checkpoint05 saved successfully during its scheduled04:45UTC minute. ZIP SHA-256: `3ca714f3fe31a9a4e27e78e0481f8d7634247ad7c32f94b4a55b86ff55caf79a`. Manifest SHA-256: `0d77823a35d2a941f7107d0c556ebb47ff4e6b3ddc8ad4e0d3ff75b1d3cc837b`. The archive contains274files and7545207bytes and remains immutable. This receipt is for the next snapshot; the saved archive is not edited.

## Formal mathematical movement review 02 — 2026-11-23 05:00:19 UTC

MOVEMENT since review01: canonical open row SA14_SA19:A2Gs-cross is now closed in its exact smooth-projective surface/tangent-subbundle scope, with the finite-flat torsor consequence. The full proof is Paper2 Proposition6.1 and Corollary6.2; ROOT_SMOOTH_TORSOR_CHECK.md and the separate symbolic intersection program record the checks. This reduces the explicit canonical open-question count from31 to30. The general Picard-point question remains open. Fresh independent proofs of arithmetic, modularity and pro-modular representability, the differential exclusion of an incompatible published example premise, certification of the inherited fourfold/finite-obstruction reduction, literature comparisons and packaging are not counted as further mathematical movement. The strict arbitrary-base fpqc and numerical-surface existence-only checks remain active. Consecutive no-movement reviews:0. Next formal review:2026-11-23 06:00UTC /07:00Europe/Berlin. Next immutable checkpoint:2026-11-23 05:30UTC /06:30Europe/Berlin.

The complete row-by-row review is in workbench/records/progress_reviews/review_02/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.

## Scheduled checkpoint06 — 2026-11-23 06:30 Europe/Berlin

The sixth complete scheduled snapshot contains all current papers and records. The fresh existence-statement-only surface proof is complete and passes full root comparison; its correct relative-duality formula replaces a false dual-symmetric-power display without changing the theorem. The arbitrary-base fpqc counterexample likewise has a complete fresh statement-only proof and root comparison, including a direct original-base propagation argument and nonrepresentability by any separated scheme. Both papers have newly compiled PDFs; changed-version expert/newcomer and all-page reviews are underway, so the preceding complete QA claims apply only to their recorded earlier versions. Paper1’s new boundary example has full two-read/all-page QA and a separate symbolic check.

A late post-freeze comparison has reopened the ordinary-(7) modularity-openness proof and the current manuscript positive-criterion dependency: completed-base modularity cannot silently be used as original-base modularity. Two workers are checking the literal axiom, a potential polynomial-base counterexample to openness, and an independent positive-criterion assembly that may avoid the step. These are unresolved at this snapshot; earlier PASS claims do not override records/CURRENT_PROOF_GAPS.md. No false proof is certified finished. This is not yet counted as movement; the next formal review is06:00UTC /07:00Europe/Berlin.

The next scheduled immutable checkpoint is06:15UTC /07:15Europe/Berlin. Consecutive no-movement reviews remain0 after review02. No unchanged input files or external-source copies are included.

Checkpoint06 was saved during its scheduled05:30UTC minute. It contains292files and7747408bytes. ZIP SHA-256: `ec82dedc13df81138eb217cea076dcbf09372792f11aa7aded9248401b4b4017`; manifest SHA-256: `9aa3b3c3542879c2c359ad5b782d3f90b3b02a8f289ab0d1958e7f807ceca7c6`. The archive is immutable.

## Formal mathematical movement review 03 — 2026-11-23 06:00 UTC

NO MOVEMENT since review02 under the stated rule. Every one of the30 canonical open questions and61 source open-scope rows has been reviewed. The new boundary purity/smallness formulation and the restricted clean cyclic-cover calculations do not close an open row or prove a strictly smaller general sufficient gate. The fixed-base modularity-openness statement has been refuted and replaced by an explicitly relative theorem, correcting a previously claimed closed result; it is not counted as an open-row closure or used to reset the research clock. The relative positive criterion retains its independent assembly proof. Strict independent checks of the expanded counterexample and relative openness remain active. Fresh surface/fpqc reconstructions, reciprocal comparisons, all-page PDF reviews and packaging are checks rather than movement. Consecutive no-movement reviews:1. Next formal review:2026-11-23 07:00UTC /08:00Europe/Berlin. Next immutable checkpoint:2026-11-23 06:15UTC /07:15Europe/Berlin. Research continues until the next review; a second consecutive no-movement review will stop new research and trigger final checking and delivery.

The complete row-by-row review is in workbench/records/progress_reviews/review_03/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.

## Scheduled checkpoint07 — 2026-11-23 06:15 UTC / 07:15 Europe/Berlin

The seventh complete scheduled snapshot contains the current five papers and known-result comparison, all proof and source records, and the third complete movement review. Paper2 and Paper3 now both have complete current-version expert/newcomer readings and all-page visual checks. The expanded fixed-base adic counterexample has a frozen statement-only reconstruction, full root comparison, and reciprocal comparison, all passing. The henselian counterexample reciprocal comparison and dated literature receipts are frozen and complete.

The first isolated relative-openness attempt is frozen as NOT PROVED, with its valid reductions and failed approaches preserved. Its author continues a separate attempt without exposure to the manuscript proof; a second independent worker has received only the same exact statement brief. The relative-openness strict checking gate therefore remains open. The E4 continuation contains a proposed standard zero-dimensional-fibre consequence; its novelty and whether it reduces an inherited gate are not accepted or counted pending comparison. Consecutive no-movement reviews remain1. The next formal review and next scheduled checkpoint are07:00UTC /08:00Europe/Berlin. This is not a final release.

The scheduled snapshot is being packaged immediately after resuming the active task at06:15:49UTC; its actual save timestamp will be recorded separately. No earlier checkpoint is changed or included.

Checkpoint07 saved successfully at06:16:32UTC, about92seconds after its scheduled time. It contains325files and7992139bytes. ZIP SHA-256: `af760b638d6229c29188c126889547eb3deba552cee37de302ff9142605090ce`; manifest SHA-256: `f65ad7c68e2ebdd0e8e76473f4fcc2fbd9ef7e32b95b37f73658ec16b2e3c9a0`. Its saved identity is libfile_d576947f35b88191b07d6b3ca0cae201. The ZIP is immutable; this receipt belongs to the next snapshot. The remaining schedule is unchanged.

## Formal mathematical movement review 04 — 2026-11-23 07:01 UTC (scheduled07:00UTC)

MOVEMENT since review03: the explicitly inherited E4 higher-dimensional abelian-torsor construction, including positive-dimensional polarization kernel over a nonnormal base, is closed by the arbitrary-base scheme pushout theorem and its full Picard-scheme corollary. The source gate is E4_schematicity_attempts.md, lines81–93; the new full proofs are Paper2 Theorem1.2, Corollary1.3 and Lemma3.1, with full root proof/source comparison in ROOT_E4_TRANSFER_COMPARISON.md. This is a strict narrowing of the general E4 normal/integral-family gate, not a solution of general E4; both canonical general questions remain open. A separate statement-only reconstruction is active, so its checking gate remains explicit. The standard zero-dimensional-fibre observation, corrections, fresh openness reconstructions, reciprocal comparisons, PDF review and packaging are not counted as movement. All30 canonical open questions and61 source open-scope rows were reviewed. Consecutive no-movement reviews:0. Next formal review:2026-11-23 08:00UTC /09:00Europe/Berlin. Next scheduled immutable checkpoint:2026-11-23 07:45UTC /08:45Europe/Berlin.

The complete row-by-row review is in workbench/records/progress_reviews/review_04/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.

## Scheduled checkpoint08 — 2026-11-23 07:00 UTC / 08:00 Europe/Berlin

The eighth whole snapshot includes all five current papers, the known-gerbe comparison, the full new abelian-torsor pushout and Picard proofs, and all four formal movement reviews. The24-page Paper2 has complete current-version full expert/newcomer and all-page visual checks; the new abelian-torsor theorem-only independent reconstruction remains active. Relative openness has one frozen independent proof with full root comparison and a frozen reciprocal PASS; the other isolated reconstruction is now frozen as complete and awaits root comparison. Paper3 has a clean freshly compiled19-page PDF after two precise wording corrections; its changed-version visual and newcomer review is still pending, and earlier full QA remains tied to its earlier recorded hash. The general E4 questions remain open, with their abelian-torsor subcase now removed from the residual gate. Current canonical tables contain1537results,179checkevents,428questions,64crosswalkrows and58numberedresearchstatements. This is not a final release.

The scheduled snapshot is being packaged after the context resume at07:00:54UTC; its actual save timestamp is recorded separately. The next checkpoint remains07:45UTC; no earlier snapshot is changed or nested.

Checkpoint08 saved at approximately07:02UTC, after the scheduled boundary. It contains357files and23889056bytes; ZIP SHA256 `5bb19fe72b78c65f1b503833cf03d9428b85795a11342d9b03d4a8198e3f25db`, manifest SHA256 `6d2db7b80c600173116f64878fe390dbb1a2b555a12f712456b7d1a3d451290e`, saved identity libfile_22428f843bf08191b7e2f635e2b5d828. Packaging audit immediately found an error: a fresh worker had put downloaded primary sources and extractions in a nested tmp directory inside its records directory, and the package script included them. This breaches the no-source-copy packaging requirement. The immutable snapshot is not altered, replaced or supplemented; the caches are being moved out of the deliverable and the packaging filter is being hardened for subsequent scheduled and final ZIPs. This packaging error does not affect the proof versions or mathematical review decision.


## Scheduled checkpoint09 — 2026-11-23 07:45 UTC / 08:45 Europe/Berlin

This ninth complete scheduled snapshot contains the five current standalone papers, the known-gerbe comparison, all189current check events,1537canonical result rows,428questions,64crosswalk rows and58numbered paper statements. All current main theorems now have completed genuinely statement-only reconstructions with full root comparisons. The newest abelian-torsor reconstruction and its full reciprocal comparison are frozen; root read both in full, with PASS. Exact approximation and full-Picard citation refinements are applied. Paper2 is24pages, PDF SHA256fa8029769c67ed5fc3f8c0c222b502f45b538b84e03d3cf697ce1d07f4ffb2a4. Paper3 is19pages, PDF SHA256454550c7429426d14c5e05cf19548e03ce59a5643c896d10f9cccc20e9e1c586. Both have complete current expert/newcomer reading and all-page visual coverage, and zero warnings, unresolved references or overfull boxes. The other papers are unchanged from their complete reviewed versions.

The new projective-modification obstruction for abelian-surface torsors was frozen by its author at07:42:54UTC. It is a proposed complete proof, not yet root-accepted: root comparison and a genuinely unexposed statement-only attack are now in progress. The A2 continuation supplies a quasi-elliptic route exclusion and exact generic conductor calculation, also still awaiting root primary-source comparison. Neither proposal is counted as accepted movement or silently incorporated into a finished theorem. The general E4, Picard-point and full local-group questions remain open. The bounded-genus curve-degeneration route leaves its extension/patching step unresolved. Published-page confirmation of the existing Cotner–Zavyalov correction is a source-locator update only.

The checkpoint08 source-cache packaging error is documented above and its immutable archive is unchanged. Current packaging rejects source/cache directories, unapproved PDFs, full retrieval payloads, unchanged input copies and nested ZIPs. The next immutable checkpoint is08:30UTC /09:30Europe/Berlin. The next formal movement review is08:00UTC /09:00Europe/Berlin; consecutive no-movement reviews remain0 after review04. This is not the final release. The exact save time and immutable archive receipt will be recorded after creation.

Checkpoint09 was created at07:45:01UTC and saved during the scheduled07:45UTC minute. It contains369files and8384983bytes. ZIP SHA2567bbbd11853676a992cec0f2d486e76b142fc817c231b7a2d788709886619cc99; manifest SHA2569de9a811008cc808a6fa88f52b47175b0e42d4a5dbbe062604012f3afe69e579; saved identity libfile_a97c79d4b00c8191ac23752ebe04cfc3. It passed the strengthened no-source-copy and integrity validation. The archive is immutable; this receipt belongs to the next snapshot.

## Formal mathematical movement review 05 — 2026-11-23 08:00:45 UTC (scheduled08:00UTC)

MOVEMENT since review04: the inherited projective-modification construction for a nonschematic abelian-surface torsor is excluded when its scheme source remains proper, flat and finitely presented with geometrically integral fibres. Both fibrewise birationality and an ordinary dense-isomorphism-open modification suffice. The complete root proof/source comparison is ROOT_E4_MODIFICATION_COMPARISON.md; the exact inherited gate is E4_schematicity_attempts.md lines95–104. This strictly narrows the previously recorded modification route, while higher-dimensional targets, projective bundles and the general E4 normal/integral-family questions remain open. The separate source audit is frozen PASS, identifies the known rank-one construction, and makes no priority claim. The genuinely unexposed statement-only reconstruction and the expanded Paper2 PDF review are still active. The completed abelian-torsor reciprocal check, A2 quasi-elliptic route exclusion and generic conductor calculation, the source typo dossier and packaging are not counted as further movement. All30 canonical open questions and61 source open-scope rows were reviewed; their general statuses are unchanged. Consecutive no-movement reviews:0. Next formal review:2026-11-23 09:00UTC /10:00Europe/Berlin. Next immutable checkpoint:2026-11-23 08:30UTC /09:30Europe/Berlin.

The complete row-by-row review is in workbench/records/progress_reviews/review_05/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.

## Scheduled checkpoint10 — 2026-11-23 08:30 UTC / 09:30 Europe/Berlin

This tenth complete snapshot contains five standalone research papers and the known-gerbe comparison,1545canonical result rows,204current check events,428questions,70crosswalk rows and64numbered research statements. These are inventory counts, not a count of distinct new theorems. All current main statements have completed genuinely statement-only same-model reconstructions and full root comparisons. The new abelian-surface modification theorem also has a complete frozen reciprocal manuscript/source review, read entirely by root with PASS. Its citation precision is applied: the AF step uses Raynaud's exact assertion; the redundant BLR alternative was removed. No theorem hypothesis changed.

Paper2 is now33pages,544454bytes, PDF SHA25613ef80588f15e256a9557a4aca9b9673e06b9c2aabef680e0e16e557cb7740f4. Its six live TeX inputs match the isolated three-pass build. All pages have complete expert/newcomer and visual coverage, with documented byte-identical carryover and full rereading/inspection of every changed page. There are zero warnings, unresolved references or overfull boxes. Paper3 and the other PDFs are unchanged from their fully checked current versions. The new Section9 proves the quasi-elliptic ampleness restriction and singular-general normalized-cover conductor identity, including its equality and strict-defect consequences. These are auxiliary constraints; the general geometric Picard-point kernel remains open. Their algebra was recomputed symbolically and by finite annihilator calculations, with geometric hypotheses checked separately.

The further equality-case group-torsor construction is a frozen PROPOSAL pending root assessment, not a newly accepted paper theorem. Its proof and source receipt are included with that status. General E4 schematicity, its projective-bundle and higher-dimensional-modification routes, and the full local fundamental-group question remain open. The latest projective-bundle attempt obtains a relative divisor but not relative ampleness or a finite flat multisection. The canonical question table was reconciled with the already completed surface checks and the previously proved fixed-base openness refutation/relative repair; this bookkeeping is not new mathematical movement.

Review05 at08:00UTC found movement from the accepted surface-modification obstruction. Consecutive no-movement reviews remain0. The next formal mathematical review is09:00UTC; the next scheduled immutable checkpoint is09:15UTC. No extra or replacement snapshot is created. Source/cache, unchanged input, unapproved PDF, full-retrieval-payload and nested-archive exclusion checks apply. This is not a final release. The exact archive and persistence receipt will be recorded after creation.

Checkpoint10 was created during the scheduled08:30UTC minute and saved by08:30:20UTC. It contains409files and8733108bytes. ZIP SHA256f7b800f2713c4e7a7023691a61232ab9c8b778239b6df55ff10f222ff974fabf; manifest SHA256760a846eb0dfc9993524febf19b10e05ecb5b3b44b3671963ca318170d52b380; saved identitylibfile_0891c2e20e408191961d40e1199329ee. It passed the hardened payload-exclusion and integrity checks. The archive is immutable; this receipt belongs to the next snapshot.

## Formal mathematical movement review 06 — 2026-11-23 09:02 UTC

MOVEMENT: the inherited projective-bundle construction over a nonschematic abelian torsor is now proved impossible over every normal base, including nonnoetherian normal schemes. The remaining construction gate is strictly smaller: nonnormal bases only. Complete frozen proof E4_PROJECTIVE_BUNDLE_NORMAL_PROOF.md and full root proof/primary-source comparison ROOT_E4_NORMAL_BUNDLE_COMPARISON.md are PASS. The separate statement-only reconstruction is active and will not be credited until completed; the theorem will enter the manuscript before the next checkpoint. General E4 remains OPEN. The A2 equality-action, singularity and plurigenus formulas are checked auxiliary refinements and are not counted as general-gate movement. F13 formal-patching and uniform-resolution complexity gates remain unchanged. Consecutive no-movement reviews: 0.

The complete row-by-row review is in workbench/records/progress_reviews/review_06/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.

## Checkpoint11 preparation, 09:13 UTC; scheduled save09:15 UTC

Review06 at09:02 records movement: the projective-bundle construction over normal bases is excluded in every rank and every relative dimension, with arbitrary normal bases reached by explicit approximation. Full frozen proof and root complete proof/primary-source comparison pass. The theorem and three auxiliary statements now enter Paper2 Section5, with complete proofs. The strict separate main-statement-only reconstruction has confirmed no proof exposure and is active; no finished claim is made for the new main theorem.

The three A2 equality-action, singularity-defect and plurigenus additions have full root checks, complete separate targeted audits and a frozen reciprocal manuscript/MRT comparison, all PASS and fully read. A further Ekedahl equality reduction is frozen as a proposal only and is under full root/separate primary review; it is not promoted into the paper. The F13 continuation is documented in ROOT_RESEARCH_CONTINUATION_06.md and leaves its gate unchanged. An adjacent source assertion in Milne Remark8.5 is under separate targeted verification; no correction is asserted yet.

Paper2 was rebuilt from a fresh seven-input source copy in three pdfLaTeX passes:44pages,611511bytes,SHA256 d35112a31615233baa88a078a8825aa350c4f2139a10e7184b4a3a00ef37a3d2, no warnings, unresolved references or overfull boxes. The current expanded PDF visual and newcomer readings are in progress; the preceding38page version was fully accepted. The new proof source has been read in full by author and root.

Next mandatory checkpoint after11:10:00UTC. Review07 is also due10:00UTC. Consecutive no-movement reviews:0 after Review06. Continue research and finish the outstanding independent/full-reading gates; the stop rule has not fired. No attached or published source copies are included.

Checkpoint11 inventory after reconciliation:1552registerrows,213checkevents,428canonicalquestions,77crosswalkrows,71numberedresearchstatements,0unresolvedaliases. Twelve current Paper2 pages (1–4,14–20,44) were individually inspected before the checkpoint; the remaining32are explicitly pending.

Final pre-save coverage update09:14:45UTC: current Paper2 pages1–20 and44 individually viewed and fully read; remaining23pages21–43 pending. Checkpoint11 is scheduled for09:15UTC, with creation gated against the clock.

Checkpoint11 saved at09:15UTC:443files,9025295bytes,SHA256 1d2aeff16f89de83119e136e1a4fb77a45e3560b3624e4b0c073a1f4f3d77e19; manifestSHA256 0ce7c27bd4eb11fb85f39ea46e2b2764dc27c5400ef09b31639216ed8bc5ae62. Immutable persisted ZIP identifier libfile_33eaa4d888ac8191834eb7b347efc3e3. Previous checkpoints untouched. Next checkpoint12 due10:00UTC.

## Equality-case reduction accepted and source corrections —09:36UTC

The a=1 equality branch of the smooth-surface Picard-kernel investigation is now reduced, by an exact application of Ekedahl I.2.4(ii), to almost-ruled surfaces or a characteristic-two surface with ample canonical bundle, chi=1, square canonical relation, and normalized Kummer cover with rational double points and K3 resolution. Root independently rederived every step and read the complete primary proof and the entire separate350-line frozen audit; all pass. The normalized cover is identified over X, and every numerical bound is checked. The expanded proof is integrated in Paper2; reciprocal manuscript review and a clean PDF build remain pending. General A2, a>1 and strict inequality remain open. This is an attributed application of a published theorem, not a priority claim. Review07 at10:00 will evaluate the precise gate movement.

Milne Remark8.5's asserted product decomposition is refuted by an explicit smooth elliptic curve in characteristic two; root and an independent targeted worker derived the counterexample and verified original/current editions. Two inverse signs in Ekedahl's printedp112 proof are corrected using the canonical formula and finite-flat norm; the stated theorem is unaffected. Both issues go only to the corrections dossier. No author was contacted.

The normal-base projective-bundle main theorem remains under strict statement-only reconstruction. The44-page pre-Ekedahl PDF has now been fully read and visually inspected; the changed manuscript is being rebuilt. No new checkpoint is made before10:00UTC.


## 09:53 UTC — current checked expansion before the scheduled checkpoint

The complete49page Paper2 fresh build is accepted after full expert/source checking and a complete newcomer reading from all49 individually viewed pages; the truncated image call was replayed. PDF SHA256 `3f7838669ca4a005e29a9d0b44d4fc319b4b222dfa09c589f6b942ab43a590f7`; all eight inputs match. The Ekedahl a=1 equality reduction has both complete exposed targeted and reciprocal comparisons frozen PASS and fully read. Four further conditional K3 refinements have complete root proof/source checks and independent local-algebra recomputation; the separate auditor is still active. They do not themselves close a question. The normal-base theorem's strict main-statement-only worker has maintained isolation and is still attempting its remaining bridge. Milne's p-torsion product assertion is refuted by the independently checked elliptic example and a separate secant formal-group computation; the two Ekedahl inverse-sign errors and both bounded errata searches are recorded only in the correction dossier. A proposed ample example does not settle the requested very-ample question. Its construction and a possible exclusion under very ampleness remain unproved research until fully checked. No checkpoint ZIP was created early.



## 09:59 UTC — final checkpoint12 build state

The two K3 reciprocal precision edits are incorporated in a new fresh three-pass49page PDF, SHA256 2dee980e926c4124c7faba86f47e44633d506563939c2c26fcf92f5959ced08e,647752bytes. All eight inputs match. Exactly pages37and49 changed; both were individually viewed and fully read, while the other47are image-byte-identical to the fully reviewed predecessor. Full current expert/newcomer and visual gates PASS. The separate254line K3 targeted audit and full sourceJSON are frozen PASS and fully read by root; reciprocal final reporting remains active. Canonical counts:1559registerrows,230checkevents,428questions,82crosswalkrows,76numberedresearchstatements,zero unresolved aliases. These are inventory counts, not distinct-theorem counts. Checkpoint12 is due10:00UTC and will include all own work with no nested archives or source copies.

## Formal mathematical movement review 07 — 2026-11-23 10:00:01 UTC

MOVEMENT: the smallest-equality surface branch of A2 is now proved, by a fully checked application of Ekedahl I.2.4(ii), to reduce to almost-ruled surfaces or characteristic-two canonical surfaces with chi=1 and the specifically identified normalized K3 cover. This is a strict structural narrowing of the preceding a=1 equality gate, with complete root proof/source and separate targeted/reciprocal comparisons PASS. Both alternatives remain open; a>1, strict inequality and the general high-dimensional Picard-point question remain unresolved. The four further K3 structural refinements are not counted as additional movement. The ample-example proposal and possible very-ample exclusion are unproved and are not counted. The normal-base main theorem retains its pending independent reconstruction gate. E4 over nonnormal bases and F13 remain unchanged. Consecutive no-movement reviews: 0.

The complete row-by-row review is in workbench/records/progress_reviews/review_07/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.


## Checkpoint12 saved and subsequent10:02UTC state

Checkpoint12 was created at the scheduled10:00UTC boundary and saved successfully:478files,9319433bytes,SHA256 87892ce0543515ac294b459b84ea24c8bf07cc71545a6040a2c3e216198031ba; manifestSHA256 d72b34c715f8743cffbca1c57735a5925912854dc9ac16959a54ab78a6fd080f; LibraryID libfile_69bf3cf9176c8191b5c051c1db8db3e1. It is immutable and will not be replaced. Next scheduled checkpoint:10:45UTC. Review07 at10:00:01UTC recorded MOVEMENT from the proved Ekedahl reduction; consecutive no-movement reviews remain zero. Next hourly review:about11:00UTC.

After the checkpoint, the complete74line K3 reciprocal report and both receipts were frozen and fully read by root. All four exact auxiliary check gates are now closed, with no further manuscript change. The normal-base main-theorem statement-only reconstruction remains a separate pending requirement; a new fully isolated statement-only worker normal_bundle_unaided2 was launched with no proof hints or project-record exposure. The earlier independent worker is freezing its honest NOT PROVED attempt, not a counterexample. Very-ample exclusion research is still active and uncounted until full proof/source checks.


## 10:25UTC — very ample equality branch narrowed and current manuscript reviewed

Root completed the full frozen very-ample proof/source comparison and a different-method exact arithmetic check. The K3 branch is excluded for a smooth very ample curve in the smallest equality case; only almost ruledness remains there. The separate ample construction remains frozen UNPROVED, and the high-dimensional/general point-kernel question, higher conductor exponents and positive defects remain open. The three supporting statements are now in Paper2, whose fresh51page PDF and all nine inputs are accepted, with complete expert/newcomer and page coverage. PDF SHA256 `e186b2dd21b97a324db2368fc66deb95dd5aae31dd1c68c613117a2329174bd7`. The separate exposed auxiliary audit is still active. The normal-base theorem's first strict attempt remains frozen NOT PROVED; its exposed audit and the second strict attempt are separately tracked. No early checkpoint archive was created. Next scheduled checkpoint remains10:45UTC; next progress review approximately11:00UTC.

## 10:34 UTC — audit closure and exact remaining reconstruction gate

Both very-ample auxiliary audits are frozen PASS and fully read by root: targeted 300 lines and reciprocal 125 lines, plus complete source/freeze receipts. No manuscript change is required; the fully reviewed current 51-page PDF remains e186b2dd21b97a324db2368fc66deb95dd5aae31dd1c68c613117a2329174bd7. The normal-base theorem's complete exposed audit also passes and has been fully read. The second independent attempt is honestly frozen NOT PROVED, alongside the first; root has read both complete reports. A third main-statement-only worker remains isolated and active. No exposed result is relabeled as a fresh re-proof.

The proposed extension through finite normalization and uniform affine boundaries remains unproved exposed research. The remaining very-ample almost-ruled equality branch is also under a new exposed attack. No new result or hourly movement is claimed for these attempts. Next scheduled checkpoint remains 10:45 UTC; next hourly review about 11:00 UTC. No archive was created early.


## 10:44 UTC — checkpoint13 preparation

Canonical inventories contain1562 register rows,245 current check events,428 questions,85 crosswalk rows and79 numbered research statements, with zero unresolved aliases. These are inventory counts, not counts of independently certified theorems. The very-ample auxiliary targeted and reciprocal checks are closed, and both failed strict normal-bundle attempts remain honestly recorded. The third isolated attempt is still exploring. The nonnormal-base extension is an exposed candidate whose complete author-proof/source comparison has not yet occurred; its working proof and exact status are preserved with the research records. The current Paper2 remains the completely reviewed51page PDF. Known FGA221 Lemma3.5 polynomial-sign errata are recorded as known only. The second strict reconstruction's frozen hashes all matched; root made its files read-only without changing content. Payload validation created no ZIP and found no forbidden source copies or nested archives. The scheduled checkpoint is10:45UTC, the next hourly mathematical review is about11:00UTC, and the last no-movement streak remains zero.


## Checkpoint13 saved at the 10:45 UTC boundary

Checkpoint13 was created at10:45:00UTC and saved successfully:513 files,9497266 bytes,SHA256 5e5efa57f1e92abe6b8d251e435f32966d359c7de9dc420f6b082342b5f711b2; manifestSHA256 4c2885f063057c0fc5fd21185f58a15b514967bd6ad97a4404d0d704f3cd703e; LibraryID libfile_0dbb4f4909308191977f356e11603d17. Post-save hash verified and archive made read-only. It will not be replaced or included in later archives. The next scheduled checkpoint is11:30UTC, and the next hourly movement review is about11:00UTC.

At cutoff the nonnormal-base projective-bundle argument is still explicitly a candidate awaiting complete frozen-proof/source comparison; its current working proof is included. The author has since reported a complete written proof and is finishing the source/freeze receipt. This report alone does not promote the result. The isolated normal-base reconstruction and exposed almost-ruled attack remain active.

## 10:59 UTC — arbitrary-base bundle proof accepted and integrated

The complete frozen proof over arbitrary schemes now passes root's full proof/primary-source comparison. Uniform boundaries over finite normalization and projective Picard-class torsors supply the simultaneous affine neighborhoods missing from the normal-only reduction. The stronger theorem and all supporting proofs are installed in Paper2; the abstract, introduction and residual question now state the arbitrary-base scope. This excludes the entire inherited projective-bundle construction, not general E4 or higher-dimensional modifications. A fresh strict main-statement-only reconstruction is active. The earlier normal-only third attempt remains unexposed and is preparing its own candidate. A different-method exact algebra check passes412assertions. Fresh build and complete changed-PDF readings are next; no finished claim is made before those gates. The next checkpoint remains11:30UTC.

## Formal mathematical movement review 08 — 2026-11-23 11:02:01 UTC (scheduled about11:00UTC)

MOVEMENT since review07: the very-ample smallest-equality branch of A2 is reduced to almost ruledness, because the K3 alternative is excluded by the complete root-checked embedding obstruction with separate targeted and reciprocal audits PASS. For merely ample curves both alternatives remain, and a>1, positive defects and the general point-kernel question remain open. Independently, the inherited projective-bundle construction over nonschematic abelian torsors is now excluded over arbitrary schemes, closing the residual nonnormal-base gate left at review06. The full frozen argument and primary sources have complete root comparison PASS in ROOT_E4_NONNORMAL_COMPARISON.md; its complete manuscript is integrated and a clean55page fresh PDF is built. Strict main-statement-only reconstruction, the exposed audit and current PDF readings remain explicit checking gates. General E4 and higher-dimensional modifications remain open. The newly frozen almost-ruled distinguished-cover refinement is still under root comparison and is not counted. Known errata, failed reconstruction attempts, source verification, numerical corroboration and packaging are not counted as movement. Consecutive no-movement reviews:0. Next hourly review:about12:00UTC. Next immutable checkpoint:11:30UTC.

The complete row-by-row review is in workbench/records/progress_reviews/review_08/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.

## 11:08UTC — distinguished-cover refinement integrated

The complete frozen almost-ruled proof and all source receipts pass root comparison. In the ample Picard-kernel setup, every degree-p purely inseparable ruled cover identifies with the particular normalized mu_p cover of M. Thus the very-ample equality corollary now forces that normalization birationally ruled, with kappa minus infinity on smooth models, while X is not birationally ruled. The complete proof and field-intersection refinement are in the manuscript. Singularities away from the inverse-image curve still block the earlier smooth ample obstruction. A separate auxiliary check and the new expanded PDF readings remain pending. Review08 at11:02:01UTC already recorded movement; no extra review or checkpoint is made. A reversed ideal quotient in Stacks0AGS is recorded only in the correction dossier; its theorem is unchanged.

## 11:24UTC — new full audits and57page build

The complete N-all exposed audit and distinguished-cover exposed targeted/reciprocal audit are frozen PASS and have been read entirely by root, including source receipts and freeze records. Their hashes and exact exposure distinctions are preserved. Root has individually viewed and fully read all57pages of the ten-input fresh build; expert/visual gates PASS, separate complete newcomer reading pending. The third isolated normal-only proof is frozen PROVED and passes full root mathematical comparison by a different numerical argument; full numerical-criterion primary-source completion remains pending. The arbitrary-base isolated reconstruction is still active. These are checking advances, not extra progress reviews. Next scheduled whole-deliverable checkpoint remains11:30UTC; next hourly movement review about12:00UTC.

## 11:26:30UTC — complete Paper2 readings closed

The separate newcomer-perspective reader completed all57pages of the exact fresh build, including references and method. Root read its full frozen report/receipts and verified every page, source and PDF hash. Expert, newcomer and individual visual coverage all PASS. No further TeX edit was required. This completes the PDF review, not the still-pending arbitrary-base main-statement reconstruction or the normal-only numerical-source supplement. The scheduled11:30checkpoint will contain the current57page paper and these exact distinctions.

## Checkpoint14 cutoff — scheduled11:30UTC,23 November2026

This complete own-work snapshot contains the current five research projects and the known-Milne comparison for the sixth topic; no new Paper6 is claimed. Paper2 is the fully reviewed57page version, SHA2568e4628806289f197f45c3346be2517e6be3b58713838f3c1143257c027d2e159. It contains the arbitrary-base projective-bundle theorem and the distinguished ruled-cover refinement with full proofs and full root/separate exposed audits. Every current PDF page has expert, separate newcomer and individual visual coverage. The canonical register has1570rows,262currentcheckevents,428questions and89crosswalkrows, subject to any explicitly recorded final additions before the scheduled packaging call; those are inventory counts, not counts of distinct verified theorems.

Remaining checking gates are exact and visible: the first isolated arbitrary-base reconstruction reports no complete proof or counterexample yet and is freezing its honest attempts; the third normal-only isolated proof passes complete root mathematical comparison but its numerical ampleness primary-source supplement is still being completed. A second arbitrary-base isolated task has been assigned to the author of that normal-only proof, with only the stronger main statement and permission to use its own previously independent work. No proposed arbitrary-base proof or auxiliary hint has been sent to either isolated worker. The source supplement is an exposed source check, not an independent re-proof. Original unsuccessful attempts remain preserved.

General A2 and E4 and the other recorded main gates remain open at their strongest checked reductions. Review08 at11:02:01 recorded mathematical movement and reset the no-movement streak to0. The distinguished-cover refinement accepted after that review is preserved for the next hourly comparison; it has not caused an extra review. Next hourly movement review about12:00UTC. Next checkpoint after this scheduled snapshot:12:15UTC. No checkpoint is created early, no previous ZIP is replaced or nested, and no original attachment or published source copy is included. The packaging call and durable-save receipt verify actual creation externally; this entry records the snapshot's scheduled cutoff.

## Normal-only reconstruction fully checked — 2026-11-23T11:46:16.177764+00:00

The third isolated normal-base projective-bundle reconstruction now passes the complete root mathematical and primary-source comparison. Its frozen exposed source supplement was read in full, all45path/hash receipts matched, complete numerical/Bertini/field-projectivity proofs were read, and relevant attached EGA overlaps were reread. The normal-only gate is CLOSED. The original Kleiman1966 article remains unobtained; full alternative published proofs are identified honestly. The first two failed isolated attempts remain unchanged. The stronger arbitrary-base theorem still requires a successful isolated reconstruction. A new different-method Koszul Euler computation passes36symbolic assertions. No TeX was changed; the fully reviewed57page Paper2 remains current. A further attached-edition cocycle-order notation correction is in the dossier only. These are checking advances, not an extra hourly movement review.

A metadata-edit script first used the wrong register field name and stopped while writing. Before any canonical assembly, root restored the entire46-row ROOT_REGISTER.tsv byte-for-byte from immutable checkpoint14 (SHA256064190127c4f28aa22ec313d35f56fd779b99a40aebbee9a80588a54bb427318), then validated the intended47-row replacement in memory and installed it atomically. No mathematical record or prior checkpoint was lost or changed.

## First all-base isolated attempt frozen unresolved — 2026-11-23T11:54:13.405446+00:00

The first exact-main-statement-only arbitrary-base reconstruction froze UNRESOLVED at11:47:06UTC. Root read all five files, including the6,027word report and complete1,022line source audit, and verified every frozen file and43source snapshots. The record is preserved as unsuccessful, not a counterexample. A third fresh isolated task began from the main statement alone; the second, based only on its own earlier independent normal-base proof, reports a candidate while completing its audit. Neither candidate nor ongoing task is counted as completed proof. The12:00movement review and12:15scheduled checkpoint remain due.

## Formal mathematical movement review 09 — 2026-11-23 12:00 UTC

MOVEMENT. Since review 08, the accepted distinguished-cover theorem strictly narrows the smallest very-ample conductor-equality gate: the particular normalization of the order-p torsion cover is birationally ruled, X is not ruled, and its ruling field A satisfies A intersect k(X)=A^p and A k(X)=k(N). This result passed full root and separate exposed proof/source comparisons and is installed in the fully reviewed current Paper 2. The earlier gate required only the existence of some ruled degree-p cover. No general A2 resolution is claimed. The positive-genus fibration refinement is still a candidate awaiting freeze and root source comparison and is not counted here. The normal-base isolated source closure, the first unresolved all-base reconstruction, the two active reconstruction attempts, PDF reviews, source-edition corrections and packaging are checking or documentation changes, not mathematical movement. All 30 explicit open questions and 61 source open-scope statuses were reviewed; only A2 changes the mathematical gate, while the two E4 rows have checking-status updates. Consecutive no-movement reviews: 0. Continue research; next review about 13:00 UTC.

The complete row-by-row review is in workbench/records/progress_reviews/review_09/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.


## 23 November 2026, 12:13 UTC — checkpoint15 preparation

The positive-genus refinement was accepted by root after complete frozen-proof and source reading at 12:05 UTC, after review09. Its manuscript is integrated; the fresh expanded PDF review gates are pending. The separate exposed audit reports PASS, final receipts pending root reading. The second all-base isolated reconstruction is frozen PROVED; root source validation remains open, so its verdict is not yet adopted. Review09 at12:00 was MOVEMENT with streak0; next review13:00. Checkpoint15 remains scheduled for12:15 UTC.


## Checkpoint15 saved, 12:15:16 UTC

Created at12:15:00.000420 UTC, saved and exact post-save hash verified. ZIP604files10111227bytes; SHA25682d7e81ef66855e052f5e8210d4dc91c0106780b3d62b2da371b67660b8e6a52; manifestSHA256e44311d864eafcb0c34cf3677f2e5046038041e426d9da71e7776570c023533c; native filelibfile_0fafa3d80b50819193180a043f32cdc7. Immutable, no prior archives nested. Next scheduled checkpoint16 at13:00 UTC. Final62page rebuild after two precision edits has SHA2560eaddcd8c4bee8427403bfdac916915da9ba1068e61cab41ca5f94792fd6620e; all full-PDF reading gates pending for that new exact hash.

## Post-checkpoint15 audit closure — 2026-11-23T12:36:53.130716+00:00

Root accepted the complete separate positive-genus proof/source audit, the reciprocal manuscript comparison and its post-edit precision addendum. All213 hash occurrences in the manuscript/newcomer identity verification pass. The complete newcomer text reading applies only to the62page PDF0eaddcd8; root expert/all-page visual review and any later rebuild remain explicitly pending. The third arbitrary-base isolated reconstruction is frozen UNRESOLVED and fully read by root; its failed converse is preserved without false proof credit. The second isolated attempt has a complete root mathematical reading and awaits the post-freeze primary-source supplement for its cohomological ampleness lemma. No additional mathematical movement is claimed for packaging or review closure.

## Before scheduled checkpoint16 — 2026-11-23T12:58:01.812516+00:00

The second arbitrary-base projective-bundle reconstruction source gate is closed; all45supplement/original/source hash occurrences pass, with its own prior normal-case exposure disclosed and the first/third failed attempts preserved. Root also accepted the complete global degree filtration, general-conductor Euler formula, rational-cover singularity defect and characteristic-two positive-genus exclusion. The last strictly narrows A2 to a rational distinguished cover in that equality branch; the defect is at least p-1 in characteristic p not3 and obstructs extension. Full proofs were installed before this checkpoint. All64combined new-proof/source hash occurrences pass and55156different-method exact arithmetic cases pass. Separate fresh main-statement workers are active for characteristic-two rationality and the degree filtration. Full final69page expert/newcomer/visual reviews remain pending; archived reviews are not transferred. Source bytes remain excluded.

## Formal mathematical movement review 10 — 2026-11-23T12:59:15Z

MOVEMENT. Since review09, the positive-genus fibration/RDP/cohomology/fibre refinement was accepted12:05, strictly narrowing the distinguished-cover gate. Subsequently the global degree filtration closed its explicit inherited gap and proved positive nonrational singularity defect/nonextension in the genus-zero branch for p not3. The characteristic-two positive-genus branch of smallest very-ample equality is excluded, leaving a rational distinguished cover and nonruled quotient. These are strict mathematical reductions; source-checking completion, PDF rebuilding and packaging are not counted. General A2 and the remaining singular rational-cover configuration stay open. Consecutive no-movement reviews:0.

The complete row-by-row review is in workbench/records/progress_reviews/review_10/REVIEW.md, with frozen OPEN_QUESTIONS.tsv and REGISTER_OPEN_SCOPE.tsv. Their statuses and strongest gates are incorporated in this ledger by reference. No source-only reduction is claimed as a new proof.
