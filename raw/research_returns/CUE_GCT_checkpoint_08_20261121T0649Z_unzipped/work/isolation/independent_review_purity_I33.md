# Independent whole-proof review: I-33

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Recorded event time: 2026-11-21T03:01:35Z.

Scope: complete reading and independent mathematical rederivation of `I33_prime_curves.tex`, including the revised explicit assumptions `n>=1`, integral `delta>=1`, and the retagged equations. I checked the prime-bound inequalities and the numerical subset-sum inequality arithmetically, without running a search for the subsets. I did not independently reopen the newly cited Bisht–Gupta–Volkovich paper, so this review does not certify its bibliographic locators or wider theorem. The construction's proof is self-contained; the AGKS product-closure mechanism was already recorded in the earlier source ledger. This is an independent agent proof review, not a formal certificate or external peer review.

## Verdict: PASS

The prime family detects a difference of two dense separated products over every field, and some member preserves the two-dimensional coefficient span when the products are linearly independent. The explicit failure of the raw family under multiplication and the interpolation repair are both valid and correctly scoped.

## Divisor separation, including positive characteristic

After canceling common factors in each rational function, every nonzero root or pole has integer multiplicity of absolute value at most `delta`. If one chosen prime equals the characteristic, composition with that power map multiplies each nonzero multiplicity by that prime. At the same point, every other chosen power map is separable and unramified away from zero, so all other multiplicities together have absolute value at most `(n-1)delta`. The chosen prime exceeds `2delta(n-1)`, making cancellation impossible. Hence that exceptional factor has no nonzero divisor. Divisor multiplicities are integers, so their being divisible by the characteristic does not make them vanish.

For any other factor, a nonzero divisor pulls back to a coset of a group of prime-order roots of unity, with the same nonzero multiplicity at all its points. A coset for a different prime meets it in at most one point: the quotient of two common points would lie in the intersection of two coprime root-of-unity groups. Each other rational function contributes at most `2delta` such cosets. Thus at most `2delta(n-1)` points can be covered by all competing divisors, fewer than the number in the selected coset. The product cannot be constant. This proves that every rational function is a constant times a monomial, with exponent magnitude at most `delta`.

## Separating exponents and preserving coefficient span

If the base curve kills the difference, the product of the scalar constants is one and the integer dot product of the monomial exponents with the base prime weights is zero. A nonzero multivariate difference has at least one nonzero exponent. Changing only that coordinate's prime changes the formal exponent by the nonzero integer `b_j(q_j-p_j)`. Formal monomials in an indeterminate remain distinct even when this integer is divisible by the characteristic. Zero component products are separately and correctly handled by injectivity of each positive-power univariate substitution.

The rank-two statement follows from the same argument with a constant ratio in place of ratio one. If the original ratio is not a monomial product, the base-curve ratio cannot be constant. If it is a nonconstant monomial product, one of the weight vectors has nonzero dot product with its exponent vector. The two substituted polynomials are therefore linearly independent on some curve. This is exactly preservation of the coefficient-row span of the two-component product row, and does not assert a basis-isolating property.

The weight vectors have full affine span in the integer cocharacter lattice. Encoding their coordinate indicators by logarithmically many bits is genuinely nonlinear, with indicator degree growing with the number of bits; this does not evade the earlier affine or fixed-degree obstruction by an incorrect linear interpretation.

## Prime bound and query count

For every prime at most the even integer `B`, the valuation of the central binomial coefficient is a sum of at most `floor(log_p B)` terms, each zero or one. Thus each prime-power contribution is at most `B`, and multiplying gives the displayed lower bound on `pi(B)`. For `B=16M^2` and `M>=2`, the two elementary logarithmic inequalities yield `pi(B)>=2M`. Removing at most `H` primes leaves more than `2n`, since `2M-H=H+4n+4`. The sieve interval is polynomial in the numerical parameters `n,delta`.

Every substituted polynomial has degree at most `delta sum_i a_i <= n delta B`, so the curve grids and union cardinality are correct. The distinct-scalar extension convention is necessary and is stated. No prime-distribution conjecture or exception for a characteristic prime is used.

## Raw product failure and its repair

At `n=64,delta=1`, the constants are `H=126`, `M=256`, and `B=1,048,576`. Each block of 32 variables has `2^32` subset sums in at most `32B+1=33,554,433` integer values, so a collision exists. Removing common indices leaves a nonzero multilinear binomial with equal prime-weight exponents. Two such binomials on disjoint blocks give a nonzero multilinear product. Every curve changes at most one coordinate, so at least one of the two factors remains zero. Concatenating their width-two diagonal programs through a rank-one constant bridge gives an ordinary width-two ROABP after absorbing the bridge in an adjacent layer.

Interpolating a single curve through the finite hitting-set list makes each nonzero two-product factor nonzero on that curve. Their product remains nonzero in the univariate polynomial domain, even when the factors share variables. The total-degree composition bound `D(S-1)` is exact, and a field with `D(S-1)+1` elements supplies both the interpolation nodes and the final grid because `D>=1`. This repairs the specified raw-family failure and gives the claimed polynomial sampler for products of these factors.

No revision is requested. The proof remains restricted to the stated product class and does not resolve arbitrary noncommuting width-two blocks, sums of three or more products, or general coefficient-matroid preservation.
