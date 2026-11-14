# Nouveau EGA V: checked texts, readers, translation and guide

Status: **PASS: all release gates passed**. Documentary counts generated 2026-11-14T23:09:49.420121+00:00.

The checked source comprises 260 pages: 184 from cote 25 and 76 from cote 24. CHECK_DECISIONS.tsv contains 12,368 decision rows. The new English translation has 184 recorded source pages. The guide manifest contains 31 prose parts.

Alexandre Grothendieck, *Nouveau EGA V*, Université de Montpellier, fonds Grothendieck, cote 25; and Piotr Blass's 1987 translation typescript, cote 24. Edition dated 14 November 2026. The archive describes cote 25 as '[à partir de 1967-1987]'.

## The three packages

EGA_V_READERS_FR.zip contains the three French forms, their annotated master and the guide. EGA_V_READERS_EN.zip contains the two new English forms, their annotated master, the three Blass forms, the Blass annotated master and the guide. Each named work is supplied as a standalone .tex file and a PDF. The guide and this README are repeated in both language packages. There are twelve distinct PDF editions in total.

EGA_V_READERS_RECORDS.zip contains the checked pages, intermediate source representations, decision records, manifests, page observations, full-page PDF review images, build scripts and their documentary outputs. Its root is the edition directory referred to by the scripts. The supplied scans and original input archives remain the sources of record and are not duplicated in these packages.

| File stem (.tex and .pdf) | Contents | Package |
|---|---|---|
| EGA_V_FR_diplomatique | French diplomatic reader | FR |
| EGA_V_FR_corrige_apparat | French corrected reader with apparatus | FR |
| EGA_V_FR_texte_de_lecture | French reading text | FR |
| EGA_V_FR_master_annotated | French annotated master | FR |
| EGA_V_EN_corrected_translator_notes | New English translation with apparatus and translator's notes | EN |
| EGA_V_EN_reading | New English reading text | EN |
| EGA_V_EN_master_annotated | New English annotated master | EN |
| EGA_V24_EN_diplomatic | Piotr Blass diplomatic reader | EN |
| EGA_V24_EN_corrected_apparatus | Piotr Blass corrected reader with apparatus | EN |
| EGA_V24_EN_reading | Piotr Blass reading text | EN |
| EGA_V24_EN_master_annotated | Piotr Blass annotated master | EN |
| EGA_V_GUIDE | English prose guide | FR and EN |

## Source and reading order

The French diplomatic volume follows cote 25 sites 1–184 in archive order. The corrected and reading volumes, their annotated master, and the new English volumes use this exact site order: 139–157, 158–184, 1–96, 97–133, 136–138, 134–135. This places IV 16, IV 17.15–17.16, IV 20 and IV 21 in numerical order, retains the interleaved leaves, and ends with the letter to Dieudonné.

The Blass diplomatic volume contains sites 1–76 in archive order. The corrected, reading and annotated-master PDFs contain sites 1–75. The handwritten French note at site 75 retains its language. The curriculum-vitae leaf at site 76 is marked as a stray sheet in the diplomatic volume; its checked page remains in checked_pages/. Blass's gaps, queries, English wording and notation remain in his text. CHECK_DECISIONS.tsv and the guide identify the checked French passages corresponding to his queries and gaps.

## How the texts were established

Both supplied manifests were checked against file sizes and SHA-256 hashes: 803 entries. Each source page was compared line by line with both supplied image halves, including unmarked typed text, formulas, indices, arrows, handwriting, cancellations and margins. PAGES_CHECKED.tsv records the start and end times and the number of decision rows. Its lines_read field counts nonblank lines in the checked LaTeX source, excluding comments and scan markers; it is not a count of physical manuscript baselines. The per-page review records preserve the definition and observations.

The checked_pages/ files retain the supplied editorial macro vocabulary. A changed reading or physical-layer classification has a decision record. Remaining uncertainty stays in the source. A lower or higher count of doubt macros alone does not measure resolved readings: the review also split marks, expanded candidates, recovered canceled wording and introduced doubts where the original transcription was too definite.

