# Intake of DP_MULT (prompt 34), part 4: checkpoint 06, the run's final return, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode). By the user's rule of 20 Nov, **checkpoint 06 (04:20 UTC) is the
final return of DP_MULT**.

## 0. What was read, and the scope

- **Return folder:** `research_returns\DP_MULT_checkpoint_06_20261121T0420Z_unzipped`; checkpoint 05 (part 3) retired.
- **Read:** `LEDGER.md` after "Checkpoint05 packaged" (the 03:50 hourly review, the 04:13 and 04:19 work entries), the open rows
  of `QUESTIONS.tsv` (Q3e, Q5f), the statement list DP54-DP65, and the statements of DP54, DP64 and DP65.
- **Logic checked (1):** DP64's leading term (Chebotarev and Mertens).
- **Statement level:** DP54-DP63, DP65 (the run reports author, root and independent readings for each, and two locator-only
  corrections in DP59 and DP65).
- **Changes to earlier findings:** none withdrawn or corrected beyond the locator fixes.

## 1. Verdicts on the new findings

| Id | Statement (short) | Verdict |
|---|---|---|
| DP54 | on DP49's polarized Jacobian over W(F_{11³}) with the trace-one theta line L = (1, w_0)^*P_λ: for every n there is κ_0(n) such that for every κ ≥ κ_0(n) a global integral section of L^{⊗κ} has the pure-kernel jet exp(−κβ) through order n, with unit leading coefficient | statement level. |
| DP55 | detection of every nonzero vector in the endpoint space F_i; a nonzero period 1 after an auxiliary principal level | statement level. |
| DP56, DP58 | quantitative tensor levels: a linear interpolation threshold, subexponential square levels; explicit degrees and linear tensor powers with no unit-parameter congruence | statement level. |
| DP57 | a literal unramified host and actual adelic endpoint for the CM repair | statement level. |
| DP59-DP63 | permitted translates contain explicit sharp witnesses; bounded representatives and section norms; row degrees and harmonic completion; individual translates; fixed factorial fillers | statement level. |
| **DP64** | for a CM subfield E ⊂ Q(ζ_m) and any CM type Φ: Σ_{p≤X, p∉S} log p Σ_i n_i c_{i,p} = (N/2) log X + O_{m,S}(N), and the same leading term for the integer floor certificates | **leading term checked.** For each i ∈ Φ the r = 1 indicator 1[σ_p i ∉ Φ] has Chebotarev density exactly ½ (a CM type contains half of every Galois orbit of embeddings, so half of the σ ∈ Gal(E/Q) send i outside Φ); Mertens gives Σ_{p≤X} log p/p = log X + O(1); the terms r ≥ 2 contribute O(1). The error constants are carried. **Meaning:** averaged over primes, every fixed CM type has the same leading budget N/2 · log X as the quadratic type of Alpöge's construction. |
| DP65 | on C = J^P × J̄^Q (E = Q(ζ_7), Φ = {1,2,3}), all CM rows with the actual embedding labels and bounded filler cost | statement level. |

**Counts.** 12 findings: logic of the leading term checked 1 (DP64); statement level 11. Refuted 0.

## 2. What the run settled in the end, and what it left open

**Settled:**
- Q1 (the bound for every height, with exact error): DP1-DP4 (optimal slope c_h = 1/(p−1) − 1/(p^h−1), constant h − 1, floor sum),
  DP34 (constant 1 on every dual direction), DP43 (loss = codimension for every cyclic CM type).
- Q2 (step 2): the exponent is the height-two case (DP6); the actual theta, period and denominator data of Alpöge's Lean
  construction are traced (DP21, DP24, DP38, DP44).
- Q3, locally: higher height cannot shorten step 8 by any local mechanism tested. Pure directions gain c_h, but the mixed
  lines the kernel follows have slope at most ρ_2 = 1/(p²−1) (DP42), harmonic polynomial selections at most c_* (DP51),
  p-divisible tensors are cancelled by the normalization (DP50), and averaged over primes every CM type has the same leading
  budget (DP64).
- Q4 (cote 54 scans 5-7, cote 4): the boxed zero p-operation concerns the universal vector extension (DP10), with Oda's Cartier
  comparison; the cote 47 and 54 readings are author's slips (autograph checked by the run).
