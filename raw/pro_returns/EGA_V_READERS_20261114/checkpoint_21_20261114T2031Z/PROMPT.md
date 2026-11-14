# "Nouveau EGA V" (cote 25) and P. Blass's English translation of part of it (cote 24): a complete check against the scans, French readers, an English translation, Blass's typescript as an English book, and a guide

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Two ZIP files are attached:
`EGA_V_SCANS.zip`, `EGA_V_TEXT.zip`. Each has `MANIFEST.tsv` at its root (path in the zip, source, bytes, SHA-256,
role); read the manifests first. Drafted by Claude Opus 5.5 (Anthropic, effort high) from the records of the
transcription.

## What this is for

Two cotes of the Grothendieck archive of the Université de Montpellier hold the material for the later chapters of
EGA.

**Cote 25**, "Nouveau EGA V": Grothendieck's French prenotes, typed, with many handwritten corrections (the archive
dates the cote "[à partir de 1967-1987]"):

| Sites | What |
|---|---|
| 2-95 | IV 20 "Sections hyperplanes et projections coniques" ("Etat 0"; contents with "Commentaires", then §§1-15) |
| 98-133, 137-138 | IV 21 "Faisceaux inversibles et diviseurs relatifs sur les fibrés projectifs et multiprojectifs; systèmes linéaires" (§§1-4) |
| 134-135 | a letter "Cher Dieudonné", on the table of contents of §§16-19 |
| 140-156 | IV 16 "Un nouveau n° : Ensemble singulier et supersingulier d'une fonction, et critères différentiels", headed "nouveau EGA V" by hand |
| 158-184 | IV 17.15 "Formes lisses" and 17.16 "Formes quadratiques lisses", with "Remords" pages (166-172) |

**Cote 24**: Piotr Blass's English translation typescript of 1987, "EGA V based on notes of Alexandre Grothendieck /
Stage 0 - translation by Piotr Blass": title page, summary, contents §§1-16, then pp. 4-74 of IV 20 §§1-11, with typed
translator queries ("[illegible ask Grothendieck]") and handwritten notes ("Ask AG"); site 75 is a handwritten note in
French; site 76 is the last page of a typed CV, a stray sheet.

Texts named here for orientation only: the Grothendieck Circle's scan `EGA5.pdf` (another copy of the cote 25
document); the English translations of P. and J. Blass (2004) at the Circle; J. C. Reinhold's web re-edition of those;
the Centre for Grothendieckian Studies' L49d (a letter to Dieudonné of 29.09.1965, perhaps the one of sites 134-135).
Nobody has transcribed cote 25.

Every one of these 260 pages was AI-transcribed into diplomatic LaTeX by Claude Opus 5.5 (Anthropic, effort high,
Message Batches API), from the page images in the SCANS zip. No draft was given. Only six pilot pages (cote 24 sites
4, 18, 37; cote 25 sites 2, 4, 140) have been checked by eye.

None of the editions named above is attached, and no reading is taken from any of them: the scans decide.

There are three parts:
- **Part A:** check the transcription against the scans.
- **Part B:** build the readers from the checked transcription.
- **Part C:** write a guide to the text.

## Sources of record

- **Pages** (`EGA_V_TEXT.zip`):
  - `transcription/<text>/pages/<key>.tex`: one file per page, with a comment header giving the cote, the site and the
    PDF page. Keys: `ega25_25_<site>` (cote 25, sites 1-184) and `ega24_24_<site>` (cote 24, sites 1-76).
  - `method/preamble.tex` defines the macros; `method/prompt_system.txt` holds the instructions the transcribing model
    had, with the meaning of each macro, and `method/batch.py` the context paragraph sent with each page (per text and
    per document). The macros are:
    - `\scanpage{cote/site}`: the scan mark;
    - `\mspage{n}`: a page number of the text;
    - `\hand{...}`: handwriting in the line;
    - `\over{typed}{written}`: handwriting over typed characters;
    - `\inserted{...}` (with `[typed]` for a typed insertion): an insertion, set where its mark points;
    - `\margin{...}`: a marginal note;
    - `\deleted{...}`: struck by hand;
    - `\xout{...}`: struck on the typewriter;
    - `\uline{...}` and `\uuline{...}`: underlined and doubly underlined;
    - `\unsure{reading|alternative}`: a doubtful reading;
    - `\illegible{n}`: n words that cannot be read;
    - `\diagram{...}`: a diagram, in tikz-cd.
  - `transcription/<text>/NOTES.tsv`: per page, the places the model asked to be checked by eye, whether the page has
    long handwritten passages, and the counts of doubt marks and handwriting macros.
  - `transcription/<text>/COMPILE_FIXES.tsv`: the pages whose braces the combined file balances.
  - `transcription/<text>/<text>_combined.tex`: all pages in archive order. `ega_v_cote25` does not compile: on 14 Nov
    pdflatex stopped at 100 errors (source line 257, after \scanpage{25/7}). `ega_v_cote24_blass` compiled on 14 Nov
    with pdflatex with 30 LaTeX errors, from which TeX recovered (76 pages; 3 overfull boxes over 2pt). The errors are
    LaTeX syntax, not readings.

