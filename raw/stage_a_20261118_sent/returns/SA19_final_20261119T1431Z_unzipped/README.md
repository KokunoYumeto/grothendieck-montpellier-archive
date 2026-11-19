# SA19 — Guide to the completed dossier

Begin with **SA19_dossier.md**. The dossier is in English, follows the archive's mathematical sequence, and gives the final counts. **SA19_directions.md** contains 27 ranked tasks for later runs; they have not been developed here.

## Authoritative registers

| File | Purpose |
|---|---|
| `SA19_entries.tsv` | Every one of the 174 indexed source entries, exactly once |
| `SA19_items.json` | 147 consolidated items, with source entries, brief quotations, locators and scope assessments |
| `SA19_claims.json` | 338 claim records; 330 source assertions and eight explicitly separate supplementary reconstructions |
| `SA19_problems.json` | 125 questions, deferred steps and documentary problems, including resolved and refuted formulations |
| `SA19_readings.tsv` | 201 mathematical alarms for image-equipped checking; no ink decision made here |
| `SA19_links.tsv` | Checked folder and publication comparisons |
| `SA19_our_project_leads.tsv` | Separate, explicitly unverified external project targets |
| `SA19_external_pointer_index.tsv` | 160 entry–target pairs preserving all 23 named external pointers |
| `SA19_publication_comparison_leads.tsv` | The original EGA IV₄ passage not recovered in readable form; not counted as a verified two-endpoint link |
| `SA19_references.bib` | Checked bibliography; each URL marked verified or unverified |
| `SA19_bibliography_audit.tsv` | Full-text, theorem, abstract, metadata and unavailable-source distinctions |
| `SA19_research_log.json` | Every claim's search route and exact scope; some common theorem families are recorded together |
| `SA19_refinements.json` | Explicit repairs, independent models and reconstructed specializations |
| `SA19_aliases.tsv` | Cross-package item, claim, problem and bibliographic aliases |
| `SA19_folder_coverage.tsv` | All listed folders, available faces, actual cotes and unavailable-source evidence |
| `CHECK_EVENTS.tsv` | Actual checks, computations, proof reviews, use of references and refutations |
| `progress.log` | UTC stages and checkpoint/finalization history |
| `SA19_counts.json` | Counts calculated from the authoritative registers |

## Source boundaries

K43-02 is listed but absent from the ZIP. Targeted searches for an indexed `P040__K43-02_transcription.tex`, `P040__SPACE_INDEX.tsv` or `K43-02` found no counterpart. This does not establish that no copy exists outside the available index. No absent passage is reconstructed. All 262 supplied transcription faces were read, including covers and reused sheets.

The cote-16 second pass has priority only where it actually applies. The confirmed date 6 January 1966 is retained. There are no manuscript images in the inputs, and no original transcription has been edited.

## Detailed work and computation

The four `workstreams/` directories preserve independent close reading, theorem locators, mathematical proofs, programs, actual outputs and more detailed synthesis. Their item IDs and counts precede the final cross-package merges. Use top-level records for canonical IDs, final classifications and counts; use the workstream files for the full proof and source audit.

- `workstreams/codex43/proofs.md`, `proofs_C16.md`, `hom_ext_cells.tsv`, `exact_checks.py`, `table_checks.py` and their saved outputs cover the Codex mathematics, including all 200 table cells. The peer review found an Ext² term missing from an initial contravariant deduction; the final proof retains it and uses a separately opened dimension theorem.
- `workstreams/pro43/computations.md`, `scripts/calculations.py` and `outputs/calculations.txt` contain the Pro43 checks and countermodels.
- `workstreams/cote16/proof_checks.md`, its calculation scripts and `outputs/exact_checks.txt` contain the integral, projector, discriminant and four-form checks. `RUNNING_THE_CHECKS.md` distinguishes repeatable computation from one-time editorial amendments.
- `workstreams/cotes44_47_54/computations.md`, `code/computations.py` and `outputs/computations.*` contain the Fourier, incidence, flatness and root-system checks. `code/README.md` explains rebuild order.

`SA19_programs.tsv` inventories the saved programs. `outputs/final_validation.json` records schema, source-scan, identifier, reference, search-ledger and check-event coverage. These validations do not generate mathematical verdicts from headings or keywords.

## Reproducing the consolidation

Keep the original supplied ZIP separately. To reproduce in a fresh directory, unpack it once into `source/`, and place this dossier at the sibling `SA19_work/`. Input hashes and the scan/line index are in `source_audit/`. Mathematical programs may require the libraries named in their workstream instructions. Read each workstream's execution guide before running a serializer or one-time amendment: not every historical editing script is a repeatable computation.

The final integration order is `scripts/consolidate.py`, `scripts/editorial_finalize.py`, `scripts/render_summary_counts.py`, `scripts/index_retrieval.py`, then `scripts/validate_final.py`. This assumes the final workstream snapshots already present in this ZIP. Running earlier generators can overwrite later manual corrections; they are preserved for provenance, not offered as an unattended rebuild of the full research process.

Original attachments, their full working copies, downloaded third-party PDFs, raw full-text retrieval responses and raw primary-source OCR are not redistributed. Mathematical code and actual calculation outputs are included. Source-extraction outputs are documented by hashes, exact page locators and access logs instead of reproducing whole third-party articles. This boundary does not remove the curated proofs, theorem comparisons or bibliographic evidence.

`PACKAGE_MANIFEST.json` gives a SHA-256 hash and byte count for every included file. Earlier checkpoints are not copied into the final ZIP. No file in this archive is a replacement for an unavailable scan or external project target.
