# Prompt updates of 24 Nov 2026: F_Archive_working_through_200 and E_Archive_small_prompts_54 (24, 32-37)

Done by Claude Opus 5.5 at effort high (agent ae43bbdc3768d8bfc, the SWEEP3 topicality agent), on the message of the main
session 329fb1e6 (Claude Opus 5.5 at effort max), under `PROMPT_UPDATE_BRIEF.md`. Work file:
`agent_notes/ae43bbdc3768d8bfc_NOTES.md`. Scripts and their outputs:
`<local>/AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15\scratchpad\topsweep3\`
(`build_settled.py`, `plan.py`, `apply.py`, `lint_all.py`).

## What was checked first

- **Sent or not.** `TO_SEND/PRO/SENT_PRO.tsv` (last written 21 Nov 01:04) lists none of 24, 32-37. From F it lists only
  001_OBJ_H035, 002_OBJ_H0K8+H0KB, 003_OBJ_H0DT and 00_range_pilot_first/033, which are no longer in the batch folders.
  None of my folders sits in a SENT or .SENT folder. Rechecked before applying.
- **What the waiting prompts already hold.** Every F object prompt and the WTA/WTB prompts carry a results ZIP built on 18 Nov
  2026 (for example `OBJ_H0AK_results/README.md`: "0 rows"). So none of the sweep-3 research returns of 19-20 Nov reached
  them.

## How the findings were matched

- **The findings.** I read the registers of the 18 sweep-3 research returns: RESEARCH_SA05-SA10, SA08_C3_D031, SA12, SA14_SA19,
  SA15, SA17, SA20-SA23, SA22_run2. The runs are GPT-6 Astra (ChatGPT Pro mode). In each row I parsed the manuscript-page
  locators, in all three forms used: `14:44-45`, `29/139-142` and `cote129 scans94,114,115`.
- **The check state.** I attached each row's outside check events from our intake files (Claude Opus 5.5 at effort max or
  high, 19-24 Nov). These are `results_register/horizontal/sweep3/SAxx/INTAKE_*CHECK_EVENTS*.tsv` and the pile's
  `INTAKE_RESEARCH_*_20261124_CHECK_EVENTS.tsv`.
- **The literature verdicts.** I added the verdicts of `TOPICALITY_SWEEP3.md` for the rows they concern:
  - L6c, B.1, SA22_run2 B.90 (the local Hurewicz example) and SA20 B.016 are known before;
  - SA05 A:class / A:hasse and the Weil-étale Z/2 rows are known;
  - C.4i, C.4n, C.4p, C.3be, G1 and SA21 A27/A06 are partly known;
  - for B.022 and geo-H the posted Hexagon note (B.022) and the history notes are given.
- **The matching.** A row is a candidate for an object when its page locators meet the pages that the object's own
  `ENTRIES.tsv` cites. This is cote and scan matching, as the message allows. Then I read each candidate object's prompt
  header, its ENTRIES index (sweep item ids, cited pages, kinds) and the matched rows.

Six candidates were dropped:

| Object | Why it was dropped |
|---|---|
| 058 H03O, 070 H03S-1, 124 H03S-2 | Their objects are reused typescripts on the backs of those leaves. The rows concern his handwritten mathematics on the same scans. |
| 023 H0B5 (Stone-Čech) | It shares cote 129 only through the package range. The rows are crystalline Dieudonné. |
| 127 H05W, 181 H00M-1 (Remords, tame topology) | The only match is the title pages 153/155:2 (analysers). |
| 187 H0CS (report 119/276-281) | One row on 119/156-157. |

In 079 H0CR, rows A.701-A.704 (119/145-146) are excluded: they belong to 025 H0CO.

## What was changed in each prompt (49 prompts)

1. **Backup.** The whole folder was copied to `TO_SEND/PRO/_backups_20261125/<folder name>/`.
2. **ZIP.** Two things were appended to the one ZIP, keeping every existing member:
   - the folder `<TAG>_settled/`: `README`-free; `SETTLED.tsv`, one row per matched statement, with the run, id, the run's
     status, his pages, the statement, where_proved, the source files, the outside check events and the 25 Nov
     literature verdict; and `sources/<run>/`, the run's own TeX and notes named in where_proved;
   - `latex_sources/`, our LaTeX of EGA (FR, EN) and FGA (FR), plus the SGA volumes that the prompt or its entries and
     passages name. This used `claude_tools/latex_sources.py add`, following the standing rule of 22 Nov ("Always include
     LaTeX where we have LaTeX as the primary source"). It was not done for 24_SA20, a notes dossier that passes `--lint`.
3. **PROMPT.md.** One section was inserted before `## How to work`: "Decided since this prompt was built (added 25 Nov
   2026)". For 24_SA20 the section is "Results on this topic since this dossier was planned", inserted before
   `## Stage 1`. The section:
   - names the runs and the number of rows, and describes `SETTLED.tsv`;
   - lifts the "our results last" rule (step 6, or step 9 in WTA/WTB) for those rows only;
   - makes each decided statement background, used and rechecked in use, with a check event of the type that happened;
   - turns each such item into the next question beyond the row: the stronger form if proved; the corrected statement and
     his likely intent if refuted; the exact locator and what his pages add if known;
   - redefines the main question as the strongest statement on these pages that the rows leave undecided;
   - sends rows about another object to `LINKS.tsv`;
   - lists up to 8 rows. Priority order: items ranked useful in SWEEP3_A/B, then items with a 25 Nov literature verdict,
     then refutations, known results and proofs, checked rows first.

   Two standing-rule paragraphs were also added where missing: **Primary sources in LaTeX** (`latex_sources/`) and **No
   copies of sources in any ZIP you return**. Without them every one of these prompts failed `--lint-math` before I
   touched it.
