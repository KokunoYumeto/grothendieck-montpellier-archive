# Intake of RESEARCH_SA07 (cp12), 20 Nov 2026

By Claude Opus 5.5 at effort max, agent a922466087ec53798, resumed by the main session (Claude Opus 5.5 at effort max)
for this intake, following `field_experts/intake_20261120/INTAKE_BRIEF.md`. I built the prompt RESEARCH_SA07 (19 Nov
2026) and checked 8.5.7 for SA15; Lead A of the prompt is mine. The run is GPT-6 Astra (ChatGPT Pro mode).

Status of this document: complete for the scope stated in section 0 (20 Nov 2026).

## 0. What was read

- Return: `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA07_checkpoint_12_20261119T1255Z_unzipped/`
  (checkpoint 12, 19 Nov 2026 12:55 UTC). Its report opens with INCOMPLETE. Register: `RESEARCH_SA07_results.csv`, 186
  rows (packets 08-10 of the intake: 116 + 57 + 13 rows). Paper: `RESEARCH_SA07_paper.tex` with `sections/*.tex`.
- Scope (updated as the reading goes):
  - read in full, with the proof (27 rows): A.1.1-A.1.3, A.2.1-A.2.7, A.3.1-A.3.4, A.4.1-A.4.9, A.5.1, A.5.3, C.1.1,
    C.3.1; read in part (2 rows): A.5.2, A.5.4. These are the main question (Part A.1-A.2), the elliptic test case of 18:13 up
    to the open gate, the 18:59 reformulation and the two Part C rows most used.
  - read in full later (20 Nov, second pass): F.2.1, with the 18:9 transcription (lines 2-20).
  - read at the level of the statement and the run's status (156 rows): every other row, listed in section 1. Next
    step, not yet done: read them in full in the order of section 5 (the refuted rows first, then E.2.3, E.2.6, E.2.7,
    E.2.9, E.2.16, E.2.22, F.3.24, then the rest).
  - Context: I wrote the prompt (19 Nov) and read the SA07 sweep files and the cote-18 notes for it; the reading above
    is of the cp12 sections themselves.

## 1. Verdicts, row by row

### Part A.1-A.2: the period triangle of 18:11 (the main question), `sections/A_triangle.tex` lines 1-636, read in full

Setting of the run: André's pure motivated motives over `k ⊂ Q̄`, `T_Hdg = gr_F T_DR`; the conjugate motive `c^*M`; the
joint torsor `T = P_{M ⊕ c^*M}` under `J ⊂ G × G` with `N_2 = ker(pr_1)`; the invariant `v = dim N_2 − dim(N_2 ∩ B^−)`,
`0 ≤ v ≤ u`.

