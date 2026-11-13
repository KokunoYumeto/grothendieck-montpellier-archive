# Return MPL_142_094-122 (cote 142, scans 94–122)

Recorded 12 Nov 2026, 15:55 UTC, by Claude Opus 5.5. This file is ours, not part of the return.

## The two zips

| Zip (in `longue_marche_pro_pilot_20261104\answers\`) | Saved | Bytes | Members | SHA-256 |
|---|---|---:|---:|---|
| `MPL_142_094-122.zip` (final) | 12 Nov 15:15:53 UTC | 148,551 | 34 | `e59539d952ee265c297aa950f79bbe65336dafeb880c1a49771209f413bcc02b` |
| `MPL_142_094-122_checkpoint_120.zip` | 12 Nov 15:08:35 UTC | 73,003 | 27 | `cf41d86cd436ad2469eb88a2a540c6e0100453dcd8b4c60d586f53973f58cbc5` |

Both unpacked folders match their zips member for member, byte for byte (no file missing, none different, none
extra).

## What the final holds

- 29 page files, `pages/MPL_142_094-122_scan094.tex` to `scan122.tex`: every scan of the package manifest
  (94–122, none skipped as blank).
- The combined transcription, the inventory (529 rows, all `transcribed = yes`, every scan 94–122 present), the
  doubts register (shared notation table, 200 curated doubts, an occurrence register per scan for all 29 scans,
  abbreviation glossary, legibility), the research notes (92 items in four sections, scans 094–100, 101–107,
  108–114, 115–122) and `progress.log`.
- `progress.log` records the SHA-256 of the 29 pages and of the combined transcription at the freeze
  (14:44:46 UTC); all 30 match the files of the final. It also records that nothing in the transcription changed
  after the context was opened.

## Does the final contain everything the checkpoint has?

Yes.

- Files: all 27 files of the checkpoint are in the final. The final adds the research notes, the six pages the
  checkpoint did not yet have (099, 100, 113, 114, 121, 122) and the full apparatus.
- Pages: the checkpoint had 23 pages (094–098, 101–112, 115–120). In the final, 2 of them are byte-identical
  (105, 119) and 21 were revised by the audit pass that `progress.log` records after the checkpoint ("scan … audited").
  No page lost a margin note, insertion, deletion or diagram: the counts of `\margin`, `\inserted`, `\deleted` and
  `\diagram` are equal or higher on every page. The word count fell on three pages (098 by 6, 101 by 2, 118 by 6
  words); the line-by-line differences there are changed readings (for example a struck word reread as
  *Inversement* on 098, `\unsure{R|\mathcal{R}}` settled as `\mathcal{R}` on 118), not dropped text.
- Inventory: all 431 (scan, element) keys of the checkpoint are in the final; the final has 529 rows. Some rows were
  reworded by the audit, so 126 checkpoint rows are not identical in the final, but none is missing.
- `progress.log`: every line of the checkpoint's log is in the final's.
- Doubts: the checkpoint's register (notation policy, doubts, abbreviations, legibility, covering 16 scans) was
  rewritten into the final's larger register, which covers all 29 scans; its lines are not carried over word for
  word.
