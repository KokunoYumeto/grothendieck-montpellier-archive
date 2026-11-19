# WTA_1_026-038: the companion's units for Alexander Grothendieck's manuscript, cote 1, scans 26-38, worked through

## What this is

The Montpellier archive (fonds Grothendieck, Université de Montpellier) holds about 16,000 scanned pages of his
manuscripts, and about 10,000 of them are transcribed. We are building two views of one body of work on them:
- **the companion:** his text read unit by unit, in the manner of the great editions of mathematicians' papers
  (Whiteside's Newton, Berndt's Ramanujan, Neumann's Galois, the Colmez-Serre correspondence): before each unit a short
  headnote, beside his lines short notes keyed to them, and after it the status of each of his claims and questions,
  dated and with references;
- **the handbook:** all the mathematics in one tag space, in the manner of the Stacks project and Kerodon. Every
  definition, statement, claim of his, question, conjecture and counterexample is one item with one tag, a status
  (proved, known, his claim, open, refuted) and its check record. The handbook's draft tags are the objects of the
  sweep that sorted the notes (`OBJECTS.tsv` in the notes zip).

This run takes one range of one folder: **cote 1, scans 26-38** (13 pages). The folder's catalogue title: « Analyse fonctionnelle : notes manuscrites (s.d.), lettre (1953). » (1953). It has 149 scans; this run takes scans 26-38, range 3 of 11 of the folder; the other ranges are separate runs.
No draft units exist for these pages.

For this range it:
1. gathers every node that bears on it (the readings, the notes earlier runs wrote, the sweep's objects, the check
   records) and picks the relevant ones;
2. reads the ink wherever a reading matters to the mathematics;
3. works through the mathematics: decides his claims, redoes his computations, attacks his questions;
4. writes each unit in the companion's format;
5. sorts what belongs in the unit and what becomes an item of the handbook, and links each unit to the tags it bears
   on, as suggested links with their evidence.

Every output is a fixed-format file, so that a script can merge the ranges, remove duplicates and keep the history.

## The attachments

- `WTA_1_026-038_scans.zip`: for every scan N of the range, four images: `1_scanNNN.jpg` (the whole page) and `_a`, `_b`,
  `_c` (its top, middle and bottom thirds, or left, middle and right thirds of a landscape sheet, overlapping a little,
  at full resolution). The pages just before and after this range (scans 25 and 39) are attached whole, as `..._neighbour.jpg`, to follow an argument across the cut: they are worked in their own ranges, and are read here only to complete such an argument. The images are contrast-enhanced and sharpened.
- `WTA_1_026-038_witnesses.zip`: `README.md` (start there), `page_map.tsv` (for every scan, every reading and who made it), and:
  - `first/MPL_1_002-050/`: witness O, the first pass by GPT-6 Astra (ChatGPT Pro mode), 10 Nov 2026, for 12 of the 13 pages, with its doubts table and the prompt it was made with (`first_pass_PROMPT.md`, which defines our macros); earlier checks found about 1 to 2.5 errors per 100 words on his dense hand, mostly fluent misreadings, dropped short conditions or symbols, wrong indices, signs and arrow directions, and missed deletions; only a third of them carried a doubt mark.
  - `first/HC1-01/`: witness C, the first reading by GPT-6 Astra at reasoning effort max (Codex web), 14 Nov 2026, for 2 of the 13 pages, with its doubts table, its audit and the task it was given (`PROMPT.md`); earlier checks found it careful on typed and light pages and about 1.4 to 1.7 errors per 100 words on his dense hand (control folder CTRL-148), with many doubt marks (about 7 per 100 words); typical slips are a struck letter given live, an insertion attached to the wrong place, a word ending read from the grammar.
  - `hua/`: witness H, the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/grothendieck-project, commit `aef7db2`), an AI transcription whose batch headers name the Claude model of each pass (Claude Opus 5, Claude Opus 5.5) but no effort setting, in that project's own macros (`hua/transcripts/preamble/grothendieck.sty` says what each means: `\struck` a deletion, `\add` an insertion, `\marginal` a margin note, `\uncertain` a doubtful reading, `\ill` a word they could not read). Their page n is our scan n + 1. H has text for 12 of these 13 pages. Earlier checks found it at about 1.5 errors per 100 words on light pages and 3 to 8 on dense ones: plausible prose in place of the ink, struck text given as live, abbreviations expanded, margins left out, drawings described. A witness only, credited; this run writes nothing in their conventions.
  - No second reading of these pages exists yet: your own reading on the crop is the second witness, with witness H where it has the page.
