# DET-16 independent proof check

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_spectral_bridge.

## Verdict and checked version

PASS. I read the complete final work/paper_arithmetic_kernel.tex, including the author's last clarification that reflection-even restriction concerns the inverse-square operator, and the complete work/arithmetic_kernel_sources.md. No mathematical correction is required.

Checked TeX SHA256: df767b2f80c28e0c46492a003364ced3104d6a2dd218cdaa316e15a9b192186b.

Checked source/scope note SHA256: 3c9cfe8e18f7fef97e1975649eec16aa7f757a92d234defd5d98841ef85cd26c.

The conclusion is an exact scalar-endpoint reconstruction under RH. The kernel is specified from the arithmetic prime sum; its recovered atom masses determine integer fiber dimensions, and those fibers give the ordinary Xi determinant. Its positivity criterion is itself equivalent to RH. This does not independently establish RH, identify the historical finite matrices, or show that their signed coefficients induce this positive kernel.

## Inputs independently inspected

In addition to the complete new TeX and scope note, I read:

- The corrected Lemma 2.1 and its surrounding sign explanation in Olivier Ramaré's corrigendum, cached in work/programme_sources/Ramare_Corrigendum_PsiTildeSimple_Acta.txt, pp. 1–2.
- STEP6-02 and its whole proof, and STEP6-03 including the whole global one-sided Landau proof, in work/paper_weil_bridge.tex.
- The complete work/paper_resolvent_bridge.tex, including the direct scalar Mellin calculation and the determinant normalization.
- B-01 and its whole proof in work/paper_core.tex.
- The complete DET-15 Bessel-projector proof and the exact source exports during the preceding independent DET-15 check. That prior check is recorded separately in work/bessel_projector_independent.md and its events file.

This check uses the stated classical completion, zero-count and genus-zero product facts. The new section supplies direct proofs for its atomic cyclic construction. This is a mathematical/source-text review, not a Lean replay or a recursive certification of imported representation-theoretic results.

## 1. Corrected explicit formula and arithmetic normalization

Write

\[
G_\zeta(X)=\sum_{n\le X}\Lambda(n)(X/n-1)-X\log X+(1+\gamma_E)X
\]

and

\[
b(X)=\log(2\pi)-\sum_{n\ge1}\frac{X^{-2n}}{2n(2n+1)}.
\]

The corrected Ramaré formula is

\[
\widetilde\psi(X)=\log X-\gamma_E+\frac{\psi(X)-X}{X}
-\sum_\rho\frac{N_\rho X^{\rho-1}}{\rho(\rho-1)}
+\frac{b(X)}X.
\]

Multiplying by X and using the ramp identity
\(\sum_{n\le X}\Lambda(n)(X/n-1)=X\widetilde\psi(X)-\psi(X)\)
gives exactly

\[
G_\zeta(X)-b(X)=\sum_\rho\frac{N_\rho X^\rho}{\rho(1-\rho)}.
\]

The sign is correct. The sum runs over distinct zeros with the displayed multiplicities; it is not a sum over an already repeated list with an additional multiplicity factor.

At a prime-power endpoint the two jumps in the ramp cancel. The bounded correction follows from the corrigendum's integral formula by expanding the logarithm and Tonelli. At X=1,

\[
\sum_{n\ge1}\frac1{2n(2n+1)}=1-\log2,\qquad
b(1)=\log(4\pi)-1,
\]

so

\[
G_\zeta(1)-b(1)=2+\gamma_E-\log(4\pi)=2\lambda_1.
\]

There is no missing constant, half-weight, or factor of two.

Dividing by \(e^{t/2}\) for \(t\ge0\), then using functional-equation reflection, gives

\[
k(t)=\sum_\rho
\frac{N_\rho e^{(\rho-1/2)t}}{\rho(1-\rho)}
=2\operatorname{Tr}(C\cos(tA)).
\]

Reflection makes this even and conjugation makes it real. Reciprocal-denominator summability and \(|\Re(\rho-1/2)|<1/2\) imply absolute local uniform convergence for all real t. The cosine operator is bounded for each fixed t even before RH, because all \(\gamma\)'s lie in the horizontal strip \(|\Im\gamma|<1/2\).

## 2. Positive type, boundedness and RH

Under RH, the signed atomic measure is

\[
\mu_K=\sum_{\gamma>0}
\frac{m_\gamma}{\gamma^2+1/4}
(\delta_\gamma+\delta_{-\gamma}).
\]

