# K34-09 diplomatic transcription

Completed scans: **149–162 and 164** (15 scans), in that order.

- `pages/`: one diplomatic LaTeX file per scan.
- `K34-09_transcription.tex`: exact concatenation, preceded by the single cote marker.
- `K34-09_standalone.tex` and unchanged `PREAMBLE.tex`: wrapper for the recipient’s compilation.
- `K34-09_doubts.md`: reconciled notation, every marked doubt, possible slips and abbreviations.
- `K34-09_inventory.csv`: 430 elements, all transcribed.
- `K34-09_audit.md`: timed second readings, formulas, corrections and supplementary checks.
- `K34-09_notes.md`: the manuscript’s unverified steps, headings and page numbering.
- `K34-09_mathnotes.md`: commentary written only after the transcription freeze.
- `progress.log` and `K34-09_frozen_sha256.json`: checkpoints and frozen transcription hashes.
- `K34-09_check_balance.py` and `K34-09_balance.json`: read-only structural checker and results.
- `notation.json`: machine-readable notation table.

Counts in the page files alone: **242 unsure**, **4 illegible**, **163 deleted** macros. Nested cancellations are counted as separate macro occurrences. The four illegible marks estimate six obscured words, all in cancelled prose.

The pages are all handwritten subject notes. Scan 150 contains live text followed by a cancelled draft, so its sheet kind remains `text`; the cancelled elements are individually marked. Archive sheet numbers are comments only. The final sentence on 164 is incomplete at the supplied page boundary.

No OCR, external transcription or web source was used. **Not compiled**, as requested. Structural balance passes; that does not certify layout or eliminate the documented reading uncertainties.
