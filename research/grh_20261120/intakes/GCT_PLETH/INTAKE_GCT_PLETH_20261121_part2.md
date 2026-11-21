# Intake of GCT_PLETH, part 2: checkpoint 04 (21 Nov 2026)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the main session's request (Claude Opus 5.5 at
effort max). The run is GPT-6 Astra (ChatGPT Pro mode), with the root and delegated agents; the run says its effort
setting is not exposed.
Part 1 is `INTAKE_GCT_PLETH_20261121.md` (checkpoints 01-02). The addendum `INTAKE_GCT_PLETH_cp03_20261121.md`
(checkpoint 03, which checked T-037 by computation) also precedes this part. Work file:
`agent_notes\20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md`.

## 0. Return read and scope

- **Folder:** `research_returns\GCT_PLETH_checkpoint_04_20261121T0201Z_unzipped`, the newest present (scheduled
  02:01 UTC). The paper is 23,846 lines. The run is still going. Its first formal review (03:01 Berlin) records
  "Movement: YES" with 0 reviews without movement; the next was due 04:01 Berlin.
- **Read, new since checkpoint 03:**
  - the LEDGER "Research update during fourth work interval" and "Formal progress review 01", with its full table of
    open rows;
  - the new QUESTIONS rows: T-042, T-043, G-020 to G-023, R-025, R-026, Q-OUTER4, Q-OUTER5;
  - the statements of G-021 (l. 10325-10380) and R-026 (from l. 16695).
- **Checked by computation:** G-021, the outer-degree-five two-row family. I drew a random sample of 50 rows with
  n = 1..3, across all seven μ ⊢ 5, from the run's table
  `work/rectangular/OUTER5_TWO_ROW_BUNDLE_INDEPENDENT_CHECK.tsv` (882 rows). I recomputed each with my own method:
  the character of S_μ(Sym^n C⁵) from the S₅ character table through power-sum plethysm, then multiplicities by
  antisymmetrization (`chk/out5.py`, character table checked by orthogonality). **50 of 50 agree**, both with the
  run's cycle-index column and with its formula column (`two_row_trace`).
- **Read at statement level only:** T-042, T-043, G-020, G-022, G-023, R-025, R-026, and the reworded archive gates
  (A-Q009 to A-Q122). The proofs of G-021 and R-026 are not read.
- **Part 1 rechecked against checkpoint 04:** the 156-row B₆ table is still exactly my recomputation; (T12.4) and
  (T13.6) are present; A-001 to A-023 keep their states. **No finding checked in part 1 or in the addendum is changed
  or withdrawn.**

## 1. Verdicts on the new and changed findings

- **Q-OUTER4 is now "proved", by T-037.** I checked it in the addendum by computation: 60 of 60 coefficients agree.
  The proof is still unread by me. Verdict unchanged: confirmed by computation only.
- **G-021** (a fixed positive formula for every p_{μ,(n)}^λ, μ ⊢ 5, on the five-parameter family (TR.1), with at most
  122 active polytopes of dimension ≤ 11 and an explicit list of 155 zero quadruples): **confirmed by computation on 50
  random cases.** The proof was not read. Its structure, from the statement, is the identification (TR.3) of the
  balanced weight space with sections of the ideal sheaf of five points on P⁴, twisted by a Schur functor of the
  tautological quotient Q. That is the five-point Cox ring of A-028 and A-029.
- **G-020, G-022, G-023, T-042, T-043** (more outer-degree-five families, all-rank staircase nonvanishing, seven
  active polytopes on the central staircase) and **R-025, R-026** (explicit multiplicity-one canonical image
  components just below the square bound b ≥ (a−1)²): **statement level, no fault seen.** The ledger records that the
  run's root read the whole proofs of R-025 and R-026.
- **Archive rows:** the run now cites the original Montpellier PDF pages it inspected for each gated row. No new
  refutation of our study appears in checkpoint 04. The A-Q122 gate (the coefficient-ring classification for scan 29)
  now reads: "all characteristic-zero fields and DVRs positive; F_p and A-023 negative". That matches part 1.

**Counts for part 2:** 1 newly confirmed by computation (G-021); 0 read in full; 0 refuted; 0 gaps; 0 withdrawn; 9
new findings at statement level.

## 2. What is new

- **The positive-formula programme for small outer degree.** Outer degree three (G-012) and four (T-037) are complete
  formulas. Outer degree five is now covered on every region except the central one, λ₂+λ₃ > 2n > λ₃+λ₄ (Q-OUTER5).
  Fixed formulas for all outer degree four, and most of five, would be new so far as I know. Thrall, Chen-Garsia-Remmel
  and Howe stop at three. A literature search must come first: algorithmic approaches to h₄[h_n] and h₅[h_n] by
  computer algebra exist, and they would need comparing.
