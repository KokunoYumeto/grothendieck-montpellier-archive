# Primer: the mathematics of GCT_PLETH as of its final return (checkpoint 09, 21 Nov 2026)

By agent a0805369bae2ebddc (Claude Opus 5.5 at effort high), for the main session to read after a compaction. It
restates; it does not develop. Run: prompt 25, GPT-6 Astra (ChatGPT Pro mode), effort not exposed. Final return:
`research_returns\GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped` (`PL` below). The paper seed is
`reports_20261122\paper_seeds\SEED_GCT_PLETH.md`, with every TeX range of `PL\GCT_PLETH.tex`.

**Check labels**, from my intakes (parts 1-4, cp03 addendum) and the seed events of 22 Nov:
- `[TPC]`: targeted proof check;
- `[COMP]`: our computation only;
- `[run]`: the run's whole-proof reviews only;
- `[stmt]`: statement level.

**Notation.** p^λ_{μ,(n)} = ⟨s_λ, s_μ[h_n]⟩ is the multiplicity of S_λV in S_μ(Sym^n V), μ ⊢ m, λ ⊢ mn. W is the
(m−1)-dimensional standard module of S_m, [ν] a Specht module.

## 1. The common mechanism

**The balanced module and the stable chart (G-015, T-032 to T-036) `[run]`.**
- Mechanism: by Cauchy and tensor words, p^λ_{μ,(n)} is the multiplicity of [μ] in the zero-weight space
  (S_λℚ^m)_{(n^m)} with its permutation action.
- When λ₂ ≤ n, removing the first row and a determinant line gives (S_λℚ^m)_{(n^m)} ≅ sgn^t ⊗ S_γW. Here t = λ_m and γ
  is the tail of λ. The coefficient becomes [S_γ W : ν] with ν = μ (t even) or μ′ (t odd).
- Good for: plethysm in a stable range is a restriction coefficient of the reduced standard module.
- My code checked this reduction on 10,164 coefficients, m = 3, 4, 5 `[COMP]`.

## 2. Fixed outer degree

- **T-037, outer degree 4 `[COMP]`** (`PL\work\theta\outer4\full_outer4_report.md`; `outer4_positive.py`).
  - Statement: every p^λ_{μ,(n)}, μ ⊢ 4, counts integer points of ≤ 108 tagged bounded polytopes in ≤ 5 variables.
  - Mechanism: with q ∈ [(3,1)] and t ∈ [(2,1,1)], R = ℚ[q,t]/(q·t) ≅ Sym(U) ⊗ H, an S₄-equivariant freeness over
    U = [(2,2)] in degree (2,0). Every graded piece of H is explicit (Sym^b W, harmonics H_L, D_b = Ind Sym^b h₃).
  - Our check: 60 of 60 table rows; proof not read.
- **G-036, outer degree 5, every value `[COMP]`** (`PL\work\root\complete_outer_five_report.md`; router
  `outer_five_positive.py`).
  - Statement: ≤ 152 bounded polytopes in ≤ 11 variables; evaluation in polynomial bit complexity.
  - Mechanism: stable first-row removal, a determinant complement normalizing to parameters (c, k), and three
    exhaustive providers: G-021 for c ≥ 2k, T-059 for k ≤ c < 2k, G-035 for c < k (walls by G-033, G-034).
  - Our check: 539 of 539 values; proofs not read.
- **G-031, outer degree 5, every zero `[COMP]`** (`PL\work\root\all_five_row_support_report.md`; data
  `FIVE_ROW_SUPPORT_INDEX.json`).
  - Strict chamber (G-028): the five middle labels always occur. The two one-dimensional labels vanish exactly on
    g = (L,1,1,1) and (1,1,1,L) with L ≡ 1 mod 5, and the trivial label also on (1,2,2,1) and (2,1,1,2).
  - Walls: a normal form with period 10 in the end gaps, then a catalogue of 344 vectors with their zero labels.
  - Our check: all 2,408,042 coefficients with n ≤ 22, and all 344 catalogue vectors with their seven values; the
    proof of exhaustion not read.
- **G-012:** outer degree ≤ 3, four polytopes `[stmt]`.
- **T-012, T-013 `[TPC]`** (`PL\work\theta\few_columns_report.md`): stable Foulkes tails of width 5 and 6 by
  Littlewood-Richardson polytopes over the tables of Λ^j(Λ³ℂ⁵) and Λ^j(Λ³ℂ⁶) (16 and 156 constituents, all of
  multiplicity one; recomputed by us). They carry out the remark after Sarkar's Theorem E (arXiv:2610.07929v2).
  Lattice sums not evaluated.

## 3. Varying outer degree (stable families)

