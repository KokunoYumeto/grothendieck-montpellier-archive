# Sweep 3 log of ae4ae3dc17acaa440 (Claude Opus 5.5 at effort max): SA22 and SA20 (the teaching notebooks and the Esquisse dossier)

The brief is the coordinator's message of 18 Nov, about 22:2x UTC (sweep 3). Outputs go to `sweep3/SA22/` and
`sweep3/SA20/`: STUDY.md, HUNCHES.md, RESEARCH_PACKAGES.md, DELIVERABLES.tsv, DEPENDS.tsv, CORRECTIONS.tsv and
CHECK_EVENTS.tsv. After a compaction: reread the brief (quoted at the top of each STUDY.md) and these files, then go on.

## Who reads which pages (for a6d42bf6fe2b0d8a8, stratifications and forms)

**I read:**
- SA22: cotes 66, 67 and 68, with 162-1 and 162-6.
- SA20, minus tame topology:
  - cote 119, the Esquisse dossier (SA20-2 to SA20-6);
  - cote 152, plane trees (SA20-7): the 152 part of MPL_152+120;
  - cotes 153 and 155, analysers and the Tannakian duality (SA20-16, SA20-17): the 153 and 155 part of
    MPL_121_049-073+153+155;
  - cote 122 (SA20-18, SA20-19);
  - cote 123 (SA20-W1, W3, W4: folders K123-01..03 and C123-01..02);
  - cote 125 (SA20-W2).

**I leave to a6d42bf6:** tame topology, cotes 120 and 121.
- These are SA20-12 to SA20-15, and the four prompted questions SA20-8 to SA20-11 (tubulure and ombre, the remords,
  o-minimal axioms, comparison of tame theories).
- In packages: the 120 part of MPL_152+120, MPL_121_001-048, and the 121 part of MPL_121_049-073+153+155.

If a6d42bf6 has already started on any of my pages, it keeps them; please write that here or in your own check-in, and
I will skip them.

## Plan (22:23 UTC)

1. SA22, cote 66 (four sheets).
2. SA20, cote 123 (the Kostant and Steinberg folders and the letter), with a check of the Steinberg and Brieskorn
   references against the papers where they are open.
3. SA22, cote 67: the 1976–78 layer, then the 1983–84 layer.
4. SA22, cote 68 with 162-1 and 162-6.
5. SA20: 122, then 153 and 155, 119, 152, 125.

Each stretch is written to the files as soon as it is read.

## Progress

