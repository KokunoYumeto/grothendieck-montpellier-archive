# Independent whole-proof review: G-16

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T02:52:21Z.

Scope: complete reading and independent rederivation of `g16_fragment.tex`, using the previously reviewed G-10, G-11, G-13, R-14, and highest-weight restriction arguments. I checked the two numerical example dimensions against `r17_fragment.tex`; I did not rerun its finite rank computations or reopen sources already checked for those dependencies. This is an independent agent proof reading, not a formal certification or external peer review.

## Verdict: PASS

The tensor construction selects the claimed nonrectangular representation and supplies stable points for every positive padding exponent. Consequently the previously proved dimension condition yields the stated explicit label family throughout its range, including the region where ordinary rectangular gaps are excluded.

## Exact grading and duals

The projectivized enhanced cone is the Segre–Veronese image of `P(Y) x P(V*)`. Since `a>0`, this gives an irreducible affine cone of dimension `dim(Y)+3`. Pullback of linear coordinates has bidegree `(1,a)`. Products of degree-one coefficient functions span `C[Y]_d`, and every monomial of degree `ad` in the dual-vector parameter splits into `d` monomials of degree `a`. Pairing those factors proves the exact coordinate grading `C[X_Y]_d=C[Y]_d tensor Sym^(ad)V`. This uses the actual coordinate ring generated in degree one, not an unproved projective-normality assumption.

The dual convention is correct. Actual coefficient functions decompose as `S_lambda V*`, so the invariant space is `Hom_SL4(S_lambda V,Sym^(ad)V)`. Restriction of an irreducible polynomial GL4 representation remains irreducible for SL4, and its highest-weight differences equal those of `Sym^(ad)V` precisely for `lambda=(ad+r,r,r,r)`. The fixed size `nd` forces `4r=md`. There is exactly one copy in this Hom space and no competing label. The divisibility condition is therefore exact.

## Stability for arbitrary padding

The chosen weighted Fermat factor is a sum of two binary products and belongs to both degree-`m` determinant and permanent cones by the cyclic pencil. Block padding places its padded form in both degree-`n` cones. The monomial norm formula for the induced symmetric-tensor metric gives `||x_0^a x_i^m||^2=a!m!/n!`; the coefficient squared is `binom(n,m)`, so all four tensor summands have equal norm.

After tensoring by `(e_0*)^a`, their weights are exactly `m e_i`. The trace-free diagonal expectation vanishes. Off-diagonal operators on the first factor connect weights differing by one root, whereas the four distinct monomials differ by `m` times a root. On the second factor the derivative is orthogonal to the fixed pure dual power or is zero. Thus the full moment map vanishes independently of the ratio between `a` and `m`.

For the stabilizer, reducing the infinitesimal equation for `x_0^a q` modulo `x_0` after dividing by `x_0^(a-1)` forces `A x_0` to be proportional to `x_0`. The Fermat equation then forces every off-diagonal entry to vanish, since its mixed monomials are distinct for `m>=3`. The four pure powers force equal diagonal entries, and trace zero forces zero. Stabilizing the projective tensor line implies stabilizing the first factor's line by the tangent equation modulo that line. Hence the projective stabilizer is finite. Kempf–Ness and the reviewed reductive-quotient facts apply, yielding dimensions `u=2n^2-10` and `dim(P_(m,4))-9>u`.

## Quantitative bounds

The ambient dimension is the product of the two symmetric-power dimensions. On SL4, the dual action is the transpose adjugate, so its matrix coefficients have degree three. The representation action degree is therefore `n+3a`. Its Lie algebra representation is nonzero and the Lie algebra is simple, hence the differential is faithful and the algebraic kernel is finite. Derksen's parameters `t=16`, group dimension `15`, equation degree `4`, and action degree `L` give the stated `sigma <= 4L^15` and generator bound `beta=6bL^30`.

The enhanced determinant parameter map has total homogeneous coordinate degree `n+a`, because determinant coefficients have degree `n` in the pencil parameters and the dual-vector power has degree `a`. This is distinct from the group-action degree and is used consistently. The generator-image projective closure consequently has degree at most `((n+a)beta)^u`, by the already reviewed homogeneous image-degree argument with base loci allowed.

Weighted invariant degree at most `d` lies inside ordinary generator degree at most `d`, since all generator weights are positive integers. Chardin bounds the latter by the displayed degree factor times `binom(d+u,u)`. A maximal algebraically independent subset of the common generator images on the larger quotient supplies at least `u+1` generators, giving the cumulative lower bound. The exact binomial ratio is correct, and at the chosen `s_*` its numerator exceeds `(u+1)C` by one. Thus the cumulative inequality is strict. Degree zero agrees on both sides, so the resulting positive-degree gap has the unique extracted label and automatically satisfies `4|md`.

For the progression, the common Veronese scale follows from the already proved generator-grouping lemma. Its determinant quotient has projective dimension `u-1` and parameter degree `(n+a)E`, giving the stated `Q`. Linear Noether normalization on the larger standard-graded quotient gives the lower Hilbert function. The ratio `(k+u)/u` is strictly greater than `Q` at and above `u(Q-1)+1`. Since `E` is divisible by four, every displayed label is integral. All quotient dimensions here are positive, so no zero-dimensional Chardin endpoint is involved.

Finally, `b=O(n^6)`, `L=O(n)`, `beta=O(n^36)`, and `u=O(n^2)` give `log d_*=O(n^2 log n)` uniformly in the stated range. The full-ambient transfer is exactly the previously reviewed four-row highest-weight restriction.

## Examples and scope

R-17 records dimensions `(816,819,802)` for the permanent, padded, and determinant cones at `(m,n)=(15,20)`, and `(969,972,970)` at `(16,22)`. Both satisfy the strict hypothesis. Substitution gives `(35r,15r,15r,15r)` at `d=4r` in the first case and `(10d,4d,4d,4d)` in the second, as written. Every label is nonrectangular because `a>0`. No additional `n<4m/3` restriction remains after the dual tensor factor cancels the padding weight.

No revisions are requested.
