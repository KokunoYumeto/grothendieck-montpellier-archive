# Primer: the mathematics of POLISH_CRISTAUX: thread A's final and thread B's checkpoint 22 (updated 24 Nov 2026)

This primer is for the main session to read after a compaction. It was written by Claude Opus 5.5 at effort max (agent
a512cf71295c14ccb) from three intakes in this folder:
- `INTAKE_POLISH_CRISTAUX_20261123_cp12.md`;
- `INTAKE_POLISH_CRISTAUX_20261123_cp18.md`;
- `INTAKE_POLISH_CRISTAUX_20261123_final.md`;
- `INTAKE_POLISH_CRISTAUX_20261124_threadB_cp22.md`.

Earlier versions are kept in `integration_backups/20261123/POLISH_CRISTAUX/`: `PRIMER_POLISH_CRISTAUX_20261123_before_final.md`
(the cp18 primer) and `PRIMER_POLISH_CRISTAUX_20261123_before_threadB_cp22.md`.

The run is GPT-6 Astra (ChatGPT Pro mode), which does not expose its effort setting. It polishes RESEARCH_SA15
(Grothendieck's manuscripts on crystals, cotes 5-9 and 100). The only check labels used below are those recorded in the
three intakes' event tables.

**Two threads.** The run split at checkpoint 13 and never rejoined.
- **Thread 92** is the original prompt. Its final, sealed 18:48 UTC, is
  `research_returns/POLISH_CRISTAUX_final_20261123T1848Z_unzipped/workbench/papers/paperN/`: 18 papers, 461 pages.
- **Thread 92b** is the continuation. Its newest filed return is
  `research_returns/POLISH_CRISTAUX_checkpoint_22_20261123T2145Z_unzipped/workbench/papers/paperN/`: 21 papers, 508
  pages. That return was still active at cp22, with movement at review 12 (19:58 UTC), so later checkpoints may exist.
- The final lacks the 92b results, and the merge is open. Papers are numbered as in the final unless marked "92b".

## 1. Paper 1: integral crystalline weak Lefschetz fails (cp12 intake: targeted check of every step)

- **Statement.** There are smooth projective X in characteristic p, with a smooth ample divisor Y (very ample, in a
  fixed embedding), such that restriction H^i_cris(X/W) -> H^i_cris(Y/W) is not injective, or not saturated, in low
  degrees. Explicitly:
  - for p = 2, a surface from y^2 + y = x^15 (genus 7) and a product threefold, with exact degree thresholds;
  - every prime p (thm:all-primes);
  - an iterated Tango threefold, non-injective exactly in degrees 1 and 2.
- **Mechanism (cp12 intake, section 1.1).**
  - Raynaud-Mukai (Tango) constructions give ample L with H^1(X, L^{-r}) nonzero for small r.
  - The product criterion computes the kernel of restriction through K^j = Omega^j_Z(log Y)(-Y). It uses Künneth
    vanishings, the injectivity of d_1 on H^1(K^1) through the composite with restriction, and a Tor argument for
    Q[p] = 0.
  - Explicit counts make the defect nonzero: the pole semigroup <2, 15>, h^0(L^9) = 556, h^0(Omega_S) <= 35 = B_2, and
    m = 591 * 9^556 + 2.
  - In the product case injectivity holds for every d >= 1, and saturation holds iff d >= 2.
  - Positive range: thm:regularity, a form of BMS Lemma 2.12.
- **Open.** A forward literature search, and a different-model re-proof of the first-lattice lemma.

## 2. Paper 2: how much p-power torsion recovers the special inertia character (SA15-B chain)

- **The index.** nu_min(p, e, 2) is the least nu >= 0 such that, among the allowed height-two groups over complete
  fields of absolute index e with mu_p in K, M[p^(nu+1)] determines the special (prime-to-p) inertia character.
  - So nu = 2 refers to p^3-torsion (final `paper2/introduction.tex` line 14).
  - "Allowed" means filtered by Barsotti-Tate groups whose graded pieces are potentially good (sheets 10-11).
  - The cp18 primer stated this definition off by one; the values were right.
- **Prime-to-p index** (thm:complete-prime-index; cp12, top level checked). For p >= 5, (p-1) | e and p not dividing e:
  nu_min = ceil((1 + log_p e)/2). For example, nu_min = 2 iff p < e < p^3. Mechanism:
  - the Newton polygon of [p] on the group, with values A = (p+1)e - z and B = z/p;
  - central p^2 rigidity, with lower ramification break b = (p^2-1)A;
  - recovery by prime Hasse invariants;
  - lower bounds from the mixed constructions (not read).
- **Wild range, final (thread 92)**, with e = k p^r (p-1). Checks: statement level; this task's computations agree with
  92b on 1,595 cases.
  - thm:wild-bands-exact: for 2 <= k <= (p^2-1)/2, nu_min = r + 2 if p does not divide k or k = p, and r + 3 if p | k,
    k >= 2p. Hence nu_min(p, p^s(p-1), 2) = s + 1, and nu_min(p, kp(p-1), 2) = 3 for 2 <= k <= 2p - 1.
  - thm:mixed-all-indices: a whole potentially supersingular group and a two-step potentially good filtered group with
    isomorphic p^n-torsion and different characters exist over some field of exact index e iff e > p^(2n-3-v), where
    v = v_p(e).
  - thm:all-index-upper: e_K <= p^(n-1) forces recovery by p^n-torsion; equivalently nu_min <= ceil(log_p e).
  - thm:one-slope-all-indices: if both good models have one first-level slope, then n >= v_p(e) + 2 recovers.
  - thm:full-supersingular-maximum: nu_min = max(nu_SS(p, e), ceil((1 + log_p e + v)/2)).
- **The first boundary, final**, at k0 = (p^2+1)/2, e = k0 (p-1) p^r, r >= 1, n = r + 3. Statement level.
  - thm:first-boundary-normal-form: an unequal pair is whole potentially supersingular with two-slope models, with
    z_1 = z_2 = ((p-1)/2) p^n and alpha_2/alpha_1 = -1. Its residual representations are split, and the isomorphism
    exchanges canonical and complementary lines.
  - cor:boundary-nonsplit-cartan-image: over the tame extension L of degree p^2 - 1, neither image lies in a conjugate of
    (1 + pO)/(1 + p^n O), where O is the unramified quadratic order.
  - Point-field degrees p^2, p^4, p^6 at r = 1.
  - The Drinfeld-monomial full Cartan with e = f = p^(n-1); at p = 5, n = 4, the indices 6500 and 78000.
  - The Liedtke-Matsumoto 2018, Ex. 5.10 cyclic quotient: divisorial bounds alone do not control normal-model
    specializations.
- **Wild range, 92b**, with e = (p-1) p^v k and p not dividing k. cp18 statements: statement level with arithmetic
  checks.
  - thm:all-wild-bands: nu_min = v + 1 for k = 1, and v + 2 for 2 <= k <= p - 1.
  - cor:all-wild-bracket: v + ceil((1 + log_p((p-1)k))/2) <= nu_min <= v + 1 + ceil(log_p k).
  - cor:wild-next-family: nu_min(p, (p^2-1)p^v, 2) = v + 2.
  - thm:wild-few-exceptions: nu_min = v + 2 for 2 <= k <= p^2 with k outside E_p, where
    E_p = {p^2 - b : 1 <= b <= p-2} u {p^2 - (p+1)b : 1 <= b <= floor((p-2)/3)} u {k : p^2/2 < k < p^2, k = (p+1)/2 mod p}
    and |E_p| = (3p-5)/2 + floor((p-2)/3). (p^2+1)/2 is the least element of the third family, and E_p lies above p^2/2.
    This theorem is superseded at cp22.
- **The complete next band, 92b cp22.**
  - thm:next-wild-band-complete: nu_min(p, (p-1)p^v k, 2) = v + 2 for every v >= 0 and 2 <= k <= p^2, p not dividing k;
    v + 1 at k = 1. There are no exceptions. Statement read.
  - The reduction is thm:single-exception-recovery, with prop:single-exception-patterns (targeted check, given three
    carried inputs). Mechanism, in `paper2/single_exception.tex` (se-parts 2-6):
    - Restrict an unequal comparison at level p^n, n = v + 3, to H_C = {P : p^(n-1) P in C} (order p^(2n-1)). Its
      primitive points have value A/p^(2n-2) if C is canonical, and z/p^(2n-1) if C is a stable noncanonical line.
    - Rescale by the Eisenstein extension u^D = pi: X_i = T_i/u^(w_i). The special fibre is a Hopf algebra generated by
      two primitives, with dim Prim = 2n - 1, a mu_D-grading, and tame scalars in F_p^x.
    - The chain count: chain i gives d - a_i distinct nonzero degrees plus one degree-zero vector. Then
      r >= 2d - a_1 - a_2 + 2 if the scalars differ, and r >= 2d - a_1 - a_2 - C + 1 if they agree, with
      C = min(d - a_1, d - a_2, v_p(u_1 - u_2)).
    - Exchanged lines force p^2 | k + (p-1)/2, so k = p^2 - (p-1)/2. Matched lines leave only b = (p-1)/2 in the three
      families t = 1, 2, 3.
  - thm:matched-midpoint-all and thm:exchanged-midpoint-all exclude both patterns at k0 = p^2 - (p-1)/2 for every v.
    Statement read; the proofs are in `all_v_midpoints.tex` and `exchanged_midpoint.tex`, with input
    lem:midpoint-normal-form: a height >= 2 law is X + Y through degree p^2 - 1 (first sentence re-proved).
  - Consequence: thread A's first-boundary form at (p^2+1)/2 is the hypothesis of the exchanged case, so that case is
    empty (given the carried inputs). The two threads use k0 for different numbers: A (p^2+1)/2, B p^2 - (p-1)/2.
- **Examples.**
  - y^2 + y = x^3 over Q_3(zeta_3) has full rational 3-torsion, additive potentially supersingular reduction and defect 6
    (rationality recomputed at cp18).
  - Over Q_p(zeta_p), p >= 5, full rational p-torsion excludes additive potentially good reduction.
  - The least e for full rational 27-torsion with additive reduction is 162 (defect 12); 216 is the first index the tame
    construction misses.
- **Open.**
  - A full check of the band closure and of its carried inputs: rc-lem:newton, pg-lem:primitives,
    prop:wild-two-slope-patterns, and the all-v midpoint proofs.
  - Multipliers k > p^2.
  - Fixed-field and elliptic realization of the lower examples.
  - A different-model check of the main chain (graph bound; mixed constructions).
  - The merge, and the paper's statement register (41 results unregistered).

## 3. Paper 3: Grothendieck's formula (8.5.1) and the unit-root count (cp12: targeted check)

- Stable exact sequence with the term T^n(X)[p]_st for every smooth ample divisor, and the unit-root count.
- These are consequences of Ogus 1975 and Katz-Messing, likely known in substance.
- Mechanism: stable extraction (Fitting, Artin-Rees), F = ba on the de Rham complex, and a snake lemma.

## 4. Paper 4: a reduced counterexample to Grothendieck's extension assertion (cp12: targeted check)

- The ring: a one-dimensional reduced noetherian local ring with non-finite normalization (Ferrand-Raynaud, Olberding
  type, m = (p, z), m^2 = pm).
- The counterexample: over it, an abelian scheme on the generic point does not extend.
- The contradiction is Serre-Tate: j = t + epsilon against j = t.

## 5. Paper 8: congruence sections and the co-Lie complex of a multiplicative local system

- **thm:sections (final).** The splitting cases of the reduction maps (final intake: computation of seven small cases):
  - GL_d(Z/p^2) -> GL_d(F_p) has a section iff d = 1 or (d, p) = (2,2), (2,3), (3,2);
  - SL_d iff d = 1 or (d, p) = (2,3), (3,2);
  - Sp_2g iff (g, p) = (1,3).
  - Elementary proofs are in lem:two-two, lem:three-linear, lem:four-two, lem:sp-three and lem:corner (not read).
- **The co-Lie complex.** For a local system M of F_p-vector spaces on S of characteristic p, the co-Lie complex of the
  Cartier dual D(M) is M tensor^L O_S (Bergh-Rydh), with connecting class in H^2(S, End E). It splits iff the lifting
  obstruction kappa_V in H^2(Gamma, End V) dies in coherent cohomology.
- **thm:surface (final).** If V has no lift to a free Z/p^2-representation, there are a smooth connected projective
  surface S and a connected Gamma-torsor with surjective monodromy for which the complex does not split. Nevertheless
  [l] = 0 in K_0(S). The construction: Godeaux-Serre free quotients with H^1(O) = 0 and a Cartan-Leray injection.
- **92b's thm:minrank.** The least non-split rank is 4, 3, 2 for p = 2, 3, >= 5, and the complex always splits on curves
  (thm:curve). This is thm:sections combined with thm:surface for the tautological GL_d.
- **Mechanism of the rank** (cp18: lem:transvection re-proved, logic confirmed).
  - lem:lift: kappa_V = 0 iff V lifts.
  - lem:transvection: for p >= 5 no lift of 1 + E_12 to GL_d(Z/p^2) has order p. With T the conjugation, sum T^i equals
    (T-1)^{p-1}, which vanishes because (T-1)^3 = 0, while U^p = 1 + pN.
  - The final intake's search confirms that no lift of 1 + E_12 of order 5 exists in GL_2(Z/25).
- **Archive.** Extends our reading of 8:81: his expectation fails in exactly three small cases.
- **Open.** A proof check of thm:surface, and locators for the classical table.

## 6. Paper 9: Grothendieck's weak-formal cohomology

- **Final (the cp13 text, unchanged).**
  - thm:affine: H^1(C_{A^1}, O) = 0 and H^1(C_{G_m}, O) = 0 for every perfect k. Integral Monsky-Washnitzer cohomology
    has [x^(p-1)dx] != 0 with p[x^(p-1)dx] = 0, and H^1_MW(G_m/W) tensor K = K dx/x, so the affine comparison fails.
    The MW half had a targeted check in the final intake. Its mechanism: x^(p-1)dx = d(x^p/p), and x^p/p is not in the
    weak completion; termwise integration on G_m leaves only the residue.
  - thm:proper: for k algebraically closed and X smooth proper over W with connected fibres, H^1_et(X, F_p) = 0 implies
    H^1(C_X, O) = 0.
  - cor:elliptic: y^2 z = x^3 - x z^2 over W(Fbar_3) has H^1(C_E, O) = 0 but H^1_dR = W^2, so the proper test fails
    even modulo torsion. The deduction was checked: the curve is supersingular at 3.
- **92b additions (cp18, statement level).**
  - thm:proper-integral-comparison: for every perfect k and smooth proper X over W, with no connectedness assumption,
    H^1(C_X, O) is the limit of H^1((X/W_n)_inf, O). For k algebraically closed and X geometrically connected (Ogus),
    it is the limit of H^1_et(X, W_n(k)).
  - thm:rational: H^1(C_{A^1}, O[1/p]) = 0 and H^1(C_{G_m}, O[1/p]) = K, so the map from H^1(C_{G_m}, O) tensor K is
    not an isomorphism.
  - Both are consistent with the final's statements.
- **92b additions at cp22 (statement level; the H^2 deduction checked).**
  - thm:nolift: H^1(C_X, O[1/p]) = H^1_rig(X/K) for every smooth separated finite-type X, with no global lift.
  - thm:integral-rational-injection: H^0(C_X, O) is the product of the W(l_i); integral H^1 is p-torsion-free and
    injects into the rational H^1.
  - thm:affine-second-torsion: on A^1, countable free W_n families in H^1(C, O/p^n) and in the infinitesimal H^1, and a
    countable sum of K/W inside H^2(C, O). The H^2 clause follows from H^1(C, O) = 0, since
    H^1(C, O/p^n) = H^2(C, O)[p^n].
  - The revised thm:proper-integral-comparison: the Ogus clause no longer assumes connectedness.
  - rem:torsion now reads "in integral first cohomology"; thread A's wording ("on the affine-line site") is false in
    degree two.
- **Open.**
  - A check of the site-side proofs (lem:finite, lem:detect).
  - The merge: start from 92b's 40-page text.
  - The proper integral comparison without a global lift.
  - Rational higher degrees.
  - Finite generation of integral H^1.

## 7. Paper 10: mixed polarization indices (final additions at statement level)

- **thm:eventual-all-mixed.** For a mixed abelian surface A over an algebraically closed field of characteristic two and
  ample M with a(M) > 0, put D = chi(M). For e >= e_0(A, M), the generic smooth C in |M^(3e)| has f_C = 9De^2 - 1 and
  r(C) = 9De^2 - 2, so g(C) - f_C = 2. The genus g = 9De^2 + 1 was checked by adjunction.
- **thm:ample-difference.** Given an ample N with a(N) = 0 and M^e tensor N^{-1} ample, the same conclusion holds.
- **thm:finite-field.** Over F_q, q = 2^f: e > 1 + 4q^m/2^a with m = ceil(2a/f).
- **thm:no-ordinary-index-zero-ample-class.** NS(A) = Z[L], chi(L) = 2, a(L) = 1, b(L) = 0; every ample class tL has
  a = 1 + v_2(t).
- **lem:alpha-two-theta-descent** (independent re-proof in the final intake).
  - Every central extension of alpha_2 by G_m over an algebraically closed field of characteristic two splits: the
    cocycles are 1 + a xy, and the coboundaries of g = 1 + bx are 1 + b^2 xy.
  - Hence P descends along any alpha_2 in K(P), by Mumford's level-subgroup criterion.
- **Open.** Smaller degrees, quantitative bounds for arbitrary pairs, and the uniform determinant.

## 8. Paper 18 (final) = 92b Paper 19: Grothendieck's Lubin-Tate lattices (cote 8:49)

- **Statement.** For a Lubin-Tate formal O_K-module (K/Q_p, e = v_K(p)):
  - final thm:tangent: the tangent images agree, alpha(A) = 0, for every finite K/Q_p;
  - final thm:threshold: the full de Rham lattice equals the constant lattice iff e <= p, for any residue degree and
    Eisenstein equation, and likewise for the covariant duals;
  - 92b thm:main: the least a with pi^a L_1 in L_0, and conversely, is max(0, e - p);
  - final cor:counterexample: pi^(p+1) = p, the first unequal case.
- **Lemmas (92b text, as checked at cp18).**
  - The Breuil window of G is Q = A x S with b(u) = eps_0(t - u) + (1 - eps_0) (Lau).
  - prop:gauge: L_1 = g(z)R with g(u) = prod_{n>=1}(1 - sigma^n(eps_0) u^{p^n}/t).
  - lem:inverse: t^{-m} lies in p^{-ceil(m/e)}B_i, and [t^{e-1}]t^{-1} = -a_0^{-1} with v(a_0) = e.
  - The final's own names for the steps: lem:convergence, prop:comparison (multiplication by C(u) is the comparison),
    lem:necessity (valuation p - e for e > p) and lem:sufficiency.
- **Mechanism** (cp18: targeted check; the example recomputed).
  - On each residue component the first exponent is b_i = p^i.
  - z^b/t contributes a t^{e-1}-coefficient of valuation exactly b - e; the other terms have larger valuation. So the
    largest denominator is z^{max(0, e - b_i)}, for g and for g^{-1}, and the minimum is at b = p.
  - On the tangent quotient the product is a unit.
  - Example: p = 2, z^3 = t^3 = 2, g_0 = 1 - t^2/z.
- **Open.**
  - The remaining elementary divisors.
  - The merge of the two versions.
  - A different-model check of the text to be posted (the cp18 check covers the 92b mechanism).
  - A STATEMENTS.tsv.

## 9. 92b Papers 18, 20, 21: mod-2 monodromy of hypersurface sections (not in the final)

Checks: statement level; genus and ranks recomputed at cp18.
- **Paper 20.** Sections of degree d in {1, 3} of E x E, with E: y^2 + y = x^3 supersingular in characteristic 2, in the
  Segre embedding:
  - genus 9d^2 + 1 and two-rank 9d^2 - 1;
  - geometric and arithmetic image GL_{9d^2-1}(F_2) (GL_8, GL_80), over every perfect field;
  - method: exact finite-field specializations and Kantor's Singer-cycle theorem.
- **Paper 21.** Pairs of ordinary cubics: GL_8 on a nonempty open. The quadric system of rank 35 has image
  F_2^96 x| GL_32, the stabilizer of three covectors.
- **Paper 18 (92b).** The invariant quotient of the relative unit-root system has dimension 2^f - eps_A, and is zero
  for odd polarization.
- **Paper 21 at cp22** (29 pp, 22 statements; statement level, with the degree recomputed).
  - thm:hasse-reduced: on an ordinary principally polarized surface in characteristic two, the Hasse divisor in
    |3d Theta| is reduced, of degree 9d^2, with generic corank one, for every d. The relative H^1 quotient over
    P(H^0(3d Theta)) is Omega_P, so the determinant is a section of O(9d^2).
  - thm:ppav-open: GL_8(F_2) on an ordinary moduli open.
  - thm:incoming: a uniform incoming isogeny of degree l^(4R) to a GL_8 source.
  - thm:natural-block: an odd isogeny with multiplier n gives an actual GL_8 block fixing a complement for every
    d >= n + 1.
  - Open: the eventual full image, Hasse irreducibility, stable rank loss, and an effective R.

## 10. Other papers (statement level only)

- Papers 5-7 and 11-16: as in the final README table.
- Paper 17: sharp residues and hypersurface monodromy, 49 pp, with 7 new auxiliary lemmas.

## 11. Open rows and gates (the final)

- **The run's record.** The run stopped under the user's rule: two consecutive no-movement reviews, with review15 at
  the 18:05:09 UTC cutoff.
  - 684 of 1,018 register rows are NOT_YET_RECHECKED (thread B at cp22: 677).
  - 43 questions carry gates in QUESTIONS.tsv.
  - The crosswalk covers 331 statements.
- **Mathematics.**
  - Paper 2: multipliers k > p^2, and fixed-field realization (the band k <= p^2 is closed by 92b, pending checks).
  - Paper 9: the integral comparison without a lift, and higher degrees.
  - Paper 21: the eventual image.
  - Paper 10: quantitative bounds.
  - Paper 12: the general odd-prime dual rank.
  - Papers 15, 17 and 92b's 20: general primitive and fixed-embedding monodromy.
  - The Lubin-Tate paper: the elementary divisors.
- **External.**
  - Merge the threads.
  - Regenerate the statement registers of Papers 2, 8, 17 and 18.
  - Different-model re-proofs of the main chains.
  - Forward literature searches.