- about 22:28 UTC: cote 66 done (SA22: STUDY §1, HUNCHES H22-1..5, R22-1).
- 22:33 UTC: cote 123 done (SA20: STUDY §1, 12 check events, 6 corrections; my part-1 'agrees' on the A_3 margin is corrected: c -> c' is not injective for A_3 either). The letter's dimension conjecture is confirmed as 'Grothendieck's conjecture' by Douglass-Röhrle 2008 (arXiv:0802.0764). Next: SA22 cote 67.
- 22:42 UTC: SA22 cote 67 done (STUDY §2; CHECK_EVENTS 8, CORRECTIONS 5, DEPENDS 10, DELIVERABLES 7 rows for cotes 66-67; HUNCHES H22-6..8; packages R22-2, R22-3). Next: SA22 cote 68 with 162-1 and 162-6.
- 22:51 UTC: SA22 cote 68 done (STUDY §3; +16 check events, +9 corrections, +5 depends, +8 deliverable rows; H22-9, H22-10; R22-4). 162-1 and 162-6 are not transcribed in the package that names them. Next: SA20 cote 122, then 153/155, 119, 152, 125.
- 22:54 UTC: SA20 cote 122 done (STUDY §2; +6 check events, +3 corrections, +3 depends, +2 deliverable rows; H20-7; R20-3). Stopped here at about 95 % of the context cap: SA20 cotes 153/155, 119, 152 and 125 were NOT read in sweep 3 (their sweep-2 placement stands); SA20-19 comparisons not made.

## Readers (main session's additions, about 22:5x and 23:1x UTC: sub-agents allowed 6, about 400k context each; three at a time)

The brief for all readers is `sweep3/READER_BRIEF_ae4ae3dc.md`. Each writes only to `sweep3/SA<nn>/readings/<stretch>*`,
and I integrate their files into STUDY, HUNCHES, RESEARCH_PACKAGES and the TSVs. The registry was rebuilt first (23:2x UTC).
- **Wave 1:**
  - SA20 `119_144-161_276-281`, a new reader;
  - SA20 `121_049-073_153_155`, a new reader;
  - SA20 `152_120`: resume ac69efa38b3a951d7 (Claude Opus 5.5 at effort max), which read 152 whole and 120 scans 1-6
    in its second pass. If it cannot be resumed, a new reader.
- **Wave 2:**
  - SA20 `121_001-048`, with the prompted questions SA20-8 to SA20-11;
  - SA22 `67_003-046_084-101`, the pages I knew only through the notes;
  - SA20 `122_125`: the SA20-19 comparisons with the register rows, cote 125 (K125-01), and the image checks of the
    open readings on 122 (028, 032) and 68 (the disputed words).
- 23:19 UTC: reader 152_120 (ac69efa38b3a951d7, Claude Opus 5.5 at effort max) DONE and integrated: STUDY §3, HUNCHES and RESEARCH_PACKAGES sections, TSV rows (SA20 now CHECK_EVENTS 52, CORRECTIONS 26, DEPENDS 31, DELIVERABLES 11). Registry KNOWS and STATE_NOTES updated. Stub files of readers 119_144-161_276-281 and 121_049-073_153_155 exist in readings/ (launched from the main session); not integrated yet. Order note: STUDY sections are in the order worked (123, 122, 152/120), not the map's order (119, 152, 120-121, 153/155, 122, 123/125).

## 19 Nov, after the compaction (the main session's messages of ~02:2x and ~03:5x UTC, by their stamps; the clock read 01:18 and 02:05 UTC at the integrations)

- 01:18 UTC: readers acf08879 (119) and aff4deb1 (121/049-073, 153, 155) integrated into SA20 by script
  (`scratchpad/s2/integrate_sa20.py`).
  - SA20 STUDY.md is rebuilt in the map's order, with a state table and the main findings.
  - translate_to and why columns were added to every DELIVERABLES row of SA20 and SA22
    (knowledge/03_archive/translation_targets.md, with my own reason per row).
  - The 155 verso row was reworded: no name, vote or date of birth.
- About 01:2x UTC: wave 2 launched (READER_BRIEF updated: sub-agents 0, translate_to and why, the privacy rule). All
  three readers are Claude Opus 5.5 at effort max:
  - a9e0641820ca2be57: 121_001-048;
  - af3526fc4890c92f1: SA22 67_003-046_084-101;
  - a8afd9e2a259051c4: 122_125, with the image checks on 122 and 68.
- 02:05 UTC: all three were done and are integrated (`integrate_sa20.py`, `integrate_wave2.py`).
  - SA20 now has 7 sections (119; 152/120; 121/1-48; 121/49-73 with 153 and 155; 122; 122 against the runs with 125;
    123).
  - SA22 now has 4 sections (66; 67, mine, corrected; 67, the reader's; 68, with the image decisions).
  - Corrected in my own SA22 text:
    - the capping Conjecture (Koebe), with H22-6 and R22-2 (b) restated;
    - the orange slice;
    - the hand of the title-sheet date;
    - the Theorem of 089 in characteristic 5;
    - the direction of the SA22-4/SA22-9 dependence;
    - the words of 68.
  - In SA20: the 122 image confirmations, "dévolution", the sign, SA20-19 done, R20-3 (d) done.
  - Counts: SA20 CHECK_EVENTS 215, CORRECTIONS 101, DEPENDS 90, DELIVERABLES 38; SA22 90, 51, 25, 20.
  - Registry hand entries were added for the three readers, and the rebuild is started.
- Next: the Pro research prompts RESEARCH_SA20 and RESEARCH_SA22 (the main session, ~03:5x UTC by its stamp).
- 02:3x UTC: Pro research prompts built; `--lint-math` passes on both, and the checkpoint rule is present.
  - `TO_SEND/11_Finish_prompts/RESEARCH_SA20/`: PROMPT.md with the study, transcriptions and literature zips (SGA 7 II
    XIII-XV, our English edition). Five Parts; the main question A.1 is the collar conjecture and the cascade (119).
  - `TO_SEND/11_Finish_prompts/RESEARCH_SA22/`: PROMPT.md with the study and transcriptions zips. Three Parts; the main
    question A.1 is whether the section-6 maps of 67 are isomorphisms.
  - Faces by other people are left out of the transcription zips (122, 153, 155, 152, 119/276-281, 67/008, 68/018), and
    the name and address on 67/012-013 are removed. The Pro notes and doubts files are not attached.
  - Built by `scratchpad/s2/build_research_zips.py`.
- Found while building: H22-4 was wrong in characteristic 0. Numerical and homological equivalence agree for 2-cycles
  on complex fourfolds by hard Lefschetz, Lefschetz (1,1) and Hodge-Riemann (my sketch). It is recorded in SA22
  HUNCHES, CHECK_EVENTS and CORRECTIONS, and is RESEARCH_SA22 B.1 / L1.
