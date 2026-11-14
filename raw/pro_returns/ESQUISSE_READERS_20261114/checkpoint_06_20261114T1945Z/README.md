# Esquisse d'un programme — readers and review records

**INCOMPLETE WORKING EDITION — this snapshot has not passed all release gates.**

README snapshot generated 2026-11-14 19:44:53 UTC by [scripts/write_readme.py](scripts/write_readme.py). Counts below describe the files read for this snapshot. Earlier checkpoints and earlier PDFs retain their own histories. A full translation source or a successful partial compilation does not establish completion of the two-copy collation or the final visual review.

## Scope and source coordinates

The edition concerns Alexander Grothendieck's January 1984 *Esquisse d'un programme*, Université de Montpellier, fonds Grothendieck, cote 119. Copy 1 comprises the sommaire and typescript pages 1–57 at archive sites 2–59; copy 2 comprises the corresponding 58 pages at sites 78–135. The archive viewer's PDF page is the site number plus one. Every source-page link is taken from [records/PAGE_MAP.tsv](records/PAGE_MAP.tsv).

The supplied text and scan manifests are retained as verified inventory outcomes in [records/SOURCE_INTEGRITY.json](records/SOURCE_INTEGRITY.json) and summarized in [records/SOURCE_INVENTORY.md](records/SOURCE_INVENTORY.md). Each source page was supplied as two overlapping image halves. A checked page requires an explicit observation of both halves; file presence and prior transcription alone do not constitute inspection. The source readings in this edition are decided from those scans. Published editions supply no replacement readings.

## Three ZIP layouts

| Archive | Paths retained at its root | Contents |
|---|---|---|
| ESQUISSE_READERS_FR.zip | FR/; README.md | Three French readers and the French annotated master, each as standalone .tex and PDF. |
| ESQUISSE_READERS_EN.zip | EN/; GUIDE/; README.md | Two English readers, the English annotated master, and the guide, each as standalone .tex and PDF. |
| ESQUISSE_READERS_RECORDS.zip | All remaining edition-root paths; README.md | Checked and annotated page files, translations, guide fragments, scripts, templates, review records, build logs, tables, JSON files and reports. |

The same README accompanies all three archives. Paths below are relative to their combined edition root. Extract the three delivery ZIPs into one directory, preserving FR/, EN/, GUIDE/ and the shared paths. For the complete source-validation workflow, extract the two supplied input archives separately as follows, from the directory containing the ZIP files:

```sh
mkdir -p work/edition work/source work/images
unzip -o ESQUISSE_READERS_FR.zip -d work/edition
unzip -o ESQUISSE_READERS_EN.zip -d work/edition
unzip -o ESQUISSE_READERS_RECORDS.zip -d work/edition
unzip -o ESQUISSE_TEXT.zip -d work/source
unzip -o ESQUISSE_SCANS.zip -d work/images
```

The scan files then lie under work/images/scans/. The supplied archives are inputs and are not repackaged inside the delivery ZIPs. A standalone reader .tex can be compiled independently of the records ZIP and the supplied scan images.

## Documents

| Role | Files | Purpose |
|---|---|---|
| French diplomatic reader | [.tex](FR/ESQUISSE_FR_diplomatique.tex) · [PDF](FR/ESQUISSE_FR_diplomatique.pdf) | Copy 1 followed by copy 2, with their checked typed and handwritten readings. |
| French corrected reader | [.tex](FR/ESQUISSE_FR_corrige_apparat.tex) · [PDF](FR/ESQUISSE_FR_corrige_apparat.pdf) | The corrected copy 1 text, with the French apparatus and separately identified copy 2 annotations. |
| French reading text | [.tex](FR/ESQUISSE_FR_texte_de_lecture.tex) · [PDF](FR/ESQUISSE_FR_texte_de_lecture.pdf) | The same corrected text with editorial apparatus and correction markers suppressed; authorial notes and doubts remain. |
| French annotated master | [.tex](FR/ESQUISSE_FR_master_annotated.tex) · [PDF](FR/ESQUISSE_FR_master_annotated.pdf) | The shared French variant-bearing source; its PDF displays the corrected apparatus projection. |
| English corrected reader | [.tex](EN/ESQUISSE_EN_corrected_translator_notes.tex) · [PDF](EN/ESQUISSE_EN_corrected_translator_notes.pdf) | The complete English translation with shared variant IDs, French-source apparatus, copy 2 annotations and translator's notes. |
| English reading text | [.tex](EN/ESQUISSE_EN_reading.tex) · [PDF](EN/ESQUISSE_EN_reading.pdf) | The same English translation with editorial apparatus and translator's notes suppressed; authorial notes and doubts remain. |
| English annotated master | [.tex](EN/ESQUISSE_EN_master_annotated.tex) · [PDF](EN/ESQUISSE_EN_master_annotated.pdf) | The shared English variant-bearing source; its PDF displays the corrected apparatus projection. |
| Guide | [.tex](GUIDE/ESQUISSE_GUIDE.tex) · [PDF](GUIDE/ESQUISSE_GUIDE.pdf) | A collation preface and one commentary paragraph for the sommaire, each of sections 1–10, and each of notes 1–7. |

