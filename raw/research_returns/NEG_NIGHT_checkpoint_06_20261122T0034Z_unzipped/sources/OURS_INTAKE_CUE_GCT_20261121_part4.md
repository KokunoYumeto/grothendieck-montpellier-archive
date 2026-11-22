# Intake of CUE_GCT (prompt 36), part 4: checkpoints 05 to 08, the run's final return, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent a17221e5; launched by the main session, Claude Opus 5.5 at effort max).

The run is GPT-6 Astra (ChatGPT Pro mode), run CUE_GCT_20261121_R1. Its newest return is checkpoint 08 of 06:49 UTC,
written right after its fourth scheduled movement review, which found movement. By the user's rule the run has ended
at that return.

## 0. What was read

- **Return folder:** `research_returns\CUE_GCT_checkpoint_08_20261121T0649Z_unzipped`. Part 3 read checkpoint 04.
- **New since checkpoint 04.** From `deliverables\LEDGER.md` (all dated blocks 04:12-06:39 UTC and the second,
  third and fourth reviews):
  - R-24 to R-33;
  - G-19 to G-28;
  - I-35 to I-44;
  - P-16 to P-20.
- **Read:**
  - `QUESTIONS.tsv`, rows RQ-26 to RQ-37 and G-Q24 to G-Q29;
  - the statement of R-27 and the opening of its proof (`CUE_GCT.tex`, lines 4773-4815);
  - R-22's statement and its proof through steps 1-2 (lines 3215-3330): the typed staircase, the simultaneous
    supports and cofactor factorizations, and the second-order local defect P_j − D_j = ε²E_j + O(ε³).
- **R-22's proof not read to its end, by choice.** The final supersedes R-22: R-27 proves the exact value
  c_m = min(C(m+3,3), 4m² − 2m + 2), so R-22's lower bound 4m² − 20m^{3/2} + 2 no longer carries any conclusion.
  The operative chain for H14 is now R-23 → R-26 → R-27 (with R-24/R-25 for m = 17, 18). I spent the round's budget
  on BR_PENCIL's 43 rather than on a superseded bound.
- **Computation, mine** (`scratchpad\kron3\quaternary_dominance.py`, rerun for m = 9 and 10): see section 2. In part 2
  I confirmed c_m = C(m+3,3) for m = 4-8.

## 1. Changes to parts 1-3

- **R-14 unchanged** (its statement is identical in checkpoint 08). It is the criterion every padded result uses.
- **Superseded, not withdrawn.**
  - R-22's lower bound is superseded by R-27's exact dimension.
  - R-20/R-22's rectangular threshold (m ≥ 8,000,001, then 2025) is superseded by R-26 (m ≥ 14) and G-20 (threshold 14
    sharp).
- **Parts 1-3 unchanged.** G-01 to G-06, P-11 and I-18 are unchanged.

## 2. Verdicts on the new findings

| id | statement | check | verdict |
|---|---|---|---|
| R-27 | exact four-variable dimension c_m = min(C(m+3,3), 4m² − 2m + 2) for all m; ε_m = 0 for m ≥ 17 | statement and proof opening; the run reports a root reading and an independent finite coefficient/Toeplitz reconstruction | not read in full |
| R-22 | c_m ≥ 4m² − 20m^{3/2} + 2 (m ≥ 99); every fixed n/m < sqrt 2 | proof read through steps 1-2 (set-up, supports, local defect), no fault found there | partly read; superseded by R-27 |
| R-24, R-25, R-26 | exact c_17 = 1124 and c_18; the uniform linear defect at most 6(m − 18); rectangular range from m ≥ 14 | statement | not read in full |
| G-20 | for m ≥ 17, a four-row direction has an eventual gap iff n² ≤ 2m² − m + 1 | statement | not read in full |
| G-21 | dim P_{m,r} = rm² − 2m + 2 for m ≥ 17, r ≥ 4 | statement | not read in full |
| G-22 to G-28 | higher-row phases. The exact rectangular range m < n < rm/(r−1) for 4 ≤ r ≤ m (G-24); all fixed nonrectangular directions through 2m rows classified (G-26 to G-28) | statement | not read in full |
| R-28 to R-33 | higher-variable determinant dimensions; stable common points; finite stabilizers | statement | not read in full |
| I-35 to I-44, P-16 to P-20 | isolation subclasses (balanced width-three through 12 variables, 13 away from characteristic 2) and purity gates | statement | not read in full |

**My computation:** c_9 = 220 = C(12,3) and c_10 = 286 = C(13,3), confirming R-13 at m = 9 and 10. With part 2
(m = 4-8), R-13 is now independently confirmed for m = 4-10. That covers the padded pairs (8, 9), (9, 10) and
(10, 11).

**Counts:** 1 partly read (R-22); about 40 at statement level; none refuted.

## 3. What the run settled in the end, and what it left open

