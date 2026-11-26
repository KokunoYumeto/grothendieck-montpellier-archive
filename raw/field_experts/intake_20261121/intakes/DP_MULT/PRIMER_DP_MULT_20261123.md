# Primer: DP_MULT (prompt 34, "the multiplicity of Alpöge's step 2 as divided powers, and Grothendieck's crystals")

ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026. This is a recall of my four intakes of the run (cp01, cp02,
part2, part3, part4). The run is GPT-6 Astra (ChatGPT Pro mode). Its final return is checkpoint 06,
`research_returns/DP_MULT_checkpoint_06_20261121T0420Z_unzipped/DP_MULT.tex`. No input from Alpöge's theorem and none
from Masullo is used. The run's subject is the p-adic size of derivatives in step 2 of Alpöge's construction, and
whether formal groups of greater height could shorten step 8 of the chain.

**Notation.** R = W(k), D is the invariant derivation, q = p^h, and the slope is c_h = 1/(p−1) − 1/(p^h−1).

## Main results, in the order of the argument

**DP1, the bound for every height (checked step by step, with 115 exact computations).**
- *Statement.* Let F be a one-dimensional formal group over W(k) of height ≥ h, and D its invariant derivation with
  Dt(0) = 1. Then D^n f ∈ p^{max(0, ⌈c_h n − (h−1)⌉)} R[[t]].
- *Optimality.* The error h − 1 is optimal, with witness f = t^{p^h−1}.
- *Mechanism.*
  - The logarithm recursion (p − p^m)ℓ_m = a_m + Σ ℓ_i [t^m] g^i makes ℓ_m integral for m < q, with v(ℓ_q) ≥ −1.
  - Change to the coordinate z = t + Σ_{m<q} ℓ_m t^m.
  - The identity Σ Δ_j u^j = exp(L(u)D) gives Δ_j = D^j/j! for j < q.
  - So D^q = p^{B_h}u_0 D + p^{B_h+1}T with T integral.
  - Legendre's digit bound then gives the estimate for n < q.

**DP2, the contraction (checked).** F_π(X, Y) = π^{−1}F(πX, πY) with π^{q−1} = p has integral L_π and E_π, and
v(e_n) ≥ −(n−1)/(q−1), with equality at n = q^r.

**DP3, the exact floor sum (checked).**
- *Statement.* D^n R[[t]] ⊂ p^{E_h(n)} R[[t]] with E_h(n) = Σ_{h∤j} ⌊n/p^j⌋, sharp at n = p^j. Also
  v(D^{q^r} t(0)) = c_h(q^r − 1), so c_h is optimal.
- *Mechanism.* D^n f(0) = n!·[z^n] f(E(z)), composed over the base-p digits.

**DP4–DP6.**
- DP4: height 1 gives no gain.
- DP5: gr Dist(F) is Γ_R(Lie F), yet D^q/q! is not integral.
- DP6: the supersingular elliptic case gives max{Σ_r ⌊n/p^{2r+1}⌋, ⌈pn/(p²−1) − 1⌉}. This is the exponent of
  Alpöge's step 2, the height-two case. It also refines ZETA_TWO ALP02.

**DP34 (checked).** On every Honda dual, D_i^n f ∈ p^{max(0, ⌈c_i n − 1⌉)} with c_i = p^i/(p^h−1) and Σ c_i = c_h
(DP32). The constant 1 is optimal, with the common witness f_* = ∏ X_j^{p−1}·X_d^{p²−1}.

**DP42, the mixed-line ceiling (checked; DP41's multiplier lemma carried).**
- *Statement.* For odd p and h ≥ 3, every primitive mixed logarithmic line t ↦ (ut, vt) in the actual pair has exact
  slope 1/((p−1)(p^k+1)), where k is the restricted-p nilpotency length. The maximum over all such lines is
  1/(p²−1), independent of h.
- *Mechanism.*
  - The arrow identities pω_{i−1} − ω_i = 1 hold.
  - The initial term is unique: SY_d^p/p.
  - The reduced inverse carries the terms v̄_j^{p^{i−j}}.
- *Consequence.* Higher height does not beat ρ_2 = 1/(p²−1) along the lines the kernel actually follows.

**DP51 (statement level).** For every integral homogeneous differential polynomial P of degree n on ℓ copies of the
primitive pair, v_p(P(∂)Θ(0)) ≥ c_* n − s·max Σ s_p(α_i), with c_* = 1/((p−1)(p^{h−1}+1)). This is optimal.

**Further statements (statement level).**
- DP50: p-divisible tensor exponents are cancelled by the source normalization.
- DP64 (leading term checked by Chebotarev and Mertens): averaged over primes, every CM type has the same leading
  budget (N/2) log X.
- DP43: the affine loss equals the codimension for every cyclic type.

**Structural rows.**
- DP10 (proof read): the boxed "p-th power zero" on cote 54 concerns the universal vector extension; Oda's Cartier
  comparison applies.
- DP11 (checked): a torsion-free ring is binomial ⇔ the identity is a Frobenius lift at every p ⇔ it is a λ-ring with
  ψ^n = id.
- DP13: Horel's binomial reconstruction.
- DP21: Alpöge's Lean `oneLog` has height 2.
- DP22, DP45 and DP49 (CM blocks of y² = x^7 − 1 of height 3 and 6): numbers checked, otherwise statement level.

**What it is good for.**
- It explains the exponent pn/(p²−1) of Alpöge's step 2 as the height-two divided-power slope.
- It shows that no local mechanism of greater height shortens step 8.

## Open rows

- **Q3e (global).** An actual mixed-type family on a CM Jacobian, with its sections, row degrees, the six lift
  identities and the full cost comparison. The local ingredients DP54–DP65 are built; the global net saving is not
  proved.
- **Q5f.** The B7 comparison; its statement was never supplied.

## Where it went

- Hexagon candidate H09, "divided powers in Alpöge's step 2". The gates were the literature search, an intake read
  of DP41 and DP51, and one independent computation of a DP42 slope.
- The ALP_MACHINE core (prompt 49) took DP44 and DP52–DP65.