- **G-037, hooks `[COMP]`** (`PL\work\root\stable_hook_report.md`).
  - Statement: for λ = (mn−a−(m−1)t−r, a+t, (t+1)^r, t^{m−2−r}), n ≥ a+t, the coefficient [S_{(a,1^r)}W : ν] is one
    polytope count in ≤ m²+3m−4 variables.
  - Support test: let L = b(ν) plus the r smallest weights j−i+1 over cells other than (1,1), (2,1), and D = a+r. The
    coefficient is positive iff D ≥ L and not (D = L+1, ν rectangular, r ∈ {0, m−2}). For ν = (m), use
    L₀ = (r+2)(r+3)/2 − 1 instead.
  - Mechanism: Koszul on Sym W ⊗ ΛW, with the bivariate character s_ν[(1−z)/(1−q)] (Macdonald I §3 Ex. 2-3), the
    coinvariant fake degrees f_ν(q) = ∑ q^{comaj}, and Solomon's theorem for ν = (m).
  - Our checks: 790 of 790 values; the support test on 15,943 cases. The hook series is essentially known
    (Kirillov-Pak, Molchanov).
- **G-038, two-row tails (a,2) `[COMP]`** (`stable_second_row_report.md`): an explicit positive series
  F_ν/∏(1−q^i) plus a Koszul term on two exceptional labels, ≤ C(m,2)+4 polytopes. Our check: 2,511 coefficients.
- **G-039, tails (a,3) `[COMP]`** (`stable_third_row_report.md`): cubic polarization, Ricci splitting, and Koszul
  cycles for e₂, e₃, … and for e₂², e₃, …. Our check: 2,250 coefficients for m ≥ 4.
- **G-040, every fixed b `[run]`** (`fixed_second_part_report.md`): a positive polytope formula of size
  f(b)(m+bits)^{g(b)}. Mechanism: the finite cokernel C_ν of polarization, its minimal covers, and Gröbner bounds
  (Aschenbrenner Thm 3.2; Liang Cor. 42).
  - Limit, GCT_POS PNEW-010 `[stmt]`: at m = 2r, b = r(r+1)+1 the cover needs ≥ 2^{r−1} generators.
- **T-062 to T-065, hooks below the stable range `[stmt]`:** n = a+t−k, with jets of I_Z^k on the simplex points of
  P(W). The bound has the factor D_k of Stirling type.

## 4. The canonical (Hadamard-Howe) map

All `[stmt]` except R-031, which is known:
- R-031: full rank law for target outer degree 5 (Cheung-Ikenmeyer-Mkrtchyan; Ikenmeyer).
- R-035, R-036: second row ≤ 2 and ≤ 3.
- R-044, R-046, R-049: surjectivity ranges, the sharpest n ≥ ⌊(D+t−q)/2⌋.
- R-021 to R-030, R-039 to R-048: families below Sra's bound.

## 5. Cote 133 (Grothendieck's λ-ring manuscript)

- A-001 `[TPC]`: in B(C₂), 2λ²E + E ≠ E² for the free orbit; this refutes our study's scan-19 line (= ALPOGE_GCT
  PL-01).
- A-003 `[TPC, key computation redone]`: over F̄₃ and C₃ the split Green ring has ψ³ not multiplicative, so it is not
  special even with 2 invertible.
- A-007 `[TPC]`: τ²E = ψ²E·ρ₂ + Λ²E·ρ₁², so the monomial terms of scan 28 are virtual. A-012 `[stmt]`: the identity
  holds integrally in exact equivariant K₀.
- A-013 `[TPC]`: h_∅ ⊔ h_∅ is not a summand of a single Hom(I,−); our paraphrase of scans 24-27 is wrong.
- Scan 29, rings for which the ρ_i freely generate:
  - A-021 `[read in part]`: yes for discrete valuation rings of characteristic 0, by rationalization (Curtis-Reiner).
  - A-023 `[TPC]`: no for ℤ_(2)[ε]/(2ε,ε²), by the determinant character 1+ε.
  - A-020 `[stmt]`: no over F₂.

## 6. Open rows at the end

- Q-EFFICIENT: positive #P formulas uniform in b, then for general shapes. Gate: the cokernel C_ν (PNEW-010 bars the
  literal cover).
- Outer degree six beyond two-row output: the checked reference table of 5,214 coefficients is GCT_POS R-NEW-001.
- Q-MAP: the critical annihilator in N_r ⊗ Sym^{r²−1}, for r = 3, 4 first.
- Q-W7 (width 7); scan 29's exact class of local rings; archive context on other cotes.

## 7. Where the results went

- **Hexagon register:** H20 (G-036 with T-037) and H21 (G-037 to G-040), with corrections from the seed:
  - "first with varying outer degree" is false (Pak-Panova-Swanson arXiv:2511.02312, Narayanan arXiv:2403.03443);
  - #P membership for fixed |μ| is known (Kahle-Michałek; Fischer-Ikenmeyer);
  - G-031's complete list of zeros is the proposed headline.
- **Seed:** `SEED_GCT_PLETH.md`, one paper: all zeros in degree five, positive formulas in degrees 4 and 5, stable
  families.
- **Prompts:** 52 (GCT_POS); the plethysm write-up.
- **Cote 133:** paper 5 of `SEED_ARCH_ALG.md`.
