# SA23, sweep 3 wave 1: task state

**Lead:** agent a3d30d2d3a27966ed (Claude Opus 5.5 at effort max). It swept SA23 in sweeps 1 and 2.

**Brief:** `results_register/horizontal/sweep3/WAVE1_LEAD_BRIEF_20261119.md`. Readers follow `READER_BRIEF.md`; the prompt is built by `PROMPT_BUILD_BRIEF.md`.

**Restart.** The first run (from about 13:39 UTC, 19 Nov) stalled before writing anything. This restart began at 13:55 UTC.

## The pages (Pro and Codex transcriptions; about 610 pages, the NEGLECT count is 604)
| cote | pages | source | stretch |
|---|---:|---|---|
| 1 | 142 | Pro MPL_1_002-050 (scans 3-50), Codex K1-01..K1-07 (51-150); HC1-01 a second witness for 4-40 | B |
| 2 | 41 | Pro MPL_2 | B |
| 21 | 27 | Codex K21-01, K21-02 | B |
| 161-1 | 15 | Codex K161-1-01 | A |
| 161-2 | 99 | Codex K161-2-01..07 | A |
| 161-3 | 46 | Codex K161-3-01..03 | A |
| 22 | 29 | Pro MPL_22+23_002-016 (Codex K22 a second witness) | C (lead) |
| 23 | 91 | Pro scans 2-16; Codex K23-01..06 (17-99) | C |
| 26 | 10 | Codex H26-01 | C |
| 161-4 | 28 | Codex K161-4-01, -02 | C |
| 161-5 | 27 | Pro MPL_93_221-236+161-5; scans 3-22 are Serre's printed papers (reused) | C |
| 161-6 | 28 | Codex K161-6-01, -02 | C |
| 162-1, 162-5, 162-6 | 9, 12, 5 | Codex H162-01, K162-5-01/02, H162-02 | C |

**Outside the 604:** the API transcriptions of cote 24 (EGA V in English, 76 pages), cote 25 (Nouveau EGA V, 184 pages) and the 162-5 typescript of the tapis (51 pages). They are listed as unread stretches unless budget remains.

## State
- [x] Reader A (aac7b158968982dd2), cotes 161-1 to 161-3: all 160 pages read; 74 check events, 18 corrections, 11 hunches (14:4x UTC).
- [ ] Reader A, resumed at 14:5x UTC for a second stretch, A2: cotes 161-4, 161-6, 162-1, 162-5, 162-6 (82 pages): readings/A2_161-4_161-6_162.*
- [ ] Reader B (acadc29d15e8e7c65), cotes 1, 2, 21: 138 of 210 pages read; resumed at 14:5x UTC for the rest (cote 2 scans 2-20 and 23-45, cote 21, cote 1 scans 140-145 and 149-150)
- [x] Lead, stretch C: cotes 22, 23, 26 and 161-5, all read (16:2x UTC): readings/C_22_23_26_161-5.* (19 check events, 4 corrections)
- NOTE (16:2x UTC): the lead's context passed 70 %. Next: merge mechanically (scripts), write STUDY.md from the readings and the readers' final reports, then build the prompt by PROMPT_BUILD_BRIEF.md. If compacted, the summary is not reliable: reread this file and the brief.
- [x] Merge done once (16:03 local): STUDY.md, HUNCHES.md, RESEARCH_PACKAGES.md, DELIVERABLES.tsv, DEPENDS.tsv, CORRECTIONS.tsv, CHECK_EVENTS.tsv. Rerun scratchpad merge3.py when readers B and A2 finish; STUDY.md then needs their findings. OLD LINE:, HUNCHES.md, RESEARCH_PACKAGES.md, DELIVERABLES.tsv, DEPENDS.tsv, CORRECTIONS.tsv, CHECK_EVENTS.tsv
- [ ] Research prompt: pro_prompt_builds/RESEARCH_SA23/, linted, packed into TO_SEND/PRO/1_Archive_research_by_topic/, with its line in ORDER.md

## 16:1x local, 19 Nov
- **Reader A2 done.** 79 pages, 25 check events, 17 corrections.
- **Prompt built and linted.** `pro_prompt_builds/RESEARCH_SA23/`, with PROMPT.md and two ZIPs; README beside it.
- **Open: reader B.** acadc29d15e8e7c65 was still running for cote 2, cote 21 and cote 1 140-150. When it finishes: rerun merge3.py and build_prompt.py, and add its findings to STUDY.md.
- **Open: TO_SEND.** The wave-1 brief asks to link the prompt into TO_SEND/PRO/1_Archive_research_by_topic as 15_SA23_..._night, with a line in ORDER.md. PROMPT_BUILD_BRIEF says the main session links and never to write into TO_SEND. Not done: left to the main session.
- **Reader B done** (210 pages, 72 events, 31 corrections). Merged and rebuilt; lint passes. Remaining for the main session: link the prompt into TO_SEND.
