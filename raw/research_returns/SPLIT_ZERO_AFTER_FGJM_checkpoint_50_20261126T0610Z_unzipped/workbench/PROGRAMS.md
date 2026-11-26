# Programs, commands, and expected outputs

Tested Python: 3.12.14. Numerical/symbolic packages in this environment: sympy 1.14.0, mpmath 1.3.0, matplotlib 3.10.8. The SMT search additionally uses a discoverable Z3 shared library through ctypes.

Run the mathematical programs from the workbench directory. Commands overwrite their own replay outputs, so use a separate extracted copy when preserving an immutable version. Expected mathematical data are in the named returned certificates; elapsed times and paths need not reproduce byte-for-byte. This catalog is documentation, not another computation event.

## Mathematical calculations and independent replays

| Program and exact command | Expected certificate under checks/ | Expected mathematical outcome |
|---|---|---|
| `python programs/paper1_exhaustive.py --output checks/paper1_certificate.json` | `paper1_certificate.json` | Exhaustive finite congruence, ideal and projective-image fields agree; no assertion is a substitute for the general proof. |
| `python programs/paper1_iterated.py --output checks/paper1_iterated_certificate.json` | `paper1_iterated_certificate.json` | All finite chain and repeated-zero image checks pass. |
| `python programs/paper1_two_level.py` | `paper1_two_level_certificate.json` | Square-zero kernel test is true and all rank cases pass. |
| `python programs/paper1_finite_lattice_projectives.py --output checks/paper1_finite_lattice_certificate.json` | `paper1_finite_lattice_certificate.json` | 19152matrices;6402idempotents;1038nonprincipal nonzero-label occurrences;0failures. |
| `python programs/paper1_finite_group_projectives.py` | `paper1_finite_group_certificate.json` | Ranks1/2:5/235idempotents,2/146fixed birth occurrences,1/91nonzero fixed births,4/416nonfixed births. |
| `python programs/root_finite_group_pair_replay.py --output checks/root_finite_group_pair_replay.json` | `root_finite_group_pair_replay.json` | PASS; all preceding counts and the full image-cardinality histograms agree by a different method. |
| `python programs/paper1_rank_three_crosscheck.py` | `paper1_rank_three_crosscheck.json` | Word-reduction trace and initial dimension-table checks agree with their recorded exact data. |
| `python programs/paper1_rank_three_search_candidates.py` | `paper1_rank_three_search_candidates.json` | The three specified searched candidates pass the separate word-formula replay. |
| `python programs/paper1_bottom_counterexample.py` | `paper1_bottom_counterexample.json` | 10000associativity equalities;1000trace containments;6167total supported-zero weights;0in the bottom cell. |
| `python programs/paper1_rank4_minor_replay.py` | `paper1_rank4_minor_replay.json` | Four modular determinants274637; norm988208, prime1000003, selected minor size114. |
| `python programs/paper2_zero_motion.py --roots 5 --steps 100` | `paper2_zero_motion_summary.json` | Heuristic continuation only; compare recorded centres, not an interval-proof verdict. |
| `python programs/paper2_interval_zeros.py --branch k` | `paper2_path_k_interval_certificate.json` | Run separately for k=1,2,3,4,5; accepted slab counts502,512,512,512,512; each branch completes. Also run --endpoints for paper2_endpoint_interval_certificate.json. |
| `python programs/paper2_path_figure.py` | `paper2_certified_paths_summary.tsv and papers/paper2/figures/hurwitz_paths.{pdf,svg,png}` | Recreates the endpoint-centre visualization; segments are interpolation, not additional certified paths. See the source for figure paths. |
| `python programs/paper3_check.py --output checks/paper3_torsion_matrix.json` | `paper3_torsion_matrix.json` | Primes2,3,5: matrix32by14, rank7; nonzero Smith factors1,1,1,1,1,2,4. |
| `python programs/paper3_independent_smith.py` | `paper3_smith_certificate.json` | Independent coset/Euclidean calculation gives the same Smith factors. |
| `python programs/paper3_review_hurwitz_certificates.py` | `paper3_hurwitz_geometry_audit.json` | Exact-rational coverage/overlap audit passes; this command audits stored geometry and is distinct from a full interval replay. |
| `python programs/paper3_review_paper5.py --output checks/paper3_paper5_matrix_certificate.json` | `paper3_paper5_matrix_certificate.json` | Independent block-matrix reconstruction verifies the specified rank-three tables. |
| `python programs/paper3_zero_bottom_trace_facts.py` | `paper3_zero_bottom_trace_facts.json` | Passes the finite trace facts used by the sixteen-slot lower bound; it does not solve effective exact-bottom existence. |
| `python programs/paper3_rank4_word_minor.py --prime 1000003 --v 2 --output checks/paper3_rank4_word_minor.json` | `paper3_rank4_word_minor.json` | Selects114words/rows; all four conjugate determinants274637 and norm988208. |
| `python programs/paper4_checks.py --output checks/paper4_results.json` | `paper4_results.json` | PASS;384000gate/input checks,7nonempty three-vertex graphs,53nonempty four-vertex C4-free graphs. |
| `python programs/paper4_witness_examples.py --output checks/paper4_witness_examples.json` | `paper4_witness_examples.json` | Both exact truth tables and the stated deleted-gate counts pass. |
| `python programs/paper4_matching_injection.py --output checks/paper4_matching_injection.json` | `paper4_matching_injection.json` | The19-gate example passes all4096inputs; the18-gate shortcut is refuted by the stored input. |
| `python programs/paper4_hurwitz_recheck.py --directory checks --output-directory checks --branches 1 2 3 4 5 --workers 5 --N 50 --M 28 --dps 60` | `paper4_hurwitz_recheck.json` | Full replay:2550slabs,2555path endpoint discs,5standalone endpoint discs; all pass. Do not use --sample for this claim. |
| `python programs/paper4_smt_search.py --directory checks/paper4_smt --timeout-ms 30000 --large` | `paper4_smt/results.json` | Produces SMT-LIB2 instances and sat/unsat/unknown records. A timeout remains unknown; runtimes and timeout outcomes may vary. |
| `python programs/paper5_rank_three.py` | `paper5_rank_three_certificate.json` | 132exact trace constants; five effective lifts with zero-weight counts54,58,54,38,42 and cancelling pairs7952,11764,7656,8288,10804. |
| `python programs/paper5_dimension_search.py` | `paper5_dimension_search.json` | 888feasible outer parameters and50946716dimension tables in the stated finite window; recorded minima are only for that family/window. |
| `python programs/paper5_unrestricted_support.py` | `paper5_unrestricted_support.json` | 10000support associativity checks;6167supported-zero weights,0bottom supported-zero weights;829nonzero coefficient triples. |
| `python programs/paper5_nonliftable.py` | `paper5_nonliftable.json` | PASS;10000support associativity equations,1000trace containments,740nonempty coefficient triples; exact nonliftability witness. |
| `python programs/root_two_missing_example.py` | `root_two_missing_example.json` | Independent truth table, matching and girth checks agree with the recorded example. |

Dependencies between calculations: run `paper5_rank_three.py` before its support-lift checks; run `paper3_rank4_word_minor.py` before its independent minor replay; run the five interval branch certificates before their geometric and full interval replays. The independent word-reduction scripts import their own adjacent word-reduction implementation; the two full Hurwitz implementations share mpmath.iv as a trusted arithmetic library.

## Record assembly and audit

`python programs/assemble_records.py` regenerates the integrated register, typed events, crosswalk, questions, dictionary and literature from authored fragments. `python programs/audit_records.py` then writes `OUTSIDE_INDEX.tsv`, `records/crosswalk_resolution.tsv` and `checks/record_structure_audit.json`. The expected finished structural audit has no unresolved canonical targets, no invalid check-event types, no missing statement labels and empty author lines. Counts grow with research and are frozen in each manifest.

## Historical authoring utilities

These scripts document the source-reconciliation and editorial workflow; they are not mathematical verifiers. They can regenerate earlier component tables and thereby replace later editorial changes. Their output is not proof credit. To replay them, use a separate research-root directory containing the original attachments unpacked as `source/` and this archive extracted as `deliverable/`; run each command from `deliverable/workbench`. No attached source or external paper is included here.

| Exact command | Required inputs and expected kind of output |
|---|---|
| `python programs/gemini_intake.py` | Authored Gemini annotation records; regenerates the initial occurrence tables. Later occurrence-specific background refinements are already in the returned canonical records and must be preserved. |
| `python programs/paper1_corpus_intake.py` | Original corpus; calls the returned `source_statement_metadata` helper directly and writes the curated corpus register/crosswalk/other-result tables. No missing temporary extraction is required. |
| `python programs/paper1_finish_event_normalization.py` | Existing component event records; preserves raw events while routing proof checks, source events and review events. Does not create a fresh mathematical proof. |
| `python programs/paper1_last_exact_paths.py` | Original source paths and authored classification mappings in the script; writes the corresponding source crosswalk, outside-result or coverage records. Source intake is not proof checking. |
| `python programs/paper1_normalize_events.py` | Existing component event records; preserves raw events while routing proof checks, source events and review events. Does not create a fresh mathematical proof. |
| `python programs/paper1_november_bridge_intake.py` | Original source paths and authored classification mappings in the script; writes the corresponding source crosswalk, outside-result or coverage records. Source intake is not proof checking. |
| `python programs/paper1_remaining_zeta_intake.py` | Original source paths and authored classification mappings in the script; writes the corresponding source crosswalk, outside-result or coverage records. Source intake is not proof checking. |
| `python programs/paper1_source_reconciliation.py` | Original source paths and authored classification mappings in the script; writes the corresponding source crosswalk, outside-result or coverage records. Source intake is not proof checking. |
| `python programs/source_program_inventory.py` | Original source tree and source inventory; records historical program/data hashes without executing them. With no unmapped files it exits without rebuilding the existing inventory. |
| `python programs/source_statement_metadata.py --source ../../source` | Reconstructs locator metadata directly from the original TeX sources:1450 occurrences in56files. The helper writes no statement or proof text; optional `--output PATH` writes locator-only JSON. Both Paper1 intake utilities import this helper. |

The locator reconstruction was compared field by field with the temporary metadata used during intake: file, line, environment, title and labels all agreed for1450occurrences. The result is recorded in `checks/source_metadata_replay.json`. This verifies reproducibility of locators; it does not rerun the historical table-writing scripts or recheck the mathematics.

## Three-missing-witness sharpness example (24 November 2026)

Run `python programs/paper4_induced_matching_d5.py` from `workbench/`. Standard library only. It independently constructs the stated eleven-vertex graph and nineteen-gate circuit, expands its exact integer polynomial, extracts its quadratic frame, checks all2048Boolean assignments, searches minimum vertex covers, and tests all common-neighbor pairs for4-cycles. Expected: PASS;13graph edges;10quadratic edges; covers5and6;14retained gates;5deleted gates, comprising3products and2additions; no4-cycle. The full graph star bound is18, so this example does not refute that bound. Output: checks/paper4_induced_matching_d5.json.

### Independent nonminimum-product scope example

Run `python3 workbench/programs/paper4_one_product_nonminimal_independent.py` from the archive root. It uses ROBDD equivalence, second derivatives, tree/cover/matching certificates, and a minimum-degree certificate. Expected: tree and exact Boolean/quadratic support checks true; cover numbers2and4;12total gates,7retained,5deleted with1product; full star count10. Output: `workbench/checks/root_one_product_nonminimal_independent.json`.


## Recovery and standalone sharpness replay

Run `node checks/outage_20261125/operator_k/SZ4-196_independent_program.js` from `workbench/` (Node.js with BigInt support; no third-party package). It prints the full exact certificate on stdout without changing the original certificate. Expected: `passed: true`,25original gates,19retained gates,6deleted gates, four missing edges, cover numbers6and8, and no weight-four vector in the complete three-dimensional binary cycle space. The seven nonzero cycle-space weights are5,5,5,5,6,6,8. The complete parsed output was replayed and compared field-for-field with `checks/outage_20261125/operator_k/SZ4-196_independent_certificate.json`; see root's standalone-replay record. This verifies the stated sharpness example, not optimality over all circuits or the cover-gain-three case.

The following maintenance programs document the execution-outage recovery. They are operational records, not mathematical certificates. Their exact input archives and coordinated snapshots are identified in their reports. Historical scripts preserve the original absolute workspace paths; reproduce them in a separate copy with those path settings explicitly adjusted. Running a historical review again does not create a new dated mathematical review.

| Program / command from workbench | Inputs and expected operational result |
|---|---|
| `python3 programs/maintenance/recover_session_payload.py < payload.json` | Own preserved UTF-8 session payload with exact byte counts and SHA256 values. Exclusive creation or verified identical-existing files, followed by real recovery timestamps; never backdates the original proof save. The original texts and recovery manifests are returned under checks/outage_20261125. |
| `python3 programs/maintenance/research_review21_recovery.py` | Verified immutable checkpoint30 and prior review20 records. Documents the actual delayed review21 and all stopped lines. Historical exact inputs are identified in its report; it must not be used to invent a new review at the old time. |
| `python3 programs/maintenance/research_review22_recovery.py` | The returned coordinated review22_snapshot and prior actual review21. Produces the127-row review, ten line-state rows and evidence manifest, keeping all eight stopped mathematical lines unchanged. |
| `python3 programs/maintenance/paper4_tex_runtime_compatibility.py` | Isolated checkpoint30 sources and recovered installed-runtime configuration at the explicit paths in the driver. Three-pass baseline compatibility report only; no mutation of the protected baseline. Runtime packages, formats and maps are not external source deliverables. A normal standalone manuscript build uses the paper's BUILD.md. |
| `python3 programs/maintenance/paper4_tex_baseline_pixel_comparison.py` | The two baseline PDFs from the preceding compatibility run; PyMuPDF and Pillow. Compares every page at96dpi and records the exact differing tail pages. Pixel comparison is not visual inspection; the separate recorded image review supplies that evidence. |
| `python3 programs/maintenance/prepare_checkpoint31.py --preflight` | All five current PDFs, exact synchronized build reports, complete assembled records, checkpoint30 and completed review22. Checks hashes, used TeX inputs, warnings, visual coverage and unchanged companion papers without freezing a new checkpoint. The non-preflight form writes the inventory and continuation entry once. |
| `python3 programs/maintenance/make_checkpoint.py 31 '<recorded delay reason>'` | Complete verified deliverable tree. Exclusively creates and reads back the full ZIP, rejects source-hash collisions and nested ZIPs, and records the actual seal time. For32onwards, the next due slot is the first unused original45-minute slot after the preceding complete seal; no duplicate catch-up archive is manufactured. |

Earlier numbered maintenance scripts preserve their own historical checkpoint/review commands and input assumptions. They are returned for audit, not as independent proof checks or as instructions to overwrite an existing checkpoint.


### Additional author replay and final-build drivers

Exact standalone commands, prerequisites and expected outputs for `checks/outage_20261125/circuits/196_author_replay.js`, `author_identity_204_207.js`, `author_identity_207_210.js` and `portable_sha256.js` are preserved together in `checks/outage_20261125/circuits/REPLAY_COMMANDS.md`. All require Node.js18or later and built-in modules only. The196author computation enumerates131072assignments and returns zero Boolean mismatches, exact quadratic support, no four-cycle, cover sizes6/8,25gates and19retained gates. It is distinct from the independent polynomial/antichain/cycle-space method. The two identity programs certify only their displayed formal Boolean identities; admission of204/207 rests on the separate complete proofs and full comparisons, not these programs or their finite identity checks. The SHA256 helper is an outage-preservation utility.

The exact executed final driver is `python3 programs/maintenance/paper4_recovery_build_20261125.py --name paper4_checkpoint31_recovery_final`. It requires Python3, PyMuPDF, Pillow, pdfLaTeX and the preserved checkpoint30 baseline at its documented local paths; it optionally consumes the recovered installed-runtime configuration. Expected output is three successful compiler passes, exact source/PDF hashes,200pages, no warnings and page-raster comparison metadata. The driver explicitly leaves visual review pending; separate human-readable model inspection records supply it. The inline runtime-repair procedure is preserved in `checks/paper4_tex_runtime_recovery.md`; no separate driver existed to return. A complete standard TeX installation builds the standalone paper without the private runtime-recovery cache.