4. **Unchanged.** Everything else: the main questions, the push paragraph, the progress-check ledger, the checkpoint rules
   and CHECK_EVENTS.tsv. No minimum, way out or cheaper alternative was added.

### The prompts

Each prompt's evidence is its `SETTLED.tsv` in the ZIP. Every row there gives the run's file and label (`where_proved`) and
the intake event file and type.

| Prompt (under TO_SEND/PRO) | Rows matched | Runs | Rows listed in the prompt | 25 Nov literature verdicts | LaTeX packs added |
|---|---|---|---|---|---|
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_1_001-017\004_OBJ_H03N_O` | 2 (0 refuted, 0 known; 2 with outside checks) | RESEARCH_SA05 | `c:bivariant-equivalence`, `c:bivariant-def` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN, SGA7_FR, SGA7_EN] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_1_001-017\007_OBJ_H04V+H050+H04R_O` | 17 (4 refuted, 0 known; 17 with outside checks) | RESEARCH_SA08 | `A-004`, `A-009`, `A-025`, `B-13`, `A-001`, `A-002`, `A-003`, `A-005` | - | [EGA_FR, EGA_EN, FGA_FR, SGA3_EN] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_1_001-017\008_OBJ_H06O_O` | 1 (0 refuted, 1 known; 1 with outside checks) | RESEARCH_SA12 | `D:prime-to-p` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN, SGA7_FR, SGA7_EN, SGA1_EN] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_1_001-017\009_OBJ_H09Z_O` | 8 (0 refuted, 0 known; 8 with outside checks) | RESEARCH_SA14_SA19 | `G1`, `G2`, `G3-Albanese`, `G3-principal`, `G2a`, `G2b`, `G3`, `R9` | G1 | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_1_001-017\014_OBJ_H0AK_O` | 601 (4 refuted, 1 known; 601 with outside checks) | RESEARCH_SA15 | `prop:OC-product-integral-counterexample`, `thm:plane-char2-all-groups`, `thm:all-X-explicit-positive-rank`, `A2-EXACT`, `A2-UNIT`, `A6-COUNTEREXAMPLE`, `thm:A-coherent-restriction-false`, `prop:root-f1-bad-five-kernel` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_1_001-017\016_OBJ_H001_O` | 45 (4 refuted, 2 known; 45 with outside checks) | RESEARCH_SA05, RESEARCH_SA06, RESEARCH_SA07 | `C.1.5`, `c:explicit-bad-reduction`, `E.1c`, `E.2b`, `E.2e`, `c:vz-positive`, `F.3.12`, `c:lie-centre` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_1_001-017\017_OBJ_H0JZ_O` | 6 (1 refuted, 3 known; 6 with outside checks) | RESEARCH_SA09 | `A4.3`, `A4.5`, `A4.4`, `A4.1`, `A4.2`, `A4.6` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_2_018-034\018_OBJ_H0CA_O` | 4 (1 refuted, 3 known; 4 with outside checks) | RESEARCH_SA14_SA19 | `SA19-H6`, `SA19-H1`, `SA19-H2`, `R10` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_2_018-034\020_OBJ_H0KN_O` | 153 (29 refuted, 88 known; 56 with outside checks) | RESEARCH_SA22, RESEARCH_SA22_run2 | `B.90`, `thm:B1c`, `thm:B2-square`, `thm:B3-pprimary`, `thm:B3-specialization`, `thm:B3-sga2`, `B.05`, `B.08` | B.90 | [EGA_FR, EGA_EN, FGA_FR, SGA6_FR, SGA6_EN] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_2_018-034\024_OBJ_H00L_O` | 50 (9 refuted, 9 known; 37 with outside checks) | RESEARCH_SA10, RESEARCH_SA20 | `B2.2`, `B3.1`, `B2.4`, `A.132`, `A5.006`, `A5.009`, `A5.010`, `A6.006` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave1_001-040\batch_2_018-034\025_OBJ_H0CO_O` | 4 (1 refuted, 0 known; 4 with outside checks) | RESEARCH_SA20 | `A.701`, `A.703`, `A.702`, `A.704` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_1_041-057\057_OBJ_H0DJ-1_O` | 10 (3 refuted, 1 known; 10 with outside checks) | RESEARCH_SA23 | `geo-H-history`, `geo-H-lidskii`, `geo-H-continuity`, `geo-H-determinant`, `geo-H-rearrangement`, `geo-H-all-scalars`, `geo-H-bounds`, `geo-H-genus` | geo-H-lidskii, geo-H-history | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\061_OBJ_H053_O` | 12 (2 refuted, 0 known; 12 with outside checks) | RESEARCH_SA08 | `A-004`, `A-009`, `A-001`, `A-002`, `A-003`, `A-005`, `A-006`, `A-007` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\062_OBJ_H06P+H065+H064_O` | 321 (8 refuted, 4 known; 321 with outside checks) | RESEARCH_SA12 | `D:wild-genus2-single-curve`, `D:fixed-boundary-gate`, `D:boundary-neighborhood`, `D:fierce-small-excess`, `D:pure-root-rational-tail-obstruction`, `D:bounded-ramification-generation-obstruction`, `D:fixed-different-unbounded-rational-chain`, `D:Chow-surface-boundary-obstruction` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN, SGA7_FR, SGA7_EN] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\063_OBJ_H09X_O` | 98 (43 refuted, 3 known; 98 with outside checks) | RESEARCH_SA14_SA19 | `D4b`, `B1`, `SA14-H2`, `SA14-H12`, `SA14-H13`, `B2-necessity`, `C4-general`, `E1-literal` | - | [EGA_FR, EGA_EN, FGA_FR, SGA6_FR, SGA6_EN, SGA3_EN, SGA2_EN, SGA1_EN] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\065_OBJ_H04F_O` | 119 (10 refuted, 6 known; 119 with outside checks) | RESEARCH_SA07 | `G.2.2`, `A.2.2`, `A.2.6`, `A.4.21`, `C.1.5`, `D.5.2`, `A.1.2`, `B.4.1` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\068_OBJ_H0AE_O` | 3 (0 refuted, 0 known; 3 with outside checks) | RESEARCH_SA15 | `thm:DE-split`, `auto:D:fa384818cda6`, `rem:DE-quote-D1` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\071_OBJ_H0K3_O` | 12 (3 refuted, 3 known; 12 with outside checks) | RESEARCH_SA08_C3_D031, RESEARCH_SA09 | `A1.2`, `A3.4`, `A1.7`, `A1.8`, `A3.5`, `A-S09-05`, `A1.1`, `A3.3` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\072_OBJ_H0CB-1_O` | 6 (1 refuted, 3 known; 6 with outside checks) | RESEARCH_SA14_SA19 | `H1`, `SA19-H6`, `SA19-H1`, `SA19-H2`, `R10`, `H-all` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\073_OBJ_H00N_O` | 80 (4 refuted, 1 known; 80 with outside checks) | RESEARCH_SA20 | `B.022`, `B.023`, `B.024`, `B.016`, `B.002`, `B.008`, `B.011`, `B.012` | B.016, B.022, B.023, B.024 | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_2_058-074\074_OBJ_H0KR_O` | 21 (6 refuted, 2 known; 14 with outside checks) | RESEARCH_SA22, RESEARCH_SA22_run2 | `A4-orange-extremal`, `A4-orange-jets`, `A7-domain-counterexample`, `A7-ratio-j`, `A:orange`, `R5.connectedness`, `A4-grafting`, `A7-real-classification` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_3_075-080\077_OBJ_H0B6_O` | 22 (4 refuted, 6 known; 20 with outside checks) | RESEARCH_SA17 | `B:crystal-counterexamples`, `B:finite-PD`, `B:PD-not-QSyn`, `B:largest-literature-class`, `B:closure-reduction`, `B:L6-refutation`, `B:square-zero-Hom`, `B:effectivity` | - | [EGA_FR, EGA_EN, FGA_FR, SGA3_EN] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_3_075-080\078_OBJ_H05K-1_O` | 3 (2 refuted, 0 known; 2 with outside checks) | RESEARCH_SA10 | `C1.01`, `C4.04`, `C3.04` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave2_041-080\batch_3_075-080\079_OBJ_H0CR_O` | 10 (1 refuted, 0 known; 10 with outside checks) | RESEARCH_SA20 | `E.009`, `E.001`, `E.002`, `E.003`, `E.004`, `E.005`, `E.006`, `E.007` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave3_081-120\batch_1_081-097\088_OBJ_H051_O` | 21 (4 refuted, 0 known; 21 with outside checks) | RESEARCH_SA08 | `A-004`, `A-009`, `A-025`, `C03`, `A-001`, `A-002`, `A-003`, `A-005` | - | [EGA_FR, EGA_EN, FGA_FR, SGA3_EN] |
| `F_Archive_working_through_200\17_working_through_wave3_081-120\batch_2_098-114\112_OBJ_H00F-1_O` | 2 (0 refuted, 0 known; 2 with outside checks) | RESEARCH_SA05 | `c:bivariant-equivalence`, `c:bivariant-def` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave3_081-120\batch_3_115-120\115_OBJ_H052_O` | 44 (7 refuted, 0 known; 44 with outside checks) | RESEARCH_SA08, RESEARCH_SA08_C3_D031 | `A-CS`, `A-TL`, `A-004`, `A-009`, `A-025`, `C03`, `C07`, `B604` | - | [EGA_FR, EGA_EN, FGA_FR, SGA3_EN] |
| `F_Archive_working_through_200\17_working_through_wave3_081-120\batch_3_115-120\116_OBJ_H062_O` | 5 (1 refuted, 0 known; 5 with outside checks) | RESEARCH_SA12 | `D:alpha-geometric-counterexample`, `B.2a`, `B.2b`, `B.3`, `D:arithmetic-tame` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN, SGA7_FR, SGA7_EN, SGA1_EN] |
| `F_Archive_working_through_200\17_working_through_wave4_121-160\batch_1_121-137\122_OBJ_H0AD+H0AJ_O` | 5 (0 refuted, 0 known; 5 with outside checks) | RESEARCH_SA15 | `lem:DE-kappa`, `lem:DE-free-ci`, `thm:DE-coherent-obstruction`, `rem:DE-universal-negative`, `rem:DE-quote-D2` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave4_121-160\batch_1_121-137\125_OBJ_H0K2_O` | 7 (2 refuted, 2 known; 7 with outside checks) | RESEARCH_SA08_C3_D031, RESEARCH_SA09 | `A3.4`, `A3.5`, `A-S09-05`, `A3.3`, `A-S09-03`, `A3.1`, `A3.2` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave4_121-160\batch_1_121-137\126_OBJ_H0CF_O` | 3 (1 refuted, 0 known; 3 with outside checks) | RESEARCH_SA14_SA19 | `H1`, `SA19-H6`, `H-all` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave4_121-160\batch_1_121-137\128_OBJ_H0KT_O` | 88 (14 refuted, 22 known; 50 with outside checks) | RESEARCH_SA22, RESEARCH_SA22_run2 | `A2-explicit-limits`, `A1-bordered-landing`, `A2-independence`, `A6-ordinary-counterexample`, `A6-procyclic`, `A6-three-classes`, `A6-special-fibre-counterexample`, `A6-frobenius-counterexample` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave4_121-160\batch_1_121-137\131_OBJ_H0B8_O` | 22 (4 refuted, 6 known; 20 with outside checks) | RESEARCH_SA17 | `B:crystal-counterexamples`, `B:finite-PD`, `B:PD-not-QSyn`, `B:largest-literature-class`, `B:closure-reduction`, `B:L6-refutation`, `B:square-zero-Hom`, `B:effectivity` | - | [EGA_FR, EGA_EN, FGA_FR, SGA3_EN] |
| `F_Archive_working_through_200\17_working_through_wave4_121-160\batch_1_121-137\133_OBJ_H0CQ_O` | 19 (11 refuted, 1 known; 19 with outside checks) | RESEARCH_SA20 | `A.104`, `A.111`, `A.101`, `A.112`, `A.110`, `A.117`, `A.118`, `A.202` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave4_121-160\batch_2_138-154\142_OBJ_H04L-1_O` | 30 (2 refuted, 0 known; 30 with outside checks) | RESEARCH_SA08, RESEARCH_SA08_C3_D031 | `A-CS`, `A-TL`, `C07`, `C11`, `A-005`, `A-007`, `A-008`, `A-010` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_1_161-177\165_OBJ_H0D8_O` | 5 (0 refuted, 1 known; 5 with outside checks) | RESEARCH_SA23 | `geo-H-history`, `geo-H-lidskii`, `geo-H-bounds`, `geo-H-genus`, `geo-H-1956-reconstruction` | geo-H-lidskii, geo-H-history | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_1_161-177\166_OBJ_H00F-2_O` | 29 (2 refuted, 1 known; 29 with outside checks) | RESEARCH_SA05 | `c:modified-diagonal`, `c:product-parity`, `c:chow-positive`, `c:matrix-presentation`, `c:pair-ranks`, `c:other-dimensions`, `c:abelian-point-classification`, `c:curve-chow-criterion` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_1_161-177\170_OBJ_H06N_O` | 18 (6 refuted, 1 known; 18 with outside checks) | RESEARCH_SA12 | `C:literal-141`, `C:cusp-all-subgroups`, `C:normal-counterexample`, `D:alpha-counterexample`, `D:alpha-geometric-counterexample`, `D:alpha-common-refinement`, `D:prop5-counterexample`, `D:arithmetic-invertible` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN, SGA7_FR, SGA7_EN] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_1_161-177\171_OBJ_H0A3-1_O` | 20 (6 refuted, 0 known; 20 with outside checks) | RESEARCH_SA14_SA19 | `B1`, `SA14-H2`, `SA14-H13`, `B2-necessity`, `E1-literal`, `E1-functor`, `SA14-H10`, `B2-sufficiency` | - | [EGA_FR, EGA_EN, FGA_FR, SGA2_EN] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_1_161-177\176_OBJ_H0A9_O` | 2 (0 refuted, 0 known; 2 with outside checks) | RESEARCH_SA15 | `thm:DE-intrinsic-nerve`, `rem:DE-quote-E4` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_2_178-194\179_OBJ_H0K1-1_O` | 8 (2 refuted, 2 known; 8 with outside checks) | RESEARCH_SA08_C3_D031, RESEARCH_SA09 | `A4.3`, `A3.5`, `A4.4`, `A4.1`, `A-S09-03`, `A3.1`, `A3.2`, `A4.2` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_2_178-194\180_OBJ_H0CE_O` | 27 (5 refuted, 2 known; 21 with outside checks) | RESEARCH_SA14_SA19, RESEARCH_SA22_run2 | `H1`, `I8`, `H3`, `H4b`, `H3b`, `B.93`, `B.94`, `B.91` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_2_178-194\182_OBJ_H0KV_O` | 64 (10 refuted, 19 known; 59 with outside checks) | RESEARCH_SA22, RESEARCH_SA22_run2 | `A1-global-refutation`, `A:04`, `A:04-exact-image`, `A2-explicit-limits`, `A1-nontoric-cut`, `A1-bordered-landing`, `A1-toric-noninjective`, `A1-toric-nondescent` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_2_178-194\185_OBJ_H0BF_O` | 22 (4 refuted, 6 known; 20 with outside checks) | RESEARCH_SA17 | `B:crystal-counterexamples`, `B:finite-PD`, `B:PD-not-QSyn`, `B:largest-literature-class`, `B:closure-reduction`, `B:L6-refutation`, `B:square-zero-Hom`, `B:effectivity` | - | [EGA_FR, EGA_EN, FGA_FR, SGA3_EN] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_2_178-194\186_OBJ_H05A-1_O` | 19 (8 refuted, 1 known; 4 with outside checks) | RESEARCH_SA10 | `C5.08`, `C2.04`, `C5.02`, `C5.04`, `C5.07`, `C2.01`, `C5.03`, `C5.06` | - | [EGA_FR, EGA_EN, FGA_FR] |
| `F_Archive_working_through_200\17_working_through_wave5_161-200\batch_3_195-200\196_OBJ_H054-1_O` | 3 (0 refuted, 0 known; 3 with outside checks) | RESEARCH_SA08 | `A-005`, `A-007`, `A-008` | - | [EGA_FR, EGA_EN, FGA_FR, SGA3_EN] |
| `E_Archive_small_prompts_54\16_small_batch_2_18-34\24_SA20_Autour_dEsquisse_dun_programme` | 148 (37 refuted, 14 known; 148 with outside checks) | RESEARCH_SA20 | `A.104`, `A.106`, `A.111`, `A.701`, `A.101`, `A.112`, `A.703`, `D.002` | - | [] |
| `E_Archive_small_prompts_54\16_small_batch_2_18-34\33_WTA_22_020-030` | 13 (4 refuted, 1 known; 13 with outside checks) | RESEARCH_SA23 | `SA23-A-05`, `SA23-A-09`, `SA23-A-11`, `SA23-A-12`, `SA23-A-13`, `SA23-A-01`, `SA23-A-02`, `SA23-A-03` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN] |
| `E_Archive_small_prompts_54\16_small_batch_3_35-51\36_WTB_22_020-030` | 13 (4 refuted, 1 known; 13 with outside checks) | RESEARCH_SA23 | `SA23-A-05`, `SA23-A-09`, `SA23-A-11`, `SA23-A-12`, `SA23-A-13`, `SA23-A-01`, `SA23-A-02`, `SA23-A-03` | - | [EGA_FR, EGA_EN, FGA_FR, SGA4_FR, SGA4_EN] |

The headline links:
- **062 H06P+H065+H064, cote 29/061-066, D.1/D.2 finiteness.** Their main question is now the run's open
  D:fixed-boundary-gate. D:boundary-neighborhood is proved, and D:wild-genus2-single-curve refutes universal tameness.
- **170 H06N.** It carries the C-part verdicts: 29/139 false (C:cusp-all-subgroups, C:normal-counterexample); 29/141 true as
  written (C:literal-141, targeted check); the 29/191-207 refutations.
- **014 H0AK, cote 4.** It carries prop:OC-product-integral-counterexample (8.3 fails), thm:plane-char2-all-groups,
  thm:all-X-explicit-positive-rank, A2-EXACT and A2-UNIT.
- **131 H0B8.** It carries B:crystal-counterexamples (the Dieudonné functor is not full; the non-reduced case is classical,
  per the S17a note) and B:PD-not-QSyn.
- **065 H04F.** It carries the 18:11 table A.2.2-A.2.6.
- **165 H0D8 and 057 H0DJ-1.** They carry geo-H (the Lidskii proof in his hand on 1:79-80, against Robert 2017).
- **025 H0CO and 133 H0CQ.** They carry A.701-A.704 and the Additif A.101-A.112.
- **182 H0KV.** It carries the capping refutation, image 0 < |q| < 16.
- **020 H0KN.** It carries the thesis-list rows of SA22 and run 2, including B.90 (known before: SGA 2 XIII note 23,
  Hamm-Lê 1990).
- **009 H09Z.** It carries G1 (partly known: Poonen-Rains 3.12(f)).

## Lint results

`python -I -B claude_tools/push_rule_pro_prompts.py --lint-math PROMPT.md` was run on all 48 object and range prompts, and
`--lint` on 24_SA20: **49 of 49 PASS**. Before the change, the same lint failed on every F object and on WTA/WTB, for
example 170 and 33. The missing rules were (E) `latex_sources/` and (F) no source copies. 24_SA20 passed `--lint` before
and after. ZIP integrity: `testzip` passes for all 49. Each folder still holds only PROMPT.md and its one ZIP; the F batch
folders' `_SPACE_FILES_*` are untouched. These are not paper-writing prompts, so `paper_completeness_lint.py` does not apply.

## Left alone, and why

- **No row on their pages:** E 32_WTA_1_051-064 and 35_WTB_1_051-064 (cote 1, scans 51-64), and 34_WTA_81_002-011 and
  37_WTB_81_002-011 (cote 81). SA23's cote-1 rows sit on scans 28-30 and 79-80, outside 51-64. No sweep-3 run worked on
  cote 81.
- **F objects with no row on their cited pages:** 005, 006, 010-013, 015, 019, 021, 022, 026, 027, 042, 055, 056, 059, 060,
  064, 066, 067, 069, 075, 076, 080, 081, 096, 109-111, 113, 114, 118-121, 123, 129, 130, 132, 134, 135, 150, 163, 164,
  167-169, 172-175, 177, 178, 183, 188, 189.
- **Cote 156 (056, 110, 164).** SA21's rows cite 156-4 to 156-9, not 156-1 or 156-2.
- **The six dropped candidates** listed above.
- **Cote 105 (027, 081, 135, 189).** The DERIVATEURS cluster names findings at 105/020 (interval generation fails for
  integral homology, DER_LOCALIZERS B.3, B.4, B.10) and 105/052 (FREX A2.8; W7 bis). Those runs are outside the 18
  registers I parsed, and they come from another cluster's agent. They are flagged here for that agent, or for the main
  session, and were not changed by me.
- **Cote 8 (POLISH_CRISTAUX S15i at 8:49, S15j at 8:81).** 068 H0AE already receives SA15's 8:81 rows
  (thm:DE-split). The POLISH_CRISTAUX papers were not added: they are outside the sweep-3 registers and their check state
  sits with the AG_POLISH cluster.

## New-prompt proposals (not built; the main session decides)

1. **Cote 57:97-100, the boxed "noyau nul si n ≥ 4"** (Pic(X) → Pic(Y) injective for ample sections in dimension ≥ 4).
   - **Main question.** Universal point injectivity Pic(X)(k) → Pic(Y)(k) for smooth ample (very ample) Y in dimension ≥ 4
     (SA14 A1/A2), proved or refuted. The scheme-level (α_p) reading already fails for ample divisors in every dimension:
     Cotner-Zavyalov Ex. 3.3.6, per MAP_GEOMETRY O5 (read there through POLISH_CRISTAUX Paper 1).
   - **What exists.**
     - SA14 A1 and A1r reduce the question to n = 4.
     - A4b: the kernel is a finite unipotent infinitesimal p-group.
     - A3 (posted, hexagon:2611.00936) is the surface case.
     - POLISH_ALGEBRAIC_GEOMETRY P90e gives the positive-excess bound.
   - **Why a new prompt.** No waiting prompt covers those scans, apart from 063 H09X, whose object is Hua's links.
   - **Inputs.** SA14 `sections/A.tex`; the P90e and P90h proofs (POLISH_AG cp35 `paper_02`); Kweon's Question 7.7.
2. **Cote 100:3 2), reduced S with finite normalization** (his boxed hypothesis, 100:7).
   - **Main question.** The extension assertion for reduced bases with finite normalization, proved or refuted.
   - **What exists.** SA15 C-RD11 (reduced, geometrically unibranch, non-finite normalization: false); C-RD4 (non-reduced:
     false); C-RD1 (Corollary 3 holds); POLISH_CRISTAUX Paper 4 (S15e).
   - **Why a new prompt.** No waiting prompt holds cote 100.
   - **Inputs.** SA15 Part C sources; Ferrand-Raynaud; Olberding.
3. **Cote 14:106-112, the C.3 local restriction table: finishing the rows read only in part** (C.3bl's auxiliary
   proposition, C.3bt's totalization file, C.3bu-bw), together with the rational top quotient in characteristic 0.
   - **Why a new prompt.** No waiting object prompt holds these scans: 070 H03S-1 is the reused typescript.
   - **Inputs.** SA06 `agents/cycles/local_*_classification.tex`; Kollár's local Picard papers.
4. **Not proposed.** These already have a home:
   - SA12 A2 (cote 31) is Paper 1 of POLISH_ALGEBRAIC_GEOMETRY;
   - SA06 C.4 is a paper for the Fable conference;
   - SA17 cote 131 is Paper 3 of POLISH_ALGEBRAIC_GEOMETRY;
   - SA07 F.3.32/F.3.33 belongs to the Longue Marche expert.


## Second pass, 24 Nov 2026: the maps MAP_GEOMETRY.md and MAP_NUMBER_THEORY.md

- **Added to eight prompts.** A paragraph "Later inputs" was inserted before the LaTeX paragraph of each. The files went into `<TAG>_settled/later_inputs/`.
  - **014 H0AK.**
    - POLISH_CRISTAUX Paper 1: `thm:all-primes`, `thm:intro-injectivity` and `thm:regularity` (cp34 l.115, 123 and 825).
    - Paper 6: `thm:ordinary` and `thm:odd`.
    - Cotner-Zavyalov Ex. 3.3.6, and the CEZB/CST obstruction marked as known.
    - The NK8 template, as the question beyond `thm:plane-char2-all-groups`.
  - **176 H0A9.** Paper 9 (`thm:nolift`, `thm:integral-rational-injection`, `thm:affine`, `thm:affine-second-torsion`), and the Ertl-Shiho-Sprang e-print (arXiv 2105.11009, LaTeX).
  - **131 H0B8.** The NK9 chain (Mok-Xu, then lci, then Anschütz-Le Bras 4.74). The question beyond it: full faithfulness over reduced rings with pd Ω infinite. The S17a note TeX is attached.
  - **062.** POLISH_AG Paper 1 `thm:boundary` (= D:boundary-neighborhood), and Paper 2 Thm 1.12 (= SA14 F11), with their TeX.
  - **009.** Paper 2 Thm 1.1 (= G1), with its credits.
  - **33 and 36.** POLISH_AG Paper 4 (= SA23 D-3, A-16, B2-2), with its TeX.
  - **065.** POLISH_TOPOLOGY_PERIODS Paper 3 (= SA07 A.2), as a pointer only; no file was added.
- **Items of the maps that touch none of the waiting prompts' pages:**
  - SA05 A:class / A:hasse (15:2-14): known, Milne math/0607569, Props 2.4-2.6 and Rem. 2.7.
  - SA12 B.1 / L6c (29/070-071): Marrama 2026 Thm 6 = Moret-Bailly 1985, Lemme 2.
  - Cote 57:97-100.
  - SA14 J5 = JAC1964 H9-C1 (cote 44).
  - NK4 (cote 133).
  - NK-7, Kahn with Milne, for SA05 prop:B-diagonal-Chow-gate (12:60-73).

  They changed no prompt. Proposal 1 is reframed above.
- **Dates.** "25 Nov" was changed to "24 Nov" in the new paragraphs. The coordinator had already fixed the earlier sections. The `SETTLED.tsv` column is still named `topicality_25nov`.

## Rule fix on the other waiting working-through prompts, 24 Nov 2026

The fix was applied to the 64 F object prompts without a backup folder and to E 32, 34, 35 and 37, 68 prompts in all.
- **Backup.** Each folder was copied to `_backups_20261125/` first.
- **ZIP.** The LaTeX packs each prompt names were added with `latex_sources.py add`: EGA FR/EN, FGA FR, and the SGA volumes named in the prompt or its entries and passages.
- **PROMPT.md.** The (E) paragraph was added in all 68 and the (F) paragraph in 64, the four E prompts already having (F). Both went before `## How to work`. Nothing else was changed.
- **Result.** All 68 pass `--lint-math` and `testzip`. The log is `scratchpad/topsweep3/rulefix_log.txt`.

