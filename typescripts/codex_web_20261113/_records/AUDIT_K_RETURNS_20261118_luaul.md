# Audit of the batch-K Work returns filed since 18 Nov 00:00 UTC (2026-11-18 08:49 UTC)

206 returns, 2921 pages. Written by tools/audit_k_returns.py (Claude Opus 5.5 at effort max); it reads the returns' files only, and compiles each standalone file with LuaLaTeX.

| measure | median | min | max |
|---|---|---|---|
| first pass, minutes a page | 1.5 | 0.7 | 26.2 |
| second reading, minutes a page | 1.5 | 0.0 | 12.5 |
| whole session, minutes | 71 | 11 | 224 |
| \unsure per 100 words | 7.22 | 1.22 | 19.05 |
| math notes, words | 1936.5 | 0 | 3388 |
| inventory rows | 291 | 4 | 639 |

By model: GPT-6.2 Astra Max: 174 returns, 2434 pages; ?: 5 returns, 77 pages; GPT-6 Astra Max: 27 returns, 410 pages

## Flags

- **compile errors**: 65: K1-02 (1), K1-05 (4), K1-06 (8), K1-07 (1), K10-01 (14), K126-02 (2), K135-02 (1), K158-01 (3), K161-1-01 (1), K162-5-01 (11), K19-01 (11), K23-02 (1), K23-03 (186), K27-01 (1), K27-03 (21), K29-03 (1), K31-02 (2), K31-03 (1), K34-06 (1), K34-08 (4), K37-01 (1), K37-02 (8), K41-01 (9), K43-01 (5), K43-03 (101), K43-04 (16), K43-08 (2), K43-09 (16), K57-01 (2), K70-02 (5), K70-03 (8), K73-01 (8), K74-01 (318), K74-04 (9), K74-05 (101), K74-07 (2), K76-01 (9), K76-02 (3), K76-03 (23), K76-04 (1)
- **no PDF**: 11: K34-02_2, K43-02, K43-02_2, K43-03, K43-04_2, K43-07_2, K46-01_2, K74-05, K79-06, K79-07, K79-11
- **unbalanced page files**: 0
- **no 'transcription frozen'**: 4: K43-02, K43-04, K43-07, K46-01
- **no 'mathnotes done'**: 4: K43-02, K43-04, K43-07, K46-01
- **hashes after the notes not stated as matching**: 4: K1-05, K63-01, K74-01, K79-13
- **inventory rows not 'yes'**: 4: K1-01, K57-03, K83-03, K84-03
- **second reading under 1 minute a page**: 26: K10-01, K10-05, K101-01, K126-01, K126-02, K158-01, K158-02, K158-03, K23-01, K23-02, K23-03, K23-05, K34-11, K43-02, K43-04, K57-03, K79-17, K83-01, K83-04, K83-06, K83-07, K84-03, K85-03, K86-01, K86-02, K88-01
- **no \unsure at all**: 6: K34-02_2, K43-02, K43-02_2, K43-04_2, K43-07_2, K46-01_2
- **math notes missing sections**: 9: K34-02_2, K43-02, K43-02_2, K43-04, K43-04_2, K43-07, K43-07_2, K46-01, K46-01_2
- **overfull boxes over 2pt**: 191: K1-01, K1-02, K1-03, K1-04, K1-05, K1-06, K1-07, K10-01, K10-02, K10-03, K10-04, K10-05, K10-06, K10-07, K101-01, K101-02, K101-03, K102-01, K111-01, K123-01, K123-02, K123-03, K125-01, K126-01, K126-02, K127-01, K127-02, K134-2-01, K134-2-03, K135-01, K135-02, K135-04, K158-01, K158-02, K158-03, K158-04, K158-05, K160-01, K160-02, K161-1-01
