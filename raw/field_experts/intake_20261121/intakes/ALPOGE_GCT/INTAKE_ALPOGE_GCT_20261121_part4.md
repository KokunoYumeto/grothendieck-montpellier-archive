# Intake of ALPOGE_GCT, part 4: the final return (checkpoint 09, 21 Nov 2026)

Intake by Claude Opus 5.5 at effort high (agent a0805369bae2ebddc), at the main session's request (Claude Opus 5.5 at
effort max). The run is GPT-6 Astra (ChatGPT Pro mode); its files say its effort is not exposed. Parts 1-3 and the
checkpoint-03 addendum precede this part. Work file: `agent_notes\a0805369bae2ebddc_NOTES.md` (mirror:
`agent_notes\20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md`).

## 0. Return read and scope

- **Folder:** `research_returns\ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped`, assembled at 05:47 UTC. Under the
  user's rule this is the run's **final return**: its newest return is more than three hours old.
  - The paper in this snapshot has 273 pages and integrates the findings through P-F72.
  - `CHECKPOINT_09_LATE_FINDINGS.md` adds P-F73 to P-F75 as checked standalone fragments that are not yet integrated.
  - P-F76 was still being researched when the run stopped.
- **Read since checkpoint 06:**
  - LEDGER, all entries from 03:56 to 05:45 UTC, including the five- and six-hour formal reviews;
  - the final question states (Q-PH1, Q-PH3, Q-PH3-WEAK, Q-SH-REVISED, Q-NONSTANDARD, Q-ALPOGE-METHOD,
    Q-MAIN-SEPARATION);
  - CHECKPOINT_09_LATE_FINDINGS.md.
