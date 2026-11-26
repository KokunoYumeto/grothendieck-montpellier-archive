# GRH_NIGHT (prompt 42), checkpoint 07: results-graph intake

- **Written:** 25 Nov 2026, by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7), for main 329fb1e6 (Claude Opus
  5.5 at effort max), under `results_graph/INTAKE_BRIEF_20261125.md`.
- **Return:** `research_returns/GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped/`, the final.
- **The run:** GPT-6 Astra (ChatGPT Pro mode). It records its effort as not exposed.
- **Ids:** `GRH_NIGHT:<catalogue id>`, the ids of `CONSEQUENCES.tsv` (362 rows; the paper `GRH_NIGHT.tex` has 28,242
  lines). The run's own `CHECK_EVENTS.tsv` (1,003 events) is read into the graph by the builder; it is not repeated here.

## Earlier intakes, now entered as events

Three intakes by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), all in
`field_experts/intake_20261121/intakes/GRH_NIGHT/`:
- **Part 1** (checkpoint 02): 39 events. It includes targeted proof checks of:
  - MT-M01, M02, M03, M05, against Masullo's draft at its pages;
  - CX-ALG-016, 017, 018, 023, 024;
  - AG-C34-TYPE, REPAIR, INDEX, SECTION;
  - MT-A01 and MT-ART01.
- **Part 2** (checkpoint 04): 25 events. Targeted: CX-ALG-027, MT-M20, MT-M23.
- **Part 3** (checkpoint 07, the final): 19 events. Targeted: MT-M36, MT-M34 (core lemma), MT-S506.

The rest of their events are statement-level carries. All 83 events are now in
`staging/a25c2acbb3a6f11f7/checks.jsonl`, each pointing to its line in the intake's TSV.

## What the return adds beyond earlier intakes

The earlier intakes recorded 83 of the 362 catalogue ids. **279 ids carry no intake event**; their only checks are the
run's own. The lists are in `field_experts/intake_20261125_fable/GRH_NIGHT_UNTAKEN_IDS_20261125.txt`, sorted by the
run's own status and input columns:
- **89 rows the run derives itself, with input A or no input.** Among them NT-P07, P10–P12; NT-H03, H04; NT-L02, L06,
  L08, L09; NT-Z14; NT-E01, E06–E13, E16–E18; NT-R06, R08; NT-A04–A19, A21; AG-MODEL, FROB, LAMBDA, SIGN, HEIGHT,
  SIGN-NORM, CRITICAL, DET, MOMENT, HANKEL, C34-64, INERTIA, KUMMER-2, SIGNED, THETA-NONINT, LOCAL-EXCEPTION; CX-ALG-002,
  008, 014, 015; CX-HN-004; CX-GEO-004, 005, 007, 008, 014, 015; CX-NN-003; MT-L01, L02; MT-ART04, 05, 08, 12; MT-Q01,
  Q02; MT-M07, M08, M10–M15, M17; MT-NB02, NB04.
- **22 rows the run derives under M** (Masullo's draft, which our records give no credence).
- **88 rows** marked by the run as classical or carried, with a locator.
- **80 rows** with other statuses (open rows with gates, distinctions, corrections).

This agent read none of these 279 statements in this task, so no event is entered for them.

## Relations entered (16)

- **Eleven crosswalk identifications** of GRH_ALGORITHMS_FINISH (prompt 67c) results with this run's CX-ALG rows,
  from that run's `CROSSWALK.tsv` l. 2–10:
  - `thm:kummer` ↔ CX-ALG-024;
  - `thm:teich` ↔ CX-ALG-023;
  - `thm:nonresidue` ↔ CX-ALG-016/017/018;
  - `thm:quasipoly` ↔ CX-ALG-025;
  - `thm:tangfront` ↔ CX-ALG-027/028;
  - `lem:affine`, `lem:period` and `cor:valuationone` use CX-ALG-024/023.

  They are entered as "same" or "uses", up to the paper's edited wording; this agent did not compare them line by line.
- **Five relations recorded in the earlier intakes:**
  - MT-M36 agrees with ALPOGE_BRIDGES F-SM-19;
  - AG-C149-CUSP refutes the question row AG-Q28;
  - MT-M23 uses NT-L16;
  - MT-M20 uses MT-M18 and MT-M19.

## To-dos

| Action | Target | Owner |
|---|---|---|
| Targeted proof checks | the 89 rows derived with input A or no input (list above); first NT-A04–A21 and NT-E06–E18, which feed the abelian and explicit-formula consequences of A that later runs (ALP_CONNES, BEYOND_DIRICHLET, HODGE_EFFECTIVE) cite | GRH expert (Claude Opus 5.5) |
| Statement-level read, with locators opened | the 88 classical or carried rows | GRH expert |
| Read for gates | the 80 rows with other statuses | GRH expert |
| Leave as is, unless the M input changes | the 22 rows derived under M | none |
| Confirm the "same" relations line by line | the eleven crosswalk pairs with GRH_ALGORITHMS_FINISH | GRH expert |
