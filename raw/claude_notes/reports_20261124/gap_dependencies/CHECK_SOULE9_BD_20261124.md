# Does BEYOND_DIRICHLET use Soulé's Lemma 9? (gap register, double-check item 4)

Written 25 Nov 2026 by Claude Opus 5.5 at effort max (the number-theory mapper of the intake pile), for the main session
329fb1e6 (Claude Opus 5.5 at effort max). The question comes from `GAP_DEPENDENCIES_20261124.md`, section 4, item 4,
and row 9 of `GAP_DEPENDENCIES_20261124.tsv`.

**The fault, as the register records it.** Soulé, *A bound for the torsion in the K-theory of algebraic integers* (Doc.
Math. Extra Vol. Kato, 2003), Lemma 9, a stability bound, is false for [F:Q] > 1. The correct bound is p ≤ N[F:Q] + 1.
This was found by KTOWER (KT-SOULE-STAB, GPT-6 Astra in ChatGPT Pro mode, with a certificate) and confirmed by Claude
Opus 5.5 at effort high; the author was told on 22 Nov, 00:55 UTC. I did not reopen Soulé's paper; this check is about
where our texts use it.

## Verdict

BEYOND_DIRICHLET uses neither Soulé's Lemma 9 nor any result that rests on it. Its K-groups of E = Q(ω, ∛269) are
unaffected, no statement needs a repair, and no follow-up message to the running prompt 69 is needed.

## 1. Every use, found

**BEYOND_DIRICHLET, checkpoint 10** (`research_returns/BEYOND_DIRICHLET_checkpoint_10_20261124T2010Z_unzipped/`).
- I searched every text file of the return (TeX, Markdown, TSV, bibliographies, programs), case-insensitively, for
  "soul" (which also catches `Soul\'e`). There was no hit.
- The two hits for "Lemma 9" are in `workbench/reviews/s5_check_events.tsv` (rows 23 and 30). Both are the run's own Lemma
  9.2 of Paper II, its strip-positivity lemma (after Miller 2002, Lemma 3.1), and have nothing to do with Soulé.

**Where Paper I's K-groups come from** (`workbench/papers/paper_I/main.tex`):
- l.49: "The comparison with algebraic K-theory and the global-to-local sequence are standard theorems; we use the
  formulations of Weibel 2013 and Kolster-Movahhedi 2000."
- l.332-333: "The integral étale comparison identifies H_e with H²(G_{E,S_3}, Z_3(e+1))", citing Weibel's *K-book*,
  Chapter VI, Theorem 8.2, Corollary 8.3 and Example 8.3.1. This is the comparison through the norm residue theorem
  (Rost-Voevodsky), valid for every number field and every odd prime.
- l.334-359: Poitou-Tate duality; the residual comparison (K_{2e}(O_K)/3 = 0 for K = Q(ω)); the localized class groups;
  the three primes above 3, giving dim_{F_3} H_e/3H_e = 2.
- The remaining steps are the logarithmic class groups (Belabas-Jaulent, Jaulent-Michel) and the run's class-number
  certificates.

No step bounds the primes that can divide the torsion of the homology of GL_N(O_E), which is what Lemma 9 is about. The
3-primary part enters through étale cohomology alone.

**The seven-primary supplement** (BD-R19, R20, R21, R27-R29; `papers/paper_I/supplement_seven/proof.tex`) is Iwasawa
theory of the cyclotomic Z_7-tower of Q(∛269), from class numbers h₇(F) and h₇(F₁). It contains no K-theoretic stability
input and no Soulé citation.