- **The records:**
  - `records/PAGES_EGA_V.tsv`: every page with its cote, site (= PDF page - 1), PDF page, page number of the text,
    class (typed, printed, handwritten, by eye), the counts of its marks, its page file, its images and its URL in the
    archive's viewer;
  - `records/API_TYPESCRIPTS_REPORT.md`, `records/NEXT_TEXTS_20261113.md`: how the pages were made, the documents and
    the context given; `records/pilot/`: the pilot of 12 Nov; `records/SPOTCHECK_NEXT_TEXTS_20261113.md`: the spot
    check of 13 Nov against the scans; `records/RUNS_subset.jsonl`: the batches; `records/COMPILE_TEST.md`: the
    compile test of the combined files on 14 Nov.
- **The scans:** `EGA_V_SCANS.zip`: `scans/<key>_a.jpg` and `scans/<key>_b.jpg`, the upper and lower part of each page
  as the transcribing model saw it. The archive's viewer shows a page at
  `https://grothendieck.umontpellier.fr/web/viewer.html?file=../<cote>.pdf#page=<pdf_page>`.
- **Terminology standard:** `standard/STANDARDIZATION_CHECK.md` and `standard/GLOSSARY_SGA_EN_UNIFIED.tsv`, the
  standard of our English readers (13 November 2026). It governs the words of the English translation, the apparatus,
  the records and the guide. It never changes his French or his English.

## Part A: the check

Settle the transcription against the page images, page by page. The check covers:
- **Every doubt mark:** 1,260 `\unsure` and 231 `\illegible`. Where the image settles the reading, write it; where it
  does not, the mark stays, with every candidate the ink allows.
- **Every handwriting macro:** 1,717 `\hand`, 212 `\over`, 770 `\inserted`, 283 `\margin`, 479 `\deleted`, 1,210
  `\xout`. For each, confirm on the image that the hand is there, that the words are right and that the macro is the
  right one; find the handwriting the transcription missed, and the typed special characters it marked as handwriting
  (the spot check found typed script letters and typed arrows taken for handwriting).
- **Every place `NOTES.tsv` lists for a check by eye** (260 pages carry notes; the 15 pages flagged as having long
  handwritten passages are read closely).
- **A complete check, page by page.** No page of these 260 has been checked by eye beyond the six pilot pages, so Part
  A reads every line of every page against its image, not only the marked places: every word, formula, index, arrow,
  reference and handwritten correction, and every place where the handwritten layer (heavy in cote 25: the corrections
  of IV 20, the "Remords" pages) was missed or misplaced. Record each page in `PAGES_CHECKED.tsv` (key, start and end
  time, lines read, number of decisions).
- **The pilot's disputed reading**: k′, or k followed by a handwritten comma (cote 25 site 140).
- **Cote 24 against cote 25**: where Blass's typescript leaves a gap or a query, note in the decision record the
  French passage it translates (by cote 25 site); a cross-reference, not a correction of either text.
- **The known error types, on every page:** a struck word given as live text; E/F, 3/5, u/n, i/j and 1/l in indices;
  an abbreviation written out; a misspelling normalized; a handwritten mark taken for typing or the reverse; a
  letterform of one alphabet read as another (a sans-serif F against a serif F, a script letter against a roman one);
  a description written inside a content macro (it belongs in a `% NOTE:` line).

Record every decision in `CHECK_DECISIONS.tsv`: key, cote, site (or scan), line, the transcription's reading, what the
image shows, the decision, and the reason. Correct the page file wherever the image shows a different reading. The
checked page files are the new source of record: deliver them all, in `checked_pages/<key>.tex`, with the same macros.

## Part B: the readers

