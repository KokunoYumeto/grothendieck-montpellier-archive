# SA12 — guide to the completed dossier

Start with `SA12_dossier.md`. The authoritative consolidated tables are the `SA12_*.json` and `SA12_*.tsv` files at this archive root. The individual reviewer packages in `reviews/` retain their original identifiers, reasoning, source reads, exact calculations, search records, and qualification of reference access. Where a later closing correction supersedes an earlier local judgment, the canonical tables and the explicit closing note govern; earlier audit records remain for traceability.

## Reading the records

- `SA12_entries.tsv` is the exact 342-row verdict ledger for this part’s source index. The four umbrella entries in MPL_29_095-140 remain four entries; their 56 internal notes are evaluated in the29b review.
- `SA12_items.json`, `SA12_claims.json`, and `SA12_problems.json` separate documentary objects, mathematical claims and open-on-the-page questions. Codex-only source objects have no fabricated source-index verdict. In `sources`, a value matching the supplied index is an entry ID; a `codex/` or `codex:` value is a documentary source locator, not an extra index entry.
- `SA12_id_map.tsv` maps every original record to its surviving canonical ID. A record can combine distinct versions, including a true restricted theorem and a false weaker draft; the statement and status fields explain that distinction. No surviving record is renumbered.
- `SA12_readings.tsv` contains alarms for the next scan-reading run. No ink decision was made and no transcription was changed.
- `SA12_links.tsv` states the actual endpoint-inspection level. `SA12_project_leads.tsv` is the separate extract of context-driven external-project leads. Those absent projects’ reported results are not certified.
- `SA12_refinements.json` gives explicit correction records for refutations that use REF identifiers. Other refutations point to an already present corrected claim, as their event specifies.
- `CHECK_EVENTS.tsv` records actual levels of checking. Numerical examples and finite consistency tests are not certificates of universal geometric assertions.

## Audit and calculations

`outputs/semantic_merge_audit.json` contains the manual alias and partial-occurrence decisions. `outputs/claim_search_coverage.json` maps every original claim to its executed search family and retained search log. `SA12_source_coverage.tsv` maps every supplied scan label to source objects; it is a coverage check, not a substitute for the saved source-reading logs. `outputs/global_counts.json` contains exact counts, including every full source-status label.

The reviews contain `independent_checks.md`, `proofs.md`, `calculations.md`, or their named equivalents, with their executable programs and outputs. Particularly material examples have dedicated files: the formal elliptic nonsplitting proof, the Picard-unit obstruction, the Bertini pinched surface, the stable-corestriction example, the duality counterexample, and the root-system checks. Search logs distinguish an exact opened theorem, metadata-only access, a backward citation, and a failed retrieval. Bibliography `note={verified}` means the listed URL/DOI was opened; read `annote` before treating it as a proof check.

The full external books, article PDFs, rendered pages and bulk retrieval prose are not redistributed. The packaged retrieval records retain queries, URLs, citation IDs and response hashes. User-supplied files and earlier checkpoint archives are also excluded. Source locators refer to the supplied attachments, which remain the authority.

## Rebuilding the consolidated files

Unpack this archive as a directory named `SA12_work`, and place the supplied source folders at the adjacent paths `source/SA12_notes` and `source/SA12_texts`. With Python3 available, the global assembly uses only the retained reviewer records and manual decisions. Run the following in order from the parent directory:

```sh
python SA12_work/programs/closing_semantic_decisions.py
python SA12_work/programs/semantic_decisions.py
python SA12_work/programs/assemble.py
python SA12_work/programs/build_directions.py
python SA12_work/programs/status_rollup.py
python SA12_work/programs/finalize_overview.py
python SA12_work/programs/validate_final.py
```

`python SA12_work/programs/build_final.py` runs these seven steps in order and saves each output.

Individual source-retrieval builders may require reopening the logged public sources; their bulk source caches are intentionally excluded. Do not assume that rerunning a raw search-log parser against its sanitized metadata will reproduce the original raw response. The calculations themselves state their dependencies, usually Python standard libraries or SymPy. Relative audit paths inside a claim resolve against the review package listed in SA12_id_map.tsv; paths beginning with reviews/ resolve from this archive root. Numbered excerpts of the user-supplied source used for inspection remain in the audit, while the original attached files are excluded. The canonical tables can be rebuilt without repeating literature searches or regenerating the manually read verdicts.

`ARCHIVE_MANIFEST.json` lists packaged paths, hashes, byte lengths and whether an external-source payload was replaced by metadata. `progress.log` records UTC stages and the scheduled checkpoints. This is the part1 dossier for cotes29,31,33; other parts listed in TOPIC.md remain outside its scope.
