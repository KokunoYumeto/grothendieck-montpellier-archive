# Independent whole-proof audit: D-EX-01–03

Reviewer: /root/g34_eightfolds; GPT-6 Astra Pro; effort inherited/unexposed; HODGE_DIVISION; 2026-11-21 UTC.

**Outcome: PASS.** Audited complete proof hash `82c1ee8138d8a28ba0624f0ec452dc3a38921f44ec062dec4e47aceedf691acd`. This includes the final automatic-transitivity and projective-faithfulness paragraphs. No external classification theorem is needed.

I checked the three cases of EX.2 separately. For 2≤c≤n/2 the paired-eigenvalue estimate gives F≤c(n−2)/2 and the remaining difference is k−n/2. For c=1, the distinct eigenvalues give the required n−2 upper bound. For c>n/2, the convex endpoint estimate gives F≤(c−1)k, leaving exactly (c−k)(c−3)/2. All inequalities also cover the smallest values n=4.

For EX.3, nonreal scalar eigenspaces pair under conjugation. For scalar −1, pairing z with −1/z and grouping the two fixed labels i,−i gives the square-of-block-dimension estimate. I checked that the equality of their multiplicities is used exactly where needed.

For EX.4 I independently derived the fixed-pair-orbit identity and its subtraction of the deleted-permutation summand. The inequality k+E≥2n/3 is valid both without fixed points and with f fixed points: in the latter case E≥fk and n≤f+2k give the displayed bound. The signed opposite-pair orbit for an even cycle is correctly excluded from fixed vectors.

The uniform contradiction correctly uses Riemann–Hurwitz for the transitive permutation quotient, not an assumed branch independence. Both parity formulas for A_n imply that seven nonidentity scalar entries exceed the total budget for n≥6. Summing the two spectral bounds then gives 2m+8. The n=5 half-integrality improvement gives19>18; the n=4 nonreal scalar-product argument gives at least14>12. These inequalities precede any tuple-generation or signature sufficient-condition claim.

Irreducibility does force transitivity: an invariant line in the deleted permutation representation splits its exterior square into two nonzero invariant summands. Projective faithfulness follows because equality of all pairwise eigenvalue products in dimension at least three forces the original matrix scalar; the deleted permutation representation has no nonidentity scalar. Consequently both projections survive quotienting the kernel, and matrix product one implies the two projected product-one relations. The actual intermediate-cover variation and marked-base factorization are the same previously proved Frobenius construction, with larger scalar field retained.

I independently constructed exact Fraction eigenvalue multisets, exterior-pair sums, and signed orbit counts for every partition from n=4 through n=12. The resulting265 partitions and2394 phase checks verify the integer spectrum formula and all three inequalities, without importing the original checker. Files: `audit_exterior_square.py` and `audit_exterior_square.json`. This finite check supplements the full uniform proof and is not claimed as its replacement.
