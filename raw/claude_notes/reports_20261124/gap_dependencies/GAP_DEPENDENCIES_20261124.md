# Gap dependency register, phase 1: our own work (24-25 Nov 2026)

Written 24 Nov 2026 ~23:5x UTC (the clock still said 24 Nov) by agent a88af1f4fbcac932c (Claude Opus 5.5 at effort high)
for the main session 329fb1e6 (Claude Opus 5.5 at effort max). The user, 24 Nov ~23:4x UTC: [the user's words, omitted] Phase 1 is our own work; phase 2, the outside literature, comes after.

This is a register of what is at risk, for checking. It makes no claim of priority. Nothing was sent, posted or pushed,
and no git was used. The full rows are in `GAP_DEPENDENCIES_20261124.tsv` (47 rows), built by `build_gap_register.py`
in this folder.

**How it was made.**
- **Gaps collected** from:
  - the check register: `results_register/CHECK_REGISTER.tsv` holds 1,982 refutation events by Claude or Fable checkers,
    most of them a run's own conjecture refined; they are summarized in one row (T2, last);
  - the errata file `reports_20261120/errata/OUTSIDE_PAPERS_ERRATA.md`;
  - the outreach register `grant_evidence/OUTREACH_REGISTER_20261122.md`;
  - the e-mail drafts index `field_experts/intake_20261121/EMAIL_DRAFTS_INDEX_20261123.md`;
  - the sent log `reports_20261124/EMAILS_SENT_20261124.md`;
  - the Hexagon board (stage N rows);
  - the pile (`INDEX.md` §§4 and 7, the TOPICALITY files, the corrections sections of the MAP files, CHECK_HN_AM and the two
    H17 checks);
  - the RUNBOOK of 20-24 Nov.
- **Uses found** by a scripted search over:
  - our posted notes' TeX (`reports_20261123/*_note/`, `reports_20261124/zh3_note/`, the H01 v5 source, the H06b v2 draft);
  - every waiting PROMPT.md in TO_SEND/PRO (293 files, excluding SENT, backups and superseded copies);
  - the pile, the intake files and `knowledge/`.

  The script is in the session scratchpad (`gapscan.py`, `gappats.tsv`, `gapscan.out`). The 67c paper's source was not
  searched, so that no paragraph the user asked not to be read was opened.
- **Limits.** A search hit is a mention, not a use. "Affected" below comes from the context recorded in the pile and the
  intakes, not from a fresh reading of each proof. The context guard stopped further reading at ~70 % of this agent's
  context, so every "unknown" is a check to make, not a verdict.

## Updates of 25 Nov 2026, ~00:5x UTC (at the main session's word; the TSV is rebuilt with them)

- **Row 6, the public mirror: DONE.** a4348514 (Claude Opus 5.5 at effort max) corrected the three bullets in
  pequalnp-mirror commits 3d2aa2f and ba9263c.
- **Row 11, Zheng Cor. 4.4: NOT AFFECTED.** P90a v3 (hexagon:2611.00936v3, posted tonight) cites Zheng only as related
  work (l. 190). Its Section 7 proves the nonvanishing directly, without Zheng: the i = p summand
  (Sym^{p−2}V)^∨ ⊗ T^{p−2} contains O_C. The main session 329fb1e6 (Claude Opus 5.5 at effort max) read that proof.
- **Row 16, H06b v2: POSTED** as hexagon:2611.00939v2. The main session checked the deduction of Remark 7.2; Remark 8.1
  restates Ishii.
- **Row 1, LM8_PUSH D.23: IN PROGRESS.** ae4ae3dc (Claude Opus 5.5 at effort max) is attack-reading it
  (CONFERENCE/ATTACK_D23.md).
- **Prompt-text fixes (double-check items 8, 9, 11), applied to waiting prompts only.**
  - **Sent status checked first.** SENT_PRO.tsv has no row for 95, INTAKE_A, INTAKE_B or 065_OBJ_H04F_O, and none of
    them is in a SENT folder. 68 and 70d have been sent and were not touched.
  - **Item 8: no change needed.**
    - 95_GT_AFTER_H17 (l.70), INTAKE_A_ANABELIAN_SECTIONS (l.269) and INTAKE_B_TOWERS (l.257) quote the sentence "…
      itself is known" only as a correction to H17 v1. Each says that no printed proof is known to us.
  - **Item 9: no change needed.**
    - No waiting prompt carries the Δ shorthand. The scan finds it only in three ALP_CONNES intake files, which are not
      prompts.
    - Prompt 68 is sent.
  - **Item 11: 065_OBJ_H04F_O changed.**
    - Backup: `TO_SEND/PRO/_backups_20261125/065_OBJ_H04F_O_before_gap_register_fix/`, holding PROMPT.md and the ZIP.
      The earlier backup `065_OBJ_H04F_O/` is another updater's and was left as it is.
    - The B.4.1 row now says "refuted as stated by our intake of 23 Nov". A correction line follows it: the normality
      clause holds only under both global centralizations and compatibility; B.4.1 is to be used with those hypotheses
      (the polish run's CROSSWALK row 74; P03-C31, C32, C34, C35).
    - A correction line follows the G.2.2 row (Bhowmik-Pathak). The counterexample at τ = i stands. A repair asking only
      that some f_r be nonzero at τ is incomplete: it fails at k = 0. A correct repair also assumes k ≠ 0 and that every
      f_r is finite at τ, as 01b states.
    - The ZIP is unchanged. The prompt tells the run to follow these notes over any attachment that states the repair
      without k ≠ 0.
    - The send folder holds only PROMPT.md and OBJ_H04F_O.zip. Lints: `--lint-math` 1 file, 0 failing; `--lint`
      1 file, 0 failing. New PROMPT.md SHA-256 begins 1008e6003f5e87e2.
    - Not builder-built, so there was nothing to rebuild or place.

---

## 1. Tier 1: gaps that reach our own work (sorted by impact)

| # | Gap | Our uses | Affected? | Double-check | Action |
|---|---|---|---|---|---|
| 1 | **LM6 E.8 = Steklov's Kummer-divisibility step (Prop. 4.6/5.10), and his "Y₁(7)(Q) = ∅" (Thm 5.14)**, arXiv:2602.17746v2. The step fails at the Fermat cusp; the lemma is false at ℓ = 7. Found by LM8_PUSH D.22, FERMAT_SUCCESSOR A.4, LM6 E.10 (GPT-6 Astra, ChatGPT Pro mode); recomputed by the LONGUE_MARCHE_A reader (Claude Opus 5.5 at effort high). Claude Fable 5.2 at effort high had passed E.8 on 14 Nov. | LM6 E.12; FERMAT_SUCCESSOR A.1-A.11; the pile's candidate A3; prompts INTAKE_A, INTAKE_B; `knowledge/04_research/results_register_and_checks.md` | **Yes**: E.12 stands only through the repair LM8_PUSH D.23 | A full read of D.23 (its global part is unread) and of n = 3, 5, 7 | Check; then an e-mail draft to Steklov under the e-mail rule |
| 2 | **Masullo's draft** (sec. 12.3-12.4, equivalent to RH; MA-HM-003, checked in full by af2a18f6, Claude Opus 5.5 at effort high) | Board H05; TRACE_DET MAS-10; our **public** page research/grh_20261120/README.md ("Under Masullo …"); a workbench heading calling GRH_NIGHT constructions "repairs" | **Yes** for every statement "under M" | That no posted note or waiting prompt states a result under M as unconditional | A version note on the public README (the user's yes; a push); H05 to void; reword the heading |
| 3 | **Caradot-Lin Prop. 3.10** (2511.22614v4), false over every nonzero ring; their Thm 3.15 stands. Found by RESEARCH_SA08; author told 22 Nov 01:56 UTC | Our corrected criteria B-003/B-004: their PD clauses rest on our B-002, unchecked | **Possibly** | A targeted check of B-002 | Check |
| 4 | **Our own suggested repair in the Bhowmik-Pathak e-mail** (22 Nov 00:53 UTC): it needs k ≠ 0. Our counterexample to their Thm 1.11 stands. Found by the main session e0d20ada (Claude Opus 5.5 at effort max) | The sent e-mail; SA07 G.2.2; prompt 065_OBJ_H04F_O | **Yes**: the authors hold a wrong suggestion from us | That 065_OBJ_H04F_O does not repeat it | The user's decision on 01b |
| 5 | **H17 v1, l.158: "The inclusion GT̂ ⊊ GT̂₀ itself is known"** (hexagon:2611.00940v1): no printed proof; only our unrefereed runs claim it. Found by MAP_GALOIS_ANABELIAN N6 (Claude Opus 5.5 at effort max) | v1; the phrase matches in prompts 95, INTAKE_A, INTAKE_B | The posted v1 only | That the three prompts call the strict inclusion our unrefereed claim | H17 v2 (by a49aabbf, Claude Fable 5.2 at effort max) carries the fix; v2's Thm 20 and Cor. 21-22 hold (CHECK_H17_V2, ae4ae3dc, Claude Opus 5.5 at effort max) |
| 6 | **Our public pequalnp mirror** (`extension/EXTERNAL.md` l.133-141) **and `fleet_map/VPVNP_INTEGRATION_20261124.md`**: three statements that runs 98 and 99 correct (the scale bullet, "only flattening ranks and quantum functionals", R5's Euclidean assertion) (MAP_COMPLEXITY §2.6, a4348514, Claude Opus 5.5 at effort max) | Public text; prompt 99 (sent) was built on the integration | **Yes** (public) | Run 99's final against the corrected statements | A correction commit (the main session decides) |
| 7 | **S6 Paper III**: four D25 gaps in the proofs of Thms III.6.5/III.6.6 (conclusions open); Thm III.5.27's display (D.V3) refuted | Paper IV: ten statements list III.6.5/6.6 as inputs, three recorded false; IV.3.21's proof cites them | **Yes** (Paper IV) | Paper IV's ten dependents once the run settles 02S8/02S9 | Held by the S6 session 5c7e951b; continuation 10 running |
| 8 | **Milne's Hexagon report (2611.00244v1), sec. 3.6**: a missing sign (-1)^r. Found by GHOSTS C15 (GPT-6 Astra, ChatGPT Pro mode); confirmed by abcaba9b and a447db23 (Claude Opus 5.5); author told 22 Nov 03:53 UTC | Prompt 70d (Milne's framing of Q01(iv)); HODGE_FINISH Paper A; C44_POS ambient E⁶; MAP_NUMBER_THEORY NK-7. All lean on his Thms 3.1 and 3.5 | **Unknown** | Whether sec. 3.6 enters the proofs of Thms 3.1/3.5 | Check |
| 9 | **Soulé, Lemma 9** (Doc. Math. Extra Vol. Kato 2003): false for [F:Q] > 1; author told 22 Nov 00:55 UTC | KTOWER/K17 over Z (unaffected); BEYOND_DIRICHLET's 3-primary K-groups of Q(ω, ∛269) | **To check** for the number-field computation | Whether that computation uses Lemma 9 | Check |
| 10 | **DEKM (1910.11598v1), Thm 4.5's enumeration**: a gap (K17 cp05); held, paywalled | K17/KTOWER K-group computations; Pintar and Mok-Zheng build on our K17-S17-JOINT | **Unknown** | Whether any K17/KTOWER statement uses Thm 4.5 in the top cases | Check; then decide on a note |
| 11 | **Zheng (1509.04993v1), Cor. 4.4**: false in characteristic 5. Both e-mails bounced; contact form only (the user's call) | P90a cites Zheng for refining Raynaud's surfaces; POLISH_CRISTAUX Paper 1 (the P90a v3 candidate) calls its nonvanishing "Zheng's range endpoint a = p, b = 1" | **Probably not**, unchecked | Which Zheng statement the endpoint is | Check before any P90a v3 |
| 12 | **Boggi-Funar, arXiv:2311.17025 Lemma 2.23** (EXIT_TOWER E.14; counterexamples not refereed line by line) | **H17 v2 Corollary 22(b)** via Lochak's Thm 5.10: **UNAFFECTED**, resolved by ae4ae3dc (Claude Opus 5.5 at effort max), `CHECK_H17_GATE_BF_20261124.md`. Lochak uses only Boggi-Funar, J. Topology 16 (2023), arXiv:2004.04135, Thm 5.3, with his own Algebra i Analiz 35 (2023) Thm 6.4 as an alternative; 2311.17025 builds on that paper, not the reverse. Limit: Lochak's proof was read in outline. Also named in prompt INTAKE_B | No for H17 v2; unknown elsewhere | A line-by-line referee of E.14 | Check; then a draft in the Boggi thread |
| 13 | **Boggi, arXiv:2011.15075v6, Prop. 6.9 and Lemma 6.16** (EXIT_TOWER E.14): false as printed; his main theorem may survive | EXIT_TOWER E.45 would follow from his main theorem; prompts 95, INTAKE_B and 28_SA30 name the paper; MAP_GALOIS GA-1 gives the Out* part without these steps; Lochak does not cite 2011.15075 | **Yes**, for any use of E.45 through Boggi's theorem | That no waiting prompt states E.45 or Boggi's theorem as settled | Check; record E.45 as open where it rests on Boggi v6 |
| 14 | **Prompt 46b** (sent) states DEG_L S-30 to S-41 too broadly (ad855737, Claude Opus 5.5 at effort high) | The HODGE_DIVISION run that received it | **Possibly** | HODGE_DIVISION rows citing those statements | Check at the next intake; correct any successor |
| 15 | **Our shorthand "Δ on GT̂ = χ₁₂∘u"** (Δ = 0 on GT̂; the formula holds on the gentle group); corrected 23 Nov in two notes, still in the ALP_CONNES intakes cp28, cp41, cp44 | Those intake files; prompt 68 carries ALP_CONNES material | **Possibly** | That the intakes and 68 carry the corrected form | A dated correction line |
| 16 | **Our posted notes corrected in later versions**: P90a v1 Thm 2 needed dim X > 0 (fixed in v2, published); S20 v1 lacked Elliott's 2013 credit (fixed in v2); H06b v1 cites Sharifi 2002 by the wrong theorem number (v2 drafted). Earlier slips fixed before posting: H22 v1's reversed closure; H22 v3's two false sentences; H07's genus-one step; H09 v1's v_p(n!) clause; H01's SG-09 Lefschetz input | The posted versions; the e-mails cite P90a v2 | No (done or drafted) | H06b v2 by a second reader | Version notes: done for P90a and S20; H06b v2 to check |

## 2. Tier 2: outside errata where our work uses the source, or refutes it

Each has its full row in the TSV. In short:
- **GCT VIII** (Conj. 3.2; unimodality at rank 3; the b₂ misprint): we use VIII's rank-three constants in the counting
  construction (`SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md` §§8-14; prompt 93). Probably unaffected: a8d75352 (Claude
  Opus 5.5 at effort high) recomputed the constants, and found the misprint that way. Author told 24 Nov 11:54 UTC.
- **GCT VI** (Thm 1.6.1(d); PH2, SH(a), PH3; the relaxed form in the BOR appendix): we refute these and nothing of ours
  assumes them. The subtitle is wrong in prompt 52 (sent) and in the runs. NOTE_E1 is held.
- **Asvin G.** (Lemma 11 integrally; the Case B limit clause): no result of ours rests on them; told three times.
- **Thakur** (Prop. 2.9): refuted, used by none; told, and he replied.
- **Elliott's conjectures**: refuted by S20, used by none; Professor Elliott has died, so nothing further is sent.
- **Ben-Bassat, Conj. 7.1**: refuted by CATHOT, used by none; told 12 Nov.
- **Esnault**: corrected by her (24 Nov); P90h should use her corrected note.
- **Mukai, RIMS-1736**: P90a uses other statements; told.
- **Partsch, Chai, Chai-Oort**: P90b waits for an independent re-proof; Partsch has no working address.
- **Friedland-Lim**: GCT_GINEQ F-08 uses the corrected forms; E2 is unsent.
- **Cotner-Zavyalov, Ex. 3.4.6(ii)**: our uses are of Ex. 3.3.6; confirm at the source.
- **Achter-Casalaina-Martin, sec. 1.7.2**: SA14 E4 cites it as its only located prior; confirm at the source.
- **Popescu, p. 510**: Paper 1 cites his tower, not the false claims; check.
- **Stacks Tags 07BV, 0BTP, 60.22.1**: S17a records the p = 2 error; drafts ready.
- **Grammatica, Rem. 4.6**: no use; draft ready.
- **Hoshi-Tsujimura, Mochizuki-Tsujimura**: check LM6 B.34 and SECTION_GHOSTS P.3; told 22 Nov.
- **Boyle-Chen, Galvin, Orson-Powell-Randal-Williams**: told 24 Nov; check that P91j uses neither faulty statement.
- **Kent, Wilkes, Porowski, Yamaguchi, Schreieder**: held; each needs a Claude targeted check first.
- **BIMS, Guo's thesis**: the 67c paper carries the corrected forms; no note sent.
- **Our runs refuted by intakes.** 1,982 refutation events are in the check register. Of the selected ones with a downstream
  use, SA07 B.4.1 appears in prompt 065_OBJ_H04F_O: check that the prompt marks it refuted.

## 3. Tiers 3 and 4: no use in our work, or editorial only

- **Tier 3**, minor or unused: Nagpal-Snowden (told), Buss et al. (told, two of four authors), Ekedahl-van der Geer (told),
  Keller (told), Jenča, Liedtke/CDL, Milne's notes (Rem. 8.5), Bhatt and Rains-Sam (misprints), the other Boggi-Funar items.
- **Tier 4**, Grothendieck's archive claims and EGA/SGA. They reach our readers, translations and editions as editorial
  notes, not as claims of ours:
  - cote 31 sheet 84; cote 4 §8.3; cote 44 Th. 5; cote 57:97-100 (the scheme-level reading); the 1964 Th. 5;
  - Les Dérivateurs II 36ter, XII Th. 2, XVI Th. 5.4, XV 9.11-9.13, XVI note 56;
  - 67/086 and 67/098; 131 sheet 13; 18:11; 15:173; 100:3; LM §49.VI; the 1969 Kostant prediction;
  - EGA IV 19.5.6(ii), III 4.3.6, IV 20.1.3 and 0_IV 19.3.12; SGA 2 XIII Conj. A.

  The working-through prompts were updated on 24 Nov. The readers take editor's notes at their next build.

## 4. The double-check list (from Tier 1 and the Tier 2 rows marked "check")

1. **LM8_PUSH D.23**, global part, and the n = 3, 5, 7 cases of Fermat for Selmer sections. LM6 E.12 rests on this repair.
2. **Our B-002** (SA08). Our B-003/B-004 depend on it after Caradot-Lin's Prop. 3.10 fell.
3. **Milne's report, sec. 3.6**: does the sign enter Thms 3.1/3.5? Our 70d, Paper A, C44_POS and NK-7 lean on them.
4. **BEYOND_DIRICHLET's K-groups of Q(ω, ∛269)**: does the computation use Soulé's Lemma 9?
5. **K17/KTOWER**: does any statement use DEKM's Thm 4.5 in its top cases?
6. **POLISH_CRISTAUX Paper 1**: which Zheng statement is "Zheng's range endpoint"? Settle it before a P90a v3.
7. **EXIT_TOWER E.14**: a line-by-line referee of its counterexamples to Boggi-Funar Lemma 2.23 and to Boggi Prop. 6.9 /
   Lemma 6.16. Also check that no waiting prompt (95, INTAKE_B, 28_SA30) states E.45 or Boggi's theorem as settled.
8. **Wording in prompts 95, INTAKE_A and INTAKE_B**: the strict inclusion GT̂ ⊊ GT̂₀ must be stated as our unrefereed
   claim, not as known.
9. **The ALP_CONNES intakes cp28/cp41/cp44 and prompt 68**: they must carry the corrected Δ statement.
10. **HODGE_DIVISION**: its rows that took DEG_L S-30 to S-41 from prompt 46b.
11. **Prompt 065_OBJ_H04F_O**: SA07 B.4.1 must be marked refuted, and the Bhowmik-Pathak repair must not be repeated.
12. **LM6 B.34 and SECTION_GHOSTS P.3** against Mochizuki-Tsujimura and Hoshi-Tsujimura.
13. **P91j**, against Galvin's and OPR's faulty statements.
14. **Popescu (p. 510), Cotner-Zavyalov (Ex. 3.4.6) and Achter-Casalaina-Martin (sec. 1.7.2)** at the source, for S12a,
    P90e and SA14 E4.
15. **H06b v2** by a second reader.
16. **Run 99's final**, against the corrected mirror statements.

Resolved tonight: **H17 v2 Corollary 22(b)**, unaffected by the Boggi-Funar gap (`CHECK_H17_GATE_BF_20261124.md`,
ae4ae3dc, Claude Opus 5.5 at effort max). Its limit: Lochak's proof was read in outline.

## 5. Picks for the phase-2 citation search (who else builds on the faulty statement)

1. **Boggi-Funar 2311.17025 Lemma 2.23, and Boggi 2011.15075 Prop. 6.9 / Lemma 6.16.**
   - They sit under the procongruence mapping-class-group literature (Lochak, Boggi-Zalesskii, the GT-action papers).
   - If E.14 holds, others' theorems may rest on them.
   - First referee E.14.
2. **Milne's report, sec. 3.6.**
   - It is a new and widely useful Hexagon report: Tate and the Hodge standard conjecture for abelian varieties over
     finite fields.
   - Others will cite its Thms 3.1/3.5 at once.
   - It matters whether the sign reaches them.
3. **Steklov 2602.17746.**
   - It claims Fermat for Selmer sections, a statement others may quote as proved.
   - The two faults are concrete.
4. **Mulmuley's GCT VI hypotheses and GCT VIII conjectures.**
   - They are the most cited items here.
   - Papers that assume PH2, SH(a) or PH3, or GCT VIII's positivity with unimodality, would be in dispute.
5. **Soulé 2003, Lemma 9.**
   - It is a stability bound that K-theory computations over number fields reuse.
6. **DEKM, Thm 4.5.**
   - K-groups and cohomology of GL_N(Z) are cited by later computations, our own descendants included (Pintar,
     Mok-Zheng).
7. **Caradot-Lin, Prop. 3.10.**
   - It is recent (v4, June 2026), so citations are few and easy to find now.
8. **Friedland-Lim, Lemma 9.2.**
   - Nuclear-norm papers cite it.
9. **Zheng, Cor. 4.4; Esnault's Lemma 2.2 / Prop. 2.5 (now corrected by her); Grammatica, Rem. 4.6; Stacks 60.22.1.**
   - Each is a statement in active subjects (Kodaira vanishing in positive characteristic, partial connections, p-adic
     comparison, Dieudonné theory), so later uses are likely.

**Not picked:**
- Elliott's conjectures: they are conjectures, settled now.
- Ben-Bassat's Conj. 7.1: a conjecture, and the paper is a month old.
- Masullo's draft: it is not a proof, and nothing should be built on it.
- Asvin G. and Thakur: the authors are already engaged.
- The misprints.
