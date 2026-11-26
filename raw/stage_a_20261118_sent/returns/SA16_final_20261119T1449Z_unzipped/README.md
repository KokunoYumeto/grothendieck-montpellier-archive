# SA16 archive guide

The primary reading order is `SA16_dossier.md`, then the registers and `SA16_directions.md`. All mathematical and bibliographic statuses are dated 19 November 2026. The final consolidated tables are at the ZIP root. Original component records and their authoring/review history are under `work/`; they preserve pre-merge identifiers and counts.

## Main registers

- `SA16_entries.tsv`: exactly one row per indexed Pro entry; tab-separated UTF-8.
- `SA16_items.json`, `SA16_claims.json`, `SA16_problems.json`: the requested fields plus explicit occurrence, attribution and audit metadata.
- `SA16_readings.tsv`: mathematical alarms only; no decision on absent manuscript images.
- `SA16_links.tsv`: folder, published-work and prior-project relations. `SA16_our_projects.tsv` isolates the last category.
- `SA16_references.bib` and `SA16_reference_audit.json`: canonical bibliography with all occurrence-level access scopes. `verified` means a URL opened at the recorded scope, not that every theorem in the work was independently proved.
- `CHECK_EVENTS.tsv`: one event per actual check/use/refutation; `refined_statement_id` resolves either to a claim or to `SA16_refinements.json`.
- `SA16_id_aliases.tsv`: retired item, claim and bibliography identifiers. All 366 original entry IDs remain unchanged.

The other `SA16_*.json/tsv` files are coverage, navigation, counts and mechanical validation aids. The source manifest proves which attached files were used; the source-immutability check compares their bytes directly with the supplied ZIP without extracting it again.

## Reproduction and paths

The ZIP includes every saved program and its output. `work/code/` contains the root calculations and assembly scripts; `work/parts/<part>/code/` contains component calculations and authoring scripts. Files in `work/outputs/` or component `outputs/` are the saved results. The version manifest records the execution environment. Pure-mathematics scripts use Python, SymPy and mpmath as indicated by their imports; finite enumerations use standard Python. Source retrieval scripts additionally require network access and the original tools or URLs.

Restore the original attached archive once into `sources/` beside `work/` if source-reading or authoring scripts are to be rerun. The attachment itself is not duplicated in this ZIP. An original component reference beginning `parts/` is relative to `work/`; `code/`, `outputs/`, `proof_notes.md` or similar unprefixed paths are relative to that component. References beginning `work/` are ZIP-root-relative. Some audit builders retain the execution workspace as a constant; adjust that constant after relocation. Computation results do not depend on the old workspace name.

The downloaded publication cache and full web response bodies are intentionally excluded. Retrieval metadata retain public URLs, request arguments where saved, provider reference IDs, dates, hashes and authored assessment. A reference into `external_cache/` documents an excluded research cache, not an expected bundled file. Source-read logs quote the supplied user attachments, which remain the authority for the diplomatic text.

The final assembly is built by `work/code/assemble_global.py`, `work/code/build_dossier.py` and the final validation/packaging scripts. These serialize manually made decisions; they do not determine verdicts from headings or keywords. Earlier failed implementation outputs are retained and labelled as rejected. No formal proof assistant was run.

## Checkpoint history

Two complete checkpoints were saved at the scheduled 45-minute boundaries and were not altered thereafter. They are not recursively copied into the final ZIP. The durable checkpoint receipt list records their names, timestamps, hashes and identifiers; no signed transfer URLs are included. `progress.log` records UTC times. The final archive is a complete current bundle and does not require extracting a checkpoint first.
