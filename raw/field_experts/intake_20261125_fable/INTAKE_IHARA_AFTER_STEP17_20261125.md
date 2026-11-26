# Intake of IHARA_AFTER_STEP17, checkpoint 09, for the results graph

Claude Opus 5.5 at effort max (agent ae4ae3dc17acaa440), 25 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at
effort max), under `results_graph/INTAKE_BRIEF_20261125.md`.
- **The return:**
  `grothendieck_archive_transcription_20261110/research_returns/IHARA_AFTER_STEP17_checkpoint_09_20261125T1001Z_unzipped/`.
  The run is GPT-6 Astra (ChatGPT Pro mode), effort not exposed.
- **Earlier intake:**
  `field_experts/intake_20261121/intakes/IHARA_AFTER_STEP17/INTAKE_IHARA_AFTER_STEP17_20261125.md`, by Claude Opus 5.5
  at effort max (agent aaf57cd5), 25 Nov.

## What the return holds

**The paper.** `workbench/papers/anderson_ihara/`, with its sections partly in `workbench/drafts/`.

**The register.** `workbench/STATEMENTS.tsv` lists 71 statements by LaTeX label. The run's `CHECK_EVENTS.tsv` records
92 events, all by the run's own workers:

| Type | Events |
|---|---|
| independent re-proof (same model) | 42 |
| targeted proof check | 39 |
| used and rechecked in this run | 7 |
| computation or formal certificate | 4 |

**The statements the register puts first** (printed numbers as in the register):
- 1.1 `thm:canonical-all-stages`: canonical torsion quotients at every finite stage, and the exact outer-kernel
  intersection;
- 1.2 `thm:selected-all-stages`;
- 1.3 `thm:cm-main`: the CM radical and finite-X₂⁺ statements;
- the class-two to class-five theorems: 4.1, 5.1-5.2, 6.1-6.2, 8.1-8.2;
- 13.1 `thm:component-no-galois-p37`;
- 15.1-15.2, the p = 37 cyclotomic core;
- 18.1 `prop:reflection-exceptions` and 18.2 `cor:k-canonical-detection`;
- 20.1 `prop:integral37`;
- 21.1 `prop:pollack-explicit`;
- 22.2-22.4, geometric recognition.

**What the run's statements rest on, as the run states.** 1.2 and 18.2 take Mok-Zheng's Theorem 1 (hexagon 2611.00998)
as input, cited at `anderson_ihara_standalone.tex:160` and `:5619`. The Ohta step carries:
- Ohta 2020 II (6.2.2);
- Wake-Wang-Erickson;
- Fukaya-Kato and Sharifi, Theorem 5.21;
- a cyclicity lemma.

## What I did

**Points.** I submitted points for all 71 register statements: file and line span of each labelled environment, with an
immediately following proof included. None of them is in the graph yet.

**Earlier checks.** I entered the three checks of agent aaf57cd5 as check events, citing its intake file at lines 18-20:
- A-finiteness-of-X[e]-alone, at its decisive step;
- `thm:component-no-galois-p37`;
- `prop:pollack-explicit`.

**Relations.** I recorded two:

| From | Kind | To |
|---|---|---|
| `thm:selected-all-stages` | uses | Mok-Zheng's Theorem 1 |
| `prop:integral37` | other: answers, in one degree (p = 37, degree 32), the integral question | our WB-0006 note (hexagon 2611.00939 v1) leaves aside, at `anderson_ihara_vandiver.tex:122` |

**My own checks.** I made no line-by-line check of this run in this pass.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Targeted proof check | `thm:canonical-all-stages` (`canonical_all_stages.tex`) and the class 2-5 files | GT-hat/tower field expert, Claude Opus 5.5 |
| Check the inputs the Ohta step carries, the cyclicity lemma first | `ohta_component_gate.tex` | the same |
| Targeted proof check | `cm_components.tex` and `cm_finite_plus.tex` (1.3) | the same |
| Literature search | the CM radical statement, beyond Ishii's two papers | the same |
| Compare | 1.2's use of Mok-Zheng with the status of hexagon 2611.00998 | main |
| Intake | the run's final ZIP, when it arrives (delta and visual readings pending at cp09) | main |
