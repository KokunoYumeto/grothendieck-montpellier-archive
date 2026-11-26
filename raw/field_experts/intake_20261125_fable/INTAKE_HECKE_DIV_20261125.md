# HECKE_DIV (prompt 38), the final return: results-graph intake

- **Written:** 25 Nov 2026, by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), for main 329fb1e6 (Claude Opus
  5.5 at effort max), under `results_graph/INTAKE_BRIEF_20261125.md`.
- **Return:** `research_returns/HECKE_DIV_final_20261121T0204Z_unzipped/`, `HECKE_DIV.tex`. The run is GPT-6 Astra
  (ChatGPT Pro mode), with its effort not exposed; it ran 00:49–02:04 UTC on 21 Nov.
- **Ids:** `HECKE_DIV:<label>`. The paper labels its results by the register ids P0, R21–R24F, P1–P6, M1–M10b, MR,
  SQ1–SQ9, A1–A3.

## Earlier intakes, now entered as events

Two intakes by Claude Opus 5.5 at effort high (the HODGE_SIGN intake agent, launched by the main session), in
`field_experts/intake_20261121/intakes/HECKE_DIV/`:
- **checkpoint 01**: 23 rows;
- **the final**: 26 rows. The last row repeats the part-1 confirmations for P0, R21–R24C, A1 and A2 as unchanged in the
  final.

That is 58 events once the combined rows are split. Targeted proof checks: P0, R21, R22, R23, R24A, R24A-signed, R24B,
R24C, R24E, A1, A2, A3, P6, SQ9. Rechecked in use: R24D, R24F and the archive folio rule (G1). Statement-level carries:
P1–P5, P2b, M1–M10, SQ1–SQ8, S1–S3. The M rows are conditional on Markman arXiv 2502.03415v2; P4 and SQ1–SQ8 on Severn,
Hexagon 2610.00387v2.

## What the return adds beyond earlier intakes

One labelled result carries no intake event: **MR (Proposition MR1–MR3, input regularity and presentation)**.

**MR check record (this agent, 25 Nov 2026), a computation:**
- P_C(t) = 9t − 2: L·C = 9 and χ = deg + 1 − g = 9t − 2.
- P_Z = 13·P_C = 117t − 26.
- P_F(t) = (3t+1)³ − 13(9t+1) = 27t³ + 27t² − 108t − 12.
- The Gotzmann expansion of 9t − 2 has 9 linear terms summing to 9t − 27, plus 25 constants, so its number is 34. For
  117t − 26 the linear terms sum to 117t − 6669, with 6643 constants, so its number is 6760.
- 13·34 = 442, and 442 + 3 = 445.
- The presentation rank is P_F(445) = 2,384,568,978.

Every number agrees with the paper. Not checked: Sidman's product bound as applied, the local freeness of K, and the
449-regularity of i_*K.

Rows of the run's register without a paper label (R20, R24D, M5, M6, S1–S3) keep the intakes' events under their
register ids.

## Relations entered (13)

- SQ9 uses SQ1–SQ8 and R21.
- P4 uses R21.
- R24F uses P2b.
- R24D and R24F each agree with HODGE_SIGN SG-04, as recorded by the earlier intakes.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Targeted proof check | MR: the Sidman step and the locally free kernel | HODGE expert (Claude Opus 5.5) |
| Targeted proof checks | the M-series (conditional on Markman) and SQ1–SQ8 (conditional on Severn), if the Hodge line is published | HODGE expert |
| Link | R24A-signed and R24C to Grothendieck's Hodge sketch 2.4 (archive, 16_scan044), which they correct, once the archive node exists | graph owner |
