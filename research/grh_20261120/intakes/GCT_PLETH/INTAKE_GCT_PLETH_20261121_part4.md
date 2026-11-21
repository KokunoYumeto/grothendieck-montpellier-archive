# Intake of GCT_PLETH, part 4: the final return (checkpoint 09, 21 Nov 2026)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the main session's request (Claude Opus 5.5 at
effort max). The run is GPT-6 Astra (ChatGPT Pro mode), with the root and delegated agents; its files say its effort
is not exposed. Parts 1-3 and the checkpoint-03 addendum precede this part. Work file:
`agent_notes\a0805369bae2ebddc_NOTES.md`.

## 0. Return read and scope

- **Folder:** `research_returns\GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped`. Under the user's rule this is the
  run's **final return**. The QUESTIONS file has 341 rows and the LEDGER runs to 06:36 Berlin. Review 04 recorded
  movement; review 05 was due but not reached.
- **Read since checkpoint 06:**
  - LEDGER: every research update and checkpoint entry from "Checkpoint06" to "Exact pair term at the next hook
    boundary";
  - the final states of all Q-rows, and the new rows Q-STABLE-*, Q-*-HOOKS, Q-MAP-*;
  - G036_REVIEW.md and G037_REVIEW.md (opening sections), and `archive/COMPLETE_OUTER_FIVE_REVIEW.md` §5-6.
- **Checked by computation.** I ran the run's own evaluators, after reading them and confirming they only compute and
  read their JSON data, with no writes. I compared them with my independent character computation: power-sum
  plethysm with Murnaghan-Nakayama characters of S_m (`chk/g036.py`, `chk/g037.py`).
  - **G-036**, the complete outer-degree-five formula, through its public router `work/root/outer_five_positive.py`:
    every λ ⊢ 5n with at most five parts for n = 1, 2, plus 40 random λ for n = 3, each with all seven μ ⊢ 5.
    **539 coefficients, 0 mismatches.**
  - **G-037**, the stable-hook formula in varying outer degree, through `work/root/stable_hook_positive.py`: every
    valid (m, a, r, t, n) with m = 3, 4, 5 and n ≤ 5, 4, 3 respectively, with every outer label.
    **790 coefficients, 0 mismatches.** This includes the claim that the coefficient does not depend on n and t
    within the stable family.
- **Read at statement level:** G-038 to G-040, T-054 to T-065, R-036 to R-049, A-088. No proof read in full this
  round.
- **Unchanged from earlier parts:** T-002, T-012, T-013, T-037, G-021, G-028, G-031, and A-001 to A-023 keep their
  states. Nothing is withdrawn.

## 1. Verdicts

| Finding | Statement (short) | Check by this intake | Verdict |
|---|---|---|---|
| G-036 | every p_{μ,(n)}^λ, μ ⊢ 5: ≤ 152 bounded polytopes in ≤ 11 variables, polynomial bit complexity | computation, 539/539 | confirmed by computation; proof not read |
| G-037 | stable hook tails, varying outer degree m: one polytope with ≤ m²+3m−4 variables, polynomial-size #P description for t ≥ 1 | computation, 790/790 | confirmed by computation; proof not read |
| G-038, G-039 | stable tails (a,2) and (a,3), varying m: ≤ C(m,2)+4 (resp. +7) polytopes | none | statement level |
| G-040 | every fixed second part b: polynomial for fixed b (Aschenbrenner, Liang bounds) | none | statement level |
| T-062 to T-065 | hook tails at every fixed ideal order k with a ≥ 2k; a = 2k via Nagel-Trok | none | statement level |
| R-044, R-046, R-049 | h_{n,a} surjective on isotypic components: λ₂ ≤ 4, λ₃ ≤ 3 for n ≥ a (R-044); D + t ≤ 2n+1 (R-046); n ≥ ⌊(D+t−q)/2⌋ (R-049) | none | statement level |
| R-036 to R-043, R-045, R-047, R-048 | explicit canonical-rank families (second row ≤ 3, width-four families, (4,4)) | none | statement level |
| G-032 to G-035, T-054 to T-059 | the pieces of G-036 | covered by the G-036 computation | as G-036 |

**Counts for part 4:** 2 confirmed by computation (G-036, G-037); 0 read in full; 0 refuted; 0 gaps; 0 withdrawn;
about 35 at statement level.

## 2. What the run settled in the end, and what it left open