- Q5 (suggestion 9): identity Frobenius lifts are binomial rings (DP11); Horel's reconstruction (DP13); the historical
  locators of cotes 133 and 137 found from pixels.

**Left open:**
- **Q3e, the global question:** an actual mixed-type family on a CM Jacobian (DP22, DP45, DP49) with its prescribed sections,
  row degrees, the six lift identities and the full cost comparison that would give a net integer saving of lifts. Every local
  ingredient is now built (DP54-DP65: global jets, endpoint detection, translates, norms, row data); the global inequality is not.
- **Q5f:** the B7 comparison of our earlier run, whose precise statement was never supplied.

## 3. Scope and frameworks
U throughout: no finding uses A or M. Frameworks as in parts 1-3: Dieudonné displays and Cartier duality (cote 54, cote 4), formal
biextensions (SGA 7 I, Exp. VII-VIII), Picard schemes of CM Jacobians (FGA, Bourbaki 232, 236), λ-rings (SGA 6 V).

## 4. Integration (final)
- **Fable suggestion 2** (FABLE_PROGRAM_SUGGESTIONS_20261120.md): "the bound is proved and optimal (DP1-DP4, DP34, DP43); the
  proposed use, faster multiplicity from larger height, is refuted for every local form tested (DP42, DP50, DP51) and for the
  prime-averaged budget of every CM type (DP64)".
- **Prompt 34, item 3:** "locally answered in the negative; the global count is open (Q3e)".
- **Our bridges files and the HODGE line:** DP42/DP51/DP64 are reasons that Alpöge's coefficient p/(p²−1) is not improved by
  changing the CM type or the height; record next to DP6.
- **Text of record (cotes 47, 54):** as in the cp02 intake: keep the diplomatic readings, add the emendations as notes.
- **Suggestion 9:** cote 133 archive pp. 5, 26-28 and cote 137 archive pp. 37-38 as the binomial/plethystic locators; Q5f open.

## 5. Prompt updates (the successor of DP_MULT)
1. **One question only: the net lift count.** On Jac(y² = x^7 − 1) at p = 11 (DP49) or p ≡ 3, 5 mod 7 (DP45), with the
   built interfaces DP44, DP52, DP54-DP65, write the actual mixed-type family and compute the cost difference Q_{M′} − Q_M of
   DP44 with the real g_j, e_j, H. Either exhibit M′ < M with a valid chain, or prove that Q_{M′} − Q_M < 0 for every admissible
   choice, which would settle prompt 34's item 3 in the negative for this construction.
2. Attach the run's paper (126 pages) and its CHECK_EVENTS, and tell the successor not to re-derive DP1-DP65.
3. Ask for the literature check of DP1-DP3, DP32, DP34, DP42, DP51, DP64 (Bannai-Kobayashi, Katz 1981, Hazewinkel, Zink,
   Ditters), which the run never made.
4. Q5f: supply the precise B7 statement from the earlier run, or drop the row.
5. Model and effort: GPT-6 Astra (ChatGPT Pro mode).

## 6. Hexagon readiness: H09 (list the changes; I have not edited the register)
H09's gate was "the run's final"; this is it.
- **Test 1 (complete):** yes for the content of the post: DP1-DP3, DP34 (pure directions), DP42 (mixed lines), DP51 (harmonic
  selections), DP64 (prime average). The global question is open, but the post does not need it.
- **Test 2 (self-contained):** yes: Hazewinkel, Lubin-Tate, Tate, Zink, Chebotarev; no RH, no Masullo.
- **Test 3 (stable):** **now met on our side** (the run has ended). The literature search is still not done.
- **Test 4 (checked):** DP1-DP3, DP34, DP42 checked by me (DP42 with DP41's multiplier lemma carried), DP64's leading term checked,
  115 exact computations for DP1/DP3. Not yet: DP41 and DP51 in full, and an independent computation of a mixed-line slope.
- **Test 5 (interest):** moderate to high: it explains the exponent of Alpöge's step 2 and shows that the higher-height idea does
  not improve it.
- **Gates left:** the literature search; an intake read of DP41 and DP51; one independent computation of DP42's slope (for
  instance p = 3, h = 3 on the last dual axis). **One stage from a post.**
