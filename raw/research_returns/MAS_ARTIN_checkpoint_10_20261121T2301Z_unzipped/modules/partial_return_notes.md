# Actual partial return: proof and scope notes

Date: 21 November 2026. Author: GPT-6 Astra Pro, MAS_ARTIN /root/input_audit; effort inherited and not externally exposed. The complete proofs are in partial_return.tex, MA-PR-001–005. Root owns integration and final persistence.

## What is now proved

For a fixed primitive unitary Hecke function, an arbitrary fixed polynomial weight exponent s≥0, and a strip whose two edges stay at least c(2+|Im ρ|)⁻² from the real part of each completed zero, compact finite-order Gevrey smoothing has an actual nuclear return from the literal Hilbert quotient into the closed smooth subrepresentation supported on its retained interior zeros. The edge condition holds at almost every pair of edges, and at almost every positive centered width.

The return is a map, constructed before any traces are compared:

- The continuous map i sends the full smooth quotient Q∞ into the actual Hilbert quotient QH.
- Qin is the closed smooth subspace whose full exterior zero jets vanish. Its restriction iin is injective with dense image.
- Sg: QH→Qin is nuclear of every positive order and has a continuous lift to the original exponential Schwartz space.
- The actual operator identities are iin Sg=Cg on QH and Sg iin=C(exp(−a·)g) on Qin.

On the full smooth quotient, Bg=Sg i is the smoothed retained operator. The discarded operator Eg=C(exp(−a·)g)−Bg is also an actual nuclear operator. Its range has zero retained jets and its exterior jets equal those of the full convolution. The two smoothing families have zero cross-products. No unsmoothed continuous projection onto either subset of zeros is asserted.

## The contour construction and its estimates

The finite block partition retains the horizontal heights h_n from MT-M18. At each block, move each strip edge inward by δ_n=δ0(2+|n|)⁻². A sufficiently small δ0 preserves exactly the interior zeros, while keeping the new vertical contours away from every nearby zero by a comparable distance. Each rectangle has uniformly bounded perimeter and width bounded below.

The finite-dimensional algebra is the quotient of holomorphic continuous functions on this inner rectangle by the ideal of full retained jets. Its norm is the quotient boundary supremum norm. This is crucial: no choice of unstable individual Hermite coordinates is used.

For h in the weighted Hilbert space, Cauchy–Schwarz bounds its Mellin transform on the inner contour by C δ_n⁻¹/²||h||≤C′(2+|n|)||h||. It therefore supplies an actual bounded restriction on QH, of polynomial norm. These restrictions jointly have zero kernel by the already proved literal closed-ideal theorem MA-WP-001.

The whole completed function Ξ, rather than a product selected only after inspecting zeros, enters the entire difference-kernel interpolation:

H_nF(z)=(2πi)⁻¹ ∮ F(w)(Ξ(z)−Ξ(w))/(Ξ(w)(z−w)) exp(τ(z−w)²) dw.

This formula matches full jets at every retained zero of the block and vanishes to full multiplicity at every other completed zero. If the prescribed class is zero, Cauchy's theorem outside the contour and entireness make the lift identically zero, so it is a well-defined linear map on the quotient algebra.

On the vertical edges the local O(log n) zero count and the n⁻² distance give a minimum modulus exp(−κ|n|−C log² n). On horizontal edges the stronger selected-height bound from MT-M18 applies. The Gaussian kernel then gives each exponential Schwartz seminorm of the lift at most exp(Cp log² n) times the quotient norm.

Compact Gevrey transforms are bounded on all these contours by C exp(−c|n|^(1/q)), q>1. That decay dominates the lift growth, the polynomial restriction norms and the logarithmic block dimensions. An Auerbach basis with square-root rescaling of that positive upper bound gives a common bounded target family and coefficients in every ℓ^p. This proves nuclearity as a topological map, not just convergence of a scalar trace.

## Actual identities and trace transport

Applying each actual retained restriction to i Sg gives the same block multiplier as applying it to Cg. The literal Hilbert kernel theorem then gives equality of the actual operators. Applying full smooth jets gives Sg iin=C(exp(−a·)g) on Qin. This also proves canonicity of the quotient-valued map despite the choices made in constructing its lift.

The same common rank-one series proves trace cyclicity:

Tr_QH Cg = Tr_Q∞ Bg = Tr_Q∞ C(exp(−a·)g) − Tr_Q∞ Eg.

The fixed-sector MT-M22/MT-M24 isomorphism carries these actual maps into Meyer's negative smooth representation. The normalization exp(−a x) is exactly the one checked in MA-HM-002. Meyer's original common-space trace additivity can therefore be applied to the full term, while the constructed exterior operator remains explicitly.

In the rational centered case and for g(0)=0, the actual ambient cutoff limit is

lim Tr(MχR Cg PG)=A0(g)+B(g)−P(g)+Tr(Eg).

This follows from actual factorization, rank-one cyclicity, Meyer geometry and MA-WP's literal ambient lift. Only after this transport is established is Tr(Eg) evaluated as the absolutely convergent sum of mρ Mg(ρ−1/2) over discarded zeros.

