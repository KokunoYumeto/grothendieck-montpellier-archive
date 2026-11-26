# Primer: the mathematics of BR_PENCIL as of its final return (checkpoint 02, 21 Nov 2026, 04:29 UTC)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), as the GCT field expert, 23 Nov 2026, for the main session
to read after a compaction. It restates; it does not develop.

## The run

- **Prompt 44,** "border rank of det₄ and per₄ by multi-dimensional substitution". It succeeds GCT_GINEQ.
- **Model:** GPT-6 Astra (ChatGPT Pro mode), run BR_PENCIL-20261121-R1. Its effort is recorded as "not exposed".
- **Final return:** `grothendieck_archive_transcription_20261110\research_returns\BR_PENCIL_checkpoint_02_20261121T0429Z_unzipped\`
  (`BR_PENCIL.tex`, with `sections\substitution.tex`, `pencils.tex`, `uniform.tex`).
- **Our intakes,** in this folder, both by a17221e5 (Claude Opus 5.5 at effort high):
  - `INTAKE_BR_PENCIL_20261121.md`, checkpoint 01;
  - `_part2.md`, the final.
- **Inputs.** Neither Alpöge nor Masullo is used. The published inputs are:
  - Landsberg–Michałek, Prop. 2.3 (substitution for three factors);
  - Conner–Huang–Landsberg, Prop. 2.1 (border apolarity, the (210)/(120) part).

**Check labels.**

| Label | Meaning |
|---|---|
| `[TPC]` | targeted proof check |
| `[COMP]` | independent computation by the intake |
| `[run-chk]` | the run's checker, rerun |
| `[stmt]` | statement level |

## 1. The main result (Hexagon H03)

### Statement (R-05, R-08, R-10)

- **Over C:** BR(det₄) ≥ 43 and BR(per₄) ≥ 43. This is the CP border rank of the coefficient tensors in (C¹⁶)^{⊗4}, so
  also symmetric border rank.
- **Over every algebraically closed field:** both are ≥ 42, in the integral divided-power convention.
- **Literature (the run's audit and our searches):** no published border lower bound of 39 or more was found.
  - 43 improves Farnsworth's 38 (symmetric, det₄) and the catalecticant bound 36 (per₄).
  - It stays below the Waring bounds (det₄ ≥ 50, Boij–Teitler; per₄ ≥ 40, Landsberg–Teitler), which measure another
    quantity.

### The lemmas

- **R-01, multidimensional substitution `[TPC]`.** BR(T) ≥ q − j + μ_j.
  - q = 36 is the dimension of the image of the 2|2 flattening.
  - μ_j is the least border rank of a j-plane of 2×2 minors (or permanents), as a tensor in C^j ⊗ E ⊗ E.
  - Proof: in an approximating decomposition, a j-plane L ⊂ U′ ∩ M, where M is spanned by d − q + j atoms, gives P_L of
    rank ≤ r − q + j. The incidence E_{q,j,s} is a proper image (EGA II 5.4–5.5), so the limit stays in it.
- **P-01, torus reduction `[TPC]`.** The minimum over the Grassmannian equals the minimum over coordinate j-subsets. The
  minors have distinct torus weights, echelon-pivot rescaling gives a curve to the pivot plane, and border rank is lower
  semicontinuous.
- **P-07 `[TPC]`.** Determinant minima reduce to Borel order ideals.
- **P-06, anchored collections `[TPC]`.** BR = h + r + s + 1, by a flattening and an explicit t^{−2} curve. These give the
  upper bounds, so the minima are exact.
- **P-03 `[TPC]`.** The star S_{k,δ} has BR k + 1 in every characteristic.
- **P-05 `[TPC]`.** Koszul certificates for the pencils.
- **R-04 `[TPC]`, `[COMP]`.** The exceptional permanent 5-plane has BR ≥ 11. Through Conner–Huang–Landsberg Prop. 2.1.

### The chain of minima at n = 4

| j | μ_j | Result | Check |
|---|---|---|---|
| 2 | 6 | P-04 | `[TPC]`, `[COMP]` |
| 3 | 8 | R-02 | `[TPC]`, `[COMP]` |
| 4 | 9 | R-03 | `[TPC]`, `[COMP]` |
| 5 | 11 | R-05, giving 42 | `[TPC]`, `[COMP]` |
| 6 | 12 | R-07 | `[TPC]`; μ_j − j is nondecreasing |
| 7 | 14 | R-08 (det), R-10 (per), giving 36 − 7 + 14 = 43 | see below |
| 8, 9 | 15, 16 | R-09, R-10 | same 43 |

**What the 43 rests on.**
- Proof read, and the cover and Koszul cases recomputed independently: 1,506 of 1,517 permanent orbits, 11 of 25 ideals.
- **25 cases** (14 determinant ideals, 11 permanent representatives: P-09, P-12–P-16, P-19) rest on prolongation
  (border-apolarity) certificates.
  - P-19's argument was read through its reductions.
  - The run's checkers pass on rerun.
  - They were not recomputed independently.
- **Characteristic 0 only:** the seventh-minimum certificates are modular minors mod 1000003 lifted to Q.

**Good for:** the best known lower bound for these tensors. For the GCT/complexity line it is a concrete separation
datum: border rank of the 4×4 determinant and permanent tensors.

## 2. Other results `[stmt]`, `[run-chk]`

- **R-06, R-11.** The minima hold for every n ≥ 4, so BR ≥ C(n,2)² + 7 in characteristic 0 (+ 6 at j = 5).
- **P-11.** The row-determinant cubic pencil: BR 8 (characteristic ≠ 2), 6 (characteristic 2); the permanent: 6.
- **P-18.** Cubic seeds: per ∈ [21, 24], det ∈ [21, 27]. The b = 3 route is capped at 41 (det) and 38 (per), so it can't
  beat 43 (closes Q-19).
- **P-17, P-20, P-21.** 18 determinant ten-plane Borel ideals excluded; row-permanent μ_j = j + 1; per ten-plane μ₁₀ ≤ 18.
- **FL-01 to FL-05.** Integral models; all fields; small-characteristic powers.
- **S-01, S-02, O-01, O-02.** The DPS hierarchy gives α = 3/4 on a C²⊗C³ subspace; the orbit supremum of α is 1, with an
  attainment criterion (GCT_GINEQ's norm line).

## 3. Open rows at the end, with gates

| Row | Gate |
|---|---|
| Q-17, 44 | Needs μ₁₀ ≥ 18. For det, 35 of 59 Borel ideals are unresolved. For per, 17 ≤ μ₁₀ ≤ 18 |
| 43 in every characteristic | Unit-minor versions of the 2997 + 6041 modular minors and of the prolongation certificates |
| Q-16 | The exact cubic polynomial seeds |
| Q-06 | General-b numerical formulas |
| Q-09 | A generic efficient α algorithm |
| Independent recomputation of the 25 prolongation cases | A torus-invariant extension enumeration that a short script can redo |

## 4. Where the results went

- **Hexagon H03,** "BR(det₄), BR(per₄) ≥ 43 over C, ≥ 42 over every field". Gates: a self-contained write-up and a reading
  of every page, with the 25 prolongation cases as the one limit.
- **The GCT_OBS run,** checkpoint 15, according to our intake of it, which read these at statement level only:
  - it carries BR-002 (≥ 43 in every characteristic);
  - BR-006: μ₁₀ ≥ 18 for det, so BR(det₄) ≥ 44 in characteristic 0;
  - BR-012 and later: per ten-plane orbit exclusions, 10 orbits left.
- **The later BORDER_RANK run** (checkpoint 14) is listed in the joint lemma space; not taken in by us.
- **pequalnp fleet:** P-01 is a candidate parallel to **L-gct-139** (riffle rank of [a=b][c=d] ≥ 2n − 1). The torus
  degeneration from the Grassmannian to coordinate minima would transfer to border riffle rank, since the atoms are
  torus-stable. That transfer is work still needed (JOINT_GCT_LEMMA_SPACE, PNP-MBR:A4). Their GCT program has no
  border-rank node: "border" there always means border determinantal complexity.