- **Read in full, with the proof:**
  - **P-F57** (`work/positivity_dyadic_dominance.tex`, all of it);
  - **P-F56** (`work/positivity_paired_wave.tex`, lines 1-900): the pole classification (P-F56a), the period
    (P-F56b), the wave identity (P-F56d), the one-witness test (P-F56e'), the dominant-pair reduction (P-F56l) to
    (P-F56p), the exact residue product (P-F56u) to (P-F56v), the increment recursion (P-F56aa) to (P-F56aj), and the
    sparse separation lemma (P-F56an).
- **Not read:** the remainder of P-F56 (the active-triple estimates behind (P-F56al)). P-F57 does not use it: it
  proves its own near estimate (P-F57b).
- **Read at statement level:** P-F58 to P-F75. Within those, P-F60 and P-F63 I read up to their statements.
- **No sign of change since part 2:** P-F31 and its inputs (P-F23, P-F24, P-F26, P-F27, P-F28, P-F30), P-F19, P-F14
  and P-F15. At the time of this part I saw no check event after 03:30 UTC on them, and their files had the byte counts
  I had listed at checkpoint 05 (`positivity_actual_cubic_pole.tex` 8,921 bytes, and so on). I compared no contents.
  Nothing from parts 1-3 is withdrawn.
  - After the fact, 22 Nov, by content, against my stored outputs of the earlier reads (`chk/gctpos/seg_compare.py`,
    `seg_more.py`): P-F31, P-F23 and P-F30 are the same as at checkpoint 05 (whole files); P-F14 and P-F15 the same as
    at checkpoint 03 (whole file); P-F26 the same as at checkpoint 05 in lines 1-40 of 229, the range compared.
    P-F24, P-F27 and P-F28 have not been compared. P-F19 has not been compared with checkpoint 05; against checkpoint
    03 it differs in two passages on scope.
  - *Corrected 22 Nov 2026. The old wording was: "Unchanged since part 2: [the same list]. No check event after 03:30 UTC
    touches them, and the file sizes are byte-identical to checkpoint 05." Only sizes had been compared.*

## 1. Verdicts on the new findings

### P-F56 and P-F57: PH2 and SH(a) fail for ordinary plethysm with inner shape (3)

**Statement.** For the cubic family f_n of P-F31:
- μ = (3), λ = (n/g), π = det^{3/g}, g = gcd(n,3);
- f_n(s) is the multiplicity of det^{3s/g} in Sym^{(n/g)s}(Sym³ C^n), that is, the dimension of the SL_n-invariant
  n-ary cubic forms of that degree;
- for every fixed 0 < c < 1/4 and all large n, p(f_n) > 2^{cn} and s(f_n) ≥ 2^{cn};
- explicitly, p(f_n) > 2^{n/8} and s(f_n) ≥ 2^{n/8} for n ≥ 2·10⁸⁰.

GCT VI's parameter is h = Θ(n⁶). So the narrow PH2 (Hypothesis 1.6.6) and SH(a) (Hypothesis 1.6.5(a)) are false on
an ordinary irreducible-inner plethysm family. The density clause SH(b) (Hypothesis 1.6.5(b)) is not claimed false.

**Check.** Targeted proof check, plus independent computations. **Confirmed.**

The proof's logic, step by step, each step checked:
1. **The wave identity (P-F56d).** The poles of H_n whose order has two-part at least M = 2^{n−1} are exactly the
   primitive M-th roots, and these poles are simple (P-F56a). The proof applies the Koszul fixed-locus criterion
   (P-F23 in dimension zero) and P-F30 at two-power order 2^a > M. So the least period L has v₂(L) = n−1, and
   q_r − q_{r+L/2} = 2W_n(r) is a constant, the dyadic wave W_n.
2. **The one-witness test (P-F56e').** If p(f_n) ≤ x, then every constituent is ≥ 0 at x, so f_n(x) = q_x(x) ≥ 2W_n(x).
   The same holds if s(f_n) + 1 ≤ x. So one x with 2W_n(x) > f_n(x) gives p(f_n) > x and s(f_n) ≥ x. I rechecked
   this against GCT VI Definitions 1.2.2 and 1.2.4. It uses the constituents at x, not only f's own residue class.
3. **The exact residue (P-F56v).** C_n(ζ) = ∏_{b∈S_n}(1−ζ^{gb})^{−1}, over an explicit multiset S_n of C(n,3)
   weights. The multiset comes from the conormal character Sym³V − V⊗V* at the chain point.
4. **The amplitude (P-F56m).** log₂|Z_n| ≥ n⁴/24 − 2n³ for the selected pair a = ±3^{−1} mod M.
5. **Dominance (P-F56l to P-F56p).** If the other residues have total mass E_n ≤ |Z_n|/4, then in every window of
   r ≤ 9 consecutive integers some x has W_n(x) ≥ |Z_n|/4. At x ≈ 2^{cn} the ambient dimension bound gives
   log₂ f_n(x) ≤ (c/6)n⁴ + O(n³ log n). That is below n⁴/24 exactly when c < 1/4.
6. **E_n/|Z_n| → 0 (P-F57).** This goes through the increment recursion P_n(a) = J_n(a)·P_{n−1}(−a), the
   selected-sibling bound (P-F56ae), and the contraction Q_n ≤ ρQ_{n−1} + 2δ_n. P-F57 proves the contraction
   (P-F56ad) with ρ = 1/2 in two ranges:
   - *near multipliers*, j ≤ 2^{δn}: the factor-by-factor logarithmic estimate (P-F57b), giving the ratio
     ≤ 2^{−n² log₂ j/12};
   - *far multipliers*: the layer-cake count of small phases (P-F57f4) and the four-cell anchor loss (P-F57f5)-(f6),
     which uses w_{j+1} = −2w_j. Against the lower bound (P-F57f9) on the selected increment, this gives the ratio
     ≤ 2^{−δ³n³/384}.

   I checked the counting in (P-F57f4) (early, mixed and late pairs, the subset-sum injectivity), the
   identity y_{jk} + y_{j+1,k} + y_{j,k+1} = 3θ, and the arithmetic in (P-F57f8)-(f9) and (P-F57g1)-(g5).

**Independent computations** (`chk/pf57.py`):
- **(P-F56v) agrees with classical invariant theory, phase included.** At n = 4, Salmon's series
  (1+t²⁵)/((1−t²)(1−t⁴)(1−t⁶)(1−t⁸)(1−t¹⁰)) gives lim (1−t⁸)H(t) at ζ = e^{2πi/8} equal to 0.125 + 0.30178i. The
  product over S₄ = {1, −2, 4, 2} gives the same number to 15 digits.
- **Q_n = E_n/|Z_n|, computed exactly from (P-F56aa)** by summing over all odd residues mod 2^{n−1}, for n = 5..16:
  24.3, 25.3, 3.44, 9.4·10⁻², 9.7·10⁻⁴, 1.2·10⁻⁶, 1.1·10⁻¹⁰, 4.6·10⁻¹⁶, 6.5·10⁻²³, 2.0·10⁻³¹, 8.8·10⁻⁴², 3.7·10⁻⁵⁴.
  So E_n ≤ |Z_n|/4 already holds from n = 8, and the decay is super-exponential, as P-F57 says.
- log₂|P_n(b_n)| grows like n⁴/24 − 0.35n³ (for example 1,240 at n = 16, against n⁴/24 = 2,731). This is consistent
  with (P-F56m).

**What is not read by me:** P-F28's proof of e_Y = 1. The n = 4 residue check covers it there, phase included, but
not for general n. The remainder of P-F56.

### The other findings, at statement level (no fault seen)

- **P-F60.** The triple-rectangular Kronecker analogue: the chain tensor in (C^n)^{⊗3} has full stabilizer with
  χ(Stab) = μ_{2^{n−1}}. The canonical-parameter clause of PH3 for Kronecker coefficients is therefore false, against
  a source rank of n² + 5n. The numerical PH3, global pole and strict-index questions for Kronecker remain open; P-F65
  finds a second fixed component with the same phase.
- **P-F62.** Explicit cubic inputs that are positive from the start and realize every stretch, still with exponential
  strict indices.
- **P-F63.** The broad, product-closed SH(b) (GCT VI Hypothesis 3.3.2(b)) fails under an explicit finite
  input-coding convention. A fixed product factor with nonzero saturation index is adjoined at constant cost, giving
  E(N+C) ≥ A(N). This depends on the coding convention, which the run states. It says nothing about the narrow
  SH(b), Hypothesis 1.6.5(b).
- **P-F64, P-F67, P-F71, P-F75.** Shortcuts refuted, and density and conductor scope results. P-F71: at
  n = binom(3r−1,2) the symmetric coefficient is 1 and the tensor coefficient 0, which refutes universal surjectivity
  and module splitting.
- **The nonstandard (GCT VII) and theta branch: P-F52, P-F58, P-F59, P-F61, P-F65, P-F66, P-F68 to P-F70, P-F72 to
  P-F74.**
  - P-F52: an actual positive quadratic order and source intertwiner.
  - P-F73: full source faithfulness.
  - P-F74: polarizations from ample line bundles.
  - P-F66: no literal geometric Frobenius eigenvalues for the actual split source numbers.
  - P-F68: fixed finite definite-theta data cannot produce the full input Θ_{E6}/δ.
  - P-F69, P-F72: exact Frobenius-trace realizations on an abelian surface and a pure cohomology space.
  - What remains open: formal grading, canonical coefficient objects and bases, and the comparison with Alpöge's
    theta operations.

**Counts for part 4:** 2 read in full and confirmed (P-F56, except the part not used, and P-F57); 0 refuted; 0 gaps;
0 withdrawn; about 20 at statement level.

## 2. What the run settled in the end, and what it left open

**Settled.** The proofs are checked in parts 1-4.

| GCT VI hypothesis | Final state | Findings |
|---|---|---|
| Thm 1.6.1(d), as printed | false (KM ray) | P-F12, PL-Q22 |
| PH1 homogeneous (1.6.4) | false (cited KM); repaired by shifted polytopes | P-K1, P-F1, P-F2 |
| PH3 canonical clause (1.6.7, plethysm) | false | P-F19 |
| PH3 existence clause (1.6.7, plethysm) | false | P-F31 |
| **PH2 (1.6.6) and SH(a) (1.6.5(a)), plethysm** | **false, with exponential indices** | **P-F56, P-F57** |
| PH3 canonical clause, Kronecker | false (statement level) | P-F60 |
| Broad 3.3.2(a), 3.3.3, 3.3.4 (subgroup restriction) | false as stated | P-F14, P-F15 |
| Broad 3.3.2(b) | false under an explicit coding convention (statement level) | P-F63 |
| PH3 ⇒ PH2 | true, with explicit bound; premise now false | P-F11, P-F12 |

**Open.**
- SH(b), the narrow density clause (1.6.5(b)), for plethysm and for Kronecker coefficients.
- PH2, SH(a) and the numerical PH3 for Kronecker coefficients. Here P-F60 and P-F65 give the canonical clause and a
  second fixed component; the global pole and the strict indices are not done.
- The nonstandard quantum-group positivity (GCT VII-VIII): the canonical coefficient objects.
- The comparison with Alpöge's theta operations (Q-ALPOGE-METHOD).
- Any actual GCT obstruction (Q-OBSTRUCTION, Q-MAIN-SEPARATION). The run makes no complexity claim; P-F8 stands.

## 3. What is new

- **P-F57** is, to my knowledge, the first refutation of Mulmuley's PH2 and SH(a) for plethysm coefficients. It
  needs a literature search: Kahle-Michałek; Briand-Orellana-Rosas only refute the old zero-index SH, which is not
  this; work after 2016 by Ikenmeyer, Panova, Walter, Mulmuley and others.
- **The method is new and general.** It reads a "dyadic wave" off a simple pole of maximal two-part order, and uses a
  single witness against the ambient dimension bound. The tools are an equivariant localization (P-F23), an exact
  extremal-stabilizer classification (P-F30), and an increment recursion in the number of variables.
- **P-F60** carries the stabilizer mechanism to rectangular Kronecker coefficients, which are the coefficients GCT
  actually uses.

## 4. Scope of the two proofs

No finding uses Alpöge's Dirichlet GRH beyond the explicit prime bounds noted in part 3 (P-F47). Nothing uses Masullo.
The theta and nonstandard work uses classical automorphic theory (Borcherds, Kudla, Allcock-Carlson-Toledo, Looijenga,
Honda-Tate), not GRH. No statement claims more than its input gives.

## 5. How the findings bear on the open problems, and the attack they open

1. **The flip's positivity programme for plethysm, as GCT VI stated it, is refuted in all three index hypotheses.**
   GCT VI's route from "positive plus small indices" to polynomial-time saturated integer programming is closed for
   plethysm.
   - What survives is shifted counting (P-F1, P-F2) and positivity itself, which is trivially true.
   - What remains open for an efficient algorithm is SH(b), the "almost everywhere zero index" clause. P-F48 shows the
     counterexamples are exponentially sparse, so SH(b) may still hold.
   - **Next attack on SH(b):** a density argument through the same mechanism. The fraction of inputs (λ, μ, π) of
     length N whose stretching ring has a stable point with large determinant-character stabilizer order is small. If
     that is the only source of nonzero saturation index, SH(b) follows. So the question is a converse: do small
     stabilizer characters at all fixed loci imply index 0? The P-F23 formula is the tool.
2. **Kronecker coefficients,** the ones GCT's obstructions use (rectangular, as in Bürgisser-Ikenmeyer-Panova).
   P-F60 gives the stabilizer, and P-F65 gives a second fixed component with the same phase.
   **Next attack:** classify every fixed component of μ_M on Spec of the rectangular Kronecker ring, as P-F30 did for
   cubics; this is now the gate. If the chain component is the only one, or the components do not cancel, the P-F56
   and P-F57 wave argument transfers verbatim. The result would be exponential strict indices for rectangular
   Kronecker coefficients, which bears directly on Mulmuley's flip for permanent versus determinant.
3. **The theta and purity route (Alpöge's steps 7-8).** The run built exact objects for n = 4, 5, 6 (P-F41, P-F46,
   P-F51, P-F55) and located the obstacles exactly (P-F66, P-F68). Purity cannot give the index hypotheses: they are
   false on rings with pure Tate cohomology (PLE-F7, P-F31).

## 6. Prompt updates: what the successor of ALPOGE_GCT needs

1. **State as settled, cite, and do not re-prove:** the table in section 2, with these intakes as the check record.
   Give the successor the exact statements of P-F23, P-F30, P-F31, P-F56, P-F57 and P-F60 as attached sources,
   preferably as the run's LaTeX fragments `positivity_noncancellation.tex`, `positivity_full_cubic_support.tex`,
   `positivity_actual_cubic_pole.tex`, `positivity_paired_wave.tex`, `positivity_dyadic_dominance.tex` and
   `positivity_tensor_chain_point.tex`.
2. **Main question 1, Kronecker.** Prove or refute PH2 and SH(a), and the numerical PH3, for the triple-rectangular
   Kronecker family of P-F60. The concrete gate: classify all μ_{2^{n−1}}-fixed components of
   Spec C[(C^n)^{⊗3}]^{SL_n³}, after P-F65's second component, and control their combined residues.
3. **Main question 2, SH(b).** SH(b) for plethysm (narrow, Hypothesis 1.6.5(b)): prove it or refute it. Use the
   converse question of 5.1 and P-F48's population conventions. Ask for the exact input population and density
   reading to be fixed first, as P-F48 does.
4. **Sharpen P-F57** to an explicit, moderate n. The proof's threshold is 2·10⁸⁰, but my computation shows
   Q_n < 1/4 already from n = 8. What fails at small n is only the crude ambient dimension bound for f_n(x). Ask for a
   computer-assisted explicit witness: an n (around 80-120 by my estimate) and an x with 2W_n(x) > f_n(x). W_n comes
   from the exact product (P-F56v); f_n(x) needs a better upper bound than the ambient dimension, such as a Molien-Weyl
   or Brion bound. That would give a concrete, checkable counterexample to PH2 and SH(a) as polynomial bounds, with
   explicit constants.
5. **Write-up.** Ask for a standalone paper of the PH-refutation chain: P-F23, P-F30 (with P-F27 integrated),
   P-F24, P-F26, P-F28, P-F31, P-F56, P-F57. Every proof in full, and the GCT VI locators exact (printed pages
   13-14, 15, 24-25, 51-57 of arXiv:0704.0229v4).
6. **The project's terms.** Ask that every finding be stated as well in Grothendieck's frameworks:
   - the GIT quotient of cubics as a coarse moduli space;
   - the pole as a fixed-point term in Lefschetz-Riemann-Roch (SGA 6, Exp. VII);
   - the wave as the character of μ_M on a residual gerbe;
   - and, wherever they apply, the λ-ring statements of the cote-133 study (part 1).
7. **Carry the open nonstandard and theta gates** with their current exact gates (Q-NONSTANDARD, Q-ALPOGE-METHOD), and
   P-F76 (the Frobenius-trace obstruction for α±(3^e)), which was in progress.
8. **Checkpoints and check events** as before. Ask the run to integrate P-F73 to P-F75 into the paper.

## 7. Hexagon readiness

**H02 should be re-titled and strengthened.** Proposed title: "PH2, SH(a) and PH3 fail for plethysm: exponential
strict indices from a dyadic wave (cubic invariants)". P-F57 is the headline, with P-F31 and P-F19 as steps and the
Theorem 1.6.1(d) erratum and P-F14/P-F15 as companions. The five tests after the final return:
1. **Complete:** yes. The chain P-F23, P-F24, P-F26, P-F27, P-F28, P-F30, P-F31, P-F56, P-F57 is proved in the run,
   with independent whole-proof checks recorded for each. In my own reading two links are at statement level:
   - P-F27, the q = 0 case of P-F30, which my exhaustive computation covers for n ≤ 4;
   - P-F28's e_Y = 1, which the classical n = 4 residue covers.
2. **Self-contained:** yes. The inputs are published: GCT VI, Luna, Huybrechts (stability of smooth cubics), the
   Stacks Project Koszul lemmas, and the cubic discriminant (Busé-Jouanolou).
3. **Stable:** within our work, yes now, since the run has ended and its successor would extend rather than replace.
   The literature search has not been done.
4. **Checked:** yes, to the register's standard.
   - This intake: targeted proof checks of P-F23, P-F30, P-F31, P-F56 and P-F57.
   - Independent computations:
     - P-F30 exhaustive for n = 3, 4;
     - Salmon's n = 4 series against P-F31 and (P-F56v), phase included;
     - the n = 4 indices;
     - Q_n for n = 5..16.
   - Still needed: the main session's own reading of every page of the write-up.
5. **Of interest now:** high. It refutes all three of GCT VI's quantitative positivity hypotheses for plethysm, which
   were the stated route of the flip. P-F60 points the same way for Kronecker coefficients.

**Gate left:** the literature search, then the self-contained write-up (prompt item 6.5, or our own) and the main
session's reading. The run's final has been taken in. Under the register's rule this is a flag-to-the-user item. The
change from the H02 entry as registered: the headline moves from P-F31 to P-F57, and the "run's final" gate is passed.

**New candidate H02b, statement level only:** P-F60, the Kronecker canonical PH3 clause. Not ready: only the canonical
clause is refuted, and it is not checked by an intake. Gate: an intake proof check, plus the successor's work
(prompt item 6.2).

**H03:** not touched by this run.

## 8. Edits for the register (field_experts\HEXAGON_CANDIDATES.md; not made)

- H02: re-title as in section 7. Set the source to "ALPOGE_GCT final (checkpoint 09): P-F56, P-F57 (+ P-F31, P-F19,
  P-F23, P-F30)". Set the checks to "intake parts 2-4: proof checks; computations pf30.py, pf57.py, q4.py; Salmon
  n = 4 residue match". Set the gate to "literature search; write-up; main-session read". State: flag to the user.
- Add an H02b row for P-F60 (Kronecker canonical PH3), state "candidate (statement level)".
