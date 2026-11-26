# Paper seeds: ALP_CONNES checkpoint 18

Seed by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), 22 Nov 2026. The run is GPT-6 Astra (ChatGPT Pro mode).

"Checked" means a targeted proof check by Claude Opus 5.5 at effort high, with the cited inputs taken as stated. "Statement read" means no proof
was read by us. Every proof also has check events of the run itself, by GPT-6 Astra (ChatGPT Pro mode), in the ZIP's CHECK_EVENTS.tsv.

Input A, throughout: Alpöge's theorem of 20 Nov 2026, RH for zeta and for every primitive Dirichlet L-function. It is
cited as a theorem and has not been replayed by us.

## Paper 1. Connes' trace formula over Q is equivalent to the generalized Riemann hypothesis

### Main theorem
For a primitive Dirichlet character χ of conductor q, let E_χψ(x) = √x Σ_{n≥1} χ(n)ψ(nx), and for χ = 1 subtract
x^(-1/2)∫_0^∞ψ. For Λ large, take the parity-selected prolate functions for time radius Λ and frequency radius Λ/q,
all indices n ≤ 4Λ²/q, and let Q_{χ,Λ} be the orthogonal projection of L²(R_+^*, d*x) onto their image under E_χ.
For χ = 1 complete by the two coordinates ψ(0) and ∫ψ, on which dilation acts by a^(-1/2) and a^(1/2), and call the
projection P_Λ. Let Q_Λ be the sum over χ of these projections and R the centred action of the idele class group
C_Q = Ẑ^* × R_+^*.

Then the following are equivalent.
1. RH for zeta and for every primitive Dirichlet L-function.
2. For every Bruhat test h on C_Q,
   lim { 2 log Λ · h(1,1) − Tr(Q_Λ R(h)) + ∫ h_1(r)(r^(-1/2) + r^(1/2)) d*r } = W(h),
   where W is Weil's distribution defined by primes and the archimedean place, and h_1 is the trivial-character part.

With input A, statement 2 is a theorem. The proof of 2 ⇒ 1 uses no RH: unconditionally the cutoff defect is
asymptotically positive, so the trace formula gives Weil positivity. The conductor and any finite set of semilocal
places stay fixed as Λ grows. There is no uniformity in either, and no statement for other number fields.

Inputs: A (only to assert 2); Connes-Consani-Marcolli's Weil criterion (Prop. 6.2, Cor. 6.3); for the unconditional
Gram bound, Matomäki-Shao-Tao-Teräväinen, Forum Math. Pi 11 (2023) e29, Lemma 3.9(ii), p. 46.

### Why it matters
Connes proposed this trace formula as the spectral meaning of RH. This supplies an explicit cutoff for which the global
formula and GRH over Q are the same statement, and with Alpöge's theorem the formula holds.