The diplomatic reader contains both copies in order. The corrected French and English forms use copy 1 as the base. The guide keeps the eighteen requested commentary paragraphs in source order; its additional collation preface is counted separately. The annotated masters and their compiled PDFs expose the reusable apparatus-bearing sources.

## Form generation and variant policy

The source of record is `checked_pages/`. `editorial_variants.json` contains only explicitly approved editorial changes with exact old/new TeX strings, bilingual reasons and stable evidence IDs. `annotated_pages/` is generated without overwriting those checked files. `scripts/build_edition.py` then embeds the common macros, font/glyph definitions, page bodies, variant declarations and note links into each standalone source.

A changed reading is represented by `\var{page reading}{corrected reading}{kind}{id}`. The diplomatic projection selects the first argument. The corrected projections select the second; the apparatus projection also prints the reason under that ID. The reading projection suppresses the apparatus marker and note. Unchanged handwriting retains its source macro and receives no variant merely for being handwritten.

| Form | Text selected | Apparatus and source marks |
|---|---|---|
| FR diplomatic | Checked readings of copy 1 and copy 2 | Typed/handwritten distinctions, deletions, insertions, overwriting, marginal material, underlining, foliation and doubts remain. |
| FR corrected with apparatus | Corrected copy 1 | Approved variants and separately identified copy 2 annotations are printed; the author's notes and doubts remain. |
| FR reading | The same corrected copy 1 | Editorial apparatus is suppressed; authorial notes and doubts remain; scan and source-page labels move to the margin. |
| EN corrected with translator's notes | Translation of corrected copy 1 | Meaningful English variants use the corresponding French IDs; unchanged English clauses carry French-source notes; translator's notes and copy 2 notes remain distinct. |
| EN reading | The same English translation | Editorial apparatus and translator's notes are suppressed; authorial notes, doubts, and marginal scan/page labels remain. |

An isolated French typing slip is corrected only through an approved evidence record. Its English clause receives an English wording variant only when the correction changes the English wording. Otherwise `\frapparatus{French-id}` prints the French old/new readings and their English explanation at the corresponding clause, without creating an English wording variant. `\tnote{TN-site-number}{English explanation}` identifies translator's notes separately. The shared French IDs, including the name correction Ladegraillerie → Ladegaillerie, are aligned in [translated_pages/FRENCH_APPARATUS_ALIGNMENT.tsv](translated_pages/FRENCH_APPARATUS_ALIGNMENT.tsv) and [translated_pages/TRANSLATION_INDEX.json](translated_pages/TRANSLATION_INDEX.json).

Copy 2 revisions are recorded in the collation and in `copy2_annotations.json`. A copy 2 correction enters the corrected copy 1 text only when explicitly approved as correcting a typing slip shared by the two copies. The source annotation then names its `merged_into_variant` ID; its evidence remains in the records, while its printed explanation is merged into that one shared variant. Other copy 2 deletions, additions, move marks and marginal marks remain identified as copy 2 evidence. Common handwriting is recorded under the explicitly approved collation kind “handwriting in both copies”, with both readings and evidence links; [records/COLLATION_COMMON_MARKS.tsv](records/COLLATION_COMMON_MARKS.tsv) is a verbatim companion subset of the full collation.

Stable IDs distinguish original differences (D1-001–D1-327; D2-001–D2-141), source lines (L-page-key-line), macros (M-page-key-occurrence), original note items (N-page-key-item), scan decisions (C-page-key-number), collation loci (COL-119-site-number), French slips (V-FR-site-number), copy 2 notes (A2-119-site-number), and translator's notes (TN-site-number). Automatic authorial deletion/insertion/overwriting variants use V-page-key-kind-number. The exact schemas are in [records/AUDIT_SCHEMA.md](records/AUDIT_SCHEMA.md).

