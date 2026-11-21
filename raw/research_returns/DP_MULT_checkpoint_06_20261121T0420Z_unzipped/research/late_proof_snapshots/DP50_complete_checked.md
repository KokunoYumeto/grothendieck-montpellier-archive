# DP50: a p-divisible tensor exponent restores the bare dual-direction slope

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. The parent reserved **DP50**. This proof treats the actual arbitrary-unit singleton/complement display and its primitive Poincaré splitting from DP46. It proves an exact pure-kernel result and a sharp universal lower bound with arbitrary integral prefactors. It deliberately does not assert equality for every prefactor.

## 1. Statement and comparison with a unit tensor exponent

Let `p` be odd, `h≥3`, `q=p^h`, `d=h−1`, and `R=W(k)` for perfect `k⊃F_q`. Put

\[
s=\frac1{p-1},\qquad \rho=\frac1{q-1},\qquad
r_i=s-p^i\rho\quad(1\le i\le d).
\tag{NT1}
\]

Use the actual arbitrary-unit cyclic display line `G`, its actual Cartier dual `H`, the Teichmüller coordinates `S,Y_1,…,Y_d`, and a normalized invariant integral Poincaré frame as in DP46. Write the primitive splitting in additive logarithm coordinates as `β(x,y)`.

Choose `u∈R^×`, a primitive `v=(v_1,…,v_d)∈R^d`, and

\[
j=\min\{i:v_i\in R^\times\},\qquad k_*=h-j,
\qquad S_{k_*}=\frac{p^{k_*}-1}{p-1}.
\]

Let `κ=p^a λ`, where `a≥1` is an integer and `λ∈R^×`. Set

\[
K_\kappa(t)=\exp\bigl(\kappa\beta(ut,vt)\bigr)
 =\sum_{n\ge0}A_nt^n.
\tag{NT2}
\]

Then, for every rational `w≥0`,

\[
\boxed{
\nu_w(K_\kappa)=
\begin{cases}
-\infty,&0\le w<r_j,\\
0,&w\ge r_j.
\end{cases}}
\tag{NT3}
\]

There is an exact coefficient sequence, for every integer `m≥0`:

\[
\boxed{
N_m=p^{k_*}q^m+1,
\qquad
v_p(A_{N_m})
=a-S_{k_*}-r_jp^{k_*}(q^m-1).}
\tag{NT4}
\]

The right side is an integer. In particular,

\[
\boxed{
\liminf_{n\to\infty}\frac{v_p(n!A_n)}n
=s-r_j=\frac{p^j}{q-1}.}
\tag{NT5}
\]

These assertions, including the exact valuations in (NT4), hold in every normalized invariant integral frame of the same primitive Poincaré biextension. Thus one factor of `p` changes the pure-kernel slope from the unit-exponent value

\[
\frac1{(p-1)(p^{h-j}+1)}
\quad\hbox{to}\quad
\frac{p^j}{p^h-1}.
\tag{NT6}
\]

Every further factor of `p` changes the constant valuation in (NT4), but not its asymptotic slope.

For every integral formal function `U`, put

`V(t)=U(E_G(ut),E_H(vt))`.

Then `V K_κ=Σ_n C_nt^n` satisfies

\[
\boxed{
v_p(n!C_n)\ge\frac{p^j}{q-1}n-\frac{s_p(n)}{p-1}.}
\tag{NT7}
\]

This coefficientwise bound does not require `U(0)` to be a unit. It remains valid for a zero restriction, with valuations `+∞`. The slope is optimal as a bound valid for all integral `U`, because `U=1` attains (NT5). We do **not** infer (NT5) for every nonzero integral prefactor: such a prefactor is only known to be bounded at and above `r_j`, and could interact with the first nonconstant kernel coefficients at that boundary.

## 2. The boundary contraction

Put

\[
w=r_j,\qquad \Delta=r_j-\rho>0,
\qquad \omega_0=r_j,\quad \omega_i=r_i\ (1\le i\le d).
\tag{NT8}
\]

