# Independent audit of the rootwise pole nonvanishing refinement

Reviewer: `/root/archive_kummer`, GPT-6 Astra Pro. Date: 21 November 2026. This is a source-content and whole-proof review, not formal execution or a priority claim.

## Verdict

**PASS**, relative to the independently audited arithmetic, topology, actual rational realization, and multivariate separation construction in `work/multieven_archive_audit.md`. Both the complete Markdown refinement and its complete TeX translation were read. The refinement proves a sufficient condition; it does not verify an additional arithmetic prime.

The condition is correctly quantified separately for every even component and every distinct root of its companion polynomial, allowing the ordered odd pair to depend on the root. Repeated roots require no additional hypothesis because the highest selected Laurent coefficient uses the restriction of the numerator itself. A globally nonzero numerator would not suffice.

## Reconstruction of the proof

At the selected disjoint pairs, the change of coordinates S=(1+T_1)(1+T_2)-alpha is a continuous formal automorphism over the splitting valuation ring because alpha-1 is topologically nilpotent. Its quotient is the single-variable formal power-series ring, so restriction is equivalent to nondivisibility by the prime divisor. Passing to the fraction field of the surviving base-variable ring makes every nonzero restriction invertible.

The previously checked maximal-pair and Pareto-maximal-order selection isolates one nonzero Magnus coefficient times the selected restrictions. Each restriction involves the one independent surviving variable in its pair. The Magnus coefficient involves the unpaired variables. Consequently their product is nonzero in the common domain whenever each restriction is nonzero. The earlier proof used unit constants solely for this nonvanishing. No integral-unit conclusion is used after this step. The no-pair case remains the ordinary bounded-measure moment argument. The root-dependent assignment of odd target characters does not introduce another coefficient: the preceding wrong-character identity and fixed singleton characters remove the same alternatives as before.

The analytic identity is first proved after clearing denominators on the large Cartesian weight tails in the bounded-denominator ring. Only then is it expanded in the Laurent ring over the base fraction field. Thus unrestricted coefficients in that auxiliary fraction field do not create a false bounded-measure assertion.

## Basis choices

For fixed gamma, a replacement lift with the same abelian class differs by a closed commutator. Its target length-two component is a bounded transform A of two odd-orbit letters; a term containing an even letter has larger target length. Therefore B changes by A and C=qB changes by qA, whose divisor restrictions vanish.

A cyclic generator identifies its finite free component with Z_p[z]/(q): the natural map is surjective between free modules of the same rank and hence an isomorphism. Another cyclic generator is multiplication by a unit b modulo q. Its target length-two component changes by b(z)B+A. The restriction of the new numerator is b(alpha) times the old one, and b(alpha) is nonzero (indeed a unit after integral scalar extension) because evaluation is a ring homomorphism and b is a unit modulo q. This remains true for repeated roots.

Changing an odd rank-one Lambda basis multiplies its linear moment by a Lambda unit f. Such f has unit constant coefficient, and f(T) stays a unit after the indicated divisor substitution. Renormalizing target letters divides the ordered-pair numerator by the product of these units. Higher commutator corrections do not alter the two-odd-letter contribution except by the already controlled analytic terms. Scalar extension is injective. No invariance under a change of gamma is asserted or needed.

The formal example C=p correctly distinguishes nonzero restriction from a unit constant and is explicitly not represented as an arithmetic example. The remaining arithmetic gate is correctly retained.

## Checked file versions

- `work/pole_nonvanishing_gate.md`: `18e4bd24c2f719e7a6ffb6fe6f5a44851adb06145f5c25b4dcf9cce378e1211f`
- `work/pole_nv_section.tex`: `084d5a3174d521bfccf1e512cd502458e6703807879e8dbfa25c28ed8bf64e21`