- **A.1.1 (typed triangle; `g = l + 2u`, `b = l + u`, `g − b = u`; `Q` a `U′`-torsor; `Big → Fil` a torsor under the
  relative unipotent radical).** Targeted proof check, confirmed. The dimension identities use only that the
  motivated group is reductive (André's category is semisimple), so the nonzero weights of the Hodge cocharacter on
  `Lie G` pair off. Consequence for the page: his `dim Fil = g − b` equals `u`, so his `trdeg Q(φ) = g − b` is the
  value `u`.
- **A.1.2 (the two descriptions of `Q`, P11 [I]; the margin arrow, P13 [I]; the denominator, P17 [I]).** Confirmed.
  `Q_H` (allowing `gr(s)` in the central torus `T_0`) is an `H′`-torsor of dimension `u + 1` with `Q` the fibre over 1;
  no `G`-equivariant section `G/B → G/L` exists unless `u = 0` (a `B`-fixed point of `B/L` forces `U = 1`), and for
  `GL_2` no section at all (every self-map of `P¹` has a fixed point). The uppercase reading `K` of P17 is degenerate.
- **A.1.3 (`(2iπ)^n ∈ k(α)` when `Q(−n)` is in the category of `M`).** Confirmed (direct).
- **A.2.1 (base extension to `Q̄` keeps `G^0`, `g, b, l, u` and every transcendence degree; the conjugate comparison
  `α_c j_B = j_dR α κ_V`).** Confirmed. The identity-component statement is the standard one (the motivated group over
  `k` contains the group over `Q̄` with finite quotient); the run's argument is a sketch of that and is correct. The
  joint-torsor construction (A.2.1b-d) and `K ⊂ k(α)·c(k(α))` (this is H2's inclusion) are correct.
- **A.2.2 (the six image dimensions: `α: g`, `β: u`, `γ: b + v`, `φ: u`, `ψ: u + v`, `(α, β): g + v`; the joint image
  is `Q × Γ`).** Independent re-derivation of the fibre dimensions, confirmed: `dim J = g + n`; the stabilizer of the
  flag pair is `B_J = J ∩ (B × B^−)` of dimension `b + n_B` (its first projection is onto `B^0`, kernel `N_2 ∩ B^−`); the
  `γ`-fibres are `S_γ = J ∩ (U × B^−)`-cosets of dimension `u + n_B`, the `(α, β)`-fibres `S_K = J ∩ (1 × B^−)`-cosets of
  dimension `n_B`. Check of the formula on two cases: a real model gives `J` a graph, `v = 0`; a curve `E` not isogenous
  to its conjugate gives `N_2 = SL_2`, `N_2 ∩ B^−` a Borel of `SL_2`, `v = 1 = u`.
- **A.2.3 (the image fills `P × Q` iff `v = u`, iff the Hodge cocharacter is central on `(G/N_2)^0`).** Confirmed.
- **A.2.4 (unconditional upper bounds = the table; equality under `PG_mot(M ⊕ c^*M)`; the relative degrees
  `K/k(α) ≤ v`, `K/k(β) ≤ b + v`, `K/k(γ) ≤ u` for the actual point).** Confirmed. The passage from Bost-Charles,
  Conjecture 2.12, to `PG_mot` is stated with their locators (Definitions 2.4, 2.9, Corollary 2.11, Propositions 2.13-2.14;
  not re-opened by me). The comparison with his list is exact: `α` and `φ` follow from `PG(M)`; `β = u` and
  `K/k(γ) = u` hold for every `v`; his values for `γ`, `ψ`, `K`, `K/k(α)` and `K/k(β)` need `v = u` and are false,
  unconditionally, whenever `v < u`. Lower bounds from `PG(M)` alone: `trdeg k(β) ≥ u − v`, `trdeg k(γ) ≥ b`.
  Run status "Proved" is right for what is stated; the general unconditional exact values remain open, as the report
  says (the row is listed as open in the sort only through that remark).
- **A.2.5 (real models: `φ̄ = f_∞ φ`, `F^opp = α f_∞ α^{−1} F`, `Q(ψ) = Q(φ)`, `K = k(α)`, `v = 0`; corrected tuple
  `(g, u, b, u, u, g; 0, b, u)` from `PG(M)`).** Confirmed; this is Lead A of the prompt (mine), proved by the run with
  the remark I had also made that `f_∞` need only normalize the motivic group after a nonreal extension.
- **A.2.6 (explicit refutation: `E: y² = x³ − x + 1` over `Q`, `M = h¹(E)`).** Independent recomputation, confirmed:
  discriminant `−16·23 = −368`, `j = −6912/23` (not integral, so no CM), `G = GL_2`; with `f_∞ = diag(1, −1)` and
  `F¹ = C e_1`, `β = [[1, −(ad+bc)/(2cd)], [0, 1]]`, `βA = [[δ/(2d), −δ/(2c)], [c, d]]`,
  `γ = [[d/δ, 1/(2c)], [−c/δ, 1/(2d)]]`, and `γ_11 γ_22 + γ_12 γ_21 = 0`, so `trdeg Q(γ) ≤ 3 < 4`. His five excessive
  values are false for this motive, unconditionally. The run's reading of Lead H2 (the implication from joint
  genericity is proved; "conjugate periods always add `u`" is refuted; the literal arithmetic equivalence left open) is
  right.
- **A.2.7 (every established `PG_mot(M ⊕ c^*M)` gives the nine equalities; CM tuple `(2, 0, 2, 0, 0, 2; 0, 2, 0)`).**
  Confirmed (a transfer).


### Part A.3-A.4 (first part): elliptic curves, `sections/A_elliptic.tex` lines 1-300, read in full

Conventions of the run (lines 1-55): `y² = 4x³ − g_2 x − g_3`, `ω = dx/y`, `ξ = x dx/y`, full periods, `η_i` the
quasi-periods with the periods of `ξ` equal to `−η_i`, Legendre `η_1 ω_2 − η_2 ω_1 = 2πi`; Katz's `S(E, ω) = −12h`.

- **A.4.1 (`h = (η_1 ω̄_2 − η_2 ω̄_1)/(ω_1 ω̄_2 − ω_2 ω̄_1) = η_1/ω_1 − π/(ω_1² Im τ) = (π²/(3ω_1²)) E_2^*(τ)`; change of
  adapted algebraic basis `h′ = (sh − t)/r`).** Independent recomputation, confirmed (solving `aω_i − bη_i = ω̄_i` with
  determinant `2πi`; `b = −A/π`; `η_1 ω_1 = π² E_2(τ)/3` for full periods).
- **A.3.1 (`Q(φ) = Q(τ)`, `Q(ψ) = Q(τ, τ̄)`; trdeg of `Q(φ)` is 0 with CM and 1 without, by Schneider 1937).**
  Confirmed. Schneider's locator (§1, result IIc, p. 5) not reopened by me.
- **A.3.2 (a curve isogenous to its conjugate has `τ̄ ∈ Q(τ)` and `h ∈ Q̄(ω_1, ω_2, η_1, η_2)`; this covers every real
  model).** Confirmed. This is the case `v = 0` of A.2.2 for elliptic curves.
- **A.3.3 (`E_7/Q(i): Y² = X³ + 2X² + (1/2 + i)X`: non-CM, no real model, isogenous to its conjugate).** Independent
  recomputation, confirmed: the 2-isogeny with kernel `(0, 0)` has target `Y² = X³ − 4X² + (2 − 4i)X`, which is the
  conjugate scaled by `u² = −2`; `j(E_7) = (−56512 + 38144i)/25`, norm `929714176/125`, not integral, so no CM. So
  `v = 0` occurs without a real model, and the "no real model" reading of Lead A is too narrow: the right condition is
  `E ~ c^*E` (A.2.5's remark).
- **A.3.4 (`E_8/Q(i)` with `j_0 = 1/(2+i)`: non-CM, no real model, not isogenous to its conjugate).** Confirmed: at
  `v = (2 + i)`, `v(j_0) = −1` and `v(j̄_0) = 0`; a cyclic `N`-isogeny would give `Φ_N(j_0, j̄_0) = 0` with `Φ_N` monic over
  `Z`, forcing `v(j_0) ≥ 0`. The gate after A.3 (algebraic independence of `τ, τ̄` for such a curve) is open, as the run
  says; `1 ≤ trdeg Q(τ, τ̄) ≤ 2`.
- **A.4.2 (CM: `h ∈ k`; the eigenvalue argument `h = a/(ū − u)`, then Masser's Theorem A1 for descent to `k`).**
  Targeted check of the eigenvalue argument, confirmed; Masser's Appendix One locators not reopened by me.
- **A.4.3 (CM period field `L = Q̄(ω_1, π)`, trdeg 2, with Chudnovsky 1978, §2A, Theorem 1).** Confirmed (the field
  identities from A.4.1 and Legendre; the transcendence input is the cited theorem, whose locator agrees with our
  `LITERATURE_CHECK.tsv` entry for Chudnovsky, ICM Helsinki 1978).
- **A.4.4 (`y² = 4x³ − 30x − 28`, `j = 8000`, CM by `Q(√−2)`, `h = 1/2`).** Confirmed by two independent routes in the
  run (explicit degree-2 endomorphism; Masser's table `Ψ(i√2) = 15/28`, `(28/30)(15/28) = 1/2`); I rechecked
  `Δ = 27000 − 21168 = 5832` and `j = 8000`, and the agreement of the two routes.
- **A.4.5 (Masser's explicit CM formula, `h = (g_3/g_2)Ψ`, with the exceptional case and the two transcription hazards in
  Spence 2018).** Carried as background without fault found (the derivation is a normalization of Masser's (100)-(106);
  locators not reopened by me).
- **A.4.6 (`h = 0` iff `j ∈ {0, 1728}`, in the fixed short-Weierstrass basis).** Independent check of the estimates,
  confirmed: on `0 < x < 1/2` the first Fourier term dominates `Im E_2` (`S_3(r)/r < 2` for `r < 1/200`); on `x = 0` and
  `x = 1/2` the function is strictly increasing (on `x = 1/2`: `y² d/dy ≥ 3/π − 36π S_3(e^{−π√3}) > 3/π − π/5 > 0`).
- **A.4.7 (isogeny transport `h_{E′} = (n/λ²) h_E − a/λ`; algebraicity of `h` is an isogeny invariant).** Confirmed.
- **A.4.8 (`h` algebraic iff `χ^*(τ) = 1728 E_2^* E_4 E_6/(E_4³ − E_6²)` algebraic, for `j ≠ 0, 1728`).** Confirmed.


### A.4.9 and Part A.5, `sections/A_generation.tex` lines 1-175 read in full, the rest of A.5.3-A.5.4 in part

- **A.4.9 (his 18:13 b, "A-t-on H = G ?": for every elliptic curve over `Q̄` the smallest algebraic subgroup containing a
  translate of the period locus is the whole motivic group, `GL_2` or `Res_{K/Q} G_m`).** The translation is checked and
  confirmed (the generated subtorsor is `z_0 H`, independent of `z_0`; `h(E)` and `h¹(E)` generate the same category;
  the direction of Bost-Charles's comparison is inverted correctly). The input is Kreutz-Shen-Vial, "De Rham-Betti
  classes with coefficients", arXiv:2206.08618v3 (2026), Proposition 3.1 and Theorem 5.13(ii), with Proposition 5.14:
  carried as background without fault found; I have not opened KSV. This settles his question b) in the affirmative;
  it is the de Rham-Betti (not the full period) statement, as the run says.
- **A.5.1 (the image of the cocycle `φ_p(σ) = (σp)^{−1} p` of `Aut(C/F)` is Zariski dense iff `p` is generic over `F`;
  its closure is `D_p(Z_F(p)_C)`, of dimension `trdeg_F F(p)`).** Targeted proof check, confirmed (it rests on
  `C^{Aut(C/F)} = F` and the density of the `Aut(C/F)`-orbit in the `F`-locus). This proves his reformulation on 18:59
  (P17 [II]) in its literal "image" reading.
- **A.5.2 (the image and the subgroup it generates have different closures).** Proved counterexample, statement read;
  consistent with the `G_m` test of P26 [II].
- **A.5.3 (right cocycle law, inversion to a left cocycle, the semidirect-product homomorphism).** Confirmed (direct
  composition; this is P15 and P20 [II]).
- **A.5.4 (a genuine motivic counterexample over a transcendental field of definition: `E_0: y² = x³ − x` and an
  augmented degree-one motive; the 18:59 genericity fails for some finitely generated bases even with π transcendental
  over the base).** Read in part (the construction and the use of Chudnovsky through A.4.3); not read in full. It
  concerns non-algebraic bases only and does not touch Bost-Charles's arithmetic conjecture, as the run says.


### Part C, the rows read in full: `sections/C.tex` lines 3-19 and 138-151

- **C.1.1 (the real Hodge realization `M ↦ (H_B(M), f_∞)` on the motives for absolute Hodge cycles over `R` generated by
  abelian varieties and Artin motives is fully faithful; the image of `h¹` is every pair of type `{(1,0), (0,1)}`).**
  Targeted proof check, confirmed: full faithfulness is Deligne's theorem (absolute Hodge on abelian varieties, cited
  as Charles-Schnell Theorem 58) plus Galois descent; for the essential image, `E(x, y) = E_0(x, y) − E_0(fx, fy)` is
  a Riemann form with `f^*E = −E` (positivity because `fJ = −Jf`), so the torus with its antiholomorphic involution is
  an abelian variety over `R`. This settles his 18:34 sentence "pleinement fidèle en vertu des conj. de Hodge" in the
  abelian case unconditionally; for Grothendieck's motives it is C.1.2, under the Hodge conjecture.
- **C.3.1 (refuted: "f_∞ = 1 seulement si M est somme de puissances tensorielles de Q(2)", 18:36-38; the correct class is
  the sums of `L^{⊗p}`, `L = A ⊗ Q(−1)`, `A` the sign Artin motive).** Independent re-proof, confirmed: `f = 1` forces type
  `(p, p)`; over `C` such a summand is a sum of `Q(−p)`; descent makes the multiplicity space a `Z/2`-representation on
  which `f_∞` acts by `(−1)^p` times the character, so `f_∞ = 1` forces `A^{⊗p}`. The concrete example
  (`P¹_C` as an `R`-scheme, `f_∞ = −d` on `H²`) is correct. This confirms RH10 [II] and corrects the direction of our R2
  that sweep 3 left unchecked.


### F.2.1 and the 18:9 conflict, read in full (`sections/F.tex` lines 128-146; the transcription `MPL_15_195-228+18_002-017_18_scan009.tex`, lines 2-20)

- **F.2.1 (`W_i(E(n)) = W_{i+2n}(E)`, `F^a(E(n)) = F^{a+n}(E)`, hence `Gr^W_i(E(n)) = (Gr^W_{i+2n} E)(n)`; the unshifted
  formula is refuted by `E = Q(0)`, `i = 0`).** Targeted proof check, confirmed. `Q(−1)` has weight 2, so
  `Gr^W_0(Q(−1)) = 0`, while `(Gr^W_0 Q(0))(−1) = Q(−1) ≠ 0`.
- **The conflict with our sweep-3 R5 is settled: both are right, about different lines of 18:9.**
  - The definitions agree with Deligne, Hodge II (2.1.13), which is what our check event at 18:9 tested:
    - line 20 of the transcription is `W_i(E(n)) = W_{i+2n}(E)`;
    - line 8 is `W_i(E(−1)) = W_{i ∓ 2}(E)`, where the transcription leaves the sign open (`\unsure{−|+}`); line 20
      decides it as `−`.
  - The graded formula on line 14, as transcribed, `W_i(E(−1))/W_{i−1}(E(−1)) ≃ [W_i(E)/W_{i−1}(E)](−1)`, is false: its
    two sides have weights `i` and `i + 2`. The correct form is `≃ [W_{i−2}(E)/W_{i−3}(E)](−1)`. This is F.2.1, and
    P09 [I] said the same.
  - Our R5 and `STUDY.md` §5 ("agrees") hold for lines 8 and 20 and fail for line 14. The sweep-3 check event at 18:9
    should be refined accordingly.
  - Whether the slip on line 14 is his or a misreading of the subscripts is a reading question for the scan. The
    transcription marks no doubt on those indices; P09 [I] calls the line frozen.

### Every other row: read at the level of the statement

For each row below I read the statement and the run's status, and nothing of the proof unless a note says so. The
verdict for each is: not read in full (statement and run status read). The run's own status is given as it stands.

| Row | Run status | Statement (title) | Place |
|---|---|---|---|
| A.3.5 | Proved | Rational-function relations and the symmetric residual equation | `A_tau.tex:3` |
| A.3.6 | Proved reductions | The exact product-period quotient and tensor relation | `A_tau.tex:29` |
| A.4.10 | Proved | A coefficient that detects the Hodge splitting | `A_elliptic.tex:371` |
| A.4.11 | Proved | The projector and the rank-three tensor of the splitting | `A_elliptic.tex:421` |
| A.4.12 | Proved | The actual algebraic-splitting hypersurface generates $\mathrm{GL}_2$ | `A_elliptic.tex:455` |
| A.4.13 | Proved | Exact applicability of the functional theorem to a single splitting value | `A_elliptic.tex:480` |
| A.4.14 | Proved | The exact unitary lift in the universal vector extension | `A_elliptic.tex:513` |
| A.4.15 | Proved | The restricted-Lie test for an algebraic splitting line | `A_elliptic.tex:550` |
| A.4.16 | Proved | Torsion lifts and the exact horizontal-lift test | `A_elliptic.tex:578` |
| A.4.17 | Proved | An algebraic compact point on the explicit non-CM curve | `A_elliptic.tex:613` |
| A.4.18 | Proved | The exact de Rham Hodge endomorphism algebra | `A_elliptic.tex:631` |
| A.4.19 | Proved | Crystalline tests of the same projector, with coefficient fields retained | `A_elliptic.tex:673` |
| A.4.20 | Proved | The Frobenius condition at one good place | `A_elliptic.tex:711` |
| A.4.21 | Proved | An explicit ordinary Hodge--Tate base change | `A_elliptic.tex:746` |
| A.4.22 | Proved | The exact denominator condition for an ordinary correction | `A_elliptic.tex:776` |
| A.4.23 | Proved | The geometric mock-form coefficient is the same splitting scalar | `A_elliptic.tex:836` |
| A.4.24 | Proved | The weight-two overconvergent criterion and its exact remaining equation | `A_elliptic.tex:882` |
| A.4.25 | Proved | The exact defect between the complex and ordinary differential operators | `A_elliptic.tex:931` |
| A.4.26 | Proved | The reduced theta coefficient field and its torsion translations | `A_elliptic.tex:963` |
| A.4.27 | Proved | The exact G-function input for the elliptic primitive | `A_elliptic.tex:1017` |
| A.4.28 | Proved | Horizontal Hodge jets and an explicit CM denominator obstruction | `A_elliptic.tex:1051` |
| A.4.29 | Proved | Division-polynomial data preserve the Gaussian parameter ambiguity | `A_elliptic.tex:1105` |
| A.4.30 | Proved | The Hodge parameter uniquely minimizes the quadratic growth type | `A_elliptic.tex:1130` |
| A.4.31 | Proved | The corrected elliptic vector field at every good prime | `A_elliptic.tex:1203` |
| A.4.32 | Proved | A density bound for the explicit restricted-Lie congruences | `A_elliptic.tex:1333` |
| A.4.33 | Proved | The conjugate elliptic quotient and its differential scalar | `A_elliptic.tex:1502` |
| A.4.34 | Proved | The exact quotient lattice and its CM case | `A_elliptic.tex:1631` |
| A.4.35 | Proved | Raw second-kind lattice invariants | `A_elliptic.tex:1758` |
| A.4.36 | Proved | Symmetric-square tensor and conjugate-extension map | `A_elliptic.tex:1847` |
| A.4.37 | Proved | Integral tangent, isogeny law, and branch denominators | `A_elliptic.tex:1968` |
| A.4.38 | Proved | Arithmetic rank of the conjugate quotient graph | `A_elliptic.tex:2152` |
| A.4.39 | Proved | Two normalized jets of the period product | `A_elliptic.tex:2261` |
| A.4.40 | Proved | Exact local sizes and arithmetic type of the invariant leaf | `A_elliptic.tex:2396` |
| B.1.1 | Proved | The generic-fibre Tate functor | `B.tex:32` |
| B.1.2 | Proved | Good and potentially good reduction; all primes | `B.tex:82` |
| B.1.3 | Refuted | The different-prime and equal-characteristic readings | `B.tex:133` |
| B.1.4 | Proved | Descriptions $2'$ and $3'$ and their Hom spaces | `B.tex:156` |
| B.1.5 | Proved | Description $6'$: the exact admissible category | `B.tex:107` |
| B.2.1 | Proved | The period-ring pair and reconstruction | `B.tex:195` |
| B.2.2 | Proved | Geometric and relative comparisons | `B.tex:335` |
| B.2.3 | Proved within the stated scope | Integral lattices, torsion and the prismatic classification | `B.tex:389` |
| B.3.1 | Proved and literal unscaled equality refuted | Problem 1a: the two meanings of lattices | `B.tex:440` |
| B.3.2 | Proved | Problem 1c: real structures and the splitting | `B.tex:468` |
| B.3.3 | Proved within the specified readings | Problem 3: the precise local comparison inputs | `B.tex:500` |
| B.3.4 | Proved within each stated scope | Problem 4: characteristic-$p$ cohomology and the requested structures | `B.tex:153` |
| B.4.1 | Proved | Compatibility and the exact cocycle | `B.tex:591` |
| B.4.2 | Proved | The kernel identity and descent of $\chi$ | `B.tex:639` |
| B.4.3 | Proved within the named scope | Analyticity and the precise relation to Sen | `B.tex:673` |
| B.4.4 | Refuted | An Artin--Tate proalgebraic counterexample with both splittings | `B.tex:742` |
| C.1.2 | Proved under stated hypotheses | The homological-motive version and its scope | `C.tex:20` |
| C.1.3 | Proved | Generation by the identity component and real Frobenius | `C.tex:27` |
| C.1.4 | Proved | An explicit polarized pair outside the abelian image | `C_image.tex:1` |
| C.1.5 | Proved | A fully specified polarized pair outside the geometric image | `C_image.tex:32` |
| C.2.1 | Proved | Tensor structure and the exact torsor | `C.tex:99` |
| C.2.2 | Proved | Artin, Tate and elliptic tests | `C.tex:123` |
| C.3.2 | Proved | Reality of the comparison point and of its torsor | `C.tex:152` |
| C.3.3 | Proved in the stated categories | Central real Frobenius | `C.tex:165` |
| C.4.1 | Proved | Fixed-topology transport and the scalar fields on 18:41 | `C.tex:176` |
| C.4.2 | Proved | The Hodge splitting over the real coefficient field | `C.tex:211` |
| C.5.1 | Proved | The positive Weil form | `C.tex:191` |
| D.1.1 | Proved | The three finite coefficient rings and the Betti lattice map | `D.tex:3` |
| D.1.2 | Proved bound | Exact quotient and the dimension bound of 18:47--49 | `D.tex:93` |
| D.2.1 | Source gate | The field \texttt{K} and Lead H5 | `D.tex:175` |
| D.3.1 | Proved | The compact-open genericity lemma, including joint genericity | `D.tex:167` |
| D.3.2 | Known inputs | Unconditional elliptic products: exact theorem inputs | `D.tex:167` |
| D.4.1 | Known criterion | Which connected affine groups have the approximation property? | `D.tex:399` |
| D.4.2 | Proved equivalence and counterexamples | The equivalence in the margin: two precise readings | `D.tex:471` |
| D.5.1 | Proved | The cocycle, its descent, and change of place | `D.tex:546` |
| D.5.2 | Proved counterexample | A CM counterexample to the integral comparison on 18:55 | `D.tex:636` |
| D.5.3 | Universal assertion refuted | Euclidean closure, the openness expectation, and a Tate counterexample | `D.tex:688` |
| D.5.4 | Necessity proved | The unfinished qualification involving pi | `D.tex:775` |
| D.6.1 | Scope recorded | Scope of the remaining place-recovery question | `D.tex:812` |
| E.1.1 | Proved | Finite diagrams and finitely generated fields | `E.tex:5` |
| E.1.2 | Refuted | The universal countable integral assertion | `E.tex:16` |
| E.1.3 | Refuted | The path-limit step and its completed reading | `E.tex:67` |
| E.1.4 | Proved | Uncountable fields: both behaviours occur | `E.tex:81` |
| E.2.1 | Refuted | One pair of distinct places defeats every plain integral test | `E.tex:124` |
| E.2.2 | Proved | One labelled CM elliptic curve separates the places of its ring class field | `E_numberfield.tex:3` |
| E.2.3 | Proved | Descent of a finite separating diagram and the exact transporter | `E_numberfield.tex:57` |
| E.2.4 | Proved | Generalized-dihedral fields covered by the finite CM test | `E_numberfield.tex:124` |
| E.2.5 | Proved | A finite polarized CM test for every totally real field | `E_numberfield.tex:173` |
| E.2.6 | Proved, with the stated CM scope | A global integral CM comparison for two quartic places | `E_numberfield.tex:267` |
| E.2.7 | Proved | Labelled real Frobenius separates every real embedding | `E_numberfield.tex:270` |
| E.2.8 | Proved | A finite comparison skeleton in one fixed-field isogeny class | `E_numberfield.tex:402` |
| E.2.9 | Proved necessary condition | Geometric cyclic quotients impose projective Tate compatibility over a fixed number field | `E_numberfield.tex:463` |
| E.2.10 | Proved algebraic-group counterexample | Finite congruence solvability does not supply a simultaneous rational lift | `E_numberfield.tex:583` |
| E.2.11 | Proved auxiliary result | The prescribed CM comparison has real and rational abelian lifts | `E_abelian_lift.tex:1` |
| E.2.12 | Proved with explicit lattice hypotheses | Finite equations give a comparison in an admissibly generated integral category | `E_admissible_isom.tex:1` |
| E.2.13 | Proved | A fixed-\(\Q\) elliptic quotient outside the admissible closure | `E_lattice_obstruction.tex:3` |
| E.2.14 | Proved | The common scalar and uniqueness in the prescribed CM fibre | `E_lattice_obstruction.tex:128` |
| E.2.15 | Proved | The Artin kernel and the uniform CM-field restriction | `E_integral_image.tex:21` |
| E.2.16 | Proved | An exact lattice criterion for the abelian integral image | `E_integral_image.tex:92` |
| E.2.17 | Proved | An explicit excluded Galois element with the quartic swap | `E_integral_image.tex:191` |
| E.2.18 | Proved | The abelian image for all remaining Galois candidates | `E_integral_image.tex:370` |
| E.2.19 | Proved | Ring-class restrictions and a fixed-field local-sign example | `E_integral_image.tex:519` |
| E.2.20 | Proved | Two CM types eliminate the local-sign ambiguity | `E_integral_image.tex:510` |
| E.2.21 | Proved | The exact Artin image of the full plain integral CM diagram | `E_integral_image.tex:512` |
| E.2.22 | Proved | An exact reduction to one tower of covers | `E_integral_image.tex:1093` |
| E.2.23 | Proved | One integral comparison for all rational elliptic isogeny classes | `E_integral_image.tex:1290` |
| E.2.24 | Proved | One integral comparison for all elliptic and CM geometric factors | `E_integral_image.tex:1554` |
| E.2.25 | Proved | One integral comparison for all surface and CM geometric factors | `E_integral_image.tex:1865` |
| E.2.26 | Proved | One integral comparison for all threefold and CM geometric factors | `E_integral_image.tex:2490` |
| E.2.27 | Proved | A profinite loop with integral classes on every finite cover | `E_integral_image.tex:3190` |
| E.2.28 | Proved | The completion preserved by all affine integral homology maps | `E_integral_image.tex:3437` |
| E.2.29 | Proved one-cover counterexample | An integral IA lift that moves actual boundary homology | `E_integral_image.tex:3813` |
| E.2.30 | Proved | The embedded completion determined by all proper cover lattices | `E_integral_image.tex:4187` |
| E.2.31 | Proved | An explicit cusp conjugator outside the proper completion | `E_integral_image.tex:4503` |
| E.3.1 | Proved | The labelled integral elliptic test | `E.tex:96` |
| E.3.2 | Proved | Failure of a universal single object in finite transcendence degree | `E.tex:115` |
| E.3.3 | Refuted for the explicitly specified enriched target | Riemann--Hodge conditions do not characterize geometric places | `E.tex:142` |
| E.3.4 | Proved counterexample in the specified target | Including all complex motives does not restore the proposed surjectivity | `E.tex:190` |
| F.1.1 | Proved | The global cycle comparison, including singular cycles | `F.tex:5` |
| F.1.2 | Proved | Proper direct image and every cohomological degree | `F.tex:32` |
| F.1.3 | Proved | Correspondences, twists and the cancellation on 18:25 | `F.tex:61` |
| F.1.4 | Proved | An unchosen complex isomorphism and its exact lattice dependence | `F.tex:80` |
| F.1.5 | Proved exact image | The two readings of ``primitifs'' on 18:29 | `F.tex:100` |
| F.1.6 | Proved | Real descent of the diagonal integral lattice | `F.tex:112` |
| F.2.1 | Proved | The corrected weight-graded twist | `F.tex:130` |
| F.3.1 | Known | Oda's comparison and the characteristic-$p$ Hodge extension | `F_audit.tex:7` |
| F.3.2 | Proved | The rational Lefschetz operator images and an integral counterexample | `F_audit.tex:23` |
| F.3.3 | Proved | Weight, Cartan and filtration gradings with their comparison maps | `F_audit.tex:64` |
| F.3.4 | Known | Reconstruction and the specified modern motivic comparisons | `F_audit.tex:86` |
| F.3.5 | Known and proved as specified | Numerical quotient, centres and central Tate extension data | `F_audit.tex:113` |
| F.3.6 | Known and proved as specified | The actual maps relating the anabelian and linear statements | `F_audit.tex:160` |
| F.3.7 | Refuted and proved as specified | Real fixed points and the corrected compact-centralizer assertion | `F_audit.tex:185` |
| F.3.8 | Known | Integral Chow specialization and its integral cycle-class square | `F_audit.tex:202` |
| F.3.9 | Proved correction | The transversal dimension on 18:15 | `F_audit.tex:222` |
| F.3.10 | Proved repair | The complete LM6 character statement and its repair | `F_audit.tex:182` |
| F.3.11 | Refuted | Abstract semilinear actions can fail effective descent | `F_audit.tex:344` |
| F.3.12 | Known theorem | Integral tensor forms and the finite-type finiteness theorem | `F_audit.tex:387` |
| F.3.13 | Proved for the specified exact category | The integral automorphism model of an admissibly generated finite stage | `F_audit.tex:515` |
| F.3.14 | Proved | A precise hypersurface normalization construction | `F_audit.tex:552` |
| F.3.15 | Proved | CM pro-prime normalizers: an independent primary-source proof | `F_audit.tex:182` |
| F.3.16 | Proved | A finite-cover CM Prym and its actual punctured quotient maps | `F_audit.tex:745` |
| F.3.17 | Proved | The precise reach and limitation of this cover tower | `F_audit.tex:848` |
| F.3.18 | Proved | A rank-one Jacobian character gives an actual CM quotient | `F_audit.tex:888` |
| F.3.19 | Proved | An absolutely simple CM surface in a finite-cover Prym | `F_audit.tex:1027` |
| F.3.20 | Proved | Degree-six recognition for every once-punctured elliptic curve | `F_audit.tex:1161` |
| F.3.21 | Proved | Actual genus-two normalizer recognition at nonsplit primes | `F_audit.tex:1417` |
| F.3.22 | Proved | All-prime recognition on the genus-two CM target | `F_audit.tex:1428` |
| F.3.23 | Proved | An actual rational detecting cover and a rational cusp | `F_audit.tex:2059` |
| F.3.24 | Proved | The genus-three universal quotient on balanced tangencies | `F_audit.tex:2244` |
| F.3.25 | Proved | Rational CM endomorphism orbits and genus-three normalizer recognition | `F_audit.tex:2548` |
| F.3.26 | Proved | The universal quotient on full symplectic basis tangencies in every genus | `F_audit.tex:2946` |
| F.3.27 | Proved | All-genus normalizer recognition for a whole absolutely simple Jacobian over Q | `F_audit.tex:3255` |
| F.3.28 | Proved | Two paired tangencies on a proper summand in genus three | `F_audit.tex:3425` |
| F.3.29 | Proved | A single normalizer line in genus three | `F_audit.tex:3650` |
| F.3.30 | Proved parametrization | An exact invariant reduction for the higher-genus single-line problem | `F_audit.tex:4007` |
| F.3.31 | Proved witness map | A full profinite counterexample produces a finite matrix witness | `F_audit.tex:4282` |
| F.3.32 | Proved by an exact polynomial certificate and the actual sub | The all-genus single-line obstruction and the full CM common kernel | `F_audit.tex:5` |
| F.3.33 | Proved from the explicit covering maps and F.3.32 | Full profinite cuspidality on every affine hyperbolic curve over a number field | `F_audit.tex:5` |
| F.3.34 | Proved using the published multiplicity bound and an exact i | An explicit six-vector reconstruction of the Johnson detector | `F_audit.tex:5` |
| F.3.35 | Known source theorem | The fourfold numerical quotient and its actual correspondence scope | `F_audit.tex:5323` |
| F.3.36 | Known source theorem | The characteristic-zero comparison on all abelian tensor motives | `F_audit.tex:5422` |
| G.2.1 | Known | The two printed passages requested in Lead H4 | `G.tex:3` |
| G.2.2 | Refuted | A specialization counterexample and the coefficient condition that repairs it | `G_arithmetic_sources.tex:9` |
| G.2.3 | Primary source checked | The May 1966 written Tate-module question and its exact scope | `G_history_sources.tex:1` |

## 2. What is new

Against our own results (the SA07 sweep-3 files, R1-R6 of the prompt) and against the literature, for the rows read in
full:

- **The main question is decided in its corrected form (A.2.2-A.2.6).** The run introduces the joint comparison torsor
  of `N = M ⊕ c^*M` and one invariant, `v = dim N_2 − dim(N_2 ∩ B^−)` with `0 ≤ v ≤ u`, and proves the complete table of
  image dimensions (`α: g`, `β: u`, `γ: b + v`, `φ: u`, `ψ: u + v`, `K: g + v`, and the relative degrees `v`, `b + v`, `u`).
  These are unconditional upper bounds for the actual points and the exact values under the period conjecture for `N`.
  Grothendieck's "Conj. de transcendance forte" of 18:11 holds conditionally exactly when `v = u`, and five of its values
  are false, unconditionally, whenever `v < u`. Explicit counterexample: `h¹` of `y² = x³ − x + 1` over `Q`.
  - Against sweep 3: our R3 had checked only internal consistency.
  - Against the prompt: Lead A (mine) is proved, and sharpened in three ways. The exact invariant is `v`. `v = 0` holds
    whenever `M ≅ c^*M` over `Q̄`, with or without a real model (A.3.3 gives a curve isogenous to its conjugate with no
    real model). For an elliptic curve not isogenous to its conjugate, `v = u = 1`, so Grothendieck's values are the
    predicted ones.
  - Against the literature: the run claims no priority and cites none for the table. I know of no source that treats
    the transcendence of the Hodge splitting through the conjugate motive in this form. I have not searched for one in
    this intake.
- **The Hodge splitting of an elliptic curve (A.4.1-A.4.8).** These are known results, with exact normalizations and
  checked locators:
  - the formula `h = (π²/(3ω_1²)) E_2^*(τ)`, which is Katz's `S = −12h`;
  - the CM case (Katz's eigenvalue argument, Masser's Theorem A1, the explicit value `h = 1/2` for `j = 8000`);
  - the zero set `j ∈ {0, 1728}` (also Sebbar-Besrour 2026, Lemma 8.1, as the run cites).

  Two parts are new to our programme: the isogeny-transport law (A.4.7), and the two transcription hazards it records
  in Spence 2018 for Masser's formula. The non-CM question of 18:13 c remains open; A.4.10-A.4.40 are criteria and
  reductions, read only at statement level here.
- **His 18:13 b is answered yes for every elliptic curve over `Q̄` (A.4.9).** This is known: Kreutz-Shen-Vial 2026, the
  de Rham-Betti theorem for elliptic curves, resting on the analytic subgroup theorem and, in the CM case, Chudnovsky.
- **His 18:59 reformulation (A.5.1) is proved in the "image" reading.** The Zariski closure of the image of the
  automorphism cocycle is the transported `F`-locus of the comparison point. The "generated subgroup" reading is refuted
  (A.5.2, and A.5.4 over transcendental bases).
- **Real Frobenius (C.1.1, C.3.1).**
  - The full faithfulness on abelian motives over `R` is Deligne's theorem with descent.
  - The essential-image description of `h¹` by the averaged Riemann form is a short argument that our files did not
    have.
  - The refutation of 18:38, with the exact class `⊕ L^{⊗p}`, confirms RH10 [II] (GPT-6 Astra, ChatGPT Pro mode) and
    corrects our R2, whose converse sweep 3 left unchecked.
- At statement level only: Parts B, D, E, F and G hold many further claims that I have not checked. Among them:
  - the corrected graded twist of 18:9 (F.2.1), which agrees with P09 [I] against our R5;
  - a CM counterexample to the integral comparison of 18:55 (D.5.2);
  - a Tate counterexample to the openness expectation of 18:61 (D.5.3);
  - countable algebraically closed fields on which no plain integral test separates places (E.1.2, E.2.1);
  - a long programme on the integral image of the places, E.2.12-E.2.31;
  - the normalizer-recognition rows F.3.15-F.3.34.

## 3. Implications for the archive and the programme

- **Cote 18, scan 11.** The companion should state 18:11 with the corrected table. For a motive isomorphic to its complex
  conjugate (in particular any motive with a real model) the conjugate periods add nothing: `K = k(α)` and `ψ` is
  rational over `Q(φ)`. His "forte" list is the prediction only when `v = u`. The reading of `T_Hdg` as `gr_F T_DR` and
  of `Q` as the normalized splittings (A.1.1-A.1.2) settles P11 and P13 [I]; P17's uppercase `K` is degenerate.
- **18:13.**
  - a) The CM case is known (degree 2); the non-CM case is the period conjecture itself.
  - b) Yes (A.4.9).
  - c) With CM, `h` is algebraic and computed (A.4.2-A.4.5). Without CM it is open, the run's gate. For a curve
    isogenous to its conjugate, `h` lies in the period field (A.3.2).
