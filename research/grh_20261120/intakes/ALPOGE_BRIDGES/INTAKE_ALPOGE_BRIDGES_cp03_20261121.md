# Intake of ALPOGE_BRIDGES checkpoint 03 (prompt 22): what is new since checkpoint 01, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), the agent that took in checkpoint 01
(`INTAKE_ALPOGE_BRIDGES_20261121.md`). Launched by the main session (Claude Opus 5.5 at effort max). The run: GPT-6 Astra
(ChatGPT Pro mode), a parent and delegated agents. It is still going.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ALPOGE_BRIDGES_checkpoint_03_20261121T0116Z_unzipped`. It was made 01:16:47 UTC,
  after 135 min of work. The checkpoint 01 folder has been retired from `research_returns`; the comparison uses the file
  list and the sizes I recorded at the first intake.
  - `root_core.tex` (29,672 bytes) and `consequences_criteria.md` (55,189 bytes) are unchanged. My checkpoint-01 verdicts
    on BR-AT-01 to BR-ANA-01 and CC-C01 to CC-F03b stand.
  - New modules: `root_springer_archive`, `root_henselian`, `root_linear_archive`, `root_effectivity`, `root_group_rank`,
    `source_masullo_kernel`, `source_K_bridge`, `source_cote123_rational`, `source_cote1348_*`, the `consequences_criteria_*`
    addenda (RESIDUE, Tate2026, WM_formality, abelian_group, adjoint_rank, apposition, cross_cycles) and the `aq14_*` and
    `aq67_*` candidates.
  - LEDGER.md grew from 18 KB to 75 KB.
- **Read in full:**
  - LEDGER.md, the movement sections (lines 129-400);
  - `research/root_springer_archive.tex` (cote 123, all 298 lines of mathematics);
  - `research/root_henselian.tex` (cote 66, all);
  - `research/source_masullo_kernel.md` (F-SM-18 to F-SM-22);
  - Masullo's PDF, p. 495, rendered and read by me (see F-SM-19).
- **Statement level** (from the ledger's dated snapshots), everything else new: cotes 14, 15, 18, 67, 134-8 and 136;
  CC-ST04, CC-RES01-02, CC-WM01-03, CC-AG01-03, CC-XC01-04; F-SM-14 to 17, F-SM-23, F-SM-26 and F-SM-28.
- **Correction carried from the ZETA_TWO intake (§5.2).** My checkpoint-01 intake, §4 item 2, glossed CC-F01b as
  "a Λ-structure gives RH for ζ_X". That is false: Spec Z[1/p] is a Λ-scheme, and its ζ = (1 − p^{−s})ζ(s) has zeros
  2πik/log p on Re s = 0. Correct reading: CC-F01b gives RH for L(H_c(X_Q̄), s) with its canonical Euler factors, from
  A_D. ζ_X differs from it by the finite factor R_{X,S} of ZETA_TWO ZT04, whose divisors lie on vertical lines and can be
  non-real. I withdraw the gloss and the "next class to try" sentence built on it.

## 1. Verdicts on what is new

| id | statement (short) | uses | verdict |
|---|---|---|---|
| (cote 123, dimension) | Grothendieck's letter to Kostant, 22 Oct 1969 (cote 123, physical pp. 22-23, footers 21-22): dim 𝓑_x = (dim Z_G(x) − r)/2 | none | **correct citation scope**: Steinberg 1976 Thm 4.6, p. 217 and Thm 6.5, p. 223; Springer 1984 Lemma 1, p. 273. Known; not re-proved. The corrected locator (physical page versus footer) is useful. |
| BR-12301 | type A: rank dχ_X = deg m_X on gl_n, deg m_X − 1 on sl_n | none | **confirmed** (trace-pairing argument). |
| **BR-12302** | **Grothendieck's prediction in the letter, that the tangent rank of the adjoint quotient at an orbit of dimension dim G − r − 2 is r − 1 when all roots have the same length and strictly smaller otherwise, is false**: in sp₄ (type C₂), N = [[0, I],[0, 0]] has orbit dimension 6 = dim G − r − 2 and rank dχ_N = 1 = r − 1; the same holds for U = I + N in the group | none | **confirmed by a targeted check, and independently by computation.** By hand, [Y,N] = [[−C, A + A^t],[0, C]], so the centralizer has dimension 4; dc₂\|_N(Y) = −Tr C; dc₄\|_N = 0 because rank N = 2. Separately, a sympy computation of my own (scratch, 21 Nov) gives centralizer dimension 4, orbit dimension 6, dc₂ = −(c₀ + c₂), dc₄ = 0, rank 1. The group version (dt_U(UY) = Tr(NY)) is checked. |
| BR-12303 | Springer fibres: #X_x(F_{q^{mr}}) = Σ b_{2i} q^{mri} for suitable m | none (Springer 1984 Thm 1, Cor 1 to Thm 2, Lemma 4) | **confirmed** (elementary from the cited purity and root-of-unity statements). |
| BR-12304 | SL₂, x = 0: Q_s(0) = 1 − q, so the passage in intake SA20 D.018 from positive counts to nonnegative Green coefficients is false | none | **confirmed** (the swap acts by −1 on H²((P¹×P¹)∖Δ)). Standard; a correction to our SA20 intake. |
| F-SM-23 | cote 123: rational singularities, affirmative by classical results plus a group-fibre reduction | none | statement level. |
| BR-66-01 | for an affine pair (A, I): henselian ⇔ H⁰ comparison for all torsion étale sheaves ⇔ comparison in all degrees ⇔ clopen bijection for finite Y → X; degree zero can be tested on f_*F₂ | none (Gabber 1994; Stacks 09ZI, 09XI, 095T) | **confirmed**. This answers Grothendieck's "Suffit-il que ce soit vrai en dim 0 ?" (cote 66, physical p. 4, footer 3, subject 21) affirmatively in the all-torsion-sheaf affine reading. The mathematics is Gabber's plus a short deduction, not new. |
| BR-66-02 | both affine cases named on the sheet (I-adically complete; henselization) are affirmative | none | **confirmed** (Stacks 0ALJ, 0A02). |
| BR-66-03 | one fixed sheaf in degree 0 does not suffice: G_m, Z = {1}, F = Z/2, the double cover u² = t | none | **confirmed**. |
| F-SM-18 | a trace-class operator has an L¹ trace density with ‖d_S‖₁ ≤ ‖S‖₁; for a genuine indentation the shell tails of Masullo's diagonal sum are dominated | conditional on the draft's trace-class input | statement level (the summary argument is sound: singular-value expansion; the weights are nonnegative and sum to 1). |
| **F-SM-19** | **Masullo's printed orbital indentation (11.3.2.2), p. 495, is identically zero, and the literal Theorem 11.3.2.1 then fails** (F = Q, S = {∞}, h ∈ C_c^∞((3/2, 5/2)), h(2) = 1: right side log 2, left side 0) | — | **confirmed against the PDF.** I rendered p. 495 of `Papors/Chatnotes/Zeta-Function-Foundation/literature/masullo_grh_20261120/Masullo_the-music-of-the-primes.pdf`. The display reads u₀(x,y) := Σ_{ξ∈F^×} ∫_{g∈E¹_F} 1_{τ(R>0)}(ξgx) ⊗ 1_{τ(R>0)}(ξgy), with no differential printed. The run's transcription is faithful; it writes a product for ⊗, which is the only reading with a common g. With the Haar measure dμ₁ of the adjacent (11.3.2.1), and E¹_Q = Ẑ^× atomless, the integrand is nonzero for at most one g, so u₀ ≡ 0. **Weight:** this is almost certainly a slip in writing the indicator. The evident intended function is the indicator of the fundamental domain τ(R>0)·E¹_F, which is exactly the run's repair F-SM-20 (Z = R>0 × Ẑ^×). It refutes the formula as printed, not Masullo's argument. |
| F-SM-20 | Z = R>0 × Ẑ^× is a clopen fundamental domain for Q^× and gives a valid indentation; compact averaging E = JJ* commutes with the operators | — | statement level (both facts are standard and correct as stated). |
| F-SM-21, F-SM-22 | with a test h having h(2) = 1, A₀(h) = P(h) = 0: the global zero trace is log 2/√2 while the unchanged S = {∞} local trace limit is 0, so no trace-preserving transport makes the naive kernel difference trace-norm small; a multiplicative Dirac replacement is not compact | conditional on the draft's identifications | statement level. They locate the remaining gap in Masullo §12.3 exactly: a global-to-local intertwiner carrying the prime contributions. |
| cote 14 (AQ-14-QUASIPROJECTIVE, AQ-14-NONPROPER, alteration) | forward cohomological implication for all smooth quasiprojective parameters in every characteristic; the integral comparison in characteristic p reduced to a p-primary discrepancy | none | statement level (the run reports two independent whole-proof readings). |
| cote 15 (CC-AG01-03, CC-XC01-04, effectivity) | full abelian-sector classification from the 2026 Tate/standard-conjecture results for abelian varieties; spectral integrality/effectivity of numerical motives ⇔ full Tate; the gate for arbitrary X reduced to a determinant nonvanishing | none | statement level. **To verify before any use:** the "current 2026 primary work supplying all-abelian Tate and standard conjectures" (`consequences_criteria_Tate2026.md`). I did not identify or open it. |
| cote 67 (AQ-67-EXACT, AQ-67-NONHOLO) | one-node capping: real image, tangent and π₁ statements proved; the complex-analytic strengthening refuted | none | statement level. |
| cote 134-8 (BR-13401-06, F-SM-17, F-SM-26, F-SM-28) | the linear "Thm(?)": proved over fields and Z, under finite pure-injective dimension, for locally f.g. projective ringoid morphisms, and for D of type FP∞; the finite-flat-dimension route excluded; a sequential-diagram example shows FP∞ does not follow from compactness of unit and interval | none | statement level. The unrestricted counit/Tor gate remains. |
| CC-ST04, CC-RES01-02, CC-WM01-03, F-SM-14-16 | stable curve (separating divisors; exit/right-Kan comparison); weight-monodromy known classes and formality; the K/class-group comparison | none / cited 2026 arithmetic | statement level. |

**Counts for what is new at checkpoint 03.**
- Confirmed with every step checked: 9 (BR-12301, BR-12302, BR-12303, BR-12304, BR-66-01, BR-66-02, BR-66-03, F-SM-19,
  and the cote 123 citation scope). Of these, BR-12302 also has an independent computation, and F-SM-19 is checked
  against the PDF page.
- Statement level, no fault found: about 30 (the rest of the table).
- Gaps: 0. Refuted: 0.

## 2. What is new

- **BR-12302 is a genuine correction to Grothendieck**: a stated prediction in his letter to Kostant (cote 123) is false
  in the first non-simply-laced case. The ledger says the run has since specified every Lie-type rank, with subregular
  rank r − 1 in every type, so the strict prediction fails in every non-simply-laced type. That part is statement level.
  - **Literature:** not searched by me. The rank of χ restricted to the subregular Slodowy slice is in the circle of
    Brieskorn (ICM 1970) and Slodowy (LNM 815, 1980), which came out of exactly these Grothendieck questions. Whether the
    rank r − 1 in types B, C, F, G is stated there is the gate.
- **F-SM-19 to F-SM-22** are the first concrete defect reports on Masullo's draft from our runs. F-SM-19 is a slip with an
  evident repair (F-SM-20). F-SM-21/22 locate the substantive gap: the global-to-local intertwiner of §12.3-§12.4, in
  Thm 12.4.1.1, pp. 514-519.
- **Cote 66, subject 21:** the answer is Gabber's affine proper base change. It is new only as the reading of the archive
  question.
- **Against tonight's other runs:**
  - F-SM-19 agrees with CX_GRH, ZETA_TWO and AN_GRH that 13.3.1.2 is blank. No other run looked at p. 495.
  - The Bach constant (Thm 2 versus Thm 3, coefficient 2 versus 3) is handled the same way by CX_GRH (CX-N02), this run
    (CC-C04) and AN_GRH (T01).

## 3. The scope of the two proofs

None of the new findings uses A_D or M as an input. The cote 123, 66, 14, 15, 67 and 134-8 work is unconditional. The
Masullo findings are about the draft, conditional where they say so. No statement claims more than its input gives.

## 4. Integration, with the attack each finding opens

1. **Cote 123** (letter to Kostant):
   - In the archive notes and the SA intake that carries cote 123, the reading of physical p. 23 should record:
     - the dimension formula is a theorem (Steinberg 1976, Thm 4.6 and Thm 6.5);
     - the strict non-simply-laced rank prediction is false (BR-12302, sp₄ subregular), with the run's all-types rank
       table to follow at its final.
   - Correct the locator "123/023": it is a physical PDF page, footer 22.
   - Next attack: what Grothendieck's prediction *should* have been. The rank deficiency in non-simply-laced types appears
     not at the subregular orbit but at orbits where the Slodowy slice singularity is a folded (non-simply-laced)
     configuration. The run's all-types table is the place to read off the correct statement.
2. **Cote 66, subject 21:** record "affirmative: Gabber 1994 (Stacks 09ZI) with the idempotent criterion (09XI); the
   fixed-sheaf reading fails (BR-66-03)". The open part is Grothendieck's non-affine reading. The next attack is
   quasi-compact separated schemes with an ample family, where the henselian-pair criterion still makes sense.
3. **SA20 intake, D.018:** the positivity claim for Green polynomials is false; cite BR-12304.
4. **Masullo:** F-SM-19 should go to the author as an erratum note, with the repair F-SM-20. It should not be posted
   (§6). F-SM-21/22 and R-MAS-KERNEL feed prompt 33's successor as the precise check target.
5. **Prompts.** Prompts 30-35 are sent. Their successors get:
   - 33: F-SM-18 to F-SM-22;
   - 35: the corrected CC-F01b reading above;
   - 32: CC-WM01-03.

## 5. Prompt updates for the successor

- Ask for the all-types rank table of cote 123, written as a correction to Grothendieck's prediction, with a literature
  check against Brieskorn 1970 and Slodowy 1980.
- Ask the run to name and attach the "2026 Tate/standard-conjecture" source behind CC-AG and CC-XC. No intake can weigh
  those findings without it.
- Ask for the Masullo defects F-SM-19 to F-SM-22 as a short, separate note with exact page and equation numbers, fit to
  send to the author.

## 6. Hexagon readiness (the five tests of `field_experts/HEXAGON_CANDIDATES.md`)

- **BR-12302 (cote 123 counterexample).**
  - 1, complete: yes.
  - 2, self-contained: yes; no A_D or M input.
  - 3, stable: the counterexample cannot be superseded. The run's all-types table could extend it into a better post.
    No literature search yet.
  - 4, checked: an intake targeted check plus an independent computation (mine); my read of a write-up is still to come.
  - 5, interest now: moderate (Lie theory, readers of the archive).
  - **Gates left:** the literature search (Brieskorn, Slodowy, Kostant's reply if it exists), then the all-types table
    from the final. Best posted as "Grothendieck's 1969 letter to Kostant: what holds and what does not", together with
    the dimension formula. **Candidate, one gate (literature) from 1-4.** Not urgent.
- **F-SM-19 (Masullo p. 495).** It passes 1, 2 and 4, and it is of interest now. But it is a typographical-level defect
  with an evident repair in an unrefereed draft under active study (Conrad). A post would be uncharitable and would be
  superseded by the author's next version (fails 3). **Not a Hexagon post**; send it to the author as an erratum,
  following the memory rule "draft emails when a gap is found".
- **BR-66-01 to 03, BR-12301, 12303, 12304:** correct but known in substance; fail test 3 (literature) or 5. Not posts.
