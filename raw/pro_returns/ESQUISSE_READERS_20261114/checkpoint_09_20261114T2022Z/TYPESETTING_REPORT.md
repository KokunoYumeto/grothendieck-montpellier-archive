# Typesetting report

This report gives measured results for the current PDFs. A partial working edition is identified explicitly. Rendered pages are counted as inspected only when a reviewer has recorded an observation against the exact PDF hash.

## Current build measurements

| PDF | Source pages | PDF pages | LaTeX errors | Overfull boxes | Widest (pt) | Missing characters | External links | Inspected / required |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ESQUISSE_EN_corrected_translator_notes | 43 | 45 | 0 | 0 | 0 | 0 | 78 | 0 / 41 |
| ESQUISSE_FR_diplomatique | 93 | 97 | 0 | 0 | 0 | 0 | 154 | 0 / 56 |
| ESQUISSE_FR_corrige_apparat | 58 | 61 | 0 | 0 | 0 | 0 | 99 | 0 / 43 |

## Baseline and repair history

- The supplied unchecked esquisse combined source, run as a diagnostic with LuaLaTeX, produced 36 errors and 10 overfull boxes, widest 432.66957 pt. Its diagnostic PDF is excluded from the readers. The supplied earlier pdfLaTeX record reported 35 errors; the engine and run are distinguished here.
- The supplied unchecked esquisse_copy2 combined source, run as a diagnostic with LuaLaTeX, produced 36 errors and 10 overfull boxes, widest 432.66957 pt. Its diagnostic PDF is excluded from the readers. The supplied earlier pdfLaTeX record reported 35 errors; the engine and run are distinguished here.

The first partial French build exposed three missing Γ characters inside a math-roman command. The fontspec no-math setting preserves the required math-font slots. Breakable underlining repairs the initial unbreakable prose boxes without changing their text. Individual repairs and page keys are recorded in TYPESETTING_FIXES.tsv; syntax repairs are recorded in CLEANUP_LOG.tsv.

## Per-PDF findings

### ESQUISSE_EN_corrected_translator_notes

% EDITION STATUS: partial; source units 43/58.

The current source and compiled-source hash agree. Expected logical external links: 78; PDF external-link annotation rectangles: 78. Distinct archive pages linked: 43.
Apparatus entries in the projected source: 36; executed counter in the build log: None. Classes: translator note: 35, wording variant: 1.
Ink outside the sheet: 0 candidates; text-area violations: 0; permitted isolated glyph overhangs: 398.
Printed nonempty apparatus bodies: not yet logged; per-ID projection/print differences: 0. Every printed body is guarded against an undefined or empty declaration.
Current PDF hash matches the successful compilation record: False. Upstream inputs changed since generation: 0.
Source starred-footnote pairs checked: 0; pairs split across physical pages or with mismatched marker counts: 0. Endnote calls: not yet checked; definitions: not yet checked; forward/return-link problems: not yet checked.

Required rendered sample and repair pages: 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45.
Inspected pages for this exact PDF: none.
Remaining required pages: 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45.


### ESQUISSE_FR_diplomatique

% EDITION STATUS: partial; source units 93/116.

The current source and compiled-source hash agree. Expected logical external links: 152; PDF external-link annotation rectangles: 154. Distinct archive pages linked: 93.
Apparatus entries in the projected source: 0; executed counter in the build log: 0. Classes: .
Ink outside the sheet: 0 candidates; text-area violations: 0; permitted isolated glyph overhangs: 0.
Printed nonempty apparatus bodies: 0; per-ID projection/print differences: 0. Every printed body is guarded against an undefined or empty declaration.
Current PDF hash matches the successful compilation record: True. Upstream inputs changed since generation: 4.
Source starred-footnote pairs checked: 18; pairs split across physical pages or with mismatched marker counts: 0. Endnote calls: 15; definitions: 7; forward/return-link problems: 7.

Starred-footnote placements:
- esq_119_009 (*): PDF page 11 has 2 marks.
- esq_119_014 (*): PDF page 16 has 2 marks.
- esq_119_019 (*): PDF page 21 has 2 marks.
- esq_119_021 (*): PDF page 23 has 2 marks.
- esq_119_022 (*): PDF page 24 has 2 marks.
- esq_119_025 (*): PDF page 27 has 2 marks.
- esq_119_025 (**): PDF page 27 has 2 marks.
- esq_119_026 (*): PDF page 28 has 2 marks.
- esq_119_042 (*): PDF page 44 has 2 marks.
- esq_119_053 (*): PDF page 55 has 2 marks.
- esq119_119_085 (*): PDF page 70 has 2 marks.
- esq119_119_090 (*): PDF page 75 has 2 marks.
- esq119_119_095 (*): PDF page 80 has 2 marks.
- esq119_119_097 (*): PDF page 82 has 2 marks.
- esq119_119_098 (*): PDF page 83 has 2 marks.
- esq119_119_101 (*): PDF page 86 has 2 marks.
- esq119_119_101 (**): PDF page 86 has 2 marks.
- esq119_119_102 (*): PDF page 87 has 2 marks.

Marginal-note placements: 104 in the margin, 0 labelled in the text block. The LuaLaTeX renderer counts actual line boxes at footnote size; it also enforces a height of at most three footnote-size baselines for a marginal placement.

