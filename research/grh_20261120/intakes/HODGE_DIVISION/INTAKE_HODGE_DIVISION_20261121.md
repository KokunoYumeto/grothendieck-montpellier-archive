# Intake of HODGE_DIVISION checkpoint 01 (prompt 46 v2)

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 21 Nov 2026, round 5. The run is built on my own attack
(`reports_20261120\hodge_bridge\HODGE_DIVISION_ATTACK_20261121.md`). **Every check below on a statement of my attack is a
check by its author, and is marked so.** Brief: `field_experts\intake_20261121\INTAKE_BRIEF_20261121.md`. Check events:
`INTAKE_HODGE_DIVISION_20261121_CHECK_EVENTS.tsv`.

## 0. What I read, and my scope

**The return:** `research_returns\HODGE_DIVISION_checkpoint_01_20261121T1124Z_unzipped\`, the only HODGE_DIVISION folder
present when I started. The run is GPT-6 Astra (ChatGPT Pro mode). It began at 10:38:55 UTC; this checkpoint is from
11:24 UTC. **The run is still going.**

**What I read:**
- `research\gaussian_fourfold.tex`, **in full** (Q1: HD-G01, HD-G02, HD-G03, HD-G04a, HD-G04, HD-G06, and HD-WQ);
- `QUESTIONS.tsv` (states), the head of `LEDGER.md`, and the van Geemen entry of `research\root_bibitems.tex` and
  `root_check_events.tsv`;
- `agents\g34_eightfolds\g34_section.tex`: the introduction (the attribution and status of inputs), the D-G34-01
  statement, and D-G34-07 in full;
- the statement lines of SF-01 to SF-05 (`agents\sixfolds\sixfold_section.tex`).

**What I did not read:** D-G34-02 to D-G34-06 (proofs), D-IM-01 to D-IM-07, HD-E6/E6b, SF-CM01 to SF-CM04, D-SR01 to
D-SR04. My context is near its limit, so these stay at the level of their QUESTIONS rows.

**Scope:**
- **Read in full with a targeted proof check:** HD-G01, HD-G02 (the proof; the van Geemen locator not opened),
  HD-G03, HD-G04a, HD-G04, HD-G06, HD-WQ.
- **Statement level:** D-G34-01 to D-G34-07 (I read D-G34-07's text); SF-01 to SF-05; the rest from the rows.

## 1. Verdicts

### Q1: Q(i) fourfolds, the principal component

- **HD-G01 (Θ|_B = 2ξ, type (2,2,2,2), kernel B[2]): confirmed.**
  - It cites Mumford, *Prym varieties I*, §3, Cor. 2 (p. 332), applied to the double cover C → D = C/σ². B is that
    cover's Prym.
  - This is a cleaner citation for my Q1-01, which I proved by complementarity. The two agree (author's check).
- **HD-G06 (the even lattice U⊕U for the Pryms, the odd I_{2,2} for E²×E²; δ_W ≤ 4·D_Pr = 3,656,994,324,480 on both
  types): confirmed.** I checked:
  - S^*I_{1,1}S = 2U and S^*US = 2I_{1,1}, with S = [[1,1],[1,−1]];
  - the isogeny from the even to the odd type has degree 2⁴, and the pullback of the target polarization is 2ξ;
  - a detecting surface therefore pushes forward with degree ≤ 4·D_Pr.

  The classification ("only U² or I_{2,2}") agrees with my Q1-02 and Q1-05. **This closes the gap my §5 left open: "the
  odd component needs its own source".** The extension is right.
- **HD-G02 (rank 4, dominance): confirmed in its proof, which is identical to mine** (S-b in §5: the multiplication
  map, the base-point-free pencil trick, and the Hurwitz count for 4p ~ 4q).
  - The run cites **van Geemen, *Theta functions and cycles on some abelian fourfolds*, Math. Z. 221 (1996) 617–631,
    Th. 5.3(3), pp. 629–630** as the published source.
  - Its source log records a read of the OCR of pp. 629–630 at the author's site (sites.unimi.it/vangeemen/...).
  - **I did not open it (context limit).** The locator is carried from the run's source log.
  - **Consequence for my attack:** §5's sentence "S-b: not in the 1988 text; proved here instead" stays true of Schoen
    1988. It must add "**published by van Geemen 1996, Th. 5.3(3), pp. 629–630; the proof in §5 is a second route**".
- **HD-G03 (the norm fibre is a union of translates of the 6-dimensional P, of type (1,1,1,1,4,4), with degree
  8,398,080): confirmed.**
  - The type is cited to Lange–Ortega (arXiv 0805.1020, §4): (1^{(d−2)(g−1)}, d^{g−1}).
  - **Is it a correction of my attack?** Only of my §2.5 sketch, which wrote deg T₀ = 3⁴·4!·(Pf of Θ|_B), a
    4-dimensional degree. That sketch was wrong.
  - My §5 (Q1-03) already used the 6-dimensional N, of type (1,1,1,1,4,4) and degree 8,398,080. So §5 and the run agree.
  - **Edit needed:** mark §2.5's displayed degree as superseded by §5 and HD-G03.
- **HD-G04a and HD-G04 (D_Pr = 914,248,581,120): confirmed. The integer is identical to my §5 D₀(Q(i)).**
  - Their nonvanishing argument goes through the primitivity and positivity of u^*W in H⁴(C⁴), with Schoen's Th. 2.0
    and Lemma 2.6.
  - Mine goes through nondegeneracy of U and P = [4]φ + const on T₀. These are two independent derivations of the same
    detector and the same bound.
- **HD-WQ (Theorem W sharpened: c_t ≤ C·δ_W²): confirmed; I rederived it.**
  - On W, A = [a]^* satisfies A + A^† = s := a^{2n} + ā^{2n} and A^†A = q² := Nm(a)^{2n}. So the Gram matrix is exactly
    d·[[1, s/2], [s/2, q²]], and only the factor Hd (H = 4q² − s²) needs clearing, not det G ~ d².
  - The coefficients: δHd·t = (4q²b₁ − 2sb₂)y₁ + (4b₂ − 2sb₁)y₂. I checked the inverse and the two norms 4q²Hd and 4Hd.
  - Then N ≤ δH(RD/n!)² and the degrees are ≤ 4δq√(HT)·κRD²/n!.
  - **This is a correction of my Theorem W, which is true but not sharp. It is right:** δ_W ≤ c_t ≤ C′·δ_W². My Q1-04 had
    the fixed Gram shape but still used Δ = 576d². The same sharpening applies there.
- **HD-G05 (an integral quadratic C₄ for Gaussian fourfolds):** statement level. It follows from HD-WQ.

**The run's corrections of my attack, in one list:**

| Place in the attack | The run's correction | Verdict |
|---|---|---|
| §2.5, deg T₀ written as a 4-dimensional degree | HD-G03: the norm fibre is 6-dimensional | **Right.** §5 already had it. Edit §2.5 |
| §1, Theorem W, exponent 4 | HD-WQ: exponent 2 | **Right.** Keep W, add HD-WQ as the sharp form |
| §5, the odd component left open | HD-G06: a 16-isogeny transfer gives D_all = 4·D_Pr | **Right.** It closes the gap |
| §5, S-b proved here | HD-G02: van Geemen 1996 Th. 5.3(3) is the published proof | **Locator carried, not opened.** My proof is a second route |
| Prompt core, target 1 | none: D₀(Q(i)) agrees | — |

### Q2–Q5 (statement level)

- **Q2, sixfolds: SF-01 to SF-05.**
  - Genus-4 cyclic sources reach only K = Q(i) and Q(ω), with split determinant. The rank is 9 (Schoen 1998, Lemma 13;
    Koike 2004, Th. 2.1). This is consistent with my Proposition O (n = 3 is the borderline case).
  - HD-E6/E6b: every Eisenstein sixfold determinant through G₃₄. Statement level.
  - Q2e (Q(√−7) through G₂₄) is active.
- **Q3, Q(ω) eightfolds from published inputs: D-G34-01 to D-G34-07.**
  - Severn's numerical data (roots, cocycles, intervals) are used only as a witness, independently reconstructed. Severn's
    Theorems A–C are not premises (I read the run's attribution paragraph).
  - The rank-16 period differential is proved (D-G34-03); the supplier repair (D-G34-04/05) and the Brauer transfer
    (D-G34-06) are from published inputs.
  - D-G34-07 gives the explicit bound D₈(Δ) = (4G⁸Δ)⁸·B₀, through HECKE_DIV SQ1–SQ7 (read by two readers in the run).
  - Statement level for me. **This is the result that would make the eightfold case independent of an unrefereed
    manuscript.** It applies Theorem W in its quartic form. With HD-WQ, c_t ≤ C·D₈² instead.
- **Q4, imprimitive sources for n ≥ 5 (D-IM-01 to D-IM-07): the natural sources do not dominate.** This settles negatively
  the first attack my Corollary O″ named. Q4c (the image rank of every Nielsen class) is active.
- **Q5:** SF-CM01 to SF-CM04 are conditional on Markman. D-SR01 to D-SR04 (the semiregular route) are in review.

**Counts.**

| Check | Findings |
|---|---|
| Targeted proof check, confirmed | 7 (HD-G01, G02, G03, G04a, G04, G06, WQ) |
| Statement level | the rest (Q2–Q5 and HD-G05) |
| A gap | 0 |
| Refuted | 0 |
| Corrections to my own attack, all right | 3 (§2.5 fibre; Theorem W exponent; odd component) |
| Citation added | 1 (van Geemen) |

## 2. What is new

- **Against the literature:**
  - The explicit D_Pr and D_all for Q(i) fourfolds are new integers; the dominance itself is van Geemen's.
  - HD-WQ is a new, sharper extraction.
  - **D-G34 would give the first proof of bounded division (and hence algebraicity) of Weil classes on split Q(ω)
    eightfolds from published inputs.** It needs an independent full read.
- **Against our results:**
  - It confirms D₀(Q(i)) of my §5 independently.
  - It extends §5 to the odd component.
  - It sharpens Theorem W.
  - It decides the n ≥ 5 imprimitive question negatively for the natural sources.

## 3. The two proofs

No RH or GRH is used. Masullo is not used. Markman is used only in Q5 (SF-CM), marked conditional. Severn's theorems are
not premises in Q3.

## 4. Integration (edits listed, not made)

- **`HODGE_DIVISION_ATTACK_20261121.md`:**
  - §2.5: mark the 4-dimensional T₀ degree as superseded (§5; HD-G03).
  - §1 R4: add "sharp form HD-WQ: c_t ≤ C′·δ_W²".
  - §5: add van Geemen 1996 Th. 5.3(3) for S-b (my proof is then a second route); add HD-G06's odd transfer, D_all =
    3,656,994,324,480.
  - §2.1 table: add a row "Q(ω) split eightfolds: D₈(Δ) from published inputs (HODGE_DIVISION D-G34, statement level)".
- **`HODGE_DIVISION_PROMPT_CORE_20261121.md`:** target 3 is being carried out (D-G34); target 4 is negative for the
  natural imprimitive sources (D-IM).

## 5. Hexagon readiness (`HEXAGON_CANDIDATES.md`; changes listed, register not edited)

| Candidate | Tests passed | Gate left |
|---|---|---|
| **H12** (the ghost dichotomy; explicit bounded division for Q(ω); now also Q(i)) | 1 and 2: yes for Q(ω) (Schoen published) and Q(i) (Schoen 1988 + van Geemen 1996, published). 4: Q(i) has two independent derivations of D_Pr (my §5 and HD-G04) and of the dominance (mine and HD-G02) | 3: the run is still going, so wait for its final. A literature search (Brünjes–Serpé covers only the principle). My read of the write-up. **One to two gates.** Add to the row: "Q(i): D_Pr = 914,248,581,120 (even), D_all = 3,656,994,324,480 (all principal); quadratic extraction HD-WQ" |
| **H04** (cote 44 Th. 5) | Unchanged by this run (complete mathematically after SIGN_NEXT) | as before |
| **New: Q(ω) split Weil eightfolds, bounded division from published inputs** (HODGE_DIVISION D-G34) | 1 and 2: claimed, with Severn's numbers as a recomputed witness only. 4: not yet; statement level for me | the run's final; an intake read of D-G34-02 to D-G34-06 in full; a rerun of `g34_reconstruct.py`; a literature search. **Test 5 is strong** (a new case of the Hodge conjecture from published inputs, if it holds). **Several gates; flag to the user once the final is in.** |

## 6. Prompt updates (for this run, or its successor)

1. **The GHOSTS attachment carried registers but no GHOSTS paper** (the run's LEDGER, line 17). Attach the GHOSTS paper
   (`GHOSTS.tex` with its `sections\`) for R10–R12 and R20–R24.
2. Use HD-WQ everywhere the quartic Theorem W is applied (D-G34-07 included).
3. For Q3: write D-G34-02 to D-G34-06 with every step proved and its locators, and attach the reconstruction outputs.
   That is the main deliverable.
4. Cite van Geemen 1996 Th. 5.3(3) as the source of Q(i) dominance, with the attack's §5 proof as a second route.

## Addendum by the main session (Claude Opus 5.5 at effort max), 21 Nov 2026 ~13:15 UTC: the van Geemen locator checked

The locator for HD-G02 is now checked against the paper itself. It was carried above from the run's source log.
- **Source:** the GDZ scan, saved in
  `recent_results_20261110\papers\hodge_sources_20261121\vanGeemen_1996_MathZ221_617-632_GDZ\` (pp. 617-632, with
  SOURCE.md).
- **What Theorem 5.3(3) on p. 629 says:** for n = 2, the general abelian variety of Weil type (2,2) with field Q(i)
  and det H = 1 is isogenous to a Prym variety as in 5.1.
- **The proof, pp. 629-630:** the Prym map M_{3,Z/4Z} → 𝓗 (the 4-fold 𝓗 := Im(H₄ → S₄ → A₄)) has as its
  codifferential the multiplication map H⁰(C, Ω¹⊗α) ⊗ H⁰(C, Ω¹⊗α³) → H⁰(C, Ω^{⊗2}). That map is injective for
  general C by the base-point-free pencil trick "as in [S], p. 30" (Schoen 1988). This is the same argument as our S-b.
- **Remark 5.4:** the sixfold case M_{4,Z/4Z} → A₆ (dim 9 = 3²) is stated there only as a hope, with Schoen's cycles
  then settling the general Q(i), det H = 1 sixfold.
- **Pages:** the article runs to p. 632, not 631.

So the Q(i) bound D_Pr = 914,248,581,120 rests on published inputs: Schoen 1988 (Theorem 2.0, Corollary 3.1) and van
Geemen 1996 (Theorem 5.3(3)). The integers are ours and the run's, and agree. The check event is added to the TSV.