- **18:36-38.** The even-Tate sentence is false (C.3.1); the companion should give the class `⊕ (A(−1))^{⊗p}`.
- **18:59.** His reformulation by density of the image is right (A.5.1), and the subgroup reading is wrong (A.5.2).
- **18:9 (settled; see section 1).** The definitions on lines 8 and 20 agree with Hodge II (2.1.13). The graded
  formula on line 14 is off by 2 and should read `Gr^W_i(E(−1)) ≅ (Gr^W_{i−2}E)(−1)` (F.2.1, confirmed; P09 [I]). Our
  R5 and `STUDY.md` §5 should say that the conventions agree and that line 14 has the slip. I have not changed
  `STUDY.md`.
- **The programme.** Part A's main question is settled up to two gates, both hard transcendence problems:
  - the unconditional exact values, in particular `h` for a non-CM curve (A.4c);
  - the algebraic independence of `τ, τ̄` for a curve not isogenous to its conjugate (gate A.3, `1 ≤ trdeg ≤ 2` for
    `E_8`).

  The literal arithmetic equivalence in H2 is also left open. The run ended INCOMPLETE at cp12, and 157 of its 186 rows
  are not yet read in full by anyone.

## 4. Bridges (redone 20 Nov 2026 on the corrected criterion of the brief, step 4)

