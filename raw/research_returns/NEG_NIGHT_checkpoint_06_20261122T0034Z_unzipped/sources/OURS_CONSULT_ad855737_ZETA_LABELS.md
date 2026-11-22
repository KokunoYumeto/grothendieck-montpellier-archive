# Consult: zero velocities, the Boolean label, and the de Bruijn-Newman collisions under RH (21 Nov 2026)

By Claude Opus 5.5 at effort high (agent ad85573792c61a914, the ZETA_TWO/ZETA_NEXT intake agent), for the main session
(Claude Opus 5.5 at effort max), at the user's word. Scripts: `consults\ad855737_scripts\labels_W.py` (mpmath, 20 digits);
outputs beside it. Status labels: **standard** (with source), **proved here**, **checked** (by script), **heuristic**, **open**.
RH and Dirichlet GRH are cited to Alpöge (A). My context budget did not allow a literature search; where I say "known" I name
what I know without a fresh check, and say so.

Notation. ρ_n = ½ + iγ_n the n-th zero (simple; simplicity is assumed where the label is used); θ the Riemann-Siegel theta;
Z(t) = e^{iθ(t)}ζ(½+it); φ_n = arg ζ(3/2 + iγ_n) (principal value); v_n = ρ'_n(0) = ρ_nζ(ρ_n+1)/ζ'(ρ_n), the velocity of the
zero under t ↦ ζ(s, 1+t) (BOOLEAN_LABEL §1). Right-mover: Re v_n > 0.

## Q1. Novelty and correctness

### 1.1 The two identities are correct
- **Velocity formula** (BOOLEAN_LABEL §1; translation note §4 item 8): v = −∂_tL/∂_sL with ∂_tζ(s,1+t) = −sζ(s+1,1+t) gives
  v = ρζ(ρ+1)/ζ'(ρ). **Standard in kind**: it is implicit differentiation, the same as dρ/da = −∂_aζ/∂_sζ =
  ρζ(ρ+1,a)/ζ'(ρ,a) for the Hurwitz zeta ζ(s,a), ∂_aζ(s,a) = −sζ(s+1,a). Numerical studies of Hurwitz and Lerch zero
  trajectories in a (Spira, Math. Comp. 1976, on the zeros of ζ(s,a) leaving the line for a ≠ ½, 1; Garunkštis and
  coauthors on Lerch zeta trajectories) use exactly this parametrization; I did not re-read them, so I cannot say whether
  the closed form at a = 1 is printed there. It is a one-line consequence and should be presented as such, not as new.
- **The split** (translation note §2): Re ρ'(0) = Im Φ₋(ρ)/Z'(γ), Im ρ'(0) = −Φ₊(ρ)/Z'(γ). **Proved** there and correct:
  Λ_0'(ρ) = −iZ'(γ) on the line, Φ₊ real and Φ₋ imaginary on Re s = ½ by the functional equation and real coefficients.
  This is the general fact that for a family of real-symmetric entire functions the normal velocity of a zero on the
  fixed line of s ↦ 1 − s̄ is carried by the anti-invariant part of the deformation. Correct; elementary; I know no source
  that states it for this family, but it is the kind of statement that will be in any trajectory paper's first page.

### 1.2 What the corrected Gram rule really is (proved here)
Write S(t) = (1/π) arg ζ(½+it) (continuous variation from 2, standard), and at a zero use the midpoint value, so that
N(γ_n) = n − ½ and θ(γ_n)/π = n − 3/2 − S(γ_n) (Riemann-von Mangoldt, N(t) = θ(t)/π + 1 + S(t)). Put
  W_n := S(γ_n) − φ_n/π = −(1/π) Δ_{σ: 3/2 → ½} arg ζ(σ + iγ_n)   (midpoint convention at σ = ½).

**Proposition 1 (proved here, simple zeros).** v_n is a right-mover ⇔ (W_n mod 2) ∈ (0, 1). For |W_n| < 1: right ⇔ W_n > 0,
i.e. ⇔ arg ζ(½+iγ_n) > arg ζ(3/2+iγ_n) in the continuous variation.

