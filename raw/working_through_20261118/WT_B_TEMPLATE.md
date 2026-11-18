# His open questions, {S}: Alexander Grothendieck's notes, Montpellier archive, cote {COTE}, scans {RANGE}

## What this is

We are making a companion to the Montpellier archive of Alexander Grothendieck's manuscripts: his text, made readable,
with headnotes, notes keyed to his lines and the status of every claim and question of his. A first run worked
through **cote {COTE}, scans {RANGE}** (run {S}A). It corrected the reading on the ink and settled from the literature
where each of his claims stands, and it listed the questions that are open as he left them and not found settled
since: `open_questions.md`, {NQ} questions.

This run attacks those questions. The aim is to settle each one: prove it, or refute it and prove the corrected
statement. His formulation and the formulation plausibly true today are both decided where they differ.

## The attachments

- `{S}A.zip`: run A's return. Read `open_questions.md` first, then for each question its claim in `claims.json`, its
  notes in `notes.json` and his pages in `pages/`: the corrected diplomatic transcription (macros: `\deleted{}`,
  `\inserted{}`, `\margin{}`, `\unsure{a|b}`). Also `references.bib`: the literature run A checked.
- `{S}_context.zip`: the subject's own context, the same as run A's. {CONTEXT_LIST}
- `{S}_results.zip`: `RESULTS_STATE.md`, the state of our own research on these subjects. **Leave it closed until
  every question has had a first attack in its own terms,** then open it and use what bears on them.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

The items are the questions of `open_questions.md`, each a row of the ledger. **The main question** is the one run A
ranks first, or, where it ranks none, the one whose answer bears most on his other questions here. For each item:
- (a) proved: the statement, in his formulation where it is true, with a complete proof, checked a second time
  independently;
- (b) refuted: a counterexample with every hypothesis checked, then the corrected statement (the version he most
  likely had in mind, and the strongest version that is true), with its complete proof.

Partly settled is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and
the smallest undecided instance are the state of an item you are still working on: record them as you go, then attack
the obstruction, starting from that instance.

**When the work is finished.** Only when every item is proved (a) or refuted (b). Keep working until then: do not stop
because the remaining items are hard, because a partial result looks presentable, or because much has already been
done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESULTS.md`
reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it
failed, and the next step you would take. Never present such a return as complete or as following an allowed
alternative: there is none.

## Rules

- **His formulation first.** Work in his notation and his terms first, and state today's form beside it. Keep apart
  what his pages say, what the literature proves, and what is ours. Ours is labelled as ours.
- **The literature.** A result you use from the literature is cited by exact locator (theorem and page) from a source
  you opened; never from memory without checking. If a question turns out to be settled in the literature after all,
  record where, with the exact statement, and check that it matches his question's quantifiers and hypotheses.
- **Proofs.** They are complete. Each is checked a second time, independently (re-derived, or a computation with other
  parameters), and the check is recorded.
- **One stream.** Do not split the work among parallel workers.

**Check events.** For every statement your work checks, uses or refutes (a question, by its id in `open_questions.md`;
a result of the literature, by its reference key; an entry of `RESULTS_STATE.md`, by its id), record its check events
in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check /
independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background
without fault found / refuted, with the refined statement's id), outcome. Give each event the type of what actually
happened, neither more nor less.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every hour of work, each under a new name, `{S}B_checkpoint_<NN>.zip` with `NN` counting up; never
overwrite, rename or delete an earlier checkpoint. Save checkpoints once an hour and at no other time: none after an
item or a proof. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the
work (`RESULTS.md`, the proofs, `PROGRESS_LEDGER.md`, `CHECK_EVENTS.tsv`, `progress.log`, the code), so that a new
session can continue from it and the attached files. Leave the attached files themselves out of it: we have them. It
is never a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the
current deliverables and documentation; earlier checkpoints are not copied into it. If the workspace comes back empty,
restore it from the newest checkpoint before you continue.

**If the execution environment disconnects.** Wait for it and retry for at least 10 minutes. If it does not come
back, the work must still reach us, so write it out in this chat as text: every file finished so far in full, each in
its own code block headed by its file name. Then go on directly in the chat, in the same form. Say at the start which
files are done and which are not. An answer that only reports the disconnection, describes the checkpoint or asks for
the files again, without writing out the work, is not acceptable.

## What to return

One zip file, `{S}B.zip`, offered as the only download, holding:
1. `RESULTS.md`: a table of every item (id, his formulation, today's formulation, outcome (a) or (b), where its proof
   is, the check), then each item in full: the statement, the proof or the counterexample with the corrected statement
   and its proof, the check;
2. the proofs as LaTeX (`proofs.tex`, one section per item);
3. `PROGRESS_LEDGER.md`;
4. `CHECK_EVENTS.tsv`;
5. `references.bib`, every work cited, with its `note` field;
6. `progress.log` (the time, UTC, at the start, at each review and at the end), and every program you ran, with its
   output.
