# Esquisse d'un programme (1984): the two typescript copies of cote 119 checked against their scans and collated, French readers, an English translation, and a guide

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Two ZIP files are attached:
`ESQUISSE_SCANS.zip`, `ESQUISSE_TEXT.zip`. Each has `MANIFEST.tsv` at its root (path in the zip, source, bytes,
SHA-256, role); read the manifests first. Drafted by Claude Opus 5.5 (Anthropic, effort high) from the records of the
transcription.

## What this is for

Alexander Grothendieck's *Esquisse d'un programme*, the research programme he wrote in January 1984 for his
application to the CNRS, is kept in the Grothendieck archive of the Université de Montpellier, cote 119, in two copies
of the same typing: a sommaire and 57 typed pages (§§1-10, footnotes (*) and (**), and the notes (1)-(7) "rajoutées
ultérieurement" at the end, pp. 52-57). Language: French.

| Copy | Sites | PDF pages | What |
|---|---|---|---|
| 1 | 2-59 | 3-60 | the sommaire (site 2) and typescript pp. 1-57 (page n = site n+2); few annotations (the handwritten numbers in the N.B.) |
| 2 | 78-135 | 79-136 | the same typing (copy 2 site = copy 1 site + 76); handwriting of its own: on p. 1 the title and the author's name are struck through, and there are corrections, insertions and margin signs |

Published editions, named here for orientation only: the French text and an English translation in *Geometric Galois
Actions 1* (ed. L. Schneps and P. Lochak, Cambridge University Press, 1997); the Grothendieck Circle's typeset
`EsquisseFr.pdf`; the Centre for Grothendieckian Studies' draft transcription G94d. They normalize and correct his
text, and none records the handwriting of the copies.

Every one of these 116 pages was AI-transcribed into diplomatic LaTeX by Claude Opus 5.5 (Anthropic, effort high,
Message Batches API), from the page images in the SCANS zip. Copy 1 was given the text layer of the Circle's typeset
PDF as a draft, to compare with after transcribing the page; copy 2 was given copy 1's transcription.
`DIFFERENCES.tsv` lists where each page departs from its draft. Only the pilot and spot-check pages have been checked
by eye.

None of the editions named above is attached, and no reading is taken from any of them: the scans decide.

There are three parts:
- **Part A:** check the transcription against the scans.
- **Part B:** build the readers from the checked transcription.
- **Part C:** write a guide to the text.

## Sources of record

- **Pages** (`ESQUISSE_TEXT.zip`):
  - `transcription/<text>/pages/<key>.tex`: one file per page, with a comment header giving the cote, the site and the
    PDF page. Keys: `esq_119_<site>` (copy 1, sites 2-59) and `esq119_119_<site>` (copy 2, sites 78-135).
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
  - `transcription/<text>/<text>_combined.tex`: all pages in archive order. `esquisse` compiled on 14 Nov with
    pdflatex with 35 LaTeX errors, from which TeX recovered (58 pages; 10 overfull boxes over 2pt). `esquisse_copy2`
    compiled on 14 Nov with pdflatex with 35 LaTeX errors, from which TeX recovered (58 pages; 10 overfull boxes over
    2pt). The errors are LaTeX syntax, not readings.
- **The differences:** `transcription/esquisse/DIFFERENCES.tsv` (327 rows: copy 1 against the Circle text; 152
  normalization, 95 silent-correction, 27 wording, 17 hand-unmarked, 13 omission) and
  `transcription/esquisse_copy2/DIFFERENCES.tsv` (141 rows: copy 2 against copy 1's transcription). Each row: key,
  cote, site, typescript page, class, the draft's text, the page's text, a note. The draft quotations are records, not
  sources.
- **The records:**
  - `records/PAGES_ESQUISSE.tsv`: every page with its cote, site (= PDF page - 1), PDF page, page number of the text,
    class (typed, printed, handwritten, by eye), the counts of its marks, its page file, its images and its URL in the
    archive's viewer;
  - `records/API_TYPESCRIPTS_REPORT.md`, `records/NEXT_TEXTS_20261113.md`: how the pages were made, the documents and
    the context given; `records/pilot/`: the pilot of 12 Nov; `records/SPOTCHECK_NEXT_TEXTS_20261113.md`: the spot
    check of 13 Nov against the scans; `records/RUNS_subset.jsonl`: the batches; `records/COMPILE_TEST.md`: the
    compile test of the combined files on 14 Nov.
- **The scans:** `ESQUISSE_SCANS.zip`: `scans/<key>_a.jpg` and `scans/<key>_b.jpg`, the upper and lower part of each
  page as the transcribing model saw it. The archive's viewer shows a page at
  `https://grothendieck.umontpellier.fr/web/viewer.html?file=../<cote>.pdf#page=<pdf_page>`.
- **Terminology standard:** `standard/STANDARDIZATION_CHECK.md` and `standard/GLOSSARY_SGA_EN_UNIFIED.tsv`, the
  standard of our English readers (13 November 2026). It governs the words of the English translation, the apparatus,
  the records and the guide. It never changes his French or his English.

## Part A: the check

Settle the transcription against the page images, page by page. The check covers:
- **Every doubt mark:** 25 `\unsure` and 1 `\illegible`. Where the image settles the reading, write it; where it does
  not, the mark stays, with every candidate the ink allows.
- **Every handwriting macro:** 71 `\hand`, 7 `\over`, 6 `\inserted`, 129 `\margin`, 9 `\deleted`, 0 `\xout`. For each,
  confirm on the image that the hand is there, that the words are right and that the macro is the right one; find the
  handwriting the transcription missed, and the typed special characters it marked as handwriting (the spot check
  found typed script letters and typed arrows taken for handwriting).
- **Every place `NOTES.tsv` lists for a check by eye** (116 pages carry notes).
- **Every row of both DIFFERENCES tables**: decide on the image what the page shows.
- **The full collation of copy 1 against copy 2**, page by page (copy 2 site = copy 1 site + 76): every typed
  difference and every handwritten mark of either copy, recording which reading each copy has, in `COLLATION.tsv`
  (typescript page, line, copy 1 reading, copy 2 reading, kind: typed difference, misreading in one transcription,
  handwriting only in copy 1, handwriting only in copy 2; decision). Copy 2's handwriting is the point of copy 2: the
  struck title and author on p. 1, the corrections, insertions and margin signs; the probable pen dot in the margin of
  site 123 (spot check) is settled on the image.
- **The pilot's miss**: the handwritten 1 and 7 in the N.B. of copy 1, typed in the transcription without the
  handwriting mark.
- **The known error types, on every page:** a struck word given as live text; E/F, 3/5, u/n, i/j and 1/l in indices;
  an abbreviation written out; a misspelling normalized; a handwritten mark taken for typing or the reverse; a
  letterform of one alphabet read as another (a sans-serif F against a serif F, a script letter against a roman one);
  a description written inside a content macro (it belongs in a `% NOTE:` line).

Record every decision in `CHECK_DECISIONS.tsv`: key, cote, site (or scan), line, the transcription's reading, what the
image shows, the decision, and the reason. Correct the page file wherever the image shows a different reading. The
checked page files are the new source of record: deliver them all, in `checked_pages/<key>.tex`, with the same macros.
Then give every DIFFERENCES row its outcome in `DIFFERENCES_OUTCOMES.tsv` (the row's columns plus `outcome` and
`reason`): the typescript reads as our transcription; our transcription corrected; the draft departs (normalizes,
corrects, adds or omits). This file is the record of where the Circle text departs from the typescript.

## Part B: the readers

Build one book per form and language, each a single LaTeX file that compiles with LuaLaTeX of a standard TeX Live:

| File | Language | Form |
|---|---|---|
| `ESQUISSE_FR_diplomatique.tex` | French | **Diplomatic**: the checked transcription as it stands, page by page: typed text plain, his handwriting marked (insertions, writing over typing, marginal notes, deletions), typewriter strike-outs, underlining, spelling and typing as on the page, doubt marks, the scan marks and the page numbers of the text |
| `ESQUISSE_FR_corrige_apparat.tex` | French | **Corrected, with apparatus**: the text he ended with. His deletions leave the running text and go to the apparatus; his insertions and corrections go in, marked; his marginal notes are set as notes at their line. A one-off slip (a doubled word, a transposed or wrong letter that the same word elsewhere shows to be a slip) is corrected only where the context settles it, and the apparatus gives the page's reading, the correction and the reason. Every remaining doubt mark stays marked. The apparatus is in French |
| `ESQUISSE_FR_texte_de_lecture.tex` | French | **Reading text**: the corrected text without apparatus; doubt marks stay marked and linked; scan and page numbers in the margin only; a short preface says what was left out |
| `ESQUISSE_EN_corrected_translator_notes.tex` | English | **Corrected, with translator's notes**: the English of the corrected French text, AI-translated, with the apparatus entries in English and a translator's note wherever a French word, a pun, an abbreviation or a notation needs one |
| `ESQUISSE_EN_reading.tex` | English | **Reading text**: the English of the reading text, as for the French |

The base text is copy 1. The diplomatic reader gives copy 1 in full, then copy 2 in full, each page with its scan
mark. The corrected and reading forms follow copy 1's typed text with his corrections; copy 2's corrections and marks
go into the apparatus as "copy 2 has", and enter the corrected text only where they correct a typing slip that both
copies share, with the apparatus saying so. The footnotes (*) and (**) stay at their page; the notes (1)-(7) stay at
the end, where the typescript has them, linked both ways from their calls.

**Masters.** Build the French forms from one annotated master (`ESQUISSE_FR_master_annotated.tex`) and the English
forms from one English annotated master (`ESQUISSE_EN_master_annotated.tex`), translated from the corrected French
text. Mark every place where the page and the corrected text differ, for instance with a macro `\var{page
reading}{corrected reading}{kind}{source id}`, and generate the forms from the master by switching the macro. Then the
forms cannot drift apart. The English master carries the same variant ids as the French one; a French slip that does
not change the English gets no variant in the English. The formulas of the English are the French's, character for
character. Use the terminology standard (`standard/`) for the English; it never changes his French.

**The clean-up.** First clean the LaTeX of the checked pages mechanically, without changing what prints: the `$...$`
nested inside the handwriting macros in math, the unbalanced braces (`COMPILE_FIXES.tsv` and the compile test),
descriptions inside content macros moved to comment lines. Record what the script did, page by page, in
`CLEANUP_LOG.tsv`.

## Part C: the guide

Write `ESQUISSE_GUIDE.tex` (with its PDF), in English, a guide for a mathematician reading the *Esquisse d'un
programme*. It is a prose commentary, written as the check of each part is finished, not at the end. Give a paragraph
to the sommaire, to each of §§1-10, and to the notes (1)-(7), in order. For each, one paragraph:
- what it does, or what it says;
- the notions it introduces or uses, with his terms;
- what it takes from the other parts and from other texts of the archive, and where it is taken up;
- where he changes his mind, with the pages.

Begin with a short preface on the two copies: what copy 2's handwriting is, the struck title and author, and what the
collation found. Where an item of the programme is taken up in other texts of the archive (*La Longue Marche à travers
la théorie de Galois*, cotes 119-121, 18, 138) or in later literature, name them only. Wherever the check turns up a
slip in the mathematics (an index, an arrow's direction, a hypothesis that another page shows was meant), note it in
the guide's paragraph, with the page, and correct nothing in the text for it.

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
   in the archive's viewer, by the URL pattern above, with the PDF page from `records/PAGES_ESQUISSE.tsv`. Count the
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
   - the editions named above, as published texts, not reproduced;
   - for copy 1: "The transcription of copy 1 was made with the text layer of the Grothendieck Circle's typeset
     *Esquisse* (`EsquisseFr.pdf`) given to the transcribing model as a draft, to compare with after it had
     transcribed each page; every reading of this edition was decided on the scans.";
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

Deliver `ESQUISSE_READERS_FR.zip`, `ESQUISSE_READERS_EN.zip` and `ESQUISSE_READERS_RECORDS.zip`:

- the 5 reader `.tex` files, the annotated masters and the guide, each with its PDF;
- `checked_pages/<key>.tex`: all 116 checked page files;
- `CHECK_DECISIONS.tsv`, `COLLATION.tsv` and `DIFFERENCES_OUTCOMES.tsv`;
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
- **The check:** every `\unsure` and `\illegible` of the 116 pages is settled on the image or still marked; every
  handwriting macro is confirmed or corrected; every place of the notes has its row in `CHECK_DECISIONS.tsv`; every
  DIFFERENCES row has its outcome; every typescript page has its collation of the two copies.
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
- **The guide** has its paragraph for every section, for the sommaire and for the notes.

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
- a difference between the copies settled without looking at both images.
- local paths or e-mail addresses in any output.

**The task is finished** only when the checked pages, the decision records, the readers, the masters and the guide
with their PDFs, the clean-up and typesetting records and report, and the README are in the ZIPs, and every condition
above holds.

## Working method

- Start from the manifests, `records/PAGES_ESQUISSE.tsv`, both `NOTES.tsv` and both `DIFFERENCES.tsv`.
- Check copy 1 in typescript order, then copy 2 against copy 1, page by page. For each page, open both parts of its
  image and the marks and notes of that page, and decide each place on the image. Write the decisions and the
  corrected page file as you go.
- Clean the LaTeX of the pages mechanically without changing what prints, and record what the script did.
- Build the masters by script from the checked pages, translate the corrected text into the English master, generate
  the forms, compile, and check the counts.
- Repair the typesetting place by place, largest overflow first.
- Write the guide's paragraph for a part as soon as its check is finished.
- After every ten typescript pages of the check and every finished reader, save a checkpoint ZIP of everything so far
  to the user's Library, or wherever files survive the loss of the execution environment. Save the final ZIPs there
  too.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so
  that an interruption loses little.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no
overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the
source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to
images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts
before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every ten typescript pages of the check and every finished
reader, each under a new name, `ESQUISSE_READERS_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename
or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If the workspace comes back
empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIPs hold
everything the checkpoints held: a file or passage left out of the final is listed in the report with the reason
(superseded by which file, or wrong).
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

