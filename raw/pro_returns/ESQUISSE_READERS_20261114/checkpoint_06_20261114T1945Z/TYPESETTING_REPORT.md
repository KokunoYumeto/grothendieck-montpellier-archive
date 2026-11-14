# Typesetting report

This report gives measured results for the current PDFs. A partial working edition is identified explicitly. Rendered pages are counted as inspected only when a reviewer has recorded an observation against the exact PDF hash.

## Current build measurements

| PDF | Source pages | PDF pages | LaTeX errors | Overfull boxes | Widest (pt) | Missing characters | External links | Inspected / required |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| ESQUISSE_EN_corrected_translator_notes | 43 | 45 | 0 | 0 | 0 | 0 | 78 | 0 / 41 |
| ESQUISSE_FR_diplomatique | 46 | 49 | 0 | 0 | 0 | 0 | 82 | 0 / 41 |
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

Required rendered sample and repair pages: 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45.
Inspected pages for this exact PDF: none.
Remaining required pages: 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44, 45.


### ESQUISSE_FR_diplomatique

% EDITION STATUS: partial; source units 46/116.

The current source and compiled-source hash agree. Expected logical external links: 82; PDF external-link annotation rectangles: 82. Distinct archive pages linked: 46.
Apparatus entries in the projected source: 0; executed counter in the build log: None. Classes: .
Ink outside the sheet: 0 candidates; text-area violations: 1; permitted isolated glyph overhangs: 371.

Text-area candidates:
- PDF page 32: danslecontextedesespacestopologiques,àcausedessempiternelsphénomènesde“sauvagerie”..

Required rendered sample and repair pages: 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49.
Inspected pages for this exact PDF: none.
Remaining required pages: 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 35, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49.


### ESQUISSE_FR_corrige_apparat

% EDITION STATUS: partial; source units 58/58.

The current source and compiled-source hash agree. Expected logical external links: 99; PDF external-link annotation rectangles: 99. Distinct archive pages linked: 58.
Apparatus entries in the projected source: 38; executed counter in the build log: 38. Classes: wording variant: 38.
Ink outside the sheet: 0 candidates; text-area violations: 1; permitted isolated glyph overhangs: 500.

Text-area candidates:
- PDF page 32: danslecontextedesespacestopologiques,àcausedessempiternelsphénomènesde“sauvagerie”..

Required rendered sample and repair pages: 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 60, 61.
Inspected pages for this exact PDF: none.
Remaining required pages: 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 40, 41, 43, 44, 45, 46, 47, 49, 50, 52, 53, 55, 56, 58, 59, 60, 61.


## Reproducible intermediates excluded from publication

Raw runtime logs, font caches, downloaded support packages, temporary diagnostic PDFs and duplicate intermediate renderings are excluded. Sanitized build logs, exact source hashes, measured results, render indices and visual observations are retained. No source reading is taken from a diagnostic PDF.
