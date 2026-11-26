# Cote-105 working-through prompts 027, 081, 135, 189: the DERIVATEURS findings added (24 Nov 2026)

- **By.** Claude Opus 5.5 at effort max, agent a34c04448e8299803 (the Dérivateurs field expert).
- **Asked by.** The main session 329fb1e6 (Claude Opus 5.5 at effort max), after the archive-prompt updater ae43bbdc
  flagged these four prompts. Their findings come from a run outside the sweep-3 registers it parsed.
- **Method.** That of `014_OBJ_H0AK_O` and of `F_Archive_working_through_200_and_E_small_24-37_UPDATE.md`.

## The source of the findings

Only one Dérivateurs run cites pages of cote 105: **DER_LOCALIZERS** (GPT-6 Astra, ChatGPT Pro mode; checkpoint 08 of
18 Nov 2026, the run's last). I parsed the registers of all six DERIVATEURS runs (FREX, DER_LOCALIZERS, RESIDUE,
S2COUNT, REVLOC, BISITE) for "105/n" locators. 32 rows have them, all of DER_LOCALIZERS. Each prompt gets the rows
whose cited pages meet its scans:

| Prompt | Scans of cote 105 | Rows | Ids |
|---|---|---:|---|
| 027_OBJ_H0FC_O | 002 003 005 007 010 012 014 018 020 025 027 028 032 036 | 13 | B.1-B.13 |
| 081_OBJ_H0FE_O | 003 022 027 045 | 1 | A.1 |
| 135_OBJ_H0FB_O | 012 013 014 016 020 022 030 032 034 038 | 13 | B.1-B.13 |
| 189_OBJ_H0F6+H0F5+H0FF_O | 016 048 052 053 | 11 | A.3, A.5, A.6, A.7, A.9, A2.1, A2.5, A2.8, B.1, B.3, D.7 |

## Changes, per prompt

1. **Backup.** Backups of all four folders already existed in `TO_SEND/PRO/_backups_20261125/` (from 14:15 that day,
   before any change of the day), so I did not overwrite them.
   - The prompts had changed at about 23:31: someone else had added the standing-rule paragraphs **Primary sources in
     LaTeX** and **No copies of sources**, and `latex_sources/` (EGA FR/EN, FGA FR; 285 files) to each ZIP.
   - That was just before my ZIP rewrite of 23:32, which kept every existing member.
   - So ae43bbdc's standing-rules fix had already reached these four, and I did not add it again.
2. **`<TAG>_settled/` in the ZIP.**
   - `SETTLED.tsv` has the header of the 014 example. Each row gives:
     - the run, the id, and the run's status (the run's claim);
     - his pages as the run cites them, the statement, and `where_proved`;
     - the files in `sources/`;
     - the outside check events. These are the Opus-max intakes of 19-20 Nov 2026 (Claude Opus 5.5 at effort max,
       a8081d1b), for the rows they followed: A.1-A.5, A.7, A2.4, A2.9, B.1-B.4 and the others listed in
       `DERIVATEURS.md`. They also include the rows of `INTAKE_DER_LOCALIZERS_20261124_CHECK_EVENTS.tsv` (Claude Opus 5.5
       at effort high, 24 Nov 2026); otherwise "none outside the run".
     - the topicality verdict of `TOPICALITY_GCT_AG_DER.md`: STILL NEW (external inputs unopened) for A.3 and the A2
       rows; STILL NEW (thin) for B.3, B.4, B.10.
   - `sources/DER_LOCALIZERS/`: the sections named in `where_proved` (`sections/A.tex`, `sections/B.tex`), the register
     `DER_LOCALIZERS_results.csv` and the report.
3. **PROMPT.md.** A section "Decided since this prompt was built (added 24 Nov 2026)" goes before "## How to work",
   worded as in the 014 example:
   - step 6 is lifted for these rows;
   - a decided statement becomes background, used and rechecked in use;
   - the item becomes the next question beyond the row;
   - the main question is the strongest undecided statement;
   - other-object rows go to `LINKS.tsv`;
   - then the list of rows, and a short paragraph on where this research stands: interval generation at 105/020; the
     reverse axioms and the false replacement margin at 105/052.

   The main questions, the push paragraph, the three-hour check, the checkpoint rules and CHECK_EVENTS.tsv are unchanged.
   No minimum, way out or cheaper alternative was added.

## Tests

- `push_rule_pro_prompts.py --lint-math PROMPT.md`: `files: 1 failing lint: 0` for each of the four.
- Each ZIP opens, `testzip()` reports no bad member, and none holds a ZIP.

| ZIP | Members | Bytes |
|---|---:|---:|
| 027 | 319 | 26.3 MB |
| 081 | 309 | 9.8 MB |
| 135 | 315 | 23.1 MB |
| 189 | 310 | 10.5 MB |

## Notes

- **The 081 prompt.** Its only row is A.1 at 105/045. Its closing paragraph on 105/020 and 105/052 is context: those
  pages are not among its scans.
- **Statements in `SETTLED.tsv`.** They are the run's register statements, some of them short titles. The full
  statements are in the attached sections.
- **Scripts.** In my scratchpad: `find105.py`, `build105.py` and `decided105.py`, Python, run with `-I -B`.