Geometric exclusions, each retaining its measured box in the JSON audit: 107. These are ink inside the reserved marginal-note frame or conservative stroke boxes whose exact butt-capped rule endpoints remain inside the main frame. Paths and images are otherwise subject to the same page/type-frame checks as text.

Link-count differences require review; a wrapped link can produce more than one PDF rectangle.
- https://grothendieck.umontpellier.fr/web/viewer.html?file=../119.pdf#page=79: source 5, PDF rectangles 7.

Required rendered sample and repair pages: 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 26, 28, 31, 32, 33, 35, 38, 40, 43, 44, 45, 46, 48, 50, 53, 55, 58, 60, 63, 65, 67, 69, 70, 72, 75, 77, 78, 80, 82, 85, 87, 90, 92, 95, 97.
Inspected pages for this exact PDF: none.
Remaining required pages: 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 26, 28, 31, 32, 33, 35, 38, 40, 43, 44, 45, 46, 48, 50, 53, 55, 58, 60, 63, 65, 67, 69, 70, 72, 75, 77, 78, 80, 82, 85, 87, 90, 92, 95, 97.


### ESQUISSE_FR_corrige_apparat

% EDITION STATUS: partial; source units 58/58.

The current source and compiled-source hash agree. Expected logical external links: 99; PDF external-link annotation rectangles: 99. Distinct archive pages linked: 58.
Apparatus entries in the projected source: 38; executed counter in the build log: 38. Classes: wording variant: 38.
Ink outside the sheet: 0 candidates; text-area violations: 1; permitted isolated glyph overhangs: 500.
Printed nonempty apparatus bodies: 0; per-ID projection/print differences: 38. Every printed body is guarded against an undefined or empty declaration.
Current PDF hash matches the successful compilation record: False. Upstream inputs changed since generation: 0.
Source starred-footnote pairs checked: 10; pairs split across physical pages or with mismatched marker counts: 0. Endnote calls: 8; definitions: 7; forward/return-link problems: 0.

Starred-footnote placements:
- esq_119_009 (*): PDF page 11 has 2 marks.
- esq_119_014 (*): PDF page 16 has 2 marks.
- esq_119_019 (*): PDF page 21 has 2 marks.
- esq_119_021 (*): PDF page 23 has 2 marks.
- esq_119_022 (*): PDF page 24 has 2 marks.
- esq_119_025 (*): PDF page 27 has 2 marks.
- esq_119_025 (**): PDF page 27 has 2 marks.
- esq_119_026 (*): PDF page 28 has 2 marks.
- esq_119_042 (*): PDF page 44 has 2 marks.
- esq_119_053 (*): PDF page 55 has 2 marks.

Apparatus discrepancies requiring repair:
- V-FR-006-001: projected 1, printed 0.
- V-FR-006-002: projected 1, printed 0.
- V-FR-007-001: projected 1, printed 0.
- V-FR-009-001: projected 1, printed 0.
- V-FR-010-001: projected 1, printed 0.
- V-FR-010-002: projected 1, printed 0.
- V-FR-012-001: projected 1, printed 0.
- V-FR-013-001: projected 1, printed 0.
- V-FR-014-001: projected 1, printed 0.
- V-FR-015-001: projected 1, printed 0.
- V-FR-016-001: projected 1, printed 0.
- V-FR-017-001: projected 1, printed 0.
- V-FR-019-001: projected 1, printed 0.
- V-FR-024-001: projected 1, printed 0.
- V-FR-024-002: projected 1, printed 0.
- V-FR-025-001: projected 1, printed 0.
- V-FR-026-001: projected 1, printed 0.
- V-FR-027-001: projected 1, printed 0.
- V-FR-027-002: projected 1, printed 0.
- V-FR-028-001: projected 1, printed 0.
- V-FR-028-002: projected 1, printed 0.
- V-FR-032-001: projected 1, printed 0.
- V-FR-033-001: projected 1, printed 0.
- V-FR-033-002: projected 1, printed 0.
- V-FR-034-001: projected 1, printed 0.
- V-FR-035-001: projected 1, printed 0.
- V-FR-035-002: projected 1, printed 0.
- V-FR-036-001: projected 1, printed 0.
- V-FR-036-002: projected 1, printed 0.
- V-FR-038-001: projected 1, printed 0.
- V-FR-039-001: projected 1, printed 0.
- V-FR-042-001: projected 1, printed 0.
- V-FR-043-001: projected 1, printed 0.
- V-FR-044-001: projected 1, printed 0.
- V-FR-045-001: projected 1, printed 0.
- V-FR-046-001: projected 1, printed 0.
- V-FR-050-001: projected 1, printed 0.
- V-FR-052-001: projected 1, printed 0.

Text-area candidates:
- PDF page 32: danslecontextedesespacestopologiques,àcausedessempiternelsphénomènesde“sauvagerie”..

Required rendered sample and repair pages: 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 60, 61.
Inspected pages for this exact PDF: none.
Remaining required pages: 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 60, 61.


## Reproducible intermediates excluded from publication

Raw runtime logs, font caches, downloaded support packages, temporary diagnostic PDFs and duplicate intermediate renderings are excluded. Sanitized build logs, exact source hashes, measured results, render indices and visual observations are retained. No source reading is taken from a diagnostic PDF.