The strict inequality uses `h≥3`. Indeed

\[
\Delta=\frac{1+p+\cdots+p^{h-1}-p^j-1}{q-1}>0,
\]

whose smallest numerator, at `j=d`, is `p+⋯+p^(d−1)>0`. All weights are positive.

Choose an integer `e` clearing the weight denominators, adjoin `π` with `π^e=p`, and set

`α_i=π^(eω_i)`, `γ=α_0=α_j`.

The scalar contracted logarithm reduces to the identity, since `r_j>ρ` and every nonlinear line-logarithm term of degree `q^n` has valuation

`(q^n−1)r_j−n>0`.

For the dual use DP40's exact arbitrary-unit path logarithm. Its selected first arrows have degree `p` around the ordinary edges and degree `p²` around the exceptional edge. Their weight defect is exactly one, so each first-arrow logarithm coefficient has valuation zero after contraction. A path through `b≥2` selected arrows has weight increment at least `1+p+⋯+p^(b−1)>b`; after its denominator `p^b` is included, its coefficient has positive valuation. Therefore

\[
\overline{\widetilde L}_G=S,
\qquad
\overline{\widetilde L}_H=\operatorname{id}+M_\eta,
\tag{NT9}
\]

where

\[
(M_\eta)_1=\eta_1Y_d^{p^2},\qquad
(M_\eta)_i=\eta_iY_{i-1}^p\quad(2\le i\le d),
\qquad \eta_i\in k^\times.
\tag{NT10}
\]

The actual integral scaled logarithms have identity linear part, so their inverses are integral. Since `M_η` is an additive polynomial map over the residue field, their reduced dual inverse is

\[
\overline{\widetilde E}_H
=\sum_{b\ge0}(-1)^bM_\eta^{\circ b}.
\tag{NT11}
\]

The sum is well defined in the formal degree topology. No coefficient is required to be Frobenius-fixed: the coefficients in an iterate are the appropriate Frobenius powers of units.

For the contracted additive line, the input to coordinate `i` is `v_i γ/α_i`. If `i>j`, it has positive valuation because `r_i<r_j`. If `i<j`, then `v_i∈pR` and

\[
0<r_i-r_j=(p^j-p^i)\rho<1,
\]

so again its valuation is positive. Exactly the `j`th unit input survives reduction. The scalar input reduces to `\bar u T`. The unique cyclic path from `j` to `d`, followed by any number of full cycles, therefore gives

\[
\overline{\widetilde E}_{H,d}(z(T))
=\sum_{m\ge0}\xi_mT^{p^{k_*-1}q^m},
\qquad \xi_m\in k^\times.
\tag{NT12}
\]

There is exactly one path for each displayed exponent; the exponents are distinct. Hence no cancellation of these coefficients is possible. In the unit-one model, `ξ_m=(-1)^(k_*−1+md) \bar v_j^(p^(k_*−1)q^m)`.

## 3. The full primitive logarithm has a single least weighted monomial

The exact arbitrary-unit ghost formula of DP46 is

\[
\begin{split}
b(S,Y)={}&-
\sum_{i=1}^d\sum_{l,n\ge0}
\epsilon_{i,l,n}
\frac{S^{p^{n+lh+i}}Y_i^{p^n}}{p^{n+l+1}}\\
&+\left(\sum_{b\ge0}A_b\frac{S^{q^b}}{p^b}\right)
\left(\sum_{i=1}^d\sum_{l\ge0}
C_{i,l}\frac{Y_i^{p^{lh+h-i}}}{p^{dl+h-i}}\right),
\end{split}
\tag{NT13}
\]

with all displayed coefficients units and `A_0=1`. Its `SY_d^p` coefficient is `a_d^(−1)/p`, where `a_d=w_0(u_d)∈R^×`. This formula includes the sign of Zink's negative Artin–Hasse map.

Define

