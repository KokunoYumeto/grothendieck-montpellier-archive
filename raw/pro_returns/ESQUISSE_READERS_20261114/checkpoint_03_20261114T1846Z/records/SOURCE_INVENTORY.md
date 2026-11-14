# Source inventory

This inventory is mechanical. It assigns no scan-reading outcome.

Both attached manifests were read before the inventories were prepared. Every listed file matched its byte count and SHA-256 digest.

| Source | Manifest entries | Verified |
| --- | ---: | ---: |
| ESQUISSE_TEXT.zip | 143 | 143 |
| ESQUISSE_SCANS.zip | 232 | 232 |

| Item | Copy 1 | Copy 2 | Total |
| --- | ---: | ---: | ---: |
| pages | 58 | 58 | 116 |
| note_items | 175 | 169 | 344 |
| difference_rows | 327 | 141 | 468 |
| hand | 33 | 38 | 71 |
| over | 0 | 7 | 7 |
| inserted | 0 | 6 | 6 |
| margin | 57 | 72 | 129 |
| deleted | 0 | 9 | 9 |
| xout | 0 | 0 | 0 |
| unsure | 6 | 19 | 25 |
| illegible | 0 | 1 | 1 |
| uline | 140 | 140 | 280 |
| uuline | 0 | 0 | 0 |
| diagram | 1 | 1 | 2 |
| mspage | 58 | 58 | 116 |
| scanpage | 58 | 58 | 116 |

The source inventory counts parsed content commands, including nested commands and a content command unintentionally suppressed after an inline percent sign (flagged in its packet). Full comment lines are excluded. Original uncertainty and handwriting assignments remain unverified until an explicit review is recorded.

## Stable identifiers

Difference identifiers retain original row order: D1-001 through D1-327 and D2-001 through D2-141. Macro identifiers are M-<page key>-<three-digit occurrence>; note identifiers are N-<page key>-<three-digit item>. Each packet records the original file hash, complete text, numbered lines, exact macro spans, all note items, original difference rows, archive metadata, and both required image names.

The original record copies in `records/source_records/` preserve ZIP-relative source names. No scan images or original page files are duplicated there. Review packet strings use LF line endings; the recorded source hash always describes the original bytes in the attachment. This newline decoding has no printed effect.
