# Late cote-138 work packet

Owner: `/root/cote138_late`. Scope: all 127 entries of `MPL_138_090-133`, global ordinals 254–380. The parent owns final cross-package merging, persistence and delivery.

## Final contents

- `entries.tsv`, `items.json`: 127 source verdicts, exactly once, consolidated into 66 items. The semantic judgments were made by reading every complete entry and its transcription passage. The serialization script does not classify headings or generate verdicts.
- `claims.json`, `problems.json`: 82 claims and 24 problem records, IDs MP-SA09-70–93.
- `readings.tsv`: 54 mathematical alarms; no source reading has been changed.
- `links.tsv`: 15 comparisons with both endpoints read. `project_leads.tsv`: 41 reported links with unavailable targets. `verified_project_links.tsv` has its header only.
- `search_log.tsv`: one exact-scope literature-fate record for each of the 82 claims. `search_coverage.md` explains channels, backward searches and access limits.
- `references.bib`: 24 opened-reference records, explicitly distinguishing metadata-only leads from mathematical passages.
- `CHECK_EVENTS.tsv`: 278 events. Textual source comparison is not recorded as proof checking.
- `synthesis.md`, `proofs.md`, `directions.md`: detailed source synthesis, checked arguments and 12 ranked future tasks. `review_response.md` records the precision changes requested by the independent cross-worker check.
- `programs/`, `outputs/`: source and outputs of the exact algebra, permutation enumeration, catalogue comparison and structural audit. Initial failed program outputs are retained with the subsequent successful versions; they are implementation/debugging records, not failed mathematical conclusions.

## Computation reproduction

Python 3.12 and SymPy 1.14 were used. From this packet directory:

```sh
python programs/exact_arithmetic.py
python programs/finite_maps.py
python programs/catalogue_checks.py
```

The arithmetic program uses exact rational polynomial operations. The finite-map program enumerates every connected oriented genus-zero map in the stated folded-edge convention through dartdegree six, and separate test examples. The catalogue program compares 29 manually transcribed passport/group assertions. A diagram-to-permutation assignment is conditional where the scan is unavailable; exact algebra does not authenticate the ink.

The `build_*.py` files serialize manually assessed records. `build_claims_extra.py` is the entry point for all 82 claims; `build_claims.py` is its imported first part. `build_problems.py` follows the claims. `polish.py` applies explicit prose-spacing edits and leaves source quotations, locators, IDs and verdicts unchanged. `build_links.py` and `build_audit.py` follow those files. The working `entries_source.json` cache used by link serialization is extracted source material, not an additional deliverable; the original attached notes remain its authoritative input.

`validate.py` checks schemas, the exact 127-entry partition, minimum-global-ordinal item IDs, cross-reference integrity, all claim searches, check-event coverage, source line bounds and declared scan numbers. It expects the existing workspace layout and original extracted sources at the workspace `source/` directory. The successful audit is in `outputs/validation.txt` and `outputs/coverage_counts.json`. This structural audit does not replace the already completed semantic reading.

## Source-copy exclusion for final packaging

`entries_source.json` and `transcription_numbered.txt` are working copies of attached source content and should be excluded from the final ZIP and checkpoints that omit the attachments. The original notes and transcription were not modified. The substantive deliverables, short evidence locators, programs, computation outputs, search records and check events are retained.

The exact later project context files are absent. Public editions, where opened, are separate references. No reported run status, missing line number, or blank public section is silently promoted into a checked result.
