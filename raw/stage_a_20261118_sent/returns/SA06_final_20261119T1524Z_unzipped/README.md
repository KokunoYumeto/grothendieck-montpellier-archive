# SA06 — dossier contents and reproduction

The top-level `SA06_*` files are the final consolidated deliverables. The dossier is in English. Assessment date: **19 November 2026**. The archive contains no manuscript scans, and no diplomatic transcription was changed.

## Reading order

1. `SA06_dossier.md` gives the source sequence, mathematical findings, corrections to earlier notes, modern status, scope of the external comparisons and final counts.
2. `SA06_entries.tsv` accounts for all 437 stable NOTES_INDEX entries. `SA06_items.json` is the canonical item catalogue; `SA06_claims.json` is the mathematical claim map; `SA06_problems.json` separates historical questions from their present status.
3. `SA06_readings.tsv` contains the 219 undecided mathematical alarms for the next scan-based run.
4. `SA06_links.tsv` distinguishes archive, publication and earlier-project links. Its evidence fields explicitly distinguish supported connections, rejected leads and unresolved run attribution.
5. `SA06_directions.md` gives24 ranked future tasks with item, claim and problem origins, mathematical interest and realistic bounded outputs. The directions have not been developed here.
6. `SA06_references.bib` and `REFERENCE_AUDIT.json` give bibliography, opened endpoints, exact locators, version/circulation distinctions and verification limits.

`MERGE_MAP.json` retains every retired identifier and its canonical target. A compound claim or problem can have two targets. Every indexed source entry still has exactly one scalar item ID. The earlier-run P¹/operator comparison is one explicitly three-clause item; its tensor-action, weight-shift and Tate-naturality assertions are not conflated.

## Evidence and audit trail

`CHECK_EVENTS.tsv` records what actually happened: source comparisons, targeted proof checks, independent arguments, exact computations, background use and refutations. Opening a theorem statement or publisher contents is not labelled an independent proof. All source items, claims and reference keys have ledger events.

`CLAIM_SEARCH_AUDIT.json` contains the executed claim-search mappings. `CONTEXT_SEARCH_AUDIT.json` preserves the contextual item and bibliographic searches separately. Shared source/query families are visible. `audit/web_query_locator_audit.json` records the executed web requests, source IDs and URLs while excluding full retrieved publications and browser-response caches.

The `parts/` directory preserves the four individually authored portions and their local proof supplements, original tables, source audits, search/open logs, exact programs and outputs. These are provenance, not a second competing set of final counts. Some early audit files describe an intermediate stage; the final top-level tables, final validation and alias map supersede those intermediate counts.

Important proof supplements include:

- `parts/cote 14_early/proof_checks.md` and `computations.py`;
- `parts/cote 14_late/computation_notes.md` and `code/recompute.py`;
- `parts/cote 15_middle/proofs.md`, `code/exact_checks.py`, and the independent C-SA06-827 review;
- `parts/root/proof_checks.md`, `code/root_computations.py` and `parts/root/root_computations_output.json`.

The root proof supplement includes the actual independent-proof events, including those attached to claims that also have a computational certificate. Exact finite calculations are distinguished from general proofs. Mathematical source and literature locators remain in the corresponding claim and reference records.

`parts/cross_merge_recommendations.json`, its scalar-schema addendum and `audit/integration_policy.json` document the read decisions behind the mechanical merge. `parts/reference_merge_review.json` records bibliography identity decisions and their limits. No source-entry verdict or mathematical identity decision was inferred by a keyword-matching program.

The external-context findings are in `audit/project_endpoint_findings.md`, `parts/cote 14_early/context_endpoint_audit.md/json` and the late-cote 14 contextual audit. Full other-project returns were not bundled. Original run labels and source hashes are retained, and reading another return's statement is not represented as repeating all its proofs or computations.

## Programs and environment

All authored Python programs are included. `audit/program_inventory.json` records their hashes and the retained outputs; `audit/runtime_environment.json` records the execution runtime. The principal exact calculations used Python3.12 and SymPy1.14, with exact integers, rational numbers and symbolic matrices. They did not rely on floating-point approximations as certificates.

The source-reading and authoring scripts expect the original attached archive unpacked once under `source/` beside the `SA06_work` working directory. Its inner directories are already unpacked in that archive. The attachment is intentionally not duplicated in this deliverable. External published sources and other-project endpoint files are identified in the fetch/read manifests. Some historical source-reading commands retain the original absolute scratch path as execution provenance; those paths need relocation if the work is reproduced elsewhere.

The exact mathematical programs can be inspected independently of rebuilding the ledgers. Their saved outputs are already present. To rebuild the merged tables from the four preserved part tables, place this archive's contents in a directory called `SA06_work`, create `SA06_work/output/`, and copy the top-level generated files into that directory as the assembly inputs. Run, in order:

```bash
python SA06_work/code/author_integration_policy.py
python SA06_work/code/integrate_sa06.py
python SA06_work/code/assemble_dossier.py
python SA06_work/code/validate_final.py
```

The authoring scripts serialize the manually reviewed decisions and prose. They do not repeat source reading or independently re-establish the theorems. The validator checks exact entry coverage, schemas, aliases, preserved source quotations and relationships, search/event coverage, link retention, reference keys and recursive certificate paths. Its strict final report is `audit/final_validation.md/json`.

`progress.log` gives UTC milestones and checkpoint times. Checkpoints were separately saved at the requested45-minute intervals and are not nested in the final archive. `audit/archive_contents.tsv` gives the final included-file hashes, and `audit/final_archive_policy.json` records the excluded source-cache categories. The final ZIP's integrity was tested after packaging.
