# SA04 in sweep 3, wave 1: the lead's plan (a6d42bf6fe2b0d8a8, Claude Opus 5.5 at effort max, 19 Nov 2026)

Brief: sweep3/WAVE1_LEAD_BRIEF_20261119.md (and the coordinator's message in task_notes/P3F22_AND_WAVE1_20261119.md).
Allowance: 4 readers (Claude Opus 5.5 at effort max, ~300k each) for all of job 2 (SA04, then SA01, SA02, SA03).
Readers already used for SA10/SA21 may be resumed with SendMessage for later stretches (a resume is not a launch).

## Where SA04's texts are
- Pro packages (transcription.tex, notes.md, doubts.md): results_register/horizontal/inputs/SA04/pro/
  MPL_93_047-091 (cote 93 scans 47-91), MPL_93_221-236+161-5 (cote 93 scans 221-236 and cote 161-5), MPL_98 (cote
  98), MPL_8_079-081+9+4+100 (cote 100 part). Full returns also in grothendieck_archive_transcription_20261110/returns/.
- Codex-web / Work K-folders: grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K<cote>-<nn>/out/
  (K..._transcription.tex, notes, doubts). Counts of done folders: K69 7, K70 8, K72 7, K73 2, K74 8, K76 4, K77 10,
  K78 9, K79 19, K80 4, K82 5, K83 14, K84 12, K85 7, K86 2, K87 3, K88 1, K89 2, K93 13, K94 2, K97 1, K100 4,
  K101 3, K102 1, K161-1..6 17. (Cotes 83-84 and some 93 overlap SA01/SA03: check sweep2/SA04/WHAT_IS_WHERE.md.)
- Scans: grothendieck_archive_montpellier/<folder>/<cote>.pdf (scan N = PDF page N).
- Maps: sweep2/SA04/WHAT_IS_WHERE.md (40 items SA04-1..), sweep2/SA04/TOPIC_NOTES.md, sweep1/SA04/.
- Reader method: sweep3/_tools_a6d42bf6/READER_BRIEF.md (written for SA10/SA21; the method applies; paths above).

## Stretches (reader -> stretch)
- R1: cote 93 crystals and p-adic representations: MPL_93_047-091, MPL_93_221-236+161-5, K93-*, K161-*.
- R2: cotes 94-102: descent, local cohomology (1958), Pour EGA VI (102), Hilbert schemes, Chern classes: MPL_98,
  MPL_8_079-081+9+4+100 (cote 100 part), K94-*, K97-*, K100-*, K101-*, K102-*.
- R3: cotes 69-74 (graphs, polygons and polyhedra over rings): K69-*, K70-*, K72-*, K73-*, K74-*.
- R4: cotes 76-79 (quadratic forms, orthogonal groups, pinned realizations): K76-*, K77-*, K78-*, K79-*.
- Unassigned (list as unread unless a reader has room): cotes 80-89 (K80, K82-K89).
## State
- [ ] readers launched/resumed  - [ ] merged into sweep3/SA04/  - [ ] prompt built  - [ ] report

## State, 19 Nov ~14:0x UTC
- R1 done: agent a0399c97cde963d2d (Claude Opus 5.5 at effort max), 377k tokens used; files readings/cote93_crystals*
  (27 check events, 13 corrections, 7 decided on scans; unread: 161-5 scans, the Pro notes of MPL_93_221-236+161-5,
  K161-1..4 and K161-6, Hua's project).
- The guard refused R2-R4 ("your brief allows 4 sub-agents and you have launched 4"): it reads the allowance line
  "Sub-agents allowed: 4" of the coordinator's job message, not the later "Sub-agents allowed: 16" (delivered inside a
  system reminder). Asked main to launch R2-R4 or re-send the allowance; meanwhile R1 is resumed for R2's stretch.
- The R2, R3, R4 launch prompts are in sweep3/SA04/READER_PROMPTS_R2-R4.md (verbatim).
- 19 Nov ~14:4x UTC: ALL READINGS IN. R1 (a0399c97cde963d2d): cote93_crystals*, cotes94-102* (18 events, 4 corrections;
  Pro/K100 diverge on 100/003, 009, 027, 030, 046, 051: scans to decide). R3 (a5723c09c05df9eda): cotes69-74* (read 69
  and 70 except 70/119 end-125; 72-74 NOT reached; 25 events, 19 corrections). R4 (a774f5c4e87a59ea4): cotes76-79*
  (76-78 full, 79/1-30 only; 79/31-297 NOT reached; 33 events, 22 corrections; only 76/7 viewed on scan).
  Unread: 70/119-125, cotes 72-74, 79/31-297, cotes 80-89 (K80, K82-K89), K161-1..4 and K161-6.
  NEXT: merge (tables + STUDY/HUNCHES/PACKAGES from the _INTEGRATION.md files), then the prompt, then SA01-SA03.
- 19 Nov ~14:5x UTC: first merge done (merge_wave1.py SA04 _STUDY_HEADER.md): CHECK_EVENTS 103, CORRECTIONS 58, DEPENDS 58,
  DELIVERABLES 19; STUDY/HUNCHES/RESEARCH_PACKAGES written from the four _INTEGRATION.md files. Readers resumed for
  the unread stretches: R3 (a5723c09c05df9eda) 70/119-125 + cotes 72-74; R4 (a774f5c4e87a59ea4) 79/31-297; R1
  (a0399c97cde963d2d) cotes 80, 82-89 + K161-1..4, -6 + the six cote-100 divergences (scans 3, 9, 27, 30, 46, 51).
  NEXT when they report: update _STUDY_HEADER.md (unread list), rerun merge_wave1.py, build the prompt
  (sweep3/PROMPT_BUILD_BRIEF.md; my builder _tools_a6d42bf6/build_research_prompt.py), lint, link + pack into
  TO_SEND/PRO/1_Archive_research_by_topic/<next>_SA04_<short>_night, add ORDER.md line; report SA04 to main; then
  SA01, SA02, SA03 (reuse R1, R3, R4 by SendMessage; they compact and go on).

## The next three topics (sources from inputs/SA0n/ and sweep2/SA0n/WHAT_IS_WHERE.md)
- SA01 (518 pages): cote 72 (pinned regular realizations; Pro MPL_72_035-081, K72-01..07), cote 83 (2x2 matrices,
  traces, quadratic algebras, Azumaya; Pro MPL_83_178-222, K83-01..14), cote 81 + 154/46-76 (immersions of the disc,
  pseudolines; Pro MPL_81_038-055+154_046-076 shared with SA11; J81-01..07), cotes 71 and 75 (plane polygons,
  Contou-Carrere's Jordan manuscript, DEA course), cote 93/92-134 (projective connections, Schwarzian, uniformization;
  K93-13). NB: R3's cotes 72-74 stretch for SA04 covers cote 72 too: reuse its reading for SA01.
  Readers: R1 -> cote 83 + 93/92-134; R3 -> cote 72 (already) + 71, 75; R4 -> cote 81 (+154/46-76 note).
- SA02 (343 pages): cote 84 (quadratic algebras, products, chi-split extensions; Pro MPL_84_097-145, MPL_84_146-193,
  K84-01..12), cote 90 (KG(X) over a Dedekind ring; EGA IV henselization typescript; MPL_90+91_002-018, K90-01), cote
  91/2-18 (Hom functors, Greenberg-Neron; K91-01). Reports: sweep2/REPORTS/cote84_*.md.
- SA03 (269 pages): cote 91/19-143 (lifting, obstructions, representability of Hom/Isom/Aut, descent, Greenberg
  functor; Pro MPL_91_019-058, _059-098, _099-143, K91-02..10), cote 93/2-60 and 135-220 (genus-one curves in char p,
  Hasse-Witt, Cartier, Gauss-Manin, Schwarzian, p-curvature, Dieudonne crystals; Pro MPL_93_002-046, K93-01..12).
- 19 Nov ~15:5x UTC: R1 reported cotes 80-89 (survey only) + the six cote-100 scans (decided); R3 finished cotes 70, 72,
  73, 74 in full (74/119-136 in a third pass). R1 resumed for SA01 (cote 83, 93/92-134) in full, then SA04 80-89 in full;
  R3 resumed for SA01 (cote72_INTEGRATION.md, cotes 71, 75). R4 still on 79/174-297.
- PROMPT SCOPE DECIDED (19 Nov ~16:0x UTC): RESEARCH_SA04 = A. his arithmetic theory of regular polytopes (70, 72,
  76-79; A.1 main = the programme of 70/122-123), B. graphs/nets/incidence (69, 74, 80, 85-89), C. chi on E_infinity
  (93/55-66), D. the 1958 notes (101). LEFT OUT, because asked elsewhere: cote 100 (RESEARCH_SA15 Part C, running;
  R1's new cote-100 ink decisions and the equal-characteristic qualification of the Baire argument are FOR THE SA15
  INTAKE); 161-5 (RESEARCH_SA23 Part J, unsent: our R6 rank-one answer and the slope lead bear on it: TELL MAIN);
  cotes 94, 97, 98 (working-through objects H035, H036, H02M). MOVED TO SA03's PROMPT (one cote-93 char-p cluster):
  P93-2 (char-p Schwarzian, 93/72-84 with 93/123-124) and H93-4 (torsor device 93/234-236 vs Deligne-Illusie).
- Builder generalized (spec may set BROAD, EQUIV, EDGES, EXAMPLE_ID, ROLE); backup build_research_prompt.py.before_wave1_20261119.
  Trial build passes both lints (study 0.24 MB + broad 0.13 MB + transcriptions 2.2 MB).
- 19 Nov ~16:2x UTC: SA04 DONE except the full reading of 80, 82, 85-89, 161-6 (R1, after SA01). R4 finished cote 79 in
  full (51 events, 29 corrections). Final merge: CHECK_EVENTS 165, CORRECTIONS 89, DEPENDS 90, DELIVERABLES 31 (with
  translate_to/why: add_translation_targets.py, PREFIX rules for SA04). Prompt built (pro_prompt_builds/RESEARCH_SA04/,
  both lints pass), linked + packed: TO_SEND/PRO/1_Archive_research_by_topic/18_SA04_Regular_polytopes_over_rings_cotes_
  69-89_93_101_night (PROMPT.md 33.9 KB + one ZIP 2.6 MB; packed lint passes); ORDER.md line 18 added.
  When R1's full 80-89 reading lands: re-merge, rerun add_translation_targets.py, rebuild, relink (remove the two send
  files, link, pack) IF the prompt is not yet sent (check SENT_PRO.tsv / the folder name).