**ALP_CONNES, checkpoint 44** (the run whose AC-G22 and AC-K10-K23 BEYOND_DIRICHLET's Paper I re-proves). It cites two
works of Soulé:
- **Soulé 1987** (*Éléments cyclotomiques en K-théorie*, Astérisque 147-148), §§6.1-6.2, the finiteness of the strict
  groups R_i, used for AC-G22 with i = −e (CHECK_EVENTS.tsv rows 14 and 1207: "Soule strict R_i finiteness applies to E
  with i = −e"). That theorem holds over every number field. It is not the 2003 Lemma 9.
- **Soulé 2003** appears in three places, none of them an input:
  - `ARITHMETIC_APPROACHES.md` l.11, under "Testing existing general K-theory bounds": Thm 2, Prop. 4, Thm 3. The file
    says of itself that it "records attempted routes and their current limits. It is not a list of additional proved
    theorems."
  - The source-scope check events SRC-Soule2003-section5.1 (row 1112) and SOURCE-SOULE-2003-5.4 (row 5303). They record
    §5.1's fixed-degree torsion conjecture and §5.4's eq. (26) "as conjectural motivation only".
  - QUESTIONS.tsv row 695, KG-Q04, an open question on whether that conjecture's degree-dependent constants could be made
    uniform. No answer is asserted.

  So nothing proved in ALP_CONNES rests on Soulé 2003. The same file cites de la Torre Durán, arXiv 2611.06300v2 (Thm 4.5
  and Lemma 4.3), whose cutoff b = dn + 1 is the corrected form of the bound, also only as context.

**Our intake files.**
- `field_experts/intake_20261121/intakes/ALP_CONNES/INTAKE_ALP_CONNES_20261122_cp18.md` l.17 and its check events (row 8):
  AC-G22 "confirmed given Soule 1987 sections 6.1-6.2".
- `PRIMER_ALP_CONNES_20261123.md` l.58: "Soulé's finiteness theorem gives cyclicity", which is again the 1987 finiteness
  theorem.
- `NIGHT_AFTER_ALPOGE/INTAKE_..._cp11_partsAC.md` l.159: the Soulé characters of the Galois action, over Z. These are
  cyclotomic characters, not Lemma 9, and over Z the register already records that nothing changes.
- The pile's `ALPOGE.md` l.269 lists "Soulé (finiteness)" among ALP_CONNES's literature, meaning 1987.
- `MAP_NUMBER_THEORY.md` has no Soulé citation.

## 2. Does any use need the lemma over a number field?

No use needs Lemma 9 at all.
- **Paper I** works prime by prime, at p = 3 (and p = 7 in the supplement), through the étale comparison. That
  comparison holds over every number field without any stability range.
- **Soulé's 1987 finiteness** holds over every number field.
- **Soulé 2003** enters only as motivation and an open question.

## 3. Repairs

None needed. A note for the intake of prompt 69's final, not for the running thread: if a later write-up of BD Q01b
("uniform elliptic-unit index bounds over growing host characters") or a successor of KG-Q04 quotes Soulé's 2003 torsion
bounds over a growing field, it must use the corrected stability bound p ≤ N[F:Q] + 1, or de la Torre Durán's
b = dn + 1, and not the printed Lemma 9.

## 4. Check events (also in `CHECK_SOULE9_BD_20261124_CHECK_EVENTS.tsv`)

| statement | date | who | type | outcome |
|---|---|---|---|---|
| BD-K01 (Paper I Thm 1.1) | 2026-11-25 | Claude Opus 5.5 at effort max, Soulé-9 dependency check | targeted proof check (dependency on Soulé 2003 Lemma 9) | unaffected: K-theory input is Weibel VI.8.2/8.3/Ex. 8.3.1, Kolster-Movahhedi, Poitou-Tate (main.tex l.49, 332-359); no Soulé citation anywhere in cp10 |
| BD-R19, BD-R20, BD-R21 (seven-primary supplement) | 2026-11-25 | same | targeted proof check (dependency) | unaffected: Iwasawa and class-number inputs only |
| AC-G22; AC-K10-K23 (ALP_CONNES cp44) | 2026-11-25 | same | targeted proof check (dependency) | unaffected: uses Soulé 1987 §§6.1-6.2 (valid over number fields); Soulé 2003 cited only as motivation (ARITHMETIC_APPROACHES.md l.11; KG-Q04 open) |
| intake AC-G22 confirmation (cp18 intake, PRIMER l.58) | 2026-11-25 | same | carried as background without fault found | the "Soulé finiteness" there is the 1987 theorem; no change |