Build one book per form and language, each a single LaTeX file that compiles with LuaLaTeX of a standard TeX Live:

| File | Language | Form |
|---|---|---|
| `EGA_V_FR_diplomatique.tex` | French | **Diplomatic**: the checked transcription as it stands, page by page: typed text plain, his handwriting marked (insertions, writing over typing, marginal notes, deletions), typewriter strike-outs, underlining, spelling and typing as on the page, doubt marks, the scan marks and the page numbers of the text |
| `EGA_V_FR_corrige_apparat.tex` | French | **Corrected, with apparatus**: the text he ended with. His deletions leave the running text and go to the apparatus; his insertions and corrections go in, marked; his marginal notes are set as notes at their line. A one-off slip (a doubled word, a transposed or wrong letter that the same word elsewhere shows to be a slip) is corrected only where the context settles it, and the apparatus gives the page's reading, the correction and the reason. Every remaining doubt mark stays marked. The apparatus is in French |
| `EGA_V_FR_texte_de_lecture.tex` | French | **Reading text**: the corrected text without apparatus; doubt marks stay marked and linked; scan and page numbers in the margin only; a short preface says what was left out |
| `EGA_V_EN_corrected_translator_notes.tex` | English | **Corrected, with translator's notes**: the English of the corrected French text, AI-translated, with the apparatus entries in English and a translator's note wherever a French word, a pun, an abbreviation or a notation needs one |
| `EGA_V_EN_reading.tex` | English | **Reading text**: the English of the reading text, as for the French |

The French forms hold cote 25. The diplomatic form keeps the archive order; the corrected and reading forms order the
pieces by EGA number (IV 16, IV 17.15-17.16, IV 20, IV 21) with the letter to Dieudonné as an appendix, and the
preface says so. Cote 24 gets three English books of its own, built the same way from
`EGA_V24_EN_master_annotated.tex`: `EGA_V24_EN_diplomatic.tex`, `EGA_V24_EN_corrected_apparatus.tex` and
`EGA_V24_EN_reading.tex`. They keep Blass's English and his queries; site 75 is kept; site 76 is in the diplomatic
book only, marked as a stray sheet. The apparatus of the cote 24 books may point to the cote 25 site a passage
translates.

**Masters.** Build the French forms from one annotated master (`EGA_V_FR_master_annotated.tex`) and the English forms
from one English annotated master (`EGA_V_EN_master_annotated.tex`), translated from the corrected French text. Mark
every place where the page and the corrected text differ, for instance with a macro `\var{page reading}{corrected
reading}{kind}{source id}`, and generate the forms from the master by switching the macro. Then the forms cannot drift
apart. The English master carries the same variant ids as the French one; a French slip that does not change the
English gets no variant in the English. The formulas of the English are the French's, character for character. Use the
terminology standard (`standard/`) for the English; it never changes his French.

**The clean-up.** First clean the LaTeX of the checked pages mechanically, without changing what prints: the `$...$`
nested inside the handwriting macros in math, the unbalanced braces (`COMPILE_FIXES.tsv` and the compile test),
descriptions inside content macros moved to comment lines. Record what the script did, page by page, in
`CLEANUP_LOG.tsv`.

## Part C: the guide

Write `EGA_V_GUIDE.tex` (with its PDF), in English, a guide for a mathematician reading Grothendieck's "Nouveau EGA V"
and Blass's translation. It is a prose commentary, written as the check of each part is finished, not at the end. Give
a paragraph to each section of IV 16, IV 17.15, IV 17.16, IV 20 and IV 21 in the order of the reading text, to the
"Remords" pages, to the letter to Dieudonné, and to Blass's translation as a whole. For each, one paragraph:
- what it does, or what it says;
- the notions it introduces or uses, with his terms;
- what it takes from the other parts and from other texts of the archive, and where it is taken up;
- where he changes his mind, with the pages.

