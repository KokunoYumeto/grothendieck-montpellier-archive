# Cote 1 and the exact numerical Masullo identity over Q

Run: `/root/source_and_masullo`. Model: GPT-6 Astra Pro. Effort: not exposed. Actual clock at completed draft reread: 2026-11-20 23:42:31 UTC (2026-11-21 00:42:31 Europe/Berlin).

The complete statements and proofs are in `source_masullo_numeric.tex`. This note records the research outcome and source mapping. It supplements, rather than replaces, `source_and_masullo.{md,tex}`.

## 1. Actual archive assertions and their completed proofs

| Supplied source | Actual assertion | Result of this run |
|---|---|---|
| Cote 1, scan 079, Corollary 4 | Fredholm coefficients of a Hilbert-space trace-class operator are bounded by those of its absolute value. | F-SM-12 gives the exterior-power proof directly. |
| Cote 1, scan 079, Corollary 5 | `|det(1+zT)| <= det(1+|z||T|)`. | F-SM-12 derives it from the coefficient bound and proves entire convergence. |
| Cote 1, scans 079–080, crossed-out Theorem 2 and corollary | Summable eigenvalues, Fredholm determinant product, genus zero, trace equals eigenvalue sum. | F-SM-12 proves all of these using compact spectral theory, finite-dimensional triangularization, determinant continuity, and F-SM-11. It does not assume the desired product or Lidskii trace identity. |
| Cote 1, scans 111–112, Proposition | Coefficient domination by a genus-zero entire function, together with summable reciprocal zeros, implies genus zero. | F-SM-11 supplies a complete corrected proof, including the exact sector argument. |

Three corrections in the transcription must be kept distinct from the actual proposition. The literal interval on scan 112 is `pi/3 < theta < pi`, whereas the next asserted positive-cosine estimate requires the narrower compatible choice `pi/3 < theta < pi/2`. The rotation in scan 111 must be the conjugate of the normalized exponential coefficient. Coefficient domination gives the radial estimate `|f(z)| <= H(|z|)` for a nonnegative-coefficient majorant; it does not generally give `|f(z)| <= |h(z)|` at the same complex argument. The pair `f=1`, `h=1+z` at `z=-1` is a complete counterexample to that latter inequality. These are repaired in the written proof, not silently attributed to the source.

The genus-zero argument is short but complete. After Hadamard factorization, suppose the remaining linear exponential has positive coefficient. In a sector of half-width strictly between `pi/3` and `pi/2`, the genus-zero product must then decay exponentially. Its global minimal-exponential-type bound controls the other two rotations. Multiplying its values at the three cube-root rotations produces an entire function that tends uniformly to zero at infinity, hence vanishes identically; a product of nonzero entire functions cannot do that.

These sheets contain no xi function or arithmetic spectral-realization question. BR-TR-01/02 are arithmetic applications of their analytic framework. F-SM-11/12 also complete the specific analytic assertions present in the draft, including a theorem whose proof is crossed out. No claim is made that these classical theorems are historically new or currently open.

## 2. Exact numerical theorem supplied for Masullo over Q

Let chi be primitive of conductor q and parity a in {0,1}, let h be smooth and compactly supported on the positive reals with h(1)=0, and define

\[
\widehat h(z)=\int_0^\infty h(t)t^z\frac{dt}{t}.
\]

The archimedean distribution is exactly

\[
A_a(h)=\frac12\int_0^\infty h(t)t^{1/2}
\left(\frac1{|1-t|}+\frac{(-1)^a}{1+t}\right)\frac{dt}{t}
=\int_0^\infty\frac{e^{-(a+1/2)x}}{1-e^{-2x}}
\bigl(h(e^x)+h(e^{-x})\bigr)\,dx.
\]

The finite distribution is exactly

\[
B_\chi(h)=\sum_{n\ge1}\frac{\Lambda(n)}{\sqrt n}
\bigl(\chi(n)h(n)+\overline\chi(n)h(n^{-1})\bigr).
\]

Under the adopted Alpöge Dirichlet theorem, for every alpha>0,

\[
A_a(h)+B_\chi(h)=\delta_\chi\bigl(\widehat h(1/2)+\widehat h(-1/2)\bigr)
-\sum_{\substack{L(\rho,\chi)=0,\ 0<\Re\rho<1\\|\Re\rho-1/2|<\alpha}}
m_\chi(\rho)\widehat h(\rho-1/2).
\]

Here delta is one for the primitive trivial character and zero otherwise. Both integrals are ordinary absolutely convergent integrals; the prime-power sum is finite; the zero sum is absolutely convergent. This is an equality of continuous linear functionals on the subspace h(1)=0.

The proof in F-SM-13 is not just a reference to the abstract F-SM-02 criterion. It derives the full explicit formula using the logarithmic derivative of

\[
\mathcal L_\chi(s)=(q/\pi)^{(s+a)/2}\Gamma((s+a)/2)L(s,\chi),
\]