Mechanical cleanup has 385 recorded operations in CLEANUP_LOG.tsv. It repairs TeX syntax and encodings while retaining the visible reading. cleaned_pages/ is that intermediate representation. master_pages/fr/ and master_pages/blass/ attach a stable source ID and a kind to every editorial difference; variant_records/ and CHANGES.tsv preserve the page reading, corrected reading and reason. CHANGES.tsv contains 3,009 entries. Resolving the diplomatic branch must reproduce the cleaned page exactly.

The corrected branch incorporates the author's insertions and replacements, places marginal notes, and retains deleted or struck text in its apparatus. The reading form selects the same corrected branch and omits the apparatus reference marks. Source doubts and marginal notes remain. The author-directed transfer from cote 25 site 21 to site 22 is recorded in AUTHOR_RESTORATIONS.tsv: the donor text and its variants are retained and the reproduced passage links back to its donor scan.

French spelling, abbreviations and notation remain those of the checked page, including préschéma, Module, systême, loc, rel, resp., sss and cqfd where written. The records preserve the particular source form. A mathematical discrepancy is discussed in the relevant guide paragraph; it supplies no unrecorded correction to the text.

The disputed mark at cote 25 site 140 is recorded as the scan-supported handwritten comma after k. The later paired-glyph review of cote 24 revises several earlier baseline/subscript judgments; VISUAL_DECISION_SUPERSESSIONS.tsv identifies those superseded decisions. Earlier checkpoint versions remain separately accounted for.

## New English translation

There are 184 recorded translations out of 184 source pages. The English master contains 197 translator-note macros; 100 further variant-specific translation notes and 227 documented French-only variant omissions are recorded separately. Their counts have different units and should not be added as a single note total.

The supplied unified SGA glossary governs the new English and editorial prose. Translation notes explain source abbreviations, puns, uncertain letterforms and grammatical repairs. Source explanations remain in the source's running text; new explanations are placed in notes. A French physical correction with identical English outcomes can have its variant omitted only with an explicit entry in EN_VARIANT_OMISSIONS.tsv.

The validator compares every mathematical token string in both the page-reading and corrected branches of each French/English master pair. It also checks the ordered variant IDs, documented omissions, numerals outside explicit math, live uncertainty and illegibility counts, and hashes of the checked page and both masters. The restored site-21 passage in site 22 is checked against its donor translation. TRANSLATION_FORMULA_AUDIT.tsv, EN_TRANSLATION_STATUS.tsv and EN_TRANSLATION_HISTORY.tsv retain these results.

## Counts from the checked sources

These are macro occurrences in the original and checked page files, before reader selection and repeated apparatus quotations. Each illegible macro is one mark even when its argument denotes several unreadable words.

| Cote | Pages counted | Macro | Before | After |
|---|---|---|---|---|
| 25 | 184 | unsure | 1234 | 1610 |
| 25 | 184 | illegible | 231 | 176 |
| 25 | 184 | hand | 1673 | 3533 |
| 25 | 184 | over | 211 | 251 |
| 25 | 184 | inserted | 769 | 791 |
| 25 | 184 | margin | 235 | 244 |
| 25 | 184 | deleted | 479 | 488 |
| 25 | 184 | xout | 1210 | 1183 |
| 25 | 184 | uline | 483 | 514 |
| 25 | 184 | uuline | 2 | 5 |
| 25 | 184 | scanpage | 184 | 184 |
| 25 | 184 | mspage | 279 | 297 |
| 25 | 184 | diagram | 14 | 15 |
| 24 | 76 | unsure | 26 | 32 |
| 24 | 76 | illegible | 0 | 4 |
| 24 | 76 | hand | 44 | 63 |
| 24 | 76 | over | 1 | 2 |
| 24 | 76 | inserted | 1 | 1 |
| 24 | 76 | margin | 48 | 48 |
| 24 | 76 | deleted | 0 | 0 |
| 24 | 76 | xout | 0 | 0 |
| 24 | 76 | uline | 183 | 183 |
| 24 | 76 | uuline | 0 | 0 |
| 24 | 76 | scanpage | 76 | 76 |
| 24 | 76 | mspage | 76 | 76 |
| 24 | 76 | diagram | 2 | 2 |

