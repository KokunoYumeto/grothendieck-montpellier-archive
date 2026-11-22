# Intake of NEG_NIGHT (prompt 54), checkpoint 04: the GCT findings NN-G001 to NN-G031

By Claude Opus 5.5 at effort high (a8d75352), for the main session (Claude Opus 5.5 at effort max), 22 Nov 2026. The run is
GPT-6 Astra (ChatGPT Pro mode), effort not exposed. The rest of NEG_NIGHT is taken by a17221e5. Check events:
`INTAKE_NEG_NIGHT_20261121_G_CHECK_EVENTS.tsv`.

## 0. What I read

**Return:** `research_returns\NEG_NIGHT_checkpoint_04_20261121T2305Z_unzipped\`. Its GCT chapter is `work\gct\chapter.tex`,
with 31 findings.

**Read:**
- the QUESTIONS rows NN-QG001 to NN-QG036;
- the subsection headings of all 31 findings;
- in full: NN-G009, NN-G011 (the statement), NN-G012, NN-G019 (the statement) and NN-G028 (the statement).

**Reran:** every verify and check script of `work\gct` in my work folder (scratchpad `negnight_root`, with our E4 scripts as
`sources\OURS_E4_scripts`), using `python -I -B`. All exited 0:
- `verify_dimension_` 7276, 7064, 5932, 4520, 3452 and 3352;
- `verify_signpoint_matrix_block`, `check_signpoint_Hecke_trace` and `check_elementary_claims`;
- `verify_dimension_ratio_optimum`, `verify_fixed_bottom_optimum`, `verify_constant_ratio_global_optimum`,
  `verify_proportional_cells_optimum` and `verify_common_cell_content_optimum`;
- `verify_degree_cutoff_constants`, `verify_mod4_obstruction` and `verify_gluing_mass6_exclusion`.

## 1. Verdicts

| Finding | Verdict |
|---|---|
| **NN-G012** (the sign-point symmetry as matrix units) | **Independent re-proof, confirmed** from our own `e3_constants.json` at v = i (`consults\E4_scripts\g012_check.py`). With β₁ = γ²₁ + Σ/4, β₂ = γ²₂ + Σ/4, β₁₂ = γ²₁₂ and β₂₁ = γ²₂₁, the map β₁ ↦ 8E₁₂, β₂ ↦ 8E₂₁, β₁₂ ↦ 16E₁₁, β₂₁ ↦ 16E₂₂ is an algebra isomorphism onto M₂ (all 16 products checked). Σ² = 0, and Σ annihilates the block. The tensor-Hecke trace is 0 on Σ, γ²₁, γ²₂ and 16 on γ²₁₂, γ²₂₁ (rerun), so it restricts to the matrix trace |
| **NN-G009** (quantified F42) | **Targeted proof check, confirmed.** 40(q^{n/2} + q^{−n/2})^{2k} has eigenvalue q^a with multiplicity 40·C(2k, k + a), so its dimension is 40·4^k. Any fixed V needs at least 2k + 1 distinct eigenvalues |
| **NN-G011** (7276 cancelling pairs, 6612 in the bottom cell) | **Computation, confirmed** by the rerun of its certificate, and by GCT_POS's rerun of N-005 with our own verifier: 0 failures |
| NN-G019, G021, G024, G025, G026, G028, G029, G030, G031 | **Computation, confirmed as certified**: their scripts reproduce the certified tables and numbers. The optimality proofs in each delimited class are read at the level of the statement |
| NN-G001 to G008, G010, G013 to G018, G020, G022, G023, G027 | Statement level. The elementary inputs of G001 and G003 are confirmed by `check_elementary_claims` |

The optimum results, at the level of the statement:
- **NN-G019:** 7276 is the exact minimum in the integral-ratio class, with two minimizers.
- **NN-G021:** 7064 with signed auxiliary parameters.
- **NN-G024:** 5932 for nonprimitive common cells.
- **NN-G025:** 4520 for proportional cells.
- **NN-G028:** 3352 with the bottom coefficients fixed (W = 3D, U₁ = 3D, U₂ = D), with rational Λ allowed.
- **NN-G029:** a degree cutoff that makes the unrestricted optimum decidable.

## 2. Where this corrects our record

1. **The main session's E4 §6b** (the C₃ at q = −1). Its cell constants are right. But the four-element cell is not closed
   at D = 0: four products carry a Σ-component 4.
   - **NN-G012 is the correct form.** In the shifted elements β₁ = γ²₁ + Σ/4 and β₂ = γ²₂ + Σ/4 the cell becomes a genuine
     M₂, and §6b's cyclic slot rotation is the cyclic identity tr(ABC) = tr(BCA) of the matrix trace in a rescaled
     matrix-unit basis.
   - GCT_POS N-001 adds that this rotation does not extend to the whole ten-element table (μe = e, e² = 16e).
   - **Edit for E4 §6b:** state the symmetry for the β-block, not for the γ-cell, and cite NN-G012 and N-001.
2. **Our dimension-ring minima are window minima, not global ones.** SPLIT_ZERO_IN_CONNES_CONSANI_TERMS records
   (lines 157–158, from `consults\dimension_ring_minimal_pairs.out`) "minimum 7,952 … exactly one ring", and 11,764 among
   unimodal rings. Since then:
   - NN-G011 and N-005 give 7276; N-005 gives 9040 with every constant unimodal;
   - NN-G021 gives 7064; NN-G025 gives 4520; NN-G028 gives 3352, each in its stated class.

   **Edit: qualify ours as "within the 14,975-ring search window"** and cite these.
3. **My GCT_NSRH part 2 (F42 as a stated limit)** is quantified by NN-G009, which also gives the exact dimension 40·4^k
   of the word-dependent objects.

## 3. How it bears, and the attacks it opens

- **The dimension rings** are exactly the "composing" categorification question left open in E4 §7. There, each constant
  had its own realization, and the composition was not shown.
  - NN-G010 says what category a dimension ring supplies.
  - NN-G011 and NN-G021 to NN-G028 minimize the cancelling pairs: the cost of making the realizations compose.
  - **The attack:** NN-G029's decidability result, run to the unrestricted optimum, and compared with E4 §7's
    quantum-integer realizations. Those had zero cancellation per constant but no composition. Does the optimum composing
    ring use the Weil restrictions Res_{F_{q²}/F_q} P¹ on the six P-F-E3-01 constants?
- **NN-G012** places the hexagon symmetry of E4 §6b in matrix units at q = −1. The open question in E4 §6b (why q = −1
  restores it) becomes: at q = −1 the χ² block is split M₂ with Σ in the radical, and the trace form is the matrix
  trace.
- **NN-G009** removes any hope of a single finite object. Each P₁^k needs an object of dimension 40·4^k, as in F45 and
  E4 §7.

## 4. Errata and Hexagon readiness

**Errata:** none to outside authors from these findings. The errata to GCT VIII are in the GCT_POS nonstandard intake.

**Hexagon:**
- **H23** (ours, P-F-E3-01): NN-G012 and N-001 refine its hexagon remark (§2.1 above). Its gate is unchanged: an
  independent re-run and a reading of VIII before the note to the author.
- **The dimension-ring optima** (NN-G019 to G031) are complete within their classes and computationally certified. But
  their interest is internal (a composing realization of one rank-three table), and the run is active, so they are not a
  candidate now.

## Full depth (22 Nov, second pass)

Every statement-level finding of §1 was taken further. The events are appended to the CHECK_EVENTS file.

**Proofs read in full and confirmed (targeted proof check):**
- **NN-G001:** the D₅ count. For U = u ≠ 0 the fibre count is q − χ(u), using Σχ(x² + a) = −1; the total is q² in every
  characteristic. The Hilbert series is (1 + t⁴)/((1 − t²)(1 − t³)), with conductor 2.
- **NN-G002 and NN-G004:** given ALPOGE_GCT's P-F31 and P-F57, which are carried as background.
- **NN-G003:** constituents X − r + 1; both indices are L − 2; I rederived the generating function.
- **NN-G005:** the universal valuation group of a finite distributive lattice is Z^{join-irreducibles}. This is standard
  (Birkhoff), and the proof is complete.
- **NN-G006:** injectivity of the Artin–Tate zeta encoding. At p = 5 and p = 3 (odd n), the Vandermonde argument applies;
  the pole order at m is a_m + a_{m−1}.
- **NN-G007:** the C₂ Burnside and representation cones.
- **NN-G008:** P/(D² + 1). This is the same phenomenon as GCT_POS N-007.
- **NN-G010:** the effective table is associative through A ⊂ Z[q^±]²; the matrix-convolution category has free split
  K₀.
- **NN-G013:** Valiant–Vazirani isolation with affine hashes, P(X = 1) ≥ 3/16. This is standard.
- **NN-G014:** unique least valuation.
- **NN-G015:** majority comparison of positive counts with full support.
- **NN-G017:** the semigroup ⟨L, L + 1⟩. Its Frobenius number is L² − L − 1, with L(L − 1)/2 gaps; A² has trivial
  cohomological data.
- **NN-G018:** φ(M) poles force dim V ≥ 2^{n−2}, given P-F31.
- **NN-G019, the optimality proof of NN-G011's 7276.**
  - The scalar-block identities force U_i and V_i.
  - The parity argument gives k₁ even and k₂ odd.
  - The range reduction from the 7276 incumbent gives w ≤ 36, d ≤ 26, k₁ + k₂ ≤ 52.
  - The minimal-Λ elimination is sound.
  - The independent exhaustive certificate reruns: minimum 7276, with exactly 2 minimizers.
  - The multiplicity formula for T is taken from NN-G011.

**Statement level only:**
- **NN-G016:** I checked the Rieffel-type cutoff partition Σc(y − nℓ)² = 1, but did not read the index computation.
- **NN-G020:** the 3-CNF to toric-ray construction; the proof was not read in full.
- **NN-G022 and NN-G023:** no separate scripts.

**Computation:** NN-G027's explicit realizations are reproduced by the 3452 and 3352 certificates.

**Result:** no finding of NEG_NIGHT's GCT chapter is refuted. The only corrections are to our own record (§2).
