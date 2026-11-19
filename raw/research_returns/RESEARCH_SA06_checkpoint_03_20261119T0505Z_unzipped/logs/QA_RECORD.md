# PDF layout and visual inspection

Checkpoint 01, 19 November 2026, 03:38 UTC (04:38 Europe/Berlin).

The 53-page LuaLaTeX PDF was rendered at 90 dpi on pages 1, 4, 10, 21, 30, 31, 35, 43, 47, and 53. The assembled contact sheet was visually inspected. Text, formulas, headers, and references fit their page areas without clipping. The spread sample covers the title, Parts A–E, and the final bibliography. Page 31 contains the corrected D.0b real-torus formula.

Earlier completed-body layout: one overfull box above 2 pt, maximum 6.54274 pt, in the former page-30 D.0b inline formula. It was converted to an aligned display. Final checkpoint layout: zero overfull boxes, zero overfull boxes above 2 pt, maximum 0 pt; zero undefined citations; zero missing characters. The final PDF contains 53 pages and 572432 bytes. The latest machine record is logs/latest_layout.json.

The first checkpoint was due at 03:35 UTC. Its packaging was delayed by first-build dependency repair and the initial render inspection; the actual archive and save times are recorded rather than backdated. Subsequent target times remain 04:20, 05:05, 05:50 UTC, and every 45 minutes thereafter.

## Checkpoint 02 — 19 November 2026, 04:17 UTC (05:17 Europe/Berlin)

The final 84-page LuaLaTeX PDF was rendered at 90 dpi on pages 1, 4, 10, 19, 24, 25, 26, 29, 34, 40, 43, 48, 50, 54, 60, 65, 70, 78 and 84. Both nine-page contact sheets and the full-size page25 were visually inspected. This covers every location with an earlier overflow: the quintic basis on page24, the S/T/Q construction on page25, the logarithmic trace formula on page34, and the real-torus formula now on page50. All fit the text area without clipping or collisions. The spread sample covers every Part and the reference list.

Before correction: the first new-content build stopped on a raw bibliography underscore and had two overfull boxes (14.10156pt and 4.97324pt); the first completed 84-page build then had one remaining 14.77728pt box in the quintic basis list. Each formula was split or displayed in its source, and the bibliography literal was escaped. After correction: zero overfull boxes, zero boxes above2pt, maximum0pt; zero undefined citations and zero missing characters. Final PDF:84pages,787018bytes. Machine record:20261119T041518Z_layout.json. The mathematical coefficient-field correction in C.2j is included in this build.

The removed intermediate C.4 remaining-work paragraphs are superseded by C.4m–p and their final precise residual-case paragraph. The previous bounds6/120 remain valid intermediate results but are replaced as strongest bounds by2/6.


## Checkpoint03 typesetting and visual verification — 2026-11-19 05:02 UTC

- Intermediate build20261119T045942Z: one overfull box,8.81996pt, in C.3h's operator display on page45. Split that display into two lines. An attempted aligned-format repair had a math-mode error; it was replaced by a gathered display. The interrupted aux exposed a build-script pre-BibTeX issue; pre-BibTeX now runs only when the aux contains bibdata.
- Final completed build20261119T050101Z:114pages; zero overfull boxes, zero above2pt, maximum0pt; no undefined citations and no missing characters. The PDF size is987497bytes.
- Rendered and visually inspected pages1,10,24,25,31,35,42,43,44,45,46,57,71,72,84,85,93,97,104,110,114. These include former overflow material, new cone/graded proofs, new effectivity and Walker proofs, arithmetic localization, source corrections and bibliography.
- Opened all three contact sheets and full-size page45 before and after the repair. The final operator display lies within the text block; headings, equations, page breaks and citations in the inspected sample are legible and unclipped. Rendered images are not included in the checkpoint.
- C.3i and C.4r–s are late independently audited fragments retained separately in this checkpoint; they are not yet inputs to the114-page PDF. Their integration and a fresh layout check will follow the scheduled save.
