# Independent review of THETA3-A12

Reviewer: `/root/definite_bridge`, GPT-6 Astra Pro; 21 November 2026.

I read the complete saved A12 (549 lines before its final coordinate clarification) and independently reconstructed the mathematical proof. The interpolation theorem, explicit half-space input, Gaussian tail certificate, algebraic inverse after period removal, and finite prescribed-array criterion pass. The sole requested clarification concerns applying the source polynomial scalar in literal `xiN` coordinates versus a changed rational Schrödinger chart; the actual Jacobian must be retained or absorbed into the displayed row matrix. This is a coordinate-scope clarification, not a gap in the first-jet interpolation.

## Complete mathematical checks

- The half-pairing phase in A12b cancels exactly the Heisenberg cocycle after modulation followed by translation. The source idempotent need sum with its conjugate to one only on the chosen finite support. A common integer clears translation denominators and character conductors; the actual function supplies all three IsRatDatum conditions.
- At a completely split good rational prime, integral lattice modulation/translation leaves the one-dimensional local vacuum. The congruence projector is a finite character average of coefficient l1-cost one. Its support is confined to one p-adic congruence class, while all other finite factors remain unchanged.
- With support inside M^-1 Zhat^g, the rational contributing points differ from x_j by (ell^t/M) Z^g. The determinant of the x_j column matrix is (Mr)^(g-1)(Mr+sum x0_i), so a positive r can be chosen explicitly. The norm condition h>2R excludes the opposite leading point.
- The disjoint-ball count is at most (2m+3)^g. The derivative tail includes 2pi B0 times the stated polynomial factor and Gaussian. The simplified constant 5^(g+1) pi B0 h is correct; the successive-term tail ratio uses 2^(g+1) exp[-a(2L+3)]. The algorithm terminates and yields sigma_min(J_t)>=sigma0/2.
- Algebraic finite theta comparison retains c_N, the original vacuum scalar u0, and one common elliptic tangent period because the actual complete StdPair type is induced from its imaginary quadratic subfield. The inverse is A_t^-1=gamma_N J_t^-1 B, with the stated norm bound. Algebraicity is established before inversion; no numerical analytic norm is used to infer arithmetic height or saturation.
- Determinants of independent first jets have one section scalar per column. A single degree-r jet has one section scalar overall. The higher-jet statement explicitly retains the canonical connection comparison.
- The prescribed xiAt gate is equality on the actual finite support/period quotient, with the locally constant descent itself required. The final E-linear Hodge obstruction follows from injectivity of each embedding and does not prohibit unrelated finite interpolation.

## Direct source reading

I read the exact heisO, IsVacO, IsSBHalf, IsPlaceModel and IsThetaAt definitions in LocalNewformFunction.lean; the complete SplitPart.lean including StdPair and xiN; IsRatDatum and ColDat.xi/Is clauses; the complete ExistsIsThetaAtOfVac.lean, ThetaFourierSumEqSumHeisenbergTranslates.lean, GaussianReadingFiniteRationalHeisenbergTranslate.lean, DatumReadingSplitPlacesEqClassicalTheta.lean, and PureTensorOZeroEqJetP.lean. The last theorem explicitly chooses s=cK*(-delta). These are selective static source reads, not a Lean compilation or transitive dependency audit.

The cited Milne CM Proposition 7.9/Corollary 7.10 were fully read in the earlier CM-descent review. I checked Milne ANT 2020 Theorem 8.31 and Corollary 8.32 at printed p147 in the official primary PDF; the theorem states the Chebotarev input and refers its proof to the class-field notes. It gives the required infinitely many split primes, with no bound on the first prime claimed.

## Final status

The author added the explicit literal-coordinate Jacobian `C_arch`, retained the isogeny row maps, and restricted absorption into B to the established algebraic-frame/common-period comparison. I read this addition in full. The entire revised A12 passes at its stated finite-input scope. Event saved in the independent-check TSV.
