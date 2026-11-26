# Intake: COUNTING_VARIETIES (prompt 63), checkpoint 12 (25 Nov 2026, 04:30 UTC)

By Claude Opus 5.5 at effort max, agent a5ef71dd (a copy of a4348514, which wrote MAP_COMPLEXITY.md and its NK-6). Written
for the pequalnp session 672ae3a0. The run is GPT-6 Astra (ChatGPT Pro mode); its README says "No human has checked this
work."
- **Return:** `grothendieck_archive_transcription_20261110/research_returns/COUNTING_VARIETIES_checkpoint_12_20261125T0430Z_unzipped/COUNTING_VARIETIES`.
  The paper is `workbench/papers/counting/` (138 pages). Research was still running at this checkpoint: the 04:30 review
  recorded movement, and the next review was due at 05:30.
- **Prompt:** `TO_SEND/PRO/1_Archive_research_by_topic/SENT/63_COUNTING_VARIETIES/PROMPT.md`.
- **Follow-up:** `SENT/63_COUNTING_VARIETIES_FOLLOWUP_MESSAGE_20261125.md`, by Claude Fable 5.2 at effort max. It relays
  the height observation (NK-6) of MAP_COMPLEXITY.md.
- **Known already:** AG_POLISH.md §9 and the rows CV-THM-MAIN, CV-THM-STABILIZER and CV-SP-* in AG_POLISH_ITEMS.tsv
  (checkpoint 01). The 25 Nov follow-up there took in cp02 and cp03. None of that is redone here.
- **Spot checks:** `INTAKE_COUNTING_VARIETIES_20261125_CHECK_EVENTS.tsv`, beside this file.

## Most interesting items, ranked by usefulness

1. **Every fixed formal-group height is complete** (`formal_introduction.tex` thm "Fixed height predicates", l.20;
   proofs in `formal_counting.tex` and `formal_seeds.tex`). Fix p. The input is a circuit for a smooth, geometrically
   integral, degree-d hypersurface in d ≥ 3 variables, with the dimension allowed to grow. Then:
   - h(X) = 1 is Mod_pP-complete;
   - h(X) ≥ r is Mod_pP-complete for every fixed r ≥ 2, with infinite height included;
   - exact height h(X) = h is Mod_pP-complete for every fixed finite h.

   This answers the follow-up's question in full for finite thresholds, and also the main question of prompt 96 Part C.
2. **The second height step counts cyclic orbits** (thm "The second height counts cyclic orbits", l.86).
   - A₂(φ) = [Z^{p+1}]P^{p+1} = S² + p·C(φ), where C ∈ #P counts the nonfixed cyclic orbits of balanced (p+1)-tuples of
     local configurations.
   - h(X_φ) ≥ 3 ⟺ S ≡ 0 and C ≡ 0 (mod p) ⟺ A₂ ≡ 0 (mod p²).
   - The invariant b_{p²}/p = C(φ) mod p can differ between two CNF presentations of the same Boolean function. So it is
     an invariant of the presentation, not of the function.
3. **Every finite height is realized over F_p** (thm "Explicit realization of every finite height", l.47). The
   hypersurface has degree p^h + p + 1 in p^h + p + 1 variables, is smooth and anticanonical, and has exact height h.
   - This seed makes exact-height hardness unconditional.
   - At cp11 the result was still conditional. At the 04:30 review it was resolved, with a separately frozen
     reconstruction by the same model.
4. **The full height is in polynomial space** (thm "The full height in polynomial space", l.108). Finite height or ∞ is
   computable in O_p(L²·log L) space. Every finite height is at most C(pd−1, d−1). Infinite-height *hardness* is open.
5. **Divisibility of invariant derivatives** (thm "Integral derivatives of a height-h lift", l.125). Over W(k):
   D^a f ∈ p^{max(0, E_h(a), ⌈c_h·a − (h−1)⌉)}, with c_h = 1/(p−1) − 1/(p^h − 1) and E_h(a) = Σ_{h∤j} ⌊a/p^j⌋.
   - Sharp at p-powers; the slope c_h and the error h − 1 are optimal.
   - This is our DP_MULT's DP1/DP3, re-derived for every one-dimensional formal-group law over W(k).
   - Honda-dual data is "not inferred from height alone". So DP34's slopes (Honda duals) are not covered.
6. **Our NK-6 checked and corrected** (`formal_groups.tex` prop "The coherent line and height one", l.21). The
   deduction holds, with two corrections (§7.1).
7. **The original programme moved forward** (README; QUESTIONS):
   - the saturation algorithm for principal ideals with bounded cofactor degrees;
   - the support-sensitive algorithm after linear constraints;
   - the minimal-support strip;
   - deterministic recovery of marked hidden split quadrics;
   - the complete-intersection results (CV-SCI-*: gap, balanced, certificate, Las Vegas excess recovery, linear prefix,
     deflation);
   - the function-field (CV-THM-FF-*), cubic and motivic (CV-THM-CUBIC; CV-THM-MOTIVIC conditional) and Walsh-multiplier
     (CV-ST-MULTIPLIER) rows;
   - one obstruction: a fixed-field, bounded-Betti exact zeta encoding is impossible (CV-PROP-FF-BETTI-FINITE).
