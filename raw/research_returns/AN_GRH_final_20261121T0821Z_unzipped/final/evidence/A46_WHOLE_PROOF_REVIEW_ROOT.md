# A46: root whole-proof reading

Date: 2026-11-21, completed at approximately 06:11 UTC.
Reader: GPT-6 Astra Pro; effort not exposed; AN_GRH /root.
Event type: targeted proof check. This is a separate same-model reading, not independent-model validation or formal verification.

I read the entire 290-line manuscript `A46_PRIMITIVE_SIGN_CRITERION.tex` at SHA256 `f708446fd0e7af24f61625fc6ea68bd1c019ce1dcfb132958e71d6cc3ceb3ae8`, from the complete statement through the final scope paragraph. Outcome: PASS.

The complete proof was checked as follows. The Ramanujan coefficient formula gives the faithful-conductor idempotent, and its integral multiple is invariant under all automorphisms of the cyclic group. Its actual image is consequently defined over the rational field even when the geometric deck group is nonconstant. The identity `A p_n = n A`, rather than an unjustified rationality assertion for A, kills the projected p-primary collision. The pointed cover is a permitted geometrically prime-to-p neighbourhood, and equality of full sections supplies one common lifted rational collision. The normal geometric index and core argument preserve the required prime-to-p topology.

The distinct subset products in A give exactly 2^omega(n) nonzero coefficients of signs +1 and -1. The P and Q deck orbits are disjoint, making the principal divisor reduced with simple zeros and poles. This also establishes separability in every characteristic. I checked the controlled-field induction as written and the elementary bound n>(2^omega(n)-1)^2, including s=1,2 and the s>=3 inequality. Hence the intermediate degree e is a nontrivial power of two. Faithfulness follows from the kernel dividing both n and e. Freeness follows by applying an odd-prime stabilizer to the full fibre divisor, with multiplicities, so it does not assume that the intermediate map is unramified.

The decisive fibre is reduced because every zero multiplicity of f is one. Freeness on the intermediate curve makes each original orbit inject there, so the fibre contains at most two points and e=2. The quadratic extension is separable, its unique involution commutes with G, and it exchanges the two full original orbits. Comparing literal integer coefficients on the free P orbit gives A sigma^(-j)=-A. Iterating through the odd order of sigma^j contradicts the nonzero torsion-free group ring. Integer divisor coefficients retain their signs in characteristic two. No ordinarity, elliptic quotient, or geometric rank hypothesis is hidden in this step.

The geometric corollary permits finite descent and pointing because geometric p-rank zero persists over every finite field extension. The rational criterion instead keeps its specified field, so it does not improperly extend a rational p-unit condition. The final paragraph correctly leaves universal existence of an appropriate cover unproved.

This strictly weakens the previously qualified rational primitive-factor sufficient condition and extends the geometric rank-zero sufficient condition to all positive characteristics, for odd cyclic degree prime to the characteristic. It does not supply the universal cover demanded by the requested Hooley route.

The known Poonen induction is being replaced by its exact cited applicability statement to comply with the user's citation-only rule for known results. The complete version read here remains retained in work evidence; a final delta reading is required and will be appended below.

## Final citation-only delta

Read the entire diff from f708446f to final SHA256 490219c87e7d801776092ec7974d2fb128fabdcb7af1daea9411514b9597d6eb. The sole change replaces the reproduced known induction by the exact perfect-field, equal-degree, d-controlled applicability of Poonen Corollary2.3. PASS. No new proof step changes.
