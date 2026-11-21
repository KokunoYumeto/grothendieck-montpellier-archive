# DP36: the genuine-pair weight quantization and a conditional kernel estimate

Run DP_MULT_20261121. Date 2026-11-21 UTC. Author /root, GPT-6 Astra Pro; effort setting not exposed. This is a proved analytic implication from explicit hypotheses on the actual pair. It is not a construction of a normalized theta section and does not assert optimality of the resulting kernel bound.

## 1. Statement and hypotheses

Let p be odd, h≥2, q=p^h, d=h−1, and k a perfect field containing F_q. Work over R=W(k), K=R[1/p], with v_p(p)=1. Let G be the Honda line with logarithm L_0 and inverse E_0 as in DP2/DP32, and let H=G^D have the actual integral model of DP32, logarithm L_H, inverse E_H. The coordinates on H are indexed i=1,…,d. Put

s=1/(p−1), ρ=1/(q−1), r_0=ρ, r_i=s−p^iρ.

Let ζ∈R be a primitive (q−1)st root. Let β(x,y_1,…,y_d)∈K[[x,y]] satisfy:

1. β vanishes on x=0 and on y=0, and has no bidegree-(1,1) monomial (x-degree1, total y-degree1).
2. β(ζx,ζ^(−p)y_1,…,ζ^(−p^d)y_d)=β(x,y).
3. The exponential addition coboundaries

