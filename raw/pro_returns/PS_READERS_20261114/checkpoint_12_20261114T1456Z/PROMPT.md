# Pursuing Stacks (1983): the typescript checked against its scans and the arXiv edition, three English readers, and a guide

You are GPT-6 Astra in ChatGPT Pro mode, with a Python and LaTeX environment. Three ZIP files are attached:
`PS_TEXT.zip`, `PS_SCANS_1.zip` and `PS_SCANS_2.zip`. Each has `MANIFEST.tsv` at its root (path in the zip, source,
bytes, SHA-256, role); read the manifests first. Drafted by Claude Opus 5.5 (Anthropic, effort max) from the records of
the transcription.

## What this is for

Alexander Grothendieck's *Pursuing Stacks* (1983) is kept in the Grothendieck archive of the Université de Montpellier
as a typescript with his handwritten corrections, insertions and marginal notes, in seven cotes: 680 pages.

| Cote | Pages (sites) | What |
|---|---|---|
| 134-2 | 81 (sites 1–81) | front matter, the letter to Quillen, letters and notes |
| 134-3 | 93 (sites 1–93) | typescript pages 1–88 |
| 134-4 | 99 (sites 1–100) | typescript pages 89–187 |
| 134-5 | 132 (sites 1–132) | typescript pages 188–319 |
| 134-6 | 124 (sites 1–124) | typescript pages 320–442 |
| 134-7 | 112 (sites 1–112) | typescript pages 443–554 |
| 134-8 | 39 (sites 1–39) | typescript pages 555–593 |

Cote 134-2 also holds, at sites 115–143 (26 pages), R. Brown's typed English translation of the mathematical part of
two letters from Grothendieck to L. Breen of 1975, with Brown's note and comments. His note says it was prepared
"with assistance from L. Breen (Rennes) and also from J-L. Loday (Strasbourg)". Grothendieck reprinted the translation,
with corrections, as the appendix of *Pursuing Stacks*.

Every one of these 706 pages was AI-transcribed into diplomatic LaTeX by Claude Opus 5.5 (Anthropic, effort high,
Message Batches API, 12–13 November 2026) from the page images. The model was given the passage of the arXiv edition
for the same page as a draft, transcribed the page first, and then listed every difference. No page has yet been
checked by eye. The arXiv edition is the LaTeX of Mateo Carmona with the collaboration of Ulrik Buchholtz (arXiv
2111.01000 v2, 2021), an extended version of the 2015 edition by "the scrivener"; it is dedicated to the public domain
(CC0 1.0). It normalizes spelling, merges the handwritten layer into the text without marks, corrects silently and adds
its editors' comments. So it is a witness to check against, not the source.

There are three parts:
- **Part A:** check the transcription against the scans, using the arXiv text as the witness.
- **Part B:** build the readers from the checked transcription.
- **Part C:** write a guide to the text.

## Sources of record

- **Pages** (`PS_TEXT.zip`):
  - `transcription/ps_pages/<key>.tex` and `transcription/brown_pages/<key>.tex`: one file per page, with a comment
    header giving the cote, the site and the PDF page. The key is `ps_<cote>_<site>` or `brown_134-2_<site>`.
  - `transcription/preamble.tex` defines the macros; `transcription/prompt_system.txt` holds the instructions the
    transcribing model had, with the meaning of each macro. They are:
    - `\scanpage{cote/site}`: the scan mark;
    - `\mspage{n}`: his page number;
    - `\hand{...}`: handwriting in the line;
    - `\over{typed}{written}`: handwriting over typed characters;
    - `\inserted{...}`: a handwritten insertion, set where its mark points;
    - `\margin{...}`: a marginal note;
    - `\deleted{...}`: struck by hand;
    - `\xout{...}`: struck on the typewriter;
    - `\uline{...}` and `\uuline{...}`: underlined and doubly underlined;
    - `\unsure{reading|alternative}`: a doubtful reading;
    - `\illegible{n}`: n words that cannot be read;
    - `\diagram{...}`: a diagram, in tikz-cd.
  - `transcription/ps_NOTES.tsv` and `brown_NOTES.tsv`: per page, the places the model asked to be checked by eye,
    whether the page has long handwritten passages, and the counts of doubt marks and handwriting macros.
  - `transcription/ps_DIFFERENCES.tsv` and `brown_DIFFERENCES.tsv`: per page, the differences from the draft.
  - `transcription/*_COMPILE_FIXES.tsv`: the pages whose braces the combined files balance.
  - `transcription/pursuing_stacks_combined.tex`: all pages in archive order. It stops compiling at 134-2/53, where
    `$...$` nested in the handwriting macros reaches TeX's error limit; a mechanical clean-up is part of Part B.