The earlier "Bridges: none" was wrong: it looked only for rows that use RH or GRH as a hypothesis.

The two inputs, as mathematics:
- **GRH (L. Alpöge, *Remark*, https://alpo.ge/remark.pdf, with the Lean archive).** For a Dirichlet character `χ` and
  `n ∈ Z`, the rank-one Artin-Tate motive `M = [χ] ⊗ Q(n)` over `Q` has `L(M, s) = L(χ, s + n)` and weight `w = −2n`. GRH
  places its nontrivial zeros on `Re s = (w + 1)/2 = 1/2 − n`. By products, the same holds for every Artin-Tate motive
  over `Q` with abelian Artin part, including `ζ_K` for `K/Q` abelian.
- **Purity (Deligne, *La conjecture de Weil* I and II).** At a good prime `p`, Frobenius on the ℓ-adic realization of a
  pure motive of weight `w` has eigenvalues of absolute value `p^{w/2}`. For `[χ] ⊗ Q(n)` this is elementary
  (eigenvalue `χ(p)p^{−n}`). For `H¹` of curves and abelian varieties it is Weil's theorem; beyond that it is Deligne's.

What each group of rows meets, row by row within the group. Rows read only at statement level are marked (s); for them
the bridge is stated from the statement.

- **The real Frobenius on Tate and Artin-Tate motives.**
  - Rows: C.3.1, C.3.2, C.3.3 (s), C.2.2 (s), C.1.1, C.1.2 (s), C.1.4 (s), C.1.5 (s), C.4.2 (s), B.3.2 (s), E.2.7 (s).
  - What the rows give: C.3.1 proves that the Artin-Tate motives over `R` with `f_∞ = 1` are the sums of `(A(−1))^{⊗p}`.
  - The meeting point with GRH: over `Q`, `f_∞` on `[χ] ⊗ Q(n)` is `χ(−1)(−1)^n`. Together with the Hodge type `(−n, −n)`
    it fixes the archimedean factor `L_∞(M, s) = Γ_R(s + n + a)`, where `(−1)^a = χ(−1)`. That factor gives the trivial
    zeros `s = −n − a − 2k`, the zeros that GRH does not place on the line.
  - For `n ≥ 1`, `f_∞ = 1` holds exactly when `L(χ, n)` is critical (`χ(−1) = (−1)^n`). That is the Bernoulli case,
    `L(χ, n) ∈ Q(χ) τ(χ) π^n`. When `f_∞ = −1` the value is non-critical (for example `ζ(2m + 1)`), and it is governed by
    Borel's regulator and the Bloch-Kato formula, a theorem for these motives (Huber-Kings 2003; Burns-Greither 2003).
    `dim M_B^{f_∞ = 1}` is Deligne's `d^+`.
  - What GRH gives there: nothing. It locates zeros and is silent on values at integers.
  - What the rows give back: nothing to GRH, since the Γ-factors of Dirichlet `L`-functions are classical.
  - C.5.1 (the positive Weil form `(2πi)^n q(x, Cy)`) is the archimedean Hodge-Riemann positivity. Its finite-field
    analogue, the Hodge standard conjecture, would imply purity (Grothendieck, Serre). Deligne's proof does not use it,
    and C.5.1 gives nothing in characteristic `p`.
- **Periods and transcendence of Tate and general motives.**
  - Rows: A.1.3, A.2.1, A.2.4-A.2.7, A.3.6 (s), A.4.3, A.4.5, A.4.9, A.4.11 (s), A.4.13 (s), A.4.34 (s), A.5.1, A.5.4,
    D.5.3 (s), D.5.4 (s).
  - The Tate period `2πi` of `Q(−1)` (A.1.3) is the period in the critical values of `ζ` and `L(χ, s)`:
    `ζ(2m) ∈ Q·(2πi)^{2m}`, which is Euler, and Deligne's conjecture for `Q(n)`, which is known.
  - The rows concern the transcendence degree of period points. RH and GRH concern zeros. Neither implies anything
    about the other, so the link carries nothing.
  - The A.4 rows meet special values through `E_2^*`. At CM points its values are Damerell-Shimura-Katz values tied to
    Hecke `L`-values of the imaginary quadratic field (Katz 1976, cited in A.4.2). These are not Dirichlet
    `L`-functions, so Alpöge's theorem does not reach them. RH for them would in any case be silent on values.
- **Artin motives of number fields, places and integral Betti diagrams.**
  - Rows: E.2.1-E.2.6, E.2.10-E.2.14, E.2.18, E.2.22-E.2.24, E.2.26, E.2.27, E.3.2-E.3.4, all (s).
  - E.2.3 uses `A_k = h⁰(Spec k)`, whose `L`-function is `ζ_k`.
  - What GRH gives: RH for `ζ_k` when `k/Q` is abelian (Kronecker-Weber). The ring class fields of E.2.2-E.2.6 are
    generalized dihedral over `Q`. Their `ζ_k` factors into Hecke `L`-functions of ring class characters of an
    imaginary quadratic field, which are dihedral Artin `L`-functions over `Q`, not Dirichlet ones, so Alpöge does not
    cover them.
  - The rows use no zeros; they separate places by integral comparisons, so the link carries nothing either way.
  - In the Artin-Verdier picture (`Spec Z ∪ {∞}` of étale cohomological dimension 3, primes as knots), his "faux, cf
    groupoïde fondamental sur Z" (E.1.2, 15:207) reads as Minkowski's `π_1^ét(Spec Z) = 1`. The real Frobenius is the
    decomposition group at `∞`, and the `f_∞`-invariants of C.3.1 are the local terms at the real place,
    `Ĥ^*(Gal(C/R), Z(n))` (`Z/2` in even degree for `n` even, odd degree for `n` odd). These enter the Lichtenbaum and
    Bloch-Kato special-value formulas, not RH.
  - E.2.22 concerns covers of `P¹ − {0, 1, ∞}`, whose motivic fundamental group is mixed Tate over `Z`
    (Deligne-Goncharov). Its periods are multiple zeta values. GRH says nothing about their transcendence, and the row
    is integral Betti only.
- **Frobenius weights.**
  - Rows: F.3.20, F.3.21, F.3.22, F.3.25, F.3.27, F.3.29; F.3.24, F.3.26; F.3.15, F.3.16, F.3.19, F.3.23, F.3.10, B.4.2,
    B.4.4; all (s).
  - What purity gives: Frobenius on `V_ℓ J` has weight 1 (Weil), while `Q_ℓ(1)` has weight `−2`. So no Galois-stable
    subquotient of `V_ℓ J` is a Tate twist. This is the weight separation that the normalizer-recognition rows use.
  - Hain's weight filtration on `π_1` of a punctured curve has graded pieces pure of weight `−n`, which is Deligne's
    Weil II on `H¹(U)` (weights 1 and 2, the weight-2 part a sum of `Q_ℓ(−1)`). These are the weights F.3.24, F.3.26 and
    F.3.29 use.
  - The rows give back nothing.
  - B.4.4 refutes the analytic-image assertion of 18:6 on an Artin-Tate tower over a local field; no weight enters.
- **Cycles, numerical motives, Hodge weights.**
  - Rows: F.2.1, F.3.3, F.3.4, F.3.5, F.3.6, F.3.8, F.3.11, F.3.35, F.3.36, D.1.1, D.1.2, D.3.1, D.3.2, D.4.1, D.4.2,
    D.5.2; all (s).
  - F.2.1 is weights of mixed Hodge structures (Hodge II), the archimedean counterpart of Deligne's weights. Its graded
    shift `Gr^W_i(E(−1)) = (Gr^W_{i−2}E)(−1)` matches the Frobenius shift of `Q_ℓ(−1)` by 2.
  - D.3.2 uses Serre's open image theorem, which is unconditional. Its effective forms (Serre 1981) use GRH for Dedekind
    zeta functions of non-abelian division fields, which is beyond Alpöge's result. GRH for Dirichlet `L` effectivizes
    only the cyclotomic part.
  - F.3.5, F.3.35 and F.3.36 concern numerical against homological equivalence in characteristic 0. They give nothing
    to purity.

### 4.1 The period bridges, against the steps of Alpöge's note (remark.pdf pp. 2-4: step 3, step 9, step 17, footnote 6)

The note's own text (pp. 2-4) has four relevant places:
- step 3 interprets a quadric "on corresponding CM e.g. C/Z[ω]";
- step 9 uses "proven divisibility via Chowla-Selberg, Weyl, and Siegel mass";
- step 17 works with "the classes in H¹(o_E[1/ℓ], Q/Z(−e)) that we couldn't kill by twisting";
- footnote 6: "vanishing of a number of K-groups of Z follows ... I had Lichtenbaum".

The SA07 rows meet these places as follows.

- **Chowla-Selberg and the CM rows (A.4.2-A.4.6, A.2.7 and A.4.3; E.2.2-E.2.6, E.2.11, E.2.14 (s); F.3.15, F.3.16,
  F.3.19, F.3.23 (s)).**
  - The formula. Let `E` have CM by `O_K`, `K = Q(√−d)`, `χ = χ_{−d}`, `w = |O_K^×|`, `h = h_K`. Then
    `ω_1 ∈ Q̄^× · π^{−1/2} · ∏_{a=1}^{d−1} Γ(a/d)^{wχ(a)/(4h)}`.
  - What it does to A.4.3. A.4.3 proves `L = Q̄(ω_1, ω_2, η_1, η_2) = Q̄(ω_1, π)` with transcendence degree 2. With the
    formula, `L = Q̄(π, ∏ Γ(a/d)^{wχ(a)/(4h)})`, and Chudnovsky's theorem as used in A.4.3 becomes the algebraic
    independence of `π` and that Γ-product.
  - Examples:
    - `y² = x³ − x` (F.3.15 and the other F.3 rows, `K = Q(i)`): the product is `Γ(1/4)²`.
    - `C/Z[ω]` of step 3 (`j = 0`, `K = Q(√−3)`): it is `Γ(1/3)³`. There A.4.6 gives `h = 0` in the short-Weierstrass basis,
      so by A.4.1 `η_1 = π/(ω_1 Im τ)`, and the whole period matrix lies in `Q̄[π^{±1}, ω_1^{±1}]` with
      `ω_1 ∼ Γ(1/3)³/π`.
    - The curve of A.4.4 (`j = 8000`, `K = Q(√−2)`, `d = 8`): it is `(Γ(1/8)Γ(3/8)/(Γ(5/8)Γ(7/8)))^{1/2}`.
  - What the rows give back. The splitting scalar is algebraic and computed (A.4.2, A.4.4, A.4.5), so in the CM case the
    quasi-period `η_1` is `Q̄`-linear in `ω_1` and `π/ω_1`. That is the exact algebraic part of the "periods of
    thetas" that steps 3 and 9 use.
- **The size of the CM period, where GRH enters.**
  - Through Lerch's formula, Chowla-Selberg is the statement that `log` of the CM period is `−(w/(4h)) L′(χ, 0)/L(χ, 0)`
    up to logarithms of algebraic numbers and of `π`. In Colmez's height form (my recollection of Deligne's
    normalization, not reopened), the Faltings height of `E` is
    `h_Fal(E) = (1/4) log d + (1/2) L′(χ, 1)/L(χ, 1) − (1/2)(log 2π + γ)`.
  - What GRH gives there (Alpöge). With no exceptional zero, `|L′(χ, 1)/L(χ, 1)| ≤ (2 + o(1)) log log d` (the GRH bound
    of Ihara-Murty-Shimura for logarithmic derivatives at `s = 1`, as I recall it; not reopened). Hence
    `h_Fal(E) = (1/4) log d + O(log log d)` for every CM elliptic curve, an effective size for the CM periods of SA07's
    test cases. Without GRH, a Siegel zero `β` would add a term of size `1/(1 − β)`.
  - The rows give back nothing to GRH: their CM statements are exact algebraic identities between periods, not sizes.
