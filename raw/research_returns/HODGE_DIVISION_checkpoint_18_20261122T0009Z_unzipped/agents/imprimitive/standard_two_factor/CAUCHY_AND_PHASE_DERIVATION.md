# Standard two-factor inequality: contribution and verification record

Author/contributor `/root/imprimitive`, GPT-6 Astra Pro, effort inherited/not exposed, run `HODGE_DIVISION`,2026-11-21. The root is writing the canonical combined HD-AST07–09 proof. This note records the exact independently contributed Cauchy argument and the checked root phase/source arguments. It is not an independent-origin audit of the whole joint result.

Let `U` be the deleted permutation module of degree `a=n−1`, let `x,y∈S_n`, and let `c,d` count their cycles. Put `K=2n−c−d` and `e=a²`. Assume `K>0`.

## Independently derived Cauchy lemma

Every eigenvalue multiplicity `m` of the full letter permutation module for `x` is at most `c`, because each cycle contributes at most one occurrence of a prescribed root of unity. Its total multiplicity is `n`. Thus the sum of its squared multiplicities is at most `cn`.

Passing to `U` removes one occurrence of the eigenvalue one, whose old multiplicity was `c`. Hence

`sum_z m_Ux(z)² ≤ cn−2c+1 = (n−2)c+1`.

For any target eigenvalue `lambda`, the multiplicity on `Ux⊗Uy` is the scalar product of the two multiplicity functions, with one translated/inverted on the finite group of roots of unity. Cauchy–Schwarz and the arithmetic–geometric mean give

`F_lambda ≤ sqrt(((n−2)c+1)((n−2)d+1)) ≤ (n−2)(c+d)/2+1`.

Consequently **every scalar target**, without a reality or phase assumption, has moving rank at least `(n−2)K/2`. When `K≥n`, this is at least

`((n−3)K+n)/2`.

This argument was derived independently and sent to root before its stronger final formulation. It avoids the otherwise unnecessary all-order composite-scalar edge analysis in that range.

## Verification of the remaining root argument

Suppose `K<n`, and put `L=n−K>0`. For a nonreal target, rationality pairs its eigenspace with its distinct complex conjugate, so its multiplicity is at most `e/2`. This is stronger than the desired estimate, since the right side at `K=n` is `(e−1)/2` and its coefficient in `K` is positive for `n≥15`.

For target one, set `C=sum_{i,j} gcd(l_i,m_j)` for the two cycle partitions, and `G=n(c+d)/2−C`. The exact moving rank on the deleted tensor is `(n−2)K/2+G`. The edges from fixed letters to nontrivial cycles give `G≥(f_y k_x+f_x k_y)/2`. Using `f_x≥n−2k_x`, `f_y≥n−2k_y` and `4k_x k_y≤K²` gives `G≥K(n−K)/2≥L/2`. Thus the stronger desired bound holds.

For target minus one, let `u,v` count the odd cycles. Define the edge weight

`w(l,m)=(l+m)/2−gcd(l,m)·1[2 divides lcm(l,m)]`.

Odd–odd edges have weight at least one, odd–even edges at least one half, and even–even edges nonnegative. Therefore `sum w≥(u d+v c)/2`. Subtracting the two deleted trivial summands shows that the gain above `(n−2)K/2` is at least

`1+[u(d−2)+v(c−2)]/2`.

If `c,d≥3`, then `u+v≥2(c+d−n)=2L` and this gain is at least `L+1`. If the smaller cycle count is two, then `L≤2` and the gain is at least one. If the smaller count is one, then `L=1` and the other permutation is the identity: the deleted spectrum of an n-cycle has all nontrivial n-th roots once, so its tensor with the identity verifies the needed gain directly. Each case gives gain at least `L/2`. These are complete parity cases; no extrapolation or untested target is used.

Thus the joint universal result is

**`nu(Ux⊗Uy) ≥ ((n−3)K+n)/2` for every nonidentity tensor permutation.**

I also checked the root's longer composite-order edge argument independently: an unmarked equal-length edge has weight its positive length; unequal lengths differing by at least two give weight at least one; consecutive unequal lengths have gcd one and weight at least three halves, except lengths one and two, which only cause a half-edge for target order two. This check is retained as an alternate derivation, not required by the simpler proof above.

## Verification of the actual all-field source consequence

For a transitive two-factor core on `U⊗U`, the actual intermediate genus/rank argument gives genus zero, at least twelve genuine inertias and `D=2e+6`, since `e>6`. This geometric reduction does not use the original imaginary quadratic field or its conductor.

Product one and transitivity force a positive even number of swaps. Four swaps and eight other genuine marks already give `D≥2e+6a`, so exactly two swaps remain. No special scalar phases need be located.

A weighted swap with cycle-product index `k_h` has moving rank at least `e/2+a k_h/2−a`, for **every** scalar. This follows from the actual swap multiplicity formula and `nu(Uh)≥ind(h)−1`; it is valid even if the product is the identity. A non-swap with nonidentity underlying permutation pair contributes at least `A'K+B'`, with `A'=(n−3)/2`, `B'=n/2`. A genuine scalar contributes full degree and also satisfies that bound.

The actual transitive degree-`2n` quotient cover gives `N+H≥2a`, where `N` sums the non-swap permutation indices and `H` the two swap-product indices. Since `a/2−A'=1>0`, summation gives

`D≥e+A'(N+H)+10B'−2a≥2e+a+5>2e+6`.

This verifies the all-field conclusion, including Eisenstein fields, with no identification of original and inducing character fields. The canonical root proof still requires the separate whole-proof reader announced by root.

## Exact tests and honest scope

- `test_standard_index.py` tested the original stronger-looking coefficient pair `A=(n²−3n+1)/(2n)`, `B=(n−1)/2`. All478,097 unordered partition pairs for15≤n≤20 passed every exact scalar eigenspace comparison. Actual completion22:42:58.103057UTC,12.87690454s. Output `standard_index_test_15_20.json` is preserved unchanged.
- `test_standard_strong_index.py` tested the improved uniform bound above on the same full finite set. Actual completion22:46:01.231212UTC,12.020758151s,allPASS. Output `standard_strong_index_test_15_20.json`.

For even n equality is attained by two fixed-point-free involutions. For odd n in this range the minimum gap is one half, attained by transposition tensor identity. Both programs use exact integer spectral convolutions and compare the largest multiplicity over all target eigenvalues. Off-spectrum targets have full moving rank automatically. There was no failed assertion or counterexample. The universal proof is the argument above, not an inference from these finite tests.
