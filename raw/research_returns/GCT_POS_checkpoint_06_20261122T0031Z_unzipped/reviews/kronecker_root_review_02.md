# Complete n=4 lift and pole review

Date2026-11-21; reader/root, GPT-6 Astra Pro, effort not exposed, GCT_POS.

Whole K-007 and K-008 proofs read in manuscript SHA256 `97b2ad01b78618a584c538e53f4641e21d5f9ad7b4b6b7959ed21a0fc800d731`. The degree-two graph reductions, Cauchy–Binet factor48, eigenvalue estimate, finite torus splitting, closed-orbit lift, and exhaustion of13curves were checked. No gap found.

All87,720 modulus16 certificates were checked independently with standard-library Fraction arithmetic:31,298 infeasibleχ8 cases, four positiveχ8 cases, and56,418 infeasibleχ16 cases. Coverage was checked by a separately written C++ orbit-expansion algorithm, checking307,307 normalizedχ8 triples and291,704 normalizedχ16 triples. Both exhaustive coverage runs passed. These counts use normalized character values; the branch generator counts all primitive character values before normalization.

ALPOGE_GCT P-F23 was read in its entirety, including its displayed several-component formula(P-F23g). The Koszul proof extends to a sum by graded prime filtrations. Every generic component in K-008 lies in the smooth quotient locus, and any vertex-supported scheme structure has finite length and cannot affect the simple pole. Thus the multi-component use requires no new unproved localization assertion.

Outcome: PASS for K-007 and K-008, including the actual primitive8 pole and its exact partial fraction. The conclusion is only n=4; no claim about all-n indices or numericalPH3 is inferred. The whole rational Hilbert series remains uncomputed.
