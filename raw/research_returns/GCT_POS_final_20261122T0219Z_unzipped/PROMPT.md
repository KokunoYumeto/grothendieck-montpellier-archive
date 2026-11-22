**The attached files.** Besides this file there is one ZIP, `GCT_POS_the_positivity_hypotheses_of_geometric_complexity_th.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `52_GCT_POS_scripts.zip` is the folder `52_GCT_POS_scripts/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# GCT_POS: the positivity hypotheses of geometric complexity theory after the plethysm refutations — Kronecker coefficients, density, efficient formulas and nonstandard bases

This prompt continues three runs of 20-21 Nov 2026, all GPT-6 Astra (ChatGPT Pro mode); the runs report their effort
setting as not exposed. They are ALPOGE_GCT (our prompt 23), GCT_PLETH (our prompt 25) and GCT_NSRH (our prompt 24).
Their final returns (`RETURN_ALPOGE_GCT_*`, `RETURN_GCT_PLETH_*`, `RETURN_GCT_NSRH_*`) are attached. Our intakes of
them are attached too, parts 1-4 for each run with their check-event files. Build on them and cite them by finding id;
do not redo what they settled.

Throughout, write GCT VI for Mulmuley, *Geometric complexity theory VI: the flip via positivity* (arXiv:0704.0229v4,
attached as LaTeX). Write p(f) and s(f) for the positivity and saturation indices of a stretching quasipolynomial f
(GCT VI, Definitions 1.2.2 and 1.2.4, printed pp. 13-14). The hypotheses are numbered as in GCT VI:
- SH = Hypothesis 1.6.5: (a) polynomially bounded saturation index; (b) zero saturation index for almost all inputs;
- PH2 = Hypothesis 1.6.6: polynomially bounded positivity index;
- PH3 = Hypothesis 1.6.7: a positive rational form of polynomially bounded modular index, more specifically the
  minimal (canonical) form.

The parameter is h = dim G + ht(λ) + ht(π). The general-form versions are Hypotheses 3.3.1-3.3.4.

## Where it stands

**Plethysm: GCT VI's index hypotheses all fail as stated.** Each line gives the finding, what it proves, and the check
it received.
- **P-K1** (cited, Kahle-Michałek, Theorem 5): homogeneous PH1 (Hypothesis 1.6.4) fails on the ray
  φ(s) = p_{(4s),(3)}^{(7s,5s)}. Our intake recomputed φ(s) for s ≤ 24.
- **P-F1** (ALPOGE_GCT): a minimal two-dimensional shifted polytope repairs the ray. Proof check and computation.
- **P-F2:** every explicit positive Hilbert series is one shifted polytope count. Proof check.
- **P-F12 / PL-Q22:** Theorem 1.6.1(d) of GCT VI fails as printed on this ray. Proof check against the source.
- **PLE-F5 to PLE-F8:** the ray's multiplicity algebra is the D₅ Kleinian ring ℂ[U,V,Z]/(Z² − UV² − 4U⁴), with pure
  Tate cohomology. Proof checks; the identities were verified symbolically.
- **P-F11, P-F12:** PH3 ⇒ PH2, with the explicit bound p(f) < (d_λ+1)A + 128(d_λ+1)³A³, A the modular index. Proof
  check.
- **P-F19:** the canonical clause of PH3 fails for inner shape (3). The chain cubic
  F_n = x₁²x₂ + … + x_{n−1}²x_n + x_n³ has a stabilizer whose determinant character has order 2^{n−1}, so every
  homogeneous system of parameters (h.s.o.p.) of the cubic invariant ring T^{(n)} has a member of degree ≥ 2^{n−1},
  against h = O(n⁶). Proof check, independent re-derivation, computation for n ≤ 13.
- **P-F30:** maximal determinant order 2^{n−1} forces the chain support. Proof check for the case q > 0; exhaustive
  computation over all cubic supports for n = 3, 4.
- **P-F23:** at a primitive M-th root ζ, the leading coefficient of a graded Hilbert series is e_Y/det(1−g | N*_{Y/X}),
  under a unique, generically smooth, top-dimensional fixed component Y. Proof check.
