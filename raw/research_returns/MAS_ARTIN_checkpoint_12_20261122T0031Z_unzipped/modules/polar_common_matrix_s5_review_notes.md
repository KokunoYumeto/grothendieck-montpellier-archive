# Independent complete review of MA-MO-018

Date: 2026-11-21, UTC. Reviewer: GPT-6 Astra Pro, `/root/s5_audit`; effort inherited/not externally exposed.

## Result and reviewed version

**PASS.** I independently read every line of `polar_common_matrix.tex`, including its full proof and final scope, MA-MO.320–337. The stable file had 375 lines and SHA256 `9bf09d54843b0999c708bbbab4a52e755ca6c7322a2f51adcc1873feb9b2391d`. No mathematical correction was requested.

The conclusion is a trace-class endomorphism of the specified augmented common completion, under the explicit zero-free right-half-plane hypothesis with a positive margin. It is not an unconditional transport from a merely generic line. It does not establish preservation of the positive completion, compute the full matrix trace, or induce a quotient endomorphism without the separately stated outgoing-column condition.

## Independent checks

### Original inverse on every negative smooth input

The Möbius series in MO.323 converges locally with all derivatives for every `y in E`, using its rapid right decay. On a wide line it is the original norm-convergent inverse. The right-half-plane premise makes its reciprocal holomorphic throughout the shift to the positive narrow line. The pole of zeta at `z=1/2` becomes a zero of the reciprocal, so it creates no inverse residue. The fixed margin supplies polynomial reciprocal derivatives on each needed strip; above the ordinary absolute-convergence line the Euler series also gives those bounds. The entire rapidly decreasing Mellin transform of y then permits the contour shift.

I checked separately that the integral `MF_y(1/2)` is genuinely absolutely convergent: the narrow weight a controls the left end, and a wide weight greater than 1/2 controls the right end. Its value is zero. The same argument is applied to `Ry` on the positive narrow line. Neither inverse identification crosses the negative line or any unaccounted right-exterior zero.

### Actual source map and both polar coefficients

I freshly reread Meyer's defining summation inverse and `p_+` formula in `main.tex`, through its proof and the definitions of `P_+` and `P_-`. Specializing this actual map to a diagonal input gives exactly `h_y=u_y+F u_Ry`. The factor `2 sqrt(|t|)` in MO.325 agrees with the centered theta convention. The source functions vanish near zero and are Schwartz at infinity.

I revisited the bilinear moment-functional construction in MO.143–146. Its weighted step is Schwartz, and the reciprocal on the positive line has polynomial growth here. The same pairing therefore applies to every y in E after the new exact inverse identification. The zero total moment yields `integral u_y=-lambda_0(y)`, while `u_y(0)=0`. Fourier evaluation gives both MO.328 coefficients. Dilation multiplies source value and integral by `G(-1/2)` and `G(1/2)`, respectively, giving both signs and indices in MO.329.

### Separated Fourier cross kernel

I recomputed MO.331 directly. Mellin transformation of the reflected Fourier source evaluates `M(q F)(-z)`. Inserting the positive-line inverse Fourier representation produces the argument `-z-w`, not `z-w`, and the factor `1/(2 pi)`. Since `q'= -phi'`, integration by parts gives `M q(xi)=P(xi)/xi` on `Re xi<0`. Thus the displayed kernel has the correct sign and denominator. Its real part is `-2a`, which cannot vanish because a is strictly positive.

The actual sequential domain is justified on the smooth source: qF is an additive Schwartz source, its Fourier image has every local positive weight, and the final zeta multiplier has polynomial growth. The two rapid kernel variables are t and t+u; their sum controls u. All remaining derivatives are polynomially bounded. Consequently the kernel is Schwartz, and the cited Bessel/Hermite argument gives trace class for every polynomial exponent. This does not make each factor bounded on the completed Hilbert space.

### Inherited sum norm and corrected diagonal row

The physical kernel in MO.332 has the correct input sum-weight denominator and output one-sided numerator. On the bounded support of x-y its left tail is `exp(2ay)` times harmless polynomial factors, while its right tail vanishes. These statements hold after every derivative, proving a Schwartz kernel and hence trace class from H to H_a. A corresponding claim on a single unchanged one-sided space would not follow; the proof does not make one.

I checked the two actual section corrections separately. Poisson summation gives `e_0` the left tail `-exp(x/2)` and `e_1` the right tail `-exp(-x/2)`, with rapid opposite tails, so both lie in H precisely in the stated range `a<1/2`. It also gives `R e_0=e_1`. The direct theta contour formula for a general even Schwartz h is valid because its centered radial vector has all weighted Schwartz estimates for `Re z>-1/2`; the shift from a wide line crosses only the zeta pole. This establishes MO.334 even when h is not flat at zero.

Starting from `C_g Theta h_y-C_g y`, the direct pole term is `-G(1/2) lambda_0(y) p_-`. Subtracting the two actual source sections with the coefficients in MO.329 combines that term with `Theta f_1` into `e_1`. The other section produces `e_0`. The identity `Z q J-1=(phi-Z phi J)-phi` then gives exactly the signs in MO.335.

### Second row and full endomorphism

Fourier interchanges the two Gaussian sections and takes `h_y` to `h_Ry`; it also replaces g by its reflection in the dilation operator. This proves the stated reflected second row with its swapped polar coordinates. On every original smooth diagonal input, the two residual rows agree by Poisson summation after both polar coordinates are removed. The two trace-class row maps and the closed diagonal isometry therefore produce the actual H-valued trace-class map in MO.336.

The two remaining columns are actual original smooth source outputs, as proved in MO016. Adding those finite columns gives MO.337 on the exact coordinates of W. The original smooth common-sum domain is dense, proving uniqueness. The same fixed-support seminorm estimates give trace-norm continuity in g. The hypothesis also implies the horizontal gap needed for the imported MO016 positive-column theorem, using reflection of zeta zeros; hence the restriction really agrees with that existing extension.

## Source and prerequisite reading scope

Freshly read for this review: Meyer `main.tex` approximately lines 3810–3995, including the complete summation lemma proof, complete source embedding/retraction lemma proof, and defining matrices; MA-MO.143–146; MA-MO.124–129 including the graph approximation; MA-RS-004's reciprocal proof through MA-RS.36; and the direct pole-subtraction proof of MA-MO-004. The entire MO016 completion proof was read in the immediately preceding recorded MO017 review and was checked again here at its coordinate and finite-column interface. This is not a claim of a new full audit of the entire Meyer paper or of every prerequisite module.

The actual scope is stronger than a positive-column result because the complementary diagonal column is now constructed, but the outgoing condition of MO.256 remains logically separate. No new arithmetic zero-location assertion follows from this analytic construction.
