# Longue Marche prompt updates of 24 Nov 2026: proposals, and what prompt 95 should take

By Claude Opus 5.5 at effort high (agent a7e00c630a8f698c6, the topicality agent of group LONGUE_MARCHE), for the main
session 329fb1e6 (Claude Opus 5.5 at effort max). This file goes with the six update reports in this folder:
- INTAKE_A_ANABELIAN_SECTIONS_UPDATE.md, INTAKE_B_TOWERS_UPDATE.md, INTAKE_C_GROUP_ACTIONS_UPDATE.md;
- 28_SA30_…_UPDATE.md, 30_SA31_…_UPDATE.md, 31_SA28_…_UPDATE.md.

The verdicts behind these changes are in `../TOPICALITY_LONGUE_MARCHE.md`.

## 1. What prompt 95_GT_AFTER_H17 should take (I did not touch it; it goes to the Galois/anabelian mapper)

The prompt is `TO_SEND/PRO/1_Archive_research_by_topic/95_GT_AFTER_H17/`. I changed nothing in it. The mapper adadbae6 updated it on 24 Nov (its report: `95_GT_AFTER_H17_UPDATE.md` in this folder); the points below were written against the earlier text, and most of them are now in the mapper's version (Lochak 2025, Question 1.2, C.29-C.31, the line-158 correction, the mod-17 computation).

1. **A conceptual point in its main question (research item 1).** (Corrected 24 Nov 2026 at the mapper's word. An
   earlier version of this file called the prompt's "LM8_PUSH C.30" an id slip. It is not: C.30's statement,
   `LM8_PUSH_checkpoint_17…\sections\C.tex` l. 2650, is the ℵ₀-dimensional family of quadratic characters vanishing on
   GT̂, "Countably infinite quadratic rank from beta defects". My mistake came from the cluster file's grouping of C.30
   with the profinite passage steps.) The mapper has since updated 95, and its current text names C.30, C.31, C.33, C.35,
   C.39 and C.34-C.38 correctly.
   - Item 1 asks to decide, for each member of that family, "whether it comes from Λ₀ or from the gap GT̂₀ ∖ GT̂". But
     every member of the B.2.25 family is a character of GT̂₀ that vanishes on GT̂ ⊇ Λ₀, so none of them restricts to a
     nonzero character of Λ₀. As written, the comparison sorts nothing. A version with content: which characters of GT̂
     (or of Λ₀) extend to GT̂₀, and is H¹(GT̂₀, F₂) → H¹(GT̂, F₂) onto its GT̂-invariant part? The B.2.25 family is then
     exactly the kernel of that restriction. The map (`../MAP_GALOIS_ANABELIAN.md`, N4(b)-(c); Claude Opus 5.5 at effort
     max, no second reader) gives the precise form. GT̂₀ = Λ₀(GT̂₀)·G_Q, with Λ₀(GT̂₀) the normalized elements of the
     gentle group. A character trivial on G_Q is determined by its restriction to Λ₀(GT̂₀), and it vanishes on GT̂ iff
     it vanishes on Λ₀. So 95's item 1 should compare characters of Λ₀(GT̂₀), not of Λ₀.
     The mapper's re-aimed item 1 (H¹(Λ₀, F₂)^{GT̂}, its restriction to G_{K₂}, and Question 1.2) already meets this point;
     nothing more is needed there.
