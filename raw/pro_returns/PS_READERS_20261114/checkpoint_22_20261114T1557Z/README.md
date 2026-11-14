# Pursuing Stacks: edition in progress

Status: visual collation and reader production in progress. No page or PDF is certified complete unless the page ledger and quality-control records explicitly say so.

All supplied manifest hashes verified: 2,158 files, 501,089,067 bytes. The sources remain unchanged in the input archives. Checked page files and decisions are written incrementally.

## Current scope

The latest merged audit is `records/COVERAGE_AUDIT.json`; it is the authoritative live count. At the last prose update it covered 180 of 706 source pages and 4,905 decision rows. All 12,140 comparison rows exist in `records/ARXIV_CONCORDANCE.tsv`; rows on unreviewed pages are explicitly pending. No missing required difference, original doubt, or NOTES decision was found among the reviewed pages. The present work is incomplete.

Each reviewer has inspected both supplied half-images of each page marked reviewed. `records/PAGE_REVIEW.tsv` records that status. Original uncertainties are either resolved with image evidence or retained. Additional uncertainties are introduced where the original transcription was overconfident. The arXiv text is a comparison witness, never a substitute for viewing a scan.

## Files and derivation

- `checked_pages/`: the incrementally corrected source of record, one file per reviewed source page.
- `records/CHECK_DECISIONS.tsv`: merged decisions, with stable original-difference, doubt, note, change and metadata identifiers.
- `records/ARXIV_CONCORDANCE.tsv`: all supplied comparison rows plus outcome and reason; interim pending states are explicit.
- `records/REVIEW_COVERAGE.tsv` and `COVERAGE_AUDIT.json`: script checks of individual decision coverage.
- `guide_sections/`: guide paragraphs written as sections finish, including mathematical cautions and changes of mind supported by the scans.
- `readers/`: standalone LuaLaTeX working readers and master, explicitly labelled with their reviewed-page count.
- `records/CHANGES_EN.tsv`: maximal editorial variants governing both corrected forms.
- `records/MASTER_VARIANTS_*.json`: explicit transpositions and other corrections requiring more than one local source macro.
- `records/TYPESETTING_PATCHES.json` and `TYPESETTING_FIXES_GENERATED.tsv`: local layout repairs and the mechanical transformations used in the working build.
- `records/OVERFLOW_HISTORY.tsv` and `VISUAL_QA.json`: all logged overflows and actual rendered-page inspections. Rendering alone is not marked as visual inspection.
- `review_notes/`: page-specific evidence and unresolved readings.
- `scripts/`: reproducible review, merge, generation, compile, audit and checkpoint code.
- `logs/` and `qa/`: build evidence, detailed scan crops, partial proof builds and rendered pages.

`scripts/build_readers.py` annotates the reviewed sources with explicit variants, reconstructs the diplomatic branch and asserts equality with the mechanically normalized source, then emits each standalone form by switching `EditionMode`. The diplomatic form preserves superseded material. The corrected apparatus applies the author's cancellations, insertions, overprints and recorded transpositions, retaining both readings and a reason in its apparatus. The reading form applies the same corrected branch without apparatus or color distinctions. Consistent authorial spelling and mathematical slips are preserved.

The current apparatus uses one entry per maximal operation: internal layers of a wholly cancelled or replaced passage remain in that entry rather than producing duplicate calls. Final apparatus counts and the treatment of unchanged marginal-note placement are still under review; no final count is certified yet.

## Build status and remaining work

The 154-source-page diplomatic working build completed with LuaLaTeX: 157 physical PDF pages, no missing characters, five overfull boxes, widest 18.79446 pt. This is a proof, not an accepted final reader. Its four pages with overflows above 2 pt were rendered and visually inspected; local breakpoint repairs are now being checked in separate-cote builds. The corrected-apparatus build previously reached its end but failed at PDF export because the local TeX font map was missing; that environment problem has been repaired. New source material is compiled incrementally. The complete readers, complete guide, final link audit and requested full visual sample are still pending.

Mechanical normalization currently occurs in the master-generation pipeline and is individually logged. Before final acceptance, these repairs must also be integrated into the checked page files with decision records, while preserving the diplomatic text. No blanket diagram scaling or enlarged `hfuzz` is used.

## Checkpoints and reproducibility

The checkpoint watcher creates immutable, complete snapshots after ten additional checked pages or before an hour elapses. `records/CHECKPOINT_HISTORY.jsonl` identifies successful snapshots. Earlier ZIPs and the supplied archives/images are not nested inside checkpoints. The final report must identify any superseded working proofs or logs omitted from the final packages.

Run the review scripts only when reproducing their recorded judgments; they contain explicit human-readable image observations, not automatic image inference. Run `python3 scripts/audit_records.py`, `python3 scripts/build_readers.py`, then `python3 scripts/compile_reader.py readers/PS_EN_diplomatic.tex` from an environment with the supplied inputs adjacent to this project. A standard TeX Live with LuaLaTeX, Latin Modern, TikZ, unicode-math and lua-ul should compile the standalone readers. The compile wrapper additionally supports the repaired local test environment. Paths in the distributed records are ZIP-relative.
