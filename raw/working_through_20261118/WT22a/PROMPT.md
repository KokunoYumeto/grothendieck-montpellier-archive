# Working through WT22a: Alexander Grothendieck's notes, Montpellier archive, cote 22, scans 002-018

## What this is

The Montpellier archive (fonds Grothendieck, Université de Montpellier) holds about 16,000 scanned pages of his
manuscripts. We are making a companion to them in the manner of the great editions of mathematicians' papers
(Whiteside's Newton, Neumann's Galois, Berndt's Ramanujan, the Colmez-Serre correspondence). The companion has two
layers that read as one:
- his text, transcribed faithfully and made readable;
- beside it, in one plain voice: a short headnote to each unit, notes keyed to his lines, and the status of each claim
  and question of his, dated and with references.

This run makes that material for one slice of one folder: **cote 22, scans 002-018** (17 pages: offprints of chapter 0_IV of EGA IV with his annotations, the annotated typescript, and the notes he wrote on the backs of typed sheets).
The folder's catalogue title: « [EGA IV]. [Chapitre] 0 IV. Cohen, différentielles, algèbres formellement simples (Compléments) : tirés à part (1963), tapuscrit annoté (s.d.), notes manuscrites (s.d.) ». It has 29 scans; this run takes scans 2-18, and the other part of the folder is a separate run.

It works the slice through as a colleague who means to use it would:
- reads it on the ink with two witnesses;
- corrects it where the ink shows an error, with the mathematics as the alarm;
- consumes the earlier research notes on it;
- writes the headnotes and the keyed notes;
- settles from the literature where each claim of his stands.

A second run takes the open questions this run lists and attacks them. A separate pass translates the corrected text
into English.

## The attachments


**The scans come in 4 zips** (`WT22a_scans_part1.zip` to `WT22a_scans_part4.zip`), each under 10 MB: unpack all of them into the same folder; together they are `WT22a_scans.zip`.

- `WT22a_scans.zip`: for every scan N of the slice, three images: `MPL_22+23_002-016_22_scanNNN.jpg` (the whole page) and `_a`,
  `_b` (its two halves at full resolution). The images are contrast-enhanced and sharpened.
- `WT22a_witnesses.zip`:
  - `README.md`, `page_map.tsv`;
  - `ours/`: witness O, the diplomatic transcription of these pages by GPT-6 Astra (ChatGPT Pro mode), one file per
    scan, with its doubts table, inventory and research notes. Its notes are the earlier notes this run consumes.
    `first_pass_PROMPT.md` defines our macros;
  - `hua/`: witness H, the transcription of the Commutator project of Michel Hua (github.com/Commutator-IO/
    grothendieck-project, commit `aef7db2`), made by AI models (Claude Opus 5 and Claude Opus 5.5, read again in part
    by Claude Fable 5.2), in that project's own macros. Their page n is our scan n + 1.
    `transcripts/preamble/grothendieck.sty` says what each macro means.
- `WT22a_context.zip`: the subject's own context, to be used from the start. It holds: `ega_fr/`, the French text of EGA 0_IV, sections 19 to 23 (formally smooth algebras and Cohen rings, derivations and differentials, differentials in characteristic p, differential criteria of smoothness and regularity), and of EGA IV, sections 16 and 17 (differential invariants; smooth, unramified and étale morphisms), as LaTeX from our edition; `ega_v/`, the typescripts of EGA V in the archive (cotes 24 and 25), transcribed by Claude over the API; `folder23/`, the transcribed pages of cote 23 (EGA IV, Compléments: his notes, letters of 1966 and 1968, a typescript; 15 of its 98 pages, by GPT-6 Astra in Pro mode); `folder26/`, cote 26 (EGA VI: plans, notations, open problems; 10 pages, by GPT-6 Astra at reasoning effort max in Codex). Cote 21 (chapter 0_III) has no transcription yet. Search these files for his objects and numbers: the passages of EGA that his pages annotate, draft or anticipate are the first grounds for the notes.
- `WT22a_results.zip`: `RESULTS_STATE.md`, the state of our own research on these subjects. **Leave it closed until
  stage 4.**

Unzip the first three in your sandbox. **Look at every image yourself:** the whole page first, then the halves, and
enlarge (crop and scale) every place you decide. Reading software (OCR) is not a substitute for looking and is not
used on these pages.

## Stage 1: the reading, on the ink

**The rule of this stage: the mathematics raises the alarm, the ink decides.** In earlier controls, the mathematically
expected word was wrong at 3 of 29 disputed places ("implique" for "indique", an added "en prenant", "sommes
disjointes"). So a reading never changes on mathematical grounds alone.

For each page, in order:
1. **First the crop, before either witness.** Read on the enlarged image:
   - every logic-bearing word: quantifiers, negations, "si", "donc", "sauf", "ne ... pas", "il suffit", "en
     général";
   - every index, exponent, sign, inequality and arrow direction;
   - every margin note, every insertion and every deletion.

   Do this before looking at witness O. Reading with its text in view lets plausible words through.
2. **Then the witnesses.** Compare your reading with witness O and witness H, word by word. Where they differ from each
   other or from your reading, decide on the ink. Every doubt mark of witness O is a place to decide on the ink.
3. **Then the mathematics.** Read the page as mathematics. Where it breaks (a statement false as read, a step that
   does not follow, a symbol that cannot be what is written), go back to the crop. Correct the reading only if the ink
   shows the other reading. Otherwise the reading stands, and the break becomes a note (his slip, or a reading
   uncertain).
4. **Missing pages.** A scan of the slice that witness O does not have is transcribed in full, in our conventions.

Write the corrected page files in `pages/` (named as in witness O, our macros, his spelling and abbreviations as
written). For every change, add a row to `CHANGES.md`, giving:
- scan, line, O's reading, H's reading, the final reading;
- what the scan shows (the strokes you saw, the crop used);
- what raised it: the witnesses differ / a doubt mark / a logic-bearing word / the mathematics / an omission;
- confidence (high, medium, low).

At the top of `CHANGES.md`, give the counts, and the consequential corrections (those that change the mathematics),
one per line.

When every page is done, write the SHA-256 of every page file to `progress.log` with the line `reading frozen <UTC
time>`. From then on the reading changes only through a new row of `CHANGES.md` with its evidence.

Then **`expansions.tsv`**: every abbreviation of his in the slice, one row per occurrence (scan, line, as written, its
expansion, confidence), so that a script can build the reading text with the expansions in square brackets.

## Stage 2: the units, the headnotes and the keyed notes

**Units.** Divide the slice into the units of his writing:
- his own divisions first: his numbered items, headings, dated sessions, a list, a letter, a typed page with his
  annotations;
- elsewhere, the stretch of argument that one headnote can introduce.

In `units.json`, one object per unit: `id` (22.<n>), `scans`, `lines`, `title` (his words where he gives a title,
else ours, marked), `date` (his, or inferred, with the evidence), and `headnote`.

**The headnote** is two to six sentences in the voice of a colleague who knows the field and the period. It says:
- where we are in the folder and in his work, and the date;
- what he is doing, in today's terms;
- what comes before and after, in this folder, in his other folders and in his published work.

It says "probably" or "we think" where it conjectures, and why. It never retells his text.

**The earlier notes.** Every entry of witness O's research notes about these scans gets a verdict and a place in
`notes_verdicts.tsv`: entry (its heading), verdict, place, reason. A verdict is one of:
- kept, as note n;
- merged into note n;
- corrected (how);
- withdrawn (why);
- rests on a misreading (the corrected reading).

None is left without one. The place says where the entry's content goes: a unit and a note kind of this companion
(`22.3, slip`), the research layer under a topic of the archive (`research: Cohen rings`), or nowhere (withdrawn).
Placing every entry now is what lets the companion and the research volumes be written from these files.

**The keyed notes.** In `notes.json`, one object per note: `unit`, `locator` (scan.line), `kind`, `text` (LaTeX,
one to four sentences), `sources` (the earlier note entries it consumes), `topic` (the topic of the archive it
belongs to, in the catalogue's words). The kinds, with their fixed openings:
- `grounds`: the result he uses, by exact locator in the context ("By EGA 0_IV 19.3.5."), so that a reader can check
  the step;
- `today`: "In today's terms: ...";
- `step`: "The step left implicit: ...";
- `draft`: "He first wrote '...'" / "He struck '...', which ...";
- `slip`: "Read '...'", with the check that shows it; a slip is called a slip, plainly;
- `reading`: "Reading uncertain: '...' or '...'; ...";
- `link`: to his other folders and to his published work, with dates ("the same question in folder 23, scan 12";
  "this becomes EGA IV 11.1.1");
- `fact`: "In fact, ...", a fact checked.

Notes are short and exact. Interpretation goes into the headnotes, and the status of claims into stage 3.

## Stage 3: where his claims and questions stand

In `claims.json`, one object for every claim and every question of his in the slice: a statement, construction,
computation, conjecture, question, hope or doubt. Use his numbering where he gives one, else `22.<unit>.<k>`.
Fields:
- `locator` and `his_statement` (a pointer to his lines); `topic` (the topic of the archive, in the catalogue's words);
- `statement`: today's precise statement with all hypotheses; `reconstruction`: what in it is ours rather than his;
- `as_he_left_it`: proved there / sketched / stated without proof / corrected by himself later (both places) / false
  as stated (with the counterexample, every hypothesis checked, the corrected statement, and the version he most likely
  had in mind) / open; with his date;
- `later`: what became of it, with dates and exact references: in his published work (EGA, SGA, his papers), proved
  by others, or still open with the best known result. Find it by searching zbMATH Open, arXiv, MathOverflow, Numdam,
  the EGA and SGA in the context, and the collected works and bibliographies of the authors concerned. Follow
  references backwards from later papers when a title search finds nothing. The absence of a first hit is weak
  evidence, and a later paper on the same broad subject is weak evidence that the exact claim was settled: match the
  exact quantifiers and hypotheses;
- `computation`: every computation of his that the claim rests on, redone, with code and output;
- `refs`, `confidence`.

Every computation and every proof of yours is checked a second time before you finish, independently (re-derived, or
re-run with other parameters), and the check is recorded.

The claims and questions that are **open** (open as he left it, and open today or not found settled) go into
`open_questions.md`, for the second run. For each:
- the strongest formulation his text supports, and the strongest formulation plausibly true today;
- the state of the art, with exact references;
- the first approaches worth trying, and why.

## Stage 4: our results, last

Only now, append `results opened <UTC time>` to `progress.log` and open `WT22a_results.zip`. In `consequences.tsv`,
list the entries of `RESULTS_STATE.md` that bear on these pages: entry id, claim or note id, relation (same object /
same statement / a consequence / a generalization / a counterexample), evidence. Add only links with evidence; force
none. Nothing found is a valid result.

## Rules

- Keep three things apart everywhere: what his pages show, what the sources say, and what you infer. His words and
  ours never share a paragraph.
- Every reference must be real and checked: give a link or DOI that you opened (`note = {verified}`); otherwise mark
  it `note = {unverified}`. Never cite from memory without checking.
- Never fill a gap in his text from what he "must have" meant; mark a reconstruction as yours.
- One stream: do the pages yourself, in order, in one stream. Do not split them among parallel workers.
- Cover every page, every unit, every earlier note entry and every claim of the slice.
- Do not stop early and do not ask questions back: make the decisions a careful editor and mathematician would make,
  state them, and carry on to the end.

**Check events.** For every statement your work checks, uses or refutes (a claim of his, by its claim id; a note, by
its id; a result of the literature, by its reference key; an entry of `RESULTS_STATE.md`, by its id), record its
check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted
proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as
background without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what
actually happened, neither more nor less: reading a statement while transcribing it is not a check of it.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every hour of work, each under a new name, `WT22a_checkpoint_<NN>.zip` with `NN` counting up; never
overwrite, rename or delete an earlier checkpoint. Save checkpoints once an hour and at no other time: none after a
page, a unit or a stage. A checkpoint is one ZIP holding every deliverable written so far and everything that
documents the work (the pages, the tables, `CHECK_EVENTS.tsv`, `progress.log`, the code), so that a new session can
continue from it and the attached files. Leave the attached files themselves out of it: we have them. It is never a
JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it. If the workspace comes back empty,
restore it from the newest checkpoint before you continue.

**If the execution environment disconnects.** Wait for it and retry for at least 10 minutes. If it does not come
back, the work must still reach us, so write it out in this chat as text: every file finished so far in full, each in
its own code block headed by its file name (the code you ran to save each file contains its text: take it from
there). Then go on with the remaining stages directly in the chat, in the same form. Say at the start which files are
done and which are not. An answer that only reports the disconnection, describes the checkpoint or asks for the files
again, without writing out the work, is not acceptable.

## What to return

One zip file, `WT22a.zip`, offered as the only download, holding:
1. `pages/` (the corrected page files) and `WT22a_transcription.tex` (all pages in order, one LaTeX fragment, our macros
   only);
2. `CHANGES.md`;
3. `expansions.tsv`;
4. `units.json`;
5. `notes.json`;
6. `notes_verdicts.tsv`;
7. `claims.json`;
8. `open_questions.md`;
9. `consequences.tsv`;
10. `references.bib`, every work cited, with its `note` field;
11. `CHECK_EVENTS.tsv`, `progress.log` (the time, UTC, at the start, at the end of each stage and at the end), and
    every program you ran, with its output.
