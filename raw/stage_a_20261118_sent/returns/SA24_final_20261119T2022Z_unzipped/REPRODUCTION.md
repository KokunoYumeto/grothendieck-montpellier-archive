# SA24 code inventory and reproduction guide

## What can be reproduced

The package preserves the authored programs, their saved outputs and the records on which consolidation was based. The exact algebraic examples and structural checks can be rerun. A program replay does not reproduce the act of reading a manuscript passage or evaluating whether a later theorem has the same hypotheses. Those decisions are documented in the source selections, proof reports, search outcomes and audit records.

Use a separate replay copy if rerunning writers. The delivered top-level registers remain the reference output. Do not execute every script in alphabetical order: several scripts are historical editorial operations, and the initial serializers can overwrite later supplements.

## Input layout

Most programs resolve paths from the location of their own file. Recreate the following layout under a chosen replay directory:

| Relative path | Required contents |
|---|---|
| `SA24_work/` | Extracted contents of this deliverable, including `code/`, `agents/`, `outputs/` and `evidence/`. Keep this directory name for scripts that explicitly construct it. |
| `source/SA24_notes/` | Extract the original notes attachment here, retaining `NOTES_INDEX.tsv`, `pro/` and `codex/`. |
| `source/SA24_texts/` | Extract the original texts attachment here, retaining `TOPIC.md`, `PREAMBLE.tex`, `pro/` and `codex/`. |
| `public_sources/` | Optional separately downloaded primary PDFs and extracted text; not supplied in this ZIP. |
| `public_sources/notes_late_reading/` | Optional external reading/OCR cache needed by the historical late search finalizer and OCR program. |
| `research_cache/` and `core_research_cache/` | Original full retrieval caches used by historical manifest/audit operations; not supplied in this ZIP. |

The source files must match `evidence/source_manifest.json` to reproduce physical-line coordinates and hash checks. The original attachments are not bundled. No image scans or second-pass files were available in the source packet.

`build_middle_stage1.py` retains the original absolute `BASE` path. Adjust that constant only in the replay copy before using that historical serializer. Other historical scripts may rely on fixed working counts or cache names; consult their inventory notes below.

## Dependencies and recorded environment

The calculation run used **Python 3.12.14** and **SymPy 1.14.0**. The four mathematical certificate scripts require SymPy; the other Python programs use the standard library. Optional PDF extraction used **Poppler pdftotext 25.03.0**; the Breen OCR helper used **Tesseract 5.5.0**. Those tools and their primary PDFs/images are needed only for extraction/OCR replay, not for reading the final registers. The downloader additionally requires network access to the public URL given to it.

In the desired Python environment, install the recorded mathematical dependency if needed:

```bash
python -m pip install sympy==1.14.0
```

No Lean proof or Lean build was run. The references to a 2026 formalization record the published scope and do not constitute a reproducible formal certificate supplied here.

## Rerun the exact calculations

From the replay `SA24_work/` directory, with the source layout above:

```bash
python code/core_computations.py
python code/middle_computations.py
python code/late_checks.py
python code/root_computations.py
```

These rewrite their corresponding JSON outputs. `core_computations.py` additionally reads the pro source for its census. Compare the mathematical data rather than timestamps or captured standard-output formatting.

| Certificate | Scope of the result |
|---|---|
| `core_computations.json` | Exact sign and elementary-chain examples, a contraction and a specific counterexample. The source census is metadata. |
| `middle_computations.json` | Symbolic quadratic/binomial identities and specified cycle/disk/counit examples. Finite checks do not supply an unrestricted theorem. |
| `late_checks.json` | Exact rank matrices, DGA identities for the typed interval counterexample, endpoint failure and explicit dual/Ext examples. General tensorwise and local-rank arguments are in the proof report. |
| `root_computations.json` | Universal free-abelian boundary identities are distinguished from finite cohomology examples; the categorical counterexamples are checked in the accompanying prose. |