8. **A claimed slip in SGA 2, Exposé V 3.5** (Q-SGA2-V35-NOTATION). The run says the displayed definition m_x = m·A_x
   does not give the intended theorem read literally; the intended reading is p_x·A_x. It is not used in the counting proof.

## 1. Useful or not

**Useful.** It turns our one-line height observation into a complete complexity classification of formal-group heights
for circuit-presented Calabi–Yau hypersurfaces:
- every finite threshold and every exact height is Mod_pP-complete;
- the second step is an explicit #P orbit count;
- the full height is in PSPACE;
- explicit prime-field seeds of every height exist;
- DP_MULT's divisibility law is re-proved in general.

Its original sparse and compression programme moved, but its main gates there stay open.

## 2. What it proved

Exact forms; the run's own check state; my checks.

- **Fixed height predicates** (above, item 1).
  - The run: "independent re-proofs" by the same model, a frozen all-height seed reconstruction, and a separate full
    classification reconstruction frozen at 04:12 UTC. Root had not yet finished comparing that reconstruction at cp12.
  - Mine:
    - the height-one proposition: targeted check, including the coefficient [p](T) ≡ H_p(F)·T^p and the complement
      trick 1 + (p−1)a^{p−1};
    - the hardness reductions in fg:thm:threshold and fg:thm:exact-seed: targeted check of the replica and seed
      coefficient factorization and of the valuation bookkeeping;
    - carried, not checked: the height criteria (eq. fg:eq:all-height and fg:eq:exact-height), the replica lemma, the
      stabilized-numerator units C_j, A_h ≡ S^h, and the seed theorem.
- **Second height** (item 2): statement read; not checked by me.
- **Seeds** (item 3): statement read; not checked by me.
- **PSPACE** (item 4): statement read. It relies on Katz–Takagi–Yobuko, Thm C, and Bhatt–Gabber–Petrov's matrix form.
  Not checked by me.
- **Derivatives** (item 5): statement read; it matches DP_MULT's checked DP1 and DP3 (intake TPC; the H09 note).
- **Earlier core**, already in AG_POLISH: CV-THM-MAIN, STABILIZER, SPLITTING and sp:thm:*.
  - Q-MAIN-INDEPENDENT is now "closed": the main theorem was independently re-proved by the same model.
- **Check events in the run:** 672 rows: 386 targeted proof checks, 128 independent re-proofs, 60 used and rechecked,
  48 computations, 47 carried, 3 refuted. All are GPT-6 Astra.

## 3. New since the pile's reading of checkpoint 01 (and its 25 Nov follow-up of cp02 and cp03)

- **The whole formal-height part.** Six sections: `formal_introduction`, `_groups`, `_counting`, `_seeds`, `_algorithms`,
  `_derivatives`. It is in answer to the follow-up message of 25 Nov.
- **Item 7's algorithms and obstructions:** complete intersections, function fields, cubic and motivic, Walsh, small zeta.
- **The SGA 2 V 3.5 note.**
- **Register:** 77 questions (35 proved, 14 current gates, 5 refuted, several randomized or partly proved), 147
  statements, 93 sources.

## 4. Open: each main question's gate

- **Infinite height.** Q-FORMAL-INFINITE-HARDNESS: membership in PSPACE is proved; hardness needs a polynomial-size
  construction forcing infinite height in a single hypersurface. Two proposals are not adopted:
  - a product-height "1 or ∞" law for self-products, which lies outside the single-hypersurface class;
  - a quotient recipe.
- **The finite-jet stabilizer.** It is not shown to preserve infinite height. An exploratory characteristic-3 example
  suggests it fails beyond the preserved range; this is still being checked.
- **Sparse saturation and complete intersections.** Q-SATURATION, sp:saturation-*, Q-CI-UNBOUNDED-EXCESS and
  Q-CI-DERANDOMIZE stay open: unbounded residual excess or cofactor complexity, and the deterministic construction of a
  good centre.
- **Compression.** sp:sparsify-coordinate: a uniform polynomial-time construction of one sparse equation would collapse
  Mod_pP to P. Whether short coordinates exist at all is not ruled out. Also open: sp:projection-input-field and
  sp:different-projective-scheme.
- **Support.** sp:full-support-boundary: intermediate excess between O(log L) (tractable) and fixed d^η (hard) is
  unclassified.
- **Small zeta.** Q-BETTI-MODULAR.
- **Structured recovery.** Q-67E543764A, Q-4FFFB1FB4E, Q-6CE82E3666 and Q-0A53ADA5A4: recovering hidden structure from an
  unmarked hypersurface.

## 5. Relations

- **NEG_NIGHT.** NN-C005 is the ancestor: N mod 2 = [x₁⋯x_n]·ML(∏(1 + f_i)), with Katz's "On a theorem of Ax" as input.
  NN-C023 and NN-C024 are the p = 2 Hasse–Witt construction and the smooth pencil. CV-THM-MAIN extends them to every p,
  with stabilization. The formal-height part goes past NEG_NIGHT entirely.
