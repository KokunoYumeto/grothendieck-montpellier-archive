# Quantitative prime sums modulo 7: exact primary source and usable consequence

Checker: `/root/archive_binomial`, GPT-6 Astra Pro; runtime reasoning effort not exposed. The source text and the rendered original PDF page were directly read in this run, closing 2026-11-21 03:12:48 UTC.

## Exact source

Zeév Rudnick, *Primes in Arithmetic Progressions: Fixed Modulus*, course notes dated May 26, 2015, §2, **p.2, equation (1)**:

https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf

For fixed q and (a,q)=1 that displayed equation gives the unconditional estimate

\[
\sum_{\substack{p\le X\\p\equiv a\pmod q}}\frac{\log p}{p}
 =\frac{1}{\varphi(q)}\log X+O(1).
\]

The paragraph immediately above gives quantitative fixed-modulus PNT estimates for π and ψ with error O(X exp(−c√log X)). The constants are allowed to depend on the fixed modulus; no RH hypothesis is made. Taking q=7 therefore supplies the required coefficient 1/6 and bounded error in each of the six nonzero classes. This exact known result can be cited without reproving it in the main paper.

The official author-hosted four-page PDF is saved as `analytic_sources/rudnick_fixed_progressions_2015.pdf`. I directly viewed the pixels of rendered page2, saved as `rudnick_fixed_progressions_page002.png`, confirming the section, equation number, fixed-modulus qualification and unconditional wording. The author's notes are the precise cited source; this is not represented as a new theorem by this project.

## A constant-plus-o(1) refinement, if that stronger form is needed

This refinement is a short deduction from the quantitative statement just cited. Let θ_a(X)=X/6+E_a(X). The difference between ψ and θ is O(√X log²X), so after decreasing c if necessary the cited ψ estimate gives E_a(X)=O(X exp(−c√log X)). Partial summation gives

\[
\sum_{\substack{p\le X\\p\equiv a\pmod7}}\frac{\log p}{p}
 =\frac{\theta_a(X)}X+\int_2^X\frac{\theta_a(t)}{t^2}\,dt
 =\frac16\log X+C_a+o(1),
\]

where

\[
C_a=\frac{1-\log2}{6}+\int_2^\infty\frac{E_a(t)}{t^2}\,dt.
\]

The integral converges absolutely: with u=√log t its tail is bounded by a constant times ∫_(√log X)^∞2u exp(−cu)du, which tends to zero. This proves the stronger form with an explicit integrable-tail justification, rather than inferring a bounded error from the weaker θ_a(X)~X/6 alone.

## Form suitable for the residue comparison

Suppose, for each a∈{1,…,6}, a local coefficient satisfies

\[
g_a(p)=\frac{A_a}{p}+O(p^{-2})\qquad(p\equiv a\pmod7),
\]

with fixed constants. Then

\[
\sum_{\substack{p\le X\\p\nmid7}}g_{p\bmod7}(p)\log p
 =\frac{A_1+\cdots+A_6}{6}\log X+C+o(1).
\]

Indeed the six leading terms use the preceding class formula, and the remaining series converges absolutely by comparison with ∑_(n≥2)log n/n². Deleting finitely many bad or level-dividing primes changes only C. Thus the sign of the sum of the six leading coefficients is the relevant signed leading-term comparison. This elementary specialization introduces no conditional analytic hypothesis and makes no geometric assertion about which local coefficient the project actually realizes.

## Source-use boundaries

Williams, *Mertens' Theorem for Arithmetic Progressions*, J. Number Theory 6 (1974), pp.353–359, Theorem1 on p.356, was also inspected as a possible published alternative. Its displayed theorem concerns the Mertens product with a stated logarithmic error; it should not be substituted without further argument for the stronger weighted prime-sum estimate above. The exact direct weighted reference used here is Rudnick §2 p.2 (1).

The general PNT is cited background, not independently re-proved in this event. The partial-summation refinement and finite-class specialization above were independently checked as written. No main-paper edit was made.
