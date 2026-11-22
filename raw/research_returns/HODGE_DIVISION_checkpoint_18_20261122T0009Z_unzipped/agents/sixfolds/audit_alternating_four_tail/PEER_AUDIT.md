# HD-ALT10 independent whole-proof audit

**Result: PASS as the stated numerical corollary, conditional on the
three-box premises establishing k>=4.** This review does not promote those
pending premises and does not count the corollary as separate movement.

Reviewer: GPT-6 Astra Pro, `/root/sixfolds`; inherited reasoning effort is
not exposed. I read the entire frozen proof
`research/alternating_four_tail_integer_cutoffs_section.tex`, SHA256
`3bcc1ca3a7e59f91cb9e46618d5fb8d05244a503a588c69610960e364485b75a`,
every line of the author's checker, and all of its actual output.
No mathematical repair is requested.

## Input scope

The proof uses the already accepted ALT07/08 inequalities with the
actual inducing degree e and the correct lower degree bound. Their
complete current sections were reread in my immediately preceding
HD-ALT09 audit; ALT08 also has my earlier separate whole-proof audit.
The original imaginary quadratic field need only be contained in the
inducing character field. No equality of these fields, no projective
alternating-module extension, and no Eisenstein case is inserted.

The step from the earlier tail bound to k>=4 is explicitly conditional
on the stated all-count three-box exclusions. The root assignment and
the reviewed status paragraph both retain their pending review status.
I did not independently audit those new hook/mixed exclusions in this
event. Once they are accepted in precisely this ordinary transitive-core
scope, the corollary follows as written.

The cited two-row degree formula is accepted background. I independently
checked its specialization to `(n-4,4)` by the actual hook product,
rather than claiming a fresh full reading of James–Liebeck here.

## Universal proof

For n<=35 the strict ALT07 long-row bound gives k<4. The inequality
reduces to `3*35^2>5*27^2`, with positive quantities on both sides before
squaring. Thus n>=36. The derivative `n-1-2k` is positive on
`4<=k<n/4`; the stronger ALT07 shape bound places k in that interval.
Replacing k by four therefore weakens the left side of the necessary
inequality in the required direction.

With m=5h>=10 and n>=36, every cleared denominator is positive. The
expression F in ALT10.4 is the exact numerator of ALT10.3 after
multiplication by those denominators. Its coefficient in m is positive:
`(n-3)(n-5)>n` implies the positive part exceeds `20n^2`, whereas the
negative part has magnitude less than `6n^2`.

At `m=(n+3)/4`, the inner quadratic simplifies directly to `n-17`.
Thus F becomes

`5n(n-3)(n-17) - (3/2)(n+3)(n-1)(n-2)`.

Expanding gives exactly `(7/2)n^3-100n^2+(531/2)n-9`. Shifting by
36 gives the four positive coefficients `43245,13347/2,278,7/2` in
ascending degree. Therefore F>0 whenever `36<=n<=4m-3`. Since
`3/(5e)<=6/[5n(n-3)]`, this strict inequality contradicts the displayed
necessary inequality. Integrality yields `n>=4m-2=20h-2`.

This is a universal argument for all integer h>=2. It does not infer
universality from a finite table or search.

## Endpoint and numerical optimality

At n=4m-2 the exact numerator is -12. Consequently the endpoint beta
is already strictly less than 1/(5h), independently of the positive
degree correction. The hook degree is
`n(n-1)(n-2)(n-7)/24`; subtraction of the degree floor factors as
`n(n+1)(n^2-11n+22)/24`. It is positive at n=38 and increases in the
relevant range. The universal strict long-row condition holds at n=38
by `3*19^2<5*15^2`, and remains true as n increases.

For completeness, the conductor-dependent stronger shape bound is also
consistent at these endpoints: `4m(n-4)<n^2` for n=4m-2. This extra
check introduces no additional premise or source claim. Every positive
tensor power of the endpoint representation still satisfies the same
numerical inequality and lower degree bound.

The eight rows are correct:

| Quadratic radicand | h | Necessary n |
| --- | ---: | ---: |
| -1 | 2 | 38 |
| -2 | 4 | 78 |
| -7 | 6 | 118 |
| -11 | 10 | 198 |
| -19 | 18 | 358 |
| -43 | 42 | 838 |
| -67 | 66 | 1318 |
| -163 | 162 | 3238 |

The endpoint assertion is optimality only for the displayed numerical
necessary conditions after the accepted exclusions. It asserts neither
existence of an inertia tuple or cover nor actual period rank, dominance,
or detecting cycles. The reviewed text correctly preserves this scope.

## Actual exact computations

The author's first output reports 2026-11-21T23:37:29.194118+00:00,
elapsed 0.04693718400085345 seconds, and 5,896 finite inequalities.
Those are author-reported metadata. I did not rerun or overwrite that
program's output.

My separate `independent_check.py` imports no author code. It expands
the two cubic products by rational coefficient convolution, reconstructs
the shift by binomial coefficients, checks the endpoint numerator,
checks all 257,922 integer pairs for 2<=h<=162, and independently
computes the actual eight hook products. It also checks the stronger
endpoint shape inequalities.

The first independent execution passed at
2026-11-21T23:38:56.991918+00:00, internal time
0.0809750550033641 seconds. Script SHA256:
`0976db4afd619c1a8f3983633e7b705e8318a3c74ec2cbbb551a93610616ee3e`.
All output was read. There was no failed assertion or mathematical
amendment in this audit. The exact output and manifest retain the
conditional-premise and finite-versus-universal distinctions.

**Conclusion:** the complete new numerical proof and table pass. Its
three-box source premises remain external to this particular review;
the result is derived only and is not independent main-gate movement.
