# WTB_150_025-037: the foundational check of Alexander Grothendieck's manuscript, cote 150, scans 25-37

## What this is

The Montpellier archive (fonds Grothendieck, Université de Montpellier) holds about 16,000 scanned pages of his
manuscripts, and about 10,000 of them are transcribed. While the pages were being transcribed, AI models wrote notes on
their mathematics, and nobody has worked those notes through yet. Everything later work builds on these pages (an
edition, a handbook of the mathematics, research) needs a foundation that has been checked: his claims decided, his
computations redone, the notes confirmed or corrected, and the readings checked on the ink wherever the mathematics
depends on them.

This run checks one range of one folder: **cote 150, scans 25-37** (13 pages). The folder's catalogue title: « Espaces stratifiés et voisinages côniques (ou : déploiement des espaces stratifiés) : notes manuscrites (s.d.). » (1981-1982[152]). It has 98 scans; this run takes scans 25-37, range 3 of 8 of the folder; the other ranges are separate runs.
No draft units exist for these pages.

It is a mathematical second pass: it works through the mathematics of the pages and of the notes on them, and reads the
ink wherever a reading matters to the mathematics. It writes no commentary for readers: its outputs are checked
statements, verdicts and corrections, in fixed-format files that a script merges across the ranges.

**A correction of 19 November 2026.** On 150/033, condition (20)ⓐ reads "Les Ẋ_β disjoints", with the dot, as the first transcription has it. The second pass of 17 November (its change 12, "Les X_β disjoints", in the witnesses and in the notes' CHECKS.tsv) is reversed: a reading of the native scan on 19 November (Claude Opus 5.5 at effort max) found the dot, and it is the only reading that constrains the data. Use Ẋ_β there.

## The attachments

- `WTB_150_025-037_scans.zip`: for every scan N of the range, four images: `150_scanNNN.jpg` (the whole page) and `_a`, `_b`,
  `_c` (its top, middle and bottom thirds, or left, middle and right thirds of a landscape sheet, overlapping a little,
  at full resolution). The pages just before and after this range (scans 24 and 38) are attached whole, as `..._neighbour.jpg`, to follow an argument across the cut: they are worked in their own ranges, and are read here only to complete such an argument. The images are contrast-enhanced and sharpened.
- `WTB_150_025-037_witnesses.zip`: `README.md` (start there), `page_map.tsv` (for every scan, every reading and who made it), and:
  - `first/MPL_150_001-043/`: witness O, the first pass by GPT-6 Astra (ChatGPT Pro mode), 14 Nov 2026, for 13 of the 13 pages, with its doubts table and the prompt it was made with (`first_pass_PROMPT.md`, which defines our macros); earlier checks found about 1 to 2.5 errors per 100 words on his dense hand, mostly fluent misreadings, dropped short conditions or symbols, wrong indices, signs and arrow directions, and missed deletions; only a third of them carried a doubt mark.
  - `second/MPL_150_001-043/`: witness K, the second pass of Claude Opus 5.5 at effort max (13-17 Nov 2026), for 13 of the 13 pages, with its changes tables and its checked notes; a second pass against the scans; on the two control folders it left about 0.5 errors per 100 words and removed about three-quarters of the first pass's errors, but left most of Pro's doubt marks undecided.
  - `hua/`: witness H, the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/grothendieck-project, commit `aef7db2`), an AI transcription whose batch headers name the Claude model of each pass (Claude Opus 5, Claude Opus 5.5) but no effort setting, in that project's own macros (`hua/transcripts/preamble/grothendieck.sty` says what each means: `\struck` a deletion, `\add` an insertion, `\marginal` a margin note, `\uncertain` a doubtful reading, `\ill` a word they could not read). Their page n is our scan n + 1. H has text for 13 of these 13 pages. Earlier checks found it at about 1.5 errors per 100 words on light pages and 3 to 8 on dense ones: plausible prose in place of the ink, struck text given as live, abbreviations expanded, margins left out, drawings described. A witness only, credited; this run writes nothing in their conventions.
