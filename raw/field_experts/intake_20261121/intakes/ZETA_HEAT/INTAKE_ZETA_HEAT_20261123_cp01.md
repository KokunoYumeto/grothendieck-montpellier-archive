# Intake of ZETA_HEAT checkpoint 01 (prompt 62), first intake

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent afa2696b67cad55de, a copy of af2a18f62da23b48e). The run
is GPT-6 Astra (ChatGPT Pro mode), still going.
- Checkpoint 01: 23 Nov, 16:54 UTC, the newest filed.
- Return: `research_returns/ZETA_HEAT_checkpoint_01_20261123T1654Z_unzipped`.
- Prompt as sent: `TO_SEND/PRO/1_Archive_research_by_topic/SENT/62_ZETA_HEAT/PROMPT.md`. Its ALP_CONNES item 5 and the
  credit of S50 to Suzuki were added by af2a18f6 earlier today.

A is Alpöge's theorem: RH for every Dirichlet L-function, ζ included.

## 0. Scope: what was read
- **Registers:** QUESTIONS.tsv (all 17 rows), the end of LEDGER.md (16:18 and 16:52 UTC), STATEMENTS.tsv (31 rows),
  and CHECK_EVENTS.tsv counted by type (104 events).
- **The finite-detection theorem** (`workbench/drafts/finite_detection/finite_detection.tex`):
  - the statement and its analytic part (lines 1-200): the Gaussian identity, the convolution estimate (fd-gauss) and
    the cone estimate (fd-cones);
  - not read: the local Hermite analysis that follows.
- **Statements read:** prop:trace-height, thm:isolated-pair, prop:liminf-rayleigh, thm:positive-directions,
  thm:two-thirds-survival, thm:nonreal-height.
- **Not read:** the other proofs, and the paper assembly (`paper/main.tex` and its sections).

## 1. Verdicts
- **thm:fd-limits, analytic part:** confirmed by a targeted proof check.
  - H_{−a} = e^{a∂²}H₀ is the Gaussian convolution of variance 2a.
  - The bound on the remainder of the canonical product follows.
  - S(z) and |L(z)| are bounded in cones |Im z| ≥ q|z|, using the zero count N(R) ≪ R log R.
  - So zeros of H_{−a} lie in |arg z| = O(√a), uniformly at large radius.
- **The Hermite orbital constants:** confirmed by computation.
  - 𝔯₂ = π: by HCIZ, φ₂(X) = sin δ/δ, whose first negative value is at δ = π.
  - 𝔯₃ = 2π/√3: from the HCIZ determinant for He₃ roots (0, ±√3), the bisection gives 3.627598728… against
    2π/√3 = 3.627598728…, agreeing to grid precision.
- **thm:isolated-pair, leading term:** confirmed by computation at κ = 0.
  - For f = (z−b)² − δ²/4, e^{a∂²}f = f + 2a, so the zeros collide at a = δ²/8, the κ = 0 term of a_c.
- **Everything else:** at statement level. It carries the run's own checks: 34 targeted, 34 independent re-proofs,
  9 computations, 2 refutations of earlier formulations (an example and the δ-free direction rule at zero 1169).

## 2. What is new, usefulness first
1. **Simplicity as the rate of a finite test** (thm:fd-limits).
   - For the backward heat flow H_{−a}, with ∂_tH = −∂²_zH and H₀ = ξ/8, the least order m_*(−a) of a negative
     Toeplitz minor of the normalized Taylor coefficients satisfies √a·m_*(−a) → min_{m_x≥2} x𝔯_{m_x}/(2√2).
   - The Jensen detecting degree satisfies a·j_*(−a) → x_*²/8, where x_* is the least multiple zero.
   - So "all zeros are simple" is equivalent to each of √a·m_* → ∞ and a·j_* → ∞.
   - Usefulness: simplicity becomes an exact asymptotic statement about a finite positivity test, with explicit
     constants (the unitary-orbital radii 𝔯_m). It is for readers of the de Bruijn-Newman literature (Rodgers-Tao)
     and of Jensen polynomials (Griffin-Ono-Rolen-Zagier).
