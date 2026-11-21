# Independent whole-proof audit: D-HOS-16

**Verdict: PASS.** No mathematical repair was requested. This is an audit of the entire frozen addendum, all interfaces invoked from D-HOS-13–15, the full new published estimate and its proof, and the author's complete rational checker. The numerical reconstruction below is separately scoped.

Auditor: `/root/imprimitive`, GPT-6 Astra Pro, reasoning effort inherited/not exposed, run `HODGE_DIVISION`. The independent arithmetic completed at **2026-11-21 21:22:53 UTC**. This report records work actually completed by that time; it does not claim a subsequent execution of the author's checker.

## Frozen objects

- Proof: `../g34_eightfolds/bireflection/higher_odd_symplectic_three_sharp_section.tex`, SHA-256 `ce8fc689891738dbf571cdae6f92879bca88937129ac66bf278b6ec6f72cdd3f`.
- Author checker: `../g34_eightfolds/bireflection/check_higher_symplectic_three_sharp.py`, read completely.
- New published source: Larsen–Shalev–Tiep, *The Waring problem for finite simple groups*, Annals of Mathematics **174** (2011), 1885–1950, DOI `10.4007/annals.2011.174.3.10`.
- Official published PDF: <https://annals.math.princeton.edu/wp-content/uploads/annals-v174-n3-p10-p.pdf>, SHA-256 `dbcfed29aab0f3cc01b6e1ab1de97d0e0901bcc8aeeb20a37f2d8a94ac41e99e`.

The complete preceding D-HOS-13–15 proof was independently audited in this run, as recorded in `../audit_symplectic_three_cutoff/PEER_AUDIT.md`. Its exact matrix reconstruction and source review remain distinct from the present short numerical reconstruction.

## 1. Exact published input

I freshly read Definition 4.1.1 and equation (4.1.1), printed p.1907; the complete statement of Theorem 4.3.6 on pp.1917–1918; its entire proof on pp.1918–1923, including the decomposition, Cases A and B, and the numerical choices; and Remark 4.3.7 on p.1923. I also viewed the rendered published formulas on pp.1918, 1922 and 1923. This visual check resolves the radical and the allowed scalar set directly from the original page, rather than from OCR.

The first bound in (4.3.2) is

\[
 |\chi(h)|/\chi(1)<\gamma_q^{\sqrt{N/7}}\qquad(N\ge567).
\]

The radical includes the entire fraction `N/7`. Part 4 of the proof, p.1922, explicitly takes `alpha=sqrt(1/7)` and `alpha*sqrt(N)>=9`. This is different from the next line of the displayed estimate. For `q=3`, the constant on p.1907 is `gamma_q=19/20`.

The theorem applies to rational points of a simple simply connected classical algebraic group and every nontrivial ordinary irreducible character of that finite group. It therefore applies to the full group `Sp_(2n)(3)` and to characters inflated from its represented central quotients. No faithfulness premise is silently added or removed.

Remark 4.3.7 explicitly says that the conclusion also holds when the support is the infimum of `codim ker(h-lambda)` over the stated scalar set. For the symplectic group this set is `mu_2`. Accordingly, a semisimple natural operator with no eigenvalue `1` or `-1` has this restricted support exactly `2n`. It need not have usual algebraic-closure support `2n`. The addendum preserves that distinction.

This audit uses the exact published theorem as an input. Reading its full proof is not recorded as a new independent proof of every cited classification or of Gluck's results used by those authors.

## 2. All-element support reduction

For a noncentral element of the perfect symplectic cover, take a power of prime order modulo the center. A central sign gives actual odd prime order when the projective prime is odd. For projective order two, the two possibilities are `h^2=I` and `h^2=-I`. The projective kernel of a nontrivial irreducible character is the center, so this reduction remains nontrivial in projective representation. Taking powers cannot increase the codimension of the largest eigenspace.

