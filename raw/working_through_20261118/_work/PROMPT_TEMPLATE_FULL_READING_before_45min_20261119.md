# {S}: working through Alexander Grothendieck's manuscript, Montpellier archive, cote {COTE}, scans {RANGE}

## What this is

The Montpellier archive (fonds Grothendieck, Université de Montpellier) holds about 16,000 scanned pages of his
manuscripts. We are making a companion to them in the manner of the great editions of mathematicians' papers
(Whiteside's Newton, Neumann's Galois, Berndt's Ramanujan): his text, transcribed faithfully and made readable, and
beside it, in one plain voice, headnotes, notes keyed to his lines, and the status of each claim and question of his,
dated and with references.

This run works through one unit of one folder: **cote {COTE}, scans {RANGE}** ({COUNT} pages).
{FOLDER_NOTE}

It works the pages through as a colleague who means to use them would, filling three layers in order:
1. **the transcription**, read on the ink with two witnesses; the pages that have no reading yet are transcribed first;
2. **the notes** that earlier runs wrote on these pages, consolidated into one reflection of the transcription;
3. **the mathematics** on that basis: his claims decided, his computations redone, his questions attacked.

Then the work corrects the layers below it, and last, it is related to our own results.

## The attachments
{ATTACH_NOTE}
- {SCANS_FILES}: for every scan N of this unit, four images: `{COTE}_scanNNN.jpg` (the whole page) and `_a`, `_b`, `_c`
  (its top, middle and bottom thirds, or left, middle and right thirds of a landscape sheet, overlapping a little, at
  full resolution). {NEIGHBOURS} The images are contrast-enhanced and sharpened.
- `{S}_witnesses.zip`: `README.md` (start there), `page_map.tsv` (for every scan, every reading and who made it), and
  the readings:
{WITNESS_LIST}
- `{S}_notes.zip`: the notes earlier runs wrote on this folder, which this run consumes:
{NOTES_LIST}
- `{S}_context.zip`: the subject's own context, to be used from the start. {CONTEXT_LIST}
- `{S}_results.zip`: the statements of our own research runs that cite this folder. **Leave it closed until the
  layers are done** (section "Last: our results").

Unzip every attachment except `{S}_results.zip` in your sandbox. **Look at every image yourself:** the whole page
first, then the thirds, and enlarge (crop and scale) every place you decide. Reading software (OCR) is not a substitute
for looking and is not used on these pages.

## Layer 1: the transcription, on the ink

**The rule of this layer: the mathematics raises the alarm, the ink decides.** In earlier controls, the mathematically
expected word was wrong at 3 of 29 disputed places ("implique" for "indique", an added "en prenant", "sommes
disjointes"). So a reading never changes on mathematical grounds alone.

Write the current time (UTC) as the first line of `progress.log`. Then:
1. **The pages with no reading** ({MISSING}) are transcribed first, in full, in our conventions (below).
2. **Every other page, in order:**
   1. **First the crop, before any witness.** Read on the enlarged image every logic-bearing word (quantifiers,
      negations, "si", "donc", "sauf", "ne ... pas", "il suffit", "en général", "implique" or "indique"), every index,
      exponent, sign, inequality and arrow direction, and every margin note, insertion and deletion. Do this before
      you look at the witnesses: reading with a text in view lets plausible words through.
   2. **Then the witnesses.** Compare your reading with each witness word by word. Where they differ from each other
      or from your reading, decide on the ink: the answer may be one witness, the other, or neither. Where they
      agree, the reading still has to be seen in the ink: they are AI readings of the same scans, and agreement
      between them is not evidence. Every doubt mark (`\unsure`) in a witness is a place to decide on the ink:
      resolve it where the ink settles it, keep it where it does not.
   3. **Then the mathematics.** Read the page as mathematics. Where it breaks (a statement false as read, a step that
      does not follow, a symbol outside its type, a word outside his vocabulary for the object), go back to the crop.
      Correct the reading only if the ink shows the other reading. Otherwise the reading stands, and the break becomes
      a note: his slip, or a doubtful reading.
   4. **Then the ink not yet in the text.** Go over the page strip by strip: every mark of ink is in the text, struck,
      inserted, a drawing, noise, or illegible.
3. **Our conventions.** The macros of `PREAMBLE.tex` in the witnesses zip: `\cotefile{C}`, `\scanpage{N}`,
   `\mspage{n}`, `\deleted{…}`, `\inserted{…}`, `\margin{…}`, `\uline{…}`, `\uuline{…}`, `\diagram{…}` in `tikz-cd`,
   `\figure{…}` in TikZ, `\unsure{reading}`, `\unsure{reading|alternative}`, `\illegible{n}`. His spelling, accents,
   punctuation, abbreviations and numbering exactly as written; mathematics in the same letters, alphabets, indices,
   arrows and decorations. A diagram is typeset, never described; a drawing is reproduced in TikZ, never described.
   Doubt is marked in place, never resolved by a guess, and the first reading in `\unsure{a|b}` is what the ink shows.
   His double quotation marks are two backticks and two apostrophes; « » only where he drew guillemets.
4. **The record.** Write the corrected page files in `pages/`, named `{COTE}_scanNNN.tex`. For every place where the
   final reading differs from a witness, add a row to `CHANGES.md`: scan, line, each witness's reading, the final
   reading, what the scan shows (the strokes you saw, the crop used), what raised it (the witnesses differ / a doubt
   mark / a logic-bearing word / the mathematics / ink not in the text), and confidence (high, medium, low). At the
   top of `CHANGES.md`: the counts, and the consequential corrections (those that change the mathematics), one per
   line.
5. **The freeze.** When every page is done, write the SHA-256 of every page file to `progress.log` with the line
   `reading frozen <UTC time>`. From then on the reading changes only through a new row of `CHANGES.md` with its
   evidence (section "The correction loop").
6. **The abbreviations.** In `expansions.tsv`, every abbreviation of his in the unit, one row per occurrence (scan,
   line, as written, its expansion, confidence), so that a script can build the reading text with the expansions in
   square brackets.

## Layer 2: the notes, consolidated

The notes in `{S}_notes.zip` are leads, not results: each is worked through to a verdict, neither trusted nor presumed
false. Some read his pages through our research on La Longue Marche or Les Dérivateurs; here the pages are read in
their own terms, and such links are checked last.

1. **The units of his writing.** Divide the pages into the units of his argument: his own divisions first (his
   numbered items, headings, dated sessions, a list, a letter, a typed page with his annotations), elsewhere the
   stretch of argument one headnote can introduce. In `units.json`, one object per unit: `id` (`{COTE}.{FIRST}.<n>`),
   `scans`, `lines`, `title` (his words where he gives a title, else ours, marked), `date` (his, or inferred, with the
   evidence), and `headnote`. The headnote is two to six sentences in the voice of a colleague who knows the field and
   the period: where we are in the folder and in his work, what he is doing in today's terms, what comes before and
   after in this folder, in his other folders and in his published work. It says "probably" or "we think" where it
   conjectures, and why. It never retells his text.
2. **Every entry gets a verdict.** Every entry of `NOTES_INDEX.tsv` (the entries on these pages) gets a row in
   `NOTES_VERDICTS.tsv`: its anchor on the ink (the passage it quotes, confirmed or corrected); its mathematics
   (confirmed, corrected, refuted, resting on a misreading, or not checkable, each with the reason); and where its
   content went (a consolidated note, a claim, a research direction, the groundwork, an edition matter, or nowhere,
   with the reason). None is left without a verdict, whatever an earlier triage or the sweep said of it.
3. **The consolidation.** Merge the entries unit by unit into `NOTES_CONSOLIDATED.md`: one section per unit, holding
   one table with the columns `id | locator | kind | note | sources | tag`. Each note appears once, anchored on the
   ink (`locator` is scan.line); duplicates are merged; contradictions between entries are resolved or marked. `kind`
   is one of: `grounds` (the result he uses, by exact locator, "By EGA 0_IV 19.3.5."), `today` ("In today's terms:
   ..."), `step` ("The step left implicit: ..."), `draft` ("He first wrote ..." / "He struck ..."), `slip` ("Read
   ...", with the check that shows it; a slip is called a slip, plainly), `reading` ("Reading uncertain: ... or
   ..."), `link` (to his other folders and his published work, with dates), `fact` ("In fact, ...", a fact checked).
   `sources` lists the entry ids it consumes; `tag` is the object's tag in `CONCORDANCE.tsv`, where the sweep gave one.
   Notes are short and exact, one to four sentences.
4. **His claims.** Each claim and question of his in the unit (a statement, construction, computation, conjecture,
   question, hope or doubt) gets a place and a first status in `CLAIMS_STATUS.tsv` (columns below).
5. **The research directions.** Note the research directions you find while consolidating as they come up, each with
   where it comes from (his words, a claim, an entry), in `RESEARCH_DIRECTIONS.md`.

## Layer 3: the mathematics

Work on the noted directions and on his own claims and questions: decide the claims, redo his computations (by hand
where they are small, by program where a computer settles them, the program and its output kept in `scripts/`), and
attack his conjectures, under the rule of the next section. For each claim, write today's precise statement with
every hypothesis, mark what in it is your reconstruction, and find what became of it: in his published work (EGA,
SGA, his papers), proved by others, or open today with the best known result.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most
of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the
smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach
stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter
search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then
push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided
step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about
three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in
every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved
reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly
smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement.
After two consecutive reviews without movement, stop that work, write the final package with every item's state, and
deliver it; this check takes precedence over the sentence above about untried approaches.

**The items** are his claims and questions on these pages (`CLAIMS_STATUS.tsv`) and the research directions of
`RESEARCH_DIRECTIONS.md`; each is a row of the ledger. A construction or a definition is an item through what he
claims of it; a computation through its result. **The main question** is his central open question on these pages,
or, where he asks none, the claim the most other items depend on. Name it at the top of the ledger.

For each item:
- (a) proved: by a complete proof of yours, checked a second time independently; or in the literature: the exact
  statement and its locator (theorem and page) in a source you opened, with its hypotheses matched to his;
- (b) refuted: a counterexample with every hypothesis checked, then the corrected statement (the version he most
  likely had in mind, and the strongest version that is true), with its complete proof.

Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and
the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack
the obstruction, starting from that instance.

**When the work is finished.** Only when every item is proved (a) or refuted (b). Keep working until then: do not stop
because the remaining items are hard, because a partial result looks presentable, or because much has already been
done. An item may carry the status "open" only when the progress check has stopped its work, or when the session
itself ends first (the environment stops you, not your choice). In the second case the first line of
`RESEARCH_DIRECTIONS.md` reads INCOMPLETE. Either way, every undecided row carries the state reached, every approach
tried with where it failed, the strongest result known in the literature with its locator, and the next step you
would take. Never present such a return as complete or as following an allowed alternative: there is none.

## The correction loop

What layer 3 found goes back into the layers below it:
- into layer 2: the notes corrected and the statuses of `CLAIMS_STATUS.tsv` updated;
- into layer 1: a misreading that the mathematics exposed is checked on the crop, and the ink decides. A change after
  the freeze is a new row of `CHANGES.md` marked `after the freeze`, with what the scan shows; the page file changes
  with it, and `progress.log` records the new hash.

Then write **`GROUNDWORK.md`**, beside his words and never mixed with them: per unit, in English, the account of what
he does in today's terms; the questions a first reader asks, answered; his claims with their status; his slips with
the corrected form; and the connections to his other folders, to his published work and to the literature, each
source opened and cited by exact locator. It is written for a career algebraic geometer who has not read the folder.

## Last: our results

Only when the layers are done, append `results opened <UTC time>` to `progress.log` and open `{S}_results.zip`.
- In `CONSEQUENCES.tsv`, list (column `kind`):
  - `bears_on`: each statement of our runs that bears on a claim or note of these pages: the statement's tag, the
    claim or note id, the relation (same object / same statement / a consequence / a generalization / a counterexample
    / a contradiction), and the evidence;
  - `quotes_corrected_reading`: each statement of our runs whose places quote a reading this run corrected: its tag,
    scan and line, the old and the new reading, and the confidence.

  Add only links with evidence; force none. Nothing found is a valid result. A status in that file is our runs'
  claim, not a check.
- In `FOR_EXPERTS.md`, for each field the pages touch: what in them bears on open questions of that field, with the
  evidence, and the questions worth a further research prompt.

## Rules

- **His terms first.** Every account is written first in his notation and his words (his objects, his names, his
  order of ideas), with today's restatement beside it, never instead of it. His words and ours never share a
  paragraph. Keep three things apart everywhere: what his pages show, what the sources say, and what is ours; label
  ours as ours.
- **Quotation.** A note quotes at most a short phrase of his and refers to the rest by scan and line.
- **The literature.** Every reference is real and checked: give a link or DOI that you opened (`note = {verified}` in
  `references.bib`); otherwise mark it `note = {unverified}`. Never cite from memory without checking. Search zbMATH
  Open, arXiv, MathOverflow, Numdam, the EGA and SGA in the context, and the collected works and bibliographies of the
  authors concerned; follow references backwards from later papers when a title search finds nothing. The absence of
  a first hit is weak evidence, and a later paper on the same broad subject is weak evidence that the exact claim was
  settled: match the quantifiers and the hypotheses.
- **No completion presented as his.** Never fill a gap in his text from what he "must have" meant; mark a
  reconstruction as yours. Never lower his statement to match a proof you can give, and never rewrite his text toward
  today's mathematics.
- **One stream.** Do the pages and the mathematics yourself, in order, in one stream: do not split them among parallel
  workers.
- **Everything.** Cover every page, every unit, every entry and every claim of the unit; do not ask questions back.
  Make the decisions a careful editor and mathematician would make, state them, and carry on.

**Check events.** For every statement your work checks, uses or refutes (a claim of his, by its claim id; a note, by
its id; an entry, by its id; a result of the literature, by its reference key; a statement of our runs, by its tag),
record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome, and where the record
is. The file has the six columns `id, date_utc, who, how, result, where`: the type goes in `how`, the outcome in
`result`, and `where` is the file and line or section of the record. Give each event the type of what actually
happened, neither more nor less: reading a statement while transcribing it is not a check of it.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every hour of work, each under a new name, `{S}_checkpoint_<NN>.zip` with `NN` counting up; never
overwrite, rename or delete an earlier checkpoint. Save checkpoints once an hour and at no other time: none after a
page, a unit or a layer. A checkpoint is one ZIP holding every deliverable written so far and everything that
documents the work (the pages, the tables, `PROGRESS_LEDGER.md`, `CHECK_EVENTS.tsv`, `progress.log`, the programs), so
that a new session can continue from it and the attached files. Leave the attached files themselves out of it: we have
them. It is never a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip
holds the current deliverables and documentation; earlier checkpoints are not copied into it. If the workspace comes
back empty, restore it from the newest checkpoint before you continue.

**If the execution environment disconnects.** Wait for it and retry for at least 10 minutes. If it does not come back,
the work must still reach us, so write it out in this chat as text: every file finished so far in full, each in its
own code block headed by its file name (the code you ran to save each file contains its text: take it from there).
Then go on with the remaining work directly in the chat, in the same form. Say at the start which files are done and
which are not. An answer that only reports the disconnection, describes the checkpoint or asks for the files again,
without writing out the work, is not acceptable.

## What to return

One zip file, `{S}.zip`, offered as the only download, holding:
1. `pages/` (the corrected page files) and `{S}_transcription.tex` (all pages in order, one LaTeX fragment, our macros
   only);
2. `CHANGES.md` and `expansions.tsv` (layer 1);
3. `units.json`, `NOTES_CONSOLIDATED.md` and `NOTES_VERDICTS.tsv` (layer 2), the last with the columns `entry_id,
   anchor, mathematics, placed, reason, right_object`;
4. `CLAIMS_STATUS.tsv`, with the columns `claim_id, unit, locator, his_words, statement, reconstruction,
   as_he_left_it, status, proof_or_reference, later, tag, check_events, confidence`; `status` is proved (with where
   the proof is), known (the reference and locator), false (the counterexample and the corrected statement), or open
   (the state reached);
5. `RESEARCH_DIRECTIONS.md`: each direction with where it came from, what was done, and the state reached; the proofs
   and counterexamples in full in `PROOFS.tex`, one section per item;
6. `GROUNDWORK.md`, `FOR_EXPERTS.md`, `CONSEQUENCES.tsv`;
7. `references.bib`, every work cited, with its `note` field;
8. `PROGRESS_LEDGER.md`, `CHECK_EVENTS.tsv`, `progress.log` (the time, UTC, at the start, at the freeze, at each
   review, at the opening of the results and at the end), and `scripts/`, every program you ran, with its output.
