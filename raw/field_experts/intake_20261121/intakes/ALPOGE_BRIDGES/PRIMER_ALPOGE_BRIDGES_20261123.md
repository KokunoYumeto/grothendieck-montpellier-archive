# Primer: ALPOGE_BRIDGES (prompt 22), Alpöge's RH and GRH bridged into Grothendieck's programme

Written 23 Nov 2026 by Claude Opus 5.5 at effort high (agent a25c2acbb3a6f11f7). It is a recall of the run and of our
intakes; nothing new.

**The run and its final.** GPT-6 Astra (ChatGPT Pro mode). The final return is checkpoint 09 (21 Nov 05:46 UTC):
`research_returns\ALPOGE_BRIDGES_checkpoint_09_20261121T0546Z_unzipped`.

**Our intakes.** Of checkpoints 01, 03, 05, 06 and 09, by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), in
`intakes/ALPOGE_BRIDGES/` (INTAKE_…_20261121.md, _cp03, _part2, _part3, _part4).

**Inputs.**
- A: Alpöge's theorem.
- M: GRH for the Hecke L-functions concerned. This was Masullo's claim, now known not to be proved.
- Cited 2026 preprints (CC-TATE01-03), as outside inputs, not checked by us:
  - van Hoften-Sempliner, Hexagon 2610.00259v2, Theorem I;
  - Milne, Hexagon 2611.00244v1;
  - Madapusi et al., Hexagon 2610.00226v1.

## 1. Bridges from A (checkpoint 01)
- **BR-AT-01**, A, confirmed: L(⊕(χ ⊗ Q(n))^m, s) = ∏ L(χ, s+n)^m. Its nontrivial zeros lie on Re s = 1/2 − n, and none
  is cancelled by poles. For a mixed object the good-prime L-function equals that of gr^W.
  - Use: RH for all Artin-Tate motives with abelian Artin part follows from A.
- **BR-TR-01**, A, confirmed: F(w) = Ξ(√w)/Ξ(0) = det(I − wB) with B = diag(t_j^{−2}) trace class. RH ⇔ B ≥ 0 for this
  normal realization.
  - Mechanism: Σ|t_j|^{−2} < ∞, and order ≤ 1/2 gives the genus-zero product.
  - BR-TR-02: under RH the Hankel matrices of the moments m_r = Σ b_j^{r+1} are positive definite.
- **Counterexamples to over-readings, all confirmed:**
  - BR-WM-01: a Frobenius determinant does not determine monodromy purity.
  - BR-ANA-01: P¹ ∖ {0, 1, ∞, 2} and P¹ ∖ {0, 1, ∞, 3} are not isomorphic but have the same ℓ-adic cohomology and the
    same zeta at all p ∉ {2, 3}.
  - BR-MIX-01: the Kummer motive K(2) is not Q(0) ⊕ Q(1).
- **Scope rows:**
  - CC-C01: Lagarias-Odlyzko 1977, Theorem 1.1, for L/K holds under A when L/Q is abelian.
  - CC-F02: an effective Siegel bound under A.
  - CC-F03: over Q(√−23) the class character of x³ − x − 1 induces an irreducible S₃ representation, so it is beyond A.
  - CC-F03b: if H_K/Q is abelian, the class-character L-functions are Dirichlet products.
- **CC-F01, F01b** (statement level): Borger Λ-schemes have rational ℓ-adic cohomology that is a sum of Tate-twisted
  finite abelian characters, so A gives their RH. Our first gloss of F01b was wrong; the base is Spec Z[1/p] (corrected
  after the ZETA_TWO intake, §5.2).
- **F-SM-01/02, F-SM-13** (statement level): a full zero trace equal to its narrow restrictions forces zeros onto the
  line. The numerical statement of Masullo's Theorem 12.5.1.1 over Q follows from A, which says nothing about his
  operator realization.

## 2. Masullo's draft: one defect located
**F-SM-19**, confirmed against the PDF, p. 495: the printed orbital indentation (11.3.2.2) is identically zero, so the
literal Theorem 11.3.2.1 fails. Test: F = Q, S = {∞}, h ∈ C_c^∞((3/2, 5/2)) with h(2) = 1; the right side is log 2 and
the left side 0. GRH_NIGHT found the same independently (MT-M36). The open step R-MAS-KERNEL (§§12.3-12.4) is the same
gate as GRH_NIGHT's Q-MAS-GEOMETRIC-NARROW. MAS_ARTIN later showed it equivalent to RH in the corrected model.

