# SA18 — Variétés abéliennes

Start with [SA18_dossier.md](SA18_dossier.md). It gives the English overview,
principal findings, source and authorship distinctions, verification limits
and final counts. The status cutoff is **19 November 2026**.

## Main deliverables

| File | Contents |
|---|---|
| [SA18_entries.tsv](SA18_entries.tsv) | Exactly one verdict for each of the335 original indexed entries |
| [SA18_items.json](SA18_items.json) | Canonical note objects, modern statements, reconstruction and text checks |
| [SA18_claims.json](SA18_claims.json) | Atomic claims, page status, calculations, searched fate, class and references |
| [SA18_problems.json](SA18_problems.json) | Questions and open steps, all occurrences, exact modern comparison and value of further work |
| [SA18_readings.tsv](SA18_readings.tsv) | Mathematical alarms for the next scan review; no new ink decisions |
| [SA18_links.tsv](SA18_links.tsv) | Checked folder and publication links with both endpoints |
| [SA18_project_links.tsv](SA18_project_links.tsv) | Earlier-run project leads, kept separate and explicitly qualified |
| [SA18_directions.md](SA18_directions.md) | Globally ranked future task specifications |
| [SA18_references.bib](SA18_references.bib) | Every bibliographic key and its verified/unverified access label |
| [SA18_reference_index.md](SA18_reference_index.md) | Readable bibliography with URLs and exact verification scopes |
| [CHECK_EVENTS.tsv](CHECK_EVENTS.tsv) | Typed checks, uses, computations, independent arguments and refutations |
| [progress.log](progress.log) | UTC start, stage records, scheduled checkpoints and completion |

Additional machine-readable files are `SA18_aliases.json`, `SA18_counts.json`,
`SA18_source_coverage.json`, `SA18_directions.json` and
`SA18_literature_search.tsv`. [SA18_proof_index.md](SA18_proof_index.md) locates
the mathematical proof records, executed programs and their actual outputs.

## Coordinates and identities

Paths beginning `SA18_texts/` or `SA18_notes/` refer to the original user
attachment after extraction. Line numbers are **absolute one-based file
lines**, not manuscript pagination or page-local line numbers. Scan numbers
are always interpreted with their cote. The source manifest records hashes
and line counts; the page index is a navigation aid, not an automatic
scientific classification.

Each indexed entry has one primary item assignment. Other contextual links
from that note to supplemental transcription findings are in
`related_note_entries`. An empty item `sources` array or claim `items` array
means that no corresponding indexed Pro-note entry exists; the direct source
coordinates remain present. No index entry was invented for Codex material.

Canonical IDs survive across tables. Removed IDs are resolved by
`SA18_aliases.json`. Source-specific statements and proof statuses remain in
merged records and occurrences. `parts/` preserves the complete owner
contributions before master normalization, so an original ID there may be an
alias in the main tables. Counts in an owner audit are owner counts, not the
final deduplicated total.

## Evidence and scientific scope

The four source owners read their assigned notes, complete transcriptions,
doubts and applicable second-pass controls. The current second-pass reading
controls where it changes the Pro witness. No source transcription was edited,
and no mathematical diagnosis was promoted to a new decision about the ink.

The dossier distinguishes the historical text, the earlier notes, opened
literature and present reconstruction. Reused material is not automatically
assigned Grothendieck authorship. A verified reference label records that a
link was opened; the accompanying scope note distinguishes a precise theorem
or proof read from a metadata-only check. An inaccessible original source is
not promoted to verified because a later paper cites it.

A finite computation proves its stated example or finite identity only.
General arguments are in the proof records. ClassificationD is a bounded
negative search result, classificationC names an exact remaining clause, and
classificationF records an unidentified statement. These are completed
assessments, not promises that an unrestricted literature search has proved
absence or that every source-level obligation is a modern open problem.

## Reproduction and audits

`scripts/integrate_dossier.py` applies the explicitly reviewed merge map; it
does not infer identities or verdicts from headings. `scripts/audit_master.py`
checks original-entry coverage, references, statuses, source coordinates,
events, searched-fate associations and output-file availability.
`outputs/master_audit.json` records its final result. The owner audits and
independent proof review are retained under `parts/`.

The integration programs expect the extracted attachment in a sibling
`sources` directory. The source-owner acquisition and navigation programs
preserve some paths from the original run. Mathematical programs and their
saved outputs are included; external web searches may yield different
content when repeated later. Primary-source PDF bodies, the original user
attachments, and earlier checkpoint archives are excluded from this ZIP.

`ARCHIVE_MANIFEST.json` records every delivered file's hash. Each checkpoint
is a complete immutable snapshot on the requested45-minute cadence; the
scheduled and actual times are recorded in the log. The final archive is the
completed consolidated dossier.
