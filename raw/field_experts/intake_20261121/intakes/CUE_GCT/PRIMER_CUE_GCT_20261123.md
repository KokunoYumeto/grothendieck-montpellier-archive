# Primer: the mathematics of CUE_GCT as of its final return (checkpoint 08, 21 Nov 2026, 06:49 UTC)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), as the GCT field expert, 23 Nov 2026, for the main session
to read after a compaction. It restates; it does not develop.

## The run and the record

- **Prompt 36.** GPT-6 Astra (ChatGPT Pro mode), run CUE_GCT_20261121_R1, started 00:49 UTC; the run records its effort
  as "not exposed".
- **Final return:** `grothendieck_archive_transcription_20261110\research_returns\CUE_GCT_checkpoint_08_20261121T0649Z_unzipped\deliverables\CUE_GCT.tex`
  (R-14 from line 1238).
- **Intakes,** in this folder, all by a17221e5 (Claude Opus 5.5 at effort high):
  - parts 1 to 4, for checkpoints 01, 02–03, 04 and 05–08.
  - Most findings were read at statement level. The checks are as marked.
- **Inputs:**
  - A (Alpöge) and M (Masullo) only in the zero-statistics audit P-Z01–P-Z05.
  - No GRH enters the GCT results. Masullo dependencies stay conditional.

**Check labels:**

| Label | Meaning |
|---|---|
| `[TPC]` | targeted proof check |
| `[COMP]` | our computation |
| `[part]` | read in part |
| `[stmt]` | statement level |

## 1. The main result: four-row multiplicity obstructions under padding (Hexagon H14)

### Statement (R-14, R-27, G-20)

Let P_{m,4} be the projection of the padded permanent's orbit closure to four variables, and let c_m be its dimension.

For m ≥ 17, a four-row multiplicity gap for z^{n−m}·per_m against det_n exists in large degree **iff n² ≤ 2m² − m + 1**,
so up to n ≈ √2·m. That is, some λ ⊢ nd with exactly four rows has m_λ(z^{n−m}per_m) > m_λ(det_n). For 8 ≤ m ≤ 16 the
finite cases come from R-13: (8, 9), (9, 10), …, (16, 17–22).

### R-14, the dimension criterion `[TPC]`, `[COMP]` (part 2)

**Statement.** If c_m + 3 > 2n² + 2, then for every large degree d some four-row λ ⊢ nd is a multiplicity obstruction.

**Proof.**
1. The projection of the padded orbit closure to four variables is Z_{m,n} = {ℓ^{n−m}q}, of dimension c_m + 3. This
   needs generic injectivity of (ℓ, q) ↦ ℓ^{n−m}q; a general q is irreducible (Eisenstein at x₃).
2. The quaternary determinant image has dimension ≤ 2n² + 2 (G-06 `[TPC]`). The stabilizer of (I, diag, generic) is
   scalar, and C(n+3,3) − (2n²+2) = C(n−1,3).
3. Hilbert polynomials of degrees c_m + 2 and ≤ 2n² + 1 force a larger GL₄ multiplicity on the permanent side in large
   degree.
4. Four-row GL_{n²} multiplicities equal those of the projected images. Highest-weight vectors use the first four
   variables, and I(Y) ∩ C[first four] = I(π(Y)), because π(Y) ⊆ Y is a torus limit.
5. G-05 removes three rows or fewer.

### R-13, the quaternary permanent dominates exactly for m ≤ 16 `[COMP]` for m = 4–10

c_m = C(m+3, 3) for 4 ≤ m ≤ 16, and dominance fails from m = 17 on (1124 < 1140). The certificates for m = 11–16
(3,348,864 entries) are the run's.

### R-27, the exact dimension `[stmt]`

c_m = min(C(m+3,3), 4m² − 2m + 2) for all m.
- R-22 `[part]`: the earlier bound 4m² − 20m^{3/2} + 2.
- R-24, R-25: c₁₇ = 1124 and c₁₈.
- R-23: the remaining defect is one Tor₁(R/J_m, S)_m graded piece, in the SGA 6 Tor-independence dictionary.

### The method's ceiling (RQ-26) `[stmt]`

- No four-variable route passes √2.
- G-21: dim P_{m,r} = rm² − 2m + 2 for r ≥ 4.
- G-24: the exact rectangular range m < n < rm/(r−1).
- G-22–G-28: higher-row phases.

### Good for, and not for

**Good for:** the representation-theoretic witnesses GCT asks for, in a genuinely padded (small linear) range. As far
as our intake found, multiplicity obstructions under genuine padding were not published.

**Not for:** it does not separate complexity classes. The separations are already known, from Mignon–Ressayre and
pequalnp's checked L-gct-010.

A literature search was named for this result:
- Kadish–Landsberg;
- Landsberg's GCT book, ch. 8–9;
- Ikenmeyer–Kandasamy;
- Gesmundo–Ikenmeyer–Panova;
- Bürgisser's survey.

## 2. Other GCT results

