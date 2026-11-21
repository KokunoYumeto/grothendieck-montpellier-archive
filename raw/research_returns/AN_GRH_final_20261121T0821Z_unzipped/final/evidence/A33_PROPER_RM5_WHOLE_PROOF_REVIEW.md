# A33 properness supplement: independent whole-proof review

Date: 2026-11-21. Reviewer: GPT-6 Astra Pro; effort not exposed; AN_GRH/gt_certificates.

**PASS.** The complete supplement, its exact arithmetic checker, and the named primary inputs were read. An independent arithmetic implementation reproduced the point counts and ratio resultant. No proof-assistant verification is claimed.

## Reviewed source

`work/row_audit/A33_SUPPLEMENT_PROPER_RM5.tex`

SHA256: `9410ef5ad99c4104e138143a08ebc9d4e2999b78f9e83865d2300b85cda9306c`.

The statement supplies an actual ordinary genus-two curve whose geometric Jacobian has no Rosati-invariant real multiplication by the discriminant-five ring. It establishes properness of the A33 target restriction; it makes no claim against section injectivity.

## Complete proof check

1. The three simple Artin–Schreier poles give genus two and rank two. The rational branch points contribute three points. The nonbranch point counts give `N4=3` and `N16=15`, hence Frobenius polynomial `P=X^4−2X^3+X^2−8X+16` by the two Newton identities.
2. Reduction modulo three is the fifth cyclotomic polynomial. Since three has order four modulo five, this proves irreducibility over the rationals and degree four for the Frobenius field.
3. The ratio resultant is exactly `256(t−1)^4 A(t)^2 B(t)`, with the displayed quartic factors. Both factors are primitive and irreducible modulo three. Their monic rational normalizations are not integral, so none of their roots is an algebraic integer; in particular no such root is a root of unity. The diagonal factors account for the four ratios equal to one. Thus every positive power of Frobenius has four distinct eigenvalues.
4. Milne's tensor-injectivity theorem applies to the whole geometric endomorphism group. A finite basis is defined over one finite extension, so the whole rational algebra embeds into the dimension-four centralizer of the corresponding Frobenius power on the rational Tate module. It already contains the quartic Frobenius field, and therefore equals that field. Poincare reducibility then excludes a nontrivial geometric decomposition, since a field has no nontrivial idempotent. This argument does not confuse mere faithfulness over the rationals with injectivity after tensoring with the local field.
5. The canonical Rosati involution sends Frobenius to four divided by Frobenius and is nontrivial. The fixed element `s=pi+4/pi` satisfies `s^2−2s−7=0`, giving the full quadratic fixed field `Q(sqrt(2))`. A Rosati-invariant embedding of the discriminant-five ring would induce a field embedding of `Q(sqrt(5))` into this distinct quadratic field, impossible. All geometric endomorphisms have been considered, so constant extension cannot change this conclusion.

## Exact arithmetic review

The full producer checker `work/row_audit/verify_A33_proper_RM5.py`, SHA256 `6b809b6ae2d3bd81d8f9f05b5e964db8ad1728a3673e13d4188886ac68cdef04`, was read. Its F16 table, all affine y-solution enumeration, companion matrix, complete 24-term determinant, primitive coefficients and mod-three tests are consistent with the proof.

A separate implementation is retained in `A33_proper_RM5_review/verify_proper_RM5_independent.py` and its `.json` output. It imports no producer code. It constructs F16 as the quadratic extension `F4[v]/(v^2+v+u)`, rather than the producer's degree-four binary presentation, and directly enumerates every y-solution over both fields. It uses SymPy's resultant computation instead of the producer's companion determinant. Executed outcome: counts `3,15`; displayed resultant identity PASS; irreducibility over Q and modulo three PASS; real-trace polynomial identity PASS.

## Primary-source check

J. S. Milne, *Abelian Varieties*, author version dated 2 January 2022, https://jmilne.org/math/xnotes/AVs.pdf.

Reopened and read Theorem 12.5 and its complete displayed proof on printed pages 21–22; Proposition 12.1 and its proof on page 19; and Lemma 19.2 and its proof on page 41. The cited hypotheses and locators match the uses above. Retrieved references: `turn773748171view0`, `turn155698012view0`, `turn155698012view1`, `turn155698012view2`.

No edits were made to the author's source, final package, or build.