## Rerun structural checks and inspect source selections

```bash
python code/validate_final.py
python code/audit_final_bibliography.py
python code/late_root_audit.py
```

The final validator checks all supplied source hashes as well as register integrity. The bibliography checker checks syntax and references without opening the internet. The root audit checker examines the retained working root records. A successful structural check is not a proof certificate.

For a fresh numbered source selection, for example:

```bash
python code/read_source.py --file SA24_texts/pro/MPL_134-8_043-087_transcription.tex --scans 77 --tag replay
python code/read_source.py --notes 341 345 --tag replay
```

This writes new timestamped reading outputs and appends to the replay reading log. It does not decide the mathematical verdict.

## Rebuilding registers and documentation

`consolidate.py` serializes the final records from the four readers' tables, explicit merge proposals and manually stated status decisions. It writes the main registers, ID maps, counts and bibliography. It does not infer verdicts from text matches. In a replay copy, run `apply_review_fixes.py` afterwards to apply the eight guarded canonical wording changes, then `write_narrative.py` and `build_supporting_guides.py` for the narrative/support files, and finally `validate_final.py`. A historical serializer must not be mistaken for a live re-research pipeline.

`build_supporting_guides.py` updates only the README, this guide, the explicit refinement registry, the code inventory and its validation output. It reads the current consolidated counts and ID map and checks that every Python program has an inventory entry. It does not change claims, problems, verdicts or the bibliography.

The original web searches were performed through the research tools. No replay script promises to reproduce ranked search results or private external-project context. Query/open records and their assessed outcomes are the evidence retained here. Where exact original query strings were unavailable, the logs say so. Full external text remains outside the package.

## Complete authored-program inventory

The machine-readable version is `evidence/code_inventory.json`, with each program's SHA-256, imports, inputs, saved outputs and execution note. A captured stdout file is distinguished from a file written directly by the program. Output paths are relative to `SA24_work/` unless described as a sibling path. A program with no dedicated saved stdout file is identified as such; no output is claimed to exist merely from its filename.

### Mathematical certificates

| Program | Purpose and inputs | Saved output / execution note |
|---|---|---|
| `core_computations.py` | Endpoint signs, bicomplex signs, strict-versus-derived comparison, contraction and a finite global-asphericity counterexample. Inputs: Explicit examples in code; pro transcription for source census. | outputs/core_computations.json; outputs/core_computations_stdout.txt. Dependencies: Python + SymPy. |
| `middle_computations.py` | Cycles/disk checks, quadratic and binomial formula checks, and underived-counit counterexample. Inputs: Explicit symbolic and finite examples in code. | outputs/middle_computations.json; outputs/middle_computations_stdout.txt. Dependencies: Python + SymPy. |
| `late_checks.py` | Rank/evaluation matrices, typed DGA interval, dual counterexample, endpoint matrix and Ext1 examples. Inputs: Explicit examples in code; hypotheses and general arguments in late_proof_checks.md. | outputs/late_checks.json. Dependencies: Python + SymPy. |
| `root_computations.py` | Sính boundary identities, finite cohomology, Kan pushout and categorical counterexamples, signs and globular cell counts. Inputs: Explicit symbolic and finite examples in code. | outputs/root_computations.json; outputs/root_computations_stdout.json. Dependencies: Python + SymPy. |

### Source and literature evidence

