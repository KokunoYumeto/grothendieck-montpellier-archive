# Build interface

All paths below are relative to the edition folder. Each reader and each master
is a standalone LuaLaTeX source. Compile any of those files directly on a standard
TeX Live installation with `lualatex` three times.

## Source and generation

- `checked_pages/` is the scan-checked diplomatic source of record.
- `editorial_variants.json` supplies individually justified editorial changes.
- `annotated_pages/` is generated from those inputs, without overwriting them.
- `translated_pages/` contains complete English translations with the same source
  page keys. A translated variant uses `\var{page reading}{corrected reading}{kind}{id}`.
  A French correction whose English is unchanged carries no English wording
  variant. Its English clause carries `\frapparatus{French variant id}` for the
  English account of that source-language correction. Translator explanations
  use `\tnote{id}{text}`; they disappear in the English reading form.
- `copy2_annotations.json`, when present, anchors copy 2 evidence in the corrected
  apparatus by source page key. Entries provide `id`, `key`, `kind`, `text_fr`,
  `text_en`, and an optional exact `anchor`; without an anchor the note is set at
  the end of that source page. `anchor_fr` and `anchor_en` select language-specific
  anchors; `copy2_key` identifies the evidence scan. An annotation whose
  `merged_into_variant` field names a French correction remains in the record but
  is printed through that correction's entry, once. Counts distinguish these
  retained records from separately printed copy2 annotations.
- `guide_fragments/` contains the separately authored guide paragraphs in order.
- `templates/retained_usages_fr.tex` lists the recurring French usages retained in the
  reading text, for its preface.

Run `python scripts/apply_mechanical_cleanup.py` after finalized scan reviews.
It applies only syntax repairs or exact individually approved repairs, records
their hash transitions in `records/MECHANICAL_PATCHES.json`, and adds their
decision/cleanup rows. It uses the same lock as the scan-review writer. The
generator also locks the source snapshot while reading it.

Run `python scripts/build_edition.py annotate` after a scan correction; run
`python scripts/build_edition.py generate` to rebuild all forms. It writes the
French and English standalone sources, their annotated masters, and the guide.
Every visible change is carried by a variant with a kind and source reference.
The generators never infer a new reading from grammar or mathematics.

A lexical variant entry has `id`, `key`, `old`, `new`, `kind`, `reason_fr`,
`reason_en`, and `source_ids`. `old` and `new` are exact TeX strings. Optional
fields are `line`, `occurrence` (one-based; default 1), `math`, and evidence fields.
The generator rejects an absent target. Original line-end hyphens are preserved.
An exact variant ending in a TeX percent comment absorbs the existing source
newline into both arguments; the resulting diplomatic recovery remains exact.
There is no general rule joining words across a hyphen or a source-page boundary.

## Compilation and mechanical checks

`python scripts/compile_readers.py` compiles all generated sources and writes
sanitized logs and measured PDF properties. `--names` selects individual stems;
`--passes` defaults to three. The sources use Latin Modern fonts, fontspec,
babel (French and English), amsmath/amssymb, ulem, xcolor, tikz-cd, marginnote,
etoolbox, microtype and hyperref.

`bootstrap_tex.py` is a fallback for an incomplete execution installation. It
prepares a private TeX support tree and LuaLaTeX format from archived TeX Live
2024 packages. It is unnecessary on a standard working TeX Live installation.
Runtime package archives, font caches and temporary TeX outputs are excluded from
publication files. The standalone reader sources do not depend on this helper.

The generated records include:

- `SOURCE_COVERAGE.tsv`: source hashes and exact diplomatic recovery checks.
- `MASTER_FORM_EQUIVALENCE.json`: exact identity of every form's body and
  declarations with the corresponding annotated master.
- `TRANSLATION_COVERAGE.tsv`: literal math-string comparison and note counts.
- `VARIANTS.json` and `CHANGES.tsv`: the complete French variant register.
- `NOTE_LINKS.json`: note definitions and all return links.
- `CLEANUP_LOG.tsv`: purely syntactic repairs and their decision references.
- `APPARATUS_COUNTS.md`: counts by language, form and kind.
- `BUILD_HISTORY.jsonl`, `PDF_CHECKS.json`, and `build_logs/`: actual build results.
- `BUILD_INPUTS.json`: included source counts and a hash snapshot of the inputs.
- `records/RENDERING_PROBE.json`: the exercised three-/four-line margin boundary,
  durable grouped note bodies, their text-occurrence counts, and visual observation.

`PDF_CHECKS.json` measures log errors, overfull boxes, missing characters, PDF
links, source-page starts, landscape pages and ink bounds. These measurements do
not claim visual review. The visual review record is completed only after the
rendered pages are inspected.

## Final PDF audit and visual observations

`python scripts/pdf_final_audit.py --render` compares the actual compiled PDFs
with the generated source. It writes `FINAL_PDF_AUDIT.json` and the typesetting
report, and renders the forty-page sample plus every recorded overflow/landscape
and designated repair page. The renderings are reproducible working files.

Each per-reader result includes `compiled_source_matches`, `compiled_pdf_matches`,
`upstream_input_mismatches`, per-ID `apparatus_entry_mismatches`, and detailed
geometry failures. Paths and images are checked, including exact butt-capped
rule geometry; the reserved marginal-note lane and conservative rule-box
exclusions are individually recorded. Optical margin protrusion is disabled.

`author_footnote_placements` gives each source (*)/(**) pair's actual physical PDF
pages and a `same_physical_page` result. `endnote_link_audit` gives the calls,
definitions, resolved PDF destinations, forward/return links and problems.
`required_visual_pages` includes the forty spread pages and repair requirements.
`uninspected_required_pages` is computed against the exact current PDF hash.

After looking at the actual rendered pages, write an observation JSON list with
`reader`, `pdf_sha256`, `pdf_page`, `phase`, and `observation`, and run
`python scripts/record_visual_qa.py observations.json`. The helper validates the
current PDF hash and appends safely to `VISUAL_QA.tsv` under a dedicated lock.
Regenerate the PDF audit after appending observations.

Final publication uses `RELEASE_STATUS.json` only after the source/collation and
content work is complete. Working sources and PDFs explicitly identify their
partial coverage. The final packaging groups FR/ in the French ZIP, EN/ and
GUIDE/ in the English ZIP, and the remaining edition paths in the records ZIP;
each ZIP also carries README.md. Extract all three into one directory to rebuild.
