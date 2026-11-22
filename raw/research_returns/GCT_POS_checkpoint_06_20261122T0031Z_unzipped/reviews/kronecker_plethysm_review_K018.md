# Independent whole-proof review of K-018

Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro; effort not exposed.  
Date: 21 November 2026.  
Status: **PASS** for the theorem as stated, concerning the full diagonal stabilizer and actual polystable tensors. No global Hilbert pole is asserted or inferred.

## Scope actually read and replayed

I read all of `deliverables/branches/kronecker/AMPLIFYING_GADGET.tex`, all of `verify_amplifying_gadget.py`, the complete K-006 doubling argument in `KRONECKER_FINDINGS.tex`, and the complete K-009 argument in `deliverables/branches/root/lift_bound.tex`. I replayed the exact certificate script successfully. It verifies the finite incidence/margin/interval data, dimensions 2, 9, 16, 23, their exact determinants and denominators, and the explicit dimension-nine fixed support and primitive character exponent. The root agent is also auditing the finite arithmetic independently.

## Gluing and the exact lattice index

The determinant multiplication proof is valid. Delete the shared boundary rows in modes two and three. In the resulting old maximal minor, the column of the edge to be removed has exactly one nonzero entry, in the shared boundary row of mode one. Its cofactor, after removing that row and edge column, therefore has determinant of absolute value the old index `d`.

In the enlarged matrix, order the old nonboundary rows first and all gadget rows last. The gadget columns vanish on the first row block. The old retained columns can meet the gadget row block at the shared mode-one row, but this is the lower-left block and does not affect triangularity. The lower-right block is exactly the gadget maximal minor. The determinant is consequently `±d d'`, as claimed; there is no omitted interaction term.

The use of this one minor as the full lattice torsion index is justified. Full column rank leaves precisely the two block-sum differences in the rational left kernel. Their primitive integral exterior product has complementary coordinates `0,±1`. All nonzero maximal minors thus have the same absolute value, and their gcd is the Smith torsion index. This also proves the enlarged columns are independent.

## Margins, positivity, and the invariant interval

The equations `Ap=256(1-b)` and `Au=256b` give margins `r` on the identified boundary and one on each newly introduced coordinate. They replace exactly the deleted old edge's mass. The strict positivity argument from the two endpoint values is correct: an affine function with nonnegative endpoint values, not zero at both endpoints, is strictly positive in the open interval.

The selected-edge map is decreasing, with exact image `(25/61,41/88)` contained in `(3/11,37/61)`. It retains the starting value `1/2` in the allowed interval. Cross-support freeness also follows exactly as stated: two shared coordinates would be boundary coordinates, and old freeness makes the deleted old edge the only old edge with that pair.

## Denominators and determinant character

For independent incidence columns, the vector solving `Aq=1` is unique. Thus `D1` lies in the incidence lattice exactly when `Dq` is integral. The least common denominator is therefore the order of the determinant-product character in the character quotient, not merely a bound on that order.

If the selected mass has denominator `D=2·256^k` and odd numerator `a`, then its successor has numerator `131D−43a`, which is odd, and denominator `256D`. Every other new mass has denominator dividing `256D`. Hence the common denominator is exactly the asserted new index. Equality between the order of this element and the entire torsion-group order proves that the torsion group is cyclic and the determinant character generates its character group. The diagonalizable stabilizer is therefore a scalar two-torus times the indicated cyclic group, with a faithful character on that finite factor.

For the intermediate dimensions, the ordinary four-edge doubling operation is applicable repeatedly. The selected mass is positive and at most one by its margin-one condition. The four replacement masses `r/2,r/2,r/2,1−r/2` are positive; a selected numerator odd at denominator `D` yields an edge of denominator `2D` with odd numerator. The relation replacement in K-006, or the same block-minor argument for the two-dimensional gadget, multiplies the lattice index by two. Thus all `n≥2`, not just `n≡2 mod 7`, are covered.

## Actual polystability and conclusion

Taking positive square roots of the masses gives reduced Hermitian matrices equal to the identity. Freeness removes every off-diagonal term. The three trace-free moment maps vanish, so the usual affine Kempf–Ness criterion proves that the `SL_n^3` orbit is closed. The argument does not rely on a support-only surrogate for polystability.

The proven diagonal character order is

`D_n = 2^(n−1+floor((n−2)/7))`.

At `n=9` it is `512`, exceeding `2^(n−1)=256`. Since the diagonal stabilizer is a subgroup of the full product stabilizer, this already disproves the proposed universal upper bound on the full determinant-character image. The theorem does not identify that full stabilizer, and the review does not upgrade it to such a claim. It also supplies no global residue or positivity/saturation-index estimate without the separate fixed-component and cancellation arguments.