### Decision outcomes

The labels below are the exact decision values in CHECK_DECISIONS.tsv. Composite labels remain composite and each row is counted once. Superseded decisions remain in the history and are identified in the supersession records.

| Recorded outcome | Rows |
|---|---|
| confirmed | 3168 |
| reviewed | 2447 |
| corrected_from_scan | 2348 |
| corrected | 1334 |
| corrected-layer | 469 |
| retained_uncertain | 288 |
| retained-uncertain | 244 |
| corrected-reading | 243 |
| doubt-retained | 235 |
| layer-confirmed;reading-unresolved | 143 |
| comparison-recorded | 142 |
| checked | 130 |
| doubt-resolved | 119 |
| retained_query_with_french_crossreference | 119 |
| revised-with-uncertainty | 58 |
| unresolved | 56 |
| comparison_note | 54 |
| restored | 54 |
| cross-reference | 46 |
| notation-placement-corrected | 44 |
| retained_illegible | 41 |
| doubt-refined | 38 |
| retained | 38 |
| superseded-after-enlargement | 38 |
| index-placement-restored | 37 |
| confirmed_after_paired_glyph_review | 35 |
| doubt-added | 34 |
| preserved | 23 |
| confirmed_query_with_french_crossreference | 20 |
| recovered-cancelled-reading | 17 |
| corrected-reading-and-layer | 16 |
| doubt-resolved;corrected-layer | 14 |
| corrected_placement | 13 |
| corrected-placement | 11 |
| retained_gap_with_french_crossreference | 8 |
| Retain checked reading after focused scan follow-up | 7 |
| partly-recovered-cancelled-reading | 7 |
| corrected-reading;doubt-refined | 6 |
| corrected_after_focused_placement_review | 6 |
| observed | 6 |
| recovered-reading | 6 |
| review-revised | 6 |
| doubt-refined;corrected-layer | 5 |
| layer-doubt-added | 5 |
| confirmed-after-encoding-repair | 4 |
| corrected-alphabet | 4 |
| corrected-layer;doubt-added | 4 |
| doubt-resolved;corrected-reading | 4 |
| index-placement-corrected | 4 |
| recovered-underlying-reading | 4 |
| added-omission | 3 |
| added-reading | 3 |
| corrected-layer;doubt-refined | 3 |
| corrected-layer;mechanical-encoding | 3 |
| corrected-reading;doubt-resolved | 3 |
| description-to-note | 3 |
| illegible-resolved | 3 |
| partial-recovery | 3 |
| recovered-reading;doubt-added | 3 |
| removed-duplicated-placement-mark | 3 |
| retained_gloss_with_french_crossreference | 3 |
| Amend checked text with localized uncertainty | 2 |
| added-layer | 2 |
| corrected-attachment | 2 |
| corrected-deletion;doubt-resolved | 2 |
| corrected-encoding;doubt-added | 2 |
| corrected-index | 2 |
| corrected-layer-after-reread | 2 |
| corrected-layer;doubt-retained | 2 |
| corrected-letterform-and-layer | 2 |
| corrected-reading;corrected-layer | 2 |
| corrected-reading;doubt-added | 2 |
| corrected-reading;doubt-retained | 2 |
| corrected-spacing | 2 |
| corrected-uncertainty-encoding | 2 |
| doubt-added;corrected-reading | 2 |
| encoding_adjusted | 2 |
| gap-marked | 2 |
| graphic-mark-recorded | 2 |
| letterform-corrected | 2 |
| mechanical-encoding-repair | 2 |
| moved-physical-mark-to-note | 2 |
| moved-to-indicated-position | 2 |
| partly-recovered | 2 |
| partly-recovered-handwriting | 2 |
| recovered-handwritten-mark | 2 |
| recovered-reading;unresolved-gaps | 2 |
| retained-uncertainty | 2 |
| retained_uncertainty | 2 |
| Preserve localized n/h overprint uncertainty | 1 |
| Retain checked visible endings | 1 |
| added-handwriting | 1 |
| added-reading;doubt-refined | 1 |
| added-underlining | 1 |
| candidate-added | 1 |
| candidates-revised | 1 |
| corrected-abbreviation | 1 |
| corrected-cancellation-layer | 1 |
| corrected-cancellation;doubt-refined | 1 |
| corrected-deletion | 1 |
| corrected-deletion-boundary | 1 |
| corrected-deletion;corrected-reading | 1 |
| corrected-diagram-placement | 1 |
| corrected-diagram-script-level | 1 |
| corrected-layer-and-scope | 1 |
| corrected-layer;added-physical-mark | 1 |
| corrected-layer;corrected-reading | 1 |
| corrected-layer;doubt-resolved | 1 |
| corrected-layer;removed-spurious-check | 1 |
| corrected-mark | 1 |
| corrected-mark;description-to-comment | 1 |
| corrected-placement-and-layer | 1 |
| corrected-placement;corrected-layer | 1 |
| corrected-placement;corrected-physical-mark | 1 |
| corrected-placement;doubt-resolved | 1 |
| corrected-placement;layer-unresolved | 1 |
| corrected-placement;removed-noncontent | 1 |
| corrected-reading;partly-resolved | 1 |
| doubt-added;layer-unresolved | 1 |
| doubt-expanded | 1 |
| doubt-refined;layer-unsettled | 1 |
| doubt-resolved;added-reading | 1 |
| doubt-resolved;attachment-unsettled | 1 |
| doubt-resolved;corrected-layer;corrected-cancellation | 1 |
| doubt-resolved;corrected-placement | 1 |
| doubt-resolved;recovered-handwritten-mark | 1 |
| doubt-resolved;recovered-margin | 1 |
| doubt-resolved;recovered-text | 1 |
| doubt-restored | 1 |
| extended-cancellation | 1 |
| gaps-marked | 1 |
| handwritten-layer-restored | 1 |
| layer-doubt-refined | 1 |
| layer-unresolved | 1 |
| layout-encoding-corrected | 1 |
| moved-description-to-note | 1 |
| partial-recovery;doubt-added | 1 |
| partly-recovered-reading | 1 |
| partly-resolved-reading | 1 |
| partly-unresolved | 1 |
| recovered-cancelled-layer | 1 |
| recovered-cancelled-reading;corrected-layer | 1 |
| recovered-cancelled-reading;corrected-mark | 1 |
| recovered-editorial-mark | 1 |
| recovered-index;corrected-layer | 1 |
| recovered-reading;corrected-formula-placement | 1 |
| recovered-reading;corrected-placement | 1 |
| recovered-word | 1 |
| removed-duplicated-cancellation-mark | 1 |
| removed-duplicated-mark | 1 |
| removed-noncontent | 1 |
| removed-spurious-mark | 1 |
| removed-spurious-overwrite | 1 |
| resolved-from-image | 1 |
| retained_blank_with_french_crossreference | 1 |
| retained_ellipsis_with_french_crossreference | 1 |
| retained_instruction_with_french_crossreference | 1 |
| retained_reference_gloss_with_french_crossreference | 1 |
| retained_reference_with_french_crossreference | 1 |
| retained_uncertainty_with_french_crossreference | 1 |
| settled-comma | 1 |
| superseded-after-reread | 1 |
| superseding-doubt-restoration | 1 |
| superseding-layer-correction | 1 |
| typesetting-recorded | 1 |
| unresolved-mark | 1 |

