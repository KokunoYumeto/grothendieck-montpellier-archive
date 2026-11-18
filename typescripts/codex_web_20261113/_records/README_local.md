# Codex-web folders of the Montpellier archive, 13 Nov 2026

> Correction of 14 Nov 2026 ~21:1x UTC (the user): every Codex-web session of this folder runs at reasoning effort max ("It's max, by the way, all of it"); the earlier text said high.

> Change of 14 Nov 2026 ~22:4x UTC (the user: "anything that goes over web codecs, it doesn't need a checkpoint. No checkpoints necessary"; the runs had saved a checkpoint ZIP after every page): the checkpoint ZIP sentences are removed from all 110 prompts in drag/ and from both templates in tools/. The page files and progress.log remain the record of progress. The prompts as they were, which is the text as sent for every folder sent before then, are in prompt_snapshots_before_no_checkpoint_20261114/. Codex-web prompts are checked with `push_rule_pro_prompts.py --lint-codex` (no checkpoint ZIP allowed). For a return that comes as checkpoint ZIPs, file the newest one per folder.

Five drag-and-drop folders, 52 scans, for the second ChatGPT account's remaining Codex allowance for the week. Each
folder is one transcription task for GPT-6 Astra at reasoning effort max, of about an hour. They hold the
easiest-to-read scans of the archive: typescripts with Grothendieck's handwritten corrections, and letters. Built by
Claude Opus 5.5 at effort high, 13 Nov 2026, ~17:40 UTC.

| Folder | Cote | Scans | Count | What the scans are | Zip |
|---|---|---|---:|---|---:|
| `drag\A57-01` | 57 (Picard) | 3-13 | 11 | typescript in English, "Local Picard schemes", with handwritten corrections | 19.2 MB |
| `drag\A57-02` | 57 (Picard) | 20-23, 73-79 | 11 | typed letters in English: one to Murre; two letter texts dated July 18, 1962, one of them with the typed signature A. GROTHENDIECK | 21.5 MB |
| `drag\A29-01` | 29 (Groupe fondamental) | 3-6, 8-12, 79-81 | 12 | letters in English, "Dear Grothendieck" / "Dear Murre" (scan 3 is dated May 10 1967): typed, one written by hand (5-6), typed comments (80-81) | 17.0 MB |
| `drag\A36-01` | 36 (SGA 7, ma part) | 10-18 | 9 | typescript in French with many handwritten corrections, insertions and typed-over words | 14.8 MB |
| `drag\A36-02` | 36 (SGA 7, ma part) | 19-27 | 9 | the same typescript, continued | 13.9 MB |

`ASSIGNMENTS.tsv` lists every folder with its cote and scans, and the Pro package of the 12 Nov packaging report that
holds them (the Pro packages are being re-cut today, so the package names will change). When a return proves good,
the Pro packaging leaves these scans out.

## Why these scans

- **Easy to read.** Grothendieck's handwritten notes in these cotes are fast and dense on nearly every page we sampled
  (contact sheets of 12 cotes: 2, 29, 31, 36, 37, 57, 62, 63, 122, 126, 130, 131). The typed and letter pages are
  the clear exception. To find them, every scan of eleven cotes with typescripts (27, 29, 32, 35, 36, 37, 45, 46, 57,
  63, 123) got a typed-text score from Tesseract word confidences, used only to choose pages, never to transcribe.
  The high-scoring runs were then looked at in contact sheets, and the coherent ones kept:
  - consecutive pages of one typescript (57 scans 3-13, opening with its title; 36 scans 10-27, opening with its
    title on scan 10, split in two);
  - the letters together (57; 29).
  Every page is upright; scan 7 of cote 29 is blank and was left out. A full-size third of 36 scan 14 was checked:
  typewriter text, sharp, with handwritten corrections legible.
