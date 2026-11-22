# Independent review of MA-MO-035

Reviewer: /root/pf26_audit, GPT-6 Astra Pro.  
Date: 2026-11-22 UTC.  
Proof: weighted_cluster_depth_sufficiency.tex, 428 lines,
MA-MO.1400--1423.  
SHA256: d773987e9202490726d2059991a4d03afb16af644efd593c5bb14905ad4a253a.

## Complete written-proof reading

I read the entire written proof in two untruncated portions and independently
rederived the new estimates and their assembly. The proof passes. No
mathematical correction is requested.

For a nonempty pole product the plus-Fourier normalization in MA-MO.1408 is
correct. When k is below p=(s+1)/2, the one-sided simplex bound is integrable
uniformly in depths and phases. For all positive depths and k>p, the gamma
ratio estimate is uniform in growing k: its upper endpoint is 2k-1 because
p>=1/2, and the central-binomial factor cancels the power of two from the
Laplace integral. The finite set with 0<2(k-p)<2 causes only a constant
depending on the fixed s. At k=p the separate integral gives exactly the
square-root logarithmic upper bound.

With m boundary factors, the convolution estimate using the integrable
positive-depth subproduct is valid without assigning exponential decay to
the boundary factors. Splitting at 1/d yields the stated power and logarithm.
The condition m<p controls the remaining tail and is explicitly a condition
on total boundary multiplicity in the window, not only individual orders.
The unlocalized empty product is correctly excluded from H^{-r}.

The canceled holomorphic factor remains polynomial when k grows
logarithmically: each uncanceled or canceled Blaschke factor costs a fixed
constant, and the complete factor count is logarithmic. The localized
H^{-r} convergence is only asserted for each fixed window. Its polynomial
uniform bound and the rapid kernel decay give summable trace-norm bounds;
dominated summation supplies the global limit without an unsupported common
window convergence modulus.

I checked the actual wide-inverse identification and the passage to the
boundary after multiplying by the smooth input. The physical inverse obtains
the required polynomial left bounds and all stronger right weights, so the
cutoff vector remains on the original local source domain. The removable
commutator is canceled before the boundary pairing, the crossed term uses
the dual reciprocal, and the closed-diagonal assembly uses the exact inherited
sum norm. It does not rely on bounded maps between entire varying-width
Hilbert spaces.

The rational two-moment formula uses bilinear Parseval with the correct
unitary Fourier factors. The total Mellin moment at 1/2 is justified on the
actual inverse and vanishes through its zeta reciprocal. Both finite polar
signs agree with the previously checked original source matrix. Full edge
retention follows from m<p, so the MO029 algebra and MO028 actual ideal trace
apply with their previously stated conventions. The finite-support
trace-norm continuity follows from finitely many kernel seminorms.

The theorem is sufficient only. It neither asserts its zero geometry for
actual arithmetic data nor treats total boundary multiplicity at least p
by the present nonoscillatory estimate. The general uncontrolled full-retention
case remains open. References to the prior A/M fixed-gap branches retain
their sector-specific scope.

## Antecedent interfaces freshly checked

I freshly reread MO030's canceled Blaschke-factor proof, whole-product
normalization, and compact partition through MA-MO.910, and MO027's
singular-input Hermite lemma, Sobolev norm identification, removable
commutator, crossed kernel and actual compatible-row proof through
MA-MO.721. These checks verify the exact interfaces used here.
They are not new complete readings of the underlying primary Meyer source.
