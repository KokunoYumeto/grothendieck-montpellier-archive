# OBJ_H095+H097: the foundational entry for 2 objects (H095, H097), from Alexander Grothendieck's Montpellier manuscripts

## What this is

The Montpellier archive (fonds Grothendieck, Université de Montpellier) holds about 16,000 scanned pages of his
manuscripts, and about 10,000 of them are transcribed. While the pages were being transcribed, AI models wrote notes on
their mathematics: several thousand entries, which nobody has worked through yet. A first sweep (Claude Opus 5.5 at
effort max, 18 November 2026) sorted every entry by the mathematical object it is about and gave each object a tag.

We are writing the handbook of the archive: one foundational entry for each object. An entry says what he wrote about
the object and where, what the object is in today's mathematics, and where each of his statements stands, with the
proof, the reference or the counterexample. Later work builds on these entries, so they must be right.

This run writes the entry for:
- **H095**: faithful flatness and derivatives for elementary function rings; divided derivatives (in the archive's topic Séminaire de Géométrie Algébrique (SGA)). The sweep's one-line statement: Pages (cote 39 scan 15): faithful flatness an explicit unresolved question; the note claims polynomial families refute faithfulness under a differential-only reading.
- **H097**: Weierstrass division and preparation for elementary function rings (in the archive's topic Séminaire de Géométrie Algébrique (SGA)). The sweep's one-line statement: Pages (cote 39 scans 19-20): unique division gives a normalized preparation factorization; cancelled proof routes do not cancel the final theorem; the final scalar alpha does not match the earlier unit series.

The entries cite 4 pages of 1 folder:
- cote 39, « Fonctions et structures " élémentaires" [Schémas formels, théorème de préparation] : notes manuscrites (s.d.). » ([vers 1960-1970][36]): scans 13, 15, 19-20

There are 10 entries: 10 from Pro's notes. These objects are small and belong to the same topic, so one run takes them together; each gets its own entry.

The entries are leads, not results. Each one is worked through to a verdict: neither trusted nor presumed false.

## The attachments

- `OBJ_H095+H097_entries.zip`:
  - `ENTRIES.md`: every note entry about these objects in full. Each is headed by its id, its source (the return and
    the file), the cote and scans it cites, its kind, and the sweep's placement of it. The placement's `basis` says
    whether the sweep read only the entry's heading (`index-row`), the entry (`entry-read`), or also the page
    (`passage-read`); `fidelity` says what the page showed where the sweep read it.
  - `ENTRIES.tsv`: the same, as an index.
  - `OBJECT.tsv`: the sweep's rows for these objects.
  - `CHECKS.tsv`: what was already checked about these entries and these objects (rows of our check register: who,
    how, the result). A row says what one check found; it settles nothing beyond that check.

  Who wrote the entries:
  - ids `<package>#<n>`: GPT-6 Astra (ChatGPT Pro mode), with its transcriptions of 9-17 November 2026, using a
    context of our earlier work;
  - ids `work:<folder>#<n>`: GPT-6.2 Astra at reasoning effort max (ChatGPT Work), as the mathematical notes of its
    readings of 17-18 November, written without context;
  - ids `codex:<folder>#<n>`: GPT-6 Astra at reasoning effort max (Codex web), 13-15 November; these list only the
    steps the pages mark as unverified and the title sheets.
- `OBJ_H095+H097_pages.zip`:
  - `PASSAGES.md`: for every page the entries cite, the reading of the page in our LaTeX conventions, and the second
    reading of it where one exists. `PREAMBLE.tex` defines the macros: `\deleted{}` struck text, `\inserted{}` an
    insertion, `\margin{}` a margin note, `\unsure{a|b}` a doubtful reading with its alternative (the first is what the
    reader saw), `\illegible{n}`.
  - `page_map.tsv`: for each page, which reading is which, and by whom.
  - `transcriptions/`: the whole of every folder this object occurs in, page by page. Use them to find his other
    statements on the object by searching for his words and his notation; do not read them through.
- `OBJ_H095+H097_scans.zip`: the whole-page images of 4 pages the entries cite, from the archive's PDFs,
  contrast-enhanced and sharpened: `<cote>_scanNNN.jpg`. Look at an image yourself wherever a reading
  decides a statement, and crop and enlarge the place in your sandbox. Reading software (OCR) is not a substitute for
  looking and is not used on these pages.
- `OBJ_H095+H097_context.zip`: the subject's own context. It holds the catalogue of the topic, the neighbouring objects with their tags, and no text of his published work (none of ours matches these folders; find the passages of EGA, SGA or his papers that these pages draft or anticipate in the literature, and cite them by exact locator).
- `OBJ_H095+H097_results.zip`: the statements of our own research runs that cite these folders. **Leave it closed until the
  entry is written** (step 6).

Unzip every attachment except `OBJ_H095+H097_results.zip` in your sandbox.

## How to work

1. Write the current time (UTC) as the first line of `progress.log`.
2. **His statements.** Read every entry and the passages it cites. Then gather every statement of his on the object:
   in the cited pages, and, by searching `transcriptions/` for his names and notation, on the other pages of these
   folders. A statement is a claim, a definition with what he claims of it, a construction, a computation, a
   question, a conjecture, a hope or a doubt. For each, record:
   - its id (`<tag>.<n>, by the object's tag`);
   - its locator: cote, scan and the line on the page, counted from the top (`22/020.3`);
   - his words, as a short quotation;
   - his date, where the folder or the page gives one.

   Keep his order and his notation.
3. **The ink decides the reading; the mathematics raises the alarm.** In earlier controls, the mathematically
   expected word was wrong at 3 of 29 disputed places ("implique" for "indique", an added "en prenant", "sommes
   disjointes"). So:
   - where a statement turns on a word (a quantifier, a negation, "si", "donc", "sauf", an index, a sign, the
     direction of an arrow), look at that place on the scan before you use it;
   - where the mathematics breaks as the page is read, go back to the scan. The reading changes only if the ink shows
     the other reading; otherwise the reading stands, and the break is his slip or a doubtful reading.
   - A reading that the mathematics expects never replaces the reading on mathematical grounds alone.

   Record every such place in `READINGS.tsv`, whatever its outcome. This run does not rewrite the transcription: a
   folder pass with the full scans settles the readings, and these rows are its leads.
4. **The mathematics.** For each statement, write today's precise statement with every hypothesis, and mark what in
   it is your reconstruction rather than his. Then decide it (section "What the outcome must be"):
   - redo every computation of his that it rests on, by hand where it is small and by program where a computer
     settles it, and keep the program and its output in `scripts/`;
   - prove it, or find it in the literature;
   - or refute it: a counterexample with every hypothesis checked, then the corrected statement, the version he most
     likely had in mind, with its proof.
5. **The entries.** Give every entry of `ENTRIES.md` its verdict in `NOTES_VERDICTS.tsv`:
   - its anchor on the page: the passage it quotes, confirmed or corrected;
   - its mathematics: confirmed, corrected, refuted, resting on a misreading, or not checkable, each with the reason;
   - where its content went: a statement id, the groundwork, a link, a reading row, or nowhere (with the reason).

   None is left without a verdict. Every entry is read in full, whatever the sweep's placement says; where the sweep
   placed an entry under the wrong object, say so and name the right one.
6. **Our results, last.** Only when the entry is written, append `results opened <UTC time>` to `progress.log`, open
   `OBJ_H095+H097_results.zip`, and list in `CONSEQUENCES.tsv` the statements of our runs that bear on this object: the
   statement's tag, your statement id, the relation (same object / same statement / a consequence / a generalization /
   a counterexample / a contradiction), and the evidence. Add only links with evidence; force none. Nothing found is a
   valid result. A status in that file is our runs' claim, not a check.
7. **The entry.** Write `ENTRY.md` last (section "What to return").

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

**The items** are his statements on the object (step 2) and the mathematical claims of the entries (step 5); each is a
row of the ledger. A construction or a definition is an item through what he claims of it: that it is well defined,
and the properties he states. A computation is an item through its result. **The main question** is the object's
central statement: the claim or question of his that the other items serve, or, where none stands out, the statement
the most other items depend on. Name it at the top of the ledger.

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
done. An item may carry the status "open" in the entry only when the progress check has stopped its work, or when the
session itself ends first (the environment stops you, not your choice). Then the first line of `ENTRY.md` reads
INCOMPLETE in the second case, and every undecided row carries the state reached, every approach tried with where it
failed, the strongest result known in the literature with its locator, and the next step you would take. Never
present such a return as complete or as following an allowed alternative: there is none.

## Rules

- **His terms first.** Write each statement first in his notation and his words (his objects, his names, his order),
  then today's form beside it. His words and ours never share a paragraph. Keep three things apart everywhere: what
  his pages show, what the sources say, and what is ours; label ours as ours.
- **Quotation.** Quote at most a short phrase of his at a time, and refer to the rest by cote, scan and line.
- **The literature.** Every reference is real and checked: give a link or DOI that you opened (`note = {verified}` in
  `references.bib`); otherwise mark it `note = {unverified}`. Never cite from memory without checking. Search zbMATH
  Open, arXiv, MathOverflow, Numdam, the EGA and SGA, and the collected works and bibliographies of the authors
  concerned; follow references backwards from later papers when a title search finds nothing. The absence of a first
  hit is weak evidence, and a later paper on the same broad subject is weak evidence that the exact statement was
  settled: match the quantifiers and the hypotheses.
- **No completion presented as his.** Never fill a gap in his text from what he "must have" meant; mark a
  reconstruction as yours. Never lower his statement to match a proof you can give.
- **One stream.** Do the work yourself, in one stream: do not split it among parallel workers.
- **Every item and every entry.** Cover every statement and every entry; do not ask questions back. Make the
  decisions a careful mathematician would make, state them, and carry on.

**Check events.** For every statement your work checks, uses or refutes (a statement of his, by its id; an entry, by
its id; a result of the literature, by its reference key; a statement of our runs, by its tag), record its check
events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof
check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as
background without fault found / refuted, with the refined statement's id), outcome, and where the record is. The
file has the six columns `id, date_utc, who, how, result, where`: the type goes in `how`, the outcome in `result`,
and `where` is the file and line or section of the record. Give each event the type of what actually happened,
neither more nor less: reading a statement is not a check of it.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `OBJ_H095+H097_checkpoint_<NN>.zip` with `NN` counting up;
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

One zip file, `OBJ_H095+H097.zip`, offered as the only download, holding:
1. `ENTRY.md`, the entry, in English (his words in his language, as written), one section per object, each in the eight parts below:
   1. the object in his terms (his names and notation) and in today's terms;
   2. where he writes about it: the folders and pages, with their dates, in his order;
   3. his statements: for each, its id, locator and short quotation; today's precise statement with every
      hypothesis; and its status line (proved, with where the proof is; known, with the reference and locator; false,
      with the counterexample and the corrected statement; or open, with the state reached), the check and the
      confidence;
   4. the groundwork a reader needs beside his words: the definitions, the results he uses (by exact locator), the
      steps he leaves implicit, and what was known when he wrote;
   5. what became of it: in his published work (EGA, SGA, his papers), in the work of others, and what is open today,
      with dates and exact references;
   6. links to the other objects, by tag (`OBJECTS_NEARBY.tsv` in the context lists them);
   7. the entries: how many, and their verdicts in brief;
   8. our results that bear on it (from step 6), kept apart from the rest;
2. `STATEMENTS.tsv`, one row per statement, with the columns `id, tag, locator, his_words, date, statement,
   reconstruction, status, proof_or_reference, later, check_events, confidence`;
3. `PROOFS.tex`: every proof and every counterexample in full, one section per statement id, as a LaTeX fragment;
4. `NOTES_VERDICTS.tsv` (step 5), with the columns `entry_id, anchor, mathematics, placed, reason, right_object`;
5. `READINGS.tsv` (step 3), with the columns `cote, scan, line, reading, what_the_mathematics_expects, scan_shows,
   decision, confidence`;
6. `LINKS.tsv`: `tag, other_tag, relation, evidence` (relation: same object / special case / generalization / uses /
   used by / same question elsewhere / contradicts);
7. `CONSEQUENCES.tsv` (step 6);
8. `references.bib`, every work cited, with its `note` field;
9. `PROGRESS_LEDGER.md`, `CHECK_EVENTS.tsv`, `progress.log` (the time, UTC, at the start, at each review and at the
   end), and `scripts/`, every program you ran, with its output.
