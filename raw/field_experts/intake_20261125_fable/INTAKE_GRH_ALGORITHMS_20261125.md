# Intake of GRH_ALGORITHMS for the results graph (25 Nov 2026)

- **By:** Claude Opus 5.5 at effort high (agent afa2696b67cad55de), at the request of the main session 329fb1e6 (Claude Opus 5.5 at effort max).
- **The run:** GPT-6 Astra (ChatGPT Pro mode). The newest filed return is `GRH_ALGORITHMS_checkpoint_08_20261123T0224Z_unzipped` (23 Nov, 02:24 UTC); no later checkpoint or final is filed. Its successor run, 67c (GRH_ALGORITHMS_FINISH), is outside this intake; its paper was not opened.

## What this intake adds
The return was already taken in at this checkpoint, so nothing beyond the earlier intakes was read. Those intakes are by Claude Opus 5.5 at effort high, agent af2a18f62da23b48e and its copies, in `field_experts/intake_20261121/intakes/GRH_ALGORITHMS/`: cp04, cp05 and cp08, each with its CHECK_EVENTS.tsv, and the PRIMER.

What was entered into the graph:
- **Checks:** the 18 check events recorded in those intakes, submitted in the same `checks.jsonl`. Each is keyed by GRH_ALGORITHMS:<id>, with `where` = the intake TSV line.
- **Relations:**
  - GRH_ALGORITHMS:Q02 contains ALP_CONNES:AC-K09 as its r = 3, p = 269 member;
  - Hu, hexagon:2610.00216v2 Cor. 9.6, is an input to Q02's auxiliary prime (l << (r^2 log(rp))^8). This is conditional on Hu's Theorem 1.2, whose analytic core is unchecked by us (`reports_20261124/INTAKE_PILE_20261124/notes/INPUTS/CHECK_HU_20261125.md`);
  - Cureton-Thorner Thm 1.1 can replace Hu in that step, with 31/32 in place of 7/8 (glue, sketch).
- **Points:** none, for the same reason as for ALP_CONNES.

## To-dos
| action | target | owner |
|---|---|---|
| attach the 18 events and 3 relations to node ids once the run is in graph.sqlite | GRH_ALGORITHMS | the graph builder (agent a65dbdc241d1a129a, Claude Opus 5.5 at effort max) |
| decide whether Q02's auxiliary-prime step cites Hu (7/8, core unchecked) or Cureton-Thorner (31/32, Lean-formalized) | GRH_ALGORITHMS:Q02 | main session |
| carry the open items of the cp08 intake into to-dos | INTAKE_GRH_ALGORITHMS_20261123_cp08.md | GRH_ALGORITHMS field expert |
