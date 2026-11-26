# Intake of ZETA_HEAT checkpoint 03 (prompt 62): diff from cp01

Written 23 Nov 2026 (~23:5x UTC) by Claude Opus 5.5 at effort high (agent afa2696b67cad55de, a copy of af2a18f62da23b48e),
at the request of the main session 329fb1e6 (Claude Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode),
still going.
- Read: checkpoint 03, 23 Nov 18:23 UTC (`research_returns/ZETA_HEAT_checkpoint_03_20261123T1823Z_unzipped`). It is
  the newest filed; I checked again before delivering.
- Checkpoint 02 never reached our folders, so this is a diff cp01 → cp03.
- Brief: `INTAKE_WAVE_20261123_EVENING.md`.
- Previous intake: `INTAKE_ZETA_HEAT_20261123_cp01.md`.

A is Alpöge's theorem: RH for every Dirichlet L-function, ζ included.

## 0. Scope: what was read
- **Diff by hash.** 88 new files, 57 changed, 1 removed (the old MANIFEST, replaced by
  `versions/checkpoint_03_manifest.sha256`).
- **Registers:**
  - QUESTIONS.tsv: 20 rows; new rows COMMON-HEIGHT, DENSITY-DETECTION, THETA-LOWER;
  - STATEMENTS.tsv: ZH.STMT.032–062 are new, 31 statements;
  - LEDGER: the entries of 17:32 and 18:19 UTC;
  - CHECK_EVENTS.tsv: 217 events against 104 at cp01. By type: 85 independent re-proof, 66 targeted proof check,
    28 used and rechecked, 25 computation or formal certificate, 7 carried as background, 5 refuted with a refined
    statement, 1 other.
  - `records/BUILD_CHECKPOINT_03.md`: 124 pages, no overfull box, with the run's visual check of 11 pages.
- **Read in full, with proofs:**
  - `paper/sections/arithmetic_compressions.tex`: thm:fd-arithmetic-complete, prop:fd-even-operator,
    prop:fd-certificate-size, the explicit-formula evaluation and the certificate table;
  - `global_growth_numeric.tex`: lem:fd-multiplicity-log, cor:fd-global-growth-numeric;
  - prop:orbital-unimodal-bound in `trace_detection.tex`;
  - in `theta_kernel_hierarchy.tex`, §1 (the theta image), §§ "What direct compact truncation proves" and "Exact
    removal of the stated trial mode";
  - `open_questions.tex`;
  - `drafts/motion_collisions/CHARACTER_LIMIT_OBSTRUCTION.md` (first half).
- **Read at statement level:**
  - prop:prolate-upper, prop:odd-prolate-upper (`prolate_upper_bound.tex`);
  - prop:finite-weil-lower, prop:finite-weil-block;
  - `PRIME_POLE_CANCELLATION.md` (identity (1));
  - the QUESTIONS gates of the motion, deformation, density and moment rows.
- **Not read:**
  - the proofs of common_deformation, common_regions, uniform_deformation, gaussian_moments, motion_bending,
    positive_kernel_surgery, positive_density_detection, boundary_multiplicity, contour_example and
    executed_probe_certificate;
  - the independent-reproof notes;
  - the certificate JSON shards. I did not run the run's checkers: my replay below is my own code.
- **Opened for one locator:** ALP_CONNES cp44 `ALP_CONNES/modules/spectral_real_zero_selection.tex`, (RZ.5).

## 1. Verdicts (this task)
- **thm:fd-arithmetic-complete.** Confirmed by a targeted proof check. I followed every step:
  - S_k = 2Σ m_γ γ^{−2k} from the paired Hadamard product;
  - tr C^{2k} = 2Σ γ^{−2k} over the distinct ordinates;
  - s_j(PCP) ≤ s_j(C) gives D_{N,k} ≥ 2Σ(m_γ − 1)γ^{−2k} ≥ 2E(T)T^{−2k};
  - min-max monotonicity in N;
  - trace-norm convergence of the 2k-th powers from Hilbert–Schmidt convergence. This takes Suzuki's C_N → C in HS
    as cited, and I did not open it in this task;
  - ‖v‖_{2k} ↓ v_max, which gives sup H_{N,k} = γ_*;
  - the bounded-height equivalence;
  - x_* = 2γ_*, which gives lim a·j_*(−a) = ½(sup H)².