The final guarded synchronization command is `python3 programs/maintenance/paper4_finalize_recovery31.py`. It requires the exact completed final build metadata, all197 changed-page inspection records and both full text-reading records. It checks their source/PDF hashes and coverage before copying the PDF and synchronizing the build report, deposit sheet, current questions and crosswalk. It is an operational synchronization step, not another mathematical proof.

### Checkpoint32 build and verification

Run `python3 programs/maintenance/paper4_checkpoint32_build.py --name paper4_checkpoint32_final` from `workbench/` in the documented research workspace. It uses Python3, PyMuPDF, Pillow and pdfLaTeX, together with the exact reviewed checkpoint31 baseline. It compiles the current standalone Paper4 in three passes, records final warnings and source/PDF hashes, and compares rendered pages with that reviewed baseline. New or changed pages are rendered separately for actual inspection. Its pending-QA output is not a visual-review certificate.

After the separately attributed changed-page inspections and complete expert/newcomer readings, `python3 programs/maintenance/paper4_finalize_checkpoint32.py` checks those source/PDF-bound records before copying the final PDF and synchronizing current build, question, deposit and crosswalk records. The explicit new admission set is192/207/208;204 remains an incomplete fresh-proof attempt and is not promoted by any build or archive operation. The synchronized build report records exact page counts and results.

`python3 programs/maintenance/prepare_checkpoint32.py --preflight` verifies the checkpoint31 baseline, the exact three new canonical IDs, all reachable TeX-input hashes, the current synchronized PDF/build evidence, and completed research review23. Omitting `--preflight` writes one dated inventory and continuation/ledger snapshot and must not be repeated after that snapshot is written. `python3 programs/maintenance/make_checkpoint.py 32 "<actual delay reason if required>"` then exclusively creates the complete archive, verifies every member and its CRC, and records its actual seal on the next unused original45-minute cadence slot. Neither command performs a mathematical proof check or changes any research stopping counter.

`python3 programs/maintenance/research_review23.py` preserves the actual review23 procedure, using its coordinated source snapshot and the complete immutable checkpoint31 baseline, including the review22 completion-frontier clarification. It reviews all83 questions and44 unresolved claims and preserves the eight stopped research lines. The report separately records an initial preflight stop caused by comparing live-source metadata with the earlier review22 snapshot; those already-baseline metadata receive no movement credit. This is a historical operational script with fixed input paths and exclusive dated outputs, not a command to fabricate another review at its recorded time.

### Checkpoint33 build and verification

Run `python3 programs/maintenance/paper4_checkpoint33_build.py --name paper4_checkpoint33_final_v5` from `workbench/` in the documented research workspace. Dependencies are Python3, PyMuPDF, Pillow, pdfLaTeX and the exact reviewed checkpoint32 baseline. The final run gives211pages, three successful passes and no final warnings. Each source version and rendered-page comparison has its own record. The final v5 differs from the fully viewed v4 only on page201, which was separately displayed and inspected. Pixel equality inherits only an already completed actual review; it is not itself a visual inspection.

`python3 programs/maintenance/paper4_finalize_checkpoint33.py` checks the complete source/PDF-bound expert, newcomer and attributed page-review records before synchronizing the final PDF, build report, questions, crosswalk and deposit sheet. Its exact admission set is204/212/214. The two pending inventories211/213 receive no theorem credit. The stronger212 theorem precedes174, whose exact statement remains with a shorter consequence proof; its earlier complete derivation is preserved.

`python3 programs/maintenance/prepare_checkpoint33.py --preflight` checks the immutable32baseline, exact new canonical set, all reachable TeX-input hashes, current build evidence, unchanged companion papers and the completed review23. The non-preflight form writes one dated inventory/continuation/ledger snapshot. `python3 programs/maintenance/make_checkpoint.py 33 "<actual delay reason if required>"` then exclusively seals and reads back the complete archive. Review24 is not required before its17:40:35UTCslot. None of these operational programs performs a new mathematical proof or changes a stopping counter.

### Checkpoint34 build, original-node inventory and review24

The build driver is `python3 programs/maintenance/paper4_checkpoint34_build.py --name paper4_checkpoint34_final2` from `workbench/` in the documented research workspace. The final run has217pages; its exact source/PDF hashes and page review are recorded in checks/paper4_checkpoint34_build.json. It requires the reviewed checkpoint33 baseline and the same Python3, PyMuPDF, Pillow and pdfLaTeX environment as the earlier drivers. Intermediate213-only builds are preserved separately; their actual page reviews can be inherited only after exact pixel comparison.

`python3 programs/maintenance/paper4_finalize_checkpoint34.py` requires the completed source-bound expert/newcomer and actual visual records before synchronizing the PDF, questions, crosswalk, deposit and build report. The new checked results are213 and215;211 remains pending unless separately documented complete fresh and mutual checks explicitly admit it. The original213 clean/author/fresh records are preserved alongside the current-P* referent clarification and selected-trace correction. These editorial or local proof corrections receive no new fresh-proof credit.

`python3 programs/maintenance/prepare_checkpoint34.py --preflight` verifies the immutable33 baseline, every unchanged prior canonical row, the exact admitted additions, reachable TeX-input hashes, synchronized builds and completed research review24. The non-preflight form exclusively writes the34 inventory and current continuation/ledger entry. `python3 programs/maintenance/make_checkpoint.py 34 "<actual delay reason if required>"` exclusively seals the complete archive, verifies every member and CRC, and preserves the original45-minute cadence. The34 due slot is18:10:35UTC; the next unused slot is computed from the actual seal.

`python3 programs/maintenance/research_review24.py` documents the actual127-row review of all83questions and44legacytracked claims, with a38-file coordinated snapshot after the17:40:35UTCslot. It verifies the complete review23/checkpoint32 baseline, unchanged640 earlier canonical rows, three subsequent admissions204/212/214, and eight byte-identical stopped line states. Legacy selector wording does not downgrade the proved070/111/112 rows. Source-status retrieval and QA/packaging receive no mathematical movement credit. This historical driver has exclusive dated outputs; rerunning it is not a new review at the old time.

The historical source-integration commands for this checkpoint are `python3 programs/maintenance/paper4_integrate_213.py` and `python3 programs/maintenance/paper4_integrate_215.py`. They consume the exact mutually checked staged TeX and comparison records identified in their source, insert the new labeled statements, and update their canonical/question fragments. Their guarded old-state assumptions must be replayed in a separate historical copy; they are not proof checkers and must not be used to overwrite a later manuscript. The final command `python3 programs/maintenance/paper4_checkpoint34_aggregate_reviews.py` combines the already completed, source/PDF-bound text and visual records for final2, verifies exact page coverage, and writes the34 aggregate review inputs for the guarded finalizer. Aggregation supplies no unperformed inspection or new independent proof.

### Checkpoint35: original-node inventory, squared preparation and review25

The commands below are the actual inspected maintenance interfaces, run from `workbench/` in the recorded research workspace. They retain fixed historical paths, exact input hashes and exclusive dated-output guards. Replaying a historical integration or review requires a separate copy of its predecessor state; it must not overwrite the current manuscript, an existing review, or an already sealed archive. No operational program supplies a new mathematical proof check.

| Exact command | Inputs and guarded result |
|---|---|
| `python3 programs/maintenance/paper4_integrate_211.py` | The exact mutually checked staged211 TeX and comparison records. Inserts `prop:allvisibleoriginalinventory`, updates its authored register/crosswalk/question fragment, and records source hashes. Original proof versions and the disclosed4-to6 clause-count correction are preserved. The later ordered-singleton and explicit-outer-factor manuscript precisions are recorded separately; the original integration script is a historical insertion, not an overwrite of those corrections. |
| `python3 programs/maintenance/paper4_integrate_216.py` | The exact separately checked216 snippet and full comparison records. Inserts `prop:squaredunequalpreparation`, its local support assertion and literal original-circuit consequence, with arbitrary K. Preserves whole-current original-carrier terminology and the separately dated squarefree-P2 explanation for same-occurrence squares. It does not admit217. |
| `python3 programs/assemble_records.py` | The current authored record fragments. Rebuilds canonical/check/source/review/question/crosswalk outputs while retaining exact event types and provenance. Unrecognized historical event types stay in their recorded category; assembly does not turn a source or review event into a fresh proof. |
| `python3 programs/maintenance/paper4_checkpoint35_build.py --name paper4_checkpoint35_final1` | The standalone current Paper4 source and exact reviewed217-page checkpoint34 baseline. Python3, PyMuPDF, Pillow and pdfLaTeX; optionally the already documented installed-runtime recovery configuration. Three compiler passes, exact source/PDF hashes, rendered changed pages and pixel-equality records. The observed final1 compilation has224pages and zero warnings. Its `build_pending_qa.json` explicitly leaves actual visual review pending. |
| `python3 programs/maintenance/paper4_finalize_checkpoint35.py --name paper4_checkpoint35_final1` | The exact final build metadata plus complete source/PDF-bound aggregate expert/newcomer and actual changed-page review JSON. Checks every changed page and every inherited pixel-identical page, then synchronizes PDF, build report, questions, crosswalk and deposit. Requires exactly the integrated211/216 results;217 stays pending. This command must wait for the aggregate records to pass. |
| `python3 programs/maintenance/prepare_checkpoint35.py --preflight --expected-new SZ4-211,SZ4-216` | Immutable checkpoint34 SHA d9f0c4bc137172385ed8441978b61f5909612295b70666d3538b21f5870fb762, unchanged645 prior canonical rows, exactly211/216 new canonical IDs, reachable TeX inputs, all five synchronized builds and completed review25. Performs read-only preflight and writes no dated inventory. The explicit `--expected-new` is required for this two-result frontier. |
| `python3 programs/maintenance/prepare_checkpoint35.py --expected-new SZ4-211,SZ4-216` | The same complete guarded state; exclusively writes one checkpoint35 inventory and continuation/ledger snapshot. It must not be repeated after that inventory exists. |
| `python3 programs/maintenance/make_checkpoint.py 35 "<actual delay reason if required>"` | A complete preflighted/frozen deliverable. Exclusively creates and reads back the archive and records the actual seal. The scheduled slot is18:55:35UTC; any delay is recorded honestly. The next checkpoint uses the next unused original45-minute slot, with no fabricated catch-up archives. |

The inspected and executed aggregate command is:

```bash
python3 programs/maintenance/paper4_checkpoint35_aggregate_reviews.py --name paper4_checkpoint35_final1 --middle-visual checks/paper4_checkpoint35_visual_root_final1_supplement.json --foundation-text checks/outage_20261125/foundation/checkpoint35_final1_actual_211_216_newcomer_review.json
```

The final interface uses `--middle-visual`, not the earlier unused `--foundation-visual` spelling. The actual selected middle-page record is root's supplement, and reviewer attribution comes from each verified input record. The driver checks56 uniquely covered changed pages,168 pixel-identical inherited pages, exact final source/PDF hashes, complete expert/newcomer readings, and byte identity of the already fully read211 block. It writes `checks/paper4_checkpoint35_visual_review.json` and `checks/paper4_checkpoint35_text_review.json` exclusively. Aggregation supplies no unperformed inspection or new proof.

The guarded finalizer then completed synchronization18:59:52.811309UTC. The224-page PDF, source, build/deposit/question/crosswalk records and full actual review attribution agree in `checks/paper4_checkpoint35_build.json`, SHA-256 `457682b420c2e6ead3f38b63e87f2e3e27e9f120153d01bdd1144aa8e28df8e6`. Its three passes returned zero and its warning list is empty. Synchronization and archive sealing remain separate recorded actions.

The exact research-review interfaces are `python3 programs/maintenance/research_review25.py snapshot` and `python3 programs/maintenance/research_review25.py review`. The actual review audited all83questions and44legacy tracked rows,127rows in total, against the full643-row checkpoint33 baseline. The snapshot and raw event counts remain immutable. An initial guard exposed213's nonstandard historical event type; the original `research_review25_pre_taxonomy_reconciliation.py` and exact raw event are preserved, and the final review semantically checks the complete proof/comparison without upgrading the snapshot's typed-check count. The live component normalization is separately dated. The proved070/111/112 legacy-selector false positives retain their proved statuses.

Review25 completed18:41:59.561995UTC and counts the closed mathematical frontier211/213/215 exactly once.211's then-pending source integration is not future research movement.216 was not admitted at that snapshot/frontier; its later complete comparison is for assessment at review26, due19:40:35UTC. Eight stopped lines retain their original stop states and counter2; the active circuit counter is zero. The historical script's dated outputs are exclusive, so rerunning it does not create another review at an old time.

## Checkpoint36 exact original-input exclusions and guarded build

These are historical maintenance commands run from the workbench directory. They use the documented local project root and, for recovered pdfLaTeX, the already installed recovery environment. Ordinary TeX installations can still build the standalone source with the standard three-pass command; no binary format/map/package is included. Every actual review remains a separately attributed human-readable record, not a consequence of compilation.

| Exact command | Input and guarded result |
|---|---|
| `python3 programs/maintenance/paper4_integrate_217_218.py` | Exact fully paired217/stronger218 snippets, immutable35 source hash, canonical components. Inserts the complete propositions, updates opening/residual/current-live wording and records, and preserves all earlier proof versions. It does not admit219. |
| `python3 programs/maintenance/paper4_checkpoint36_build.py --name paper4_checkpoint36_final1` | Current standalone Paper4 source, exact reviewed224-page35 PDF baseline, Python3/PyMuPDF/Pillow/pdfLaTeX. Runs three passes, hashes inputs/output, renders changed pages and records pixel-identical inheritance. Compilation alone does not count as visual review. |
| `python3 programs/maintenance/paper4_finalize_checkpoint36.py --name paper4_checkpoint36_final1` | Complete source-bound visual/text aggregate and exact current scope metadata. Checks all changed/inherited pages and full expert/newcomer coverage, then synchronizes PDF, build report, crosswalk, questions and deposit. Exclusively writes the36 final build report. |
| `python3 programs/maintenance/paper4_checkpoint36_documentation_closeout.py` | The already synchronized36 report. Updates only the current README section and this program catalogue; historical35 source/report/notes remain unchanged. Does not claim a seal or future review. |
| `python3 programs/assemble_records.py` | Authored record fragments; rebuilds aggregate register, check/source/review/question/crosswalk tables with exact event taxonomy and provenance. No new proof credit is created. |
| `python3 programs/maintenance/prepare_checkpoint36.py --preflight --expected-new SZ4-217,SZ4-218` | Exact immutable35 archive SHA21bf0aa0…, all647 prior canonical rows unchanged, exactly217/218 new IDs, completed actual review26, all five synchronized PDFs and complete current QA. Read-only preflight; no dated inventory is written. |
| `python3 programs/maintenance/prepare_checkpoint36.py --expected-new SZ4-217,SZ4-218` | The same fully guarded current state; exclusively writes the dated36 inventory/continuation record. Any later additional admission requires an explicit guard widening and complete new main/QA evidence first. |
| `python3 programs/maintenance/make_checkpoint.py 36 "<actual delay reason if required>"` | A fully frozen/preflighted deliverable. Creates/readback-checks one complete36 archive and records actual sealing. The scheduled slot is19:40:35UTC; any delay is recorded honestly and no fabricated catch-up archive is made. |
| `python3 programs/maintenance/research_review26.py snapshot` and `python3 programs/maintenance/research_review26.py review` | Coordinated immutable source/canonical/questions snapshot at or after19:40:35, followed by the actual127-row review against the complete earlier frontier. A snapshot or typesetting change is not itself mathematical movement. |

The exact aggregate command for final1 is:

```bash
python3 programs/maintenance/paper4_checkpoint36_aggregate_reviews.py --name paper4_checkpoint36_final1 --visual checks/paper4_checkpoint36_visual_root_final1.json --visual checks/outage_20261125/foundation/checkpoint36_final1_visual_review.json --visual checks/paper4_checkpoint36_visual_circuits_final1.json --expert checks/outage_20261125/root/checkpoint36_final1_actual_text_review.json --newcomer checks/outage_20261125/foundation/checkpoint36_final1_actual_217_218_newcomer_review.json
```

The aggregator verifies disjoint actual page coverage, exact final source/PDF hashes and complete source-bound expert/newcomer readings. It exclusively writes the36 aggregate visual and text reports. The exact final input paths must exist and match their saved hashes; rendering, truncated image outputs, and prior differently hashed source readings do not receive automatic inspection credit.

## Checkpoint37 original-family refinements and guarded build

These are historical maintenance commands run from the workbench directory under the documented local project root. Recovery builds use the already installed runtime configuration; ordinary TeX installations can still compile the standalone source with three ordinary passes. No binary format/map/package is included.

