# SA09 — Complete dossier and evidence package

Begin with `SA09_dossier.md`. The five principal data registers are `SA09_entries.tsv`, `SA09_items.json`, `SA09_claims.json`, `SA09_problems.json` and `SA09_readings.tsv`. `SA09_directions.md` provides twelve separately ranked subsequent tasks; none of those tasks is represented as completed research here.

## Navigation and provenance

`SA09_links.tsv` contains correspondences checked at both endpoints. `SA09_project_links.tsv` extracts its checked project correspondences into their own table. Their verification is textual and does not certify the mathematical proofs in an external research return. `SA09_project_leads.tsv` preserves the historical inventory of reported project leads, including explicit updated statuses for selected endpoints retrieved during this run. Unlocated endpoints are not counted as verified links.

`SA09_id_aliases.tsv` resolves the six item merges, one duplicate claim and bibliographic aliases. Original component identifiers remain in `workers/` as provenance; the top-level JSON and TSV files are canonical. The 380 source entries are exactly those in the supplied index. An additional unindexed cote137 packet was read and contributes claims and problems without creating extra verdict rows.

`SA09_claim_search_coverage.tsv` maps every canonical claim to the actual component search records. The component bibliographies and `reference_provenance.json` preserve distinct reading scopes when a work occurs in several packets. A bibliography `verified` flag means the stated source was opened; its annotation and `CHECK_EVENTS.tsv` distinguish metadata, theorem inspection, proof checks and computation. The check events do not claim that a source comparison is a proof.

The mathematical arguments are in:

- `workers/cote137/proof_audit.md`;
- `workers/cote138_early/synthesis.md`, its claim records and computation outputs;
- `workers/cote138_middle/proof_audit.md`;
- `workers/cote138_late/proofs.md`.

Independent reviews are retained in `qa_middle.md`, `late_independent_qa.md` and `qa_assembly.md` under their respective worker directories. They include the corrections and the limits of each check.

`claim_status_groups.tsv` is counts-only metadata. It retains the original qualified status for each claim and explains the reporting group used in the overview. `VALIDATION.json` records structural and provenance checks, not automated semantic judgments. `source_manifest.tsv` supplies initial SHA-256 values for the source files and the final validator compares them unchanged.

## Reproduction

The archive excludes the attached inputs, full downloaded reference texts and external project archives. Use the original supplied archive as the source authority. To reproduce the local checks, place the contents of this dossier in a directory named `SA09_work` and the already unpacked attachment contents in its sibling directory `source`. Do not recursively unpack the folders named after the original internal ZIPs: those are already directories in the supplied archive.

The exact mathematical programs are:

- `workers/cote137/programs/recompute.py`;
- `workers/cote138_early/programs/computations.py`;
- `workers/cote138_middle/programs/compute_middle.py`;
- `workers/cote138_late/programs/exact_arithmetic.py`;
- `workers/cote138_late/programs/finite_maps.py`;
- `workers/cote138_late/programs/catalogue_checks.py`.

Their saved outputs specify the finite ranges and exact symbolic results. They use Python and, where recorded, SymPy. General proofs are given separately; a finite test range never substitutes for a universal proof. The late worker's `README.md` gives its detailed execution order. The early worker's `outputs/run_all.json` records its reproduction run.

With the authored component ledgers present, the canonical assembly order is:

```bash
python3 SA09_work/programs/build_claim_status_groups.py
python3 SA09_work/programs/consolidate.py
python3 SA09_work/programs/write_count_tables.py
python3 SA09_work/programs/validate_dossier.py
```

These commands assemble and audit existing semantic decisions. They do not recreate a source review by matching headings or keywords. Individual `build_*.py` scripts preserve the manually authored decisions and search assignments. `final_editorial_pass.py` documents a historical editorial mutation and need not be rerun against its already edited output.

The retrieval helpers and selected-extraction programs are included to document the acquisition process. Their external files, credentials or signed download links are not required for the local mathematical computations. Expired signed links are not durable access guarantees. External project code and restoration instructions were not executed. The final package is a research dossier, not a modified edition of the transcriptions.

`ARCHIVE_MANIFEST.json`, written by the packaging program, lists every packaged file and its SHA-256. Checkpoint archives are immutable, separately named and not nested inside this archive.