## Retained source usages, doubts and mathematical content

The French forms retain recurring usages including Légo-Teichmüller, bidimensionelle/bidimensionelles, boite, arètes, polygône/polygônes, occurence and points bases. They also retain checked source naming and lexical variation such as the singular title Histoire de Modèles and hyperquadratique. The individual retention reasons, as well as the approved isolated slips, are recorded in [records/EDITORIAL_ADJUDICATIONS.tsv](records/EDITORIAL_ADJUDICATIONS.tsv); superseded decisions remain in its history table. A spelling or agreement rule alone does not silently replace a source reading.

Uncertain readings retain `\unsure{...}` and illegibility retains `\illegible{...}`, with links to their particular scans in every reader. Doubtful dots and unresolved alternatives are retained at the translated anchors and explained where necessary. The rounded open mathematical glyph recorded as `\unsure{\sourceglyph{119A}}` preserves an individually inspected contour without assigning a conventional alphabet. Its vector, coordinate transformation and provenance are documented in [records/SOURCE_GLYPHS.md](records/SOURCE_GLYPHS.md), [records/SOURCE_GLYPH_119A.json](records/SOURCE_GLYPH_119A.json) and [records/SOURCE_GLYPH_USAGE.tsv](records/SOURCE_GLYPH_USAGE.tsv). The vector definition is embedded in each standalone source.

The English formulas preserve the exact checked French TeX fragments, including source peculiarities and the complete diagram. The translation index compares their ordered strings and records both source hashes. The guide discusses identified mathematical difficulties using explicit maps or calculations and exact source references; those discussions do not alter the readers' formulas. The source's authorial notes (1)–(7) remain at the end, with every call linked to its note and every note linked back to its calls. Local (*) and (**) authorial notes remain associated with their source-page text. Marginal content of more than three rendered lines is set as a labeled block; shorter content uses the reserved margin. Handwritten archive foliation is preserved without attributing its hand to the author.

English terminology follows the supplied unified glossary and standardization instructions. The guide's references to later literature are named and sourced without borrowing their readings of the Esquisse. Checked external reference details are in [guide_fragments/EXTERNAL_REFERENCES.tsv](guide_fragments/EXTERNAL_REFERENCES.tsv).

## Current source and apparatus counts

| Measure | Current value | Evidence |
|---|---|---|
| Checked copy 1 pages | 58/58 | checked_pages/ and reviews/ |
| Checked copy 2 pages | 11/58 | checked_pages/ and reviews/ |
| Current finalized page declarations | 69/116 | Matching checked hashes and explicit two-image/full-text declarations |
| Scan-decision rows | 3570 | CHECK_DECISIONS.tsv |
| Original difference outcomes | 365/468 | DIFFERENCES_OUTCOMES.tsv |
| Collated page pairs | 11/58 | records/COLLATION_PAGE_COVERAGE.tsv |
| Individual collation loci | 50 | COLLATION.tsv |
| Editorial wording-locus adjudications | 141 | records/EDITORIAL_ADJUDICATIONS.tsv |
| Approved isolated French slips | 46 | editorial_variants.json |
| English source pages | 58/58 | translated_pages/ |
| Exact math fragments in translation index | 519 | TRANSLATION_INDEX.json; current hashes: yes |
| Complete diagrams in translation index | 1 | TRANSLATION_INDEX.json |
| Translator's notes | 52 | tnote markers in translated_pages/ |
| Guide commentary units | 18/18 | guide_fragments/ excluding filenames containing preface |
| Additional guide prefatory units | 1 | guide_fragments/ |
| Copy 2 annotation records | 28 | copy2_annotations.json |
| Copy 2 notes printed separately | 26 | Records without merged_into_variant |
| Copy 2 records merged into shared variants | 2 | Records with merged_into_variant |

These are current input counts. The last generated build records report 67 checked pages, 58 translated pages and 46 French variants. Any difference from the current inputs requires regeneration; the per-document freshness checks below also detect content changes that leave counts unchanged.

### Decision and collation outcomes

