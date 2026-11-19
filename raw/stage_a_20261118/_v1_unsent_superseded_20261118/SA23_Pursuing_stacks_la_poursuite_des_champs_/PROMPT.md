# Topic dossier SA23: Alexander Grothendieck's papers, Montpellier archive. Pursuing stacks (À la poursuite des champs). First episode : The Modelizing Story (Histoire de Modèles)

## What this is

The Montpellier archive (fonds Grothendieck, Université de Montpellier) holds about 16,000 scanned pages of his
manuscripts. AI models transcribed them folder by folder into diplomatic LaTeX: GPT-6 Astra in ChatGPT Pro mode and
GPT-6 Astra at reasoning effort max in Codex. Beside each Pro transcription, the run wrote research notes on the
pages: his conjectures, his unproved claims, the implications he did not pursue, the run's own ideas, and questions
about the reading. Over 105 runs these notes come to 13 MB. They have never been consolidated: each run wrote its
notes without seeing the others', so the same claim is noted several times, readings differ, and links between
folders were seen by no one.

This run consolidates the notes of one topic of the archive, **Pursuing stacks (À la poursuite des champs). First episode : The Modelizing Story (Histoire de Modèles)** (cotes 134-1, 134-2, 134-3, 134-4, 134-5, 134-6, 134-7, 134-8, 135), into one dossier. The
dossier becomes the foundation of the next work on these folders: the companion to each folder (his text, a
commentary, the status of each claim) and the research on his open questions. It is the step that should have come
before more notes were made.

**Read the topic in its own terms.** The notes were written with context packets that leaned toward two of our other
projects, La Longue Marche à travers la théorie de Galois and Les Dérivateurs, and toward our results on them, so
they partly see this topic through that lens. Work from his objects, his notation, his questions and the literature
of this subject. The links to those projects are kept, apart from the rest (Stage 5).



## The attachments

