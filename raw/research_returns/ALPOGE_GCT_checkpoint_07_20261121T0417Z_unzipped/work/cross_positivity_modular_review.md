# Independent proof review of P-F11

Reviewer: `/root/bridges`, GPT-6 Astra Pro, effort inherited/undisclosed. Date and completion clock: 20 November 2026, 23:36:52 UTC. Draft reviewed: `work/positivity_modular.tex`, observed SHA-256 `4f89354c935280b3057d24d3410430ad11a72396908bb6ae4d37bf55b33605e6`.

## Verdict

**PASS.** Read and checked the entire proof. The estimate

`p(f) ≤ h + 128 r^3 A^3 < rA + 128 r^3 A^3`

is justified under the stated global quasi-polynomial and nonnegative-numerator hypotheses. This is a targeted proof check by an independent agent. I reconstructed the principal coefficient and error estimates while stress-testing the proposed result, but do not describe the entire review as an independent re-proof or formal certificate.

The only editorial suggestion is to make `r≥1` explicit in the statement; the definition `A=max_i a_i` already presupposes a nonempty list. There is no additional needed hypothesis concerning the sizes of numerator coefficients, the common period, or pairwise coprimality of the weights.

## Checks of the analytic bound

1. **Pole structure.** For relatively prime weights, the only root of unity at which every denominator factor vanishes is 1. All remaining poles have multiplicity at most `r−1`. Each pole's order as a root of unity divides at least one `a_i`, hence is at most `A`; the distinct pole count is at most `sum a_i≤rA`. This does not assume that the common period is small.

2. **Principal coefficient.** In the local variable `z=1−T/zeta`, a vanishing factor is `a_i z u_(a_i)(z)`. Thus at `zeta=1` the order-`r` principal coefficient is exactly `c=1/product a_i`, positive. The chosen partial-fraction convention has no missing phase or sign.

3. **Small-disk estimates.** For `rho=1/(16rA^2)`, the finite geometric sum bounds `|u_a−1|≤a rho`. The inequality `−log(1−x)≤2x` applies because `a rho≤1/16`. Consequently the product of the reciprocal singular corrections is at most `exp(1/(8A))<2`.

4. **Nonvanishing factors.** When `zeta` has order `d` and `zeta^a≠1`, the nontrivial root has angular distance at least `2pi/d` from 1, yielding `|1−zeta^a|≥2sin(pi/d)≥4/d≥4/A`. The perturbation is at most `2A rho`, so the stated lower bound `>3/A` is valid. The special case `A=1` has no nonvanishing factor to which this argument would need to apply.

5. **Laurent-to-Taylor extraction.** Multiplying by `z^m` makes the local function analytic. Contributions from poles other than `zeta` begin in Taylor degree at least `m`; therefore Taylor degree `m−j`, with `j≥1`, is exactly the desired principal coefficient `C_(zeta,j)`. Cauchy's estimate on the pole-free disk gives

   `|C_(zeta,j)|/c ≤ 2 A^(2(r−m)) rho^(−(m−j)) ≤ 2D^(r−j)`.

   The exponent accounting is correct even when `m<r`, and the estimate remains valid for the leading term itself.

## Coefficientwise dominance, not merely positivity of values

For each residue class, write the constituent in the binomial basis supplied by partial fractions. These are real rational polynomials: their values at infinitely many integers in the class are integers, so the expression's polynomial coefficients are real (indeed rational by interpolation).

Set `B_j(n)=binomial(n+p+j−1,j−1)` for real `p>0`. The identity

`B_r(n)=B_j(n) product_(l=j)^(r−1) (n+p+l)/l`

has nonnegative coefficients in every factor. Keeping only the additional factors' constant product yields the coefficientwise inequality in the proof. The factorial multiplier is exactly `(r−1)!/(j−1)!`, and its bound by `r^(r−j)` is in the correct direction. Coefficients above degree `j−1` of the error term vanish, so every degree through `r−1` is covered.

For each possible error order `j<r`, at most `N` roots contribute. Therefore the relative absolute error in any monomial coefficient is bounded by

`2N sum_(k=1)^(r−1) (Dr/p)^k`.

At `p0=128r^3A^3`, the ratio is `1/(8rA)≤1/(8N)`. Extending the finite sum to a geometric series gives at most `2/7<1`. The positive main coefficient dominates the full error, including complex phase cancellations. Thus every coefficient of every constituent is positive. Larger real shifts preserve positivity by substitution with a nonnegative constant.

## Common divisor and numerator handling

Let `d=gcd(a_i)`. The sequence is zero away from multiples of `d`. Its nonzero constituent polynomials are polynomials for the relatively prime reduced weights evaluated at `n/d`. After a real shift `p`, they are the reduced constituents evaluated at `n/d+p/d`. The reduced bound requires only `p/d≥128r^3(A/d)^3`, which is precisely the stated sufficient condition. Positive scaling of the polynomial variable preserves nonnegative coefficients. Zero constituents stay zero. The separate `r=1` case is a periodic indicator with nonnegative constant constituents.

For numerator degree `h`, the coefficient sequence agrees on large indices with the positive convolution `sum_i H_i g(n−i)`. On each fixed residue class this is equality of polynomials because it holds at infinitely many indices; global quasi-polynomiality therefore identifies it with the actual constituent polynomial of `f`. The final shift `P=h+p0` is an integer. Each shifted summand has translation `P−i≥p0`; the residue label changes, but the preceding estimate was uniform in every label. Summing with `H_i≥0` is legitimate regardless of coefficient size.

This step would require an eventual/quasi-polynomial qualification if global quasi-polynomiality were removed. The draft does not remove it.

## Independent check of the referenced degree bound

The use of P-F9's `h<sum a_i` is sound. Here is a direct verification. For a common period `L` and maximal constituent degree `d`, write the generating function as a sum over residues `b=0,...,L−1` of

`T^b sum_(m≥0) f_b(Lm+b) (T^L)^m`.

Each inner sum has denominator `(1−T^L)^(d+1)` and a numerator of degree at most `Ld` in `T`; multiplication by `T^b` keeps the total numerator degree below `L(d+1)`. Thus the rational generating function is strictly proper. In the given nonzero expression `H/product(1−T^ai)`, cancellation cannot change the degree difference. Hence `h−sum a_i<0`, as claimed.

## Mathematical and historical scope

The proof supplies a polynomial positivity-index bound from a positive rational expression with polynomially bounded **number of factors and numerical weights**. A polynomial bit length for `A` alone does not mean the numeric bound is polynomial in the input length. The theorem does not compute a positive expression, its parameters, or all constituents, and does not assert a small period.

The attached GCT VI source explicitly distinguishes positivity of constituent coefficients from eventual positivity of function values (Definition `dintropos1`) and proves a saturation-index bound from a positive form (Lemma `lmodularindex`). Its later paragraph says that PH2 may also follow from PH3. P-F11 addresses the stronger coefficient-positivity issue under its stated quantitative parameter hypotheses. I performed no exhaustive priority search and make no novelty certification.
