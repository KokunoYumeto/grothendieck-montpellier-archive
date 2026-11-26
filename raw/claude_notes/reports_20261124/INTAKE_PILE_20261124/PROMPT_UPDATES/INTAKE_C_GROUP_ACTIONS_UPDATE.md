# INTAKE_C_GROUP_ACTIONS: update of 24 November 2026

By Claude Opus 5.5 at effort high (agent a7e00c630a8f698c6), 24 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort max), following `../PROMPT_UPDATE_BRIEF.md`. Verdicts behind the changes: `../TOPICALITY_LONGUE_MARCHE.md`, `../MAP_GALOIS_ANABELIAN.md` (N1-N6), `../LONGUE_MARCHE_A.md`, `../LONGUE_MARCHE_B.md`; `../OLDER_RUNS.md` was read (its Longue Marche entries: H07 stage W, H16, LM1/LM3/LM8_LIE covered elsewhere; nothing further for these prompts). Proposals and the list for prompt 95: `LONGUE_MARCHE_PROPOSALS_AND_95.md`.

**Sent?** Not in `TO_SEND/PRO/SENT_PRO.tsv` (batch 2 of the small archive prompts is sent only for 18-23) and not in a SENT folder. **Backup:** `TO_SEND/PRO/_backups_20261125/<folder>/` (whole folder, before any change).

Its runs still point at their newest returns: the LM1_GROUP_SCHEMES rerun (12 Nov), LM4_FINITE_GROUP_ACTIONS (14 Nov 04:06),
LM4_SUCCESSOR cp40. Nothing is newer. I made no change to the run table.

## Changes to PROMPT.md

1. **A new section, "Settled, checked and published since this prompt was built (19-25 November 2026)"**, before "How to
   work". It holds six items:
   - **Item 1: C.29-C.31 answer Lochak-Schneps 2006, Question 1.1.**
     - Statements, the proof's location (`work_CE/C_further.tex` l. 474-740, which is in zip 1) and the cluster reader's
       checks (`../LONGUE_MARCHE_A.md` item 3; `INTAKE_LM4_SUCCESSOR_20261124_CHECK_EVENTS.tsv`).
     - Evidence for novelty: Lochak-Schneps 2006 §1, Q1.1 (opened, `textes/farb.pdf`, the text quoted);
       Dolgushev-Guynee 2401.06870, Def. 2.5 (TeX); Dolgushev-Le-Lorenz 2008.00066 §4.3.
     - Asks for checks of the BHR inputs and a literature search for C.29.
     - Next questions: endomorphisms of the tower for IΓ and Λ; finite level, the GT-shadows (DLL Question 4.4 is a
       neighbouring one).
   - **Item 2: A.6** against LS2006 Q1.4.
   - **Item 3: LM4_FINITE_GROUP_ACTIONS D.30, D.21 and D.29**: what is checked and what is not.
   - **Item 4: Boggi-Zalesskii 2406.08639v2** (the latest version) does not decide F.7 or Main B.
   - **Item 5: the GT line elsewhere**: hexagon:2611.00940, and LM8_PUSH C.30-C.39 for A.13 and A.100-A.105.
   - **Item 6: the map's N1 and N4**, marked as having no second reader.
2. **Section 7**, **the literature line** and **the material list** are updated as in INTAKE_A.

## Changes to the ZIP

The ZIP was repacked with every original member (300) kept and `INTAKE_C_6_updates_20261124/` added. It holds:
- earlier documents: `LONGUE_MARCHE_A.md` with two check-event files and `check_c30_a5.py`/`.out`; the topicality files;
  the map with its table and events;
- literature: Lochak-Schneps 2006 as a PDF (no TeX online), and the e-prints of 2401.06870, 2008.00066, 1703.05143,
  1504.01605 and 2406.08639.

## Lint

- `push_rule_pro_prompts.py --lint PROMPT.md`: files: 1 failing lint: 0
- `--lint-math`: files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\7_Longue_Marche_intakes\18_Pro_intakes_Longue_Marche_thin_runs\INTAKE_C_GROUP_ACTIONS\PROMPT.md [] push rule present: False checkpoint rule present: True missing: none The backup of 19 Nov gives the same result (files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\_backups_20261125\INTAKE_C_GROUP_ACTIONS\PROMPT.md [] push rule present: False checkpoint rule present: True missing: none). This prompt is not a research prompt and carries no push paragraph by design; `--lint` is the lint its builder used and the one the rules ask for ("`--lint` for any other").
- `paper_completeness_lint.py`: not applicable (the prompt writes no paper).

## Result

`INTAKE_C_GROUP_ACTIONS.zip`: 324 members, 5,321,400 bytes, no ZIP inside; the send folder holds only PROMPT.md and this ZIP. SHA-256 of the new ZIP: abda58fb73faa3ffe0077280dc86f0520d5e6b8fdd55d7a9fa7f9b6ee1ae8a0a.