| Record | Outcome or kind | Count |
|---|---|---|
| Scan decisions | add hand wrapper | 6 |
| Scan decisions | confirm typed arrow | 3 |
| Scan decisions | confirmed on image | 392 |
| Scan decisions | describe nonlinguistic mark in NOTE comment; no content character assigned | 1 |
| Scan decisions | difference description corrected | 1 |
| Scan decisions | earlier handwriting classification superseded | 3 |
| Scan decisions | full line checked on image | 2464 |
| Scan decisions | illegibility retained | 1 |
| Scan decisions | mechanical LaTeX repair; printed reading unchanged | 1 |
| Scan decisions | note checked on image | 214 |
| Scan decisions | our transcription corrected | 21 |
| Scan decisions | our transcription corrected; uncertainty retained | 1 |
| Scan decisions | record nonlinguistic mark; no content character assigned | 1 |
| Scan decisions | still doubtful | 2 |
| Scan decisions | the typescript reads as our transcription | 336 |
| Scan decisions | transcription corrected | 107 |
| Scan decisions | typescript reads as our transcription | 1 |
| Scan decisions | uncertainty retained | 14 |
| Scan decisions | uncertainty retained for preceding point; numeral confirmed | 1 |
| Original differences | difference description corrected | 1 |
| Original differences | our transcription corrected | 21 |
| Original differences | our transcription corrected; uncertainty retained | 1 |
| Original differences | still doubtful | 2 |
| Original differences | the typescript reads as our transcription | 336 |
| Original differences | typescript reads as our transcription | 1 |
| Original differences | uncertainty retained | 3 |
| Collation | handwriting in both copies | 13 |
| Collation | handwriting only in copy 2 | 17 |
| Collation | misreading in one transcription | 18 |
| Collation | typed difference | 2 |
| Editorial consideration | approved isolated slip | 44 |
| Editorial consideration | retained after editorial consideration | 97 |

### Doubt marks before and after review

| Copy | Scope | Pages | unsure | illegible |
|---|---|---|---|---|
| 1 | original complete copy | 58 | 6 | 0 |
| 1 | original pages now checked | 58 | 6 | 0 |
| 1 | current checked pages | 58 | 39 | 0 |
| 2 | original complete copy | 58 | 19 | 1 |
| 2 | original pages now checked | 11 | 8 | 1 |
| 2 | current checked pages | 11 | 11 | 1 |

The original counts come from the supplied-source inventory; current counts parse the checked pages, including nested doubt macros. Review can add a newly observed doubt as well as resolve an earlier one, so subtraction of these totals is not a count of resolved loci. Each decision and its prior state remain traceable in the review records.

### Apparatus entries by form and kind, cote 119

| Form or entry class | Kind | Current input count |
|---|---|---|
| FR diplomatic | editorial apparatus | 0 |
| FR reading | editorial apparatus | 0 |
| EN reading | editorial apparatus and translator's notes | 0 |
| FR corrected | slip corrected | 46 |
| EN corrected: English wording | slip corrected | 1 |
| EN corrected: French-source note | slip corrected | 45 |
| FR corrected | copy 2: deletion | 2 |
| FR corrected | copy 2: handwritten sign | 1 |
| FR corrected | copy 2: marginal note placed | 19 |
| FR corrected | copy 2: relocation | 1 |
| FR corrected | copy 2: uncertain mark | 1 |
| FR corrected | copy 2: writing over | 2 |
| EN corrected | copy 2: deletion | 2 |
| EN corrected | copy 2: handwritten sign | 1 |
| EN corrected | copy 2: marginal note placed | 19 |
| EN corrected | copy 2: relocation | 1 |
| EN corrected | copy 2: uncertain mark | 1 |
| EN corrected | copy 2: writing over | 2 |
| EN corrected | translator's note | 52 |

French-source notes explain the French correction at an unchanged English clause and are counted separately from English wording variants. Merged copy 2 evidence is counted once under its shared variant. The generator's last emitted apparatus table is [APPARATUS_COUNTS.md](APPARATUS_COUNTS.md); actual printed-entry IDs and counts are checked against the PDF build log in the final audit.

## Per-PDF build, link and visual-review status

The build columns report the latest sanitized build record for each named file. A PDF is current only after its standalone source matches the current inputs, its compiled-source hash matches that source, and the final audit records the exact current PDF hash. A row with a stale or absent audit does not certify current links or geometry.