- **Late in order W.** The scans belong to packages 159 (36), 164 (57), 170 and 171 (29) of the 12 Nov packaging
  report: ranks 21, 23 and 24, near the end of the send order. None is in a package sent or returned (01-35,
  `packages_done\`, `returns\`). `packages\` and `packages_work\` were not touched.
- **Left out on purpose:** copies of other authors' printed articles (63), his handwritten calculation drafts, and
  the typed French text of 29 (scans 13-38), which is legible but dense in indices and would need smaller folders.

## How the folders were sized: about an hour at Astra high

The Deligne drag returns record their times in `progress.log` (deligne_codex_packets_20261112\returns\). Over the 20
returns of 12-13 Nov (GPT-6 Astra at reasoning effort max), start to frozen transcription took 12-76 minutes for
6-12 pages: median 4.3 minutes per page, of which about 1.5 for the first pass and the rest for the second reading.
The one typescript graded (D002-01) took 5.1 minutes per page.

- **The two typescripts of 36:** 9 scans each. The pages are full, and nearly every line has a correction or a
  typed-over word; they will run slower than D002.
- **The typed letters (57, 29):** 11-12 scans each. The letters run at about the D002 rate.

The rate for handwriting does not enter: the only handwritten pages are the two of one letter (29 scans 5-6),
written in a clear hand.

## How to run them

On the second ChatGPT account, open a work session (Codex) with **GPT-6 Astra, reasoning effort max**, one session
per folder, as for the Deligne drag folders. Drag in the three files of the folder: `PROMPT.md`, `PREAMBLE.tex` and
`<ID>_scans.zip`. The first line of `PROMPT.md` says that the file is the task. To check the method on one return
before the rest, start with A57-01: look at its final message, `out\progress.log` (minutes per page) and
`out\A57-01_audit.md`, whose second reading must list what it checked. The four other folders can run while you
check.

## What comes back, and where it goes

Each session offers `<ID>_out.zip`. It holds:
- `pages\<ID>_<cote>_scanNNN.tex`;
- `<ID>_transcription.tex` and `<ID>_standalone.tex`;
- `<ID>_doubts.md`: the notation table, the doubts, the slips kept as written and the abbreviations;
- `<ID>_inventory.csv`, with the columns `sheet_kind` and `hand`;
- `<ID>_audit.md`;
- `<ID>_notes.md`: the steps the pages mark as unverified, and their titles, dates and page counts;
- `progress.log`.

Drop the zip into `C:\Users\user\Documents\grothendieck_archive_transcription_20261110\codex_web_20261113\returns\`.

## How a return is graded

One return is graded before the scans are taken out of the Pro packages, the way D002-01 was
(`deligne_codex_packets_20261112\returns\GRADE_D002-01_20261113.md`). The grade is an in-app check by Claude Opus 5.5
at effort max.
- **Pages.** Two of the return's pages, read line by line against the images: the one densest in formulas and
  corrections, and an ordinary one.
- **What is counted:**
  - omissions;
  - text errors, mathematics errors and font errors;
  - doubt marks missing where the page is unclear, and marks put where it is clear;
  - handwritten corrections left out or put in the wrong place.
- **Also checked:**
  - the counts in the final message against the files;
  - the first and last lines of the other pages against the images;
  - a LuaLaTeX build of the standalone file here, with the overfull boxes counted (the sandbox does not compile).

Verdict: good enough as is, good enough with a second pass, or not usable. If the grade is good, the ASSIGNMENTS.tsv
rows are dropped from the Pro packages.

## The prompt

`tools\PROMPT_TEMPLATE_CODEX_WEB.md` takes these parts from the archive's Pro template (`ARCHIVE_PROMPT_TEMPLATE.md`):
- the macros (`\cotefile`, `\scanpage`, `\mspage`, `\deleted`, `\inserted`, `\margin`, `\uline`, `\uuline`,
  `\diagram`, `\figure`, `\unsure`, `\illegible`) and its doubt rules;
- one stream, and the notation table;
- the inventory with `sheet_kind`;
- the two standing questions.

It is laid out like the Deligne drag prompt:
- the whole page and three thirds per scan, with MANIFEST.tsv;
- a page file and progress line per page as the checkpoint;
- a full second reading with a per-page audit;
- frozen hashes, and a zip offered as a download.

Without the context zip and the research notes, which are the Pro runs' part. New for this material:
- `\handwritten` for his hand on a typed page;
- typed-over words as `\deleted`;
- letters, letterheads and the archive's sheet numbers;
- a `hand` column in the inventory.

The four prompt changes from the D002-01 grade are applied:
1. **Overstruck letters.** Every capital in a heading or a functor name is checked for double striking on its own
   crop; a notation entry for the body does not cover a heading. A typescript has no bold.
2. **Second reading from a fresh crop.** The accents and the odd-looking words of each line are written down from
   the crop before the page file is opened.
3. **Recurring ambiguous glyphs.** The doubt is recorded once in the notation table, with every candidate, and
   marked at its first occurrence on each page.
4. **No compilation in the sandbox.** LuaLaTeX does not work there; only the balance check is run, and we compile
   the return here.

Also added: `\diagram` with tikz-cd needs `ampersand replacement=\&`, as the Pro returns write it. Every PROMPT.md
passes `push_rule_pro_prompts.py --lint`. `tools\PREAMBLE.tex` was test-compiled with every macro under LuaLaTeX and
pdfLaTeX, with no errors.

## Files

- `drag\<ID>\`: the five folders, flat, as dragged.
- `ASSIGNMENTS.tsv`.
- `returns\`: for the returned zips.
- `tools\`:
  - `build_codex_web.py`, which builds the folders; it reads the archive PDFs only and skips folders that exist;
  - `PROMPT_TEMPLATE_CODEX_WEB.md`;
  - `PREAMBLE.tex`;
  - `BUILD_LOG.jsonl`: per folder its scans, ink values, zip size and SHA-256.

Images are taken as in the Pro packages, then converted to grayscale:
- the largest image of each PDF page (about 1700 x 2150 px, 228 ppi);
- autocontrast with cutoff 1, and an unsharp mask (r2 p120 t3);
- JPEG at quality 88;
- thirds overlapping by 60 px.

SECTIONS_STATE.md lists a CSG transcription (L12d) of a letter from cote 29; which letter it is was not checked.


## Batch B, 13 Nov 2026 ~19:1x UTC: 20 more folders, 181 scans (user: every easy-to-read run, Codex web at GPT-6 Astra max)

Effort: the user runs these folders at GPT-6 Astra **max** (A57-01 ran at max and took about 2 hours for 11 scans; checked on scans 003 and 008 by Claude Opus 5.5 at effort max: no misreadings, markup correct).

Source of the pages: the typed-page inventory `api_typescripts_20261112/TYPED_INVENTORY_20261113.tsv` (made by eye from contact sheets), the typed scans of cotes 10 (typescript on Tannakian categories, 84 scans), 37 (typed letters, lists, typescripts, tables of contents, 48 scans), 12 (22 scans) and 15 (27 scans, some faint or probable). None of these was sent over the API or to Pro. Upside-down typed versos are left out. Scan numbers are PDF pages (the inventory's site number + 1); a first build that used the site numbers was set aside in `_wrong_pages_20261113_not_for_use/`. Folders: B10-01 to B10-10, B37-01 to B37-05, B12-01, B12-02, B15-01 to B15-03; each 5-11 scans. Rows in `ASSIGNMENTS.tsv`.

## Batch C, 13 Nov 2026 ~19:5x UTC: 12 folders, 70 pages

Every page of cotes 27, 29, 32, 35, 36, 45, 46 and 123 was scored by `tools/score_typed_C.py` (Tesseract, words of 3+ letters read at confidence >= 80; `scoring_C/scores.tsv`). Pages scoring 60 or more and not already in a folder were kept (`scoring_C/selected.json`) and all 70 were checked by eye on one contact sheet: all typescript, many with handwritten corrections and formulas. Folders of 4-8 pages (cote 29's French text is dense, so its folders are small): C29-01 to C29-07, C32-01, C45-01, C46-01, C123-01, C123-02. Single typed pages of cotes 35 and 36 were left out. A57-01 is in `done/`; the builder now skips folders found there.

## Batch H, 14 Nov 2026: handwriting, 32 folders, 238 pages (user: "180 pages of a codex, yeah, build that")

Built by Claude Opus 5.5 at effort high from the nine runs of `HANDWRITING_CANDIDATES_20261114.md` (one row per run
and per cote in `HANDWRITING_INVENTORY_20261114.tsv`). The nine runs are 182 pages, of which 10 are typed (109
scans 13-15; 97 scans 8, 10, 14, 19; 26 scans 4, 6; 35 scan 2). Then come the 56 typed pages of cote 63 (folders
H63-03 to H63-09), sent with run 2 so that 63 leaves the Pro packaging almost whole. Builder:
`tools/build_handwriting.py`; log: `BUILD_H_20261114.log` and `tools/BUILD_LOG.jsonl`; rows in `ASSIGNMENTS.tsv`.
No effort is stated in the folders: the user sets it in Codex web.

**The prompt.** The handwritten folders use `tools/PROMPT_TEMPLATE_HANDWRITING.md`, the typed template with these
changes:
- a section "Reading handwriting", built from the errors found when the A, B and C returns were checked against the
  scans: slanted or sideways margin notes ("pas prouvé" read as "pour journé"); symbols written into formulas (an
  index `ih` read `jh`, a "; " read ","); punctuation and endings (a comma left out, double quotes as single,
  "papers" as "paper"); struck words given as live text; E/F and 3/5; his letters reduced to strokes; insertions put
  in the wrong place;
- the rule that every doubtful reading is marked, and that a handwritten page without any doubt mark is a warning
  sign;
- `\handwritten` only for handwriting on a typed page. A word written over another is given in its final form, with
  the form underneath in `\deleted`. Margin notes written sideways carry a comment;
- the second reading also rereads every margin note in its own direction, and every struck word or block;
- a section "The attached draft". Where a draft by others exists, it is in the folder and named with its source. It
  is to be compared only after the page has been transcribed from the images; at a difference the ink decides, or
  both readings go in `\unsure`. The doubts file then carries a table of the differences.

The same macros and the same `PREAMBLE.tex` are used. The typed folders of 63 use the typed template unchanged.
Every PROMPT.md passes `push_rule_pro_prompts.py --lint`.

**Drafts.**
- `DRAFT_PS_Breen_letters.tex` is in H134-02 to H134-06. It is the appendix "Three letters to Larry Breen" of
  chapter I of Pursuing Stacks, from arXiv:2111.01000 (ed. M. Carmona with U. Buchholtz), file `ps1.tex`, copied
  unchanged from the line `\chapter*{Appendix: ...}` to the end of the file. It gives the letters of 5.2 and 17.2.1975
  in French, the first without its beginning, but the letter of 17-19.7.1975 only in R. Brown's English translation.
  The prompt says so.
- **Not yet in the folders:** the CSG drafts of two of the 1974 letters on Sính's thesis, L30d
  (https://csg.igrothendieck.org/wp-content/uploads/2024/09/L30d.pdf) and L31d
  (https://csg.igrothendieck.org/wp-content/uploads/2025/10/L31d.pdf). Neither is on this machine, and this build
  downloaded nothing. To add them:
  1. put the PDFs in `tools/drafts_20261114/`;
  2. give H103-01 and H103-02 the draft entry in `build_handwriting.py`, after finding which scans each covers;
  3. move the two folders out of `drag/` and rerun.

  **Decided 14 Nov ~05:3x UTC (main session):** both PDFs were downloaded to `tools/drafts_20261114/` (L30d: letter to
  P. Deligne, 7.8.74; L31d: letter to Deligne, Giraud, Verdier, 23.6.1974; both cote 103). They say "(c) 2024 Grothendieck
  Institute, All rights reserved", so they do not go into any upload folder (as with the reader packages, only free
  witnesses are uploaded). They stay local, for our own comparison with the returns of H103-01 and H103-02; no reading is
  taken from them, and the comparison credits them by name (CSG, ed. Mateo Carmona).

  The other drafts in SECTIONS_STATE.md are CSG L15d-L20d (letters from cote 37) and U25d (cote 66, "complete").
  They are not in the folders either, and which scans they cover was not checked.

**Extents checked at build** (contact sheets):
- **Letter to Mumford:** scans 14-15 of cote 13, two half-sheets, signed on 15. Scans 16-20 are English notes on the
  same subject and go in the same folder.
- **Serre's letter:** one page, scan 2 of cote 97. Scans 3 (a list of names) and 4 (a short note) go with it, with
  the annotated typed pages 8, 10, 14 and 19.
- **Cote 37:**
  - scan 13 is already in B37-01, and scan 74 (a typed letter) in B37-04; both stay there;
  - scans 54-55 are one handwritten letter on Harvard letterhead, signed;
  - scans 75-76 are one handwritten letter on graph paper;
  - scans 52, 53 and 77 are handwritten lists;
  - so H37-01 holds 52-55 and 75-77.

**Send order** (on the second account, one Codex-web session per folder, as for the earlier folders):
1. **First, runs 1-6:**
   - run 1: H109-01, H109-02, H109-03;
   - run 2: H63-01, H63-02, then the typed H63-03 to H63-09;
   - run 3, the pilot: H156-01;
   - runs 4-6: H13-01, H97-01, H37-01.
2. **Grade the pilot H156-01** (Grothendieck's spaced hand of 1986) as D002-01 and A57-01 were graded.
3. **Then run 8:** H26-01, H48-01, H35-01, H66-01, H162-01, H162-02. Its pages are lists and can go without waiting
   for the pilot.
4. **Runs 7 and 9, only once the pilot's grade is good:** H103-01, H103-02, H104-01, H104-02; then H134-01 to
   H134-06. If the pilot is not good, these scans stay in Pro.

| Folder | Cote | Scans | Pages | Grade | What | Run |
|---|---|---|---|---|---|---|
| H109-01 | 109 | 9-11, 13-15 and 17-19 | 9 | B | R. Brown's handwritten corrections to Pursuing Stacks (lists); 13-15 typed comments | 1 |
| H109-02 | 109 | 21-29 | 9 | B | R. Brown's handwritten corrections to Pursuing Stacks (lists) | 1 |
| H109-03 | 109 | 30-38 | 9 | B | R. Brown's handwritten corrections to Pursuing Stacks (lists) | 1 |
| H63-01 | 63 | 3-8 | 6 | A/B | Tate's handwritten formulaire on elliptic curves | 2 |
| H63-02 | 63 | 9-14 | 6 | A/B | Tate's handwritten formulaire on elliptic curves | 2 |
| H63-03 | 63 | 16-24 | 9 | A (typed) | typed formulaire and typescripts on elliptic curves | 2 |
| H63-04 | 63 | 25-34 | 10 | A (typed) | typed formulaire and typescripts on elliptic curves | 2 |
| H63-05 | 63 | 41-48 | 8 | A (typed) | typed formulaire and typescripts on elliptic curves | 2 |
| H63-06 | 63 | 49-55 | 7 | A (typed) | typed formulaire and typescripts on elliptic curves | 2 |
| H63-07 | 63 | 57-64 | 8 | A (typed) | typed formulaire and typescripts on elliptic curves | 2 |
| H63-08 | 63 | 78, 80-81 and 83-85 | 6 | A (typed) | typed formulaire and typescripts on elliptic curves | 2 |
| H63-09 | 63 | 87-94 | 8 | A (typed) | typed formulaire and typescripts on elliptic curves | 2 |
| H156-01 | 156-7 | 2-9 | 8 | B-C (pilot) | Analysis situs, 3rd version (1986), his late spaced hand | 3 (pilot) |
| H13-01 | 13 | 14-20 | 7 | B (16-20 B-C) | letter to Mumford, Algiers 1 Nov 1965 (14-15), English notes (16-20) | 4 |
| H97-01 | 97 | 2-4, 8, 10, 14 and 19 | 7 | B; typed A | Serre's letter 4 Nov 1966 (2), list (3), note (4), annotated typed pages | 5 |
| H37-01 | 37 | 52-55 and 75-77 | 7 | B | handwritten lists on the re-editions (52, 53, 77); letter on Harvard letterhead (54-55); letter on graph paper (75-76) | 6 |
| H103-01 | 103 | 2-7 and 9-10 | 8 | B / B-C | correspondence on Sinh's thesis (1974): typed pages and his letters | 7 |
| H103-02 | 103 | 11-18 | 8 | B / B-C | correspondence on Sinh's thesis (1974): typed pages and his letters | 7 |
| H104-01 | 104 | 2-9 | 8 | B-C | Champs (stacks) 1, copies of his notes | 7 |
| H104-02 | 104 | 10-17 | 8 | B-C | Champs (stacks) 1, copies of his notes | 7 |
| H26-01 | 26 | 2-11 | 10 | B | EGA VI plans, notations, open problems (4, 6 typed) | 8 |
| H48-01 | 48 | 2-6 | 5 | B | plan of EGA VII | 8 |
| H35-01 | 35 | 2-5 | 4 | B | plan of SGA 7 (2 typed) | 8 |
| H66-01 | 66 | 2-5 | 4 | B-C | Problemes (1964) | 8 |
| H162-01 | 162-1 | 2-10 | 9 | B-C | list of names and papers lent | 8 |
| H162-02 | 162-6 | 2-6 | 5 | B | isolated pencil sheets with formulas | 8 |
| H134-01 | 134-1 | 2 and 4-7 | 5 | B-C | cover; letter Cher Deligne | 9 |
| H134-02 | 134-2 | 146-153 | 8 | B-C | copies of his letters to L. Breen, 1975 (draft attached) | 9 |
| H134-03 | 134-2 | 154-161 | 8 | B-C | copies of his letters to L. Breen, 1975 (draft attached) | 9 |
| H134-04 | 134-2 | 162-169 | 8 | B-C | copies of his letters to L. Breen, 1975 (draft attached) | 9 |
| H134-05 | 134-2 | 170-177 | 8 | B-C | copies of his letters to L. Breen, 1975 (draft attached) | 9 |
| H134-06 | 134-2 | 178-185 | 8 | B-C | copies of his letters to L. Breen, 1975 (draft attached) | 9 |

## Batch J, 14 Nov 2026: B-C handwriting, 110 folders, 840 pages (after the spot check of batch H)

These were built by Claude Opus 5.5 (the agent that built batch H) after `SPOT_CHECK_H_20261114.md`.
- **The check:** 23 pages of batch H were compared word by word with the scans. GPT-6 Astra in Codex web at reasoning
  effort max made 0.18 errors per 100 words, against a median of 0.80 over the 14 Pro sample checks.
- **What the batch holds:** every B-C cote of `HANDWRITING_INVENTORY_20261114.tsv` that is neither in a sent Pro package
  nor in a Codex-web folder, and one C-hand pilot.
- **How it was built:**
  - Builder: `tools/build_handwriting_j.py`, which calls `build_handwriting.build()`. Same images and template as batch H,
    no drafts.
  - Logs: `BUILD_J_20261114.log`, `PLAN_J_20261114.log`; the ink values are in `tools/J_INKS_20261114.json`.
  - The rows are in `ASSIGNMENTS.tsv`, and the per-folder table is in `J_TABLE_20261114.md`.
- **Blank scans left out:** 13 #3, 13, 22, 26, 33, 36, 45; 71 #2, 5, 16, 18, 20, 35; 75 #29; 81 #9, 31; 156-9 #129.
- **The checkpoint rule of 14 Nov:** both templates, and every J and HC1 PROMPT.md, now save a checkpoint ZIP of `out/`
  after every finished and every audited page, and hourly. The templates as they were are kept as
  `tools/*_before_checkpoint_20261114.md`.
- **Checks:** all 110 PROMPT.md pass `push_rule_pro_prompts.py --lint`, and every name has 40 characters or fewer. The
  zips total 1.07 GB.

Cost at the measured 0.29 % of a 10x week per page:

| Send | Folders | Cote | Pages | Share of a week | Now in Pro package (ASSIGNMENTS.tsv) |
|---|---|---|---|---|---|
| 1 | HC1-01 | 1 (scans 4, 12, 15, 24, 27, 35, 39, 49) | 8 | 2 % | none: these pages were done by Pro and scored in `returns/MPL_1_002-050_check`. This is the C-hand pilot; compare the two |
| 2 | J156-7-01 to -14 | 156-7, 10-114 | 105 | 31 % | 166-168 |
| 3 | J156-3-01 to -05 | 156-3 | 40 | 12 % | 128 |
| 4 | J156-4-01 to -11 | 156-4 | 88 | 26 % | 162-163 |
| 5 | J156-5-01 to -06 | 156-5 | 48 | 14 % | 127 |
| 6 | J156-6-01 to -12 | 156-6 | 93 | 27 % | 164-166 |
| 7 | J156-8-01 to -16 | 156-8 | 126 | 37 % | 124-126 |
| 8 | J156-9-01 to -18 | 156-9 | 138 | 41 % | 129-131 |
| 9 | J13-01 to -05 | 13 (all but 14-20) | 37 | 11 % | 84 |
| 10 | J53-01 to -05 | 53 | 33 | 10 % | 196 |
| 11 | J71-01 to -06 | 71 | 41 | 12 % | 169 |
| 12 | J75-01 to -04 | 75 | 31 | 9 % | 107 |
| 13 | J81-01 to -07 | 81 | 52 | 15 % | 171-172 |
| | **110 folders** | | **840** | **about 2.5 weeks** | |

- **Why HC1-01 goes first.** Its result decides whether the roughly 100 C cotes can follow the same route; they are
  the bulk of the archive.
- **One week's allowance** (about 340 pages) covers sends 1 to 5, and most of 6.
- **Grading as returns come back.** Grade one page per cote by the method of `SPOT_CHECK_H_20261114.md`. Drop the
  scans from the Pro package named in ASSIGNMENTS.tsv only once the return passes.
- **Before sending a Pro package that holds any of these scans,** decide which route takes them.

## Batch K, 17 Nov 2026: the tail of the Pro queue, 247 folders, 3,536 pages (round 1 built: 35 folders and 2 controls)

Built by Claude Opus 5.5 at effort high (the agent that built batches H and J), from `BRIEF_BATCH_K_20261117.md` and the
template decision of `METHOD_AUDIT_AND_PLAN_20261117.md`. **Why:** one ChatGPT account has about 120x of Codex capacity
that expires on Saturday 21 Nov 2026, and every hand grade can now go to Codex web.

**What the batch holds**
- Every queued Pro package except the sixteen promoted ones (`.01_` to `.16_`) and the next twenty, which stay on Pro:
  P051, P052, P054-P058, P060, P064, P066-P076.
- That is 91 packages, 3,536 scans, in 247 folders of 6-16 scans (most of them 14-16, about two hours a session).
- Every scan was checked against `packages_done/`, `returns/`, `packages_work/CODEX_COVERED_SCANS.tsv`,
  `ASSIGNMENTS.tsv`, the API page files and the packages kept on Pro. None of the batch's scans is done or out on
  another route.
- **Blank scans:** the builder's own test (ink below 0.0003) left out none of the scans in the packages. The 188 scans
  missing inside the batch's cote ranges, not counting the scans that other routes have, are blank pages: 179 are in
  the package builder's blank list, and 9 of cote 119 (#162, 182, 193, 196, 214, 241, 254, 272, 275) have ink 0.0.
  The list is `K_GAPS_20261117.tsv`.

**How it was built**
- Builder: `tools/build_handwriting_k.py` (`--plan`, `--build R`, `--prompts R`), which calls `build_handwriting.build()`.
  The images and folder form are those of batches H and J; the plan is `K_PLAN_20261117.json` and `.tsv`.
- Template: `tools/PROMPT_TEMPLATE_HANDWRITING_K.md`, the handwriting template with three changes:
  - G1, the mathematical notes, `{ID}_mathnotes.md`, written only after `transcription frozen`;
  - G2, two more error kinds: a script T read as Gamma, and a plausible neighbouring word put in place of the ink;
  - G3, the folders of the same cote named before and after, with notation tables reconciled afterwards.
- `--prompts` rewrites PROMPT.md and PREAMBLE.tex of built folders without touching the zips.
- Material sentences: `tools/k_material.py`. They say only what the survey of `HANDWRITING_INVENTORY_20261114.tsv`
  saw on sample pages.
- Logs: `BUILD_K_ROUND1_20261117.log`; ink values in `tools/K_INKS_20261117.json`.
- **Checks:** all 37 built PROMPT.md pass `push_rule_pro_prompts.py --lint-codex`, and the round-1 zips total 721 MB.

**Queue:** the twelve packages round 1 covers completely are in `../packages_moved_to_codex_20261117/` (its README
lists them). P124 (cotes 76, 88 and 70) stays in `packages/` until its round-5 folders are built.

### Send order and rounds (as first planned; superseded by "Rounds 2-6 as built" below)

At 0.030x a page (batches H and J). G1 adds an expected 10-25 % after the freeze, so all seven rounds come to about
106x for the reading and about 117-133x with G1. That is near or above the 120x available; the pilot measures it.

| Round | Folders | Pages | Credit (reading) | Cotes, in send order | State |
|---|---:|---:|---:|---|---|
| 0 | CTRL-148, CTRL-145 | 30 | 0.9x | 148 (scans 44-58), 145 (scans 20-34) | built: send first |
| 1 | 35 | 532 | 16.0x | 34, 46, 43, 45, 70 | built |
| 2 | 35 | 515 | 15.4x | 158, 123, 119, 63, 80, 74, 23, 57 | planned |
| 3 | 46 | 644 | 19.3x | 118, 102, 127, 35, 49, 50, 85, 86, 31, 101, 37, 79 | planned |
| 4 | 39 | 596 | 17.9x | 77, 84, 62, 27, 28, 93, 83 | planned |
| 5 | 34 | 454 | 13.6x | 51, 52, 10, 73, 76, 88, 111, 135, 162-5, 125, 126, 32, 29, 94 | planned |
| 6 | 33 | 461 | 13.8x | 97, 21, 78, 19, 161-1, 161-2, 160, 82 | planned |
| 7 | 25 | 334 | 10.0x | 40, 41, 42, 87, 128, 161-6, 1, 161-3, 161-4, 109, 55 | planned |

- **Rounds 2-7 wait for the pilot's result:** the control readings against the corrected text, the G1 overhead, and
  the value of the notes (`METHOD_AUDIT_AND_PLAN_20261117.md`, section 3).
- **Control folders.** CTRL-148 and CTRL-145 re-transcribe pages that already have a Pro first pass and a Claude second
  pass of 17 Nov, so they measure the method. They are not new work, so they have no ASSIGNMENTS row.
  `tools/file_returns.py` files their returns into `returns_control/`, never into `returns/`. The script as it was is
  kept as `tools/file_returns_before_controls_20261117.py`; K IDs needed no change.

**Round 1 folders** (`drag/`; the rows are in `ASSIGNMENTS.tsv`):
- **34** (SGA 7 notes), K34-01 to K34-12: scans 18-210, 188 pages.
- **46**, K46-01 to K46-03: scans 49-95, 47 pages.
- **43**, K43-01 to K43-10: scans 1-93 and 143-208, 149 pages.
- **45**, K45-01 to K45-02: scans 2-32, 31 pages.
- **70**, K70-01 to K70-08: scans 2-125, 117 pages.

**Per session:** open a new Codex-web session with GPT-6 Astra at reasoning effort max, one per folder, and drag in
the three files of the folder (`PROMPT.md`, `PREAMBLE.tex`, `<ID>_scans.zip`). Send the two controls first, then round 1
in the order above. The returns `<ID>_out.zip` land in Downloads; `tools/file_returns.py` files them.

### Rounds 2-6 as built (17 Nov 2026 ~18:xx UTC); this replaces the round table above

**What changed, by the main session's message of 17 Nov ~17:4x-17:5x UTC**
- **Eleven packages left batch K** and stay with Pro:
  - the small ones of `../packages_work/SMALL_FOR_EXPIRING_ACCOUNT_20261117.txt` that were in the batch: P086, P093,
    P097, P121, P135, P158, P160, P161, P179, P181. They are for the expiring account's Pro, and are renamed `.s_` in
    `../packages/`;
  - P177 (`.AUDIT2_`), which the user runs unchanged on Codex as a test.
- **Batch K is now** 80 packages, 223 folders and 3,220 pages: about 96.6x for the
  reading, or about 106-121x with the mathematical notes (+10-25 %),
  plus 0.9x for the controls.
- **Rounds 2-6 are in `drag_next/`, not in `drag/`,** so that they cannot be sent by mistake. The main session moves a
  round into `drag/` after the pilot's verdict.
- **Their packages stay in `../packages/`** until that verdict, and their ASSIGNMENTS.tsv rows are added when a round
  moves.
- **Plan:** `K_PLAN_20261117.json` and `.tsv`, made with `build_handwriting_k.py --plan2`. The plan before the
  exclusions is `K_PLAN_20261117_before_exclusions.json`.

**Hua's transcription as a witness** (approved by the user: a witness, never a basis)
- Rounds 2-6 use `tools/PROMPT_TEMPLATE_HANDWRITING_K2.md`: the K template with a witness check inside method 7, after
  the line `transcription frozen`.
- **What the run does with it:**
  - it opens Hua's files only then, and only for the places still marked `\unsure` or `\illegible`;
  - it changes a place where his reading, checked against the ink, settles it, and adds his reading as the alternative
    where the ink does not decide;
  - it never takes his wording or conventions, and never fills a passage from his text;
  - it records each place in a "Witness check" table of the doubts file ("Hua batch-NN reads ..."), hashes the text
    again (`witness check done`), and only then writes the mathematical notes.
- **What the zips hold:** under `hua/`, his batch files (with their drawing files) whose pages overlap the folder's
  scans, from `ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts/<cote>/`, and his
  `grothendieck.sty`.
- **Coverage:** every one of the 188 folders has batch files. Of the 2,688 scans, Hua has text for 2,499, only a
  description for 19, and nothing for 170. A folder whose scans he does not cover would get no Hua step; the builder
  cuts the blocks marked `<!--HUA-->` out of the template, but no folder needed it.
- **Round 1 and the controls** stay as built, without Hua: they are the pilot.

| Round | Folders | Pages | Credit (reading) | Hua: text / description only / none | Cotes, in send order | State |
|---|---:|---:|---:|---|---|---|
| 0 | CTRL-148, CTRL-145 | 30 | 0.9x | (no Hua step) | 148 (scans 44-58), 145 (scans 20-34) | in `drag/`: send first |
| 1 | 35 | 532 | 16.0x | (no Hua step: the pilot) | 34, 46, 43, 45, 70 | in `drag/`, being sent |
| 2 | 33 | 493 | 14.8x | 423 / 11 / 59 | 158, 123, 63, 80, 74, 23, 57 | built in `drag_next/`, waits for the pilot's verdict |
| 3 | 41 | 585 | 17.6x | 541 / 7 / 37 | 102, 127, 35, 85, 86, 31, 101, 37, 79 | built in `drag_next/`, waits for the pilot's verdict |
| 4 | 37 | 554 | 16.6x | 517 / 0 / 37 | 77, 84, 62, 27, 28, 93, 83 | built in `drag_next/`, waits for the pilot's verdict |
| 5 | 41 | 555 | 16.6x | 525 / 1 / 29 | 10, 73, 76, 88, 111, 135, 162-5, 125, 126, 32, 29, 94, 97, 78 | built in `drag_next/`, waits for the pilot's verdict |
| 6 | 36 | 501 | 15.0x | 493 / 0 / 8 | 19, 161-1, 161-2, 160, 82, 40, 41, 42, 1, 161-3, 55 | built in `drag_next/`, waits for the pilot's verdict |

**Checks**
- All 188 PROMPT.md in `drag_next/` and the 37 in `drag/` pass `push_rule_pro_prompts.py --lint-codex`.
- Every zip tests clean and is under 500 MB. The `drag_next/` zips total 3.56 GB.
- **Blank scans:** the builder's test left none out. The 162 scans missing inside the batch's cote ranges, not
  counting the scans that other routes have, are all in the package builder's blank list (`K_GAPS_20261117.tsv`).
- **Build logs:** `BUILD_K_ROUNDS2-6_20261117.log`. 38 of the folders were built by a run that was stopped when they
  were moved to `drag_next/`; their records were written to `tools/BUILD_LOG.jsonl` afterwards from the zips.

### After the pilot verdict (17 Nov 2026, about 19:30 UTC): G1, rounds 2-6 released

- **Verdict:** under METHOD_AUDIT section 3, batch K continues with G1, the light notes. The verdicts are in
  `returns_control/<ID>/VERDICT_*.md`.
- **Two lines from the CTRL-145 verdict are now in both templates** (`PROMPT_TEMPLATE_HANDWRITING_K.md` and `_K2.md`):
  - under "Where readings go wrong": a hatched or scribbled block over an exponent, index or sign is a cancellation,
    transcribed with `\deleted{...}`;
  - in the notes: no slip, convention change or error claim above low confidence when its reading carries a doubt
    mark or sits on a struck or overwritten mark.
- **Rebuilt with these lines:** every unsent PROMPT.md, that is 34 round-1 folders in `drag/` and `drag_split/`
  (K34-01 was sent and is left as it was) and all 188 folders of rounds 2-6.
- **Lint:** all of them pass `push_rule_pro_prompts.py --lint-codex`. Plain `--lint` fails them all, and K34-01 as
  sent, only because it requires the checkpoint-ZIP rule, which Codex-web tasks do not have (the user, 14 Nov 2026).
- **Chrome fallback:** `tools/split_for_chrome.py` now also writes `<ID>_PROMPT.zip`, holding the PROMPT.md, and its
  paragraph names it. It packs parts to 8.95 MB, so every part is under 9,000,000 bytes.
- **Round 1:** K45-02 was split again, into 4 parts.
- **Rounds 2-6, split for Chrome:** in `drag_split_next/`, 188 folders and 511 parts. `drag_split_next/ROUNDS.tsv`
  gives each folder's round in send order, and Hua's files are in part 1 of each.
- **Packages:** the 68 packages of rounds 2-6, P124 among them, are in `../packages_moved_to_codex_20261117/`. The
  dot-prefixed packages stay in `../packages/` for Pro. ASSIGNMENTS.tsv has the 188 rows.
