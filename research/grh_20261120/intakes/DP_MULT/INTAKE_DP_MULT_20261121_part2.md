# Intake of DP_MULT (prompt 34), part 2: checkpoints 02-04, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), still going. Part 1 is `INTAKE_DP_MULT_20261121.md` (checkpoint 01,
DP1-DP24). Checkpoint 02 (DP25-DP33) was taken in `INTAKE_DP_MULT_cp02_20261121.md`; its verdicts are repeated here in one
line each so that part 2 is complete.

## 0. What was read, and the scope

- **Return folder:** `research_returns\DP_MULT_checkpoint_04_20261121T0250Z_unzipped` (packaged 02:50:48 UTC). Checkpoints 01-03
  have been retired from disk. Newest DP_MULT present at the start and at the end of this part.
- **Read:** `LEDGER.md` from "Checkpoint02 packaged" to the end (movement at 02:03, the Zink-convention correction after
  checkpoint 03, movement at 02:32, the first three-hour review at 02:50), the changed rows of `QUESTIONS.tsv`, and in
  `DP_MULT.tex` (2849 lines): the statements of DP34-DP48; the whole proofs of DP34 (lines 1054-1093) and DP42 (lines
  1852-1978); the statement and consequence of DP45 (2225-2250); DP44 (2127-2160).