\[
\tau=r_j+p r_d-1=s-1+\Delta,
\qquad \mu=\alpha_0\alpha_d^p/p,
\quad v_p(\mu)=\tau.
\tag{NT14}
\]

Although `τ` may be negative, every other displayed term of (NT13) has valuation strictly greater than `τ` after contraction (NT8). Here is the full check.

For the first family put

`A_i^*=p^i r_j+r_i=s+p^i Δ>s`.

Its baseline `n=l=0` has excess over `τ`

\[
A_i^*-1-\tau=(p^i-1)\Delta>0.
\tag{NT15}
\]

The further excess at general `n,l` is

\[
(p^n-1)A_i^*-n+p^{n+i}r_j(q^l-1)-l.
\tag{NT16}
\]

Each term is nonnegative, and strictly positive when its respective index is positive. For the first, use `A_i^*>s` and `(p^n−1)s≥n`. For the second use `r_j(q−1)>1` and `(q^l−1)/(q−1)≥l`.

For the product family put `e_i=h−i`. Its baseline excess is

\[
r_j+p^{e_i}r_i-e_i-\tau
=(p^{e_i}-p)s-e_i+1\ge0,
\tag{NT17}
\]

with equality exactly when `e_i=1`. For positive line index `b` or dual cycle index `l`, the additional excess is

\[
r_j(q^b-1)-b+p^{e_i}r_i(q^l-1)-dl>0.
\tag{NT18}
\]

For the dual term it suffices that

\[
p^{e_i}r_i(q-1)\ge\frac{q-p}{p-1}
=p+p^2+\cdots+p^{h-1}>d.
\]

Thus precisely the `+a_d^(−1)SY_d^p/p` term attains `τ`. Equivalently,

\[
\boxed{
\overline{\mu^{-1}b(\alpha_0S,\alpha_1Y_1,\ldots,\alpha_dY_d)}
=\bar a_d^{-1}SY_d^p.}
\tag{NT19}
\]

This calculation uses the full ghost formula at the boundary weights. It does not extrapolate the narrower `τ≥0` interval used for the unit-exponent theorem.

## 4. Infinitely many exact coefficients survive exponentiation

Compose (NT19) with the integral inverse maps and the scaled line from §2. Reduction commutes with this formal composition. By (NT12),

\[
\overline{\mu^{-1}\beta(u\gamma T,v\gamma T)}
=\bar a_d^{-1}\bar u\,T
\left(\sum_{m\ge0}\xi_mT^{p^{k_*-1}q^m}\right)^p
=\sum_{m\ge0}\chi_mT^{N_m},
\quad\chi_m\in k^\times.
\tag{NT20}
\]

In particular the coefficient infimum of the restricted logarithm is exactly `τ`, and (NT20) gives infinitely many coefficients at that minimum after scaling. This is the decisive difference from an argument based only on the first nonintegral coefficient.

Put `z(T)=κβ(uγT,vγT)`. Its coefficient infimum is

\[
L=a+\tau=a+s-1+\Delta>s,
\tag{NT21}
\]

because `a≥1` and `Δ>0`. For every exponential order `b≥2`,

\[
\nu(z^b/b!)-L
\ge(b-1)L-v_p(b!)
\ge(b-1)(L-s)>0.
\tag{NT22}
\]

Therefore `exp(z)` is integral with constant one, and the entire initial form of `exp(z)−1`, after division by `κμ`, is just the unit multiple of (NT20). In particular

\[
v_p(A_{N_m})+r_jN_m=a+\tau
\qquad(m\ge0).
\tag{NT23}
\]

The identity

`τ−r_j(p^(k_*)+1)=−S_(k_*)`

turns (NT23) into (NT4). Also `r_j(q−1)=1+p+⋯+p^(h−1)−p^j` is an integer, so (NT4) is an integer as asserted.

At weight `r_j`, the kernel and its inverse are integral, both with coefficient infimum zero. At every larger weight the same is true by monotonicity. At every smaller weight, (NT23) gives

`v_p(A_(N_m))+wN_m=L−(r_j−w)N_m→−∞`.