- **P-F24, P-F26:** proof checks in part.
- **P-F27, P-F28:** carried at statement level by our intakes; the run has independent whole-proof readings.
- **P-F31:** H_n(t) has a simple pole at every primitive 2^{n−1}-th root of unity, so the existence clause of PH3 fails
  too. Proof check; matches Salmon's classical Hilbert series of cubic surfaces at n = 4.
- **P-F56, P-F57:** PH2 and SH(a) fail on this family: p(f_n) > 2^{cn} and s(f_n) ≥ 2^{cn} for every c < 1/4 and all
  large n, explicitly 2^{n/8} for n ≥ 2·10⁸⁰. The mechanism:
  - the dyadic wave W_n, the difference of constituents half a period apart, is a constant;
  - its selected conjugate pair dominates;
  - a single witness x then has 2W_n(x) > f_n(x), against the ambient dimension bound.

  Check: proof check of P-F57, and of P-F56 through its line 900. The exact residue formula (P-F56v) matches Salmon's
  n = 4 residue 0.125 + 0.30178i, phase included. The ratio Q_n = E_n/|Z_n| was computed exactly for n = 5..16; it is
  below 1/4 from n = 8 (0.094) and falls super-exponentially.
- **P-F14, P-F15:** the general-form Hypotheses 3.3.2(a), 3.3.3 and 3.3.4 fail as stated, because rank(x) omits the
  embedding weights. Proof check against the source.
- **P-F63** (statement level only): the broad Hypothesis 3.3.2(b) fails under an explicit finite input-coding
  convention.
- **P-F48** (statement level): the cubic families are exponentially sparse in both SH(b) populations, so SH(b) is
  untouched by them.
- **P-F42, P-F34:** the earlier average-polynomial route.

**Kronecker coefficients: only the canonical clause is done.**
- **P-F60** (statement level in our intakes): the chain tensor
  T_n = Σ c_i(e_i⊗e_i⊗e_{i+1} + permutations) + c_n e_n^{⊗3} in (ℂ^n)^{⊗3} has a closed SL_n³ orbit and full stabilizer
  {(aD_ζ, bD_ζ, cD_ζ)}, with χ(Stab) = μ_{2^{n−1}}. The ring R^{ten}_n = ℂ[(ℂ^n)^{⊗3}]^{SL_n³}, graded by degree/n, has
  Hilbert function the triple-rectangular Kronecker coefficient g((s^n),(s^n),(s^n)). Every h.s.o.p. has a member of
  degree ≥ 2^{n−1}, against the source rank n² + 5n.
- **P-F65** (statement level): a second fixed component, with its own stabilizer, smooth local curve and the same
  principal-embedding phase. The other fixed components were not classified.

**Positive formulas** (GCT_PLETH).
- **Outer degree three:** G-012.
- **Outer degree four:** T-037. Computation check, 60/60 coefficients.
- **Outer degree five:** G-036, every coefficient p_{μ,(n)}^λ, μ ⊢ 5, by at most 152 bounded polytopes in at most 11
  variables, with polynomial bit complexity. Computation check: the run's router against an independent
  character computation, 539/539. Support: G-031; its strict-chamber rule checked on 266 cases.
- **Stable width ≤ 6:** T-012 and T-013 (from Sarkar, arXiv:2610.07929v2, Theorem D). The B₅ and B₆ tables were
  recomputed exactly.
- **Varying outer degree m:**
  - G-037, stable hooks, one polytope with at most m² + 3m − 4 variables. Computation check, 790/790.
  - G-038, G-039, G-040: stable two-row tails (a, b), for b = 2, 3 and then every fixed b. Statement level. The bounds
    are f(b)(…)^{g(b)}, from Aschenbrenner's and Liang's Gröbner degree bounds.
  - T-062 to T-065: fixed-order hooks (statement level).