- **Read in full, every step checked (2):** DP34 (the low-order operator identities (all-dual-low) carried from DP33), DP42
  (DP41's multiplier lemma carried).
- **Statement level, with arithmetic spot checks (13):** DP35-DP41, DP43-DP48. Spot checks: DP45's slopes and mean, its type
  A = {0,1,2} from the CM type {1,2,3} of y² = x^7 − 1 under p ≡ 3, 5 mod 7; DP42's weight identities.
- **Changes to earlier findings:** none of DP1-DP33 is withdrawn. One correction: DP38's signs (Zink's negative Artin-Hasse
  convention; coefficients −1/p and +1/p, DP39(b)'s value −(p−1)!/2); the run says all valuations and unit conclusions
  survive. I did not check DP38 in part 1, so no verdict of mine changes.

## 1. Verdicts on the new and changed findings

| Id | Statement (short) | Verdict |
|---|---|---|
| DP25, DP28, DP32 (cp02) | induced CM type ⇒ slope 1/2 at inert p; the direct higher-height `LemmaS` substitution fails; the actual Honda dual has directional slopes p^i/(p^h−1) | confirmed (cp02 intake). |
| DP29, DP31 (cp02) | scalar estimate with residual ρ_2; scalar higher-height correction is integral | proof read, cited theorems carried (cp02 intake). |
| DP26, DP27, DP30, DP33 (cp02) | | statement level (cp02 intake). |
| **DP34** | on every Honda dual, D_i^n f ∈ p^{max(0,⌈c_i n − 1⌉)}, c_i = p^i/(p^h−1); constant 1 optimal, common witness f_* = ∏_{j<d}X_j^{p−1}·X_d^{p²−1} with v(D_i^{q−1}f_*(0)) = p^i − 1 | **confirmed.** I checked: for n < q, ⌊n/R_i⌋ ≥ c_i n − 1 with R_i = p^{h−i} (write n = aR_i + r, it reduces to a ≤ p^i − 1), equality at n = q−1; the induction from D_i^q = p^{p^i}u_iD_i + p^{p^i+1}U_i (both terms ≥ c_i n − 1); the witness (Σ e_j m_ij = q−1 by telescoping, Σ e_j r_j = d, v((q−1)!) = (q−1)/(p−1) − h). The low-order identities D_i^p = aD_{i+1} + pT_i, D_d^{p²} = p^p bD_1 + p^{p+1}T_d are carried from DP33. |
| DP35 | compatible splittings with bounded denominators are integral; the weighted infimum w_t(B) is 0 or −∞; linear growth of denominators | statement level. |
| DP36, DP37 | unequal weights restore the kernel quantization; the true dual torus A_ζ with A_ζ^D = [ζ]; an invariant integral Poincaré frame and its unique invariant rational splitting | statement level. |
| DP38 (corrected) | first primitive Poincaré coefficients [S^pY_1]B = −1/p, [SY_d^p]B = +1/p; (log B)_{p+1} = (−S^pY_1 + SY_d^p)/p; D_G^pD_1B(0) = −(p−1)!, D_GD_d^pB(0) = (p−1)!, both units | statement level; the sign correction after checkpoint 03 noted. |
| DP39 | harmonicity removes full-series denominators for some data, but the `HaO` harmonic conditions do not transfer the bare integral-function gain through the primitive exponential | statement level. |
| DP40 | arbitrary-unit cyclic displays H_{A,u} of type A ⊂ Z/h: sharp directional slopes c_j = Σ_{i∉A}p^{[j−i]}/(q−1); dual = complementary display; the equally weighted type-plus-dual sum S_h(A) is maximal exactly for alternating type | statement level. |
| DP41 | the exponential of the primitive logarithm has exact inflation threshold a = p in the weights a·r; no nonzero bounded prefactor improves it | statement level. |
| **DP42** | for odd p, h ≥ 3, every primitive mixed logarithmic line t ↦ (ut, vt) in the actual pair has exact slope c_k^path = 1/((p−1)(p^k+1)), k = h − j the restricted-p nilpotency length of the reduced dual direction; the maximum over all such lines is 1/(p²−1), **independent of h** | **confirmed, DP41's multiplier lemma carried.** I checked: c_k^path = s − w_k; the arrow identities pω_{i−1} − ω_i = 1 and p²ω_d − ω_1 > 1; the product-family baseline excess vanishes only at i = d (w + pω_d − 1 − τ = 0); the unique initial term SY_d^p/p and the reduced inverse (−1)^{i−j}v̄_j^{p^{i−j}}T^{p^{i−j}}; the restricted-p reading (D_i^{[p]} ∝ D_{i+1}, D_d^{[p]} = 0). |
| DP43 | for every cyclic type, the optimal affine loss in direction i is the codimension h − m, with a periodic floor sum and one common sharp monomial | statement level (author and root readings; an independent review was in progress at checkpoint 04). |
| DP44 | the Lean `Ranks` record can be rebuilt at every smaller even M′ ≥ 2 (HC parameters, hosts, Hermitian spaces), but the terminal period and auxiliary signatures change; exact formula Q_{M′} − Q_M = −Σ_{j>M′}(g_j − e_j − H) for the cost comparison | statement level. |
| DP45 | for p ≡ 3, 5 mod 7, Jac(y² = x^7 − 1) over W(F_{p^6}) is connected of height 6, dimension 3, cyclic display of type {0,1,2}; slopes (p, p², p³)/((p−1)(p³+1)); mean c_2(p²+p+1)/(3(p²−p+1)) < c_2; largest slope exceeds c_2 by p/(p³+1) | **numbers and type confirmed** (3 and 5 are primitive roots mod 7; the CM type {1,2,3} occupies three consecutive places of the single Frobenius orbit; mean < c_2 ⇔ 2(p−1)² > 0; difference p/(p³+1) recomputed). Jacobian model carried from DP22. |
| DP46, DP47, DP48 | unit-arrow and invariant-frame independence of DP42; the hyperbolic Poincaré pullback; a quadratic gauge e^{ct²} cannot improve the path slope | statement level. |

**Counts (checkpoints 03-04).** 15 new rows (DP34-DP48): confirmed 2 (DP34, DP42), numbers confirmed 1 (DP45), statement
level 12. Refuted 0; withdrawn 0; corrected 1 (DP38, signs only, by the run).

## 2. What is new

- **DP42 is the decisive local fact of this round.** Along every primitive mixed line of G_h × G_h^D, the line the theta
  kernel actually follows, the slope is 1/((p−1)(p^k+1)) ≤ 1/(p²−1) = ρ_2, for every h. The gain c_h of DP1-DP3 grows with
  h, but it lives in the pure directions; the mixed (Poincaré) direction is best at height two. So "a formal factor of
  larger height wins multiplicity faster" (Fable suggestion 2's proposed use; prompt 34, item 3) is **false along every
  primitive mixed line**; DP48 adds that a quadratic gauge does not rescue it. What is still open is a non-primitive or
  selected-harmonic route (DP42's closing remark) and the global cost.
- DP34 and DP43 complete the local theory of part 1: optimal constant 1 on every Honda-dual direction, and loss equal to the
  codimension for every cyclic CM type. DP40 identifies alternating type as the maximum of the equally weighted sum.
- DP45 is the first actual Jacobian with three directions; its largest slope beats c_2 by p/(p³+1) but its mean is below c_2.
- Literature: none of DP34-DP48 is classical in this form as far as I know; they rest on Zink's displays (2002) and
  Hazewinkel. A search is still owed (H09).

## 3. Scope of the two proofs
Unchanged: every finding is unconditional (U); the Lean archive is used as a source of the definitions in which height two
enters (`Ranks`, `HCParam`, `Host`, the gain/main-term definitions in DP44), never as a premise.

## 4. Grothendieck's frameworks
DP35-DP38, DP41, DP47 are statements about formal biextensions and the Poincaré biextension of G × G^D (SGA 7 I, Exp. VII-VIII);
DP40 and DP43 about Dieudonné displays of p-divisible groups with CM (the crystalline side of cote 4 and of cote 54 scan 5's
Cartier duality); DP42's k is the length of the restricted p-power chain on Lie(G^D_k) (SGA 3 VII_A). The run states them
with Zink's displays and does not cite SGA 7; add SGA 7 I, Exp. VII-VIII as the framework locator.

## 5. Integration
- **Fable suggestion 2** (FABLE_PROGRAM_SUGGESTIONS_20261120.md): replace its "proposed use" by "pure directions gain c_h
  (DP1-DP3, DP34, DP43); the primitive mixed lines that a theta kernel follows have slope at most ρ_2 for every height
  (DP42), so higher height does not shorten step 8 along them".
- **Prompt 34's item 3 (the shorter chain):** the question narrows to: a non-primitive mixed line, a selected harmonic
  operator that is not a line restriction, or a global correspondence whose cost (DP44's Q_m formula) improves for reasons
  other than the local slope. That is the attack DP42 leaves open; DP44 gives the exact bookkeeping for it.
- **Alpöge step 2 in our bridges files:** add DP42 next to DP6: the note's coefficient c_2 = p/(p²−1) = s − ρ_2 is the
  pure height-two slope, and ρ_2 = 1/(p²−1) is the largest mixed-line slope at every height; both numbers are those of
  height two, whatever h.
- **Text of record:** no new transcription rows in checkpoints 03-04 (the cote 54/47 rows are as in the cp02 intake).

## 6. Prompt updates (successor of DP_MULT)
1. Main question: the selected harmonic operators of the source theta (`HaO`) and non-primitive mixed lines, against DP42's
   ceiling; or prove that every admissible selection reduces to a line restriction, which would settle prompt 34's item 3
   negatively for this construction.
2. DP44's cost formula: ask for the sign of g_j − e_j − H for the source's actual data, which decides whether dropping lifts
   at fixed data can ever pay.
3. Literature check of DP1-DP3, DP32, DP34, DP42 (Bannai-Kobayashi, Katz 1981, Hazewinkel, Zink, Ditters).

## 7. Hexagon readiness: H09 ("divided powers in Alpöge's step 2")
- **What the new checkpoints do:** they strengthen H09 and change its message. The post now has two halves: the pure-direction
  bounds (DP1-DP3, DP34: slope c_h, constant 1 on the dual) and the mixed-line ceiling (DP42: ρ_2 for every h). Together
  they explain why Alpöge's exponent a/p + a/p³ + … is where it is and why higher height does not improve it along the
  kernel's lines. That makes H09 more interesting, not less.
- **Tests.** 1 Complete: DP1-DP3, DP34, DP42 have complete proofs, checked by me (DP42 with DP41's lemma carried, so DP41 must be
  checked too). 2 Self-contained: yes (Hazewinkel, Lubin-Tate, Zink, Tate; no RH). 3 Stable: **not yet**: the run is still
  going (next review 03:50 UTC) and its final may add the harmonic case; literature search not done. 4 Checked: targeted
  checks plus my 115-check computation for DP1/DP3; DP42 and DP34 have no independent computation yet. 5 Interest: moderate
  to high.
- **Gate left:** the run's final, the literature search, a check of DP41, and an independent computation of DP42's slope on
  one example (for instance p = 3, h = 3, the line along the last dual axis). Still one stage from posting.