*Update 23 Nov 2026 (intake of ALP_CONNES cp44, agent afa2696b67cad55de, Claude Opus 5.5 at effort high, after the H27 editor's records `reports_20261123/h27_note/RECORDS.md`, Claude Fable 5.2 at effort max):* the editor reports that the statement of T51 is Connes's own, that Connes 1999 proves his Theorem 5 only in positive characteristic, and that S50 (the finite prime-built approximants of Ξ/Ξ(0) with multiplicities, ALP_CONNES checkpoint 24) is a direct consequence of M. Suzuki, arXiv:2610.32704. Before this paper is written, compare T51 with Connes's statement at its locator and present what is ours as the proof for this cutoff; S50 is credited to Suzuki.

It continues these works (all from memory or through the run's locators; none opened):
- A. Connes, Selecta Math. 5 (1999), §VIII and Appendix II, Theorem 6;
- Connes-Consani-Marcolli, "The Weil proof and the geometry of the adeles class space" (2007 preprint), Theorem 6.1
  and Proposition 6.2;
- R. Meyer, Duke Math. J. 127 (2005), Theorems 5.8 and 5.11.

Before any wording of novelty, open Connes 1999 §VIII and compare the cutoff and the statement of his equivalence.

### The argument, in order
| result | exact scope | proof file and lines | check by us |
|---|---|---|---|
| AC-T01, T02 | A is RH for all unitary characters of C_Q, and is equivalent to Weil positivity | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_windows.tex` 41-151 | statement of T02 and start of its proof read |
| AC-T42, T43 | theta transform and constrained prolate approximation | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_principal.tex` 33-420 | T42 statement read |
| AC-T41 | trace formula in a nonprincipal sector, under A | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_frequency_tightness.tex` 361-567 | statement read |
| AC-T44 | trace formula in the principal two-constraint sector, under A | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_principal.tex` 422-953 | proof read; checked given AC-T25, T28-30, T38-40, T42, T43 |
| AC-T45 | the two polar lines, unconditional; trace under A | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_polar_completion.tex` 32-238 | checked given T42, T44 |
| AC-T46 | assembly over all characters | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_rational_assembly.tex` 3-90 | checked given T41, T44, T45 |
| AC-T47, T48 | semilocal dictionary and angle cutoffs at fixed S | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_adelic_dictionary.tex` 24-595 | not read |
| AC-T49 | Möbius polynomial bound, unconditional | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_unconditional_converse.tex` 11-73 | checked given the cited lemma |
| AC-T50 | Gram bound and positive defect, unconditional | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_unconditional_converse.tex` 74-299 | checked given the raw prolate estimates of T29 and T48 |
| AC-T51 | the equivalence | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_unconditional_converse.tex` 301-401 | checked given the rows above and the criterion |
| MA-HM-001, MA-HM-003 | a narrow Hilbert return to Meyer's quotient exists at every width iff RH | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\hilbert_meyer_bridge.tex` 86-254, 387-507 | checked given GRH_NIGHT MT-M18 and M26 |
| MA-JP-004, MA-FT-002 | local and global limits agree iff the upper zero deficiency is empty | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\causal_trace_separation.tex` from 4; `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\MAS_ARTIN_checkpoint_15_20261122T0246Z_unzipped\modules\full_test_slow_band.tex` 305-359 | checked given MA-FT-001 |
| MT-M20, MT-M23 | limits of positive models when zeros are multiple | `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\GRH_NIGHT_checkpoint_07_20261121T0617Z_unzipped\GRH_NIGHT.tex` from 18843 and from 19513 | checked earlier given MT-M18/19 and Hu-Kaneko-Martin-Schildkraut |
| AC-T13 | strict positivity in each fixed window, under A | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\trace_windows.tex` 1150-1189 | statement read |

None of these uses Masullo's claim. MA-HM-003 is proved in the run's reconstructed model and is not to be worded as a
refutation of his draft.

Programs: none is needed for the main theorem.

### Research question
Prove statement 2 for one Dirichlet sector directly from the cutoff, without zero location. This would be a second proof
of RH for that function. The gate is the identification of the positive defect limit with Weil's distribution: AC-T50
proves positivity and not the limit.

Routes not tried, as far as we read (suggestions by Claude Opus 5.5 at effort high):
- growing S with Λ and controlling the semilocal defect uniformly;
- the translation bound on the narrow completion of MA-HM-003;
- the same identity over F_q(t), compared with purity.

Workbench: RH, trace formulas and noncommutative geometry.

## Paper 2. The 3-primary even K-groups of Q(ω, ∛269), in every degree

### Main theorem (unconditional, computer-assisted)
Let E = Q(ω, α) with α³ = 269, ω² + ω + 1 = 0, and λ = ω − 1. Let σ(α) = ωα make the module a Z_3[ω]-module. For every
integer e ≥ 1,

    K_{2e}(O_E)_(3) ≅ Z_3[ω]/λ^κ,    κ = 5 + 2 v_3(e) + [e ≡ 2 mod 3],

so its order is 3^κ. Equivalently, the strict 3-adic Selmer group over K = Q(ω) of T/O(χε^(-e)), with O = Z_3[ω],
T = Q_3(ω), χ the cubic Kummer character of 269 and ε cyclotomic, is O/λ^m with m = 4 + [e ≡ 2 mod 3]. "Strict" means
zero at 3 and unramified at 269. At e = 0 that Selmer group is zero, and Cl(E)_(3) = 0.

Inputs: Soulé, Astérisque 147-148 (1987) §§6.1-6.2, pp. 246-247; the K-theory to étale cohomology comparison (Weibel,
K-book VI 8.3); Chevalley's ambiguous class formula; Schneider's logarithmic descent; class groups, units and
logarithmic class groups from PARI/GP 2.19.1 with full bnfcertify (Belabas-Jaulent's algorithm). All are through the
run's locators, with no source opened. Neither A nor Masullo's claim is used.

### Why it matters
It gives an infinite family of K-groups of a non-abelian sextic field exactly, and shows a variation with the weight
mod 3 besides the cyclotomic term v_3(e). For the Alpöge programme it settles the coefficient-3 length left open in
ALP_MACHINE AM-H08, and only that prime: it gives no zero location.

### The argument, in order
| result | content | proof file and lines | check by us |
|---|---|---|---|
| AC-G22 | finiteness, cyclicity, residual line | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cm_twisted_selmer.tex` 39-271 | checked given Soulé |
| AC-K10, K11 | localization and local subtraction | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\selmer_k_theory.tex` 20-179 | not read |
| AC-K12 | class group and cyclic K-module | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\selmer_k_theory.tex` 181-284 | checked given K10, K11 and the cited theorems |
| AC-K13 | logarithmic invariant of E | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_logarithmic.tex` 25-112 | not read |
| AC-K15 | certified first-layer bound | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_layer_certificate.tex` 14-293 | statement read |
| AC-K16, K17 | tower and rank gate | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_iwasawa_tower.tex` 20-298; `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_rank_gate.tex` 9-164 | not read |
| AC-K18 | exponent five, period nine | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_uniform_explicit.tex` 10-239 | statement read |
| AC-K20 | finite action | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_finite_action.tex` 9-201 | not read |
| AC-K21 | exponents 4 or 5, period three | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_three_weights.tex` 9-181 | checked given K12, K15, K18, K20 |
| AC-K22 | descent to the degree-nine field | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_real_descent.tex` 12-174 | deduction checked; PARI not rerun |
| AC-K23 | action 4 on Z/9, hence the formula | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\cubic_oriented_action.tex` 9-269 | deduction checked; printed matrices recomputed |
| AC-K09 | for this L-function the Weil form on [-log λ, log λ] is at least the squared norm for 1 < λ ≤ 4, with no RH | `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\kummer_lambda.tex` 470-551 | checked; margin recomputed as 1.282 > 1 by our own program |

Before posting, check K10-K20 and replay the PARI certificates on a second installation or system.

Programs in the ZIP `<local>/Downloads\ALP_CONNES_checkpoint_18.zip`, not run by us:
`ALP_CONNES/evidence/cubic_logarithmic/{pure_cubic_base,real_cubic_layer1,real_cubic_field_action,real_cubic_logarithmic_gamma}.gp`
and `ALP_CONNES/scripts/check_cubic_269.py`.

### Research question
Prove RH for L(s) = ζ_F(s)/ζ(s), F = Q(∛269). Its gate is AM-H04: for every θ > 1/2 there are a constant and
arbitrarily large Y with the Landau-ramp sum at most C y^θ on [Y, Y^(1+δ)].

The arithmetic gate toward it is AC-K25's comparison (`<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\modules\fixed_base_character_reduction.tex` 12-328, statement
read). It moves the all-prime Selmer total to character groups over K with an error x^(409+161ε/5)(log x)². Those
character groups still need the bound o(exp(x^ε/2)).

Routes not tried, as far as we read (suggestions by Claude Opus 5.5 at effort high): an identity with a cubic phase in place of Alpöge's sign,
through Patterson's theta; a bound on elliptic-unit indices uniform over the host characters.

*Update 23 Nov 2026 (intake of ALP_CONNES cp44, agent afa2696b67cad55de, Claude Opus 5.5 at effort high):* by checkpoint 44 the run has proved strict Selmer vanishing over K = Q(√−3), on the original coefficient rings, for most families of the all-prime budget (AC-G130 to G218), and at coefficient 7 it proves the opposite for the matched cubic family: S_7(K, D) ≅ O/7^{s(e)} with s(e) ≥ 1, the weights with s(e) ≥ n lying in at most one residue class mod 7^{n−1} (AC-G219; steps 1-5 checked by us given the PARI class group Cl(L) ≅ C_7², which was not replayed). AC-G220 keeps one matched weight pair in the remainder. The gate is unchanged: the largest matched pair, the other unsupported mixed and noncritical terms, the numerical bound of the maximum, H04.4 and cubic RH (review 34). Intake: `field_experts/intake_20261121/intakes/ALP_CONNES/INTAKE_ALP_CONNES_20261123_cp44.md`.

The run's ordinary rank-three forms at 269 depend on retained automorphy inputs and stay out of this paper.

Workbench: cubic Hecke L-functions.

## For both papers

LaTeX to attach: the modules in the tables; the e-prints arXiv:math/0703392 (Connes-Consani-Marcolli) and
arXiv:math/0311468 (Meyer), both identifiers from memory, to verify before packing.

Never to GitHub, inside the ALP_CONNES returns:
- every .lean file (838 in this ZIP, under `evidence/source_interface`, `evidence/propgk`, `evidence/cubic_*` and
  `work_in_progress`): interface sources of Alpöge's archive, and I found no licence file in the ZIP;
- `evidence/ALPOGE_remark.txt`;
- `work_in_progress/active_agents/sites/evidence/inert_cyclotomic_mu/Johnson_Leung_Kings_0804.2828v2.txt`;
- `work_in_progress/active_agents/sites/evidence/cubic_arithmetic_ec/03QO.txt` and `03QP.txt` (Stacks Project, GFDL).

The screen was by extension and file name. Copies inside .md, .json or .bin members were not screened.

No literature search was made, Hexagon included.