- `SA23_notes.zip`:
  - `NOTES_INDEX.tsv`: one row per note entry, with its stable id `<package>#<n>` (the n-th `###` entry of that
    package's notes file), its heading, its kind and the scans it cites. There are 509 entries from
    1 packages;
  - `pro/<package>_notes.md` and `pro/<package>_doubts.md`: the notes and the doubts tables of every package of the
    topic, as returned;
  - `second_pass/<package>/`: where Claude (Claude Opus 5.5 at effort max) has checked a package against the scans, its change
    logs (`*_changes.md`: the old reading, the new one, what the image shows) and its check of the notes
    (`*_notes_checked.md`). A changed reading there is the current reading;
  - `codex/<folder>_notes.md`: the short notes of the Codex transcriptions of the topic. They were written without
    any context and list the steps the pages themselves mark as unverified, with titles and page counts. They are
    leads, and they take no verdict rows.
- `SA23_texts.zip`:
  - `TOPIC.md`: the folders of the topic: cote, the catalogue's title, dates, pages, what is transcribed and by
    which model, what is not;
  - `pro/<package>_transcription.tex` and `codex/<folder>_transcription.tex`: the transcriptions the notes are about,
    one file per package or Codex folder, with `\scanpage{N}` at each scan page and the cote in `\cotefile{}`;
  - `PREAMBLE.tex`: the macros of the transcriptions (`\deleted{}`, `\inserted{}`, `\margin{}`, `\unsure{a|b}`,
    `\illegible{n}` and the others).

Unzip both in your sandbox. Work from the files with your tools (search, scripts, tables), and read the passages
themselves: an entry is checked against the page it is about, never against its own summary.

## Stage 1: every note entry, once

For every row of `NOTES_INDEX.tsv`, read the entry and the passage of the transcription it is about. Merge the
entries that are about the same thing (the same claim, object, question or reading) across packages into one item.
For each item:
- its id, `SA23-<n>`, and the ids of all its source entries;
- its kind: conjecture / unproved claim / unpursued implication / idea of the earlier run / reading question /
  self-flagged step (a step he marks as unverified) / withdrawn in the same text (he corrects or retracts it later,
  with both places) / title, date or page count / other;
- where it is: cote, scan, line;
- his words, quoted briefly from the transcription;
- the mathematics, stated precisely in today's terms, with all hypotheses, and what in that statement is your
  reconstruction rather than his text;
- the check against the text: whether the transcription says what the entries say (agrees / overstates /
  understates / misreads / not on the page), with the reason.

Every source entry gets a verdict: kept (as item n), merged into item n, corrected (how), withdrawn (why), or rests
on a misreading (then it also goes to Stage 4). No entry is left without a verdict.

## Stage 2: the claims map

Every claim of his in this topic that the notes or the transcriptions record: theorems, propositions, lemmas,
statements without proof, constructions said to work, computations. For each claim:
- where (cote, scan, line), his statement as he writes it, and today's statement;
- its status on the pages: proved there / proof sketched / stated without proof / corrected by himself later (both
  places) / false as stated (with the counterexample, every hypothesis checked) / open on the pages;
- every computation of his that the claim rests on, redone, with the code and its output;
- its fate in the literature: what became of it and when (the date of first circulation apart from the date of
  publication when they differ), found by searching: zbMATH Open, arXiv, MathOverflow, Numdam, EGA, SGA and his
  published papers, the collected works and bibliographies of the authors concerned. Follow references backwards
  from later papers when a title search finds nothing. The absence of a first hit is weak evidence, and a later paper
  on the same broad subject is weak evidence that the exact claim was settled: match the exact quantifiers and
  hypotheses;
- its class: **A** in his own later published work; **B** developed by others into established results; **C**
  partly developed (say exactly what remains open); **D** not developed (say what you searched); **E** known before
  him (standard at the time); **F** not identifiable from the pages;
- its present status, dated (as of November 2026), and your confidence (high, medium, low).

## Stage 3: his open steps and questions

The problem index of the topic: each open question, conjecture, hope or doubt of his ("?", "je conjecture", "il
serait intéressant de", "on devrait pouvoir", "à vérifier", a step left for later), merged across the folders. For
each problem:
- its id `MP-SA23-<nn>` and a short title;
- every place it occurs;
- the strongest formulation his text supports and, separately, the strongest formulation that is plausibly true
  today, with all hypotheses;
- the state of the art, with exact references and the exact results they prove;
- why it stayed open or was dropped, where the sources say;
- in one sentence, whether it is worth developing now, and why.

## Stage 4: readings to check on the scans

The places where the mathematics suggests that the transcription misreads the ink: an index that makes a formula
false, a struck word that the argument needs, a sign, a quantifier, a word that reverses the logic. For each: cote,
scan, line, the reading, the alternative the mathematics suggests, the evidence, and how much the mathematics depends
on it. This run has no scans, so none of these is decided here and no reading is changed: the next run on the folder
has the scans and decides each on the ink. The mathematics raises the alarm; the ink decides.

## Stage 5: links

- Across the folders of the archive: his own cross-references, and the links the notes find (cote and scan on both
  sides, and what the link is).
- To his published work: the passages of EGA, SGA, his papers, the Esquisse d'un programme or Récoltes et Semailles
  where the same object, claim or question appears, with exact locators.
- To our other projects (La Longue Marche, Les Dérivateurs, S6, the research runs the notes name): the links the
  notes make, each with its note ids and the run names it cites. These are leads from the earlier runs' context, not
  results, and they stay in their own table.

## Stage 6: research directions

The directions you find while consolidating: where each comes from (item, claim and problem ids), what it would
establish, what is known, and the first concrete step. Rank them by interest and by how far one research run of a
few hours could take them. Develop none of them here: each becomes its own task, and this list is what those tasks
are cut from.

## Rules

- Keep three things apart everywhere: what his pages show, what the sources say, and what you infer. Ideas of the
  earlier runs are labelled as theirs, and yours as yours.
- Every reference must be real and checked: give a link or DOI that you opened (`note = {verified}`); otherwise mark
  it `note = {unverified}`. Never cite from memory without checking. Quote sources briefly and cite them exactly.
- Never fill a gap in his text from what he "must have" meant; mark a reconstruction as yours.
- Cover every entry of `NOTES_INDEX.tsv` and every folder of `TOPIC.md`.
- Do not stop early and do not ask questions back: make the decisions a careful researcher would make, state them,
  and carry on to the end.
- Save your work to files as you go, stage by stage, so that nothing is lost if a later step is interrupted.

**Check events.** For every statement your work checks, uses or refutes (a claim of his, by its claim id; an item of
the notes, by its item id; a reference's result, by its key), record its check events in `CHECK_EVENTS.tsv`, one row
per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof /
computation or formal certificate / used and rechecked in this run / carried as background without fault found /
refuted, with the refined statement's id), outcome. Give each event the type of what actually happened, neither more
nor less: reading a statement in the notes is not a check of it.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every hour of work, each under a new name, `SA23_checkpoint_<NN>.zip` with `NN` counting up; never
overwrite, rename or delete an earlier checkpoint. Save checkpoints once an hour and at no other time: none after a
stage, a folder or a table. A checkpoint is one ZIP holding every deliverable written so far and everything that
documents the work (the tables, the dossier, `CHECK_EVENTS.tsv`, `progress.log`, the code), so that a new session can
continue from it and the attached files. Leave the attached files themselves out of it: we have them. It is never a
JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it. If the workspace comes back empty,
restore it from the newest checkpoint before you continue.

**If the execution environment disconnects.** Wait for it and retry for at least 10 minutes. If it does not come
back, the work must still reach us, so write it out in this chat as text: every file finished so far in full, each in
its own code block headed by its file name (the code you ran to save each file contains its text: take it from
there). Then go on with the remaining stages directly in the chat, in the same form. Say at the start which files are
done and which are not. An answer that only reports the disconnection, describes the checkpoint or asks for the
files again, without writing out the work, is not acceptable.

## What to return

One zip file, `SA23.zip`, offered as the only download, holding:
1. `SA23_dossier.md`: the dossier's overview, in English: what the folders hold; his lines of work in them, in his
   order and his terms; the main claims and questions; what the earlier notes got right and wrong; the state of the
   topic today. Then the counts: entries, items, verdicts by kind, claims by class and status, problems, readings to
   check, directions.
2. `SA23_entries.tsv`: `entry_id, item_id, verdict, reason`, one row for every row of `NOTES_INDEX.tsv`.
3. `SA23_items.json`: the items of Stage 1, as a list of objects with the fields `id, sources, kind, cote, scans,
   lines, his_words, statement, reconstruction, check, check_reason`.
4. `SA23_claims.json`: the claims of Stage 2, with the fields `id, items, cote, scans, lines, his_statement,
   statement, status_on_pages, computation, class, fate, fate_date, present_status, refs, confidence`.
5. `SA23_problems.json`: the problems of Stage 3, with the fields `id, title, occurrences, as_he_states,
   plausible_today, state_of_art, why_open, worth, refs`.
6. `SA23_readings.tsv`: Stage 4, `cote, scan, line, reading, alternative, evidence, weight, confidence`.
7. `SA23_links.tsv`: Stage 5, `kind, from, to, what, evidence, note_ids`, where `kind` is folder, published work or
   our projects.
8. `SA23_directions.md`: Stage 6, ranked.
9. `SA23_references.bib`: every work cited, with its `note` field.
10. `CHECK_EVENTS.tsv`, `progress.log` (the time, UTC, at the start, at each stage and at the end), and every
    program you ran, with its output.
