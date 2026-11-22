# Independent review of MA-PI-004

Reviewer: GPT-6 Astra Pro, MAS_ARTIN agent /root/pf26_audit.

Date: 2026-11-21.

I read the complete 650-line written proof, equations MA-PI.120–148 and both final scope paragraphs, then reread the explicit two-image clarification. Final reviewed file: imaginary_projection_obstruction.tex, 652 lines, SHA256 3c262f3640ba82efb08e479540aff8a2244812d8d2ae884197916f2d8b7b264e.

**Outcome: pass. No mathematical defect found.** The sole requested wording refinement now explicitly identifies the two smooth theta images, without asserting that an orthogonal projection of a smooth input must itself be smooth.

The subsequent status-only promotion was also read: final checked-status SHA256 e56c675a982c85225260f7c780f86c5bc4554dbad779f1d77a914aa0c1e23d27. It changes no theorem, formula, proof or mathematical scope.

## Arithmetic and original source

The choice \(S=\{\infty,\mathfrak p_3,\mathfrak q_{269}\}\) meets both the conductor/structural requirements of Definition 7.3.2.3 and the additional field-ramification hypothesis on p.514. The initially considered omission of the different prime is not used. Class number one gives the required structural condition and compact norm-one representatives by finite units and an archimedean phase. The radial archimedean factor, unit-invariant 3-adic factor, and prescribed ramified unit character therefore give the actual compact isotype.

The previous arithmetic proof gives trivial local character at 3, tame conductor exponent one at the inert prime over 269, and no descent from a Dirichlet norm character. I freshly reread the whole MA-CH-003 conductor proof and the MA-CGP-001 primitive-vector, phase and Poisson argument. In the preparatory source check for this module I directly read Masullo pp.354–355 and 514–515. The original PW source only requires the exhibited compact Fourier support and the two polar conditions; the proof uses direct membership with \(S'=S\), not an unproved equality of all finite-level ranges.

## Exact finite Fourier calculation

For \(v=\operatorname{vol}(\mathcal O_{\mathfrak p})=3^{-1/2}\),
\[
h_{\mathfrak p}=1_{\mathcal O}-4\,1_{\pi\mathcal O}
3\,1_{\pi^2\mathcal O},
\qquad
\widehat h_{\mathfrak p}
=v(1_{|\xi|\le3}-\tfrac43 1_{|\xi|\le9}
+\tfrac13 1_{|\xi|\le27}).
\]
Thus the two nonzero shells have norms 9 and 27 and coefficients \(-v\) and \(v/3\). The equality with \(3^{-3/2}h_{\mathfrak p}(\pi^3\xi)\) is exact. Inverting the individual shells gives \(h_9=1_{\mathcal O}-3\,1_{\pi\mathcal O}\) and \(h_{27}=3\,1_{\pi^2\mathcal O}-1_{\pi\mathcal O}\), whose sum is \(h_{\mathfrak p}\). The ramified 269-adic Fourier shell has norm \(q=269^2\), so the physical product norms are precisely \(9q\) and \(27q\).

I independently recomputed the inverse-shell constants and the two-term physical cutoff formula. The output retains the original ramified factor after inverse Fourier transform. Consequently each summand has both global polar moments zero, although the output need not remain coordinate-flat. The finite output decomposition is essential to the final error estimate.

## Theta, Mellin and Gram normalization

The six global units give the factor 6 in the norm-radius theta sum. The new source vector produces the exact centered filter with coefficients \(1,-4/\sqrt3,1\), hence
\[
E_3(s)=(1-3^{-s})(1-3^{1-s}),\qquad
E_3(s)=3^{1-2s}E_3(1-s).
\]
The effective reflection scale is \(Q_*=9Q=27q\), while the primitive arithmetic conductor remains \(Q=3q\). The principal-idèle relation and trivial local character at 3 remove a possible uniformizer phase; a complex rotation does not affect a radial function.

Using the norm radius \(t=|z|^2\), self-dual complex measure \(2\,dx\,dy\), and the self-dual Gaussian \(e^{-2\pi|z|^2}\), I recomputed the ratio \(\Gamma_{\mathbb C}(s)/\Gamma_{\mathbb C}(1-s)\), the continued functional equation, and the Gram symbol
\[
W_b(t)=36Q_*^{-2b}A_\psi(d+it)A_{\bar\psi}(d-it),
\qquad d=\tfrac12-b.
\]
The local Tate equation is the already supplied normalized primary interface; this review does not claim a fresh full reading of Tate's proof.

The new temperateness argument is valid without an extra vertical-growth theorem: modulating one fixed annular frequency source gives polynomial growth of each required finite collection of Schwartz seminorms; actual theta continuity bounds its Hilbert norm polynomially. Positivity of the Gram identity then gives polynomial local mass bounds for \(W_b(t)\,dt\). There is no circular assumption that this multiplier was already tempered.

## Noncompact Gram kernel and original finite witness

The entire continuation at \(z=i(n+\tfrac12+d)\) contains \(A_\psi(-n-\tfrac12)\). The exact gamma reflection identity yields growth bounded below by a constant times \(c^n(n!)^2\), since the positive-real dual factors tend to 1. This contradicts the polynomial-times-exponential bound forced by compact support of the inverse Fourier distribution. Reality of the real-axis symbol supplies Hermitian support symmetry; evenness is not assumed.

The separated test argument therefore produces actual compact high/low annuli with a nonzero Gram pairing. I rechecked its inherited finite-order distribution and approximate-delta proof. Complex dilations scale norm frequencies by \(e^L\) and theta functions by translation \(x\mapsto x+L\). The limits in both the symmetric and exact one-sided polynomial metrics have the correct factors \(e^{-2aL}L^{-s}\) and \(e^{2bL}L^{-s}\).

The low vector belongs directly to the actual PW range. The high vector is killed by every permitted physical profile. Flattening the high input near the complex origin gives the exact theta rescaling \(\epsilon Y_{g_\epsilon}(x-2\log\epsilon)\), hence errors \(\epsilon^{1-2a}\) and \(\epsilon^{1+2b}=\epsilon^{2A}\), with the stated polynomial logarithmic factors. The two fixed finite Fourier bands allow the cutoff error to converge in actual radial Schwartz space and then in theta space. A finite positive \(\epsilon\), chosen after the profile, gives the genuine original flat-source witness. The theorem does not substitute a nonflat limiting vector.

Finally, I checked the exact compact-Haar unitary in MA-PI.148, including its inverse and the distinction \(b=A-\tfrac12\). Orthogonality is transferred by this actual isometry, not by norm equivalence. The conclusion concerns the specified canonical physical-cutoff/orthogonal-projection comparison. It does not refute a different Gram-corrected map or claim that the source prints this candidate equality literally.