Here \(\gamma\) is a distinct positive ordinate. It has total mass k(0), and the positive-frequency half has mass k(0)/2. The absence of a central Xi zero excludes an atom at zero.

Its Fourier representation proves positive type by the integral of the squared modulus of a finite exponential sum, and gives \(|k(t)|\le k(0)\). Conversely, the two-point Gram matrix gives the same bound whenever the kernel is positive definite.

For a merely bounded k, the exact arithmetic definition gives
\(|G_\zeta(X)-b(X)|\le M\sqrt X\), hence an eventual global lower bound for \(G_\zeta\) of order \(\sqrt X\). The STEP6-03 lemma with \(\theta=1/2\) then excludes every zero to the right of the critical line. Reflection excludes those to the left.

I checked the full Landau argument used here. The Mellin transform has nonzero residue
\(m/[\rho(1-\rho)]\) at a nontrivial zero; its apparent pole at 1 cancels. It is analytic near every positive real point: the alternating eta series excludes real zeros in (0,1), and the Euler product excludes them above 1. After adding the eventual nonnegative error bound, the Laplace transform of a nonnegative function cannot be regular at its finite convergence abscissa. The supplied Taylor/Tonelli proof establishes that fact. Meromorphic uniqueness then rules out poles in the asserted half-plane. This is a valid global eventual bound argument. It does not convert the source's weighted-character power-window estimates into such a bound.

## 3. Exact Weil Gram form

For \(q_t(x)=e^{-t/2}\mathbf1_{(0,e^t]}(x)\),

\[
\mathcal Mq_t(s)=e^{(s-1/2)t}/s.
\]

With the stated conjugate-linear-first convention, direct multiplication gives

\[
\overline{\mathcal Mq_u(1-\bar\rho)}
\,\mathcal Mq_v(\rho)
=\frac{e^{(\rho-1/2)(v-u)}}{\rho(1-\rho)}.
\]

Thus the defined Weil form has Gram matrix \(k(v-u)\). Absolute convergence holds on the finite test span; reflection-conjugation gives Hermitian symmetry. Under RH it is the sum of absolute squares of the Mellin values.

For \(X=e^t\) and \(a=X^{\eta-1/2}\), the actual two-indicator test is \(q_0\pm a q_{-t}\). Its quadratic value is

\[
k(0)(1+a^2)\pm2ak(t)
=2\lambda_1(1+X^{2\eta-1})
\pm2X^{\eta-1}(G_\zeta(X)-b(X)).
\]

The center, both factors of two, and the signs agree with STEP6. Calling this a specified candidate form rather than the undefined historical W is accurate.

## 4. Atom recovery and integer multiplicity

For any finite positive measure representing k, Fubini on a finite time interval transforms the Cesàro coefficient at \(\lambda\) into the integral of

\[
\frac{\sin(T(x-\lambda))}{T(x-\lambda)}.
\]

This function has modulus at most one, equals one at \(x=\lambda\), and tends to zero elsewhere. Dominated convergence therefore recovers precisely the mass of that atom.

The same calculation proves uniqueness among finite positive representing measures: the recovered atoms already have combined mass k(0), which is the total mass of any such measure. No continuous remainder is possible.

The formula

\[
a_K(\lambda)=\lim_{Y\to\infty}\frac1{\log Y}
\int_1^Y
\frac{G_\zeta(X)-b(X)}{X^{3/2}}
\cos(\lambda\log X)\,dX
\]

has the correct normalization. Evenness converts the symmetric time average to \(T^{-1}\int_0^T\); the substitution \(X=e^t\) supplies the factor \(X^{-3/2}\). No extra factor two remains.

The identity
\(m_K(\lambda)=(\lambda^2+1/4)a_K(\lambda)\)
recovers a positive integer because the exact explicit formula identifies the measure. Arbitrary positive-definite kernels do not have this integrality property. The paper makes this dependence explicit. The recovered support is discrete and bounded away from zero by its identification with noncentral Xi zeros.

## 5. Cyclic Hilbert model and ordinary trace

The explicit map of the abstract symbols to \(e_t(x)=e^{ixt}\) in \(L^2(\mu_K)\) is isometric. For every atom, the strong averaged exponential tends to its indicator in \(L^2\), by the same sinc calculation. The vector integrals exist since finite mass gives norm continuity. Atomic indicators span a dense subspace. This proves the required surjectivity without an unproved general representation theorem.

Multiplication by \(e^{ixt}\) is strongly continuous by dominated convergence. The generator with maximal domain \(\int x^2|h(x)|^2d\mu_K<\infty\) is selfadjoint by its normalized atomic basis and the adjoint-domain test.