Cite the published EGA IV by number where these prenotes continue it. For Blass's translation, say what it covers and
where it departs from the French, from the check only. Wherever the check turns up a slip in the mathematics (an
index, an arrow's direction, a hypothesis that another page shows was meant), note it in the guide's paragraph, with
the page, and correct nothing in the text for it.

## Rules

1. **Keep his French and his notation** in every French form. His consistent spellings and usages stay in every form,
   and the reading text's preface lists them. Correct only the one-off slips described above, with the reason. Never
   standardize notation silently; you may write one consistent macro set, but it must not change what prints. The
   English translation translates the corrected text; it adds nothing and explains in translator's notes only.
2. **No reading changes without a record.** Every change to a page is a row of `CHECK_DECISIONS.tsv`. Every difference
   between the diplomatic and the corrected form is a variant in the master, with a kind (deletion, insertion, writing
   over, slip corrected, marginal note placed) and a source id. A doubt mark is removed only where the image settles
   the reading.
3. **Links.** In every reader, every `\unsure{...}`, every `\illegible{n}` and every scan mark is a link to its page
   in the archive's viewer, by the URL pattern above, with the PDF page from `records/PAGES_EGA_V.tsv`. Count the
   links of each PDF and compare the counts with the marks of its source; the number of distinct pages linked from
   each cote is its number of pages in this work.
4. **Marginal notes.** A note that fits in the margin in three lines stays in the margin. Every other note is set in
   the text block at the place it belongs to, and reads as a marginal note (small type, a rule, a label). No note is
   dropped, cut or moved to another page than its line's without a mark at that line.
5. **Typesetting, repaired in the source.** A wide diagram gets column and row separations, a font size and, where it
   has to be, line breaks in its entries that let it fit. A diagram that at 70 % of its size is still wider than the
   line is turned onto a landscape page or split into parts joined by repeated objects, and the apparatus says so. A
   wide display is broken where the mathematics breaks. A formula in running text that cannot break gets breakpoints
   or moves to a display line with a mark. A blanket scaling pass over the book is not a repair. Record every place in
   `TYPESETTING_FIXES.tsv` (reader, page key, source line, what was wrong, what was done).
6. **Credit and rights.** Each reader's front matter and the guide's carry:
   - the author, the title, the date, the archive (Université de Montpellier, fonds Grothendieck) and the cotes;
   - "AI-transcribed by Claude Opus 5.5 (Anthropic, effort high, Message Batches API); checked against the scans, and
     this edition built, by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic)"; in the
     English translation also "AI-translated by GPT-6 Astra (OpenAI, ChatGPT Pro mode)". Never "AI-assisted";
   - in the cote 24 books: "The translation in cote 24 is Piotr Blass's (1987); the rights in it belong to its
     translator or his heirs.";
   - the texts named above, as published texts not reproduced and not consulted for any reading;
   - this rights statement, word for word, in English: "The rights in the original work belong to its author or the
     author's representatives or heirs. Where we hold rights, in the AI-produced transcription, translation,
     corrections and typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for
     educational, non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and
     object to its publication here, please open a GitHub issue and we will take it down."
   - and in the French readers also in French: « Les droits sur l'œuvre originale appartiennent à son auteur, à ses
     représentants ou à ses ayants droit. Dans la mesure où nous détenons des droits sur la transcription, la
     traduction, les corrections et la composition produites par l'IA, nous les consacrons au domaine public sous CC0
     1.0. Cette édition est publiée à des fins éducatives et non lucratives, et nous ne revendiquons aucun droit que
     nous ne détenons pas. Si vous détenez des droits sur cette œuvre et vous opposez à sa publication ici, veuillez
     ouvrir une issue GitHub et nous la retirerons. »
7. **Privacy.** Never copy a local file path into a reader or a record; refer to files by their path inside the ZIP.
   Copy no e-mail address.

## What to deliver

Deliver `EGA_V_READERS_FR.zip`, `EGA_V_READERS_EN.zip` and `EGA_V_READERS_RECORDS.zip`:

- the 8 reader `.tex` files, the annotated masters and the guide, each with its PDF;
- `checked_pages/<key>.tex`: all 260 checked page files;
- `CHECK_DECISIONS.tsv` and `PAGES_CHECKED.tsv`;
- `CHANGES.tsv`: every difference between the corrected reader and the diplomatic one (cote, site or scan, place, page
  reading, corrected reading, kind, reason);
- `APPARATUS_COUNTS.md`: per cote and form, the number of apparatus entries by kind;
- `CLEANUP_LOG.tsv` and `TYPESETTING_FIXES.tsv`;
- `TYPESETTING_REPORT.md`, giving for each PDF:
  - the overfull boxes of its log (count, and the widest);
  - the pages with ink outside the sheet or the type area;
  - the missing characters;
  - the number of links;
  - the pages you rendered and looked at, with what you saw on each;