2. **A trace certificate below a height** (prop:trace-height).
   - E(T) = Σ_{0<γ≤T}(m_γ − 1) ≤ (T²/2)·𝒟_N, for the trace defect 𝒟_N of the finite compressions.
   - So a certified 𝒟_N < 2/T² proves simplicity up to height T, and 𝒟_N → 0 is equivalent to simplicity of all zeros.
   - Usefulness: a finite numerical route to simplicity at a given height, on the spectral side.
3. **Motion and persistence.**
   - The isolated pair: collision at a_c = δ²(1/8 + κ/32 + O(κ²)).
   - Each direction of zero motion holds for a proportion ≥ 10^{−14} of the zeros, for every fixed Dirichlet
     character, with the δ-free rule refuted at zero 1169.
   - Every fraction < 2/3 of zeros survives for −c/(log T)² ≤ t ≤ 0.
   - Nonreal zeros of H_{−a} occur below exp(exp(C/√a)).
4. **CUE collision statistics:** the first collision is Weibull-3/2, and the label-agreement probability is
   0.666546601837…
5. **The spectral comparison:**
   - prop:liminf-rayleigh: a vanishing liminf of the ratio along one subsequence already forces simplicity.
   - S50 is presented as Suzuki's (rem:suzuki-multiplicity), as our prompt required.
6. **The main question (MAIN-SIMPLE) is open.** The current gates: scaled Toeplitz or Jensen divergence, 𝒟_N → 0, a
   moment polynomial certificate, or the liminf ratio. "No such estimate established."

## 3. Scope of the inputs
- A is used for the zero location of H₀ (the statements say so where it enters).
- The CUE results are unconditional random-matrix theorems.
- Masullo: not used.

## 4. Integration
No note of ours on the heat flow or Jensen polynomials exists in `claude_math_notes/`, `results_register/` or the paper
seeds. `reports_20261122/extended_grand_rh/workshop_inputs/62/` is the RH workshop's (Codex's) material, and I did not
edit it. Nothing was applied. For the main session: the board rows below.
Log: `INTEGRATION_ZETA_HEAT_20261123.tsv`.

## 5. Prompt updates
None. The prompt is sent and the run is going.

## 6. Hexagon readiness
| result | state | gate left |
|---|---|---|
| thm:fd-limits | analytic part and 𝔯₂, 𝔯₃ checked by us; the run reports independent re-proofs | a check of the local Hermite/orbital part; comparison with Shi (2026) and Griffin-Ono-Rolen-Zagier |
| prop:trace-height | statement only | a proof check |
| thm:isolated-pair | the leading term checked | the O(κ²) and uniqueness proof |

## 7. Board candidates
| title | statement | what it adds | gate left |
|---|---|---|---|
| Simplicity of the zeta zeros as the growth rate of a finite positivity test | Under A: √a·m_*(−a) → min_{m_x≥2} x𝔯_{m_x}/(2√2), and a·j_*(−a) → x_*²/8. Simplicity ⇔ √a·m_* → ∞ ⇔ a·j_* → ∞. 𝔯₂ = π, 𝔯₃ = 2π/√3. | exact limits and constants for the de Bruijn-Newman finite tests | check of the local part; literature |
| A trace certificate for simplicity below a height | E(T) ≤ (T²/2)𝒟_N | a finite certificate at a given height | proof check |

## 8. For the P vs NP fleet
The Toeplitz-minor test is a determinant-sign (total-positivity) certificate. The fleet's proof graph has no
total-positivity or Pólya-frequency node: its determinant nodes L-gct-001 to 003 concern determinantal expressions of
polynomials. No map was constructed; the translation would need a node for "sign patterns of minors of a coefficient
sequence".
