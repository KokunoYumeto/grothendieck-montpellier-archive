# Independent whole-proof audit: HD-COMP and HD-COMP4

**Result: PASS.** The entire current proof in `research/general_compensation.tex` was read, including its final statement of the existential status of the remaining numerical gates.

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, reasoning effort inherited/unexposed, HODGE_DIVISION, 2026-11-21 (approximately 12:05–12:10 UTC by the clock tool). This is a mathematical whole-proof check, not an independent derivation of the higher-dimensional input bounds.

## Normalization and arithmetic

For the convention conjugate-linear in the first argument,

\[
h(x,y)=E(x,\tau y)-\bar\tau E(x,y)
\]

is Hermitian and the coefficient of \(\tau\) is \(E(x,y)\). On a one-dimensional Hermitian block \(h(v,v)=a\), the ordered rational basis \((v,\tau v)\) has \(E(v,\tau v)=a\). Therefore the determinant relation \(\det_{\mathbf Z}E=(\det_Kh)^2\) has no extra field-discriminant factor. It extends under a change of \(K\)-basis because both sides multiply by the square of the norm of its determinant. Class number one provides the free integral maximal-order lattice basis. The sign \((-1)^n\) agrees with signature \((n,n)\), and hence \(\det h=(-1)^n\Delta\).

The balanced elliptic surface with polarization \(\lambda=\vartheta_1+\Delta\vartheta_2\) has determinant \(-\Delta\) and polarization product \(\Delta\). Its product with the input has signed determinant \(\Delta^2=\operatorname{Nm}(\Delta)\) and polarization product \(\Delta^2\). The cited rational Hermitian classification therefore gives the required split higher-dimensional space. This uses the actual determinant class, not just the real signature.

## Algebraic contraction and effectiveness

The two coordinate elliptic curves and the graphs of \(1,\tau\) span \(\operatorname{NS}(E_K^2)_{\mathbf Q}\). Subtracting their coordinate parts leaves the two off-diagonal classes, which span the balanced Weil plane. The graph matrices have nonzero eigenvalues \(2\) and \(1+\operatorname{Nm}(\tau)\); each coordinate class also satisfies the same nef bound. Since \(\Delta\ge1\), the displayed comparison with \(c_K\lambda\) is valid.

The Weil plane of the product embeds in the Künneth factor \(W_K(A)\otimes W_K(T)\). If all four contractions vanished after projection to \(W_K(A)\), contraction against the two off-diagonal linear combinations would vanish. The nondegenerate intersection pairing on \(W_K(T)\) then forces the relevant tensor to vanish, contrary to the higher-dimensional detector. This is a test of a projection of the whole effective cycle; it does not assume the cycle is a pure Weil class.

Translation in \(T\) gives proper intersection simultaneously with the finitely many components of the detector: the incidence variety over any component has expected generic fiber dimension, or empty generic fiber. Effective Cartier intersection followed by proper pushforward remains an effective integral cycle. The nonzero Weil projection guarantees a detecting component survives pushforward. Projection formula and the nef inequalities give exactly the stated, deliberately nonsharp, constant \(c_K\). Selecting one reduced detecting component can only decrease degree.

## Numerical and conductor statements

The Gaussian calculation is \(2(2\Delta^2)^6D_{G,6}=128\Delta^{12}D_{G,6}\). Both \(\mathbf Q(\sqrt{-7})\) and \(\mathbf Q(\sqrt{-2})\) admit the chosen integral generator of norm two, giving constant three. Their sixfold functions are the already independently audited explicit bounds.

For a fourfold with an action of \(\mathbf Z+f\mathcal O_K\), the lattice \(f\mathcal O_K\Lambda\) lies between \(f\Lambda\) and \(\Lambda\), so its index is at most \(f^8\). Pullback multiplies the polarization product by that index; pushforward preserves detector degree and the rational Weil plane. The displayed functions are increasing, so substituting \(f^8\Delta\) is valid and yields \(f^{96}\) in the Gaussian expression.

## Scope

This audit checks the complete compensation proof and its applications to the stated input functions. It does not newly prove Schoen's Hermitian classification, the Gaussian sixfold input, or Perry/S14. The final distinction between numerical bounds and the merely existential detector integers for the remaining fields is correct.
