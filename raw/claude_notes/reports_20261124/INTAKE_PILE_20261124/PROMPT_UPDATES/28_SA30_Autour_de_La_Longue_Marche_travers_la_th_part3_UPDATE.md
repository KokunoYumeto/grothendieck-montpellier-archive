# 28_SA30_Autour_de_La_Longue_Marche_travers_la_th_part3: update of 24 November 2026

By Claude Opus 5.5 at effort high (agent a7e00c630a8f698c6), 24 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort max), following `../PROMPT_UPDATE_BRIEF.md`. Verdicts behind the changes: `../TOPICALITY_LONGUE_MARCHE.md`, `../MAP_GALOIS_ANABELIAN.md` (N1-N6), `../LONGUE_MARCHE_A.md`, `../LONGUE_MARCHE_B.md`; `../OLDER_RUNS.md` was read (its Longue Marche entries: H07 stage W, H16, LM1/LM3/LM8_LIE covered elsewhere; nothing further for these prompts). Proposals and the list for prompt 95: `LONGUE_MARCHE_PROPOSALS_AND_95.md`.

**Sent?** Not in `TO_SEND/PRO/SENT_PRO.tsv` (batch 2 of the small archive prompts is sent only for 18-23) and not in a SENT folder. **Backup:** `TO_SEND/PRO/_backups_20261125/<folder>/` (whole folder, before any change).

This is a notes-consolidation dossier: Stages 1-6 on Grothendieck's pages, which its prompt asks to read "in its own terms",
with our projects kept to Stage 5. The additions respect that. Published work goes to the fates and the state of the art
(Stages 2 and 3), with locators. Our unpublished run results are leads for the Stage 5 table, each with its check state.
A reading flagged by the mathematics goes to Stage 4 and is not decided. The stages, rules, return format, check events
and checkpoints are unchanged.

## Changes to PROMPT.md

1. **The attachments list** has a third bullet, `SA30_updates_20261124.zip`, and "Unzip both" now reads "Unzip all three".
2. **A new section, "Literature and our results since the notes were written (added 25 November 2026)"**, before
   "Rules", with an introduction on how to use it. Its bullets:
   - **The Galois action on the Teichmüller groupoids (cote 146) and on the tower.**
     - Published: Nakamura-Schneps, HLS, LNS 2026 (with §8), hexagon:2611.00940, Boggi 2011.15075v6, Basualdo
       Bonatto-Robertson, LS2006, Lochak 2025, Furusho 2002.
     - Leads: EXIT_TOWER E.14 against Boggi; the map's N1.
   - **Leads on cotes 146 and 147.** EXIT_TOWER (cote 147 rows A.4-A.15 and C.1, from the register's manuscript column,
     which I scanned; the Lego models B.12-B.24); LM5 F.10-F.51; the general intake of EXIT_TOWER.

## Changes to the ZIP

The ZIP was repacked with every original member kept and `SA30_updates_20261124/` added. It holds:
- `ours_published/`: the h17 note;
- `literature/`: LS2006, Lochak 2025 and Furusho 2002 as PDFs, and the e-prints of 2602.12462, 2011.15075 and
  2606.01466.

## Lint

- `push_rule_pro_prompts.py --lint PROMPT.md`: files: 1 failing lint: 0
- `--lint-math`: files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\E_Archive_small_prompts_54\16_small_batch_2_18-34\28_SA30_Autour_de_La_Longue_Marche_travers_la_th_part3\PROMPT.md [] push rule present: False checkpoint rule present: True missing: ['LaTeX of EGA/SGA/FGA attached as latex_sources/ (E): claude_tools/latex_s The backup of 19 Nov gives the same result (files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\_backups_20261125\28_SA30_Autour_de_La_Longue_Marche_travers_la_th_part3\PROMPT.md [] push rule present: False checkpoint rule present: True missing: ['LaTeX of EGA/SGA/FGA attached as latex_sources/ (E): claude_tools/latex_sources.py']). This prompt is not a research prompt and carries no push paragraph by design; `--lint` is the lint its builder used and the one the rules ask for ("`--lint` for any other").
- `paper_completeness_lint.py`: not applicable (the prompt writes no paper).

## Result

`SA30_Autour_de_La_Longue_Marche_travers_la_th_part3.zip`: 108 members, 4,369,733 bytes, no ZIP inside; the send folder holds only PROMPT.md and this ZIP. SHA-256 of the new ZIP: 84dce759de8442dfa39c51f84b9c2f11d1a5eb65ac14265eda87cd16b42c88c2.
