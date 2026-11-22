# HD-ALT-07a/b — whole-proof and primary-source audit

**PASS on the final frozen proof.** Reviewer `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. The complete final proof, bibliography, author program and author output were read. A separate exact supplement was written and executed. No repair to the final mathematical proof was requested.

Frozen file: `research/ordinary_alternating_fixed_free_section.tex`.

SHA-256: `78ffa543eacf6f88a656c2bc37f673b75acca4eba98671cbba9f564f4885c9b7`.

The earlier draft `dfa52960...` was also read. Before the final freeze, the author clarified the positive bracket in the threshold calculation and replaced the illustrative `(22,3)` label by `(88,12)`. The earlier label illustrated improvement over the uniform `87/100` consequence but did not survive the stronger old finite-degree inequality. The final witness correctly survives that inequality too. The report and successful final supplement are bound to the corrected frozen proof, not to the earlier illustrative claim.

## 1. Original published input and access scope

I read the complete original Fomin–Lulov Sections 1–2, printed pp. 219–223, through the official Mathnet full-text link, including Theorem 1.1 and its character interpretation on p. 220, Corollary 2.2 and Theorem 2.3 on p. 221, and the complete Möbius-inversion proof on pp. 222–223. Its exact bound is

`f_r^λ ≤ m! r^m (f^λ/n!)^(1/r)`, where `n=rm`.

The character interpretation at equal cycle lengths gives the required `r=2` estimate. A nondecomposable shape has value zero by the same rim-hook rule. The theorem's upstream combinatorial references are accepted in the stated published scope; this audit does not claim to reconstruct those entire sources.

Official record: <https://www.mathnet.ru/eng/znsl4388>.

Ordinary full-text link: <https://www.mathnet.ru/php/getFT.phtml?jrnid=znsl&option_lang=eng&paperid=4388&what=fullt>.

At the time of this audit, the latter returned an actual eight-page PDF to the web extraction service, resolving to `https://www.mathnet.ru/links/e3dbc82ece785e023d4625bf0c98e540/znsl4388.pdf`. The alternate indexed original at `https://www.mathnet.ru/links/595730c901c50a6213580230b6afc984/znsl4388.pdf` supplies a substantially clearer mathematical text extraction, and its complete invoked sections were read too.

**No local PDF or visual inspection is claimed.** Ordinary binary downloads returned HTTP 403, and the screenshot tool returned text placeholders. The author's old PostScript link returned 502; the replacement host did not supply that file. The Springer translation is subscription content and was not accessed. These failures and the successful original-text reading are separately recorded in `sources/FominLulov1995_retrieval.json` and `FominLulov1995_source_check.json`.

The other precise published degree input was freshly rechecked from Guralnick–Katz–Tiep, *Rigid local systems and alternating groups*, Tunisian J. Math. 1 (2019), 295–323, proof of Theorem 9.7, pp. 312–313: <https://msp.org/tunis/2019/1-3/tunis-v1-n3-p01-p.pdf>. The degree-only consequence of Rasala explicitly stated on p. 312 is the part used. The surrounding semisimple-regular-element hypothesis is not imported into the present application. The complete theorem proof was reread; no fresh reconstruction of Rasala's original classification is claimed.

## 2. Single-factor normalizer support

The long-row assumption `1≤k<n/4` prevents a self-conjugate partition, so the ordinary alternating restriction is irreducible on the full Specht space. The previously checked automorphism and Schur argument makes every compatible linear normalizer a scalar multiple of a symmetric-group operator. Its scalar phase does not affect projective support. The standard case `k=1` is correct: every nonidentity permutation has a nonscalar deleted-standard operator, and support at least one equals the claimed bound.

For the nonstandard cases, the degree floor is `a≥n(n−3)/2`. The two tail-two shapes have exactly the displayed degrees. All other shapes in this range satisfy the stated cubic floor. There is no factor-of-two loss from restricting a split constituent. The strict comparison with `4(n+1)` is checked by the positive translated polynomial `x²+19x+52`, where `n=15+x`.

I rechecked the commutator dichotomy directly. A cycle of length at least three admits a transposition of consecutive letters whose commutator is a three-cycle. A nonidentity involution with a fixed letter admits a transposition joining that fixed letter to a moved letter, again giving a three-cycle. Thus the sole remaining case is a fixed-point-free involution. The transposition acts on the actual symmetric extension, so no unproved extension of a split alternating constituent is required.

For any scalar phase `α`, the rank of `[A,B]−I` is at most twice `rank(A−αI)`. Minimizing over `α` gives twice projective support. Equality of the two nontrivial three-cycle eigenmultiplicities gives the exact support contribution `(1−u)a/3`. The previously proved tail-content bound then supplies `β(n,k)a` with the stated denominator.