- `WTA_1_026-038_notes.zip`, the nodes:
  - `NOTES_ON_THESE_PAGES.md`: every note entry on these pages (2: 0 from the notes of the Pro first passes, by GPT-6 Astra (ChatGPT Pro mode), written with a context of our earlier work; 0 from the math notes of Work's readings, by GPT-6.2 Astra at reasoning effort max (ChatGPT Work), written without context; 2 from the notes of Codex web, by GPT-6 Astra at reasoning effort max, which list only the steps the pages mark as unverified and the title sheets), in full, in page order, each with the object the sweep placed it under and the object's tag; `NOTES_INDEX.tsv`, the same as an index; `files/`, the whole files they come from;
  - `CONCORDANCE.md`, `CONCORDANCE.tsv`: for every object these entries are about, the entries on the same object elsewhere in the archive (28), nearest first, with their text;
  - `OBJECTS.tsv`: the sweep's rows of these 1 objects, whose tags are the handbook's draft tags;
  - `CHECKS.tsv`: what was already checked about these entries and objects (0 rows of our check register: who, how, the result).
- `WTA_1_026-038_context.zip`: the subject's own context. It holds: `this_folder/cote_1.tex`: the whole folder as transcribed so far, each page in the reading a pass starts from, for the argument before and after this range; `topics/SA23_TOPIC.md`: the catalogue of the topic (its folders, what is transcribed and how). Search these files for his objects and numbers: the passages of his published work that his pages annotate, draft or anticipate are the first grounds.
- `WTA_1_026-038_results.zip`: the statements of our own research runs that cite this folder. **Leave it closed until the units
  are written** (step 9).

Unzip every attachment except `WTA_1_026-038_results.zip` in your sandbox. **Look at the images yourself:** the whole page first,
then the thirds, and enlarge (crop and scale) every place you decide. Reading software (OCR) is not a substitute for
looking and is not used on these pages.

## How to work

1. **Start.** Write the current time (UTC) as the first line of `progress.log`.
2. **The units.** Draw the units from his own divisions. A unit is one piece of his writing: a numbered section, a list or question of his, a
   dated session, a construction with its proof attempt, a letter, a typed draft with his annotations; where he makes
   no division, the stretch of argument that one headnote can introduce. Keep his numbering. Give each unit the id
   `1:<its first scan>` (with `.2`, `.3` where two units start on the same scan).
3. **The nodes.** For each unit, gather what bears on it: the entries that cite its pages (`NOTES_ON_THESE_PAGES.md`),
   the entries on the same objects elsewhere (`CONCORDANCE.md`), its objects and their tags (`OBJECTS.tsv`, with
   `THEMES.tsv` and `LINKS.tsv`), and what was already checked about them (`CHECKS.tsv`). Every entry on these pages
   gets a verdict in `NOTES_VERDICTS.tsv`:
   - its anchor on the ink: the passage it quotes, confirmed or corrected;
   - its mathematics: confirmed, corrected, refuted, resting on a misreading, or not checkable, each with the reason;
   - where its content went: a note of a unit, a claim, a handbook item, a research direction, or nowhere (with the
     reason).

   None is left without a verdict, whatever an earlier triage or the sweep said of it. An entry is a lead, not a
   result: neither trusted nor presumed false. Some entries read his pages through our research on La Longue Marche or
   Les Dérivateurs; here the pages are read in their own terms, and such links are checked in step 9.
4. **The reading, wherever it matters.** The readings are AI readings of the same scans; the scan decides. **The rule:
   the mathematics raises the alarm, the ink decides.** In earlier controls, the mathematically expected word was
   wrong at 3 of 29 disputed places ("implique" for "indique", an added "en prenant", "sommes disjointes"), so a reading
   never changes on mathematical grounds alone.
   - The pages with no reading (scans 37) are transcribed first, in full, in our conventions (`PREAMBLE.tex`; his
     spelling, abbreviations and numbering as written; doubt marked in place with `\unsure{a|b}`, the first reading
     being what the ink shows), into `pages/1_scanNNN.tex`.
   - On every other page, list the places to decide: every doubt mark (`\unsure`) of the readings; every place where
     the readings differ in a word, a symbol, an index or a sign; every logic-bearing word that a claim turns on
     (quantifiers, negations, "si", "donc", "sauf", "ne ... pas", "il suffit", "implique" or "indique"); every margin
     note and insertion that a claim or a note uses. Read each place on the crop before you read what the readings
     have there: reading with a text in view lets plausible words through. Differences of macro syntax, spacing or
     punctuation that change no meaning are left alone.
   - Where the mathematics breaks as the page is read (a statement false as read, a step that does not follow, a symbol
     outside its type, a word outside his vocabulary for the object), go back to the crop. The reading changes only if
     the ink shows the other reading; otherwise it stands, and the break is his slip or a doubtful reading.

   Record every place you decided in `SCAN_CHECKS.tsv`, one row each (columns below): `check scan` rows where the ink
   confirms the reading, `scan error` rows where the reading is wrong (with the reading the ink shows), and
   `undecided` rows with the alternatives. This run does not rewrite the readings' page files; a script applies the
   `scan error` rows.
5. **The mathematics.** For each claim and question of his in the range, write today's precise statement with every
   hypothesis, and mark what in it is your reconstruction. Decide it under the rule of the section "What the outcome
   must be": redo every computation of his that it rests on (by hand where it is small, by program where a computer
   settles it, the program and its output kept in `scripts/`); prove it, or find it in the literature; or refute it
   with a counterexample and prove the corrected statement. Note the research directions you find while working, each
   with where it came from, in `RESEARCH_DIRECTIONS.md`, and work on them under the same rule.
