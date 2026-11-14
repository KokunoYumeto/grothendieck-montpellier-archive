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
  A French correction whose English is unchanged carries no English variant.
- `copy2_annotations.json`, when present, anchors copy 2 evidence in the corrected
  apparatus by source page key. Entries provide `id`, `key`, `kind`, `text_fr`,
  `text_en`, and an optional exact `anchor`; without an anchor the note is set at
  the end of that source page.
- `guide_fragments/` contains the separately authored guide paragraphs in order.
- `retained_usages_fr.tex` lists the recurring French usages retained in the
  reading text, for its preface.

Run `python scripts/build_edition.py annotate` after a scan correction; run
`python scripts/build_edition.py generate` to rebuild all forms. It writes the
French and English standalone sources, their annotated masters, and the guide.
Every visible change is carried by a variant with a kind and source reference.
The generators never infer a new reading from grammar or mathematics.

A lexical variant entry has `id`, `key`, `old`, `new`, `kind`, `reason_fr`,
`reason_en`, and `source_ids`. `old` and `new` are exact TeX strings. Optional
fields are `line`, `occurrence` (one-based; default 1), `math`, and evidence fields.
The generator rejects an absent target. Original line-end hyphens are preserved.

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
- `TRANSLATION_COVERAGE.tsv`: literal math-string comparison and note counts.
- `VARIANTS.json` and `CHANGES.tsv`: the complete French variant register.
- `NOTE_LINKS.json`: note definitions and all return links.
- `CLEANUP_LOG.tsv`: purely syntactic repairs and their decision references.
- `APPARATUS_COUNTS.md`: counts by language, form and kind.
- `BUILD_HISTORY.jsonl`, `PDF_CHECKS.json`, and `build_logs/`: actual build results.

`PDF_CHECKS.json` measures log errors, overfull boxes, missing characters, PDF
links, source-page starts, landscape pages and ink bounds. These measurements do
not claim visual review. The visual review record is completed only after the
rendered pages are inspected.
