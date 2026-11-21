# The existing monomial algebra behind the height-two rational-point rule

This is a source application supplement to F28, not a new theorem. It answers the constructive part of the rectangular investigation: an actual ordinary invariant-theory object already gives a positive monomial rule in this restricted family, even though the signed Young-orbit mechanism is impossible for its unprojected symmetric-group tensor square.

## Exact primary input

Read Manivel, *A note on certain Kronecker coefficients*, arXiv:0809.3710v1, §2 pp.2–3 and the whole §3 pp.3–4, especially the four numbered boundary components and the last paragraph of §3. Local files: primary_sources/Manivel_0809_3710.pdf and .txt. Primary URL: <https://arxiv.org/pdf/0809.3710>.

For complex spaces \(U,V,W\) of dimensions \(2,2,4\), let \(N\) be the unipotent radical of the chosen Borel in \(GL(W)\). The source proves

\[
\mathcal A=\mathbf C[U\otimes V\otimes W]^{SL(U)\times SL(V)\times N}
=\mathbf C[f_1,f_2,f_3,f_4].
\]

The four \(f_i\) are homogeneous semi-invariants, with degrees \(4,2,4,6\), and with the following three partition labels in the source's dual-polynomial convention:

\[
((2,2),(2,2),(1,1,1,1)),\quad
((1,1),(1,1),(2)),\quad
((2,2),(2,2),(2,2)),\quad
((3,3),(3,3),(2,2,2)).
\]

The published argument uses an open orbit of \(SL(U)\times SL(V)\times B\) and its four boundary equations. Schur–Weyl duality identifies the indicated highest-weight multiplicity with the rectangular Kronecker coefficient. These are the cited source inputs, not deductions from a spectral sign theorem.

## Explicit exponent calculation

A monomial \(f_1^{a_1}f_2^{a_2}f_3^{a_3}f_4^{a_4}\) has the padded \(W\)-partition label

\[
\begin{split}
\nu_1&=a_1+2a_2+2a_3+2a_4,\\
\nu_2&=a_1+2a_3+2a_4,\\
\nu_3&=a_1+2a_4,\\
\nu_4&=a_1.
\end{split}
\]

Solving these four equations gives

\[
a_1=\nu_4,\qquad
a_2=(\nu_1-\nu_2)/2,\qquad
a_3=(\nu_2-\nu_3)/2,\qquad
a_4=(\nu_3-\nu_4)/2.
\]

The partition inequalities make all four numbers nonnegative. They are integral exactly when all padded parts of \(\nu\) have the same parity. The \(U,V\) determinant exponents are then both

\[
d=2a_1+a_2+2a_3+3a_4=\tfrac12|\nu|,
\]

which also equals half the polynomial degree. Since \(\mathcal A\) is the stated polynomial ring, its monomials are an actual basis, so these exponents count the corresponding highest-weight multiplicity without cancellation. Their uniqueness explains multiplicity freeness directly from the cited algebra structure.

The point used in F28 has coordinates

\[
\left((\nu_1-\nu_4)/2,(\nu_2-\nu_4)/2,(\nu_3-\nu_4)/2\right)
=(a_2+a_3+a_4,\ a_3+a_4,\ a_4).
\]

This is an integral triangular coordinate change of determinant one from \((a_2,a_3,a_4)\); the remaining exponent \(a_1=\nu_4\) is fixed and integral. Thus F28's three-dimensional ambient rational-point model is the actual exponent rule, expressed in different lattice coordinates. It is not an arbitrary assignment of an integral or nonintegral point after inspecting whether a coefficient is zero.

## What this constructive route does establish

The source supplies, for all height-two rectangle squares, an explicit ordinary algebra, homogeneous semi-invariant generators, a monomial basis, a multiplicity identification, and elementary linear conditions for the basis exponents. The right-hand sides are binary polynomial-size and scale homogeneously, so the restricted Ehrhart interpretation is exact.

The monomial basis is for this highest-weight invariant algebra and its torus grading. It is not an \(S_{2d}\)-signed Young-orbit basis of \([(d,d)]^{\otimes2}\); F28 rules out that latter structure for every \(d\ge2\). There is no contradiction because these are different representation-theoretic realizations with an actual known multiplicity comparison.

The source does not thereby identify the specified nonstandard quantum basis, its structure constants, a general-height rectangular formula, or the determinant-orbit-closure multiplicities needed for an asymptotic GCT obstruction. No finite-field model, Frobenius normalization, or spreading theorem beyond what is explicitly stated here is inferred. The restricted positive rule is already obtained in ordinary characteristic-zero invariant theory.

## Check record

The exact four generator labels and degrees were read in context in the primary source. The linear equations, their inverse, total degree, determinant exponent and unimodular coordinate transformation were derived and checked directly in this note. The external open-orbit/boundary theorem is cited, not independently re-proved. This supplement does not change the proof of the hook obstruction.