6. **The companion's units.** For each unit, in this order:
   - the headnote: two to six sentences in the voice of a colleague who knows the field and the period: where we are
     in the folder and in his work, the date, what he is doing in today's terms, what comes before and after in this
     folder, in his other folders and in his published work. It says "probably" or "we think" where it conjectures, and
     why. It never retells his text;
   - the notes keyed to his lines, each one to four sentences, opening with its locator (`1:<scan>.<line>`), and
     of one of these kinds, in these phrasings: `grounds` (the result he uses, by exact locator: "By EGA 0_IV
     19.3.5."), `today` ("In today's terms: ..."), `step` ("The step left implicit: ..."), `draft` ("He first wrote
     '...'"; "He struck '...', which ..."), `slip` ("Read '...'", with the check that shows it; a slip is called a slip,
     plainly), `reading` ("Reading uncertain: '...' or '...'"), `link` (to his other folders and his published work,
     with dates), `fact` ("In fact, ...", a fact checked). No note interprets at length: interpretation belongs in the
     headnote;
   - the status of each claim and question of his, in his numbering: the statement as he makes it (a pointer to his
     line) and today's precise statement; as he left it, with his date (proved there / sketched / stated without proof
     / corrected by himself later, both places / false as stated, with the counterexample, the corrected statement and
     the version he most likely had in mind / open); later, dated and with exact references (in his published work,
     proved by others, or open today with the best known result); developed further, a line and the handbook item or
     our result where it is (step 9), never "solved two days later".

   And in `expansions.tsv`, every abbreviation of his in the range, one row per occurrence, so that a script can build
   the reading text with the expansions in square brackets.
7. **The sort into the handbook.** Decide, for everything the units hold, what stays in the unit and what becomes a
   handbook item. A note about his page (a slip, a draft, a reading, a pointer, the grounds of a step) stays in the unit.
   A definition, a statement, a claim of his, a question, a conjecture or a counterexample becomes an item in
   `ITEMS.tsv`: its kind, its statement in today's notation, its status (proved, with where the proof is; known, with
   the citation; his claim, with the gap named; open, with the strongest proved reduction; refuted, with the refined
   item), his places (every place on these pages and in the concordance where he treats it), the literature, its
   provenance (the entries it consumes) and its checks. Give it the tag of the object it belongs to from `OBJECTS.tsv`,
   or `new` with a proposed object name where none fits. An item already in the tag space (the same statement under
   the same object) is not repeated: give its existing place and add only what these pages change.
8. **The links.** In `LINKS.tsv`, link each unit to the tags it bears on, as suggested links with their evidence: the
   relation (states, discusses, proves, refutes, uses, the same question as, developed there), the locator on his
   page, and the item or entry that shows it. Every link is a suggestion with its evidence; none is forced.
9. **Our results, last.** Only when the units are written, append `results opened <UTC time>` to `progress.log` and
   open `WTA_1_026-038_results.zip`. In `CONSEQUENCES.tsv` (column `kind`): `bears_on`, each statement of our runs that bears on
   a claim, an item or a note of these pages (its tag, your id, the relation: same object / same statement / a
   consequence / a generalization / a counterexample / a contradiction, and the evidence); `quotes_corrected_reading`,
   each statement of our runs whose places quote a reading that a `scan error` row corrects (its tag, scan and line,
   the old and the new reading, the confidence). Add only links with evidence; force none. Nothing found is a valid
   result. A status in that file is our runs' claim, not a check. Then fill the "developed further" lines of step 6.