This proves (NT3) directly, without deducing an exponential radius from the logarithm radius. Since `N_m→∞`, (NT23) also gives `liminf v_p(A_n)/n=−r_j`; the opposite inequality follows from integrality at weight `r_j`. Legendre's formula proves (NT5).

## 5. Invariant frame changes and integral prefactors

Let `J(S,Y)` be the ratio of two normalized invariant integral frames. It is an integral unit, its restrictions to both axes equal one, and every nonconstant supported monomial has positive `S` degree.

Under the original weights `(ρ,r_1,…,r_d)`, torus invariance puts every positive monomial weight in `s Z`, hence at least `s`, as proved in DP46. Increasing only the scalar weight from `ρ` to `r_j=ρ+Δ` raises it by at least `Δ`. Therefore at (NT8)

\[
\nu(J-1)\ge s+\Delta>s,
\qquad \nu(\log J)\ge s+\Delta.
\tag{NT24}
\]

The logarithm inequality follows termwise from `v_p(b)≤(b−1)s`. A frame change changes the invariant splitting by `±log J`; there is no residual invariant bilinear term. After multiplication by `κ`, its valuation is at least

\[
a+s+\Delta=L+1.
\tag{NT25}
\]

Thus it cannot alter (NT20)–(NT23). This proves the stated invariant-frame independence, including the exact coefficient valuations. No assertion about arbitrary binomial exponents before contraction is required.

For an arbitrary integral `U`, the inverse maps and scaled inputs in §2 show that `V(γT)` is integral. Multiplying by the integral kernel proves `v_p(C_n)≥−r_jn`, hence (NT7). The pure kernel `U=1` proves optimality of this universal slope. An arbitrary prefactor is not multiplied by `κ` as a frame logarithm is; it could enter at the same first nonconstant level as (NT23). Accordingly the proof makes no exact-radius claim for every individual prefactor.

## 6. A concrete instance and the prime-sum limitation

In DP49's actual height-three block at `p=11`, a tensor exponent divisible by 11 gives the following **pure-kernel** slopes in the invariant product normalization:

| Primitive dual class | Unit-exponent slope | Exponent divisible by 11 |
|---|---:|---:|
| First dual coefficient a unit (`j=1`) | `1/1220` | `11/1330` |
| First coefficient in `11R`, second a unit (`j=2`) | `1/120` | `121/1330` |

The latter column is also the sharp universal lower-bound slope with integral prefactors. These are genuine local improvements. They cannot be inferred by adding `v_p(κ)` to the old asymptotic slope: all valuations `v_p(κ)≥1` give the same slope in that column, while the exact coefficient constant in (NT4) records the additional powers.

For a **fixed nonzero integer** tensor exponent `κ`, only finitely many odd primes divide it. In any prime-sum comparison at derivative order `n`, replacing the local unit-exponent slope by the slope in (NT6) changes a fixed finite set of terms. In particular it changes that sum by `O_κ(n)`, not its `n log X` coefficient as the prime cutoff `X` tends to infinity. An elementary absolute bound for the coefficient change is

\[
0\le\sum_{\substack{p\mid\kappa\\p\text{ odd}}}
\log p\left(\frac{p^{j_p}}{p^{h_p}-1}
-\frac1{(p-1)(p^{h_p-j_p}+1)}\right)
\le\sum_{\substack{p\mid\kappa\\p\text{ odd}}}\frac{\log p}{p-1}
\le\frac12\log\operatorname{rad}_{\rm odd}(\kappa)
\le\frac12\log|\kappa|.
\tag{NT26}
\]

The first difference is positive by cross multiplication: after cancelling the common positive factor, its numerator is `(p−2)q+(p−1)p^j+1>0`. The upper bound uses `p^j/(p^h−1)<1/(p−1)`. No cost or gain theorem for a tensor exponent varying with the global construction is supplied by (NT26). A finite local improvement can matter in a finite inequality; this calculation does not deny that possibility.