### Apparatus entries

Counts are per printed form. Nested physical corrections retain separate IDs. The diplomatic and reading forms print no apparatus entries. APPARATUS_COUNTS.md gives the per-kind counts for each volume.

| Volume | Source pages | Printed apparatus entries |
|---|---|---|
| EGA_V_FR_diplomatique | 184 | 0 |
| EGA_V_FR_corrige_apparat | 184 | 2958 |
| EGA_V_FR_texte_de_lecture | 184 | 0 |
| EGA_V_FR_master_annotated | 184 | 2958 |
| EGA_V_EN_corrected_translator_notes | 184 | 2732 |
| EGA_V_EN_reading | 184 | 0 |
| EGA_V_EN_master_annotated | 184 | 2732 |
| EGA_V24_EN_diplomatic | 76 | 0 |
| EGA_V24_EN_corrected_apparatus | 75 | 47 |
| EGA_V24_EN_reading | 75 | 0 |
| EGA_V24_EN_master_annotated | 75 | 47 |

## Compilation, links and visual review

TYPESETTING_FIXES.tsv contains 1,803 reader-specific repair records. Local repairs are applied to the generated page payloads and are recorded with their source location; the common mathematical master remains available for the translation token checks. LOCAL_DIAGRAM_SCALE_AUDIT.tsv records the measured local scaling. Every resulting PDF has its own compile report, source and PDF hashes, historical overflow list, link inventory and visual observations.

