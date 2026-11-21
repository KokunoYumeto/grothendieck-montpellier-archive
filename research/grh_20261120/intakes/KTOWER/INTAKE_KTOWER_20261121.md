# Intake of KTOWER (prompt 47, the Galois action on the tower, the K-groups of Z and cote 149), checkpoint 03, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), still going (no progress review yet at checkpoint 03).
Notation: **A** = Alpöge's archive theorems, cited as theorems by the prompt's convention.

## 0. What was read, and the scope

- **Return folder:** `research_returns\KTOWER_checkpoint_03_20261121T1747Z_unzipped` (17:47 UTC). Prompt: `SENT\47_KTOWER_...\PROMPT.md`.
- **Read:** `QUESTIONS.tsv` (all 23 rows), `LEDGER.md` (the post-checkpoint-02 part), in `KTOWER.tex` (7020 lines): §KT-ONECHAR-CLOSED
  (lines 126-230), KT-U3-DIM, KT-U3-SECOND with its proof (322-470), KT-U3-ENDO-SIX, KT-U3-ENDO-EXACT (statements), KT-K52-K56-K60-VANISH,
  KT-QUARTIC-QUARTER, KT-SOULE-STAB with its proof, KT-FF-SEC with its proof, KT-POLY-FAIL, KT-ARTIN-FAIL, KT-R2-POINT (statements).
  Lean source in `evidence\lean_chain\source\`: `FOneCharU.lean` lines 75-95, `LinkedUnlE.lean` lines 40-56,
  `SmallClassNumbers\CorGKOf.lean` lines 1-30, `WindowBoundOfLiteratureLevel.lean` lines 20-32. `evidence\Soule_2003.txt` (Lemma 9).
  `evidence\gl2_uniform.json`.
- **My computations** (in this folder): `u3_second_check.py` (the U(3) Hecke value by a character average, own implementation);
  `gl2_check.py` (T_p on M_k(Γ_0(3), χ_{−3}) from the basis a^{k−3j}b^j, compared with the run's `gl2_uniform.json`).
- **Checked in full (5):** KT-ONECHAR-CLOSED (as a source trace), KT-U3-SECOND (by recomputation), KT-U3-ENDO-SIX (consistency with
  my GL_2 computation), KT-SOULE-STAB, KT-FF-SEC.
- **Independent computation of inputs (1):** the GL_2 halves of the certificates for e = 6, 26, 28, 30 at p = 7 and e = 26 at p = 13.
- **Statement level:** the rest.

## 1. Verdicts

| Id | Statement (short) | Verdict |
|---|---|---|
| **KT-ONECHAR-CLOSED** | `UpperTheory.V.Z.J.OneCharU_s` has a closed proof term in the archive: the implication `oneCharU_of_katoTwoW_rig_admI_automorphy` (FOneCharU.lean:75-95) takes nine hypotheses, and all nine are supplied by archive theorems; the full application is written in CorGKOf.lean and LinkedUnlE.lean | **confirmed as a source trace.** I read the declaration (nine arrows exactly as listed) and `SmallClassNumbers/CorGKOf.lean`: `corGK_of (hH : HypothesesH')` applies the implication to `cohInp_alt hH.litN hK`, `Alg.M.main_holds`, `Alg.M.mprime_holds`, `Alg.lemmaP`, `katoTwoW_of_printsH hH`, `rigIUE_alt …`, `rigII_a_alt …`, `admissible_typeI_even_level_alt …` and `automorphyUnramified_of_litN_of_gdEnd …` (lines 11-18), and line 25 closes `hH` by `published_hypotheses_from_patching_alt litN descWeak`, with `litN` a theorem of the same file (lines 20-23). The same term occurs in `count_i_of_printed_bound_k_kato_automorphy` (LinkedUnlE.lean:49-54), called from `vwin_of_hypotheses_H_E_alt` (WindowBoundOfLiteratureLevel.lean:25-29) on the route to `riemannHypothesis`. **Not done, by the run or by me: the compiled `#print axioms` check.** The run's `OneCharUClosed_UNCOMPILED.lean` is marked uncompiled. |
| KT-U3-DIM | dim M_d = A(d) − A(d−1), a cubic quasipolynomial; dim M_5 = 1, dim M_{e−1} = (e/6)³ for 6 \| e | **checked at d = 5, 11** (my character average gives 1 and 8 = (12/6)³); the formula itself statement level. |
| **KT-U3-SECOND** | 7⁵T_7 = 157899 on M_5 (level-one compact U(3) over Q(√−3), Γ = μ_6³ ⋊ S_3 of order 1296, 57 coset representatives from the three reflection classes of sizes 3, 18, 36) | **confirmed by recomputation** (`u3_second_check.py`, own implementation of the character average 7^d tr T_7 = (1/1296)Σ_r m_r Σ_γ [h_d(A)h̄_d(A) − 7h_{d−1}(A)h̄_{d−1}(A)], A = U_rγ): 157899.0000. This is the U(3) half of the K_12 certificate (H18), now computed by two methods. The coset identification (U_r and the elementary-divisor argument) is the run's, carried. |
| **KT-U3-ENDO-SIX** | the unique form on M_5 is the endoscopic lift of the non-CM quadratic-twist pair in S_13(Γ_0(3), χ_{−3}); 7⁵T_7 = 7⁶ + 40250, 13⁵T_13 = 13⁶ + 1284050 | **confirmed for p = 7 and consistent for p = 13**: my characteristic polynomial of T_7 on M_13(Γ_0(3), χ_{−3}) is (x − (1+7¹²))²(x − 40250)²(x + 153502), so the non-CM pair has a_7 = 40250 and 7⁶ + 40250 = 157899; from the run's p = 13 cubic (whose coefficients my code reproduces), the pair has a_13 = (−6829482 + 9397582)/2 = 1284050. Two independent routes to 157899 now agree. |
| KT-U3-ENDO-EXACT | endoscopic dimension ⌊(e−1)/3⌋ for every even e ≥ 2; the stable dimension formula | statement level. |
| KT-GL2-CM, GL_2 certificate inputs | complete Hecke data on S_{2e+1}(Γ_0(3), χ_{−3}) | **independent computation:** my `gl2_check.py` reproduces the run's cuspidal characteristic polynomials and comparison values P_p(1 + p^{2e}) exactly for (k, p) = (13, 7), (53, 7), (57, 7), (61, 7), (53, 13). |
| **KT-K52-K56-K60-VANISH** | K_52(Z) = K_56(Z) = K_60(Z) = 0 under A; with K17, K_{4k}(Z) = 0 for k ≤ 15 | statement level for the deduction (U(3) halves at e = 26, 28, 30 and the two-modulus support argument not checked by me); its GL_2 inputs at p = 7 (and at p = 13 for e = 26) confirmed above. |
| KT-QUARTIC-BOUND, KT-QUARTIC-QUARTER | log\|K_{2e}(Z)\| < e⁴/4 for every even e ≥ 2 (and < (239/960)e⁴ for e ≥ 4), under A | statement level. It replaces the existential VK-EXP7 constant by an explicit fourth-power bound. |
| KT-C7-EXPLICIT | the constants of the seventh-power bound made explicit (≤ 10^(10^3500)) | statement level. |
| **KT-SOULE-STAB** | Soulé 2003, Lemma 9 (pp. 777-778: γ ≠ 1, γ^p = 1 in GL_N(O_F) ⇒ p ≤ 1 + sup(r, N)) is false as printed; the correct bound is p ≤ N[F:Q] + 1; for F = Q the printed bound holds | **confirmed.** The printed statement is in `evidence\Soule_2003.txt`, line 917-919. The counterexample M = (0 −1; 1 t), t = (√5 − 1)/2 ∈ O_{Q(√5)}, has characteristic polynomial x² − tx + 1 with t = 2cos(2π/5), so M has order 5 in SL_2(O_F); r = [F:Q] = 2, N = 2, and 5 > 1 + 2. The replacement follows from the minimal polynomial Φ_p dividing the degree-N[F:Q] characteristic polynomial over Q. The correction changes only the small-prime class S_{1+sup(r,N)} in Soulé's Theorem 1; for Z nothing changes. |
| **KT-FF-SEC** | rational points → section classes of Π_C^{(p′)} → G_k is not surjective for all proper hyperbolic curves over finite fields | **confirmed** (and standard in substance, as the run says: Stix, *Rational Points and Arithmetic of Fundamental Groups*, ch. 15, p. 197): every surjection onto Ẑ splits; the explicit curve y² + y = 1 + (x² + x)/(x³ + x + 1) over F_2 has genus 2 (three simple poles over the cubic place, different exponent 2 each, 2g − 2 = −4 + 6) and no F_2-point (the fibres over x = 0, 1, ∞ are y² + y = 1). |
| KT-POLY-FAIL, KT-ARTIN-FAIL, KT-PRODUCT-SEP | point separation fails for a hyperbolic polycurve surface over F_4 with the maximal prime-to-2 quotient, also for affine elementary-fibration towers; a positive refinement for products | statement level. |
| KT-F149-REVIEW, KT-F149-COMP | the literature review of F149-MARKED-RECOGNITION; the two normalizer comparisons (K17 F149-RELATIVE, GRH_NIGHT AG-C149) agree in scope | statement level. |
| KT-R2-POINT | over F̄_2 the point P imposes no condition: any connected cyclic étale cover with primitive factor of 2-rank 0 can be pointed above every P | **confirmed** (trivial: the fibre over P is nonempty). It reduces route 2 to the existence of the cover; KT-Q7 stays open. |
| Q1b, Q1c (uniform k), Q5 (Q3-IRREG), Q1C-NEXT-32/34/36 | open; e = 32, 34, 36 computations running | open. |

**Counts.** 23 question rows, about 40 findings. Checked in full: 5. Independent computation of inputs: 5 (k, p) cases. Statement
level: the rest. Refuted by me: 0.

## 2. What is new, and how it bears

- **H18's gates move.** (i) The U(3) half of the K_12 certificate is now confirmed twice: by the character-average recomputation and by
  its endoscopic identification 157899 = 7⁶ + a_7(f), f the non-CM pair in S_13(Γ_0(3), χ_{−3}), whose a_7 = 40250 my own GL_2 computation
  gives. (ii) `OneCharU_s` is a closed theorem of the archive by the source trace (CorGKOf.lean line 25); the remaining gate is the
  compiled `#print axioms`. (iii) The range grows: K_{4k}(Z) = 0 for k ≤ 15 (K_52, K_56, K_60 new), with their GL_2 inputs confirmed.
- **The uniform mechanism (the main question) is not yet there.** The run proved the dimension and endoscopic structure for every
  even e (KT-U3-DIM, KT-U3-ENDO-EXACT), and identified the obstruction to a uniform certificate: stable congruences in unbounded
  weights at a fixed large prime (KT-STABLE-PROPAGATION at 8361790201; KT-ORDINARY-SYM2-EXPLICIT-LARGE at 697446897311), which
  rational reflection kills but which a uniform unit argument must handle. In the project's terms: the step from "every k ≤ 15" to
  Vandiver's conjecture needs a uniform control of the congruence primes of the stable U(3) spectrum and of S_{2e+1}(Γ_0(3), χ_{−3}),
  or a uniform reflection argument (KT-FIELD-CHARACTER-REDUCTION: simultaneous nonvanishing of B_1(χ_D), B_1(χ_Dω^e), B_1(χ_Dω^{2e})).
- **Soulé 2003 corrected** (KT-SOULE-STAB): a genuine error in a published lemma, harmless for Z. A short note to the author is
  justified (memory: draft emails when a gap is found).
- **Cote 149 after scan 36.** Section surjectivity over finite fields fails (KT-FF-SEC, standard), and A05's point separation does not
  extend to polycurves with the full prime-to-p quotient (KT-POLY-FAIL, KT-ARTIN-FAIL). In the project's terms: cote 149 scans 35-36
  (A1) is the right statement for curves; its higher-dimensional extension needs a smaller quotient (the product refinement
  KT-PRODUCT-SEP), which is what Grothendieck's Artin-neighbourhood programme in the anabelian letter assumes.

## 3. Scope
A (the archive's theorems, including `OneCharU_s`) for every K-group vanishing and bound; the rest unconditional. No Masullo input.

## 4. Integration
- **Bridges Q06 and H18:** "K_{4k}(Z) = 0 for k ≤ 15 under A (K17 + KTOWER KT-K52-K56-K60-VANISH); K_12 certificate confirmed in both
  halves by the intake (U(3) by recomputation and by endoscopy, GL_2 by recomputation); `OneCharU_s` closed by source trace
  (CorGKOf.lean:25); compiled #print axioms outstanding".
- **K17 part 4 intake §7 (H18 gates):** strike "an independent U(3) computation"; keep "the coverage theorems" (KTOWER rates them
  PROVED_UNDER_STIPULATED_SOURCE_CONVENTION: statement level here) and "the #print axioms check".
- **Cote 149 companion:** add KT-FF-SEC, KT-POLY-FAIL, KT-ARTIN-FAIL under scans 35-36.
- **Soulé note:** draft to C. Soulé on Lemma 9 (the counterexample and the corrected bound), after the run's final.

## 5. Prompt updates (for KTOWER's successor)
1. The uniform question as the main one: a uniform bound on the congruence primes of the stable U(3) spectrum in weight (e, 0, −e), or the
   simultaneous Bernoulli nonvanishing of KT-FIELD-CHARACTER-REDUCTION for a fixed discriminant D and all e.
2. The compiled `#print axioms` on `OneCharU_s` and `UpperTheory.V.SmallClassNumbers.corGK` (needs Lean; outside the Pro run).
3. The U(3) halves for e = 26, 28, 30 by the character-average method (traces of T_{7^j}, so the full characteristic polynomial).

## 6. Hexagon readiness (changes for the register; not edited)
- **H18 (K_{4k}(Z) = 0):** test 1 complete for k ≤ 15 in the run; test 2 self-contained except the archive input and the coverage
  theorems; test 3 not yet (run going; e = 32-36 running); test 4 now has independent computations of both K_12 halves and of the GL_2
  halves for K_52-K_60; test 5 very high. **Gates left:** the compiled `#print axioms`; a read of the two coverage theorems; the U(3)
  halves for e ≥ 26; the run's final. Flag stands.
- **New candidate: Soulé 2003 Lemma 9 corrected** (KT-SOULE-STAB): complete, checked, self-contained; interest moderate; better as a note to
  the author than as a post.
- **H16 (cote 149 scan 85):** KT-F149-REVIEW is the literature review that was its gate; statement level here, so the gate is now an intake
  read of that review.
