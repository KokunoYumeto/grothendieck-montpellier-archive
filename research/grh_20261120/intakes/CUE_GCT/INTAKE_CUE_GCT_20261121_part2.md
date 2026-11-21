# Intake of CUE_GCT (prompt 36), part 2: checkpoints 02 and 03, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high, the same agent that wrote part 1 (launched by the main session, Claude Opus
5.5 at effort max).

The run is GPT-6 Astra (ChatGPT Pro mode), run CUE_GCT_20261121_R1, still going. Its three-hour review is due about
03:50 UTC.

## 0. What was read

- **Return folder:** `research_returns\CUE_GCT_checkpoint_03_20261121T0304Z_unzipped`, checkpoint 03 of 03:04 UTC, the
  newest present when I started. Part 1 read checkpoint 01.
- **What is new since checkpoint 01.** Read from `deliverables\LEDGER.md` (the blocks of 02:04-02:57 UTC) and
  `QUESTIONS.tsv` (RQ-19 to RQ-25, G-Q10 to G-Q18, and the I and P rows):
  - R-15 to R-21;
  - G-10 to G-17;
  - I-21 to I-33;
  - P-12, P-13.
- **Read in full, with proof:**
  - R-14, the dimension criterion that survives padding (`CUE_GCT.tex`, from line 1216). It was in checkpoint 01
    but was not read in part 1. Every padded result of checkpoints 02-03 rests on it.
  - The statements of R-16 and G-11.
- **Read at statement level:** the rest.
- **Computation, mine** (`scratchpad\kron3\quaternary_dominance.py`):
  - *What it computes.* The Jacobian of (A_1, ..., A_4) ↦ per_m(Σ x_k A_k), at a random point mod 2^61 − 1, has rank
    C(m+3, 3) for m = 4, 5, 6, 7, 8: ranks 35, 56, 84, 120 and 165.
  - *What it shows.* The quaternary permanent image is every quaternary form of degree m, so c_m = C(m+3, 3). This
    independently confirms R-13 for m = 4-8.
  - *The consequence.* At m = 8, c_8 + 3 = 168 > 2·9² + 2 = 164, so R-14's criterion holds for the padded per_8
    against det_9.

## 1. Changes to what part 1 checked

- **G-01 to G-06, P-11, I-18: unchanged.** Their statements open identically in checkpoint 03; the line numbers moved
  (G-05 is now at line 3251, I-18 at 6199, P-11 at 9245).
- **The dependency table (P-Z01 to P-Z05): unchanged.** The LEDGER says "Source-specific RH predicates and support
  ranges retained".

## 2. Verdicts on the new and newly read findings

**R-14, a dimension criterion for four-row multiplicity obstructions under padding.** Confirmed: targeted proof
check plus computation.
- *Statement.* If c_m + 3 > 2n² + 2, with c_m = dim of the quaternary permanent image P_{m,4}, then for every large
  degree d some λ ⊢ nd with exactly four rows has m_λ(z^{n−m} per_m) > m_λ(det_n).
- *Proof checked step by step.*
  1. The projection of the padded orbit closure to four variables is exactly Z_{m,n} = {ℓ^{n−m} q}, of dimension
     c_m + 3. This uses generic injectivity of (ℓ, q) ↦ ℓ^{n−m} q, since a general q is irreducible
     (x_1^m + x_2^{m−1}x_3 is Eisenstein at x_3).
  2. The quaternary determinant image has dimension at most 2n² + 2 (G-06, confirmed in part 1).
  3. The Hilbert polynomials have degrees c_m + 2 and at most 2n² + 1, so in large degree some GL_4 multiplicity is
     larger on the permanent side.
  4. Four-row GL_{n²} multiplicities equal those of the projected images. Highest-weight vectors use only the first
     four coefficient variables, and I(Y) ∩ C[first four coefficients] = I(π(Y)), because π(Y) ⊆ Y is a limit of
     torus elements.
  5. G-05 removes three rows or fewer.
- *Consequence.* With R-13 and my computation, multiplicity obstructions exist for the padded per_m against det_n at
  (m, n) = (8, 9), (9, 10), ..., (16, 17-22), as listed in R-14's table. The partitions and degrees are not explicit.

**R-13 (c_m = C(m+3, 3) for 4 ≤ m ≤ 16, failure for m ≥ 17).** Confirmed by my computation for m = 4-8. For
m = 9-16 the run's certificates (3,348,864 entries, rechecked by the run's own second method) were not rerun by me. The
failure from m = 17 is consistent with the dimension bound 4m² − 2m + 2 < C(m+3, 3) at m = 17 (1124 < 1140).

**Read at statement level only:**
- R-15 to R-21: R-16 to R-20 push the padding ratio to every ρ < sqrt(5/3), and R-20 gives rectangular gaps for every
  m < n < 4m/3 when m ≥ 8,000,001;
- G-10 to G-17 (G-12 is a refutation: no rectangular gap for n ≥ 4m/3; G-14 and G-15 are jet dominance and give
  λ_1 ≥ d(n−m)+4);
- I-21 to I-33;
- P-12, P-13.

The R-16 to R-20 dimension lower bounds, which feed R-14, are the next proofs to read.

**Counts:**
- 1 confirmed by targeted proof check and computation (R-14);
- 1 confirmed by computation in part of its range (R-13, m = 4-8);
- about 45 at statement level;
- none refuted. Part 1's verdicts unchanged.

## 3. What is new

