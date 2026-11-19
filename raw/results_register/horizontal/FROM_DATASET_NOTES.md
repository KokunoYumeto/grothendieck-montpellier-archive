# Notes on the organization, from building the dataset

Written by the dataset agent (Claude Opus 5.5 at effort max), while building
`KokunoYumeto/grothendieck-programme-algebraic-geometry` v2 (work folder `training_data_20261118\`). What connects to
what, duplicates, gaps, misplacements, objects to merge or split. Each batch is dated; the numbers are from the build
scripts (`training_data_20261118\tools\`), not from reading.

## Batch 1, 18 Nov 2026 ~16:3x UTC

### Gaps in the results register
1. `REGISTER.tsv` (built 14:06) lags the returns. Newer returns on disk now: SECTION_GHOSTS final 20261118T1305Z
   (register: checkpoint 7), FREX final 20261118T1235Z (register: checkpoint 10), S6_06_BLIND checkpoint 35
   (register: 33). A rerun of `build_register.py` picks them up; the dataset reads the newest return itself.
2. LM3_TEICHMULLER_TOWER (110 statements) and LM3b_TEICHMULLER_PUSH (93) are in no register: their returns are only
   in the published `grothendieck-longue-marche/raw/pro_returns` (sparse clone in `training_data_20261115\src\`), not
   in `longue_marche_pro_pilot_20261104\answers\`, so `build_check_ledger.find_returns()` misses them. The dataset
   takes them from the published copy (one-line statements only: the clone has no LaTeX for them).
3. Statements whose LaTeX is not in the return folder, so only their one-line statement is in the dataset:
   - LM4_SUCCESSOR (401): `where_proved` names `work_A/*.tex` etc.; checkpoint 40 keeps those files only inside
     `historical_documents.tar`.
   - S6_06_BLIND checkpoint 35 (296): `S6_06_BLIND_paper.tex` is a 5.7 KB stub; `where_proved` names `notes/part1.tex`,
     which is not in the checkpoint.
   - DELTA_ON_GT (134 of 221 not located) and S2COUNT (53 of 85): their statements sit in agent working files under
     other ids.
   In all, 6,4xx of 7,259 statements were located in their return's LaTeX and 5,7xx have a proof or refutation.

### Check register
4. 793 events of `CHECK_REGISTER.tsv` name the checker as "Claude Fable 5.2 at the session's default effort (none
   set at launch)": the default's value is not given (AGENTS.md: say where it came from and what it was). Three name
   "GPT-6 Astra Pro; current run" (the dataset maps these to GPT-6 Astra (ChatGPT Pro mode)).
5. Of 25,494 check events (register + French-school + second-pass verdicts), 20,0xx name a row of the dataset; the
   rest name statements of runs not in the register (S6_09_PAPERS 1,153 and S6_10_PAPERS 1,449 lineage members,
   FINMON 603), so those runs' papers have no statements table the register reads.

### Ids of the notes (sweep 1)
6. The sweep uses three id forms for Pro notes: the n-th `###` section (`<pkg>#<n>`, stage A); the heading's own
   label in files without `###` (`MPL_137_002-044#R001`); and sub-entries inside one `###` section
   (`MPL_29_095-140#3:N046`, where entry 3 holds notes N046-N050). The dataset follows all three; sub-entries are
   attached to their entry. Worth fixing in one rule for sweep 2.
7. Work math-notes files use `#` units in some folders (K34-*, K45-02, K46-01_2, K43-05: "# What the pages do",
   ...) and `##` in others; the sweep handled both. Codex-web `_notes.md` units are `codex:<folder>#<n>`.
8. 19 of 14,395 placements name entries that no longer exist in the files: work:K161-2-06_2 (5), work:K162-5-02 (4),
   work:K147-01 (3), MPL_137_002-044 (2), work:H66-01 (2), work:K32-02, work:K123-02, codex:K162-5-02 (1 each).
   The files changed after the sweep read them, or the units were counted differently.

### Packages the sweep did not see
9. Sixteen Pro packages exist only as checkpoints, so stage A (which skips checkpoint folders) left them out of
   NOTES_INDEX and the sweep: e.g. MPL_136_328-376 (checkpoint 2: doubts only, no notes file) and MPL_15_139-194
   (checkpoint 1: `research_leads_before_context.md`, no notes file). The dataset includes what they hold.
10. Two second chats on the same scans: `MPL_15_195-228+18_002-017_chatB` (notes nested one folder down, with
    `_from_earlier_checkpoints`) and `MPL_33_002-049_chatB`. They are parallel witnesses of the same pages; the
    sweep has no row for them.
11. Codex-web folder variants: `B15-02` and `B15-02_2`, `K46-01_2`, `K161-2-06_2`, the CTRL-* controls in
    `returns_control\`: two returns of one folder. The dataset keeps every returned file; the sweep's placements
    point to one of each pair.
12. Pro packages without a notes file in the final: `MPL_1_002-050` (it has `MPL_1_002-050_pointers.md`), and the
    `_check` folders (SAMPLE_CHECK.md of Claude's page checks) are separate from their packages.

### Duplicates
13. 20 note sections are exact duplicates of others (the same text in two packages or two files), e.g. the 116
    entries of `MPL_81_038-055+154_046-076` indexed both in SA01 and SA11 (sweep flag of SA01). The dataset keeps one
    row and lists the other ids in `duplicate_ids`.
14. 220 statements share their exact one-line statement with a statement of another run (`same_statement_group`);
    the checkedness ledger's lineages (7,677) group the same claim more widely.

## Batch 2, 18 Nov 2026 ~17:0x UTC (Stacks work and parallel editions)

### Our Stacks-format work
15. Our Stacks integration lives in seven local clones of the fork: stacks-ftg (FAC, Tohoku, GAGA), stacks-ftg-fga-
    normalized (the same plus FGA, normalized), stacks-ega, and four micro branches (01kr, tohoku, fga, ftg-fga-pr).
    All sit on older upstream bases than the mirror `stacks-project`, so upstream changes show as deletions in every
    branch (moduli.tex, etale.tex, quot.tex: the same blocks in all seven). Our text is what the branches insert.
16. The two FTG branches overlap: 316 of our units occur in both (the dataset keeps the normalized branch's copy and
    lists the other). stacks-ftg has 10,530 inserted lines in cohomology.tex and 3,182 in homology.tex; the
    normalized branch keeps 162 and 89 there, so the Tohoku material was moved or cut in normalization. Which branch is
    current for which chapter is not recorded in one place.
17. The decision tables (fac/, gaga/, tohoku/, fga/ dec.csv, units.csv, map.csv; ega/ in stacks-ega) place every source
    unit against the Stacks project: FAC 661 units (189 equivalent, 179 stronger, 81 extensions, 118 new statements,
    ...). 1,761 decisions in all. They are the cross-reference between the classical sources and the Stacks tags; the
    sweep's objects could link to them by Stacks label.
18. The sidecar `mathematics-commons-stacks` registers zero overlays and three namespace leases (fac, tohoku, gaga);
    the branches are not imported into it. The D-check records (D1002-D1031) give per-unit source references and
    statuses only for 36 units.
19. The hub archive (gdrive Dump, F3_stacks_hub.7z; file list UP_20261118/lists/F1-F3_files.tsv) is mostly build and
    visual-QA machinery (00_control/session_fixes_20260910: 15.5 GB of jsonl and png). Candidate material of ours that
    is not in the branches: ALGEBRA_CONTEXTUAL_COMPANION_20260929 (974 tex), ALGEBRA_EDITORIAL_DRAFTS_20260929 (387
    tex), CORRECTION_OCCURRENCE_TRIAGE_20260922.jsonl (12 MB), MORE_ALGEBRA_INTAKE, DERIVED_INTAKE, HOMOLOGY_INTAKE.
    Not yet read; they need the archive.

### Parallel editions
20. The EGA retranslation (ega_en_retranslation_20261025) keeps French and English chunk by chunk with the same labels
    in the same order (89 of 89 chunks), so it aligns at the label level (2,887 units). Two French chunks have no
    English. The rest of our EGA English (ours/EGA_English_Global_0_IV.tex and the other languages) has no shared
    unit ids with the French yet.
21. The French-school check returns come in three layouts: Tohoku per-page files (dip/, fr/, en/), Illusie II with
    `% P. n` markers in all three layers, GAGA with a FINAL_PAGE_MAP for the French layers but an English cut by
    component with statement anchors (gaga:prop:1, ...) the French lacks. FAC and Illusie I have no page markers in
    their checkpoints; Verdier's checkpoints carry no sources. One page map per return would make all six align.