| Program | Purpose and inputs | Saved output / execution note |
|---|---|---|
| `read_source.py` | Print physically numbered source selections and record what was selected. Inputs: source/SA24_notes/pro/..._notes.md for --notes A B; source/<relative-file> for --file, with --lines A B or --scans N ... . | outputs/<UTC timestamp>_<tag>.txt; appended evidence/read_log.jsonl. Dependencies: Python standard library. Selection is mechanical; the log does not itself prove a mathematical claim or make a note verdict. |
| `inspect_calendar.py` | Inventory the vector calendar on K135-03 scan 37 without treating path geometry as mathematical prose. Inputs: source/SA24_texts/codex/K135-03_transcription.tex. | outputs/calendar_structure.json; captured outputs/calendar_inspection.txt; appended progress.log. Dependencies: Python standard library. |
| `download_public.py` | Download an already identified public source and log success or failure. Inputs: Command arguments: URL and local basename. | Sibling public_sources/<basename> (outside this package); appended evidence/download_log.jsonl. Dependencies: Python standard library. Requires network access to the given source. Public-source PDFs are not bundled here. |
| `extract_public_pdf.py` | Run pdftotext -layout on a downloaded primary PDF. Inputs: Command argument: basename under sibling public_sources/. | Sibling public_sources/<stem>.txt (outside this package); evidence/download_log.jsonl and progress.log. Dependencies: Python standard library + Poppler pdftotext. |
| `late_ocr_breen.py` | OCR the 30 rendered pages of the Breen1969 article with printed-page markers. Inputs: Sibling public_sources/notes_late_reading/late_breen69-*.png; exactly 30 images. | Sibling public_sources/notes_late_reading/late_Breen1969_ocr.json and .txt; provenance in evidence/late_primary_reading_files.json. Dependencies: Python standard library + Tesseract. The rendered images and full OCR remain outside the deliverable; OCR is a reading aid, not an ink adjudication. |

### Working-record serializers

| Program | Purpose and inputs | Saved output / execution note |
|---|---|---|
| `core_build_items.py` | Serialize the manually read core item judgments. Inputs: Pro transcription and manually encoded decisions. | agents/core_items.json; agents/core_entries.tsv; outputs/core_items_validation.json. Dependencies: Python standard library. Overwrites working records; archival reproduction only after subsequent edits are reconciled. |
| `core_build_claims.py` | Serialize core claims and problems. Inputs: Pro transcription and manually authored mathematical records. | agents/core_claims.json; agents/core_problems.json; outputs/core_claims_validation.json. Dependencies: Python standard library. Overwrites working records; does not perform new research. |
| `core_support.py` | Serialize core reading alarms, links, search scopes and events. Inputs: Core items/claims/references and original notes/index; authored outcomes in code. | agents/core_readings.tsv; core_links.tsv; core_search_log.tsv; core_CHECK_EVENTS.tsv; outputs/core_support_summary.json; progress.log. Dependencies: Python standard library. Overwrites these working tables. |
| `build_middle_stage1.py` | Serialize the 170 individually assessed middle note entries and items. Inputs: Pro notes, transcription, NOTES_INDEX.tsv and manually authored decisions. | agents/middle_entries.tsv; middle_items.json; middle_links.tsv; middle_CHECK_EVENTS.tsv; middle_stage1_status.json. Dependencies: Python standard library. Contains the original absolute workspace path; change BASE in a replay copy. Overwrites working records. |
| `build_middle_results.py` | Serialize the manually assessed middle claims. Inputs: Mathematical records and physical source anchors authored in code. | agents/middle_claims.json. Dependencies: Python standard library. Overwrites working claims. |
| `build_middle_support.py` | Serialize middle problems and reading alarms. Inputs: Manually authored problems, references and source ranges in code. | agents/middle_problems.json; agents/middle_readings.tsv. Dependencies: Python standard library. |
| `build_middle_audit.py` | Build middle search/event/link evidence from saved retrievals and manual outcomes. Inputs: agents/middle_claims.json, existing middle event/link tables, evidence/middle_web_manifest.json, sibling research_cache/middle_web01–39.json, and manually authored outcome assignments. | agents/middle_search_log.tsv; middle_CHECK_EVENTS.tsv; middle_links.tsv; evidence/middle_web_manifest.json. Dependencies: Python standard library. Some input caches are deliberately outside the package. Preserves known limits of the earliest query records; it cannot reconstruct missing exact original query strings. |
| `build_late_stage1.py` | Serialize individually read late decisions and anchors. Inputs: code/late_decisions.tsv; original pro notes/transcription. | agents/late_entries.tsv; late_items.json; late_links.tsv; late_CHECK_EVENTS.tsv; outputs/late_stage1_counts.json. Dependencies: Python standard library. Do not run as a final refresh: it overwrites later event/link supplements; it is the initial serialization stage. |
| `build_late_claims.py` | Serialize late claims, problems and reading alarms. Inputs: Manually authored definitions, judgments and proof pointers in code. | agents/late_claims.json; late_problems.json; late_readings.tsv. Dependencies: Python standard library. |
| `late_finalize.py` | Serialize final late events, bibliography uses, searched-fate coverage and checked links. Inputs: Late working records and sibling public_sources/notes_late_reading/late_web_records.json. | agents/late_CHECK_EVENTS.tsv; late_search_log.tsv; late_links.tsv; outputs/late_final_counts.json. Dependencies: Python standard library. Needs the outside retrieval cache; does not regenerate the manually authored bibliography or reports. |
| `build_root_claims.py` | Serialize root mathematical records and source-to-scan anchors. Inputs: Original Codex transcriptions; manually authored claim/problem/reading/link/event records. | agents/root_claims.json; root_problems.json; root_readings.tsv; root_links.tsv; root_CHECK_EVENTS.tsv; root_claim_search_map.tsv; outputs/root_build_output.json; progress.log. Dependencies: Python standard library. |
| `build_root_references.py` | Serialize the manually checked root bibliography and verification scope. Inputs: Manually authored reference and access-scope records. | agents/root_references.bib; evidence/root_reference_verification.json; captured outputs/root_references_output.json. Dependencies: Python standard library. Verified refers to the specified access/result scope, not an independent proof audit. |
| `root_extra_events.py` | Serialize supplementary reference-use, proof and counterexample events. Inputs: evidence/root_reference_verification.json and authored extra event definitions. | agents/root_extra_CHECK_EVENTS.tsv; outputs/root_extra_events_output.json. Dependencies: Python standard library. |

