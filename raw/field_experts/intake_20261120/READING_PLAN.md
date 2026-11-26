# Reading plan for the readers at effort high (intake of 20 Nov 2026)

Sorting by Claude Opus 5.5 at effort medium, 20 Nov 2026 (the sorting step: no proof was judged). The runs are GPT-6 Astra (ChatGPT Pro mode). Scope: the research runs of `INTAKE_LEDGER.md` (built 20 Nov 18:50 UTC) section 1 (never taken in) and section 1b (taken in thinly); the SPnn, IMnn and DMnn transcription units are out of scope.

## How to use it

- Each packet is one reader's job. Its rows are in `packets/PACKET_nn.tsv` (run, row id, why it is in the packet, kind, the run's status, the proof location as file:line in the return, an estimate of the proof's length, the statement).
- A row is in a packet when it is a **main result** (named in its report's main or conclusion sections, or in its paper's abstract), a row the **programme rests on** (three or more rows of its register depend on it), a row **no intake has treated** (for the section-1 runs: every row; for the section-1b runs: rows whose id appears in none of the intake documents that mention the run; for S6_SERIES_GRIND: rows whose check record names no Claude intake), or a **bridge flag**. The full registers are in `SORTED/<RUN>.tsv`; each run's half-page is `SORTED/<RUN>.md`.
- Size: proof lines from the statement's line to the next statement of the register in the same file (at most 400; 30 where the proof was not located); about 50 lines a page. Target per packet: about 7000 lines (about 140 pages), packets kept within one field and, where possible, one run.
- Read the run's `.md` and its report first; read the proofs at the file:line given; record what you find in the run's own terms (the check-event types of the check rubric).
- LM_READERS is a reader-production job with no mathematical statements: no packet (see `SORTED/LM_READERS.md`).
- Field experts (rule of 13 Nov: use the field expert before any new agent): the ledger names a2fedc2a and ab3f12f2 (Claude Fable 5.2 at effort max) for Longue Marche and anabelian, aa7b8224 (Claude Fable 5.2 at effort max) for S6, none in the registry for the archive research runs (sweep 3) or, in the ledger's route column, for the Derivateurs rows here. Fable is on sabbatical since 17 Nov (memory: no Fable without the user's OK), so whether a packet goes to an expert or to a new reader at effort high is the coordinator's call.
- S6_SERIES_GRIND is a consolidation of the earlier S6 returns into five papers; most of its 'no intake' rows are rows whose inventory check record names no Claude intake, although their source runs were taken in. Its 22 packets can wait behind the archive research.
- Bridge flags (RH, GRH, L-zeros, Weil, Deligne's weights, motives, Tate twists) are in `BRIDGE_FLAGS.tsv` for the reader at effort max who bridges Levent Alpöge's RH/GRH result; they are also inside the packets.

## Runs sorted

| Run | Field | Section | Return sorted | Rows | Main | Open/conj. | Bridge flags |
|---|---|---|---|---:|---:|---:|---:|
| RESEARCH_SA06 | archive research | 1 | final | 246 | 138 | 1 | 114 |
| RESEARCH_SA07 | archive research | 1 | cp12 | 186 | 0 | 2 | 85 |
| RESEARCH_SA08_C3_D031 | archive research | 1 | cp08 | 112 | 29 | 3 | 1 |
| RESEARCH_SA11 | archive research | 1 | cp01 | 25 | 0 | 0 | 0 |
| RESEARCH_SA12 | archive research | 1 | cp23 | 404 | 0 | 2 | 13 |
| RESEARCH_SA14_SA19 | archive research | 1 | cp05 | 207 | 6 | 15 | 10 |
| RESEARCH_SA15 | archive research | 1 | cp37 | 1018 | 0 | 0 | 23 |
| RESEARCH_SA17 | archive research | 1 | cp12 | 271 | 0 | 2 | 1 |
| RESEARCH_SA20 | archive research | 1 | final | 267 | 20 | 2 | 2 |
| RESEARCH_SA22 | archive research | 1 | final | 159 | 5 | 0 | 8 |
| RESEARCH_SA22_run2 | archive research | 1 | final | 202 | 3 | 1 | 8 |
| RESEARCH_SA23 | archive research | 1 | final | 120 | 0 | 0 | 3 |
| S6_SERIES_GRIND | S6 | 1 | cp10 | 1588 | 34 | 8 | 30 |
| LM_READERS | Longue Marche and anabelian | 1 | cp13 | 0 |  |  | 0 |
| SECTION_GHOSTS | Longue Marche and anabelian | 1b | final | 228 | 6 | 10 | 58 |
| DER_LOCALIZERS | Derivateurs | 1b | cp08 | 100 | 29 | 6 | 0 |
| ANABELIAN_A1_SUCCESSOR | Longue Marche and anabelian | 1b | cp05 | 210 | 0 | 8 | 39 |
| LM4_SUCCESSOR | Longue Marche and anabelian | 1b | cp40 | 401 | 0 | 19 | 4 |
| GT_TOWER_CHECK | Longue Marche and anabelian | 1b | cp10 | 180 | 41 | 13 | 19 |
| ANABELIAN_A1 | Longue Marche and anabelian | 1b | cp03 | 121 | 29 | 7 | 24 |
| ANABELIAN_SUCCESSOR | Longue Marche and anabelian | 1b | final | 157 | 0 | 5 | 23 |
| FERMAT_SUCCESSOR | Longue Marche and anabelian | 1b | cp06 | 144 | 20 | 10 | 46 |
| REVLOC | Derivateurs | 1b | cp17 | 152 | 3 | 2 | 1 |
| LM8_PUSH | Longue Marche and anabelian | 1b | cp17 | 304 | 103 | 30 | 44 |
| LM7_PUSH | Longue Marche and anabelian | 1b | cp09 | 218 | 64 | 1 | 17 |
| LM4_FINITE_GROUP_ACTIONS | Longue Marche and anabelian | 1b | return | 272 | 160 | 3 | 0 |
| LM1_GROUP_SCHEMES_rerun_20261112 | Longue Marche and anabelian | 1b | return | 84 | 0 | 9 | 2 |
| RESIDUE | Derivateurs | 1b | return | 85 | 25 | 13 | 0 |

## Packets

### PACKET_01 (archive research): 49 rows, about 7015 proof lines (~140 pages)

- **RESEARCH_SA06** (final): 49 rows, `A.1a` ... `C.1n` in register order; ~7015 lines; why: no intake 49, main 16, bridge flag 13, programme 5. Main files: `sections/A_deuring.tex` (21), `agents/frobenius/part_B.tex` (12), `agents/cycles/cycles.tex` (6), `agents/cycles/positivity_consequences.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.

### PACKET_02 (archive research): 36 rows, about 7307 proof lines (~146 pages)

- **RESEARCH_SA06** (final): 36 rows, `C.1o` ... `C.3w` in register order; ~7307 lines; why: no intake 36, main 24, bridge flag 11, programme 7. Main files: `agents/cycles/cycles.tex` (7), `sections/C2_pencil.tex` (6), `sections/C3_local.tex` (3), `agents/cycles/positivity_stabilization.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.

### PACKET_03 (archive research): 39 rows, about 7285 proof lines (~145 pages)

- **RESEARCH_SA06** (final): 39 rows, `C.3x` ... `C.3bj` in register order; ~7285 lines; why: no intake 39, main 39, bridge flag 1, programme 1. Main files: `agents/real_weil/C3_positive_characteristic_boundary.tex` (1), `agents/real_weil/C3_multiplicative_divisor_quotient.tex` (1), `sections/C3_completion_algebraization.tex` (1), `agents/real_weil/C3_segre_nori_quotient.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.

### PACKET_04 (archive research): 39 rows, about 7141 proof lines (~142 pages)

- **RESEARCH_SA06** (final): 39 rows, `C.3bk` ... `C.4z` in register order; ~7141 lines; why: no intake 39, main 22, bridge flag 9, programme 5. Main files: `agents/cycles/cycles.tex` (7), `agents/frobenius/C4_additions.tex` (5), `agents/frobenius/C4_prym_addition.tex` (2), `agents/frobenius/C4_pt6_addition.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.

### PACKET_05 (archive research): 23 rows, about 7026 proof lines (~140 pages)

- **RESEARCH_SA06** (final): 23 rows, `C.4aa` ... `D.4e` in register order; ~7026 lines; why: no intake 23, bridge flag 19, main 5, programme 2. Main files: `agents/real_weil/part_D.tex` (16), `agents/cycles/cycles.tex` (5), `agents/frobenius/C4_transfer_countermodel.tex` (1), `agents/cycles/partial_fourier_correspondence.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.

### PACKET_06 (archive research): 36 rows, about 7065 proof lines (~141 pages)

- **RESEARCH_SA06** (final): 36 rows, `D.4f` ... `E.4c` in register order; ~7065 lines; why: no intake 36, bridge flag 23, main 19, programme 2. Main files: `agents/cycles/effectivity_albanese.tex` (11), `agents/cycles/walker_obstruction.tex` (6), `agents/frobenius/part_E2.tex` (5), `agents/cycles/saito_filtration.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.

### PACKET_07 (archive research): 20 rows, about 7065 proof lines (~141 pages)

- **RESEARCH_SA06** (final): 20 rows, `E.4d` ... `E.5g` in register order; ~7065 lines; why: no intake 20, bridge flag 20, main 13. Main files: `agents/real_weil/part_E456.tex` (20). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.

### PACKET_08 (archive research): 120 rows, about 7144 proof lines (~142 pages)

- **RESEARCH_SA06** (final): 4 rows, `E.6a` ... `F.2b` in register order; ~143 lines; why: no intake 4, bridge flag 2. Main files: `agents/real_weil/part_E456.tex` (2), `sections/F_state.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA06_final_INCOMPLETE_20261119T2052Z_unzipped`.
- **RESEARCH_SA07** (cp12): 116 rows, `A.1.1` ... `E.2.11` in register order; ~7001 lines; why: no intake 116, bridge flag 44, programme 28. Main files: `RESEARCH_SA07/sections/A_elliptic.tex` (43), `RESEARCH_SA07/sections/B.tex` (16), `RESEARCH_SA07/sections/D.tex` (12), `RESEARCH_SA07/sections/C.tex` (11). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA07_checkpoint_12_20261119T1255Z_unzipped`.

### PACKET_09 (archive research): 57 rows, about 7277 proof lines (~145 pages)

- **RESEARCH_SA07** (cp12): 57 rows, `E.2.12` ... `F.3.26` in register order; ~7277 lines; why: no intake 57, bridge flag 30, programme 16. Main files: `RESEARCH_SA07/sections/F_audit.tex` (26), `RESEARCH_SA07/sections/E_integral_image.tex` (17), `RESEARCH_SA07/sections/F.tex` (7), `RESEARCH_SA07/sections/E.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA07_checkpoint_12_20261119T1255Z_unzipped`.

### PACKET_10 (archive research): 47 rows, about 7077 proof lines (~141 pages)

- **RESEARCH_SA07** (cp12): 13 rows, `F.3.27` ... `G.2.3` in register order; ~1850 lines; why: no intake 13, bridge flag 4, programme 3. Main files: `RESEARCH_SA07/sections/F_audit.tex` (10), `RESEARCH_SA07/sections/G.tex` (1), `RESEARCH_SA07/sections/G_arithmetic_sources.tex` (1), `RESEARCH_SA07/sections/G_history_sources.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA07_checkpoint_12_20261119T1255Z_unzipped`.
- **RESEARCH_SA08_C3_D031** (cp08): 34 rows, `AT21` ... `AT11` in register order; ~5227 lines; why: no intake 34, main 8, programme 5. Main files: `sections/A_cosimplicial.tex` (5), `sections/A_rectification.tex` (3), `sections/A_closed_boundary_cells.tex` (2), `sections/A_cotangent.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA08_C3_D031_checkpoint_08_20261119T2043Z_unzipped`.

### PACKET_11 (archive research): 50 rows, about 7059 proof lines (~141 pages)

- **RESEARCH_SA08_C3_D031** (cp08): 50 rows, `AT12` ... `B-001` in register order; ~7059 lines; why: no intake 50, main 13, programme 7. Main files: `sections/A_tail_completion.tex` (5), `sections/A_integral.tex` (3), `sections/A_paths.tex` (3), `sections/A_unresolved.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA08_C3_D031_checkpoint_08_20261119T2043Z_unzipped`.

### PACKET_12 (archive research): 95 rows, about 7043 proof lines (~140 pages)

- **RESEARCH_SA08_C3_D031** (cp08): 28 rows, `B-002` ... `A-L21` in register order; ~4052 lines; why: no intake 28, main 8, programme 2, bridge flag 1. Main files: `sections/B_lifting_audit.tex` (7), `sections/B_tail_obstruction.tex` (3), `sections/B_scaled_closure.tex` (3), `sections/B_bounded_free_flatness.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA08_C3_D031_checkpoint_08_20261119T2043Z_unzipped`.
- **RESEARCH_SA11** (cp01): 25 rows, `E1` ... `T4` in register order; ~1531 lines; why: no intake 25, programme 3. Main files: `RESEARCH_SA11/RESEARCH_SA11_paper.tex` (25). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA11_checkpoint_01_20261119T1525Z_unzipped`.
- **RESEARCH_SA12** (cp23): 42 rows, `A:basic` ... `A:principal-completion-bound` in register order; ~1460 lines; why: no intake 42, bridge flag 6. Main files: `parts/A/paper_A.tex` (22), `parts/A/A2_approximation.tex` (6), `parts/A/iwasawa_A2_post02.tex` (5), `parts/A/additions_A_post01.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`.

### PACKET_13 (archive research): 48 rows, about 7277 proof lines (~145 pages)

- **RESEARCH_SA12** (cp23): 48 rows, `A:A2-local-surface` ... `B.2o` in register order; ~7277 lines; why: no intake 48, programme 3, bridge flag 1. Main files: `parts/B/paper_B.tex` (28), `parts/A/arithmetic_A2_post04.tex` (3), `parts/A/overrings_A2_post04.tex` (3), `parts/A/topological_models_A2_post05.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`.

### PACKET_14 (archive research): 70 rows, about 7089 proof lines (~141 pages)

- **RESEARCH_SA12** (cp23): 70 rows, `L6c` ... `D:vertical-fibration-multiplicity` in register order; ~7089 lines; why: no intake 70, programme 9, bridge flag 1. Main files: `parts/D/paper_D.tex` (44), `parts/C/paper_C.tex` (15), `parts/B/paper_B.tex` (10), `parts/B/B2_regular_model_stabilization.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`.

### PACKET_15 (archive research): 86 rows, about 7100 proof lines (~142 pages)

- **RESEARCH_SA12** (cp23): 86 rows, `D:surface-map-to-curve` ... `D:quadratic-cyclic-Frobenius-witnesses` in register order; ~7100 lines; why: no intake 86, programme 16, bridge flag 1. Main files: `parts/D/paper_D.tex` (65), `parts/D/D_uniform_ramification_bound.tex` (4), `parts/D/D_tame_surface_linear_cohomology.tex` (4), `parts/C/D_p_H1_surface_post09.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`.

### PACKET_16 (archive research): 65 rows, about 7019 proof lines (~140 pages)

- **RESEARCH_SA12** (cp23): 65 rows, `D:local-complete-Lang` ... `D:exceptional-canonical-energy` in register order; ~7019 lines; why: no intake 65, programme 28, bridge flag 1. Main files: `parts/B/post09_reconstruction/D_fixed_rank_constructible_B.tex` (4), `parts/B/post09_reconstruction/D_uniform_local_representation_growth_B.tex` (3), `parts/D/D_tame_quadratic_count_candidate.tex` (3), `parts/C/D_local_cross_characteristic_H2.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`.

### PACKET_17 (archive research): 52 rows, about 7125 proof lines (~142 pages)

- **RESEARCH_SA12** (cp23): 52 rows, `D:punctured-cover-linear-energy` ... `D:controlled-one-curve-gerbe-anchors` in register order; ~7125 lines; why: no intake 52, programme 22, bridge flag 1. Main files: `parts/D/post16_research/D_Brauer_zero_projective_growth.tex` (3), `parts/C/post16_research/D_RDP_Hom_boundary_framing.tex` (3), `parts/D/post16_research/D_local_Brauer_zero_projective_growth.tex` (3), `parts/B/post17_research/D_sparse_DVR_atlas_B.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`.

### PACKET_18 (archive research): 46 rows, about 7077 proof lines (~141 pages)

- **RESEARCH_SA12** (cp23): 41 rows, `D:one-curve-unbounded-period-projective-count` ... `D:wild-swap-exact-image` in register order; ~6804 lines; why: no intake 41, programme 18, bridge flag 2. Main files: `parts/D/post20_research/D_unramified_field_semilinear_crowns_root.tex` (3), `parts/B/post21_research/D_coherent_root_sector_compression_B.tex` (3), `parts/C/post20_research/D_etale_resolution_hereditary_crowns.tex` (2), `parts/B/post20_research/D_radial_tame_cover_geometry_B.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA12_checkpoint_23_20261120T1725Z_unzipped`.
- **RESEARCH_SA14_SA19** (cp05): 5 rows, `A1` ... `B1` in register order; ~273 lines; why: no intake 5, main 3, programme 2. Main files: `sections/K.tex` (2), `sections/A.tex` (2), `work/bce/section_B.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA14_SA19_checkpoint_05_20261120T1748Z_unzipped`.

### PACKET_19 (archive research): 146 rows, about 7015 proof lines (~140 pages)

- **RESEARCH_SA14_SA19** (cp05): 146 rows, `B2` ... `H1` in register order; ~7015 lines; why: no intake 146, bridge flag 6, main 2, programme 2. Main files: `sections/K.tex` (114), `sections/A.tex` (8), `work/dgj/section_G.tex` (4), `work/dgj/section_J.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA14_SA19_checkpoint_05_20261120T1748Z_unzipped`.

### PACKET_20 (archive research): 104 rows, about 7044 proof lines (~140 pages)

- **RESEARCH_SA14_SA19** (cp05): 56 rows, `H2` ... `A2D` in register order; ~4406 lines; why: no intake 56, bridge flag 4, main 1. Main files: `sections/K.tex` (20), `sections/I.tex` (7), `sections/A.tex` (7), `sections/H.tex` (6). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA14_SA19_checkpoint_05_20261120T1748Z_unzipped`.
- **RESEARCH_SA15** (cp37): 48 rows, `A-ALG-FITTING` ... `prop:B-RD25-basechange-obstruction` in register order; ~2638 lines; why: no intake 48, programme 13, bridge flag 6. Main files: `sections/B.tex` (34). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_21 (archive research): 97 rows, about 7066 proof lines (~141 pages)

- **RESEARCH_SA15** (cp37): 97 rows, `auto:B:c83d5f781371` ... `lem:B-RD58-anti-signature` in register order; ~7066 lines; why: no intake 97, programme 31, bridge flag 4. Main files: `sections/B.tex` (97). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_22 (archive research): 117 rows, about 7083 proof lines (~141 pages)

- **RESEARCH_SA15** (cp37): 117 rows, `thm:B-RD58` ... `prop:B-RD81-Cartan` in register order; ~7083 lines; why: no intake 117, programme 19, bridge flag 1. Main files: `sections/B.tex` (117). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_23 (archive research): 99 rows, about 7211 proof lines (~144 pages)

- **RESEARCH_SA15** (cp37): 99 rows, `cor:B-RD81` ... `thm:A-all-degree-ranges` in register order; ~7211 lines; why: no intake 99, programme 2. Main files: `sections/B.tex` (87), `sections/A_integral_counterexample.tex` (6), `sections/A_injectivity_counterexample.tex` (5), `sections/A_foundations.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_24 (archive research): 149 rows, about 7008 proof lines (~140 pages)

- **RESEARCH_SA15** (cp37): 149 rows, `lem:linear-covectors-any-nil-length` ... `thm:relative-ordinarity-fails-smooth` in register order; ~7008 lines; why: no intake 149, programme 35, bridge flag 5. Main files: `sections/D.tex` (39), `sections/C.tex` (26), `sections/F.tex` (17), `sections/A_monodromy.tex` (8). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_25 (archive research): 91 rows, about 7046 proof lines (~140 pages)

- **RESEARCH_SA15** (cp37): 91 rows, `thm:quintic-char2-monodromy` ... `lem:ss-simple-pole-transvection` in register order; ~7046 lines; why: no intake 91, programme 18, bridge flag 2. Main files: `sections/A_monodromy.tex` (91). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_26 (archive research): 110 rows, about 7017 proof lines (~140 pages)

- **RESEARCH_SA15** (cp37): 110 rows, `thm:ss-product-degree-one-full-group` ... `lem:ss-tangent-triple-bridge` in register order; ~7017 lines; why: no intake 110, programme 15, bridge flag 3. Main files: `sections/A_monodromy.tex` (110). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_27 (archive research): 96 rows, about 7008 proof lines (~140 pages)

- **RESEARCH_SA15** (cp37): 96 rows, `auto:A_monodromy:2b2a821f869e` ... `lem:p-rank-one-genus-two-polar-stable-candidate` in register order; ~7008 lines; why: no intake 96, programme 14. Main files: `sections/A_monodromy.tex` (96). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_28 (archive research): 119 rows, about 7022 proof lines (~140 pages)

- **RESEARCH_SA15** (cp37): 119 rows, `rem:p-rank-one-polar-unit-certificate-candidate` ... `rem:DE-Moore-Fermat-scope` in register order; ~7022 lines; why: no intake 119, programme 7. Main files: `sections/A_monodromy.tex` (119). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.

### PACKET_29 (archive research): 119 rows, about 7025 proof lines (~140 pages)

- **RESEARCH_SA15** (cp37): 92 rows, `lem:principal-theta-Cartier-translated-square` ... `thm:ss-rectangular-all-degrees` in register order; ~5438 lines; why: no intake 92, programme 7, bridge flag 2. Main files: `sections/A_monodromy.tex` (89), `sections/A_supersingular_rectangular_ranks.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped`.
- **RESEARCH_SA17** (cp12): 27 rows, `A:NR-counterexample` ... `A4:boundary` in register order; ~1587 lines; why: no intake 27, programme 4. Main files: `RESEARCH_SA17/sections/A.tex` (9), `RESEARCH_SA17/sections/A_gluing.tex` (4), `RESEARCH_SA17/sections/A_finish_localglobal.tex` (4), `RESEARCH_SA17/sections/A45.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped`.

### PACKET_30 (archive research): 105 rows, about 7016 proof lines (~140 pages)

- **RESEARCH_SA17** (cp12): 105 rows, `A4:boundary-gate` ... `C:squarezero_intrinsic_criterion` in register order; ~7016 lines; why: no intake 105, programme 11, bridge flag 1. Main files: `RESEARCH_SA17/sections/C.tex` (29), `RESEARCH_SA17/sections/B.tex` (21), `RESEARCH_SA17/sections/A45.tex` (10), `RESEARCH_SA17/sections/D.tex` (7). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped`.

### PACKET_31 (archive research): 69 rows, about 7046 proof lines (~140 pages)

- **RESEARCH_SA17** (cp12): 69 rows, `C:ramified_squarezero_criterion` ... `C:Om-finite-base-form-example` in register order; ~7046 lines; why: no intake 69, programme 11. Main files: `RESEARCH_SA17/sections/C4_finish.tex` (6), `RESEARCH_SA17/sections/C_finish_artinian_perfect.tex` (6), `RESEARCH_SA17/sections/C_finish_C1_fields.tex` (5), `RESEARCH_SA17/sections/C_finish_complete_finite_residue.tex` (5). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped`.

### PACKET_32 (archive research): 51 rows, about 7055 proof lines (~141 pages)

- **RESEARCH_SA17** (cp12): 51 rows, `C:Om-finite-field-algorithm` ... `C:profinite-projective-data` in register order; ~7055 lines; why: no intake 51, programme 9. Main files: `RESEARCH_SA17/sections/C_finish_function_fields.tex` (4), `RESEARCH_SA17/sections/C_finish_henselian_effective.tex` (4), `RESEARCH_SA17/sections/C_finish_locally_finite.tex` (4), `RESEARCH_SA17/sections/C_finish_global_function_arithmetic.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped`.

### PACKET_33 (archive research): 57 rows, about 7146 proof lines (~142 pages)

- **RESEARCH_SA17** (cp12): 19 rows, `C:profinite-WG` ... `C:Om-canonical-example` in register order; ~2520 lines; why: no intake 19, programme 3. Main files: `RESEARCH_SA17/sections/C_finish_canonical_templates.tex` (5), `RESEARCH_SA17/sections/C_finish_regular_coherent.tex` (4), `RESEARCH_SA17/sections/C_finish_separably_closed.tex` (3), `RESEARCH_SA17/sections/C_finish_shallow_mixed_three_torsion.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped`.
- **RESEARCH_SA20** (final): 38 rows, `A.101` ... `A.138` in register order; ~4626 lines; why: no intake 38, programme 8, main 1. Main files: `RESEARCH_SA20/parts/parametric_concordance.tex` (18), `RESEARCH_SA20/parts/collars.tex` (13), `RESEARCH_SA20/parts/hausdorff_cones.tex` (1), `RESEARCH_SA20/agents/higher_comparison/part_elementary_extensions.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA20_final_20261120T0404Z_unzipped`.

### PACKET_34 (archive research): 57 rows, about 7050 proof lines (~141 pages)

- **RESEARCH_SA20** (final): 57 rows, `A.139` ... `A5.007` in register order; ~7050 lines; why: no intake 57, programme 1, main 1. Main files: `RESEARCH_SA20/parts/axioms.tex` (9), `RESEARCH_SA20/agents/lie_theory/part_A5.tex` (7), `RESEARCH_SA20/parts/filtrations.tex` (6), `RESEARCH_SA20/parts/foliation.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA20_final_20261120T0404Z_unzipped`.

### PACKET_35 (archive research): 67 rows, about 7083 proof lines (~141 pages)

- **RESEARCH_SA20** (final): 67 rows, `A5.008` ... `B.043` in register order; ~7083 lines; why: no intake 67, programme 13, main 11. Main files: `RESEARCH_SA20/agents/tensor_and_finite/part_B.tex` (43), `RESEARCH_SA20/agents/tensor_and_finite/part_A6.tex` (10), `RESEARCH_SA20/agents/lie_theory/part_A5.tex` (7), `RESEARCH_SA20/agents/maximal_locus/part_A5_method.tex` (1). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA20_final_20261120T0404Z_unzipped`.

### PACKET_36 (archive research): 72 rows, about 7043 proof lines (~140 pages)

- **RESEARCH_SA20** (final): 72 rows, `B.044` ... `D.008` in register order; ~7043 lines; why: no intake 72, programme 12, main 7, bridge flag 2. Main files: `RESEARCH_SA20/agents/tensor_and_finite/part_B.tex` (39), `RESEARCH_SA20/agents/singularities_duality/part_C.tex` (23), `RESEARCH_SA20/agents/lie_theory/part_D.tex` (8), `RESEARCH_SA20/agents/singularities_duality/unchecked_C.tex` (2). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA20_final_20261120T0404Z_unzipped`.

### PACKET_37 (archive research): 131 rows, about 7060 proof lines (~141 pages)

- **RESEARCH_SA20** (final): 33 rows, `D.009` ... `E.014` in register order; ~2589 lines; why: no intake 33, programme 3. Main files: `RESEARCH_SA20/agents/lie_theory/part_D.tex` (19), `RESEARCH_SA20/agents/tensor_and_finite/part_E.tex` (14). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA20_final_20261120T0404Z_unzipped`.
- **RESEARCH_SA22** (final): 98 rows, `A1-dimensions` ... `thm:B2-square` in register order; ~4471 lines; why: no intake 98, programme 20, main 5, bridge flag 3. Main files: `RESEARCH_SA22/sections/part_a6.tex` (18), `RESEARCH_SA22/sections/part_b.tex` (10), `RESEARCH_SA22/sections/part_a1.tex` (7), `RESEARCH_SA22/sections/part_a3.tex` (6). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA22_final_20261119T1905Z_unzipped`.

### PACKET_38 (archive research): 131 rows, about 7019 proof lines (~140 pages)

- **RESEARCH_SA22** (final): 61 rows, `prop:B2-kernel` ... `C-packed-asymmetry` in register order; ~2913 lines; why: no intake 61, bridge flag 5, programme 2. Main files: `RESEARCH_SA22/sections/part_b.tex` (42), `RESEARCH_SA22/sections/part_c.tex` (16), `RESEARCH_SA22/sections/part_b1b_class.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA22_final_20261119T1905Z_unzipped`.
- **RESEARCH_SA22_run2** (final): 70 rows, `A:shadowdef` ... `A:eigenmodule-correction` in register order; ~4106 lines; why: no intake 70, programme 6, bridge flag 3, main 3. Main files: `RESEARCH_SA22/sections/part_A567.tex` (29), `RESEARCH_SA22/sections/part_A1234.tex` (17), `RESEARCH_SA22/sections/C_A2b_image.tex` (8), `RESEARCH_SA22/sections/A1_radius_domain.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA22_run2_final_20261119T2149Z_unzipped`.

### PACKET_39 (archive research): 170 rows, about 7056 proof lines (~141 pages)

- **RESEARCH_SA22_run2** (final): 132 rows, `A:real-topology` ... `U:henselian-comparison` in register order; ~5439 lines; why: no intake 132, programme 13, bridge flag 5. Main files: `RESEARCH_SA22/sections/part_B.tex` (90), `RESEARCH_SA22/sections/part_C.tex` (24), `RESEARCH_SA22/notes/C_KnudsenMumford_sign_fragment.tex` (5), `RESEARCH_SA22/notes/C_constructible_group_algebraization.tex` (3). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA22_run2_final_20261119T2149Z_unzipped`.
- **RESEARCH_SA23** (final): 38 rows, `SA23-A-01` ... `SA23-D-3` in register order; ~1617 lines; why: no intake 38, programme 1. Main files: `RESEARCH_SA23/sections/algebra_C.tex` (10), `RESEARCH_SA23/sections/root_A12.tex` (9), `RESEARCH_SA23/sections/root_A3.tex` (6), `RESEARCH_SA23/sections/root_A4.tex` (4). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA23_final_20261120T0511Z_unzipped`.

### PACKET_40 (archive research): 82 rows, about 3963 proof lines (~79 pages)

- **RESEARCH_SA23** (final): 82 rows, `SA23-D-4` ... `cat:L8` in register order; ~3963 lines; why: no intake 82, programme 5, bridge flag 3. Main files: `RESEARCH_SA23/sections/algebra_D.tex` (14), `RESEARCH_SA23/sections/geometry_K.tex` (14), `RESEARCH_SA23/sections/category_I.tex` (12), `RESEARCH_SA23/sections/geometry_H.tex` (10). Folder: `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA23_final_20261120T0511Z_unzipped`.

### PACKET_41 (Longue Marche and anabelian): 66 rows, about 7145 proof lines (~142 pages)

- **SECTION_GHOSTS** (final): 66 rows, `P.2` ... `E.61` in register order; ~7145 lines; why: no intake 46, bridge flag 26, programme 22, main 1. Main files: `SECTION_GHOSTS/sections/part_A_cohomology.tex` (11), `SECTION_GHOSTS/sections/part_P_literature.tex` (9), `SECTION_GHOSTS/sections/part_B_cohomology.tex` (7), `SECTION_GHOSTS/sections/part_E_symmetry_audit.tex` (7). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped`.

### PACKET_42 (Longue Marche and anabelian): 53 rows, about 7064 proof lines (~141 pages)

- **SECTION_GHOSTS** (final): 53 rows, `E.62` ... `E.145` in register order; ~7064 lines; why: no intake 53, bridge flag 17, programme 10, main 1. Main files: `SECTION_GHOSTS/sections/part_E_elliptic_audit.tex` (26), `SECTION_GHOSTS/sections/part_E_embedding_gate.tex` (6), `SECTION_GHOSTS/sections/part_E_exact_four.tex` (4), `SECTION_GHOSTS/sections/part_E_exact_class_three.tex` (3). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped`.

### PACKET_43 (Longue Marche and anabelian): 37 rows, about 7142 proof lines (~142 pages)

- **SECTION_GHOSTS** (final): 37 rows, `E.146` ... `E.183` in register order; ~7142 lines; why: no intake 37, bridge flag 8, programme 2. Main files: `SECTION_GHOSTS/sections/part_E_harmonic_audit.tex` (6), `SECTION_GHOSTS/sections/part_E_two_inert_audit.tex` (4), `SECTION_GHOSTS/sections/part_E_all_prime_class_two.tex` (4), `SECTION_GHOSTS/sections/part_E_gt_geometric_repair.tex` (4). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped`.

### PACKET_44 (Longue Marche and anabelian): 55 rows, about 7372 proof lines (~147 pages)

- **SECTION_GHOSTS** (final): 28 rows, `E.184` ... `E.218` in register order; ~5127 lines; why: no intake 26, programme 6, main 4, bridge flag 2. Main files: `SECTION_GHOSTS/sections/part_E_finite_field_detector.tex` (2), `SECTION_GHOSTS/sections/part_E_compact_quaternion_detector.tex` (2), `SECTION_GHOSTS/sections/part_E_gt_translation_fusion.tex` (1), `SECTION_GHOSTS/sections/part_E_gt_involution_bridge.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\SECTION_GHOSTS_final_20261118T1305Z_unzipped`.
- **ANABELIAN_A1_SUCCESSOR** (cp05): 27 rows, `A.1` ... `A.56` in register order; ~2245 lines; why: programme 21, bridge flag 8. Main files: `ANABELIAN_A1_SUCCESSOR_paper.tex` (27). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_A1_SUCCESSOR_checkpoint_05_20261118T0610Z_unzipped`.

### PACKET_45 (Longue Marche and anabelian): 68 rows, about 7094 proof lines (~141 pages)

- **ANABELIAN_A1_SUCCESSOR** (cp05): 68 rows, `A.57` ... `B.119` in register order; ~7094 lines; why: no intake 48, programme 27, bridge flag 20. Main files: `ANABELIAN_A1_SUCCESSOR_paper.tex` (68). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_A1_SUCCESSOR_checkpoint_05_20261118T0610Z_unzipped`.

### PACKET_46 (Longue Marche and anabelian): 72 rows, about 7106 proof lines (~142 pages)

- **ANABELIAN_A1_SUCCESSOR** (cp05): 31 rows, `B.120` ... `C.11` in register order; ~5534 lines; why: no intake 29, programme 12, bridge flag 4. Main files: `ANABELIAN_A1_SUCCESSOR_paper.tex` (31). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_A1_SUCCESSOR_checkpoint_05_20261118T0610Z_unzipped`.
- **LM4_SUCCESSOR** (cp40): 41 rows, `A.1` ... `A.86` in register order; ~1572 lines; why: programme 29, no intake 16. Main files: `LM4_SUCCESSOR/sections/a_canonical_cusp_frame.tex` (3), `LM4_SUCCESSOR/sections/a_v4_fox_defect.tex` (2), `LM4_SUCCESSOR/sections/a_marked_three_cycle_cusp_frame.tex` (1), `LM4_SUCCESSOR/sections/a_normalized_residual_reduction.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped`.

### PACKET_47 (Longue Marche and anabelian): 43 rows, about 7068 proof lines (~141 pages)

- **LM4_SUCCESSOR** (cp40): 43 rows, `A.87` ... `B.9` in register order; ~7068 lines; why: programme 34, no intake 18. Main files: `LM4_SUCCESSOR/sections/b_audit.tex` (4), `LM4_SUCCESSOR/sections/b_geometry.tex` (2), `LM4_SUCCESSOR/sections/a_marked_three_cycle_cusp_frame.tex` (1), `LM4_SUCCESSOR/sections/a_alexander_dihedral_coefficient.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped`.

### PACKET_48 (Longue Marche and anabelian): 74 rows, about 7349 proof lines (~146 pages)

- **LM4_SUCCESSOR** (cp40): 74 rows, `B.10` ... `B.123` in register order; ~7349 lines; why: no intake 60, programme 33, bridge flag 4. Main files: `LM4_SUCCESSOR/sections/b_lattice.tex` (4), `LM4_SUCCESSOR/sections/b_symmetric_nonasphericity.tex` (3), `LM4_SUCCESSOR/sections/b_cross_sheet_block.tex` (3), `LM4_SUCCESSOR/sections/b_geometry.tex` (2). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped`.

### PACKET_49 (Longue Marche and anabelian): 36 rows, about 7104 proof lines (~142 pages)

- **LM4_SUCCESSOR** (cp40): 36 rows, `B.124` ... `B.159` in register order; ~7104 lines; why: no intake 36, programme 14. Main files: `LM4_SUCCESSOR/sections/b_outer_source_retract.tex` (1), `LM4_SUCCESSOR/sections/b_ordinary_star_single_cross.tex` (1), `LM4_SUCCESSOR/sections/b_final_prefix_axes.tex` (1), `LM4_SUCCESSOR/sections/b_family_kernel_schreier.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped`.

### PACKET_50 (Longue Marche and anabelian): 79 rows, about 7438 proof lines (~148 pages)

- **LM4_SUCCESSOR** (cp40): 67 rows, `B.160` ... `E.52` in register order; ~4930 lines; why: no intake 48, programme 29. Main files: `LM4_SUCCESSOR/sections/a_actual_boundary_reflection.tex` (2), `LM4_SUCCESSOR/sections/b_actual_nilpotent_target_exclusion.tex` (1), `LM4_SUCCESSOR/sections/b_unfilled_source_double.tex` (1), `LM4_SUCCESSOR/sections/b_unfilled_double_full_topology.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped`.
- **GT_TOWER_CHECK** (cp10): 12 rows, `A.1` ... `A.4.10` in register order; ~2508 lines; why: no intake 8, programme 4, main 2. Main files: `GT_TOWER_CHECK/part_a_centralizers.tex` (2), `GT_TOWER_CHECK/part_a_cm.tex` (1), `GT_TOWER_CHECK/part_a_finite.tex` (1), `GT_TOWER_CHECK/part_a_detector.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\GT_TOWER_CHECK_checkpoint_10_20261117T0945Z_unzipped`.

### PACKET_51 (Longue Marche and anabelian): 32 rows, about 7117 proof lines (~142 pages)

- **GT_TOWER_CHECK** (cp10): 32 rows, `A.4.11` ... `A.4.46` in register order; ~7117 lines; why: no intake 29, main 9, programme 3. Main files: `GT_TOWER_CHECK/part_a_orthogonal_lemmas.tex` (2), `GT_TOWER_CHECK/part_a_normalizer_lemmas.tex` (2), `GT_TOWER_CHECK/part_a_finite_deck_reconstruction.tex` (1), `GT_TOWER_CHECK/part_a_quaternion_surface_detector.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\GT_TOWER_CHECK_checkpoint_10_20261117T0945Z_unzipped`.

### PACKET_52 (Longue Marche and anabelian): 46 rows, about 7091 proof lines (~141 pages)

- **GT_TOWER_CHECK** (cp10): 46 rows, `A.4.47` ... `C.1.3` in register order; ~7091 lines; why: no intake 30, main 27, programme 12, bridge flag 2. Main files: `GT_TOWER_CHECK/part_b_descent_proofs.tex` (2), `GT_TOWER_CHECK/part_b_cyclic_descent.tex` (2), `GT_TOWER_CHECK/part_b_relative_obstruction.tex` (2), `GT_TOWER_CHECK/part_c_results.tex` (2). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\GT_TOWER_CHECK_checkpoint_10_20261117T0945Z_unzipped`.

### PACKET_53 (Longue Marche and anabelian): 68 rows, about 7100 proof lines (~142 pages)

- **GT_TOWER_CHECK** (cp10): 41 rows, `C.1.4` ... `C.3.11` in register order; ~5644 lines; why: no intake 34, bridge flag 15, programme 10, main 3. Main files: `GT_TOWER_CHECK/part_c_compatibility.tex` (3), `GT_TOWER_CHECK/part_c_h2.tex` (3), `GT_TOWER_CHECK/part_c_class3.tex` (3), `GT_TOWER_CHECK/part_c_prefix_class3.tex` (3). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\GT_TOWER_CHECK_checkpoint_10_20261117T0945Z_unzipped`.
- **ANABELIAN_A1** (cp03): 27 rows, `A.1` ... `B.3` in register order; ~1456 lines; why: programme 17, bridge flag 11, main 8. Main files: `ANABELIAN_A1/ANABELIAN_A1_paper.tex` (27). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped`.

### PACKET_54 (Longue Marche and anabelian): 81 rows, about 7123 proof lines (~142 pages)

- **ANABELIAN_A1** (cp03): 42 rows, `B.4` ... `C.11` in register order; ~3322 lines; why: main 21, no intake 13, bridge flag 11, programme 10. Main files: `ANABELIAN_A1/ANABELIAN_A1_paper.tex` (42). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped`.
- **ANABELIAN_SUCCESSOR** (final): 39 rows, `A.1` ... `F.9` in register order; ~3801 lines; why: programme 26, bridge flag 11, no intake 4. Main files: `ANABELIAN_SUCCESSOR_paper.tex` (39). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_SUCCESSOR_final_20261116T1243Z_unzipped`.

### PACKET_55 (Longue Marche and anabelian): 69 rows, about 7113 proof lines (~142 pages)

- **ANABELIAN_SUCCESSOR** (final): 28 rows, `F.10` ... `F.50` in register order; ~4503 lines; why: no intake 19, programme 11, bridge flag 11. Main files: `ANABELIAN_SUCCESSOR_paper.tex` (28). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\ANABELIAN_SUCCESSOR_final_20261116T1243Z_unzipped`.
- **FERMAT_SUCCESSOR** (cp06): 41 rows, `A.1` ... `A.59` in register order; ~2610 lines; why: no intake 31, bridge flag 20, programme 8, main 1. Main files: `deliverable/sections/A_main.tex` (12), `deliverable/sections/A_root.tex` (11), `deliverable/sections/A_census.tex` (6), `deliverable/sections/A_twists.tex` (4). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\FERMAT_SUCCESSOR_checkpoint_06_20261116T0649Z_unzipped`.

### PACKET_56 (Longue Marche and anabelian): 42 rows, about 7192 proof lines (~143 pages)

- **FERMAT_SUCCESSOR** (cp06): 42 rows, `A.60` ... `B.36` in register order; ~7192 lines; why: no intake 34, bridge flag 15, main 13, programme 12. Main files: `deliverable/sections/B_main.tex` (25), `deliverable/sections/A_finiteprime.tex` (2), `deliverable/sections/B_cusp_counterexample.tex` (2), `deliverable/sections/B_seven_classification.tex` (2). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\FERMAT_SUCCESSOR_checkpoint_06_20261116T0649Z_unzipped`.

### PACKET_57 (Longue Marche and anabelian): 56 rows, about 7091 proof lines (~141 pages)

- **FERMAT_SUCCESSOR** (cp06): 33 rows, `B.37` ... `D.4` in register order; ~4458 lines; why: no intake 29, main 6, bridge flag 6, programme 4. Main files: `deliverable/sections/C_main.tex` (17), `deliverable/sections/C_scope_refutation.tex` (4), `deliverable/sections/D_root.tex` (4), `deliverable/sections/C_root.tex` (2). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\FERMAT_SUCCESSOR_checkpoint_06_20261116T0649Z_unzipped`.
- **LM8_PUSH** (cp17): 23 rows, `P.1` ... `A.24` in register order; ~2633 lines; why: main 16, programme 11, no intake 6, bridge flag 6. Main files: `sections/P.tex` (5), `sections/A.tex` (4), `sections/A_residual_audit.tex` (4), `sections/P_literature.tex` (3). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped`.

### PACKET_58 (Longue Marche and anabelian): 28 rows, about 7250 proof lines (~145 pages)

- **LM8_PUSH** (cp17): 28 rows, `A.25` ... `A.57` in register order; ~7250 lines; why: main 20, programme 20, bridge flag 11, no intake 5. Main files: `sections/A_D3_monodromy.tex` (1), `sections/A_fixed_first_layer.tex` (1), `sections/A_D3_fixed_all.tex` (1), `sections/A_C3_stable_graph.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped`.

### PACKET_59 (Longue Marche and anabelian): 46 rows, about 7118 proof lines (~142 pages)

- **LM8_PUSH** (cp17): 46 rows, `A.58` ... `C.30` in register order; ~7118 lines; why: programme 25, main 21, no intake 17, bridge flag 4. Main files: `sections/C.tex` (15), `sections/B.tex` (12), `sections/A_heisenberg_five_fixed.tex` (1), `sections/A_nilpotent_cover_normalizers.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped`.

### PACKET_60 (Longue Marche and anabelian): 57 rows, about 7192 proof lines (~143 pages)

- **LM8_PUSH** (cp17): 57 rows, `C.31` ... `D.59` in register order; ~7192 lines; why: programme 32, main 26, no intake 23, bridge flag 4. Main files: `sections/D.tex` (33), `sections/C.tex` (18), `sections/D_prosolvable_local.tex` (1), `sections/D_prosolvable_legendre.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped`.

### PACKET_61 (Longue Marche and anabelian): 21 rows, about 7082 proof lines (~141 pages)

- **LM8_PUSH** (cp17): 21 rows, `D.60` ... `D.83` in register order; ~7082 lines; why: programme 16, main 10, bridge flag 10, no intake 9. Main files: `sections/D_alexander_zero.tex` (1), `sections/D_alexander_all_lim1.tex` (1), `sections/D_alexander_separated.tex` (1), `sections/D_alexander_one_prime.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped`.

### PACKET_62 (Longue Marche and anabelian): 52 rows, about 7137 proof lines (~142 pages)

- **LM8_PUSH** (cp17): 32 rows, `D.84` ... `H.10` in register order; ~4852 lines; why: no intake 23, main 10, bridge flag 7, programme 6. Main files: `sections/H.tex` (8), `sections/G.tex` (6), `sections/F.tex` (5), `sections/E.tex` (3). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped`.
- **LM7_PUSH** (cp09): 20 rows, `A.1` ... `A.27` in register order; ~2285 lines; why: programme 19, bridge flag 4, main 4, no intake 1. Main files: `LM7_PUSH/sections/A_agent.tex` (17), `LM7_PUSH/sections/A_root.tex` (3). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped`.

### PACKET_63 (Longue Marche and anabelian): 49 rows, about 7054 proof lines (~141 pages)

- **LM7_PUSH** (cp09): 49 rows, `A.28` ... `D.20` in register order; ~7054 lines; why: programme 34, main 22, bridge flag 7, no intake 3. Main files: `LM7_PUSH/sections/B_agent.tex` (15), `LM7_PUSH/sections/A_agent.tex` (13), `LM7_PUSH/sections/C_agent.tex` (9), `LM7_PUSH/sections/D_agent.tex` (6). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped`.

### PACKET_64 (Longue Marche and anabelian): 32 rows, about 7083 proof lines (~141 pages)

- **LM7_PUSH** (cp09): 32 rows, `D.21` ... `E.19` in register order; ~7083 lines; why: programme 25, main 12. Main files: `LM7_PUSH/sections/E_agent.tex` (4), `LM7_PUSH/sections/E_class2_agent.tex` (3), `LM7_PUSH/sections/D_root.tex` (2), `LM7_PUSH/sections/D_peripheral_agent.tex` (2). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped`.

### PACKET_65 (Longue Marche and anabelian): 26 rows, about 7214 proof lines (~144 pages)

- **LM7_PUSH** (cp09): 26 rows, `E.20` ... `E.50` in register order; ~7214 lines; why: programme 21, main 6, no intake 3, bridge flag 2. Main files: `LM7_PUSH/sections/E_root.tex` (1), `LM7_PUSH/sections/E_ferrari_degree4_agent.tex` (1), `LM7_PUSH/sections/E_ferrari_degree5_agent.tex` (1), `LM7_PUSH/sections/E_ferrari_degree6_agent.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped`.

### PACKET_66 (Longue Marche and anabelian): 29 rows, about 7249 proof lines (~144 pages)

- **LM7_PUSH** (cp09): 29 rows, `E.51` ... `F.29` in register order; ~7249 lines; why: main 19, programme 14, bridge flag 4. Main files: `LM7_PUSH/sections/F_root.tex` (4), `LM7_PUSH/sections/F4_agent.tex` (3), `LM7_PUSH/sections/E_symplectic_five_p7_agent.tex` (1), `LM7_PUSH/sections/E_symplectic_integral_root.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped`.

### PACKET_67 (Longue Marche and anabelian): 63 rows, about 7162 proof lines (~143 pages)

- **LM7_PUSH** (cp09): 1 rows, `F.32` ... `F.32` in register order; ~266 lines; why: main 1. Main files: `LM7_PUSH/sections/F4_agent.tex` (1). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped`.
- **LM4_FINITE_GROUP_ACTIONS** (return): 62 rows, `A.1` ... `C.45` in register order; ~6896 lines; why: no intake 34, programme 32, main 31. Main files: `LM4_FINITE_GROUP_ACTIONS_paper.tex` (62). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped`.

### PACKET_68 (Longue Marche and anabelian): 30 rows, about 7399 proof lines (~147 pages)

- **LM4_FINITE_GROUP_ACTIONS** (return): 30 rows, `C.46` ... `C.75` in register order; ~7399 lines; why: main 30, no intake 18. Main files: `LM4_FINITE_GROUP_ACTIONS_paper.tex` (30). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped`.

### PACKET_69 (Longue Marche and anabelian): 40 rows, about 7246 proof lines (~144 pages)

- **LM4_FINITE_GROUP_ACTIONS** (return): 40 rows, `C.76` ... `D.37` in register order; ~7246 lines; why: main 30, programme 16, no intake 7. Main files: `LM4_FINITE_GROUP_ACTIONS_paper.tex` (40). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped`.

### PACKET_70 (Longue Marche and anabelian): 28 rows, about 7392 proof lines (~147 pages)

- **LM4_FINITE_GROUP_ACTIONS** (return): 28 rows, `D.38` ... `D.65` in register order; ~7392 lines; why: main 28, no intake 6, programme 1. Main files: `LM4_FINITE_GROUP_ACTIONS_paper.tex` (28). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped`.

### PACKET_71 (Longue Marche and anabelian): 37 rows, about 7161 proof lines (~143 pages)

- **LM4_FINITE_GROUP_ACTIONS** (return): 37 rows, `D.66` ... `F.28` in register order; ~7161 lines; why: main 36, no intake 4, programme 1. Main files: `LM4_FINITE_GROUP_ACTIONS_paper.tex` (37). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped`.

### PACKET_72 (Longue Marche and anabelian): 24 rows, about 3269 proof lines (~65 pages)

- **LM4_FINITE_GROUP_ACTIONS** (return): 5 rows, `F.29` ... `F.33` in register order; ~1933 lines; why: main 5. Main files: `LM4_FINITE_GROUP_ACTIONS_paper.tex` (5). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM4_FINITE_GROUP_ACTIONS_20261114T0406Z_unzipped`.
- **LM1_GROUP_SCHEMES_rerun_20261112** (return): 19 rows, `A.1` ... `E.16` in register order; ~1336 lines; why: programme 17, bridge flag 2. Main files: `LM1_GROUP_SCHEMES/sections/E.tex` (6), `LM1_GROUP_SCHEMES/sections/B.tex` (3), `LM1_GROUP_SCHEMES/sections/C.tex` (3), `LM1_GROUP_SCHEMES/sections/D.tex` (3). Folder: `<local>/Documents\longue_marche_pro_pilot_20261104\answers\LM1_GROUP_SCHEMES_rerun_20261112_unzipped`.

### PACKET_73 (Derivateurs): 56 rows, about 6863 proof lines (~137 pages)

- **DER_LOCALIZERS** (cp08): 56 rows, `A2.2` ... `C.21` in register order; ~6863 lines; why: main 24, no intake 23, programme 21. Main files: `DER_LOCALIZERS/sections/C.tex` (19), `DER_LOCALIZERS/sections/A2_review.tex` (12), `DER_LOCALIZERS/sections/B.tex` (8), `DER_LOCALIZERS/sections/A.tex` (6). Folder: `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112_work\DER_LOCALIZERS\DER_LOCALIZERS_checkpoint_08_20261118T0954Z_unzipped`.

### PACKET_74 (Derivateurs): 42 rows, about 6764 proof lines (~135 pages)

- **DER_LOCALIZERS** (cp08): 9 rows, `C.22` ... `D.2` in register order; ~2412 lines; why: main 5, no intake 4, programme 3. Main files: `DER_LOCALIZERS/sections/C.tex` (7), `DER_LOCALIZERS/sections/D.tex` (2). Folder: `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112_work\DER_LOCALIZERS\DER_LOCALIZERS_checkpoint_08_20261118T0954Z_unzipped`.
- **REVLOC** (cp17): 33 rows, `A.1` ... `D.2.36` in register order; ~4352 lines; why: no intake 26, programme 13. Main files: `REVLOC/sections/D.tex` (6), `REVLOC/sections/A.tex` (3), `REVLOC/sections/B.tex` (3), `REVLOC/sections/D1_Moore.tex` (3). Folder: `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112_work\REVERSIBLE_LOCALIZERS\REVLOC_checkpoint_17_20261116T0257Z_unzipped`.

### PACKET_75 (Derivateurs): 31 rows, about 6887 proof lines (~137 pages)

- **REVLOC** (cp17): 31 rows, `D.2.13` ... `D.3.6` in register order; ~6887 lines; why: no intake 30, programme 6, bridge flag 1, main 1. Main files: `REVLOC/sections/D2_hopf_extension.tex` (1), `REVLOC/sections/D2_integral_mixed.tex` (1), `REVLOC/sections/D2_integral_primary_sources.tex` (1), `REVLOC/sections/D2_integral_square_nonzero.tex` (1). Folder: `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112_work\REVERSIBLE_LOCALIZERS\REVLOC_checkpoint_17_20261116T0257Z_unzipped`.

### PACKET_76 (Derivateurs): 63 rows, about 6281 proof lines (~125 pages)

- **REVLOC** (cp17): 22 rows, `D.3.7` ... `I.9b` in register order; ~2376 lines; why: no intake 19, main 2, programme 1. Main files: `REVLOC/sections/F3.tex` (5), `REVLOC/sections/I.tex` (4), `REVLOC/sections/D_nullification.tex` (3), `REVLOC/sections/H5.tex` (3). Folder: `<local>/Documents\derivateurs_companion_20261109\pro_prompts_max_20261112_work\REVERSIBLE_LOCALIZERS\REVLOC_checkpoint_17_20261116T0257Z_unzipped`.
- **RESIDUE** (return): 41 rows, `A.1` ... `J.1` in register order; ~3905 lines; why: main 25, programme 12, no intake 9. Main files: `RESIDUE/sections/I.tex` (9), `RESIDUE/sections/D.tex` (8), `RESIDUE/sections/B.tex` (6), `RESIDUE/sections/C.tex` (6). Folder: `<local>/Documents\derivateurs_companion_20261109\pro_returns_20261110\8_RESIDUE`.

### PACKET_77 (S6): 72 rows, about 7232 proof lines (~144 pages)

- **S6_SERIES_GRIND** (cp10): 72 rows, `inv:A1.0` ... `push:src:B.4.10` in register order; ~7232 lines; why: programme 53, no intake 26, bridge flag 1. Main files: `S6_SERIES_GRIND_I.tex` (72). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_78 (S6): 41 rows, about 7120 proof lines (~142 pages)

- **S6_SERIES_GRIND** (cp10): 41 rows, `push:src:B.4.19` ... `push:src:E.2.22` in register order; ~7120 lines; why: programme 38, no intake 4. Main files: `S6_SERIES_GRIND_I.tex` (13), `S6_SERIES_GRIND_II.tex` (13), `S6_SERIES_GRIND_IV.tex` (11). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_79 (S6): 46 rows, about 7349 proof lines (~146 pages)

- **S6_SERIES_GRIND** (cp10): 46 rows, `push:src:E.2.23` ... `cdp:st:C.2.UN.41` in register order; ~7349 lines; why: programme 46. Main files: `S6_SERIES_GRIND_II.tex` (44), `S6_SERIES_GRIND_I.tex` (1), `parts/II.body.linked.tex` (1). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_80 (S6): 24 rows, about 7332 proof lines (~146 pages)

- **S6_SERIES_GRIND** (cp10): 24 rows, `cdp:st:C.2.UN.37` ... `cdp:st:C.2.UN.49` in register order; ~7332 lines; why: programme 23, bridge flag 3. Main files: `S6_SERIES_GRIND_II.tex` (24). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_81 (S6): 31 rows, about 7110 proof lines (~142 pages)

- **S6_SERIES_GRIND** (cp10): 31 rows, `cdp:st:C.2.UN.70` ... `cdp:st:D.2.3` in register order; ~7110 lines; why: programme 30, bridge flag 2. Main files: `S6_SERIES_GRIND_II.tex` (30). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_82 (S6): 47 rows, about 7322 proof lines (~146 pages)

- **S6_SERIES_GRIND** (cp10): 47 rows, `cdp:st:D.2.7` ... `maps:src:D.2.22` in register order; ~7322 lines; why: programme 42, no intake 9. Main files: `S6_SERIES_GRIND_III.tex` (22), `S6_SERIES_GRIND_IV.tex` (13), `S6_SERIES_GRIND_II.tex` (8), `S6_SERIES_GRIND_I.tex` (2). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_83 (S6): 29 rows, about 7295 proof lines (~145 pages)

- **S6_SERIES_GRIND** (cp10): 29 rows, `maps:src:D.2.23` ... `maps:src:E.2.16` in register order; ~7295 lines; why: programme 29, bridge flag 1. Main files: `S6_SERIES_GRIND_III.tex` (21), `S6_SERIES_GRIND_V.tex` (8). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_84 (S6): 52 rows, about 7186 proof lines (~143 pages)

- **S6_SERIES_GRIND** (cp10): 52 rows, `maps:src:E.2.19` ... `ari:C.6.R5` in register order; ~7186 lines; why: programme 28, no intake 27, bridge flag 2. Main files: `S6_SERIES_GRIND_V.tex` (29), `S6_SERIES_GRIND_I.tex` (22). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_85 (S6): 78 rows, about 7038 proof lines (~140 pages)

- **S6_SERIES_GRIND** (cp10): 78 rows, `ari:C.6.T1` ... `wbII:lem:picard-cusp-defect` in register order; ~7038 lines; why: no intake 77, bridge flag 13, programme 13. Main files: `S6_SERIES_GRIND_I.tex` (32), `S6_SERIES_GRIND_II.tex` (17), `audit_corrections/I_permitted_wb_lem_toric-chart-control.tex` (1), `audit_corrections/I_permitted_wb_thm_candidate-cusp-geometry.tex` (1). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_86 (S6): 81 rows, about 7060 proof lines (~141 pages)

- **S6_SERIES_GRIND** (cp10): 81 rows, `wbII:prop:direct-boundary-picard` ... `wb:cusp-s12-nullity-scope` in register order; ~7060 lines; why: no intake 81, programme 6, bridge flag 3. Main files: `S6_SERIES_GRIND_II.tex` (28), `S6_SERIES_GRIND_III.tex` (26). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_87 (S6): 199 rows, about 7026 proof lines (~140 pages)

- **S6_SERIES_GRIND** (cp10): 199 rows, `wb:cusp-null:thm` ... `courseIII:low-index-slides:9.1` in register order; ~7026 lines; why: no intake 182, programme 20. Main files: `S6_SERIES_GRIND_I.tex` (17), `S6_SERIES_GRIND_III.tex` (2). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_88 (S6): 117 rows, about 7155 proof lines (~143 pages)

- **S6_SERIES_GRIND** (cp10): 117 rows, `courseIII:low-index-slides:9.2` ... `night:P1.18` in register order; ~7155 lines; why: no intake 117, programme 6, bridge flag 2. Main files: `S6_SERIES_GRIND_V.tex` (16), `S6_SERIES_GRIND_III.tex` (14). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_89 (S6): 88 rows, about 7088 proof lines (~141 pages)

- **S6_SERIES_GRIND** (cp10): 88 rows, `night:P1.19` ... `night:P4R.3` in register order; ~7088 lines; why: no intake 87, programme 37. Main files: `S6_SERIES_GRIND_IV.tex` (28), `S6_SERIES_GRIND_II.tex` (26), `S6_SERIES_GRIND_I.tex` (17), `S6_SERIES_GRIND_V.tex` (9). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_90 (S6): 34 rows, about 7004 proof lines (~140 pages)

- **S6_SERIES_GRIND** (cp10): 34 rows, `night:P4R.4` ... `night:P3K.10` in register order; ~7004 lines; why: no intake 34, programme 24. Main files: `S6_SERIES_GRIND_IV.tex` (24), `S6_SERIES_GRIND_II.tex` (9), `S6_SERIES_GRIND_I.tex` (1). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_91 (S6): 25 rows, about 7144 proof lines (~142 pages)

- **S6_SERIES_GRIND** (cp10): 25 rows, `night:P3K.11` ... `night:P3F.52` in register order; ~7144 lines; why: no intake 25, programme 22. Main files: `S6_SERIES_GRIND_IV.tex` (25). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_92 (S6): 22 rows, about 7208 proof lines (~144 pages)

- **S6_SERIES_GRIND** (cp10): 22 rows, `night:P3K.33` ... `night:P3K.51` in register order; ~7208 lines; why: no intake 21, programme 15. Main files: `S6_SERIES_GRIND_IV.tex` (21), `S6_SERIES_GRIND_II.tex` (1). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_93 (S6): 20 rows, about 7138 proof lines (~142 pages)

- **S6_SERIES_GRIND** (cp10): 20 rows, `night:P3K.52` ... `night:P3K.73` in register order; ~7138 lines; why: no intake 19, programme 18. Main files: `S6_SERIES_GRIND_IV.tex` (20). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_94 (S6): 20 rows, about 7365 proof lines (~147 pages)

- **S6_SERIES_GRIND** (cp10): 20 rows, `night:P3K.74` ... `night:P3K.94` in register order; ~7365 lines; why: no intake 19, programme 16. Main files: `S6_SERIES_GRIND_IV.tex` (20). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_95 (S6): 22 rows, about 7068 proof lines (~141 pages)

- **S6_SERIES_GRIND** (cp10): 22 rows, `night:P3K.95` ... `night:P4.31` in register order; ~7068 lines; why: no intake 22, programme 16. Main files: `S6_SERIES_GRIND_IV.tex` (14), `S6_SERIES_GRIND_II.tex` (8). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_96 (S6): 43 rows, about 7080 proof lines (~141 pages)

- **S6_SERIES_GRIND** (cp10): 43 rows, `night:P4.32` ... `iv:i3_all_reduced_caps` in register order; ~7080 lines; why: no intake 43, programme 16. Main files: `S6_SERIES_GRIND_II.tex` (36), `S6_SERIES_GRIND_III.tex` (2), `S6_SERIES_GRIND_I.tex` (2), `S6_SERIES_GRIND_IV.tex` (2). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_97 (S6): 78 rows, about 7201 proof lines (~144 pages)

- **S6_SERIES_GRIND** (cp10): 78 rows, `night:P3K.109` ... `series:I:G` in register order; ~7201 lines; why: no intake 78, programme 14, main 7. Main files: `S6_SERIES_GRIND_IV.tex` (44), `S6_SERIES_GRIND_I.tex` (7). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

### PACKET_98 (S6): 30 rows, about 3517 proof lines (~70 pages)

- **S6_SERIES_GRIND** (cp10): 30 rows, `series:II:A` ... `inv:E2.5` in register order; ~3517 lines; why: no intake 30, main 27. Main files: `S6_SERIES_GRIND_IV.tex` (9), `S6_SERIES_GRIND_II.tex` (8), `S6_SERIES_GRIND_III.tex` (7), `S6_SERIES_GRIND_V.tex` (6). Folder: `<local>/Documents\s6_pro_prompts_20261112_work\returns\S6_SERIES_GRIND_checkpoint_10_20261120T0211Z_unzipped`.

## Totals

98 packets, 6147 rows, about 686823 proof lines (~13736 pages).

