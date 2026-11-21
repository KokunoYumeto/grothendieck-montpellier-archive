# Independent complete proof review: I-34

Reviewer: GPT-6 Astra Pro; effort not exposed; /root/purity_zero_status; run CUE_GCT-20261121-purity.

Review completed and recorded: 2026-11-21T03:27:01Z.

Scope: the entire I34_prime_rank_repair.tex; I-33's divisor lemma and prime-count argument were previously read and checked in full. The author reported a typesetting repair and an explicit working-extension qualification after the initial review. No new external source or large numerical matrix computation was checked here.

**PASS.** The missing backslash in the second spacing command of (I.71) was reported and repaired; no mathematical correction was required.

- The prime supply and size bounds follow from the already checked elementary prime count. The \(\delta+1\) distinct formal powers of \(T\) are valid interpolation nodes over \(F(T)\) in every characteristic. Thus the family of prime substitutions and the family of free-coordinate cylinders are equivalent for the stated individual-degree class.
- With local nullity one, the nonzero product-value vector lies on a constant one-dimensional kernel. Its full support is essential and is correctly proved. Applying I-33 to each ratio forces every off-coordinate factor ratio to be a constant times a monomial. A free-coordinate cylinder then groups terms by the formal integer exponent; each nonempty group would be a proper kernel relation unless all exponents agree. The unique-circuit property forces those exponents to be zero, and the whole polynomial vanishes. The empty off-coordinate set when \(n=1\) is consistent.
- The induction on the number of products is valid. Choosing a local coefficient basis of rank \(r\ge2\) leaves at most \(s-r+1\) products in each coefficient polynomial. The base cases with one, two, and three products cover the small subproblems. Under local nullity \(c\ge2\), these coefficient polynomials have at most \(c+1\) terms and need at most \(c-1\) additional free coordinates, plus the chosen coordinate. The truncation by the available number of coordinates is harmless.
- Column scaling and deletion preserve the local-nullity upper bound. Applying the scalar theorem to every linear functional over the working field therefore preserves the joint coefficient span across the full family. The proof correctly avoids claiming one curve preserves the whole span.
- The displayed three-product identity was checked algebraically. Its exponent equations produce exactly the claimed base-prime cancellation, and freeing \(A\) leaves \((T^{1663}-A)(1-T^{662})\). It shows why the two-product divisor argument cannot simply be asserted for three summands.
- The rank-four example is a product of two disjoint binomials with independent equal prime sums. Every one-coordinate cylinder leaves one whole zero binomial untouched. The displayed coefficient flattening is a Kronecker product of two rank-two matrices, so the separated-product rank is exactly four in every characteristic. Two freed coordinates remove this specific obstruction.

The result gives polynomial sampling for fixed local nullity and an explicit exponent depending on the number of summands in general. It does not resolve polynomial PIT for unbounded nullity or give a Hoza decoder.