| Document | PDF pages | Errors | Warnings | Overfull / widest pt | Missing glyphs | Source current / compiled source current |
|---|---|---|---|---|---|---|
| French diplomatic reader | — | 2 | 0 | 0 / 0 | 0 | no / no |
| French corrected reader | 61 | 0 | 0 | 0 / 0 | 0 | no / no |
| French reading text | 61 | 0 | 0 | 0 / 0 | 0 | no / no |
| French annotated master | 61 | 0 | 0 | 0 / 0 | 0 | no / no |
| English corrected reader | — | 2 | 0 | 0 / 0 | 0 | no / no |
| English reading text | 56 | 0 | 0 | 0 / 0 | 0 | no / no |
| English annotated master | 56 | 0 | 0 | 0 / 0 | 0 | no / no |
| Guide | 9 | 0 | 0 | 0 / 0 | 0 | no / no |

| Document | Archive / all external / internal link annotations | Final audit current | Required pages inspected for exact PDF | Outside sheet / text area |
|---|---|---|---|---|
| French diplomatic reader | — / — / — | no | current audit required | 0 / 0 |
| French corrected reader | 99 / 99 / 16 | no | current audit required | 0 / 1 |
| French reading text | 97 / 97 / 16 | no | current audit required | 0 / 1 |
| French annotated master | 99 / 99 / 16 | no | current audit required | 0 / 1 |
| English corrected reader | — / — / — | no | current audit required | 0 / 0 |
| English reading text | 92 / 92 / 12 | no | current audit required | 0 / 0 |
| English annotated master | 94 / 100 / 12 | no | current audit required | 0 / 1 |
| Guide | 52 / 70 / 0 | no | current audit required | 0 / 0 |

The required visual sample consists of forty pages spread through each reader, or every page of a shorter document, plus every mandatory overflow/repair, landscape and special-glyph/diagram page identified by the audit. Rendering alone adds no inspection credit. [VISUAL_QA.tsv](VISUAL_QA.tsv) records actual page observations against the exact PDF SHA-256; observations for older PDF hashes remain as history. Permitted isolated glyph overhangs are reported separately from text-line, vector or image violations.

### French diplomatic reader

[FR/ESQUISSE_FR_diplomatique.pdf](FR/ESQUISSE_FR_diplomatique.pdf) · [FR/ESQUISSE_FR_diplomatique.tex](FR/ESQUISSE_FR_diplomatique.tex)

EDITION STATUS: partial; source units 67/116.

- PDF SHA-256: `dc82ace53840ab01ebf0226ab2443f3f81f6416b0b232fd24208cbe42ec14bd4`.
- Standalone-source SHA-256: `3c543780d79407b80bdc54c39184957de64e420c6da54437237ba534ba058081`.
- Last recorded compilation: 2026-11-14T19:39:30.846219+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.
- Error: ! File ended while scanning use of \DeclareVariant.
- Error: !  ==> Fatal error occurred, no output PDF file produced!

### French corrected reader

[FR/ESQUISSE_FR_corrige_apparat.pdf](FR/ESQUISSE_FR_corrige_apparat.pdf) · [FR/ESQUISSE_FR_corrige_apparat.tex](FR/ESQUISSE_FR_corrige_apparat.tex)

EDITION STATUS: partial; source units 58/58.

- PDF SHA-256: `51960c8c6fac762060f48bb63100a740a23eb0a5b8daeb2ec1c79dad1c134022`.
- Standalone-source SHA-256: `8be56236df438df3ad601b5ace34502bce6c6de259a489facdd3a84d147456a0`.
- Last recorded compilation: 2026-11-14T19:26:24.059021+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.

### French reading text

[FR/ESQUISSE_FR_texte_de_lecture.pdf](FR/ESQUISSE_FR_texte_de_lecture.pdf) · [FR/ESQUISSE_FR_texte_de_lecture.tex](FR/ESQUISSE_FR_texte_de_lecture.tex)

EDITION STATUS: partial; source units 58/58.

- PDF SHA-256: `049d4d26348b691da3fddef842de6d2e72527ea687d6866c38fe856c83d3056c`.
- Standalone-source SHA-256: `ac689a6cc11f52933b36ab6b27f35ac8053d61fc30346f0f95a914b1ebe0c550`.
- Last recorded compilation: 2026-11-14T19:28:53.368886+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.

### French annotated master

[FR/ESQUISSE_FR_master_annotated.pdf](FR/ESQUISSE_FR_master_annotated.pdf) · [FR/ESQUISSE_FR_master_annotated.tex](FR/ESQUISSE_FR_master_annotated.tex)

EDITION STATUS: partial; source units 58/58.

