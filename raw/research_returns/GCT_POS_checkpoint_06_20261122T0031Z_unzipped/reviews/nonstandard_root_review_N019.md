# Complete root review of the maximal-scaling basis and full table

Reviewer: `/root`; model: GPT-6 Astra Pro; effort: not exposed; run: GCT_POS.
Date: 21 November 2026, completed 23:22 UTC.

**PASS for the explicitly changed selection rule.** Read the entire proof `branches/nonstandard/maximal_scaling_globalization.tex`, the complete constructor `gt_hermite_multiplication.py`, and the complete separate verifier `verify_gt_hermite_multiplication.py`. The actual-order and faithful GT-map certificates used here had already received complete proof/code readings and independent root replays in N-015/N-017.

The polynomial Hermite remainder condition is intrinsic after clearing the denominator of each GT column: both the column and its pivot are multiplied by the same factor. Monic pivot degrees give the two local lattice scalings. For an arbitrary element in the triple intersection, the first nonzero Hermite coefficient is a Laurent polynomial with order at zero nonnegative and degree at infinity nonpositive. It must be constant. Induction gives the whole balanced triple, without imposing bar invariance on candidates.

For the current fibre at exponent a, the leading Laurent exponent u equals 2(a+d_i), while the largest exponent w satisfies w+2(a+d_i)<=0. Since u<=w, a<=-d_i. Equality forces u=w=0 and residue normalization forces the coefficient one. The balanced lower flag excludes any further element with zero residue. This proves existence and uniqueness for the full external domain, including all half-integral scalings. Rational changes of representatives of the fixed GT lines only change lattice generators by local units, translate scalings and rescale the unique result by a nonzero rational constant. No saturation of the actual order is used.

## Exact table replay

After the system Python and primary Python attempts reported that python-flint was absent from their default paths, the already installed task-local dependency was used through `PYTHONPATH=/workspace/scratch/e1d2c905d8a8/runtime_nonstandard`. No dependency or certificate was changed. The independent replay completed in7.036seconds and checked all12,996 products in the nine faithful dense matrix blocks. It confirmed204,876 nonzero structure constants, degree at most8, the identity row, and the coefficient m_(1,10)^92=D-9/2. The verifier imports no constructor and performs no Hermite division.

The constructor's exact common-denominator division and subsequent triangular division compute elements of the actual polynomial order. The separate verifier checks the stored linear combinations by ordinary dense matrix products. Associativity follows from the faithful algebra embedding and is not extrapolated from a finite sample of associativity identities.

At v=sqrt(2), D=9/2 while v-v^(-1) is nonzero. A nonzero Laurent polynomial with nonnegative coefficients is strictly positive there. Hence the displayed structure constant cannot have the requested signed factored positive form, irrespective of unimodality. This is a complete obstruction for this basis alone.

The selected114-element rational-order basis and its full table are genuine completed constructions. They do not identify the basis with VIII's printed E(4), do not repair the integral nonfreeness of N-009, and do not construct a canonical dimension ring or geometric category.
