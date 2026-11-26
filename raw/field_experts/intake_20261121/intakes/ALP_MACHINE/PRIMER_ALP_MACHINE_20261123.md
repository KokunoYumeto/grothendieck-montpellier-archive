# Primer: ALP_MACHINE, the mathematics as it stands on 23 Nov 2026 (checkpoint 67, 24 Nov 01:08 UTC)

For the main session to read after a compaction. By Claude Opus 5.5 at effort high (agent abcaba9b6ae84b747). It
restates; the check levels are those of my check events, and nothing here is new development.

## The setting

Prompt 49 asks how Alpöge's proof of RH for Dirichlet L-functions (20 Nov 2026, with Lean) works at its step 8, a chain
of theta lifts between definite unitary groups, and whether the chain can be shortened. Its main questions:
- Q1, the net lift count (DP_MULT Q3e);
- Q2, the definite MainX pairing (THETA3 G1);
- Q3, RH for a Kummer Hecke character over Q(ω);
- Q4, an oscillator comparison;
- Q5, Grothendieck frameworks.

**Two separate runs of prompt 49 exist.**
- **Run 20:03:** ids AM-L, AM-SS, AM-ST, AM-S. Its last filed checkpoint is 08.
- **Run 19:35:** ids ALP-LIFT, AM-K, AM-R, AM-DO. Its last filed checkpoint is 67 (updated in place from the checkpoint-59 and checkpoint-55 versions, whose
  copy is in `integration_backups\20261123\ALP_MACHINE\`).

Files are in `research_returns\ALP_MACHINE_checkpoint_67_20261124T0108Z_unzipped\ALP_MACHINE\` (run 19:35) and in the
Downloads ZIP `ALP_MACHINE_checkpoint_08(1).zip` (run 20:03).

## 1. The size floors of step 8 (LIFT54, LIFT55; run 19:35)

**Statement.** Let a datum satisfy Alpöge's formal size predicate `SizesAt` (pinned commit 7cbf…). Write x > 1,
0 < ε < 1/52, L = x^ε, the chain length m (even, 2 ≤ m ≤ f ≤ k, m + 3 ≤ k), f = [F:Q] with [E:Q] = 2f, and k the
initial rank. Then:
- x^{1/2−29ε/400} ≤ m ≤ x^{1/2−21ε/400};
- (log f)² ≤ m/2 − 1, so m = 2 is impossible;
- L > 2^300, m > 2^7778, f > 2^33598, k > 2^73197.

**Inputs.** Five clauses of the Lean source:
- SizeM: x^{∓θ}√(xδ₁) bounds m, with θ = ε/100 and δ₁ = x^{−ε/8};
- the conjunct log f ≤ √r_S, with r_S = m/2 − 1;
- SizeG at i = j = 0: (k e^L)^8 ≤ g ≤ exp(x^θ L);
- SizeN: n ≥ x^{2+8ε−θ};
- SizeK: k ≥ x^{9/2+10ε−θ}.
The files are ElevenLe.lean 24–49 and 123–138, DataParams₂.lean and Params.lean.

**Mechanism.**
1. SizeM is the first claim after writing √(xδ₁) = x^{1/2−ε/16}.
2. Squaring the log clause gives the second.
3. SizeG gives 8(L + log k) ≤ L^{101/100}, so L^{1/100} > 8.
4. Then x > L^52 and the lower clauses give the floors.

**Checks.** My targeted checks against the Lean definitions (22 Nov). The run's two whole-proof reviews. A Lean 4.33.1
standalone certificate in NIGHT_AFTER_ALPOGE (its bridge to SizesAt is not yet compiled). **Scope:** a theorem about
the formal interface, not about theta lifting as such.

## 2. The phase lemmas (AM-S1–S4; run 20:03, oscillator_sign.tex 392–655)

- **S1.** In W = (Z/3)² ⋊ ⟨s⟩ (swap), Z(W) = diagonal C₃ and [W,W] = antidiagonal C₃. Any map making s central kills
  the antidiagonal.
- **S2.** If F commutes with W on a representation M, then Tr(sFⁿ | M) = Tr(sFⁿ | M^{⟨a⟩}). Reflected traces see
  nothing of the rotation-nontrivial part, so they bound no eigenvalue there. The example is the standard
  representation of S₃ ⊗ Q_ℓ(−N).
- **S3.** If s has order d and commutes with F, then bounds on Tr((sF)^{dn}) bound every eigenvalue of F. With a
  reflected relation (sFs = F^{−1}) they do not.
- **S4.** A formal half-weight variable v = √q gives no reduction to Hecke-character RH. The P¹ count already uses it,
  and so does the rank-one canonical element b = H + v^{−1}, with H² = (v − v^{−1})H + 1, b̄ = b and
  b² = (v + v^{−1})b.

**Checks:** targeted (22 Nov). S4's example was recomputed on 23 Nov.

## 3. Structural constraints on a literal instance (run 19:35)

- **LIFT079.** The literal CMObj, and independently LamObjGood, force the target to be isogenous to a power of one CM
  elliptic curve. Statement level.
- **LIFT083.** A J-isotypic fibre (J = Jac(y² = x⁷ − 1)) fails the pinned determinant condition at every stage.
  - Over Q(√−7) the Lie multiplicities are (2a+b, a+2b), so DetCond needs p ≤ 2q and q ≤ 2p.
  - The pinned profiles p_j = k + j − 1, q_j = m − j have k ≫ m.
  - Statement level.
- **LIFT109.** For a CM host with prime fundamental discriminant −d (d ≡ 7 mod 16):
  - N_{E/K}: Cl(E) → Cl(K) is onto (statement level);
  - h_K is odd, and the class above 2 has odd order h₂ with 2^{h₂} ≥ (d+1)/4, so h₂ ≥ 7 when d > 365 (rederived).
- **LIFT110**, `agents\abelian_coefficient_normalized_ideal_obstruction.md`.
  - **Theorem A:** for K imaginary quadratic with μ(K) = {±1}, F/K finite abelian, and J O_F = (ξ) with |σξ|² = N J
    for all σ, we have [J]² = 1.
  - **Mechanism:** u = ξ^h/γ is a unit with all conjugates on the unit circle, so a root of unity (Kronecker). Then
    ξ^{hm} = γ^m, the splitting field of X^{hm} − γ^m is abelian over K, and Schinzel's theorem gives
    γ^{m gcd(hm,2)} = b^{hm}. Cancel in the ideal group.
  - **Theorem B:** with LIFT107–109, a literal instance needs a coefficient field outside K^ab.
  - **Checks:** targeted, 23 Nov.
- **LIFT112**, `agents\exact_normalized_coefficient_degree.md` (Theorem B checked 23 Nov).
  - **Statement:** let G be an odd subgroup of Cl(K) of order g and exponent e, with an invariant-factor basis
    [J_i] of orders h_i and J_i^{h_i} = (γ_i). Over any abelian B/K, the field F_* = B(α_i), α_i^{h_i} = γ_i, has
    [F_*:B] = g and F_* ∩ K^ab = B. Every field carrying the normalized table has g | [F : F ∩ K^ab] (Theorem A). If F/K
    is Galois, the commutator of Gal(F/K) surjects onto Hom(G, μ_e) (Theorem C).
  - **Mechanism:** over A = B(μ_e), the classes of b_i = γ_i^{e/h_i} in A^×/A^{×e} are independent. A relation would
    give a normalized generator of some J in the abelian A/K, so [J]² = 1 by LIFT110, hence [J] = 1 since G is odd.
    Kummer theory then gives degree g.
- **LIFT113:** the optimal field F_* is CM, and F_*(μ_e) is CM, Galois over Q and metabelian, with commutator Hom(G, μ_e).
  So a literal instance needs, and can have, a metabelian non-abelian coefficient field of relative degree exactly
  h_K. Statement level.
- **LIFT111, 114–116, R104, R105:**
  - LIFT111: ramification and root-discriminant bounds for this field, rd(F_+) ≤ g³ rd(F_0).
  - LIFT114–116, R104: reconstruction of the full formal datum D7 after changing the integral coefficient ring
    inside a fixed ambient field, with exact lattice and slope costs (≤ 2 log c).
  - R105: the scalar local-error repair preserves the fixed-input error law only when c = 1.
  - All statement level.
- **Transport of the whole formal family to the new coefficient ring (checkpoint 67; statement level, except one
  inequality).** In a fixed ambient field LL with A = O_LL:
  - LIFT117 resupplies the period and local lattice bounds; the row height changes by 0 ≤ Δ ≤ 2 log c₀.
  - LIFT118: SizesAt bounds that cost by 2 log c₀ ≤ 32 x^{11+726ε/25} < 32 x^{12}, which is below b = exp(x^ε) once
    x ≥ max(2, 32 q!) with q = ⌈13/ε⌉. So the nine LinkDIV clauses transfer (the exponent and the exp-versus-power
    step rechecked by me).
  - R108: the theta-index projection descends rationally.
  - R110: a supplied complete FamP is rebuilt over O_LL with every constant unchanged and height change zero, given
    stability and rational projection on all tuples.
  - LIFT120: the actual RowPk construction supplies those premises.
  - Combined with LIFT112–113, the metabelian coefficient field can carry a supplied literal family. Its existence is
    not constructed.
- **LIFT100–108** construct the remaining interface pieces conditionally: ThNe0, IsNab, ShortValTot, ShortThetaUnit,
  the kPsi table on Cl(K), the beta law. Statement level.

## 4. The analytic side (run 19:35)

- **LIFT068–076 and LIFT077.** The prescribed bottom period is determined by local factors and one global statement.
  - The local factors at the T place: the canonical factor q/[(q−1)(q^k−1)], the G-place factor 1/d_ς, the away
    factors.
  - LIFT074: if the two specified embedded occurrences are globally Bessel-distinguished, the period is c_Per·b̄ ≠ 0.
  - LIFT077: |b|² is an explicit positive constant times a ratio of central L-values at 1/2, times local factors.
  - So nonvanishing reduces to a central value, of Ichino–Ikeda/GGP shape.
  - LIFT075: the direct compact-source theta lift is killed by Alpöge's projector e0 for every even m (targeted check,
    given Mínguez Th. 1(2) and Gow–Vinroot).
  - The rest is statement level.
- **The finite signed gate (DO/R/K rows).**
  - The energy of the all-top J⁵⁶ kernel is 1 + Re Σ w(h) + ε, with |ε| < 2^{−230}.
  - Supports through 30 are removed or absorbed into six nonnegative completions (P27, P28, P29, Pmix, Pmix30, P30;
    DO129–DO143); the allowances plus all absolute errors stay below 2^{−230}.
  - **Open:** Re Σ_{support ≥ 31} w(h) > −1 + 2^{−230}; the uniform H8192 floor is 11. One run row was refuted by the
    run itself as a duplicate (R109).
  - Statement level, except R062's exponent and R067's assembly (my checks).

## 5. Open rows and their current gates

| Row | Gate |
|---|---|
| Q1 (lift count) | a changed size interface, or a proof that the cost balance forces m → ∞. Follow-up 49b was not taken up by this run; NIGHT_AFTER_ALPOGE Part B works it |
| Q2 (MainX pairing) | the global Bessel distinction (LIFT074) or central-value nonvanishing (LIFT077); the arithmetic image and its content; the signed gate at support ≥ 28 |
| Q3 (Kummer Hecke RH over Q(ω)) | an arithmetic comparison to the ray-theta Mellin period of K021, prime-norm and conductor costs, and an every-ε window |
| Q4 | global arithmetic compatibility of the oscillator comparison |
| Literal instance of step 8 | coefficient field with [F : F ∩ K^ab] divisible by h_K, attained by a CM metabelian field (LIFT110, LIFT112, LIFT113); host not J-isotypic (LIFT083); sizes as in §1 |
