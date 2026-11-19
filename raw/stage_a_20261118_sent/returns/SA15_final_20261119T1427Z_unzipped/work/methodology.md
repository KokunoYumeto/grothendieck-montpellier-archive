# Working conventions

The input ZIP was extracted once to `sources/`. No scans or second-pass files are supplied. Input files remain unchanged.

`NOTES_INDEX.tsv` contains 80 rows, all in `MPL_7_061-072+8_001-078`. Other packages use level-two headings and are absent from that index. Indexed IDs remain unchanged. Supplemental note IDs use `PACKAGE##N`, the ordinal level-two note heading; the supplementary verdict table is additional to the required exactly 80-row entry table.

Locations use cote, scan and one-based line numbers in the supplied transcription file (including blank lines); they are not claimed to be handwritten line numbers. Cote and scan are mandatory because scan numbers repeat between folders. Where a page has no supplied text, record that fact without reconstructing it.

The manuscript, earlier model commentary, current mathematical reconstruction, and literature evidence are separate evidence layers. An opened bibliographic landing page verifies metadata only; it does not verify a theorem. `verified` in the bibliography means the URL was opened, with the scope of inspection recorded separately.

Reviewers are GPT-6 Astra Pro, reasoning effort not exposed by this runtime, run `SA15-20261119` with the task name as suffix. No events will be labelled formal certificates unless a genuine formal certificate exists.

Checkpoints are new ZIPs at 45-minute elapsed intervals from 13:02:39 UTC, containing all current deliverables and work documentation, excluding source attachments and earlier checkpoint archives. The final archive is `SA15.zip`; it is the sole final download.
