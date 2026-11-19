# Saito 1992: correction of a failed closure inference

## Status

**The proposed closure of the general integral E.3 converse is withdrawn.** No result row or theorem fragment asserting that closure was written. The initial message to the other agents misread the denominator in equation (1.8.2). The corrected reading leaves the same general subgroup equality unproved.

## Source and visual check

H. Saito, *Generalization of Abel's theorem and some finiteness property of zero-cycles on surfaces*, Compositio Mathematica **84** (1992), 289–332.

Primary PDF, opened: https://www.numdam.org/item/CM_1992__84_3_289_0.pdf

The decisive page is printed p. 296, Example 1.8, equation (1.8.2). We independently viewed the local primary-page image supplied by the cycles agent, then cropped its lower portion without altering the source:

- Source PDF: `research/agents/cycles/sources/Saito1992.pdf`.
- Source page image: `research/agents/cycles/output/Saito1992_pdf9_printed296.png`.
- Independently viewed crop: `research/agents/frobenius/output/Saito1992_p296_bottom_crop.png`.

The equation reads

\[
\operatorname{Gr}^{l}\operatorname{CH}(V)
=\frac{\langle H^{*l}\rangle_0\operatorname{CH}(V)}
 {\bigl(\langle H^{*l}\rangle_0\cap H^{*(l+1)}\bigr)\operatorname{CH}(V)}.
\]

The intersection sign and the absence of the zero-cycle-generation brackets around the second term are visible in the primary page. The incorrect reading replaced this denominator by the subgroup generated from the next step, which is a different expression.

## Mathematical consequence

Example 1.9 identifies the first zero-cycle-generated step with algebraic equivalence. Consequently, the degree-one quotient in Theorem 6.2 is

\[
\operatorname{Gr}^{1}\operatorname{CH}^{p}(V)
=A^{p}(V)/(A\cap H^{*2})\operatorname{CH}^{p}(V),
\]

not the quotient by the subgroup generated under correspondences by Albanese-zero zero-cycles. Corollary 6.3 and the zero-cycle case can identify the relevant relation on zero-cycles, but that does not justify replacing the displayed intersection by its zero-cycle-generated subrelation in every codimension.

In the notation of the E.3 investigation, identifying the latter generated relation with N therefore does **not** imply

\[
N=(A\cap H^{*2})\operatorname{CH}^{p}(V).
\]

That equality is precisely an additional missing argument. Theorem 6.2, Corollary 6.3, and Remark 6.4 cannot be cited as proving it from the displayed definitions alone. We make no general identification of P with the Walker Jacobian on this basis.

## Error detection and reproducibility

The root and cycles agents independently noticed that the proposed conclusion would also imply a general universal regular algebraic representative, conflicting with the still-conjectural status discussed in modern Walker literature. This was an effective consistency check, but the decisive correction is the directly inspected source formula above. We explicitly distinguish a source-reading error from a counterexample to the desired mathematical equality: the equality remains unproved here.

The earlier E.3m–n reductions remain unchanged. Their role is conditional or structural; this source does not close their remaining general hypothesis.