with all Mellin and digamma integrals computed. The classical inputs are Dirichlet continuation, functional equation, order-one completion, and zero counting. The contour argument includes an explicit choice of avoiding heights and a polynomial logarithmic-derivative bound. The conductor term is `log(q/pi) h(1)=0`; it is absent because of the actual test-function restriction. The adopted zero-location theorem then makes every positive-width strip contain the entire nontrivial zero divisor.

### Exact agreement with Masullo's notation

Masullo **L(c) is completed**, whereas L(s,chi) in the displayed formulas above denotes the finite Dirichlet series. Masullo Definition 3.2.1.2 and equations (3.2.1.2)–(3.2.1.4), p. 123, give

\[
L_{\mathrm M}(c_{\chi,s})=\pi^{-(s+a)/2}\Gamma((s+a)/2)L(s,\chi),
\qquad L_f(c_{\chi,s})=L(s,\chi).
\]

The conductor-normalized completion used in the contour proof differs by the nowhere-zero factor q^((s+a)/2). Their zero divisors are identical. Trivial finite-series zeros are canceled by the gamma factor; none is inadvertently included by allowing arbitrary positive alpha.

Use `C_Q = Zhat^times x R_{>0}`, with test `phi(u,t)=chihat(u)h(t)` and character `c_chi,s(u,t)=chihat(u)^(-1)t^s`. Masullo's measures (Definitions A.3.2.1–A.3.2.2, p. 560) give real measure dx/|x|, finite unit volumes one, and compact idele-class volume one. Thus the global measure is `du dt/t` with du a probability measure. The real local coefficient is exactly 1/2. The unramified finite shells give B_chi; every ramified shell averages to zero because h(1)=0 and the local unit character is nontrivial. Finite Fourier expansion handles every allowed Bruhat test function, not only a single isotypic test.

Consequently F-SM-13 proves **the exact numerical statement of Theorem 12.5.1.1, pp. 519–520, for Q and every allowed test function**, from the adopted Alpöge input and classical analytic facts.

## 3. Remaining geometric gate

The numerical result does not establish the missing Section 12.3 construction. The specific outstanding geometric assertion remains the decomposition of the smoothed geometric kernel into its S-local and prime-local terms, followed by a justified exchange of diagonal restriction, integration, and the local sum. Equality of independently identified numerical distributions does not prove that the manuscript's proposed kernels realize them. The Sobolev, nuclearity, quotient-map, and limiting-operator compatibilities need their own proof.

Thus there is now a positive, concrete result stronger than the earlier abstract conditional criterion: the numerical restricted-strip identity is completed over Q. The general-number-field and geometric-kernel questions remain separate.

## 4. References and verification scope

Grothendieck, A. (n.d.). Cote 1, scans 079–080 and 111–112 [supplied manuscript transcription]. All four supplied texts were read in full. Source locator is the supplied archive filename; no unseen full-cote attribution is claimed.

Masullo, A. (2026). *The music of the primes* [supplied manuscript]. Definitions 3.2.1.2 and 3.2.1.4, pp. 123–124; Theorem 12.5.1.1, pp. 519–520; Definitions A.3.2.1–A.3.2.2, p. 560; Theorem B.4.4.7, p. 623. https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf . Previously retrieved primary web refs: `turn575499152view2`, `turn466669506search3`. The numerical result is derived independently of the manuscript's unfinished geometric proof.

Iwaniec, H., & Kowalski, E. (2004). *Analytic number theory*. American Mathematical Society. https://doi.org/10.1090/coll/053 . Relevant background: Sections 4.6, 5.3, and 5.5; Theorem 5.8 is the zero-counting theorem on p. 104, not the explicit-formula theorem. DOI metadata verified in primary search refs `turn142128100search0`, `turn522158935search0`. The university-hosted PDF found at https://unina2.on-line.it/sebina/repository/catalogazione/documenti/Iwaniec%2C%20Kowalski%20-%20Analytic%20Number%20Theory.pdf contains only six preliminary/table-of-contents pages, so it did not provide a direct reading of Theorem 5.8. Publisher direct page fetch returned 403. This bounded source lookup establishes neither a primary proof check of that theorem nor any adverse conclusion about it. No complete copyrighted book is included in the deliverable.

The original analytic background is carried as established input. F-SM-11–13 were fully reread by their drafter after writing. Parent `/root` subsequently read all three complete proofs, including all equations and normalizations, and reported no gap: the sector argument and radial majorant; the noncircular Fredholm determinant and finite Riesz arguments; and the Dirichlet contour signs, Mellin inversions, digamma coefficient, archimedean parity, idele-class Haar normalization, ramified-unit averaging, and finite Fourier completeness. Those are logged as targeted whole-proof readings, not independent re-proofs or formal kernel certifications. Model: GPT-6 Astra Pro; inherited effort unavailable; run: ALPOGE_BRIDGES; local date: 2026-11-21 Europe/Berlin (report logged 2026-11-20 23:48:15 UTC).
