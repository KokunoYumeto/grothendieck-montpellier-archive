# INTAKE_B_TOWERS: update of 24 November 2026

By Claude Opus 5.5 at effort high (agent a7e00c630a8f698c6), 24 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort max), following `../PROMPT_UPDATE_BRIEF.md`. Verdicts behind the changes: `../TOPICALITY_LONGUE_MARCHE.md`, `../MAP_GALOIS_ANABELIAN.md` (N1-N6), `../LONGUE_MARCHE_A.md`, `../LONGUE_MARCHE_B.md`; `../OLDER_RUNS.md` was read (its Longue Marche entries: H07 stage W, H16, LM1/LM3/LM8_LIE covered elsewhere; nothing further for these prompts). Proposals and the list for prompt 95: `LONGUE_MARCHE_PROPOSALS_AND_95.md`.

**Sent?** Not in `TO_SEND/PRO/SENT_PRO.tsv` (batch 2 of the small archive prompts is sent only for 18-23) and not in a SENT folder. **Backup:** `TO_SEND/PRO/_backups_20261125/<folder>/` (whole folder, before any change).

Its runs still point at their newest returns: LM7_FERMAT_TOWER (14 Nov), LM7_PUSH cp09, FERMAT_SUCCESSOR cp06, LM8_PUSH cp17, EXIT_TOWER
cp28, GT_TOWER_CHECK cp10. I listed `answers/` and found nothing newer. I made no change to the run table.

## Changes to PROMPT.md

1. **A new section, "Settled, checked and published since this prompt was built (19-25 November 2026)"**, before "How to
   work". It holds six items:
   - **Item 1: Δ = 0 on GT̂ is published** (hexagon:2611.00940), by a route independent of EXIT_TOWER E.42-E.44 and
     GT_TOWER_CHECK A.6.
     - Check records: h17 `RECORDS.md`; the Hexagon board row H17 (ae4ae3dc's exhaustive Z/12 check of E.264-E.268);
       `REFEREE_E42_E43_A6_a49aabbf.md`.
     - Asks for independent re-proofs of LM7_PUSH E.65 and E.58, the inputs of Corollary 4 (RECORDS §1, last two rows).
   - **Item 2: GT̂ ⊊ GT̂₀; no published work has it.** The rows: LM8_PUSH C.30 (the ℵ₀ quadratic family; `sections/C.tex`
     l. 2650, corrected on 24 Nov at the mapper's word: I had first taken C.30 for a passage step), C.31, C.33, C.35, C.39;
     GT_TOWER_CHECK A.7 and B.2.25-B.2.30.
     - Evidence: Dolgushev-Guynee 2401.06870 TeX line 378 ("obviously contains"); Furusho math/0702128 (abstract and
       TeX line 65).
     - The checked graded input (`../LONGUE_MARCHE_A_checks/check_w12_brackets.py`, `check_lm2_graded.py`).
     - Asks for full checks of LM8_PUSH P.2-P.4, C.30, C.32 and the C.35 certificate; the C.46 sign convention
       (`check_c46.py`); and the question of the quotient as a section-7 item.
   - **Item 3: Fermat for Selmer sections.** Steklov's two errors, with their locators as in the INTAKE_A report; the
     cluster checks (`check_fermat_cusp.py`, `check_quintic.py`; `../LONGUE_MARCHE_A.md` items 2 and 10). Asks for D.23's
     global part and n = 3, 5, 7, a comparison with Steklov Thm 5.2 / Prop. 5.1, the A.53 locator, and A.52's inputs.
   - **Item 4: EXIT_TOWER against the literature.**
     - E.45 against Boggi 2011.15075v6, its main theorem (abstract opened; version date from arXiv).
     - E.48, E.14 and E.54: the latest versions are unchanged (Boggi v6 22 Apr 2026; Boggi-Funar 2311.17025v3
       7 Jan 2026; Corob Cook-Vannacci 1907.05063v3 25 Jun 2020; arXiv abstract pages).
     - E.60 is known in substance (topicality verdict).
     - D.50-D.106 against Gaifullin 2611.20353 and Pshenichnyi 2611.24813 (abstracts).
     - The general intake of EXIT_TOWER cp28, now attached.
   - **Item 5: other checks of the cluster readers**, and a reading flag. GT_TOWER_CHECK B.5 says the scans show 1/4.
     Our transcription in the SA31 package (`MPL_148_029-072_transcription.tex`, scan 31, line 123) reads `tw_{1/3}` on
     the arrow into III₁. The scans decide, on our side.
   - **Item 6: the Galois/anabelian map.**
     - N1: E.45 settled for Out* by Lochak 2025 Thm 5.10 with H17, with the two gates and r_{g,n} = Lochak's lego action.
     - N4: the Galois-trivial characters are tests of G_Q = GT̂, decided on Λ₀.
     - N5: C.34's a_n = dim W_n; asks for the F₁₇ weight-16 pentagon computation.
     - N6: the correction to the note's line 158.

     All of these are marked as the mapper's proofs with no second reader.
2. **Section 7** now includes the new questions. **The literature line** names zip 6. **The material list** has a bullet
   for `INTAKE_B_6_updates_20261124.zip`.

Unchanged: the run table, the 1,358-row scope, the D.72 paragraph, every rule.

## Changes to the ZIP

The ZIP was repacked with every original member (2,137) kept and `INTAKE_B_6_updates_20261124/` added. It holds:
- earlier documents: `LONGUE_MARCHE_A.md` and `LONGUE_MARCHE_B.md` with six check-event files and
  `LONGUE_MARCHE_A_checks/`; the topicality files; the general intake of EXIT_TOWER with `pro_intake_20261119/CHECK_EVENTS.tsv`;
  the h17 note set; DELTA_SEXTIC; the map set;
- literature: the e-prints of 2602.17746, 2602.12462, 2401.06870, 2008.00066, math/0702128, 2011.15075, 2311.17025,
  2406.08639, 1907.05063, 2611.20353 and 2611.24813; Lochak 2025 and Furusho 2002 as PDFs.

It has its own MANIFEST and WHO_WROTE_WHAT. The archive holds no ZIP inside it.

## Lint

- `push_rule_pro_prompts.py --lint PROMPT.md`: files: 1 failing lint: 0
- `--lint-math`: files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\7_Longue_Marche_intakes\18_Pro_intakes_Longue_Marche_thin_runs\INTAKE_B_TOWERS\PROMPT.md [] push rule present: False checkpoint rule present: True missing: none The backup of 19 Nov gives the same result (files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\_backups_20261125\INTAKE_B_TOWERS\PROMPT.md [] push rule present: False checkpoint rule present: True missing: none). This prompt is not a research prompt and carries no push paragraph by design; `--lint` is the lint its builder used and the one the rules ask for ("`--lint` for any other").
- `paper_completeness_lint.py`: not applicable (the prompt writes no paper).

## Result

`INTAKE_B_TOWERS.zip`: 2227 members, 26,285,298 bytes, no ZIP inside; the send folder holds only PROMPT.md and this ZIP. SHA-256 of the new ZIP: 03f146624e84ef23730684079a416119a8d37a5c97df0c92ec097adc6fde4fe8.
