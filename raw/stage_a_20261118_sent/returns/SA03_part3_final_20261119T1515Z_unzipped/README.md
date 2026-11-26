# SA03 part 3 — using this archive

Start with `SA03_dossier.md`. The requested canonical deliverables are the files
beginning `SA03_`, together with `CHECK_EVENTS.tsv` and `progress.log`.
The original attached archive is the source of truth and is not repeated here.

## Data and locators

`SA03_entries.tsv` has exactly one row per original indexed note. A merged entry
points to its canonical item; corrections and withdrawals retain their reasons.
`SA03_items.json`, `SA03_claims.json` and `SA03_problems.json` contain the full
mathematical and evidential records. Item/claim `lines` are arrays of objects
with `file`, `start` and `end`, relative to the root of the supplied source ZIP.
All are 1-based inclusive line ranges. Problem occurrences use the same locator
objects and also preserve original string locators when useful. Scan numbers are archival marker numbers, not
PDF pages.

`ID_ALIASES.tsv` documents reviewed cross-package consolidation.
`RECORD_ORIGINS.tsv` points to the original part audit. `parts/` preserves those
audits, their human-authored serialization code, proof notes, reading logs,
searches, computations and outputs. Part files may use pre-consolidation IDs;
the alias table gives the canonical IDs in the top-level files. Their local
counts describe those local audits, not additional canonical records.

`SOURCE_MANIFEST.tsv` verifies byte identity with the original ZIP.
`TOPIC_COVERAGE.tsv`, `TRANSCRIPTION_COVERAGE.tsv` and `SCAN_LOCATORS.tsv`
distinguish the whole topic catalogue from this part's actual supply.
`CLAIM_SEARCH_COVERAGE.tsv` links each canonical claim to its documented search.
`CLAIM_EVIDENCE_INDEX.tsv` locates its part's proof and computation bundle; the
claim's own computation field specifies the exact scope and named check.
`STATUS_GROUPS.tsv` supplies the reviewed census grouping without discarding
qualifications in the original `status_on_pages` text.

`SA03_links.tsv` is the two-endpoint-checked link table. Missing outside endpoints
are kept separately in `SA03_link_leads.tsv` and `SA03_project_leads.tsv`.
Read `REFERENCE_POLICY.md` before interpreting a bibliography verification flag.

## Reproduction

Python 3 is used for serialization and exact computations; individual scripts
document additional dependencies such as SymPy, requests or PyMuPDF. Public
literature retrieval requires network access and is not guaranteed to remain
available. For reproduction, extract this final ZIP into a directory named
`deliverable/`. Source-processing programs expect the original attached ZIP
extracted once as the sibling directory `source/`, and the original ZIP itself
at `upload/SA03_Gomtrie_et_topologie_combinatoire_part3.zip` beside those two
directories, matching this run's workspace. The root
programs make no mathematical verdicts: they apply authored merge decisions,
normalize locators and validate integrity.

The main sequence is:

1. Reproduce a relevant part's computation using its `code/` and compare the
   included `outputs/`; do not treat a serialization script as a theorem checker.
2. Run `code/source_audit.py` to compare the original source ZIP with `source/`.
3. Run `code/consolidate.py` after the part records and review tables are present.
4. Run `code/build_support_tables.py`; after any editorial changes, run
   `code/finalize_directions.py` and `code/finalize_dossier.py` as appropriate.
   Then run `code/validate_dossier.py`.
5. Use `code/package_deliverable.py SA03.zip` only for a new final archive; the
   program refuses to overwrite an existing archive.

`outputs/validation.json` records the final mechanical checks and their scope.
`PACKAGE_MANIFEST.json` records each delivered file's size and SHA-256 hash.
`CHECKPOINTS.tsv` identifies scheduled persistent checkpoints; prior ZIPs and
input files are excluded from this ZIP. `progress.log` uses UTC as requested.
