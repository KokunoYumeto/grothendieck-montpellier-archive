# Independent complete proof review: G-28

Reviewer: GPT-6 Astra Pro; effort not exposed; `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Actual review completed: 2026-11-21 06:33:32 UTC.

Reviewed file: `work/root/g28_fragment.tex`, SHA256 `de5e7f1401fb8f65ec35c865e527482d2891fb75eb08b2914f3be61a592b4160`.

**Outcome: PASS, complete proof read and all new dimension/period cases independently checked.**

The upper determinant ring is inside R32's row range and has the required nonrectangular no-scaling point. The lower permanent ring satisfies exactly the strict q<m squared range of R33, which I independently read immediately beforehand. The proof consistently uses its actual dimension w only through w at most v; it never assumes stable points, period one, or equality with the generic-orbit upper bound.

The dimension-difference lower bound is unchanged from G27 and does not use its earlier smaller row upper bound. The identity q(m squared minus q) minus (m squared minus one) equals (q-1)(m squared-q-1) is correct and nonnegative in the stated interval, so v is positive and exceeds two. The same ambient generator and parameter-degree upper bounds apply regardless of stability of the lower ring.

If w is zero, a finitely generated nonnegatively graded domain over C with degree-zero part C has no nonzero positive-degree element: such an element would be transcendental by grading. Thus B=C as claimed. When w is positive, the actual generator-degree gcd argument of G27 gives precisely the needed upper-degree multiplier on each occurring residue. The standard Veronese has projective dimension w-1. When w is one, its projective integral zero-dimensional image over C is a reduced point, of degree one; this handles the endpoint separately from a positive-dimensional Chardin hypothesis.

For w at least one, both the degree factor and the binomial coefficient in the displayed upper bound are monotone in w, so replacing w by v is valid. The unchanged upper-ring Noether-normalization lower bound and G27's exact binomial ratio then give strict comparison at the unchanged explicit integer threshold. No equality in a rational-quotient or invariant-quotient dimension formula is used.

The below-face argument needs only upper-ring occurrence and padded vanishing. Finally r at most 2m implies r at most 2n-2 and r at most m squared for the stated m,n, so the smaller-row theorem, this boundary theorem and the strict-direction theorem combine in exactly the asserted nonrectangular range. The larger boundary range does not imply a larger strict range or a rectangular period-one statement.

No new external source was opened. This review uses the fully reviewed R32, R33 and G27 arguments and the stated earlier Pieri/dimension inputs; it makes no numerical or historical-priority claim.
