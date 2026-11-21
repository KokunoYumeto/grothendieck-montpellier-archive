**The attached files.** Besides this file there is one ZIP, `CUE_GCT_random_matrices_and_isolation_through_GCT.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_AGKS_hitting_sets_ROABP_basis_isolation.zip` is the folder `LIT_AGKS_hitting_sets_ROABP_basis_isolation/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# CUE_GCT: the random-matrix side of the Riemann hypothesis, and derandomized isolation, through geometric complexity theory

This prompt is one of a set run in parallel on what the two proofs of 20 November (Alpöge's, cited as a theorem; Masullo's, a draft) make true. Prompts 24-28 treat P versus NP through geometric complexity theory: Mulmuley's nonstandard Riemann hypothesis, plethysm, Kronecker coefficients, Grothendieck's inequality, and the GRH and ETH results in complexity. This one treats the random-matrix side of the zeros, and derandomized isolation, through geometric complexity theory. Keep to this prompt's questions; the others are asked there.

## The results cited

**Alpöge.** On 20 November 2026 Levent Alpöge (a number theorist: Bhargava's student; Harvard Society of Fellows)
posted a four-page note and a complete Lean formalization of a proof of the Riemann hypothesis and of GRH for Dirichlet
L-functions, found with Claude. `ALPOGE_Main.lean` proves Mathlib's `RiemannHypothesis` and the Dirichlet statements
(defined in `ALPOGE_Statements.lean`); a text scan of all 175,187 source files (`ALPOGE_LEAN_SCAN.tsv`) finds no sorry,
axiom or native_decide. It has not been refereed, and that is not our concern here: its theorems are cited as theorems,
L. Alpöge, *Remark*, https://alpo.ge/remark.pdf (attached as `ALPOGE_remark.pdf`), with its Lean archive. The steps of
the note used below (numbered as in its pages 1-4): step 2, p-adic divisibility of derivatives of CM theta values at
inert primes; steps 3 and 5, the count qN = M^k + R on the path quadric and the "sign-only proof of Weil and Deligne"
(a definite sign from middle cohomology, square-root cancellation by iterated Parseval, opposite signs forbidding
cancellation of inverse roots); steps 4 and 7, positivity by determinants and Gan-Gross-Prasad periods (values 0 or 1
for interlacing weights); step 8, iterated theta lifts between totally definite unitary groups, each winning one order
of multiplicity; step 13, the Bost slope inequality; step 17, the groups H^1(o_E[1/l], Q_l/Z_l(-e)) and a weakening of
Vandiver's conjecture.

**Masullo.** A. M. Masullo, *The Music of the Primes* (940 pages, a draft posted 20 November 2026 and announced by
R. Vakil), proposes a proof of GRH for the Hecke L-functions of every number field (its §1.2), by adelic θ-functions,
idelic zeta functions and a trace formula on "orbital Schauder bases". It is neither refereed nor formalized: cite its
statements as the draft's claims, by chapter and statement number (`MASULLO_STATEMENTS_INDEX.md` lists all 336 numbered
statements with their PDF pages), and mark every finding that depends on it as conditional on it.

## Where things stand

- **Pair correlation (the Montgomery-Odlyzko law).** Montgomery (1973) proved, assuming RH, that the pair correlation
  of the zeros of ζ agrees with that of random unitary (GUE/CUE) eigenvalues for test functions whose Fourier transform
  has support in (−1, 1). Dyson recognised the random-matrix form, and Odlyzko's computations support the full
  conjecture. With Alpöge's theorem, Montgomery's theorem holds unconditionally.
- **Quantum chaos.** Berry and Keating (H = xp), and the Bohigas-Giannoni-Schmit conjecture, read the zeros as the
  spectrum of a quantized chaotic system without time-reversal symmetry, hence GUE statistics. Cite these from your
  knowledge with locators, and mark what you take from memory.
- **Families (Katz-Sarnak).** The low-lying zeros of families of L-functions follow the statistics of U(N), USp(2g) or
  O(N).
  - Over function fields this is a theorem, through Deligne's equidistribution theorem (Weil II) and the monodromy
    groups of families.
  - Over number fields it is proved for restricted support under GRH: Hughes-Rudnick for Dirichlet families (attached),
    and Iwaniec-Luo-Sarnak for GL_2 families, which needs GRH beyond Dirichlet and Hecke L-functions.
- **Moments.**
  - Keating and Snaith predict the moments of ζ from the moments of characteristic polynomials over the CUE. The
    Conrey-Farmer-Keating-Rubinstein-Snaith recipe is attached.
  - Bump and Gamburd (attached) show that averages of products of characteristic polynomials over U(N) are characters of
    irreducible representations of U(2k) with rectangular highest weight (N^k). So the CUE moment constants are
    dimensions of rectangular GL_(2k)-representations.
  - A representation-theoretic approach to moments over function fields is attached.
- **Invariant theory.** By Molien-Weyl, the Hilbert series of a ring of invariants is a Haar integral over the compact
  group of 1/det(1 − tρ(k)). The characteristic polynomial of the Keating-Snaith moments is this Molien denominator.
- **Geometric complexity theory.**
  - Multiplicities in the coordinate rings of the orbit closures of the determinant and the padded permanent;
    rectangular Kronecker and plethysm coefficients (Ikenmeyer-Panova); Bürgisser-Ikenmeyer-Panova's theorem that
    occurrence obstructions do not suffice.
  - GCT IV, VII and VIII: nonstandard quantum groups and their positivity.
  - GCT V: derandomized polynomial identity testing against explicit Noether normalization.
  - Forbes-Shpilka (attached): explicit Noether normalization for the ring of matrix invariants in quasi-polynomial
    time, through hitting sets for read-once algebraic branching programs (ROABPs).
- **Derandomized isolation.**
  - Hoza, *NL = UL* (ECCC TR26-323, posted 20 November 2026, attached): an explicit min-isolating weight-assignment
    generator for width-w length-n layered digraphs, with seed length O(log(wn)). With Reinhardt-Allender (SICOMP
    2000), it gives NL = UL. It derandomizes the isolation lemma of Mulmuley-Vazirani-Vazirani for paths.
  - Agrawal-Gurjar-Korwar-Saxena (attached): basis-isolating weight assignments give quasi-polynomial hitting sets for
    ROABPs; polynomial-size hitting sets are open.
  - Kabanets-Impagliazzo: derandomizing general PIT forces circuit lower bounds (NEXP ⊄ P/poly, or the permanent needs
    super-polynomial arithmetic circuits).
- **Pseudorandomness from purity.** Weil's bound for curves gives small-bias sets (the quadratic-character
  construction of Alon-Goldreich-Håstad-Peralta) and algebraic-geometry codes. Deligne's Ramanujan bound gives the
  Lubotzky-Phillips-Sarnak expanders. Dirichlet GRH, now a theorem, gives deterministic quadratic non-residues and square
  roots mod p in polynomial time (Bach's bound 2 log² p). Prompt 28 treats that last point; cite it, do not redo it.

## The task

These links are real; none of them is a mere corollary, or it would already be known. So the task is not to ask whether
they hold but to show how they work, and then to use the new results to attack the open problems. Where a route meets an
obstacle, locate it exactly and attack it with the next tool the new results give. An obstacle is never an end point.

1. **The rectangular bridge.** Bump-Gamburd's rectangular characters and the rectangular shapes of geometric complexity
   theory are the same representation theory of GL. The shapes in question:
   - the rectangular Kronecker and plethysm coefficients;
   - the multiplicities in the coordinate rings of the orbit closures of det_n and of the padded permanent.

   Show exactly how the moment identities and the CFKRS recipe (its sum over swaps) act on those multiplicities. Then
   use them to prove positive formulas, bounds or identities for the rectangular coefficients that geometric
   complexity theory needs.
2. **Haar integrals.** Write the multiplicities geometric complexity theory needs as Haar integrals over compact groups:
   Molien-Weyl; Kronecker coefficients through U(n) × U(m) ⊂ U(nm); plethysm through powers, after Rains's theorem on
   the eigenvalues of U^k. Then bring the methods of random-matrix theory to bear on them, positivity above all:
   Weingarten calculus, the ratios recipe, Gelfand-Tsetlin and RSK counts. Prove what they give.
3. **Isolation through geometric complexity theory.** Hoza's min-isolating generator and the basis-isolating weight
   assignments of Agrawal-Gurjar-Korwar-Saxena isolate in the same layered structure.
   - Show how the first carries over to the second, and use it to build polynomial-size hitting sets for width-w
     ROABPs.
   - From those, derive polynomial-time explicit Noether normalization for matrix invariants (Forbes-Shpilka) and its
     consequences in GCT V.
   - Where the transfer meets an obstacle, locate it exactly and push the next construction.
   - State isolating weights as one-parameter subgroups: Gröbner degenerations to an initial monomial, and open cones of
     the normal fan of a Newton polytope.
4. **Pseudorandomness from purity.** Equidistribution of Frobenius is algebraic geometry's source of explicit
   pseudorandom objects (Deligne; the monodromy groups of Katz-Sarnak), as Weil's bound gives small-bias sets.
   - Use it to construct explicit isolating weight families or hitting sets for ROABPs, and prove what it gives.
   - Bring in what Dirichlet GRH (Alpöge), and conditionally Masullo's claim, add over number fields.
5. **What is now unconditional.** List the random-matrix statements about zeros that were proved under RH or GRH,
   with the GRH each uses. Mark each as unconditional by Alpöge, conditional on Masullo only, or beyond both, naming the
   missing statement.

## The attached files

- `LIT_Bump_Gamburd_averages_of_characteristic_polynomials/`, `LIT_CFKRS_integral_moments_of_L-functions/`,
  `LIT_Hughes_Rudnick_low-lying_zeros_linear_statistics/`, `LIT_representation_theory_approach_to_moments_function_fields/`,
  `LIT_Forbes_Shpilka_explicit_Noether_normalization_matrix_invariants/`, `LIT_AGKS_hitting_sets_ROABP_basis_isolation/`:
  LaTeX sources (arXiv).
- `LIT_Mulmuley_GCT_V_Noether_normalization/`, `LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/`,
  `LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/`, `LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/`,
  `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/`, `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`,
  `LIT_Landsberg_GCT_introduction_for_geometers/`: LaTeX sources.
- `ECCC_TR26-323_Hoza_NL_equals_UL.pdf` (no source posted).
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`; `MASULLO_STATEMENTS_INDEX.md`.
- `ARCHIVE_133_*.tex`: Grothendieck's pages on λ-operations and plethysm (cote 133), with `SA17_STUDY_cote133_lambda.md`.

