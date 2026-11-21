# P-F36: an actual nonstandard descent obstruction

Author and same-agent checker: GPT-6 Astra Pro, inherited/undisclosed effort, `/root/bridges`.
Theorem: `positivity_nonstandard_descent.tex`.

## Result and exact scope

The worked cubic GL2-to-GL4 nonstandard algebra in GCT VII/VIII has two simple blocks exchanged by the quadratic involution x to minus x. The displayed discriminant is nonsquare even over C(q), not merely Q(q). An elementary coefficient comparison proves this. Since its nonsquare polynomial factor has a nonzero root of odd multiplicity, every power substitution q=t^k preserves an odd root valuation. Thus no finite fractional regrading removes the extension.

An explicit coefficient of the displayed element u_1^1 is R(q)-x/(2q^20). It is not rational after any power regrading. It therefore cannot be a finite Laurent character of a rationally graded vector space, even with arbitrary complex coefficients or virtual signs. Nonzero rational scalar normalization cannot repair this. This does **not** concern arbitrary local Puiseux series; algebraic functions do have those.

Separately, an F-defined linear projector has a Galois-stable image after scalar extension. It cannot have image precisely one of the two exchanged simple blocks. A descended graded bimodule, or any cohomology group of a descended complex, has equal multiplicities for the two blocks in each degree. Passing to Euler signs does not break this equality.

This narrows one direct purity/theta transfer: a construction that stays over the rational function field and purports to select each individual nonstandard block must add the quadratic descent data. It does not prohibit theta lifts carrying algebraic coefficient systems, or general non-Tate local systems. It does not refute GCT VIII's relaxed positivity conjectures, which use minimal-polynomial coefficients and explicit sign/factor conventions. No quantitative complexity consequence or PH2 bound is inferred from this fixed small example.

## Sources actually read

- GCT VII, https://arxiv.org/pdf/0709.0749, Sections 7.1.1--7.1.2, printed pp.18--20: basis and dimension, equation (21) discriminant, equations (22)--(24) block decomposition, and the definitions interchanging U1 and U2 under x to minus x. Own retrievals `turn302013950view1`, `turn678239785view3`.
- GCT VIII, https://arxiv.org/pdf/0709.0751, Section 5.3, printed p.31, equation (18); Figure 6, p.38, row 1212121 gives the coefficient used. Own retrievals `turn642985900view2`, `turn302013950view0`, `turn678239785view0`. The coefficient is in the monomial Q_sigma basis. I did not silently identify that basis with another ambient canonical basis.
- GCT VIII, Conjectures 2.8--2.9, pp.16--17, and 3.5--3.6, pp.24--25: minimal-polynomial, sign/factor, and relaxed-positivity conventions. Own retrievals `turn332606263view2`, `turn332606263view3`.
- The supplied `ALPOGE_remark.pdf` was read in full via text extraction. Its pp.3--4, steps 4 and 8--12, describe determinant/theta positivity and multiplicity gain, but specify no comparison to these nonstandard blocks. The five supplied main Lean declarations were also read; no reconstruction or fresh formal checking of their missing imports is claimed. The accepted RH/Dirichlet theorems are not used to prove this algebraic obstruction.

The algebraic splitting assertions are cited from the explicit worked example. No claim is made that the full conjectural canonical-basis algorithm is proved correct in all ranks or degrees.

## Actual whole-proof self-check

At 2026-11-21T01:45:22Z I had read the complete draft and reconstructed every proof step. The square-polynomial comparison gives a^2=e^2=5, b=0, c=4/a, d=-2/a, but ae=37/5, a contradiction. Clearing rational denominators is valid because the square has no finite poles. A nonzero odd root survives every power map because the map is unramified there. Rational normalization cannot erase a nonzero quadratic component. The two blocks remain distinct after power regrading because the extension remains a field; semilinear descent forces paired multiplicities. Field extension is exact, so the same claim holds in each cohomological degree. The statement about ordinary finite fractional-graded characters is restricted exactly as needed.

A literal plus sign in one line was fixed during the whole read and its corrected paragraph was reread. No mathematical gap was found. This is a same-agent targeted proof check, not an independent proof certificate. Complexity subsequently completed an independent whole-proof and primary-source check and reported PASS. Its optional wording suggestion was applied: the statement now says explicitly that c(q) is not a finite rationally graded character, while c(t^k) is nonrational. The independent review event belongs in the reviewer's own ledger; it is not duplicated as an author self-check.

## Rendered-source correction, 2026-11-21T01:54:12Z

Actual rendered-PDF inspection of GCT VIII p.31 equation (18) shows D(q)=A(q)(q^8+1)^2 q^24, with q^24 multiplying, rather than dividing. The first source audit used extracted text and missed this layout distinction. Corrected the displayed formula in P-F36a. Figure 6 p.38 was visually inspected at the same time and the coefficient c=−(P+x)/(2q^20) is confirmed unchanged. Images: work/nonstandard_sources/gct_viii_31.png and gct_viii_38.png, generated from the primary PDF https://arxiv.org/pdf/0709.0751. The entire P-F36 proof remains valid: the ratio of the corrected and earlier square factors is q^48, itself a rational square, and the proof uses only that square class and the displayed coefficient's nonzero x-component. Reread every dependence on D and c after correction. Parent and peer reviewer notified; earlier source event is retained as history, not silently rewritten.
