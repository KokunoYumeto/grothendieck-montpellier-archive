# C.3bk — root review of the owner-specific finite certificate

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), /root. No priority claim.

Reviewed on 19 November 2026, approximately 15:15 UTC. The complete source `agents/real_weil/code/check_C3bk_higher_product_kernel.py` was read. The retained JSON certificate's scope, inputs, all recurrence and tensor rows, endpoint matrix, original timestamps, runtime, and every one of its 91 named check outcomes were inspected. One long raw print was truncated; a subsequent bounded extraction displayed the complete list of check names and outcomes. The program was not rerun.

The original run began 2026-11-19T15:10:53.456062+00:00 and finished 2026-11-19T15:10:53.633054+00:00, runtime 0.176992202999827 seconds. It records 91 passes and zero failures. The exact recurrence is checked for r=2 through 12, with the h-coefficient matrix of determinant one. The positive top degree is (2s+1)!·3^s·4/2^s, s=r−1. These are integer calculations, so their use is not invalidated by a characteristic dividing a positive degree.

The r2/m0 matrix is the explicit block matrix with 4I_7, the anticanonical vector (3,−1,−1,−1,−1,−1,−1), and its intersection pairing. Its determinant is −3·4^6=−12288. The primitive-vector gcd is one. The r3/m1 checks retain the determinant-three integer pairing system and the independent Picard-torsion coefficients three and two, whose difference is one. Thus no reduction modulo three is being used to solve an integer system.

For s=1 through 9, the tensor of the off-diagonal unit matrices is represented by the complement permutation on 2^s indices. This is an involution with coefficient one; the finite-prime samples include 2,3,5,7,11. The arbitrary-s claim rests on the integral tensor identity in the proof, not on extrapolation from samples. The certificate hashes the earlier bj and lattice certificates and explicitly does not rerun them.

Outcome: PASS for this supporting finite certificate. It verifies specified integer identities and coefficient conventions. It does not certify Bertini, formal existence, actual-family descent, the sheaf cohomology arguments, or the theorem by computation; those belong to the separate complete proof audit in `ROOT_C3bk_INDEPENDENT_REVIEW.md`.