- SA01 readers: R1 cote 83 + 93/92-134 in full; R3 cote72_INTEGRATION + cotes 71, 75; R4 cote 81. SA01/readings/cote72_*.tsv
  copied from SA04 (copy_cote_rows.py). NEXT: merge SA01 when the three report; SA02 (R4: cote 84 natural, after 77),
  SA03 (R1: 91, 93/2-46, 135-220 + SA04's P93-2, H93-4).
- 19 Nov ~16:3x UTC: found the STAGE-A topic dossiers (GPT-6 Astra, ChatGPT Pro mode) of the same catalogue topic, parts
  1-4 = our SA01-SA04 (inputs/SA0n/SOURCE.txt): returns in grothendieck_archive_transcription_20261110/
  stage_a_20261118_sent/returns/: SA04_v2_final_20261119T0323Z (part 4 = cotes 93, 98, 100, 161-5; claims C-SA04-n,
  problems, directions); SA02_final_20261118T1145Z (v1, provisional) + SA02_part2_checkpoint_01_20261119T1355Z;
  SA03_part3_checkpoint_01_20261119T1355Z; SA01: none yet. SA04's prompt now attaches SA04_dossier.md, _directions.md,
  READ_ME.md (study/stage_A_dossier_SA04_v2/) and cites its chi claims in R10; relinked + repacked (relink_one.py),
  PROMPT.md 34.5 KB + ZIP 2.67 MB, packed lint passes. FOR SA01-SA03: read their stage-A dossier returns first.
- OVERLAPS TO RESPECT in the SA01-SA03 prompts (working-through objects in TO_SEND/PRO/F_Archive_working_through_200,
  from sweep2/GLOBAL/GLOBAL_OBJECTS.tsv): SA01: H00W (SA01-1 pinned realizations, cote 72; 006_OBJ_H00W_O), H01C (SA01-3,
  the invariant form; 060), H01D (SA01-4, continuants; 114, 168), H01J (SA01-38/SA02-10, KG(X), cote 90; 010).
  SA02: H01J, H01K (SA02-11, EGA IV typescript in 90; 118), H01L (SA02-12, Hom functors, 91; 064, 172).
  SA03: H026 (SA03-18 connections, 93:135-207; 042, 069, 096), H028 (SA03-2; 015), H02A (SA03-3; 123), H02B (SA03-4;
  177), H02D (SA03-6; 150). SA04's A.1 touches H00W/H01C/H01D (cote 72): A.1 asks the 70/122-123 programme for every
  type and the degeneration locus; the WT runs check his cote-72 pages. Tell main (done in the SA04 report? NO: add).
- 19 Nov ~16:5x UTC, main's side job DONE (reported): RESEARCH_SA23 Part J carries SA04-R1615-02/-03 (+K1615-01, lead
  H1615-1), study ZIP + readings/SA04_reading_161-5_excerpt.md; send folder 17_SA23 recopied + repacked (PROMPT.md 23.0 KB,
  ZIP 573 KB; both lints pass); ORDER.md line 17 updated. Seven WT prompts (006 H00W, 060 H01C, 114 H01D-1, 168 H01D-2,
  055 H036, 109 H02M-1, 163 H02M-2) got the "Sweep-3 results on these pages." paragraph after the Space marker (CRLF kept,
  bytes before the marker identical; --lint passes); backups in scratchpad sa04/wt_backups/.
  NEXT: SA01 merge when its three readers report (wait btll52hjr).
