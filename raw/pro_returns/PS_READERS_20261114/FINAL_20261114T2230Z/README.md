# Pursuing Stacks — complete checked English readers

Alexander Grothendieck, *Pursuing Stacks* (1983), with R. Brown's appendix translation. The primary witness is the supplied Université de Montpellier archive typescript, cotes 134-2–134-8. All 706 source pages (680 main-work pages and 26 Brown pages) have recorded inspection of both supplied image halves.

## Deliverables

`PS_READERS_EN.zip` contains five standalone LuaLaTeX sources and their PDFs: the diplomatic reader, corrected reader with apparatus, reading text, annotated master, and guide. `PS_READERS_RECORDS.zip` contains all 706 `checked_pages/` files, decision and concordance tables, variant and typesetting records, build and verification scripts, logs, review notes, proof images and final visual-QA evidence. Paths in the records are relative to that records package; `readers/` refers to the corresponding files in the English package.

### Extraction and duplicate-image aliases

Extract both packages into one working directory while preserving their folder structure. Each distinct image byte sequence is stored once. `records/FILE_ALIASES.tsv` identifies every omitted duplicate-image path, its retained identical image and the SHA-256 of those bytes. The complete set of logical proof paths is therefore recoverable without changing any image content or resolution.

Before running the record or proof-verification scripts, restore those duplicate paths from the extracted project directory:

```sh
python3 scripts/restore_file_aliases.py
```

The restoration script verifies the retained bytes against the alias manifest before recreating each duplicate path. Preserve the manifest with the records. All core sources, PDFs and records are physical archive members; the alias mechanism applies to duplicate images.

### Explicit supersession of intermediate PDFs

The final packages contain only the five published PDFs under `readers/`. `records/FINAL_OMISSIONS.tsv` explicitly supersedes 59 intermediate PDFs, including cote builds, diagnostic excerpts, clean isolated proofs and complete predecessor PDFs. Each row gives the exact old path, byte count and SHA-256, the final-reader replacement and its SHA-256, and the reason. Workspace files and immutable checkpoints are preserved. Intermediate TeX, logs, actually-viewed PNGs, observations and provenance records remain in the delivery.

Before packaging, the full workspace gate verifies the retained old PDF bytes and geometry. In an extracted delivery those explicitly superseded PDFs are absent. After restoring image aliases, verify that delivery without rewriting its archived gate record by running:

```sh
python3 scripts/final_qa_gate.py --allow-omitted-historical-pdfs --check-only
```

This mode requires an exact omission row and validates the preserved original observation, old PNG hash, equivalence-audit hash and final replacement hash. It freshly renders the current page at the original image scale and at 144 dpi, requiring equality with the preserved old PNG and audited current signatures. An old PDF that is present is always verified normally. The verification scripts import PyMuPDF and Pillow; rerunning the complete ink screen additionally uses NumPy and SciPy.

For complete verification of the published ZIP pair, including restoration and the final publication gate, run:

```sh
python3 scripts/verify_final_archives.py PATH_EN.zip PATH_RECORDS.zip --restore --final-gate
```

Replace the two ZIP arguments with the paths to the English and records archives. Generic checkpoint manifest/restoration verification alone establishes those checkpoint properties; publication verification additionally requires `--final-gate`.

The master contains 11,291 recorded maximal variants. The three reader sources have an identical annotated body and select its diplomatic or corrected branch through `EditionMode`. The master PDF renders the corrected branch with apparatus. A nested correction inside a wholly replaced or deleted passage is retained within that passage's one complete variant; it is not duplicated as an unrelated apparatus entry.

Every master body page, physical pages 2–1195, was compared with the corresponding corrected-apparatus page at 144 dpi. All 1,194 pairs had identical geometry, decoded RGB bytes and lossless PNG bytes. This supports reuse of the 477 corresponding apparatus pages with validated visual review; it does not claim that every master body page was opened. The distinct master title/front page was opened directly from the final PDF. The complete proof is `records/MASTER_APPARATUS_RASTER_EQUIVALENCE.json`.

## Source review and uncertainty