- **G-05 `[TPC]`.** Det_n contains every ternary form, so multiplicities with ≤ 3 rows equal the ambient ones. Classical:
  Dickson; Beauville, Prop. 3.1(a). The same result as GCT_KRON O-007.
- **G-14, G-15 `[stmt]`.** Jet dominance of determinant pencils gives λ₁ ≥ d(n − m) + 4. The same technique as GCT_KRON's
  M-013.
- **G-12 `[stmt]`.** No rectangular gap for n ≥ 4m/3.
- **G-18 `[stmt]`.** Gaps exist at every large stretch of a strict four-row direction. Occurrence obstructions are
  eventually absent along each direction, so these are multiplicity gaps, not occurrence gaps.
- **G-08 `[stmt]`.** Quantitative universality: ℓ^{n−m}f is an n×n determinant for n ≥ S(m, r).
- **G-10, G-11, G-13, G-16, G-17 `[stmt]`.** Explicit labels, with astronomically large degree bounds.
- **G-04 `[TPC]`.** Integral orbit-closure coefficient matrices, with exact base change over Z[1/δ_d].
- **G-03 `[TPC]`.** Two honest G_m-representations equal modulo F_γ^{D+1}, with different weight multiplicities.

## 3. Cote 133 (λ-rings) and isolation

- **G-01 `[TPC]`, `[COMP]`.**
  - In B(G): s₂ = b₂ + E and E² = E + [Inj({1,2},E)], so the boxed 2b₂ + E = E² of cote 133, scan 019, fails.
  - In representation K₀: V² = 2Λ²V + ψ²V.
  - This is independent agreement with GCT_KRON A-001.
- **G-02 `[TPC]`.** λ^i(xy) needs λ^i(x) and λ^i(y), so scan 006 lines 25–26 read λ^i.
- **Forced readings** (TRANSCRIPTION_NOTES.tsv). Scan 019: lines 10, 13, 20. Scan 028: line 10. The ink was not
  inspected.
- **P-11 `[TPC]`.** A number-field point encoding a hitting set is polynomially interconvertible with an integer hitting
  set. So number fields add nothing to ROABP PIT except through a Frobenius/Chebotarev encoding (P-08).
- **I-18 `[TPC]`.** Regularize-then-specialize fails for width-2 ROABPs. The criterion is a unit Plücker minor.
- **I-21–I-44 `[stmt]`.** Isolation subclasses: fixed width; balanced width three through 12 variables (13 away from
  characteristic 2).
- **P-01–P-20 `[stmt]`.** Purity samplers and their gates.
- **P-Z01–P-Z05.** What A and M discharge among the zero statistics; carried. For instance, Montgomery's pair
  correlation for Fourier support in (−1, 1) is proved under A.

## 4. Open rows at the end

| Row | Gate |
|---|---|
| Explicit gaps | An explicit four-row λ, degree and separating equation at (8, 9) and at (17, 23). The attack named: GCT_KRON A-034's ray algebra with KRON's exclusions |
| Padding beyond √2 | Multiplicity comparisons that don't come from a dimension count, such as ranks of explicit orbit-coefficient matrices (R-05, R-06, G-04) |
| I-Q01, I-Q13 | Polynomial-in-width ROABP hitting sets, and their GCT V consequence |
| P-08 | The purity-to-ROABP encoding |
| Cote 133 | The ink-level readings |
| Rerunnable certificates | R-13 (m = 9–16), R-24, R-25, R-27 |

## 5. Where the results went

- **Hexagon H14** (R-14 with R-13 and G-20). Gates: a literature search (Dörfler–Ikenmeyer–Panova first), and proof
  checks of R-23, R-26, R-27.
- **GCT_OBS** (prompt 53) took the explicit-gap question. QC-019 gives a named weight and degree with q > K at (8, 9),
  conditional on a 156-function certificate. QC-014 shows that at m = 4 no ≤ 4-row multiplicity obstruction exists for
  n ≥ 7.
- **Our pequalnp survey** (`<local>/pequalnp_work\MAPPING_OUR_RESULTS_TO_PEQUALNP.md` §1.2): H14 is a barrier
  to four-row routes toward L-gct-011.
- **pequalnp fleet**, one line per result:
  - **R-14** — parallel to **L-gct-011**: a barrier. Four-row multiplicity obstructions for the genuinely padded
    permanent exist only when c_m + 3 > 2n² + 2.
  - **R-12, R-13** — parallel to **L-gct-010**: the separation is already known. R-13 is a candidate parallel to
    **L-gct-057**, but no useful step follows.
  - **G-08** — parallel to **L-gct-005**: quantitative Valiant universality.
  - **P-02** — candidate parallel to **L-gct-129**: hitting sets for sparse polynomials. Whether character-point hitting
    sets give DIV-type bounds (L-gct-103, L-gct-104) is undecided.
  - **The run's sentence "m²/2 is established" (ctx-G13)** — superseded on pequalnp by Lean-checked results:
    - **L-gct-070**: (2m² − 10m + 11)/3, past m²/2 for m ≥ 19;
    - **L-gct-056 / L-gct-074**: border dc(perm_m)/m² → ∞.

    The sentence is correct only for refereed bounds.
