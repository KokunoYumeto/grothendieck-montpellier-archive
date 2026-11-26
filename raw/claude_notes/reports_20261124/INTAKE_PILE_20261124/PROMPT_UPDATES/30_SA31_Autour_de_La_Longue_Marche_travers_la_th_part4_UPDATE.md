# 30_SA31_Autour_de_La_Longue_Marche_travers_la_th_part4: update of 24 November 2026

By Claude Opus 5.5 at effort high (agent a7e00c630a8f698c6), 24 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort max), following `../PROMPT_UPDATE_BRIEF.md`. Verdicts behind the changes: `../TOPICALITY_LONGUE_MARCHE.md`, `../MAP_GALOIS_ANABELIAN.md` (N1-N6), `../LONGUE_MARCHE_A.md`, `../LONGUE_MARCHE_B.md`; `../OLDER_RUNS.md` was read (its Longue Marche entries: H07 stage W, H16, LM1/LM3/LM8_LIE covered elsewhere; nothing further for these prompts). Proposals and the list for prompt 95: `LONGUE_MARCHE_PROPOSALS_AND_95.md`.

**Sent?** Not in `TO_SEND/PRO/SENT_PRO.tsv` (batch 2 of the small archive prompts is sent only for 18-23) and not in a SENT folder. **Backup:** `TO_SEND/PRO/_backups_20261125/<folder>/` (whole folder, before any change).

This is a notes-consolidation dossier: Stages 1-6 on Grothendieck's pages, which its prompt asks to read "in its own terms",
with our projects kept to Stage 5. The additions respect that. Published work goes to the fates and the state of the art
(Stages 2 and 3), with locators. Our unpublished run results are leads for the Stage 5 table, each with its check state.
A reading flagged by the mathematics goes to Stage 4 and is not decided. The stages, rules, return format, check events
and checkpoints are unchanged.

## Changes to PROMPT.md

1. **The attachments list** has a third bullet, `SA31_updates_20261124.zip`, and "Unzip both" now reads "Unzip all three".
2. **A new section, "Literature and our results since the notes were written (added 25 November 2026)"**, before
   "Rules", with an introduction on how to use it. Its bullets:
   - **Scan 052.** Carlson-Stix v2, Theorems A, B and D (the package's note C052.1 in `MPL_149_001-090_notes.md` l. 716
     cites CHW only), and CHW Theorem 0.1 and Examples 2.30-2.31. Leads: LM5 F.50, ANABELIAN_149_PUSH F.45,
     A1_SUCCESSOR B.137-B.147 and B.49-B.55.
   - **Scans 035-036.** Saïdi-Tamagawa 2009 and Mochizuki 1999 are the literature; A1 (unposted, with its check state) is
     the lead. The note B036.1 (l. 479) reads his question as about the full section map, so the run is asked to settle
     on the page what (*) is.
   - **Scan 032.** A1_SUCCESSOR C.2.
   - **Scans 056 and 126-127.** BKL and Li-Lüdtke as published special cases. Leads: SECTIONS_OVER_Q, SECTION_GHOSTS
     D.2, and the map's N2 (Proposition L, no second reader).
   - **Scan 085.** K17 (H16).
   - **Cote 148, Stage 4.** `MPL_148_029-072_transcription.tex`, scan 31, line 123 reads τ_{π,ρ} = tw_{1/3} into III₁;
     GT_TOWER_CHECK B.5 claims the scans show 1/4. The 1080 relators of EXIT_TOWER B.25 and GT_TOWER_CHECK B.5 come with
     the count 1079 = 1620 − 542 + 1, checked in `pro_intake_20261119/CHECK_EVENTS.tsv` (EXIT_TOWER B.13, ae4ae3dc).
   - **The Galois action on the tower (cote 148).** LNS, hexagon:2611.00940, LS2006, Dolgushev-Guynee, Lochak 2025,
     Furusho 2002; the map's N1 as a lead.
   - **Cote 149, his doubts.** The FLAGGED_149 report and tables are attached as leads (19 of 107 rows checked).

## Changes to the ZIP

The ZIP was repacked with every original member kept and `SA31_updates_20261124/` added. It holds:
- `ours_published/`: the h17 note;
- `literature/`: LS2006, Lochak 2025 and Furusho 2002 as PDFs, and the e-prints of 2410.22474, 2407.19920, 0801.1452,
  2305.09462, 2608.20615, 2602.12462 and 2401.06870;
- `ours_leads/FLAGGED_149/`.

## Lint

- `push_rule_pro_prompts.py --lint PROMPT.md`: files: 1 failing lint: 0
- `--lint-math`: files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\E_Archive_small_prompts_54\16_small_batch_2_18-34\30_SA31_Autour_de_La_Longue_Marche_travers_la_th_part4\PROMPT.md [] push rule present: False checkpoint rule present: True missing: ['LaTeX of EGA/SGA/FGA attached as latex_sources/ (E): claude_tools/latex_s The backup of 19 Nov gives the same result (files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\_backups_20261125\30_SA31_Autour_de_La_Longue_Marche_travers_la_th_part4\PROMPT.md [] push rule present: False checkpoint rule present: True missing: ['LaTeX of EGA/SGA/FGA attached as latex_sources/ (E): claude_tools/latex_sources.py']). This prompt is not a research prompt and carries no push paragraph by design; `--lint` is the lint its builder used and the one the rules ask for ("`--lint` for any other").
- `paper_completeness_lint.py`: not applicable (the prompt writes no paper).

## Result

`SA31_Autour_de_La_Longue_Marche_travers_la_th_part4.zip`: 83 members, 3,762,921 bytes, no ZIP inside; the send folder holds only PROMPT.md and this ZIP. SHA-256 of the new ZIP: 33129a3dfe652315ae1d64138beceff5844978018143e5f58ecfdd41492553fd.