There are 23,136 decision rows and 12,140 concordance rows. Every required difference, original doubt and note has its decision record. `CHANGE_REPLAY_AUDIT.json` independently reconstructs all 706 checked pages from the supplied drafts and recorded edits. `FINAL_STRUCTURE_AUDIT.json` verifies exact diplomatic reconstruction from the master, source order, scan metadata, apparatus correspondence and link targets.

The replay audit explicitly accounts for 1 historical explanatory record already incorporated by exact edit rows. Its hashed adjudication is `records/REPLAY_RECORD_ADJUDICATIONS.json`; unexplained unmatched records, adjudication issues and replay exceptions all number zero.

| Source group | Pages | Original unsure | Original illegible | Checked unsure | Checked illegible |
| --- | --- | --- | --- | --- | --- |
| 134-2 | 81 | 417 | 100 | 293 | 86 |
| 134-3 | 93 | 456 | 95 | 290 | 80 |
| 134-4 | 99 | 421 | 116 | 459 | 134 |
| 134-5 | 132 | 504 | 125 | 345 | 138 |
| 134-6 | 124 | 373 | 97 | 336 | 251 |
| 134-7 | 112 | 455 | 97 | 337 | 108 |
| 134-8 | 39 | 140 | 29 | 109 | 78 |
| Brown (134-2) | 26 | 8 | 0 | 16 | 0 |

The checked totals include newly recognized unreadable undertext and provenance doubts. A reduction in one class and an increase in another do not measure a percentage of readable text. The corrected running text omits canceled passages; their doubts remain in the diplomatic form and apparatus. Every doubt which remains in a form is linked to its source scan.

### Concordance outcomes

| Outcome | Rows |
| --- | --- |
| our transcription corrected | 2225 |
| the arXiv text adds | 19 |
| the arXiv text corrects | 1084 |
| the arXiv text merges handwriting | 3731 |
| the arXiv text normalizes | 2768 |
| the arXiv text omits | 14 |
| the typescript reads as our transcription | 2299 |

### Decision labels