The table reports the final log for each current PDF. The warning count includes warning messages collected by the compiler, separately from overfull boxes and missing glyphs. TYPESETTING_REPORT.md preserves the before/after compile history and every recorded page observation.

| PDF | Pages | Errors | Warnings | Missing glyphs | Overfull boxes | Widest (pt) | Over 2 pt | Required / passed views |
|---|---|---|---|---|---|---|---|---|
| EGA_V_FR_diplomatique | 187 | 0 | 15 | 0 | 1 | 1.85934 | 0 | 53 / 53 |
| EGA_V_FR_corrige_apparat | 426 | 0 | 15 | 0 | 1 | 1.07368 | 0 | 73 / 73 |
| EGA_V_FR_texte_de_lecture | 187 | 0 | 50 | 0 | 0 | 0.00000 | 0 | 54 / 54 |
| EGA_V_FR_master_annotated | 426 | 0 | 15 | 0 | 1 | 1.07368 | 0 | 73 / 73 |
| EGA_V_EN_corrected_translator_notes | 424 | 0 | 18 | 0 | 0 | 0.00000 | 0 | 123 / 123 |
| EGA_V_EN_reading | 187 | 0 | 55 | 0 | 0 | 0.00000 | 0 | 71 / 71 |
| EGA_V_EN_master_annotated | 424 | 0 | 18 | 0 | 0 | 0.00000 | 0 | 123 / 123 |
| EGA_V24_EN_diplomatic | 80 | 0 | 3 | 0 | 0 | 0.00000 | 0 | 49 / 49 |
| EGA_V24_EN_corrected_apparatus | 78 | 0 | 2 | 0 | 0 | 0.00000 | 0 | 48 / 48 |
| EGA_V24_EN_reading | 78 | 0 | 3 | 0 | 0 | 0.00000 | 0 | 48 / 48 |
| EGA_V24_EN_master_annotated | 78 | 0 | 2 | 0 | 0 | 0.00000 | 0 | 48 / 48 |
| EGA_V_GUIDE | 25 | 0 | 0 | 0 | 0 | 0.00000 | 0 | 25 / 25 |

Every source-page scan marker and every printed uncertainty/illegibility mark has an archive link. Named logical destinations let the audit compare source-mark counts with the PDF and test the actual URI near each individual mark. Archive PDF pages equal site numbers plus one. A linked word or phrase can wrap across multiple PDF annotations, so the logical mark count and annotation count are reported separately.

