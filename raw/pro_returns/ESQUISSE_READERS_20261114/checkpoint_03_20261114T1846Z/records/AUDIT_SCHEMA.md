# Scan-review records

The records distinguish an observation made by the reviewer from a mechanical operation performed by a script. The scripts never mark a scan inspected because its file exists or because a prior transcription is present.

## Source packets

Each page packet contains the original byte hash, complete source text with LF line endings for review, numbered source lines, archive metadata, both required scan-image names, every content macro, all review notes, and every original difference row. The inventory includes nested commands. The `commented` flag identifies content commands suppressed by an inline percent sign; full comment lines do not contribute content commands.

Difference IDs retain original record order: `D1-001`–`D1-327` and `D2-001`–`D2-141`. Macro IDs use `M-<key>-<occurrence>`, and note IDs use `N-<key>-<item>`. Source-line IDs use `L-<key>-<line>`.

## CHECK_DECISIONS.tsv

Columns: `decision_id`, `source_item_id`, `key`, `cote`, `site`, `line`, `transcription_reading`, `image_reading`, `decision`, `reason`, `images`.

`line` addresses the supplied page transcription, whose line divisions generally follow the typed lines. A textual position is retained where the source record identifies a margin or supplies no line. `images` names the two reviewed halves by their paths inside the scan ZIP. Each explicit correction has an exact old reading, observed reading, decision, and reason. Confirmed source lines and confirmed markup also have individual rows. Retained doubt is recorded as uncertainty retained.

## DIFFERENCES_OUTCOMES.tsv

The original columns `key`, `cote`, `site`, `typescript_page`, `class`, `draft`, `page`, and `note` remain unchanged. Added columns are `difference_id`, `outcome`, `reason`, and `decision_ids`. Corrections to the checked page do not rewrite the original `page` field: the decision record supplies the new reading.

## COLLATION.tsv

Columns: `collation_id`, `typescript_page`, `line`, `copy1_key`, `copy2_key`, `copy1_reading`, `copy2_reading`, `kind`, `decision`, `reason`, `decision_ids`.

The table is initialized without outcomes. A source-file comparison supplies possible places to inspect; it does not settle a reading. Collation decisions require both copies to have been viewed.

`scripts/collate_page.py` supplies `prepare(copy2_key)` and `collate(copy2_key, full=..., originals=..., entries=...)`. Preparing a comparison assigns no outcomes. Calling `collate` certifies inspection of all four image halves and requires both checked source files. Every locus entry supplies its location, both readings, kind, decision, and reason; stable source IDs can be attached. Explicit `folio1` and `folio2` observations optionally record the two copy-specific folios as individual loci. The full-page declaration and checked-source hashes are retained in `records/COLLATION_PAGE_COVERAGE.tsv` and `collation_reviews/`. A revised collation preserves its earlier declaration and locus rows in `collation_reviews/history/`. Final audit validation requires all 58 pairs and detects source changes made after a collation.

## Explicit review interface

`scripts/review_page.py` exposes `commit(key, notes=..., patches=..., macro=..., diffs=..., full=...)`. Calling it certifies that both image halves in the page packet have been inspected. Every observation argument is required. The notes list must match the packet's note-item order and length. An observation can be a string, or a dictionary containing `image_reading`, `reason`, `line`, and `decision`.

Exact corrections are dictionaries with `old`, `new`, and `reason`. A repeated old string requires an explicit `occurrence` or `replace_all` flag. Optional `macro_overrides` and `difference_overrides` provide item-specific results. `additional` records observations absent from the initial target list.

The lower-level `scripts/audit_apply.py` accepts the same observations as an explicit JSON declaration. It requires both inspected image names and full-text confirmation. Before finalizing a page, it checks coverage of every original macro, note item, and difference. The declaration is retained in `reviews/`, allowing the checked file and records to be regenerated. No declaration is generated for an unviewed page.

## Source representation

The input page files use CRLF line endings. The review tools decode these as LF without changing the printed text. The source hash refers to the original attachment bytes. Comments identifying the source transcription's earlier unchecked state are updated on finalization, and one review-status comment is added; these comments do not print. Mechanical TeX repairs are tracked separately in `CLEANUP_LOG.tsv`.
