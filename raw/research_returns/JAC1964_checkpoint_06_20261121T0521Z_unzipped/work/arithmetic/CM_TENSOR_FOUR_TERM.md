# Further CM tensor calculation after AR25

Run JAC1964-20261121, `/root/arithmetic_sign`. Research note; no new positivity theorem.

## Exact reduction from sixteen terms to four

On \(h^1(E)\), write \(u=[i]_*\). Then \(u^2=-1\). The projector onto the two extreme tensors in \(h^1(E)^{\otimes3}\) is

\[
\Pi=\frac14(1-u_1u_2-u_1u_3-u_2u_3).
\]

Indeed after adjoining \(i\) to the coefficients, the two one-factor projectors are \((1-iu)/2\) and \((1+iu)/2\). Summing their third tensor powers cancels all odd powers and gives the displayed expression. It equals the order-sixteen group average in AR25 exactly, since both descriptions are character projectors for the same group action; no realization-only comparison is involved.

Put \(a_j=t_{j,0}\) and \(b_j=t_{j,1}\). Then

\[
a_j^t=a_j,\qquad b_j^t=-b_j,
\]

and AR25 becomes

\[
h_K(z,z)=\frac{1}{4DM^2}
\left\langle
 \widehat a_1\widehat a_2\widehat a_3
 -\widehat b_1\widehat b_2\widehat a_3
 -\widehat b_1\widehat a_2\widehat b_3
 -\widehat a_1\widehat b_2\widehat b_3
\right\rangle_{K'}.
\]

Equivalently the numerator is the real part of

\[
\left\langle
 (\widehat a_1+i\widehat b_1)
 (\widehat a_2+i\widehat b_2)
 (\widehat a_3+i\widehat b_3)
\right\rangle_{K'}.
\]

The terms with an odd number of \(b_j\)'s vanish under simultaneous transposition on \(C\times C\). This uses the uniqueness/functoriality of the admissible metrics, so the transposition identities hold for their arithmetic classes, not only for underlying divisors.

## What the ordinary divisor inequalities do not immediately supply

This is a **pure cubic** in complex CM eigencorrespondences, rather than a Hermitian square \(c\overline c\) against a nef class. Each \(a_j\) is a normalized degree-zero correspondence in both factors. It is not a nef divisor on the surface merely because it arises from an elliptic quotient. The \(b_j\) are skew under transposition and are also not available as nef polarizations. Thus the hypotheses of Yuan–Zhang's divisor Hodge index theorem do not apply directly to the displayed cubic. The rigorous nef perturbations made in AR22 give symmetric bounds and remain available.

## Archimedean check, not a global sign argument

At a complex place, the admissible curvature of \(a_j+i b_j\) is concentrated in one of the two cross types
\(H^{0,1}(C)\otimes H^{1,0}(C)\) or its conjugate, with the same choice for all \(j\). One sees this either from the CM projectors or by pulling the translation-invariant Poincare curvature from \(E\times E\). Consequently the wedge of any two of these chosen cross curvatures is zero: two holomorphic one-forms occur on the same curve factor, and likewise for antiholomorphic forms.

This explains why replacing this pure cubic by a positive Hermitian norm is not justified. It does **not** imply that the arithmetic triple intersection vanishes: arithmetic intersections include divisor terms and finite-place data, and the factorwise curvature observation is not a replacement for an admissible arithmetic intersection formula. The already proved nonzero Fermat height is consistent with this distinction.

No source theorem has yet been identified that gives the needed sign for this four-term expression on every auxiliary curve. Zhang 2010, Conjecture 2.4.1 remains the precise general tensor positivity statement; Theorem 2.3.5 gives the exact intersection identity.
