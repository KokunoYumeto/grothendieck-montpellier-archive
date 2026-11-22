# Independent audit of the corrected Saito reductions

## Outcome and exact distinction

The current `research/agents/cycles/saito_filtration.tex`, statements E.3o–q, passes this independent audit. This is a positive audit of the corrected statements. It does not reinstate the withdrawn general closure recorded in `E3_Saito_correction_REVIEW.md`.

We directly viewed the primary images of Saito's printed pp.321,323,325, in addition to the decisive definition on p.296. The two quotients must remain distinct:

\[
\operatorname{Gr}^{1}\mathrm{CH}^{i}(X)
 =\mathcal A^i(X)/(\mathcal A\cap\mathcal H^{*2})^i(X),
\qquad
{}'\operatorname{Gr}^{1}\mathrm{CH}^{i}(X)
 =\mathcal A^i(X)/(\mathcal A*\mathcal H)^i(X).
\]

The first denominator is the corrected reading of equation(1.8.2). The second quotient is explicitly introduced in Lemma6.2.1 on printed p.321. Neither is defined as the quotient by the zero-cycle-generated relation N in general.

## E.3o: exact integral Walker kernel

The source supports the finite-kernel assertion used in the draft. On printed p.323, Saito gives the surjective factorization from the primed quotient to the unprimed quotient and then to the algebraic intermediate Jacobian. He constructs a surjection from an abelian variety to the primed quotient whose composite with the Jacobian is an isogeny. Consequently every kernel in that factorization is finite. Remark6.4 on p.325 visibly records the inclusions

\[
\mathcal A*\mathcal H\subset\mathcal A\cap\mathcal H^{*2}
 \subset\ker(\psi_{\mathrm{AJ}}|_{\mathcal A})
\]

and equality up to finite groups, with exact equality under the torsion-injectivity hypothesis of Theorem6.2(iii).

The draft's integral strengthening is correct. The product relation A*H is divisible because one divides its algebraically trivial factor. Its Walker image lies in the finite kernel of the Walker isogeny and must therefore vanish. The quotient kerWalker/(A*H) is both finite by the preceding source statement and divisible by the already checked ACMV divisibility theorem for the Walker kernel. It is zero. This proves kerWalker=A*H, with no replacement of the intersection denominator by N.

On zero-cycles the torsion-injectivity hypothesis holds, and the p.323 proof explicitly treats p=dimV. The inclusions A*H⊂H^{*2}⊂kerAJ then identify H^{*2} on zero-cycles with the Albanese kernel. The second inclusion is given by Example1.11, pp.297–298; the integral relation is the H=H_Z defined in Example1.8. Taking all correspondence images is exactly N=<H^{*2}>_0. Thus the remaining general gate is the equality of this generated relation with A*H, which is not proved here.

The optional replacement of the second H factor of A*H by rational-homologically-trivial cycles is also valid: multiply that factor by an integer killing its integral cohomology class and divide the A factor by the same integer. It does not justify changing the definition of H^{*2} itself.

## E.3p: integral surface generators

The complete-intersection argument is sound integrally. A sufficiently positive smooth connected surface can be chosen through every point in the finite support of an integral zero-cycle on a smooth projective complex variety of dimension at least three. Successive weak Lefschetz isomorphisms on integral H1 give an actual Albanese isomorphism. The same formal zero-cycle on the surface therefore remains Albanese-zero.

The pullback of the correspondence is the refined pullback along the smooth regular immersion. Compatibility with proper pushforward gives the equality of cycle actions without requiring the chosen correspondence representative to meet the surface properly. No denominator or degree factor is introduced. Dimension one contributes no Albanese kernel; dimension zero contributes no connected degree-zero zero-cycle. Saito's Lemma7.1.1, pp.326–327, is consistent with this direct argument.

## E.3q: codimension two under surface support

We also audited the appended codimension-two statement. Transposing the support decomposition gives two well-typed routes:

- CH2(X)→CH2(S)→CH2(X), with dimS≤2;
- CH2(X)→CH1(D)→CH2(X), with dimD=dimX−1.

The first route takes an Abel–Jacobi-zero algebraically trivial cycle into a surface Albanese kernel, hence into N after pushing forward. The second route takes it to an Abel–Jacobi-zero divisor, which is zero. The resulting uniform integer M kills kerWalker/N. This quotient is divisible, so the bounded-exponent quotient is zero. This is an integral argument, even though the diagonal construction initially requires clearing one integer.

For codimension two, Corollary6.3 and Remark6.4 use the exact torsion theorem, so kerAJ=A*H=kerWalker. The Walker isogeny therefore has zero kernel. No corresponding assertion in arbitrary codimension is inferred.

## Primary-page record

Primary PDF: https://www.numdam.org/item/CM_1992__84_3_289_0.pdf , independently opened in this session.

Visually inspected local source pages:

- `research/agents/cycles/output/Saito1992_pdf9_printed296.png`;
- `research/agents/cycles/output/Saito1992_pdf34_printed321.png`;
- `research/agents/cycles/output/Saito1992_pdf36_printed323.png`;
- `research/agents/cycles/output/Saito1992_pdf38_printed325.png`.

We used OCR only to locate the additional passages; the decisive quotient and finite-kernel statements were checked on the primary page images. This audit does not erase the earlier source-reading error: it records the corrected, narrower conclusions.
