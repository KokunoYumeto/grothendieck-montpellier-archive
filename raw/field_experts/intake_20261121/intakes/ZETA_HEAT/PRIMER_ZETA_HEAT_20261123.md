# Primer: the mathematics of ZETA_HEAT (prompt 62), as of the final (23 Nov 2026, 22:19 UTC)

For the main session after a compaction. Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent
afa2696b67cad55de). Updated 24 Nov for the final (backups of the cp01 and cp03 versions in `integration_backups/20261123/ZETA_HEAT/`).
- The run is GPT-6 Astra (ChatGPT Pro mode). It ended INCOMPLETE on the main question under the two-review rule:
  9 rows proved, 2 refuted, 9 INCOMPLETE.
- Its paper: one 169-page text, "The simplicity question for the Riemann zeros after Alpöge's theorem".
- Files are relative to `research_returns/ZETA_HEAT_final_20261123T2219Z_unzipped/workbench/paper/sections/`.
- "Checked by us" means our check events (cp01 and cp03 intakes). Everything else carries the run's own checks.

A is Alpöge's theorem: RH for every Dirichlet L-function, ζ included. The run's main question is whether every zero of
ζ is simple. It is open.

## 0. Objects
- **The heat family.** H_t(z) = ∫₀^∞ e^{tu²}Φ(u)cos(zu) du, with Φ the positive theta kernel. Then
  H₀(z) = ξ(1/2 + iz/2)/8 and ∂_tH_t = −∂_z²H_t. Under A the zeros of H₀ are real: x = 2γ, with multiplicity m_x.
- **The finite tests.**
  - F_a(w) = H_{−a}(i√w)/H_{−a}(0) = Σ b_k(a)w^k.
  - m_*(−a) is the least order of a negative Toeplitz minor det[b_{j_v−i_u}].
  - j_*(−a) is the least degree N at which the Jensen polynomial J_{N,a} has a nonreal zero.
  - L_T = lim √a·m_*(−a) and L_J = lim a·j_*(−a).
- **The spectral side.** Ξ(z) = ξ(1/2 + iz). In the Weil Hilbert space (≅ ℓ²(Γ, m) under A), C has eigenvalue 1/γ
  on one coordinate per distinct signed ordinate γ.
  - P_N projects onto the mean-zero dyadic piecewise-linear space V_N on [−N, N], with mesh 2^{−N} and
    dim V_N = 2N·2^N − 2.
  - C_N = P_NCP_N, Suzuki's compressions.
  - S_k = −2k[z^{2k}]log(Ξ(z)/Ξ(0)) = 2Σ_{γ>0} m_γγ^{−2k}.
  - D_{N,k} = S_k − tr C_N^{2k} and H_{N,k} = (2/D_{N,k})^{1/(2k)}.
  - E(T) = Σ_{0<γ≤T}(m_γ − 1).
- **The window side** (ALP_CONNES S47–S52). a₁(L) ≤ a₂(L) are the lowest eigenvalues of the Weil form on [−L, L], with
  λ = e^L. v_L is the even prolate trial.

## 1. Finite detection along the heat flow (`finite_detection.tex`, thm:fd-limits)
- **Statement.**
  - √a·m_*(−a) → min_{m_x≥2} x𝔯_{m_x}/(2√2), and a·j_*(−a) → x_*²/8, with x_* the least multiple zero.
  - Here 𝔯_m is the least spread of a Hermitian X at which φ_m(X) = ∫_{U(m)} e^{i tr(D_mUXU*)}dU turns negative, with
    D_m the roots of He_m.
  - Simplicity ⇔ L_T = ∞ ⇔ L_J = ∞.
- **Mechanism.**
  1. Gaussian convolution: H_{−a}(z) ≈ H₀(z)e^{aL(z)²}, with L = H₀'/H₀.
  2. Cone estimates: all zeros of H_{−a} lie in |arg z| = O(√a).
  3. The local rescaling at a zero of multiplicity m gives He_m, and the minors become φ_m.
- **Checked by us:** steps 1 and 2; 𝔯₂ = π and 𝔯₃ = 2π/√3 (HCIZ).

## 2. The arithmetic test, exact at every height (`arithmetic_compressions.tex`) — new at cp03
**thm:fd-arithmetic-complete** (checked by us). Under A:
- D_{N,k} > 0 and D_{N,k} ≥ 2E(T)/T^{2k};
- D_{N,k} decreases in N to 2Σ(m_γ − 1)γ^{−2k};
- sup_{N,k} H_{N,k} = γ_*, the first multiple ordinate (∞ if none);
- the zeros up to height T are simple iff some D_{N,k} < 2/T^{2k};
- L_J = γ_*²/2 = ½(sup H)².

