# Intake of ALP_CONNES checkpoint 41 (prompt 55, follow-up 55b), by diff from checkpoint 28

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode), still going. This intake takes in checkpoint 31, which was filed but not read, through the same diff.

A is Alpöge's RH and GRH for Dirichlet L-functions, a theorem. Masullo's draft is not a proof, and nothing here rests on
it.

## 0. Read and not read
- **Register diff:** QUESTIONS.tsv against movement review 22, the run's full snapshot at the cp28 time. Of 1042 rows,
  3 are new and 2 changed state.
- **Gate diff:** the main-gate table of review 31 against review 22. Reviews 23-31 give their movement lines: review 23
  says no, all others yes.
- **The statement list of the new modules, G140-G208.** The statements of G172, G175, G186, G203 and G207 were read in
  full. Their proofs were not read.
- The DELTA23 row (Q-B08) and its IMPLICATIONS.md paragraph (line 508).
- **Not read:** CHECK_EVENTS row by row, the proofs of G140-G208, the cote 16 scan readings.

## 1. What moved
- **Four main gates:** H04.4, cubic RH (now "R_cub"), the T51 limit without zero location and the a₂ lower bound are
  all unchanged.
  - Q3 and Q4 changed only by integrating S47-S52, already taken in at cp24 and cp26, plus new "derivative
    competitors". These rule out lower estimates with α > 4 for a₂; every 0 < α ≤ 4 stays open.
  - Q1, Q2, Q5, Q6 and the BCM follow-up row are word for word those of review 22.
- **Connes-Consani F₁, Deninger, BC/BCM:** nothing new.
- **The cubic branch: about seventy new strict-vanishing rows and "window" reductions (G140-G208).** These remove
  proved sectors from the H04.4 arithmetic budget. Examples:
  - G175: for ℓ ≥ 5, δ primitive of 2-power conductor 2^c with 2^c > 84ℓ(ℓ+1)², and any character ε₇ mod 7, the strict
    group of δε₇ω_ℓ^{−s}κ^{−1}c^{−e} over K = Q(√−3) vanishes for every s, e and κ. This is unconditional.
  - G203 and G207: strict zero for the cubic labels χ^j, and their quadratic twists, at every prime
    ℓ ≡ 1 mod 3, ℓ ≠ 7, 269, with 269 a noncube mod ℓ, whenever ℓ−1 | e. This gives the exact deletion identity
    R_J = R_{J∖M(T)}.
  - G172: a common arithmetic window for the abelian sector, bounding 𝓑(F_u, u^401) = o(exp(u^ε/2)) under the
    retained source inputs.
  - G186, a negative result: for χ₋₇, δ = 1 and every odd e, O/2O injects into the strict group. So the quadratic-seven
    family is not strictly zero at coefficient 2.
  - G185: the class number of Q(ω, ζ₇+ζ₇⁻¹) is 1, by an elementary proof.
- **Grothendieck dictionary:** cote 16, scans 43-49, read at scan level, with locators and transcription corrections
  (QG27, QG46). No mathematical gate closes.

## 2. Checks by us
| statement | done | outcome |
|---|---|---|
| AC-G185 | independent re-proof | **Confirmed.** The discriminant of L = Q(√−3)·Q(ζ₇)⁺ is (−3)³·49² = −64827. The Minkowski bound is (4/π)³·6!/6⁶·√64827 ≈ 8.1. The primes 2, 3, 5 have residue degree 6, 3, 6 in L (2 inert in both factors; 3 ramified in K, inert in the cubic; 5 inert in both), so every prime ideal over them has norm above the bound. Over 7: N_{L/K}(a−ω) = −f(ω) for f = x³+x²−2x−1, so −f(ω) = −ω(ω−2) and N(a−ω) = \|ω−2\|² = 7. Hence the primes over 7 are principal, and Cl(L) = 0. |
| Q-B08 (Δ) | comparison with our DELTA23 intake | see §3 |

## 3. Δ on GT̂: the run against DELTA23
**Same object, same claims, no conflict.**
- The run (Q-B08, IMPLICATIONS line 508): (−1)^δ = χ₁₂(u_H) on H. On the full gentle group,
  (−1)^Δ = χ̄₁₂(ū), with ū defined only modulo {1, 11}. It is not the cyclotomic multiplier character.
- `intakes\DELTA23\INTAKE_DELTA23_20261121.md`:
  - D23.L1: L₂L₃ = (−1)^δ = χ₁₂(u), with u the CRT representative of (−1)^{a₂} mod 4 and (−1)^{a₃} mod 3;
  - D23.L5: the product is choice-independent, and neither bit is a Dirichlet character of the multiplier;
  - A.7: Δ|GT̂ = 0.
- These agree. χ₁₂(11) = χ₋₄(11)χ₋₃(11) = 1, so χ₁₂ is well defined modulo {1, 11}, which is the run's descent.
  "Not the cyclotomic character" is D23.L5.
- **What needs correcting is our own shorthand** "Δ on GT̂ = χ₁₂∘u" (the coordinator's direction of 21 Nov, point
  (3)). Δ vanishes on GT̂ (A.7). The formula holds on the gentle group GT̂₀, with u the CRT representative of the frame
  bits, taken modulo {1, 11}, and not the cyclotomic character. Edit to list, not made by me: wherever our records carry
  the shorthand.

## 4. Converging or stalled
The reviews say yes 8 times out of 9, all for cubic sector removals. By the 17 Nov criterion, none of the main gates
moved. The run is productive on the H04.4 budget's arithmetic sectors and is not converging on its main questions.

## 5. Hexagon readiness
| result | proved / checked by us / new? | one gate left |
|---|---|---|
| AC-T51 (cp18): Connes's trace formula over Q ⇔ A | proved; deduction checked by us | the comparison with Connes 1999 §VIII and Connes-Consani-Marcolli, and a check of the analytic inputs T25-T43 |
| AC-S50 (cp24): finite prime-built real-rooted approximants converge to Ξ/Ξ(0), with multiplicities, under A | proved; checked by us | the comparison with Suzuki arXiv:2610.32704 |
| K-groups of Q(ω, ∛269) at 3 (cp18) | proved; deductions checked, certificates not replayed | a replay of the PARI certificates and the K10-K20 proofs |
| G175 (uniform 2-power-conductor strict vanishing) | proved by the run; statement read only | an expert check, and a literature comparison with Washington's theorem on ℓ-parts in the cyclotomic Z₂-tower and its effective versions |
| G185 | proved and re-proved by us | not new: a routine class-number computation. No post |
| G186 (coefficient-2 obstruction) | statement only | a check; it bounds a route, not a post on its own |

## 6. Not for GitHub
- `input_material/`.
- The .lean interface files.
- `evidence/ALPOGE_remark.txt`.
- The publisher transcriptions of cotes 2 and 16.
- The third-party texts listed in the cp24 intake.