- **Hadamard-Howe (Foulkes-Howe) map h_{n,a}:**
  - R-031, the full rank law for a = 5 (known: Cheung-Ikenmeyer-Mkrtchyan, Ikenmeyer);
  - R-035, R-036: second row ≤ 2 and ≤ 3;
  - R-044, R-046, R-049: surjectivity ranges, the sharpest full surjectivity at n ≥ ⌊(D+t−q)/2⌋;
  - all statement level. The open gate (Q-MAP): the critical annihilator injects into N_r ⊗ Sym^{r²−1}, where N_r has
    first row ≥ r²+1 and second row ≥ r(r−1).

**Nonstandard algebras** (GCT_NSRH; the source is GCT IV, arXiv cs/0703110, attached).
- **F03, F04, F17, F24, F32:** purity from opposite path-output signs plus pointwise and dual bounds plus visibility.
- **F50:** the path sign can always be produced. So the only real input is an independent pointwise (stalk) weight
  bound.
- **F26, F42, F48, F51-F55:** no single finite Weil object carries the nonstandard traces.
- **F57, F58, F67:** strict effectivity fails from rank four.
- **F43, F45, F46, F50, F53, F56, F61, F66:** positive constructions at rank three.
- **INT-NSRH-4** (our intake's exact computation, `h4cone.py`, `h4cone_check.py`): the word
  ω = P₂P₃P₂P₃P₂P₃P₁P₂P₁P₂P₁ has six negative coordinates in the C⊗C basis of Ȟ₄. So the alternating-word basis that
  is C⊗C-positive at rank three (INT-NSRH-2) fails at rank four.
- Whether Ȟ₄ has any Z[v^±]-basis in the C⊗C cone is open. GCT IV, Remark 11.19, calls it uncertain.

**Inputs that are not theorems.** Findings marked "statement level" above are the runs' results, not yet checked by an
intake; treat them as conditional inputs and recheck what you use. No item of this prompt uses Masullo's draft; if
you use it, label every consequence as conditional on it. Alpöge's theorem (GRH for Dirichlet L-functions) enters
only through explicit prime bounds (ALPOGE_GCT P-F47); cite it as a theorem.

## The task

1. **Main question: PH2, SH(a) and the numerical PH3 for triple-rectangular Kronecker coefficients.** Let
   k_n(s) = g((s^n),(s^n),(s^n)), the Hilbert function of R^{ten}_n. Decide each of the following:
   - (i) Does H^{ten}_n(t) = Σ_s k_n(s)t^s have a pole at the primitive 2^{n−1}-th roots of unity, so that the
     existence clause of PH3 fails for Kronecker coefficients?
   - (ii) Are p(k_n) and s(k_n) bounded by a polynomial in n?

   The route the plethysm case took, carried over step by step:
   - (a) **Classify every fixed component** of μ_{2^{n−1}}, acting through the grading, on Spec R^{ten}_n. This is the
     analogue of P-F30 and P-F31, and it starts from P-F60 and P-F65. For every polystable tensor with a diagonal
     stabilizer element of two-power order whose determinant character has order 2^{n−1}, determine its support up to
     the S₃ × (S_n)³ symmetries. Prove the bound on the determinant order and classify the equality cases.
   - (b) **Decide whether the leading coefficients of the components cancel.** Compute each top-dimensional
     component's contribution by P-F23 (e_Y/det(1 − g | conormal)). Then decide whether their sum vanishes. If several
     components have the same phase, as P-F65 found, compute the sum exactly.
   - (c) **If the pole survives,** build the dyadic wave of P-F56 for k_n, its selected-pair amplitude, and the
     contraction of P-F57. Then prove or refute exponential lower bounds for p(k_n) and s(k_n). Use the ambient bound
     k_n(x) ≤ dim Sym^{nx}(ℂ^{n³}).
   - (d) **If the components cancel,** say exactly where (which components, which phases), and decide PH2 and SH(a)
     for k_n by another route. The average-polynomial test of P-F34 is one; a direct computation of the n = 3, 4
     Hilbert series is another.

     Give the n = 3 and n = 4 Hilbert series of R^{ten}_n exactly. For n = 3 the invariants of ℂ³⊗ℂ³⊗ℂ³ are
     classical; locate the source and check it. These calibrate every general claim.

   Rectangular Kronecker coefficients are the ones geometric complexity theory uses for permanent versus determinant
   (Bürgisser-Ikenmeyer-Panova; Ikenmeyer-Panova, both attached). Say what the answer means for the flip as GCT VI
   designed it, and for the multiplicity-obstruction programme after the no-occurrence theorem (ALPOGE_GCT P-F8).

2. **The standalone write-up of the plethysm refutation (P-F57 and its chain), with an explicit witness.** Write a
   self-contained paper, every step proved, of the theorem: for inner shape (3), PH3 (both clauses), PH2 and SH(a)
   fail. Its proof runs through P-F23, P-F24, P-F26, P-F27, P-F28, P-F30, P-F31, P-F56 and P-F57. Include the
   Theorem 1.6.1(d) erratum (P-F12) and the general-form failures (P-F14, P-F15) as companion sections. Give the GCT VI
   locators exactly: printed pp. 13-15, 24-25, 50-57 of arXiv:0704.0229v4.

   Make the threshold explicit and moderate. The proof's bound n ≥ 2·10⁸⁰ comes from crude estimates; our computation
   shows Q_n < 1/4 already from n = 8. What fails at small n is only the ambient upper bound for f_n(x). Find an
   explicit pair (n, x), with n as small as you can prove, such that 2W_n(x) > f_n(x), and prove the inequality:
   - W_n(x) from the exact product (P-F56v), which is computable;
   - f_n(x) from a sharper upper bound, such as a Molien-Weyl or Brion-Vergne bound, or an exact count.

   That witness gives p(f_n) > x and s(f_n) ≥ x by P-F56e'. Then give an explicit n₀ beyond which p(f_n) > 2^{n/8},
   with all constants.

3. **SH(b) for plethysm** (Hypothesis 1.6.5(b), the narrow density clause). Fix the population and the density reading
   exactly, as P-F48 does. Then prove SH(b) or refute it.
   - The converse question that the plethysm work opens: does a nonzero saturation index force a stable point of the
     stretching quotient whose stabilizer has a determinant character of order growing with the input?
   - If so, bound the density of such inputs, using P-F48's counting. If not, give the counterexample.
   - State the result also for the broad clause 3.3.2(b), against P-F63's coding convention.

4. **Polynomial-size positive formulas for two- and three-row tails in varying outer degree** (GCT_PLETH Q-EFFICIENT).
   GCT_PLETH's G-040 gives, for each fixed second part b, a positive formula polynomial for fixed b, with bound
   f(b)(m + binary lengths + 1)^{g(b)}.
   - Give a positive #P formula of size polynomial in m, b and the binary lengths for all stable two-row tails (a, b);
     then the same for three-row tails.
   - The gate is G-040's finite cokernel modules: support in degrees b−1 to 2b−2, at most b−2 low variables. A positive
     basis of them, uniform in b, removes the Gröbner bounds. Construct it.

   This is GCT VII's Problem 1.1 on infinite families with varying outer degree. State exactly where the result sits
   against the NP-hardness of plethysm positivity (Fischer-Ikenmeyer, fixed inner degree three).

5. **Outer degree six.** Give a fixed positive formula, polytope counts with polynomial bit complexity, for every
   p_{μ,(n)}^λ with μ ⊢ 6, as G-036 did for μ ⊢ 5. Use GCT_PLETH's interpolation reading:
   - the balanced weight space (Gay's theorem, T-002) is H⁰ of a twisted power of the ideal sheaf of the six simplex
     points of P(h₆) = P⁴ (G-015, G-016, G-021, T-053);
   - the Cox ring of the blow-up and its degeneration supply the positivity.

   Decide support as G-031 did. Deliver the evaluator with its certificates, and check it against an independent
   character computation on every λ with n ≤ 3.

6. **The Hadamard-Howe map: Q-MAP for r = 3 and r = 4** (a = r + 1). Compute the critical annihilator in
   N_r ⊗ Sym^{r²−1} exactly, starting from R-047 to R-049 and R-032. Determine the rank of h_{n,a} on every isotypic
   component of the remaining band, and state the resulting full rank law for a = 4 and a = 5 in every inner degree.
   Compare with Foulkes' conjecture for (a, n): name the first component, if any, where the rank falls below the
   target multiplicity inside Sra's window.

7. **The Ȟ₄ positivity question** (GCT_NSRH, gate 2; GCT IV, Remark 11.19). Decide whether the nonstandard Hecke
   algebra Ȟ₄ has a Z[v^±]-basis inside the C⊗C cone, or in IV's signed or factored form.
   - Run an exact lattice or linear-programming search over bounded-degree combinations of P-words. Start from
     INT-NSRH-1 (Θ², from IV Prop. 11.6(iii)), INT-NSRH-2 and INT-NSRH-4, using the attached `h4cone.py` and
     `h4cone_check.py`.
   - Prove the answer for every degree, not only the searched range.
   - Explain why the negative coordinates sit at the extreme degrees, in F57, INT-NSRH-4 and F67 alike.

8. **The stalk gate for the rank-three algebra** (GCT_NSRH, gate 1). For the actual rank-three algebra (F19, F21, F44,
   F46), construct a constructible ℓ-adic sheaf on an affine space over F_q with these properties:
   - its stalks are pure of a known weight, checkable pointwise and independently of its cohomology;
   - its compact cohomology carries the coefficient objects with the actual P₁, P₂ action.

   F03 or F24 then gives purity, and F50 supplies the sign, so this is the whole remaining step. Decide it: construct
   the sheaf, or prove that no such sheaf exists, and say which hypothesis fails.

9. **Rank three in the counting form, and what rank four has to show.** Our results of 21 Nov are attached:
   `OURS_SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md` (sections 5-12), `OURS_E4_RANK_FOUR_20261121.md` (sections 6-7)
   and `OURS_CONSULT_a157422a_COUNTING_CONSTRUCTION.md`, with scripts in `OURS_E4_scripts/` and `OURS_counting_scripts/`.
   They concern VIII's E^opp(3) with the sign of b₂ that VIII's own figure requires.
   - **Ground ring.** At every rank the Q(D)-span of the P-words is a Q(D)-form of Ȟ_r, D = q + 2 + q⁻¹. In every basis
     of Q(D)-combinations of P-words each structure constant lies in Q(D): a is even, and f is bar-invariant of Tate type
     with even weights (counting consult, Theorem 1).
   - **Positivity at rank three, in a sharper form.** All 132 constants are in closed form (Theorem 2). Every f lies in
     N[u], u = q + q⁻¹ (`positivity_in_u.py`). Here u is the normalized count |P¹(F_{q²})|/q of the Weil restriction
     R = Res_{F_{q²}/F_q} P¹, so every rank-three constant is ±(v − v⁻¹)^a times an N-combination of products of R's.
   - **The unimodality failures** P-F-E3-01 are [3]_q·u², with q-coefficients (1, 1, 3, 2, 3, 1, 1). The middle
     cohomology of R is two classes that Frobenius swaps, of trace 0, so the traces dip in the middle while the graded
     dimensions (1, 5, 11, 14, 11, 5, 1) are unimodal.
   - **Split and inert.** On the two-dimensional representations P₁P₂P₁ = λ_i·P₁ with λ₁ = D and λ₂ = (D − 2)², and
     λ₂(v) = λ₁(v²): the second cell is the first at Frobenius squared, as at an inert prime.
   - **Composition.** A categorification exists: a dimension ring, that is nonnegative constants d ≥ |c| with
     d ≡ c mod 2 forming an associative ring on the same basis, with a choice in which all 132 dimension polynomials are
     unimodal (Theorems 5, 7, 7′). The constant-by-constant realizations of E4 section 7 do not compose (Proposition 5),
     and every composing realization carries cancelling pairs in the bottom cell (Proposition 6). Counting those
     pairs selects: among the 14,975 dimension rings of the consult's search window, the fewest pairs (7,952) occur in
     exactly one ring, the consult's Theorem 7 ring, and among the unimodal ones in exactly one, its Theorem 7′ ring
     (`dimension_ring_minimal_pairs.py`). Whether this minimum holds outside the window is part of (d).
   - **The sign point.** At q = −1, that is D = 0, the trace form on the χ² cell is monomial, and the cyclic rotation of
     the three slots is an exact symmetry of order 3 of the cell's constants. With the Dynkin swap it generates C₆, with
     the transpose D₃ (`gram_signpoint.py`, `cell_c3_check.py`). At q = −1 the split cell's trace form is identically
     zero (λ₁ = 0 = θ(P_i)); at q = 1 and q = ω the two sheets coincide (λ₁ = λ₂) and the form has rank one; at q = i
     (λ₂ = 0) no symmetry appears (`cell_c3_both_sheets.py`). q = −1 is where the Hecke algebra's trivial and sign
     characters coincide (T_s has eigenvalues v and −v⁻¹). The six failures and the C₃ both live on the inert sheet.
   - Purity is not the gate. The global zetas of these realizations are products of ζ(s − j) and L(s − j, χ₋₄), pure
     by A. The content is effectivity and composition (consult a8d75352, finding Q2-d).

   Do all of the following:
   - (a) Construct VIII's E(4) from GCT VII's nonstandard Gelfand-Tsetlin basis, with its scalings and its label order,
     and compute every structure constant in VIII's signed form.
   - (b) Decide whether E(4) consists of Q(D)-combinations of P-words. If it does not, determine the field its
     constants need: Q(D)(v) (odd weights, realized by Gauss and Jacobi sums, that is Hecke characters of CM fields),
     or a non-abelian extension.
   - (c) Decide whether every rank-four f lies in N[q + q⁻¹], and identify the objects whose Frobenius traces the
     constants are: products of projective spaces, Weil restrictions from F_{q^k}, tori, or pieces that are not Tate.
   - (d) Decide whether a dimension ring exists for (Ȟ₄, E(4)). Give a canonical dimension ring at ranks three and four
     from the Hecke category of S_r × S_r with the involutions σ⊗σ (v ↦ −v⁻¹, which Koszul duality induces on
     Grothendieck groups) and β⊗β (v ↦ −v), using P_s = C′_s⊗C′_s + C_s⊗C_s; or prove that the category gives none
     and state what selects one.
   - (e) Decide whether the q = −1 symmetry extends from the χ² cell to the whole rank-three table, and whether rank
     four has the same structure at D = 0.

10. **Literature, before anything is called new.** For each finding of this run, say whether it is known. Search all of
   the following, and every further source they lead to, and cite each with its exact locator:
   - GCT VI, VII and VIII and Mulmuley's later statements of the positivity hypotheses;
   - Kahle-Michałek, *Obstructions to combinatorial formulas for plethysm*;
   - Briand-Orellana-Rosas on reduced Kronecker coefficients and SH;
   - Ikenmeyer-Mulmuley-Walter, *On vanishing of Kronecker coefficients*;
   - Fischer-Ikenmeyer on the complexity of plethysm coefficients;
   - Pak-Panova-Swanson (arXiv:2511.02312);
   - Sarkar (arXiv:2610.07929);
   - Cheung-Ikenmeyer-Mkrtchyan (arXiv:1509.03944) and Ikenmeyer (arXiv:1509.04957);
   - the formulas for h₄[h_n] and h₅[h_n];
   - hook and two-row plethysm formulas with varying outer degree (Langley-Remmel, Paget-Wildon);
   - the classical invariant theory of ternary trilinear forms (n = 3 in item 1).

   Locate and read the sources that are not attached; record each locator you checked. A result someone has
   published is cited, not claimed.

11. **In the project's terms.** State every main result also in Grothendieck's frameworks:
   - the stretching rings as coordinate rings of GIT quotients, i.e. coarse moduli of cubics and of trilinear forms;
   - the poles as fixed-point terms of Lefschetz-Riemann-Roch (SGA 6, Exp. VII);
   - the dyadic wave as the character of μ_M on a residual gerbe;
   - the positive formulas as H⁰ of twisted ideal sheaves, and as identities in the λ-ring K₀ (SGA 6, Exp. V), with
     the cote-133 corrections of our GCT_PLETH intakes (A-001 to A-023) where they apply.

    Cite our ids for every input (run and finding id).

The links between these questions and the earlier results are real. Where a route meets an obstacle, locate it exactly
and take the next route; an obstacle is never an end point.

## The attached files

- `RETURN_ALPOGE_GCT_*/`, `RETURN_GCT_PLETH_*/`, `RETURN_GCT_NSRH_*/`: the final returns (papers, registers, check
  events, the runs' scripts and evaluators).
- Our intakes of the three runs, all parts, with their check events.
- `52_GCT_POS_scripts/`: our independent check scripts.
  - `pf57.py`: the residue product, the Salmon comparison and Q_n.
  - `pf30.py`: the exhaustive support check.
  - `pf19.py`, `q4.py`, `km.py`.
  - `w5.py`, `w6.py`: the exterior-cube tables.
  - `out5.py`, `g036.py`, `g037.py`: the independent plethysm computations and the evaluator comparisons.
  - `h4cone.py`, `h4cone_check.py`, `nsrh_f57.py`: from the GCT_NSRH intake.
- The predecessor prompts 23 and 24 with their attachments: GCT IV, V, VI, VII and VIII; Landsberg's survey;
  Bürgisser-Ikenmeyer-Panova; Ikenmeyer-Panova; Borger.
- LaTeX sources: Sarkar (arXiv:2610.07929), Pak-Panova-Swanson (arXiv:2511.02312), Cheung-Ikenmeyer-Mkrtchyan
  (arXiv:1509.03944), Ikenmeyer (arXiv:1509.04957).

## The attached files

- `RETURN_ALPOGE_GCT_checkpoint_09_20261121T0547Z/`: final return (checkpoint 09): P-F1..P-F75, the PH refutation chain, P-F60 Kronecker (354 files: the run's paper, registers, scripts and certificates)
- `RETURN_GCT_PLETH_checkpoint_09_20261121T0546Z/`: final return (checkpoint 09): positive formulas, evaluators, canonical-map ranks, archive rows (1021 files: the run's paper, registers, scripts and certificates)
- `RETURN_GCT_NSRH_checkpoint_09_20261121T0545Z/`: final return (checkpoint 09): F01-F69, nonstandard algebras, stalk gate (441 files: the run's paper, registers, scripts and certificates)
- `INTAKE_ALPOGE_GCT_20261121.md`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_20261121_CHECK_EVENTS.tsv`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_20261121_part2.md`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_20261121_part2_CHECK_EVENTS.tsv`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_20261121_part3.md`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_20261121_part3_CHECK_EVENTS.tsv`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_20261121_part4.md`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_20261121_part4_CHECK_EVENTS.tsv`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_cp03_20261121.md`: our checks of ALPOGE_GCT
- `INTAKE_ALPOGE_GCT_cp03_20261121_CHECK_EVENTS.tsv`: our checks of ALPOGE_GCT
- `INTAKE_GCT_PLETH_20261121.md`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_20261121_CHECK_EVENTS.tsv`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_20261121_part2.md`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_20261121_part2_CHECK_EVENTS.tsv`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_20261121_part3.md`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_20261121_part3_CHECK_EVENTS.tsv`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_20261121_part4.md`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_20261121_part4_CHECK_EVENTS.tsv`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_cp03_20261121.md`: our checks of GCT_PLETH
- `INTAKE_GCT_PLETH_cp03_20261121_CHECK_EVENTS.tsv`: our checks of GCT_PLETH
- `INTAKE_GCT_NSRH_20261121.md`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_20261121_CHECK_EVENTS.tsv`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_20261121_part2.md`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_20261121_part2_CHECK_EVENTS.tsv`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_20261121_part3.md`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_20261121_part3_CHECK_EVENTS.tsv`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_20261121_part4.md`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_20261121_part4_CHECK_EVENTS.tsv`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_cp03_20261121.md`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `INTAKE_GCT_NSRH_cp03_20261121_CHECK_EVENTS.tsv`: our checks of GCT_NSRH (INT-NSRH-1..4)
- `PREVIOUS_PROMPT_23.md` and its attachments: GCT V, VI (LaTeX), Landsberg survey, Burgisser-Ikenmeyer-Panova, Ikenmeyer-Panova, Borger
- `PREVIOUS_PROMPT_24.md` and its attachments: GCT IV, VII, VIII (LaTeX): the nonstandard algebras for items 7-8
- `LIT_Sarkar_stability_of_plethysm_coefficients/` (arXiv:2610.07929, LaTeX source): Theorem D and the reduction used by T-012/T-013 and R-046
- `LIT_Pak_Panova_Swanson_plethysm_Kronecker/` (arXiv:2511.02312, LaTeX source): positive formulas in the two-row range; literature check
- `LIT_Cheung_Ikenmeyer_Mkrtchyan_Foulkes_5/` (arXiv:1509.03944, LaTeX source): Foulkes a=5, the h_{5,5} kernel (R-031); Q-MAP
- `LIT_Ikenmeyer_McKay_propagation/` (arXiv:1509.04957, LaTeX source): propagation theorem for the Hadamard-Howe map (R-031); Q-MAP
- `52_GCT_POS_scripts/g036.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/g037.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/h4cone.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/h4cone_check.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/km.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/nsrh_f57.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/out5.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/pf19.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/pf30.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/pf57.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/q4.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/w5.py`: our independent check script (listed in the core, attached files)
- `52_GCT_POS_scripts/w6.py`: our independent check script (listed in the core, attached files)
- `LIT_Briand_Orellana_Rosas_SH_counterexamples/` (arXiv:0810.3163, LaTeX source): counterexamples to the strong saturation hypothesis SH for Kronecker coefficients (2009): what is already refuted on the Kronecker side
- `LIT_Kahle_Michalek_plethysm_lattice_points/` (arXiv:1408.5708, LaTeX source): the plethysm quasi-polynomials and the Kahle-Michalek ray of H02
- `LIT_Ikenmeyer_Mulmuley_Walter_Kronecker_vanishing/` (arXiv:1507.02955, LaTeX source): NP-hardness of deciding positivity of Kronecker coefficients
- `LIT_Fischer_Ikenmeyer_plethysm_complexity/` (arXiv:2002.00788, LaTeX source): #P-hardness of plethysm coefficients and NP-hardness of their positivity
- `LIT_Kahle_Michalek_obstructions_plethysm_formulas/` (arXiv:1507.07131, LaTeX source): Kahle-Michalek Theorem 5 (P-K1: homogeneous PH1 fails on the ray); the base of H02
- `OURS_SPLIT_ZERO_IN_CONNES_CONSANI_TERMS_20261121.md`: our write-up: split zero in Connes-Consani's terms, counting with the basepoint (zeta as the unit), sections 5-12
- `OURS_E4_RANK_FOUR_20261121.md`: rank three and four of VIII's canonical basis: P-F-E3-01, realizations, the hexagon of labels, the q = -1 symmetry
- `OURS_E4_RANK_FOUR_20261121_CHECK_EVENTS.tsv`: check events of the E4 file
- `OURS_E4_scripts`: scripts and data: e3_constants.json, positivity_in_u.py, gram_signpoint.py, cell_c3_check.py, hexagon_labels.py
- `OURS_CONSULT_a157422a_COUNTING_CONSTRUCTION.md`: counting consult (Claude Fable 5.2 at effort max): ground ring Z[D], closed forms, dimension rings, the supported zero 1 + eps
- `OURS_counting_scripts`: the counting consult's scripts and the minimal cancelling-pair score of the dimension rings
- `OURS_CONSULT_a8d75352_NSRH_WEIL.md`: consult: no finite Weil object (F42); VIII's signed form as a Boolean Moebius sum of effective fibres; purity is not the gate

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

The rule that governs everything below: push. Work on the main question first: Do PH2, SH(a) and the numerical PH3 of GCT VI hold for the triple-rectangular Kronecker coefficients g((s^n),(s^n),(s^n)), decided by classifying the 2^{n−1}-fixed components of the SL_n³-invariant ring of (ℂ^n)^{⊗3} and computing their combined pole and dyadic wave? Give it most of the time.
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
environment, once every 45 minutes of work, each under a new name, `GCT_POS_checkpoint_<NN>.zip` with `NN` counting up.
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

One final ZIP, `GCT_POS_final.zip`, holding:
1. **The paper**, `GCT_POS.tex`, in LaTeX:
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