Mechanism:
1. Hadamard gives S_k = 2Σm_γγ^{−2k}, and tr C^{2k} = 2Σγ^{−2k}.
2. Compression lowers singular values, so tr C_N^{2k} ≤ tr C^{2k}.
3. Min-max gives monotonicity in N.
4. Suzuki's HS convergence, cited, passes to trace norm for 2k-th powers.
5. ‖v‖_{2k} ↓ max v, for v the list of 1/γ over multiple ordinates repeated m_γ − 1 times.

**Evaluation with no zero ordinates.**
- Gram and primitive matrices: G_{ij} = g((j−i)h) − g(jh) − g(ih) + g(0) and B_{ij} = a((j−i)h) − a(jh) + a(ih).
  Here g and a are Weil's functional W, in the explicit formula (eq:fd-arithmetic-weil), applied to the hat
  correlation b and to its primitive.
- Then tr C_N^{2k} = (−1)^k tr((G^{−1}B)^{2k}).
- Arb at 120 digits, with prime powers < e^{2N}.

| N | dim | k | D_{N,k} ≤ U | height T certified |
|---|---|---|---|---|
| 1 | 2 | 9 | 3.946530144e−21 | 14.134 |
| 2 | 14 | 3 | 2.539105111e−8 | 20.704 |
| 3 | 46 | 3 | 5.419648073e−9 | 26.782 |
| 4 | 126 | 2 | 7.880330238e−7 | 39.913 |
| 5 | 318 | 2 | 1.318023575e−7 | 62.413 |
| 6 | 766 | 3 | 2.309270917e−12 | 97.632 |

So every zero with 0 < Im ρ ≤ 97.632 is simple. That is the run's rigorous certificate. Our non-rigorous replay
(own code) reproduces all six rows to 10 digits: at cp03 for rows 1–4, and in the final intake for rows 5 and 6, with
D_{5,2} = 1.31802357404e−7 and D_{6,3} = 2.30927091610e−12.

**prop:fd-inertia-complete** (final; checked by us). ι_N(T) = ind_+(TH_N − G_N) is the number of eigenvalues of C_N
above 1/T.
- It increases in N, is at most n_dist(T), and eventually equals n_dist(T) when Ξ(T) ≠ 0.
- So the packet through T is simple iff ι_N(T) ≥ n(T) for some N.
- Parity form: ι_N = ind_+(T²KᵀG₊⁻¹K − G₋).
- Our replay gives ι = n(T) at T = 39.913, 62.413 and 97.632.

**thm:strong-inertia-density, thm:fd-inertia-density** (final; statement level).
- ind_+(TH_N − G_N) ≥ (d_MT − η)n(T) with N = ⌈A_η log T⌉, d_MT = 0.83625….
- Localized coordinates for a (c_MT − η)-fraction of simple ordinates, ‖CU_N − U_NΛ‖ ≪ 1/(T² log T).
- The proportions are those of Alpöge–Furman, Lamzouri and Knausgård; the credit split is not yet made.

**prop:finite-simple-deflation** (checked by us). Deleting certified simple coordinates leaves 2Σ(m_γ − 1)γ^{−2k}
unchanged.

**prop:fd-arithmetic-precision** (perturbation step checked by us). Input accuracy 2^{−p}, with
p = O(e^{2N/d_MT}N log N + k log T), suffices to enclose D_{N,k} to T^{−2k}. Conditioning comes from
thm:cosine-lower-rate.

**prop:fd-even-operator** (checked by us). ‖C − C_N‖ ≤ (2/√3)D_{N,k}^{1/(2k)}. The constant is sharp for the block
estimate. Row 6 gives ‖C − C₆‖ < 0.0133.

**prop:fd-certificate-size** (checked by us).
- D_{N,k} ≥ 2Σ_{j>r_N}γ_j^{−2k}, with d_N = 2r_N. So a certificate at height T needs d_N ≥ 2n(T).
- For fixed N, H_{N,k} → γ₁ as k → ∞. So N and k must grow together.

## 3. Global constants (`global_growth_numeric.tex`, `trace_detection.tex`) — new at cp03
- **lem:fd-multiplicity-log** (checked by us). m_γ < ¾ log γ for γ ≥ 10.
  Mechanism: 2m/3 ≤ Re ξ'/ξ(2 + iγ) < ½ log γ, from the completion formula, Re ψ, and A₂ = −ζ'/ζ(2) < 3/5.