Integrated exact-source insertion drivers present at closeout: `programs/maintenance/paper4_integrate_219.py`, `programs/maintenance/paper4_integrate_220.py`, `programs/maintenance/paper4_integrate_221.py`, `programs/maintenance/paper4_integrate_222.py`. Each preserves immutable earlier proofs and uses the separately completed mutual-comparison gate; an insertion script is not itself a fresh mathematical check.

The actual build command was `python3 programs/maintenance/paper4_checkpoint37_build.py --name paper4_checkpoint37_final5`. It uses the reviewed229-page36 source/PDF baseline, Python3/PyMuPDF/Pillow/pdfLaTeX, three passes, source/PDF hashing and changed-page pixel comparison. Rendering by itself is not visual inspection. The earlier `--compile-only` stage, when present, deliberately records no rendered or visual coverage.

The exact actual-review transfer command was `python3 programs/maintenance/paper4_checkpoint37_transfer_reviews.py --from-name paper4_checkpoint37_final3 --to-name paper4_checkpoint37_final4 --visual checks/outage_20261125/root/checkpoint37_final3_visual_root.json --visual checks/outage_20261125/operator_k/checkpoint37_final3_visual_operator.json --visual checks/outage_20261125/circuits/checkpoint37_final3_visual_sheets07_09.json`. It checks full RGB samples and raster dimensions at the same page index, preserves every original source/PDF/review hash and attribution including upstream inheritance, and creates delta sheets only for pixels still requiring an actual view. The transfer itself is not a new image inspection. Evidence: `checks/paper4_checkpoint37_actual_review_transfer.json`.
The exact actual-review transfer command was `python3 programs/maintenance/paper4_checkpoint37_transfer_reviews.py --from-name paper4_checkpoint37_final4 --to-name paper4_checkpoint37_final5 --visual checks/outage_20261125/circuits/checkpoint37_paper4_checkpoint37_final4_inherited_1.json --visual checks/outage_20261125/circuits/checkpoint37_paper4_checkpoint37_final4_inherited_2.json --visual checks/outage_20261125/root/checkpoint37_final4_visual_root.json --visual checks/outage_20261125/operator_k/checkpoint37_final4_visual_operator.json --visual checks/outage_20261125/circuits/checkpoint37_final4_visual_delta05.json`. It checks full RGB samples and raster dimensions at the same page index, preserves every original source/PDF/review hash and attribution including upstream inheritance, and creates delta sheets only for pixels still requiring an actual view. The transfer itself is not a new image inspection. Evidence: `checks/paper4_checkpoint37_actual_review_transfer_paper4_checkpoint37_final5.json`.

The exact aggregate command selected from the saved input records is:

```bash
python3 programs/maintenance/paper4_checkpoint37_aggregate_reviews.py --name paper4_checkpoint37_final5 --visual checks/outage_20261125/circuits/checkpoint37_paper4_checkpoint37_final5_inherited_1.json --visual checks/outage_20261125/circuits/checkpoint37_paper4_checkpoint37_final5_inherited_2.json --visual checks/outage_20261125/circuits/checkpoint37_paper4_checkpoint37_final5_inherited_3.json --visual checks/outage_20261125/circuits/checkpoint37_paper4_checkpoint37_final5_inherited_4.json --visual checks/outage_20261125/circuits/checkpoint37_paper4_checkpoint37_final5_inherited_5.json --visual checks/outage_20261125/circuits/checkpoint37_final5_visual_page229.json --expert checks/outage_20261125/root/checkpoint37_final5_actual_text_review.json --newcomer checks/outage_20261125/operator_k/checkpoint37_final5_actual_newcomer_review.json
```

It verifies disjoint actual page coverage, exact final hashes and complete source-bound expert/newcomer readings. `python3 programs/maintenance/paper4_finalize_checkpoint37.py --name paper4_checkpoint37_final5` then checks all changed/inherited pages and exact current scope metadata before synchronizing the PDF/report/crosswalk/questions/deposit. `python3 programs/maintenance/paper4_checkpoint37_documentation_closeout.py` writes only this current README/program catalogue closeout after the synchronized report exists; it does not claim an archive seal or future research review.

`python3 programs/assemble_records.py` rebuilds the aggregate authored records with exact event types and provenance. `python3 programs/maintenance/prepare_checkpoint37.py --preflight --expected-new SZ4-219,SZ4-220,SZ4-221,SZ4-222` and the same command without `--preflight` guard the exact completed frontier against immutable36, all prior canonical rows, latest completed actual review and all synchronized PDFs. The latter exclusively writes the dated inventory. After complete frozen preflight, `python3 programs/maintenance/make_checkpoint.py 37 "<actual delay reason if required>"` creates/readback-verifies one complete archive and records the actual seal. The scheduled slot is20:25:35UTC; any delay must be recorded honestly, with no fabricated catch-up checkpoint.

The complete report currently records239pages,39 actually reviewed changed pages and200 exact pixel matches. No truncated image/text output or proof-copy time is silently upgraded to inspection or independent-proof time.

### Prepared review27 interface

`python3 programs/maintenance/research_review27.py preflight` audits the current state without writing a research review. At or after the scheduled20:40:35UTC slot, `python3 programs/maintenance/research_review27.py snapshot` exclusively captures the coordinated immutable evidence, then `python3 programs/maintenance/research_review27.py review` writes all83question and44legacy-claim rows, the line states, exact evidence report, manifest and append-only continuation notes. Inputs include the immutable review26 snapshot and `checks/outage_20261125/review27_frontier_input.json`; expected new fully paired mathematics is219,220,221,222, with all649 previous canonical rows unchanged and the eight stopped lines preserved. A prepared driver or successful preflight is not an executed review. The actual snapshot/review timestamps determine execution and subsequent cadence. No future review or new proof credit is inferred by this catalogue entry.

## Checkpoint38 original-family refinements and guarded build

These are historical maintenance commands run from the workbench directory under the documented local project root. Recovery builds use the already installed runtime configuration; ordinary TeX installations can still compile the standalone source with three ordinary passes. No binary format/map/package is included.

Integrated exact-source insertion drivers present at closeout: `programs/maintenance/paper4_integrate_223.py`, `programs/maintenance/paper4_integrate_224.py`. Each preserves immutable earlier proofs and uses the separately completed mutual-comparison gate; an insertion script is not itself a fresh mathematical check.

The actual build command was `python3 programs/maintenance/paper4_checkpoint38_build.py --name paper4_checkpoint38_final2`. It uses the reviewed239-page37 source/PDF baseline, Python3/PyMuPDF/Pillow/pdfLaTeX, three passes, source/PDF hashing and changed-page pixel comparison. Rendering by itself is not visual inspection. The earlier `--compile-only` stage, when present, deliberately records no rendered or visual coverage.

The exact actual-review transfer command was `python3 programs/maintenance/paper4_checkpoint38_transfer_reviews.py --from-name paper4_checkpoint38_final1 --to-name paper4_checkpoint38_final2 --visual checks/outage_20261125/root/checkpoint38_final1_visual_root.json --visual checks/outage_20261125/operator_k/checkpoint38_final1_visual_operator.json --visual checks/paper4_checkpoint38_final1_visual_circuits.json`. It checks full RGB samples and raster dimensions at the same page index, preserves every original source/PDF/review hash and attribution including upstream inheritance, and creates delta sheets only for pixels still requiring an actual view. The transfer itself is not a new image inspection. Evidence: `checks/paper4_checkpoint38_actual_review_transfer_paper4_checkpoint38_final2.json`.

The exact aggregate command selected from the saved input records is:

```bash
python3 programs/maintenance/paper4_checkpoint38_aggregate_reviews.py --name paper4_checkpoint38_final2 --visual checks/outage_20261125/circuits/checkpoint38_paper4_checkpoint38_final2_inherited_1.json --visual checks/outage_20261125/circuits/checkpoint38_paper4_checkpoint38_final2_inherited_2.json --visual checks/outage_20261125/root/checkpoint38_final2_visual_root.json --visual checks/outage_20261125/foundation/checkpoint38_final2_visual_218_225.json --visual checks/outage_20261125/operator_k/checkpoint38_final2_visual_operator.json --visual checks/paper4_checkpoint38_final2_visual_circuits.json --expert checks/outage_20261125/root/checkpoint38_final2_actual_text_review.json --newcomer checks/outage_20261125/operator_k/checkpoint38_final2_actual_newcomer_review.json
```

It verifies disjoint actual page coverage, exact final hashes and complete source-bound expert/newcomer readings. `python3 programs/maintenance/paper4_finalize_checkpoint38.py --name paper4_checkpoint38_final2` then checks all changed/inherited pages and exact current scope metadata before synchronizing the PDF/report/crosswalk/questions/deposit. `python3 programs/maintenance/paper4_checkpoint38_documentation_closeout.py` writes only this current README/program catalogue closeout after the synchronized report exists; it does not claim an archive seal or future research review.

`python3 programs/assemble_records.py` rebuilds the aggregate authored records with exact event types and provenance. `python3 programs/maintenance/prepare_checkpoint38.py --preflight --expected-new SZ4-223,SZ4-224` and the same command without `--preflight` guard the exact completed frontier against immutable37, all prior canonical rows, latest completed actual review and all synchronized PDFs. The latter exclusively writes the dated inventory. After complete frozen preflight, `python3 programs/maintenance/make_checkpoint.py 38 "<actual delay reason if required>"` creates/readback-verifies one complete archive and records the actual seal. The scheduled slot is21:10:35UTC; any delay must be recorded honestly, with no fabricated catch-up checkpoint.

The complete report currently records243pages,63 actually reviewed changed pages and180 exact pixel matches. No truncated image/text output or proof-copy time is silently upgraded to inspection or independent-proof time.

The prepared hourly driver `programs/maintenance/research_review28.py` accepts `preflight`, `snapshot`, or `review`, run from the workbench as `python3 programs/maintenance/research_review28.py MODE`. It uses the immutable review27 baseline, all83 questions and44 tracked claims, and the exact fully closed223/224 frontier with223's preserved correction qualification. Its read-only preflight ran21:16:07UTC; no review28 snapshot or actual review has run at this closeout. The original due time is21:40:35UTC. The prepared driver and frontier are evidence of preparation only, not mathematical movement or a completed scheduled review.

## Historical checkpoint39 final2 commands before later admissions

These are historical maintenance commands run from the workbench directory under the documented local project root. Recovery builds use the already installed runtime configuration; ordinary TeX installations can still compile the standalone source with three ordinary passes. No binary format/map/package is included.

Integrated exact-source insertion drivers present at closeout: `programs/maintenance/paper4_integrate_225.py`. Each preserves immutable earlier proofs and uses the separately completed mutual-comparison gate; an insertion script is not itself a fresh mathematical check.

The actual build command was `python3 programs/maintenance/paper4_checkpoint39_build.py --name paper4_checkpoint39_final2`. It uses the reviewed243-page38 source/PDF baseline, Python3/PyMuPDF/Pillow/pdfLaTeX, three passes, source/PDF hashing and changed-page pixel comparison. Rendering by itself is not visual inspection. The earlier `--compile-only` stage, when present, deliberately records no rendered or visual coverage.


The exact aggregate command selected from the saved input records is:

```bash
python3 programs/maintenance/paper4_checkpoint39_aggregate_reviews.py --name paper4_checkpoint39_final2 --visual checks/outage_20261125/root/checkpoint39_final2_visual_root.json --visual checks/paper4_checkpoint39_final2_visual_circuits.json --expert checks/outage_20261125/root/checkpoint39_final2_actual_text_review.json --newcomer checks/paper4_checkpoint39_final2_actual_newcomer_circuits.json
```

It verifies disjoint actual page coverage, exact final hashes and complete source-bound expert/newcomer readings. `python3 programs/maintenance/paper4_finalize_checkpoint39.py --name paper4_checkpoint39_final2` then checks all changed/inherited pages and exact current scope metadata before synchronizing the PDF/report/crosswalk/questions/deposit. `python3 programs/maintenance/paper4_checkpoint39_documentation_closeout.py` writes only this current README/program catalogue closeout after the synchronized report exists; it does not claim an archive seal or future research review.

`python3 programs/assemble_records.py` rebuilds the aggregate authored records with exact event types and provenance. `python3 programs/maintenance/prepare_checkpoint39.py --preflight --expected-new SZ4-225` and the same command without `--preflight` guard the exact completed frontier against immutable38, all prior canonical rows, latest completed actual review and all synchronized PDFs. The latter exclusively writes the dated inventory. After complete frozen preflight, `python3 programs/maintenance/make_checkpoint.py 39 "<actual delay reason if required>"` creates/readback-verifies one complete archive and records the actual seal. The scheduled slot is21:55:35UTC; any delay must be recorded honestly, with no fabricated catch-up checkpoint.

The complete report currently records247pages,19 actually reviewed changed pages and228 exact pixel matches. No truncated image/text output or proof-copy time is silently upgraded to inspection or independent-proof time.

### Historical pending R3 driver before its later execution

`programs/maintenance/paper4_integrate_226.py` is staged but has not been executed at this closeout. It requires the exact current source hash and explicit complete fresh/forward/reverse file paths plus hashes. After verified full mutual comparison it can insert the complete original R3 theorem, preserve any reviewed225-only checkpoint39 source/PDF/report and review logs before revising the unsealed current report, and mark the new build pending. Parsing this driver is not proof admission, a fresh mathematical check or manuscript completion. Its complete author-based TeX remains explicitly pending in the checks directory.

## Checkpoint39 original-family refinements and guarded build

These are historical maintenance commands run from the workbench directory under the documented local project root. Recovery builds use the already installed runtime configuration; ordinary TeX installations can still compile the standalone source with three ordinary passes. No binary format/map/package is included.

Guarded exact-source insertion drivers present at closeout: `programs/maintenance/paper4_integrate_225.py`, `programs/maintenance/paper4_integrate_226.py`, `programs/maintenance/paper4_integrate_227.py`. Each preserves immutable earlier proofs and requires the separately completed mutual-comparison gate. Only IDs listed in the synchronized report are admitted; a present pending driver is not an execution, admission or fresh mathematical check.

The actual build command was `python3 programs/maintenance/paper4_checkpoint39_build.py --name paper4_checkpoint39_final4`. It uses the reviewed243-page38 source/PDF baseline, Python3/PyMuPDF/Pillow/pdfLaTeX, three passes, source/PDF hashing and changed-page pixel comparison. Rendering by itself is not visual inspection. The earlier `--compile-only` stage, when present, deliberately records no rendered or visual coverage.

The exact actual-review transfer command was `python3 programs/maintenance/paper4_checkpoint39_transfer_reviews.py --from-name paper4_checkpoint39_final3 --to-name paper4_checkpoint39_final4 --visual checks/outage_20261125/root/checkpoint39_final3_visual_root.json --visual checks/outage_20261125/operator_k/checkpoint39_final3_visual_operator.json --visual checks/paper4_checkpoint39_final3_visual_circuits.json`. It checks full RGB samples and raster dimensions at the same page index, preserves every original source/PDF/review hash and attribution including upstream inheritance, and creates delta sheets only for pixels still requiring an actual view. The transfer itself is not a new image inspection. Evidence: `checks/paper4_checkpoint39_actual_review_transfer_paper4_checkpoint39_final4.json`.

The exact aggregate command selected from the saved input records is:

```bash
python3 programs/maintenance/paper4_checkpoint39_aggregate_reviews.py --name paper4_checkpoint39_final4 --visual checks/outage_20261125/circuits/checkpoint39_paper4_checkpoint39_final4_inherited_1.json --visual checks/outage_20261125/circuits/checkpoint39_paper4_checkpoint39_final4_inherited_2.json --visual checks/outage_20261125/root/checkpoint39_final4_visual_root.json --visual checks/outage_20261125/operator_k/checkpoint39_final4_visual_operator.json --visual checks/paper4_checkpoint39_final4_visual_circuits.json --expert checks/outage_20261125/root/checkpoint39_final4_actual_text_review.json --newcomer checks/outage_20261125/operator_k/checkpoint39_final4_actual_newcomer_review.json
```

It verifies disjoint actual page coverage, exact final hashes and complete source-bound expert/newcomer readings. `python3 programs/maintenance/paper4_finalize_checkpoint39.py --name paper4_checkpoint39_final4` then checks all changed/inherited pages and exact current scope metadata before synchronizing the PDF/report/crosswalk/questions/deposit. `python3 programs/maintenance/paper4_checkpoint39_documentation_closeout.py` writes only this current README/program catalogue closeout after the synchronized report exists; it does not claim an archive seal or future research review.

