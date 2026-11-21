# Intake of DP_MULT (prompt 34), part 3: checkpoint 05, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), still going. Part 2 read checkpoint 04 (DP34-DP48).

## 0. What was read, and the scope

- **Return folder:** `research_returns\DP_MULT_checkpoint_05_20261121T0335Z_unzipped` (packaged 03:35:00 UTC); checkpoint 04
  has been retired from disk. Newest DP_MULT present at the start and the end.
- **Read:** the ledger after "Checkpoint04 packaged" (movement through DP51 at 03:20 UTC, through DP53 at 03:33 UTC), and the
  statements of DP49, DP50 with its corollary, DP51 with its corollary, DP52, DP53 (`DP_MULT.tex` lines 2563-3610). No proof read
  in full.
- **Statement level:** all five findings and two corollaries. The run reports author, root and independent whole-proof readings
  for DP49-DP53. No earlier finding is withdrawn or corrected.
- Q5e is split: its historical part is closed (from pixels: cote 133, archive pp. 5 and 26-28; cote 137, archive pp. 37-38); the
  B7 comparison is carried forward as Q5f.

## 1. Verdicts (all statement level)

| Id | Statement (short) | Verdict |
|---|---|---|
| DP49 | on Jac(y² = x^7 − 1) over W(F_{11³}), with w_0 = −(a + a² + a⁴) (w_0 + w_0^† = 1, w_0w_0^† = 2), the polarized completion is DP47's hyperbolic block G × H (G of height 3, dimension 1; H its dual); nonzero theta germs have nonzero restrictions in every primitive residue class | statement level; w_0 + w_0^† = 1 is consistent with a + … + a⁶ = −1 and a^† = a^{−1}. |
| DP50 + corollary | a p-divisible tensor exponent κ = p^aλ moves the threshold to r_j; after the source's normalization (`IsThRule.lean` lines 66-70: exponent M², factor M^{−deg}) the slope is p^j/(q−1) − v_p(M) < 0, so forcing p \| M cannot help | statement level. |
| **DP51 + corollary** | for every nonzero integral homogeneous differential polynomial P of degree n on ℓ copies of the primitive pair, v_p(P(∂)Θ(0)) ≥ c_*n − s·max Σ s_p(α_i), c_* = 1/((p−1)(p^{h−1}+1)), optimal; for ℓ ≥ 2 already optimal on the source's `HaO` submodule | statement level. **It closes the escape route left open in part 2** (selected harmonic operators): over all polynomial selections the universal slope is c_*, the smallest line slope of DP42, and c_* < ρ_2 = 1/(p²−1) for h ≥ 3. |
| DP52 | the smaller-rank rebuild of DP44 carries the endpoint period interface (TPar restriction, Hyp3 under 1801 ≤ k + M′ − 1 + t, the six-input induction) | statement level. |
| DP53 | on Jac(y² = x^7 − 1), odd p ≠ 7, the redistribution between the types Φ = {1,2,3} and Ψ = {1,2,4} keeps the leading bare-jet budget; sharp table with T(p) = p(p²+p+1)/((p−1)(p³+1)) | statement level. |

**Counts.** 7 statements, all at statement level. Refuted 0; withdrawn 0.

## 2. What is new, and how it bears
- Every **local** route to a shorter step-8 chain through higher height is now closed: pure directions gain c_h (part 1), but the
  mixed lines the theta kernel follows are bounded by ρ_2 (DP42), harmonic polynomial selections by c_* ≤ ρ_2 (DP51), p-divisible
  tensors are cancelled by the source normalization (DP50), and the cyclotomic redistribution keeps the leading budget (DP53). What
  remains open (Q3e) is global: the net lift count with the rebuilt endpoint period (DP44, DP52).
- **For Alpöge's note:** the height-two coefficient p/(p²−1) of step 2 is not an artefact of the choice of supersingular primes; on
  every local form of the mechanism the run tested, height two is optimal or tied.

## 3. Scope and frameworks
Unchanged: U throughout. DP49 and DP53 are statements on a concrete CM Jacobian (FGA Picard theory, Shimura-Taniyama); DP51 on
formal biextensions (SGA 7 I, Exp. VII-VIII).

## 4. Integration
- **Fable suggestion 2:** add "harmonic selections do not escape (DP51); p-divisible tensors do not escape (DP50)".
- **Prompt 34, item 3:** the local half is answered negatively; only the global count (DP44, DP52 interfaces) is open.
- **Cotes 133 and 137:** record the run's pixel locators (cote 133 archive pp. 5, 26-28; cote 137 archive pp. 37-38) in suggestion
  9's row; the B7 comparison (Q5f) stays open.

## 5. Prompt updates
1. Ask a successor only the global question: the net integer lift count for the rebuilt chain (DP44's Q_m formula with DP52's
   endpoint), or a proof that it cannot drop.
2. A literature check of DP1-DP3, DP32, DP34, DP42, DP51 before the paper calls them new.

## 6. Hexagon readiness: H09
- **Changed:** H09's second half is now a complete local picture: pure slope c_h (DP1-DP3, DP34), mixed-line ceiling ρ_2 (DP42),
  harmonic ceiling c_* (DP51). The post can say that the exponent of step 2 is the height-two one, and that no local
  higher-height refinement improves it.
- **Gates left:** the run's final; a literature search; an intake read of DP41 and DP51 in full (both carry the ceiling); an
  independent computation of one ceiling (for instance DP42 at p = 3, h = 3). The content is now complete enough to write up once
  the final lands.
