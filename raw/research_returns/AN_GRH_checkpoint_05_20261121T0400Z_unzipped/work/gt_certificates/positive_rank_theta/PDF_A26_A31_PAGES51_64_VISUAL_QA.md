# Independent visual QA: frozen A01–A31 build, pages 51–64

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

## Scope and result

**PASS — no clipping, overlap, missing symbols, equation-tag collisions, or table-layout defects observed in the requested range.** This is a visual layout review, not an additional mathematical proof check.

The reviewer opened and inspected every full-size rendered PNG from `page-51.png` through `page-64.png` in `work/effective_galois/tex_build/a01_a31/qa/`. These are pages 51–64 of the 88-page frozen PDF, covering A26–A31 and the transition to effective Galois comparison. No final source, build file, or rendered image was edited.

Frozen PDF: `work/effective_galois/tex_build/a01_a31/AN_GRH.pdf`.

PDF SHA256: `ed7908c3570a783dce30ef1c7289d6d583cad36281cd7319004f5edbdc92ded7`.

Frozen source SHA256: `447fed6f4d8c8b3479fe08d96eb10c8cf8c7ae21840de43c7f2822615484e287`.

## Page-by-page observations

| Page | Material inspected | Layout result |
| --- | --- | --- |
| 51 | A26 statement and Fourier/augmentation proof; RA.1–RA.3 | Clear text and displays; no collisions. |
| 52 | A26 source/scope paragraph; A27 statement and Frobenius data; RO.1–RO.7 | Headings, two-line polynomial, and bottom display are legible and within margins. |
| 53 | A27 eigenspace and all-extension bounds; RO.8–RO.12 | Inequalities, subscripts, and proof-step headings are clear. |
| 54 | Nine-row finite verification table RO.13; A28 statement; RC.1–RC.2 | Table columns, row entries, and equation label are separated; following section fits cleanly. |
| 55 | A28 residual scope; A29 statement and cyclic quotient; PC.1–PC.4 | Multiline Prym display and surrounding prose are separated; no clipping. |
| 56 | A29 Lang connectedness and character-polynomial derivation; PC.5–PC.7 | Dense formulas, sums, and proof paragraphs remain readable. |
| 57 | A29 faithful-character, Prym, and deck arguments; PC.8–PC.12 | Product limits, displayed identities, and end-of-proof symbol are correctly placed. |
| 58 | A29 characteristic-two form and strictness; A30 opening; PC.13–PC.14, DC.1–DC.2 | Section boundary and bottom display are clean. |
| 59 | A30 counterexample scope and elliptic Lang construction; DC.3–DC.7 | Full-width character factorization fits; long formulas and maps are legible. |
| 60 | A30 Euler-factor and individual-character calculations; DC.8–DC.11 | Fractions, products, overlines, and two-character display have no collisions. |
| 61 | A30 unramified-double-cover discussion; A31 opening and coordinate change; DC.12–DC.13, TS.1–TS.2 | Dense discussion and two-line coordinate display fit within the page. |
| 62 | A31 exact isomorphism, norm, divisor, and theta twist; TS.3–TS.10 | Aligned coefficient calculation and exact norm formulas are clear; bottom display is safe. |
| 63 | A31 signed orbit and detector scope; TS.11; effective Galois section opening | Proof ending and new section boundary are legible; ordinary heading line break causes no overlap. |
| 64 | Effective Chebotarev statement and G01/G02 proofs | Long bound and Galois notation fit; no clipping or tag collisions. |

The report is limited to this requested full-size range. The build owner separately reviews the remaining pages and overall contact sheets.