`python3 programs/assemble_records.py` rebuilds the aggregate authored records with exact event types and provenance. `python3 programs/maintenance/prepare_checkpoint39.py --preflight --expected-new SZ4-225,SZ4-226,SZ4-227` and the same command without `--preflight` guard the exact completed frontier against immutable38, all prior canonical rows, latest completed actual review and all synchronized PDFs. The latter exclusively writes the dated inventory. After complete frozen preflight, `python3 programs/maintenance/make_checkpoint.py 39 "<actual delay reason if required>"` creates/readback-verifies one complete archive and records the actual seal. The scheduled slot is21:55:35UTC; any delay must be recorded honestly, with no fabricated catch-up checkpoint.

The complete report currently records254pages,72 actually reviewed changed pages and182 exact pixel matches. No truncated image/text output or proof-copy time is silently upgraded to inspection or independent-proof time.

## Prepared actual review29 and preserved preparation versions

The fixed next actual review is due25November2026 at22:40:35UTC. From the workbench, `python3 programs/maintenance/research_review29_v2.py preflight` checks the immutable review28 baseline, current canonical rows, all83 questions and44 tracked legacy claims without executing a snapshot or review. The modes `snapshot` and `review` respectively create one exclusively named due-time snapshot and audit its127 rows; both reject execution before the scheduled time. The input is `checks/outage_20261125/review29_frontier_input.json`, with the exact fully paired226/227 frontier and the prior counted223/224/225 baseline.228 remains pending. Later typesetting of225 is not new movement.

The guarded launcher command is `python3 programs/maintenance/research_review29_scheduler_v2.py`. It was already launched22:16:04.670215UTC and must not be launched a second time. It checks exact driver/frontier/baseline hashes, waits for the original due time, then invokes snapshot and review sequentially and reads back every declared output. A brief coordinated write hold is required at the due-time snapshot. Its own waiting status is not an executed research review. No main, canonical or question component is edited by the driver; the actual dated review outputs and append-only continuation notes are separate. Only Python3 standard-library modules are required. If the fully paired mathematical frontier changes before the due time, preserve the original fixed inputs and explicitly prepare/rearm a revised version rather than silently changing the running scheduler's expected hashes.

`programs/maintenance/research_review29.py` and `programs/maintenance/research_review29_scheduler.py` are preserved initial preparation versions. Their full readback detected an incorrect prior line-state filename before execution. The corrected `_v2` files and actual preparation/readback/launch records preserve the chronology; the originals are not the active commands and do not claim an earlier completed audit. Exact evidence is in `checks/outage_20261125/foundation/review29_scheduler_v2_launch.json` and its neighboring preparation/readback records. No future review completion or movement is inferred by this catalogue.

## Historical checkpoint40 guard preparation — initial empty admission sets

`programs/maintenance/prepare_checkpoint40.py` is prepared from the sealed39 guard and binds the exact checkpoint39 archive SHA-256 `038755eca93940febf562f2bd93b207c1a27f08cc17894ab1df2d84ad87bfdf3`, all658 sealed canonical rows, and actual completed research review29. Its allowed and mandatory new-result sets and exact-label map are empty. Root must explicitly widen them only after complete paired proof checks and main/canonical integration. A reserved or staged candidate supplies no admission.

The read-only command `python3 programs/maintenance/prepare_checkpoint40.py --preflight` correctly stopped at the missing actual-review29 assertion during preparation; no inventory or review completion was claimed. After that actual review and all current source/PDF/text/visual gates pass, the same command without `--preflight` exclusively writes checkpoint40's inventory. The original scheduled slot is22:40:35UTC; later archives follow unused original45-minute slots.

The reviewed254-page39 source, PDF, full build report and aggregate visual/text records are preserved byte-for-byte from named members of the exact sealed archive under `build/paper4_checkpoint39_reviewed_baseline/`. Their hashes and archive-member locators are recorded in `checks/paper4_checkpoint40_baseline39.json`. No228 or229 proof content was read during guard preparation. The complete preparation/expected-block evidence is `checks/paper4_checkpoint40_guard_verification.json`; the initial guard is preserved under `checks/checkpoint40_guard_preparation_history/` with its one disclosed cadence-wording correction. This section documents preparation, not an executed inventory or a new mathematical check.

## Checkpoint40 original-family refinements and guarded build

These are historical maintenance commands run from the workbench directory under the documented local project root. Recovery builds use the already installed runtime configuration; ordinary TeX installations can still compile the standalone source with three ordinary passes. No binary format/map/package is included.

Guarded exact-source maintenance drivers present at closeout: `programs/maintenance/paper4_checkpoint40_compact_abstract.py`, `programs/maintenance/paper4_checkpoint40_source_coefficient_precision.py`, `programs/maintenance/paper4_integrate_checkpoint40.py`. Each preserves immutable earlier proofs and requires the separately completed mutual-comparison gate. The actual source sequence was `python3 programs/maintenance/paper4_integrate_checkpoint40.py --expected-source 88a675e0ad52c47466182f9a0e440366baedff62cbe60c11b673d48354c456b3`, then `python3 programs/maintenance/paper4_checkpoint40_compact_abstract.py`, then `python3 programs/maintenance/paper4_checkpoint40_source_coefficient_precision.py`. These require the exact recorded predecessor bytes and preserve every source/comment/crosswalk precision. The last two are editorial operations, not fresh proofs. Only IDs listed in the synchronized report are admitted; a present pending driver is not an execution, admission or fresh mathematical check.

The actual build command was `python3 programs/maintenance/paper4_checkpoint40_build.py --name paper4_checkpoint40_final3`. It uses the reviewed254-page39 source/PDF baseline, Python3/PyMuPDF/Pillow/pdfLaTeX, three passes, source/PDF hashing and changed-page pixel comparison. Rendering by itself is not visual inspection. The earlier `--compile-only` stage, when present, deliberately records no rendered or visual coverage.


The exact aggregate command selected from the saved input records is:

```bash
python3 programs/maintenance/paper4_checkpoint40_aggregate_reviews.py --name paper4_checkpoint40_final3 --visual checks/outage_20261125/root/checkpoint40_final3_visual_root.json --visual checks/outage_20261125/operator_k/checkpoint40_final3_visual_operator.json --visual checks/outage_20261125/circuits/checkpoint40_final3_visual_circuits.json --expert checks/outage_20261125/root/checkpoint40_final3_actual_text_review.json --newcomer checks/outage_20261125/operator_k/checkpoint40_final3_actual_newcomer_review.json
```

It verifies disjoint actual page coverage, exact final hashes and complete source-bound expert/newcomer readings. `python3 programs/maintenance/paper4_finalize_checkpoint40.py --name paper4_checkpoint40_final3` then checks all changed/inherited pages and exact current scope metadata before synchronizing the PDF/report/crosswalk/questions/deposit. `python3 programs/maintenance/paper4_checkpoint40_documentation_closeout.py` writes only this current README/program catalogue closeout after the synchronized report exists; it does not claim an archive seal or future research review.

`python3 programs/assemble_records.py` rebuilds the aggregate authored records with exact event types and provenance. `python3 programs/maintenance/prepare_checkpoint40.py --preflight --expected-new SZ4-228,SZ4-229` and the same command without `--preflight` guard the exact completed frontier against immutable39, all prior canonical rows, latest completed actual review and all synchronized PDFs. The latter exclusively writes the dated inventory. After complete frozen preflight, `python3 programs/maintenance/make_checkpoint.py 40 "<actual delay reason if required>"` creates/readback-verifies one complete archive and records the actual seal. The scheduled slot is22:40:35UTC; any delay must be recorded honestly, with no fabricated catch-up checkpoint.

The complete report currently records263pages,25 actually reviewed changed pages and238 exact pixel matches. No truncated image/text output or proof-copy time is silently upgraded to inspection or independent-proof time.

### Prepared-only review-transfer helper

`programs/maintenance/paper4_checkpoint40_transfer_reviews.py` accepts `--from-name`, `--to-name`, and repeated `--visual` arguments. It requires complete prior actual visual coverage and exact same-page RGB bytes and dimensions before carrying any actual view forward. Its SHA-256 is `f2d5670b8a964144e77c166c461be714416134dde4ebd1ae0b20ee76cc1ae1f9`. It was prepared but NOT executed for checkpoint40: every one of final3's25 changed pages received a new actual view. Rendering or a hash alone supplies no actual-view credit.

## Review30 guarded preparation — no early snapshot or review

All commands in this section run from the workbench with Python3 and the standard library. `programs/maintenance/research_review30.py` and `programs/maintenance/research_review30_scheduler.py` are preserved prepared-only predecessors. They were not launched. The v2 pair explicitly adds230 as pending before any scheduler launch; earlier prepared bytes are unchanged.

`programs/maintenance/research_review30_v2.py` is the current guarded audit of all83questions and44tracked claims,127rows. It fixes the immutable actual review29 snapshot SHA-256 `2a2da1e5c0a15de18b041bb7c940e1f4227777667dc9433d8058e73968ec876f`,658canonical rows, the already counted226/227 mathematical frontier, and the unchanged eight stopped lines. The exact modes are `python3 programs/maintenance/research_review30_v2.py preflight`, `python3 programs/maintenance/research_review30_v2.py snapshot`, and `python3 programs/maintenance/research_review30_v2.py review`. Preflight performs read-only validation and earns no research-review credit. Snapshot and review are guarded until23:40:35UTC on25November2026 and must not be run early or backdated. The fixed newly completed mathematical frontier is228/229;230 remains pending. Later typesetting of228/229 is not a new result. Any further complete pair before the actual review requires an explicitly preserved/versioned frontier and scheduler re-arm; no live hash is silently changed.

`python3 programs/maintenance/research_review30_scheduler_v2.py` pins the driver SHA-256 `470cd1c9faaf6f90333b5387e67ea434939f0627c43ddaeb8a415c1f8da824f9` and frontier SHA-256 `83f4b9804deae4d51b5b3c8eeb55a83576179075a42ee9f94c749280ea4f96c4`, waits until the actual due time, and then creates the immutable snapshot and runs the127-row audit once. The scheduler SHA-256 is `3af24fb0bce8d70c079d7be8e49e982a45048f6dfda0a196e6c151ed9e100fae`. The durable preparation and separate entire-readback evidence is `checks/outage_20261125/foundation/review30_prepared.json`, `review30_pending230_prelaunch_version.json`, and `review30_v2_prelaunch_readback.json` in that same foundation directory. The last has SHA-256 `da555f47b0c532cc65de8ee3437daa1fe145917ea89ccc3455e8a004a721a2bf`. At this checkpoint40 catalogue closeout no timer, snapshot or review30 has been launched; only preflight ran. A later actual launch must have its own true-time record. The completed review29 and its preserved pending230-independent successor preparation are not rerun by this catalogue entry.

## Historical initial checkpoint41 inventory preparation

`programs/maintenance/prepare_checkpoint41.py` is prepared against the exact sealed40 archive (SHA-256 `09bab9b99ff4d0bfd497a70fdeddfc898fd05410651a6e54777decb59c9736cd`) and660 immutable canonical rows. `python3 programs/maintenance/prepare_checkpoint41.py --preflight` passed read-only at23:04:40UTC with EMPTY allowed/mandatory new sets and EMPTY label map, exact263-page40 source/PDF/report, and latest actual review29. The guarded no-flag inventory command was not executed. Root must explicitly widen all three admission fields after any complete new full proof pair and actual manuscript/build/QA admission.41 is due23:25:35UTC; review30 is due23:40:35 and is not required or claimed early. Full baseline/guard hashes and the disclosed preexecution literal corrections are in `checks/paper4_checkpoint41_baseline40.json` and `checks/paper4_checkpoint41_guard_verification.json`.At that initial preflight230/231 were pending research only; the later explicit authorization and synchronized report below supersede that initial frontier.

## Review30 explicit v3 rearm after230 completion

The earlier prepared drivers and armed v2 are preserved unchanged. The v2 host session94941 was explicitly interrupted and returned exit130 before the resumed23:30:04.317416 record; the exact stop second was not separately observed. It ran no due snapshot or audit. The preserved stop record is `checks/outage_20261125/foundation/review30_v2_explicit_stop_before_v3.json`.

`python3 programs/maintenance/research_review30_v3.py preflight` checks the fixed review29 baseline and the separately versioned `checks/outage_20261125/review30_frontier_input_v3.json`. Its observed preflight passed with661 canonical rows and127 audit rows. The fixed newly completed mathematics is228,229,230;231 remains pending. Driver SHA-256 `27f8a4073e5dec10868c603ee48bca0460716615bfad5e48e431277519cc327e`; frontier SHA-256 `c4b81210d7547832fdfe919d599ac1ed5bb3a502940dbf22c2cabef55e3cf13b`. The same driver accepts positional `snapshot` and `review` modes, guarded by the due time and immutable snapshot; no flag-style preflight interface is asserted.

`python3 programs/maintenance/research_review30_scheduler_v3.py` was actually armed at23:33:56.346511UTC, ready23:33:56.437902, host session97754. Scheduler SHA-256 `c0828387da36f19be24cd263c35bd1c6e81a27069cdc5d84abebef42edac7c0a`. It waits for the original23:40:35UTC due time before snapshotting and auditing; launch is not an actual review. The launch and host-sidecar records preserve these observations. The coordinated write hold begins23:40:30 and releases only after the actual immutable audit and complete readback.

The original truncated readback attempt remains explicitly excluded from full-reading credit. `checks/outage_20261125/foundation/review30_v3_complete_readback_correction.json` records the subsequent bounded complete driver delta/scheduler/frontier readings and full hash/size verification of all70 evidence files. No file-copy time, preparation, rearm, pending proof or typesetting edit creates mathematical movement.

## Checkpoint41 complete unaffected-input family and synchronized build

These commands run from the workbench directory under the documented local root. They are historical maintenance programs; a present script is not evidence that it ran. Ordinary TeX installations still compile the standalone source with three ordinary passes. Recovery uses the recorded local runtime; no binary format/map/package is bundled.

`python3 programs/maintenance/paper4_integrate_checkpoint41.py --expected-source c11389316f3c1f2e91fa144fbdf770194dd9bfac403b8a53311e1d59286f89c6` inserted only fully paired230 after verifying exact clean/author/fresh/readback/stage/comparison hashes and all prior references. It preserved the complete prior source and record components. The subsequent formatting-only correction is separately preserved in `checks/outage_20261125/root/checkpoint41_heading_format_correction.json`: all ten proof-internal heading wrappers changed, with all words and mathematics identical. The initial failed build is retained and has no PDF or visual-review credit.

`python3 programs/maintenance/paper4_checkpoint41_build.py --name paper4_checkpoint41_final2` built the final source in three clean passes, used the exact reviewed263-page40 source/PDF baseline, and rendered/hash-compared every page using Python3, PyMuPDF, Pillow and pdfLaTeX. `--compile-only` is also accepted and deliberately supplies no visual-review credit. Rendering alone is not inspection.

The actual aggregate command is:

```bash
python3 programs/maintenance/paper4_checkpoint41_aggregate_reviews.py --name paper4_checkpoint41_final2 --visual checks/outage_20261125/root/checkpoint41_final2_visual_root.json --visual checks/outage_20261125/foundation/checkpoint41_final2_visual_foundation.json --expert checks/outage_20261125/root/checkpoint41_final2_actual_text_review.json --newcomer checks/outage_20261125/foundation/checkpoint41_final2_actual_text_newcomer_review.json
```

The aggregator checks exact final hashes, disjoint actual changed-page coverage and complete source-bound expert/newcomer readings. `python3 programs/maintenance/paper4_finalize_checkpoint41.py --name paper4_checkpoint41_final2` then requires exact current scope metadata and all changed/inherited pages before synchronizing the PDF, report, numbered crosswalk, questions and deposit/build records. `python3 programs/maintenance/paper4_checkpoint41_documentation_closeout.py` preserves the preceding README/program catalogue and writes this closeout only after the synchronized report exists.

`python3 programs/assemble_records.py` rebuilds the aggregate authored records. `python3 programs/maintenance/prepare_checkpoint41.py --preflight --expected-new SZ4-230` checks exactly one new admission against immutable40, all660 prior canonical rows, exact typed proof coverage, the latest completed actual review and all five synchronized PDFs. The same command without `--preflight` writes the dated inventory exclusively. Its original empty authorization version and the complete explicit widening diff are preserved in the root check directory. No231 admission is authorized.

