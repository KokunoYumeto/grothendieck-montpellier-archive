# THETA3-A14 independent whole-proof review

Reviewer: GPT-6 Astra Pro, `/root/definite_bridge`; reasoning effort inherited and not exposed. Date: 2026-11-21.

**Result: PASS after the explicit TC/Later hypothesis clarification.** I read all of `paper_A14.tex`, reconstructed its finite-character and coefficient-field arguments, and checked the literal source clauses listed below. A13's previously established ray-class and finite-column realization results are retained as named inputs; this review is not a transitive Lean audit or a build.

## Mathematical reconstruction

For Galois CM `E`, complex conjugation is central. Chebotarev therefore gives infinitely many primes with Frobenius precisely complex conjugation, outside every specified finite set. Such a prime splits completely in the real subfield and is inert in each relative quadratic completion. The finite exclusions ensure it is odd and does not divide the roots-of-unity group. A prescribed primary inertia character consequently kills A13's roots-of-unity kernel. Extension from the subgroup of the finite anticyclotomic ray-class quotient is valid; raising to the CRT exponent congruent to one on the p-primary part and zero on the prime-to-p part preserves the prescribed inertia while producing p-power order.

At the coefficient prime p, unramifiedness and triviality on the real-subfield local multiplicative group together imply triviality on the entire quadratic local multiplicative group: an unramified quadratic extension has the same uniformizer. This verifies the actual stronger `IsPsi.atl` clause. The exact ramification set is allowed to shrink; all remaining ramification places have prime residue cardinality, ramification index one, and the required split and avoidance properties.

The multiquadratic enlargement is correct. Distinct primes congruent to one modulo `4p` and outside the discriminant of the old normal coefficient field give independent squareclasses, a totally real extension split at p, and trivial intersection with the old field: every nontrivial multiquadratic subextension contains a quadratic field ramified at a newly chosen prime. Local tensor products split each old p-adic place into `2^r` copies. Complex conjugation fixes the totally real field and every such local label, so each old conjugation orbit gives `2^r` distinct new orbits. The extra degree is exactly the stated power of two, less than `2t` for `t>1`.

Assigning one prescribed character to each of t distinct orbits and the trivial character elsewhere verifies every `TwDat` condition, including its conjugation clause and its behavior away from p. Since p differs from the reference prime, the literal `xiTw` formula gives precisely the stated character range. Contraction of coefficient primes under further normal extension preserves residue characteristic, conjugation, and the range by lying over.

The corrected TC paragraph explicitly retains A13's diagonal-space, mass, reference-value, orientation, selection and ambient-datum conditions. `Later` is now asserted only with `HasLetters`, for instance from retained `K.Over`. This resolves the only scope clarification raised during review. For the stronger `ColW` assertion, the initial witness and the retained context are explicit. The orientation constructor changes only `piG`, so both Pins clauses remain; the fixed complex images of `Ks` and `LL0` preserve their reference-value assertions. Extending a principal fractional ideal preserves its generator, and the fixed ideal generators defining `ellLat` base change exactly, so `FieldOK` persists. No original full host or initial `ColW` is manufactured by this argument.

The final finite Fourier formula on the primary quotient is correct, including the coefficient l1 bound at most two. Its scope is the quotient of nonzero oriented wedge values and the actual support/covariance of the seed, not arbitrary matrix delta functions or an unproved global derivative-rank assertion.

## Sources actually checked

- Milne, *Algebraic Number Theory*, version 3.08, Theorem 8.31 and Corollary 8.32, printed p147, from the official primary PDF. Only these stated Chebotarev inputs are invoked; no independent proof of Chebotarev is claimed.
- `Formalism/LocalToGlobal/UnitaryNorms/CharHost.lean`: full `IsPsi`, including `atl`.
- `Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/CmQuadraticFormEqAlternatingForm.lean`: `Enl`, `TwDat`, `xiTw`, `set`, and the finite `offSet` proof.
- In the same definitions directory, `IsRationalUnitaryDeterminantMapRationalUnitaryTo.lean`: full `IsTwist`; `PositionOfIntro.lean`: full `ColW`; `LatAtLattice.lean`: both `Pins` clauses; `IsHalfPtIff.lean`: `ellLat`, `IsGen`, and `FieldOK`.
- `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/ExistsColumnInputAssembled.lean`: complete `exists_oriented`, `exists_colIn`, and `isTwist_of_mem_set` proof bodies.
- `FixedCoefficientFieldInComplex.lean`: `FieldDat`, `KsExact`, and the surrounding reference-value predicates; `Formalism/LocalToGlobal/UnitaryNorms/CharTied.lean`: full `ValLL0` and its embedding definition.

These are selective static reads of the commit-pinned mirror already recorded by the project. They do not certify compilation or all imported dependencies.