*Proof.* BOOLEAN_LABEL §2: Re v = −|ζ(ρ+1)|[γ cos(θ+φ) + ½ sin(θ+φ)]/Z'(γ). Here θ + φ = π(n − 3/2) − πW_n, so
cos(θ+φ) = (−1)^n sin(πW_n) and sin(θ+φ) = (−1)^n cos(πW_n). For simple zeros the signs of Z'(γ_n) alternate, and
Z'(γ_1) > 0 (Z < 0 on [0, γ_1), as Z(0) = ζ(½) < 0), so sign Z'(γ_n) = −(−1)^n. Therefore, exactly,
  Re v_n = |ζ(ρ_n+1)|·[γ_n sin(πW_n) + ½ cos(πW_n)]/|Z'(γ_n)|,
so v_n is a right-mover ⇔ sin(πW_n + δ_n) > 0 with tan δ_n = 1/(2γ_n) (δ_n < 0.036). Up to the thin set of W_n within
δ_n/π of an integer, right ⇔ W_n mod 2 ∈ (0,1). ∎ (Checked: Claim A below.)

**Proposition 2 (proved here, given Proposition 1).** The rule "right ⇔ frac((θ(γ_n)+φ_n)/π) < ½" agrees with the label ⇔
W_n ∈ (−½, ½] mod 2. Its first failure is the first zero with |S(γ_n) − φ_n/π| > ½ (mod 2). Since S(t) is unbounded
(Selberg; under RH S(t) = O(log t/log log t) and Ω-results both ways) while |φ| ≤ log ζ(3/2)-type bounds keep φ/π bounded,
the rule fails infinitely often; it is a restatement of "the horizontal argument change from 3/2 to ½ is less than π/2",
not a new law.

**What this means.** The label is the parity class of the horizontal argument change W_n of ζ between σ = 3/2 and σ = ½ at
the zero, in units of π. The "corrected Gram rule" is exactly the statement |W_n| < ½ (mod 2). Equivalently, by
Riemann-von Mangoldt, the label is a function of S(γ_n) − (1/π)arg ζ(3/2+iγ_n): Gram's law with the Dirichlet-series part
of S removed, which is why it beats the plain Gram rule (444/500 there).

### 1.3 Computation (checked)
`labels_W.py a b out.tsv` computes, for each zero, the sign of Re v from the exact velocity, the rule, W_n, Claim A
(right ⇔ W mod 2 ∈ (0,1)) and Claim B (rule = label ⇔ W ∈ (−½,½] mod 2).

### 1.4 Results (checked)
- **Zeros 1-300:** 152 right-movers; rule 300/300; Claims A and B 300/300; consecutive labels agree 105/299.
- **Zeros 1-1449** (partial run of 1-5000; the full run continues in `run_1_5000.tsv`, summary `out_1_5000.txt`): W_n has mean
  −0.0001, standard deviation 0.185, max |W_n| = 0.538. **The corrected rule first fails at n = 871 (γ = 1267.5706,
  W = +0.5377)**, then at n = 965 (W = −0.5108), 1308 (W = −0.5133), 1431 (W = −0.5108): each time exactly because
  |W_n| > ½, as Proposition 2 says. The failure at n = 1169 (W = −0.00006) is of the other kind: W within 1/(2πγ) of an
  integer, where the exact criterion sin(πW + δ_n) > 0 (tan δ_n = 1/(2γ_n)) decides and the ½cos term flips the sign; there
  Claim A in its simplified form fails too, and the exact form holds.
- **Zeros 100001-100400** (γ ≈ 74921-75188): 207 right-movers of 400; the rule matches 384/400 (16 failures, the first at
  n = 100019, γ = 74934.028, W = −0.5613); **Claims A and B hold 400/400**; consecutive labels agree 186/399 (46.6%, up from
  35% at n ≤ 300, moving toward the predicted limit 66%). Σ Im ρ' over the block = 3.206·10⁶ against the main term
  (T_b² − T_a²)/(4π) ≈ 3.19·10⁶.

So: the corrected rule is the statement |W_n| ≤ ½, it first fails at the 871st zero, and its failure rate grows with the
variance of S (about 4% near the 10⁵-th zero). The labels themselves are given exactly, at every computed zero, by
Proposition 1.