- **The certificate table: confirmed by computation.** Two layers:
  1. **The table arithmetic.**
     - dim V_N = 2N·2^N − 2;
     - the prime-power counts 5, 24, 98, 465, 2532, 15040, and the largest prime power 162751;
     - U < 2/T^{2k} in all six rows;
     - consistency with the tail bound of prop:fd-certificate-size and with d_N ≥ 2n(T), where n(97.632) = 28;
     - the operator bound (2/√3)U^{1/6} = 0.013275 < 0.0133.
  2. **An independent replay of D_{N,k}.** Script:
     `<local>/AppData\Local\Temp\claude\f2c80a22394db22f\329fb1e6-0570-47be-9060-a2a454bf3e15\scratchpad\replay_weil_compression.py`.
     - I wrote it from the formulas of the section only, in mpmath floating point at 40 digits:
       - the explicit formula (eq:fd-arithmetic-weil);
       - the hat correlation b, in closed form, and its primitive;
       - G, B and (−1)^k tr((G^{−1}B)^{2k});
       - S_k from the Taylor series of log Ξ, with no zero ordinates.
     - Results against the run's upper enclosures U:

       | (N, k) | D (replay) | U (run) |
       |---|---|---|
       | (1, 9) | 3.94653014373e−21 | 3.946530144e−21 |
       | (2, 3) | 2.5391051101e−8 | 2.539105111e−8 |
       | (3, 3) | 5.41964807266e−9 | 5.419648073e−9 |
       | (4, 2) | 7.8803302378e−7 | 7.880330238e−7 |

       All agree to 9–10 digits, and each replayed D lies below U.
     - Rows N = 5, 6 (height 97.632) were not replayed: they are too large for plain mpmath here.
     - So the four rows through height 39.913 are recomputed independently, but not rigorously; the run's Arb
       enclosures are its own. I also checked by hand the constant conversion from CCM (3.2)–(3.7), namely
       2∫(e^{−2x} − e^{−x})/(1 − e^{−2x}) dx = −log 4.
- **lem:fd-multiplicity-log (m_γ < ¾ log γ for γ ≥ 10).** Confirmed by a targeted proof check:
  - the 2/3 contribution of the zero, under A;
  - Re ψ(1+iy) < 1 − γ_E + ½ log(1+y²);
  - A₂ < 3/5;
  - 11/10 − ½(γ_E + log 2π) < −1/20.
- **cor:fd-global-growth-numeric.** Confirmed by a targeted proof check and a computation:
  - L_J > 97.632²/2 = 4766.003712;
  - the m = 2 term 97.632π/√2 = 216.8838;
  - for m ≥ 4, γ > e^{4m/3}, with the value at m = 4 equal to 297.0069 > 297;
  - the two-sided comparison L_T versus L_J. Its upper half uses 𝔯_m ≤ π√(m−1), cited as earlier proved; I did not
    check that.
- **prop:orbital-unimodal-bound (𝔯_m² ≥ 4π²(m+1)/(3m²)).** Confirmed by a targeted proof check:
  - E Y² = m V_X/(m+1), from the Dirichlet moments of a Haar row, with tr D_m = 0 and tr D_m² = m(m−1);
  - V_X ≤ mR²/4;
  - the inequality sinc u ≥ ½ − u²/(2π²), checked on a grid of 20001 points (minimum ≥ 0, equality at π);
  - unimodality through the Gelfand–Tsetlin polytope and Brunn–Minkowski. Olshanski's corner formula is taken as cited.

  It agrees with the cp01 values 𝔯₂ = π (equality in both bounds) and 𝔯₃ = 2π/√3.
- **The theta image.** Confirmed by computation by hand: M_h(s) = ½s(s−1)π^{−s/2}Γ(s/2) for
  h = (4π²u⁴ − 6πu²)e^{−πu²}, and the j = 0 tail ∫_L^∞|K|² ~ 4π³λ⁷e^{−2πλ²}.