### Consolidation and validation

| Program | Purpose and inputs | Saved output / execution note |
|---|---|---|
| `consolidate.py` | Apply explicit semantic merge/status decisions, assign final IDs, and serialize consolidated registers. Inputs: All agent registers/bibliographies/search logs; agents/cross_merge_proposals.json; manual decisions in code. | SA24_entries.tsv, SA24_items.json, SA24_claims.json, SA24_problems.json, SA24_readings.tsv, SA24_links.tsv, SA24_project_leads.tsv, SA24_references.bib, CHECK_EVENTS.tsv, SA24_search_log.tsv, SA24_claim_search_map.tsv, SA24_id_map.tsv; evidence/final_merge_decisions.json, primary_status_decisions.json, bibliography_records.json, working_to_final_ids.json; outputs/consolidation_counts.json; captured outputs/consolidate_stdout.json; progress.log. Dependencies: Python standard library. Mutates the main registers. Use only in a separate replay copy with all final editorial decisions reconciled; it does not redo source reading or literature assessment. |
| `validate_final.py` | Check final coverage, source hashes, schemas and referential/event/search integrity. Inputs: Consolidated registers, expected documentation and original source/ files. | outputs/final_validation.json; captured outputs/validate_final_stdout.json. Dependencies: Python standard library. Structural validation; cannot certify mathematical correctness or adjudicate readings. |
| `audit_final_bibliography.py` | Check BibTeX balance/fields, unique keys, and reference coverage. Inputs: SA24_references.bib; final claims and problems. | agents/final_bibliography_audit.json. Dependencies: Python standard library. No network access; successful syntax/key checks do not mean a source was opened anew. |
| `inspect_integration.py` | Inspect working schemas, statuses and merge data. Inputs: Four agent tables and supporting TSV files. | Standard output captured as outputs/integration_review.txt. Dependencies: Python standard library. |
| `late_root_audit.py` | Check root schemas, scan membership, problem links and bibliography-key resolution. Inputs: Root working claims/problems/proof report/readings; original transcriptions; all agent bibliographies. | outputs/late_root_audit_validation.json. Dependencies: Python standard library. Source-support judgments are separate in agents/root_independent_audit.md. |
| `core_merge_audit_view.py` | Print cross-agent claim records for manual semantic merge review. Inputs: Four agent claim tables. | outputs/core_claim_merge_audit_view.txt. Dependencies: Python standard library. |
| `core_problem_merge_audit_view.py` | Print selected owners’ problem records for manual merge review. Inputs: Agent problem tables; optional command arguments selecting owners. | outputs/core_problem_merge_audit_view.txt and recorded _middle_late.txt / _root.txt views. Dependencies: Python standard library. |
| `core_root_locator_audit.py` | Mechanically compare declared scans with physical source ranges. Inputs: agents/root_claims.json; cited source files; optional lower/upper claim numbers. | outputs/core_root_locator_audit_1_13.json in the recorded run. Dependencies: Python standard library. No semantic mathematical verdict is inferred. |
| `core_review_final_consolidation.py` | Review final merge structure, references and selectable record views. Inputs: Final registers/ID map; agent tables; cross_merge_proposals.json. Modes include checks, items lo hi, claims, problems, links, remaining, review_summary. | outputs/core_final_merge_structure.json; outputs/core_final_problem_reference_check.json in checks mode; selected views on standard output. Dependencies: Python standard library. |
| `core_narrative_review_view.py` | Show the canonical records cited by selected final narrative sections and compare register counts. Inputs: SA24_dossier.md, SA24_directions.md, final items/claims/problems and count/reference/event/search registers; modes ids, counts, or selected final IDs. | Standard output evidence view; the program does not write a separate output file. Dependencies: Python standard library. Supports manual narrative review; it does not decide mathematical fidelity or change the registers. The manual result is summarized separately in agents/narrative_core_review.md. |
| `core_report_format_audit.py` | Inspect the core report’s formatting. Inputs: agents/core_report.md. | Standard output only; no dedicated saved-output file was produced. Dependencies: Python standard library. |
| `validate_middle.py` | Check middle coverage/reference/search/event integrity and normalize escaped backticks in three reports. Inputs: Middle tables, bibliography, directions/proof/report files. | agents/middle_validation.json; normalized middle_directions.md, middle_proof_checks.md, middle_report.md. Dependencies: Python standard library. Not read-only: it rewrites those three Markdown files and assumes this run’s fixed working counts. |
| `apply_review_fixes.py` | Apply the eight independently reviewed canonical wording changes, guarded by complete old/new values. Inputs: agents/final_consolidation_fixes.json and its named final JSON/TSV registers. | Updated named final registers; outputs/review_fixes_output.json; captured outputs/apply_review_fixes_stdout.json; progress.log. Dependencies: Python standard library. Run after consolidate.py in a replay copy. Already-applied exact new values are accepted; an unexpected value stops the program. Reader variants and source transcriptions remain unchanged. |