| PDF | Logical scan | Logical unsure | Logical illegible | Provenance | All annotations | Archive annotations | Distinct archive pages |
|---|---|---|---|---|---|---|---|
| EGA_V_FR_diplomatique | 184 | 1610 | 176 | 0 | 2056 | 2056 | {"25": 184} |
| EGA_V_FR_corrige_apparat | 184 | 2063 | 247 | 2 | 5315 | 2560 | {"25": 184} |
| EGA_V_FR_texte_de_lecture | 184 | 1166 | 32 | 1 | 1447 | 1447 | {"25": 184} |
| EGA_V_FR_master_annotated | 184 | 2063 | 247 | 2 | 5315 | 2560 | {"25": 184} |
| EGA_V_EN_corrected_translator_notes | 184 | 2028 | 247 | 2 | 5265 | 2526 | {"25": 184} |
| EGA_V_EN_reading | 184 | 1166 | 32 | 1 | 1453 | 1453 | {"25": 184} |
| EGA_V_EN_master_annotated | 184 | 2028 | 247 | 2 | 5265 | 2526 | {"25": 184} |
| EGA_V24_EN_diplomatic | 76 | 32 | 4 | 0 | 112 | 112 | {"24": 76} |
| EGA_V24_EN_corrected_apparatus | 75 | 40 | 4 | 0 | 166 | 119 | {"24": 75} |
| EGA_V24_EN_reading | 75 | 32 | 4 | 0 | 111 | 111 | {"24": 75} |
| EGA_V24_EN_master_annotated | 75 | 40 | 4 | 0 | 166 | 119 | {"24": 75} |
| EGA_V_GUIDE | 0 | 0 | 0 | 0 | 130 | 123 | {"24": 15, "25": 78} |

For each PDF, the required visual set includes forty evenly spread pages (every page for a shorter work), all landscape pages, the final page ranges corresponding to historical overflows and local repairs, and all current text, vector and image geometry flags. A successful page observation is tied to the exact PDF SHA-256 and rendered-image SHA-256. Reuse of a previously viewed complete page requires byte-for-byte identity of its newly rendered PNG with the actually viewed image; PDF_VISUAL_EQUIVALENCE.tsv records both PDF hashes, both page numbers, the common image hash and the originating inspection. Every differing required image is inspected separately. PDF_GEOMETRY_REVIEW.tsv records the explicit visual disposition of each permitted single-letter overhang or conservative graphics bound. A real overflow or overlap requires a source repair and review of the changed page.

Marginal-note placement uses the number of actual packed lines measured by LuaTeX. A note of at most three lines remains in the margin; a longer note appears as a labeled, ruled block at its attachment. MARGIN_LINE_AUDIT.tsv records the measured routes, and the PDF audit verifies that every queued marginal note and its attachment remain on the same physical page. The earlier height-only test admitted notes that occupied four lines and was replaced; those repairs and their superseded PDF observations remain documented.

## Documentary file map

| Path | Purpose |
|---|---|
| checked_pages/ | All 260 checked diplomatic page sources. |
| CHECK_DECISIONS.tsv; PAGES_CHECKED.tsv | Reading decisions and completed page-review records. |
| CHANGES.tsv; APPARATUS_COUNTS.md | Every corrected/diplomatic difference, with kind and reason; counts by form. |
| CLEANUP_LOG.tsv; TYPESETTING_FIXES.tsv | Mechanical TeX cleanup and local layout repairs. |
| TYPESETTING_REPORT.md | PDF log results, geometry, link counts and actual visual findings. |
| records/BUILD_REPORT_PROVENANCE.json | Input and output hashes for the cumulative reports; the release gate rejects stale report evidence. |
| cleaned_pages/; corrected_pages/; master_pages/; variant_records/ | Reproducible intermediate source representations and variants. |
| readers/ | Current standalone reader, master and guide TeX sources. |
| guide_parts/; records/GUIDE_PARTS.tsv | The guide's prose and section manifest. |
| records/NOTES_COVERAGE.tsv | Per-item cross-references from the supplied NOTES.tsv concerns to the decisions. |
| records/EN_*.tsv; records/TRANSLATION_FORMULA_AUDIT.tsv | Translation coverage, source hashes, variant explanations and token comparisons. |
| records/PDF_*.tsv; build/visual_review/ | PDF freezes, actual inspection records, geometry dispositions, images and image manifests. |
| build/*/audit/; build/*/*.log | Compile reports, sanitized logs, overfull-box history and individual PDF link audits. |
| review_work/ | Per-page review records, comparison notes and retained work documentation. |
| scripts/ | Build, checking, reporting, checkpoint and packaging programs. |
| records/CHECKPOINT_CATALOG.tsv; records/CHECKPOINT_MEMBER_ACCOUNT.tsv | Immutable checkpoint catalogue and the disposition of every earlier file version. |
| records/RELEASE_AUDIT.json; records/RELEASE_AUDIT.md | The final release gates and their evidence. |
| records/FINAL_FILE_MANIFEST.tsv | Package-member byte counts and SHA-256 hashes; the manifest excludes its own self-hash. |

