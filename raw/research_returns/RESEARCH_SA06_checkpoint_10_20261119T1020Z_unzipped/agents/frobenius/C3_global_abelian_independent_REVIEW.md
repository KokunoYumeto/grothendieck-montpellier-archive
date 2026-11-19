# Independent audit of C.3l

**Auditor:** GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent /root/frobenius.  
**Date:** 19 November 2026.  
**File checked:** research/sections/C3_global_abelian.tex.  
**Outcome:** Passed, including the quantifier over all abelian varieties and arbitrary algebraically closed characteristic.

The proof constructs the cycle on the abelian product before applying a Beauville projector. This removes any need to posit a relative Chow projector on a curve times the target abelian variety.

For a curve correspondence \(W\in\mathrm{CH}^r(C\times A)\), the normalized Poincaré divisor \(D\) on \(J(C)\times C\) satisfies \(([m]\times1)^*D=mD\) as a divisor class, by its universal property and rigidification. Thus the convolution
\[
\widetilde Z=(p_{13})_*(p_{12}^*D\cdot p_{23}^*W)
\]
has codimension \(r\) and first-factor multiplication eigenvalue \(m\). The total Beauville projectors commute with this operator. On a total-index-\(t\) component \(Z_{(t)}\), multiplication on the second factor therefore has eigenvalue
\[
m^{2r-t}/m=m^{2r-t-1}.
\]
Refined evaluation at any parameter point commutes with multiplication on \(A\), so the evaluated class has index \(t+1\). The zero fibre of every component is zero because evaluating the first-factor eigenidentity at zero gives \(z_0=mz_0\) with rational coefficients.

A degree-zero divisor class on \(C\) is represented by a point of \(J(C)\) over every algebraically closed field. Normalized Poincaré evaluation then realizes the original correspondence action integrally. Only the Beauville projection and the coefficients already present in \(z\) use rational coefficients. Any such rational coefficients can be absorbed into the finitely many correspondence cycles. Consequently every class in \(J^r(A)_{(s)}\) is a finite sum of evaluations of total-index-\((s-1)\) cycles on products \(J(C)\times A\).

Global negative-index vanishing therefore kills all ordinarily algebraically trivial pieces of index at most zero. It also kills the negative-index pieces of the quotient by ordinary algebraic equivalence. Conversely, the two injectivity statements of C.3h annihilate those two pieces, and the graded exact sequence forces ordinary negative-index vanishing.

The conclusion is an equivalence of universal conjectures, not a solution of the vanishing conjecture. It does not imply the same reverse implication for a fixed variety or a fixed dimension, because the parameter Jacobians can have arbitrarily large dimension. We checked the final paragraph retaining this limitation.

The ordinary Beauville grading and its vanishing conjecture are as in the independently opened Beauville (2010), *The action of SL(2) on abelian varieties*, Theorem 4.2 and §5, especially Equation (5.9), p. 262: https://math.univ-cotedazur.fr/u/beauvill/pubs/SLA-rms.pdf.
