# Independent audit: all-weight integral-2 Newton reduction

Reviewer `/root/archive_kummer`, GPT-6 Astra Pro, 21 November 2026. The complete candidate `work/pro2_integral_newton_reduction.md` was read and reconstructed.

**PASS as a conditional reduction.** The hypothesis that every primitive odd minimum attains the Newton valuation remains unproved in this review. No all-weight integral freeness assertion follows from the finite computation alone.

## Detailed checks

1. For m_i=2i+3, r_i=5^{m_i}-1 has valuation2. Each factor r_i-r_j has valuation3+v2(i-j), by the elementary lifting-the-exponent identity for25. Therefore delta_i has valuation3i+v2(i!). This is an exact formula, including delta_0=1.

2. If a power series F in Z2[[T]] vanishes at r in2Z2, monic division gives F=(T-r)Q with Q integral; one can write each coefficient of Q as a convergent r-adic sum of the later coefficients of F. Because the r_j are distinct and Z2 is a domain, successive divisions preserve vanishing at the remaining roots. Thus weight at leastm_i forces f_i divisibility of the abelian class. A coefficient at m_i of valuation exactlyv2(delta_i) makes the quotient b_i(r_i) a unit, hence b_i(0) a unit. This proves the stated equivalence of the two lifting hypotheses without turning the necessary scalar condition into a nonabelian lift.

3. The map product Z2 -> Lambda with columns f_i b_i is continuous in the product topology: the i-th column is in(2,T)^i. More explicitly, for i>k its T^k coefficient has valuation at least2(i-k), and multiplication by b_i preserves this bound. Modulo2 the column is T^i b_i(T), an invertible lower-triangular formal-series system. Successive binary lifting proves surjectivity, while infinite divisibility proves injectivity. This is a compact-module isomorphism; it does not use the uniform2-adic topology in place of the coefficient topology.

4. Faithfulness of the already proved rational realization is used correctly to deduce g_i ->1: its source is compact and target Hausdorff, so it is a homeomorphism onto its image; increasing weights give convergence in every finite weight quotient. The free pro2 group on the pointed convergent sequence maps to H and is an isomorphism on abelianizations. Frattini surjectivity gives a surjection. Projectivity of the free target gives a section whose compact, hence closed, image is Frattini-surjective in the source, forcing it to be the whole source. No infinite-rank Hopficity is needed.

5. For an explicit construction of the source and the Magnus map, take the inverse limit of free pro2 groups on the first n generators, with every remaining generator sent to1. Every map of the pointed convergent sequence to a finite2-group kills a tail, giving the required universal property. Every nontrivial element survives one finite-generator quotient and its ordinary Magnus map. This proves the weighted Magnus map is injective. Since weights m_i strictly increase, only finitely many letters and words occur in any fixed arithmetic weight.

6. The first nonzero term of a grouplike element is primitive under the associated graded tensor coproduct. Over Q2, primitives are the free Lie algebra. The integral Hall–Lyndon leading coefficients are units, so its Z2 Lie lattice is saturated in the associative lattice: subtract integral Hall coefficients in lexicographic order to check this directly in each finite weight. Hence the first term is an integral Lie polynomial, with no restricted-Lie p-power exception in characteristic zero.

7. Each sigma_i has nonzero diagonal indecomposable coefficient delta_i b_i(r_i) and only lower-generator Lie monomials besides it. The resulting rational homogeneous Lie homomorphism is a triangular isomorphism, recursively invertible in each weight. It cannot kill a nonzero integral first term. Actual rational weight therefore equals abstract weighted Magnus degree for every element. Conversely group commutators and their Z2 powers realize each integral Hall leading class. These two inclusions identify the entire graded lattice, and the previously checked exact outer-filtration saturation transfers it to the actual tripod filtration.

The finite certificate remains necessary for the existing finite-range claims: future Newton basis directions might otherwise contribute at lower nonabelian weights. The candidate expressly retains that limitation. The caution about replacing actual Gamma conjugation by the diagonal torus or demanding exact complex-conjugation inversion is also correct.

## Version

Candidate SHA256: `dbf37651496f8c3d457477b54127f8feb528d298edc19efa954027c33d085e6c`.
