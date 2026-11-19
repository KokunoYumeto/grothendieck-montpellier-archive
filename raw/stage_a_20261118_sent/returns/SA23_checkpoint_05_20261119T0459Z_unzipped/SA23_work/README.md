# SA23 dossier — reading and audit guide

The final assessment is dated 19 November 2026. Start with `SA23_dossier.md`. The canonical registers are at the top level; the `parts/` directories preserve the individually authored topic records, source-reading ledgers, mathematical arguments, search logs, programs and outputs from which the integration was made.

## Required deliverables

| File | Contents |
|---|---|
| `SA23_dossier.md` | English overview, separate topic narratives, final counts and qualifications. |
| `SA23_entries.tsv` | Exactly one source-based verdict for each of the 326 indexed note entries. |
| `SA23_items.json` | Consolidated subjects and all indexed source-entry IDs; additional direct-source subjects have empty `sources` arrays. |
| `SA23_claims.json` | Precise claims, literal source statements, page status, computations, searched fates, dates and confidence. |
| `SA23_problems.json` | Consecutively numbered questions, occurrences, supported and plausible formulations, state of the art and individual recommendations. |
| `SA23_readings.tsv` | Mathematical alarms for a later scan-reading run. No transcription has been emended. |
| `SA23_links.tsv` | Archive and publication comparisons, plus explicitly labelled earlier-project leads. |
| `SA23_directions.md` | Ranked follow-up tasks with source IDs and concrete first steps; none developed here. |
| `SA23_references.bib` | Checked reference records, with `verified` or `unverified` and exact reading scopes. |
| `CHECK_EVENTS.tsv` | Individually typed check events, distinguishing reading, proof checks, independent arguments, computation and background use. |
| `progress.log` | UTC start, stages, scheduled checkpoints and completion. |

## Additional audit files

`SA23_source_coverage.tsv` and `outputs/source_coverage.json` identify all supplied files by route and hash. `SA23_fate_coverage.tsv` links every final claim to actual recorded search-log rows. `SA23_project_leads.tsv` isolates the other-project leads. `SA23_document_records.json` holds nonmathematical documentary records excluded from the claim count. `SA23_editorial_tasks.json` separates translator requests and present-run repairs from the authorial problem index. `SA23_directions.json` is the machine-readable ranking; `SA23_editorial_directions.md` and its JSON companion preserve follow-ups whose provenance is entirely editorial, outside that ranking. `SA23_id_aliases.json` maps former identifiers to final ones; original witnesses are preserved in merged records. `outputs/final_validation.json` and `FINAL_MANIFEST.json` provide structural and package checks.

The parts are named for ownership, not for an additional historical classification:

| Directory | Source topics |
|---|---|
| `parts/analysis_curves/` | Cotes1 and21. |
| `parts/root/` | Cote2. |
| `parts/ega/` | Cotes22,23 and26. |
| `parts/forms/` | Cotes24 and162-5, with the Tapis and attached Quillen texts. |
| `parts/hyperplanes/` | Cote25. |
| `parts/groupes/` | Cotes161-1 and161-2. |
| `parts/spaces/` | Cotes161-3 and161-4. |
| `parts/bt/` | Supplied cote93 leaves and cote161-5. |
| `parts/misc/` | Supplied cote68 leaves and cote161-6. |

## Reproduction and limits

The ZIP deliberately omits the original attachments, extracted input transcriptions, full third-party publications, raw search-result caches and earlier checkpoint archives. Their routes and the concise evidence needed to assess the conclusions are retained. The original attachments are needed for a new source-reading run. Place their extracted contents under a sibling `sources/notes/` and `sources/texts/` directory, as indicated by the coverage table. The original working directory was a parent containing `SA23_work/` and `sources/`; the archive retains `SA23_work/` as its top-level working tree.

The checked computations and their saved outputs are under their owning parts. Python programs use the standard library and, where imported explicitly, SymPy, NumPy or mpmath. The source-fetch and PDF-inspection utilities document the work already performed; rerunning them requires the relevant network access and PDF utilities. Saved mathematical outputs do not depend on reopening an external site. The source-reading and integration programs do not generate mathematical verdicts from headings or keywords.

To rebuild the final assembly from the preserved assessed records, run `python3 SA23_work/programs/make_consolidation_plan.py`, then `python3 SA23_work/programs/build_final_bibliography.py`, `python3 SA23_work/programs/finalize_dossier.py`, `python3 SA23_work/programs/build_fate_coverage.py` and `python3 SA23_work/programs/validate_final.py` from the parent containing `sources/` and `SA23_work/`. Do not use the earlier `aggregate_current.py` for the final assembly: it was the scheduled-checkpoint collector. `integration/consolidation_plan.json` contains the explicit source-based merge decisions. The final assembly preserves those decisions; it supplies no new literature verdict or research conclusion.

No manuscript images were available. Cotes162-1 and162-6 are catalogue-only entries in these attachments, and the cote1 Pro-page count in TOPIC has no supplied matching Pro file. These boundaries are stated in the dossier. A verified bibliography link is not a claim to have read an entire book; its annotation and reference-check records specify what was actually inspected. Missing first-circulation dates and inaccessible originals remain missing rather than inferred.
