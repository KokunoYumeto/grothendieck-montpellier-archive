# Regularized one-sided Euler commutator

## What is proved

The complete proofs are in modules/regularized_strip.tex, MA-RS-001–003.

1. For almost every σ in (1/2,1), all nontrivial zeta zeros satisfy
   |σ−Reρ| ≥ cσ(2+|Imρ|)^−2. Borel–Cantelli uses the unconditional local zero count. The MT-M18 finite-disk Blaschke/Harnack argument then gives exp(C log²(2+|t|)) bounds for 1/ζ(σ+it) and each derivative.
2. On H_a = L²(exp(2ax)dx), a = σ−1/2, the weighted unitary Fourier transform V_a diagonalizes actual closed operators Z and J with multipliers A(t)=ζ_S(σ+it) and j(t)=1/A(t). Their common graph core is V_a inverse of compact smooth functions in frequency. An explicit finite Euler sum plus N^(1−s)/(s−1) counterterm realizes Z on this core. No uniform bounded inverse is asserted.
3. If g has compact support and finite Gevrey order and φ has endpoint values 1 and 0 with compact Gevrey derivative, every composition in C_g Z[J,M_φ] is defined on that core. Multiplication by φ creates Gevrey Fourier tails outside the original compact frequency support, and those tails dominate the inverse multiplier growth.
4. The actual Fourier kernel is
   i/(2π) · Mg(a+it) A(t) · (j(t)−j(u))/(t−u) · F_+(φ′)(t−u).
   It is Schwartz in both variables, hence gives a unique trace-class extension. Its diagonal is
   −(2π)^−1 Mg(a+it)(ζ_S′/ζ_S)(σ+it).
5. A justified contour shift to c>1 gives the actual trace
   P_out^+(g) − Mg(1/2) + sum_(Reρ>σ) mρ Mg(ρ−1/2).
   Reflection produces the actual paired diagonal regularization with trace
   B_out(g) − P(g) + sum_(|Reρ−1/2|>a) mρ Mg(ρ−1/2).
   The generic line and zero symmetry exclude boundary zeros.

The trace is derived from the concrete closed-operator composition and its Schwartz kernel before the residue sum is computed. It is not an operator assigned a prescribed spectral scalar.

## Critical scope boundaries

- Generic widths, not every width.
- Compact finite-order Gevrey tests and cutoff derivatives, not all compact smooth tests.
- The inverse is a closed multiplier with its specified maximal domain. Its bounded regularizations have no asserted uniform norm bound.
- The paired diagonal regularization has been constructed. The full narrow Meyer projection matrices, their off-diagonal entries, and their global-to-local intertwining domains are not identified by this proof.
- The actual trace contains crossed poles and zeros. Omitting those terms does not preserve the trace of the constructed operator.
- Compact Gevrey cutoffs have zero trace; when the one-sided trace is nonzero, trace-norm convergence from such compact-cutoff commutators is impossible. Strong convergence for the unbounded inverse compositions has not been asserted.

The logarithmic derivative is better behaved than the reciprocal itself: G′/G is polynomially bounded in the finite-disk decomposition, and B′/B is at most polynomial by the horizontal distance estimate. Therefore the scalar trace integral and residue distribution extend to all Cc-infinity tests. This observation does not prove that the actual commutator is trace class for those tests; the two-variable kernel still involves the reciprocal rather than just its logarithmic derivative.

## Sources and checks

- NT-Z10 and MT-M18, supplied GRH_NIGHT checkpoint07, work/root/block_arithmetic_synthesis.tex, M18.5–M18.9: fixed-strip polynomial bounds, local zero count, finite-disk Blaschke/Harnack lower bound and selected horizontal ordinates. The new generic-line version is proved in MA-RS-001.
- NIST Digital Library of Mathematical Functions, §25.2(iii), equation25.2.8: https://dlmf.nist.gov/25.2.E8. It states exactly the finite sum plus N^(1−s)/(s−1) minus the fractional-part integral for positive integer N and Re s>0. Its source locator is Apostol (1976), Introduction to Analytic Number Theory, Theorem12.21 and equation(25), p269. The sign and remainder bound were independently derived by Abel summation. Retrieved source reference: turn980758673view0.
- MA-MEY-001–003: prior checked wide-strip operators, actual commutator convention and reflected diagonal pair. Meyer (2005), author pp39–44, Lemmas5.3–5.6 and Theorem5.8, remains the source for those wide-space geometric maps.
- Gevrey Fourier decay is proved directly by optimizing the number of integrations by parts. Schwartz-kernel trace class and the diagonal trace are proved by an absolutely summable Hermite expansion.
- The inherited Grothendieck/nuclear-trace placement uses BR-TR-01/02, F-SM-11/12 and cote1 scans079–080 and111–112; no new scan audit is claimed here.

Author complete-proof checks are recorded in regularized_strip_events.tsv. Root independently read all three proofs and reported that they pass, including a direct source check of DLMF25.2.8. The S5 agent subsequently completed an independent whole-proof reading of all three statements and the Euler regularization, with four passing events in regularized_strip_s5_review_events.tsv. All input classes for MA-RS-001–003 are none in the A/M/outside-preprint taxonomy, with the published classical and inherited unconditional inputs retained above.

The separate MA-RS-004, regularized_smooth.tex, proves the arbitrary compact smooth extension under a fixed horizontal zero gap; the stipulated A supplies that gap for every fixed rational zeta line 1/2<σ<1. That conditional improvement does not change the unconditional generic-line scope here. The new MA-PR-001–003 constructs an actual partial return to the retained smooth Meyer subrepresentation at generic edges with Gevrey smoothing, with an actual discarded-block operator correction. It still does not identify every original off-diagonal common-space map with the unbounded inverse composition in this section.