The theorem concerns the invariant primitive kernel and integral prefactors. A rational quadratic gauge must still be tracked separately. In particular one must not carry over without checking DP48's observation that an integral quadratic coefficient is harmless in the **unit-exponent** situation: the new boundary `r_j` can lie below `s/2`. If the quadratic arises as `κQ` with `Q` integral, its extra factor of `p` does make its exponential integral at every nonnegative weight, but a general rational `Q` is a separate input.

## 7. The recovered level normalization reverses this proposed improvement

There is a direct source-specific consequence. In

`Formalism/LocalToGlobal/ProjectiveLattices/IsThRule.lean`,

the definition `thExpr`, lines **66–70** in the recovered source, uses sections of tensor exponent `M²` at lines 68 and 70, and multiplies a polynomial value by `M^(−P.totalDegree)` at line 69. Thus its homogeneous degree-`n` ordinary-path specialization includes the normalization `M^(−n)`.

Let `M` be a nonzero integer and put `b=v_p(M)≥1`. Then `κ=M²` has valuation `2b`. For the pure kernel the normalized series is

\[
K_{M^2}(t/M)
=\sum_{n\ge0}\frac{A_n}{M^n}t^n.
\tag{NT27}
\]

Formula (NT5) gives exactly

\[
\boxed{
\liminf_n\frac{v_p(n!A_n/M^n)}n
=\frac{p^j}{q-1}-b<0.}
\tag{NT28}
\]

Indeed every coefficient valuation is decreased by `bn`. For an arbitrary integral prefactor, (NT7) gives the corresponding sharp universal lower bound

\[
v_p(n!C_n/M^n)
\ge\left(\frac{p^j}{q-1}-b\right)n
-\frac{s_p(n)}{p-1},
\tag{NT29}
\]

with universal sharpness again supplied by the pure kernel. Relative to a unit-level primitive pure kernel, whose slope is `c_unit=s/(p^(h−j)+1)`, the change is

\[
\frac{p^j}{q-1}-b-c_{\rm unit}
<s-b\le-\frac b2
\qquad(p\text{ odd},\ b\ge1).
\tag{NT30}
\]

The last inequality uses `s≤1/2` and `b≥1`. Thus forcing `p|M` cannot improve this universal ordinary-path slope after the actual `thExpr` normalization; its degree-linear denominator exceeds the nonunit-exponent improvement just proved. This is stronger and more directly tied to the recovered interface than the fixed-prime asymptotic observation (NT26).

The conclusion is precisely about the displayed tensor/degree normalization and the ordinary-path specialization. It does not exclude additional divisibility of a particular algebraic section, a special selected harmonic value, or another compensating factor in the full construction. Nor does it treat a nonhomogeneous polynomial as though every monomial had its total degree: the path comparison uses homogeneous degree `n`.

## 8. Dependencies, proof scope and checks

The known primary input is Zink's actual display pairing, with its negative Artin–Hasse convention: *The display of a formal p-divisible group*, Astérisque 278 (2002), Definition 19/(22), divided-ghost formulas (147)–(156), Proposition 106, formulas (196), (211), (218), and Theorem 122, at the exact locators recorded in DP40–DP46. The needed full arbitrary-unit ghost formula was proved and independently checked in DP46. No new classification or deformation-rigidity premise is used here.

The new arguments are the boundary profile, full-cycle reduced inverse, strict unique minimum of the full primitive ghost series at that profile, infinite coefficient sequence surviving exponentiation, exact nonunit-exponent radius, and the one-order-later invariant frame correction. These arguments handle the possible Artin–Hasse cancellation directly; they do not assume that scaling a logarithm automatically shifts its exponential radius.

The full proof and the exact `thExpr` source block have been read; the final saved-text reread and observed time and hash are recorded separately. No numerical experiment, Lean execution or machine formalization is claimed. No statement about every individual theta prefactor, an arbitrary prescribed selected harmonic jet, or a shorter global lift chain is inferred.
