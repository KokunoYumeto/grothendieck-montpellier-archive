# MA-MO-030: uniformly bounded local multiplicity near an edge

## Exact hypothesis and result

Every completed centered zero is assumed to lie in |Re lambda|<=a. In a fixed band a-delta<=Re lambda<=a, the total multiplicity in every ordinate window |Im lambda-T|<=2ell is at most one fixed integer M. The condition is imposed for both dual sectors; the functional equation supplies the corresponding left-edge control. Under s>2M-1, the actual full common-space matrix extends in trace class for every compact smooth test, both for the structural nontrivial character sector and for the rational principal polar completion.

Infinitely many boundary zeros and infinitely many interior zeros tending to the edge are permitted. No zero separation or individually controlled Laurent coefficient is assumed. The bound on total local multiplicity is an additional arithmetic hypothesis, not a consequence of the ordinary O(log T) local count. No claim that it holds for the supplied characters is made.

## New proof

On a frequency interval of fixed length, factor all zeros in the slightly larger edge rectangle as one polynomial P_n. The quotient P_n/A is holomorphic on a fixed neighborhood. The finite-disk Blaschke/Harnack argument bounds it and all derivatives by a power of the height: all omitted zeros stay a fixed distance from that neighborhood, and the O(log T) remaining factors cost only a polynomial.

The full reciprocal pole product has an elementary Laplace representation. Its inverse Fourier function is a convolution of at most M one-sided exponentials, bounded in absolute value by t^(k-1)/(k-1)!. This gives a uniform H^(-s/2) bound and a uniform right-boundary limit precisely under the stated sufficient inequality. The proof estimates the product directly, so collisions and approach to the edge do not create uncontrolled partial-fraction coefficients.

A smooth frequency partition gives compactly supported boundary distributions with polynomial height bounds. The singular-input Hermite lemma from MO027 then gives trace-class bounds that decrease faster than every power after multiplying by a two-variable Schwartz kernel. Their entire infinite series converges in trace norm, including the right-boundary limit.

The original wide inverse is identified before the boundary limit. For actual smooth common inputs, the boundary transform and all its frequency-polynomial multiples lie in H^(-s/2), giving polynomial physical left bounds by a weighted local H1 estimate. This proves actual source cutoff membership and the rational total Mellin moment. A j_+=1 is established before the removable forward divided difference. The actual dual crossed kernel and both rational polar moments retain the previous source normalizations and signs.

## Actual spaces and traces

The paired rows are compared on the original smooth core at widths b>a before taking the boundary limit. Closed-diagonal completion gives the exact inherited sum norm. Rational finite source columns remain actual Schwartz-theta columns. The smoothed composition is bounded and trace class; the reciprocal alone is not asserted to act boundedly on every Hilbert input.

All boundary jets are retained because their multiplicities are <=M. The already checked all-width ideal return and relative trace algebra therefore give the evaluated trace/determinant identities of MO029. The rational raw determinant retains its two-by-two correction. The prime formulas retain the condition g(0)=0.

## Comparison and remaining question

The theorem contains MO027: choose the edge band below its interior gap and choose the window shorter than the finite distinct-edge-ordinate separations. Then M is the maximum boundary multiplicity, or zero if the edge divisor is empty.

The general case of growing near-edge counts at fixed s is not settled. Nor is the total-count condition necessary for a particular arithmetic function asserted. This is a proved sufficient class after the stated reviews, not an unconditional arithmetic conclusion.

## Checks actually completed

The author independently reconstructed the proof, wrote it, and read all 656 initial lines. The final explicit Laplace normalization, empty-product convention, dual functional-equation multiplicity sentence and display layout were then read, giving the final 666-line version. The author recomputed the disk geometry, distances of omitted zeros, uniform product Fourier estimate, translated Sobolev multiplier norms, absolute S1 series, original inverse limits, weighted H1 pointwise bound, both rational moments, source-row compatibility and full-retention scope. No defect remained.

The arithmetic analytic inputs and exact source interfaces were already freshly checked in MO027/028. This module does not claim a new full primary-source reading.

The independent input reader requested an explicit restriction of MA-MO.909 to nonempty pole products: the unlocalized empty product1 is not in H^(-r). This display-scope correction was applied and reread; the existing localized empty-product treatment was unchanged. Final667-line SHA256f4633983ffa8242aeeed8219becbf1ef293cad5bbb002666a1ce770d094cd6c2 has complete root and input-agent proof passes, recorded separately.
