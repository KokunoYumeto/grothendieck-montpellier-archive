# Intake of HODGE_BOUNDED_CYCLES final (prompt 70), by diff from checkpoint 02

By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747), 23 Nov 2026.

- **Return:** `research_returns\HODGE_BOUNDED_CYCLES_final_20261123T0508Z_unzipped\HODGE_BOUNDED_CYCLES\` (05:08 UTC). The
  paper is at `workbench\work\UNFILED\v1\paper\` (27 .tex files, main.pdf, 120 pages).
- **Run:** GPT-6 Astra (ChatGPT Pro mode). It stopped under the two-reviews-without-movement rule, at the five- and
  six-hour reviews, then did a final verification.
- **Check events:** `INTAKE_HODGE_BOUNDED_CYCLES_20261123_final_CHECK_EVENTS.tsv`.
- **Baseline:** `INTAKE_HODGE_BOUNDED_CYCLES_20261123_cp02.md`. Checkpoint 05 was not taken in, and 70b was not sent:
  the abstract and title are unchanged from checkpoint 02.

## 0. What I read, what I ran

- **Read:** QUESTIONS.tsv (32 rows) in full; README; the ledger's review entries and its final verification; the
  abstract, title, §1 and the closing note of main.tex (unchanged in substance from checkpoint 02, which I read in full
  then); introduction-additional.tex 36–60; `polarization-quotients.tex` in full; `pure-weil-complexes.tex` 1–110;
  the statement of the coniveau theorem in `mumford-coniveau.tex`; the reference list for Voisin, Severn and the
  rStation item.
- **Not read:** the other new sections (effective sixfolds, Eisenstein eightfolds, Gaussian trace networks, simple
  Hodge bundles, finite-cover eightfolds, spin, sign-cube, tree-extension, Mumford sections other than one statement,
  analytic Weil sheaves) and every program.
- **Ran:** a rebuild from a fresh copy of the 27 .tex files with MiKTeX latexmk: 120 pages, 0 overfull boxes, 0
  undefined references. I did not view the pages; the run says it inspected every page.
- **Banned-word search:** no run names, ids or paths. "seed" (the run's word for a deformation seed object) and three
  uses of "retained" remain, mathematical rather than process words.

## 1. Register: what changed since checkpoint 02

| State | Rows |
|---|---|
| Proved | Q01–Q05 (unchanged); new: Q09 (higher-dimensional table, relative to Perry and Severn), Q10, Q11, Q12, Q14, Q15, Q18, Q20, Q28, Q29, Q31 |
| Refuted | Q13 (sixteen-line two-level gluing), Q16 (tree-supported deformation), Q17 (generic coordinate-sign network), Q21 (strict global vector-bundle resolution), Q30 (rational-base fibre-product supplier) |
| Open | Q06, Q07, Q08, Q19, Q22, Q25, Q26, Q27 |
| Unchecked | Q23, Q24, Q32 (kept out of the paper) |

**Verdict counts (mine):**
- targeted proof checks in this pass: 2 (Q10, Q12);
- carried from checkpoint 02 with the text unchanged: 7 (the equivalence and its lemmas, extraction, 48/192,
  stabilization);
- statement level: the rest;
- refuted by me: 0.

## 2. The main results, each with its check

| Result | Run's checks (GPT-6 Astra (ChatGPT Pro mode)) | My check |
|---|---|---|
| Equivalence (Q01) | targeted, statement-only re-proof | targeted at checkpoint 02; text unchanged |
| Poincaré-pairing bound on the multiplier | targeted, re-proof | targeted at checkpoint 02 |
| Quadratic extraction (Q02) | two re-proofs | rederived at checkpoint 02 |
| 48 / 192 / 36 (Q03) | targeted; Schoen 1988 pp. 11–19 now read in full | 48 and 192 targeted at checkpoint 02; 36 earlier in the prompt-46 run's text |
| Stabilization (Q04) | re-proof | targeted at checkpoint 02 |
| **Principal hyperbolic quotient (Q10)**: every split Weil 2n-fold with O_f-action is isogenous to a principally polarized split one, with lattice H(Q) and q*Θ = t_K f L, deg q = (t_K f)^{2n}Δ. So δ_W(A) ≤ (t_K f m_K)^n Δ C_U, m_K ≤ (2/π)√\|disc K\|. Over every K one principal family U^n suffices | targeted | **targeted, whole proof read:** saturation and splitting S = P₀ ⊕ Q, the unimodular Γ, the shear by η with η + η̄ = t_K, the degree count, the Steinitz reduction and the Minkowski bound. No fault |
| **Pure-Weil strong-semiregularity test (Q12)**: for e^B ch(E) = w ∈ W_K \ 0 on a 2n-fold (2n ≥ 4), strong G-semiregularity ⟺ dim Ext²(E,E)^G = 2n(2n−1), and ≥ always | statement-only re-proof | **targeted, whole proof read:** HKR, adjointness of σ² and ev^{g−2}, the B-shear, η = a·vol_{H₁} + b·vol_{H₂} with kernel H₁⊗H₂ on ∧²H, and the quotient ∧^{g−2}H₁ ⊕ ∧^{g−2}H₂. No fault, given the cited Atiyah–Chern identities (not opened) |
| Coniveau transfer (Q29): a nonzero coniveau-one part of an explicit rank-16 summand P ⊂ H³(B) of a split sixfold gives the Hodge conjecture for every power of the Hodge-generic Mumford fourfold | run checks | statement only |
| Eisenstein eightfolds B₀f⁴Δ (Q28), relative to Severn (unrefereed) | targeted | statement only |
| All-field split sixfolds δ_W < 10^179 d^53 f³ Δ, relative to Perry (unrefereed) | second hostile review | statement only |
| Gaussian trace network (Q18), 6272 equations | computation | statement only |
| The refutations Q13, Q16, Q17, Q21, Q30 | run checks | statement only |

## 3. The paper against HOW.md, and the fixes of checkpoint 02

| Fix (cp02 number) | Made in the final? |
|---|---|
| 1. State of the field from Voisin's exposé 1248 | **No.** The exposé is still cited only for Lemma 2.9 and Corollary 2.10. The main session's `reports_20261123\hodge_context\VOISIN_1248_STATE_OF_FIELD_20261123.md` has the text to insert |
| 2. Severn's eightfold preprint; the withdrawn OpenAI eightfold manuscript | **Severn: yes,** cited as an unrefereed input, and the B₀ bound is proved relative to it. **OpenAI withdrawal: not in the paper**; it is only in LITERATURE.md |
| 3. Markman's ICM statement quoted exactly | **Partly.** "Theorem 1.2 … the published account gives a proof sketch and points to the detailed preprint", without the theorem quoted |
| 4. The abstract names the inputs; "the Hodge conjecture" | **No.** Abstract and title are unchanged |
| 5. "Why anyone should care" as its own paragraph | **No** |
| 6. One explicit sentence on what is new | **No** |
| 7. "After Brünjes and Serpé" in the title decided on the merits | **No change** |
| 8. Unreviewed constructions kept out | **Yes.** Q23, Q24 and Q32 are kept outside the paper |
| 9. The open gate stated exactly | **Yes,** in Section 33 |
| 10. Page check, two readings, deposit sheet | **Yes,** per the ledger: every page rendered, two readings, DEPOSIT_SHEET.md written |

**Box 8 under the new wording** ("The proof overview, a section headed 'Proof overview'"): **not met.** There is a
subsection "Why the argument works", two paragraphs, and it covers only the equivalence.

**New problems of the final:**
- **Length and focus.** 120 pages. The equivalence, the Weil engine, the fourfold bounds, stabilization and Q10 make one
  paper of about 45 pages. The trace networks, the Mumford-square criteria and the obstruction sections (Q11, Q13–Q21,
  Q29–Q31) are a second body of work with a different reader. The abstract describes only the first. The finishing
  prompt should either split it into two papers, or rewrite the abstract and Section 1 to announce the second part.
- **One citation needs a status sentence.** "lelong_ridge and cm_symmetry_scout, rStation, paper 75" (used in
  finite-cover-eightfolds.tex for a reflection classification). The authors appear to be agent handles on an
  AI-agent preprint site. Cite it as such, or rest on Cohen and Malle alone, which the same paragraph already cites.
- **The run's own new strong results are not in the abstract:** Q10 (one principal family per field), the all-field
  sixfold bound relative to Perry, and the Q12 test.

## 4. Hexagon readiness: proved, checked by me, new

| Candidate | Status | The one gate left |
|---|---|---|
| **The equivalence with the Poincaré-pairing bound** (Q01, with H12's dichotomy Q05) | proved; my targeted check; same-model blind re-proof; the independent check of 22 Nov | the presentation: fixes 1, 4–7 and the proof overview, in the finishing prompt. Novelty is bounded by Cattani–Deligne–Kaplan p. 483 and the Bhattacharjee–Bhattacharya preprint, both cited |
| **Quadratic extraction, 48/192/36, stabilization, and Q10** (the Weil engine) | proved; my targeted checks | the same paper's presentation; for 36, a check of the Schoen 2007 smoothing input (not opened by me) |
| **Q12, the exact Ext² test for pure Weil characters** | proved; my targeted check | a literature search on semiregularity of Weil-character objects (Markman's and Perry's settings) to fix its novelty. It could be a short note of its own |

Not candidates yet: Q28 and the all-field bound (unrefereed inputs), Q29 (a criterion whose premise is open), the
refutations (construction-specific).

## 5. Fixes for the finishing prompt 70c

1. Insert the state of the field from `VOISIN_1248_STATE_OF_FIELD_20261123.md` into Section 1, before the theorems.
2. Rewrite the abstract: whose work it starts from; the equivalence with published inputs only (the CM theorems are
   not inputs); the Weil engine, Q10 and the fourfold numbers; what is not proved; the closing sentence as now.
   Title: "The Hodge conjecture for abelian varieties as a uniform bound over finite fields", keeping "after Brünjes
   and Serpé" only if Section 1 shows their Theorem 3.4 to be the engine of the arithmetic direction.
3. Add a section headed **Proof overview**, covering every main theorem: the equivalence, extraction, the small
   detectors, stabilization, Q10, Q12. For each: the difficulty, the idea, and where each hypothesis is used.
4. Add a paragraph "Why this matters" and one sentence "What is new here", with the credit split by statement and page
   (CDK p. 483; Bhattacharjee–Bhattacharya Lemmas 4.2–4.3 and Th. 4.5; Brünjes–Serpé Th. 3.4).
5. Quote Markman's ICM Theorem 1.2 exactly. Add one sentence on the withdrawn OpenAI eightfold manuscript.
6. Split the 120 pages into two papers (the criterion with the Weil engine; the construction obstructions with the
   Mumford criteria), or restructure Section 1 to announce both parts.
7. Give the rStation citation a status sentence, or rest the step on Cohen and Malle.
8. Keep Q23, Q24 and Q32 out until checked. Rebuild, render every page, read twice. Update the deposit sheet's box
   map, including box 8.

## 6. Edits I suggest outside my folder (not made)

- HEXAGON_CANDIDATES: in H12/H25 cite the paper's numbers (2·16^n/n!, n(2n+1), max(1, Nm τ/Δ)/(n+1), Q10), and add
  Q12 as a candidate.
