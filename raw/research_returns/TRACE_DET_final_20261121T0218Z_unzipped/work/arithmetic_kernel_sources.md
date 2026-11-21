# DET-16 source and scope notes

Date: 2026-11-21. Author/checker: GPT-6 Astra Pro; effort not exposed; TRACE_DET_20261121 /root/masullo_bridge_check.

## Exact inputs inspected

1. Read all of work/paper_weil_bridge.tex. STEP6-02 defines the actual prime-sum scalar

\[
G_\zeta(X)=\sum_{n\le X}\Lambda(n)(X/n-1)-X\log X+(1+\gamma_E)X
\]

and its explicit correction

\[
b(X)=\log(2\pi)-\sum_{n\ge1}\frac{X^{-2n}}{2n(2n+1)}.
\]

The corrected explicit formula there gives \(G_\zeta(X)-b(X)=2\sqrt X\,\operatorname{Tr}(C\cos(A\log X))\). Its primary source is the previously inspected Ramaré corrigendum, corrected Lemma 2.1, pp. 1–2, cached as work/programme_sources/Ramare_Corrigendum_PsiTildeSimple_Acta.txt. The original article's uncorrected signs are not used. STEP6-03 supplies a fully proved global one-sided Landau lemma.

2. Read all of work/paper_resolvent_bridge.tex. DET-11 fixes \(C=B(I+B/4)^{-1}\), the reverse transform \(B=C(I-C/4)^{-1}\), and \(\det(I-s(1-s)C)=2\xi(s)\). DET-16 preserves the same normalization. The source scalar is Formalism/StatementOC.lean, lines 11–13; the already-checked scalar Mellin transform is the source statement mellin_Gchi_modOne and its poleData change of variable cited in DET-11.

3. Read B-01 and its full proof in work/paper_core.tex. The target operator uses one representative of every +/- pair, with full multiplicity, and determinant \(G(w)=\Xi(\sqrt w)/\Xi(0)\). The classical input includes no central Xi zero, discrete nontrivial zeros, reciprocal-square summability and the normalized genus-zero product.

4. Read all of work/paper_bessel_projector.tex and work/paper_period_frame.tex. The corollary in DET-16 retains every Std, Side, IsEll, quotient-measure, measurable-domain and representation-theoretic hypothesis of DET-15. It uses its proved fixed orthogonal source projections and its trace-class convolution-sum theorem. No independent re-proof of their imported representation-theoretic source theorems is claimed here.

## What is proved directly in the new section

The proof is saved in work/paper_arithmetic_kernel.tex. It establishes:

- The exact arithmetic definition and all normalization constants of the even kernel.
- Positive type iff RH, with the converse reduced to the previously fully proved global Landau lemma.
- Its exact Gram realization on normalized dilations of the indicator function, using an explicitly defined conjugate-linear-first Weil form.
- A self-contained atomic cyclic/GNS construction, including density of the exponential orbit, strong continuity and the maximal diagonal selfadjoint generator.
- Recovery of every atom by a Cesaro Fourier average, uniqueness among finite positive representing measures, and arithmetic formulas for its mass.
- Recovery of the integer multiplicity from the mass using the classical explicit formula.
- The reduced multiplicities of the cyclic space and the distinction between vector-state weights and ordinary operator trace.
- The full-multiplicity Hilbert reconstruction, trace bounds, spectral transform and ordinary Xi determinant.
- The exact repeated weights these reconstructed data assign to the actual source Bessel projections.

The cyclic construction from a positive-definite function is standard. The section gives the complete proof of the specific atomic case rather than claiming novelty or relying on an unproved general GNS/Bochner theorem.

## Key factor and multiplicity checks

With \(t=\log X\),

\[
k(t)=X^{-1/2}(G_\zeta(X)-b(X))
=2\sum_{\gamma>0}\frac{m_\gamma\cos(\gamma t)}{\gamma^2+1/4},
\qquad k(0)=2\lambda_1.
\]

Each signed atom has mass \(a(\pm\gamma)=m_\gamma/(\gamma^2+1/4)\). Thus the positive-frequency total mass is \(\lambda_1\), not \(2\lambda_1\).

For \(q_t(x)=e^{-t/2}\mathbf1_{(0,e^t]}(x)\), the original two-indicator test is \(q_0\pm X^{\eta-1/2}q_{-\log X}\). Its quadratic value is \(k(0)(1+a^2)\pm2a k(\log X)\), reproducing exactly STEP6's sign and factor 2.

The cyclic \(L^2(\mu_K)\) space has one dimension per distinct signed atom, independently of its mass. Its positive-frequency or reflection-even inverse-square determinant is the simple-zero product. Its full signed inverse-square determinant is the square of that reduced product.

The restored positive-frequency space has a fiber \(\mathbb C^{m_\gamma}\) for each positive atom. Its inverse-square determinant is the full \(G\). The restored full signed space has determinant \(G^2\). These spaces must not be conflated.

The signed generator exchanges reflection-even and reflection-odd subspaces. The reflection-even half used for the single determinant is an invariant subspace of its inverse square, not of the signed generator itself.

For Bessel projections the correct repeated weights are

\[
\beta=\frac{a/m}{1-a/(4m)}=\gamma^{-2},
\]

one on each of \(m\) orthogonal source lines. Taking one line of weight a per atom, or one line of weight \(\gamma^{-2}\) per atom, gives different determinants whenever the relevant multiplicities matter.

## Scope retained

The kernel is defined from the arithmetic scalar without supplying a zero enumeration. Its proof and the proof that recovered masses are integral use the classical explicit formula. Positivity is RH-equivalent, so the construction under stipulated RH is not an independent RH proof.

The atom data determine the spectral Hilbert realization up to unitary choices within each finite-dimensional fiber. They do not give a canonical embedding into the source Bessel model, whose orthogonal source vectors remain choices.

The theorem does not identify the historical Remark's undefined W, its finite period determinant family or signed coefficients. It does not replace weighted-character bounds on power windows by a global zeta-only bound. No arithmetic cohomology or Frobenius object is constructed.
