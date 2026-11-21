# Intake of GCT_PLETH, part 3: checkpoint 06 (21 Nov 2026)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the main session's request (Claude Opus 5.5 at
effort max). The run is GPT-6 Astra (ChatGPT Pro mode); the run says its effort is not exposed. Part 2 covered
checkpoint 04. Work file: `agent_notes\20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md`.

## 0. Return read and scope

- **Folder:** `research_returns\GCT_PLETH_checkpoint_06_20261121T0331Z_unzipped`, the newest present (03:31 UTC). The
  paper is about 25,000 lines and the QUESTIONS file has 284 rows. The run is still going. Formal review 02
  (04:01 Berlin) recorded "Movement: YES" with a zero no-movement count. R-036 is marked active and unchecked.
- **Read since checkpoint 04:** the LEDGER entries from "Research update after review01" to "Checkpoint06", with the
  open-row table of review 02. I also read:
  - G-031 from `work/root/all_five_row_support_report.md` (its first page: the decision rule);
  - the statement of R-031 and its source paragraph (paper l. 24753-24830 and l. 13378-13400).
- **Checked by computation:** G-028's strict-chamber rule, which G-031 uses for every shape with all four gaps
  positive. I enumerated every λ ⊢ 5n with five rows and all gaps ≥ 1, for n = 2, 3, 4: that is 38 shapes, each
  with all seven μ ⊢ 5, so 266 coefficients. I computed each coefficient p_{μ,(n)}^λ independently (power-sum
  plethysm with the S₅ character table; `chk/g028.py`) and compared its vanishing with the rule.
  **All 266 agree.** The checked set includes the predicted zeros at g = (1,1,1,1) for both extreme labels, at
  g = (1,2,2,1) and (2,1,1,2) for the effective trivial label, and the parity swap μ ↦ μᵗ for odd d.
- **Read at statement level:**
  - G-024 to G-027, G-029, G-030, G-031 (beyond the strict-chamber rule);
  - T-045 to T-053, including T-052 (a charged-oscillator realization of every outer degree) and T-053 (the frame
    Rees algebra as an equal-charge incidence subalgebra);
  - R-027 to R-035, including R-031 (the full canonical rank law for target outer degree five) and R-035 (the
    second-row ≤ 2 band).
- **Part 1, the addendum and part 2 are unchanged in checkpoint 06.** The QUESTIONS states of T-002, T-012, T-013,
  T-037, G-021 and A-001 to A-023 are the same, and nothing is withdrawn.

## 1. Verdicts

- **G-031** (a decision procedure for the nonvanishing of every p_{μ,(n)}^λ, μ ⊢ 5, in every inner degree): a fixed
  344-vector table, normalization along two stable directions, and G-028 for the strict chamber.
  - **Confirmed by computation for the strict-chamber part** (G-028), on all 266 cases with n ≤ 4.
  - The wall and multiple-wall parts (the 344-node catalog) are statement level. The run reports an independent
    comparison of all 344 rows.
- **R-031** (the actual canonical rank law with target outer degree five: injective for n ≤ 4, kernel exactly the
  eight labels of (OF.4) at n = 5, surjective for n ≥ 6): **background, correctly cited.** It assembles
  Cheung-Ikenmeyer-Mkrtchyan, *Symmetrizing tableaux and the 5th case of the Foulkes conjecture*, arXiv:1509.03944,
  Theorem 6(a),(b), and Ikenmeyer, *On McKay's propagation theorem*, arXiv:1509.04957, Theorem 1.3. The n ≤ 4 step is
  the run's own gap-sum argument. The run claims no novelty for the rank law; I agree. I did not open the cited
  papers.
- **R-035** (the second-row ≤ 2 band, determined exactly through an explicit determinant-square scalar),
  **T-045, T-046, T-050, T-051** (closing the order-one, two-below and three-below families of outer degree five),
  **G-027 and T-049** (the flag-model row closed by an exact fat-arrangement product ideal): statement level, no
  fault seen.
