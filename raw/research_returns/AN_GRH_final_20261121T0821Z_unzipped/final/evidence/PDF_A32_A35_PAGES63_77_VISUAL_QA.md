# Independent visual QA: frozen A01–A35 build, pages 63–77

Date: 2026-11-21, completed 04:10 UTC. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Scope and result

**PASS — no clipping, overlap, missing glyphs, equation-tag collisions, or table-layout defects observed in the requested range.** This is a visual layout review, not an additional mathematical proof check.

The reviewer opened and inspected every full-size rendered PNG from `page-063.png` through `page-077.png` in `work/effective_galois/tex_build/a01_a35/qa/`. These are pages 63–77 of the 102-page frozen PDF, covering A32–A35 and the adjacent section boundaries. Each page was inspected at the supplied render size. No final source, build file, or rendered image was edited.

Frozen PDF: `work/effective_galois/tex_build/a01_a35/AN_GRH.pdf`.

PDF SHA256 (recomputed locally): `4d7f909477553080831e2df00e0a427803f67311e8886b8a078b7436f1d913ad`.

Frozen source SHA256 (recomputed locally): `28f6eea75623e702cc9b3a76edab3334cdcea1356a6a0ec814c3ad9415f34ec7`.

## Page-by-page observations

| Page | Material inspected | Layout result |
| --- | --- | --- |
| 63 | End of A31; A32 opening and OR.1–OR.3 | Section boundary, statement, and displays fit cleanly. |
| 64 | A32 finite-field model and divisor data; occupancy table OR.9; interpolation OR.11 | All thirteen occupancy columns are legible and within margins; no formula/tag collision. |
| 65 | A32 reduction, pointed character factors, and scalar calculation; OR.12–OR.17 | Long norm-reduction and product formulas remain clear; no clipping or overlap. |
| 66 | A32 comparison and constant-extension argument; A33 opening and DR.1 | End-of-proof symbol, section boundary, and multiline assumption are clear. |
| 67 | A33 statement, source scope, and reflection quotient; DR.2–DR.5 | Long prose and displayed rank data fit; headings are separated from text. |
| 68 | A33 Prym and integral real multiplication; DR.6–DR.7c | Correspondence formulas, adjoints, and labels remain distinct; normal-core paragraph fits. |
| 69 | Common lifted collision and the two quotient maps; DR.8–DR.11 | Dense proof text and all maps have adequate spacing; proof ending is correctly placed. |
| 70 | A33 finite canonical sufficient condition; A34 opening; BE.1–BE.2 | Section boundary and exponent bound display are clear. |
| 71 | A34 degree, intermediate field, and different calculation; BE.3–BE.5 | Four-point divisor, inequalities, and local power series are readable and within margins. |
| 72 | A34 two-fibre contradiction and exact exponent; BE.6–BE.8 | Long character-polynomial and primary-module displays fit without label collisions. |
| 73 | A34 Weil bounds, exception, and comparison with the older test; BE.9–BE.13 | Cases display is properly split; inequalities, sums, and subsequent headings are clear. |
| 74 | A34 realized degree-nineteen example; BE.14–BE.20 | Nineteen-entry occupancy list, valuation congruences, and recurrence fit cleanly. |
| 75 | A34 exact exponent conclusion; A35 opening and T2F.1–T2F.3 | Primary-group display, theta formula, cases display, and section boundary are legible. |
| 76 | A35 theta intersection, valuation induction, and residual set; T2F.4–T2F.9 | Long theta-intersection display and matrix-power indices are readable; no clipping. |
| 77 | A35 residual scope and RM5 corollary; T2F.10; effective Galois section opening | Corollary, section heading, and following source paragraph are clear; ordinary heading wrap causes no overlap. |

The report is limited to this requested full-size range. The build owner separately reviews the remaining pages and all contact sheets.