- **prop:orbital-unimodal-bound** (checked by us). 𝔯_m² ≥ 4π²(m+1)/(3m²) and (m−1)𝔯_m² ≥ π².
  Mechanism:
  1. Y = tr(D_mUXU*) has an even unimodal law, by Gelfand–Tsetlin (Olshanski) and Brunn–Minkowski.
  2. E cos Y ≥ ½ − 3EY²/(2π²).
  3. EY² = mV_X/(m+1) ≤ m²R²/(4(m+1)).
- **cor:fd-global-growth-numeric** (checked by us, except the cited 𝔯_m ≤ π√(m−1)).
  - L_T > 216.88 and L_J > 4766.003712.
  - (4π/3)√(L_J/log√(2L_J)) ≤ L_T ≤ (√3π/2)√(L_J log√(2L_J)).
- The trace transport improves to π/√𝒟_N (cor:trace-global-threshold, statement level).
- **prop:trace-height (cp01)** is the case k = 1: E(T) ≤ (T²/2)𝒟_N.

## 4. The window side, at the run (`prolate_upper_bound.tex`, `theta_kernel_hierarchy.tex`, `finite_weil_lower_certificate.tex`)
- **prop:prolate-upper.** q(v_{log λ}) ≪ λ^{9+ε}e^{−4πλ²}, hence a₁ ≪ λ^{9+ε}e^{−4πλ²}.
- **prop:odd-prolate-upper** (new; statement level). An odd competitor from prolate modes 2 and 6 tends to K' and gives
  a₂ ≪ λ^{13+ε}e^{−4πλ²}.
- **The target** (ALP_CONNES cp44, (RZ.5), opened by us). a₂(log λ) ≥ cλ^{9+α}e^{−4πλ²}, and so 0 < α ≤ 4.
  - Our prompts 62 and 68 wrote λ^α; the run corrected this as SPEC-POWER-NORMALIZATION.
  - Under this bound q(v_L)/a₂ → 0: S48 and S49 give convergence to Ξ and simplicity.
- **One-mode restriction** (eq:theta-hier-24, checked by us). b_L = inf{q(f) : ‖f‖ = 1, f ⊥ v_L} satisfies
  a₁ + a₂ − q(v_L) ≤ b_L ≤ a₂. THETA-LOWER asks for b_L ≥ cλ^{9+α}e^{−4πλ²}.
- **Theta image** (checked by us).
  - K = Θh, with h = (4π²u⁴ − 6πu²)e^{−πu²}, (Θψ)(x) = e^{x/2}Σψ(ne^x), and K̂ = Ξ.
  - ∂_xΘ = ΘE, with E = u∂_u + ½.
  - The profiles K^{(j)} have zero sampling image.
  - Their compact cutoffs reach only q ≪ (log λ)³λ^{7+4j}e^{−2πλ²}, which is half the prolate exponent.
- **All-window lower rate** (thm:cosine-lower-rate, final; statement level).
  - a₁(L), a₂(L), b_L ≥ exp{−Cμ^{1/d_MT}log μ(1+log log μ)}, with μ = e^{2L} = λ².
  - This improves Mori's μ^{6/5} (his Thm 4.3).
  - Mechanism: Montgomery–Taylor cosine test in the uniform pair argument, Hall matching, and Voss's sampling
    theorem.
  - Gap to the target λ^{9+α}e^{−4πμ}: the power μ^{1/d_MT} = λ^{2.3916…} in the exponent, against μ.
- **Finite lower certificate** (prop:finite-weil-lower and prop:finite-weil-block, statement level).
  - a₂(L) ≥ min{b, λ₂(M_{L,T,N})} − ε_{L,T,N}, from finite prime sums.
  - The 2 × 2 coupling bound: a₂ ≥ (a + c − √((a−c)² + 4z²))/2.
  - No asymptotic margin is proved.
- **Prime-pole cancellation** (`drafts/spectral_audit/PRIME_POLE_CANCELLATION.md`, identity (1)).
  q(f) = q_arch(f) + ∫e^{−|u|/2}g + 2Re∫₀^{2L}R(u)g'(u)du, with R(u) = μ((0, u]) − 2(e^{u/2} − 1). The RH bound on R
  loses one derivative, too much for the target.

