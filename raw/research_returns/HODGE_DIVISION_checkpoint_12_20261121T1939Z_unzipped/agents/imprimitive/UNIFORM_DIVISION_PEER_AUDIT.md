# Whole-proof audit of HD-U and HD-U6

Run HODGE_DIVISION; 2026-11-21, approximately 12:24--12:26 UTC.
Reader `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed.

**PASS.** I read the complete `research/uniform_division.tex` and reread
the full HD-WQ proof in `research/gaussian_fourfold.tex`. The latter
explicitly retains the supplied Theorem W, Steps 1--4, as an input.

The eigenvalue identity is exact: factoring out `bar(a)^(2n)` gives
`1+r^(2n)-r^j-r^(2n-j)=(1-r^j)(1-r^(2n-j))`. The non-torsion ratio
therefore separates the desired eigenvalue from every other character
summand. All eigenvalues are rational algebraic integers. The polynomial
in the sum of the two actual pullbacks is consequently an integral
correspondence equal to the stated integer multiple of the Weil projector.

For an n-dimensional cycle on a 2n-fold, pullback by a scales degree by
`deg(a)/Nm(a)^n=Nm(a)^n=q`. Each factor of the polynomial has weighted
coefficient mass at most `2q+abs(alpha_j)`. Expanding into effective signed
cycles bounds the sum of the two degrees by kappa times D; in particular
each sign is bounded by that quantity. Thus no unjustified passage from
a per-sign bound to a smaller total bound occurs. The estimate
`abs(alpha_j)<=2q` gives both `kappa<= (4q)^n` and `R<= (4q)^n`.

The Gram discriminant `H=4q^2-s^2` is strictly positive: equality would
make `a^(2n)` real and hence make `a/bar(a)` torsion. In HD-WQ the inverse
Gram identity, the integer multiplier `delta*H*d`, and the two squared
dual-functional norms are all correct. Its use of signed integral cycles
requires no rational cancellation in the cycle group.

The multiplier estimate becomes
`4 delta 16^n q^(2n+2) D^2/(n!)^2`, and the per-sign degree estimate becomes
`8 delta 16^n q^(2n+2) sqrt(T) D^2/n!`. The second coefficient dominates
the first. Since `ceil(sqrt(T))>=1`, it also bounds the multiplier even
when T is a small positive rational. The scalar ceilings are exactly
1024, 5462 and 21846 for n=2,3,4. Replacing q by `Q^n` gives the exponent
`2n(n+1)`.

The proposed integral endomorphism belongs to the prescribed order:
`a=f(2+sqrt(-m))` lies in `f O_K`. Its norm is `f^2(m+4)`.
In nonexceptional imaginary quadratic fields, a nontrivial real and
imaginary part excludes the only possible roots of unity, plus or minus
one. In the Gaussian and Eisenstein fields the real parts of the ratio
are respectively 3/5 and 1/7, excluding their larger root groups.

Finally I independently multiplied all exponents. For sixfolds,
the norm factor contributes `f^48(m+4)^24`; the squared detector bound
contributes `2^648 d^114 f^144 Delta^12`. With `5462<2^13`, these give
`2^661 delta ceil(sqrt(T)) (m+4)^24 d^114 f^192 Delta^12`.
For fourfolds, the corresponding factors are `f^24(m+4)^12`,
`c_K^2 2^648 d^114 f^192 Delta^24`, and `2^10`, giving precisely
the printed bound with conductor exponent 216. The eightfold exponent
40 and the factor `(7f^2)^40` are also correct.

This audit verifies the uniform division step and its substitutions. Its
geometric detector premises retain the separate statuses of HD-CM6,
HD-COMP and the G34 construction, and its semiregularity input retains
the explicitly authorized Perry preprint status.