| Recorded decision | Rows |
| --- | --- |
| our transcription corrected | 8091 |
| note checked | 4731 |
| correct transcription | 2897 |
| the typescript reads as our transcription | 1731 |
| doubt retained | 1272 |
| retain | 690 |
| mechanical source integration; reading unchanged | 615 |
| retain doubt | 532 |
| settled on image | 422 |
| doubt resolved from image | 375 |
| review metadata updated | 326 |
| doubt resolved | 241 |
| metadata updated | 211 |
| metadata update | 169 |
| reading refined; residual doubt retained | 133 |
| the arXiv text adds | 52 |
| correct provenance | 49 |
| the arXiv text normalizes | 40 |
| illegible retained | 34 |
| doubt narrowed | 29 |
| illegibility retained | 25 |
| master slip variant | 24 |
| correct layer | 23 |
| mechanical macro repair | 22 |
| correct layer attribution | 20 |
| superseded visual judgment | 18 |
| provenance reassessed | 18 |
| arXiv omission | 14 |
| doubt resolved with corrected reading | 13 |
| arXiv addition | 12 |
| retain author notation | 11 |
| source limitation retained | 11 |
| the arXiv text omits | 11 |
| doubt revised | 10 |
| illegible resolved | 8 |
| the arXiv text corrects | 7 |
| source spelling retained | 7 |
| authorial spacing instruction recorded | 7 |
| source formula retained | 7 |
| arXiv retains deleted text | 6 |
| mechanical correction | 6 |
| master author instruction | 6 |
| illegibility resolved | 5 |
| provenance correction | 5 |
| arXiv supplies note text elsewhere | 4 |
| correct punctuation attribution | 4 |
| isolated typing slip in corrected forms | 4 |
| provenance doubt retained | 4 |
| doubt partly resolved | 3 |
| reconstruct graphic | 3 |
| retain apparent authorial slip | 3 |
| authorial join for master | 3 |
| retain mathematical slip for guide | 3 |
| doubt narrowed with corrected reading | 3 |
| source reading retained | 3 |
| source notation retained | 3 |
| source masked; collation unavailable | 3 |
| source wording retained | 3 |
| doubt settled | 3 |
| the arXiv text merges handwriting | 3 |
| illegible narrowed | 2 |
| illegibility partly resolved | 2 |
| correct transcription; arXiv rewrites note | 2 |
| retain apparent authorial overstatement | 2 |
| apply author instruction in corrected forms | 2 |
| isolated typing slip corrected only in corrected forms | 2 |
| apply physical continuation in corrected forms | 2 |
| doubt narrowed and transcription corrected | 2 |
| doubt retained as graphic | 2 |
| isolated slip recorded | 2 |
| handwriting confirmed | 2 |
| typed notation confirmed | 2 |
| source spacing retained | 2 |
| source edge limitation retained | 2 |
| correct placing mark | 2 |
| reading spacing variant recorded | 2 |
| illegible partly resolved | 1 |
| one-off slip corrected in corrected forms only | 1 |
| arXiv addition on this page | 1 |
| arXiv retains replaced letter | 1 |
| correct transcription; arXiv substitutes description | 1 |
| correct presentation | 1 |
| retain deletion; correct insertion provenance | 1 |
| correct intersection glyphs | 1 |
| correct transcription and placement | 1 |
| reconstruct instruction | 1 |
| retain formula; correct layer attribution | 1 |
| settled and corrected scope | 1 |
| retain apparent authorial symbol slip | 1 |
| apply authorial joining instruction | 1 |
| correct provenance; retain doubt | 1 |
| retain uncertainty | 1 |
| retain apparent authorial composition slip | 1 |
| retain apparent authorial hypothesis slip | 1 |
| retain apparent authorial cross-reference slip | 1 |
| reject false deletion | 1 |
| correct call number | 1 |
| settle pen correction | 1 |
| reject false punctuation | 1 |
| retain doubtful revision | 1 |
| retain source punctuation after pen deletion | 1 |
| settle source and record one-off slip | 1 |
| correct transcription; retain doubt | 1 |
| replace speculative character by graphic | 1 |
| retain authorial mathematical limitation; discuss in guide | 1 |
| correct transcription provenance | 1 |
| retain uncertain cancellation | 1 |
| record author paragraph instruction | 1 |
| retain doubtful marked superscript | 1 |
| retain doubtful mark | 1 |
| retain mathematical qualification for guide | 1 |
| correct provenance and glyph | 1 |
| authorial word separation for master | 1 |
| retain handwritten spelling | 1 |
| retain authorial formula slip | 1 |
| retain source cross-reference slip for guide | 1 |
| correct transcription cancellation | 1 |
| retain source mathematical slip for guide | 1 |
| correct insertion and cancellation | 1 |
| retain source formula slip for guide | 1 |
| retain source qualification for guide | 1 |
| master author join applied | 1 |
| retain author claim | 1 |
| retain author argument | 1 |
| retain author wording | 1 |
| illegibility narrowed | 1 |
| doubt retained and alternatives revised | 1 |
| doubt retained with graphic corrected | 1 |
| doubt retained with layering restored | 1 |
| doubt retained with location corrected | 1 |
| doubt retained with layers separated | 1 |
| doubt retained with final status corrected | 1 |
| doubt resolved as graphic | 1 |
| doubt resolved with layering corrected | 1 |
| doubt retained with mechanism corrected | 1 |
| mechanical typesetting repair | 1 |
| doubt narrowed and revised | 1 |
| retain source wording; discuss in guide | 1 |
| retain; cross-page spelling evidence | 1 |
| settled on image; isolated slip recorded | 1 |
| correct transcription; placing mark | 1 |
| correct layer placement | 1 |
| correct provenance and cancellation span | 1 |
| correct cancellation spans | 1 |
| handwritten deletion confirmed | 1 |
| pen cancellation confirmed | 1 |
| uninterpreted pen mark preserved | 1 |
| whole-definition cancellation confirmed | 1 |
| handwritten relation confirmed | 1 |
| handwritten qualification confirmed | 1 |
| handwritten reading confirmed | 1 |
| uninterpreted nonlexical mark recorded | 1 |
| authorial layout instruction recorded | 1 |
| provenance annotation corrected | 1 |
| probable authorial display instruction recorded | 1 |
| source blanks retained | 1 |
| source inconsistency retained | 1 |
| graphic preserved with provenance uncertainty | 1 |
| crowded typing retained | 1 |
| mechanical math-mode correction | 1 |
| source cross-reference retained | 1 |
| no additional overwrite inferred | 1 |
| spurious difference row rejected | 1 |
| mechanical override repaired | 1 |
| no additional content inferred | 1 |
| source mathematical question retained | 1 |
| source terminology retained | 1 |
| source date retained | 1 |
| source assertion retained | 1 |
| source defect retained | 1 |
| source revision retained | 1 |
| retain source claim; guide handoff | 1 |
| correct placement punctuation | 1 |
| retain source; guide qualification | 1 |
| correct layers and retain doubt | 1 |
| correct transcription; placing curve | 1 |
| record typed layers | 1 |
| isolated typing slip recorded | 1 |
| correct provenance and preserve marks | 1 |
| correct and retain scoped doubt | 1 |
| retain scoped doubt | 1 |
| authorial transposition recorded | 1 |
| mechanical LaTeX correction | 1 |
| authorial spacing variant | 1 |
| source clipping retained | 1 |
| source construction recorded | 1 |
| source spellings retained | 1 |
| reading continuation recorded | 1 |
| cancellation geometry recorded | 1 |
| source gaps retained | 1 |
| nonlexical marks recorded | 1 |
| reading join variant recorded | 1 |