- PDF SHA-256: `ea6acb9487f08d0fccb5d19406578533dc2c48513ae3ad79769da6f294ba4b44`.
- Standalone-source SHA-256: `9ab222aa5a11135930e6b7007da20d481f53cf8c73315e2a934bcc664ae167b8`.
- Last recorded compilation: 2026-11-14T19:28:04.596809+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.

### English corrected reader

[EN/ESQUISSE_EN_corrected_translator_notes.pdf](EN/ESQUISSE_EN_corrected_translator_notes.pdf) · [EN/ESQUISSE_EN_corrected_translator_notes.tex](EN/ESQUISSE_EN_corrected_translator_notes.tex)

EDITION STATUS: partial; source units 58/58.

- PDF SHA-256: `0e3af459f39c2d599203e985f6120f710eefc020f559151086bceb18f87531a7`.
- Standalone-source SHA-256: `fa2367f4dfca298c3d11a92bb9863cb075c2bdda649c6d72d5f10616db211beb`.
- Last recorded compilation: 2026-11-14T19:39:20.256815+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.
- Error: ! File ended while scanning use of \DeclareVariant.
- Error: !  ==> Fatal error occurred, no output PDF file produced!

### English reading text

[EN/ESQUISSE_EN_reading.pdf](EN/ESQUISSE_EN_reading.pdf) · [EN/ESQUISSE_EN_reading.tex](EN/ESQUISSE_EN_reading.tex)

EDITION STATUS: partial; source units 58/58.

- PDF SHA-256: `4fcd6d809e22ba17d3565961c45d59b062336b5f534ca079cc941d912713782d`.
- Standalone-source SHA-256: `80083e55c93adacedce752e5e2790f9ebb6f816b19199604d0360224b9fa7d8a`.
- Last recorded compilation: 2026-11-14T19:25:41.487442+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.

### English annotated master

[EN/ESQUISSE_EN_master_annotated.pdf](EN/ESQUISSE_EN_master_annotated.pdf) · [EN/ESQUISSE_EN_master_annotated.tex](EN/ESQUISSE_EN_master_annotated.tex)

EDITION STATUS: partial; source units 58/58.

- PDF SHA-256: `6fbe41e33ca7b3687b682276ecdcbd7e3d0bdef02afa1c0523bba1fb5ce67052`.
- Standalone-source SHA-256: `75c2ef7c9843525893569adb41ef21c31d33076f1413654769de3a7862131012`.
- Last recorded compilation: 2026-11-14T19:24:56.724749+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.

### Guide

[GUIDE/ESQUISSE_GUIDE.pdf](GUIDE/ESQUISSE_GUIDE.pdf) · [GUIDE/ESQUISSE_GUIDE.tex](GUIDE/ESQUISSE_GUIDE.tex)

EDITION STATUS: partial; source units 18/18.

- PDF SHA-256: `ff664a12c040456ee3c70fc136055fe8d12ecec0c7a3ffc9b9dce7359d50f6c5`.
- Standalone-source SHA-256: `a1278f1125d5df38062cd1f984bd970fc4e82cf78b598e3aad0676ebc558a8d0`.
- Last recorded compilation: 2026-11-14T19:29:32.568194+00:00.
- Current input projection matches source: no; compiled-source hash matches source: no; final audit matches current PDF and source: no.
- Link targets, printed apparatus, footnote placement and required-page coverage await an audit of the current file.
- Pages with actual observations for this PDF hash: none.

## Release gates

| Gate | Status | Current evidence |
|---|---|---|
| Both supplied manifests verified | PASS | ESQUISSE_TEXT.zip: 143/143; ESQUISSE_SCANS.zip: 232/232 |
| All 116 scan pages explicitly reviewed | OPEN | 69 current finalized review declarations; copy 1 58/58, copy 2 11/58 |
| All 468 original differences decided | OPEN | 365/468 unique outcome rows |
| All 58 page pairs collated against current files | OPEN | 11/58 pair declarations; recorded hashes current: yes |
| Complete source and editorial validator current | OPEN | validator status: in progress; snapshot current: no |
| Complete English translation and exact formula index current | PASS | 58/58 pages; 519 math fragments and 1 complete diagram; index current: yes |
| French IDs aligned with the English apparatus | PASS | 46 French IDs; 1 English wording variants and 45 French-source notes |
| Guide units and completed collation preface present | OPEN | 18/18 commentary units; completed collation preface: no |
| No unintegrated mechanical TeX repairs | PASS | 0 current projection repairs awaiting integration |
| All standalone sources regenerated from current inputs | OPEN | 0/8 files match the generator's current projection |
| Six reader/guide PDFs pass recorded build, links and visual QA | OPEN | 0/6 pass all current-hash checks |
| Release status explicitly final | OPEN | RELEASE_STATUS.json final: no |

