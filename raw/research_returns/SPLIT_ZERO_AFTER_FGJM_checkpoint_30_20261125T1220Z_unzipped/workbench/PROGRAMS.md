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
