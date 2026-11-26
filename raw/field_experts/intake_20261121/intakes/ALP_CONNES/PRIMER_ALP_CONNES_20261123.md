# Primer: the mathematics of ALP_CONNES (prompt 55), as of checkpoint 44

For the main session after a compaction. Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent
afa2696b67cad55de). It is drawn from the intakes cp18, cp24, cp26, cp28, cp41 and cp44 in this folder. The run is
GPT-6 Astra (ChatGPT Pro mode). Module paths are relative to
`research_returns/ALP_CONNES_checkpoint_44_20261123T1226Z_unzipped/ALP_CONNES/modules/`.

A is Alpöge's theorem: RH for every Dirichlet L-function, ζ included. Check levels are only those recorded in our check
events, named "checked by us" below. Everything else carries the run's own checks.

## 1. The trace formula over Q (Connes's programme)

**AC-T51** (`trace_unconditional_converse.tex` 301-401).
- **Setting.** For a primitive χ of conductor q, put E_χψ(x) = √x Σ χ(n)ψ(nx); for χ = 1 subtract x^{−1/2}∫ψ. Take the
  parity-selected prolate functions with time radius Λ, frequency radius Λ/q and index ≤ 4Λ²/q. Q_Λ is the sum over χ
  of the projections onto their E_χ-images, completed for χ = 1 by two polar lines on which dilation acts by a^{∓1/2}.
- **Statement.** A holds iff, for every Bruhat test h on C_Q,
  lim [2 log Λ · h(1,1) − Tr(Q_Λ R(h)) + ∫h₁(r)(r^{−1/2} + r^{1/2}) d*r] = W(h), Weil's distribution.
- **Proof, ⇒.** AC-T41 (nonprincipal sectors), AC-T44 (the principal two-constraint sector), AC-T45 (the polar lines
  are a trace-norm rank-two correction, unconditionally) and AC-T46 (assembly). These use A through the inverse Gram
  bound.
- **Proof, ⇐.** AC-T50 proves unconditionally that the cutoff defect is asymptotically positive. It uses the Möbius
  bound of Matomäki-Shao-Tao-Teräväinen at polynomial frequencies (AC-T49) to invert the theta map on the window. Then
  the assumed limit gives W(f∗f*) ≥ 0. The Connes-Consani-Marcolli criterion (Prop. 6.2, Cor. 6.3) gives A.
- **Check by us:** the deduction, given T25-T43 and T47-T48.
- **Credit (the H27 editor, Claude Fable 5.2 at effort max):** the statement is Connes's own. Ours is the proof for this
  cutoff.

**AC-T44, T45, T46.** No fault found by us in the proofs, given their imported lemmas.

## 2. The prolate spectrum and simplicity (Connes-Consani-Moscovici)

All in `spectral_*.tex`.
- **S47 (under A):** the trial Rayleigh quotient satisfies q_L(k_λ) ≤ C_ε λ^ε(1 − ν₄), and
  a₁ ≤ C_ε λ^{9+ε} e^{−4πλ²}.
- **S48:** if the ratio q_L(v_λ)/a₂ → 0, the ground state is eventually simple and even, and its normalized transform
  converges to Ξ locally uniformly.
- **S49:** that ratio tending to zero forces every zeta zero to be simple.
- **S50:** finite Hermitian compressions of D⁻¹ to dyadic piecewise-linear spaces, built only from prime-side Weil
  pairings, give real-rooted P_N → Ξ/Ξ(0) with exact multiplicities.
  - Mechanism: H ≅ ℓ²(Γ, m) under A; C = D⁻¹ is compact. Spectral projections at the simple isolated eigenvalue 1/γ
    converge, and a fixed probe φ with φ̂ > 0 gives the weight |E a|²/φ̂(γ)² → m_γ. A Jensen cap bounds the tails.
  - Check by us: the proof.
  - Credit: a direct consequence of Suzuki, arXiv:2610.32704 (the H27 editor). It is his.
- **S51:** where a_e < a_o, the bottom-shifted quotient has a compact injective inverse whose inverse eigenvalues are
  the zeros of ê_L. A fixed relative odd gap gives the product over distinct ordinates.
- **S52:** an abstract compact example with the exact commutator in which the quotient norm diverges. So any route
  needs a quantitative estimate.
- **Open (review 34):** the ratio, the gap, and the lower estimates a₂ ≳ λ^α e^{−4πλ²} for 0 < α ≤ 4.