This README never changes `RELEASE_STATUS.json` and never supplies missing review observations. Final release status must agree with completed source validation, current generated files, successful PDF audits and recorded visual inspection. Changing any source or macro can change a PDF hash and therefore requires the corresponding fresh PDF audit and visual record.

## Reproducible compilation and full rebuild

### Compile one standalone document

Use a working TeX Live installation with LuaLaTeX, Latin Modern, French and English babel support, fontspec, amsmath/amssymb, ulem, xcolor, graphicx, TikZ/tikz-cd, marginnote, etoolbox, microtype and hyperref. From the combined edition root, the following example runs three passes for stable cross-references:

```sh
cd EN
lualatex -interaction=nonstopmode -halt-on-error -file-line-error ESQUISSE_EN_reading.tex
lualatex -interaction=nonstopmode -halt-on-error -file-line-error ESQUISSE_EN_reading.tex
lualatex -interaction=nonstopmode -halt-on-error -file-line-error ESQUISSE_EN_reading.tex
cd ..
```

Substitute another .tex filename in FR/, EN/ or GUIDE/ to compile that document. Each source embeds its required edition macros and source-glyph contour; it has no external page-file or image dependency. A new TeX environment can change pagination or PDF bytes, so a locally rebuilt PDF needs its own recorded audit and visual inspection.

### Regenerate all forms from the review records

Python 3 is required for generation and record processing. PyMuPDF is required for PDF link and geometry measurements; Pillow is used for the rendered review sheets. The optional source-glyph tracing helper also uses NumPy and Matplotlib. With all three delivery archives combined in work/edition and the inputs extracted as above, run from that edition root:

```sh
python scripts/audit_validate.py --complete
python translated_pages/attach_fr_apparatus.py
python translated_pages/refresh_index.py
python scripts/build_edition.py generate
python scripts/compile_readers.py --passes 3
python scripts/pdf_final_audit.py --render
```

The complete validator intentionally reports failure while any of the 116 pages, 468 differences or 58 page pairs remains unchecked. Without `--complete`, it validates the current reviewed subset and records its incomplete scope. The generation command refreshes annotated pages, both masters, every reader, the guide, coverage tables, variant register, note links and apparatus counts. The compiler writes sanitized logs and measured results; `--names` selects particular document stems. The final-audit command compares projected scan/doubt links, apparatus IDs, authorial note links, physical note placement and required visual-page coverage.

Open and inspect the rendered page images before recording observations. The locking helper accepts a JSON list containing `reader`, `pdf_sha256`, `pdf_page`, `observation` and `phase`. It rejects an observation when the PDF hash has changed. With actual observations saved in records/visual_observations.json, the remaining commands are:

```sh
python scripts/record_visual_qa.py records/visual_observations.json
python scripts/pdf_final_audit.py
python scripts/write_readme.py
```

The execution environment used an isolated support tree because its installed TeX file databases, font support and French files were incomplete. That fallback is documented in [scripts/ENVIRONMENT.md](scripts/ENVIRONMENT.md) and [scripts/bootstrap_tex.py](scripts/bootstrap_tex.py). On a standard working TeX Live installation it is unnecessary. To reproduce that fallback from the edition root, run `python scripts/bootstrap_tex.py ../tex-runtime` before the compile command. The helper downloads its explicitly listed archived TeX Live packages into the private runtime directory and does not alter the system installation.

Standalone compilation and regeneration preserve source strings. Syntax-only repairs, such as removing redundant nested math delimiters or using TikZ's ampersand replacement inside the diagram macro, have exact before/after records. `scripts/apply_mechanical_cleanup.py` is the controlled integration helper for such already-defined repairs; it records hash transitions and history. It is not a spelling or mathematical correction operation. The source review records and original attachments are required to replay their validation.

## Record and helper inventory

