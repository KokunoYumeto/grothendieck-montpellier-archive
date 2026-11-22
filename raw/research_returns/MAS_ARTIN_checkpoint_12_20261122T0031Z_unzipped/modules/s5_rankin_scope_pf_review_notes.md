# Independent review of MA-RB-011

Reviewer: /root/pf26_audit, GPT-6 Astra Pro.  
Date: 2026-11-21 UTC.  
Target: s5_rankin_scope.tex, 397 lines, SHA256
efc93d7bde23fe2ecd58916ec12d2e085ea2185e9b19be1ec39190d8ba999f5a.

## Completed written-proof reading

I read the entire written proof, including the separate exact-completion and
source-scope paragraphs, and independently checked its calculations. The proof
passes. No mathematical correction is requested.

The finite representation argument uses an actual invariant Hermitian form.
Consequently the endomorphism character is the squared absolute value of the
original character. Averaging over each inertia group gives the asserted
dimension bound, and the positive ramification-filtration weights give the
Artin conductor bound. The Frobenius coset average is valid at ramified as well
as unramified primes. If a Frobenius power lies in inertia, the coset average
contains the identity contribution; if it does not, the regular representation
contribution vanishes. This proves the coefficientwise Euler comparison with
the stated direction.

For the six-dimensional representation, the archimedean dimensions 20 and 16,
the odd-power contribution 4 at the specified prime five, and the displayed
geometric series all agree. I also freshly read the actual MA-RB-006 order
matrix and its surrounding comparison scope. Substituting that matrix into
the five-weight quadratic form gives the stated nonnegative multiplicity.
The character identity and the bounds on p/d^2 produce the strict score
inequality. The positive part is necessary when the guaranteed multiplicity
does not exceed the pole cost; it has not been omitted.

The near-one optimization is an assertion about its specified leading model.
The exact completion paragraph correctly retains the positive unscaled pole
cost. The conductor, gamma, and Euler signs alone do not imply an ordering of
the full variational minima. The actual Artin completion of End(X) is kept on
the Artin side; ramified tensor-product compatibility is not inferred from
equality of scalar standard L-factors. The inherited
conductor--discriminant locator is explicitly not presented as a fresh
monograph reading.

## Fresh primary statement checks

I opened the full primary PDFs through the available search references and
read the exact statements used for the final scope paragraph:

* Harcos, G., & Thorner, J. (2025). *A new zero-free region for Rankin--Selberg
  L-functions* (arXiv:2303.16889v6), Theorem 1.1, printed p. 3.
  <https://arxiv.org/abs/2303.16889>
* Harcos, G., & Thorner, J. (2026). *Tatuzawa's theorem for Rankin--Selberg
  L-functions* (arXiv:2508.10844v3), Theorem 1.1 and Corollary 1.4,
  printed p. 3, and Theorem 1.6, printed pp. 4--5.
  <https://arxiv.org/abs/2508.10844>

The first result gives the stated ineffective, conductor-dependent
near-one lower bound. The second supplies the stated exceptional-function
alternative and its conductor-dependent region. Theorem 1.6's exact
necessary condition for its exceptional zero is
pi tensor chi^2 = pi. A quadratic twist satisfies that condition, independently
of whether the degree is odd. These statements therefore support the
module's limited conclusion and do not establish coverage of the remaining
shared-zero interval.

This was a statement-and-interface check, not a complete independent reading
of either Harcos--Thorner proof. No arithmetic gate is recorded as closed by
this review.
