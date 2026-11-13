# Return MPL_16+47+54+44 (cotes 16, 47, 54, 44; package 11)

Recorded 12 Nov 2026, 16:29 UTC, by Claude Opus 5.5. This file is ours, not part of the return.

## The zip

| Zip (in `longue_marche_pro_pilot_20261104\answers\`) | Saved | Bytes | Members | SHA-256 |
|---|---|---:|---:|---|
| `MPL_16+47+54+44.zip` (final) | 12 Nov 17:26:06 local (16:26:06 UTC) | 310,110 | 87 | `9450f40c7adb6e2ad71468ae1b680317fa1a9ce12c3c9c2e35b27fbad6f775b9` |

The zip test passes. Its 87 members are files only (no folder entries, no unsafe paths): 82 pages in `pages/`, the
combined transcription, the doubts register, the inventory, the research notes and `progress.log`. This unpacked folder
matches the zip member for member, byte for byte (none missing, none different, none extra). No checkpoint zip of this
run was saved locally; `progress.log` records eight checkpoints written to the Library (scans 048, 031, 008, 056, 012,
005, 042, 045).

## Pages per cote, against `packages_work\MPL_16+47+54+44\MANIFEST.json`

| Cote | Title (archive) | Scans in manifest | Pages returned | Same scans | Skipped as blank by the package |
|---|---|---:|---:|---|---|
| 16 | Formalisme algébrique des correspondances et algèbres de Poincaré-Hodge (1966-1967) | 54 (1, 3–23, 25–56) | 54 | yes | 2, 24 |
| 47 | Produit de convolution sur les VA et transformation de Fourier dans les VA (s.d.) | 11 (1–11) | 11 | yes | none |
| 54 | Dualité en cohomologie des V. A. ([à partir de 1971]) | 8 (1–8) | 8 | yes | none |
| 44 | Jacobiennes intermédiaires (1964) | 9 (1–9) | 9 | yes | none |
| | | **82** | **82** | | |

Page files are named `pages/MPL_16+47+54+44_<cote>_scan<NNN>.tex`. The four very short pages are folder title
sheets: 16 scan 31 ("Algèbres de Hodge", 79 bytes), 16 scan 32 ("Formulaire des $L,\Lambda$, etc", 92 bytes), 47 scan 2
(the folder title, 151 bytes) and 54 scan 2 (the folder title, 79 bytes). Two other short pages carry text: 44 scan 6
(Theorem 7 with the "Matsusaka" margin, 200 bytes) and 16 scan 55 (435 bytes).

## `progress.log` (423 lines)

- Started 14:45:06 UTC; 82 "done" lines, one per scan; 152 "revised" lines; 16 checkpoint lines (8 created, 8 saved).
- Audit: 84 per-scan "audited" lines (with the reader that audited each), covering all 82 scans; 16 scan 005 and
  54 scan 003 were audited twice. An 85th line mentioning the audit is the pre-freeze summary below.
- 15:43:23 UTC: LaTeX syntax QA, all 82 page fragments compiled to DVI; TikZ-cd ampersands, isolated math delimiters
  and math-mode quotation marks corrected "without reading changes".
- 15:57:54 UTC: "Final pre-freeze checks passed: all 82 individually audited page fragments and the combined fragment
  compiled to DVI; … no external mathematical context or literature consulted before freeze."
- 15:57:54 UTC: "transcription frozen", followed by 83 SHA-256 lines (the 82 pages and the combined transcription).
  **All 83 match the files of this return.**
- 16:17:28 UTC: "Post-freeze research completed and independently reviewed: 347 page-specific notes plus 81
  literature/computation supplements (428 total) … no frozen transcription changes."
- 16:17:29 UTC: "frozen hashes verified unchanged".

## Counts

- **Research notes** (`MPL_16+47+54+44_notes.md`): 428 = 347 page-specific notes (`## cote:scan:n` headers; 148
  unproved claims, 73 reading questions, 58 unpursued implications, 45 own ideas, 23 conjectures) + 81 post-freeze
  items in four sections (R1–R22, S1–S19, F1–F20, D01–D20), each section with its references. The counts agree with
  the log.
- **Doubts** (`MPL_16+47+54+44_doubts.md`): shared notation table (44 rows), 624 doubts (cote 16: 418, 47: 87,
  54: 55, 44: 64; confidence low 336, medium 231, high 57) on 74 of the 82 scans, abbreviations (212 rows), and a
  section on legibility and limits.
- **Inventory** (`MPL_16+47+54+44_inventory.csv`): 1,716 rows (cote 16: 1,287, 47: 129, 54: 122, 44: 178), all
  `transcribed = yes`, every one of the 82 scans present.
- **Combined transcription** (`MPL_16+47+54+44_transcription.tex`): 185,919 bytes.
