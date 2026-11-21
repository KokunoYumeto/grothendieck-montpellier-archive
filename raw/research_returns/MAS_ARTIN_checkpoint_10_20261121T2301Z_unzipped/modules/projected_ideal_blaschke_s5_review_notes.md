# Independent complete review of MA-MO-015 and its cross-weight interface

Date: 2026-11-21, UTC. Reviewer: GPT-6 Astra Pro, `/root/s5_audit`; effort inherited/not externally exposed.

## Result

**PASS.** I read the complete 277-line `projected_ideal_blaschke.tex`, MA-MO.230–241, including every proof section and the final scope. Reviewed SHA256: `48b722227e8173393b975b8bac83b7f8e0d5fb8e6f8fbee5ec0c7ee378afdaf6`.

I also read the entire cross-weight construction and proof in `projected_ideal_gram.tex`, MA-MO.210–214 (and continued into its finite-band setup). This is a full check of the invoked cross-weight portion, not a claimed independent check of all the later Gram estimates. That module's read-version SHA256 is `e388f17c8380c950629ec49dc4d22309b5f5001f118dc844c18bf2135386c88a`.

## Checks performed

* **Actual closure and normalization.** I revisited MA-HY's general primitive-Hecke setup, onto Mellin norm, and actual ideal-closure statement. Taking its centering parameter to be 1/2 and edges to be -a,a gives MO.233. Its conformal half-derivative factor commutes with multiplication, so it does not change the inner multiplier. The absence of edge zeros is exactly part of the two declared MO012 regimes.

* **Strip factor derivatives.** I independently differentiated `(w-w_lambda)/(w-conjugate(w_lambda))` with `w=exp(i kappa(z+a))`. On the two real boundary rays the numerator and denominator give precisely the factors `kappa sin(theta)/(cosh(kappa(t-gamma)) ± cos(theta))` in MO.235. Near the corresponding edge, derivative order j is bounded by a constant times `delta^(-j-1)`; beyond unit ordinate distance it has an exponential tail uniformly in the horizontal zero coordinate. The local O(log T) count plus the stated generic polynomial edge separation, or fixed gap, gives polynomial derivatives of the boundary logarithmic derivative. Product convergence across finite boundary segments and the recursive derivative identity then give MO.236. This is sufficient for the two-sided multiplication of the Schwartz kernel in MO.231.

* **Inherited projector.** The pointwise orthogonal projection onto the span of `(exp(ax),exp(-ax))` is exactly MO.237, including its off-diagonal entries. Unit-modulus boundary multiplication conjugates the whole diagonal projector to the ideal projector. The off-diagonal blocks do not enter the trace only because the other operator is block diagonal; they are not discarded as operators.

* **Fourier sign and coefficient.** With positive-exponential Fourier transform, the derivative rule is `F_+(f')=-iv F_+f`. The beta integral for `theta_+'` therefore yields the positive `i pi/(4a)` principal-value coefficient for `theta_+`, and its negative for `theta_-`. The trace-product projection kernel is evaluated at `(u,t)`, hence at the difference `u-t`. Pairing positive and negative differences gives the exact `+i/(8a)` odd-difference term in MO.241. The delta term contributes one half of the diagonal integral. Unimodular boundary factors cancel on that diagonal.

* **Absolute convergence.** The numerator of the odd difference has a factor v with a Schwartz majorant integrable in t near v=0. At large v the hyperbolic sine gives exponential decay. Thus the displayed correction is an ordinary absolutely convergent integral after the symmetric difference, not an undefined iterated principal value.

* **All polynomial weights.** The weight `(1+x^2)^(s/2)` in the squared norm corresponds to the unitary factor `Lambda^(s/2)` under the definition `Lambda^r=(1-partial_t^2)^(r/2)`. Thus the target/input exponents in MO.213 are correct. Bessel operators of either real order preserve Schwartz kernels, giving actual cross-weight trace-class maps. Dense smooth-ideal approximation puts both outputs in the same target ideal. The inclusion factorizations in MO.214 give trace and determinant equality by bounded/nuclear cyclicity and finite-rank approximation.

No mathematical correction was requested. The theorem's correction is not declared zero. Its own proof evaluates the projected ideal trace and retains the specified analytic regimes; a later, separately proved source return such as MO017 may identify that value with a local source trace. Nothing here proves the full quotient trace identity or removes the discarded-divisor condition.
