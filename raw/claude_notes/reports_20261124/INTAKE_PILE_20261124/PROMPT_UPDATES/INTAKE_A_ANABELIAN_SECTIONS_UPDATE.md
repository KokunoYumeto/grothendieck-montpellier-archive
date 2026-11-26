# INTAKE_A_ANABELIAN_SECTIONS: update of 24 November 2026

By Claude Opus 5.5 at effort high (agent a7e00c630a8f698c6), 24 Nov 2026, for the main session 329fb1e6 (Claude Opus 5.5 at effort max), following `../PROMPT_UPDATE_BRIEF.md`. Verdicts behind the changes: `../TOPICALITY_LONGUE_MARCHE.md`, `../MAP_GALOIS_ANABELIAN.md` (N1-N6), `../LONGUE_MARCHE_A.md`, `../LONGUE_MARCHE_B.md`; `../OLDER_RUNS.md` was read (its Longue Marche entries: H07 stage W, H16, LM1/LM3/LM8_LIE covered elsewhere; nothing further for these prompts). Proposals and the list for prompt 95: `LONGUE_MARCHE_PROPOSALS_AND_95.md`.

**Sent?** Not in `TO_SEND/PRO/SENT_PRO.tsv` (batch 2 of the small archive prompts is sent only for 18-23) and not in a SENT folder. **Backup:** `TO_SEND/PRO/_backups_20261125/<folder>/` (whole folder, before any change).

Its runs still point at their newest returns: ANABELIAN_SUCCESSOR final (16 Nov), ANABELIAN_A1 cp03 (final by the user's
word), ANABELIAN_A1_SUCCESSOR cp05 (18 Nov), SECTIONS_OVER_Q cp17, SECTION_GHOSTS final (18 Nov). I listed `longue_marche_pro_pilot_20261104/answers/`
and found nothing newer for any of them. I made no change to the run table.

## Changes to PROMPT.md

