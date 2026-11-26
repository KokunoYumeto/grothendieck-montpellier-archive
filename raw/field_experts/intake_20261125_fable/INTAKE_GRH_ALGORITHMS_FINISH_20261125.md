# GRH_ALGORITHMS_FINISH (prompt 67c), checkpoint 07: results-graph intake

- **Written:** 25 Nov 2026, by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), for main 329fb1e6 (Claude Opus
  5.5 at effort max), under `results_graph/INTAKE_BRIEF_20261125.md`.
- **Return:** `research_returns/GRH_ALGORITHMS_FINISH_checkpoint_07_20261123T2059Z_unzipped/`, the newest. The run is
  GPT-6 Astra (ChatGPT Pro mode). The edition of 24 Nov is by GPT-6.2 Astra at reasoning effort ultra (Codex).
- **Ids:** `GRH_ALGORITHMS_FINISH:<paper label>`. The paper is `workbench/work/unfiled/v1/papers/grh_algorithms.tex`;
  `CROSSWALK.tsv` maps the register ids GRH-P### to the labels.

## What the return adds beyond earlier intakes

Nothing. Checkpoint 07 is the newest, and two earlier intakes by this agent took it in:
- `field_experts/intake_20261121/intakes/GRH_ALGORITHMS_FINISH/INTAKE_GRH_ALGORITHMS_FINISH_20261123_cp04.md` (P144,
  P145);
- `.../INTAKE_GRH_ALGORITHMS_FINISH_20261124_cp07.md` (Codex's five fixes, P150, P161).

Their events are now entered in the graph (`staging/a25c2acbb3a6f11f7/checks.jsonl`, 10 events).

## Results of the finishing part (P144–P164), with their check events

| Register id | Label (graph id suffix) | Events |
|---|---|---|
| P144 | thm:threshold-cyclotomic-cofactor (l. 138) | targeted proof check by this agent (cp04 intake); in-run statement-only re-proof (CROSSWALK l. 145) |
| P145 | thm:selected-cyclotomic-cofactor (l. 1232) | targeted proof check by this agent (cp04); in-run re-proof (CROSSWALK l. 146) |
| P146 | cor:fixed-set-cubic-cofactor | in-run re-proof only (CROSSWALK l. 147) |
| P147–P148 | prop:quantitative-real-residue, lem:cyclotomic-primary-quotient | in-run independent reports only (CROSSWALK l. 148–149) |
| P149 | thm:bounded-congruence-cofactor (l. 188) | the sign step only, targeted by this agent (cp07); in-run reports. It uses A (Alpöge) for fixed r and t |
| P150 | prop:genus-two-trace-collision (l. 10812) | computation by this agent (cp07): the point counts agree |
| P151–P155 | the cyclic-period, lift and obstruction statements | in-run independent reports only (CROSSWALK l. 152–156) |
| P156 | prop:small-frobenius-quotient (l. 15126) | wording edit carried by this agent; in-run report |
| P157–P159 | prop:tal-trace-local-units, prop:ideal-profile-residue, prop:fixed-shift-maximal-cyclotomic | in-run reports only |
| P160 | prop:genus-two-quotient-twist (l. 10969) | computation by this agent: a third quotient at t = 0; the edition text was changed |
| P161 | prop:genus-two-chebyshev-comparison (l. 11110) | computation by this agent: counts agree |
| P162 | prop:restricted-reflex-ideal-constructions | in-run integration fragment only |
| P163 | rem:literal-prime-power-loop (l. 4847) | computation and targeted check of the repair by this agent |
| P164 | rem:frobenius-ideal-equal-degree (l. 13404) | targeted check by this agent after the edition change |

## Relations entered (`staging/a25c2acbb3a6f11f7/relations.jsonl`)

- P144 is a special case of P145 (S = ∅).
- P145 generalizes P128 (`thm:small-cyclotomic-cofactor`), and through it P129 and P131; this is the crosswalk's
  "Extends".
- The HNAM note (hexagon:2611.01018 v2 draft, Theorem A, l. 86) sharpens `prop:fixed-strip-hn-am` (l. 4641, Prop. 17.2
  of hexagon:2611.00987) with an explicit threshold x₀.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Targeted proof check | P147–P149 whole (the quantitative chain under A) | GRH expert (Claude Opus 5.5) |
| Targeted proof check | P151–P155 (cyclic periods and lifts) | GRH expert |
| Targeted proof check | P146, P157–P159, P162 | GRH expert |
| Enter the relation | P149 uses A: link to the Alpöge node when the graph has one | graph owner |