10. **The correction loop.** What the mathematics found goes back into what came before: the notes and the statuses
    corrected; a misreading that the mathematics exposed checked on the crop, the ink deciding, as a new row of
    `SCAN_CHECKS.tsv`.

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

**The items** are his claims and questions in the range (`CLAIMS_STATUS.tsv`), the mathematical claims of the entries,
and the research directions of `RESEARCH_DIRECTIONS.md`; each is a row of the ledger. A construction or a definition
is an item through what he claims of it; a computation through its result. **The main question** is his central open
question in the range, or, where he asks none, the claim the most other items depend on. Name it at the top of the
ledger.

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

## Rules

- **His terms first.** Every account is written first in his notation and his words (his objects, his names, his
  order of ideas), with today's restatement beside it, never instead of it. His words and ours never share a
  paragraph. Keep three things apart everywhere: what his pages show, what the sources say, and what is ours; label
  ours as ours.
- **Quotation.** A note or an item quotes at most a short phrase of his and refers to the rest by scan and line.
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
- **Everything.** Cover every page, every unit, every entry and every claim of the range; do not ask questions back.
  Make the decisions a careful editor and mathematician would make, state them, and carry on.

**Check events.** For every statement your work checks, uses or refutes (a claim of his, by its claim id; an item, by
its id; a note or an entry, by its id; a result of the literature, by its reference key; a statement of our runs, by
its tag), record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort,
run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in
this run / carried as background without fault found / refuted, with the refined statement's id), outcome, and where
the record is. The file has the six columns `id, date_utc, who, how, result, where`: the type goes in `how`, the
outcome in `result`, and `where` is the file and line or section of the record. Give each event the type of what
actually happened, neither more nor less: reading a statement while transcribing it is not a check of it.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `WTA_1_026-038_checkpoint_<NN>.zip` with `NN` counting up;
never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save
checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or
reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you
continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable
written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a
new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it,
the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export
of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints
are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is
lost.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.

## What to return

One zip file, `WTA_1_026-038.zip`, offered as the only download. Every table is tab-separated with the header given; every row
carries the run id `WTA_1_026-038` where a column `run` is named. It holds:
1. `UNITS.json`: one object per unit: `id`, `scans`, `lines`, `title` (his words where he gives one, else ours,
   marked), `date` (his, or inferred, with the evidence), `from_draft` (the draft units it covers, or `none`),
   `headnote` (LaTeX);
2. `NOTES.tsv`: `id, unit, locator, kind, text, sources, tag` (one row per keyed note; `sources` the entry ids it
   consumes; `tag` the object's tag);
3. `CLAIMS_STATUS.tsv`: `claim_id, unit, locator, his_words, statement, reconstruction, as_he_left_it, later,
   developed_further, status, proof_or_reference, tag, check_events, confidence` (`status`: proved, with where the
   proof is; known, the reference and locator; false, the counterexample and the corrected statement; open, the state
   reached);
4. `ITEMS.tsv`: `item_id, tag, kind, statement, status, proof_or_where, uses, his_places, literature, provenance,
   checks, run` (`item_id` is `WTA_1_026-038.<n>`; `tag` an existing tag, or `new: <proposed object name>`);
5. `LINKS.tsv`: `unit, tag, relation, locator, evidence, status` (`status` is `suggested`);
6. `SCAN_CHECKS.tsv`: `scan, line, kind, readings, ink_shows, decision, raised_by, confidence` (`kind`: check scan /
   scan error / undecided; `readings` each reading with its witness); and `pages/`, the new transcriptions of the
   pages that had none;
7. `expansions.tsv`: `scan, line, as_written, expansion, confidence`;
8. `NOTES_VERDICTS.tsv`: `entry_id, anchor, mathematics, placed, reason, right_object`;
9. `RESEARCH_DIRECTIONS.md` (each direction: where it came from, what was done, the state reached, and the questions
   worth a further research prompt) and `PROOFS.tex` (every proof and counterexample in full, one section per item);
10. `CONSEQUENCES.tsv`: `kind, tag, our_id, relation, evidence, scan, line, old_reading, new_reading, confidence`;
11. `references.bib`, every work cited, with its `note` field;
12. `PROGRESS_LEDGER.md`, `CHECK_EVENTS.tsv`, `progress.log` (the time, UTC, at the start, at each review, at the
    opening of the results and at the end), and `scripts/`, every program you ran, with its output.
