# VPVNP_HINGE (run 98) in the results graph, 25 Nov 2026

By Claude Opus 5.5 at effort max, agent a5ef71dd7993387cb, for main 329fb1e6 (Claude Opus 5.5 at effort max). The run is
GPT-6 Astra (ChatGPT Pro mode). It is read at its final checkpoint 12:
`grothendieck_archive_transcription_20261110/research_returns/VPVNP_HINGE_checkpoint_12_20261125T0459Z_unzipped`.

## Earlier records this note builds on

- **The intake:** `field_experts/intake_20261121/intakes/VPVNP_HINGE/INTAKE_VPVNP_HINGE_20261125_cp12.md`, with its check
  events beside it.
- **The gate-1 check:** `pequalnp_work/square_note/GATE1_CHECK_20261125.md`, with `CHECK_EVENTS_GATE1_20261125.tsv`. It
  was done by agent af3258db660f11e1f (Claude Opus 5.5 at effort max), a copy of a4348514ce0275bbf.
- **The connection map:** `reports_20261124/INTAKE_PILE_20261124/MAP_COMPLEXITY.md` (checkpoint 02 era).

This note adds no reading beyond those records. It writes them into the graph.

## What went into the graph

The staging folder is `results_graph/staging/a5ef71dd7993387cb/`.

**Points.** I pointed at 31 statement spans from run 98, each statement with its proof. `rg_admit.py` admitted all of them
(`data/staged_a5ef71dd7993387cb.jsonl`):
- in `price_geometry.tex`: PG-FOUR-CORE, PG-FOUR-CONDITIONAL, PG-SQUARE-GATE, PG-CROSSPOLY-GATE, PG-PENDANT, PG-TREE-ALL,
  PG-TREE-CONTRACTION, PG-OP-COMPLETE, PG-OP-DETERMINISTIC, PG-OP-SLICE-DETERMINANT, PG-CYCLE-GAP, PG-CYCLE-FINITE and
  PG-SLICE-CLIFFORD;
- in `shortening.tex`: SH-02 to SH-09, SH-38, SH-55d, SH-57 to SH-60 and SH-60b;
- in `root_route_audit.tex`: RT-W6-PARAM, RT-SOS and RT-FINITE.

**Checks.** These were submitted through `rg_check.py submit-file`.
- **From gate 1** (agent af3258db660f11e1f):
  - PG-CROSSPOLY-GATE, PG-FOUR-CORE, PG-SQUARE-GATE and PG-FOUR-CONDITIONAL;
  - SH-03 (covering SH-02 to SH-04), SH-05 (covering SH-05 and SH-06), SH-07 and SH-08;
  - all targeted proof checks.
  - What was found: no fault. For PG-CROSSPOLY-GATE and SH-08 the inputs are Anthropic's Thm A.6 and Prop C.3. For
    PG-FOUR-CONDITIONAL, PG-PENDANT's outside input (Wigderson–Zuiddam 2025, Thm 12.23) was not opened, and its
    hypothesis line names no inputs.
- **From the intake:**
  - SH-60b, a targeted check: the case partition is complete, and the dimension-one argument holds;
  - RT-W6-PARAM, a computation: every numeric inequality holds, while its geometric inputs were not checked;
  - PG-OP-DETERMINISTIC, a targeted check of the steps listed in its row.

**Relations:**
- SH-08 states the same theorem as run 99's thm:crosspolytope-shortening;
- PG-SQUARE-GATE states the same as 99's thm:tree-price-dichotomy;
- PG-CROSSPOLY-GATE states the same as 99's thm:cross-polytope-price-flat;
- the report's exponent row states the same as 99's thm:crossing-exponent-dichotomy;
- RT-SOS states the same as Liu hexagon:2611.00994, "Two crossing cuts";
- PG-SLICE-CLIFFORD runs parallel to Singh 2026.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Audit the exact certificate families behind SH-60b with independent code or another model: SH-28d, SH-38, SH-46, SH-53, SH-55b/d, SH-57 to SH-60 | VPVNP_HINGE:SH-60b | a fresh-context Opus agent with code |
| Check the geometric inputs of RT-W6-PARAM: the SH-23 condition, the path-length capacity bound, the sign-frame bound | VPVNP_HINGE:RT-W6-PARAM | same |
| Check rt:sos, pg:op-sos-duality, pg:op-signed and PG-OP-COMPLETE | VPVNP_HINGE:PG-OP-DETERMINISTIC | an Opus intake agent |
| Open Wigderson–Zuiddam 2025, Thm 12.23, at its statement | VPVNP_HINGE:PG-PENDANT | same |
| Read EX-47 and EX-48 and the remaining EX-29 to EX-43 rows | VPVNP_HINGE exponent_audit.tex | same |
| Carry SH-60b, the q = 128 system and the width-7 search into the successor prompt | 102_VPVNP_SQUARE | main |