C_X=exp(δ_x β(L_0(S),L_0(S'),L_H(T)))

and

C_Y=exp(δ_y β(L_0(S),L_H(T),L_H(T')))

are integral units with constant coefficient1. In δ_y, the vectors y,y' are added in additive logarithm coordinates. The substitutions then use the actual integral laws of G and H.

All coefficients have integer valuations, because the coefficient field is the fraction field of W(k). We keep the no-(1,1) condition explicit to match the source interface, although the stated torus symmetry already excludes it.

For an integral formal series U in the original group coordinates and σ∈{1,−1}, put

Θ(x,y)=U(E_0(x),E_H(y)) exp((σ/2) β(x,y)).

Then for every multiindex a=(a_0,…,a_d),

v_p(a! [x^a_0 y_1^a_1 … y_d^a_d] Θ)
≥γ_0 a_0 +sum_(i=1)^d γ_i a_i −sum_(i=0)^d s_p(a_i)/(p−1),

where

γ_0=s−pρ, γ_i=p^(i+1)ρ−1.

This is a sufficient estimate. The γ_i for i<d are negative; no claim is made that the actual coefficients have negative valuation or that these constants are optimal.

On the specific linear path x=t, y_d=εt, y_i=0 for i<d, with ε∈R^×, it gives

v_p(n! [t^n] Θ(t,0,…,0,εt))≥ρ n−s_p(n)/(p−1).

The leading coefficient in this sufficient diagonal estimate is ρ=1/(p^h−1), which decreases with h. It must not be confused with the increasing derivative slope c_h for an arbitrary integral formal function. At h=2 the coordinate weights are equal and this recovers the familiar scalar residual ρ_2.

## 2. The genuine-pair quantization identity

For a monomial x^a y^b, torus invariance says

a−sum_i p^i b_i is divisible by q−1.

Its weighted degree for the weights (r_0,r_1,…,r_d) is

r_0 a+sum_i r_i b_i
=ρ(a−sum_i p^i b_i)+s|b|∈s Z.

All r_i are positive. Hence every nonconstant invariant monomial has weighted degree at least s. The same statement holds when the x-variable is duplicated, or when all the y-variables are duplicated: add their exponents with the same torus characters. Integral coefficients can only increase the lower bound, since their valuations are nonnegative integer multiples of1=(p−1)s.

The group laws, logarithms and exponentials are equivariant for the indicated Teichmüller actions. For H this follows directly from the monomial-cycle logarithm in DP32, also with the negative powers of ζ. Therefore C_X,C_Y inherit torus invariance. Their differences from1 have positive ordinary degree and integral coefficients, so their weighted valuations are at least s.

This explains why the two-scalar test in DP28 failed while the actual pair admits quantization: the actual dual has weights r_i, rather than another copy of the scalar radius ρ.

## 3. From the coboundaries to β

For a formal series A write w_r(A)=inf(v_p(A_a)+sum_i r_i a_i), with repeated variables given the corresponding repeated weights. The inverse estimates DP2 and DP32 give w_r(E_0)≥r_0 and w_r(E_(H,i))≥r_i. Substitution of these series preserves the lower weighted bounds. Thus

C_X(E_0(x),E_0(x'),E_H(y))−1

and its Y analogue have weight at least s. Taking formal logarithms proves

w_r(δ_xβ)≥s, w_r(δ_yβ)≥s.

Indeed, for weight at least s, the mth logarithm term has weight at least ms−v_p(m)≥s. The inequality v_p(m)≤(m−1)/(p−1) follows by writing m≥p^v_p(m) and summing the geometric series. No analytic convergence is needed; at each total degree the formal expansions use finitely many terms.

Take a monomial x^a y^b in β. Its x-degree and total y-degree are both positive, and they are not both1. If a≥2, an interior binomial coefficient binomial(a,j) of p-valuation at most1 appears in δ_xβ. This elementary fact follows by a nonzero base-p digit when a is not a p-power; if a=p^e, choose j=p^(e−1), giving valuation1.

If a=1 and |b|≥2, split the y-multiindex. When at least two components of b are nonzero, send one complete positive component to the first vector and the other components to the second; the resulting coefficient is1. When b is supported on one component, choose the preceding one-variable binomial coefficient of valuation at most1. In each case the selected coefficient of a coboundary is exactly that multiplier times the coefficient of β, with no contribution from another monomial, because recombining the split multiindices determines the original exponent uniquely.

Consequently w_r(β)≥s−1.

## 4. Exponentiation and the factorial estimate

Every monomial in β has positive weighted degree at least s by §2. Increasing every coordinate weight from r_j to p r_j adds at least (p−1)s=1 to the weight of every coefficient. Thus

w_(p r)(β)≥s.

The scalar σ/2 is integral because p is odd. Formal exponentiation therefore has nonnegative weighted valuation, since the mth term has weight at least ms−v_p(m!)≥0. The integral factor U(E_0,E_H) also has nonnegative weight: the original inverse bounds hold at r, and increasing positive weights preserves them. Hence

v_p([x^a_0 y^a]Θ)≥−p sum_(i=0)^d r_i a_i.

Adding the exact factorial identity gives the asserted estimate with γ_i=s−p r_i. For i≥1 this simplifies to p^(i+1)ρ−1; for i=0 it is s−pρ.

On the stated diagonal path, assign t weight p r_d. We have r_d≥r_0: (p^(h−1)−1)/(p−1)≥1, with equality at h=2. Both nonzero substitutions therefore have at least their required weights; all other coordinates are set to zero. The kernel has nonnegative weight in t and the final factorial coefficient is bounded below by (s−p r_d)n−s_p(n)/(p−1). Since s−p r_d=ρ, the displayed path estimate follows.

## 5. Meaning for the remaining question

This is an explicit extension of the analytic weight-and-coboundary argument to the actual 1-by-(h−1) Cartier-dual model. It is stronger information than the former vague requirement to generalize a two-letter logarithm. It restores the quantization identity with the correct unequal weights and states exactly which coefficient functional is bounded.

It does not establish that the prescribed geometric theta expression satisfies these hypotheses, that the chosen path is the source's path, that this sufficient bound is optimal, or that no sharper primitive-class calculation is possible. In particular, a decreasing sufficient coefficient does not upper-bound actual geometric gain. The next datum remains the exact normalized Poincare/theta cocycle, its frame/period identity and the global cost calculation.

## Check status

The root derived the argument by redoing the source quantization and binomial-extraction mechanism with the actual-dual inverse weights. Complete saved-proof and independent checks are to be recorded after those readings occur. This note is not a Lean formalization.