- **The character-limit obstruction.** Confirmed by a targeted proof check. I derived it myself: Z_j'/Z_j real gives
  Re(L'/L)(s₀, χ_j) = −θ_j'(t₀) = −½ log(q_j/π) + O(1) → −∞, against the boundedness forced by locally uniform
  convergence to F(s₀) ≠ 0.
- **The exponent correction** (the run's SPEC-POWER-NORMALIZATION). Confirmed at the source: ALP_CONNES cp44 (RZ.5)
  reads a₂(log λ) ≥ cλ^{9+α}e^{−4πλ²}, for some c, α > 0. Our prompts 62 and 68 wrote λ^α.
- **Everything else** is at statement level, carried by the run's own events.

## 2. What is new, usefulness first
1. **Simplicity becomes a terminating search at every height** (thm:fd-arithmetic-complete).
   - Usefulness:
     - an exact, finite and arithmetic criterion, using prime powers and archimedean integrals and no zero ordinates;
     - all-height simplicity is exactly unboundedness of sup H_{N,k};
     - the heat-flow Jensen constant equals ½γ_*², which ties the heat side of cp01 to Suzuki's compressions on
       windows [−N, N].

     It is for readers of the zero-simplicity and de Bruijn–Newman literature, and for prompt 68 (item 3 on D_N,
     research item 5).
   - Checked by us: the proof, and four of six certificate rows replayed.
   - Result: every zero with 0 < Im ρ ≤ 97.632 is simple. This is the run's rigorous certificate; we replayed it
     through 39.913.
2. **Constraints on any proof by these certificates.**
   - ‖C − C_N‖ ≤ (2/√3)D_{N,k}^{1/(2k)}, with 2/√3 sharp for the block estimate (prop:fd-even-operator);
   - a certificate at height T needs dim V_N ≥ 2n(T);
   - in one fixed space, k → ∞ returns the threshold to γ₁ (prop:fd-certificate-size).

   Usefulness: they say what a quantitative all-height proof must do, namely let N and k grow together.
3. **Explicit global constants** (cor:fd-global-growth-numeric, checked by us). The heat-flow limits satisfy
   L_T > 216.88 and L_J > 4766.003712, and L_T and L_J determine each other within √log factors. With
   m_γ < ¾ log γ (checked by us), this is the first unconditional-in-multiplicity numerical form of cp01's
   thm:fd-limits.
4. **The sharper orbital radius** (checked by us). 𝔯_m² ≥ 4π²(m+1)/(3m²) and (m−1)𝔯_m² ≥ π². These replace the
   variance constant of cp01: the global transport is now π/√𝒟_N, against π√15/(4√𝒟_N).
5. **The window eigenvalue range is now pinned** (prop:odd-prolate-upper, statement level).
   - An odd prolate competitor from modes 2 and 6 gives a₂(log λ) ≪ λ^{13+ε}e^{−4πλ²}.
   - With q(v_L) ≪ λ^{9+ε}e^{−4πλ²}, the needed gain is exactly λ^{9+α} with 0 < α ≤ 4.
   - Also: b_L, the one-mode restriction, satisfies a₁ + a₂ − q(v_L) ≤ b_L ≤ a₂ (Ky Fan), so b_L carries the problem.
   - Direct compact cutoff of the theta profiles reaches only e^{−2πλ²}.
   - Usefulness: this corrects the target in our own prompts, and states the THETA-LOWER gate exactly.
6. **Finite height closed by two independent methods** (COMMON-HEIGHT, the run's).
   - A spectral residual/projection probe and a whole-edge heat contour both certify the packet through height 20.
   - The contour alone certifies through 45, with 8 simple real centres.
7. **Further proved rows (the run's):**
   - DENSITY-DETECTION: all three detection indices are infinite on the surviving positive-density packets;
   - a positive-kernel surgery that keeps the even superexponential heat class and threshold 0 while imposing a
     double endpoint. It shows that leading moments cannot decide MAIN-MOMENTS;
   - exact Poisson and prime-ramp multiplicity identities;
   - Gaussian restricted moments, anisotropic continuation, and conductor-uniform deformation;
   - the motion second jets.
8. **Negatives, each a precise obstruction:**
   - **Character limits.** For primitive real characters of fixed parity and growing conductor, no rescaling
     c_jL(s, χ_j) converges near a critical-line point to a function that is nonzero there (checked by us). The run
     extends this to complex characters.
   - **Gap isolation.** Small absolute gaps plus a positive fraction of short normalized gaps do not force κ → 0. A
     periodic triple-cluster function has κ ≥ 4/9 (PAIR-Q2).
   - **Prime-pole cancellation.** The RH prime-count remainder cancels the leading pole kernel exactly, by identity (1)
     of PRIME_POLE_CANCELLATION, but loses a derivative, too much for the a₂ target.
9. **The main question is open.** MAIN-SIMPLE: sup_{N,k}(2/D_{N,k})^{1/(2k)} = ∞. The gate is proved through 97.632
   only.

## 3. Scope of the inputs
- A enters through the zero location in C, in the 2/3 step and in the cone estimates.
- Suzuki's HS convergence and Olshanski's corner formula are cited.
- The certificates use only Λ(n) for n < e^{12}, archimedean integrals and the Taylor series of ξ at ½.
- Masullo is not used.

## 4. Integration (applied)
- `field_experts/structural_maps_20261123/NCG_ZETA.md`, my own note, attached to prompt 68 as `ours/structural/`:
  - §3(a), the failure-scale cell: corrected to the exponents 9+ε / 13+ε / 9+α;
  - §3(b): added the exact heat–window link of thm:fd-arithmetic-complete;
  - §4.3: replaced the heuristic a ~ 1/L² by the rate question that is actually left.

  Backup: `integration_backups/20261123/ZETA_HEAT/NCG_ZETA.md.bak_before_cp03`.
- The primer was updated in place. Backup: `PRIMER_ZETA_HEAT_20261123.md.bak_cp01`.
- **For the main session:**
  - the two cp01 board rows are still unapplied; one is now superseded, see §7;
  - the copy of NCG_ZETA.md inside the prompt-68 zip is the old one;
  - the prompt edits of §5.
- Log: `INTEGRATION_ZETA_HEAT_20261123.tsv`.

## 5. Prompt updates: prompt 68 (CONNES_AFTER_RH, waiting), as edits for the main session
1. **Line 65 (item 5).** Replace "a lower bound a_2 ≳ λ^α e^(−4πλ^2) with 0 < α ≤ 4" by:

   > "a lower bound a_2(log λ) ≳ λ^(9+α) e^(−4πλ^2) with 0 < α ≤ 4 (ALP_CONNES cp44, (RZ.5); the trial quotient is
   > ≪ λ^(9+ε)e^(−4πλ^2) and an odd competitor gives a_2 ≪ λ^(13+ε)e^(−4πλ^2), ZETA_HEAT cp03 prop:odd-prolate-upper,
   > so α ≤ 4 is forced)".

   As written, the prompt asks for a bound weaker than the trial quotient, which would prove nothing. Prompt 62 has the
   same slip; the run caught it (SPEC-POWER-NORMALIZATION).
2. **Item 6 (lines 69–79).** Attach `ZETA_HEAT_cp03` in place of cp01, with this intake. Add to the list of that run's
   results:

   > "thm:fd-arithmetic-complete: with D_{N,k} = S_k − tr C_N^{2k} for Suzuki's compressions, sup_{N,k}(2/D_{N,k})^{1/(2k)}
   > is the first multiple ordinate, lim a·j_*(−a) = ½(sup)^2, and the zeros through height 97.632 are certified simple
   > from prime powers below e^{12}; prop:fd-even-operator ‖C − C_N‖ ≤ (2/√3)D_{N,k}^{1/(2k)}; prop:fd-certificate-size
   > dim V_N ≥ 2n(T); the one-mode restriction b_L with a_1 + a_2 − q(v_L) ≤ b_L ≤ a_2 (THETA-LOWER)."
3. **Research item 3 (the D_N question).** Replace "the trace defect D_N of the other run's prop:trace-height" by "the
   trace defects D_{N,k} of the other run's thm:fd-arithmetic-complete (k = 1 is prop:trace-height)". Ask: is D_{N,k}
   the 2k-th moment defect of a cutoff in the sense of T50, and does T50's unconditional positivity give
   D_{N,k} ≥ 0 without A?
4. **Research item 5, bullet "One mechanism in four places".** Replace the last sentence ("If matching the two failure
   scales, a ~ 1/L², gives an estimate on the actual Weil operator, state it with its proof: it is the gate of both
   runs.") by:

   > "At the level of limits the two deformations are already one invariant: the other run's thm:fd-arithmetic-complete
   > gives lim a·j_*(−a) = ½(sup_{N,k} H_{N,k})^2 = ½γ_*^2, with D_{N,k} computed on the windows [−N, N]. What is open
   > is the rate: bound j_*(−a) or m_*(−a) at a given a by D_{N,k} at explicit N(a), k(a), and compare with a_2(L) at the
   > scale λ^(9+α)e^(−4πλ^2). If your work on the cutoff gives such a rate, or the lower bound for b_L, state it with
   > its proof: it is the gate of both runs. Direct compact cutoff of the theta profiles reaches only e^(−2πλ^2)
   > (ZETA_HEAT eq:theta-hier-22)."
5. **The zip.** Replace `ours/structural/NCG_ZETA.md` with the corrected file.

Prompt 62 is sent and running, so there is nothing to change there.

## 6. Hexagon readiness
| result | state (this task) | gate left |
|---|---|---|
| thm:fd-arithmetic-complete | proof checked; rows N ≤ 4 replayed (non-rigorous) | a rigorous replay of N = 5, 6, or a reading of the Arb certificate; open Suzuki's HS convergence at its locator |
| cor:fd-global-growth-numeric + lem:fd-multiplicity-log | checked, except 𝔯_m ≤ π√(m−1) | check that upper radius bound |
| prop:orbital-unimodal-bound | checked (Olshanski cited) | open Olshanski Prop. 3.1 / Cor. 3.2 |
| thm:fd-limits (cp01) | analytic part checked | local Hermite part |
| character-limit obstruction | checked (real characters) | the complex-character version |

## 7. Board candidates (rows for `field_experts/hexagon/HEXAGON_BOARD.tsv`; for the main session)
| title | statement | what it adds | gate left |
|---|---|---|---|
| A finite arithmetic test for simplicity of the zeta zeros, exact at every height | Under A: for Suzuki's compressions C_N and S_k = −2k[z^{2k}]log Ξ, D_{N,k} = S_k − tr C_N^{2k} > 0, D_{N,k} ≥ 2E(T)/T^{2k}, and sup_{N,k}(2/D_{N,k})^{1/(2k)} = γ_* (first multiple ordinate). The zeros with 0 < Im ρ ≤ T are simple iff some D_{N,k} < 2/T^{2k}. lim a·j_*(−a) = γ_*²/2. Certified: all zeros through 97.632 are simple, from prime powers < e^{12} | a terminating, zero-free finite certificate; exact link of heat flow and Weil compressions | rigorous replay of the two largest rows; Suzuki locator |
| Explicit constants for the de Bruijn–Newman finite tests | m_γ < ¾ log γ (γ ≥ 10); L_T > 216.88, L_J > 4766.003712; (4π/3)√(L_J/log√(2L_J)) ≤ L_T ≤ (√3π/2)√(L_J log√(2L_J)); 𝔯_m² ≥ 4π²(m+1)/(3m²) | numbers for cp01's limits | the upper radius bound |

The cp01 row "A trace certificate for simplicity below a height" is superseded by the first row (k = 1 is that
statement), so it should not go up separately. The cp01 row on thm:fd-limits stays, with the second row merged into it.

## 8. For the P vs NP fleet (`pequalnp_work/fleet_map/PROOF_GRAPH.tsv`)
Map constructed, not graded.
- **Nodes:**
  - L-gct-128: weak Descartes, at most (#monomials − 1) distinct positive roots;
  - L-gct-138: Descartes for real exponents, a combination of N powers has at most N − 1 distinct positive zeros.
- **Translation.**
  - prop:fd-certificate-size says that a rank-d Hermitian compression certificate sees at most d/2 counted positive
    roots, and that the distinct-versus-counted gap is exactly E(T), read off by the moment defect.
  - The Descartes nodes bound distinct positive roots by the dimension of the space spanned, i.e. the number of
    monomials.
  - Dictionary:
    - the monomials x^{a_i} correspond to the basis b_j of V_N;
    - the number of sign changes corresponds to the rank of C_N;
    - multiple roots correspond to E(T).
- **Work to complete the bridge.** For a real exponential sum f = Σ_{i≤N} c_i e^{a_i x}, build the analogue of C_N:
  the compression of the multiplication-by-x⁻¹ operator to span{e^{a_i x}} in a positive form for which the zeros of f
  are the spectrum. Then prove the dimension bound (distinct positive zeros ≤ N − 1) as an instance of
  prop:fd-certificate-size, and read the multiplicity excess as a moment defect.
- **Not mapped:** the CUE and motion results, which have no node.
