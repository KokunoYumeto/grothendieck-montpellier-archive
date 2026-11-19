# A literal Tate-twist issue in the consulted BGV purity wording

19 November 2026. This note checks a narrow statement directly in the retained primary arXiv version 2306.05099v2. It does not refute the paper's monodromy equivalence or its final comparison theorem.

Definition 2.42(3), author page 17, requires algebraic-integer eigenvalues in its definition of a pure Frobenius module. Example 2.43(2), on the same page, defines the twist K0(n) using p^(-n) times Frobenius. Example 3.29(1), page 28, includes all integer Tate twists {n}=(n)[2n] in the Chow heart. Proposition 4.44(2), page 38, asserts the indicated purity for every object of that full heart. Remark 4.41, pages 37–38, fixes the realization of 1(-1) as K0(-1).

Take k=F2 and M=1(1)[2]. The Frobenius on K0=Q2 is the identity. Monoidality and the displayed normalization give the unique nonzero cohomology of the realization of M as Q2(1), in degree minus two, with eigenvalue 1/2. This has the expected spectral weight minus two. It is not an algebraic integer: a monic integer equation of degree m for 1/2, multiplied by 2^m, would say

\[
1+2a_{m-1}+\cdots+2^m a_0=0,
\]

which is impossible modulo two. Thus the literal integrality requirement cannot hold on the full Tate-stable heart. Dropping integrality from the spectral-weight definition, or restricting the integrality claim to an appropriately effective range, avoids this particular contradiction. A proof of every downstream comparison is not supplied here.

The C6 square-zero encoding uses the compact ind-nilpotent results in Sections 2 and 4.1–4.4, including Corollary 4.14. It does not use Proposition 4.44(2). The separate pure-local diagnostic uses the usual spectral-weight and weight–monodromy requirements, and does not require algebraic-integral roots after arbitrary Tate twists. This finding therefore does not change either written argument.

The issue was initially suggested by a secondary search result, but the definition, twist convention, heart and proposition were all checked in the retained primary text before making this claim. Primary URL: https://arxiv.org/pdf/2306.05099v2. No inference about an uninspected later correction is made.

Root independently read the actual primary Definition 2.42(3), Examples 2.43(2) and 3.29(1), Definition 4.40, Remark 4.41, and the complete Proposition 4.44 with its local proof. The variance and explicit reciprocal Tate eigenvalue passed that check. A minimal exact `Fraction` certificate is retained as `post08/code/check_bgv_twist_purity.py`, with output `post08/output/bgv_twist_purity_certificate.json`. It verifies the twist inversion, degree and spectral-weight arithmetic and the reduced denominator two; the elementary algebraic-integrality proof is given above.
