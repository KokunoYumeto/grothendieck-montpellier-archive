# Independent whole-proof audit: HD-ALT-04a/b

**Result: PASS.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, run HODGE_DIVISION, 2026-11-21 approximately 17:52–17:57 UTC.

I read the complete `research/ordinary_alternating_three_quarters.tex`. The reviewed SHA-256 is `9903e06b3603613f6193488b0cd9774d20492848541a53686fbb60a158a6e5cc`. I checked the universal argument independently and wrote a separate exact arithmetic program without importing the author's program. No TeX compilation is claimed.

## Content inequalities

The diagonal-hook proof from HD-ALT-01 applies to any upper bound on both the first row and first column. Every arm or leg has length at most (k-1); its sum of squared coordinates is at most its length times (k(2k-1)/6). Their total length is at most (n-1). Substitution of (k\le3n/4) gives exactly the claimed upper bound for the normalized three-cycle character.

The row/column content-sum bound is valid with this same (k). Cauchy's inequality (S\ge t^2/n) retains the negative term in the double-transposition formula and cancels the factor (n-3) as displayed. The resulting strict upper bound (v<9/16) is equivalent to (9n^2-109n+118>0); its value at 15 is 508 and its forward difference is (18n-100). This proves the all-degree inequality, independently of the finite enumeration.

The previously audited complete-normalizer lemma HD-ALT-03a applies to extendible and split alternating constituents and to every scalar phase. It gives (\nu(T)\ge7a/64). No reality assumption is being smuggled into this local lemma.

## Structural and period-map scope

Transitivity of the normalizer on the simple factors is explicit and used twice. Since (n\ge15), the automorphism description of (A_n) makes the shapes agree up to transpose and the alternating restriction ambiguity, so the shape condition is uniform. If a factor is self-conjugate, every factor satisfies the earlier half-size condition and HD-ALT-03c excludes the whole core. The remaining factor representations are restrictions of real Specht representations, with invariant symmetric forms. Their tensor product has a unique invariant line of such forms, so the whole finite normalizer has a bilinear multiplier character.

That multiplier is nontrivial because its being trivial would make the finite representation self-dual and its character field real. This contradicts the explicit hypothesis that the inducing character field contains the original imaginary quadratic field. Equality of the two fields is not needed.

The actual intermediate-cover factorization, rather than a dimension heuristic on the original branch space, forces genus zero and at least twelve genuine inertias. At least two inertia multipliers are nontrivial: they generate the image and their product is one. Such fixed spaces are isotropic and give the half-degree bound. Other nonscalar factor-preserving operators have the local (7/64) bound; a factor permutation has the stronger quarter bound; a nonidentity scalar moves the whole space. Thus

\[
2\lceil e/2\rceil+10\lceil7e/64\rceil\le2e+6
\]

implies (e\le64).

The precise GKT/Rasala consequence previously checked in the HD-ALT-01/03 audits excludes all nonlinear Specht degrees below (2n^3/27) except the three specified long shapes. All three have a row longer than (3n/4) for (n\ge15). Division by at most two on restriction gives (a\ge n^3/27\ge125), contradicting the budget. The theorem has no extra nonsplit determinant, inducing-field equality, or unmentioned self-duality premise.

## Independent computation and source boundary

`audit_alternating_three_quarters.py` independently checks the symbolic cancellations, the exact polynomial and its forward difference, and every partition for (15\le n\le30). It checked 28,121 partitions, of which 27,425 satisfy the three-quarter bound, including 157 self-conjugate shapes. Every exact content inequality and the displayed degree contradiction passed. The actual successful run took 0.887 seconds. The output is `audit_alternating_three_quarters.json`.

The first run rejected a structurally different but algebraically identical SymPy expression using `==`. Direct simplification gave zero; the assertion was changed to test the simplified difference. No mathematical formula, inequality, or finite input changed. This failed initial check is retained in the event log.

The published content identities, normalizer classification and low-degree theorem retain the primary-source status recorded in my earlier whole HD-ALT-01/03 audits. This audit does not claim a new reading of the complete Rasala classification proof or a new proof of that classification. The new Cauchy estimate, transitivity reduction, multiplier argument and period budget have all been checked in full.
