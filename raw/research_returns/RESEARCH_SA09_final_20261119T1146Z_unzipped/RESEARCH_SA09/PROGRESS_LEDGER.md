# RESEARCH_SA09 progress ledger

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). Run began
2026-11-19 11:03:18 UTC (12:03:18 Europe/Berlin). Initial gates were recorded
at the start; final mathematical review recorded at 11:45 UTC (12:45 Berlin).
Detailed actual checks and responsible runs are in CHECK_EVENTS.tsv.

| Item | Initial gate | Final state and strongest result |
|---|---|---|
| A.1 / L1 | Reconstruct all polynomial-category axioms beyond homogeneous composition | Settled. Identification refuted; all-module Hom-law proved; independence/countermodels; exact necessary-and-sufficient mixed coherence repair; scalar-weight criterion. A1.1–A1.9. |
| A.2 / L3 | Universal property and ring hypotheses | Settled. Nonnegative Frobenius claim false; all-ring matrix essential image; exact/admissible variants; PID and two-sided replacements. A2.1–A2.6. |
| A.3 / L2 | Additional structure and integral homotopy information | Settled. Full natural Gamma action constructed; multiplication recovered by cross effects; function ring reconstructed; opened Horel/Mandell/Toen comparisons derived; weaker readings refuted. A3.1–A3.5. |
| A.4 | Normalization ranks versus derived perfection | Settled. All-ring uniform rank criterion; regular/noetherian perfection comparison; original directions refuted; nonregular derived-fibre criterion. A4.1–A4.6. |
| B.1 | Pinning action and stabilizers | Settled. Orbit formula, equality criterion, torus certificate, complete connected kernel classification. B1.1–B1.3. |
| B.2 / L5 | Cubic, enumeration and moduli | Settled. All three functions/fields; raw quintic versus effective cubic; single S3 orbit; doubtful signs resolved algebraically. B2.1–B2.5. |
| B.3 | Classes I–III and cellwise stabilizers | Settled. Complete compact clean list, all oranges and positive-genus C2 family; explicit functions and isotopy distinction. B3.1–B3.4. |
| B.4 / L4 | Kummer congruences and every level | Settled. Literal rank-one L4 true; complete Fermat-fibre images/indices; independent-number-field-element scalar-affine openness. B4.1–B4.4. |

## Movement and repaired gates

The main-question review found a missing repeated-inner-degree step in the
first A1.7 proof. The final theorem uses whole-map normalization, including
off-diagonal vanishing; the proof groups equal inner degrees before applying
the exponential comparison. Two independent targeted reviewers accepted the
repair. No minimality assertion is needed. A1.8's abstract enrichment model
was separately checked in all zero, one, and positive index cases.

For A3 the decisive gate was to recover multiplication from the Gamma action
itself. Cross effects and bounded cofree tests close that gate. The lens-space
counterexample is explicitly not applied to the full action. For B4, the
cyclotomic radical intersection proves equality of the rank-one image beyond
the known square-root obstruction; a separate coordinate calculation gives
the full-fibre image and the correct ambient group.

The final coverage audit compared every task/lead with all sections and the
registry. It found and closed two metadata defects: B3.2 status alignment
and extra TSV fields. No mathematical gate remains open.

## Required reviews and checkpoints

The first three-hour review would be due about 14:03 UTC. All mathematical
rows were settled before it was due. No hourly no-movement review was needed;
the two-review stop rule was not invoked. Packaging is not counted as movement.

The first 45-minute checkpoint is due at 11:48:18 UTC (12:48:18 Berlin).
No checkpoint was created before that interval. The archive log records whether
the final package completed before that deadline or a scheduled checkpoint
was required. Earlier checkpoint ZIPs are never nested in archives.

## Final verification

All four exact certificates passed their integration rerun. The registry has
43 statements, 180 check events and 30 bibliography entries. The final 41-page
LuaLaTeX paper has zero overfull boxes, missing characters or undefined
references; rendered-page review is in qa/QA_REPORT.md. Unopened passages are
identified and are not proof dependencies. Source-specific R1/R5 assertions
not needed by the proofs are not silently marked checked.
