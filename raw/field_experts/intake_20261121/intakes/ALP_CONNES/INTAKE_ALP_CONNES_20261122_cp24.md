# Intake of ALP_CONNES checkpoint 24 (prompt 55), by diff from checkpoint 18

Written 22 Nov 2026 by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e). The run is GPT-6 Astra (ChatGPT Pro
mode) and is still going. The return is at `<local>/Documents\grothendieck_archive_transcription_20261110\research_returns\ALP_CONNES_checkpoint_24_20261122T2109Z_unzipped\ALP_CONNES`
(below `A`). Checkpoint 18 is the intake `INTAKE_ALP_CONNES_20261122_cp18.md` beside this file.

Masullo's GRH draft is not a proof. Nothing here is a fix, repair or completion of it. Results that our earlier files
called conditional on Masullo are conditional on GRH for the L-functions concerned, an open hypothesis. This line is an
independent construction from Alpöge's theorem A (RH for zeta and every primitive Dirichlet L-function). The run's own
phrase "coherent repair", quoted in our MAS_ARTIN intakes, means a corrected statement in the run's own model.

## 0. What was read, and what was not

- **Diff method:**
  - QUESTIONS.tsv was compared row by row with the checkpoint 18 copy at
    `<local>/Documents\reports_20261122\overnight_intake\ALP_CONNES\QUESTIONS.tsv`. Of 983 rows, 127 are new,
    23 changed and none removed.
  - The \input lists of the two papers were compared, giving 39 new modules.
  - The 20 modules I checked at checkpoint 18 are byte-identical in checkpoint 24, so those checks carry over.
- **Proofs read in full:** AC-S50; AC-G114-residual; AC-T15 and AC-T17, with the statements in Morishita's preprint
  that they correct.
- **Statements only:** AC-S47, S48, S49, S51; AC-G114-strict, G115, G116, G123, G124, G125, G126; AC-T18. I read the
  127 new and 23 changed question rows only as their state and first 170 characters.
- **Not read:** the proofs of the other new modules (G101-G113, G117-G122 and the rest), CHECK_EVENTS row by row, and
  LEDGER beyond the movement reviews. I ran no code of the return and replayed no PARI certificate.

## 1. What moved since checkpoint 18

### Spectral line (Connes-Consani-Moscovici prolate operator, Weil quadratic form)

