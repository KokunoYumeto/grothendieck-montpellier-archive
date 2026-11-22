# Supplementary complete-proof checks

Reviewer `/root`, GPT-6 Astra Pro; effort not exposed; run GCT_POS; date21November2026. These entries record checks completed during the run that had not yet been copied to the central event register.

## K-022

Read the entire smooth-cancellation proof and `verify_smooth_cancellation.py`, and replayed the exact verification. PASS. The fixed scheme is precisely the union of the two weight-M Plücker lines; both nonzero curves lie in smooth charts. Their moving Euler products are opposite and nonzero. The all-M numerator factorization contains Phi_M² and cancels both relevant denominator factors. The ring-property proof was also read: invariant factorization gives factoriality; the codimension-three Pfaffian resolution gives Cohen–Macaulay/Gorenstein properties; the ordinary cone resolution and projective cohomology vanishing give rational singularities. Independently read Corti–Reid Proposition2.1 and its full proof, plus the specified charts and numerator. The example has a chosen weighted grading, and does not prove tensor cancellation or bounded largest actual pole order.

## N-011

Read the complete extreme-coefficient proof and `edge_coefficients.py`, then replayed it. PASS. For delta=v+v^-1, D=delta² and L=2m+epsilon, the coefficient at v^(L-2r) is the sum of a_(m-k) times binomial(L-2k,r-k). The six listed examples reproduce their exact outer and next-to-outer coefficients. In particular F67 has a positive outer coefficient and a negative coefficient one step inward. These are explanations of inherited negative examples, not newly discovered obstructions.

## N-016 linear addendum

Read the complete direct linear implementation, equations N-76–N-77, after the earlier whole-proof check of the finite cutoff. PASS. A lexicographic candidate is tested against all possible comparator failures, each by linear bounds and a nonzero current functional. The bounded full bar-fixed space, including odd parity, has a unique normalized solution exactly when its dimension is one. The proof does not claim that every stage succeeds or that the complexity is polynomial.

## Counting consult Theorem5 and N-005

Read the full supplied `OURS_CONSULT_a157422a_COUNTING_CONSTRUCTION.md`, Theorem5 proof, in the specific place used by N-005. PASS for the abstract additive monoidal realization: left-regular matrices over the signed dimension category inherit associators, and the unit column detects independent label classes. Consequently N-005 does yield abstract composing realizations. Canonical choice, rigidity, geometric Hecke-category identification and global pair-score minimality remain additional questions. The dictionary and implications were corrected to retain this distinction.

## ALPOGE_GCT P-F33

Read the complete proposition and proof again, including all global constituents, the normality/singularity calculation, the rationality argument, and the exact period. PASS within the stated graded-ring scope. Its weighted hypersurfaces have arbitrarily large actual periods, normal rational Gorenstein singularities and fixed negative a-invariant, but strict positivity and saturation indices zero. This is the precise reason the new tensor pole theorem alone does not settle the tensor indices. The rational-singularity criterion is a cited classical input with the inherited exact source locator; this review does not claim a new full reading of that entire source paper.
