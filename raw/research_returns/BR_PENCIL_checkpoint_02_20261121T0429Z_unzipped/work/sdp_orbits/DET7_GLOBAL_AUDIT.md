# Independent review of the determinant seven-plane global cover

## Reviewed objects

I read the entire current `work/root/verify_det7_global.py` and the complete proofs P-07, P-09, P-12, P-14, and P-15. I also reran the root global verifier; it returned PASS with25 Borel ideals and2997 exact modular minors. This was an audit and replay of the independently written verifier, not a claim that I authored an additional independent matrix implementation.

## Coverage and direction

P-07 supplies a direct transvection degeneration from any coordinate determinant plane to an order-ideal plane, preserving dimension and never increasing border rank. For each transvection the nontrivial exterior-coordinate actions are disjoint two-element chains; the limit frame is independent. The decreasing integer index sum guarantees termination. Closure under all lower replacements is exactly componentwise order on pairs of two-subsets. This proof is valid in every characteristic, although the later rank certificates here assert characteristic zero only.

The root verifier enumerates all order ideals of cardinality7 by adjoining an element only after every strict predecessor is present. Inductively this yields every ideal, since removing a maximal element of any nonempty ideal produces a smaller ideal. The exact resulting set has25 elements and matches the certificate without repetition.

Each certificate row is one of: two ordinary support flattenings, seven Koszul flattenings on the7-dimensional factor, two Koszul flattenings on the support factor, or fourteen prolongation cases covered by P-09/P-12/P-14/P-15 and transposition. The explicit representative/transposition map is checked against the actual subset in every prolongation row.

## Koszul minors

The verifier reconstructs the signed quadratic matching coefficients directly. Its A-Koszul and B-Koszul entry formulas have the usual exterior insertion sign. Pure-tensor costs are binomial(6,p) and binomial(m-1,p), respectively. Every selected minor order or sum of disjoint weight-block minor orders exceeds13 times that cost. The numerical weight encoding with base32 separates the bounded row/column torus characters; the tensor grading identity makes off-diagonal weight blocks zero. Distinct row and column sets and distinct block weights are explicitly checked before ranks are summed. Primality of1000003 is verified, and all nonzero modular determinants certify nonzero integer determinants over characteristic zero.

## Prolongation proof readings

P-09 correctly treats the11- and12-variable types by quotient dimensions2 and1, saturation kernel monotonicity, and counts of nonzero columns in distinct output weights. Its two-line overlap subtraction is in the correct direction. P-12 has baseline A rank74 and requires added-line increment at least5 to contradict78. P-14 has the correct A/B limits78/130 and its last conditional-base argument quotients by U plus the unique fixed first line before testing the second line; rank125 plus increment6 exceeds130. P-15's full support9 proof and standalone exact determinant replay were checked separately. No off-by-one or missing transpose was found.

## Consequence and scope

Conditional only on the listed checked prolongation certificates, the verified cover proves every determinant seven-plane has border rank at least14 in characteristic zero. The anchored seven-edge construction gives a matching global minimum14. Generalized substitution then gives36-7+14=43 for the determinant4 tensor in that characteristic-zero scope. This audit does not upgrade the characteristic of the modular certificates.