After a complete frozen preflight, `python3 programs/maintenance/make_checkpoint.py 41 "<actual delay reason>"` creates one complete immutable archive and reads back every member. The scheduled slot is23:25:35UTC; the actual late seal and reason are recorded. The next checkpoint uses the next unused original45-minute slot after that seal, with no catch-up archives. Original sources, external papers/extractions and earlier ZIPs remain excluded.

The final report records267pages,21 newly actually inspected changed pages and246 exact pixel matches. No truncated output, proof-copy time, typesetting edit or packaging event is upgraded to mathematical movement or an independent proof.

## Checkpoint42 exact two-visible transfer consequence and synchronized build

These commands run from the workbench directory with Python3 under the documented local recovery root. Presence of a script is not evidence that it ran. Ordinary TeX installations can still compile the standalone source with three ordinary passes; no binary format/map/package is bundled.

`python3 programs/maintenance/paper4_integrate_checkpoint42.py --expected-source f01050d750b268df58d68dccca257cd6ba4f0a84844cf2122cabfd3004d719b5` inserted only fully paired232 after verifying its exact proof/readback/comparison/stage hashes and already admitted dependencies. The full preceding source/components remain in `checks/checkpoint42_preintegration_state`. The corollary is a non-movement consequence, not a fresh reduction beyond actual review30. The sole subsequent source change is the live-observation timestamp, preserved at `checks/outage_20261125/root/checkpoint42_live_observation_update.json`.

`python3 programs/maintenance/paper4_checkpoint42_build.py --name paper4_checkpoint42_final2` built the final268-page source in three clean passes, rendered/hash-compared every page against the reviewed267-page41 baseline, and prepared contact sheets. It uses Python3, PyMuPDF, Pillow and pdfLaTeX. The optional `--compile-only` mode supplies no visual-review credit. Rendering itself is not inspection.

The completed aggregate command is:

```bash
python3 programs/maintenance/paper4_checkpoint42_aggregate_reviews.py --name paper4_checkpoint42_final2 --visual checks/outage_20261125/root/checkpoint42_final2_visual_root.json --visual checks/outage_20261125/foundation/checkpoint42_final2_visual_foundation.json --expert checks/outage_20261125/root/checkpoint42_final2_actual_text_review.json --newcomer checks/outage_20261125/foundation/checkpoint42_final2_actual_text_newcomer_review.json
```

The aggregator requires exact final hashes, complete changed-page evidence and full source-bound expert/newcomer text reviews. `python3 programs/maintenance/paper4_finalize_checkpoint42.py --name paper4_checkpoint42_final2` then synchronized the PDF, report,215-row numbered crosswalk, questions and deposit/build records only after those gates passed. Before execution its inherited heading was corrected to “Checkpoint42 — exact two-visible transfer consequence”; the initial unexecuted script and exact correction are preserved. `python3 programs/maintenance/paper4_checkpoint42_documentation_closeout.py` preserves the entire preceding README/PROGRAMS and writes only documentation and its closeout record after that finalizer report exists.

`python3 programs/assemble_records.py` rebuilds authored aggregate records. `python3 programs/maintenance/prepare_checkpoint42.py --preflight --expected-new SZ4-232` checks only232 against immutable41 and all661 prior canonical rows, exact typed proof coverage, latest completed actual review30 and all five synchronized PDFs. The same guard without `--preflight` writes the dated inventory and continuation/ledger notices; this documentation program does not run it. Original initial/empty authorization scripts and the explicit later232 widening remain preserved. No231 or233 admission is authorized by this guard.

After a frozen successful preflight, `python3 programs/maintenance/make_checkpoint.py 42 "<actual delay reason, if any>"` creates the single immutable archive and reads back every member. The original slot is26November00:10:35UTC. The actual seal and any delay must be recorded when observed; the next checkpoint uses the next unused original45-minute slot after the actual seal, with no catch-up archives. Original user sources, external papers/extractions and earlier ZIPs remain excluded.

The exact final42 coverage is17 changed pages with actual-view evidence (9 direct final2 inspections and8 exact-pixel inherited actual final1 views), plus251 exact41 page matches. No truncated output, proof-copy time, typesetting, source follow-up or packaging event is converted to proof credit or mathematical movement.

## Review31 armed strict-frontier audit

The immutable baseline is actual review30's snapshot, SHA-256 `6d255375a7141c22d7b9d2dbb854d68be3926fcaf5ca3c6ab5ed8969cb166353`, with661 canonical entries. `checks/outage_20261125/review31_frontier_input.json`, SHA-256 `b54f65afee449a6822411c94111b6de994e2f1d192d9dec458832cc9b501d8af`, records an empty new strict frontier,232 as a fully checked non-movement consequence of213/227/230, and231 as pending. Later pending233 was received after this fixed frontier; it is unpaired and has no movement or admission credit. The fixed frontier is not silently changed.

The exact positional interface is `python3 programs/maintenance/research_review31.py preflight`, `python3 programs/maintenance/research_review31.py snapshot`, and `python3 programs/maintenance/research_review31.py review`. Snapshot and review are due-time/immutability guarded; there is no flag-style preflight interface. The observed preflight passed662 canonical entries and127 audit rows (83 questions plus44 tracked rows). The complete stopping rule preserves all eight stopped lines; empty new strict movement advances the circuit counter0→1, and the second consecutive unchanged review stops research.232's canonical insertion cannot reset that counter.

`python3 programs/maintenance/research_review31_scheduler.py` was actually launched at2026-11-25T23:58:45.523729+00:00, ready23:58:45.653855UTC on25November, host session91762. It pins the exact driver/frontier/baseline hashes and waits until26November00:40:35UTC; the coordinated write hold starts00:40:30. Its launch is **not** an actual snapshot or review. Launch, entire readback, preflight and host evidence are in `checks/outage_20261125/foundation/review31_scheduler_launch.json`, `review31_prepared_readback.json`, and `review31_scheduler_host_session.json`. Any new genuinely paired strict reduction before the due time requires a preserved explicit frontier/script version, full readback/preflight and observed rearm. There is no early/backdated audit or repeat credit for already counted mathematics.

### Exact maintained program hashes

| Program in `programs/maintenance` | Bytes | SHA-256 |
|---|---:|---|
| `paper4_integrate_checkpoint42.py` | 14754 | `68ff58c3851f83d783226a7f4ff2f9970df5178fd3fa06f8c19e1f52ac9b2f9c` |
| `paper4_checkpoint42_build.py` | 4413 | `8d7ecc40e4b00f764d1f385dac2a87b5ba32e1001b1631a47ccc59cd0897ba12` |
| `paper4_checkpoint42_aggregate_reviews.py` | 3153 | `3e982200318a17c42345539b00b91a03fdcbd193e79c9a481a19f6b94f6508e0` |
| `paper4_finalize_checkpoint42.py` | 6541 | `445c95d56cb2b2649b3c21552c39ae6c84d1282fb1f79faf5044f1dc0a48b602` |
| `paper4_checkpoint42_documentation_closeout.py` | 12901 | `0cff08f8549fd0ef6ee651da8805cb2408fb4e8d7ded6e64d659d2dec5cffc0f` |
| `prepare_checkpoint42.py` | 15788 | `a2a8e0201aeb30561461b7e784624150c1c27fc0679e3c9fbbba573cff290c91` |
| `research_review31.py` | 24710 | `398b291069c077271c1e759a24030e7d729331982e578c494ad833ccaa8de7ba` |
| `research_review31_scheduler.py` | 3978 | `f4ab752063e4c029ce92ce59477c4e4bed7217b04b2210800d72317dad2736df` |

The complete prior README/PROGRAMS bytes are retained in `checks/checkpoint42_precloseout_documents`. Documentation closeout is separate from actual review31 and checkpoint42 sealing; neither future event is asserted complete here.

## Checkpoint43 two-target necessity and seven zero-cross reductions

Commands run from the workbench directory with Python3. Script presence is not execution evidence. `paper4_integrate_checkpoint43.py` inserted only fully paired233 after its complete proof/readback/comparison gates; root owns the main, canonical and question mutations. Its exact invocation and preserved predecessor source/components are recorded by that integrator. No231,234 or235 admission is authorized.

`python3 programs/maintenance/paper4_checkpoint43_build.py --name paper4_checkpoint43_final2` built272 pages with three clean passes, rendered every page and compared full pixels against the immutable268-page reviewed42 baseline. Optional `--compile-only` produces no visual credit. Dependencies are Python3, PyMuPDF, Pillow and pdfLaTeX; no binary TeX format/map/package is bundled. The completed aggregate command was:

```bash
python3 programs/maintenance/paper4_checkpoint43_aggregate_reviews.py --name paper4_checkpoint43_final2 --visual checks/outage_20261125/root/checkpoint43_final2_visual_root.json --expert checks/outage_20261125/root/checkpoint43_final2_actual_text_review.json --newcomer checks/outage_20261125/foundation/checkpoint43_final2_actual_text_newcomer_review.json
```

The aggregate requires final source/PDF hashes, all changed-page actual-view evidence and complete source-bound expert/newcomer text records. `python3 programs/maintenance/paper4_finalize_checkpoint43.py --name paper4_checkpoint43_final2` synchronized the final PDF, report, numbered crosswalk, questions and build/deposit records after those gates passed. Root directly viewed all20 changed final2 pages;252 others exactly match reviewed42. The prior final1 source/build and subsequent abstract-only tightening remain preserved. Rendering, truncated output and a copied proof are never inspection or independent-proof credit.

`python3 programs/maintenance/paper4_checkpoint43_documentation_closeout.py` runs only after the synchronized report exists. It preserves the entire prior README/PROGRAMS and copies the current CONTINUE/LEDGER for provenance, changes only README/PROGRAMS and its own evidence, and leaves the continuation files byte-identical. `python3 programs/assemble_records.py` rebuilds authored aggregates; this documentation script does not invoke it.

`python3 programs/maintenance/prepare_checkpoint43.py --preflight --expected-new SZ4-233` checks only233 against immutable42, all662 old canonical rows, exact typed proof evidence, latest completed review31 and all five synchronized PDFs. Root explicitly widened the initially empty guard only after233's full pair; the original empty guard and entire widening delta are preserved. Running the guard without `--preflight` creates the inventory and append-only continuation entries; this closeout does not run inventory. After a frozen successful preflight, `python3 programs/maintenance/make_checkpoint.py 43 "<actual delay reason, if any>"` creates the immutable archive and reads back every member. The original slot is2026-11-26T00:55:35+00:00; actual seal/delay are recorded only when observed. The next checkpoint is the next unused original45-minute slot after actual sealing, with no catch-up archive. User source files, external source PDFs/extractions and earlier ZIPs remain excluded.

## Review31 explicit preserved rearm and actual completion

The initial empty-frontier driver, scheduler, frontier, launch, host and events remain byte-for-byte in `checks/outage_20261125/foundation/review31_v1_preserved_before_v2/`, together with its manifest. Original host91762 was explicitly stopped at the observed00:30:02UTC second, exit130; subsecond stop time was not observed. Its due audit never ran. The separate stop record is `review31_v1_explicit_stop_before_v2.json` in that directory's parent.

The new v2 fixed frontier SHA-256 `3dd0eaed3016a11fa6bc2b1a6926e5db3feb22f169f44708e8813f25b98dcbdf` pins233 as the only new strict reduction,232 as non-movement,231 pending, and immutable review30 snapshot SHA-256 `6d255375a7141c22d7b9d2dbb854d68be3926fcaf5ca3c6ab5ed8969cb166353`. All proof metadata/evidence hashes were verified; no234 or235 proof was read for this mapping. Exact interfaces are `python3 programs/maintenance/research_review31_v2.py preflight`, `... snapshot`, and `... review`. They are positional modes, not a flag-style interface. Snapshot/review are due-time and non-overwrite guarded. The separate scheduler `python3 programs/maintenance/research_review31_scheduler_v2.py` pins the exact hashes, was launched at2026-11-26T00:33:19.127402+00:00, ready00:33:19.246872UTC, in host41595, and waited for00:40:35 after the00:40:30 hold. Entire script/frontier/delta and separate launch readbacks are preserved; the context-truncated attempt receives no read credit.

The actual immutable snapshot completed00:40:35.187910UTC,101 files, SHA-256 `8b3109ceca31d1165a002cdefc4f09cafb1a533f977769789d2c54450cea4c33`. The127-row audit completed00:40:35.315899UTC. `checks/outage_20261125/recovery_review31.json` has SHA-256 `b4caf5d769b38d2f26fd4835a3babee4086be1167b88a942435a1a9e0e44cec9` and the output manifest SHA-256 `6b7686bcadbf98932a04e0cde478fb857ca1bb1580b639916ee72e5e03408319`. Whole output/snapshot bytes and hashes, the entire report/manifest/line states, and all127 ID/status entries were checked separately in `foundation/review31_actual_readback_closeout.json`. That additive closeout truthfully records234 as later pending, without modifying the fixed actual report. Source/PDF synchronization was still pending at the review snapshot; later43 finalization is not backdated into it.

All eight stopped lines remain unchanged. Only233 resets the active circuit counter to0.232 and every already counted theorem, additional check, correction, source retrieval and packaging event earn no reset. Next actual review32 is due01:40:35UTC, not an early catch-up review. This catalogue asserts no32 launch or completion and no43 archive seal.

### Exact maintained program hashes

| Program in `programs/maintenance` | Bytes | SHA-256 |
|---|---:|---|
| `paper4_integrate_checkpoint43.py` | 13151 | `5946829480a38e9a3bb1d45039a18ed5f6dbd2681702feca9d52286584b8c03d` |
| `paper4_checkpoint43_build.py` | 4411 | `ee7aca6d70947b9d09b88a8a87e26b5edff3cf68973dd03ee65551a255d24f24` |
| `paper4_checkpoint43_aggregate_reviews.py` | 3153 | `59a76d3d743c536fb8d1d199934101d6446a2649ca84cd02670a46c498fcf60a` |
| `paper4_finalize_checkpoint43.py` | 6535 | `53174a990d86cdb71fa389af26501aa9a828757eef80844ff34f7e0703525569` |
| `paper4_checkpoint43_documentation_closeout.py` | 13934 | `8e761071ef907dbcb2349e79c00adb8405596e71c4ca08ed1f370af1941e62b2` |
| `prepare_checkpoint43.py` | 16233 | `867df70afd4cd1fad494026dec5604107b4dac26abc09b877d2e5c6a6802ff74` |
| `research_review31.py` | 24710 | `398b291069c077271c1e759a24030e7d729331982e578c494ad833ccaa8de7ba` |
| `research_review31_scheduler.py` | 3978 | `f4ab752063e4c029ce92ce59477c4e4bed7217b04b2210800d72317dad2736df` |
| `research_review31_v2.py` | 24722 | `3b6f78d62f6bad5d509e5947a3c4fbe116f0ae79768e3dde7bb12b4999564c9c` |
| `research_review31_scheduler_v2.py` | 3993 | `968860e347b4ac6bef5aa587a936f51dd79a6071885a8ac28c9b4cce27d8191e` |

Full previous documentation and continuation bytes are preserved under `checks/checkpoint43_precloseout_documents`. Actual documentation deltas must be read separately after this script runs.

## Checkpoint44 unsafe-high necessity and the double-middle row

Commands run from the workbench directory with Python3. Script presence is not execution evidence. Root's `paper4_integrate_checkpoint44.py` admits only234 and235 after complete pair closure and pins the full original author transcriptions. It preserves all663 predecessor canonical rows. The entire two new proofs are retained;235 does not substitute for234's complete split-cell argument.231 is still pending.

`python3 programs/maintenance/paper4_checkpoint44_build.py --name paper4_checkpoint44_final1` built281 pages with three clean passes, rendered every page and compared full pixels against the immutable reviewed272-page43 baseline. Optional `--compile-only` grants no visual credit. Runtime dependencies are Python3, PyMuPDF, Pillow and pdfLaTeX; no binary TeX format/map/package is bundled. The completed aggregate command was:

```bash
python3 programs/maintenance/paper4_checkpoint44_aggregate_reviews.py --name paper4_checkpoint44_final1 --visual checks/outage_20261125/root/checkpoint44_final1_visual_root.json --visual checks/outage_20261125/operator_k/checkpoint44_final1_visual_operator.json --expert checks/outage_20261125/root/checkpoint44_final1_actual_text_review.json --newcomer checks/outage_20261125/foundation/checkpoint44_final1_actual_text_newcomer_review.json
```

