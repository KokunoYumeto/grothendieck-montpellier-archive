# Independent whole-proof review: I-37

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.
Actual completed reading/rederivation: 2026-11-21 04:43:04 UTC.
File: I37_multilinear_singular_two_pairs.tex.
SHA256: 4e185cf9d3da15375df951f1f8ca7c21b58c40bf93acd8a95341d857fd860274.
Outcome: PASS. This is an independent-agent proof reading and targeted rederivation, not an external or formal certification.

## Complete scope read

Read the entire statement, all six proof parts, sampling bounds, and provenance/scope paragraph. Independently checked the following points.

1. The arbitrary-slope Cauchy center dominates every specified pair: the numerator in (I.92) cannot vanish because the nodes are distinct and both slopes are nonzero. This remains true over fixed coefficient extensions.
2. The coefficient of the second pole amplitude yields first partials at the one-pole center. Distinct poles isolate these partials in every characteristic. Differentiation along the center parameter gives Hc=0 without division by two. Multilinearity makes the diagonal zero in every characteristic.
3. Irreducible factor inheritance is restricted correctly to multilinear polynomials. Individual degrees force disjoint variable sets, specialization of the other factors realizes the desired factor up to a nonzero scalar, and absorbing constant matrices preserves affine singular factors. Extension to an algebraic closure is a proof device only.
4. Primitive-column factorization of a polynomial rank-one matrix is valid over a multivariate polynomial UFD. A denominator factor would divide every column entry, contradicting primitivity. Rank-one strict internal intervals would split the irreducible polynomial into factors respectively depending on the first and last variables; neither factor can be constant. Thus all strict internal intervals have rank exactly two.
5. The I36 second-compound/pivot-clearing argument has exactly the needed simultaneous quantifiers. A nonzero entry is a product of univariate endpoint factors and adjacent bivariate factors after multiplying by nonzero pivots; pairwise dominance preserves the whole product despite shared variables.
6. Endpoint nonvanishing follows from two-coordinate dominance, and preservation of rank-two interior products makes it persist. The compatible gauges use image/ker complements justified by adjacent rank two, with full-interval rank ensuring transported bases remain active.
7. The endpoint shears are explicitly correct: L^-1 P=P, PR=P, and the endpoint passive components can be eliminated because the active row/column are nonzero. The two shears act at different state cuts and remain valid when n=3, where they occur on the same interior matrix from opposite sides. They preserve affine dependence and singularity.
8. In the normalized pencil P+Y_iD_i, the determinant's linear coefficient is D_i,33, so it vanishes. First derivatives give the displayed zero active transition and endpoint coordinates. For nonadjacent second derivatives an intervening P kills the passive state; the remaining lower-triangular active blocks cannot move state one to state two. The Hessian is therefore zero-diagonal tridiagonal.
9. Hc=0 with every c_i nonzero forces the consecutive entries to vanish successively along the path, with no characteristic-two exception. All three adjacent Hessian formulas were checked directly.
10. Every nonzero output state path must either cross 1→3→2 at consecutive positions, start passively and enter state two at the first position, or exit passively at the final position. The displayed zero products cover each case; any return to state one requires a later forbidden crossing. The n=3 endpoint cases are also covered.
11. The rescaling F(W)=f(W_i/d_i), c_i=d_i, and amplitude substitution z_h→-z_hA(y_h) give the ordinary centered SV2 map with the stated signs. The rescaling preserves the class. The finite interpolation count and field-size condition follow from the existing Newton-simplex lemma; n≤2 and D=0 are harmless endpoints.

## Limits preserved

The theorem applies to affine singular-factor width-three representations, with arbitrary unknown order and arbitrary characteristic over a sufficiently large working field. It does not prove two pairs for mixed generic-rank-two/rank-three factors or for nonlinear singular factors. No general factor-width monotonicity is used. No numerical rerun was needed; the proof is algebraic and the possible endpoint and characteristic risks were resolved directly.
