# Independent whole-proof audit: all 26 ternary coface fillings

**Finding:** K17-K12-TERNARY26-FILLINGS-AUDIT. **Verdict:** PASS. Date: 2026-11-21 UTC. Auditor: `/root/vandiver_k`, GPT-6 Astra Pro, effort not exposed, run K17.

I read the complete 112-line `k12_ternary_coface_section.tex` and the entire 151-line standard-library verifier `k12_ternary_coface_certificate.py`, then replayed the exact verifier on every frozen record. It passed all 26 cases; the exhaustive short-vector searches use 327–477 nodes. I also freshly read DEKM's author-current primary text §1.2.1, equations (1)–(2), §1.2.2/Proposition1.3, and §1.2.3/Proposition1.5, printed pp.4–5, and the beginning of §2.1 p.6.

## What was independently checked

1. **Actual cells.** Rational LDL decomposition proves positive definiteness and is itself reconstructed entrywise. At each enumeration node the integer interval is exact: if the rational shift is a/b, the radius is floor(sqrt(floor(b² R))), so the lower endpoint `-((radius+a)//b)` is precisely ceil((-radius-a)/b). Descending recursion therefore searches all integer vectors of norm at most one, without a finite-box assumption. Exactly the 28 signed listed vectors occur, all with norm one. Minimum vectors are automatically primitive. The independent quadratic rank is 14, so the cone is simplicial and its projective degree is 13.

2. **Every old facet is handled.** The verifier matches each old template exactly, includes every one of the 26 old `(record,orbit)` keys once, and partitions all 13 old-ray deletions into explicit integral odd reflections or rank-deficient relative facets. The reflection functional is checked integral in the actual ambient lattice coordinates, not merely the index-three minimum-generated sublattice. Each matrix is checked involutory, exchanges exactly the prescribed pair up to a common sign, fixes all remaining facet rays, and fixes the added ray. Thus its action on independent quadratic rays is an odd transposition. All marked old coloop deletions are separately checked to retain vector rank nine after the new ray is added; no hidden full-rank facet is discarded.

3. **The coface itself is orientable.** The new-ray deletion is the prior orientable cell, whose orientation classification I had independently whole-audited and replayed in `k12_ternary_glue_vandiver_audit.md`. Every other full-rank facet has an odd stabilizer; equivalence preserves that property and vector rank. A stabilizer of the coface must therefore fix the unique orientable full-rank facet and the complementary ray. Its permutation on that facet is even, hence so is the permutation on all 14 rays. This proves the source coface belongs to the oriented chain complex.

4. **Coefficient exactly one.** DEKM equation(1) sums incidences over actual facets in the target orbit. Here there is precisely one such facet and its simplicial incidence is ±1. The coface stabilizer fixes it, so any equivalent transfer description has source index one; target stabilizer order does not multiply the degree-zero orientation-coinvariant map. Thus an orientation choice gives ∂η=ρ over R=Z[1/13!]. Odd facets vanish because 2 is inverted. The finite-stabilizer localization at rank ten is covered by the same primary §1.2.2.

5. **Homology support conclusion.** The earlier classification supplies all maximal-index-at-most-three oriented generators, with the minimum-generated survivor already filled and the proper-index-three cases exactly these 26. Subtracting the 26 explicit boundaries from an arbitrary degree-twelve cycle preserves its homology class and removes precisely those coefficients. This establishes representatives supported at maximal minimum-basis index at least four. It does not prove vanishing of that residual group or of K12.

No correction was requested. The unused helper functions in the verifier do not affect these checks; the active certificate reconstructs all needed minimum sets and integral facet identities directly.

## Reviewed file hashes

- `k12_ternary_coface_section.tex`: `8315d583dc0c610d8e01f3961fadad854632482151d4ad8270796c6eb28b0e1f`
- `k12_ternary_coface_certificate.py`: `767d7bc27ff0ae44d461ef08b2c2b7d51000dfd6ec7e7884741cd14b782e11e7`
- `k12_ternary_coface_data.json`: `119691eb6607afd11d8ae3a583b2442702c1595f95cc584b0d22ddce799d9678`

The earlier 26-template coverage is a previously audited input, with the published five-polytope completeness theorem still treated as cited background. No new claim to rerun that published finite classification is made.
