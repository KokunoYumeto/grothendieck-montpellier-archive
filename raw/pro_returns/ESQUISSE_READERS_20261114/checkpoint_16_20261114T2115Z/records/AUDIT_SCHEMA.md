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

The four requested kinds remain `typed difference`, `misreading in one transcription`, `handwriting only in copy 1`, and `handwriting only in copy 2`. An explicitly approved fifth kind, `handwriting in both copies`, records shared handwritten marks with both exact readings and source IDs. These rows also appear verbatim in the derived `records/COLLATION_COMMON_MARKS.tsv`; the complete requested table therefore retains every observed handwritten mark without falsely labeling a shared mark as copy-specific.

`scripts/collate_page.py` supplies `prepare(copy2_key)` and `collate(copy2_key, full=..., originals=..., entries=...)`. Preparing a comparison assigns no outcomes. Calling `collate` certifies inspection of all four image halves and requires both checked source files. Every locus entry supplies its location, both readings, kind, decision, and reason; stable source IDs can be attached. Explicit `folio1` and `folio2` observations optionally record the two copy-specific folios as individual loci. The full-page declaration and checked-source hashes are retained in `records/COLLATION_PAGE_COVERAGE.tsv` and `collation_reviews/`. A revised collation preserves its earlier declaration and locus rows in `collation_reviews/history/`. Final audit validation requires all 58 pairs and detects source changes made after a collation.

The optional explicit `annotations` list supplies bilingual `text_fr`/`text_en`, a kind, stable source IDs, and optional one-based `collation_loci`. It synchronizes that pair's entries in `copy2_annotations.json`, attaching them to the corresponding copy1 page. Each observed copy2 archive foliation receives a concise margin-mark apparatus entry; its handwriting is described as archive foliation, without attribution to the author. Supplying an annotation never creates a reading decision: it refers to the explicit collation and scan records.

## Explicit review interface

`scripts/review_page.py` exposes `commit(key, notes=..., patches=..., macro=..., diffs=..., full=...)`. Calling it certifies that both image halves in the page packet have been inspected. Every observation argument is required. The notes list must match the packet's note-item order and length. An observation can be a string, or a dictionary containing `image_reading`, `reason`, `line`, and `decision`.

Exact corrections are dictionaries with `old`, `new`, and `reason`. A repeated old string requires an explicit `occurrence` or `replace_all` flag. Optional `macro_overrides` and `difference_overrides` provide item-specific results. `additional` records observations absent from the initial target list.

The lower-level `scripts/audit_apply.py` accepts the same observations as an explicit JSON declaration. It requires both inspected image names and full-text confirmation. Before finalizing a page, it checks coverage of every original macro, note item, and difference. The declaration is retained in `reviews/`, allowing the checked file and records to be regenerated. No declaration is generated for an unviewed page.

## Source representation

The one-argument helper `\handcircle{...}` records a handwritten enclosing oval while preserving its complete argument as typed content. It is counted as one enclosing mark in checked macro inventories; its argument is not reclassified as handwriting. The supplied original page sources contain no `handcircle` commands. The first observed use, copy2 site095, is linked to `D2-051`, `N-esq119_119_095-002`, and `L-esq119_119_095-020`; the argument `(*).` includes the typed call and following full stop. Its rendering definition is embedded in the standalone sources.

The input page files use CRLF line endings. The review tools decode these as LF without changing the printed text. The source hash refers to the original attachment bytes. Comments identifying the source transcription's earlier unchecked state are updated on finalization, and one review-status comment is added; these comments do not print. Mechanical TeX repairs are tracked separately in `CLEANUP_LOG.tsv`.

`records/MECHANICAL_PATCHES.json` stores exact mechanical edits as hash transitions: `key`, `before_sha256`, `after_sha256`, `patches`, and `source_ids`. The validator first replays the visual review, then only mechanical entries whose before-hash matches that exact result. It verifies each after-hash. A mechanical repair never substitutes for a scan observation.

## Editorial consideration

`records/EDITORIAL_CANDIDATES.tsv` contains individual proposed corrections, their exact old and new strings, bilingual reasons, and checked same-word parallels. A candidate is emitted only after its page and its evidence page are checked. Stable difference and source-line IDs connect it to the scan record. `editorial_variants.json` contains only explicitly approved candidates and supplies the corrected-master generator; it does not modify `checked_pages/`.

`records/EDITORIAL_ADJUDICATIONS.tsv` covers each checked DIFFERENCES row classified as `silent-correction` or `wording`, plus individually identified lexical-normalization loci. The fields give its stable difference ID, original source reading, candidate and approved-variant IDs where present, editorial outcome and reason, scan-decision links, and checked-page hash. Explicit retentions explain recurring spellings, unresolved visual readings, ambiguous wording, or insufficient checked parallel evidence. Newly checked loci absent from the authored decision map remain pending. Mechanical comparison does not create an approval or a retention. Superseded editorial outcomes and reasons are retained in `records/EDITORIAL_ADJUDICATION_HISTORY.tsv`.

`records/SECOND_READINGS.tsv` records targeted independent visual comparisons. A second reading can support a revision, preserve a handwriting assignment, or retain alphabet uncertainty. Earlier superseded observations stay in the review history.
