# Primer: DEG_L (prompt 41, "Hodge degrees are L-values: Rallis and semiregularity")

ad855737 (Claude Opus 5.5 at effort high), 23 Nov 2026. This is a recall of my intakes: part 1 (cp03), part 2 (cp06)
and cp06 (22 Nov).

**The run.**
- Model: GPT-6 Astra (ChatGPT Pro mode). It ended at checkpoint 06 (21 Nov 05:17 UTC), with no final return.
- Return: `research_returns/DEG_L_checkpoint_06_20261121T0517Z_unzipped/DEG_L/DEG_L.tex`.
- "032" is OpenAI's family-032 proof of the rational Hodge conjecture for CM abelian varieties.
- Inputs: no Alpöge and no Masullo input is needed. The L-values that occur lie in absolute convergence or at the edge.

**State at the end:** 72 proved, 41 refuted, 4 open.

## Main results

### T6.1-T6.3 (checked step by step): the degree of a surface image

**T6.1.** Let f: S → A be a map with surface image and H ample. Then

- deg_H f_*[S] = ∫(f^*Ω_H)² = ½ Σ_{a<b} ∫ ξ_ab∧ξ̄_ab, with ξ_ab = f^*ω_a∧f^*ω_b.

So the degree is a positive sum of wedge norms.

**T6.2.** The output class of 032 Prop. 3.1 is a switch class in H¹⊗H¹⊗H¹⊗H¹. Against the product polarization it has
degree 0: each factor has odd degree 1 + 2a_i.

- Hence the prompt's premise ("the degree of the 032 cycle is an L-value") is refuted as worded.

**T6.3.** Replacing each clearing map f_i by [M]∘f_i multiplies the degree by M⁴ at the same level. So the level alone
does not fix the degree.

### T6.11-T6.13 (proof read; Haan and GQT carried): the energy as a finite sum of L-values

**T6.11.** The energy is

- E_f = (2/a_K) Σ Q_jσ, with Q_jσ = L_E(3/2, BC(τ_σ)⊗γ_σ³)/L_F(3, ε_{E/F}) · Z^#_σ.

This is Haan's Rallis inner product formula for U(1) → U(3) (Haan, Thm 3.4). Then

- deg ≤ 4(ΣQ)²/(a_K²∫ω²), by Hodge index.

The L-value sits at s = 3/2, inside absolute convergence.

**T6.12-T6.13.** The wedge Θ_1∧Θ_2 is a theta transform with a finite cuspidal expansion (GQT, Thm 11.4(ii)). Then

- deg = (4/a_K) Σ_λ L(1, π_λ×χ_V) Z^*_λ(q, q).

These are standard L-functions of U(2) cusp forms at the edge s = 1.

### B1 (checked)

For σ > 1: ζ_K(2σ)/ζ_K(σ) ≤ |L_K(σ, χ)| ≤ ζ_K(σ). This bounds the factors in T6.11 with no GRH.

**Use.** It locates the difficulty: the L-values are not where it lies.

### B19 (checked step by step): fixed-source transport and the core index J

**Setting.** A fixed simple CM isogeny class (E, Φ), A = C^g/Φ(Λ), and J = [Λ : Λ^−], the index of the largest
O_E-stable sublattice.

**Statements.**

1. covol Hom_E(A_0, A) = 2^{−g} √|D_E| (V/V_0) J.
2. The least nonzero squared Hom-norm lies in [g(VJ/V_0)^{1/g}, K_E(VJ/V_0)^{1/g}], where
   K_E = (2/π)(g!√|D_E|)^{1/g}.
3. A minimal isogeny h satisfies J ≤ deg h ≤ K_E^g J/g^g.
4. For Weil type (g = 2n): a witness of degree O(√J), and bounded-division complexity O(J).
5. J ≤ N(f_A).

**Inputs.** Milne, ANT Thm 4.19 and Prop. 4.26.

**Mechanism.**

- Ideal-lattice covolumes: c(IJ) = c(I)c(J)/c(O).
- Minkowski's theorem for the least norm.

### B20, B21, T6.25, B22a (statement level): the lower bounds

- **B20-B21.** Every bounded-degree source witness has a reduced image of degree ≥ c√J. This uses Ullmo-Yafaev
  Prop. 4.1 and FGA 221 boundedness.
- **T6.25.** The √J lower bound extends to every proper transport from a maximal-order source.
- **B22a.** The source degree must grow at least like J^{1/4}.

**Use.** No fixed-source transport gives uniform bounded division along a CM sequence with J → ∞. This feeds Theorem W
and Theorem E of `reports_20261120/hodge_bridge/HODGE_DIVISION_ATTACK_20261121.md`.

### S-05, S-06 (checked; Venkataramana, Calabi-Vesentini and Buchweitz-Flenner carried): semiregularity fails at depth

For a compact ball quotient Y → A with surface image:

- dim ker τ_f ≥ g·q(Y) − C(2g, g−2).
- q(Y_j) → ∞ along a cofinal system of congruence covers.

So the Buchweitz-Flenner semiregularity map is not injective at deep level. This refutes T7 in its universal form.

### S-01 (checked) and S-02 (statement level)

- **S-01.** Étale covers keep the period but lose the immersion.
- **S-02.** For an embedded surface, semiregularity is equivalent to surjectivity of H¹(O_A)⊗∧³W → H¹(Y, N^∨⊗K_Y).

### S-14 with DER4 and DER7 (statement level)

- **S-14.** One weakly G-semiregular perfect complex E_0 with e^{B_0}ch(E_0) = λt + P(θ) at one fibre gives bounded
  division on the whole family. This uses Perry's deformation theorem and DIV1.
- **DER4.** The Adams operation ψ^M untwists the Kummer gerbe.
- **DER7.** The multiplier does not depend on the order of the gerbe.

### S-30-S-41 (statement level, and read only in ledger summaries)

These are exclusions of rank-one and balanced-RM replacement objects, under restrictive hypotheses:

- balanced-RM;
- gluable;
- simple or nonequivariant;
- principal maximal-local-order settings.

**Caution.** Do not read S-30-S-41 as constraints on all survivors.

## Open rows (the end state)

- **Q-BOUNDS:**
  - intrinsic bounded-cycle realizations;
  - nonmaximal sources;
  - unbounded image multiplicities;
  - new joint correspondences.
- **Q-T7-FIXED:** the conormal surjectivity of S-02 for a specified smooth image.
- **Q-DIV:** bounded division on generic Weil families.
- **Q-T7-REPLACEMENT:** the semiregular objects that survive S-30-S-36.

## Where it went

**Prompt 46, HODGE_DIVISION.** Its attack already uses B19 and B21. Its Proposition O is the S-14 route.

**The follow-up message** `TO_SEND/PRO/1_Archive_research_by_topic/46b_HODGE_DIVISION_FOLLOWUP_1_DEG_L_open_rows/PROMPT.md`
is still unsent. It must be corrected before it goes:

- It states the constraints S-30-S-41 for all survivors. The run proves them under restrictive hypotheses only.
- "Markman's construction must pass S-30-S-36" is unjustified.