- **DP_MULT.** The derivative theorem re-proves DP1 and DP3 for every one-dimensional formal-group law over W(k), with
  sharpness and the infinite-height endpoint. Honda-dual-specific statements such as DP34 are explicitly not covered.
  This is a second derivation, by GPT-6 Astra, of results that Claude agents checked.
- **MAP_COMPLEXITY NK-6 and prompt 96 Part C.**
  - NK-6 holds, corrected (§7.1).
  - 96's Part C main question, the height of the formal group past 1 and its complexity, is answered here for every
    finite threshold.
  - If 96 is still unsent, its Part C needs a further update: the background takes items 1–5; the main question becomes
    infinite-height hardness, or the next open gates.
- **Runs 98 and 99.**
  - There is no direct mathematical link. CV is Boolean counting (Mod_pP, #_pP) inside coherent cohomology; 98 and 99
    are about algebraic circuits through tensor prices.
  - The bridge is the transfer from Boolean to algebraic hypotheses over finite fields (Bürgisser; recalled, not
    reopened). Mod_pP ⊄ P/poly would imply algebraic separations over F_p. The VP ≠ VNP claims give no Boolean hardness
    for CV.
  - Parallel: characteristic 2 is special for the permanent (99 Q4d), while CV is fully uniform at p = 2 (Mod₂P = ⊕P).
- **Other runs.** POLISH_CRISTAUX and the crystalline frame (MAP L40): the height is the first slope of
  H^{d−2}_cris, so items 1–4 are complexity statements about F-crystals.
- **Literature** (as the run cites it):
  - Artin–Mazur, II Cor. 2.11–2.12 and 4.2, pp. 106–110;
  - Stienstra, Thm 1, p. 907;
  - Silverman, IV Thm 7.4 and Cor. 7.5;
  - Katz–Takagi–Yobuko, Thm C and Thm 4.18;
  - Bhatt–Gabber–Petrov, §3.4;
  - Yobuko;
  - Katz on Ax's theorem;
  - SGA 2 XII Cor. 3.7 and V 3.5.
- **The fleet** (mirror of 25 Nov, 8,977 lemmas). No node concerns Hasse–Witt invariants, Mod_pP or formal groups. The one
  regex hit, L-pcx-089 (prefix parity), is incidental.

## 6. Candidates

- **A Hexagon note.** "Formal-group heights of circuit-presented Calabi–Yau hypersurfaces: every fixed height is Mod_pP
  complete." Items 1–4, crediting COUNTING_VARIETIES and NEG_NIGHT. It needs:
  - a different-model check of the seeds and the height criteria;
  - the run's final.
- **What a finishing prompt should carry** (the user's single prompt to finish our P vs NP work):
  - CV-THM-MAIN and items 1–5 as proved background, with their check states;
  - the P-vs-NP-relevant open gates: infinite-height hardness; sp:sparsify-coordinate; the support boundary; the
    recovery gates;
  - the corrections in §7;
  - the link to the VP ≠ VNP line, which is only the Boolean-to-algebraic transfer. CV should be a part of its own, not
    merged into the wire-geometry part.
- **Corrections to report.**
  - Our own NK-6 wording in MAP_COMPLEXITY.md, and the follow-up message's: §7.1.
  - Prompt 96's Part C text, if unsent: "The p-th coefficient of Stienstra's logarithm … is S mod p" should read "the
    T^p-coefficient is b_p/p, whose numerator b_p is S mod p".
  - SGA 2 V 3.5 (item 8): check against the scan, then consider an editorial note in our SGA 2 editions.

## 7. Problems

1. **Our observation needed two corrections.** The run found both (`formal_groups.tex` l.1–20 and the height-one proof).
   - (a) **The denominator.** "The coefficient of T^p in (fg:eq:stienstra) is b_p/p; the coherent scalar is the reduction
     of its integral numerator b_p." Our "p-th coefficient of the logarithm is S mod p" was imprecise.
   - (b) **The curve case.** "For n = 1, the previous-degree vanishing would be false". The follow-up message had stated
     that H^{d−3}(X, O) = 0 for every d − 2 ≥ 1. In the plane-cubic case H⁰(O) = k. The run proves smoothness through
     the formal Picard group instead; the heights there are 1 or 2.
2. **The checking is same-model and was incomplete at cp12.** The full-classification reconstruction frozen at 04:12 UTC
   had "no root-comparison pass recorded". The seed became unconditional only at the 04:30 review.
3. **Conditional rows.** Q-CUBIC-MOTIVE is "proved conditional only on stated standard cofiber/purity background".
   Several items are randomized: Monte Carlo, or Las Vegas.
4. **This is not a final.** Research was still running at 04:30. A later checkpoint may supersede this intake.
5. **Unread by me:** the seed proof, the PSPACE algorithm, the orbit-count proof, and every non-formal-height section.
   Their states above are the run's.