## The language of the results

Whatever the outcome for P versus NP, the mathematics of this prompt has to transfer to our programme on Grothendieck's
work. So every finding is also stated, with its proof or the exact dictionary that carries the proof across, in the
language of algebraic geometry and of Grothendieck's own frameworks: schemes and group schemes over Z (SGA 3), λ-rings,
K_0 and the γ-filtration (SGA 6), representation rings as K_0 of categories of representations, Schur functors as
operations on locally free sheaves, orbit closures as schemes over Z with their Hilbert and Quot schemes (FGA), ℓ-adic
sheaves, weights and purity (SGA 4, SGA 5, Weil II), motives where they apply. For each finding, say where it lives in
Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact locator. A finding proved in
combinatorial, representation-theoretic or complexity language is stated again in this language in the paper, in a
part of its own, with the dictionary.

## How to work

The rule that governs everything below: push. Work on the main question first: how the random-matrix side of the zeros (Bump-Gamburd's rectangular characters, Haar integrals and the moment recipes) acts on the rectangular Kronecker and plethysm multiplicities of geometric complexity theory, used to prove their positivity; and Hoza's isolation generator carried to polynomial-size hitting sets for ROABPs. Give it most of the time.
When one approach stalls, take the next one. Deliver nothing while an item is undecided and an untried approach
remains. A gap in a proof is an undecided step: attack it, never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the strongest
proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly
smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement.
After two consecutive reviews without movement, stop that work, write the final package with every item's state, and
deliver it; this check takes precedence over the rule about untried approaches.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type
of what actually happened, neither more nor less. Cited statements you use get their events too.

Every proof is checked before the package is final, by a reading of the whole proof, and the check is recorded with
who, how, model, effort and date. A proof that fails its check is reported with its gap.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `CUE_GCT_checkpoint_<NN>.zip` with `NN` counting up.
Never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save
checkpoints once every 45 minutes and at no other time. A checkpoint is one ZIP holding every deliverable written so far
and everything that documents the work, so that a new session can continue from it and the attached files. It is never
a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.

## What to deliver

One final ZIP, `CUE_GCT_final.zip`, holding:
1. **The paper**, `CUE_GCT.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
5. **`TRANSCRIPTION_NOTES.tsv`**: every place where the mathematics shows that our text of record of cote 133 misreads
   Grothendieck's page: cote, scan, line, our reading, the reading required, the reason, how sure you are.
4. **`IMPLICATIONS.md`**: what the findings change, for P versus NP through geometric complexity theory and for
   Grothendieck's texts (cote and scan).

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
