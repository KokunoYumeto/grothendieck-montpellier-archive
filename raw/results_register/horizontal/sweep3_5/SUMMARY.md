# Sweep 3.5: what today's settled results settle elsewhere (19 Nov 2026)

By a0c4bb37 (Claude Opus 5.5 at effort max), saved by the main session because the harness blocked the sub-agent's
write of report files. Rows: `PROPAGATION.tsv` (503); prompts to update: `PROMPTS_TO_UPDATE.tsv`; checks:
`CHECK_EVENTS.tsv` (5, on implications 1-5, read on both sides).

**Count.** 503 places where today's settled results bear on other work: 52 in other topics, 58 in one unsent prompt,
393 in the source topic's own entries. Inputs: 255 settled results from the six intakes (SA05, SA08, SA09, SA10, SA17,
SA21 in its finished version) and the OBJ_H035 pilot verdict: 156 confirmed, 54 readings, 37 refuted, 8 counterexamples;
128 name an item or a cote/scan place that can be followed.

**The implications that matter most**
1. **Cote 94 → the unsent range pilot 033.**
   - The verdict reads "non nul" before B at 94/004 l.19, which reverses the run's "false as written" on Proposition 3
     (H035.5). The Work note K94-01#1 was right. **Corrected 19 Nov ~14:0x UTC (a11a6de3):** the transcription supplied
     to the pilots (`cote_94.tex` l.79, the K94-01 reading) already has `\inserted{non nul}`; it is witness H (Hua's
     batch-01.fr.tex l.167) that omits it. PROPAGATION.tsv rows 55-56 say so; only the first version of this summary
     said "lacks".
   - The verdict also covers H035.10 (the converse of Remarque 5 bis fails for L = Σ_p (1/p)ℤ), H035.21 (the EGA IV
     6.11.8 enlargement is false), and his slips at 94/010 and 94/012.
   - `F_Archive_working_through_200/00_range_pilot_first/033_WT_94_002-013_B` covers scans 2-13 and carries the old
     state. Its builder must put in the corrected reading and the verdicts, and cote 94's second pass needs the same
     reading.
2. **SA10 → SA20.** The SA10 answer settles what SA20's lead (d) plans to examine against 151/039-044
   (`sweep3/SA20/RESEARCH_PACKAGES.md:391`):
   - at the homotopy level the shape of ∞-topoi preserves colimits;
   - B.4's premise is refuted: * ← BZ → * already gives S², and 151/041 withdraws that fear itself.

   SA20 is already running on its earlier prompt, so its intake checks (d).
3. **SA05 → SA06 (cote 15).** Two results bear on SA06 STUDY.md lines 51 and 98 and on 22 SA06 lead lines:
   - 15:3 has "F⁰(Q(1)) = Q", so the repair the intake had proposed is withdrawn (INT-SA05-E25);
   - the μ₂-components are 1/2 at p and at ∞, and 0 at l ≠ p (E09).

   SA06's run is still going, so its intake reads these marks.
4. **SA08 → SA15.** The SA08 main answers bear on SA15's claim link about constant ℤ_p coefficients
   (`CLAIM_LINKS.tsv:312`).
5. **SA17 → SA05.** A reading in the SA17 intake's "His text" bears on SA05 `CLAIM_LINKS.tsv:147`.
6. **The S6 line.** The cp11 numbers proposed for the papers are false as stated (P3K.74). The S6_10 papers (cp15)
   already print them as refuted with their replacements, and no unsent S6 prompt needs an update.
7. **SA09 and SA21.** No links outside their own topics.

**Limits.** DEPENDS and ITEM_DEPENDS gave no rows, because the intakes name run statements (A.1, B.4), not sweep-2 item
ids. One-digit place pairs (3:5) were not followed, since math text gives false matches. Each row is a link found, not a
check. No transcription or prompt was edited.