The prior independently checked carrier proof gives the following exhaustive cases:

1. Actual order three: support at least `2a/9`.
2. Noncentral `h^2=I`: after a central sign the smaller nonzero symplectic eigenspace is fixed. A fixed hyperbolic plane can be removed, while the quotient moving rank is at least `n>=4`. The carrier inequality gives `(1/4)(1-3^-2)a=2a/9`.
3. Odd prime at least five with a natural eigenvalue in `mu_2`: the actual odd-order representative has a fixed symplectic plane and quotient moving rank at least two. The bound is `(1/2)(4/5)(1-1/3)a=4a/15`.
4. The residual semisimple cases, including `h^2=-I`, have no natural eigenvalue in `mu_2`. The refined published support is `2n>=568>567` when `n>=284`. Taking `N=567=7*9^2` gives `|chi(h)|/a<(19/20)^9`.

If an eigenvalue has maximum multiplicity `a-nu`, rotate it to 1. The triangle inequality gives `|chi(h)|>=a-2nu`. Thus the last case has support strictly greater than

\[
 \delta_*a,\qquad
 \delta_*={189312302221\over1024000000000}.
\]

The exact inequalities `1/6<delta_*<2/9<1/4` ensure the elementary cases satisfy the asserted uniform bound too. All finite-order matrices here are semisimple over the complex coefficient field; unipotence refers only to the natural representation in characteristic three.

## 3. Full compatible normalizers and actual source rank

The normalizer argument is restricted to the nonselfdual factor modules in the source consequence. At these ranks the universal cover is `Sp_(2n)(3)`, the field automorphism group is trivial, and the only outer class is represented by a nonsquare similitude. The previously checked anti-symplectic factorization identifies its character action with complex conjugation. It cannot stabilize a nonselfdual factor character. Schur's lemma therefore makes every compatible factor normalizer a scalar times an inner operator. The perfect-cover lifting and possible represented central quotient cause no additional intertwiners.

For a factor-preserving operator, eigenvalue multiplicities convolve, so a nonscalar factor supplies the same normalized support bound on the whole tensor product. A nontrivial factor cycle has the already checked `1/4` bound, stronger than `delta_*`. Nonidentity scalar inertia moves all dimensions. These arguments permit different ranks, arbitrary allowed central quotients and scalar extensions, and factor permutations; no equality between the inducing character field and the original imaginary quadratic field is used.

The actual intermediate-cover Euler formula is `6=2e(h-1)+D`. The degree lower bound `e>=3^283` excludes `h>=2`. For `h=1`, `D=6` gives at most six genuine marks and hence image rank at most six. A rank-nine source must have `h=0`, at least twelve genuine inertia points and `D=2e+6`. The support bound would force

\[
 e\le {6\over12\delta_*-2}
   ={1536000000000\over55936906663}<28,
\]

contradicting `e>=3^283`.

In a transitive core, all factor modules have the same selfduality status. The selfdual case is already excluded in the main imaginary-field setting by D-HOS-12. Combining the two results leaves only `4<=n<=283`. This is a necessary remaining interval, with no existence assertion for any rank in it.

## 4. Independent exact arithmetic and limits

`independent_check.py` imports no author arithmetic and uses integer exponentiation, gcd reduction and cross multiplication instead of the author's `Fraction` routine. It checks the frozen proof and source hashes, reconstructs the exact `c_*`, `delta_*` and source ceiling, verifies the two carrier constants, proves `2*283<567<=2*284`, and checks the integral degree cutoff 27 directly after clearing denominators.

Actual result: **PASS, 0.002043289 seconds**, saved in `independent_checked.json`. No failed attempt occurred in this new arithmetic audit. The author's code had already been read; this is an independently implemented reconstruction, not a blind audit.

The arithmetic does not enumerate the groups, verify the published character theorem computationally, or replace the universal mathematical proof. The frozen proof has no gap identified in the full review.
