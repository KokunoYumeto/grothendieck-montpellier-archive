**The attached files.** Besides this file there is one ZIP, `NEG_NIGHT_everything_that_follows_from_the_refutations_of_ET.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `LIT_Briand_Orellana_Rosas_SH_counterexamples.zip` is the folder `LIT_Briand_Orellana_Rosas_SH_counterexamples/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# NEG_NIGHT: everything that follows from the refutations of ETH and of GCT VI's positivity hypotheses, together with the two GRH proofs

This is tonight's whole task, and it is open-ended by design. Within a few weeks, several hypotheses that structured the
study of P versus NP have been refuted: the Exponential Time Hypothesis with its strong, gap and counting forms, and the
positivity and saturation hypotheses through which Mulmuley's geometric complexity theory (GCT VI) proposed to carry out
its "flip" for plethysm coefficients. At the same time GRH became a theorem for Dirichlet L-functions and is claimed for
all Hecke L-functions. The refutations are a few hours to a few weeks old, and nobody has pulled them through the rest of
the theory yet. Do that: derive everything they imply, alone, together, and with the two GRH results, each consequence
proved or located, in one catalogue we can read along with you as the checkpoints come in.

## The results cited

**E: OpenAI, *The Exponential Time Hypothesis is False* (preprint, 25 October 2026; LaTeX attached as
`LIT_OpenAI_ETH_is_False/`).** Cite its statements as theorems, by number.
- **Theorem 1.1.** For each fixed k ≥ 2, a deterministic algorithm counts the satisfying assignments of a k-CNF with n
  variables and m clauses, in (n+m)^{O_k(1)}·2^{O_k(n log log n/√log n)} bit operations and polynomial space; for m ≤ Dn
  the exponent is O_{k,D}(n/√log n).
- **Its core.** It counts the common zeros in {0,1}^n of O(n) sparse polynomials over F₂ (degree ≤ k, ≤ (log n)^c
  monomials each) in 2^{O(n (log log n)²/√log n)}.
- **Its corollaries:**
  - approximate Max-SAT;
  - counting independent sets and q-colourings in 2^{o(v)}, and perfect matchings in 2^{o(v+e)};
  - E^NP ⊄ SIZE(O(n)), with circuit size above c·n√log n infinitely often.
- **Our earlier catalogue.** It records what E refutes and what it leaves standing (CX_GRH CX-E01 to E06): ETH, #ETH,
  fixed-width SETH and #SETH, their randomized forms, Gap-ETH and NSETH fall; OVC, 3SUM, APSP and FPT ≠ W[1] stand.

**The refutations in geometric complexity theory.** GCT VI is Mulmuley, *Geometric Complexity Theory VI: the flip via
positivity* (arXiv:0704.0229v4, attached as LaTeX). Its hypotheses PH1, SH, PH2 and PH3 were to place the relaxed
positivity problems for Kronecker and plethysm coefficients in P.
- **Refuted by our runs** (each in the attached returns and intakes, with its check events):
  - P-F57 (ALPOGE_GCT): PH2 and SH(a) fail for ordinary plethysm with inner shape (3); both indices exceed 2^{cn} for
    every c < 1/4. Checked in full by our intake.
  - P-F19: the canonical clause of PH3 fails for the same family; the degree needed is at least 2^{n−1}, against
    O(n⁶).
  - P-F31: the existence clause of PH3 fails.
  - The run's Q-C-POSITIVE-START-STRICT-INDICES: the exponential index obstructions persist when the initial coefficient
    and every realized positive stretch are positive (statement level for us).
  - GCT VI Theorem 1.6.1(d) is false as printed: on the Kahle-Michałek plethysm ray the generating function is the
    Hilbert series of the D₅ Kleinian singularity (P-F12).
- **Refuted earlier:**
  - occurrence obstructions for padded permanent against determinant (Bürgisser-Ikenmeyer-Panova, arXiv:1604.06431);
  - polynomial-time positivity of Kronecker coefficients, unless P = NP (Ikenmeyer-Mulmuley-Walter, arXiv:1507.02955),
    and of plethysm coefficients even at fixed inner degree (Fischer-Ikenmeyer, arXiv:2002.00788);
  - the strong saturation hypothesis SH for Kronecker coefficients (Briand-Orellana-Rosas, arXiv:0810.3163);
  - homogeneous PH1 for plethysm (Kahle-Michałek, arXiv:1507.07131, Theorem 5).

