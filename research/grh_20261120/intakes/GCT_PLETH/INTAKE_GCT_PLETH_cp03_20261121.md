# Addendum: GCT_PLETH checkpoint 03 (21 Nov 2026)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the main session's request (Claude Opus 5.5 at
effort max). Earlier intake: `INTAKE_GCT_PLETH_20261121.md` (checkpoints 01-02). The run is GPT-6 Astra (ChatGPT Pro
mode); its effort is not exposed.

## 0. Return read and scope

- Folder: `research_returns\GCT_PLETH_checkpoint_03_20261121T0116Z_unzipped`, scheduled for 01:16 UTC. The paper has
  grown to 20,540 lines. The run is still going; the first three-hour review was due 03:01 Berlin.
- I read only what is new since checkpoint 02: the ledger blocks "Checkpoint 02 update" and "Research status before
  checkpoint03", the new QUESTIONS rows (T-024 to T-041, G-013 to G-019, R-012 to R-024, A-028, A-029), and
  `work/archive/STUDY_ADDITIONS.md` (lines 28-40).
- **Checked by computation:** T-037, the outer-degree-four formula. I recomputed 60 random rows (n = 2..4, all five
  outer shapes μ ⊢ 4) of the run's table `work/rectangular/OUTER4_ALL_FORMULA_INDEPENDENT_CHECK.tsv` (1,980 rows). My
  method is independent of the run's cycle-index check: I expanded the character of S_μ(Sym^n C⁴) through power-sum
  plethysm with the S₄ character table, and took multiplicities by antisymmetrization. **All 60 agree** with the
  formula's values.
- **Read at the statement level only:** T-024 to T-036, T-038 to T-041 (the outer-degree-four chain, the five-point
  quadric algebra); G-013 to G-019; R-012 to R-024, including R-021 (every even-rank boundary determinant lies in the
  canonical image, B = a(a−2)) and R-022 (component surjectivity ranges for b in [r²−r+1, r²−1] with r = a−1); A-028
  and A-029 (the Cox ring of P⁴ blown up in five points as the Plücker ring of Gr(2,6)).
- The proof of T-037 is not read in full. It rests on T-035, the four-point vanishing model.

## 1. Verdicts

- **T-037** (an explicit formula for p_{μ,(n)}^λ for every μ ⊢ 4 and every n, by at most 108 tagged polytopes in at
  most five variables): **computation check, 60 of 60 agree**; the proof was not read. The run's own independent
  checks cover 1,370 chamber coefficients and 420 central-family coefficients.
- **The scans 24-27 correction** (A-013, extended in `STUDY_ADDITIONS.md`): the run now reports that the manuscript
  itself (PDF page 25, site page 24) says "direct summands of H_I for I of sufficiently large cardinality". The
  counterexample h_∅ ⊔ h_∅ still holds: at a singleton E every Hom(I, E) is a singleton. So the correction applies to
  Grothendieck's page, not only to our paraphrase. The corrected statement: finite sums of representables are the
  direct summands of finite sums of the Hom(I, −). **Confirmed as mathematics.** I did not look at the scan image; the
  run says it did.
- **Everything else new: carried at statement level.** I saw no fault in the statements.

**Counts this round:** 1 checked by computation (T-037); 1 correction confirmed as mathematics (the scan-25
statement); 0 refuted; 0 gaps; about 45 at statement level.

## 2. What is new

- **T-037.** A complete positive formula for outer degree four, in every inner degree and for every output, would be a
  real step. Explicit rules exist for outer degree ≤ 3 (Thrall, Chen-Garsia-Remmel, Howe). I do not know a complete
  polytope formula for outer degree four, but a literature search is needed before any claim. The run's G-012 already
  covered outer degree three.
- **R-021 and R-022** move the Hadamard-Howe (Foulkes-Howe) map below Sra's bound b ≥ (a−1)², component by component.
  This bears directly on Foulkes' conjecture and on the GCT rank datum H_λ (ALPOGE_GCT PL-06). It is new as stated,
  but read at statement level only.
- **A-028 and A-029** concern the Cox ring of the five-point blow-up. The identification with Gr(2,6) is classical
  (Castravet-Tevelev; Batyrev-Popov). The run uses it as a tool.

## 3. Scope of the two proofs

Unchanged: no finding uses Alpöge or Masullo. Q-ALPOGE and Q-MASULLO are still gates.

## 4. How the findings bear on the open problems, and the attack they open

1. **Foulkes' conjecture and the canonical map.** R-022 gives surjectivity on all components with λ₂ ≤ b − r in the
   window just below Sra's bound. Foulkes' conjecture for (a, b) is the statement that h_{a,b} is surjective for
   b ≥ a.
   **Next attack:** iterate R-024's recursive second-row argument down in b, and record the first b at which a
   component's rank falls below its coefficient. That b is either a counterexample to the Hadamard-Howe injectivity
   that GCT would want, or a new range for Foulkes.
2. **Positive formulas.** With T-037 (outer degree four) and T-012/T-013 (stable tails of width ≤ 6), the next case of
   both programmes is a single computation: outer degree five, or width seven (the G₂ sector, Q-W7).

## 5. Integration (no edits made outside this folder)

- **SA17 study, scans 24-27:** replace my earlier suggested note with: "The page (PDF p. 25) itself says 'direct
  summands of H_I for I large'. That is false: the constant functor h_∅ ⊔ h_∅ is not a summand of any single
  Hom(I, −). The correct statement uses finite sums of the Hom(I, −) (GCT_PLETH A-013, 21 Nov; to be confirmed on the
  scan image)." Also record it as a correction to Grothendieck's text in our reading of cote 133.
- **The other study edits** from `INTAKE_GCT_PLETH_20261121.md`, section 5, stand unchanged.
- **Successor prompt of GCT_PLETH:** add T-037 to the settled list, after a full proof reading. Target outer degree
  five and the Foulkes window of 4.1.

## 6. Hexagon readiness

- **T-012/T-013: stable plethysm positive formulas through width six.**
  1. Complete: yes.
  2. Self-contained: yes, given Sarkar, arXiv:2610.07929v2, Theorem D and Proposition `prop-reduction`.
  3. Stable: no. The run is live and its width-seven work may extend it.
  4. Checked: an intake proof check, plus my exact recomputation of the B₅ and B₆ tables. I did not evaluate the
     lattice sums against direct plethysm.
  5. Interest: moderate (algebraic combinatorics; Sarkar's paper is a month old, so timing matters somewhat).

  Gates left: the run's final; an evaluation of (T12.4) and (T13.6) on a table of λ; a literature check against
  Sarkar's later versions.
- **T-037: plethysm in outer degree four.**
  - Test 1 (complete): not established by me, since the proof was not read.
  - Test 4 (checked): computation only, 60 rows.
  - Test 3 (stable): needs a literature search and the run's final.

  Interest: moderate to high in algebraic combinatorics. Gates left: a full proof reading, the literature search, and
  the final.
- **Archive corrections (A-001, A-003, A-013, A-021, A-023):** these are companion material for cote 133, not Hexagon
  posts.

Nothing here passes all five tests yet, and nothing is a flag-at-once item.
