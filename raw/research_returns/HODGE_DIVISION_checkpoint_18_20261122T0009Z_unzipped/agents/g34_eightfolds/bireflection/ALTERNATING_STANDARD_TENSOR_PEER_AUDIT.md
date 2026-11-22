# Whole-proof audit: D-AST01–03

**PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro,
effort inherited/unexposed, HODGE_DIVISION,2026-11-21,17:28–17:30UTC.

I read the entire current `alternating_standard_tensor_section.tex`.
Reviewed SHA-256: `1985ab22f170cdd7534b4549a1c4e1515ff3a189948cf035154f3958f322e0c4`.

Every tensor-wreath trace is a product of standard permutation traces,
each in{−1,0,...,a}. If the product is negative, one factor is−1 and
there are at mostt−1 other factors of absolute value at mosta. Thus the
lower bound−e/a holds. Every power is itself in the same wreath image,
so this is an all-powers statement, not a claim just about one trace.

For a nonreal eigenvalue, its distinct conjugate has the same
multiplicitym. A power puts their real parts at most−1/2, including
order3 and even-order endpoints. Their combined trace contribution is
at most−m, while the other e−2m eigenvalues contribute at moste−2m.
Comparison with the all-powers lower bound gives the stated estimate.
This remains valid when the two powered eigenvalues coincide at−1.

The normalizer extraction is complete: intrinsic simple factors are
permuted, all factor automorphisms are implemented by standard S_n
matrices, and the residual operator centralizes the entire irreducible
core and is scalar. Hence g=λT for the actual rational orthogonal tensor
operatorT. The multiplier isλ². The proof applies the nonreal bound to
thatT at eigenvalueλ^−1, not to an arbitrarily shifted convolution.

The weaker1/a projective-support bound covers factor-preserving
operators. The already reviewed weighted tensor-cycle quarter bound
is stronger for nontrivial factor permutations in this range. Genuine
scalar inertia moves every vector. The inducing field may be larger
than the original imaginary quadratic field; the inclusion still
forces a nontrivial multiplier, since otherwise the finite inducing
representation is self-dual and has real-valued character.

The actual intermediate-cover argument excludes positive genus and
forces at least12 genuine inertia with total moving rank2e+6.
Generation and the product-one relation force at least two nontrivial
multipliers. Applying the strong bound to two entries and1/a to at
least ten others yields e≤9a/(14−a). Its strict incompatibility with
e≥a² is checked on the complete interval7≤a≤13, both directly by the
concave quadratic a(14−a) and in an independent exact seven-case
arithmetic output, `audit_alternating_standard_tensor.json`.

This is a whole-proof mathematical audit plus independent endpoint
arithmetic. I did not rerun or independently reconstruct the author's
finite20551 tensor/463 swap spectrum exploration in this event; root's
separate actual rerun is already recorded by the author. No such finite
sample is needed for the proof for arbitraryt. The Aut(A_n)=S_n input
and the weighted-cycle argument have their previously reviewed scopes.
No conclusion for n≥15 or for arbitrary shifted real spectra is asserted.