## Q2. What RH gives for the statistics

### 2.1 The first moment of the velocities (proved here, under RH)
**Proposition 3.** Assume RH (A). Let T_m ∈ [m, m+1] be heights with |ζ(σ + iT_m)|^{−1} ≪ T_m^ε uniformly for
−2 ≤ σ ≤ 2 (they exist under RH: Titchmarsh, *Theory of the Riemann zeta-function*, 2nd ed., §14.16; standard). Then
  Σ_{0<γ≤T_m} ρ'(0) = i T_m²/(4π) + O(T_m^{1+ε}).
So Σ Im ρ'(0) ~ T²/(4π) and Σ Re ρ'(0) = O(T^{1+ε}), while Σ|ρ'(0)| is of order T²: the real parts cancel to relative order
T^{−1+ε}.

*Proof.* By the residue identity of the translation note §4 item 4 with h = 1 (Res_ρ ∂_t log L_t = −ρ'(0)),
Σ_{0<γ≤T} ρ'(0) = (1/2πi)∮_R sζ(s+1)/ζ(s) ds over the rectangle R with vertices c + i, c + iT, −1−ε + iT, −1−ε + i,
c = 1 + 1/log T. There are no other poles in R: sζ(s+1) is regular at s = 0, and trivial zeros are real.
- Right edge: sζ(s+1)/ζ(s) = sΣ_n α₁(n)n^{−s}, α₁(1) = 1. The n = 1 term gives (1/2π)∫_1^T (c+it)dt = iT²/(4π) + O(T).
  For n ≥ 2, integration by parts gives in total −(T/2π)G(c+iT) + O(T), with G(s) = Σ_{n≥2}α₁(n)n^{−s}/log n =
  ∫_s^∞(ζ(w+1)/ζ(w) − 1)dw = O(log log T) under RH.
- Left edge: sζ(s+1)/ζ(s) = s·[χ(s+1)/χ(s)]·ζ(−s)/ζ(1−s) and χ(s+1)/χ(s) = −2π cot(πs/2)/s exactly, so the integrand is
  −2π cot(πs/2)·ζ(−s)/ζ(1−s) = 2πi(1 + O(e^{−πt}))Σ_n(φ(n)/n)n^{s} on Re s = −1−ε (as ζ(w)/ζ(w+1) = Σφ(n)n^{−1−w}).
  The n = 1 term gives −i(T−1); the rest is O(1).
- Horizontal edges at T_m: |s| ≍ T, |ζ(s+1)| ≪ T^{1/2+ε}, |1/ζ(s)| ≪ T^{σ−1/2+ε} for σ ≤ ½ and T^ε for σ ≥ ½; each edge
  is O(T^{1+ε}). ∎

**Consistency.** The zeros drift upward at average speed (T/2π)/((1/2π)log T) = T/log T at height T; equivalently the
count of zeros of ζ(s, a) in the strip has dN/da = −T/(2π) at a = 1. **Checked:** first 300 zeros: Σ Im ρ' = 22948
against T²/(4π) = 23364 (T = γ_300 = 541.85); Σ Re ρ' = 108. More in §1.4.

### 2.2 The proportion of right-movers
- The first moment cannot decide it (Proposition 3 cancels the real parts). By Proposition 1 the proportion is the
  asymptotic frequency of {W_n mod 2 ∈ (0,1)}.
- **Proposition 4 (under RH, given one input).** If the values S(γ_n), n ≤ N(T), satisfy Selberg's central limit theorem
  with variance σ_T² = (1/2π²)log log T, then W_n mod 2 equidistributes on R/2Z and the proportion of right-movers tends to
  ½, with error O(e^{−π²σ_T²/2}) = O((log T)^{−1/4}) from the first Fourier mode.
  *Proof.* φ_n/π is bounded, so W_n has variance σ_T² + O(σ_T) → ∞; a Gaussian of variance → ∞ equidistributes mod 2 (its
  characteristic function at πk, k ≠ 0, is e^{−π²k²σ²/2}). ∎
  The input (the CLT for S at the ordinates) is obtained by Selberg's moment method with the Landau-Gonek formula
  Σ_{0<γ≤T}x^{iγ} = −(T/2π)Λ(x)/√x + O(x log(2xT)log log 3x + log T/log x) (standard). The Landau-Gonek main term is real
  for x = p^k, so it shifts the mean of log|ζ| at zeros, not of S, which is the imaginary part. I believe this CLT is in the
  literature (Fujii's work on S at the ordinates) but have not checked a locator: **standard in method, attribution open.**
- **Simplicity.** The label needs a simple zero. Under RH, Montgomery's pair correlation gives ≥ 2/3 simple (standard);
  the proportion statement is over simple zeros and does not need all zeros simple.
- **Gonek-Hejhal moments** are not needed for the proportion. They are what a statement about the sizes of Re v needs:
  Σ|v|² ≈ Σγ²|ζ(ρ+1)|²/|ζ'(ρ)|² is of J_{−1} type (conjecture J_{−1}(T) = Σ_{γ≤T}|ζ'(ρ)|^{−2} ~ (6/π³)T; open).

### 2.3 Random-matrix (CUE) prediction (heuristic, with the computation)
- **Proportion:** ½. For a Haar unitary of size N the counting-function fluctuation at eigenangles is Gaussian of variance
  (1/2π²)log N, symmetric; its parity class equidistributes. The arithmetic term φ is bounded and does not change the limit.
- **Consecutive labels:** by Riemann-von Mangoldt, W_{n+1} − W_n = 1 − δ_n − (φ_{n+1} − φ_n)/π, δ_n the normalized spacing
  (θ(γ_{n+1}) − θ(γ_n))/π; the φ-difference is O(1/log γ). In the equidistribution limit, for a shift u ∈ [−1,1],
  P(the classes of W and W + u agree) = 1 − |u|. Hence
    P(label_{n+1} = label_n) → 1 − E|1 − δ|,  correlation of the ±1 labels → 1 − 2E|1 − δ|.
  With the GUE Wigner surmise p(s) = (32/π²)s²e^{−4s²/π}: E|1−δ| = 0.3388, so P(same) → 0.661 and the correlation → +0.32
  (mpmath quadrature; the exact Gaudin law moves the third digit).
- **At computable heights the regime is different:** σ_T² ≈ 0.1-0.2, W_n stays near 0, the label is sign(W_n), and the
  increments 1 − δ_n are as large as W itself, so labels flip often. Observed for n ≤ 300: 105/299 consecutive agreements
  (anticorrelated). The crossover to positive correlation needs σ_T of order 1, i.e. log log T of order 20. A clean
  prediction: **the consecutive-label correlation is negative at every computable height and tends to +0.32 (GUE).**

## Q3. Λ = 0 and the collisions at negative times

**Standard inputs.** H_t(z) = ∫_0^∞ e^{tu²}Φ(u)cos(zu)du has only real zeros exactly for t ≥ Λ (de Bruijn 1950, Newman
1976); Λ ≥ 0 (Rodgers-Tao, Forum Math. Pi 2020); RH ⇔ Λ ≤ 0. **With A: Λ = 0.**

1. **Proved:** for every t < 0, H_t has a non-real zero (definition of Λ, with Λ = 0).
2. **Proved (the user's local law, 22_rh_counterexample_routes.tex, "Zeros as Burgers poles and their collision
   coordinates"):** a double zero z_0 of H_{t_0} unfolds as z_0 ± √(2(t − t_0)) + O(|t − t_0|), real for t > t_0, a conjugate
   pair for t < t_0. With Λ = 0, every collision lies at a time t_c < 0, and the real points of the discriminant curve of
   the family {H_t} all lie in t < 0. At t = 0 the coordinate of ρ = ½ + iγ is z = 2γ, so consecutive ζ-zeros with gap Δγ
   have Δz = 2Δγ.
3. **Heuristic (leading order):** a pair much closer than its neighbours (a Lehmer pair) collided at t_c ≈ −(Δz)²/8 =
   −(Δγ)²/2, corrected by the repulsion of the other zeros (z_j' = 2Σ'_{k≠j}1/(z_j − z_k), Polymath 15, Prop. 3.1). This is
   the mechanism of the lower bounds for Λ from Lehmer pairs (Csordas-Smith-Varga 1994; Saouter-Gourdon-Demichel 2011): each
   such bound is a certified collision time.
4. **Heights against times (heuristic):** the backward heat flow at time t < 0 acts on the scale √|t|, and the mean spacing
   at height x is ≈ 2π/log x in γ. Zeros at height x stay real at time t while √|t| is small against that spacing. So the
   collision front recedes as t ↑ 0 like |t|(log x(t))² ≍ 1, x(t) ≈ exp(c/√|t|). With GUE gap statistics the number of
   collisions in [−τ, 0) at heights ≤ X would be ≍ N(X)·P(normalized gap ≤ c√τ·log X), with P(gap ≤ ε) ~ (π²/9)ε³ for small
   ε. **Open** as a theorem; Rodgers-Tao's proof of Λ ≥ 0 is the rigorous form of "at negative times the zeros cannot all
   stay real".
5. **Finite certificates** (the user's "Finite certificates for Newman collisions and nonreal zeros"): with Λ = 0 known, a
   certified non-real zero at some t < 0 no longer bears on RH; it certifies a point of the collision front, and a certified
   double zero gives an exact real point (x_c, t_c) of the discriminant curve.

## The findings in algebraic-geometry and representation-theory terms (the user's follow-up)

- **Velocity and split (AG).** For the family of divisors D_t = div Λ_t on C × (t-line), the velocity of a zero is the image
  of the Kodaira-Spencer class in H⁰(D, N_D) = ⊕_ρ T_ρC: v(ρ) = −(∂_tΛ/∂_sΛ)(ρ). With the antiholomorphic involution
  σ(s) = 1 − s̄, whose fixed curve is the critical line, **the normal velocity of a zero on Fix(σ) is the σ-anti-invariant
  part of the Kodaira-Spencer class**, and the tangential velocity its invariant part: the Z/2-isotypic decomposition of the
  deformation class.
- **The label (representation theory).** The label is the sign character of Z/2 = (R/2Z)/(R/Z), evaluated on W_n ∈ R/2Z.
  Proposition 4 is **equidistribution of W_n in the compact group R/2Z** (Weyl's criterion: all nontrivial characters average
  to 0 along the zeros); the CUE prediction is the same statement for Haar measure on U(N).
- **Proposition 3 (AG).** The trace of the Kodaira-Spencer derivative over the zero divisor up to height T is the period
  ∮ sζ(s+1)/ζ(s) ds; its main term iT²/(4π) is the a-derivative of the degree of the divisor of ζ(s, a) up to height T.
- **Λ = 0 (the main session's form, checked).** Ξ(z) = Σ(−1)^k b_k z^{2k}, b_k > 0. Ξ has only real zeros ⇔ F(w) = Σb_k w^k
  has only negative zeros ⇔ (F has order ½) F(w) = b_0∏(1 + w/γ_j²) ⇔ (b_k) is a Pólya frequency sequence (Aissen-Schoenberg-
  Whitney; Edrei 1953) ⇔ the normalized specialization is an extremal character of S_∞ with Thoma parameters α = 0,
  β_j = γ_j^{−2}/Z(2), Z(2) = Σ_{γ>0}γ^{−2} (Thoma 1964), with value (−1)^{k−1}Z(2k)/Z(2)^k on a k-cycle. **Checked: correct**,
  with Z summed over positive ordinates, each once, so that Σβ_j = 1. Λ = 0 says: the normalized Taylor sequence of H_t lies in
  the Thoma simplex exactly for t ≥ 0. **The collisions at negative times are the points where a conjugate pair of "Thoma
  parameters" becomes real**: the real points of the discriminant curve of {H_t}, all in t < 0, accumulating only as
  t → 0⁻, x → ∞ (the accumulation statement is item 4, heuristic).
- **Collisions (representation theory).** The local model of a collision of multiplicity m is the heat flow
  z^m ↦ (2t)^{m/2}He_m(z/√(2t)). The Hermite polynomials are the weight vectors of the oscillator representation, and the
  heat operator e^{−t∂²} is the exponential of an element of the sl₂ acting there: a collision is where the family meets the
  discriminant of degree-m polynomials, in the oscillator model.
