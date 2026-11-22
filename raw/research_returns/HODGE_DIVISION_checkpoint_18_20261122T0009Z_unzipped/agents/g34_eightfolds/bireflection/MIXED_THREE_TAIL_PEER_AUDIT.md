# Independent whole-proof audit: HD-MT301–03

**Result: PASS in the stated scope.** I read the complete frozen proof, every line of the author's checker, its full successful output, and the invoked primary character-polynomial statement and proof. I found no mathematical defect or requested repair. The accompanying independent computation also passed its first execution.

Reviewer: `/root/g34_eightfolds`; GPT-6 Astra Pro; reasoning effort inherited/unexposed; run HODGE_DIVISION. Actual independent computation completed **2026-11-21 23:37:54.066909 UTC**. This report is being saved after that completed run; no estimated future completion time is used.

## Frozen objects and scope

- Root proof: `research/alternating_mixed_three_tail_section.tex`, SHA-256 `3073a8ef70d698db8d7ff748ba7df56c1352e24fa1dfbdb1c3c61d54f783f8a8`.
- Root checker: `research/check_alternating_mixed_three_tail.py`, SHA-256 `79195c7c4b2e71b885315bff2b3a617a06561edc9515e4d9fdc0332f55f53a8e`.
- Root successful output: `research/alternating_mixed_three_tail_checked.json`; 22,517 classes, 193,333 exact phase-order entries, 30 actual flag cases.
- My independent implementation and output: `audit_mixed_three_tail.py` and `audit_mixed_three_tail.json` in this directory.

The theorem concerns the ordinary label `(n-3,2,1)` for `n >= 15`. It excludes a single factor over every original imaginary quadratic field, and every transitive tensor count at least two when the inducing character field contains a non-Eisenstein imaginary quadratic field. It includes compatible scalar, outer and factor-permuting actions. It makes no assertion about nontransitive cores or cycle construction, and does not identify the original field with a possibly larger inducing field.

The cyclic-average method originates in the root's preceding HD-AT301 proof. The exact weighted-cycle and actual quotient framework was developed and reviewed in D-ATT07–09. I checked their applications here, but do not call their origin independent of that shared work. My finite reconstruction imports no author code, selected rows, transform, or output data. I had read the author's checker before writing it, which is explicitly disclosed.

## Primary input checked

I freshly opened the published Garsia–Goupil paper, *Character Polynomials, their q-Analogs and the Kronecker Product*, Electronic Journal of Combinatorics **16**(2) (2009), R19, DOI `10.37236/85`:

<https://www.combinatorics.org/ojs/index.php/eljc/article/download/v16i2r19/pdf>

I read Proposition I.1 and its domain on printed p. 2, the complete invoked proof, equations (2.1)–(2.6), printed pp. 9–11, and the relevant row of Table 5.1 on p. 31. The frozen local primary PDF is `sources/GarsiaGoupil2009.pdf`, SHA-256 `f3f9de4eb2d202bb355aa64a479818329f09a5daddbf2fd321915dd2e8f2f0b8`. This event uses extracted text, not a claimed visual rendering.

The table gives exactly

\[
\chi=f(f-2)(f-4)/3-X_3.
\]

As a separate normalization check, the standard `S_3` character `(2,0,-1)` in the published umbral formula yields

\[
\tfrac13((f)_3-3(f)_2+3f)-X_3,
\]

which is the same polynomial. Evaluation at the identity gives the displayed integral degree. The stable-shape domain holds for all `n >= 15`. The non-self-conjugate restriction and rational full normalizer are the previously checked ordinary alternating interfaces; this audit does not claim a new proof of the published representation classification.

## HD-MT301: every target eigenspace

The lower character estimate follows from `3X_3 <= n-f` and the exact identity

\[
f(f-2)(f-4)+f=f(f-3)^2.
\]

It therefore applies to every power, including the identity. Dropping `-X_3` in the upper estimate and dividing the defect by `n-f` gives the stated quadratic `c_f`; its derivative in `f` is positive in the claimed range. The un-divided inequality has both sides zero at the identity, so no division-by-zero argument enters the cyclic average.

For a cyclic group, the average fixed-letter count equals the number of permutation cycles. Thus the average defect yields `a-m_1 >= c I`. For any nontrivial target root, the mean cosine is zero, and each factor `Re(z^-j)-1` is nonpositive. The real character lower bound therefore gives `m_z-m_1 <= b` with exactly the displayed normalization. The trivial target is immediate. This is a bound on maximum-eigenspace codimension, so it remains valid after any scalar twist.

For large index, `c-A=2n/3` gives the exact constant `B` at `I >= (n-2)/2`. For small index, the moved support is at most `2I`, so every power retains at least `f_0=n-2I` fixed letters. The improved coefficient is `c_(f_0)`. Clearing the positive denominators produces exactly the cubic in (MT3.9). Its second derivative is `12-6f`, nonpositive on the stated interval. The two endpoint values are positive, and concavity gives positivity throughout. The interval also includes all relevant integer `f_0`, since the permutation is nonidentity. No dimension inequality is being mistaken for period dominance.

