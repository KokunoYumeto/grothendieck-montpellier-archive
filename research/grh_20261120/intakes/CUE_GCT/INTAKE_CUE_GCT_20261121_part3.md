# Intake of CUE_GCT (prompt 36), part 3: checkpoint 04, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high, the same agent that wrote parts 1 and 2 (launched by the main session, Claude
Opus 5.5 at effort max). The run is GPT-6 Astra (ChatGPT Pro mode), run CUE_GCT_20261121_R1, still going.

## 0. What was read

- **Return folder:** `research_returns\CUE_GCT_checkpoint_04_20261121T0349Z_unzipped`, checkpoint 04 of 03:49 UTC,
  the newest present when I started. Part 2 read checkpoint 03.
- **New since checkpoint 03.** From `deliverables\LEDGER.md` (the blocks of 03:28, 03:36 and 03:42 UTC, and the
  first scheduled movement review of 03:49 UTC, which found movement and carries a complete row table):
  - G-18;
  - R-22, R-23;
  - I-34;
  - P-14, P-15.
- **Read:** the statement of R-22 (`CUE_GCT.tex`, lines 3193-3235) and the paper's opening summary (line 53).
- **Not read in full:** the proofs of G-18, R-22, R-23, I-34, P-14 and P-15.
- **No new computation of mine.** Part 2's c_m computation (m = 4-8) is unaffected.

## 1. Changes to what parts 1 and 2 checked

- **R-14: unchanged.** R-22 and G-17/G-18 use it as before.
- **The H14 core: unchanged.** The finite range certified through R-13 (m = 8-16, with my independent recomputation
  for m = 4-8) stands.
- **Parts 1 and 2: unchanged.** No earlier finding is withdrawn.

## 2. Verdicts on the new findings (statement level)

| id | statement | verdict |
|---|---|---|
| R-22 | for b ≥ 3, m ≥ 8b: c_m ≥ 2m² + 2 + (2b−2)hT; for m ≥ 99, 4m² − 20m^{3/2} + 2 ≤ c_m ≤ 4m² − 2m + 2. Every fixed n/m < sqrt 2 eventually has four-row gaps (R-14), and the rectangular boundary m < n < 4m/3 holds for every m ≥ 2025 | not read in full. The arithmetic of the threshold is consistent: m ≥ 100/(2−ρ²)² with ρ = 4/3 gives m ≥ 100/(2/9)² = 2025 |
| R-23 | the four-variable dimension defect is one degree-m Tor_1 group; earlier Tor_1 degrees vanish generically; full regular-sequence restriction is refuted for m = 3-16 | not read in full |
| G-18 | gaps at every sufficiently large stretch of each strict four-row direction, including rectangles; an all-integer multiplicity ratio; eventual absence of occurrence obstructions along each fixed four-row direction | not read in full |
| I-34, P-14, P-15 | bounded local nullity; scalar bridge conditions for rank-one/full-rank factors; a one-pair width-three refutation | not read in full |

**Counts:** 0 read in full, 6 at statement level, none refuted.

## 3. What is new, and how it bears

- **The padding ratio.** R-22 takes H14's existence of four-row multiplicity gaps from ratios below sqrt(5/3) to every
  fixed ratio below sqrt 2. The run states the exact ceiling of the method: the dimension method cannot reach sqrt 2
  or superlinear padding (row RQ-26).
  - *The obstacle.* The four-variable projection dimension is at most 4m² − 2m + 2, against 2n² + 2 for the
    determinant.
  - *The next attack.* Use five or more variables. The projection to r variables compares dim P_{m,r} with the
    r-variable determinantal locus. The run has not tried r > 4.
- **R-23.** It locates the remaining exact-dimension gate in one Tor_1 graded piece (SGA 6 Tor-independence
  dictionary). This is a clean statement in our frameworks: Tor_1(R/J_m, S)_m.
- **G-18's "eventual absence of occurrence obstructions along each fixed four-row direction".** It is in the same
  spirit as Bürgisser-Ikenmeyer-Panova, but in the small-padding range. It shows the gaps are multiplicity gaps, not
  occurrence gaps.

## 4. Scope of the two proofs

Unchanged: no use of Alpöge or Masullo in the new findings. The review states "No additional Dirichlet GRH implication
is inferred".

## 5. Integration and prompt updates

- **Integration.** Add R-22 to the shared ledger of the row and padding gate proposed in part 2. KRON gives exclusions;
  CUE now gives existence for every n/m < sqrt 2, non-explicit.
- **Prompt update for the successor.** Make the five-variable projection the main route past sqrt 2. Keep the request
  for rerunnable certificates (R-13 for m = 9-16, R-22's grid choice).

## 6. Hexagon readiness

- **H14 (four-row multiplicity obstructions under padding).** Strengthened, not changed in kind.
  - *What changed.* The claimed range is now every fixed n/m < sqrt 2 (R-22, unread). The core R-14 plus the
    finite certified range (m = 8-16) is unchanged and checked.
  - *Gates left.* The literature search; and the run's final, because the range keeps moving. When posted, the post
    should state R-14, the certified finite range, and R-22's range only after its proof is read.
- **H13 and H03.** CUE_GCT checkpoint 04 does not bear on them.