## Rebuilding

Each supplied reader .tex is self-contained and compiles with LuaLaTeX in a standard TeX Live installation. Run LuaLaTeX twice to settle page references. The sources use Latin Modern fonts and the standard packages fontspec, babel (English/French), geometry, amsmath, amssymb, mathtools, newunicodechar, xcolor, tikz-cd, lua-ul, marginnote, fancyhdr, pdflscape, microtype and hyperref.

To regenerate the edition, extract the records ZIP into a directory named edition and the supplied EGA_V_TEXT.zip into its sibling source directory. For scan-based reinspection, extract EGA_V_SCANS.zip into the sibling scan_source directory. Python 3, PyMuPDF and pypdf support the build audits; LuaLaTeX supplies the typesetting. Commands are run from the parent of edition:

```sh
python edition/scripts/build_readers.py build --family all
python edition/scripts/build_guide.py
python edition/scripts/compile_readers.py edition/readers/*.tex
python edition/scripts/generate_build_reports.py
python edition/scripts/audit_release.py
python edition/scripts/generate_readme.py
```

The preserved PDF freeze ledger intentionally prevents an accidental overwrite of a reviewed edition. A deliberate rebuild must first release the affected reader with pdf_review.py release and a concrete reason. New PDF bytes require their own freeze, rendered pages and explicit page observations; commands and the observation schema are in records/PDF_REVIEW_WORKFLOW.md. The release audit remains blocked until those requirements are fulfilled. Earlier review evidence remains in the ledger.

Historical audit scripts document how the checked pages were established. Rebuilding the readers uses the checked_pages/ sources directly; it does not replay earlier reading decisions. In particular, the paired-glyph supersession record controls the later cote-24 index decisions.

## Checkpoints and retained history

CHECKPOINT_CATALOG.tsv identifies every numbered, immutable checkpoint by bytes, SHA-256 and saved-file identity. CHECKPOINT_MEMBER_ACCOUNT.tsv gives one row for every member of every checkpoint: original member path and SHA-256, retained destination or replacement path and hash, and the reason for supersession or omission. The final packages retain current deliverables and documentary work. Earlier development PDFs and TeX auxiliary products are accounted for individually; they are not included among the published PDFs.

## Credits and rights

AI-transcribed by Claude Opus 5.5 (Anthropic, effort high, Message Batches API); checked against the scans, and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic).

AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

The translation in cote 24 is Piotr Blass's (1987); the rights in it belong to its translator or his heirs.

The Grothendieck Circle scan EGA5.pdf, the P. and J. Blass translations (2004), J. C. Reinhold's web re-edition and the Centre for Grothendieckian Studies item L49d are named as published texts. They are not reproduced and were not consulted for any reading. Published EGA IV is cited in the guide by numbered results, with the verification method and limits recorded in records/PUBLISHED_REFERENCE_METHOD.md.

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.

Les droits sur l'œuvre originale appartiennent à son auteur, à ses représentants ou à ses ayants droit. Dans la mesure où nous détenons des droits sur la transcription, la traduction, les corrections et la composition produites par l'IA, nous les consacrons au domaine public sous CC0 1.0. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons aucun droit que nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez ouvrir une issue GitHub et nous la retirerons.