The aggregate requires exact final source/PDF hashes, actual-view evidence covering all25 changed pages and complete source-bound expert/newcomer text records.256 remaining pages exactly match reviewed43. `python3 programs/maintenance/paper4_finalize_checkpoint44.py --name paper4_checkpoint44_final1` synchronizes the final PDF, numbered crosswalk, questions and build/deposit records only after those gates pass. No rendering, truncated output or copied proof earns actual-view or independent-proof credit.

`python3 programs/maintenance/paper4_checkpoint44_documentation_closeout.py` requires both the synchronized report and completed actual32. It preserves the entire prior README/PROGRAMS and copies CONTINUE/LEDGER, changes only README/PROGRAMS and its own evidence, and leaves the continuation files byte-identical. Root may subsequently run `python3 programs/assemble_records.py`; this script does not.

`python3 programs/maintenance/prepare_checkpoint44.py --preflight --expected-new SZ4-234,SZ4-235` is read-only and checks immutable43, all663 old canonical rows, exact proof gates, current actual review32 and all five synchronized PDFs. Root explicitly widened its initially empty authorization only after the full pairs; initial bytes and deltas are preserved. Unlike the older permissive interface, unsupported flags are rejected by argparse before writes. `--preflight-only` is not supported and must not be used. Running the guard without `--preflight` creates the inventory and append-only continuations; this documentation script does not. After frozen successful preflight, root may run `python3 programs/maintenance/make_checkpoint.py 44 "<actual delay reason, if any>"` and verify every archive member. The original slot is2026-11-26T01:40:35UTC; actual seal/delay are recorded only when observed. The next checkpoint is the next unused original45-minute slot after sealing, without catch-up archives. User source files, external source PDFs/extractions and earlier ZIPs remain excluded.

The generic archive writer's prior basename test omitted nested files named `MANIFEST.json`. Root preserved the original and made the one-expression repair at01:39:39UTC: only the generated top-level manifest is excluded now, so nested provenance manifests enter future archives. `make_checkpoint.py` SHA-256 is `9187e121575818d9051468501002c0c2a4ce9fef793c665a44be4bd28a448f80`; exact original/diff/record are in `checks/outage_20261125/root/make_checkpoint_before_nested_manifest_precision.py` and `make_checkpoint_nested_manifest_precision.diff` / `.json`. Historical ZIPs remain unchanged; no retroactive nested-manifest completeness is claimed. Future seals still require complete CRC and member-byte verification.

## Review32 preserved supersession and actual due-time audit

Snapshot annotation dated2026-11-26T01:42:07.203057+00:00: the immutable line-state/current-gate text carries a copied preparation phrase saying final synchronization pending. The actual report and snapshot hashes correctly identify fully synchronized44 at01:37:58.546039; the copied phrase does not supersede that observed status. The actual typed-check count1582 is the assembled snapshot before the root01:38:46 QA event was included by a later assembly. The original audit remains unchanged, and neither clarification changes mathematical movement.

The entire initial EMPTY driver/scheduler/frontier, preparation/readback, launch/host and events remain byte-for-byte in `checks/outage_20261125/foundation/review32_initial_preserved_before_v2/`, manifest SHA-256 `a4b123e95fb325d80a0f2cf95078aebe1d2b7b2423f16e49a207bdca8bfa1451`. Initial host21365 launched01:03:49.815143UTC. The later stop request returned `Unknown process id`; process inspection found no scheduler, no initial snapshot/result existed, and no successful termination time is claimed. The exact failed-stop history is preserved in `review32_initial_stop_attempt.json`.

Under explicit root authorization, the obsolete original driver and scheduler paths were replaced at01:29:08.442795--01:29:08.443192UTC with fail-closed supersession stubs. Their exact prior bytes and event history were not altered in the preserved bundle. The replacement breaks the initial scheduler's pinned driver hash before any snapshot/review write even if a stale loaded process survived; that process may only record its own failure diagnostics. Newly invoked old paths exit before writes. `review32_initial_disarm_supersession.json` preserves the actual writes/hashes and uncertainty. The old paths listed in the hash table below are intentionally stubs, not the preserved original scripts.

The separate v2 fixed frontier SHA-256 `8fd620c3efa76ebff4bcb54c5380df890466c2a5ed31f27c1b16e6e90d1a21a9` admits exactly234+235 as strict new reductions and231 pending, anchored to immutable review31 snapshot SHA-256 `8b3109ceca31d1165a002cdefc4f09cafb1a533f977769789d2c54450cea4c33`. It explicitly preserves the limited235 exposure qualification and does not double-count overlapping GH or old zero-cross cases. Entire scripts, frontier, delta and launch were read back; the earlier truncated frontier attempt grants no read credit. Read-only preflight passed01:34:22.308568UTC against665 canonical rows,83 questions and44 tracked claims.

Exact positional interfaces are `python3 programs/maintenance/research_review32_v2.py preflight`, `... snapshot`, and `... review`. The latter two are due-time/non-overwrite guarded. `python3 programs/maintenance/research_review32_scheduler_v2.py` pins every version hash and was actually launched at2026-11-26T01:34:46.532419+00:00, ready01:34:46.664876UTC, host21736, for the original01:40:35 due time after the01:40:30 shared hold. No early review or snapshot ran. It has separate v2 launch/events/result files. The actual completed report is `checks/outage_20261125/recovery_review32.json`, SHA-256 `57959df072c4eb3360dba710177b711dec610bd7e5cefa44bd354ae939d566d1`; the actual output/snapshot readback closeout is separate. Only234+235 are counted once at32; main synchronization or later typesetting cannot reset33 again. All eight stopped research lines retain their stopped state.

### Exact maintained program hashes

| Program in `programs/maintenance` | Bytes | SHA-256 |
|---|---:|---|
| `paper4_integrate_checkpoint44.py` | 5920 | `273e39472d1a65d7ed3f8e9825861f95563acde7c31ec9a50f5d2b81b8dcca4a` |
| `paper4_checkpoint44_build.py` | 4411 | `6ca548417836d1a9e35b4430abe81efedf60c2decab51946fada941d2030bc1d` |
| `paper4_checkpoint44_aggregate_reviews.py` | 3153 | `dcc4a320b2614c4b36e49a38ce5af7b8b9ac42bf2e4f1c560f98b59f8ccd922f` |
| `paper4_finalize_checkpoint44.py` | 6535 | `a095c2999d99da1deafcb154e37d7ae9bbf2722c3226ad889c1e5e9f9f46ae33` |
| `paper4_checkpoint44_documentation_closeout.py` | 16138 | `ed903faad46a1cdb26d3b715799def63c785f1374f09c908d9c22caa005dfe90` |
| `prepare_checkpoint44.py` | 16849 | `1cfd461dec5c039e2ff4b3969d5d57e7f096044585fa7023c1a980780cb33432` |
| `research_review32.py` | 507 | `09b6ab1675b0795b01c6f1e677edfbb0d05a8c7b4d7a5262d8ee063598fae96e` |
| `research_review32_scheduler.py` | 507 | `09b6ab1675b0795b01c6f1e677edfbb0d05a8c7b4d7a5262d8ee063598fae96e` |
| `research_review32_v2.py` | 24726 | `29fc4bf30f082c69a58dcb7010d79c21e701507e944cec68cbfdf5f0947acb2c` |
| `research_review32_scheduler_v2.py` | 3993 | `1a85421cbe7d961db33b4dce04ceb3ce868f750e572a83e5d67f741393402583` |
| `make_checkpoint.py` | 3414 | `9187e121575818d9051468501002c0c2a4ce9fef793c665a44be4bd28a448f80` |

Full previous documents and continuation bytes are preserved in `checks/checkpoint44_precloseout_documents`. Documentation deltas require their own entire readback. This catalogue does not claim an archive seal.

## Checkpoint45 and review33 preparation snapshot

The following catalogue records the actual preparation state before any45 source integration or new result admission. Later execution/authorization records supersede only their own status fields.

# Prepared checkpoint 45 and armed actual review 33

Prepared interfaces only. Root retains admission, main/canonical, integration, inventory and seal ownership. No checkpoint 45 build, aggregation, finalization or inventory has been executed by foundation. No new candidate is authorized by this preparation.

## Immutable reviewed checkpoint 44 baseline

The five read-only files in `build/paper4_checkpoint44_reviewed_baseline/` preserve the entire reviewed 281-page source/PDF/report/visual/text state. Their full bytes independently match both the live checkpoint 44 files and the sealed archive. The archive SHA256 is `b1ef96f2945eecdaff78094218db28edb2b1aa6c7bea010cfb072e1a46392bf6`; the actual seal was 2026-11-26 01:44:27.591614 UTC. The copied manifest SHA256 is `299fde2ee919f868486f7181e2f285445115196f589e4d3100bafe937d90ef01`. Copying preserves existing QA and grants no new visual or proof credit.

## Checkpoint 45 prepared programs

All program paths below are relative to `workbench/programs/maintenance/`.

| Program | Exact interface | SHA256 |
| --- | --- | --- |
| `prepare_checkpoint45.py` | `--preflight` is read-only. Optional `--expected-new ID,ID` must satisfy the root-authorized sets, which are currently EMPTY. Running without `--preflight` writes the actual inventory and continuations and is reserved to root. Unknown arguments are rejected. | `eafc84c15634b2fef13fb8003eb277d3fd341c732d4f7d9ead41f37c27e52aa4` |
| `paper4_checkpoint45_build.py` | `--name NAME [--compile-only]`; three TeX passes, warning checks and pixel comparison with immutable reviewed 44. Not run. | `6114f975b8b5792fc2724c1b91dcd634543d132387b603a2f5dbe87dd4a972d9` |
| `paper4_checkpoint45_aggregate_reviews.py` | `--name NAME --visual RECORD [--visual RECORD ...] --expert RECORD --newcomer RECORD`; complete source/PDF-bound text and actual-page coverage. Not run. | `eb9bfe90dd1c7e52cc9dccf68951b678ab058436f7962cd752cf92540ea0a62c` |
| `paper4_finalize_checkpoint45.py` | `--name NAME`; requires exact current scope plus complete QA before synchronization. Not run. | `e9cfaab0feb743fdf234d91432f66239f120d6eebd0f2dd8c2ae49b2b19e6d24` |

The guarded scheduled slot is 02:25:35 UTC. All 665 old canonical rows must be unchanged. Allowed/default mandatory new IDs and new labels are EMPTY. The checkpoint 45 integration program and `checks/paper4_checkpoint45_current_scope.json` remain unset. A 45 report is preferred; exact unchanged source/PDF may use the fully reviewed 44 fallback. The latest actual review must be at least 32 before 02:40:35 and at least 33 afterward. The next checkpoint uses the next unused original 45-minute slot after the actual seal.

Read-only preflight passed 01:51:33.080170 UTC: 665 canonical, 1583 typed checks, 669 source events, 88 review events, 9929 crosswalk rows and 83 questions; pages 71/25/20/281/33; no new IDs. The initial unexecuted guard and delta are preserved; its archive basename and two chronological prose references were corrected before any execution. Complete code/delta reads and separate full-byte baseline verification are recorded in `checks/outage_20261125/foundation/checkpoint45_pipeline_entire_readback_preflight.json` (SHA256 `7a3c154161458be9f01cecd4136525d90dfec0782244b717a064d646fb553c1f`).

## Armed actual review 33

`research_review33.py` has positional modes `preflight`, `snapshot`, `review`; only `preflight` has run. Its SHA256 is `cd7e7e2f321c80a82aa72a1dfbe85ffb1d1eb302511c8072ad56a883acd55bd0`. `research_review33_scheduler.py` takes no arguments and has SHA256 `64b737184a9cb2b390dd39f06224aacaeed2cfc0ebe07c9150c13d0b94458f2f`. The pinned frontier `checks/outage_20261125/review33_frontier_input.json` has SHA256 `a77a5cfb700c98e156e6974594cd6be86d8691bc1ececf3e65fbdd7e8cdea8ed`.

The scheduler launched 01:55:48.256869 UTC on host session 78855 and became ready 01:55:48.386774. It waits for the unchanged original due time 02:40:35 UTC; a shared input hold is planned from 02:40:30. Its independent read-only preflight passed with 665 canonical rows, 83 questions and 44 tracked claims. No snapshot, review, stop-counter change or early mathematical credit has occurred.

Actual review 32 is the immutable baseline, snapshot SHA256 `4b3bafe1bdf099ff0a056f496e3f1e5092aa8c2fe56c5967495c83d5f49c50e7`. Results 234/235 have already been counted exactly once. The new strict frontier is EMPTY, 232 remains a nonmovement consequence, and protected 231 remains pending. If unchanged at the due-time snapshot, the active circuit counter increments from 0 to 1; all eight stopped lines remain stopped. Any later fully paired reduction requires an explicit preserved version and rearm, never silent modification of the pinned generation.

Complete readback/preflight: `checks/outage_20261125/foundation/review33_preparation_entire_readback_preflight.json`, SHA256 `b89294e9bcbfefdcc8996e987b76f24de09f76fcadf0b7a6ee1b0068f114fca8`. Actual launch record SHA256 `d46929808e2dbc6a955e48f007708423a2d2db6444ec79052362cf68da05aca5`. Host-launch record `checks/outage_20261125/foundation/review33_scheduler_host_launch.json`, SHA256 `0473d0b25d6ee316aaa0a384d0342dd8c459e4626d0d60124b0eb8fef93e10de`. All old proof/exposure qualifications remain unchanged; no pristine-isolation claim or protected proof access is added.


## Checkpoint45 actual source-only closeout

Root's initially EMPTY `paper4_integrate_checkpoint45.py` remained EMPTY and executed with zero new admissions at02:18:07.548292UTC. Its exact plan is `checks/paper4_checkpoint45_source_only_plan.json`; source/plan hashes, full root readbacks and preserved preintegration documents are separate. The conditional236 source draft remained unexecuted. The integrator changed only the current source-observation time and one blank line; all old canonical rows and full mathematical bodies are unchanged.

Actual build: `python3 programs/maintenance/paper4_checkpoint45_build.py --name paper4_checkpoint45_final1`. Actual aggregation uses the root expert/visual records and operator_k newcomer record under `checks/outage_20261125/`; actual finalizer uses the same build name. Complete QA precedes synchronization and grants no new independent-proof credit. `python3 programs/maintenance/paper4_checkpoint45_documentation_closeout.py` preserves prior README/PROGRAMS and CONTINUE/LEDGER, changes only its named documentation/evidence, and does not run assembly or inventory. The guard remains `python3 programs/maintenance/prepare_checkpoint45.py --preflight` for read-only verification; omitting `--preflight` writes the actual inventory. Unknown flags are rejected. Sealing uses the unchanged strict next-unused-slot archive writer and complete CRC/member-byte verification.

The exploratory stdlib-only program `programs/experiments/independent_middle_local_factors.py` is preserved with SHA256 `54c241b979464ac907870b5f01290b2cf3cb891b8fe8057c0b72895b849ff1df`. Running it from the workbench writes a non-overwriting diagnostic under the root236 records. It enumerates necessary local target restrictions, omits outside/full-frame data, and explicitly is not a circuit realization or proof. Its failed exploratory inference and the honest incomplete root proof remain separate. Do not expose these exploratory files to a protected checker. No enumeration earns a theorem or movement credit.

Current maintained program hashes (the earlier preparation catalogue remains historical):

| Program | Bytes | SHA256 |
|---|---:|---|
| `paper4_integrate_checkpoint45.py` | 5835 | `1f35849c65686437273f35c7fb012a174e7207c67671713bb96ae9aaec89cdf4` |
| `paper4_checkpoint45_build.py` | 4411 | `6114f975b8b5792fc2724c1b91dcd634543d132387b603a2f5dbe87dd4a972d9` |
| `paper4_checkpoint45_aggregate_reviews.py` | 3153 | `eb9bfe90dd1c7e52cc9dccf68951b678ab058436f7962cd752cf92540ea0a62c` |
| `paper4_finalize_checkpoint45.py` | 6535 | `e9cfaab0feb743fdf234d91432f66239f120d6eebd0f2dd8c2ae49b2b19e6d24` |
| `paper4_checkpoint45_documentation_closeout.py` | 7915 | `25e3888f82835b12e06da84de3e34eb9c3b81803b35202eb4f5cf041a214669d` |
| `prepare_checkpoint45.py` | 16124 | `eafc84c15634b2fef13fb8003eb277d3fd341c732d4f7d9ead41f37c27e52aa4` |
| `research_review33.py` | 24859 | `cd7e7e2f321c80a82aa72a1dfbe85ffb1d1eb302511c8072ad56a883acd55bd0` |
| `research_review33_scheduler.py` | 3978 | `64b737184a9cb2b390dd39f06224aacaeed2cfc0ebe07c9150c13d0b94458f2f` |
| `make_checkpoint.py` | 3414 | `9187e121575818d9051468501002c0c2a4ce9fef793c665a44be4bd28a448f80` |