### Historical editorial operations

| Program | Purpose and inputs | Saved output / execution note |
|---|---|---|
| `core_write_merge_proposals.py` | Serialize the completed manually adjudicated merge proposals. Inputs: Agent items/claims/problems and authored merge decisions. | agents/cross_merge_proposals.json. Dependencies: Python standard library. Overwrites proposal history; not a live automatic merge detector. |
| `core_write_final_consolidation_review.py` | Serialize the completed manual consolidation review and guarded old/new fix proposals. Inputs: Final records/ID map, cross_merge_proposals.json and the final problem-reference check. | agents/final_consolidation_review.md; agents/final_consolidation_fixes.json. Dependencies: Python standard library. Historical snapshot, not a live validator. Does not modify final registers. |
| `core_repair_report_format.py` | Perform the recorded one-time formatting repair. Inputs: agents/core_report.md. | Rewritten agents/core_report.md; outputs/core_report_format_repair.json. Dependencies: Python standard library. Do not rerun as a general formatter: the parenthesis heuristic was specific to that earlier report snapshot. |
| `core_cache_manifest.py` | Move full external core retrievals outside the deliverable and write their manifest. Inputs: Historical evidence/core_web_*.json retrieval files. | Sibling core_research_cache/ files; evidence/core_web_manifest.json. Dependencies: Python standard library. Do not rerun unmodified: its historical glob can include its own manifest on a later run. Full external retrievals are not bundled. |
| `sync_middle_builders.py` | Synchronize two authored-data builders with reviewed middle records. Inputs: agents/middle_claims.json and middle_items.json; the existing builders. | Rewritten code/build_middle_results.py and build_middle_stage1.py; outputs/middle_builder_sync.json. Dependencies: Python standard library. Mutates code; retained as an exact record of a one-time synchronization, not a routine verification step. |

