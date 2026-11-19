# Horizontal sweep 2, part 2: final check-in of the broad agent

By a0c4bb37 (Claude Opus 5.5 at effort max), 18 Nov 2026, 22:26 UTC. I merged all four deep agents (part 2) and my three sub-agents, rebuilt GLOBAL, WHAT_IS_WHERE.md and the check register, and built the neglect table.

## Final counts
- **Coverage:** 17,394 notes entries (3.09M words, without the doubts files). 17,259 are placed and 135 linked; 0 are unplaced. The doubts files (4,558 entries) are joined to items by scan: 2,174.
- **Placements:** 18,145 rows. 13,783 rest on the index, heading or folder; 4,221 on reading the entry or its opening; 141 on the passage.
- **Map:** 873 items and 793 objects (H tags). 64 objects lie in more than one topic. There are 56 themes, 3 strands (TH-C93, TH-C109, TH-CRYS) and 2 hand joins (H0HW, the five-point problem; H037, cote 100).
- **Records:** 362 flags; 296 corrections in sweep2/SA<nn>/CORRECTIONS.tsv; 29 reports in sweep2/REPORTS/.
- **Interlinks, by shared pages:**
  - 2,652 item-unit links;
  - 3,270 item-statement links;
  - 640 item uses through EDGES;
  - 447 links from claims of his to statements.

  The topic agents' own dependency readings add 796 rows, which give 302 objects a "uses" link.
- **Check events:** 457 in sweep 2 (the topic files, plus GLOBAL/CHECK_EVENTS_broad.tsv with my 6).
- **The register:** 25,994 checks on 9,175 ids, from 62 files.
  - No sweep row is counted twice. I removed the copied sweep-1 rows again, 9 of them, after the agents' re-runs, and the dedupe now also drops rows written twice within a sweep-2 file.
  - The only duplicates left are 5 rows inside results_register/checkedness/CHECKEDNESS_EVENTS.tsv, which is not a sweep file.

## Settled from the deep agents' part-2 check-ins
- **a28ea31fa17dd65e1:**
  - H046 (SA05-18 = SA06-9) and H045 (SA05-19 = SA06-8) are joined.
  - ANABELIAN_A1_SUCCESSOR:B.111-B.118 cite "cote 14, scans 003, 007, 011, 041" (paper l. 16729). I read MPL_14_002-044 on those scans and found no anabelian content, so the citation is misplaced. It is left out of every link (GLOBAL/MISPLACED_REGISTER_PLACES.tsv), and crystals_dieudonne_motives.md is corrected: no research statement sits on those pages.
  - The pointer regex read item ranges such as "SA20-12/13" as cote/scan. It is fixed, and 4 false pointers are gone.
- **ae4ae3dc17acaa440:** the control runs CTRL-145 and CTRL-148 count in SA29 and SA31 (OWNER_OVERRIDES.tsv). Coverage moved accordingly: SA28 481, SA29 396, SA31 623.
- **a34c04448e8299803:** its re-run duplicates are removed. 159/20 is decided in REPORTS/H03F_projective_connections.md (his slip).

## The neglect ranking (GLOBAL/NEGLECT.md)
- **22 of 32 topics have no research-run statement on their pages.** From least to most researched, ties broken by transcribed pages:
  - SA04 (1,611 pages), SA21, SA23, SA05, SA13, SA01, SA08, SA12, SA14, SA02, SA07;
  - SA16, SA18, SA15, SA03, SA06, SA09, SA19, SA11, SA22, SA27, SA26.
- **Then the topics with few statements:** SA17 (1), SA10 (6), SA20 (25), SA24 (26), SA29 (35), SA25 (32), SA30 (85).
- **The research sits in three places:**
  - SA32 (601, Les Dérivateurs, counted at topic level until the cote-157 scan concordance exists);
  - SA31 (970) and SA28 (1,072), the cotes around La Longue Marche;
  - La Longue Marche itself (cote 140, 855 places), which is not one of the 32 topics.

## Still open
- 29/125: the month of the Serre letter cannot be read, 6 or 8.
- F01: the printed EGA 0_IV 22.5.10(i) is not in the archive.
- 156-4 to 156-9 need a mathematical reading; there are no Work notes.
- H024 against H0LN: one programme or two stages?
- H0HW: check that SA22-7 belongs.
- The cote-157 scan concordance.
- The 4,558 doubts entries are not read.
- The misplaced ANABELIAN citation is in the register's source.
- The topic agents' open readings are in their part-2 check-ins.