The central distinction is correct: there is one Hilbert dimension at each distinct signed atom, regardless of its mass. Consequently the positive-frequency cyclic inverse-square determinant includes each distinct positive ordinate once. It equals G exactly when every zero is simple. Trace class follows from

\[
\sum_{\lambda>0}\lambda^{-2}
\le\sum_{\lambda>0}m_K(\lambda)\lambda^{-2}<\infty.
\]

The reflection-even inverse-square restriction gives the same reduced product; the full signed cyclic model gives its square. The signed generator itself exchanges parity. The final wording now explicitly makes that distinction for the restored model as well.

The diagonal mass operator \(D_K\) is trace class because its ordinary eigenvalue sum is \(\sum_{\lambda\ {\rm signed}}a_K(\lambda)=k(0)\). Thus \(k(t)=\operatorname{Tr}(D_KU_t)\). This does not identify atom mass with spectral dimension: an ordinary trace of \(f(A_{\rm cyc})\) has one term per distinct signed atom.

## 6. Restoring all fibers and the two determinants

Giving each positive atom a fiber \(\mathbb C^{m_K(\lambda)}\) restores the algebraic zero multiplicities. If \(\lambda_0=\inf\Gamma_K>0\),

\[
\operatorname{Tr}C_K=\sum_{\lambda>0}a_K(\lambda)=k(0)/2,
\]

and

\[
\operatorname{Tr}B_K
=\sum_{\lambda>0}a_K(\lambda)
\left(1+\frac1{4\lambda^2}\right)
\le
\left(1+\frac1{4\lambda_0^2}\right)\frac{k(0)}2.
\]

These are positive diagonal operators, so the displayed sums are their trace norms; summable eigenvalues are not being used to infer trace class for a nonnormal operator. The bound \(\|C_K\|<4\) justifies the bounded inverse in
\(B_K=C_K(I-C_K/4)^{-1}\).

The full-multiplicity genus-zero product yields \(\det(I-wB_K)=G(w)\). The spectral transformation gives

\[
\det(I-vC_K)=\frac{G(v-1/4)}{G(-1/4)}.
\]

With \(v=s(1-s)\), evenness of Xi and \(\xi(0)=1/2\) give exactly \(2\xi(s)\). The factor two is correct.

Retaining both signs gives determinant \(G^2\). The vector with every coordinate equal to \((\lambda^2+1/4)^{-1/2}\) has the correct signed matrix coefficient and only one cyclic line per signed fiber. Taking one sign, or the reflection-even restriction of the inverse square, recovers \(B_K\). No simplicity assumption is hidden here.

## 7. Transfer to the actual Bessel projections

The new corollary retains the hypotheses of DET-15 and uses its fixed, actual orthogonal source projections. The arithmetic atom contributes m separate lines, each of weight

\[
\beta=\frac{a_K(\lambda)/m}{1-a_K(\lambda)/(4m)}
=\frac{a_K(\lambda)}{m-a_K(\lambda)/4}
=\lambda^{-2}.
\]

The denominator is positive, and the full repeated sequence is summable by the preceding trace bound. Mapping the standard fiber basis to the selected orthonormal Bessel vectors identifies the resulting operator with \(B_K\oplus0\). Hence its positivity, exact trace-norm tails and determinant G follow on that actual fixed Hilbert model.

Every finite weighted sum is the bounded extension of the source convolution with the stated finite kernel sum. The limiting measurable kernel and trace-norm convergence use DET-15; the corollary does not assert a new convergence theorem for a single group convolution kernel.

Using just one projection of weight equal to the atom mass would instead have positive-half trace k(0)/2, whereas \(B_K\) has strictly larger trace. Using one reciprocal-square weight per distinct positive atom would yield the reduced determinant if multiplicities occur. The paper correctly separates both mistakes from the required fiber construction.

## 8. Scope and remaining gate

The arithmetic definition of k requires no input enumeration of zeros. The spectral identification, positivity under the stipulated RH, and recovered integrality nevertheless use the explicit formula and the zero theory. Infinite Fourier averages are definitions and existence statements; no finite numerical recovery algorithm is claimed.

The spectral Hilbert realization is determined up to unitary fiber choices. Its embedding into the Bessel model depends on the chosen source vectors. This does not provide a canonical arithmetic embedding or identify historical period matrices.

All requested checks pass with these stated dependencies. The conclusion belongs to the analytic trace-class and exterior-power framework. It is not an arithmetic cohomology or Frobenius construction.

