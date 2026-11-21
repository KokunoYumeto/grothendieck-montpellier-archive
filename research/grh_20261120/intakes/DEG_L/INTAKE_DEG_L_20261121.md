# Intake of DEG_L (prompt 41, "Hodge degrees are L-values: Rallis and semiregularity"), checkpoint 03, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent ad85573792c61a914), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), root and child agents (`/root/rallis_t6` and others) of the same
model; the run writes "GPT-6 Astra Pro, effort not exposed". It began 21 Nov 00:47 UTC and **is still going**; no
three-hour review had occurred at checkpoint 03.

Notation: **A** = Alpöge's RH and Dirichlet GRH (a theorem); **M** = Masullo's Hecke GRH (conditional); **U** = unconditional.
"032" = OpenAI's family-032 proof of the rational Hodge conjecture for CM abelian varieties; "vHS" = van Hoften-Sempliner.

## 0. What was read, and the scope

- **Return folder:** `research_returns\DEG_L_checkpoint_03_20261121T0302Z_unzipped\DEG_L\` (checkpoint 03, 03:02:14 UTC).
  Newest DEG_L present at the start and the end of this intake.
- **Prompt as sent:** `SENT\41_HODGE_DEGREES_ARE_L_VALUES_Rallis_and_semiregularity\PROMPT.md` (the question, the task, the
  language section).
- **Read:** `LEDGER.md` (all), `QUESTIONS.tsv` (all 80 rows), `IMPLICATIONS.md` §§ "degree and L-value", "Route 2",
  "Semiregularity", `TRANSCRIPTION_NOTES.tsv` (header only: no rows), and in `DEG_L.tex` (4455 lines): §1 lines 84-163
  (what 032 supplies, T6.1-T6.3), 385-505 (T6.11-T6.14 with proofs), 1242-1431 (B19, all five parts with proofs), the
  statements of B20 (1479-1520) and B21 (1601-1690), S-01, S-02, S-05, S-06 with proofs (1772-1940), S-14's statement
  (2144-2175), the GRH-hypotheses section and B1's inequality (grep).
- **Read in full, every step checked (9):** T6.1, T6.2, T6.3, T6.14, B1 (the Euler-product inequality), B19 (B19.1-B19.5),
  S-01, S-05, S-06 (Venkataramana carried).
- **Proof read, structure checked, cited theorems carried (3):** T6.11 (Haan, Thm 3.4), T6.12 (Gan-Qiu-Takeda, Thm 11.4(ii);
  the finite-spectrum argument checked), T6.13.
- **Statement level:** everything else (T6.4-T6.10, T6.15; B1a-B18, B20, B21; S-02-S-04, S-07-S-21; DIV1-DIV5; DER1-DER7;
  LN7), with the run's states taken as reported.
- **Compared with:** my ZETA_TWO intake (CM01, the scope of A and M), and the THETA3 and HECKE_DIV intakes (parts 1-2).

**Settled and moving.** Settled: the literal T6 (refuted: Q-T6), the exact degree identities (T6.1, T6.9-T6.14), the
refutation of universal semiregularity (Q-T7-UNIVERSAL), and many reductions. Open: Q-BOUNDS (uniform target-dependent
witnesses), Q-T7-FIXED (semiregularity of a fixed smooth image: the conormal gate S-02), Q-DIV (bounded division on Route 2).

## 1. Verdicts

| Id | Statement (short) | Input | Verdict |
|---|---|---|---|
| T6.1 | for f: S → A with surface image and ample H, deg_H f_*[S] = ∫_S(f^*Ω_H)² = ½Σ_{a<b}∫ξ_ab∧ξ̄_ab, ξ_ab = f^*ω_a∧f^*ω_b: a positive sum of wedge norms | U | **confirmed** (sign and the factor ½ rechecked). |
| T6.2 | every class in H¹(B_1)⊗…⊗H¹(B_4) ⊂ H⁴(A) has degree 0 against the product polarization; so 032 Prop. 3.1's output (a switch class) is never effective, and its degree cannot equal a positive theta norm | U | **confirmed** (odd degree 1 + 2a_i in each factor). This is the refutation of the sketch's T6 as worded. |
| T6.3 | replacing the clearing maps f_i by [M]∘f_i at the same level gives deg z_M = M⁴ deg z and k_M = M⁴k: level alone does not determine the raw degree | U | **confirmed**. |
| T6.4-T6.8 | cover and clearing divisions cancel in Chow; norm/trace clearing of the period; signed-degree bound for the divisor kernels | U | statement level (T6.5's check note on ∏M_i consistent with T6.3). |
| T6.9, T6.10 | every pulled-back coordinate form has a finite theta expansion; the scalar/form norm conversion | U (vHS, Liu, BMM) | statement level. |
| **T6.11** | exact energy E_f = (2/a_K)Σ_{j,σ}Q_jσ with Q_jσ = L_E(3/2, BC(τ_σ)⊗γ_σ³)/L_F(3, ε_{E/F}) · Z^#_σ (Haan's Rallis formula, U(1) → U(3)); deg ≤ 4(ΣQ)²/(a_K²∫ω²), with equality up to the primitive defect | U (Haan Thm 3.4; Wu) | **proof read, Haan carried.** The Hodge-index step (deg ≤ E²/∫ω²) and the bookkeeping checked. The L-value is at s = 3/2 in the unitary normalization: inside absolute convergence (B1a: arithmetic 3, centre 2). |
| **T6.12, T6.13** | the wedge Θ_1∧Θ_2 is the theta transform of a toric period on H = U(W_1⊥W_2); a genuinely finite cuspidal expansion; ‖Θ_1∧Θ_2‖² = (8/a_K)Σ_λ L(1, π_λ×χ_V)Σ p_λr p̄_λs Z^*_λ; in general deg = (4/a_K)Σ L(1, π_λ×χ_V)Z^*_λ(q, q) | U (GQT Thm 11.4(ii), Wu Thm 5.3) | **proof read, GQT carried.** Checked: anisotropy (definite W at the active place) so no Eisenstein terms; the graph-orbit unfolding argument for orthogonality of distinct copies; finiteness from dim H⁰(X_K, Ω²) < ∞ plus admissibility. The L-functions are **standard L-functions of U(2) cusp forms at the edge s = 1**, not Hecke L-functions. |
| T6.14 | fixed-data level change by index d multiplies a_K^{−1}, energies and raw degree by d | U | **confirmed** (Haar volume). |
| T6.15 | a Steinberg constituent occurs in an admissible balanced wedge (refutes the character-only reduction Q-T6-CHARONLY) | U | statement level. |
| B1 | for Re s = σ > 1: ζ_K(2σ)/ζ_K(σ) ≤ \|L_K(σ,χ)\| ≤ ζ_K(σ) | U | **confirmed** (Euler product). It bounds T6.11's global factor uniformly for fixed [F:Q], **with no GRH**. |
| B1a, B2-B18 | infinity type; LLS edge bounds (A, Dirichlet) and Hecke edge bounds (M), not used by the main line; level vs conductor; Weil projector B6 with resultant denominator; B7, B8 (effective witness ⇒ bounded division, quadratic bounds); B15 (linear bound in polarized isogeny degree); B17-B18 | mixed | statement level. |
| **B19** | fixed simple CM isogeny class (E, Φ), A = C^g/Φ(Λ), J = [Λ : Λ^−] (index of the largest O_E-stable sublattice): covol Hom_E(A_0, A) = 2^{−g}√\|D_E\|(V/V_0)J; least nonzero squared Hom norm in [g(VJ/V_0)^{1/g}, K_E(VJ/V_0)^{1/g}], K_E = (2/π)(g!√\|D_E\|)^{1/g}; a minimal isogeny has J ≤ deg h ≤ K_E^g J/g^g; for Weil type (g = 2n) a witness of degree ≤ D_0K_E^n(VJ/V_0)^{1/2} and bounded-division complexity O(J); J ≤ N(f_A) (conductor of the endomorphism order) | U (Milne ANT Thm 4.19, Prop. 4.26; B8 constants) | **confirmed.** I checked: I = (Λ:I_0), II_0 = Λ^−; c(IJ) = c(I)c(J)/c(O); c(O) = 2^{−g}√\|D_E\|; ∏λ_σ = deg h·V/V_0; AM-GM; Minkowski with v_{2g} = π^g/g! giving K_E; deg(h_*Z_0) ≤ Q(h)^n deg Z_0; J ≤ N(f_A); p_h = √(deg h)p_0. The B8 constants C_N, C_D are carried. |
| B20, B21 | for every integral Z_0 ⊂ A_0 of dimension n and degree ≤ D_0 with nonzero Weil projection, the reduced image h(Z_0)_red has degree ≥ √2·n!√V/(R·S(D_0))·√J; with B19 the least such degree is pinched between two fixed multiples of √J | U (Ullmo-Yafaev Prop. 4.1; FGA 221 boundedness) | statement level. |
| S-01 | the 032 morphism f: Y → A pulled back to a connected étale cover of degree d > 1 keeps the nonzero period but is not an immersion | U | **confirmed**. |
| S-02 | for a smooth embedded surface Y ⊂ A, g ≥ 3: Bloch semiregularity ⇔ surjectivity of H¹(O_A)⊗∧³W → H¹(Y, N^∨⊗K_Y) | U | statement level. |
| **S-05, S-06** | for a compact ball quotient Y → A with surface image: dim ker τ_f ≥ g·q(Y) − C(2g, g−2); along a cofinal system of principal congruence covers q(Y_j) → ∞, so the Buchweitz-Flenner semiregularity map is not injective at deep levels | U (Calabi-Vesentini; Buchweitz-Flenner Prop. 7.21; Venkataramana Thm 1) | **confirmed, cited theorems carried** (H¹(T_Y) = 0 gives H¹(O_Y)^g ↪ T²; Vandermonde Σ_r C(g,r)C(g,r+2) = C(2g, g−2); unbounded q since the compact dual P² has H¹ = 0). It refutes the sketch's T7 in its universal (all-level) form; T7 for a fixed smooth image stays open. |
| S-03, S-04, S-07-S-21 | shortcuts refuted (S-03, S-11, S-13, S-15, S-18-S-21); descent S-07; integral Chern projector S-09; **S-14: one weakly G-semiregular perfect complex E_0 with e^{B_0}ch(E_0) = λt + P(θ) at one fibre ⇒ bounded division on the whole family** (Perry's deformation theorem + DIV1); S-16, S-17 | U | statement level. |
| DIV1-DIV5 | proper parameter space of bounded signed cycles (FGA 221); bounded witnesses on a dense set suffice; the embedded semiregular implication; an explicit Hecke bound; a posteriori bounded complexity for Markman's fourfolds | U (+ Markman) | statement level (the run reports independent whole-proof checks). |
| DER1-DER7 | test-object repairs refuted (DER2, DER3, DER5, DER6); **DER4: an Adams operation ψ^M (M = the Kummer gerbe's band order) untwists in virtual rank zero and multiplies the Weil component by M^n; DER7: multiplier N^* = v\|b β_0\|\|r\|^n independent of the gerbe order for r ≠ 0** | U (SGA 6 V, (7.1.1)) | statement level. |
| LN7 | (refuted local-newvector claim) | U | statement level. |

**Counts.** About 75 findings in the register; my rows group them. Every step checked: 9 (T6.1, T6.2, T6.3, T6.14, B1, B19,
S-01, S-05, S-06). Proof read with the cited theorems carried: 3 (T6.11, T6.12, T6.13). Statement level: the rest. Refuted
by me: 0. The run's own refutations (Q-T6, Q-T6-CHARONLY, Q-T7-UNIVERSAL, B18, B20, B21 as "transport cannot be uniform",
S-13, S-15, S-18-S-21, DER2, DER3, DER5, DER6, LN7) stand as far as I read.

## 2. What is new

- **The prompt's premise is answered, strictly.** The degree of the 032 surface is an exact finite sum of L-values
  (T6.11 with Hecke L at 3/2; T6.12-T6.13 with standard U(2) L at 1), but **not one L-value**, and the output class of 032 Prop.
  3.1 has degree zero (T6.2). The Hecke values at 3/2 are bounded above and below with no GRH (B1). So **the L-values are not
  where the difficulty is.** The growth that matters is arithmetic: the core index J of the target lattice (B19), with
  witness degree of exact order √J for fixed-source transport (B19 + B21). That is a precise, new location of the obstacle.
- **B19 is the cleanest new theorem of the run** (as far as I know; classical ingredients): exact covolume of Hom_E(A_0, A),
  sharp least norm of order J^{1/g}, and from it a Weil witness of degree O(√J) and bounded-division complexity O(J), with
  explicit constants depending only on (E, D_E, V/V_0). It is unconditional.
- **B21** makes the √J lower bound uniform over every bounded-degree source witness (finite stabilizers over the whole Hilbert
  family). So no fixed-reference transport can give uniform bounded division along a CM sequence with J → ∞.
- **S-05/S-06** refute semiregularity of the 032 morphism at deep levels; **S-14 with DER4/DER7** turns one weakly
  equivariant semiregular perfect complex at one fibre into bounded division on the whole family with an explicit multiplier.
- **Against tonight's runs:**
  - **HECKE_DIV** (P0, R21-R23, A1: bounded division ⇔ a uniform effective bound; P2b: raw transport grows like m^{2n}):
    B19 sharpens the transport. A minimal-norm isogeny gives degree O(√J) instead of the raw growth, and B21 shows √J cannot
    be beaten by any bounded source. The three runs' common picture ("uniformity along the orbit is the gate") now has an
    exact rate: √J.
  - **THETA3** (B17: the seesaw's upper space has signature (3,1), so the sketch's 1.7 is not proved): DEG_L uses only the
    U(1) → U(3) Rallis formula (Haan) and the U(2) → U(3) doubling formula (GQT); it does not touch 1.7, and its anisotropy
    argument for T6.12 is the definite-at-one-place condition THETA3 found missing in the other direction.
  - **ZETA_TWO** (CM01: RH for CM motives under M): T6.11's Hecke characters are of the CM type CM01 treats, but they are
    evaluated at 3/2, where neither RH nor GRH is needed; T6.13's L(1, π_λ × χ) are U(2) (GL_2-type) L-functions at the edge,
    which neither A nor M reaches.

## 3. The scope of the two proofs

- **Neither proof enters the main line.** T6.11's Hecke values at s = 3/2 are in absolute convergence (B1, U). B19-B21, the
  S-rows, DIV and DER are U.
- **A:** only in B2's edge estimates for Dirichlet characters (LLS v3 Thm 1.5), which the main reductions do not use.
- **M:** only in B2's Hecke edge estimates, likewise unused.
- **Beyond both:** any bound at the edge for T6.13's standard L(1, π_λ × χ) of U(2) cusp forms (Ramanujan and GRH for GL_2-type
  L-functions); the run says it asserts no such bound.
- **No statement claims more than its input.** The run's GRH section (lines 4365-4377) states this scope correctly.
- The prompt's sentence "the size of those L-values controls the degrees, and with them the bounded-division gate" is
  therefore **refined, not confirmed**: the L-values are uniformly bounded for free; the gate is the integral data (J, the
  Schwartz inputs, the realization coefficients).

## 4. In Grothendieck's frameworks

The run states T6 in Hodge theory on Shimura varieties (positive (1,1)-forms, the Hodge index theorem), B6-B8 in homological
and numerical motives with the Hodge standard conjecture (B7 uses Hodge standard positivity, now a theorem for abelian
varieties by Milne's Hexagon paper), DIV1 with the Hilbert and Chow parameter spaces of FGA (Bourbaki 221, Lemme 2.4 p. 255,
Théorème 3.2 p. 260), T6.5 with SGA 7 I Exp. VII §2.4 (biextensions), DER4 with SGA 6 V (7.1.1) (Adams operations). Two
translations it does not give:
- **S-14 is the variational Hodge conjecture route** (Grothendieck, "On the de Rham cohomology of algebraic varieties", Publ. IHÉS 29,
  1966, the footnote stating it, p. 103 from memory: locator to verify): a Hodge class that is algebraic at one fibre, realized by a semiregular object, stays algebraic in the
  family. The run's contribution is the bounded version (fixed N, D) needed for Route 2.
- **B19 in motivic terms:** in the CM isogeny class, the Hom lattice is the ideal (Λ : I_0) of O_E; J measures how far the
  lattice is from being an O_E-module, i.e. the conductor of End(A) (B19.4). Bounded division is controlled by the
  Néron-Severi/Hom lattice of the CM motive, not by its L-function.
- No archive cote is engaged; the TRANSCRIPTION_NOTES file is empty. Cote 16 is named once (line 1575, as context).

## 5. Integration

- **HODGE_BRIDGE_SKETCH_20261121.md** (`reports_20261120\hodge_bridge\`):
  - **T6:** "refuted as worded (DEG_L T6.2, T6.3); replaced by the exact finite identities T6.11 (Hecke L(3/2), unconditional
    bounds B1) and T6.13 (standard U(2) L(1)); the degree is not one L-value".
  - **T7:** "universal semiregularity refuted at deep levels (S-05, S-06); fixed smooth image open at the conormal gate S-02;
    deformation reduced to one weakly equivariant semiregular perfect complex (S-14, DER4, DER7)".
  - **Route 2:** "fixed-reference transport gives witness degree Θ(√J) (B19, B21) and complexity O(J); uniformity requires
    target-dependent cycles or the S-14 deformation".
- **HECKE_DIV intakes:** add B19 next to P2b (the √J transport replaces raw m^{2n} growth along CM sequences of fixed field) and
  B21 next to R24E/R24F (bounded sources cannot be uniform).
- **ZETA_TWO intake §3:** add "DEG_L: the L-values in the Rallis degree formulas are at 3/2 (absolute convergence) or are U(2)
  standard L-values at 1; neither A nor M bears on the 032 degrees".
- **Prompts 37-40 successors (THETA3, HECKE_DIV, GHOST, JACOBIANS):** B19's J is the parameter to carry; S-14 the deformation
  target.

## 6. Prompt updates (successor of DEG_L)

1. **Main question: J and the deformation object.** Either construct, on one fibre of a Weil-type family, a weakly G-semiregular
   perfect complex with e^{B_0}ch(E_0) = λt + P(θ) (S-14's hypothesis), following Markman's fourfold construction in higher
   dimension; or prove a uniform bound on J along a dense set of CM points of a Weil family (B19 then gives uniform bounded
   division there, DIV2). These are the two exits the run has located; ask for one of them, not more refutations.
2. State in the prompt that the Hecke values at 3/2 are bounded unconditionally (B1) and that GRH enters only at the edge, so
   that the successor does not spend time on GRH bounds.
3. For T6.13, ask whether the U(2) standard values L(1, π_λ × χ) can be avoided altogether (T6.11 already does), or are needed
   for a lower bound.
4. Model and effort: GPT-6 Astra (ChatGPT Pro mode).

## 7. Hexagon readiness

- **B19 (+ B21): "Weil witnesses of degree Θ(√J) in a CM isogeny class".** 1 Complete: B19 yes (checked); B21 statement level.
  2 Self-contained: yes (Milne, Minkowski, Ullmo-Yafaev, FGA; the B8 constants come from B6-B8 of the same run, which would
  have to be included). 3 Stable: the run is still going; literature search not done (the Hom-lattice covolume is classical
  in spirit; its use for Hodge-class witnesses after 032 is likely new). 4 Checked: my targeted check of B19; no independent
  computation (a numerical example for g = 2 would do). 5 Interest: moderate now (the Hodge conjecture for CM abelian
  varieties is news this month; uniform bounds are the next question). **Gates:** B6-B8 and B21 checked; a literature
  search; the run's final. Candidate, not urgent.
- **T6.2 (032's Prop. 3.1 output has degree zero for the product polarization)**: elementary; useful as a remark in a 032 note,
  not a post on its own.
- Nothing else is near the five tests.