- **T-052 and T-053** (the charged-oscillator realization of every outer degree, and the frame Rees algebra as the
  nonnegative equal-charge subalgebra of a quadratic incidence ring, with at most 2^r bounded polytopes per weight
  space): statement level. T-053 also proves that no monomial initial ideal in these coordinates keeps the literal
  S_m action; that locates exactly why the finite normalizer projector remains.

**Counts for part 3:** 1 confirmed by computation (G-028's strict-chamber rule inside G-031); 1 background correctly
cited (R-031); 0 refuted; 0 gaps; 0 withdrawn; about 25 at statement level.

## 2. What is new

- **G-031** (complete nonvanishing for outer degree five, decidable in polynomial bit complexity): new as stated,
  read only in part. The support of plethysm coefficients is NP-hard in general (Fischer-Ikenmeyer, with inner
  degree 3 fixed). Here the *outer* degree is fixed, which is a different regime, so there is no conflict.
- **R-031** is known (Cheung-Ikenmeyer-Mkrtchyan, Ikenmeyer).
- **R-035** and the R-027 to R-034 families extend the explicit picture of the Hadamard-Howe map below the square
  bound. Statement level.
- **T-052/T-053** make the oscillator (theta) side of the prompt exact for every outer degree. This is the "dual
  pair" object that Q-ALPOGE needs on the representation side.

## 3. Scope of the two proofs

Unchanged: no use of Alpöge or Masullo. Q-ALPOGE and Q-MASULLO remain input gates.

## 4. How the findings bear on the open problems, and the attack they open

1. **Positivity for outer degree five.** Nonvanishing is now decided completely (G-031). The coefficient formula is
   open only on k ≥ 3, 0 ≤ c ≤ 2k−4, with its zero sets already known.
   **Next attack:** apply T-053's incidence-algebra polytopes (at most 2^r per weight space) with the explicit
   Specht projector in this remaining region. The projector, not the polytopes, is the last non-positive step, so
   the target is a positive formula for the S₅-isotypic decomposition of a direct sum of polytope lattice points.
   That is a combinatorial-representation problem of fixed size.
2. **Foulkes-Howe.** For outer degree five the rank law is now complete (R-031, known), and for second row ≤ 2 in all
   outer degrees (R-035). The varying-rank gate stays Q-MAP's annihilator in N_r ⊗ Sym^{r²−1}.
3. **The theta comparison (Q-ALPOGE).** T-052 gives the compact Howe-pair side for every outer degree. ALPOGE_GCT's
   P-F51 gives a definite-U₃ theta source on the automorphic side, for cubic threefolds. The two runs now meet: the
   comparison to build is between T-052's charged oscillator for (U(V), U(E)) and ALPOGE_GCT's ball-quotient theta
   lifts, for inner shape (3).

## 5. Integration (no edits made outside this folder)

- Study edits: unchanged from part 1 and the addendum.
- **Successor prompt:** settled list adds G-031 (after a full reading of the wall catalog) and R-031 (as known,
  cited). Main targets: the remaining outer-five region (4.1), and the cross-run comparison of 4.3.
- **The project's terms:** G-031 and T-053 are statements about the Rees algebra of the ideal sheaf of the simplex
  points of P(h₅) = P³: graded pieces of ⊕_j H⁰(I_Z^j(c) ⊗ S_β Q), the coherent-sheaf formulation of part 2. The
  oscillator form T-052 is the compact Howe pair realization (T-001, T-002) carried to every outer degree.

## 6. Hexagon readiness

- **Outer degree four and five positive formulas and support (T-037, G-021, G-031):** not ready. Outer degree five
  still has an open coefficient region. My checks are computational only (60 + 50 + 266 cases). A literature search
  is needed on h₄[h_n] and h₅[h_n], and on Foulkes-type support results.
- **H02:** not touched by this run.
- **H03:** not touched by this run.
