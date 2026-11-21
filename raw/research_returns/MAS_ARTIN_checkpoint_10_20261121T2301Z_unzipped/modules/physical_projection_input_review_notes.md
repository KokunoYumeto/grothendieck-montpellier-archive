# Independent whole-proof review of MA-PI-001

Reviewer: MAS_ARTIN /root/input_audit, GPT-6 Astra Pro; inherited effort not externally exposed. Date: 2026-11-21.

**Result: passed the complete final written proof, every displayed formula MA-PI.1–31, the final source/norm qualifications, and the appended Grothendieck placement.** No mathematical correction was requested. The final reviewed file has SHA256 444ee30e883c9235b34b08941b22b24b40f449063fc38729a9e571d5a67d7f17; its last delta from the author's preceding hash was the status-only opening paragraph, which was separately reread.

## Exact scope and source interfaces

The theorem uses the corrected centered global realization in the explicitly specified symmetric norm
\[
L^2(\mathbb R,e^{2a|x|}(1+x^2)^{s/2}\,dx),\qquad 0<a<1/2,\ s\ge0.
\]
I freshly read Masullo printed/PDF pp.354–355, Definition7.3.2.3 and equations7.3.2.12–17; pp.488–489, Definition11.2.1.3 and equations11.2.1.6–8; and pp.516–517, StepII and equations12.4.1.8–10. The product-norm Fourier support and the two polar conditions are precisely the membership conditions used. Page488 instead presents an a-twisted level in its W^{s,2} realization. The new theorem correctly fixes its own adopted GP/CGP/GW metric and does not transfer orthogonal projectors by mere equivalence of norms. No additional coordinate twist is needed for that explicitly fixed theorem. It does not claim a theorem for a distinct untwisted or one-sided source metric.

The physical cutoff is exactly inverse Fourier, multiplication by a smooth norm-ball profile, then Fourier as specified by the coherent convention. I also reread MA-GA.2 and the relevant MA-CGP.2–7 source model, Poisson identity and continuity proof. The intermediate bandlimited vectors need not be flat. They are genuine admissible Schwartz PW source vectors because the ramified finite factor kills both adelic polar moments. The final finite-epsilon approximation is in the original coordinate-flat LF core.

## Mathematical checks

1. The two 2-adic residue-class integrals give \(i\chi_4(4\xi)/2\) on the exact shell \(|\xi|_2=4\). The inverse finite transform cancels its phase, leaving the exact archimedean multiplier \(\rho_Y(4|\xi|)\). Odd parity at infinity and the finite character make the two integer signs contribute equally, producing the theta factor2.
2. The sine-Mellin calculation gives the displayed \(i\Gamma_{\mathbb R}(z+1)/\Gamma_{\mathbb R}(2-z)\) with the stated Fourier convention. The logarithmic frequency power in MA-PI.10 and Plancherel factor \(1/(2\pi)\) give exactly the one-sided Gram symbol MA-PI.13. Partial summation and Stirling give its \(O(1+|t|)\) bound.
3. The odd Gaussian has Fourier phase \(-i\), which cancels the finite phase \(i\). The actual conductor4 Poisson identity gives the functional equation MA-PI.16 and hence the entire continuation \(4^{1-2b}\beta(d+iz)\beta(d-iz)\). The recurrence at negative even integers and the positive-real beta bound produce factorial growth, which contradicts the finite-order exponential-type bound of a compactly supported distribution.
4. The distributional separation argument has the right quantifier: for every prescribed cut and gap it produces suitable compact bands beyond those cuts. It does not assert nonzero pairing for every preassigned pair of bounded bands. The translated test and approximate delta give an actual smooth pair with nonzero Gram pairing.
5. The frequency dilation is unitary, its theta image is translated by \(+L\), and the rescaled symmetric weighted inner product tends to the one-sided pairing with \(b=-a\). The majorant is integrable for every \(s\ge0\). Thus nonzero pairing holds for every sufficiently large level, independently of the transition values of every permitted profile.
6. The origin removal has the exact amplitude \(\varepsilon^{3/2}\) in theta coordinates and the norm bound \(\varepsilon^{3/2-a}(1+|\log\varepsilon|)^{s/2}\). The compact smooth cutoff output converges through Fourier derivative bounds \(O(\varepsilon^{j+2})\). The profile is fixed before choosing epsilon, so no unproved uniform derivative estimate enters.

## Limits of the conclusion

The result refutes the canonical theta/physical-cutoff intertwining on genuine flat source vectors in the specified centered metric. It does not assert that the draft printed that exact equation; it identifies why the missing operator comparison cannot be supplied by that canonical map. It does not refute Gram-corrected projections, the actual nuclear source returns, a conditional scalar trace identity, or every conceivable comparison map. It uses no zero-location information. The appended Artin/local-system paragraph is consistent with the already audited inherited SGA/Deligne/cote1 locators; I did not claim a fresh reading of those inherited primary passages in this review.