## Addendum: cote 8 and cote 136 rows from the AG_POLISH cluster (24 Nov 2026)

By the AG_POLISH cluster reader (Claude Opus 5.5 at effort high), on the main session's message. Script:
the scratchpad file `agpolish/addrows.py`. Each ZIP was rewritten with every existing member kept, the extended
`SETTLED.tsv` and the run's TeX under `<TAG>_settled/sources/<run>/`. An "Added 24 Nov 2026" paragraph and its rows
went into the "Decided since" section, before the standing-rule paragraphs. The backups in `_backups_20261125/` were
not touched. After the change, `--lint-math` passes on all four prompts, and `testzip` passes on all four ZIPs.

- **068 H0AE (8:79-81) and 122 H0AD+H0AJ (8:78).** Six POLISH_CRISTAUX rows each (S15j, merged checkpoint 33, Paper 8):
  thm:sections, lem:transvection, lem:lift, thm:surface, thm:minrank, thm:curve.
- **115 H052 and 142 H04L-1 (136:111, 117-121).** Four ARCH_ALG rows each: ARCH-136-PATHS, -FRACTIONS, -HOM-SEMILOCAL
  and -ARITH-BOUND.
- **S15i (Lubin-Tate, cote 8, printed sheets 47 and 49, PDF images 48 and 50) was added nowhere.** No waiting F object
  cites those pages; 176 H0A9 cites cote 7:28 and 61-72 only, with its cote-8 numbers being cross-references.
- **Not duplicated.** Some cluster findings fall on cited pages already covered by the sweep-3 rows of the same
  statements:
  - CRISTAUX Papers 1 and 3 on 014 H0AK (cote 4), which already holds SA15's OC and A2 rows;
  - POLISH_TOPOLOGY_PERIODS Paper 3 on 065 H04F (18:11), which already holds SA07's A.1-A.3 rows with our checks;
  - Paper 2 on the cote 119, 150 and 153 objects (SA20 rows);
  - Paper 4 on the cote 66-67 objects (SA22 rows).
