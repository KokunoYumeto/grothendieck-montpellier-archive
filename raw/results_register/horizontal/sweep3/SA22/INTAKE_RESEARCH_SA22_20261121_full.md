# Full intake of RESEARCH_SA22 (run 1), statement by statement (22 Nov 2026)

By Claude Opus 5.5 at effort max (agent af3526fc4890c92f1). Requested by the coordinator at the user's word of 21 Nov
~23:5x UTC ("I also want the full intake"). The run is GPT-6 Astra (ChatGPT Pro mode); its return is
`grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA22_final_20261119T1905Z_unzipped`.

**Inputs:**
- the list: field_experts/INTAKE_LEDGER.md section 9 (133 ids of run 1 not checked before);
- the earlier intake: INTAKE_RESEARCH_SA22_20261120.md (26 rows of this run checked on 20 Nov; their events are
  carried over into this file's TSV and marked so);
- this file's check events: `INTAKE_RESEARCH_SA22_20261121_full_CHECK_EVENTS.tsv`. Every event names the run.
- The companion file for run 2 is `INTAKE_RESEARCH_SA22_run2_20261121_full.md`. Where run 2 repeats a run-1 statement,
  the check was done once, and the run-2 event says which run-1 id carries it.

**Status: complete.** Every one of the 133 ids has an event. The work file is
agent_notes/af3526fc4890c92f1_NOTES.md; my scripts are in agent_notes/af3526fc4890c92f1_work/.

## 1. Counts (strongest event per id, the 133 listed ids)

| check type | ids |
|---|---|
| computation or formal certificate | 0 |
| independent re-proof (ours) | 4 |
| targeted proof check | 34 |
| used and rechecked | 0 |
| carried as background without fault found | 55 |
| statement level (read only, or read and consistent) | 40 |

- The 4 independent re-proofs are:
  - `A3-boundary-chart`;
  - `A6-matrix-presentations`;
  - `thm:B1a-etale`, in the Betti case;
  - `A5-moduli`, its coarse space at every prime, including 3; see section 3.
- Among the 40 statement-level rows, 7 Part C rows agree with our own sweep-3 re-derivations of 68/019-020 and
  68/036-042: `C-exp-log`, `C-filtered`, `C-differential`, `C-other-autos`, `C-intertwine`, `C-symmetry` and
  `C-rearrangement`. In this intake I only read and compared their statements.
- The 55 background rows include the 36 rows of the run's B.3 inventory (`thm:B3-*`). For those I read the statement,
  the locator and the scope, not the source.

## 2. Refutations

- **No refutation by us.** No checked statement is wrong.
- **The run's own refutations:** 21 rows in the list.
  - 10 are checked and hold:
    - `A1-bordered-landing`;
    - `A1-toric-noninjective`;
    - `A1-nontoric-cut`;
    - `A1-cut-not-algebraic`;
    - `A4-orange-jets`;
    - `A6-ordinary-counterexample`;
    - `A6-procyclic`;
    - `A6-three-classes`;
    - `A6-frobenius-counterexample`, in mechanism;
    - `A6-node-character`, a correction.
  - 11 stay at statement level or background:
    - `A1-toric-nondescent`;
    - `A6-special-fibre-counterexample`, `A6-wild-counterexample`;
    - `C-K-counter`, `C-functor-counter`, `C-other-autos`, `C-packed-asymmetry`;
    - `thm:B1c`, `thm:B3-pprimary`, `thm:B3-sga2`, `thm:B3-specialization`.
- **The refutations checked on 20 Nov** (not in this list) still stand:
  - `A1-global-refutation`;
  - `A2-independence`;
  - `A7-domain-counterexample`;
  - `A7-ratio-j`.

## 3. What was checked beyond the earlier intake

**Jets of the capping projective structure:**
- the third-jet coefficient β(λ) = 5/16 + 1/(16(λ²+4)) (`A1-pant-third-jet`);
- the four-point cubic coefficient 11/64 + 1/(64(λ₁²+4)(λ₂²+4)) (`A1-four-point-plumbing-jet`);
- the bordered landing refutation, by a two-line jet check.

**Plumbing and welding comparisons.** The coordinate derivations of these rows are confirmed:
- `A1-Earle-Marden-original`: the collar |t|/ρ < |z| < ρ of modulus Im τ − 2h;
- `A1-Earle-Sipe-comparison`: e^{iθ}∂_u⊗∂_v = t ∂_z⊗∂_w;
- `A1-welding-plumbing`;
- `A1-wolpert-comparison`: core length 2π²/(−log|t|).

The citations themselves, the Earle–Marden draft and Earle–Sipe 1991, are the run's and were not opened by me.

**Collars:**
- the transformation laws give Δu = e^{2u} − 1 and ∂_n u = −k_h (`A2-collar`, `A2-collar-general`);
- the Neumann mechanism of `A2-collar-shape`;
- the length–area step of `A2-strebel-deficit`;
- the radius bounds of `A2b-recession`: Koebe, the area theorem and Schwarz, by genus.

**Anabelian rows:**
- Kummer injectivity (`A6-kummer`);
- the blow-up and log-canonical-model arguments (`A6-blowup`, `A6-canonical-compactification`);
- SL₂(ℤ)/B_∞ = P¹(ℚ) (`A6-projective-line`);
- the node inertia character ℤ̂(1)⊗ε_e (`A6-node-character`).

**`A5-moduli` at the prime 3, closed today.** Batch 4 had left this point open; it is now settled by our own argument.
- Put A = R[λ, 1/λ, 1/(λ−1)] with R = ℤ[1/2, i]. Then A^{S₃} = A ∩ ℚ(i)[J].
- Suppose P ∈ ℚ(i)[J] ∩ A had a prime π of R in its denominator. Write dP = P₀ with P₀ ≢ 0 mod π. Then P₀(J) = 0 in
  A/πA. That ring is a domain in which J is transcendental, since J has a double pole at λ = 0. This is a
  contradiction.
- Hence the coarse space is Spec R[J] over all of R, including the fibre at 3.
- The same argument checks run 2's `A:unordered-stack`, which writes j = 256 J; 256 is a unit in R.

## 4. Gaps left (steps not checked)

- `A1-toric-nondescent`: the phase rule and the final comparison.
- `A1-hinich-counterexample`: the critical parameter t = 9/11. Run 2's exact instance `A:hinich-explicit` is checked;
  see the run-2 file.
- `A2b-energy`: the positivity step.
- `A2-cap-limit`: the identification of the limit.
- The A6 model and specialization rows: `A6-model-system`, `A6-model-specialization`, `A6-tame-specialization` and
  `A6-intrinsic-tame` are at statement level.
- `thm:B1b-abelian` rests on Broe's 2026 preprint, which we have not checked.
- Part C's finite certificates were not recomputed.

## 5. Errata

- **In the run:** none found in any statement I checked.
- **In our own record:** the sweep-3 correction of 67/091 ("needs Spec k connected") is refuted by both runs, as the
  20 Nov intake already records. The counterexample R = ℤ[x,y,z]/(x²+yz−1) was checked then.

## 6. What is new in run 1

These items are not in the 20 Nov intake. They are new to us, and as far as the run's sources show they are not in
the literature; no literature search has been made.
- The explicit second and third jets of the canonical caps, and the four-point plumbing jet (section 3).
- The toric non-injectivity counterexample. Caps of radii (1,1) and (2,1/2) give the same tensor on the same
  normalization.
- The analytic non-toric cut h(e^{iθ}) = exp(i(−θ + sin θ/2)).
- The small-range answers. The (0,4) range is 0 < |q| < 16. The (1,1) case has weights (1,1,0), with half-planes as
  extremals.
- The collar and length–area results of A2.
- The anabelian corrections. Bare cyclotomic procyclic subgroups are infinitely many: `A6-procyclic` and
  `A6-three-classes`. The node inertia carries the sign twist ε_e.

## 7. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, five tests)

Taken together with run 2, see the run-2 file, section 7. For run 1 alone:
- **The (0,4) refutation and its exact image, 0 < |q| < 16** (`A1-global-refutation`, `A1-small-ranges`; run 2's
  `A:04` and `A:04-exact-image`).
  - Test 1, complete: passes.
  - Test 2, self-contained: passes; Koebe's theorem is classical.
  - Test 4, checked: passes. It has targeted checks on 20 Nov and today, the two runs prove it independently, and our
    sweep-3 Koebe check is a third.
  - Test 3, stable: open. A literature search is needed, including Michel Hua's project as a witness only.
  - Test 5, of interest now: moderate, for the archive line.
  - **One gate.**
- **The jets** (β(λ) and the cubic coefficient). They are checked, but they serve the answer to 67/068 rather than
  stand as a post.
- Nothing else in run 1 passes tests 1-4.