- **Colmez (CM abelian varieties).**
  - Colmez's formula expresses the Faltings height of a CM abelian variety through `L′/L(χ, 0)` of the characters of
    its CM type. He proved it for abelian CM fields, where these are Dirichlet `L`-functions.
  - The genus-two Jacobian of `y² = 1 − x⁵` in F.3.21 and F.3.22 (s) has CM by the abelian field `Q(ζ_5)`. So its height
    is a sum of `L′/L(χ, 0)` over odd characters mod 5, and by Lerch a sum of `log Γ(a/5)`. Its periods are Beta values
    `B(a/5, b/5)`, the Gross-Deligne case.
  - What GRH gives there (Alpöge): the same `O(log log)` control for each Dirichlet factor.
  - What the rows give back: F.3.21-F.3.22 use this Jacobian for normalizer recognition and use no height or period
    size, so they give back nothing.
  - For CM abelian varieties in general, the period conjecture stays open (R6 of the prompt). Colmez concerns heights,
    not transcendence, so the gap is not closed.
- **Ihara, step 17 and footnote 6 (twisted Tate classes and K-groups of `Z`).** Rows: E.2.22, E.2.27-E.2.31, F.3.33,
  F.3.34 (s): covers and profinite loops of `P¹ − {0, 1, ∞}`, integral homology of covers, cuspidality.
  - These are the Betti fibre of the motivic fundamental group of `P¹ − {0, 1, ∞}`, which is mixed Tate over `Z`
    (Deligne-Goncharov).
  - Its ℓ-adic realization carries Ihara's Galois action. Its abelianized graded pieces give the Soulé characters
    `κ_m ∈ H¹(Z[1/ℓ], Z_ℓ(m))`, `m ≥ 3` odd. Those are nonzero (Soulé; Deligne-Ihara), and their rank 1 matches
    `K_{2m−1}(Z)` (Borel).
  - The torsion is `H²(Z[1/ℓ], Z_ℓ(m)) ≅ K_{2m−2}(Z) ⊗ Z_ℓ` (Quillen-Lichtenbaum, by Rost-Voevodsky). Its order is the
    `ℓ`-part of `ζ(1 − m)` up to 2 (Lichtenbaum, by the main conjecture). Vandiver for `ℓ` is equivalent to
    `K_{4n}(Z) ⊗ Z_ℓ = 0` for all `n` (Kurihara, Soulé).
  - Step 17 and footnote 6 are exactly these groups: classes in `H¹(o_E[1/ℓ], Q_ℓ/Z_ℓ(−e))` and the vanishing of some
    `K`-groups of `Z`. What they give there: integral information on the ℓ-adic image of Galois in
    `Aut(π_1^{(ℓ)}(P¹ − {0, 1, ∞}))`. Where the relevant `H²` vanishes, the `κ_m` are surjective onto `Z_ℓ(m)`, and the
    Lie algebra of the image is integrally as large as its rational generators allow (the Ihara-Sharifi question).
  - What the rows give: E.2.22-E.2.31 work only with the topological fundamental group and integral homology of covers,
    with no Galois coefficients. They neither use nor give the Galois-side statement. The link is that the same mixed
    Tate motive carries both: the rows' integral Betti structure, and Alpöge's integral ℓ-adic structure.