## 3. Grothendieck's archive
**Cote 123, the letter to Kostant.**
- **BR-12302**, confirmed by hand and by sympy. Grothendieck predicted that the tangent rank of the adjoint quotient at
  an orbit of dimension dim G − r − 2 is r − 1 when all roots have the same length, and strictly smaller otherwise. The
  "strictly smaller" part is false.
  - Instance: in sp₄, N = [[0, I], [0, 0]] has centralizer dimension 4, so orbit dimension 6. dc₂|_N(Y) = −Tr C and
    dc₄|_N = 0 since rank N = 2, so rank dχ_N = 1 = r − 1. The same holds for U = I + N in the group.
  - **CC-RK04** (part 4): this is Richardson 1987, §5 and Lemma 5.1, p. 234 (after Slodowy). For every simple 𝔤 there
    is exactly one nilpotent orbit of dimension N − r − 2, and rank dχ = r − 1 there. A known theorem: a companion
    note, not a post.
- **CC-APG04** (part 2), existence direction confirmed: an Out(G)-invariant class of apposition quadruples ("a
  distinguished class", physical p. 22) exists iff the type is not A_{2m}.
  - Mechanism: outside A_{2m} the Γ-orbits of simple roots are pairwise orthogonal. n = ∏_O φ_O(s) lifts a Coxeter
    element and is Γ-fixed. T₀ = Z_G(n)°, and a Γ-stable Borel comes from a Γ-fixed generic cocharacter.
  - The converse for A_{2m} rests on CC-AP04-05's normal form, which we did not open. Given it, an affine map reversing
    an ordering is impossible for odd n.

**Cote 136, the divided-power de Rham conjectures (SA08 C.3).**
- **AQ-136-STRICT** (part 2), confirmed for the strict reading: Grothendieck's (b), that two maps C ⇉ C′ are equalized
  by some admissible C″ → C (physical p. 121), is false over every nonzero ring, Z included.
  - Counterexample: j₀, j₁ : B ⇉ D = B ⋉ M with j₁ = (id, δ), δ the universal relative PD derivation. Here ker δ = S,
    and D is admissible.
  - An equalizer would split S → E, making k·T^{[w]} a constant summand of every row, against eventual acyclicity.
  - The sheet writes «'égalise'» in quotation marks, so the homotopy reading stays open.
- **AQ-136-SEMILOCAL** (part 3), step 1 confirmed by the arithmetic fracture sequence: over rings with only finitely
  many non-unit primes, the localized groupoid is terminal.
- **AQ-136-COSPAN, SEMILOCAL-SOURCES, CONNECTED-SOURCES** (part 4, statement level): a strict common source for finite
  families over such rings; over any ring, (a) is equivalent to connectedness of the category.

**Cote 134-8 (Dérivateurs).** F-SM-32 proves the linear statement for AB4 categories with enough projectives. F-SM44
reduces the compatibility gate to surjectivity in degrees ≥ 2; injectivity is proved in all degrees. Statement level.

**Cote 15 (motives over F_p, abelian sector)**, statement level, resting on Vial 2013 (Theorem 4.2, Corollaries 4.4,
4.8), Kahn-Sujatha and the CC-TATE preprints:
- finite descent profiles (CC-AG12-17);
- forward cross-cycles by Chow correspondences for low-degree Chow-generation classes (CC-XC16-23);
- BR-14-SEP: cote 14 closed for smooth connected separated parameters.

**BR-15-CLASSBOUND** (part 4): Thakur 2020, arXiv:2001.00210v1, Proposition 2.9, p. 6, is refuted.
- Counterexample: a simple threefold over F_{2⁹} with Frobenius polynomial (T² − 24T + 512)³ and
  K = Q(√−23), h_K = 3, has no isogenous model over F₈.
- Checked: γ = 12 − 4s has norm 512 and trace 24; (η) = 𝔭³ with N(η) = 8; no element of norm 2.
- The Honda-Tate index (CC-AG14) is statement level.

## 4. Open rows at the final, and where the results went
**Open:**
- Cote 136: connectedness, hence (a) and terminality, over Z; and the homotopy reading of «'égalise'».
- Cote 134-8: higher surjectivity in degrees ≥ 2.
- Cote 15: the general forward-cycle gate, which amounts to full Tate.
- R-MAS-KERNEL, now known to be equivalent to RH.
- Cote 18 (non-CM periods) and R-GTHAT.

**Where the results went:**
- Core 50 (ARCH_ALG: cotes 136, 134-8, 15, 123), `TO_SEND\PRO\_staging_20261121\cores\CORE_50_ARCH_ALG.md`.
- The Masullo defect table.
- The Hexagon register: H08 (BR-12302) became a companion note, since it is Richardson's lemma.
- MAS_ARTIN (the R-MAS-KERNEL gate).
- The bridges records in `reports_20261120\alpoge_rh\bridges\`.
