# Primer: the mathematics of NEG_NIGHT as of checkpoint 15 (22 Nov 2026, 07:19 UTC)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), 23 Nov 2026, for the main session to read after a
compaction. It restates; it does not develop.

## The run and its inputs

**The run.** Prompt 54, "the night of negative results". GPT-6 Astra (ChatGPT Pro mode), started 21 Nov 20:04 UTC; it
records its effort as "not exposed". It has 164 findings in four families:
- **NN-S:** split-zero framework;
- **NN-A:** zeta labels, CUE, heat flow;
- **NN-C:** complexity;
- **NN-G:** GCT.

**Return.** `grothendieck_archive_transcription_20261110\research_returns\NEG_NIGHT_checkpoint_15_20261122T0719Z_unzipped\`,
with the TeX in `paper_parts\`.

**Our intakes, in this folder.** All are by Claude Opus 5.5 at effort high:

| Intake file | Agent | Coverage |
|---|---|---|
| `INTAKE_NEG_NIGHT_20261121.md` | a17221e5 | checkpoint 04, NN-S, NN-A, NN-C |
| `INTAKE_NEG_NIGHT_20261121_G.md` | a8d75352 | checkpoint 04, NN-G, with a "Full depth" pass |
| `INTAKE_NEG_NIGHT_20261122_cp15.md` | a17221e5 | the 57 new findings of checkpoint 15, compared by diff, GCT first |

**Inputs, as the run names them.**
- **A:** Alpöge's theorem, RH for ζ and every Dirichlet L-function, cited as a theorem.
- **M:** Masullo's draft. It is unrefereed and used only by A043, which the run marks conditional.
- **E:** the run's designated counting theorem, an input of the prompt.

**Check labels.**
- `[TPC]`: targeted proof check.
- `[IRP]`: independent re-proof.
- `[COMP]`: computation or certificate rerun.
- `[stmt]`: statement level.

## 1. Zeta zeros: labels, CUE, heat flow

### NN-A001 `[TPC]`, `[IRP]` (`paper_parts\analytic.tex`)

**Statement.** The exact right-mover criterion for zeros under the deformation is sin(πW_n + δ_n) > 0, with
δ_n = arctan(1/(2γ_n)). The uncorrected rule fails at zero 1169.

**Proof.** Implicit differentiation, using DLMF 25.11.17, ζ′(ρ) = −ie^{−iθ}Z′(γ), and sgn Z′ = (−1)^{n+1}.

**Check.** Recomputed with mpmath, and the Arb certificate was rerun. At zero 1169, sin πW < 0 but sin(πW + δ) > 0.

**Good for:** it corrects our consult ad855737 (`OURS_CONSULT_ad855737_ZETA_LABELS.md`, Q1, Prop. 1).

### NN-A002 `[TPC]`

A CLT for S(γ_n) doesn't give equidistribution of W_n mod 2. The gate is odd Fourier modes with the (−1)^n twist.

### The CUE model

- **A003, A016 `[stmt]`, with parts read.** Labels are uniform and independent of the gaps, with long-range decorrelation.
- **A017 `[TPC]`, `[IRP]`.**
  - The adjacent label agreement is 1 − 2Σ(−1)^{n+1}E(n), certified in (0.66654660183721072003, …072008).
  - Rederived from A003.1, and recomputed by Bornemann's Nyström method.
- **A024 `[stmt]`, consistent with Ben Arous–Bourgade.**
  - The first backward-heat collision occurs at time δ_min²/8.
  - It has a Weibull-3/2 law.
  - A025: a Poisson collision process of intensity (3/2)√v dv.

### Simplicity of zeros

- **A028 `[stmt]`.** Under A, all nontrivial zeros are simple iff √a·m_*(−a) → ∞, where m_* is the least order of a
  negative Toeplitz minor at time −a.
- **G039 `[stmt]`.** The Jensen form: lim a·j*(−a) = x*²/8.
- **A014, A018 `[COMP]`.** The checkers were rerun.

### New at checkpoint 15 `[stmt]`

- A031: CUE labels are positive in proportion → 1/2.
- A036–A042, A045–A049: both velocity signs occur, with positive lower proportions, for ζ (A047: ≥ 10^{−14}, needs RH) and
  for each primitive character, under A.
- A050: almost 2/3 of the zeros stay real and simple for −c/log²T ≤ t ≤ 0 (RH).
- A051: nonreal zeros of H₋ₐ occur below height exp(exp(C/√a)).
- A033, A034: Martinet's Q₈ field, central order 2, two branches.

## 2. Complexity: counting and parity in actual geometric objects (the NEG row of the Hexagon board)

### Parity of #SAT is a Hasse–Witt scalar

- **NN-C005 `[TPC]`.** N mod 2 = [x₁⋯x_n]·ML(Π(1 + f_i)). It is ⊕P-complete for O(n) sparse quadratics.
- **NN-C023, C024, C030 `[stmt]`, mechanism checked.** The coefficient of z₁⋯z_r is the Hasse–Witt (Frobenius) scalar of
  the degree-r hypersurface in P^{r−1} over F₂. The Fermat pencil H + uF is smooth for odd r. So computing the Frobenius
  scalar on the top coherent cohomology of an explicit smooth hypersurface is ⊕P-hard.
- **C031, C032 `[stmt]`.** Over F₄; a model over F₂ with four-dimensional coherent cohomology.

### Other geometric objects

- **NN-C026 `[stmt]`.** A smooth projective curve with #C(F_q) = 1 + 2·#SAT.
- **NN-C027 `[stmt]`.** A smooth sparse cubic scheme over Z with [X] = 𝕃^{v+h} + N·𝕃^h.
  - S016 gives its Chow ring and homotopy type.
  - S017: it is a wedge of N motivic spheres.
  - S018: the F₂-rank of a γ-graded piece is #P-complete.
- **NN-C028 `[stmt]`.** Embedding comparison of actual Tate cohomology is PP-complete.

### The E line

- **NN-C001 to C004 `[TPC]`.** They extend E:
  - to quasilinear sparse systems (compression to 6n rows by conditional expectation);
  - to fixed F_{2^r};
  - to exact weighted partition functions;
  - to algebraic tensor alphabets and quantum amplitudes in 2^{O(s/√log s)}.
- **C033–C042, C055 `[stmt]`.** Symbolic counting, integral CNF, permanents of sparse or structured matrices. They say
  nothing about per_n in the orbit closure of det_n.

### Where the obstacles are located `[stmt]`

- C012: PIT. C014: hitting sets are the whole cube.
- C007, C019: isolation. C008, C009, C021: proof systems.
- C010: Bürgisser's characteristic-zero transfer needs RH for Dedekind zeta functions of arbitrary number fields, which A
  doesn't give. C015: the constant-free form needs neither.
- C047, C054: PosSLP. C048–C053: odd-root circuits. C053 removes A in its scope.

**Good for:** it shows exactly where purity stops helping. A controls the zeros of ζ_X(s) = ζ(s − v − h)·ζ(s − h)^N; the
counting difficulty is the multiplicity N.

## 3. The split-zero framework

- **NN-S001 `[TPC]`.** A G(R)-semimodule is a disjoint union of R-modules M_b over the join-semilattice B = eM. The
  Fix(−1) = ⨆M_b[2]. Z/2 over G(Z) is a counterexample to Booleanness.
- **NN-S002 `[TPC]`.** The sign-fixed scheme is Spec Z[x]/(2x): non-flat, with characteristic-two fibre (SGA 3 I,
  Rem. 4.7.1.2).
- **NN-S003 `[TPC]`.** Linearization kills the support skeleton: R ⊗_{G(R)} 𝔹 = 0.

## 4. GCT (NN-G; a8d75352's intake, with the "Full depth" pass)

### Proofs read and confirmed `[TPC]`

- **G001.** The D₅ count: the fibre count is q − χ(u), and the Hilbert series is (1 + t⁴)/((1 − t²)(1 − t³)).
- **G002, G004.** Given ALPOGE_GCT P-F31 and P-F57.
- **G003.** It is the A7 proposition of prompt 56:
  - f_L(n) = L⌊n/L⌋ + 1 is positive with p = s = L − 2;
  - so large strict indices don't give a vanishing coefficient.
  - Checked for L ≤ 80.
- **G005–G008, G010, G013–G015, G017.**
- **G018.** φ(M) poles force dim V ≥ 2^{n−2}, given P-F31.
- **G009.** F42 quantified: 40(q^{n/2} + q^{−n/2})^{2k} has dimension 40·4^k.

### The rank-three table and its dimension rings

These are effective lifts of GCT VIII's E₃ constants. They are noncanonical, and none decides a GCT hypothesis.

- **G012 `[IRP]`, from our `e3_constants.json`.**
  - At v = i, β₁ = γ²₁ + Σ/4 ↦ 8E₁₂, β₂ ↦ 8E₂₁, β₁₂ ↦ 16E₁₁, β₂₁ ↦ 16E₂₂ is an algebra isomorphism onto M₂.
  - So the hexagon symmetry of E4 §6 is matrix-unit cyclicity at q = −1.
- **G011, G019 `[COMP]` + optimality proof `[TPC]`.** 7276 cancelling pairs is the exact minimum in the integral-ratio
  class, with 2 minimizers.
- **G021, G024, G025, G028 `[COMP]` as certified.** The class minima are 7064, 5932, 4520 and 3352.
- **G032–G037 `[TPC]`, checkpoint 15.**
  - Decidability.
  - An explicit lift with 2744 pairs.
  - 2744 is the exact, uniquely attained minimum of the symmetric closed-table class.
  - Every lift on all 810 positions has ≥ 112.
- **G038.** The classification is confirmed; the bound 932 is carried.
- **Current intervals:** [112, 2744] on all positions; [932, 2744] on the original support.

### The prompt-56 additions (cp15 intake §3a)

- **Corollary A1-C**, from GCT_POS PNEW-013 with G002 and G018.
  - Every quasi-period of k_n is divisible by 2^{n−1}·3^r.
  - Every recurrence k_n satisfies has order ≥ 2^{n−2}.
  - Any trace model tr(AF^s) of k_n needs dim V ≥ 2^{n−2}.
- **The A3 sentence** for plethysm.
- **The A7 wording rule** (G003).

### Corrections to our record

- E4 §6b: state the symmetry for the β-block (G012 with N-001).
- Our "minimum 7,952" is a minimum within the search window only.

## 5. Open rows, with gates

| Gate | Next step |
|---|---|
| 6, zeta labels | odd-mode cancellation with the (−1)^n twist, through sgn Z′ and Gram-law statistics |
| 7, arithmetic collision law | transfer A024 and A025 through extreme-gap statistics |
| 10–11, detection and multiplicity | bound √a·m_*(−a) below from the known proportion of simple zeros |
| 2–3, PIT and isolation | uniform isolating families (CUE_GCT I-31 to I-44) |
| geometric counting | whether any polynomial cohomological operation extracts N mod p, p ≥ 3 (C028 suggests PP-hard) |
| GCT tables | the 932 enumeration certified by a second program; a lift below 2744 inside G037's 92-dimensional parity space |

## 6. Where the results went

- **Hexagon NEG row.** Not ready. A047, A048, A050, A051, G039, C052, C053, S017 and S018 need whole-proof checks and
  literature searches.
- **Prompt 56 / 56c (GCT write-up).** A1-C, the A3 sentence, the A7 wording.
- **Our record.** `SPLIT_ZERO_IN_CONNES_CONSANI_TERMS` lines 157–158 and E4 §6b/§7, as above.
- **pequalnp fleet.** NEG_NIGHT is not in the joint GCT lemma space. In our survey
  (`<local>/pequalnp_work\MAPPING_OUR_RESULTS_TO_PEQUALNP.md` §1.5), the parity lemmas (meta 56, 58, 60, 63, 92,
  639; pcx 78, 81, 86, 89, 92) and the SAT lemmas do not touch these statements.
