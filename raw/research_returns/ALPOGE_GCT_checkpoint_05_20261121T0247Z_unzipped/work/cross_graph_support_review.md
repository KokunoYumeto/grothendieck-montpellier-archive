# Independent whole-proof review: P-F27

Reviewer: GPT-6 Astra Pro; effort inherited/undisclosed; run `/root/bridges`.
Actual whole-proof review completed 2026-11-21T01:09:28Z.
Draft: `work/positivity_graph_support.tex`.

## Outcome: PASS

I read the entire draft and independently reconstructed its lattice, graph, and equality arguments. The proof handles arbitrary finite two-power lift order and rank deficiency; neither is assumed away.

The rational-span implication from semistability is valid in any coordinate basis: a nonzero invariant evaluation has a nonzero coefficient monomial, and its torus weight makes a positive constant multiple of the all-ones vector a nonnegative integral combination of the support exponent columns. The determinant character factors through the support cokernel exactly as asserted.

For each connected support component, a spanning-tree matrix has independent columns, as leaf elimination shows. In rank `v−1`, all its maximal minors are nonzero signed powers of two. The unique rational solution `Tc=1` has denominator dividing every maximal minor by Cramer's rule. The signed cofactor kernel vector has adjacent absolute coordinates in ratio two; this forces the minimum exponent at most `v−2`. Thus the determinant class is torsion with the claimed stronger bound even though other cokernel directions are free and eigenvalues can have larger order.

In full rank, adding one support column gives a connected unicyclic square basis. Leaf elimination produces factors one or two. For a nonloop cycle of length `l`, I verified the two permutation terms `2^a+(-1)^(l-1)2^(l-a)`, including a double edge. Equal exponents force a zero determinant in the even-length case; otherwise the two-adic valuation is their minimum. Hence every nonloop cycle gives at most `v−2`, while a loop gives at most `v−1`.

The product of component characters has two-power order at most the largest component order. Extremal order `2^(n−1)` therefore requires one connected full-rank component on all variables, a loop basis, and all tree leaf factors equal to two. Rooting at the loop gives parent eigenvalue equal to the inverse square of its child. Depth bounds the order of each eigenvalue, so maximal determinant order forces a path of depth `n−1` rooted at an endpoint. The deepest eigenvalue is primitive. I checked that the resulting distinct-valuation spectrum admits only the chain monomials and final cube; all are present in the chosen basis. Rescaling therefore gives the smooth chain cubic and also bounds the matrix order itself in this equality case.

The final quotient consequence correctly combines P-F26 with semistability: every competing singular boundary representative must have a three-distinct-variable monomial in every eigenbasis of every eligible finite lift. It does not classify that hypergraph case or prove global Hilbert-series noncancellation.

No correction was required. No external source theorem is silently used for the graph determinant or deficient-rank torsion assertion; both are proved explicitly. No historical-priority claim is made.

No edits were made to the author's theorem file.

## Added connected-graph-part extension: whole-proof PASS

At 2026-11-21T01:13:42Z I read and independently reconstructed the complete appended argument. If the graph submatrix has full rank, P-F27 already gives the chain spectrum and excludes every extra triple monomial. If its rank is `n−1`, the signed tree cofactors have the form `epsilon*2^e*(-2)^h_i`, and adjoining a triple column gives the sum of three such cofactors. A nonzero sum of three powers of `-2` has valuation below the largest exponent unless all three exponents coincide. The exceptional maximal bound `e+H=n−1` forces every rooted-tree leaf factor to be two and makes the maximal-height vertex unique, so three distinct vertices cannot all attain it. This supplies the strict `n−2` valuation bound. If all triple columns lie in the tree span, the previously checked deficient-rank argument applies instead. Every case is covered, and no nonnegative-span or exact-lift assumption is added. The resulting disconnected-graph requirement is valid.
