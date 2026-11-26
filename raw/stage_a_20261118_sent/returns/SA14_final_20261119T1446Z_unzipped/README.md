# SA14 — archive guide and reproduction

The top-level dossier and registers are the final consolidated deliverables. The
`parts/` directories preserve the individually researched source judgments,
proofs and retrieval evidence. Their historical counts and IDs may differ from
the final registers because cross-package merging and publication-authorship
corrections happened later. `research/consolidation_aliases.json` records the
explicit semantic joins. Preserved `source_variants` are historical witnesses,
not extra primary items or stale outward pointers.

## Main files

- `SA14_dossier.md`: English synthesis following the programme on57:66, with final counts.
- `SA14_entries.tsv`: exactly440 independently read verdicts.
- `SA14_items.json`, `SA14_claims.json`, `SA14_problems.json`: the final canonical registers.
- `SA14_readings.tsv`: mathematical alarms; no manuscript scan decision has been made.
- `SA14_links.tsv`: all three required link kinds, with unavailable project endpoints labelled.
- `SA14_project_leads.tsv` and `SA14_checked_links.tsv`: the quarantined and checked rows separately.
- `SA14_directions.md`:18 ranked follow-up tasks, not developed here.
- `SA14_references.bib`: opened links or explicit unverified labels, with scope in `annote`.
- `CHECK_EVENTS.tsv` and `progress.log`: statement-level checks and UTC stages/checkpoints.

## Locators and evidence

Scan numbers are the supplied `\scanpage` labels. Lines are one-based physical
lines of the named `.tex` files. `research/source_manifest.json` and
`research/source_coverage.tsv` identify every supplied transcription and its hash.
The complete source inputs are not repackaged here; use the original attached ZIP.
No source transcription was edited. A source-only item may cite a transcript
rather than an indexed note. SA14-446 deliberately has no manuscript locus:
it is an earlier-run comparison explicitly judged not on the page.

Claims' `search_events` point to the corresponding part's `search_log.tsv`;
root `searches` point to saved web receipts and `research/root_search_map.md`.
Discovery hits, failed fetches and later quotations are not confused with an
opened exact theorem. Some URL receipts preserve a short summary/hash instead
of an entire external book. Full downloaded external PDFs are excluded.

## Calculations and mathematical checks

- Root: `research/root_proofs.md`, `scripts/root_computations.py`,
  `outputs/root_computations.json`.
- Early Picard: `parts/picard_early/computations.md`,
  `scripts/recheck_calculations.py` and `outputs/calculations.json` in that part.
- Late Picard/Lefschetz: `parts/picard_lefschetz/outputs/proof_checks.md`,
  `scripts/calculations.py` and `outputs/calculations.json` in that part.
- Cote60: `parts/lfunctions/proof_notes.md`, `scripts/calculations.py` and
  `outputs/calculations.txt` in that part.

Finite examples and symbolic identities certify the stated calculations under
their assumptions. General arguments are written separately. Structural
validation is not a certificate of every theorem. Independent cross-reviews
record both their inspected scope and the errors that were corrected.

## Reproducing the final join

Extract this archive into a directory named `SA14_work`. Beside it place the
original input unpacked once into `sources`, so that
`sources/SA14_texts/codex/…` and `sources/SA14_notes/…` exist. Run the following
from their common parent directory. Python3 and SymPy are the calculation
dependencies; the archived outputs do not require rerunning anything to read.

```bash
python3 SA14_work/scripts/root_bibliography.py
python3 SA14_work/scripts/build_root.py
python3 SA14_work/scripts/root_finalize_part.py
python3 SA14_work/scripts/consolidate.py
python3 SA14_work/scripts/build_final_directions.py
python3 SA14_work/scripts/finalize_documentation.py
python3 SA14_work/parts/picard_early/scripts/audit_crossregister.py
python3 SA14_work/scripts/validate_final.py
```

The part tables already contain their final reviewed corrections. Do not run
one early builder alone and treat its intermediate output as the final state.
The part READMEs explain their build order. One-time `refine`/patch programs
are retained as evidence of authored changes, not a second pipeline to replay
blindly. `root_records.py` and `root_aux.py` are authored data modules executed
by `build_root.py`; they do not infer judgments from text cues.

`research/program_manifest.tsv` lists every retained program and its hash;
`research/output_manifest.tsv` lists saved small outputs. Reading tools save
their displayed chunks and, where available, actual timestamps. Retrospective
read records are labelled rather than supplied with invented exact times.
Ad hoc directory/metadata inspection is distinguished from mathematical
computation; an inspection-path error was corrected without changing an input
or treating its failed invocation as a mathematical check.

## Checkpoints and provenance

Immutable45-minute checkpoints were made according to the requested schedule.
Their manifests name their predecessors; the earlier ZIPs themselves and the
original attachments are excluded from this final ZIP. `progress.log` records
the actual creation times. Final metadata and file hashes are in
`research/final_package_manifest.json`, with the packaging verification output.
