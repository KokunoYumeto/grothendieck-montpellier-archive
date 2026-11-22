# Whole-proof review of N-019

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS for the complete mathematical proof, with the actual-order
certificate and table arithmetic retained as explicit certified inputs.**
Read all of `maximal_scaling_globalization.tex`, equations N97–103.
This review did not replay all12996 products or re-audit N017's actual-order
certificate. The root is independently reading and replaying those data.

The row-Hermite remainder inequalities survive division by each column's
common denominator and are invariant under enlarging that denominator.
Monic pivots have the claimed leading term at both v=0 and infinity because
D=v^-2(1+v²)². Strict off-diagonal degree bounds make the other residues
zero. Thus the actual Hermite rows lie in both lattices with the required
normalized residues.

Using the actual R-basis expansion, the smallest nonzero coefficient of
an element in both lattices is a Laurent polynomial whose minimum exponent
is nonnegative and maximum exponent is nonpositive. It is a rational
constant. Subtraction and induction prove the full balanced-triple result
without requiring a bar-fixed candidate. The same triangular argument works
in every terminal GT flag.

At a current exponent a, the nonzero residue forces ord_0 f=2(a+d_i),
while infinity gives deg_infinity f+2(a+d_i)<=0. Since the minimum exponent
does not exceed the maximum, a<=-d_i. Equality forces f=1 by normalization.
The balanced lower flag gives uniqueness. The valuation argument also
excludes missing fractional exponents over Q(v); nonempty fibres require
half-integral exponents. Rational normalization of the GT lines transports
the lattices by units and changes the output only by nonzero rational
constants, as stated using N96.

Given the existing faithful actual-order GT model, exact matrix products,
common-denominator divisibility and zero Hermite remainders prove the full
table identities. Associativity comes from the faithful matrix algebra and
is not inferred from selected tests. The table sizes and the particular
coefficient D−9/2 remain certified-computation inputs to this reading.

At v=sqrt(2), D=9/2 and v−v^-1 is nonzero. A nonzero Laurent polynomial
with nonnegative coefficients is strictly positive at this positive v, so
the displayed coefficient cannot have the proposed signed factored form.
The proof correctly confines this obstruction to the selected alternative
basis, and distinguishes it from VIII's failed selection rule and from
integral mixed-characteristic basis questions.