## Editorial policy

Authorial wording and notation are retained, including consistent forms such as “standart,” “developped,” “it's” for “its,” and “A la.” Only individually justified isolated slips are corrected in the corrected branch. Mathematical defects and missing hypotheses are discussed in the relevant guide paragraph without alteration of the reader text. The supplied terminology standard governs editorial prose, with exact quotations and formulas protected; `EDITORIAL_STANDARDIZATION.tsv` records those editorial changes.

The guide has 189 paragraphs, including every numbered section 1–140 and 16-prime in order, the front matter, complete letter to Quillen, related letters and notes, and Brown's appendix. Its references distinguish archive sites from internal typescript folios. It records changes of mind, dependencies and consequential differences from the arXiv witness.

## Compilation and verification

| PDF | PDF pages | Engine exit | Overfull boxes | Widest, pt | Missing glyphs | Archive annotations | Distinct source pages |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Diplomatic | 709 | 0 | 3 | 1.91537 | 0 | 3820 | 706 |
| Corrected with apparatus | 1195 | 0 | 3 | 1.91537 | 0 | 3955 | 706 |
| Reading text | 709 | 0 | 1 | 1.91537 | 0 | 1704 | 706 |
| Annotated master | 1195 | 0 | 3 | 1.91537 | 0 | 3955 | 706 |
| Guide | 107 | 0 | 0 | 0 | 0 | 0 | 0 |

| PDF | LaTeX errors | LaTeX/package warnings | Underfull boxes |
| --- | --- | --- | --- |
| Diplomatic | 0 | 30 | 2 |
| Corrected with apparatus | 0 | 29 | 2 |
| Reading text | 0 | 769 | 2 |
| Annotated master | 0 | 29 | 2 |
| Guide | 0 | 2 | 2 |

Warning-family counts and their harmless interpretations are given in `TYPESETTING_REPORT.md`; the totals above are stated directly for each delivered PDF.

| PDF | Selected pages | Current-PDF images opened directly | Prior observations inherited by exact raster equality | Reviewed apparatus body pages reused in master |
| --- | --- | --- | --- | --- |
| Diplomatic | 90 | 21 | 85 | 0 |
| Corrected with apparatus | 471 | 25 | 453 | 0 |
| Reading text | 90 | 18 | 91 | 0 |
| Annotated master | 1 | 1 | 0 | 477 |
| Guide | 107 | 9 | 98 | 0 |

Counts are distinct pages within each evidence class. Extra targeted openings can exceed the selected sample. An inherited observation is not counted as an opening of the current image. Master body comparison and inherited apparatus coverage are reported separately.

Each `.tex` file is self-contained and compiles with LuaLaTeX from a standard TeX Live installation. Required packages include fontspec, unicode-math, amsmath, mathtools, tikz-cd, lua-ul, pdflscape, geometry, hyperref and bookmark; the fonts are Latin Modern Roman/Sans/Math. Compile a source twice with `lualatex -interaction=nonstopmode -halt-on-error FILENAME.tex`. No external image or TeX input is needed for a delivered reader.