- **The comparison:** `records/PS_ARXIV_DIFF.tsv`, 12,140 rows. Each row gives:
  - the arXiv file, line, section and paragraph;
  - the arXiv text, and the page's reading;
  - the kind;
  - the typescript page, the cote, the site, the PDF page and the page key.

  The kinds and their counts:

  | Kind | Rows |
  |---|---:|
  | handwritten material printed unmarked | 5,419 |
  | normalization | 2,925 |
  | silent correction | 1,191 |
  | wording | 627 |
  | formula | 486 |
  | handwriting on the page absent from the arXiv text, or a handwritten deletion not applied | 463 |
  | addition | 367 |
  | omission | 334 |
  | handwriting rewritten in the arXiv text | 144 |
  | other | 130 |
  | struck text printed as live text | 53 |
  | unparsed | 1 |
- **The method:**
  - `records/API_TYPESCRIPTS_REPORT.md`: how the pages were made, and the pilot;
  - `records/pilot/`: the check of 184 known differences, of which the method caught 178;
  - `records/PAGES_PS.json`: every page's cote, site, PDF page and typescript page.

  The report's known residual errors: a struck word left live, a misspelling normalized where the draft normalizes
  it, E/F and 3/5 confusions.
- **The arXiv edition:** `arxiv/`, its complete LaTeX source with its licence:
  - `ps.tex` is the main file, and `ps1.tex`–`ps7.tex` are its seven chapters;
  - `\pspage{n}` marks where the editors placed typescript page n (it can be off by a few words);
  - `\scrcomment{...}` is the editors' own comment.
- **The scans:** `PS_SCANS_1.zip` (cotes 134-2, 134-3, 134-4, with Brown's pages) and `PS_SCANS_2.zip` (134-5 to
  134-8): `scans/<key>_a.jpg` and `scans/<key>_b.jpg`, the upper and lower half of each page as the transcribing
  model saw it. The archive's viewer shows a page at
  `https://grothendieck.umontpellier.fr/web/viewer.html?file=../<cote>.pdf#page=<pdf_page>`.
- **Terminology standard:** `standard/STANDARDIZATION_CHECK.md` and `standard/GLOSSARY_SGA_EN_UNIFIED.tsv`, the
  standard of our English readers (13 November 2026). It governs the words of your apparatus, records and guide. It
  never changes his English.

## Part A: the check

Settle the transcription against the page images, page by page:
- **Every row of `PS_ARXIV_DIFF.tsv` whose kind needs a decision:** wording, formula, addition, omission, other,
  handwriting absent from the arXiv text, handwriting rewritten in the arXiv text, struck text printed, unparsed.
  That is 2,605 rows on 644 pages. Look at the place on the image and decide what the typescript shows: the
  transcription's reading, the arXiv reading, or a third reading.
- **Every `\unsure` and every `\illegible`:** 2,766 and 659 in Pursuing Stacks, 8 `\unsure` in Brown's pages. Where
  the image settles the reading, write it; where it does not, the mark stays.
- **Every place `*_NOTES.tsv` lists for a check by eye.** Read closely the 53 pages with 4 or more `\illegible` or
  12 or more `\unsure`, and the 18 pages with long handwritten passages.