## HD-MT302: actual one-factor source

The rational `S_n` image has no nonidentity scalar because a scalar centralizes the faithful `A_n` image and the permutation centralizer is trivial. The permutation quotient is consequently an actual homomorphism, and its image contains a transitive `A_n`. The resulting degree-`n` cover is connected.

I checked the use of the actual intermediate-cover Euler identity and the marked Hurwitz rank bound. Since the degree is at least 715, genus at least two is impossible; genus one has at most six genuine marks. Rank nine therefore forces genus zero, at least twelve genuine marks, and the exact moving-space budget `D=2a+6`.

Riemann–Hurwitz is applied to the actual connected quotient, giving total natural index at least `2n-2`. Each nonscalar inertia has the proved `AI+B` bound, while a genuine scalar has full moving rank and satisfies it at index zero. The resulting excess is exactly `(6n^2-20n-16)/3`, which is strictly greater than six for every `n >= 15`. This argument needs no conductor or non-Eisenstein restriction.

## HD-MT303: all transitive tensor counts

I checked all of the following interfaces, including the scalar and identity cases.

1. The faithful rational tensor-wreath image meets scalars trivially through its conjugation action on the simple factors. The rational and scalar coordinates are actual homomorphisms. Its natural `nt`-letter action is transitive.
2. The inducing character field lies in the scalar cyclotomic field. A non-Eisenstein imaginary quadratic subfield forces at least two inertia phases outside `mu_6`: otherwise generation or product one fails in the quotient of the scalar image by its intersection with `mu_6`. Equality of fields is unnecessary.
3. Every power of a rational tensor-wreath operator has trace at least `-(b/a)e`. The trace is a product of cycle-product traces; if negative, at least one factor contributes absolute value at most `b` and the others at most `a`.
4. Rational cyclotomic multiplicities give the quarter bound for all marked phase orders other than four. At order four the square-trace bound gives the stated `(3-b/a)e/4` moving rank. Both are valid for the actual marked inertia.
5. A factor-fixed nonscalar entry has at least `(d_0/a)e` support by spectral convolution; a genuine scalar has full rank. A factor-moving entry has the stronger weighted-cycle half bound. The displayed polynomial comparisons `2d_0 <= a-1`, `b <= d_0`, and `d_0 > 97` hold throughout the range.
6. If at least three inertia entries move factors, one is distinct from the two scalar marks. Nine additional genuine entries supply the displayed contradiction. There must therefore be precisely two factor-moving entries. Their inverse factor permutations generate a transitive cyclic group, so they are full cycles.
7. The actual degree-`nt` quotient gives `H+N >= 2n-2`. At a factor-fixed entry, average only over active factors and then enlarge the denominator to `t`; the complete positive constant `B` survives. Scalars are checked separately.
8. At each full factor cycle the exact weighted error is retained. The identity cycle product is allowed because only `nu >= AI` is used there. The errors give `2R_t/a^(t-1) <= 2` for both `t=2` and `t>=3`.
9. Summation yields exactly (MT3.13). The final comparison follows from `9tB >= 18B` and the positive quadratic in (MT3.14). It is strict and contradicts the exact source budget.

The strictness witness `(97,2,1)` is distinct from the previously excluded labels and satisfies the earlier long-row necessary inequality over the Gaussian field. The theorem excludes that necessary family; it does not assert that a source existed there.

## Independent exact computation

The independent checker first derives the polynomial from the published `S_3` umbral input. For every partition of every `n=15,...,29`, it computes power traces and inverts them triangularly in the integral basis of virtual cyclic permutation characters. This differs from the author's Ramanujan transform. Primitive-root multiplicities are then obtained by summing virtual cycle coefficients over divisible lengths.

It checks integrality, nonnegative multiplicities, the degree, the character lower bound, and every target-order support inequality. It passed **22,517 classes and 193,333 phase-order entries**, with least finite margin **16**.

The second reconstruction uses actual actions on flags consisting of a distinguished member of a three-element set. Subtracting the three-subset and ordered-pair actions and adding the letter action gives the relevant virtual character. Complete orbit enumeration for **90 cases** checks **670,200 actual points and 136,388 orbits**, matching the independent triangular inversion. These cases include long cycles, mixed cycles, and complete products of two-, three-, and four-cycles.

Finally it verifies the exact polynomial identities, both concavity endpoints, and eight shifted-positive polynomials. The first and only execution passed, taking **2.408466194 seconds**. No assertion failure or repair occurred. These finite calculations supplement the universal written proofs; they do not replace them or certify an arbitrary Hurwitz rank computation.
