# Exact primitive minimum and a fixed-norm obstruction

GHOSTS-20261121. Checker/author: GPT-6 Astra Pro, inherited effort not separately observable, `/root/bounded_specialization`. The full proof is in `sections/primitive_weil.tex`. Joint discovery/check with `/root/prime_arithmetic`; the finite catalog search was not used as a theorem dependency.

## Conclusions

The primitive integral half-class t0=t_star/2 has exact complex complexity16, and exact local complexity16 at every geometric good reduction, including characteristics2 and3. The proof covers every positive multiplier and arbitrary effective integral surface cycles. V03 first establishes the complex and p>3 cases; V05–V06 supply the complete small-characteristic argument.

The proof closes the N1 gap left by the period bound. Both odd Kunneth components of the two main low-degree graph surfaces differ. At most one low-degree odd correction fits in each numerator, and two orientations must be corrected. This forces both main graphs to have degree at most10, hence to be automorphisms with matrices having two or three Eisenstein unit entries. A rank-one trace inequality excludes a normsum2 main matrix, and the cofactor formula excludes two normsum3 matrices.

The complete classification of degree<=6 extra components was independently checked by coordinate-pair projection degrees, including cross-block graphs in supersingular characteristic. It gives exactly the normsum budget needed for the odd coefficients; it does not silently assume every correction is a graph over one of the preselected B factors.

For characteristics2 and3, V05 proves that every nonzero-Weil surface of degree<=14 is an abelian graph over one of the six coordinate pairs. If no pair projection has degree1, the dependence partition of the four nonconstant coordinate function fields must be(1,3), which makes the surface E times a curve and gives zero Weil projection. V06 then treats every pair of main types: two dominant projections; exactly one dominant projection, in either orientation; and products of two curves. Odd-rank and matrix-support arguments eliminate mixed types. The same-orientation one-dominant case uses the exact normsum table and the six pair-projection degrees. Product pairs are excluded by the rank-two target in T tensor T, the J projections, and the exact low-norm quaternion data. Thus the proof has no finite-catalog or numerical-enumeration dependency.

The same section proves that norm T alone cannot determine or bound the minimum, even with A and theta fixed. The explicit rational vectors v_n=((n²−1)t0+(2n−1)R t0)/(n²−n+1), for n positive and divisible by3, have self-intersection6 and exact integral cohomology denominator n²−n+1, so c(v_n) is unbounded.

## Checks actually performed

- Read the full low-degree surface argument in the finite-characteristic memo and independently reconstructed the coordinate-pair classification.
- Checked the cross-pair matrices f,g, including quaternion multiplication order, the formula U=Nm(b)g f^-1, and the equality degree2(1+normsum U).
- Checked that the degree pair of odd coefficients is(d,d³), hence(2,8)/(8,2) for degree2 graphs, and that equality of an odd coefficient would force equality of the main graph and its Weil coordinate.
- Checked the two-correction allocation, multiplicities, residual degrees, and every positive multiplier.
- Independently derived the initial longer unit-matrix case exclusion; then checked prime agent's shorter rank-one trace proof, which is used in the final section.
- Checked integrality using even Kunneth summands, self-intersection24/4=6, and primitiveness from the absence of a square divisor of6.
- Checked fixed-norm vectors, their gcd, the index relation h² divides27, and the lower denominator bound. No claim that a fixed norm and fixed integral denominator alone lead to unboundedness is made.
- Proved the dependence-partition lemma for all degree<=14 nonzero-Weil surfaces, including inseparable projections: pair degrees count total field-extension degree, so degree1 is birational; the argument does not require separability of other projections.
- Checked every V06 pair of main types, the normsum identity T_R=ac, uniqueness of the connected subgroup associated with a rational graph, the same-orientation correction allocation, and the support vectors of degree4 correction graphs.
- Checked the P/P rank-two argument, the absence of T tensor J and J tensor T in every degree<=6 correction, and the fact that each correction with a T contribution has a single coordinate-fiber factor and can contribute to only one of T tensor I and I tensor T.
- Read the communicated independent full-proof checks from /root/prime_arithmetic and /root/cm_transport; both report a pass of V05–V06. The parent also reports a complete read and no fault. These are separate human-readable mathematical checks, not formal proof verification.

## Check events

statement_id	date	who_model_effort_run	type	outcome	method_or_locator
V01	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Even integral Kunneth projection, graph intersections, self-intersection6 and primitiveness checked	sections/primitive_weil.tex
V02	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	All irreducible degree<=6 surfaces classified; cross-block odd coefficients and exact degree/normsum formula checked in arbitrary characteristic	sections/primitive_weil.tex
V03	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Full proof covers all multipliers, both odd blocks, correction allocation and matrix cases; exact16 over C and every p>3; p2/3 not asserted	sections/primitive_weil.tex
V04	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	independent re-proof	Explicit fixed-norm rational sequence has exact cohomology denominator q_n and unbounded complexity at fixed A,theta	sections/primitive_weil.tex
V05	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	joint derivation and complete proof check	Dependence equivalence, crossing-pair count, product E times curve exclusion, degree-one extension and all-characteristic scope checked; every nonzero-Weil surface of degree<=14 is an abelian graph over a coordinate pair	sections/primitive_weil.tex
V06	2026-11-21	GPT-6 Astra Pro; inherited effort not separately observable; GHOSTS /root/bounded_specialization	joint derivation and complete proof check	All multipliers and all main-type pairs excluded at p2/p3; quaternion sparse matrices, one-dominant norm/support table and product rank-two I/J/T argument checked; primitive exact16 at every good reduction	sections/primitive_weil.tex
