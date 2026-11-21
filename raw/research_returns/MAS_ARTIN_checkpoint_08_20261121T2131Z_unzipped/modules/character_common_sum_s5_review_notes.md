# Independent complete review of MA-MO-012

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort inherited/not externally exposed; MAS_ARTIN /root/s5_audit.

**Outcome: PASS.** Read the entire stable 522-line `character_common_sum_transport.tex`, including all of the written proof, the trace identity, character applications, source placement and remaining-gate qualifications. No mathematical correction was requested. This is an independent written-proof check, not an inference from the prior route outline or the author's reported pass.

## Exact result reviewed

The actual original smoothed common-sum action, restricted to the nontrivial character theta ideal, extends to a trace-class endomorphism of its inherited Hilbert closure in the sum weight. This holds for every polynomial exponent s >= 0 in either of the stated regimes: a fixed horizontal zero gap with arbitrary compact smooth tests, or a simultaneous generic width with compact finite-order Gevrey tests. The inverse-domain statement on the entire smooth theta ideal is unconditional and does not need either regime. The theorem does not claim an action on every smooth zero-quotient class or equality with the full Meyer trace.

## Complete proof checks

1. **Finite-L division and endpoints.** The full completed-zero jets cancel the corresponding zeros of H_y/L. The remaining possible poles come from the finite-order gamma-pole locations, all on the nonpositive real axis. There are only finitely many in a fixed wider vertical strip, and their possible orders are bounded by the gamma multiplicities. A fixed polynomial clears them. The argument permits an overlap with a completed endpoint zero without silently discarding its full multiplicity.

2. **Uniform rectangle estimates.** Rechecked the exact M18 averaging choice of heights, product bound, disk Blaschke removal and Harnack estimate. The resulting polynomial reciprocal bound for the finite L-function is uniform on each chosen horizontal segment. The right Euler edge and left functional-equation/Stirling edge supply the other sides. Multiplication by the finite clearing polynomial retains arbitrary vertical decay. The maximum principle on every height rectangle, followed by Cauchy estimates on a slightly wider positive strip, gives all derivatives. This is an actual estimate, not an inference that an analytic quotient must be Schwartz.

3. **Finite deleted factors and the actual inverse.** E_S is inverted only on positive closed strips. Its infinitely many possible zeros on Re z = 0 are not included in the polynomial-clearing step. Mellin contours then shift freely for b > -1/2, producing the same F and e^(b x)F in Schwartz space. On a wide line the inverse is the absolutely convergent ideal Möbius operator. The structural-S invariant identification and the injective wide summation map show that this F is the actual local source vector, not an arbitrarily chosen lift.

4. **Literal cutoff domains.** F need not belong to the exponential Schwartz space E. The arbitrarily large positive weights nevertheless give rapid decay of every derivative at the right end; q = 1-phi removes the left end, so qF is in E. For U in E, the nonprincipal finite L-function is entire, so its literal ideal sum is again in E and has all completed-zero jets. Thus Z(phi F) = y-Z(qF) lies in the actual theta ideal. The same identity proves the maximal narrow multiplier domains, including at a line with isolated zeros, since the canceled inverse equals the Schwartz transform of F almost everywhere.

5. **Actual common-space signs and phases.** A nontrivial finite-order character has nontrivial compact restriction, so both polar characters vanish after that compact average. The source maps give F-tilde = Fourier-star F in the dual sector, with the finite-place phases retained. Applying Poisson to the actual qF and qF-tilde gives the full formula Delta_eta y = y-Q_eta y-R Q_bar-eta R y. Both components agree; subtraction is P_+^S-P_-. No unsupported archimedean Fourier involution is used, and no assumption that phi is symmetric is inserted.

6. **Both lines, both characters, exact kernel.** The completed functional equation reflects the union of the eta and conjugate-eta divisors by rho to 1-rho. Hence the stated right-edge gap or generic-distance estimate also controls the left edge. Rechecked the kernel i/(2 pi) times G_b(t) A_b(t) [j_b(t)-j_b(u)]/(t-u) times the plus Fourier transform of phi-prime. The delta part cancels and the diagonal is the ordinary divided-difference limit. Polynomial reciprocal growth in the gap case, or logarithmic-square growth in the generic case, is dominated by the appropriate two Fourier tails, with all mixed derivatives.

7. **All polynomial weights and genuine graph agreement.** The Bessel exponent r = s/2 gives the exact weighted norm, and conjugation applies Lambda_t^r Lambda_u^(-r) to the Schwartz kernel. Its Hermite expansion is absolutely summable in rank-one trace norms. For an arbitrary smooth ideal input, both u and j u are Schwartz by the division lemma. Cutting u in frequency simultaneously cuts j u; both converge in Schwartz topology. The sequential source outputs therefore converge in every required Sobolev norm. The proof never assumes that the reciprocal multiplier preserves all Schwartz functions in the generic regime.

8. **Inherited sum norm, endomorphism and trace.** Recomputed the nonsymmetric correction psi = 1-phi(x)-phi(-x), reflection of convolution and both line operators T. The diagonal embedding into H_(a,s) direct-sum H_(-a,s) is isometric. On the dense actual ideal the two outputs agree and remain in that ideal; closedness therefore gives an output in the same closed diagonal ideal. Trace-class restriction has the stated norm bound. The bounded cyclic trace is Tr_J B = Tr_bigH(T Pi_J), with Pi_J the actual orthogonal projection. It cannot be replaced by the identity. The ordinary Fredholm determinant is legitimate, but no arithmetic value is supplied by this proof.

## Source and prerequisite reading actually performed

Freshly read the invoked part of MT-M18 in `block_arithmetic_synthesis.tex`, lines 1–232, including the complete selected-height and minimum-modulus proof (M18.7–M18.9). The later block interpolation proof is a carried checked input, not newly reread for this event.

Freshly read the entire MT-M24 proof in the supplied `work/root/section.tex`, beginning at MT-M24 and continuing through (M24.9) and its proof ending. This verifies actual averaged theta image, polar conditions and topology rather than just the zero-jet formula.

Freshly read Meyer's `main.tex`, lines 3590–4037: sufficiently large S and compact invariants; the global coinvariant theorem and its displayed proof; fixed-S source identification; structure maps; summation lemma and its whole proof; the embedding lemma and its whole proof; the definitions of P_+^S and P_-; and the Poisson/common-sum identities. Imported local coinvariant, Shapiro and classical Poisson theorems were not newly proved in this check. The known later matrix-label sign issue is avoided by deriving the sign from the defining maps.

Re-read MA-CC-001 through its entire proof and the reciprocal/domain/kernel portion of MA-RS-005. The rest of the RS trace evaluation, previously independently checked, is not needed for MO012's endomorphism assertion. The cited finite-monodromy and cote 1 placement is inherited; no new source-proof audit of those categorical inputs is claimed.

No numerical experiment, new finite representation certificate, or assumed zero location was used for the independent generic-regime proof check. The use of A for Dirichlet characters and of the corresponding Hecke RH or M for the non-induced character in the gap regime is explicit.