1. **A new section, "Settled, checked and published since this prompt was built (19-25 November 2026)"**, before "How to
   work". It holds six items:
   - **Item 1: SECTION_GHOSTS E.176-E.191 are published as hexagon:2611.00940v1 (23 Nov).**
     - Evidence: the Hexagon listing in `../LITERATURE_20261124.md`, appendix, and the Hexagon API dump.
     - Check record: `reports_20261123/h17_note/RECORDS.md` §§1-2 (crosswalk and check events); `reports_20261120/delta_sextic/DELTA_SEXTIC_20261121.md`
       (the re-proof of E.191).
     - Literature: Lochak-Nakamura-Schneps, arXiv:2602.12462v1, p. 2. I opened the TeX; the quotation is from §1.
     - Next questions: (III′) on GT̂, and LNS §8 (the note's "What remains open", items 1-2).
   - **Item 2: A1 is written up.**
     - Evidence: `reports_20261123/h07_note/h07_note_v3.tex`, its `RECORDS.md` and `CLAUDE_CHECK_A05_steps3to6_20261123.md`;
       the Hexagon board row H07 (stage W).
     - Literature: Saïdi-Tamagawa 0801.1452, Prop. 1.8(vi) (opened by the main session, 17 Nov); my searches of 24 Nov
       (`../TOPICALITY_LONGUE_MARCHE.md`, rows ANABELIAN_SUCCESSOR A.3 and ANABELIAN_A1 A.1/A.33/A.CR10).
     - Asks for a full check of A1_SUCCESSOR A.42-A.49, B.68 and A.51 (run only); next question A12.
   - **Item 3: the cluster readers' checks of 24 Nov** (`../LONGUE_MARCHE_B.md`, table "What I checked") and the general
     intake of SECTIONS_OVER_Q cp17 (`pro_intake_20261119/`, built after this prompt). The Pan and Helm-Voloch checks come
     first.
   - **Item 4: known results labelled Proved.** SECTION_GHOSTS E.209-E.210 (classical for regular ℓ; topicality verdict
     KNOWN BEFORE) and SECTIONS_OVER_Q C.3 (Clark 2006). The run is asked for the locators.
   - **Item 5: outside work to compare with**, each opened by me at the statement:
     - Carlson-Stix 2410.22474v2, Theorems A and B (TeX read at lines 60-100);
     - Carlson-Haine-Wolf 2407.19920, Theorem 0.1 and Examples 2.30-2.31;
     - Steklov 2602.17746v2, Theorem A = 5.14, Prop. 4.6/5.10, Cor. 5.6 (PDF text, lines 84, 1015, 1371, 1236-1256,
       1512-1530);
     - Betts-Kumpitsch-Lüdtke 2305.09462v2 (abstract);
     - Li-Lüdtke 2608.20615 (abstract);
     - Porowski 2509.15660 (abstract).

     The run must say which part of each reconstruction row Carlson-Stix proves. A1_SUCCESSOR's own comparison, at paper
     line 16693, is cited.
   - **Item 6: the Galois/anabelian map**, with its N1-N6 marked as the mapper's own proofs with no second reader:
     - N1 (Lochak 2025 Thm 5.10 with H17: Out* = GT̂ for g ≥ 1; the two gates);
     - N2 (Proposition L, which reduces SECTIONS_OVER_Q A.24), written as **Check 1** at the coordinator's request
       (24 Nov), together with the check of A.14 against Pan 2022, Theorem 1.0.4, and Helm-Voloch 2011, Proposition 6
       (the run's keys LegPan2022 and LegHelmVoloch2011; their use in `sections/legendre_agent.tex` l. 227-273);
     - N3 (the obstruction of the section tower in K_{2r}(Z) ⊗ Z_ℓ, which extends E.209 to every odd ℓ), written as
       **Check 2**, with its inputs to open (Milne ADT II.2, Herbrand-Ribet, Mazur-Wiles, Kurihara 1992, Quillen-Lichtenbaum
       via Rost-Voevodsky, Hart-Harvey-Ong 2017);
     - N4 (G_Q = GT̂ iff Λ₀ = G_{K₂});
     - N6, a correction to the attached note: its line 158 calls GT̂ ⊊ GT̂₀ "known" without a citation.
2. **Section 7 (our open items)** now includes "the questions named in the section 'Settled, checked and published since
   this prompt was built'".
3. **The literature line** ("The attachments hold no literature") now names zip 6's `literature/`.
4. **The material list** has a bullet for `INTAKE_A_6_updates_20261124.zip`.

Unchanged: the run table, the 961-row scope, every rule (what every row gets, the order of the work, the hourly ledger
with its step-4 stop rule, the outcome rules with INCOMPLETE only on environment failure, check events, checkpoints, no
copies of sources).

## Changes to the ZIP

The ZIP was repacked with every original member (874) kept and the folder `INTAKE_A_6_updates_20261124/` added. That
folder has its own `MANIFEST.tsv` (origin, SHA-256, reason) and `WHO_WROTE_WHAT.tsv`. It holds:
- earlier documents: `LONGUE_MARCHE_B.md` with five check-event files and `LONGUE_MARCHE_B_checks/`;
  `TOPICALITY_LONGUE_MARCHE.md`/`.tsv`; the general intake of SECTIONS_OVER_Q with its events; the h07 note v3 with its
  RECORDS and check; the h17 note as deposited with its RECORDS, referee report, reviews and events; DELTA_SEXTIC with
  its script; the map with its table, events and scripts;
- literature: the arXiv e-prints, unpacked LaTeX sources, of 2410.22474, 2407.19920, 2305.09462, 2608.20615, 2602.17746,
  2602.12462, 2509.15660, 0801.1452 and 2606.01466, and Lochak 2025 and Furusho 2002 as PDFs (no TeX exists online).

The archive holds no ZIP inside it and passes `testzip`.

## Lint

- `push_rule_pro_prompts.py --lint PROMPT.md`: files: 1 failing lint: 0
- `--lint-math`: files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\7_Longue_Marche_intakes\18_Pro_intakes_Longue_Marche_thin_runs\INTAKE_A_ANABELIAN_SECTIONS\PROMPT.md [] push rule present: False checkpoint rule present: True missing: none The backup of 19 Nov gives the same result (files: 1 failing lint: 1  | FAIL <local>/Documents\TO_SEND\PRO\_backups_20261125\INTAKE_A_ANABELIAN_SECTIONS\PROMPT.md [] push rule present: False checkpoint rule present: True missing: none). This prompt is not a research prompt and carries no push paragraph by design; `--lint` is the lint its builder used and the one the rules ask for ("`--lint` for any other").
- `paper_completeness_lint.py`: not applicable (the prompt writes no paper).

## Result

`INTAKE_A_ANABELIAN_SECTIONS.zip`: 1004 members, 10,852,317 bytes, no ZIP inside; the send folder holds only PROMPT.md and this ZIP. SHA-256 of the new ZIP: c0f7d9b60114598edc2228515cd535fedd18cf62d637bd2cdb61aa5f61dc9ccd.