For the exceptional involution, the factorial prefactor has square

`4^m / binom(2m,m) ≤ 2m+1`.

This follows directly by averaging the binomial coefficients. Together with the strict degree floor, it gives `|χ(g)|<a/2`. The exact two-eigenvalue formula is therefore `ν(g)=(a−|χ(g)|)/2>a/4`, valid also after an arbitrary scalar phase and for either parity of the permutation. Finally `β(n,k)<1/4` follows from monotonicity and the positive translated polynomial `x²+22x+113`. Hence this new involution estimate is stronger than the required common support fraction.

## 3. Full inducing group and actual source budget

The proof keeps the same transitive ordinary-core and original imaginary-field-inclusion hypotheses as the earlier alternating results. Transitivity identifies the labels up to transpose, so all factors have the same support bound. Spectral convolution transfers this bound to factor-preserving tensor operators. A nontrivial tensor permutation has the previously proved quarter bound, stronger than `β`; a nonidentity scalar has full actual moving rank.

Each ordinary factor is real and has an invariant symmetric form. Their tensor core has a unique symmetric-form line. The full inducing group acts on that line by a character. If this character were trivial, its finite orthogonal representation would have real-valued character, contradicting the inclusion of the original imaginary quadratic field in the actual inducing character field. Thus the multiplier is nontrivial without identifying the two coefficient fields.

The actual intermediate-cover factorization gives genus zero, at least twelve genuine inertia points and total moving rank `2e+6`. Product one and generation force at least two inertias with nontrivial multiplier, whose fixed spaces are isotropic and whose moving ranks are at least `e/2`. Applying the support fraction to ten others gives exactly

`β(n,k) ≤ 1/10 + 3/(5e)`.

No dominance is inferred from the number of parameters; this is a necessary consequence of an actual rank-nine period map.

## 4. Strict radical threshold and actual improvement

Put `c=(1−sqrt(3/5))/2`. The exact relations `c(1−c)=1/10` and `1/10<c<1/8` are correct. If `k≥cn`, then `k≥2`, and monotonicity gives the displayed exact rational expression for `β(n,cn)−1/10`.

The multiplication of lower bounds is legitimate because the whole lower bracket `13n/8−2` and the factor `c` are positive. The denominator is positive and strictly below `n²`. Cross-multiplication in the next comparison gives exactly `13n²−151n+48`, whose translation is `13x²+239x+708`. The degree floor makes the final comparison go in the required direction. Thus the claimed strict threshold holds for every `n≥15`, with no omitted finite interval.

I freshly reread the earlier ALT06 formulas when checking strictness. For `(88,12)`, the old minimum is `1519571/15684900<1/10`; the new support fraction is `58/539`. The exact two-row degree is `908791246463100`, and the new support fraction exceeds `1/10+3/(5e)` already at `e=a`, hence at every larger tensor degree. The example proves a strict improvement of necessary inequalities; it asserts no existence of a source with that label.

## 5. Code and independent arithmetic

The full author checker and its final JSON were read. They report 3,820 exact domino-character rows for even `n=16,…,24`, along with the universal polynomial identities and corrected witness. This audit does not claim a fresh execution of that author program.

The separate `audit_alternating_fixed_free.py` imports no author code. Its first implementation was written before the author program was read; the mathematical draft had already been read. Both use the natural signed horizontal/vertical domino-removal recursion. The independent program checks all **15,578** partitions for even `n=16,…,30`, deriving involution character values from that recursion and degrees from hook lengths. It checks the squared exact factorial inequality for every row, and the strict half-trace bound on **158** nonstandard long shapes. It also checks the universal algebraic identities, translated positive polynomials, and rational radical comparisons.

The initial successful output, preserved as `audit_alternating_fixed_free_initial.json`, still used the earlier coarse illustrative witness. The final program was extended to the author's corrected `(88,12)` witness, computing its first-row content squares as a direct finite sum and independently matching both the old and new bounds. It was rerun successfully at **2026-11-21 22:05:08.593213 UTC**, in **0.644287000 seconds**; final output is `audit_alternating_fixed_free.json`. The final proof hash is explicitly asserted. No failed mathematical assertion occurred in either execution.

These computations supplement the universal proof; finite partitions do not establish an all-rank theorem. TeX compilation was not performed or claimed.

## 6. Final scope

All compatible scalar, outer and tensor-permutation operators are retained. The result concerns the actual nonsplit-source gate and the stated ordinary transitive core. It leaves the still-longer shapes and any separately unexcluded standard tensor cases open. It supplies no cycle, no existence theorem for surviving labels, and no new unconditional Markman, Severn or 032 premise.
