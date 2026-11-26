# Intake wave of 23 Nov 2026, evening: the brief

Written by the main session 329fb1e6 (Claude Opus 5.5 at effort max), 23 Nov 2026 ~18:0x UTC, at the user's word
(USER_INPUTS P9556, P9576-P9579): "a wave of genuine intake of the mathematics"; "did we do reading the intake for
stuff and updating the existing stuff in the way that we were thinking about?"; "the intake stuff also feeds to [the
P vs NP fleet]". This file adds to `INTAKE_BRIEF_20261121.md` (same folder), which still holds for everything not
changed here: read it again first.

The Riemann hypothesis is proved for every Dirichlet L-function, zeta included (L. Alpöge, 20 Nov 2026,
https://alpo.ge/remark.pdf, formalized in Lean). Cite it as a theorem.

## Your task
Take in your run from your last intake to the newest checkpoint present when you start, as a diff: what is new, what
changed status, what was withdrawn or refuted, and what moved on the main questions. The assignment table is at the
end. If a newer checkpoint lands while you work (the filer runs often), take it in too before you finish.

## How to read
- **Work through the mathematics.** Read each new main result with its proof, follow every step, recompute what can be
  recomputed, and open a cited source at its locator when a step rests on it.
- **Status comes only from what you did in this task:** a proof check you carried out, a computation you ran, a
  source you opened at an exact locator. Never label a statement proved, conjectural, true or false from what you
  remember: this mathematics postdates every model's training (Alpöge's proof, the November runs, our own results of
  the last days). A negative is a precise obstruction you proved to one formulation, followed by the next formulation.
- **Usefulness first.** For each new result say first what it is good for: which open question of ours or of the
  literature it moves, and which reader would want it.

## What to deliver (in `intakes/<RUN>/`)
1. `INTAKE_<RUN>_20261123_cpNN.md` (NN = the newest checkpoint you read), with the sections of
   `INTAKE_BRIEF_20261121.md` (0 scope, verdicts, what is new, scope of the inputs, integration, prompt updates,
   Hexagon readiness), plus:
   - **Board candidates:** every new result that adds something, as a row ready for
     `field_experts/hexagon/HEXAGON_BOARD.tsv` (title, statement, what it adds, the gate left).
   - **For the P vs NP fleet:** for each new result that bears on complexity (GCT, level spaces, circuits, counting,
     sparse polynomials, finite geometry, anything mappable), the map onto the fleet's proof graph
     (`<local>/pequalnp_work/fleet_map/PROOF_GRAPH.tsv`; maps in `fleet_map/maps/`): the node ids, the
     translation, and the work that would complete the bridge. Construct the map; do not grade it.
2. `INTAKE_<RUN>_20261123_cpNN_CHECK_EVENTS.tsv`: one row per check event (statement id, date, who: model, effort,
   agent id; type; outcome), in the types of the check rubric.
3. **The integration, applied this time.** The intakes of 22-23 Nov listed edits to our existing files that were never
   applied. For your run (this wave's findings and, where your own earlier intakes of this run listed edits that are
   still unapplied, those too):
   - edit our own notes where the finding belongs: the study notes in `results_register/`, our draft notes and
     reports in `reports_2026112*/`, `claude_math_notes/`. Before each edit, copy the file once to
     `field_experts/intake_20261121/integration_backups/20261123/<RUN>/`;
   - log every edit as a row of `INTEGRATION_<RUN>_20261123.tsv` (file, place, old_text_short, new_text_short,
     source intake and finding, state: applied / for the main session);
   - do not edit the shared registers: the Hexagon board, the prompts in `TO_SEND`, anything under
     `<local>/pequalnp_work/`, the returns themselves. List those edits in the intake with the state "for the
     main session".
4. `PRIMER_<RUN>_20261123.md`: the mathematics of the run as it stands now, written for the main session to read after
   a compaction so that it knows the mathematics before any discussion. For each main result: the statement in standard
   terms, the lemmas it uses, and the proof in outline (the mechanism, step by step), with locators (file and statement
   id). Then the open rows with their current gate. Restate faithfully; no new development here and no labels beyond
   the check events you recorded. Use the length the mathematics needs.

## Rules
- No sub-agents. Name every model with its effort. No git. Never Grep or Glob over the whole of
  `<local>/Documents`; name the folder.
- Leave unopened: prompt 74 and the SAT_KRONECKER_FINITE_FIELDS and SAT_WITNESS_EXTRACTION files (Codex's), the
  S6_SERIES_PUBLISH returns (session 5c7e951b's). If a safety notice stops you on a paper, drop that paper and move on.
- Write only in your intake folder, the backup folder, the files of our own notes you edit as above, and your work
  file.

## Final reply (under 300 words)
Per run: the checkpoints read; the findings read in full and at statement level; the verdict counts; the main new
results with their usefulness; the edits applied (count and files); the board candidates; the fleet maps; the paths.

## Assignments

| Run | From (last intake) | To (newest filed) | Expert |
|---|---|---|---|
| ALP_CONNES | cp41 | cp44 or newer | copy of af2a18f6 cut at 13:34 UTC (after 62/69/67c) |
| ZETA_HEAT (prompt 62, first return) | none | cp01 or newer | same copy |
| GRH_ALGORITHMS_FINISH (prompt 67c) | GRH_ALGORITHMS cp08 | cp04 or newer | second copy of af2a18f6 at the same cut |
| ALP_MACHINE | cp48 | cp55 or newer | abcaba9b |
| HODGE_FINISH | none (prompt 70c, built on 70 and 70b) | final | copy of abcaba9b |
| NIGHT_AFTER_ALPOGE | cp11 | cp13 or newer | ad855737 |
| POLISH_ALGEBRAIC_GEOMETRY | cp12 | cp20 or newer | a018e2d2 |
| POLISH_TOPOLOGY_PERIODS | cp12 | cp13 or newer | a9e9559d |
| POLISH_CRISTAUX | cp12 | cp18 or newer | copy of ac8bd2a2 cut after its RESEARCH_SA17 intake (it reads its own cp12 intake first) |

Returns: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\<RUN>_checkpoint_NN_..._unzipped`
(and `<RUN>_final_..._unzipped`). Prompts as sent: `TO_SEND\PRO\1_Archive_research_by_topic\SENT\<NN>_<name>\PROMPT.md`.
