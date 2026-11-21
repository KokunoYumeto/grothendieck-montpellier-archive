# Independent Hardy-strip review

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro, `/root/s5_audit`; effort inherited and not externally exposed. This records a complete independent reading of the written proofs of MA-HY-001–003, followed by primary-source checks of the precise Hardy-space inputs. The mathematical checks pass with the scope stated in the module: polynomial weight zero, actual partial open-strip quotient, and no unconditional identification with the full Meyer trace.

## Exact conformal normalization: an independent verification

There is a direct verification of (MA-HY.6) after the Mellin isometry (MA-HY.4), independent of any ambiguity about Hardy conditions at the two infinite ends. Put \(L=v-u\), \(c=(u+v)/2\). The reproducing kernel of the Mellin image of

\[
L^2\bigl(\mathbb R,(e^{2ux}+e^{2vx})\,dx\bigr)
\]

is

\[
\begin{aligned}
K_\Pi(z,\zeta)
&=\int_{\mathbb R}\frac{e^{(z+\overline\zeta)x}}{e^{2ux}+e^{2vx}}\,dx\\
&=\frac{\pi}{2L}\sec\frac{\pi(z+\overline\zeta-2c)}{2L}.
\end{aligned}
\]

The integral is absolutely convergent for \(z,\zeta\in\Pi\). To evaluate it, write the denominator as \(2e^{2cx}\cosh(Lx)\) and substitute \(y=e^{2Lx}\); the resulting beta integral is \(\int_0^\infty y^{r-1}(1+y)^{-1}dy=\pi/\sin(\pi r)\), with \(0<\operatorname{Re}r<1\). The boundedness of every evaluation also follows directly from Cauchy–Schwarz with this same integral.

For \(q(w)=c+(2L/\pi)\arctan w\), choose the analytic square root of \(q'\) positive at zero. Then

\[
q'(w)^{1/2}\overline{q'(\omega)^{1/2}}
K_\Pi(q(w),q(\omega))=\frac1{1-w\overline\omega}.
\]

Indeed, the argument of the secant becomes \(\arctan w+\arctan\overline\omega\), and the cosine addition identity cancels the factors \(\sqrt{1+w^2}\sqrt{1+\overline\omega^2}\) against the two derivatives. The right-hand side is exactly the usual disk \(H^2\) reproducing kernel. Equality of reproducing kernels gives an isometry on the dense linear spans of their kernel functions, and then a unitary onto the corresponding reproducing-kernel spaces. Evaluating this unitary pointwise identifies it as \(F\mapsto\sqrt{q'}\,F\circ q\). This proves onto-ness as well as the precise normalization used in MA-HY.6.

## Main proof checks

The actual theta ideal is carried through the continuous dense inclusion of the test-function space, and then through bounded multiplication by \(\Xi(a+z)\); it is not replaced by an independently prescribed jet kernel. The singular factor is excluded on ordinary boundary arcs by absolute continuity of the representing measure, at finite boundary zeros by the polynomial order of an analytic zero, and at the two infinite ends by the selected-height lower bound. The last step compares a logarithmic lower bound of order \(-C|t|-C\log(2+|t|)\) with the hypothetical singular-atom upper bound of order \(-C'e^{\pi|t|/L}\).

The trace-class proof is valid for zeros approaching either boundary: the two strip Poisson kernels have a uniform exponential tail away from their ordinate, with no reciprocal boundary-distance factor. The Malmquist basis handles repetitions, and factorization into two Hilbert–Schmidt compressed analytic multipliers establishes trace class before the zero-sum trace is evaluated. The actual quotient resolvent square gives the premise needed by the existing ambient lift calculation. Its integration by parts retains the two graph-domain evaluations at the cusp of the exponential weight.

The final geometric statement is a limit of traces of the actual operators in the prescribed order. Only the spectral product against the cutoff is asserted to converge in trace norm. Boundary and exterior zero blocks are absent at \(s=0\), so this result does not by itself give an unconditional full Meyer transport or RH.

## Literature checks and limits of the audit

Beurling, A. (1949). On two problems concerning linear transformations in Hilbert space. *Acta Mathematica, 81*, 239–255. https://doi.org/10.1007/BF02395019. The Factorization Lemma in §7, pp.245–246, and the complete proof of Theorem I in §9, pp.247–249, were read; these pages were also visually inspected. The classical factorization ingredients named there are carried as background.

Bakan, A., & Kaijser, S. (2007). Hardy spaces for the strip. *Journal of Mathematical Analysis and Applications, 333*(1), 347–364. https://doi.org/10.1016/j.jmaa.2006.10.088. Definitions (2.1)–(2.3), Theorems 2.1–2.2 and Corollary 2.1 on pp.349–350, the conformal/Poisson setup in §3, and the complete §4 proofs of the two isomorphism theorems on pp.352–355 were read for the exact \(p=2\) application. The direct kernel calculation above independently verifies the precise special case used here. No claim is made to have newly proved all upstream classical Hardy-space results.

The proof-check event file is `hardy_strip_s5_review_events.tsv`. No changes to the author's Hardy module were required.
