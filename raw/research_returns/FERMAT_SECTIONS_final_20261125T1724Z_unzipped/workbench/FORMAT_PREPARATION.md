# Format 1 and filing

This is an unfiled edition of two works intended for the common Fermat-sections workbench. Its table columns, statuses, check types, source records, original-only file policy, and manifests follow format 1 of the central mathematics-workbenches registry. It does not invent the two WB numbers: the custodian assigns those numbers when filing.

`STATEMENTS.tsv` contains every current numbered mathematical environment, together with earlier superseded statements and explicit refutations. `STATEMENT_TAG_MAP.json` fixes the stable local tag attached to each LaTeX label. `STATEMENT_DETAILS.tsv` gives the exact statement text, dependency information, and check-record pointers. Definitions are recorded as checked conventions; the proper local preprint is an unchecked hypothesis, and the implication conditional on that hypothesis is a proved theorem. `CHECK_EVENTS.tsv` preserves the historical events and distinguishes independent same-model re-proofs from later comparisons and calculations.

The stable local tags have the prefixes FS, FQ, and ERR. They are not represented as allocated permanent WB tags. The original-format tables preceding consolidation remain in `records/statement_history_before_format1.tsv` and `records/check_event_history_before_format1.tsv`; their pending check descriptions reflect the dates when those events occurred, not the latest state.

## Validate the unfiled edition

From the workbench root:

```sh
python3 tools/validate_workbench.py --write-manifest
python3 tools/validate_workbench.py
```

The first command is permitted only while the edition is undeposited. The second checks the table schema, statement coverage, check tags, proof-file pointers, source-key uniqueness, original-file policy, and the full manifest. An unfiled PASS explicitly concerns the declared local-tag edition; it is not a claim that the central registry validator accepts unassigned tags.

## Prepare the numbered version folders

After the custodian has assigned both numbers in `registry/works.tsv`, run `tools/prepare_filing.py` with the registry path, the two assigned numbers, and a new output directory. Its `--help` documents the exact arguments. The utility verifies that both supplied numbers occur in the registry, creates `work/WB-nnnn/v1/` folders, substitutes permanent tags in the format-1 tables, and changes each paper's record address to its assigned page. It writes a tag translation map and never edits this edition or the public registry.

The utility deliberately omits old PDFs after changing their record addresses. Rebuild each numbered paper with its `BUILD.md` command, inspect every page, refresh the corresponding manifests, and then use the central registry's own current validator before depositing. No deposit, publication, author contact, or external repository write has been performed here. A deposited version is immutable; later corrections receive new version folders and dated registry entries.

## Manifest and source identity

The open-text source allowlist includes `.js` and `.mjs` for original JavaScript sources and directly executable ECMAScript modules. The research-record importer, format validator and checkpoint packager preserve both extensions. The earlier exact-integer algorithm keeps its original `.js` source bytes, and the cyclotomic relative-class-number certificate keeps its `.mjs` CLI with a separate expected JSON output. Neither source is renamed or replaced by a generated binary.

`MANIFEST.sha256` records every delivered original file except itself. Source fingerprints are separately recorded in `SOURCE_HASHES.tsv`; none of the referenced external source bytes is included. Historical proof hashes refer to the preserved independent-check snapshots. Any portability-only change made for the public edition is recorded with both hashes in `RECORD_TRANSFORMS.tsv`.

The final paper identity block will distinguish the immutable source snapshot from the generated PDF manifest. A paper cannot contain the hash of a manifest that in turn contains the hash of that very paper without a circular hash dependency. The source manifest therefore omits the generated identity block and PDFs; the complete delivered-artifact manifest, including those files, is detached. The source commit and source-manifest digest identify the mathematical source, while the detached manifest verifies the exact delivered files.
