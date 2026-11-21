# Independent whole-proof review of the complete outer-five formula

Reviewed on 2026-11-21 by GPT-6 Astra Pro; the effort setting is not surfaced.

**Result: PASS.** I read the complete
`work/root/complete_outer_five_report.md`, (CF.1)–(CF.10) and every
following section, and inspected the complete original-partition route
in `work/root/outer_five_positive.py`. This review does not claim a
second execution of the component certificates or the root's 1708
original-partition coefficient comparisons.

## Stable and complementary module maps

The Cauchy/tensor-word comparison identifies the requested coefficient
with the Specht multiplicity in the balanced weight space, retaining
the actual permutation-matrix action. The five-horizontal-strip
argument proves every output with more than five rows has zero
multiplicity. At degree zero the balanced module is the trivial line.

For nonpositive raw order, the first-row removal has gap
\(3\lambda_2-\lambda_3-\lambda_4-\lambda_5\ge0\), so its input
is a partition. The exact invariant multiplication \(u^e\), together
with the already proved polynomial division map, retains the Specht
label. All size and balanced-weight increments agree with (CF.3).

For the complement, the exterior-column pairing and rational Young
projectors give the indicated dual module with determinant character
\(\operatorname{sgn}^{H}\). The averaged rational positive Gram
form is nonsingular and supplies an actual equivariant duality map.
The sign-twisted Specht label is therefore transposed precisely when
\(H\) is odd. Direct substitution gives
\[
(x^c,b^c,c^c,d^c,k^c_{\rm raw})
=(2b+x+3c-5k,c,b,0,b+c-k).
\]
When the last entry is negative, stable removal has exponent
\(e=k-b-c\) and leaves first gap
\(x-5e=(2b+x+3c-5k)+3b+2c\ge0\). This checks the endpoint
partition and the absence of any further sign. Choosing the smaller
raw order gives \(b+c\ge2k\) after at most one complement and
one stable removal.

## Complete providers and complexity

The three cases \(c\ge2k\), \(k\le c<2k\), and \(c<k\)
are disjoint and exhaustive. The first maps to G021 by
\(t=c-2k\). The second maps to T059 by
\[
(X,B,K,U)=(x,b-2k+c,2k-c-1,c-k),
\]
which is nonnegative and reconstructs every physical parameter.
The third has exactly G035's domain; its complete inverse routing was
independently checked in `G035_REVIEW.md`. Consequently the stated
providers leave no uncovered boundary or interior point.

Every provider's constants have their exact sign proof, and each
selector/increasing-subset construction is a literal bijection with
the associated summand. The largest order-set size is 152 and the
largest variable count is eleven. The affine changes and parity
decisions have fixed size. All coefficient evaluations use fixed
orders at most six and fixed bounded arguments in their constant
calculations, so exact arithmetic has polynomial bit complexity in
the binary input length. This conclusion uses no bound on an
input-dependent elimination procedure.

## Executable and geometric comparison

I checked the complete `partition_route`: it validates the partition
and outer label, handles overlength zero, performs the complement
with the correct original height and label transpose, removes the
stable power, and verifies the exact reconstructed shape and both
normalized inequalities. The resulting outer label is passed to the
selected provider, which supplies its own proved internal determinant
twist. There is no duplicate global twist. Degree zero routes to the
correct trivial balanced module.

The final geometric paragraph retains the actual generic-fiber Schur
class, specifies the rational projector base localization, and uses
the already proved representation/coherent-module maps. It makes no
unproved assertion of constant modular multiplicities. The remaining
varying-outer-degree requirement is stated in terms of the previously
constructed finite algebra and elimination procedure. No unresolved
gap was found in the full outer-five synthesis.