- **R-14 with R-13: four-row multiplicity obstructions under genuine padding.** These are representation-theoretic
  multiplicity gaps for ℓ^{n−m} per_m against det_n at n = m+1 (m ≥ 8), proved by a dimension count of four-variable
  projections. R-16 to R-20 claim them for linear ratios n/m up to sqrt(5/3), and up to 4m/3 for rectangular λ.
  - *Novelty.* The existence of multiplicity obstructions in a genuinely padded range has, as far as I know, not been
    published. The known results are negative for occurrence obstructions at large padding (Ikenmeyer-Panova
    n > 3m^4; Bürgisser-Ikenmeyer-Panova n ≥ m^25). For multiplicity obstructions the general padded question is
    open. But the argument is short, and an equivalent dimension argument may exist in the literature. A search is
    needed before anything is called new. Search first in:
    - Kadish-Landsberg, *Padded polynomials, their cousins, and geometric complexity theory*;
    - Landsberg's *Geometry and Complexity Theory*, chapters 8-9;
    - Ikenmeyer-Kandasamy (2020);
    - Gesmundo-Ikenmeyer-Panova;
    - Bürgisser's survey.
  - *Bearing on GCT.* It does not separate complexity classes. Mignon-Ressayre already puts per_m outside Det_n for
    n < m²/2. What it adds is the representation-theoretic witnesses that GCT's programme asks for, in a padded
    range.
- **Two runs on the same gate.** G-14 and G-15 (jet dominance of determinant pencils) are the same technique as
  GCT_KRON's M-013, F022 and M016, reached independently. The two runs approach the middle range from opposite sides:
  - GCT_KRON excludes obstructions with few rows or short second rows, in the BIP range;
  - CUE_GCT proves non-explicit four-row obstructions exist at small linear padding.

## 4. Scope of the two proofs

- **The new statements use neither Alpöge nor Masullo.** P-12 says "no extra GRH input". The zero-statistics table
  is unchanged (part 1, section 3).
- **No overclaim.** R-14 to R-20 are stated as existence results with non-explicit degree (except G-11/G-13's
  explicit but huge bounds), and IMPLICATIONS keeps them apart from complexity separations.

## 5. Integration

1. **GCT_KRON.** Its QMMAIN row ("compare all remaining actual multiplicities") and CUE_GCT's RQ-19 to RQ-24 are two
   sides of one question: for which (m, n) do multiplicity obstructions exist? Put them in one shared ledger:
   - KRON's exclusions: the staircase, M-006 to M-020, O027;
   - CUE's existence results: R-14 to R-20, G-16, G-17;
   - the explicit unpadded families: KRON A-030, F-025.

   *The attack this opens.* Make the four-row gaps explicit at (m, n) = (8, 9). The degree is bounded by G-10 and G-13.
   Then test them against KRON's exclusions, which those gaps must satisfy (λ_1 ≥ d(n−m)+4 from G-15; KRON's row
   conditions).
2. **Grothendieck's frameworks.** R-14 is a statement about the Hilbert polynomials of two projective varieties: the
   multiplication image P³ × P(P_{m,4}) → P(Sym^n C^4) (EGA II 5.5, properness), and the quaternary determinantal
   locus. It sits with the run's Proj/Hilbert dictionary (D-FGA). The run states it there.
3. **H03 (GCT_GINEQ F-23, successor prompt 44).**
   - *No direct bearing.* CUE_GCT bounds dimensions of four-variable projections, not CP border rank.
   - *A tool prompt 44 can adopt.* R-13's method, Jacobian rank of a pencil map at a random point over a large prime,
     is the same certificate that can certify BR seeds for F-23 (dominance of a decomposition map). Prompt 44 can
     use it as is.
4. **Cote 133.** No new transcription notes since part 1. Its rows stand for the transcription record.

## 6. Prompt updates for the successor

1. Main question: make R-14's gaps explicit at (8, 9): the partition, the degree, and an explicit separating equation.
   Then the padding range: the generic-fiber dimension c_m = min(C(m+3, 3), 4m² − 2m + 2) beyond m = 16.
2. Attach GCT_KRON's ledger of exclusions, so the two runs do not re-derive each other.
3. Ask for the certificates of R-13 (m = 9-16) and of R-16 to R-20 in a form an independent script can rerun.
4. Literature check of R-14 (section 3).
5. As before: GPT-6 Astra (ChatGPT Pro mode); no ways out.

## 7. Hexagon readiness

1. **R-14 with R-13 at m = 4-16: four-row multiplicity obstructions under genuine padding (n = m+1, m ≥ 8).**
   - *Tests passed.* Test 1, complete: R-14's proof is written. Test 2, self-contained: its inputs are G-05 (Beauville,
     published), G-06 (proved) and the computed c_m. Test 4, checked: my targeted check, and my independent
     computation of c_m for m = 4-8, which covers the case (8, 9).
   - *Gates left.* Test 3, stable: the literature search (section 3) has not been done. And the run is pushing the
     range (R-16 to R-20), so a post should state R-14 with the certified finite range and wait for the final for
     the linear range.
   - *Interest (test 5).* High in GCT: it is the first (as far as I know) existence of multiplicity obstructions in a
     padded range.
   - **State: one gate (the literature) away, and strong on interest. Flag to the main session now.**
2. **R-16 to R-20 (the linear range).** Not read. Later, after the final.
3. **I-21 to I-33 and P-12, P-13.** These are steps toward the isolation gate. Not candidates alone.
