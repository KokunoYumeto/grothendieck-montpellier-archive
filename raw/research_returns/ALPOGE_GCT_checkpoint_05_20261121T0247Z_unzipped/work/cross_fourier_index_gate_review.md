# Independent whole-proof review: P-F34

Reviewer: GPT-6 Astra Pro, inherited/undisclosed effort, `/root/bridges`.
Completed: 2026-11-21 01:47:43 UTC.
File: `positivity_fourier_index_gate.tex`.
Outcome: **PASS**. The coefficient-norm estimate remains explicitly unproved.

## Fourier normalization and literal indices

For period L, the transform P_rho=(1/L)sum rho^r q_r inverts to q_r=sum rho^(-r)P_rho. Thus the term with rho=zeta has its pole at t=zeta. A polynomial of degree a contributes a pole of order a+1 there; other roots are analytic there. The actual simple pole from P-F31 therefore makes this Fourier polynomial a nonzero constant. The ratio (1-t^M)/(1-t/zeta) tends to M, so the constant is C_n(zeta)/M, with the stated orientation and factor.

The rho=1 term is the constituent average and is intrinsic: passing to a common multiple of two periods repeats the unique constituent polynomials. The binomial basis identifies it exactly with the principal part at one, not with an arbitrary asymptotic average. The quotient dimension is m-n^2+1, and therefore its degree is m-n^2=binomial(n,3).

If all constituent values at x are nonnegative, the Fourier triangle inequality bounds the constant amplitude by their average. A positivity shift p gives nonnegative constants q_r(p); a strict saturation shift s gives positive q_r(s+1) for every nonzero constituent and zero for zero constituents. Relabeling residues under a shift does not change these all-constituent statements. Thus both necessary inequalities are exact. They are not presented as sufficient conditions or as equivalences to either index hypothesis.

## Absolute value in the specified complex embedding

The chosen xi=zeta^(-g) induces precisely the desired grading parameter, because g gamma=3 and 3S0=1-(-2)^n is congruent to one modulo M. It is primitive since g is odd. Inverting eigenvalues for the cotangent/point-action convention preserves absolute values, so the moving cubic/adjoint determinant ratio is correct.

The n chain weights are pairwise distinct. Every off-diagonal adjoint factor is consequently nontrivial and has modulus at least 4/M. Exactly n cubic monomials are fixed. Among the first q=floor(n/2) variables, exactly q-1 chain monomials are fixed, leaving L_q=binomial(q+2,3)-(q-1) moving monomials. Their integer weights have absolute value at most 3*2^(q-1). Multiplication by the primitive-root exponent g<=3 and |1-exp(i theta)|<=|theta| gives the displayed upper bound 9*pi*2^q/M. All remaining denominator factors have modulus at most two.

I recomputed the logarithmic combination. The numerator contributes -n(n-1)(n-3). Replacing L_q denominator factors by the smaller bound contributes L_q(n-q-log2(9*pi)); the other factors and the additional division by M leave exactly -m+1. This is the stated P-F34r, with no missing n or M factor.

For n>=10, L_q>=q^3/6>=(n-1)^3/48, and the multiplying term is at least n/2-5>=0. Expanding gives exactly

`(n^4-125n^3+369n^2-351n+106)/96`.

At n>=250, n^4-125n^3>=n^4/2 and the remaining quadratic is positive. Hence the lower bound 2^(n^4/192) holds. This is a complex absolute-value estimate, independently of the cyclotomic valuation.

Finally, |B(x)|<=U max(1,x)^D for x>=0 gives the displayed necessary lower bounds. Under the additional unproved estimate U<=2^(C n^3 log2(n+2)), the positive logarithm can be divided by D<=n^3/6 to yield n/32-6C log2(n+2). It eventually exceeds zero, permitting removal of max(1,p). Every conditional quantifier is correct. No claim about U was inferred from f(0)=1, finite coefficient samples, normality, or Gorenstein reciprocity.

The precise source index conventions were freshly read earlier in this review run from GCT VI, Definitions 1.2.2 and 1.2.4, printed pp.13--14, https://arxiv.org/pdf/0704.0229 ; own refs `turn555734407view0`, `turn238082362view1`. The new Fourier and amplitude calculations are proved directly in the file. No correction was required.

## Sharpened amplitude addition P-F34t–u, 2026-11-21T01:59:56Z

Read the entire appended proof and reconstructed it independently. Grouping moving monomials by largest nonzero chain index k gives N0=1 and Nk=(k²+3k)/2. The four multiplicity cases prove |b|>=2^(k−2); upper<=3·2^k is immediate. For k<=n−6 and g<=3, g|b|<=M/2; sine bounds yield logarithm k−n+epsilon with1<=epsilon<=7. The closed bulk sum is correct, including n6 boundary. At most C(n+1,2)+4C(n,2)<3n² remaining cubic factors have logarithms bounded byn in absolute value, as do each of the n(n−1) adjoint factors. Together with |Sn−n4/24| and7m, the explicit12n³ error is conservative and valid for n>=6. Finally the limsup gap below1/24 supplies delta>0 and log2(|A|/U)>=delta n4 eventually; D<=n³/6 gives both index lower bounds2^(6delta n), with max1 removed legitimately. PASS. No bound on actual U has been proved, and the file states this explicitly.
