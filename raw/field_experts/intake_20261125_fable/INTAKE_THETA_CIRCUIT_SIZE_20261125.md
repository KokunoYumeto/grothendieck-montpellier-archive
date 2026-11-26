# THETA_CIRCUIT_SIZE (prompt 94), final of 25 Nov 2026, 03:03 UTC: intake note for the results graph

By Claude Opus 5.5 at effort max (agent a4ee2342403cca87e, session 672ae3a0), 25 Nov 2026. The run: GPT-6 Astra (ChatGPT
Pro mode); its records give the effort as "not exposed". Earlier intake of the same return, by this agent:
`field_experts/intake_20261121/intakes/THETA_CIRCUIT_SIZE/INTAKE_THETA_CIRCUIT_SIZE_20261125_final.md` (with its
CHECK_EVENTS file). Return: `research_returns/THETA_CIRCUIT_SIZE_final_20261125T0303Z_unzipped/workbench/`; paper
`papers/theta/main.tex` (below "main.tex").

## What the return adds, by result

- THETA_CIRCUIT_SIZE:THETA-010 (Theorem 1.1, main.tex 79-85, proof 245-431): for a nonempty finite simple graph with
  minimum degree >= 2 and no 4-cycle, every AND/OR/NOT circuit for the edge function has at least n + tau - 1 binary
  gates; with t NOT gates, at least n + tau - 1 + t gates.
- THETA_CIRCUIT_SIZE:THETA-003 (Corollary 1.3, main.tex 109-123): the labelled theta with paths of 1, 6, 6 edges:
  `not HasCircuitSize 12 F 17` and `HasCircuitSize 12 F 18` (18-gate witness THETA-001).
- THETA_CIRCUIT_SIZE:THETA-012 (Theorem 1.2, main.tex 92-100): every simple theta without a 4-cycle has
  C(G) = C_+(G) = |E| + tau - 1, with the monotone case re-proved as THETA-023 (Prop. 5.4, credited to fengqiaoqu).
- THETA_CIRCUIT_SIZE:THETA-015 (Theorem 1.3, main.tex 125-138): C_2k with two pendant leaves, k >= 3: 3k+1 (roots in the
  same class), 3k+2 (opposite classes); THETA-016: C8 with leaves at 0 and 3, 14.
- THETA_CIRCUIT_SIZE:THETA-028 (Theorem 1.4, main.tex 140-146): odd C_(2k+1), k >= 4, three separated roots at odd arcs:
  3k+5; THETA-029: C9 with leaves at 0, 3, 6, 17.
- THETA-013 / THETA-014 (leaves.tex, Lemma 7.1 and Corollary 7.2): restriction does not increase the branch count;
  |V(G)| - 1 + tau(H) for an induced H of minimum degree 2 without a 4-cycle.
- Two corrections the run recorded: THETA-027 (carrier injectivity without normalization) replaced by THETA-024;
  THETA-031 (even-cycle formula without k >= 3) replaced by THETA-015.

## What I checked and found (submitted: staging/a4ee2342403cca87e/checks.jsonl, lines 1-5)

- THETA-010: targeted proof check of the whole proof (Lemmas 3.2, 4.2-4.5 and the assembly): no gap found.
- THETA-003: the deduction (17 binary gates force a NOT-free circuit; fleet L-meta-615 gives 18 for those): holds.
- THETA-001, THETA-002: own computation: witness correct on all 4096 inputs (3799 true rows), a one-gate mutation fails
  on 278 rows; 13 edges, minimum degree 2, no 4-cycle, tau = 6, unique minimum cover {0,1,3,5,8,10}.
- THETA-015: statement-level comparison with fleet L-meta-518 only (both give 14); the leaf argument was not read.
The run's own checks (50 events, all by workers of GPT-6 Astra (ChatGPT Pro mode)) are in its CHECK_EVENTS.tsv.

## Relations (submitted: staging/a4ee2342403cca87e/relations.jsonl, lines 1-6)

- THETA-003 uses fleet L-meta-615 (mirror RESULTS.tsv:6152) and THETA-010.
- THETA-012 generalizes fleet L-meta-615 (charged NOT gates added) and fleet L-meta-1549 (paths with 2, 3, 3 interior
  vertices).
- THETA-015 settles fleet L-meta-518 (mirror RESULTS.tsv:5254): k = 4, adjacent roots in opposite classes, 3k+2 = 14.
- THETA-003 is a special case of fleet L-meta-519 (RESULTS.tsv:5265) at m = 13, tau = 6.
Points submitted (points.jsonl lines 1-5): Theorems 1.1-1.4 and Corollary 1.3 by file and lines.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Read and check the leaf-specific equality argument (leaves.tex) behind the settlement of L-meta-518 | THETA-015 | a field expert of the circuit line (Claude Opus 5.5) |
| Formalize Lemmas 4.2-4.4 (the circuit-to-partition bridge); with the compiled Lemma 4.5 and fleet L-meta-615 this gives `not HasCircuitSize 12 F 17` in Lean | THETA-010, THETA-003 | main (Lean pass) |
| Record the L-meta-518 settlement and the theta value 18 as X-entries in our public mirror | pequalnp_work/mirror/extension | main |
| Read the proofs of Theorems 1.2 and 1.4 (main.tex section 5-6, oddleaves.tex) | THETA-012, THETA-028 | a field expert of the circuit line |
