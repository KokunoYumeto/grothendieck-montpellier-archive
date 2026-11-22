# Whole-proof review: PNEW-012

- Date: 2026-11-21, 22:09 UTC.
- Reviewer: `/root`, GPT-6 Astra Pro; effort not exposed; GCT_POS.
- Type: whole-proof targeted check and exact replay; source/encoding-scope audit.
- Outcome: **PASS** for the scalar fat-point / two-row-output formula.

The whole proof of `outer_six_scalar_positive.tex` was read, together with all367 lines of the positive-template/evaluator script and all256 lines of the independent character/matrix-count verifier. The classical KOH/GOS identities are explicitly cited published inputs, already full-chain read by the branch. Root also inspected the primary PPS output-shape reduction and §2.2 encoding discussion. The contribution is a compilation of that known positive identity, with no claim to have discovered two-row positivity.

The Gaussian transpose makes the only variable tree have fixed partition mass6. At a node of mass b, the all-ones partition alone preserves that mass; every other partition reduces total child mass. Maximal-run compression is unique, including runs of length zero. The affine child constraints imply validity of every omitted intermediate step. The telescope gives a finite skeleton set independent of n. The finite recurrence and JSON matrix generation agree exactly:330 tagged polytopes in total, at most45 for a given outer shape, at most11 variables.

The marking formula is a direct iterated two-factor interval identity. Its parity is enforced by the final integer equality, and all negative endpoints occur strictly above the midpoint3n. This proves that the positive polytope count is the desired two-variable Weyl coefficient. The zero-parameter and zero-leaf arguments are valid and prevent a spurious multiplicity from unit factors.

Real boundedness, not merely integer boundedness, follows from the mass/center telescopes. Run variables and marks lie in [0,3n]. The exact hook-content evaluator has at most128 reciprocal-denominator queries of fixed degree at most21. Under the parity recurrence the denominator roots remain on the unit circle and its coefficients are uniformly bounded by fixed binomial bounds; numerator bit lengths grow only linearly in the number of halving steps. This proves polynomial bit complexity without assuming positivity of the intermediate signed calculation.

Root replayed all2,717 positive-path versus fast-evaluator comparisons; regenerated all330 matrix templates; and replayed the separate full n≤3 character checker, including5,214 coefficients,242 literal polytope-matrix counts and44 dimension checks. This is a replay of the supplied independent algorithms, not a claim that root independently authored them. The independently authored root R-NEW-001 table is a separate prior verification.

The scalar substitution n=c−k, r=c is correct and its chamber inequality is equivalent to4c−6k≥0. Arbitrary flag tails and three-row outputs remain outside the theorem. Thus the all-output Question5 is not marked solved.
