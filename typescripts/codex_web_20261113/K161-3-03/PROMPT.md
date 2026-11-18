**This file is the task: carry it out in full, now. The other attached files are its materials.**

# Transcription task K161-3-03: Alexander Grothendieck's papers, Montpellier archive, cote 161-3, 15 scan pages

You are making a **diplomatic transcription into LaTeX** of 15 scan pages from the Montpellier archive of
Alexander Grothendieck: the file `161-3.pdf`, "Topos[176] : notes manuscrites (s.d.)." ([vers 1963-1973][175]). The pages are scans 41-55 of that PDF, in this
order. Sample pages of this file, looked at in a survey, are his handwritten working notes in his dense working hand, with formulas, insertions, margin notes and struck passages. Other kinds of page may occur among them (typed sheets, letters, printed pages, other hands, drawings): transcribe each page as it is, in its own language, and record its hand in the inventory. The language is mostly French, sometimes English or German: keep the language of the page.

**Most of these pages are handwritten.** Handwriting is read more slowly than type: every word letter by letter,
every formula symbol by symbol, every doubtful reading marked. The section "Reading handwriting" below lists the
errors found in earlier transcriptions of this archive's handwriting; guard against each of them on every page.


The attached zip `K161-3-03_scans.zip` holds, for every scan page N (its page number in the archive's PDF), four images:

- `K161-3-03_161-3_scanNNN.jpg`: the whole page, for the layout;
- `K161-3-03_161-3_scanNNN_s1.jpg`, `_s2.jpg`, `_s3.jpg`: the top, middle and bottom thirds of the same page (left, middle
  and right thirds of a landscape sheet) at full resolution, overlapping a little, for small writing, indices,
  exponents, accents and corrections.

`MANIFEST.tsv` lists every image with its size, SHA-256 and scan. The images were taken from the archive's PDF
(https://grothendieck.umontpellier.fr/161-3.pdf), contrast-enhanced and sharpened.

The zip also holds, under `hua/` (not listed in `MANIFEST.tsv`), another transcription of these pages: the batch files
of cote 161-3 by Michel Hua's Commutator project (github.com/Commutator-IO/grothendieck-project, an AI transcription),
and its preamble `hua/preamble/grothendieck.sty`. **Do not open anything under `hua/` before the line
`transcription frozen` is in `out/progress.log`.** It serves one purpose only, the witness check of method 7.

**Look at every image yourself** with your image-viewing tool: the whole page first, then the three thirds. Reading
software (OCR, a PDF text layer, any text-recognition library) is not a substitute for looking and must not be used.
If you cannot view the images, stop at once and say so in your final message; do not produce a transcription by any
other means.

**The task is a complete transcription: every word, symbol, formula, diagram, drawing, deletion, insertion and
marginal note on every page, in the order on the page.** Anything left out is an error. Accuracy is required as
well: a wrong confident reading is worse than an honest mark of doubt, but a mark of doubt is never a reason to leave
something out. Take the time this needs. Work page by page and line by line.

**A description is not a transcription.** Never replace content by a description, a summary, a paraphrase, "[...]",
"etc.", "and so on", or a note that something is there. Never include an image. If you cannot read something,
transcribe what you can and mark the rest with the doubt macros (rule 6), in place.

## Absolute rules

1. **Transcribe only what you see.** Do not fill anything in from memory, from published texts (some of this material
   was later printed or transcribed elsewhere; do not look for, use or reproduce any such text, except an attached
   draft in the one way the section "The attached draft" allows), from what the mathematics "should" say, or from
   your knowledge of Grothendieck's work. If the page says something surprising, transcribe the surprise.
2. **No translation, no modernization, no correction.** Keep the spelling, accents (or their absence), punctuation,
   abbreviations ("cat.", "resp.", "cf.", "th.", "prop.", "dém.", ...) and numbering ("N° 3", "Prop. 1.7", "§ 2")
   exactly as written or typed. Never expand an abbreviation in the text. A slip of the pen or a typing error stays as
   it is on the page; list it in the doubts file (deliverable 2), never correct it in the text.
3. **Mathematics exactly as written**, in LaTeX: the same letters, the same alphabet (script `\mathscr`, calligraphic
   `\mathcal`, Gothic `\mathfrak`, bold, blackboard `\mathbb`, Greek), the same indices and exponents and their
   placement, the same brackets, signs, arrows, bars, hats, tildes, dots and primes. Nothing is simplified, expanded
   or rewritten. Do not define your own notation macros. **Typescripts have no bold type.** A typed letter struck
   twice, or typed over itself so that it looks heavier or doubled, is a double-struck letter (`\mathbb{R}`); a
   letter written in by hand on a typed page is read from its own strokes (a hand-drawn double stroke is `\mathbb`, a
   script capital `\mathscr` or `\mathcal`). Decide every such letter on its own crop: check every capital in a
   heading or in a functor name (R, L, D, H, ...) for double striking separately; a notation-table entry made for the
   body of the text does not cover a heading.
4. **Mark the state of the page**, with these macros only (they are defined in the attached `PREAMBLE.tex`):
   - `\cotefile{161-3}` once, at the very start; then `\scanpage{N}` at the top of each scan page (N as above);
   - `\mspage{n}` where a page or sheet number of the text itself is visible: his own numbering, or the typed page
     number of a typescript ("- 16 -"); a document number typed at the top ("n° 296") is typed text and is
     transcribed. The archive's own pencilled sheet number in a lower corner is not part of the text: note it only as
     a comment line `% archive sheet number: NN`;
   - `\handwritten{...}` for words or symbols written by hand on a typed page (inside a word or formula, around the
     handwritten part only). On a page written entirely by hand it is not used: the hand is recorded in the
     inventory's `hand` column. Text typed into a handwritten page (a typed slip, a stamp) is noted in the inventory;
   - a word or sign written over another one (a correction made by writing on top): the visible final form as live
     text, the form underneath as `\deleted{...}` just before it, if you can read it;
   - `\deleted{...}` for struck-through or typed-over text you can still read (typed `xxxx` over a word included);
     `\deleted{\illegible{2}}` if you cannot;
   - `\inserted{...}` for words added above the line or in the margin and meant to go in at that place, where the
     caret, arrow or line points;
   - `\margin{...}` for marginal notes that are not insertions, written sideways or slanted ones included (transcribe
     them as text, at the place where they stand, and add the comment `% margin note written sideways` or
     `% slanted`);
   - `\uline{...}` for underlined words; double underlining is `\uuline{...}`;
   - `\diagram{...}`: every diagram typeset in `tikz-cd` (or an array for a table), with every object, arrow, label,
     direction and decoration exactly as on the page (inside the macro write
     `\begin{tikzcd}[ampersand replacement=\&]` and separate the cells with `\&`, or the diagram will not compile),
     struck-out parts included (`\deleted` inside the diagram). A diagram is **never** described in words; if part of it is hard to read, typeset it anyway with `\unsure` or
     `\illegible` inside the diagram at that place;
   - `\figure{...}` for drawings that are not diagrams (curves, regions, pictures): **reproduce the drawing in TikZ**,
     with its shape, the relative positions of its parts and every label. Only for a genuine picture too complex for
     TikZ, give your best TikZ approximation and add the comment `% crop-candidate: scan N`;
   - displays: `\[ ... \]`; a display on several lines: `\begin{aligned} ... \end{aligned}` inside `\[ ... \]`, broken
     where the page breaks it; a display label as written: `\tag*{<label>}`;
   - a printed letterhead or printed form on the sheet is text: transcribe it, with the comment line `% letterhead`
     (or `% printed form`) above it. Library or archive stamps are noted only as `% stamp: <what it is>`.
5. **Letters.** For a letter, transcribe the place and date, the salutation, the body, the closing and the signature
   as written, in their order and lines; an address or a note added by the recipient is transcribed where it stands
   (`\margin{...}` if it is in the margin). Who wrote the sheet (Grothendieck or a correspondent, by hand or typed)
   goes in the inventory (deliverable 3), not in the text.
6. **Doubt, explicitly:**
   - `\unsure{reading}` for a reading you believe but are not certain of;
   - `\unsure{reading|alternative}` when two or more readings are possible: list **every** candidate the ink allows
     (`\unsure{E|F}`, `\unsure{3|5}`), the first being what the ink shows, not the expected form: his spelling
     ("standart", not "standard"), his agreement, a plain dash where he drew no arrowhead. If the surrounding text
     favours another candidate, say so in the doubts file; never change the reading for it. Do not mark a glyph whose
     shape decides it;
   - **a recurring ambiguous glyph** (the same letter or sign that could be ℰ or 𝒞 every time it occurs): record the
     doubt once in the notation table, with every candidate, and mark it `\unsure{...|...}` at its **first occurrence
     on each page**; its other occurrences on that page are written with the first candidate, unmarked;
   - `\illegible{n}` for n words whose ink is physically unreadable at the highest zoom (estimate n). Before you use
     it, try a reading and prefer `\unsure{...}`. Never use it for a symbol inside a formula or a diagram: give your
     best reading there with `\unsure`.
   Never guess silently, never leave a gap.
7. Keep the paragraphing and the order of the text on the page. Words hyphenated at a line end are joined; hyphens
   that belong to the word stay. One blank line between paragraphs; line breaks inside a paragraph are not kept
   (except in the lines of a letter's heading, closing and signature, which end with `\\`).

## Reading handwriting

On Grothendieck's manuscripts about one word in fifty to seventy was misread in earlier work of this kind, and two
thirds of the misreadings carried no doubt mark. On clear handwritten letters of this archive the rate was about one
in a hundred, mostly punctuation. The errors found in checked transcriptions of these handwritten pages, each of
which you must guard against:

- **Slanted and sideways margin notes.** A short oblique note in a margin reading "pas prouvé" was transcribed as
  "pour journé". Turn your attention to every note written at an angle or along the edge: read it letter by letter on
  the crop, in its own direction, and mark every letter you have not seen clearly. Never let a margin note pass
  because it is short.
- **Symbols written into formulas.** Handwritten indices and separators were misread: an index `ih` read as `jh`, a
  semicolon in "(x₀ ; y₀)" given as a comma. In every formula, read each index, exponent, separator, prime and
  bracket from its own ink, even where the line above has the other form.
- **Punctuation and small words.** A comma left out, double quotation marks given as single ones, "papers" read as
  "paper". Copy the punctuation stroke by stroke; read each ending (plural s, -é or -er, -ant or -ent) from the ink.
- **Struck words given as live text.** Before you write a word as live text, look for a line, a scribble or a cross
  through it, including a light pencil line and a line through a whole block. A struck block is still transcribed,
  inside `\deleted{...}`.
- **E and F, 3 and 5**, and the other look-alikes listed below: decide each from its own strokes; if the strokes do
  not decide, write `\unsure{E|F}` or `\unsure{3|5}` at that place.
- **His hand reduces letters to strokes.** In his faster hand the middles of words become a wave or a line, and the
  ends of words are often a single stroke. Do not complete a word from what it should be: a word whose letters you
  have not all seen is marked `\unsure{reading}` (with every candidate the ink allows), however well it fits.
- **Insertions placed wrongly.** Follow every caret, arrow, loop and line from the inserted words to the exact point
  in the line where they go, and put the `\inserted{...}` there.

**Every doubtful reading is marked.** If you are not sure of a word, letter, sign or punctuation mark, it carries
`\unsure` (rule 6); an unmarked reading is a claim that you saw every stroke of it. Marks of doubt are expected on
handwritten pages, and many of them; a page of handwriting with no mark at all is a warning sign, not a success.

## Where readings go wrong

On typed pages, and in handwriting too, the errors that remain are of a few further known kinds. Guard against all
of them:

- **The expected word in place of the written one.** A typescript of a related series had "soit èxact à gauche" with
  a grave accent; the transcription wrote "exact" with no mark. Another had "le même resultat vaut", "la
  divisibilitié des", "par voie I-adique" (a capital I) and "(á paraître)"; the transcription wrote résultat,
  divisibilité, l-adique and à paraître. **Read every word letter by letter; check which way each accent points and
  whether it is there at all; tell I, l and 1 apart.** A word that looks right to you is where the risk is. Write
  what is on the page and list the slip in the doubts file.
- **A plausible mathematical word in place of the ink**, on handwritten lines and handwritten corrections: if you
  have not seen every letter of a word, mark it `\unsure`, however well it fits. Read each ending (singular or plural,
  -é or -er, -ant or -ent) from the ink, not from the grammar.
- **A script capital read as a Greek letter.** In the second passes of 17 Nov 2026 over cotes 143 and 148, his script
  T was read as a Gamma (`\Gamma`) again and again. Decide from the strokes whether a capital is script
  (`\mathscr`, `\mathcal`) or Greek, compare it with its other occurrences in the notation table, and where the
  strokes do not decide, mark both candidates.
- **A plausible neighbouring word in place of the ink.** The same second passes found words replaced by a neighbour
  or an opposite that fits the sense: "minimaux" for "maximaux", "loc" for "lac", "cohérente" for "évidente",
  "Cartan" for "Cartier". That a word fits the sentence says nothing about whether it is on the page: read its
  letters, and mark it `\unsure` if you have not seen them all.
- **A short condition or symbol left out**: a "≠ 0", an inclusion sign, a subscript on one of several equal letters,
  inner parentheses, a minus sign, a dual or a star, an "Ob". After each display, margin note and insertion, check
  symbol by symbol that everything on the page is in your text.
- **A handwritten correction on a typed page attached to the wrong place, or left out.** Typed pages in this archive
  carry his corrections: words crossed out by hand, words typed over with x, carets with an insertion above the line,
  symbols filled in by hand in blanks the typist left. Every one goes in, at its place, with its macro.
- **A struck word read as live text.** Before you write a word as live text, look for a line through it.
- **A struck exponent, index or sign read as live.** A hatched or scribbled block over an exponent, index or sign is a
  cancellation: it is not part of the live formula. Transcribe it with `\deleted{...}` and read the formula without it.
  On scans 24-25 of cote 145, 8 of the 23 unmarked errors of the control run were struck superscripts read as a live
  $-1$.
- **i and j, and other look-alikes, in indices and exponents**: j has a descender and i does not; index `1`, `l`, `i`
  and `\ell`; `v` and `\nu`; `n` and `\eta`; `u` and `\mu`; `\epsilon`, `\varepsilon` and `\in`; `\phi` and
  `\varphi`; `o`, `0` and `\circ`; E and F; 3 and 5; u and n; script, calligraphic and roman capitals; `*`, `\bullet`
  and `\cdot` in exponents; an exclamation-mark exponent `^!` and a prime `'`; prime and comma; tilde, bar and hat.
  Read each from the ink, one by one, even where the line above has the other; if the ink does not decide, mark it.
- **Directions**: `\leq` and `\geq`, `\Rightarrow` and `\Leftarrow`, the direction of every arrow, inclusion and
  isomorphism, upper and lower indices (`H^i` and `H_i`, `f_*` and `f^*`, `f_!` and `f^!`): from the ink, never from
  what the argument needs.
- **Quotation marks**: his double quotation marks are written ``...'' (two backticks, two apostrophes); « » only
  where guillemets are drawn or typed.
- **Accents and French text**: é and è, à and a, ô and o, ç; accents on capitals exactly as on the page.
- **The first pages done fastest.** In earlier work of this kind the pages done in the first minutes had three times
  as many errors as later ones. Read the first page as slowly as the last.

## The attached draft

There is no draft for these pages: transcribe them from the images alone.

## Method

1. Unpack `K161-3-03_scans.zip` into your working folder and check its files against `MANIFEST.tsv` (names and SHA-256).
   Create the folder `out/` beside them, with its subfolder `pages/`, and copy the attached `PREAMBLE.tex` into
   `out/`. Read nothing but the attached files. No internet access is needed; do not search the web.
2. Write the current time (UTC) as the first line of `out/progress.log`.
3. For each scan page, in order: read the whole page once, then transcribe it line by line from the three thirds.
   Re-read the images against your transcription, line by line; correct, or mark doubt. Then make the page
   **inventory**: every text block, letter part, display, diagram, drawing, margin note, insertion, deletion and
   handwritten addition on the page, top to bottom; check that each one is in your transcription, complete. Fix any
   gap.
4. **As soon as a page is done**, write it to its own file `out/pages/K161-3-03_161-3_scanNNN.tex`, add its rows to
   `out/K161-3-03_inventory.csv`, append a line `scan NNN done <current UTC time>` to `out/progress.log`. Saving these
   files is your checkpoint. Only then
   go to the next page.
5. **One stream, one notation.** Transcribe the pages yourself, in one stream, in order: do not split them among
   parallel workers or sub-agents. When the pages of an earlier package of this archive were split among workers,
   the same signs were read in different ways and the errors went unmarked. Keep a notation table from the first page
   on: the recurring signs and exponents, the letters of each alphabet, the quotation marks and abbreviations, each
   with how it is written in LaTeX. **Build every entry from the image, not from convention**, with the scan and line
   where you looked; for each recurring ambiguous glyph, its candidates (rule 6). The table is a set of readings, not
   facts: check each entry again on every new page. Before the transcription is final, compare how each recurring
   sign was read across all the pages, check every difference against the images, and make the readings agree where
   the page agrees. The other scans of cote 161-3 in this batch are transcribed in separate tasks that run in parallel: K161-3-01 to K161-3-02 (scans 4-13, 15-16, 18-22, 24-27, 29, 31-33 and 35-40) before this one. The notation tables of all these tasks are reconciled afterwards, so every entry of yours names the scan and the line where you saw the glyph.
6. **A second reading of every page, as a second reader.** When every page is done, read each page again from the
   start against its three thirds. This is a full reading, not a skim: in an earlier series a "second reading" of
   11-35 seconds per page found none of its six errors; a page needs several minutes. For each page, **first** read
   the crops line by line and write down, before you open the page file, every accent and every word that looks
   misspelled or unusual, as you see it in the crop; **then** open the page file and compare. Write a section per page
   in `out/K161-3-03_audit.md`: the start and end time (UTC); that list of words and accents from the crops; every display
   and inline formula, checked symbol by symbol (list them); every i and j in an index or exponent; every handwritten
   correction on a typed page and where it went; every margin note, read again in its own direction, letter by
   letter; every struck word or block, and every word you wrote as live text that has any line near it; every double-struck or script candidate with what you saw; and every
   change made, as `before -> after` (or "no change"). Correct, or mark doubt, and append
   `scan NNN audited <current UTC time>` to `out/progress.log`.
7. **Assemble and check.** Write `out/K161-3-03_transcription.tex`: the page files in order, concatenated, as one LaTeX
   fragment (no preamble, no `\documentclass`). Write `out/K161-3-03_standalone.tex`: `\input{PREAMBLE.tex}`
   `\begin{document}` `\input{K161-3-03_transcription}` `\end{document}`. **Do not try to compile**: this sandbox has no
   working LuaLaTeX (earlier tasks of this kind spent their time building formats that could not work); we compile
   the return ourselves. Instead check with a short script that braces, `\[ \]`, `$ $` and environments balance in
   every page file, and fix what does not (the fix is syntax only and never changes a reading). Then write the
   SHA-256 of each page file and of the assembled file to `out/progress.log` with the line
   `transcription frozen <current UTC time>`.

   **Then, and only then, the witness check with Hua's transcription.** Open `hua/`. Each batch file covers about
   twenty archive pages, with `\pages{a}{b}` at its top; their page n is our scan n + 1, and the comments of
   `hua/preamble/grothendieck.sty` say what each of their macros means. Use it for one thing only: the places of your
   frozen text still marked `\unsure` or `\illegible`. For each such place, find his reading of the same place, then
   read the ink again on the crop:
   - where his reading, checked letter by letter against the ink, settles the place, change your text to what the ink
     shows;
   - where the ink still does not decide, keep your reading first and add his as the alternative, in
     `\unsure{your reading|his reading}`;
   - change nothing you did not mark, and never fill a passage from his text.

   His transcription is a witness, never a basis: never take his wording, spelling, punctuation, conventions, notes,
   headings or descriptions into the text. Record every place you looked at in a table "Witness check" at the end of
   `out/K161-3-03_doubts.md`: scan, line, your frozen reading, his reading (written "Hua batch-NN reads ..."), what the ink
   shows, and the result (changed, alternative added, unchanged). Then write the SHA-256 of each page file and of the
   assembled file again to `out/progress.log`, with the line `witness check done <current UTC time>` and the number of
   places changed and of alternatives added. The text so written is the final transcription. Pages his files do not
   cover get no witness check.
8. **The mathematical notes, after the freeze.** Only after the line `transcription frozen` and the line
   `witness check done` are in `out/progress.log`,
   write `out/K161-3-03_mathnotes.md`, in English. The notes never change a reading: the page files and the assembled
   file stay exactly as last hashed, and at the end you check that their SHA-256 still match the last ones in
   `out/progress.log` and say so in
   `out/progress.log`. If a doubt about a reading comes up while you write the notes, record it in the notes as a
   reading question (scan, line, the frozen reading, the other reading, and why), never in the transcription. The
   notes are light and come from these pages alone, in these sections:
   - **What the pages do:** one short paragraph per mathematical unit (a definition, a construction, a proof, a
     computation, a list, a letter), with its scans.
   - **Statements left without proof:** his claims stated without proof or left for later, each with its scan and
     his words.
   - **Questions and conjectures:** his questions, conjectures, hopes and doubts, each with its scan and his words.
   - **Slips:** his slips (a wrong index, sign, exponent, reference or word) with the corrected form and the reason,
     each with its scan. The transcription keeps the slip as written.
   - **Pointers:** where he points to his other texts, other cotes, papers or people, each with its scan and his
     words.
   - **Remarks of the model:** your own remarks (what might follow, what looks wrong, a link he does not make), each
     labelled as yours, with its confidence (high, medium, low) and the reason.

   In the notes, no slip, convention change or error claim may rise above low confidence when the reading it rests on
   carries a doubt mark or sits on a struck or overwritten mark. (On cote 145, a high-confidence convention claim
   rested on a struck $-1$.)

   No proofs, no literature search, no long derivations. Write "none" in a section that has nothing. Then append
   `mathnotes done <current UTC time>` to `out/progress.log`, make `K161-3-03_out.zip` of the whole `out/` folder and offer
   it as a download.
9. **If time or context runs short.** If the environment tells you that time or context is running out, do not stop
   silently: at once write the assembled file, the doubts file and the inventory for the pages finished so far, list
   the unfinished pages in `out/progress.log` and in your final message, and offer `K161-3-03_out.zip` of what is finished
   as a download. Work that is not delivered is lost.

This task is long by design: 15 pages, each read twice, then the mathematical notes. Work through all of it completely; do not stop at a
sample or a plan, and do not ask whether to continue.

**Check events.** For every statement your notes check, use or refute (a claim of his or a remark of yours, by its place in the notes), record its check events in `out/CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what actually happened, neither more nor less: reading a statement while transcribing it is not a check of it. Write "none" under the header if there is no such event.

## What to deliver (all in `out/`, zipped as `K161-3-03_out.zip` and offered as a download at the end)

1. `pages/K161-3-03_161-3_scanNNN.tex`, one file per scan page, and `K161-3-03_transcription.tex`, the assembled fragment
   starting with `\cotefile{161-3}` and the `\scanpage` of the first page, using only the macros above plus standard
   LaTeX, `amsmath`, `amssymb`, `mathrsfs`, `tikz-cd`, `tikz`, `enumitem` and `ulem`; and `K161-3-03_standalone.tex`.
2. `K161-3-03_doubts.md`, in English (readings as on the page): the notation table (method 5) at the top; then a table of
   doubts (scan, line approximately, your reading, every alternative, confidence high / medium / low, and which
   candidate the surrounding text favours, if any, and why); then the slips kept as written (scan, line, as written,
   apparently intended, why); then the abbreviations met, each with what you think it stands for (in this list only,
   never in the text); then a short honest note on how legible these pages were and which parts you trust least.
3. `K161-3-03_inventory.csv` with the columns
   `cote,scan,sheet_kind,hand,element,kind,position,first_words_or_objects,transcribed`: one row per element of every
   page (kind: text, letter part, display, diagram, drawing, margin note, insertion, deletion, handwritten), with
   `transcribed` = yes for every row. A row that is not yes means the transcription is not finished. `sheet_kind` says
   what the sheet is: `text` (notes or a typescript on the subject of the folder), `letter`, `reused_typed` (a typed
   page of another text that he wrote on or whose back he used), `cancelled_draft` (a draft struck through), or
   `cover` (a folder cover or title sheet). `hand` says who wrote that element as far as the page shows it:
   `typed`, `Grothendieck` (his hand, as the folder's notes show it), `other hand`, or `unknown`.
4. `K161-3-03_audit.md`, the second reading page by page (method 6).
5. `K161-3-03_notes.md`, in English, two short sections answered from these pages only: **the steps the pages themselves
   mark as unverified** ("à vérifier", "sauf erreur", "je présume", "admis", "il faudrait vérifier", a "?" on a step),
   each with its scan and the words; and **the title sheets, dates and page counts they carry** (a title, a date, a
   "19 pages", the numbering of a typescript), each with its scan. Write "none" where there is none.
6. `K161-3-03_mathnotes.md`, the mathematical notes (method 8), written after the freeze.
7. `progress.log`.

Your final message: the download link of `K161-3-03_out.zip`, the pages done and audited, the number of `\unsure`,
`\illegible` and `\deleted` marks, how the balance check came out, the times of `transcription frozen` and
`mathnotes done`, whether the hashes still matched after the notes, the number of places the witness
check changed and annotated, and any page that is not finished.
