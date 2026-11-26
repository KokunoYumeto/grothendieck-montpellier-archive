# Primer: the mathematics of GCT_OBS as of checkpoint 15 (22 Nov 2026)

By agent a8d753525905811ab (Claude Opus 5.5 at effort high), as the GCT field expert, 23 Nov 2026, for the main session
to read after a compaction. It restates; it does not develop.

## The run

**Prompt 53**, explicit GCT obstructions for the padded permanent, the successor of GCT_KRON and CUE_GCT. It was run by
GPT-6 Astra (ChatGPT Pro mode); the run records its effort as "not exposed".

**Files:**
- **Text read:** `reports_20261122\overnight_intake\GCT_OBS_cp15\text\GCT_OBS.tex`, plus the run's
  `work/support_lmr/findings.tex` (S-001 to S-004 are lines 1–468) and `work/quaternary/quartic_padding_containment.tex`.
  The checkpoint 05 folder is
  `grothendieck_archive_transcription_20261110\research_returns\GCT_OBS_checkpoint_05_20261122T0257Z_unzipped\`.
- **Intake:** `INTAKE_GCT_OBS_20261122_cp15.md`, in this folder, by a17221e5 (Claude Opus 5.5 at effort high).
  - It is a diff against checkpoint 05.
  - Its own programs are in `checks\`.
  - Its keep audit is in `GCT_OBS_cp15_keep_audit.tsv`.

**Inputs:** no use of Alpöge or Masullo.

**Check labels:**

| Label | Meaning |
|---|---|
| `[TPC]` | targeted proof check |
| `[COMP]` | our computation |
| `[bg]` | carried as background without fault found |
| `[stmt]` | statement or title level |

## 1. Explicit separation at n = m = 3, by both sides (S-001 to S-003)

### S-001 = GCT_KRON F-016, the support lemma `[TPC]`

**Statement.** Every coefficient c_α of a highest-weight vector of weight λ in Sym^d Sym^n has Σ_{i≥j} α_i ≤ λ_j.

**Proof.** A flag-minor argument. The same proof is in GCT_KRON from line 15823.

### S-002 `[TPC]`, `[COMP]`

**Statement.** Six explicit highest-weight functions P₀, …, P₄, R form a basis of the ambient space at d = 12,
λ = (19, 7, 2⁵), n = 3.

**Check:**
- a = 6 by the cycle index and Murnaghan–Nakayama (3560 types);
- the raising operator kills all six;
- the rank is 6 on generic cubics.

### S-003 `[TPC]`, `[COMP]`

**Statement.** a = 6, the ideal multiplicity is 1, K₃ = 5 and q = 6. The separating equation is
Ψ = 2P₀ + 21P₁ + 7P₂ + 35P₃ + 7P₄.

**Proof.**
- f divides H on seven-variable determinant pencils, because the Hessian of det₃ has rank six at a rank-two matrix.
  That gives K ≤ 5.
- The evaluation minors give K ≥ 5 and q = 6.
- Ψ vanishes identically when f divides H.
- The evaluation ranks are 5 on det₃ and 6 on per₃.

Neither F-016 nor Landsberg–Manivel–Ressayre's values are needed. LMR (Comment. Math. Helv. 88 (2013), p. 476) is then
cited only as known.

**Good for:** the multiplicity-not-occurrence example of GCT_KRON F-025, with both sides explicit. This is prompt 56's
B2. The paper must say exactly which of "six ambient copies, one in the ideal, six on the permanent" LMR already print.

## 2. The padded question

### S-004, the padding conventions `[TPC]`, conditional on F-009, M-008, M-013, M-014, M-019, A-025

**Statement.**
- Internal padding x₁₁^{n−m}·per_m has ≤ m² essential variables.
- Independent padding z^{n−m}·per_m has ≤ m² + 1.
- With independent padding the row cap is m² + 1.
- GCT_KRON's BIP-range conditions stand, except M-019's threshold, which becomes λ₂ ≥ 238356708. The value 239063403
  holds only for r ≤ m².

**Consequence.** For m < n both caps are below n², so every GCT_KRON O-030 member with u > 0 has q = 0 under either
padding.

### QC-014 `[TPC]`, with the symbolic check det M = z³Φ and Jacobian rank 35 `[COMP]`

**Statement.**
- ℓ^{n−4}q ∈ D_{n,4} for every quaternary quartic q and every n ≥ 7.
- So q_λ ≤ K_n(λ) in every degree, for every λ with ≤ 4 rows, at (4, n), n ≥ 7.
- That is: no ≤ 4-row multiplicity obstruction exists for the padded per₄ against det_n, n ≥ 7.

**Proof.** A dominant morphism of parameter schemes, then closedness. This gives an inclusion of cones and a surjection
of coordinate rings.

### QC-019, an obstruction at (8, 9)

**Statements.**
- The upper bound K₉(9d − 3b, b, b, b) ≤ C(3b + 151, 151) `[TPC]`, with tangent rank 92 and slice dimension 151.
- The lower bound q(sλ₀) ≥ C(s + 155, 155), for λ₀ = (216, 9, 9, 9) in degree 27. It needs 155 (S-025), respectively 156,
  algebraically independent padded functions `[bg]`. The Jacobian certificate (a minor equal to 13 mod 101) was not
  recomputed.
- Hence, for z·per₈ against det₉, q(sλ₀) > K₉(sλ₀) at s = 67·28³⁸, d = 27s `[TPC]` on the comparison. It is
  conditional on the 156-function certificate and on c₈ = 165.

**Good for:**
- A named weight and degree for an obstruction in CUE_GCT's certified range.
- A much shorter proof and a smaller bound than CUE_GCT G-11, G-13, G-17.

**Not for:** it gives no equation.

### Other findings `[stmt]`

- **QC-021:** I(D_{n,r})_d = 0 for n ≥ 6 and d ≤ 10. It rests on a published degree-five seed that the run did not rerun.
- **Complete determinant restrictions:** OBS-011 to 016, QC-015 to 018, QC-020, QC-026 to 029, S-026, S-028. These are
  degree and tail boxes at (8, 9) and (17, 23).
- **Refuted upper-bound routes, null pencils, semistable centres, arc constraints:** QC-022 to 025, S-023, S-024,
  S-029 to S-037.

### The state of the padded main questions Q1a and Q1b (as the run records it)

**At (8, 9).** K = a holds in the boxes proved so far. A four-row obstruction there needs:
- second row ≥ 15;
- third row ≥ 12 if the second is 15 or 16;
- third row ≥ 7 if the second is 17 to 27.

**At (17, 23).** The second row must be ≥ 20, among further conditions.

**What is still open.** No padded separator or equation has been found. 4,214 labels remain.

## 3. Border rank (carried from BR_PENCIL's line) `[stmt]`

- **BR-002:** BR(det₄), BR(per₄) ≥ 43 in every characteristic.
- **BR-006:** μ₁₀ ≥ 18 for det, hence BR(det₄) ≥ 44 in characteristic 0. The first part of its proof was read.
- **BR-012 to BR-057:** exclusions of permanent ten-plane orbits. 10 orbits (6,048 subsets) remain for per's 44.

## 4. Open rows

| Row | Gate |
|---|---|
| Q1a, Q1b | An explicit four-row separator and degree at (8, 9) and (17, 23), inside the boxes above |
| QC-019 | Recompute the 156-function Jacobian certificate |
| QC-021 | Read the published seed and the proof |
| 44 for per₄ | The 10 remaining ten-plane orbits |
| A-035, A-036 | Their proofs. Our intakes have only the statements |

## 5. Where the results went

**Prompt 56 / 56c, GCT write-up (Paper B):**
- **B1:** replace the ray by GCT_KRON O-030.
- **B2:** S-002/S-003 explicit on both sides.
- **B3:** state the padding convention (S-004).
- QC-014 is offered as optional, because prompt 56 says "claim nothing about padded obstructions".

**Hexagon:**
- **H13:** now O-030 with S-002/S-003.
- **H14 with QC-019:** gated on its certificate.
- **H03:** BR-002/BR-006, after an intake of them.
- **QC-014:** a possible small note, gated by a literature check on the determinantal complexity of quaternary quartics.

**pequalnp fleet**, one line per result (JOINT_GCT_LEMMA_SPACE):
- **Q1a, Q1b.** The *separations* are already settled. **L-gct-010** (checked, Landsberg–Manivel–Ressayre m²/2), with
  **L-gct-006** and its converse (our survey item), gives border dc(perm₈) ≥ 32 > 9 and border dc(perm₁₇) ≥ 144.5 > 23.
  Only the explicit obstruction is open.
- **S-002, S-003.** They reconstruct LMR's degree-12 example, which shows border dc(perm₃) ≥ 4. **L-gct-010** gives ≥ 5.
  S-003's Hessian step is the checked **L-gct-012** at n = 3 (the Hessian of det_n has rank ≤ 2n on its zero set).
- **S-004.** It uses the same padding convention as their `paddedPerm`: the pad variable sits outside the m² permanent
  variables, so the cap is m² + 1. It is parallel to **L-gct-011**.
- **QC-014.** Parallel to **L-gct-010**: at (4, 7) border dc ≥ 8 separates, yet no ≤ 4-row multiplicity obstruction
  witnesses it. It is consistent with **L-gct-024**: padded quaternary quartics have border dc ≤ 7.
- **QC-019, S-025.** The same (8, 9) separation as **L-gct-010**.
- **Our border bound against theirs.** The fleet's checked **L-gct-070/072** ((2m² − 10m + 11)/3) and **L-gct-074**
  (superquadratic) improve the "m²/2" that our GCT texts cite.
