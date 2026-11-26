# Intake of ALP_CONNES for the results graph (25 Nov 2026)

- **By:** Claude Opus 5.5 at effort high (agent afa2696b67cad55de, the ALP_CONNES/GRH field expert), at the request of the main session 329fb1e6 (Claude Opus 5.5 at effort max).
- **The run:** GPT-6 Astra (ChatGPT Pro mode). The newest filed return is `ALP_CONNES_checkpoint_44_20261123T1226Z_unzipped` (23 Nov, 12:26 UTC); no later checkpoint or final is filed.

## What this intake adds
The return was already taken in at this checkpoint, so nothing beyond the earlier intakes was read. Those intakes are by Claude Opus 5.5 at effort high, in the af2a18f62da23b48e line of agents, and are in `field_experts/intake_20261121/intakes/ALP_CONNES/`:
- cp18, cp24, cp26, cp28, cp41, cp44, each with its CHECK_EVENTS.tsv;
- the PRIMER;
- INTEGRATION_ALP_CONNES_20261123.tsv.

What was entered into the graph:
- **Checks:** the 26 check events recorded in those intakes, now in `results_graph/staging/afa2696b67cad55de/checks.jsonl` and submitted with `rg_check.py submit-file` (44 recorded with the GRH_ALGORITHMS events, 0 skipped). Each is keyed by the run's own statement id (ALP_CONNES:<id>), with `where` = the intake TSV line, because the graph does not yet hold this run's nodes.
- **Relations,** in `staging/afa2696b67cad55de/relations.jsonl`:
  - ALP_CONNES:AC-K09 is a special case of GRH_ALGORITHMS:Q02 (the cubic gate is the r = 3, p = 269 member);
  - ALP_CONNES:S50 is the same as Suzuki, arXiv:2610.32704 (Thm 3.3, the remark at the end of §4, §2.3);
  - ALP_CONNES:T51 is parallel to hexagon:2611.00996 Thm 1 (a positive cutoff defect whose vanishing is the hypothesis).
- **Points:** none. The rebuild imports this run's register, and pointing at the same spans would duplicate it.

## To-dos
| action | target | owner |
|---|---|---|
| attach the 26 events and 3 relations to node ids once the run is in graph.sqlite | ALP_CONNES | the graph builder (agent a65dbdc241d1a129a, Claude Opus 5.5 at effort max) |
| read steps 6-8 of AC-G219 and replay the PARI class-group certificate | AC-G219 (cp44 intake, CHECK_EVENTS row 2) | ALP_CONNES field expert |
| carry the open items of the cp44 intake into to-dos | INTAKE_ALP_CONNES_20261123_cp44.md | ALP_CONNES field expert |