- **Settled.**
  - *Four-row multiplicity obstructions under padding.* Through R-14 with the exact c_m (R-27) and G-20, for every
    m ≥ 17 a four-row gap exists in large degree exactly when n² ≤ 2m² − m + 1, that is up to n ≈ sqrt 2 · m. The
    finite cases m = 8-16 come from R-13.
  - *The boundaries of the dimension method.* It is exactly characterized: no four-variable route beyond sqrt 2,
    and higher r gives smaller ratios, rm/(r−1) for rectangles.
  - *The higher-row phase structure* (G-22 to G-28).
  - *The zero-statistics dependency audit* (P-Z, unchanged).
  - *A run of isolation subclasses* (fixed width, balanced width three up to 12-13 variables).
- **Open.**
  - *Explicit gaps.* The four-row gaps are non-explicit in degree (G-10/G-13 give huge bounds).
  - *Padding beyond sqrt 2* needs a different method. The dimension method cannot pass it (RQ-26).
  - *Polynomial-in-width ROABP hitting sets* (I-Q01) and their GCT V consequence (I-Q13).
  - *The purity-to-ROABP construction* (P-08 encoding).
  - *Cote 133 ink-level readings*: the scan images were not attached.

## 4. Scope of the two proofs

Unchanged. The review states "No additional Dirichlet GRH implication is inferred". Masullo dependencies stay
conditional (Gao-Zhao). No overclaim.

## 5. Integration

- **The joint picture with GCT_KRON** (KRON part 3, section 5):
  - explicit unpadded obstructions (KRON A-030/A-034);
  - non-explicit four-row multiplicity obstructions exactly up to n² ≤ 2m² − m + 1 (CUE);
  - necessary conditions in the BIP range (KRON);
  - no occurrence obstructions for n ≥ m^25 (BIP).
- **The bridge attack.** Take KRON's A-034-type explicit covariants into CUE's certified range at (m, n) = (8, 9),
  where a gap provably exists. There KRON's exclusions (λ_1 ≥ d(n−m)+4 from CUE G-15; KRON's row conditions) prune
  the candidates.
- **In Grothendieck's frameworks.** R-23 and R-27 are a Tor-independence statement: the vanishing of
  Tor_1(R/J_m, S)_m for the restriction to four variables (SGA 6 dictionary in the paper). G-21 is its higher-r form.
  These are clean statements in our language and belong with the D-S6 dictionary of the paper.

## 6. What the successor prompt needs

1. **Main question: explicit obstructions in the certified range.** At (m, n) = (8, 9), and at m = 17, n = 23
   (n² ≤ 2m² − m + 1 = 562, so n ≤ 23): an explicit four-row λ, a degree, and a separating equation. Use KRON A-034's
   ray-algebra technique and KRON's exclusions.
2. **Beyond sqrt 2.** The dimension method is capped. Ask for representation-theoretic multiplicity comparisons that
   do not come from a dimension count: for instance the ranks of explicit orbit-coefficient matrices (R-05/R-06,
   G-04) on families of λ.
3. **Isolation.** The growing-width gate I-Q01 with the shared-seed coefficient-matroid bridge. Attach I-31 and
   I-41 to I-44 as the base.
4. **Rerunnable certificates.** R-13 (m = 9-16), R-24/R-25 (m = 17, 18), and R-27's fixed Toeplitz certificate, in a
   form an independent script can check.
5. **Provenance:** GPT-6 Astra (ChatGPT Pro mode). No ways out.

## 7. Hexagon readiness

**H14 (four-row multiplicity obstructions under genuine padding), now "exactly for n² ≤ 2m² − m + 1 when m ≥ 17, and
in the R-13 finite range".**
1. *Complete:* yes, as written by the run. R-14 plus R-27 plus G-20.
2. *Self-contained:* yes. The inputs are Beauville (G-05), published; the rest is proved.
3. *Stable:* yes. The run has ended, and the dimension method's ceiling is exactly located, so nothing of ours will
   soon supersede this. The literature search has still not been done.
4. *Checked:* only partly.
   - *Done:* my proof check of R-14; my computation of c_m for m = 4-10, which gives the cases (8, 9), (9, 10) and (10, 11).
   - *Not done:* the asymptotic range rests on R-23, R-26 and R-27, which I have not read; the run reports root and
     independent readings.
5. *Of interest now:* high if new (GCT).

**Gates left:** (a) the literature search (Kadish-Landsberg, Landsberg's book chapters 8-9, Dörfler-Ikenmeyer-Panova,
Ikenmeyer-Kandasamy, Gesmundo-Ikenmeyer-Panova); (b) an intake proof check of R-23, R-26 and R-27, with
recomputation of the m = 17 certificate (RQ-28: minor of order 88 mod 101). A narrower post, R-14 with the finite range
m = 8-16 (my computation covers m = 4-10), would need only gate (a) and the check of R-13 for m = 11-16.

**H03 and H13.** Not affected by this run.
