# Pursuing Stacks: working checkpoint 01

This checkpoint records work in progress. It is not a completed edition.

The first review batches have been committed with explicit image findings; the complete edition remains in progress.

- Pages visually reviewed and committed: 54 / 706.
- Original comparison rows: 12,140; all are present in ARXIV_CONCORDANCE.tsv.
- Rows awaiting image review retain the explicit pending outcome.
- Source edits recorded: 364.
- Decision records: 1036.
- No reader has passed the complete publication gates at this checkpoint.

## Contents and continuation

checked_pages/ contains only pages with a complete, explicit visual review.
review/ holds the item-level findings and exact source edits. A page's original
metadata header is historical; its current status is in its review record.
guide_parts/ holds section paragraphs completed during review.
build_scripts/ contains the reproducible record and edition tooling written so far.
PAGE_REVIEW_COVERAGE.tsv and REVIEW_STATUS.json provide exact coverage.

The supplied archives PS_TEXT.zip, PS_SCANS_1.zip and PS_SCANS_2.zip remain the
sources for transcription/, records/, arxiv/, standard/ and scans/. Extract them
beside build_scripts/, preserving their internal paths, then restore this
checkpoint over the extracted tree. The arXiv witness and scans are not republished
inside this checkpoint. No previous checkpoint ZIP is embedded.

Run `python build_scripts/assemble_records.py` to rebuild the audit tables.
Run it with `--require-complete` to enforce the visual-review completion gate.
Run `python build_scripts/review.py status` to report coverage by cote.
The scripts themselves do not make or infer image decisions.