2. **Literature for "Where it stands" and the paper's opening** (each opened at the statement; e-prints are in the
   INTAKE_B update folder):
   - Lochak-Nakamura-Schneps, arXiv:2602.12462v1: GT̂ acts on Γ̂_{g,0} and Γ̂_{g,1}; §1 says it is "unclear" whether the
     Nakamura-Schneps condition defines a proper subgroup; §8 asks whether the Lego action extends to all of GT̂;
   - Lochak-Schneps 2006 (Proc. Symp. Pure Math. 74; Lochak's page `textes/farb.pdf`), §1:
     - Question 1.2: is the abelianization of GT̂ the cyclotomic Ẑ^×? It bears directly on GT̂/Λ₀ ≅ Gal(Q(μ_∞, 2^{1/∞})/Q)
       and on "ρ₂ mod 2 is the character of Q(√2)" (the prompt's `GALOIS_GT.md` §1.1). The paper should state what its
       result says about Question 1.2.
     - Question 1.1: answered by LM4_SUCCESSOR C.30/C.31 (below).
   - Dolgushev-Guynee, arXiv:2401.06870v2, p. 2: the gentle group GT̂_gen = GT̂₀ "obviously contains GT̂", and nothing
     more. Strictness (GT̂ ⊊ GT̂₀) is not in print; it is ours (LM8_PUSH C.39, GT_TOWER_CHECK A.7, SECTION_GHOSTS E.198),
     and so far run-only on its profinite steps.
   - Boggi, arXiv:2011.15075v6 (22 Apr 2026): Out^{I₀}(PΓ̌(S)) ≅ Σ_n × GT̂ when χ(S) < g − 2. EXIT_TOWER E.14 disputes its
     Proposition 6.9 and Lemma 6.16. Cite it with that caveat, or not at all.
   - Furusho, math/0702128: pentagon ⇒ hexagons in the Lie, pro-unipotent, pro-ℓ and pronilpotent settings (not the
     profinite one).
3. **Results of ours that 95 can cite as background**, with their check state:
   - LM4_SUCCESSOR C.29-C.31: the profinite GT̂ monoid is a group, and a unit pair satisfying duality and the hexagon is
     an automorphism. Checked step by step by Claude Opus 5.5 at effort high (24 Nov); it answers Lochak-Schneps 2006
     Question 1.1. Use it wherever 95 passes from pairs (λ, f) to automorphisms.
   - LM2 B.g3: the graded input of the GT̂₀/GT̂ gap, dim W₁₂ = 7 against grt₁, with an indecomposable in weight 12.
     Checked by two computations of Claude Opus 5.5 at effort high (`../LONGUE_MARCHE_A_checks/`).
   - LM8_PUSH C.46: its witness value 5I in SL₂(Z/12) depends on E.58's sign normalization (it is I under the opposite
     one). This matters for item 3 of 95 (the level-12 layer).
4. **From the Galois/anabelian map** (`../MAP_GALOIS_ANABELIAN.md`, 24 Nov; Claude Opus 5.5 at effort max; its N1-N5
   are the mapper's own proofs, with no second reader):
   - **N1.** H17 Theorem 1 with Lochak, Algebra i Analiz 37:2 (2025), Theorem 5.10, gives IΓs = IΓ = GT̂ and
     Out*(Γ̌(S)) ≅ GT̂ for every generic type with g ≥ 1. 95's paper opens with Hatcher-Lochak-Schneps and must cite
     Lochak 2025, which H17 does not cite. The two gates are Lochak's use of Boggi-Funar 2023, and his p. 61 remark,
     which may give (III′) on GT̂.
   - **N4.** GT̂ = G_Q iff Λ₀ = G_{K₂}; and GT̂^ab ≅ Ẑ^× iff Λ₀ lies in the closed commutator subgroup of GT̂. The second
     is Lochak-Schneps 2006, Question 1.2, in 95's own terms, and belongs in its paper.
   - **N5.** The characters of LM8_PUSH C.34 are the weight-(p − 1) generators of W, with d₁₂ = 1, d₁₄ = 10,
     d₁₆ = 37, … (`c34_an.py`). The next computation, the linearized pentagon over F₁₇ in weight 16, decides whether
     there are 37 more characters vanishing on GT̂.
   - **N6.** H17 line 158 ("The inclusion GT̂ ⊊ GT̂₀ itself is known") has no citation; 95 must not repeat it as known.

5. **Item 3 of 95 ("are the Δ of LM7_PUSH E.65 and the Δ of H17 the same character?")** is partly answered by the note
   itself. Corollary 4 of hexagon:2611.00940 is stated for any homomorphism Δ: GT̂ → F₂ that is trivial on G_Q and equal
   to δ on Λ₀, and `h17_note/RECORDS.md` §1 maps Lemmas 12-14 to LM7_PUSH E.61 and E.65 "on the subgroup t = 0". What
   stays open is whether E.65's Δ on GT̂₀ restricts to the note's δ on Λ₀. The note says that "only the equality of the
   second of the two fields with Q(i,(3/4)^{1/4}) has been verified independently". The INTAKE_B update now asks for an
   independent re-proof of E.65 and E.58.

## 2. New-prompt proposals (none built; the main session decides)

No waiting prompt in TO_SEND can take items 2.1, 2.2 or 2.4 without changing its subject. I checked
`1_Archive_research_by_topic` (68, 70d, 78, 94, 95, 96), `7_Longue_Marche_intakes` and `E_Archive_small_prompts_54`.

### 2.1 FERMAT_SECTIONS_PAPER: Fermat's theorem for Selmer sections, for every odd exponent, with a correct proof

- **Main question.** Prove, with every step in the paper, that every Selmer section of the affine Fermat curve U_n/Q is
  cuspidal for every odd n ≥ 3. With the p-adic section theorem (OpenAI, *The p-adic section conjecture*, openai/math,
  24 Sep/6 Oct 2026, as a named input), the section set is the three cusp packets. For even n there are no sections.
  Then go beyond it:
  - the maximal prosolvable, metabelian and pro-3 versions (FERMAT_SUCCESSOR A.52, B.14, B.30; LM7_FERMAT_TOWER E.23);
  - the Y₁(N) statement LM6 B.15, for all N with g(X₁(N)) ≥ 2.
- **Why it matters.** This is the form of Fermat's theorem that Grothendieck asks for in La Longue Marche §51.16. The
  only printed claim is Steklov's, arXiv:2602.17746v2 (3 Mar 2026): primes ℓ ≥ 7 only, and its proof fails at two
  steps. The Kummer-divisibility step of Proposition 4.6/5.10 fails at the cusp, and "Y₁(7)(Q) = ∅" is false. A
  correct proof for every odd exponent would be the first.
- **What exists.**
  - LM6 E.6-E.12, followed on 14 Nov by Claude Fable 5.2 at effort high, who passed the false step.
  - LM8_PUSH D.22 and D.23 (the repair; its local part read by Claude Opus 5.5 at effort high).
  - FERMAT_SUCCESSOR A.1-A.11, A.4, A.52, A.53 (A.4, A.9 and A.53 checked by computation, Claude Opus 5.5 at effort
    high).
  - The cluster reader's `check_fermat_cusp.py`.
  - INTAKE_B (now updated) checks D.23's global part, if it is sent first.
- **Inputs.** The returns of LM6 (final), LM8_PUSH (cp17, `sections/D.tex`), FERMAT_SUCCESSOR (cp06), and LM7_FERMAT_TOWER;
  Steklov's e-print; Stoll 2007 (finite descent) and its erratum; Kriz-Li 2019; Mazur 1977, Kamienny, Merel; the
  OpenAI p-adic preprint. The outreach rule then covers an e-mail to Steklov (two errors).

### 2.2 GT0_GAP_PAPER: the gap between GT̂ and GT̂₀

- **Main question.**
  - Prove or refute, with every step written out, that the quotient of GT̂₀ by the closed normal subgroup generated by
    GT̂ maps onto C₅ × C₇ × C₁₃ × C₂^ℕ (LM8_PUSH C.33-C.39; GT_TOWER_CHECK B.2.25-B.2.30).
  - Then determine that quotient: is it abelian? What is Hom(GT̂₀/⟨⟨GT̂⟩⟩, Q/Z)? Is Δ in the span of the quadratic
    characters?
  - Give the graded statement in full: which weights of W/[W, W] are not in grt₁ (LM2 B.g3).
- **Why it matters.** It shows that Drinfeld's two relations do not imply the pentagon for the profinite groups, and it
  measures the gap. Every GT-shadow computation (Dolgushev et al.) works inside GT̂₀. No printed source has strictness
  (Dolgushev-Guynee 2024, p. 2).
- **What exists.**
  - The graded input, checked (two computations, Claude Opus 5.5 at effort high).
  - LM7_PUSH E.65, E.58, D.50, refereed (Claude Opus 5.5 at effort max, 14 Nov).
  - GT_TOWER_CHECK A.7, partly checked (GT_LINE intake, Claude Fable 5.2 at effort high).
  - Unchecked: the profinite steps of LM8_PUSH (P.2-P.4, C.30, C.32) and the C.35 pentagon certificate.
  - The map's N5 (no second reader): C.34's a_n = dim W_n, with d_{p−1} candidate characters at each p ≥ 13. The
    F₁₇ computation in weight 16 is the first new case (37 candidates). INTAKE_B (updated) asks for it.
- **Inputs.** LM2 (`sections/B_graded.tex`), LM8_PUSH cp17 (`sections/C.tex`, `code/pbc_*`), GT_TOWER_CHECK cp10,
  SECTION_GHOSTS E.195-E.198, LM7_PUSH cp09, DELTA_ON_GT cp05; Dolgushev-Guynee, Dolgushev-Le-Lorenz, Furusho, Ihara's
  special-derivation papers, Harbater-Schneps 2000.
- **Overlap with 95.** 95's item 1 touches this family. If the mapper widens 95, this can be one of its parts instead of
  a prompt.

### 2.3 No Pro prompt needed: a Hexagon note on LM4_SUCCESSOR C.29-C.31 (Lochak-Schneps 2006, Question 1.1)

The proof is short, and our reader has already checked it step by step. What remains:
- opening Boavida de Brito-Horel-Robertson (arXiv:1703.05143) at Definition 6.4, Lemma 7.1, and Propositions 7.3, 7.7
  and 8.1;
- the goodness input;
- a literature check of C.29 in the profinite rigidity literature.

That is a Claude note (field expert, editor), not a Pro run. INTAKE_C (updated) carries the same checks if it is sent
first.

### 2.4 RECONSTRUCTION_BEYOND_SUBPADIC: étale reconstruction over fields that contain μ_∞

- **Main question.** Prove pinned étale reconstruction (Carlson-Stix's formulation) over every subfield of a finitely
  generated extension of Q^ab, over finitely generated extensions of Q̄ of positive transcendence degree, and over
  K_{p,nil} and the infinite Galois extensions of D^h. Then classify which fields of finite transcendence degree over Q
  reconstruct (ANABELIAN_A1_SUCCESSOR B.52).
- **Why it matters.** Carlson-Stix, arXiv:2410.22474v2 (20 Sep 2026), settled the sub-p-adic fields. The natural next
  class is fields with μ_∞, and our runs claim it (LM5 F.50, ANABELIAN_149_PUSH F.45, A1_SUCCESSOR B.137-B.147). It
  answers cote 149, scan 52, as far as fields go.
- **What exists.** Run proofs:
  - F.47's integrality lemma and the first half of F.45, read by Claude Fable 5.2 at effort high;
  - B.46-B.50, read for sense by Claude Fable 5.2 at effort max;
  - B.123-B.147, run only;
  - the negative classes B.49-B.55 and F.49.
- **Inputs.** LM5 final, ANABELIAN_149_PUSH final, ANABELIAN_SUCCESSOR final (Part F), A1_SUCCESSOR cp05 (Part B);
  Carlson-Stix v2, Carlson-Haine-Wolf 2024, Voevodsky 1990, Mochizuki 1999, Hoshi-Mochizuki-Tsujimura (AVKF fields),
  Murotani-Ozeki arXiv:2501.11277.
- **Overlap.** INTAKE_A (updated) asks which part of each row Carlson-Stix proves. If INTAKE_A runs first, this prompt
  starts from its verdicts.

## 3. Prompts I left alone

- 95_GT_AFTER_H17 (another session's; section 1 above).
- No prompt of mine was in SENT_PRO.tsv or in a SENT folder. Batch 2 sent only 18-23; 28, 30 and 31 are unsent.
- SA29 (part 2 of the "Autour de La Longue Marche" topic, cotes 144-145) was not in my list, and I did not look for it.