**Settled.** Proofs by the run with its independent whole-proof reviews; my checks as listed in parts 1-4.
- **Archive, cote 133 (part 1 and the addendum):**
  - A-001: the scan-19 equivariant identity is refuted.
  - A-002, A-003, A-015: the λ-structures on the quadratic Witt and split rings (scan 6).
  - A-004, A-005: Witt descent fails (scan 8).
  - A-006: the struck-out factorization on scan 9.
  - A-007, A-012: scan 28's tensor-power identity holds integrally in exact K₀, while its monomial summands are not
    effective.
  - A-013: scans 24-27, the "summands of H_I" statement is false on Grothendieck's own page.
  - A-020, A-021, A-023: Grothendieck's scan-29 local-ring question has a positive answer for fields and DVRs of
    characteristic 0, and negative answers for F_p and Z_(2)[ε]/(2ε, ε²).
- **Positive formulas for fixed outer degree:**
  - outer degree ≤ 3: G-012;
  - outer degree 4: T-037;
  - outer degree 5: G-036, all values; G-031, all support.
- **Positive formulas in varying outer degree, for families:**
  - stable hooks: G-037;
  - fixed-order hooks: T-062 to T-065;
  - stable two-row tails with a fixed second part: G-038 to G-040;
  - stable width ≤ 6 (Sarkar's range): T-012, T-013.
- **Hadamard-Howe (Foulkes-Howe) canonical map:**
  - full rank law for target outer degree five: R-031, which is known (Cheung-Ikenmeyer-Mkrtchyan; Ikenmeyer);
  - full rank law for second row ≤ 2 and ≤ 3: R-035, R-036;
  - surjectivity ranges, the sharpest being R-049;
  - explicit families below Sra's square bound: R-021 to R-030, R-039 to R-048.
- **The theta side:** the charged-oscillator realization of every outer degree (T-052) and the frame Rees algebra
  (T-053).

**Open (the run's own final gates).**
- **Q-EFFICIENT:** a polynomial-size positive #P description for arbitrary shapes with varying outer degree. Only
  families are done.
- **Q-MAP:** the general canonical-map rank. The critical annihilator injects into N_r ⊗ Sym^{r²−1}.
- **Q-W7:** width seven, the G₂ valuation filtration.
- **Q-ALPOGE:** no comparison map is given in Alpöge's note.
- **Q-MASULLO:** no source was supplied.
- **Q-ARCH-CONTEXT:** archive gates on other cotes (crystalline Lefschetz, the motivic self-duality on PDF pp. 31-43,
  the triangulation reconstruction on PDF pp. 46-51), and the exact class of coefficient rings for scan 29.

## 3. What is new

- **G-036** (outer degree five, complete) and **T-037** (outer degree four) are complete positive formulas with
  polynomial bit complexity. So far as I know they are new as formulas; the literature search is still to be done.
  Earlier work is algorithmic (Chen-Garsia-Remmel; computer algebra for h₄[h_n] and h₅[h_n]) or partial.
- **G-037 to G-040** are, as far as I know, the first polynomial-size #P descriptions of plethysm coefficients for
  infinite families with varying outer degree. That is the regime of Mulmuley's GCT VII Problem 1.1 and of the
  Fischer-Ikenmeyer hardness results, so it needs a careful literature comparison. Known positive formulas with
  varying outer degree include Langley-Remmel's hook results and the Paget-Wildon results on hooks and near-hooks.
- **R-046 and R-049** are new surjectivity ranges for the Hadamard-Howe map, in the size and width of the tail. They
  sit alongside the Brion, McKay, Cheung-Ikenmeyer-Mkrtchyan and Sra bounds. A comparison is needed.

## 4. Scope of the two proofs

Unchanged through the end: no finding uses Alpöge or Masullo. Nothing claims more than its input gives.

## 5. How the findings bear on the open problems, and the attack they open

1. **Positivity for plethysm.**
   - ALPOGE_GCT's final return refutes GCT VI's index hypotheses PH2, SH(a) and PH3 for plethysm.
   - GCT_PLETH's final return shows the positive *counting* side working: fixed small outer degree, and families with
     varying outer degree, both have polynomial-size positive formulas.
   - Together they say that what the flip can still hope for is polynomial-size #P formulas (GCT VII Problem 1.1),
     not small-index saturation.
   - **Next attack:** extend G-040 from fixed b to b varying polynomially. The obstruction is located: the
     Aschenbrenner/Liang Gröbner bounds f(b)(…)^{g(b)} are exponential in b. A positive basis of the finite cokernel
     modules, uniform in b, would remove them. G-040 shows those modules are supported in degrees b−1 to 2b−2 with at
     most b−2 low variables.
2. **Foulkes-Howe.** R-049 gives full surjectivity at n ≥ ⌊(D+t−q)/2⌋. Foulkes' conjecture for (a, n) asks for
   injectivity or surjectivity at n ≥ a. Components with large D are the hard ones.
   **Next attack:** the remaining Q-MAP annihilator, with R-047 to R-049's exact families as base cases.
3. **Theta.** T-052 (the compact oscillator) and ALPOGE_GCT's ball-quotient theta lifts (P-F41, P-F46, P-F51) are now
   both exact. The cross-run comparison for inner shape (3) is the concrete next object.

## 6. Prompt updates: what the successor of GCT_PLETH needs

1. **Settled list, to cite and not redo:** the "Settled" block of section 2, with these intakes as the check record.
   Attach the evaluators `work/root/outer_five_positive.py` (with its data) and `work/root/stable_hook_positive.py`
   as executable certificates, and the reports `complete_outer_five_report.md` and `stable_hook_report.md`.
2. **Main question: Q-EFFICIENT for varying b.** Give a positive #P formula of polynomial size, with b varying, for
   stable two-row tails (a, b), then for three-row tails. The gate is G-040's dependence on b.
3. **Second question: outer degree six.** Through the interpolation reading of part 2: the Cox ring of P⁴ blown up in
   six points, then the same router architecture. Ask for the run's evaluator and certificate style.
4. **Third question: Q-MAP.** The critical annihilator in N_r ⊗ Sym^{r²−1}, for r = 3, 4 first.
5. **Literature first:** require a search on h₄[h_n] and h₅[h_n] formulas, hook and two-row plethysm formulas with
   varying outer degree, and Hadamard-Howe surjectivity ranges. Its results go in a "Prior work" section before any
   novelty statement.
6. **Archive.** Carry Q-ARCH-CONTEXT. For cote 133, ask for the exact class of coefficient rings for scan 29, and
   test the determinant-character conjecture of part 1, section 4.4. The other cotes' gates go to their sweep
   readers, not to this successor.
7. **The project's terms.** Ask, as before, for each family formula to be restated as H⁰ of twisted ideal sheaves on
   the simplex points of P(h_m) (the part-2 dictionary), and as λ-ring identities in K₀ where they apply.
8. **Integrate the late-ledger findings** (G-040 and the pair-boundary results) into the paper, with full proofs.

## 7. Hexagon readiness

- **New candidate (proposed; next free number, H05 is taken), "plethysm in outer degree five by a fixed positive formula" (G-036, with T-037 for
  outer degree four):**
  1. Complete: the run has whole-proof reviews; I have not read the proofs.
  2. Self-contained: yes, with Sarkar's and Nagel-Trok's cited theorems where used.
  3. Stable: yes within our work, since the run has ended; the literature search is not done.
  4. Checked: computation only (539 coefficients for G-036; 60 for T-037), with no proof check by an intake.
  5. Of interest: moderate to high in algebraic combinatorics.

  Gates: an intake proof reading of G-036's providers, and the literature search.
- **New candidate (proposed; the number after it), "polynomial-size positive formulas in varying outer degree" (G-037 to G-040):**
  1. Complete: the run's reviews.
  2. Self-contained: yes.
  3. Stable: within our work.
  4. Checked: G-037 by computation, 790 coefficients; no intake proof check.
  5. Of interest: high. It bears on GCT VII Problem 1.1 and on the hardness boundary of Fischer-Ikenmeyer.

  Gates: a proof reading and the literature search (Langley-Remmel, Paget-Wildon).
- **H02:** not touched by this run, except that GCT_PLETH's counting results are the positive side of the same
  conclusion; see ALPOGE_GCT part 4.
- **H03:** not touched.

## 8. Edits for the register (not made)

- Add two rows under the next free numbers, for G-036 + T-037 and for G-037 to G-040, with the tests and gates of section 7. State: candidate, not
  ready. Source: "GCT_PLETH final (checkpoint 09)". Checks: "computations g036.py (539), g037.py (790), out4.py (60);
  no intake proof check".