Prior entire documents are preserved in `checks/checkpoint45_precloseout_documents`. Actual documentation deltas require separate complete readback. This record does not claim an archive seal or a future research audit.

## Checkpoint 46 and review 33 version 2 preparation — 2026-11-26T02:37:32.076120+00:00

`programs/maintenance/prepare_checkpoint46.py` prepares a guarded inventory with an empty candidate set, empty mandatory set and no new theorem labels. It pins sealed checkpoint 45 as the 665-row canonical baseline, accepts only a current source/PDF-matched build report, and requires actual review 33 before its first preflight. At or after 03:40:35 UTC it requires actual review 34. It rejects unknown flags before writes. No inventory or seal has run. The checkpoint 46 slot is 03:10:35 UTC.

`paper4_checkpoint46_build.py`, `paper4_checkpoint46_aggregate_reviews.py` and `paper4_finalize_checkpoint46.py` retain the three-pass build, full changed-page raster comparison, actual page inspection and expert/newcomer text-review gates. The exact checkpoint 45 source, PDF and review reports were copied from the sealed archive and compared byte for byte to the current files. The preparation manifest, complete initial delta, preserved initial guard, one-label precision delta and entire final code readback records are under `checks/outage_20261125/root/checkpoint46_*`. These prepared programs authorize no new mathematical result.

`research_review33_v2.py` and `research_review33_scheduler_v2.py` explicitly supersede the preserved initial review 33 generation. The scheduler launched at 02:33:43.046417 UTC, due 02:40:35 UTC. Its pinned frontier includes pending SZ4-231 and SZ4-236, with no new fully paired result. Root completed the whole-code and whole-delta review; circuits independently checked only scheduler mechanics and permitted metadata. The original host handle was unavailable, with no observed termination time; obsolete entry points were replaced by recorded fail-closed stubs after exact preservation. All actual launch and readback records are retained. No review is run early and no pending proof receives movement credit.

## Checkpoint46 completed admission and QA catalogue

This current catalogue explicitly supersedes the earlier **prepared-only EMPTY46** catalogue above. That earlier text, original generators, EMPTY integrator/guard copies, initial plans and every exact preparation/admission delta remain historical and are not rewritten. Root authorized only231/236 after the complete proof and stage gates. Exact integration at2026-11-26T03:19:37.913998+00:00 used `checks/outage_20261125/root/checkpoint46_admission_plan_v2.json`, SHA256 `33fc12df7fd01780d3ba22b1ec56e7e57c8ce93a5de530d009603d95f81a0e60`; prior plan/status precision versions remain preserved. All665 older canonical rows remain exactly unchanged, and no237 result is admitted.

The following are recorded commands for their stated lifecycle stages, **not instructions to repeat create-exclusive historical actions**. Run portable TeX builds with ordinary installed TeX dependencies, or use the preserved recovered-runtime driver with its historical environment prerequisites. No package/cache trees are added to the deliverable.

```sh
python3 programs/maintenance/prepare_checkpoint46_admission_plan.py
python3 programs/maintenance/paper4_integrate_checkpoint46.py --plan checks/outage_20261125/root/checkpoint46_admission_plan_v2.json --plan-sha256 33fc12df7fd01780d3ba22b1ec56e7e57c8ce93a5de530d009603d95f81a0e60 --expected-source 6b2aca4f1dce1bd63b47f61391369dfcc4350f6cbfb41db60bc6d173ab43e50d
python3 programs/maintenance/paper4_checkpoint46_build.py --name paper4_checkpoint46_final1
python3 programs/maintenance/paper4_checkpoint46_aggregate_reviews.py --name paper4_checkpoint46_final1 --visual checks/outage_20261125/root/checkpoint46_final1_visual_review.json --visual checks/outage_20261125/foundation/checkpoint46_final1_visual_review.json --visual checks/outage_20261125/operator_k/checkpoint46_final1_visual_review.json --visual checks/outage_20261125/circuits/checkpoint46_final1_visual_review.json --expert checks/outage_20261125/root/checkpoint46_final1_actual_text_review.json --newcomer checks/outage_20261125/foundation/checkpoint46_final1_actual_text_newcomer_review.json
python3 programs/maintenance/paper4_finalize_checkpoint46.py --name paper4_checkpoint46_final1
python3 programs/maintenance/paper4_checkpoint46_documentation_closeout.py
python3 programs/maintenance/prepare_checkpoint46.py --preflight --expected-new SZ4-231,SZ4-236
```

The first plan generator, integration, aggregate and finalizer actions are non-overwriting and cannot simply be rerun into existing evidence. The build/render driver uses a unique `--name`; `--compile-only` does not supply visual-review credit. Actual source-bound expert/newcomer readings and actual changed-page views must precede aggregation and synchronization. Final46 report SHA256 `5f7ae3ae5e423e9eee6285de99d246832c32ba09da76fdc809ba52658210088b` records302 pages, three clean passes,202 actually inspected changed pages and100 exact-RGB inherited pages. The guard's `--preflight` is read-only; omitting it creates the actual inventory/continuation records after all current gates. Unknown flags are rejected. It requires actual33 now and actual34 at/after03:40:35; this closeout manufactures neither audit nor seal. The original due slot remains03:10:35; later sealing/delivery metadata is separate.

### Review34 version2: exact explicit supersession

Actual33 is `checks/outage_20261125/review33_manifest.json` and `recovery_review33.json`, based on snapshot SHA256 `535fecb3c0250a893a0d9480d458761f486c6bc7147600f97615ee5020f90a8e`. Its circuit counter1 is not altered by this catalogue. The initial34 scheduler was observed terminated with exit130 before03:12:27.524038; the exact signal microsecond was not exposed. Its complete armed generation is retained under `checks/outage_20261125/root/review34_initial_armed_preserved_20261126_0311/`, while the earlier pre-line-state-precision generation is also preserved. The original34 entrypoints now fail closed; the old frontier bytes remain unchanged. The explicit record is `checks/outage_20261125/root/review34_v2_explicit_supersession_root.json`.

Current `research_review34_v2.py` and `research_review34_scheduler_v2.py` pin the new frontier SHA256 `199a4131b851df203650c2d29bfec510c527a034a77d3f2fa1ab27dcf760680e`, driver SHA256 `e35377095f4cb8f37bab9c1fbd5eedb8e807fe4f8f88eb24b0b2c41116bf79d5` and baseline33 snapshot. The v2 scheduler actually launched at2026-11-26T03:12:35.677515+00:00 and waits for03:40:35UTC; launch and event records are separate under `checks/outage_20261125/foundation/review34_scheduler_v2_*`, with root host-launch evidence also preserved. The immutable frontier's earlier UNLAUNCHED wording is preparation-time history; the later launch record is the arm evidence. The intermediate236-only v2 prepared generation is preserved under `foundation/review34_v2_236_only_prepared_preserved/`; the final v2 frontier contains both231/236. Nested overlap creates one Boolean progress decision, never duplicate resets. The existing scheduler invokes preflight, then snapshot/review only at or after due time. Do not start another scheduler or manually duplicate the scheduled audit.

### Complete current program hashes

| Program | Purpose | Bytes | SHA256 |
|---|---|---:|---|
| `prepare_checkpoint46_pipeline.py` | Historical EMPTY-admission pipeline/baseline preparation; preserve, do not rerun into existing outputs | 5191 | `f4eb983be5c0e1268d3da29fcc1c0cdfbaf183776a63393c8f937de9d19b1c1a` |
| `draft_checkpoint46_pending231_scope.py` | Historical conditional scope draft; no independent admission authority | 8798 | `bc05dbccc7dd07ff58e621a2b7534121a0a79f69d96b66a931e2344ba3c6c2cf` |
| `prepare_checkpoint46_admission_plan.py` | Source-pinned fully paired admission-plan generator; create-exclusive historical action | 9922 | `974e3f2925f67cb6d6e2a112671f9f67bfb4b3980d7cabbb3eb25de312d6254d` |
| `paper4_integrate_checkpoint46.py` | Exact plan/hash/source guarded one-time integration | 5851 | `9f10b0cf960836783969ace5d31a54d568d4f41593bac94623380a731935bfea` |
| `paper4_checkpoint46_build.py` | Three-pass build and complete final-page rendering/comparison | 4411 | `671f3632f7f4f73b5a0d2fb0bbe61ff576f81c158b878d5ade5e1f87d0e04d12` |
| `paper4_checkpoint46_aggregate_reviews.py` | Bind actual source/PDF-specific text and visual coverage | 3153 | `fa4d688fe6a887c5bc9c6a99baec2d5b7eb51fc1e94b7b1ab4d1a4c10f502a0a` |
| `paper4_finalize_checkpoint46.py` | Guarded final source/PDF/report synchronization | 6535 | `ae855c7ea36f5f769a8a16e5454656cbcfc2ef1351282f5619de123dee6186bf` |
| `prepare_checkpoint46.py` | Explicit231/236 inventory guard; --preflight is read-only | 16307 | `1dec3b1fee4e9f828f73faeadeed6ef7fc3814d13f16e3e504b5838077d7031b` |
| `paper4_checkpoint46_documentation_closeout.py` | This preservation, append-only catalogue and exact-delta closeout | 22118 | `bfed6d38be83eb0a7581cc1dd06480e5ed9cb657d4763cb011dbadfd7f447cfc` |
| `prepare_research_review34.py` | Historical initial review34 preparation; superseded generation retained | 6026 | `2b2def0a39be5f1b79ef6a834c4bf9b4192b4e398b80701d7ac15bc5f7606644` |
| `research_review34.py` | Superseded initial driver entrypoint; current stub fails closed | 261 | `c033d42d41d52616e920d0f1cdf918fd005860747e187f64e647d158d9ba40cd` |
| `research_review34_scheduler.py` | Superseded initial scheduler entrypoint; current stub fails closed | 261 | `c033d42d41d52616e920d0f1cdf918fd005860747e187f64e647d158d9ba40cd` |
| `research_review34_v2.py` | Current pinned actual34 driver; preflight/snapshot/review modes | 25234 | `e35377095f4cb8f37bab9c1fbd5eedb8e807fe4f8f88eb24b0b2c41116bf79d5` |
| `research_review34_scheduler_v2.py` | Already armed due-time scheduler; do not launch a duplicate | 3993 | `591ec6a9735745db20a3fc3558ccc194d9cb92ae6237844ac5b3607a7ca1bc23` |
| `make_checkpoint.py` | Existing strict archive writer; actual seal remains a separate operation | 3414 | `9187e121575818d9051468501002c0c2a4ce9fef793c665a44be4bd28a448f80` |

The historical stdlib readback helper `checks/outage_20261125/circuits/SZ4-231_stage_readback_evidence/circuits231_stage_read_segment.py` (1337 bytes, SHA256 `481092d69df5553ead486bd0696563720d3efb30e216d253c6f18f9d31ed8397`) is also preserved. It pins the exact231 stage, emits bounded segments and creates separate segment metadata without overwriting existing outputs. Its original absolute-workspace and output-directory assumptions are historical QA prerequisites. Reading emitted text was an actual reviewer action; the helper alone is neither a proof nor a review. Full proof/stage/readback sources remain beside it.

This closeout first preserves the complete existing README/PROGRAMS/CONTINUE/LEDGER under `checks/checkpoint46_precloseout_documents`, then supersedes only README's current45 heading and appends this PROGRAMS catalogue. CONTINUE and LEDGER remain byte-identical; main/canonical/questions are untouched. The original documents, preservation manifest and entire two document deltas remain available for separate complete readback. No archive, delivery, future review or new237 proof is claimed by executing this script.

## Checkpoint47 operational chronology and prepared command catalogue

The following catalogue is the operator's preserved preparation-time record. Its statements that no operational command has run refer to that author's preparation, not later root actions. Root completed separate entire code/delta/baseline readbacks and ran read-only47 preflight at03:51:15.590998UTC: PASS, no new IDs, latest actual34. Root's chronology is in checks/outage_20261125/root/checkpoint47_pipeline_entire_root_readback.json. The inventory and archive are subsequent root operations with their own actual timestamps. Current source/PDF exactly equal46, so no47 build, render, review aggregation or finalizer is needed or credited. The catalogue and initial/final code versions are preserved.

# Checkpoint47 prepared pipeline — no operational execution

The original next unused slot after checkpoint46 sealed03:37:34.691345 is **2026-11-26 03:55:35 UTC**. This preparation introduces no mathematical admission and changes no current manuscript or documentation. The initial admission sets and labels are empty.

## Exact immutable baseline

Sealed46 archive SHA256 `d5e4843dc72b5e7e9e669044f222ccc4f4386b52006d7f55639b6871ef796763` pins667 canonical rows,1592 checks,679 source events,88 review events,10369 crosswalk rows and83 questions. PDF lengths are71/25/20/302/33. The exact paper4 source/PDF/build/text/visual baseline is extracted under `build/paper4_checkpoint46_reviewed_baseline`; its durable manifest is `checks/outage_20261125/operator_k/checkpoint47_reviewed46_baseline_manifest.json`. Extraction is not new visual inspection.

Actual review34 completed03:40:35.333892 and counted231/236 once, with circuit counter0 and eight stopped lines unchanged. Those results are checkpoint46 history. The next actual review35 is due04:40:35 and is handled separately. The guard requires34 before then and35 at or after that time. No future review or counter is created by this pipeline.

## Prepared commands, not executed

All operational paths below are relative to `deliverable/workbench`. Root retains execution and archive authority. The current source and PDF exactly equal46; the guard permits the existing46 report only on exact source/PDF and complete used-input/page/QA matches. Its historical report.new_results231/236 do not become47 admissions.

- Read-only verification, only when root authorizes: `python programs/maintenance/prepare_checkpoint47.py --preflight`.
- Dated inventory/continuation write, only when root authorizes: `python programs/maintenance/prepare_checkpoint47.py`.
- If root actually changes source and authorizes a fresh build: `python programs/maintenance/paper4_checkpoint47_build.py --name paper4_checkpoint47_final1`. A fresh workspace-local name is required; a previous build/QA tree is never overwritten.
- Review aggregation requires actual source/PDF-bound evidence: `python programs/maintenance/paper4_checkpoint47_aggregate_reviews.py --name paper4_checkpoint47_final1 --visual ACTUAL_VISUAL_RECORD --expert ACTUAL_EXPERT_RECORD --newcomer ACTUAL_NEWCOMER_RECORD`. Repeat `--visual` for each disjoint actual allocation. These uppercase record arguments are placeholders, not claims of existing reviews.
- Final synchronization requires an explicitly supplied root current-scope record and complete QA: `python programs/maintenance/paper4_finalize_checkpoint47.py --name paper4_checkpoint47_final1`. Its new-result authorization is also initially empty. It refuses to overwrite dated47 report/crosswalk/log outputs.

No47 integrator/current-scope/admission plan is prepared or executed by this assignment. Any future result requires root to explicitly widen the guard and finalizer authorization after full proof comparisons, actual manuscript insertion and full build/text/visual QA. The existing scripts do not authorize237 or any other pending claim.

## Preservation and exact verification

The exclusive preparation ran03:46:57.238039. Whole-code readback caught one inherited prose label Original46 slot; a separately recorded pre-execution precision changes it to Original47 while preserving the initial files, preparation record and diff. The due time and executable conditions were already correct. Final full-code, complete34,650-byte delta and baseline readbacks are recorded in `checks/outage_20261125/operator_k/checkpoint47_pipeline_entire_readback.json`; the authoritative delta is `checkpoint47_pipeline_entire_delta_v2.diff`. All five new Python files parse. No guard/preflight/build/aggregator/finalizer/inventory/scheduler/archive command has run. No fresh-proof, typed-check or research-movement credit is claimed.

## Checkpoint48 source-only closeout and actual review35

