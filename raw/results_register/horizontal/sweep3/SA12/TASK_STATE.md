# SA12, sweep 3, wave 1: task state (lead a65dbdc241d1a129a, Claude Opus 5.5 at effort max)

If I am compacted, my summary is not reliable. To resume:
1. Reread `sweep3/WAVE1_LEAD_BRIEF_20261119.md`, `sweep3/READER_BRIEF.md`, `sweep3/PROMPT_BUILD_BRIEF.md` and this file.
2. Read the files in `sweep3/SA12/` and `sweep3/SA12/readings/`.
3. Go on from the first step below that is not done.

## The launch (coordinator, 19 Nov 2026, about 13:40 UTC)
- I lead SA12: 469 transcribed pages, rank 8 of the least studied.
- Sub-agents allowed: 2 readers (Claude Opus 5.5 at effort max, about 300k each). My own bound is about 250k.
- Backup: `field_experts/agent_backups_20261119/a65dbdc241d1a129a_before_sweep3_wave1_20261119/`.

## Pages (469), by the tool `sweep3/SA12/_tools/readtex_sa12.py <cote> <first> <last>`
| cote | pages | sources |
|---|---|---|
| 29 | 213 | Pro MPL_29_049-094, MPL_29_095-140, MPL_29_141-187 (final folders); Codex A29-01, C29-01..07, K29-01..11 |
| 31 | 93 | Pro MPL_31_002-051; Codex K31-01..03 |
| 33 | 96 | Pro MPL_33_002-049, MPL_33_050-097 |
| 37 | 55 | Codex B37-01..05, H37-01 |
| 32 | 8 | Codex C32-01 |
| 35 | 4 | Codex H35-01 |

## The split
| stretch | who | pages |
|---|---|---|
| c29a: cote 29 scans 2-140 | reader A | 136 |
| c29b_c31: cote 29 scans 141-217, then cote 31 scans 2-102 | reader B | 77 + 93 |
| c33_c37: cote 33 scans 2-97, then cotes 37, 32, 35 | me, the lead | 96 + 67 |
| REVISED 14:35 UTC: c31_lead = cote 31 scans 2-102, read by me first (B's interrupted share). Then cote 33 as far as the budget allows. 29/188-217 and cotes 37, 32, 35 stay unread in sweep 3 (placed in sweeps 1-2) | me | 93 (+ cote 33) |

## Steps
- [x] 1. Briefs read; tool written; pages counted (13:45 UTC).
- [x] 2. Readers launched at about 13:47 UTC.
  - Reader A (c29a, agent a203d72bad105bea5, Claude Opus 5.5 at effort max) FINISHED at 14:32 UTC: 138 scans read, 52 check events, 11 corrections, 8 hunches; it used 460k tokens.
  - Reader B (c29b_c31): its Agent call was "interrupted by user for tool use"; its last file write was at about 14:12 UTC and the interruption is recorded at 14:26 UTC. It had written c29b_c31.md through 29/187, items 1-11. Unread: 29/188-217 and all of cote 31.
  - B is NOT resumed: the user interrupted that call. The report says so, so that the coordinator can decide.
- [x] 3. My own reading: `readings/c31_lead.md` (cote 31, scans 2-102, all 93 pages), with `c31_lead_CHECK_EVENTS.tsv` (16) and `c31_lead_CORRECTIONS.tsv` (8), written about 14:39 UTC. Compacted after it.
  - Cote 33 NOT read: my bound (~250k) is spent. Cote 33, cotes 37, 32, 35 and 29/188-217 (191 pages: 28 + 96 + 55 + 8 + 4) are listed as unread in STUDY.md, for the coordinator to give to a reader.
- [x] 4. Merged (about 15:00 UTC): STUDY.md, HUNCHES.md (H1-H18), RESEARCH_PACKAGES.md (RP-SA12-1..4), DELIVERABLES.tsv (17 rows), DEPENDS.tsv (34), CORRECTIONS.tsv (21), CHECK_EVENTS.tsv (92), by `_tools/merge_sa12.py` and `_tools/tables_sa12.py`.
- [x] 5. The research prompt, built 15:12 UTC by `_tools/build_research_prompt_sa12.py` (body and file list in `_tools/research_prompts/`); both lints pass; linked and packed into `TO_SEND/PRO/1_Archive_research_by_topic/16_SA12_SGA_cd_of_affines_and_pi1_cotes_29-31_night` (PROMPT.md + one ZIP of 1.46 MB); line 16 added to ORDER.md. In `pro_prompt_builds/RESEARCH_SA12/`:
  - lint `--lint-math`;
  - pack;
  - link into `TO_SEND/PRO/1_Archive_research_by_topic/<n>_SA12_<short>_night`;
  - add its line to ORDER.md.
- [x] 6. Report to the coordinator: the final message of agent a65dbdc241d1a129a, about 15:16 UTC.

## Readers
- A (c29a): a203d72bad105bea5, finished.
- B (c29b_c31): agent a3c8d7ded052a745e (Claude Opus 5.5 at effort max, from its meta.json), interrupted by the user at 14:26 UTC ([the user's words, omitted]) after writing through 29/187.

## Coordinator's follow-up (19 Nov, about 15:30 UTC): reader B's stretch 29/188-217 merged
- [x] Merged: STUDY.md (header counts, new §15A and §15B, §12 and §15 notes, the corrections list), HUNCHES.md (H18 revised, H19-H23), CHECK_EVENTS.tsv (106), CORRECTIONS.tsv (24), DEPENDS.tsv (40), DELIVERABLES.tsv. Cotes 29 and 31 are read in full; unread: cotes 33, 37, 32, 35 (163 pages).
- [x] Prompt body updated (results 13, 22-27; leads L7-L10; parts D.7 on 29/207 and D.8 on G5; Rydh and the log-étale sources), rebuilt, both lints pass, send folder relinked and repacked at 15:37 UTC (PROMPT.md 41,642 bytes, one ZIP of 1.47 MB); ORDER.md line 16 updated. Not sent.