## What remains outside the theorem

The theorem does not remove Eg. If a discarded zero exists, a full return for all tests is excluded by MA-HM-003. The unchanged geometric identity for all tests is still the exact zero-location criterion MA-EG-001. The present result computes and transports the actual partial object.

The generic-edge hypothesis excludes boundary zeros. It therefore does not construct a return carrying MA-WP's truncated boundary modules at exceptional widths. The new MA-PR-004 proves the sharp local obstruction: if 0<r<m jets survive, a translation-equivariant return factoring the test multiplier exists on that primary block exactly when Mg and its derivatives through order min(m−r,r)−1 vanish at the boundary spectral point. In particular a nonzero constant term cannot lift. The proof computes Hom(C[z]/z^r,C[z]/z^m) as the annihilator z^(m−r)C[z]/z^m. It includes all solution classes and an explicit compact Gevrey witness with g(0)=0 and Mellin value 1. The converse is a finite-block statement; it does not supply infinite-block estimates or a global exceptional-width return.

The unregularized return theorem uses compact tests of finite Gevrey order. The available interpolation bounds do not establish the same unregularized return for arbitrary compact smooth tests at generic edges. MA-PR-005 gives actual regularized returns for every exponential Schwartz test, as detailed below.

The regularized one-sided commutator of MA-RS carries the same discarded-divisor trace, but equality of these trace corrections is not an identification with all of Meyer's original off-diagonal common-space maps. Their unbounded inverse domains remain a separate issue.

If every zero is uniformly inside the strip, MA-HM already gives the full return with polynomial lifts and all exponential Schwartz tests. The new theorem does not weaken or hide that premise; it replaces the full target by the actual retained smooth subrepresentation.

## Gaussian-regularized extension

For any g in E, convolve with the normalized Gaussian γ_ε(x)=(4πε)⁻¹/² exp(−x²/(4ε)). Its Mellin multiplier is exp(εz²), so the actual uncentered block multiplier is Mg(w−a) exp(ε(w−a)²). The proof shows convergence to g in every E seminorm, with an O(sqrt ε) bound using one additional derivative. If g(0)=0, subtract g_ε(0)b for one fixed compact Gevrey b with b(0)=1; this preserves that normalization and the E convergence.

For each fixed ε>0 the contour multipliers have positive-power exponential decay. The existing nuclear-series proof therefore constructs S_ε, B_ε=S_ε i and E_ε=C(exp(−a·)h_ε)−B_ε as actual operators with the same retained/discarded full-jet descriptions. The Hilbert convolutions converge in trace norm by MA-WP's E→S1 continuity. Independently, the full smooth traces converge through MT-M19's common rank-one block series. Their difference proves convergence of the correction traces.

No convergence of S_ε, B_ε or E_ε as maps into the smooth quotient is asserted for general g. The Gaussian regularizers are generally not compactly supported. To obtain the geometric formula for an original compact test, the proof applies Meyer's compact-test formula only to that original test after passing the full smooth trace limit; the ambient cutoff theorem is also applied only to that original test. There is no unproved common-space geometric extension to noncompact regularizers.

The final correction trace limit is subsequently evaluated as the exterior divisor sum. That scalar evaluation is separate from the construction of the actual maps and the two actual trace limits.

## Sources and checks

All arithmetic inputs are unconditional: NT-Z10's fixed-strip upper bounds and local zero count; MT-M18.5–.13's Euler lower bound, selected heights, finite-disk Harnack argument, Stirling bounds, entire interpolation and full smooth zero-jet description. The generic inner-contour adaptation, restriction norms and nuclear construction are proved in the new TeX module.

MA-WP-001 supplies the literal Hilbert closure and finite block identification. MA-WP-003 supplies the ambient trace-class lift and cutoff order. MT-M22/MT-M24, MA-HM-002 and MA-MEY.15–.16 supply the actual smooth representation and the already checked geometric trace signs.

There is no A, M, or new outside preprint premise. All constants concern one fixed character and strip. No uniformity in field, conductor or character is claimed.

The Grothendieck interpretation uses the abelian category of finite-length C[z]-modules at retained and discarded spectral points; determinant operations are over the underlying finite-dimensional complex vector spaces with endomorphism. The inherited cote 1 scan locators remain 079–080 and 111–112. No new arithmetic positivity or ℓ-adic weight realization is asserted.

Author QA checked all 43 equation tags for uniqueness and matching LaTeX environments. Root and the S5 agent independently read all of MA-PR-001–003 and reported full passes; the S5 review also reread the exact M18 synthesis and approximation-property inputs and WP's cutoff scope. The S5 agent then independently read both complete MA-PR-004–005 additions and reported passes, including the boundary affine solution set and the separate Gaussian Hilbert/full-smooth trace limits. Root has been notified that the additions are ready for its own review. The author events and questions are partial_return_events.tsv and partial_return_questions.tsv; independent S5 events are recorded separately.