- `WTB_150_025-037_notes.zip`, the nodes:
  - `NOTES_ON_THESE_PAGES.md`: every note entry on these pages (27: 27 from the notes of the Pro first passes, by GPT-6 Astra (ChatGPT Pro mode), written with a context of our earlier work; 0 from the math notes of Work's readings, by GPT-6.2 Astra at reasoning effort max (ChatGPT Work), written without context; 0 from the notes of Codex web, by GPT-6 Astra at reasoning effort max, which list only the steps the pages mark as unverified and the title sheets), in full, in page order, each with the object the sweep placed it under and the object's tag; `NOTES_INDEX.tsv`, the same as an index; `files/`, the whole files they come from;
  - `CONCORDANCE.md`, `CONCORDANCE.tsv`: for every object these entries are about, the entries on the same object elsewhere in the archive (80), nearest first, with their text;
  - `OBJECTS.tsv`: the sweep's rows of these 7 objects, whose tags are the handbook's draft tags; `THEMES.tsv` and `LINKS.tsv`: their themes and the sweep's links;
  - `CHECKS.tsv`: what was already checked about these entries and objects (23 rows of our check register: who, how, the result).
- `WTB_150_025-037_context.zip`: the subject's own context. It holds: `this_folder/cote_150.tex`: the whole folder as transcribed so far, each page in the reading a pass starts from, for the argument before and after this range; `topics/SA10_TOPIC.md`: the catalogue of the topic (its folders, what is transcribed and how); `sweep3/SA10/`: the deep sweep of this topic (horizontal sweep 3, Claude Opus 5.5 at effort max, 18-19 Nov 2026; each file names its agent): `STUDY.md` (what the topic's pages and notes establish), `HUNCHES.md`, `RESEARCH_PACKAGES.md`, `CORRECTIONS.tsv` (readings and statements it corrected), `DEPENDS.tsv`, `CHECK_EVENTS.tsv` and `readings/` (passages it read in full, with their corrections). Build on it: what it settles is used and rechecked in use, not redone, and a correction of yours to it is a row of your tables; where it and the ink disagree, the ink decides. Search these files for his objects and numbers: the passages of his published work that his pages annotate, draft or anticipate are the first grounds.
- `WTB_150_025-037_results.zip`: the statements of our own research runs that cite this folder. **Leave it closed until the
  check is done** (step 7).

Unzip every attachment except `WTB_150_025-037_results.zip` in your sandbox. **Look at the images yourself:** the whole page first,
then the thirds, and enlarge (crop and scale) every place you decide. Reading software (OCR) is not a substitute for
looking and is not used on these pages.

## How to work

1. **Start.** Write the current time (UTC) as the first line of `progress.log`.
2. **The units.** Draw the units from his own divisions. A unit is one piece of his argument: a numbered section, a list or question of his, a
   dated session, a construction with its proof attempt, a letter, a typed draft with his annotations; where he makes
   no division, a stretch of argument with one subject. Give each unit the id `150:<its first scan>` (with `.2`,
   `.3` where two units start on the same scan) and list the units in `UNITS.tsv`.
3. **The nodes.** For each unit, gather what bears on it: the entries that cite its pages (`NOTES_ON_THESE_PAGES.md`),
   the entries on the same objects elsewhere (`CONCORDANCE.md`), its objects and their tags (`OBJECTS.tsv`, with
   `THEMES.tsv` and `LINKS.tsv`), and what was already checked about them (`CHECKS.tsv`). Every entry on these pages
   gets a verdict in `NOTES_VERDICTS.tsv`:
   - its anchor on the ink: the passage it quotes, confirmed or corrected;
   - its mathematics: confirmed, corrected, refuted, resting on a misreading, or not checkable, each with the reason;
   - where its content went: a claim, a finding, a research direction, or nowhere (with the reason).

   None is left without a verdict, whatever an earlier triage or the sweep said of it. An entry is a lead, not a
   result: neither trusted nor presumed false. Some entries read his pages through our research on La Longue Marche or
   Les Dérivateurs; here the pages are read in their own terms, and such links are checked in step 7.
4. **The reading, wherever it matters.** The readings are AI readings of the same scans; the scan decides. **The rule:
   the mathematics raises the alarm, the ink decides.** In earlier controls, the mathematically expected word was
   wrong at 3 of 29 disputed places ("implique" for "indique", an added "en prenant", "sommes disjointes"), so a reading
   never changes on mathematical grounds alone.
   - The pages with no reading (none here: every page of this range has a reading) are transcribed first, in full, in our conventions (`PREAMBLE.tex`; his
     spelling, abbreviations and numbering as written; doubt marked in place with `\unsure{a|b}`, the first reading
     being what the ink shows), into `pages/150_scanNNN.tex`.
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
5. **The mathematics.** For each claim and question of his in the range, and for each mathematical claim of the
   entries, write today's precise statement with every hypothesis, and mark what in it is your reconstruction. Decide
   it under the rule of the section "What the outcome must be": redo every computation it rests on (by hand where it
   is small, by program where a computer settles it, the program and its output kept in `scripts/`); prove it, or find
   it in the literature; or refute it with a counterexample and prove the corrected statement. Note the research
   directions you find while working, each with where it came from, in `RESEARCH_DIRECTIONS.md`, and work on them
   under the same rule.
6. **The findings.** For each unit, in `FINDINGS.md`: what he does, in two or three sentences of today's mathematics;
   what was checked and how (the claims, the computations, the readings); what was found (his slips with the corrected
   form, the notes corrected or refuted, the scan errors); and what is left for the research directions.
