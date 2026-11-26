# Sweep 1 over the register: where everything goes, and what does not fit (brief, 18 Nov 2026)

Written by the main session (Claude Opus 5.5 Max). Each sweep agent is Claude Opus 5.5 at effort max, with one scope
(a set of runs) given in its launch message. Name every model with its effort in what you write.

## Why
The user, 18 Nov 2026 (USER_INPUTS.md P6848): "do a light sweep, see where everything goes, do another light sweep, see
how everything interlinks, see if there are obvious inconsistencies ... just Bayesian refinement. And like layer per
layer ... Stack ... all the math that we have ... internal consistency checks, like making a sort of like the tags, see
what depends on what. Basically, just like go organize. And during that, you'll also find a whole bunch of corrections
and refinements. Make notes of those too." The structure it feeds is
`<local>/Documents\grothendieck_archive_montpellier\HANDBOOK_SKETCH_20261118.md`. Read its sections 2-5 first.

## What you have
`<local>/Documents\results_register\` (sweep 0, by script, no model):
- `REGISTER.tsv`: one row per statement, keyed by its draft tag RUN:ID (columns: run, line, id, status, statement,
  where_proved, depends_on, uses, lineage, his_places, check_events, check_docs, same_statement, notes, ret, results).
  Status is normalized (False is Refuted).
- `EDGES.tsv`: "uses" edges read from depends_on, and "names" edges where a row names another run's id.
- `FLAGS.tsv`: what the script saw:
  - a proved row that cites a refuted row. In the rows read so far, the proved row uses the refutation as a lemma, which
    is sound. Each needs a look all the same.
  - a dependency that names no id of its run;
  - a proved row with no check recorded in our files. Check events exist only since 17 Nov, so this is a gap in the
    records, not a sign of an unchecked claim.
- Each row's `ret` and `results` columns point to the run's newest return and its results table. The returns hold the
  proofs: papers, notes, checks.

Work by script over the TSVs; do not read REGISTER.tsv whole into your context. Read the returns where a question needs
them. No recursive search over big trees: name the folders you open.

## What to do, for the runs of your scope
1. **Placement.** Give every row a place in the sketch's outline (part, chapter, section), first by script (run,
   keywords), then by reading where it is unclear. Write `PLACEMENT.tsv`: tag, part, chapter, section, how placed
   (script / read), note.
2. **Lineage and merges.** The same mathematics appears in several runs: successor runs carry ids, and later runs
   restate, strengthen or correct. Write `MERGES.tsv`: canonical tag, member tag, relation (same / stronger / weaker /
   refines / corrects / refuted by), and a reason.
3. **The flags of your scope.**
   - For each proved row that cites a refuted row: does it use the refutation (sound), or the refuted claim as if true
     (an inconsistency)? Give the place.
   - For each dependency that names no id: what it points to (another run's id, a paper's label, the literature, or
     nothing).
   Write `FLAG_VERDICTS.tsv`: tag, flag, verdict, place, note.
4. **Consistency.** Watch, while you place, for:
   - two rows that contradict each other;
   - a proved row whose proof rests on an open row;
   - a status that does not match its proof;
   - the same object under two names or with two definitions.
   Read the proofs where it matters, and work the mathematics through as mathematics.
5. **Corrections and refinements.** `CORRECTIONS.md`: for each one, the row, what is wrong or can be sharpened, the fix,
   how sure you are, and what you read. Record each check you make in `CHECK_EVENTS.tsv`: statement tag, date, who
   (Claude Opus 5.5 at effort max, sweep 1, your scope), type (targeted proof check / independent re-proof /
   computation / used and rechecked / refuted, with the refined statement), outcome.
6. **`SUMMARY.md`.** It holds:
   - the counts;
   - the corrections that matter most;
   - per chapter, what is proved, what is open, and the strongest proved reduction of each open item;
   - which of your runs had not been taken in before (field_experts/INTAKE_LEDGER.md) and what you found in them.

Write all of it in `<local>/Documents\results_register\sweep1_<scope>\`.

## Rules
- Read `<local>/Documents\AGENTS_MATHEMATICS.md` before you judge any proof.
- Work the mathematics through, critically, as mathematics; do not presume it false (the user, 18 Nov: AI mathematics
  is not presumed bad; mathematicians check too).
- Read-only on the returns, the register and every file outside your folder.
- Cite known results by exact locator; do not re-prove them.
- Credit Michel Hua's project wherever a finding is his.
- Do not stop for context below your bound. If your context starts with a summary, you were compacted: reread this
  brief and your own files, then go on. Your final message to the main session: five lines at most, with your folder.
