# A19 and A20: independent complete-proof checks

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed;
/root/effective_galois.

## A19: PASS

Complete source read:
work/gt_certificates/positive_rank_theta/A19_FINITE_SUPPORT_THETA.tex

SHA256:
ed23fcccd3578b2a8d3d734362d70d5ca8aef5fc32fe7b0e5ed178a92a066e4a.

The full proof, explicit algorithm and final [3]Theta reformulation were checked.

The genus-two intersection bound follows directly from two distinct effective
degree-two divisors in the same class: their class must be canonical, and the
degree-one residual divisor is unique. Thus a nonzero difference has at most two
ordered point representations, in every characteristic.

The exact powering identity is valid, rather than merely equality up to an
invertible matrix. If (U-1)v has order ell^s and N=ell^(s-1), every higher
binomial term has valuation at least
(s-1-v_ell(j))+(j-1)>=s. This includes the tight case ell=3,j=3.
The residual translation has exact order ell and is fixed by U.

For several primes, each congruence-kernel action has prime-power order.
A power prime to the selected ell kills all other component orbits while
preserving nontrivial motion in the selected component. The powering lemma
then gives a full ell-point translation orbit on theta, contradicting the
two-point intersection bound. Thus every S-primary theta point is fixed by
the stated Frobenius power.

The explicit GL4 exponent, resultant sign, finite S-part integer N_S and
terminating enumeration all check. No rational basepoint is needed: B itself
is a rational degree-one line bundle defining the theta embedding.
The empty-prime-set convention is consistent.

For q unequal to three, a nonzero order-q point on [3]Theta lifts to a theta
point of order q or 3q, and conversely. This is an exact equivalence, but
does not supply such a point. The Poonen theorem's extra multiplier is not
silently removed. The inaccessible original Boxall theorem is explicitly
not a premise of the complete elementary proof.

The parent independently reported a complete A19 proof read PASS.

## A20: PASS

Complete source read:
final/proof_sources/no_three_power_theta.tex

SHA256:
ce952867826b57ea53011da24fc886a899e6505cf4d1b981b9befb1cd9d5b798.

The characteristic polynomial is also justified by the explicit F2 and F4
counts in A09. Polynomial divisibility modulo three and Cayley–Hamilton
make all 3^4 geometric points of J[3] rational over F_(2^20). The exact
Jacobian order has 3-adic valuation four, so its entire rational 3-primary
subgroup is already J[3]. A19 places all geometric 3-power theta points in
that field. A10 excludes nonzero order-three points, and the effective
Raynaud line bundle gives the origin on theta. This proves equality with
{0}, and genuinely excludes every positive power of three.

Independent numerical check:
A20_recurrence_check.py and A20_recurrence_check.json.
The script uses only the Python standard library and imports neither of
the parent's programs. It uses Newton power sums, not their companion
determinant or polynomial resultant:

- s20=-287;
- s40=143809;
- second Weil coefficient over F_(2^20)=-30720;
- #J(F_(2^20))=1099812538656;
- 3-adic valuation four and cofactor13577932576 congruent1 modulo3.

It independently multiplies the displayed quotient polynomial modulo three
and verifies P(T)Q(T)=T^20-1. The actual run returned PASS.
This is exact arithmetic and mathematical proof checking, not formal
proof-assistant verification.