### Packaging

| Program | Purpose and inputs | Saved output / execution note |
|---|---|---|
| `package_checkpoint.py` | Create an immutable complete checkpoint and move selected external-text caches out of the deliverable. Inputs: --timestamp and --number; current SA24_work/; historical external-cache files. | Sibling SA24_checkpoint_NN.zip; outputs/checkpoint_NN_manifest.json; evidence/web_root_manifest.json and middle_web_manifest.json; progress.log. Dependencies: Python standard library. Refuses to overwrite a checkpoint. Does not upload the archive. The saved checkpoint_01_receipt.json records the separate upload; checkpoint archives and original attachments are not nested in the final package. |
| `package_final.py` | Create the final deliverable archive and a file manifest. Inputs: The completed SA24_work/ files and successful final validation. | Sibling SA24.zip; outputs/final_package_manifest.json; outputs/package_final_stdout.json; appended progress.log; upload receipt stored outside the final ZIP. Dependencies: Python standard library. Writes the two packaging metadata files before zipping and checks member CRCs after writing. Original attachments and external full-text caches are outside the input tree; ZIP/bytecode files and symlinks are excluded. |

### Supporting documentation

| Program | Purpose and inputs | Saved output / execution note |
|---|---|---|
| `build_supporting_guides.py` | Build this README, reproduction guide, refinement definitions and code inventory from current IDs/counts plus authored explanations. Inputs: outputs/consolidation_counts.json; evidence/working_to_final_ids.json; final claims/references; code/*.py; definitions in this script. | README.md; REPRODUCTION.md; SA24_refinements.json; evidence/code_inventory.json; outputs/supporting_guides_validation.json; captured outputs/supporting_guides_stdout.json. Dependencies: Python standard library. Does not modify the main registers. Fails if a new Python program has not yet been documented. |
| `write_narrative.py` | Serialize the manually authored dossier and 12 ranked future tasks, inserting current final IDs and counts. Inputs: evidence/working_to_final_ids.json; outputs/consolidation_counts.json; authored prose in code. | SA24_dossier.md; SA24_directions.md; outputs/narrative_counts.json; captured outputs/write_narrative_stdout.json; progress.log. Dependencies: Python standard library. Does not automatically develop a direction or infer a mathematical verdict. |

## Additional inputs and archival outputs

`code/late_decisions.tsv` is a manually authored decision ledger, and `code/root_search_requests.json` is a request record; neither is executable code. The directories also retain some one-time validation snapshots, manual audit proposals and captured reading selections not generated by a dedicated named script. Their role is provenance, not an undocumented second mathematical pipeline.

Full downloaded third-party papers, full OCR and raw external retrieval caches are not distributed. The helper programs document their acquisition/extraction and retain status logs and manifests. Previously created checkpoint archives are likewise not nested here; the checkpoint manifest/receipt records the historical checkpoint operation separately from this final package.