## 5. Motion, pairs, survival, CUE (`motion_*`, `isolated_pair`, `survival`, `cue_*`, `signed_density`, `common_*`, `uniform_deformation`, `gaussian_moments`)
- **thm:isolated-pair** (κ = 0 term checked by us). a_c = δ²(1/8 + κ/32 + O(κ²)), with a unique double collision.
- **thm:positive-directions.** For ζ and each fixed χ, both motion directions occur with proportion > 10^{−14}.
- **The refutation at zero 1169.** The δ-free direction rule fails there, while the phase δ = arctan(1/(2γ)) is exact.
- **Survival.** Every fraction below the Montgomery–Taylor proportion 0.67250… of the zeros survives for
  −c/(log T)² ≤ t ≤ 0 (final; it was 2/3 at cp03).
- **thm:nonreal-height.** Nonreal zeros of H_{−a} occur below exp(exp(C/√a)).
- **New at cp03 (statement level):**
  - common deformation and anisotropic Hurwitz continuation;
  - conductor-uniform deformation;
  - Gaussian direction moments;
  - second jets at multiple zeros and at simple tangents (motion_bending).
- **CUE.** The first collision is Weibull-3/2, early collisions are Poisson with intensity (3/2)√v, the label agreement
  is 0.666546601837…, and far labels decorrelate.
- **Obstructions:**
  - **Character limits** (CHARACTER_LIMIT_OBSTRUCTION; real case checked by us). Primitive L(s, χ_j) with q_j → ∞ have
    no rescaled limit that is nonzero on the critical line: Re L'/L(s₀) = −θ_j'(t₀) → −∞.
  - **PAIR-Q2.** A periodic triple-cluster function with κ ≥ 4/9 refutes the scalar implication.
  - **PAIR-Q3.** Refuted by Lagarias–Rodgers, Thm 3.1.

## 6. Finite heights, by method
- Arithmetic trace: 97.632.
- Heat contour, whole edge: 45, with 8 centres and common real heat interval 1e−257 (sec:executed-contour).
- Spectral probe, residual/projection: 20 (prop:executed-local-probe).
- COMMON-HEIGHT: probe and contour agree on the packet through 20.
- DENSITY-DETECTION (cor:fd-density-detection): all three indices are infinite on the surviving positive-density
  packets.

## 6b. Approaches closed in the final, with their obstructions (FINAL_STATUS.md; statement level)
- **Prime-form multiplication.** The closed extension fails by a constructed graph residual
  (prop:fd-multiplication-domain).
- **Hermite–Biehler.** An explicit subharmonic counterexample to the proposed boundary inference.
- **Burnol jets.** The fixed two-jet compact Rayleigh quotient grows like cL (prop:burnol-coupled-cutoff).
- **Finite simple deletion.** The excess is unchanged.
- **Conductor variation.** The count is at least (r/12)log q − C, and it gives no smaller gate
  (prop:conductor-local-count).
- **Adaptive Nyman–Beurling.** The constant retains Σm(m−1)/|ρ|².
- **Möbius endpoint.** Exact Plancherel, Abel and gcd maps; the O(1/ε) endpoint norm bound is open.

## 7. Open rows and their gates (QUESTIONS.tsv at the final; all marked INCOMPLETE)
| row | gate |
|---|---|
| MAIN-SIMPLE | sup_{N,k}(2/D_{N,k})^{1/(2k)} = ∞, equivalently L_T or L_J = ∞, equivalently ind_+(TH_N − G_N) = n(T) for finite N at unbounded zero-free T; proved through 97.632; N = O(log T) reaches the fraction d_MT − η |
| MAIN-MOMENTS | for every height, P(0) = 1 with certified square sum < 2; the positive-kernel surgery shows that leading moments cannot decide it, so arithmetic input is needed; the Poisson and prime-ramp thresholds have no upper estimates |
| MAIN-CONTOURS | uniform growing contours: separation, complex-time nonvanishing, remainder budgets; fixed-contour partition proved |
| MAIN-TRACE | for every T, some certified D_{N,k} < 2/T^{2k}; dimension ≥ 2n(T) needed |
| MAIN-RATIO | liminf q(v_L)/a₂(L) = 0; needs a₂ ≳ λ^{9+α}e^{−4πλ²}, 0 < α ≤ 4; proved only a₂ ≥ exp{−Cλ^{2/d_MT}log λ(1+log log λ)} |
| THETA-LOWER | b_L ≥ cλ^{9+α}e^{−4πλ²} along unbounded windows |
| MOTION-Q3 | half-balance of labels; needs periodic odd-mode information |
| PAIR-Q2 | exterior inverse-square control on shrinking gaps |
| PAIR-Q4 | marked extreme-gap limits with isolation, for a zeta Weibull/Poisson law |