Closeout observed2026-11-26T04:42:45.070300+00:00. No new admission is authorized; all667 canonical rows equal sealed47. Final48 report SHA256 `21e7248425049c685a5535e2bb8c54972a1bbb1e9a2d1cd1aa5b87100f5152da` records source `e624d97f9fd22954d24b20a5f6ba1393072abcef30af2525601b3caa02af4960`, PDF `3f0cf0a594d34655c8ffdaddc894b12de680bddd2a6f5ba4bac6778a942c3c6c`,302 pages, three clean passes and completed actual/text QA. Current source differs from reviewed46 only by the04:00:20–04:00:21 retrieval-window phrase.237 remains private/pending; no proof route, theorem or movement credit is imported.

### Exact commands and lifecycle

Commands below are a catalogue of their recorded or guarded lifecycle, **not instructions to repeat create-exclusive historical actions**. Use the workbench directory. The48 pipeline preparer ran at2026-11-26T04:04:01.601115+00:00; the updater ran at2026-11-26T04:05:45.086100+00:00; final synchronization occurred at2026-11-26T04:28:45.616076+00:00. The build requires the documented installed/local TeX runtime. Rendering is not visual inspection; exact source/PDF-bound actual reviews precede aggregation. The guard's `--preflight` is read-only; its separate inventory-writing form omits that flag and remains root-owned. This closeout runs neither inventory nor archive writer.

```sh
python3 programs/maintenance/prepare_checkpoint48_pipeline.py
python3 programs/maintenance/paper4_checkpoint48_source_update.py
python3 programs/maintenance/paper4_checkpoint48_build.py --name paper4_checkpoint48_final1
python3 programs/maintenance/paper4_checkpoint48_aggregate_reviews.py --name paper4_checkpoint48_final1 --visual checks/outage_20261125/root/checkpoint48_final1_visual_review.json --expert checks/outage_20261125/root/checkpoint48_final1_actual_text_review.json --newcomer checks/outage_20261125/operator_k/checkpoint48_final1_actual_text_newcomer_review.json
python3 programs/maintenance/paper4_finalize_checkpoint48.py --name paper4_checkpoint48_final1
python3 programs/maintenance/prepare_checkpoint48.py --preflight
python3 programs/maintenance/prepare_research_review35.py
python3 programs/maintenance/prepare_research_review35_v2.py
python3 programs/maintenance/research_review35_v2.py preflight
python3 programs/maintenance/research_review35_scheduler_v2.py
python3 programs/maintenance/paper4_checkpoint48_documentation_closeout.py
```

Review35's initial preparation at2026-11-26T04:06:26.378719+00:00 remained unexecuted as an audit: full readback found inherited33-input/34-output filenames. Its original files are retained. The corrected v2 preparation at2026-11-26T04:10:17.056686+00:00 uses completed34 inputs and exclusive35 outputs, with the full correction and code/delta gate at `checks/outage_20261125/operator_k/review35_preparation_entire_readback_v2.json`. Never launch the initial driver/scheduler or duplicate the v2 scheduler. The v2 driver supports exactly `preflight`, `snapshot` and `review`; the latter two are invoked by the scheduler only at or after the actual due time.

Root's pinned v2 scheduler actually launched at2026-11-26T04:15:28.447626+00:00; the actual35 snapshot completed at2026-11-26T04:40:35.204702+00:00, and the audit completed at2026-11-26T04:40:35.300853+00:00. The scheduler result completed at2026-11-26T04:40:35.313898+00:00. `checks/outage_20261125/review35_manifest.json` (SHA256 `feca03aec86f131638fabeae48bef2c6f9f03fde3b2ca19344468baa270dddfd`) binds all four actual outputs; the report's counter1 and no-movement decision are runtime observations, not preparation-time predictions. Runtime launch/events/result files are `checks/outage_20261125/root/review35_scheduler_*`; the frozen input is `review35_frontier_input_v2.json`. The next actual review36 is due2026-11-26T05:40:35Z. All34 code/history and both35 preparation generations remain preserved.

### Complete maintained program hashes

| Program | Bytes | SHA-256 |
|---|---:|---|
| `prepare_checkpoint48_pipeline.py` | 6282 | `f514e09546a06cf2bc56d1e3deb126d9d081044892f3bc786c304c11aa118be9` |
| `paper4_checkpoint48_source_update.py` | 4004 | `37c21e0269ecfe57d07194e08670be0fb82cbd8b4faacc9962b1d916d7d8f7a3` |
| `prepare_checkpoint48.py` | 16165 | `bc9678b563cccd252527ff2c09718b3891a52cd35ad41d95412fd501ef2897d2` |
| `paper4_checkpoint48_build.py` | 4618 | `e94a56602bd0323b542af050cc05e91e66179146cc8f6928fa076f4a08d6fe54` |
| `paper4_checkpoint48_aggregate_reviews.py` | 3473 | `56bb7ee39f50b7f2ece05814894a96703d1ecaab4c4296b03c825a19281187cd` |
| `paper4_finalize_checkpoint48.py` | 7241 | `ef8b318fc51f43ef408f849e47a4980b0790178a6c43ca0a2621ebacf4652e54` |
| `prepare_research_review35.py` | 14256 | `cf9714b1109a1e825b3a065364a5bd35f26e217e4da0266f38803005767198ab` |
| `prepare_research_review35_v2.py` | 7299 | `3f69922577d1844571aab4dcf979e08d433aa2d45da14446cd5a57ff71900f48` |
| `research_review35.py` | 26630 | `1d6a794f16ad2d068b876c669fc39f9efdc5f625984496eaada70862a03155a0` |
| `research_review35_scheduler.py` | 4093 | `0936afd6d5fc8d71f13f7ce6d04621e97a3706621af87f43457461f3374d5a18` |
| `research_review35_v2.py` | 26642 | `d066bd49f990a79b52f6f858e4dce4d5c24a1959e65cefd22682902e05bc694f` |
| `research_review35_scheduler_v2.py` | 4099 | `b3d6376aba5ad66dc3117ef622cc6693697a5fb519734ebc7351dc56e58167b3` |
| `paper4_checkpoint48_documentation_closeout.py` | 19808 | `750621a911087f5ef5dfa49e34a96cc188820f7ca85f3aff2f96ead928a651e9` |

Key48 artifacts are `checks/paper4_checkpoint48_current_scope.json`, `paper4_checkpoint48_integration.json`, the final build/text/visual reports, and `checks/checkpoint48_presource_state/main_source_delta.diff`; exact reviewer attribution remains in those reports. The source updater's initial scope and integration-time QA-pending statement are historical; completed-QA precision is separately preserved. This catalogue does not redate those records or claim a new mathematical check.

Before either document write, this closeout preserves the complete actual absolute `workbench/README.md`, `workbench/PROGRAMS.md`, root `CONTINUE.md` and root `LEDGER.md` under `checks/checkpoint48_precloseout_documents`. Only README's current47 heading becomes a new current48 section plus historical47; PROGRAMS is append-only. CONTINUE/LEDGER, main/canonical/questions/PDFs and archive bytes remain untouched. The exact preservation manifest and full document deltas accompany `checks/paper4_checkpoint48_documentation_closeout.json`. Archive sealing/delivery remains a separate root operation.

## Checkpoint49 source-only closeout and prepared actual review36

Closeout observed 2026-11-26T05:18:35.704408+00:00. No admission or new mathematical movement is asserted; all667 canonical rows equal sealed48. Final49 report SHA256 fef8d875f3b476b0b1ac0572a56f1865c3833cf70c15d8a5310535ca377f56a6 binds source e3ac1d2bad22b47bd3a1c08e4c2b725f59a4598e9b424692b9f91f672b6a8f59, PDF 519786095fe8df8990ee1c4253ae004a98d9e5527d84d2e406a74012348275b3,302 pages, three clean passes, full text review and actual changed-page QA. Only the05:00:00–05:00:01 retrieval-window phrase differs from reviewed48.237 remains pending; no protected proof route is used.

### Exact commands and lifecycle

The following is a catalogue, not an instruction to repeat exclusive historical actions or launch a duplicate scheduler. Run paths from workbench. The49 pipeline preparation occurred at 2026-11-26T04:48:34.309336+00:00, source update at 2026-11-26T05:05:37.722435+00:00, and synchronization at 2026-11-26T05:08:59.963373+00:00. The guard's --preflight is read-only; the separate inventory-writing mode and archive writer remain root-owned. This closeout executes neither. Rendering alone never earns visual credit.

~~~sh
python3 programs/maintenance/prepare_checkpoint49_pipeline.py
python3 programs/maintenance/paper4_checkpoint49_source_update.py
python3 programs/maintenance/paper4_checkpoint49_build.py --name paper4_checkpoint49_final1
python3 programs/maintenance/paper4_checkpoint49_aggregate_reviews.py --name paper4_checkpoint49_final1 --visual checks/outage_20261125/root/checkpoint49_final1_visual_review.json --expert checks/outage_20261125/root/checkpoint49_final1_actual_text_review.json --newcomer checks/outage_20261125/operator_k/checkpoint49_final1_actual_text_newcomer_review.json
python3 programs/maintenance/paper4_finalize_checkpoint49.py --name paper4_checkpoint49_final1
python3 programs/maintenance/prepare_checkpoint49.py --preflight
python3 programs/maintenance/prepare_research_review36.py
python3 programs/maintenance/research_review36.py preflight
python3 programs/maintenance/research_review36_scheduler.py
python3 programs/maintenance/prepare_checkpoint49_documentation.py
python3 programs/maintenance/paper4_checkpoint49_documentation_closeout.py
~~~

The completed35 audit and its corrected v2 code remain the immutable baseline: snapshot 2026-11-26T04:40:35.204702+00:00, completion 2026-11-26T04:40:35.300853+00:00, manifest SHA256 feca03aec86f131638fabeae48bef2c6f9f03fde3b2ca19344468baa270dddfd, counter 1. Its original preparation/correction/launch history is retained in the48 catalogue; no new35 execution occurred here.

Review36 preparation completed at 2026-11-26T04:49:44.462680+00:00, using completed35 inputs and exclusive36 outputs. Root's complete-code/delta gate is checks/outage_20261125/root/review36_entire_root_readback.json (SHA256 218da5691f5e13ba700d34a9e0171f58c540bfea93f8f4bd52029c6e2f2eb418); the preparer's separate full gate is checks/outage_20261125/operator_k/review36_preparation_entire_readback.json. Root actually launched the pinned scheduler at 2026-11-26T04:54:00.794271+00:00; its ready event is 2026-11-26T04:54:00.924932+00:00. Due time is 2026-11-26T05:40:35Z. The frozen review36_frontier_input.json has no new mathematical frontier or consequence, with237 pending. The scheduler is armed, not completed: no future counter or stopping outcome is claimed. Only a completed due-time audit can determine it. Do not rerun the scheduler. Exact launch/events are checks/outage_20261125/root/review36_scheduler_launch.json and review36_scheduler_events.jsonl.

### Maintained program hashes

| Program | Bytes | SHA-256 |
|---|---:|---|
| `prepare_checkpoint49_pipeline.py` | 10099 | `a20c0ba9b5cd6397ebd9633e08db808c29a02d02076abf96b9c57ee8a5f2ed90` |
| `paper4_checkpoint49_source_update.py` | 4029 | `5fadc87e945c9c2329c65141bec4e3d5db4391c8a122d92974bc88de575f4f4f` |
| `prepare_checkpoint49.py` | 16165 | `fb4ac200eda4a45ce45f9db371802cb37cf21b2ef3447eb252c8a8858d99c7b8` |
| `paper4_checkpoint49_build.py` | 4618 | `9e4f3c95e01282e776401767e7efa5ed1b43a1306ca904a95c1c630a8fbd1a93` |
| `paper4_checkpoint49_aggregate_reviews.py` | 3473 | `d93750749207fecf28aaa0397fee230b15504b444d62e9c3a00868928fa49cab` |
| `paper4_finalize_checkpoint49.py` | 7241 | `d393453871c8e615a5b0fa7d568f0278d93d86db7871ce56d1b3843701df9973` |
| `research_review35_v2.py` | 26642 | `d066bd49f990a79b52f6f858e4dce4d5c24a1959e65cefd22682902e05bc694f` |
| `research_review35_scheduler_v2.py` | 4099 | `b3d6376aba5ad66dc3117ef622cc6693697a5fb519734ebc7351dc56e58167b3` |
| `prepare_research_review36.py` | 15383 | `3f7ef45f2815d2ea89a2f4ae2d1cbdc678cffa4dd02a09b5f9a9cf15b4081b2a` |
| `research_review36.py` | 29070 | `61822be6f6b51c266b58676f0dcde52350224132700d1d6e677752fa99a9e545` |
| `research_review36_scheduler.py` | 4093 | `3a97049a9fc597181cfc9f1e7f7e746f7edd2266f6b3905a6906b31a9f25894c` |
| `prepare_checkpoint49_documentation.py` | 17703 | `a66b122aed3f8f1e20cb9e420131480bfb460cdd5d2cab1f3356c400bac639c3` |
| `paper4_checkpoint49_documentation_closeout.py` | 21531 | `d484049abbbc7b4e3be16afffd15796466efa2b650c167df4a2142f411bfc151` |

The49 current scope, integration, build/text/visual reports and checks/checkpoint49_presource_state/main_source_delta.diff preserve actual chronology. Integration-time pending-QA wording remains historical; final scope/report record the completed review. The independent pipeline inspection and source-only newcomer records are under checks/outage_20261125/operator_k/checkpoint49_*; they earn no theorem credit.

Before either document write, the code preserves the complete actual absolute workbench/README.md, workbench/PROGRAMS.md, deliverable/CONTINUE.md and deliverable/LEDGER.md under checks/checkpoint49_precloseout_documents. It inserts current49 plus historical48 in README and appends this PROGRAMS section. The actual CONTINUE/LEDGER files, all main/canonical/question/PDF/archive bytes remain unchanged. Preservation hashes and both whole document deltas accompany checks/paper4_checkpoint49_documentation_closeout.json. Any237 comparison/admission or a completed/due review36 makes this fixed scenario fail closed and requires explicit reassessment.

## Checkpoint50 final stopped-state closeout

Actual documentation time 2026-11-26T05:47:22.134677+00:00. This conditional path was used only after actual36 completion 2026-11-26T05:40:35.411797+00:00 and both whole-audit readbacks. Evidence and hash pins are in checks/checkpoint50_final_state_authorization.json; the independent reader and all previous preparation/audit histories remain immutable. Review36's outcome is counter2, stopped, without new movement; no37scheduler or research restart is authorized.

Commands below are a lifecycle catalogue, not instructions to rerun exclusive actions. Run from workbench:

~~~sh
python3 programs/maintenance/paper4_checkpoint50_documentation_closeout.py
python3 programs/maintenance/prepare_checkpoint50.py --preflight
python3 programs/maintenance/prepare_checkpoint50.py
~~~

The shared checkpoint50_final_state.py is a read-only validator imported by those two commands; it is not an operational scheduler. The documentation command writes only README/PROGRAMS after preserving all four actual documents. Inventory separately preserves all four, writes checks/checkpoint50_inventory.json, and updates final CONTINUE/LEDGER. Both commands fail closed unless the completed36report/manifest/snapshot and independent/root full-readback evidence are hash-bound, all667canonical and five source/PDF sets equal sealed49, all nine research lines are stopped,237unadmitted, and no37artifacts exist. Neither command runs a build, source refresh, audit, scheduler or archive writer. Root's separate final-seal authorization and writer occur only afterward.

| Program | Bytes | SHA-256 |
|---|---:|---|
| `checkpoint50_final_state.py` | 13290 | `d283e2029da54007688745460e657e962e8b19913220dd7be1d163e499e2c6c7` |
| `paper4_checkpoint50_documentation_closeout.py` | 7507 | `33c24c9f2b8115b3dc112d379a5dd2fd0d26ccc8cfb4c1e53639f51d7aaa2985` |
| `prepare_checkpoint50.py` | 6965 | `2d0c9540ebd2bc706f890999ffabeeb28626abba3aad143e1bdeae66fc9e6d0d` |

All preceding49 build/source, actual35 and36 preparation/launch catalogues retain their actual historical times. The inherited49 report records3clean passes, actual page300 QA and301exact RGB matches;50adds no QA credit. Exact output metadata, prior document preservation and full diffs are in checks/paper4_checkpoint50_documentation_closeout.json and checks/checkpoint50_inventory.json. Original final50 due time is06:10:35UTC; actual seal/delivery and any delay are separate evidence.