7. **Our results, last.** Only when the check is done, append `results opened <UTC time>` to `progress.log` and open
   `WTB_150_025-037_results.zip`. In `CONSEQUENCES.tsv` (column `kind`): `bears_on`, each statement of our runs that bears on a
   claim or an entry of these pages (its tag, your id, the relation: same object / same statement / a consequence / a
   generalization / a counterexample / a contradiction, and the evidence); `quotes_corrected_reading`, each statement
   of our runs whose places quote a reading that a `scan error` row corrects (its tag, scan and line, the old and the
   new reading, the confidence). Add only links with evidence; force none. Nothing found is a valid result. A status in
   that file is our runs' claim, not a check.
8. **The correction loop.** What the mathematics found goes back into what came before: the verdicts and the statuses
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

**The items** are his claims and questions in the range, the mathematical claims of the entries, and the research
directions of `RESEARCH_DIRECTIONS.md`; each is a row of the ledger. A construction or a definition is an item through
what he claims of it; a computation through its result. **The main question** is his central open question in the
range, or, where he asks none, the claim the most other items depend on. Name it at the top of the ledger.

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

- **His terms first.** Every statement is written first in his notation and his words, with today's form beside it.
  Keep three things apart everywhere: what his pages show, what the sources say, and what is ours; label ours as ours.
- **Quotation.** Quote at most a short phrase of his at a time, and refer to the rest by scan and line.
- **The literature.** Every reference is real and checked: give a link or DOI that you opened (`note = {verified}` in
  `references.bib`); otherwise mark it `note = {unverified}`. Never cite from memory without checking. Search zbMATH
  Open, arXiv, MathOverflow, Numdam, the EGA and SGA in the context, and the collected works and bibliographies of the
  authors concerned; follow references backwards from later papers when a title search finds nothing. The absence of
  a first hit is weak evidence, and a later paper on the same broad subject is weak evidence that the exact claim was
  settled: match the quantifiers and the hypotheses.
- **No completion presented as his.** Never fill a gap in his text from what he "must have" meant; mark a
  reconstruction as yours. Never lower his statement to match a proof you can give.
- **One stream.** Do the pages and the mathematics yourself, in order, in one stream: do not split them among parallel
  workers.
- **Everything.** Cover every page, every unit, every entry and every claim of the range; do not ask questions back.
  Make the decisions a careful mathematician would make, state them, and carry on.

**Check events.** For every statement your work checks, uses or refutes (a claim of his, by its claim id; a note or an
entry, by its id; a result of the literature, by its reference key; a statement of our runs, by its tag), record its
check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted
proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as
background without fault found / refuted, with the refined statement's id), outcome, and where the record is. The file
has the six columns `id, date_utc, who, how, result, where`: the type goes in `how`, the outcome in `result`, and
`where` is the file and line or section of the record. Give each event the type of what actually happened, neither
more nor less: reading a statement while transcribing it is not a check of it.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `WTB_150_025-037_checkpoint_<NN>.zip` with `NN` counting up;
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

One zip file, `WTB_150_025-037.zip`, offered as the only download. Every table is tab-separated with the header given. It holds:
1. `UNITS.tsv`: `id, scans, title, from_draft` (`title` his words where he gives one, else ours, marked; `from_draft`
   the draft units it covers, or `none`);
2. `SCAN_CHECKS.tsv`: `scan, line, kind, readings, ink_shows, decision, raised_by, confidence` (`kind`: check scan /
   scan error / undecided; `readings` each reading with its witness); and `pages/`, the new transcriptions of the
   pages that had none;
3. `CLAIMS_STATUS.tsv`: `claim_id, unit, locator, his_words, statement, reconstruction, as_he_left_it, later, status,
   proof_or_reference, tag, check_events, confidence` (`status`: proved, with where the proof is; known, the reference
   and locator; false, the counterexample and the corrected statement; open, the state reached);
4. `NOTES_VERDICTS.tsv`: `entry_id, anchor, mathematics, placed, reason, right_object`;
5. `FINDINGS.md` (step 6);
6. `RESEARCH_DIRECTIONS.md` (each direction: where it came from, what was done, the state reached, and the questions
   worth a further research prompt) and `PROOFS.tex` (every proof and counterexample in full, one section per item);
7. `CONSEQUENCES.tsv`: `kind, tag, our_id, relation, evidence, scan, line, old_reading, new_reading, confidence`;
8. `references.bib`, every work cited, with its `note` field;
9. `PROGRESS_LEDGER.md`, `CHECK_EVENTS.tsv`, `progress.log` (the time, UTC, at the start, at each review, at the
   opening of the results and at the end), and `scripts/`, every program you ran, with its output.