- **`A(−1)` and `Q(2)` (C.3.1) against the special values.** The classes of C.3.1 are the archimedean data of the motives
  `[χ](n)` whose values footnote 6 controls through Lichtenbaum: `f_∞ = χ(−1)(−1)^n`, and `dim M_B^{f_∞ = 1} = d^+`.
  - For `Q(n)`, `n ≥ 2`: `d^+ = 1` for `n` even, where `ζ(n) ∈ Q·π^n` is critical. For `n` odd, `d^+ = 0`, `ζ(n)` is a
    Borel regulator value, and `K_{2n−1}(Z)` has rank 1.
  - Lichtenbaum's formula, `ζ(1 − n)` against `|K_{2n−2}(Z)| / |K_{2n−1}(Z)_tors|` up to 2, is the special-value
    statement on the other side of the functional equation.
  - The parity that C.3.1 computes (the real Frobenius on `Q(n)` and on `A(−1)`) is exactly what decides which of
    `K_{2n−1}(Z) ⊗ Q` and the critical value is nonzero.
  - GRH places no constraint on these values. Alpöge's footnote uses Lichtenbaum, a theorem, not GRH. The link
    identifies C.3.1's invariant with `d^+`, and carries nothing further.
- **CM heights (added 21 Nov 2026; corrected 21 Nov 2026 after the intake of ZETA_TWO, Claude Opus 5.5 at effort
  high).** No Faltings-height or Colmez row exists in this intake (ZETA_TWO IA01). New rows of the topic:
  - ZETA_TWO IA04: the CM elliptic Faltings height h_F = ¼log(Df²) + ½L′/L(1,χ_{−D}) − …, with an explicit error
    < ½R_−(D) under Alpöge (checked at statement level in the ZETA_TWO intake; the substitution step checked).
  - ZETA_TWO IA05: Alpöge removes the no-Siegel-zero gate for CM heights (quadratic Dirichlet GRH plus Stark's descent of
    an exceptional zero of a normal field to a quadratic subfield); dependency: A (zero gate) + an individual Colmez
    formula (B, except for abelian CM types) (logic confirmed in that intake, constants at statement level).
  - Rows E.2.1-E.2.6 (ring-class fields): RH for their Dedekind zeta functions is M (Masullo), not A.

