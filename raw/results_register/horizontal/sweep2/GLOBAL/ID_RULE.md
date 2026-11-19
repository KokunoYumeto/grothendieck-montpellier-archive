# One id rule for the notes (horizontal sweep 2, 18 Nov 2026)

Set by the broad agent a0c4bb37 (Claude Opus 5.5 at effort max) for the work list's item 8. Applied by
`sweep2/_tools/refresh_inputs.py`, which writes every entry to `sweep2/inputs/UNITS.tsv`.

## The rule
An entry id is `<source>#<n>`: the n-th entry of one file, counted from 1 in file order.

| file | `<source>` |
|---|---|
| Pro `<pkg>_notes.md` (final, else the newest checkpoint) | `<pkg>` |
| Pro second chat | `<pkg>_chatB` |
| Pro `<pkg>_doubts.md` | `<pkg>:doubts` |
| Pro records (`research_leads*.md`, `*_pointers.md`) | `<pkg>:records:<file stem>` |
| Work and Codex-web `<folder>_mathnotes.md` | `work:<folder>` |
| Codex `<folder>_notes.md` (notes on the sheets) | `codex:<folder>` |
| Codex `<folder>_doubts.md` | `codex:<folder>:doubts` |

A variant folder keeps its own name (`work:K43-02_2`) and is linked to the base folder.

## What counts as an entry
An entry is a section at the file's entry level:
- **Pro files:** the deepest of `###`, `##` and `#` that occurs at least twice. This is stage A's `###` where it exists, which is why the sweep-1 ids stay valid. Files without `###` were the ones NOTES_INDEX skipped.
- **Work and Codex files:** the shallowest heading level that occurs at least twice, which is the level of "What the pages do", "Statements left without proof" and so on.

## Labels and sub-entries
- A label in a heading (R001, N141.1) is kept in the `label` column.
- The sweep-1 ids of the forms `<pkg>#R001` and `<pkg>#3:N046` are aliases of the canonical `<pkg>#<n>`. They are listed in `GLOBAL/ID_ALIASES.tsv`, together with exact duplicate sections (one entry; the others are aliases) and variant folders filed under their base name.