- **The geometric mechanism is the new idea.** The run reads the balanced weight space of Gay's theorem (T-002) as
  sections of powers of the ideal of the k simplex points of P(h_k) = P^{k−2}, twisted by tautological Schur bundles
  (G-015, G-016, G-021). Here k is the outer degree; for k = 5 this is P³ with five points, by (TR.2). Plethysm in
  outer degree k becomes interpolation, in the sense of Alexander-Hirschowitz, for k points of P^{k−2}. For k = 5,
  the Cox ring of the blow-up is the Plücker ring of Gr(2,6) (A-028).
- **R-025 and R-026** extend the known surjectivity range of the Hadamard-Howe map (Sra III, Theorem 1.3) by explicit
  components. They are new as stated, read at statement level.

## 3. Scope of the two proofs

Unchanged: no finding uses Alpöge or Masullo. Q-ALPOGE and Q-MASULLO remain input gates.

## 4. How the findings bear on the open problems, and the attack they open

1. **Positive formulas (the flip's PH1-type demand, in shifted form).** T-037 and G-021 are fixed positive formulas,
   with no computation that grows with the input, in outer degrees four and five. They are exactly the kind of #P
   formula that GCT VII Problem 1.1 asks for, in bounded outer degree.
   **Next attack:** bounded outer degree k, through the interpolation reading. Plethysm coefficients become dimensions
   of spaces of sections of I_Z^j(c) ⊗ S_β Q on P^{k−2}, with Z the k points (the vertices of the simplex in P(h_k)).
   Positivity then follows from a torus-equivariant degeneration (SAGBI or toric, as in T-026) of the Cox ring of the
   blow-up. For k ≥ 6 the obstacle is the presentation of that Cox ring. The blow-up of P^m in m+2 points is a Mori
   dream space: the case of at most m+3 points, after Mukai and Castravet-Tevelev, which I cite from memory and have
   not checked here. So the Cox ring is finitely generated for every k. The open question is whether its presentation
   and degeneration stay uniform enough to give a fixed positive formula. That is a conjecture for the successor, which
   should test it at k = 6.
2. **Canonical maps (Foulkes-Howe).** The remaining annihilator is located exactly (Q-MAP): it injects into
   N_r ⊗ Sym^{r²−1}, with first row ≥ r²+1 and second row ≥ r(r−1).
   **Next attack:** compute that annihilator for r = 3 and 4 by the run's common-polarization certificates. A nonzero
   vector would be the first component where h_{b,a} fails to be injective (or surjective) inside Sra's window.
3. **Cote 133.** No new archive correction. The gated rows on other cotes (crystalline Lefschetz, the motivic
   self-duality on PDF pp. 31-43, the triangulation reconstruction on PDF pp. 46-51) are outside cote 133. They
   should go to the sweep readers of those cotes as open readings.

## 5. Integration (no edits made outside this folder)

- **The study edits of part 1, section 5, and of the addendum stand unchanged.**
- **Successor prompt of GCT_PLETH:**
  - settled: T-037, G-021 (after a full proof reading);
  - main targets: the central region of outer degree five (Q-OUTER5); the interpolation route for outer degree six
    (4.1); the r = 3, 4 annihilator for the canonical map (4.2).
- **The project's terms.** G-021's dictionary is Grothendieck's: sections of a coherent sheaf I_Z^k ⊗ S_β Q on the
  projective space of a representation; the tautological quotient of EGA I and II; Schur functors on locally free
  sheaves, as in the λ-ring of SGA 6. Gay's weight space (T-002) becomes H⁰ of a twisted ideal sheaf. That is the
  form in which cote 133's tensor-power formula (A-012, scan 28) and the positive formulas meet. The integral Cauchy
  filtration of A-012 is the integral form of the same decomposition.

## 6. Hexagon readiness

- **T-037 together with G-021 ("plethysm in outer degree four, and most of five, by fixed positive formulas").**
  - Test 1 (complete): not established for outer degree five, which has the central gate; I have not read the
    outer-degree-four proof.
  - Test 4 (checked): computation only, 60 + 50 rows.
  - Test 3 (stable): no; the run is live on outer degree five.
  - Test 5 (interest): moderate to high in algebraic combinatorics.
  - Gates left: the run's final, a full proof reading of T-037, and a literature search on h₄[h_n] and h₅[h_n]
    formulas.
- **T-012/T-013 (part 1):** unchanged; same gates as in the addendum.
- **H02:** not touched by this run. ALPOGE_GCT's P-F31 strengthens H02; see `ALPOGE_GCT\INTAKE_ALPOGE_GCT_20261121_part2.md`,
  section 7.
- **H03 (border rank, GCT_GINEQ F-23):** not touched by GCT_PLETH. Its rectangular and Kronecker findings (R-014: a
  stable rectangular-Kronecker lower bound) concern multiplicities, not border rank. Nothing here strengthens, changes
  or supersedes H03.

Nothing passes all five tests, and nothing is a flag-at-once item from this run.