- **The known error types on every page:** a struck word given as live text, E/F and 3/5, an abbreviation written
  out, a handwritten mark taken for typing or the reverse.

Record every decision in `CHECK_DECISIONS.tsv`: key, cote, site, line, the transcription's reading, what the image
shows, the arXiv reading, the decision, and the reason. Correct the page file wherever the image shows a different
reading. The checked page files are the new source of record: deliver them all, in `checked_pages/<key>.tex`, with
the same macros.

Then give every one of the 12,140 rows its outcome in `ARXIV_CONCORDANCE.tsv` (the row's columns plus `outcome`
and `reason`). The outcomes are:
- the typescript reads as our transcription;
- our transcription corrected;
- the arXiv text normalizes, corrects, merges handwriting, adds or omits.

This file is the record of where the arXiv edition departs from the typescript.

## Part B: the readers

Build one book per form, each a single LaTeX file that compiles with LuaLaTeX of a standard TeX Live:

| File | Form |
|---|---|
| `PS_EN_diplomatic.tex` | **Diplomatic**: the checked transcription as it stands, cote by cote and page by page: the typed text plain, his handwriting marked (insertions, writing over typing, marginal notes, deletions), typewriter strike-outs, underlining, spelling and typing as typed, doubt marks, the scan marks and his page numbers |
| `PS_EN_corrected_apparatus.tex` | **Corrected, with apparatus**: the text he ended with. His handwritten deletions leave the running text and go to the apparatus; his insertions and corrections go in, marked; his marginal notes are set as notes at their line. A one-off typing slip (a doubled word, a transposed or wrong letter that the same word elsewhere shows to be a slip) is corrected only where the context settles it, and the apparatus gives the typescript's reading, the correction and the reason. Every remaining doubt mark stays marked |
| `PS_EN_reading.tex` | **Reading text**: the corrected text without apparatus; doubt marks stay marked and linked; scan and page numbers in the margin only; a short preface says what was left out |

Brown's translation is an appendix of each reader, in the same three forms, headed with the cote and the sites.

**Build the forms from one annotated master** (`PS_EN_master_annotated.tex`). Mark every place where the typescript
and the corrected text differ, for instance with a macro `\var{typescript}{corrected}{kind}{source id}`, and generate
the three forms from the master by switching the macro. Then the forms cannot drift apart.

## Part C: the guide

Write `PS_GUIDE.tex` (with its PDF), a guide for a mathematician reading *Pursuing Stacks*. For every section of the
typescript, in order, give one paragraph:
- what the section does;
- the notions it introduces, with his terms;
- what it takes from earlier sections, and where later sections use it;
- where he changes his mind, with the pages.

Add the same kind of paragraph for the front matter, the letter to Quillen, and Brown's translation. Wherever the
check of Part A turns up a slip in his mathematics (an index, an arrow's direction, a hypothesis that a later page
shows he meant), note it in the guide's paragraph, with the page, and correct nothing in the text for it. Name the
places where the typescript and the arXiv edition differ in a way that matters for the mathematics. Write the guide
as you finish the check of each section, not at the end.

## Rules

1. **Keep his English and his notation** in every form. His consistent spellings and usages are his English and stay
   in every form, for instance "standart", "developped", "it's" for "its", "A la"; the reading text's preface lists
   them. Correct only the one-off slips described above, with the reason. Never standardize notation silently; you
   may write one consistent macro set, but it must not change what prints.
2. **No reading changes without a record.** Every change to a page is a row of `CHECK_DECISIONS.tsv`. Every
   difference between the diplomatic and the corrected form is a variant in the master, with a kind (deletion,
   insertion, writing over, slip corrected, marginal note placed) and a source id. A doubt mark is removed only where
   the image settles the reading.