| row | statement (run's id) | our check |
|---|---|---|
| AC-S50 (new; SQ20-22) | Under A, finite Hermitian compressions of D⁻¹ to piecewise-linear spaces V_N, computed only from explicit-formula Weil pairings with finitely many prime powers, give real-rooted polynomials P_N → Ξ(z)/Ξ(0) locally uniformly. A fixed probe recovers every zero's multiplicity. No zero data is input. | **targeted proof check, confirmed**, given the explicit formula, the local strict positivity AC-S03 (not reread) and Hadamard |
| AC-S47 (new) | Unconditional leakage bounds; under A, q_L(k_λ) ≤ C_ε λ^ε(1−ν₄) and a₁ ≤ C_ε λ^(9+ε)e^(−4πλ²). The sufficient lower bound for a₂ drops from λ^(9+α) buffers to λ^10 | statement read |
| AC-S48 (new) | Under A, ratio q_L(v_λ)/a₂ → 0 gives simple-even ground state, L² convergence and locally uniform convergence of the transforms to Ξ | statement read |
| AC-S49 (new) | Under A, that ratio → 0 implies all zeta zeros simple | statement read |
| AC-S51 (new; SQ24-27) | Where a_e < a_o, the bottom-shifted quotient has an injective compact inverse whose inverse eigenvalues are the real simple zeros of ê_L. With a fixed relative odd gap κ, ê_L/ê_L(0) → ∏(1−z²/γ²) over the distinct ordinates | statement read |
| AC-SE-Q02, SQ05, SQ12, SM-Q01, SR-Q03, SQ10 (changed) | Upper rates sharpened by S47; the lower bounds stay open | |

**Bridge shown:** Weil positivity under A makes the Weil completion H ≅ ℓ²(Γ,m). D⁻¹ is then compact, and its
finite prime-built compressions reconstruct Ξ with multiplicities (S50).

**Not shown:** that the actual lowest eigenvector of the localized Weil operator converges to Ξ. This is the
Connes-Consani-Moscovici selection question. Its gate is a lower bound on a₂, or the ratio directly, or a fixed
relative odd gap (S51).

### Deninger's dynamical systems, through Morishita's comparison

These results were already in checkpoint 18; this is the first check by us.
- **AC-T15, independent re-proof.** Hom(F̄_p^×, C^×) ≅ ∏_{ℓ≠p} Z_ℓ, and the image of Ẑ_(p)^× × N is exactly the
  characters of finite kernel. So the surjection (2.2.7) in M. Morishita, arXiv:2508.15971 (source opened: the copy
  in `A\input_material\followup1\LIT_Deninger_vs_CC_adelic_spaces`), needs Deninger's admissibility condition, which
  his Remark 2.1.13 drops.
- **AC-T17, independent re-proof.** The fiber over ā of the mapping torus is H_p ×_{p^Z} R_{>0}, with
  H_p the closure of p^Z. It is a compact solenoid with dense nonclosed flow orbits, so it is not R_{>0}. Morishita's
  Theorem 2.2.8(2), as printed, says it is R_+ (source opened, line 386 ff.).
- **AC-T18 (statement read).** For abelian F the closed-orbit factors give ζ_F = ∏L(χ), so under A all its zeros are
  on the line and the finite-window positive operators apply. The run states that no intertwiner from leafwise
  cohomology to the Hilbert trace spaces is constructed.

**Bridge shown:** Alpöge's theorem gives positivity on the Connes side for abelian F.
**Only spotted:** a Deninger-side Lefschetz formula that matches it.

### Cubic arithmetic at the coefficient prime 269 (about 100 new rows, G101-G126)

Here K = Q(√−3), χ is a cubic character cutting out K(∛269), ψ = χ₋₄ or χ₋₂₀, and c_p is cyclotomic with p = 269.

**Unconditional:**
- **AC-G114-residual: targeted proof check, confirmed** given the PARI class number h(Q(∛269,√3)) = 7, which was
  not rerun. For e ≡ 267 mod 268 and j = 1, 2, the strict residual Selmer group of χ^(−j)ψ^(−1)c_p^(−e) over K is
  zero. I recomputed independently:
  - P(s−t) = 0;
  - the characteristic polynomial of the printed global unit U, which matches and has constant term 1;
  - its reduction 82+122s, 260+95s with ratio 11s;
  - that 3 is a nonsquare mod 269.

  From these the local non-p-th-power w = 1 + 66s·t follows.
- **G114-strict, G115, G125, G126 (statements read):** the strict group with original coefficients is zero for
  e ≡ 133 or 267 mod 268 and both cubic labels, and for every continuous lift of the coefficient character, for
  ψ = χ₋₄ and χ₋₂₀. At each fixed weight, exactly 2·269^(m−1) finite characters of conductor dividing 269^m qualify.
  No automorphic, host or model premise is used.

**Conditional on retained modularity, local-global and coefficient inputs (statements read):**
- **G116, G117:** under the inherited hypotheses there is no actual quadratic-character Type II point. So the original
  N4 endpoint that fed G103's automorphic instance and G106-native **cannot be instantiated**: those implications are
  valid with an empty instance (rows G106N-Q01 to Q03, QG491, QG492, QG546). This is the main thing checkpoint 24
  removes from what we held.
- **G119-G124:** an auxiliary ordinary seed (q = 3229, θ(6) = ζ₂₆₉) gives actual hosts, support and all five model
  conditions M1-M5 on four quadratic rows (conductors 4 and 20 at e ≡ 267, 1076 and 5380 at e ≡ 133 mod 268). These
  bound normalized lengths by a nonzero integer with log ≤ 10C₁Y^(A₁+1) log 11.

**Still open:** H04.4, RH for the cubic Kummer character, the all-prime and all-family budget, and G118's quartic seed.
At e ≡ 133 and 267 the literal construction fails (Eisenstein constant 145 mod 269).

## 2. Strongest results now, in the project's terms

1. **Shown:** AC-T51 (checkpoint 18, unchanged). Connes's global trace formula over Q, for the explicit prolate cutoff,
   is equivalent to A, and by Alpöge it is a theorem.
2. **Shown under A:** AC-S50. The arithmetic side of the explicit formula determines Ξ, with multiplicities, through
   finite real-rooted approximants. Spectrally: the compact operator D⁻¹ on the Weil completion is approximated by
   finite prime-built matrices.
3. **Shown, unconditional, computer-assisted:** the exact even K-groups of Q(ω,∛269) at 3 (checkpoint 18). Also the
   vanishing strict Selmer groups at 269 for two infinite character towers (G114, G115, G125, G126), with G114 checked.
4. **Shown, corrections to a published preprint:** T15 and T17 on Morishita's Deninger-Connes-Consani comparison.
5. **Only spotted:**
   - the Deninger-side Lefschetz formula;
   - Connes-Consani's F₁ objects (Riemann-Roch on Spec Z̄, the scaling site, zeta cycles, the absolute twistor line),
     whose LaTeX sources are in `A\input_material`: IMPLICATIONS.md draws no theorem from A for them;
   - the Marcolli line beyond the BCM neutrality results of checkpoint 18.

## 3. Converging or stalled

Every movement review from 12 to 19 says "Movement: yes", with 0 consecutive reviews without movement. Review 20 was due
at 22:09 UTC.

By the 17 Nov criterion that movement is real only on side rows: the cubic M1-M5 rows changed status, and the spectral
sufficient gates shrank. Each main gate is unchanged since checkpoint 18:
- H04.4;
- RH for the cubic character;
- the T51 defect limit without zero location;
- the lower bound for a₂.

So the run is productive and is not converging on its main questions. The cubic branch also lost its original
endpoint (G116).

## 4. What the next prompt should ask, and what 68_CONNES_AFTER_RH lacks

**Ask for:**
- **Deninger.** Tao's remark (20 Nov thread) places Masullo's manuscript nearer Deninger than Connes. The run supplies
  the corrected Deninger space: finite-kernel characters, solenoid fibers (T15, T17), and for abelian F the orbit
  factorization (T18). Ask for a leafwise cohomology and Lefschetz formula on that corrected space whose spectral side
  is the AC-T46 trace, abelian F first. Ask whether A then gives Deninger's positivity, or which hypothesis it lacks.
- **Connes-Consani F₁.** For each of their conditional statements (Riemann-Roch on Spec Z̄ and the scaling site,
  Hochschild and zeta cycles, the absolute twistor line), decide which follow from A. Compare S50's compressions with
  the zeta-cycle spaces.
- **Marcolli, Ha-Paugam, Yalkinoglu, Laca-Larsen-Neshveyev.** Push A through the BC and BCM systems for number
  fields: KMS states, partition functions and abelian zeta factors.
- **The CCM selection question.** Ask for the lower bound a₂ ≥ cλ^10 e^(−4πλ²), the ratio, or the relative odd gap κ.

**Prompt 68 lacks:**
- AC-S49, S50, S51 and rows SQ20-SQ27. Its `ours/workshop_68` holds only S47 and S48, and its `ours/ALP_CONNES` has no
  spectral module after them.
- Suzuki, "Spectral convergence associated with Weil's quadratic form", arXiv:2610.32704. S50 builds on it, so it is
  needed for any novelty statement.
- Morishita's preprint and AC-T15 to T18.
- The Connes-Consani F₁ and BC-system sources, and the Masullo rule above.

**Check before it goes:** the 68 ZIP contains `ours/GRH_NIGHT/evidence/masullo_trace_selected.txt`, a 49 kB text
extract of Masullo's PDF beginning "PDF PAGE 15". The coordinator's rule of 21 Nov forbids attaching any text extracted
from his document. It also has `ours/GRH_NIGHT/root/masullo_*.tex`, which are the run's own files and were not opened by
me.

## 5. Outreach and Hexagon readiness

**Outreach:**
- **M. Morishita:** T15 and T17 show that Theorem 2.2.8(2) and surjection (2.2.7) of arXiv:2508.15971 need the
  finite-kernel condition, and that the fiber is a solenoid. Both were re-proved by us. Worth a draft.
- **M. Suzuki:** S50 completes his compression with a proof that the sampling map is onto, multiplicity recovery and a
  finite rational algorithm. Ask him whether this is known.
- **Connes, Consani, Moscovici:** S49 shows that their selection ratio would force simple zeros. S51 gives the
  parity-gap route. These were read as statements only, so check them before any letter.

**Hexagon:**
- **S50: candidate, not ready.** Gates: compare with Suzuki 2610.32704 and Connes-Consani-Moscovici; reread AC-S03;
  independent re-proof; literature search.
- **G114 to G126: not ready.** Gates: G114-strict, G115, G125, G126 proofs; PARI replay on a second system; search.
- **T15, T17:** errata to someone else's preprint, which go in a letter, not a post.

## 6. Files of others in this return, never to GitHub

- `A\input_material\` (2,229 files): arXiv LaTeX sources by Connes, Consani, Marcolli, Moscovici, Morishita, Borger, de
  Smit, Ha, Paugam, Laca, Larsen, Neshveyev, Yalkinoglu and others, and Alpöge's `ALPOGE_remark.pdf`.
- The .lean interface files.
- `evidence/ALPOGE_remark.txt`.
- The Johnson-Leung-Kings text.
- The Stacks tags.

The input_material also holds our own OURS_* notes and intakes. Not screened: .md and .json members.
