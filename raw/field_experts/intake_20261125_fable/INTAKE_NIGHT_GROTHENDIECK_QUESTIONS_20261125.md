# Intake of NIGHT_GROTHENDIECK_QUESTIONS, checkpoint 13, for the results graph

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 25 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at
effort max), under `results_graph/INTAKE_BRIEF_20261125.md`.

The return is
`grothendieck_archive_transcription_20261110/research_returns/NIGHT_GROTHENDIECK_QUESTIONS_checkpoint_13_20261124T0037Z_unzipped/`.
The run is prompt 76, GPT-6 Astra (ChatGPT Pro mode), effort not exposed.

**Earlier intakes, all in `field_experts/intake_20261121/intakes/NIGHT_GROTHENDIECK_QUESTIONS/`.**
- Checkpoint 04, parts A, B and C (23 Nov).
- Checkpoint 13, part A (24 Nov), by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc). It records the following:
  - Between checkpoints 04 and 13 only `papers/A133_lattices` changed.
  - The run's parts B and C had not started by checkpoint 13 (LEDGER l.333-334).
  - It read Theorem 26.1 with its proof, and the statements of Theorem 27.1, Corollary 27.3 and part of Theorem 18.1.

## What the return holds

| Paper | Register | Statements |
|---|---|---|
| `papers/A133_lattices/` | `STATEMENTS.tsv` | 59 |
| `papers/A123_tori/` | `records/A123_tori/STATEMENTS.tsv` | 11 |
| `papers/A15_finite_fields/` | `records/A15_finite_fields/STATEMENTS.tsv` | 12 |

## What I did

**Points.** I submitted 78 points: each register statement located by its printed number (theorem counters recomputed
from each paper's `main.tex` and its inputs) at its file and line span.

| Paper | Located | Not located |
|---|---|---|
| A133 | 56 | NGQ-A133-002 and -009 (they cite whole sections); NGQ-A133-024 (Theorem 16.2, not found under that number) |
| A123 | 10 | 1 |
| A15 | 12 | none |

I spot-checked the location of Theorem 26.1 against the earlier intake: `singular_distinguished_monic.tex:14-44`.

**Earlier checks.** I entered the 28 checks recorded by the four earlier intakes as check events, each citing its TSV
file and line.

**Relations and my own checks.** I added no relations, and made no check of my own in this pass.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Place the three unlocated statements by hand (two section-level, one number mismatch) | NGQ-A133-002, -009, -024 | main or the A133 field expert |
| Targeted proof check of what checkpoint 13 added beyond Theorem 26.1 | Theorems 27.1 and 28.2, Corollary 27.3, the all-truncations section | a field expert for lattices over regular local rings (not the GT-hat/tower expert) |
| Intake of later checkpoints, when parts B and C run | the run's next return | main |