3. **Links.** In every reader, every `\unsure{...}`, every `\illegible{n}` and every scan mark is a link to its page
   in the archive's viewer, by the URL pattern above, with the PDF page from `records/PAGES_PS.json`. Count the links
   of each PDF and compare the counts with the marks of its source; the number of distinct pages linked from each
   cote is its number of pages.
4. **Marginal notes.** A note that fits in the margin in three lines stays in the margin. Every other note is set in
   the text block at the place it belongs to, and reads as a marginal note (small type, a rule, a label). No note is
   dropped, cut or moved to another page than its line's without a mark at that line.
5. **Typesetting, repaired in the source.** A wide diagram gets column and row separations, a font size and, where
   it has to be, line breaks in its entries that let it fit. A diagram that at 70 % of its size is still wider than
   the line is turned onto a landscape page or split into parts joined by repeated objects, and the apparatus says so.
   A wide display is broken where the mathematics breaks. A formula in running text that cannot break gets
   breakpoints or moves to a display line with a mark. A blanket scaling pass over the book is not a repair. Record
   every place in `TYPESETTING_FIXES.tsv` (reader, page key, source line, what was wrong, what was done).
6. **Credit and rights.** Each reader's front matter and the guide's carry:
   - the author, the title, the year, the archive and the cotes;
   - "AI-transcribed by Claude Opus 5.5 (Anthropic, effort high); checked against the scans, and this edition built,
     by GPT-6 Astra (OpenAI, ChatGPT Pro mode); prompts and records by Claude (Anthropic)". Never "AI-assisted";
   - the witness consulted and not reproduced: the LaTeX edition of Mateo Carmona with the collaboration of Ulrik
     Buchholtz (arXiv 2111.01000 v2, 2021), extended from the 2015 edition by "the scrivener", CC0 1.0;
   - for the appendix: "The translation in the appendix is R. Brown's, prepared with assistance from L. Breen and
     J-L. Loday, as his note says; the rights in it belong to its translator or his heirs.";
   - this rights statement, word for word: "The rights in the original work belong to its author or the author's
     representatives or heirs. Where we hold rights, in the AI-produced transcription, translation, corrections and
     typesetting, they are dedicated to the public domain under CC0 1.0. This edition is published for educational,
     non-profit purposes, and we claim no rights we do not hold. If you hold rights in this work and object to its
     publication here, please open a GitHub issue and we will take it down."
7. **Privacy.** Never copy a local file path into a reader or a record; refer to files by their path inside the ZIP.
   Copy no e-mail address.

## What to deliver

Deliver `PS_READERS_EN.zip` and `PS_READERS_RECORDS.zip`:

- the three reader `.tex` files, the annotated master and the guide, each with its PDF;
- `checked_pages/<key>.tex`: all 706 checked page files;
- `CHECK_DECISIONS.tsv` and `ARXIV_CONCORDANCE.tsv`;
- `CHANGES_EN.tsv`: every difference between the corrected reader and the diplomatic one (cote, site, place,
  typescript reading, corrected reading, kind, reason);
- `APPARATUS_COUNTS.md`: per cote and form, the number of apparatus entries by kind;
- `TYPESETTING_FIXES.tsv`;
- `TYPESETTING_REPORT.md`, giving for each PDF:
  - the overfull boxes of its log (count, and the widest);
  - the pages with ink outside the sheet or the type area;
  - the missing characters;
  - the number of links;
  - the pages you rendered and looked at, with what you saw on each;
- `README.md`: what each file is, how each form was made, the counts (decisions by outcome, doubt marks before and
  after, apparatus entries), and the compile status of each reader with its LaTeX errors and warnings;
- your build scripts, with their outputs.

## When it is done

Do everything: every page checked, every fix integrated, every form built, the guide written, and the records
complete.

**Each item is done when:**
- **The check:** every row of `PS_ARXIV_DIFF.tsv` has its outcome, every row of the decision kinds has its row in
  `CHECK_DECISIONS.tsv`, and every `\unsure` and `\illegible` of the 706 pages is either settled on the image or
  still marked.
