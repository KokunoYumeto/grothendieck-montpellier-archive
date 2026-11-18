**This file is the task: carry it out in full, now. The other attached files are its materials.**

# Reading task V3-CTRL-145: Alexander Grothendieck's papers, Montpellier archive, cote 145, 138 places on 14 scan pages

This is a reading of **selected places**, not a whole transcription. The pages are scans 20-31 and 33-34 of the file
`145.pdf` of the Montpellier archive, "Printemps 81 (vieille rédaction)[149] : notes manuscrites (s.d.)." (1981): his handwritten working notes, in
French, with formulas, insertions, margin notes and struck passages.

**The places.** `places/V3-CTRL-145_places.tsv` in the zip lists 138 places. Each is a short stretch of a page (a
word, a few words, a symbol, an index, a formula, sometimes a whole line) that earlier readers found hard. For each
place it gives the scan, the third of the page where it most probably stands (`s1`, `s2`, `s3`), and the text just
before and just after it as an earlier reader transcribed it, in LaTeX; other places inside that text appear as
`[[Pnnn]]`. **The place itself is withheld: you read it from the ink alone.** The context can be wrong in a detail;
use it only to find the place, never as a reading.

The attached zip `V3-CTRL-145_scans.zip` holds, for every scan page N that has a place to read (its page number in the archive's PDF), four images:

- `V3-CTRL-145_145_scanNNN.jpg`: the whole page, for the layout;
- `V3-CTRL-145_145_scanNNN_s1.jpg`, `_s2.jpg`, `_s3.jpg`: the top, middle and bottom thirds of the same page (left, middle
  and right thirds of a landscape sheet) at full resolution, overlapping a little, for small writing, indices,
  exponents, accents and corrections.

`MANIFEST.tsv` lists every image with its size, SHA-256 and scan. The images were taken from the archive's PDF
(https://grothendieck.umontpellier.fr/145.pdf), contrast-enhanced and sharpened.

**Look at every image yourself** with your image-viewing tool: the whole page first, then the three thirds. Reading
software (OCR, a PDF text layer, any text-recognition library) is not a substitute for looking and must not be used.
If you cannot view the images, stop at once and say so in your final message; do not produce a transcription by any
other means.

The rules and the two sections below were written for whole transcriptions. They apply to every reading you write
here: the same macros, the same care. There is no attached draft in this task. Where they speak of the doubts
file (deliverable 2), use the `ink` column of your answer file.

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
   - `\cotefile{145}` once, at the very start; then `\scanpage{N}` at the top of each scan page (N as above);
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

## Method

1. Unpack `V3-CTRL-145_scans.zip` into your working folder and check its images against `MANIFEST.tsv` (names and
   SHA-256). Create the folder `out/` beside them. Read nothing but the attached files; do not search the web. Write
   the current time (UTC) as the first line of `out/progress.log`.
2. **Read each place, in order.** Open the whole page of its scan, then the third named in the list. Find the place
   from the context before and after it; if it is not in that third, look in the neighbouring thirds and on the whole
   page. Then read the place, from where the "before" text ends to where the "after" text begins, nothing more and
   nothing less: every word letter by letter, every formula symbol by symbol, every accent, index, exponent, struck
   or inserted mark. Write it in LaTeX with the macros of rules 4 and 6: `\deleted{...}` for what is struck,
   `\inserted{...}` for an insertion, `\unsure{a|b}` where the ink does not decide between readings (your first
   choice first), `\illegible{n}` for what you cannot read. If nothing stands there, write `(nothing)`.
3. After the last place of a scan, append `scan NNN done <current UTC time>` to `out/progress.log`.
4. **A second reading of every place.** When all places are read, read each place again in the ink before you look
   at your first answer; then compare, and correct or mark doubt. Note every change in the `ink` column, as
   `second reading: a -> b`. Append `second reading done <current UTC time>` to `out/progress.log`.
5. Write `out/CHECK_EVENTS.tsv` (below). Make `V3-CTRL-145_out.zip` of the whole `out/` folder and offer it as a download.

**Checkpoints that survive a disconnection.** Once every hour of work, save a checkpoint ZIP of everything in `out/`
so far to the user's Library, or wherever files survive the loss of the execution environment, named
`V3-CTRL-145_checkpoint_NN.zip` with NN counting up from 01; never overwrite an earlier checkpoint. Save checkpoints
once an hour and at no other time. Leave the attached scans out of it: we have them. A checkpoint is never a JSON
file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it. Work that is in no checkpoint is lost.

Every one of the 138 places is read, from the ink, twice. Work through all of them completely; do not stop at
a sample, and do not ask whether to continue.

**Check events.** For every statement your work checks, uses or refutes (a claim of his, by its scan and line), record
its check events in `out/CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the
type of what actually happened, neither more nor less: reading a statement while transcribing it is not a check of it.
Write "none" under the header if there is no such event.

## What to deliver (all in `out/`, zipped as `V3-CTRL-145_out.zip` and offered as a download at the end)

1. `V3-CTRL-145_places_read.tsv`, UTF-8, tab-separated, with the header line
   `place	scan	reading	confidence	found	ink` and one line for every place of the list, in its order:
   - `reading`: the place in LaTeX, as the ink shows it;
   - `confidence`: high, medium or low;
   - `found`: yes, or no if you could not locate the place (then say in `ink` where you looked);
   - `ink`: a few words on what the strokes show that decides the reading, or why it stays undecided.
2. `progress.log`.

Your final message: the download link of `V3-CTRL-145_out.zip`, the number of places read, how many were not found, how
many readings are high, medium and low, and how many changed at the second reading.
