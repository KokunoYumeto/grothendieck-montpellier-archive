# 31_SA28_Autour_de_La_Longue_Marche_travers_la_th_part1: update of 24 November 2026

By Claude Opus 5.5 at effort high (agent a7e00c630a8f698c6), 24 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort max), following `../PROMPT_UPDATE_BRIEF.md`. Verdicts behind the changes: `../TOPICALITY_LONGUE_MARCHE.md`, `../MAP_GALOIS_ANABELIAN.md` (N1-N6), `../LONGUE_MARCHE_A.md`, `../LONGUE_MARCHE_B.md`; `../OLDER_RUNS.md` was read (its Longue Marche entries: H07 stage W, H16, LM1/LM3/LM8_LIE covered elsewhere; nothing further for these prompts). Proposals and the list for prompt 95: `LONGUE_MARCHE_PROPOSALS_AND_95.md`.

**Sent?** Not in `TO_SEND/PRO/SENT_PRO.tsv` (batch 2 of the small archive prompts is sent only for 18-23) and not in a SENT folder. **Backup:** `TO_SEND/PRO/_backups_20261125/<folder>/` (whole folder, before any change).

This is a notes-consolidation dossier: Stages 1-6 on Grothendieck's pages, which its prompt asks to read "in its own terms",
with our projects kept to Stage 5. The additions respect that. Published work goes to the fates and the state of the art
(Stages 2 and 3), with locators. Our unpublished run results are leads for the Stage 5 table, each with its check state.
A reading flagged by the mathematics goes to Stage 4 and is not decided. The stages, rules, return format, check events
and checkpoints are unchanged.

## Changes to PROMPT.md

1. **The attachments list** has a third bullet, `SA28_updates_20261124.zip`, and "Unzip both" now reads "Unzip all three".
2. **A new section, "Literature and our results since the notes were written (added 25 November 2026)"**, before
   "Rules", with an introduction on how to use it. Its bullets:
   - **The two cyclic equations without the pentagon.** For scan 025 and note N025.5 in `MPL_142_001-093_notes.md`
     line 667, which I opened:
     - published: Harbater-Schneps GT̂₀; Dolgushev-Guynee p. 2; Furusho math/0702128;
     - leads: LM8_PUSH C.39, GT_TOWER_CHECK A.7, LM2 B.m2.
   - **Invertibility of the lifts.** LS2006 Q1.1 and Q1.4; the lead is LM4_SUCCESSOR C.30, checked.
   - **The Galois action on the Teichmüller tower in higher genus.** Nakamura-Schneps, Hatcher-Lochak-Schneps, LNS 2026,
     hexagon:2611.00940, Basualdo Bonatto-Robertson; then Lochak 2025 and Furusho 2002, and the map's N1 as a lead with
     no second reader.
   - **Leads on cotes 142 and 143.** A1_SUCCESSOR B.93 (cote 142, scan 096); FLAGGED_149 G1-G11 and Z142a-g (cote 142,
     scans 5-21); EXIT_TOWER E.T1-E.T13, E.77 and E.X1 (cote 143).

## Changes to the ZIP

The ZIP was repacked with every original member kept and `SA28_updates_20261124/` added, with its own MANIFEST and
WHO_WROTE_WHAT. It holds:
- `ours_published/`: the h17 note as deposited;
- `literature/`: Lochak-Schneps 2006, Lochak 2025 and Furusho 2002 as PDFs, and the e-prints of 2602.12462, 2606.01466,
  2401.06870 and math/0702128;
- `ours_leads/FLAGGED_149/`: the report and the results and readings tables.

## Lint

- `push_rule_pro_prompts.py --lint PROMPT.md`: files: 1 failing lint: 0
- `--lint-math`: files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\E_Archive_small_prompts_54\16_small_batch_2_18-34\31_SA28_Autour_de_La_Longue_Marche_travers_la_th_part1\PROMPT.md [] push rule present: False checkpoint rule present: True missing: ['LaTeX of EGA/SGA/FGA attached as latex_sources/ (E): claude_tools/latex_s The backup of 19 Nov gives the same result (files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\_backups_20261125\31_SA28_Autour_de_La_Longue_Marche_travers_la_th_part1\PROMPT.md [] push rule present: False checkpoint rule present: True missing: ['LaTeX of EGA/SGA/FGA attached as latex_sources/ (E): claude_tools/latex_sources.py']). This prompt is not a research prompt and carries no push paragraph by design; `--lint` is the lint its builder used and the one the rules ask for ("`--lint` for any other").
- `paper_completeness_lint.py`: not applicable (the prompt writes no paper).

## Result

`SA28_Autour_de_La_Longue_Marche_travers_la_th_part1.zip`: 110 members, 4,371,981 bytes, no ZIP inside; the send folder holds only PROMPT.md and this ZIP. SHA-256 of the new ZIP: 52e82a57861dd39bd249c01ec023270942f06c434b40a3584b98764dd582efeb.