`TYPESETTING_REPORT.md` gives the complete final log metrics, harmless warnings, logical/source link counts, annotation counts, all-page ink screening and every validated visual observation. It distinguishes direct openings from inherited exact-raster observations and separately documents master-body reuse. `APPARATUS_COUNTS.md` distinguishes variant inventory from apparatus entries actually printed in each form. No blanket scaling or raised overflow tolerance is used. The final gate is recorded in `records/FINAL_QA_GATE.json`.

## Rebuilding and records

To regenerate the reader sources, the extracted `edition/` and `inputs/` directories must be siblings under one working parent, with the supplied text files under `inputs/text/`: the build script resolves the inputs at `PROJECT.parent / 'inputs/text'`. Within that input directory it expects `records/PAGES_PS.json`. `scripts/build_readers.py` reads the canonical checked pages, explicit variants and that metadata; `scripts/build_guide.py` joins the reviewed guide fragments. From a fresh working parent containing the supplied archives, one concrete layout is:

```sh
mkdir -p edition inputs/text
unzip PS_READERS_EN.zip -d edition
unzip -o PS_READERS_RECORDS.zip -d edition
unzip PS_TEXT.zip -d inputs/text
python3 edition/scripts/restore_file_aliases.py
python3 edition/scripts/build_readers.py
python3 edition/scripts/build_guide.py
```

The original input archives are intentionally not duplicated in the final delivery. The standalone delivered `.tex` files compile independently of these inputs using the LuaLaTeX command above. `SOURCE_NORMALIZATION.json` records hashes for the completed mechanical integration; do not rerun historical review scripts over the final checked pages.

`CHECK_DECISIONS.tsv` includes exact before/after readings, reasons and source IDs. `ARXIV_CONCORDANCE.tsv` retains all original comparison columns plus outcomes and reasons; `BROWN_CONCORDANCE.tsv` provides the additional Brown comparison. `CHANGES_EN.tsv` has one row for every master variant and apparatus entry. Supplemental ownership tables, notes and historical proofs document the development of the edition and may retain explicitly obsolete working status.

## Checkpoint retention

Every available immutable checkpoint has been inventoried by archive SHA-256 and member path/size/CRC. `CHECKPOINT_ARCHIVES.tsv` identifies the archives; `CHECKPOINT_SUPERSESSION.tsv` lists every distinct earlier member version and either its identical final file or its specific replacement and reason. No earlier ZIP is nested in the final packages. Checkpoint number 61 was reserved across an interrupted save and is not asserted to be a verified saved archive; the recovery record describes that interruption. All work recoverable from the verified checkpoints and the conversation is retained or explicitly superseded.

Checkpoint 67 was valid locally at 591,029,848 bytes, but preparation of its save was rejected before upload because it exceeded the 512 MiB per-file limit. Its local ZIP remains immutable; it is not counted as durably saved.

Checkpoint 68 was durably uploaded using lossless duplicate-image packaging. ZIP CRC validation passed and all 817 aliases were restored exactly. Its verification nevertheless found a two-file manifest race: `scripts/write_final_reports.py` and `records/MATH_PROSE_PROOF_RENDER_MANIFEST.json` changed between manifest hashing and ZIP writing. All 5,851 logical files are accounted for; the discrepancy concerns two stale checksum rows and does not indicate lost content. The archive remains immutable, and its actual member versions are inventoried separately from those stale declarations in `records/CHECKPOINT_68_LOGICAL_MEMBER_AUDIT.json`. Subsequent full checkpoints capture stable member bytes before hashing and ZIP writing; their records explicitly supersede the affected entries. The retention manifest continues to enumerate every earlier version and its replacement.

## Credits and rights

AI-transcribed by Claude Opus 5.5 (Anthropic, effort high); checked against the scans, and this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic).

The witness consulted and not reproduced is the LaTeX edition of Mateo Carmona with the collaboration of Ulrik Buchholtz (arXiv 2111.01000 v2, 2021), extended from the 2015 edition by “the scrivener,” CC0 1.0.

The translation in the appendix is R. Brown's, prepared with assistance from L. Breen and J-L. Loday, as his note says; the rights in it belong to its translator or his heirs.

The rights in the original work belong to its author or the author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its publication here, please open a GitHub issue and we will take it down.