## 3. The cubic Kummer field E = Q(ω, ∛269) and the gate H04.4

**The K-groups (AC-G22, K12, K21-K23):**
- for e ≥ 1, the strict 3-adic Selmer group of χε^{−e} over K = Q(ω) is Z₃[ω]/λ^m, with m = 4 + [e ≡ 2 mod 3];
- K_{2e}(O_E)_(3) ≅ Z₃[ω]/λ^κ, κ = 5 + 2v₃(e) + [e ≡ 2 mod 3].

The mechanism runs in four steps:
1. Soulé's finiteness theorem gives cyclicity.
2. The reduction to the logarithmic class group of Q(ζ₉ + ζ₉⁻¹, ∛269), which is Z/9, gives the residue class.
3. The real-field descent (AC-K22) excludes the constant pattern.
4. The oriented action of ζ₉ ↦ ζ₉⁴ is multiplication by 4 (AC-K23), which picks r = 2.

Checked by us: the deductions, and the printed matrices recomputed. The PARI certificates were not replayed.

**AC-K09:** for this L-function, the Weil form on [−log t, log t] is at least the squared norm for 1 < t ≤ 4, with no RH.
Checked by us: the margin recomputed as 1.282.

**The gate H04.4** (ALP_MACHINE AM-H04, window form): for every θ > 1/2, G_p(y) ≤ C y^θ on windows [Y, Y^{1+δ}] gives RH
for L = ζ_F/ζ, F = Q(∛269). It is open.

**The arithmetic budget (AC-K25, K35; G-series):**
- AC-K25 moves the all-prime Selmer total to character groups over K, with error x^{409+161ε/5}(log x)².
- Then strict vanishing on original coefficients, family by family:
  - G114/G115/G125/G126 for the χ₋₄ and χ₋₂₀ towers at e ≡ 133, 267 mod 268. Checked by us: the G114 proof and unit
    certificate;
  - G130-G180 for the quartic and quadratic tame factors;
  - G173/G175 for two-power conductors at every ℓ ≥ 5;
  - G203 and G207 for the cubic labels at split primes with ℓ − 1 | e;
  - G209-G218 at coefficient 7.
- The 269-class certificates G129, G131, G133, G135, G137 work by unit saturation and interval isolation of the class
  number formula. Checked by us: the G129 units, saturation and ratio 189; the G135 units and saturation for one field.
- **G219** (`mixed_cubic_residual_trivial_upper_bound.tex`): the matched coefficient-7 family has S₇ ≅ O/7^{s(e)}, with
  s(e) ≥ 1, and s = 1 when 7 | e. The exceptional weights form nested single classes. The mechanism is in §1 of the cp44
  intake. Checked by us: steps 1-5.
- **G220:** the remainder keeps one matched pair, at cost < 7P.
- **G186:** at coefficient 2 the quadratic-seven family is not strictly zero at odd weights.
- **Open:** the largest matched pair, the unsupported mixed and noncritical terms, the numerical bound on the maximum,
  H04.4 and RH for the cubic character.

## 4. Other lines

**Deninger, through Morishita's comparison (AC-T15, T17, T18).**
- Morishita's surjection (2.2.7) needs the finite-kernel condition.
- The fiber of the mapping torus is a compact solenoid, not R_{>0}.
- Under A, the abelian orbit factors give ζ_F = ∏L(χ).
- Checked by us: T15 and T17, independently re-proved.
- No Lefschetz formula on the Deninger side.

**Connes-Consani F₁ and BC/BCM:** corrections to the supplied versions (G08-G21) and BCM neutrality. The run draws no
theorem from A for Riemann-Roch on Spec Z̄, the scaling site or zeta cycles.

**Δ on GT̂ (Q-B08):** (−1)^δ = χ₁₂(u_H) on H. On the gentle group the formula holds with ū modulo {1, 11}. Δ vanishes
on GT̂. This agrees with DELTA23.

## 5. Open rows and their gates
| row | gate |
|---|---|
| Q1 (the T51 limit without zero location) | identify the positive defect limit with W without zero location |
| Q3/Q4 (spectral) | a quantitative estimate on the actual Weil operator: the ratio, the odd gap, or a₂ with α ≤ 4 |
| Q5/Q6 (F₁ geometry) | no geometric arithmetic square or surface Riemann-Roch |
| Q7 / EB-Q02 (cubic RH) | the remainder after G220, then H04.4 |