- `README.md`: what each file is, how each form was made, the counts (decisions by outcome, doubt marks before and
  after, apparatus entries, translator's notes), and the compile status of each reader with its LaTeX errors and
  warnings;
- your build scripts, with their outputs.

## When it is done

Do everything: every page checked, every fix integrated, every form built, the translation made, the guide written,
and the records complete.

**Each item is done when:**
- **The check:** every `\unsure` and `\illegible` of the 260 pages is settled on the image or still marked; every
  handwriting macro is confirmed or corrected; every place of the notes has its row in `CHECK_DECISIONS.tsv`; every
  one of the 260 pages has its row in `PAGES_CHECKED.tsv`, read line by line.
- **A reader** compiles with LuaLaTeX without errors. It holds the text of every page it is meant to hold, checked by
  script against `checked_pages/`, with the counts in the README, and its scan marks agree with `\scanpage` in the
  pages. The English readers hold every part of the corrected form that is translated, in English.
- **The apparatus** has one entry for each difference between the diplomatic and the corrected form, and none for
  anything else.
- **Typesetting.** The log of every PDF has no overfull box wider than 2pt, whether a diagram, a display or a line of
  text, and no missing character. No page has ink beyond the sheet, and none has ink outside the type area except the
  overhang of a single letter. You have rendered to images and looked at every page that had an overflow in any build,
  every landscape page, and forty pages spread evenly over each reader.
- **Links.** Every doubt mark and scan mark of every reader is a link to its page, and the counts are in the report.
- **The guide** has its paragraph for every section, for the "Remords" pages, for the letter and for Blass's
  translation.

**Not acceptable:**
- a reader that drops, summarizes or paraphrases any part of the text;
- a correction in one form and missing from another;
- a reading changed without a row in `CHECK_DECISIONS.tsv`, or a doubt mark removed where the image does not settle
  it;
- a reading taken from a published edition, or from memory of one, instead of the image;
- an apparatus entry without a kind and a reason;
- a silent change of notation, or his spelling standardized;
- a translation that adds, drops or explains in the text what the French does not say;
- a diagram or formula made to fit by a scale below 70 %, or by a scaling pass over the whole book;
- a box wider than the line by more than 2pt left in a log, or hidden by raising `\hfuzz`;
- a page marked as checked whose lines were not all read against the image.
- local paths or e-mail addresses in any output.

**The task is finished** only when the checked pages, the decision records, the readers, the masters and the guide
with their PDFs, the clean-up and typesetting records and report, and the README are in the ZIPs, and every condition
above holds.

## Working method

- Start from the manifests, `records/PAGES_EGA_V.tsv` and both `NOTES.tsv`.
- Check cote 25 in archive order, then cote 24. For each page, open both parts of its image and the marks and notes of
  that page, and decide each place on the image. Write the decisions and the corrected page file as you go.
- Clean the LaTeX of the pages mechanically without changing what prints, and record what the script did.
- Build the masters by script from the checked pages, translate the corrected text into the English master, generate
  the forms, compile, and check the counts.
- Repair the typesetting place by place, largest overflow first.
- Write the guide's paragraph for a part as soon as its check is finished.
- After every section of cote 25 (and cote 24) of the check and every finished reader, save a checkpoint ZIP of
  everything so far to the user's Library, or wherever files survive the loss of the execution environment. Save the
  final ZIPs there too.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so
  that an interruption loses little.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no
overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the
source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to
images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts
before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every section of cote 25 (and cote 24) of the check and
every finished reader, each under a new name, `EGA_V_READERS_checkpoint_<NN>.zip` with `NN` counting up; never
overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If the
workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The
final ZIPs hold everything the checkpoints held: a file or passage left out of the final is listed in the report with
the reason (superseded by which file, or wrong).
Save one also whenever an hour of work has passed since the last checkpoint, whichever comes first. A checkpoint is
one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs,
scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave
the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file,
a recovery file, a summary, or an export of the newest pages only. The checkpoints are what keeps the work if this
session dies: work that is in no checkpoint is lost.

## If the execution environment fails

If the workspace disconnects or an attached ZIP cannot be opened, wait and retry for ten minutes. If it does not come
back, write the work out in the chat as text:
- the decision records, the change log, the README and the report so far, each in full in its own code block headed by
  its file name;
- your build scripts in full, so that the readers can be rebuilt from the attached sources;
- which parts are checked, which readers are finished, and where their checkpoints are.

Then continue the remaining work in the chat in the same form until every part is written. An answer that only reports
the failure or asks for the files again is not acceptable.

