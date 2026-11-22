# Independent whole-proof audit: D-UP-01–03

Reviewer /root/g34_eightfolds, GPT-6 Astra Pro, inherited/unexposed effort, HODGE_DIVISION, 2026-11-21 UTC. Audited full proof SHA256 `5a2bcdf5ce22b61f99d235a36a559c6110c57ec8a99cd7a38cfb5021998d5314`.

**PASS.** I read and checked the entire current proof, including its generic inducing-field statement, faithful quotient, automatic transitivity, and the separate n=4 treatment.

The incidence injection is valid since a_i+a_j=0 for every pair forces all coefficients zero. The symmetric-square cancellation correctly gives Sym²Std ≅ the unordered-pair permutation module. The fixed-pair orbit count gives D1=((n−3)k−e+Q)/2; in both fixed-point cases the displayed bound2k−e+Q≥n/2 is valid.

For the nonidentity scalar inequality, I independently expanded the symmetric eigenspace estimate F≤((c+1)k+(c−5)b)/2. When c≥5, b≤c gives the residual(n+c)/2; when c≤4, dropping the nonpositive b term gives(n+c(c−4))/2≥(n−4)/2. The estimates remain valid for the identity permutation and for arbitrary scalar order. Their strict positivity correctly proves projective faithfulness for n≥5, without claiming it for n=4.

The all-degree sum uses only the actual transitive permutation quotient and Riemann–Hurwitz. For n≥11 the at least two nonreal scalar entries yield a strict excess(n−10)/2 above2m+6. The complete small-degree spectrum genuinely covers all scalar orders, since a scalar off the finite eigenvalue list has full moving rank. I independently rebuilt that list from explicit cycles of the permutation action on actual unordered pairs, then subtracted the letter-permutation spectrum:127 partitions and751 matching phases pass, with exact minimum n−3 in every degree5–10. This third construction imports neither of the original two spectrum implementations. Code/output: `audit_unordered_pair.py/.json`.

The transitivity deduction is correct: any preserved subset with both sides of size at least two supplies a proper invariant line by subtracting letter-orbit counts from pair-orbit counts; the single-fixed-letter case splits as Std_(n−1)⊕W_(2,n−1), with both summands nonzero. Frobenius gives the actual intermediate-cover variation, and its pointed-base factorization handles all base genera. The exceptional n=4 inducing degree is two and is correctly treated by the rank≤7 theorem, with no projected permutation assertion.

The finite certificate is used only for the explicitly finite small range. The inequalities prove the remaining unbounded range. No local-profile sufficiency or dimension-only dominance inference is used.