- **A reader** compiles with LuaLaTeX without errors. It holds the text of every one of the 706 pages, checked by
  script against `checked_pages/`, with the counts in the README, and its scan marks agree with `\scanpage` in the
  pages.
- **The apparatus** has one entry for each difference between the diplomatic and the corrected form, and none for
  anything else.
- **Typesetting.** The log of every PDF has no overfull box wider than 2pt, whether a diagram, a display or a line of
  text, and no missing character. No page has ink beyond the sheet, and none has ink outside the type area except the
  overhang of a single letter. You have rendered to images and looked at every page that had an overflow in any
  build, every landscape page, and forty pages spread evenly over each reader.
- **Links.** Every doubt mark and scan mark of every reader is a link to its page, and the counts are in the report.
- **The guide** has its paragraph for every section, for the front matter, for the letter to Quillen and for the
  appendix.

**Not acceptable:**
- a reader that drops, summarizes or paraphrases any part of the text;
- a correction in one form and missing from another;
- a reading changed without a row in `CHECK_DECISIONS.tsv`, or a doubt mark removed where the image does not settle
  it;
- the arXiv reading taken over without looking at the image;
- an apparatus entry without a kind and a reason;
- a silent change of notation, or his spelling standardized;
- a diagram or formula made to fit by a scale below 70 %, or by a scaling pass over the whole book;
- a box wider than the line by more than 2pt left in a log, or hidden by raising `\hfuzz`;
- local paths or e-mail addresses in any output.

**The task is finished** only when the checked pages, the decision and concordance records, the three readers, the
master and the guide with their PDFs, the typesetting records and report, and the README are in the two ZIPs, and every
condition above holds.

## Working method

- Start from the manifests, `records/PAGES_PS.json`, `records/PS_ARXIV_DIFF.tsv` and `*_NOTES.tsv`.
- Check cote by cote, in the order of the typescript. For each page, open both halves of its image and the rows of
  that page, and decide each place on the image. Write the decisions and the corrected page file as you go.
- Clean the LaTeX of the pages mechanically (the nested `$...$` inside the handwriting macros, the unbalanced braces
  listed in the compile fixes) without changing what prints, and record what the script did.
- Build the master by script from the checked pages, generate the forms, compile, and check the counts.
- Repair the typesetting place by place, largest overflow first, compiling the cote on its own before the whole
  reader.
- Write the guide's paragraphs for a section as soon as its check is finished.
- After every ten typescript pages of the check and every finished reader, save a checkpoint ZIP of everything so far to the
  user's Library, or wherever files survive the loss of the execution environment. Save the final ZIPs there too.
- This task is long by design. Work through it completely; do not stop at an outline, a sample or a plan, and do not
  ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so
  that an interruption loses little.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no
overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the
source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to
images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts
before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library after every ten typescript pages of the check and every finished reader, each under a new name, `PS_READERS_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or
delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. If the workspace comes back empty,
restore it from the newest checkpoint and from this conversation before you continue. The final ZIPs hold everything
the checkpoints held: a file or passage left out of the final is listed in the report with the reason (superseded by
which file, or wrong).
Save one also whenever an hour of work has passed since the last checkpoint, whichever comes first. A checkpoint is
one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs,
scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave
the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file,
a recovery file, a summary, or an export of the newest pages only. The checkpoints are what keeps the work if this
session dies: work that is in no checkpoint is lost.

## If the execution environment fails

If the workspace disconnects or an attached ZIP cannot be opened, wait and retry for ten minutes. If it does not come
back, write the work out in the chat as text:
- the decision and concordance records, the change log, the README and the report so far, each in full in its own
  code block headed by its file name;
- your build scripts in full, so that the readers can be rebuilt from the attached sources;
- which cotes are checked, which readers are finished, and where their checkpoints are.

Then continue the remaining work in the chat in the same form until every part is written. An answer that only
reports the failure or asks for the files again is not acceptable.