| Path | Role |
|---|---|
| CHECK_DECISIONS.tsv; reviews/; reviews/history/ | Every explicit scan decision, complete-page declaration and superseded observation. |
| DIFFERENCES_OUTCOMES.tsv | Every original draft/transcription difference retained with its final scan outcome and stable decision links. |
| COLLATION.tsv; collation_reviews/; records/COLLATION_PAGE_COVERAGE.tsv | Both readings at each collated locus, full four-image declarations and current checked-source hashes. |
| records/COLLATION_COMMON_MARKS.tsv | Shared-handwriting rows reproduced from the complete collation. |
| editorial_variants.json; records/EDITORIAL_CANDIDATES.tsv; records/EDITORIAL_ADJUDICATIONS.tsv | Approved corrections, their candidate evidence, and explicit correction/retention decisions. |
| copy2_annotations.json | Bilingual copy 2 apparatus text and links, including records merged into a shared correction. |
| checked_pages/; annotated_pages/ | Checked diplomatic source files and the generated variant-bearing versions. |
| translated_pages/; guide_fragments/ | Complete English page translations, translator review history, math index, apparatus alignment and ordered guide prose. |
| VARIANTS.json; CHANGES.tsv; APPARATUS_COUNTS.md | Generated variant register, old/new readings, stable IDs, reasons and counts by language/form/kind. |
| SOURCE_COVERAGE.tsv; TRANSLATION_COVERAGE.tsv; NOTE_LINKS.json | Source hash recovery, literal math comparison, and every authorial endnote definition/call/return. |
| CLEANUP_LOG.tsv; MECHANICAL_CLEANUP.json; REVIEW_STAGE_CLEANUP.json; records/MECHANICAL_PATCHES.json | Exact syntax-only repairs and their source IDs, replay order and hash transitions. |
| TYPESETTING_FIXES.tsv; TYPESETTING_REPORT.md | Source locations, reasons and measured outcomes of typography repairs and PDF validation. |
| BUILD_INPUTS.json; BUILD_HISTORY.jsonl; PDF_CHECKS.json; build_logs/ | Actual generation scope, compilation history, sanitized logs and measured PDF properties. |
| FINAL_PDF_AUDIT.json; VISUAL_QA.tsv | Exact-PDF link/apparatus/geometry and required-page audits, plus actual human/model visual observations. |
| records/INDEPENDENT_TEXT_REVIEW.tsv; records/SECOND_READINGS.tsv | Independent FR/EN/guide reading and targeted visual comparisons, with hashes and observations. |
| records/SOURCE_INTEGRITY.json; records/SOURCE_PAGE_INVENTORY.tsv; records/PAGE_MAP.tsv; packets/ | Manifest integrity, complete inventories, archive coordinates and source-review packets. |
| records/SOURCE_GLYPHS.md; records/SOURCE_GLYPH_119A.json; glyphs/ | Observed special-glyph provenance, vector transformations and inspected rendering probes. |
| scripts/; templates/ | Reproducible review, collation, generation, compilation, audit and rendering code plus reusable TeX definitions. |
| records/CHECKPOINTS.tsv; records/OMITTED_CHECKPOINT_FILES.tsv | Earlier checkpoint identities and explicit reconciliation of files not repeated in the final archives. |

The records ZIP retains the authored review history and reproducibility files. Unmodified input-table duplicates removed from earlier checkpoints are identified in [records/OMITTED_CHECKPOINT_FILES.tsv](records/OMITTED_CHECKPOINT_FILES.tsv) with their original archive location and reason. Runtime downloads, font caches, temporary TeX outputs and duplicate intermediate diagnostic renderings are reproducible intermediates; they are excluded from publication while sanitized logs, source hashes, measured results and actual review observations are retained. The diagnostic build baseline is recorded in [ORIGINAL_BUILD_BASELINE.json](ORIGINAL_BUILD_BASELINE.json); its unchecked PDFs are not readers.

## Credits and rights

AI-transcribed by Claude Opus 5.5 (Anthropic, effort high, Message Batches API); checked against the scans, and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic). AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

The transcription of copy 1 was made with the text layer of the Grothendieck Circle's typeset *Esquisse* (`EsquisseFr.pdf`) given to the transcribing model as a draft, to compare with after it had transcribed each page; every reading of this edition was decided on the scans.

The published French text and English translation in *Geometric Galois Actions 1*, edited by L. Schneps and P. Lochak (Cambridge University Press, 1997), the Grothendieck Circle's typeset `EsquisseFr.pdf`, and the Centre for Grothendieckian Studies' draft transcription G94d are named as published texts. They are not reproduced here.

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.
