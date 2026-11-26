# VPVNP_WIRE_GEOMETRY (run 99) in the results graph, 25 Nov 2026

By Claude Opus 5.5 at effort max, agent a5ef71dd7993387cb, for main 329fb1e6 (Claude Opus 5.5 at effort max). The run is
GPT-6 Astra (ChatGPT Pro mode). It is read at its final checkpoint 09:
`grothendieck_archive_transcription_20261110/research_returns/VPVNP_WIRE_GEOMETRY_checkpoint_09_20261125T0432Z_unzipped`.
The paper is `workbench/papers/wire_geometry/`.

## Earlier records this note builds on

- **The intake:** `field_experts/intake_20261121/intakes/VPVNP_WIRE_GEOMETRY/INTAKE_VPVNP_WIRE_GEOMETRY_20261125_cp09.md`,
  with its check events.
- **The gate-1 check:** `pequalnp_work/square_note/GATE1_CHECK_20261125.md`, by agent af3258db660f11e1f (Claude Opus 5.5
  at effort max).

No reading beyond those records.

## What went into the graph

The staging folder is `results_graph/staging/a5ef71dd7993387cb/`.

**Points.** 17 statement spans, all admitted:
- in `planar.tex`: lem:rectangle, cor:planarobstruction, lem:cross-polytope-flat and thm:cross-polytope-price-flat;
- in `shortening.tex`: lem:terminal-selector, thm:shortening-nonflat, thm:square-shortening-equivalence and
  thm:crosspolytope-shortening;
- in `crossing_exponent_gap.tex`: thm:crossing-exponent-dichotomy and cor:hurwitz-exponent-dichotomy;
- in `cycle_search.tex`: lem:pt-upper, thm:square-pt-exponent and cor:square-hurwitz;
- in `tree_prices.tex`: thm:tree-price-dichotomy;
- in `weight_block_gate.tex`: prop:weight-block-gate and cor:weight-block-square-gate;
- in `duality.tex`: thm:coverduality.

**Checks.**
- **From gate 1**, all targeted proof checks, all with no fault found:
  - lem:rectangle (covering the planar section);
  - thm:square-shortening-equivalence;
  - thm:crosspolytope-shortening (register row Q3b);
  - thm:tree-price-dichotomy;
  - thm:square-pt-exponent;
  - lem:pt-upper (its lower bound);
  - thm:crossing-exponent-dichotomy;
  - cor:square-hurwitz.
- **What else gate 1 found:** three statements name only Prop C.3, but their proofs also use cover duality (Anthropic
  Thm A.6): the Q3b register row, the header of thm:square-pt-exponent, and cor:square-hurwitz.
- **From the intake:**
  - prop:weight-block-gate: an independent re-proof, no fault;
  - cor:weight-block-square-gate: a targeted check, no fault.

**Relations.** Four relations with run 98, all of kind "same":
- thm:crosspolytope-shortening and SH-08;
- thm:tree-price-dichotomy and PG-SQUARE-GATE;
- thm:cross-polytope-price-flat and PG-CROSSPOLY-GATE;
- thm:crossing-exponent-dichotomy and run 98's exponent row.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Correct the hypothesis lines to name both Thm A.6 and Prop C.3 | register row Q3b; thm:square-pt-exponent; cor:square-hurwitz | main, as a correction to report to the run's record |
| Check the upper bound q^{√2+o(1)} (Anthropic Prop. B.2 and Khoruzhii's counting) | VPVNP_WIRE_GEOMETRY:lem:pt-upper | an Opus intake agent |
| Check prop:optimal-crossing-hubs, that F(β) < 4 for β < √2 | VPVNP_WIRE_GEOMETRY shortening.tex | same |
| Read centralizer_gates.tex (the SL₂ centralizer restriction) and the rows Q4f, Q4g, Q6f and Q7d | VPVNP_WIRE_GEOMETRY | same |
| Settle which normalization the tree-family gap uses: 1 − 1/√2 (Q1d-7) or (√2 − 1)/2 (Q2c) | VPVNP_WIRE_GEOMETRY QUESTIONS.tsv | same |
| Carry the exponent gap, with its carried inputs, into the successor prompt | 102_VPVNP_SQUARE | main |
