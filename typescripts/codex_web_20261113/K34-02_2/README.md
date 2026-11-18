# K34-02 — scans 34–49

This package contains the diplomatic LaTeX transcription of all sixteen supplied scans, the individual page sources, an assembled fragment, the supplied preamble, and a standalone wrapper. It also includes the doubt register and notation table, element inventory, page-by-page audit, documentary notes, and mathematical notes.

Read `K34-02_doubts.md` alongside the transcription. There are 241 `\unsure` occurrences, no `\illegible` occurrences, and 195 `\deleted` occurrences in the sixteen page files. These counts include nested and canceled material and count each page once. The 392 inventory rows are all marked `transcribed=yes`; nested revisions have separate entries.

The page files are concatenated in scan order to make `K34-02_transcription.tex`. The standalone wrapper inputs `PREAMBLE.tex` and that fragment. No compilation was attempted, as requested. `check_balance.js` checks braces, inline and display math delimiters, and environment nesting; its actual results are in `K34-02_balance.txt`. The manuscript's own unfinished parentheses and cut-edge formulas are preserved and are distinct from LaTeX delimiter balance.

The original workspace became accessible again after the recovery checkpoint. Every original page file and the preamble matched the recovery copy byte for byte. The full original audit and timestamps are restored, and the final cross-page notation comparison is appended to the audit. None of the sixteen page files was changed during completion. Any later reading questions are in section 6 of the mathematical notes.

`audit_evidence/` contains the original per-page start records and observations made before opening each page file for its second-pass comparison. `working_records/` preserves the original visual inventory, original progress log, initial notation working notes, and recovery-checkpoint progress log. These are historical records: use the main inventory and doubt register for the final element enumeration and notation readings. Text blocks may contain displays or revisions that also have their own inventory entries; source-line locators anchor them in reading order, with physical regions indicated separately.

`progress.log` records the final freeze, all seventeen source SHA-256 hashes, completion of the mathematical notes, and the subsequent unchanged-hash check. `K34-02_frozen_sha256.txt` repeats the seventeen frozen source hashes. `SHA256SUMS` covers all delivered files except itself, with paths relative to this folder. `input_manifest.tsv` is the supplied image manifest; the image files themselves are not included in this output package.

All scans 34–49 are transcribed and audited. No page is unfinished. The manuscript's uncertain readings remain explicitly documented; completion does not mean that every compressed or canceled word can be deciphered with certainty.