**A: Alpöge.** RH and GRH for Dirichlet L-functions, with a complete Lean formalization (L. Alpöge, *Remark*,
https://alpo.ge/remark.pdf, attached; our map of the archive is attached). Cite them as theorems.

**M: Masullo.** GRH for the Hecke L-functions of every number field, claimed in a 940-page draft (A. M. Masullo, *The
Music of the Primes*, 20 November 2026). It is neither refereed nor formalized, and our runs found defects with repairs
(`MASULLO_DEFECTS_20261121.md`). Mark every consequence that uses it as conditional on M. The draft itself is not
attached; cite it by statement number as our catalogues do.

**Isolation, 2026.** W. M. Hoza, *NL = UL* (ECCC TR26-323, attached). An explicit min-isolating weight-assignment
generator with seed O(log(wn)) for width-w, length-n layered digraphs gives, with Reinhardt-Allender, NL = UL. The paper
cites Applebaum (2026), NL ⊆ ⊕L and NL ⊆ Mod_pL, which builds on the 2026 bipartite perfect matching result of
Chatterjee-Ghosh-Gurjar-Raj-Thierauf. These derandomize isolation in log-space. Isolation is the randomized step of
Valiant-Vazirani, which is why the NP analogues (NP ⊆ ⊕P, or NP = UP deterministically) belong in the catalogue.

**The nonstandard Riemann hypothesis of GCT.** GCT IV, VII and VIII (attached) define nonstandard quantum groups for
the Kronecker and plethysm problems. They propose that positivity of their canonical bases, and with it PH1, the hypothesis
our refutations leave standing, would follow from a nonstandard Riemann hypothesis: purity over F_q, in the sense of
Weil II, for the associated sheaves. Our run GCT_NSRH (prompt 24, attached with its intakes) carried Alpöge's
sign-only purity mechanism, his step 5, to these objects. It found:
- a conditional sign-only purity criterion, with the path sign always constructible;
- strict positivity only at rank three (F58 fails at rank four);
- no single finite Weil object to carry the purity;
- no bounded Soergel lift (F59).

**The split-zero framework (ours, attached as `OURS_split_zero_corpus/`).** G(R) = R ⊔ {τ}, where τ is an external
additive zero and multiplicative absorber.
- **The classical ideal zeta sheet.** It is exactly ζ_K for R = O_K. The Boolean pair A = {0, τ} ≅ B has infinite
  norm there and does not enter.
- **The separated congruence zeta sheet.** ζ^sep = Σ_{J≠0} (N(J)+1)^{-s} counts τ's class in every quotient. It is
  non-Eulerian. Over Z it equals ζ(s) − 1, and over O_K it is ζ_K plus shifted copies ζ_K(s+k).
- **The Boolean pair as a fixed locus.** For every domain R and every unit u ≠ 1, the fixed locus Fix_{G(R)}(u) is
  exactly A. In particular, A is the fixed locus of the sign −1, and ζ^sep takes the value −1 at every zero of ζ.

So GRH, now a theorem for abelian K by A, holds in a setting that carries an attached Boolean structure without being
disturbed by it. Some of these papers draw on correspondence with a third person; keep every attribution exactly as the
papers state it.

## The task

Derive everything that follows from these results. For each consequence, give:
- its statement;
- its exact inputs: E, which refutation, A, M, and every classical theorem used, with its locator;
- a proof, or the exact locator of a classical proof;
- whether it bears on P versus NP, on VP versus VNP, or on an open row of our runs, and how.

**The refutations are inputs in their own right.** A false hypothesis is a true negation, and its failure says
something about the objects it described. Here those objects are:
- the plethysm and Kronecker semigroups and their stretching quasi-polynomials;
- the moment polytopes and cones against the actual supports;
- the coordinate rings of the orbit closures;
- the satisfiability and counting problems whose exponents were thought fixed.

Derive what each negation implies about them, and what follows when those statements are combined with the rest of the
theory.

The territory, all of it:
1. **Exact and fine-grained algorithms.** What E gives for other problems: through its corollaries, through reductions,
   and through its core on sparse F₂ systems. Which conditional lower bounds lose their support, and which conjectures now
   carry the load.
2. **Circuit lower bounds and derandomization.** How algorithms yield lower bounds (the route by which E proves its
   circuit corollary), and what E and its core give there. Also: hitting sets and PIT, and hardness against randomness.
3. **Counting, parity and isolation.** #P, ⊕P, Toda, Valiant-Vazirani; E as a counting algorithm; isolation and its
   derandomizations (Mulmuley-Vazirani-Vazirani; Hoza's NL = UL; Applebaum's NL ⊆ ⊕L). Also the parity of the number of
   common zeros of sparse F₂ systems, and its algebraic and cohomological expressions: Chevalley-Warning, Ax-Katz, and
   the trace of Frobenius on coherent cohomology mod p (SGA 7 XXII).
4. **Algebraic complexity and GCT.** What the refutations imply for the flip, the obstructions and the semigroups. What A
   and M make unconditional, such as Bürgisser's comparison of Cook's and Valiant's hypotheses and Koiran's
   Nullstellensatz in AM (our CX-K01 to K06). Border complexity.
5. **Representation theory and combinatorics.** Exponential saturation indices, holes, the D₅ Hilbert series, positive
   formulas (our G-036, G-037), the Foulkes and Hadamard-Howe maps.
6. **Proof complexity.** What E's algorithm and its core say about propositional and algebraic proof systems over F₂.
7. **Cryptography and number-theoretic algorithms.** What E, A and M do to the assumptions in use, and what becomes
   deterministic or unconditional.
8. **The combinations.** E with A or M; the GCT refutations with E; and each of these with our runs' open rows.
9. **Transfers between Boolean and algebraic complexity.**
   - Bürgisser's comparison of Cook's and Valiant's hypotheses (Theoretical Computer Science, 2000) runs in one
     direction: in characteristic 0, under GRH, #P ⊄ P/poly implies VP ≠ VNP over C. No converse is known.
   - Determine exactly which GRH it needs (which zeta and L-functions, of which fields), and so whether A suffices or M
     is needed. Our CX-K01 settled the same question for Koiran.
   - Then derive what follows, and whether anything runs in the other direction.
10. **The nonstandard Riemann hypothesis, Alpöge's sign mechanism, and the split-zero framework.** Derive what follows
    from the following, in this order of dependence:
    - **(a)** Run Alpöge's sign-only purity argument with coefficients in G(R)-semimodules in place of Q_ℓ. In G(R) the
      fixed locus of every nontrivial unit, the sign −1 included, is the Boolean pair. Say what purity statement results
      and what its sign-invariant part is.
    - **(b)** Say whether that statement, the classical sheet or the separated sheet supplies the finite Weil object that
      GCT_NSRH lacked, so that the nonstandard canonical-basis structure constants become traces or counts in a setting
      where GRH is now a theorem. Say what that gives for PH1 and beyond rank three.
    - **(c)** Say what GRH, holding in such a setting, forces on the attached Boolean structure, and through it on
      Boolean counting, parity and satisfiability: the support map N → B and the reduction N → F₂.

    - **(d)** The first jet of the deformation L_t = e^{-tD}L gives every simple zero ρ the velocity ρ·L(ρ+1)/L′(ρ).
      Its sign off the line is a non-constant Boolean label on the zeros. See `OURS_BOOLEAN_LABEL_OF_ZEROS_20261121.md`:
      it gives an exact phase formula; our consult `OURS_CONSULT_ad855737_ZETA_LABELS.md` proves the exact criterion (right-mover iff W_n mod 2 lies in (0,1), W_n = S(γ_n) − arg ζ(3/2+iγ_n)/π) and that the corrected-Gram rule is its restatement |W_n| < 1/2 (mod 2), first failing at zero 871. Derive its asymptotic
      proportion, the correlations of its values, its CUE prediction, and its behaviour under higher jets, for ζ, ζ_K
      and Dirichlet L-functions. Also say what it gives the questions (a)-(c).

    - **(e)** What we found on (a)-(c) on 21 Nov is attached: `OURS_SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md`
      (sections 1-12), `OURS_CONSULT_a157422a_COUNTING_CONSTRUCTION.md` and `OURS_E4_RANK_FOUR_20261121.md`, with scripts.
      - (a) runs fibre by fibre with G(R)-coefficients. Its subtraction-free part is the effective cone K₀⁺, and the
        Boolean skeleton has weight 0 (consult af2a18f6, Q3).
      - Counting with the basepoint makes ζ the unit. The map c(q) = Σ_j a_j q^j ↦ Π_j ζ(s − j)^{a_j} is a ring
        isomorphism onto Euler products with the Witt product and unit ζ, and Z_{X₊} = Z_X·ζ. With the sign ε of
        Connes-Consani's F_{1²} globalized as χ₋₄, a sign-twisted count has zeta Π_j ζ(s − j)^{a_j⁺}·L(s − j, χ₋₄)^{a_j⁻},
        multiplicative over Z[1/2]. The supported zero e of G(Z) is the class 1 + ε: Spec Z[i], with zeta ζ_{Q(i)}.
      - At GCT rank three all 132 structure constants are such counts, every f lies in N[q + q⁻¹], and a
        categorification exists. There the nonstandard Riemann hypothesis is A, the GL₁ slice of the Grand Riemann
        Hypothesis, together with the existence of a dimension ring. A canonical basis that needs v = √q moves it to
        Hecke characters of CM fields (ERH); pieces that are not CM move it to GL₂ and beyond.
      Derive what follows from this for (c): for Boolean counting and parity through the supported zero 1 + ε and the
      support map N → B, and for the complexity theorems that use GRH (Koiran's HN ∈ AM and Bürgisser's transfer need
      Dedekind zeta functions, beyond A).

    Read the split-zero papers in full. Several of their statements are made for special rings and extend; record the
    general forms you prove.

11. **Working back from A on the zeta constructions.** RH and GRH for Dirichlet L-functions are theorems (A). Derive
    what they force on constructions that were made without assuming them. `OURS_TRANSLATION_SPLIT_ZERO_20261121.md`
    (sections 2, 4, 13, 14) states the starting points:
    - the completed Hurwitz family Λ_t = π^{-s/2}Γ(s/2)ζ(s,1+t): every simple zero moves off the line at first order
      by the anti-invariant part of the deformation, Re ρ' = Im Φ₋(ρ)/Z'(γ), Im ρ' = −Φ₊(ρ)/Z'(γ) (checked on 200
      zeros, `OURS_antiinvariant_drives_offline.py`); the user's defect preprint isolates that anti-invariant part;
    - the explicit formula for the velocities, Σ_ρ h(ρ)ρ' = (1/2πi)∮ h(s)·sζ(s+1)/ζ(s) ds: its main terms with the
      contour on Re s = 1/2, and what they give for the labels of item 10(d);
    - Λ = 0 (Rodgers-Tao with A): H_t has real simple zeros for t > 0 and nonreal zeros for t < 0; derive the law of
      the collisions at negative times (heights against times as t increases to 0), using the user's collision
      calculus in `OURS_RH_WORKBENCH_22_rh_counterexample_routes.tex`;
    - the user's RH workbench (the attached satellites): its Weil-form matrices, the Bost-Connes observables and the
      Navier-Stokes transport, read with Weil positivity, the Lee-Yang property of the Bost-Connes partition
      function and Λ = 0 now theorems;
    - Montgomery's pair-correlation theorem, which assumed RH: derive what it now gives the CUE comparisons of
      `OURS_split_zero_corpus` (papers 12-14);
    - total positivity: with A, the coefficients b_k of Ξ(z) = Σ(−1)^k b_k z^{2k} form a Pólya frequency sequence (every
      minor of the Toeplitz matrix (b_{j−i}) is nonnegative; Pólya, Edrei), equivalently the multiplicative central
      function σ ↦ Π_{cycles c}(−1)^{|c|−1} Z(2|c|)/Z(2)^{|c|} on S_∞ is positive definite, Z(s) = Σ_γ γ^{-s} the
      secondary zeta function of the zeros (Thoma); Λ = 0 says the heat flow H_t keeps this property exactly for
      t ≥ 0. Derive what follows in these terms (Lusztig's total positivity and canonical bases, Vershik-Kerov
      asymptotic representation theory, characters of U(∞) and the CUE).

    State every consequence of items 11 and 12 also as a theorem in the language of algebraic geometry and of GCT and
    representation theory: Weil positivity as the Hodge index inequality of Weil's proof for curves, Frobenius classes
    and reductions mod p, orbit closures and multiplicities, total positivity.
12. **Supported zeros and computation.** Sections 7-9 of the translation note: in G(F₂) the sum ⊕ is the pair (XOR,
    OR); a parity test passes exactly on the Boolean pair {τ, 0}; section 6 of the ETH paper removes the supported
    zeros; a G(R)-circuit computes a ring circuit together with its monotone shadow; for monotone functions, circuits
    without supported zeros are monotone circuits up to constants; so CLIQUE ∈ P/poly exactly when supported zeros give
    exponential savings for CLIQUE, and on slice functions they can be removed at polynomial cost (Berkowitz). Derive
    what follows, with E: what E says about the savings supported zeros give for counting, and what the isolation
    theorems (Valiant-Vazirani, Mulmuley-Vazirani-Vazirani, Hoza's NL = UL) say in these terms. For GCT, treat
    canonical-basis positivity (PH0 in GCT VI) as the absence of supported zeros in a canonical formula, PH1 as such a
    formula that also counts points of a polynomial-size polytope, and Bürgisser-Ikenmeyer-Panova as containment of
    the permanent's support in the determinant's (n ≥ m^{25}). On P-F57's cubic family the count is a near-supported
    zero of its pole expansion (terms of size about 2^{n⁴/24} cancelling to a small count): derive what that says. Our
    consult `OURS_CONSULT_a0805369_GCT_SUPPORT.md` found that isolation on a signed formula detects existence of terms,
    not the value (Kronecker g((1,1),(1,1),(1,1)) = 0), that a cheap uniform test family would give NP ⊆ RP, and that
    P-F30 with P-F23 is the Mulmuley-Vazirani-Vazirani argument run in reverse; build on it. Derive which positive
    formulas with hashing, or unique-extremal localizations on faces, decide positivity of plethysm or Kronecker
    coefficients, and what A and M add through Koiran's and Bürgisser's transfers.

The links to each of these are real. No consequence has to be a mere corollary to be worth deriving, so do not ask
whether a link holds: show how it works, prove what follows, and where a route meets an obstacle, locate it and take
the next one. Do not pick a target in advance: the catalogue decides where the work goes. Every consequence that bears on
P versus NP or VP versus VNP gets a paragraph saying exactly what it shows and what it leaves open, in either direction.

## What we already found (attached): use it, do not redo it

These are our results so far, background to build on, to correct where wrong, and to cite by file and id:
- `RETURN_CX_GRH_final_*/`, our complexity catalogue of 21 Nov, and its intake;
- `RETURN_GRH_NIGHT_checkpoint_07_*/`: the catalogue of the two GRH proofs, 362 rows in CONSEQUENCES.tsv. Do not repeat
  its rows; build on them;
- `RETURN_ALPOGE_GCT_checkpoint_09_*/`: P-F19, P-F31, P-F56, P-F57 and their chain;
- our intakes of ALPOGE_GCT, GCT_PLETH, GCT_KRON, CUE_GCT, GCT_NSRH and BR_PENCIL;
- our implications report of 21 Nov, whose sections 3.9, 3.10 and 10 cover these runs;
- the Masullo defect table;
- our counting construction and rank-three results of 21 Nov (the split-zero write-up, sections 5-12;
  the E4 file; the counting consult).

## The attached files

- `LIT_OpenAI_ETH_is_False`: E: OpenAI, The Exponential Time Hypothesis is False (25 Oct 2026), LaTeX
- `LIT_Mulmuley_GCT_VI_flip_via_positivity`: GCT VI (arXiv:0704.0229v4), LaTeX: the hypotheses PH1, SH, PH2, PH3
- `LIT_Mulmuley_GCT_V_Noether_normalization`: GCT V, LaTeX: Noether normalization, the GRH and border-hardness premises (our CX-K05, K06, E06)
- `ALPOGE_remark.pdf`: A: Alpöge's note (public)
- `OURS_ALPOGE_LEAN_MAP_20261120.md`: our map of Alpöge's Lean archive
- `OURS_MASULLO_DEFECTS_20261121.md`: our defect table for Masullo's draft (M)
- `OURS_IMPLICATIONS_REPORT_20261121.md`: our implications report of 21 Nov (sections 3.9, 3.10 and 10)
- `RETURN_CX_GRH_final_20261121T0005Z/`: our complexity catalogue (prompt 28): Koiran, GCT V, E (CX-K, CX-N, CX-E rows) (59 files: the run's paper, registers, scripts and certificates)
- `RETURN_GRH_NIGHT_checkpoint_07_20261121T0617Z/`: the catalogue of the two GRH proofs (prompt 42), CONSEQUENCES.tsv with 362 rows (207 files: the run's paper, registers, scripts and certificates)
- `RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/`: P-F19, P-F31, P-F56, P-F57 and their chain (prompt 23's run, final) (354 files: the run's paper, registers, scripts and certificates)
- `OURS_INTAKE_CX_GRH_20261121.md`: our intake, with its check events
- `OURS_INTAKE_GRH_NIGHT_20261121.md`: our intake, with its check events
- `OURS_INTAKE_GRH_NIGHT_20261121_part2.md`: our intake, with its check events
- `OURS_INTAKE_GRH_NIGHT_20261121_part3.md`: our intake, with its check events
- `OURS_INTAKE_ALPOGE_GCT_cp03_20261121.md`: our intake, with its check events
- `OURS_INTAKE_ALPOGE_GCT_20261121.md`: our intake, with its check events
- `OURS_INTAKE_ALPOGE_GCT_20261121_part2.md`: our intake, with its check events
- `OURS_INTAKE_ALPOGE_GCT_20261121_part3.md`: our intake, with its check events
- `OURS_INTAKE_ALPOGE_GCT_20261121_part4.md`: our intake, with its check events
- `OURS_INTAKE_GCT_PLETH_20261121_part4.md`: our intake, with its check events
- `OURS_INTAKE_GCT_KRON_20261121_part3.md`: our intake, with its check events
- `OURS_INTAKE_CUE_GCT_20261121_part4.md`: our intake, with its check events
- `OURS_INTAKE_GCT_NSRH_20261121_part4.md`: our intake, with its check events
- `OURS_INTAKE_BR_PENCIL_20261121_part2.md`: our intake, with its check events
- `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence/` (arXiv:1604.06431, LaTeX source): no occurrence obstructions
- `LIT_Ikenmeyer_Mulmuley_Walter_Kronecker_vanishing/` (arXiv:1507.02955, LaTeX source): Kronecker positivity NP-hard; holes
- `LIT_Fischer_Ikenmeyer_plethysm_complexity/` (arXiv:2002.00788, LaTeX source): plethysm positivity NP-hard at fixed inner degree
- `LIT_Briand_Orellana_Rosas_SH_counterexamples/` (arXiv:0810.3163, LaTeX source): counterexamples to strong SH for Kronecker coefficients
- `LIT_Kahle_Michalek_obstructions_plethysm_formulas/` (arXiv:1507.07131, LaTeX source): homogeneous PH1 fails (Theorem 5)
- `LIT_Kahle_Michalek_plethysm_lattice_points/` (arXiv:1408.5708, LaTeX source): plethysm quasi-polynomials
- `LIT_Hoza_2026_NL_eq_UL_ECCC_TR26-323.pdf`: Hoza, NL = UL (ECCC TR26-323, 2026): explicit isolation for layered digraphs (no LaTeX source exists)
- `LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker`: GCT IV (arXiv cs/0703110): nonstandard quantum group, Kronecker problem
- `LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm`: GCT VII (arXiv 0709.0749): nonstandard quantum group, plethysm problem
- `LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups`: GCT VIII (arXiv 0709.0751): canonical bases and the nonstandard Riemann hypothesis
- `PREVIOUS_PROMPT_24_GCT_NSRH.md`: our prompt 24 as sent: the nonstandard RH against purity by positivity
- `RETURN_GCT_NSRH_checkpoint_09_20261121T0545Z/`: GCT_NSRH final (prompt 24): the sign-only purity criterion for the nonstandard objects, F01-F69 (441 files: the run's paper, registers, scripts and certificates)
- `OURS_INTAKE_GCT_NSRH_cp03_20261121.md`: our intake, with its check events
- `OURS_INTAKE_GCT_NSRH_20261121.md`: our intake, with its check events
- `OURS_INTAKE_GCT_NSRH_20261121_part2.md`: our intake, with its check events
- `OURS_INTAKE_GCT_NSRH_20261121_part3.md`: our intake, with its check events
- `OURS_globalization_note_G_Z_March_2026.tex`: our note on the globalization semiring S(O_K): zeta_{S(O_K)} = zeta_K with a Boolean subsemiring {0, tau}
- `OURS_split_zero_corpus`: the split-zero (globalization) research corpus: G(R) = R with an external zero; the classical and separated zeta sheets; Boolean shadows; latest LaTeX of each paper with the theorem index
- `OURS_BOOLEAN_LABEL_OF_ZEROS_20261121.md`: the first jet of the split-zero deformation labels every simple zero: velocity rho*zeta(rho+1)/zetaprime(rho); the right-mover rule, 500/500
- `OURS_zero_motion_gram.py`: the computation behind the note
- `OURS_TRANSLATION_SPLIT_ZERO_20261121.md`: our translation of the split-zero programme into standard terms (dictionary; sections 2-14: velocity split, ETH support, supported zeros and circuits, the July thread, the shape, GRH backward)
- `OURS_antiinvariant_drives_offline.py`: check of the anti-invariant split of the zero velocities, 200 zeros
- `OURS_RH_WORKBENCH_22_rh_counterexample_routes.tex`: the user's RH workbench (Sep 2026): Bost-Connes observables, Weil-form matrices, de Bruijn-Newman heat and Burgers, collision calculus
- `OURS_RH_WORKBENCH_24_retained_weil_test_algebra.tex`: the user's RH workbench: the retained Weil test algebra
- `OURS_RH_WORKBENCH_29i_ns_actual_witness.tex`: the user's RH workbench: the Navier-Stokes transport into the zeta coordinate (preserves zero heights)
- `OURS_CONSULT_a0805369_GCT_SUPPORT.md`: our consult (Claude Opus 5.5 at effort high, 21 Nov): GCT read through supported and unsupported zeros; PH0/PH1; BIP; P-F57 as a near-supported zero; isolation limits
- `OURS_CONSULT_af2a18f6_GRH_BACKWARD.md`: our consult (Claude Opus 5.5 at effort high, 21 Nov): the GRH-conditional results now unconditional, A or M scope; Koiran and Bürgisser in AG terms; item 10(a)
- `OURS_CONSULT_a8d75352_NSRH_WEIL.md`: our consult (Claude Opus 5.5 at effort high, 21 Nov): item 10(b): no finite Weil object from the split-zero candidates; GCT VIII's signed form as effective fibres over a Boolean cube
- `OURS_CONSULT_ad855737_ZETA_LABELS.md`: our consult (Claude Opus 5.5 at effort high, 21 Nov): the exact label criterion, the velocity sum under RH, label statistics against random matrices, collisions with Lambda = 0
- `OURS_CONSULT_a157422a_FABLE_SHAPE.md`: our consult (Claude Fable 5.2 at effort max, 21 Nov): the shape as a totally positive point at the boundary of a positive part; RH as Weil positivity and as square-root cancellation of mu; Li-Toeplitz sections
- `OURS_consult_a157422a_checks.py`: checks of that consult: Li-Toeplitz sections, Jacobi-Trudi determinants, sedenion annihilators
- `OURS_CONSULT_a157422a_IMPLICATIONS.md`: our consult (Claude Fable 5.2 at effort max, 21 Nov): what the extracted statements imply: K0 of Spec G(R), Li coefficients as Hodge index, the S_inf character, GCT VIII cube, S6 cusp identity, ghosts
- `OURS_SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md`: our write-up: split zero in Connes-Consani's terms, counting with the basepoint (zeta as the unit), sections 5-12
- `OURS_E4_RANK_FOUR_20261121.md`: rank three and four of VIII's canonical basis: P-F-E3-01, realizations, the hexagon of labels, the q = -1 symmetry
- `OURS_E4_RANK_FOUR_20261121_CHECK_EVENTS.tsv`: check events of the E4 file
- `OURS_E4_scripts`: scripts and data: e3_constants.json, positivity_in_u.py, gram_signpoint.py, cell_c3_check.py, hexagon_labels.py
- `OURS_CONSULT_a157422a_COUNTING_CONSTRUCTION.md`: counting consult (Claude Fable 5.2 at effort max): ground ring Z[D], closed forms, dimension rings, the supported zero 1 + eps
- `OURS_counting_scripts`: the counting consult's scripts and the minimal cancelling-pair score of the dimension rings

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

The rule that governs everything below: push. Work on the main question first: the complete catalogue of what follows from the refutation of ETH and its variants (E), from the failure of GCT VI's positivity and saturation hypotheses and the earlier negations, and from GRH for Dirichlet L-functions (A) and for Hecke L-functions (M, conditional), alone and in combination, each consequence proved or located with its exact inputs and kept current in CONSEQUENCES.tsv through every checkpoint. Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `NEG_NIGHT_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `NEG_NIGHT_final.zip`, holding:
1. **The paper**, `NEG_NIGHT.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change, for P versus NP through geometric complexity theory and for
   Grothendieck's texts (cote and scan).

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
