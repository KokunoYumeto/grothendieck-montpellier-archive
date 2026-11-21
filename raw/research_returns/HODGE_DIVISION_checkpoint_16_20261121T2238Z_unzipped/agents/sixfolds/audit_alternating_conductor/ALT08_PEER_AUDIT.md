# Independent whole-proof audit: HD-ALT-08

**Verdict: PASS, with one completed footer precision and no theorem repair.**

Reviewer: GPT-6 Astra Pro, `/root/sixfolds`; inherited reasoning effort is not exposed. The entire proof, author checker and output, and the relevant complete dependency sections were read. The proof was independently reconstructed and supplemented by separately authored exact arithmetic and hook-length code. No author code was imported.

## 1. Reviewed versions and exact scope

The first completely read version of `research/ordinary_alternating_conductor_section.tex` had SHA-256

`1a59912868a5604bfde96ecf117465ff9ae6efea18f39fcd3ae47d446065a4e2`.

The sole requested precision was in the framework footer. A nonreal one-dimensional scalar character is defined over its cyclotomic field; restriction of scalars produces a rational representation class, generally of larger dimension. The original phrase about a scalar line in the rational representation lambda-ring could suggest otherwise. The author made exactly this wording change, with every theorem and display unchanged. The final footer was reread, and the final reviewed proof hash is

`53a5c7f3433579520265800de4a44ee706f5a9e573c54936818beff02fadb2b8`.

The complete `research/check_alternating_conductor.py`, its full original JSON result, and the preserved initial root record were read. The complete HD-ALT-07 section `ordinary_alternating_fixed_free_section.tex` and HD-ALT-03 section `ordinary_alternating_sharp_obstruction.tex` were reread, including their stated source boundaries. The theorem concerns the transitive ordinary alternating-core setting and actual rank-nine **sixfold** sources. It makes no claim for projective or spin cores, arbitrary finite groups, or construction of a source.

## 2. General-label rational and scalar interface

After transposition, a remaining long label has first row `n−k` with `k<n/4`. It cannot be self-conjugate, so its ordinary Specht module restricts irreducibly to `A_n`. It has the ordinary rational symmetric-group realization used here. The represented `A_n` is faithful: the kernel is normal in the simple group and the representation is nontrivial. Its projective kernel is also trivial, because a scalar image of the whole perfect group would be trivial.

Transitivity identifies the factor labels up to transpose. The restrictions of transposed Specht labels agree, so the same long-label symmetric extension may be chosen for each factor. Any difference of sign extensions is absorbed into the scalar coordinate. Thus the normalizer decomposition is into a scalar and an element of one fixed finite rational tensor-wreath group, rather than an unrelated rational structure chosen separately for each inertia.

A scalar in this tensor-wreath image cannot permute the distinct represented simple factors. For each remaining factor, the implementing symmetric permutation must centralize the faithful represented `A_n`. The centralizer is trivial, by the argument checked in HD-AST-04. Consequently the tensor-wreath image contains no nonidentity scalar. This proves uniqueness and multiplicativity of the scalar coordinate for the general label too.

The resulting inclusion is precisely

`K ⊂ F ⊂ Q(ζ_M)`.

Nothing identifies the original quadratic field with the full inducing character field. The conductor criterion and cyclic quotient argument then give two scalar marks of order with totient at least `h`, with `h=4` in the dyadic case or `h=p−1` for an odd discriminant prime `p≥5`. The characteristic polynomial of the actual rational operator has equal multiplicities on primitive conjugate roots, so each of those two inertias has fixed-space dimension at most `e/h`. No trace estimate for a general Specht character has been assumed.

The cyclotomic and quadratic-conductor source is exactly the Milne source freshly and fully checked for the immediately preceding AST04–06 audit: version 4.03, Chapter V, Example 3.2 p.157, Remark 3.8 p.158, Examples 3.10–3.11 p.159. The companion `PEER_AUDIT.md` records the primary URL, page images, and source-status boundary. No second full audit of upstream reciprocity is claimed.

## 3. Inherited support and actual-source interface

The full HD-ALT-07 proof was reread. Its support fraction is

`β(n,k)=k(n−1−k)/((n−1)(n−2))<1/4`.

That statement concerns projective support and permits all scalar phases. Tensor spectral convolution preserves the bound for factor-preserving operators. Genuine factor permutations satisfy the stronger quarter bound; nonidentity scalars move the full inducing space. Therefore it applies to each of the other ten genuine inertias without an assumption that those entries preserve each tensor factor.

The previously reviewed intermediate-cover and actual period-factorization argument gives genus zero, at least twelve genuine inertias, and total moving rank `2e+6`. Combining it with the two arithmetic marks gives exactly

`2e+6 ≥ 2(1−1/h)e + 10β(n,k)e`,

equivalently `β(n,k)≤1/(5h)+3/(5e)`.