These are my statements of standard theorems, from memory where marked; the run itself states none of them. Check
events: BRIDGE-SA07-7 to -10.

## 5. Prompt updates for a successor of RESEARCH_SA07

- **Do not redo Part A.1-A.2.** Give A.2.2-A.2.6 as results (checked here), with the invariant `v`. The successor's
  Part A should attack the two gates:
  - the algebraicity of `h` for a non-CM curve over `Q̄`: give it the run's criteria A.4.10-A.4.40 as the state, once
    they are checked;
  - the algebraic independence of `τ, τ̄` for a curve not isogenous to its conjugate (gate A.3, `E_8`).

  Under the push rule and the ledger check, these are the right main questions. State that they are transcendence
  problems at the level of the period conjecture for `E × c^*E`, so that the ledger can stop a run that does not move
  them.
- **H2's literal equivalence.** The successor should be asked to find a motive for which genericity of the `(α, β)`
  projection and genericity of the joint point differ, or to prove the equivalence.
- **D.2.** The run reports that the pages 18:42-49 do not define the `K` of 18:45. That is a transcription question:
  route it to a second-pass reading of 18:42-45 against the scans, not to a research run.
- **Corrections to feed in:**
  - R2: the converse is false (C.3.1);
  - R5: the graded formula is off by 2 (F.2.1, to be checked);
  - Lead A: the condition is `M ≅ c^*M`, not a real model (A.3.3).
- **Checking order for the rows not read in full here.** Many rows are used by others (E.2.3 by 15, E.2.6 by 11, E.2.9
  by 8, E.2.7, E.2.16, E.2.22, F.3.24 by 7 each). They should be checked before a successor builds on them:
  - first the refuted rows: B.1.3, B.4.4, D.5.2, D.5.3, E.1.2, E.1.3, E.2.1, E.3.3, E.3.4, F.3.7, F.3.11, G.2.2;
  - then E.2.3, E.2.6, E.2.7, E.2.9, E.2.16, E.2.22 and F.3.24.
- **The literature inputs to open:**
  - Kreutz-Shen-Vial (arXiv:2206.08618v3; A.4.9);
  - Sebbar-Besrour 2026 (A.4.6);
  - Masser 1975 Appendix One (A.4.2, A.4.5);
  - Bost-Charles §2 (A.2.4).

  None was reopened in this intake.