The support theorem, published Fomin–Lulov estimate used inside it, and precise low-degree classification consequence remain identified previously reviewed inputs. Their complete dependency proofs were read here; no fresh full reading of the Fomin–Lulov or classification primary papers is claimed by this audit. Likewise the actual-source interface is not replaced by a finite group dimension argument.

## 4. The strict long-row threshold

Set `c=(1−sqrt(1−4/(5h)))/2`. Then `c(1−c)=1/(5h)` and `0<c<1/16` for `h≥4`. The strict upper bound follows from monotonicity of `x(1−x)` on `[0,1/2]` and `15/256>1/20`.

If the asserted long-row threshold fails, then `k≥cn`. All comparisons in the proof have positive denominators in the stated range `n≥15`.

### Standard label

When `k=1`, one has `cn≤1`, and thus `c(1−c)<1/n`. The separate single-standard exclusion forces at least two tensor factors among the remaining cases, hence `e≥(n−1)^2`. Therefore

`β(n,1)−c(1−c) > 1/(n(n−1)) > 3/(5(n−1)^2) ≥ 3/(5e)`.

The strict middle inequality is `5(n−1)>3n`, valid here. The standard exception has been handled explicitly; it is not hidden in the nonstandard dimension bound.

### Nonstandard label with cn≤1

When `k≥2`, the inherited degree consequence gives `e≥n(n−3)/2`. The function `β(n,k)` increases on the required interval. Since again `c(1−c)<1/n`,

`β(n,k)−c(1−c) > 2(n−3)/((n−1)(n−2))−1/n > 1/(2n) > 6/(5n(n−3)) ≥ 3/(5e)`.

The two strict comparisons reduce to `n²−3n−6>0` and `5(n−3)>12`. These hold for all `n≥15`; the first becomes `x²+27x+174` at `n=15+x`.

### Nonstandard label with cn≥1

Direct subtraction gives the exact identity

`β(n,cn)−c(1−c)=c((2−3c)n−2+2c)/((n−1)(n−2))`.

The assumptions `c≥1/n`, `c<1/16`, and the positive bracket yield the strict lower bound `(29n−32)/(16n³)`. This exceeds `6/(5n(n−3))`: clearing positive denominators gives `49n²−595n+480`, which is `49x²+875x+2580` at `n=15+x`. This completes all cases and contradicts the finite-degree inequality. There is no asymptotic cutoff or table extrapolation.

After the initial transposition the long row is strictly longer than the column in this range, so translating `k<cn` into the displayed maximum of first row and first column is valid.

## 5. Strictness and field scope

The discriminant choices give `h=4,6,10,18,42,66,162` for the seven stated non-Gaussian, non-Eisenstein class-number-one fields. The first threshold is `(1+sqrt(4/5))/2`; increasing `h` strengthens it. Neither a Gaussian `h≥4` nor an additional Eisenstein exclusion is inferred.

For `(94,6)` at `n=100`, I independently calculated the hook-length degree `1116764880`, agreeing with the binomial difference. Its lower support fraction is `31/539`, strictly below `1/10` and above `1/20+3/(5e)` even at the single-factor degree. Thus it satisfies the previous numerical gate at every tensor degree and violates the new dyadic gate at every tensor degree. It is neither standard nor tail two. The strictness assertion is correctly a comparison of necessary inequalities, not a curve or source construction.

## 6. Independent exact certificate

`independent_alt08.py` and `independent_alt08_checked.json` are adjacent to this report. The complete script and full output were read after its first successful run. The implementation uses its own sparse integer polynomial arithmetic and individual Young-diagram hook lengths; it does not import the author's code or SymPy.

Actual execution: **2026-11-21 22:29:12.302870 UTC**, runtime **0.1175192890004837 s**, **PASS**. The certificate is bound to final proof SHA `53a5c7f3…fadb2b8`. Script SHA:

`a7689dad49475723489981d7f7f46be7b3de6fb274d8c8524ba2e884036c4a8f`.

The certificate checks the universal formal difference identity, positive shifted polynomial coefficients, 1,068 individual hook dimensions for long labels at `15≤n≤40`, and 252,746 exact integer threshold inequalities for every integer `4≤h≤80`, including samples near `5h` and beyond `10h`. Radical comparisons are converted to the exact inequality `5h k(n−k)≥n²`, valid on the tested interval. No numerical rounding is used. The hook witness `(94,6)` is separately reconstructed.

These finite checks supplement the proof. They do not prove the universal low-degree classification, normalizer theorem, source interface, or existence of any source. The author's 13,740-comparison result was read as an author execution, not rerun by this reviewer. The author separately reported a final-hash rerun after the footer change; its status is not represented as a reviewer computation.

## 7. Final disposition

The full theorem, actual-source arithmetic interface, and every strict estimate pass. The sole requested adjustment was the completed scalar-field footer wording. All theorem statements and displayed equations are unchanged. Canonical promotion in this precise scope is supported.

Final report time and all file hashes are recorded in the adjacent manifest and the reviewer check register.
