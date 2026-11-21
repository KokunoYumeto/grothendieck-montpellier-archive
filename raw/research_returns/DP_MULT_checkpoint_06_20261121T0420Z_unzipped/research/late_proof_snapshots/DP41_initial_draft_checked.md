# DP41: the uniform weight inflation p is sharp for the actual primitive class

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. The root reserved finding identifier DP41. This memo derives the entire primitive rational logarithmic splitting from the cyclic display, then proves an exact weighted-radius statement. The proof uses Zink's **negative** Artin–Hasse convention, as corrected in DP38. It does not infer an exponential radius merely from a sharp logarithm coefficient.

## 1. Statement

Assume `p` is odd, `h≥2`, `q=p^h`, `d=h−1`, and `O=W(F_q)`. Put

`s=1/(p−1)`, `ρ=1/(q−1)`, `r_0=ρ`, `r_j=s−p^jρ` for `1≤j≤d`.

All `r_j` are positive. Use the cyclic Teichmüller coordinates of DP38 on `G_h×G_h^D`, and its normalized equivariant frame of the primitive Poincaré biextension. Let `b(S,Y)` be its unique invariant rational logarithmic splitting. Write

`β(x,y)=b(E_0(x),E_H(y))`

in normalized additive logarithm coordinates, where `E_0,E_H` are the formal exponentials. Let `λ∈O^×`; in particular `λ=1`, `−1`, or `±1/2` is allowed.

For every nonnegative rational `a`, the exact weighted infimum is

\[
\boxed{
w_{a\mathbf r}\bigl(\exp(\lambda\beta)\bigr)
=\begin{cases}
-\infty,&0\le a<p,\\
0,&a\ge p.
\end{cases}}
\tag{ER1}
\]

Here `w_(a r)(Σ c_α z^α)=inf_α(v_p(c_α)+aΣr_iα_i)`. The same statement holds in the integral group coordinates for `exp(λb)`. It also holds after multiplication by `U(E_0,E_H)` for any integral formal function `U` with `U(0)` a unit.

Thus the uniform anisotropic inflation factor `p` used in DP36 is optimal for this actual primitive class. No smaller factor admits even a finite additive coefficient error for the full multivariate unit kernel. This does **not** prove that the sufficient one-variable residual `ρ_h` is optimal on every prescribed diagonal, or settle the selected harmonic-jet estimate or global lift count.

## 2. Divided Witt ghosts and the exact logarithms

Use the displays of DP38, with basis `e_0,…,e_d` and dual basis, and let `A,A′` be their constant Frobenius matrices:

`A e_0=e_1`, `A e_j=p e_(j+1)` for `j≥1`,

`A′e_0^*=p e_1^*`, `A′e_j^*=e_(j+1)^*` for `j≥1`,

with cyclic indices. Their pairing satisfies `<Au,A′v>=p<u,v>`.

For a Witt vector `z`, let

\[
u_n(z)=\frac{w_n(z)}{p^n}, \tag{ER2}
\]

where `w_n` is the ordinary Witt ghost polynomial. Work coefficientwise over the fraction field and on a finite nilpotent truncation of the formal variables. These ghost sequences are finite: every sufficiently high power of a nilpotent variable vanishes. Therefore all resolvent sums below are finite on each such truncation and define formal series after passage to the limit.

On divided ghosts, Witt Frobenius sends `u_n` to `p u_(n+1)`. The extension of the display operator `V^(−1)=p^(−1)F` is consequently

`(V^(−1)z)_n=A u_(n+1)(z)`.

Thus, writing `T` for the left shift of the ghost sequence,

\[
d_G=V^{-1}-1=AT-1,\qquad d_G^{-1}=-\sum_{m\ge0}(AT)^m. \tag{ER3}
\]

For the dual replace `A` by `A′`. The normal-decomposition condition `z∈Q` says that the `T`-component of its zeroth ghost is zero. Hence the linear functional

\[
\ell_P(z)=\operatorname{pr}_T\sum_{n\ge0}A^n u_n(z) \tag{ER4}
\]

vanishes on `d_GQ`: substitution telescopes to `−pr_T u_0(Q)=0`. It is the identity on the section whose only ghost is a zeroth ghost in `T`. It therefore gives the normalized characteristic-zero logarithm of the formal group.

This argument is a calculation with the rationalized integral display identities. It does not apply a theorem about displays over a `p`-nilpotent base to a field in which `p` is invertible. The integral formal groups and quotient identities are already constructed over `O/p^n` and passed to the limit; (ER4) is checked directly to be additive and to have identity differential. Zink's divided-Witt and exponential formulas (147)–(156), pp.204–207, give the source context for this calculation.

For the line's Teichmüller section `σ(S)=[S]e_0`, its ghosts are

`u_n=S^(p^n)e_0/p^n`.

Only cycles of length `h` return to `T=O e_0`, with multiplier `p^d`, so (ER4) gives exactly

\[
L_0(S)=\sum_{m\ge0}\frac{S^{q^m}}{p^m}. \tag{ER5}
\]

For `τ(Y)=Σ_j[Y_j]e_j^*`, put

`v_n=Σ_j Y_j^(p^n)e_j^*/p^n`.

The full vector `Z(Y)=Σ_n(A′)^n v_n` satisfies

`Z(Y)=Σ_jY_j e_j^*+(A′/p)Z(Y^p)`.

Write its `e_0^*` component as `C(Y)` and its `T′` components as `L_1,…,L_d`. Then

`C(Y)=p^(−1)L_d(Y^p)`,

`L_1(Y)=Y_1+C(Y^p)=Y_1+p^(−1)L_d(Y^(p²))`,

`L_i(Y)=Y_i+p^(−1)L_(i−1)(Y^p)` for `i≥2`.

These are precisely DP32's functional equations, so the Teichmüller coordinates used here have **exactly** its logarithm, not merely isomorphic special fibres or the same Lie characters. The complementary component is

\[
C(Y)=\sum_{j=1}^d\sum_{l\ge0}
\frac{Y_j^{p^{lh+h-j}}}{p^{dl+h-j}}. \tag{ER6}
\]

Indeed the path from `e_j^*` first reaches `e_0^*` after `h−j` steps, and each additional cycle contributes one numerator factor `p` over `h` further ghost denominators.

## 3. Full primitive logarithm from a rational bilinear section

Let `x=L_0(S)` and `y=L_H(Y)`. Choose the rational additive lifts `g_0(x)`, `g′_0(y)` whose only nonzero divided ghost is their zeroth ghost, respectively `x e_0` and `Σ y_j e_j^*`. Since they are additive in the logarithm variables, the scalar-one section in their quotient frame is bilinear. Their comparison with the Teichmüller frame gives the rational splitting explicitly.

Let

`k=d_G^(−1)(σ(S)−g_0(x))`,

`l=d_H^(−1)(τ(Y)−g′_0(y))`.

Their zeroth ghosts have zero `T` or `T′` projection by (ER4), so they belong to the respective rationalized `Q` modules. From (ER3),

\[
k_n=-\sum_{r\ge0}A^r u_{n+r}+\mathbf1_{n=0}x e_0,
\quad
l_n=-\sum_{r\ge0}(A')^r v_{n+r}+\mathbf1_{n=0}\sum_jy_j e_j^*.
\tag{ER7}
\]

Proposition106's quotient relation and Zink (218) show that the Teichmüller frame is the additive frame multiplied by

`hex⟨V^(−1)k,τ⟩ · hex⟨g_0,l⟩^(−1)`.

Thus the scalar representing the bilinear section in the Teichmüller frame is the inverse of that product. Zink's sign convention is

\[
\log\operatorname{hex}(z)=-\sum_{n\ge0}\frac{w_n(z)}{p^n}.
\tag{ER8}
\]

For a pairing of two divided-ghost sequences `u_n,v_n`, the right side is `−Σ_n p^n<u_n,v_n>`, because Witt multiplication multiplies ordinary ghosts. Substitution of (ER7) therefore gives

\[
b(S,Y)
=-\sum_{n\ge0}\sum_{r\ge0}p^n
  \langle A^{r+1}u_{n+r+1},v_n\rangle
  +L_0(S)C(Y). \tag{ER9}
\]

Counting the cycle powers of `A` turns this into the entirely explicit formula

\[
\boxed{
b(S,Y)=
-\sum_{j=1}^d\sum_{l,n\ge0}
 \frac{S^{p^{n+lh+j}}Y_j^{p^n}}{p^{n+l+1}}
+L_0(S)\sum_{j=1}^d\sum_{l\ge0}
 \frac{Y_j^{p^{lh+h-j}}}{p^{dl+h-j}}.}
\tag{ER10}
\]

To check the first sum's exponent, a path of length `lh+j` from `e_0` ends at `e_j` with multiplier `p^(dl+j−1)`; combining this with the two ghost denominators and the factor `p^n` gives precisely `p^(−n−l−1)`.

Every fixed ordinary degree has only finitely many contributions. Some terms of the two sums cancel; the formula is an equality of formal series and does not assume their supports are disjoint. Its first coefficients are exactly the corrected DP38 values `−S^pY_1/p+SY_d^p/p`.

Each monomial is invariant under the actual action `(ζS,ζ^(−p)Y_1,…,ζ^(−p^d)Y_d)`. The rational additive lifts are also equivariant, and both axes are normalized. Therefore this is the unique invariant splitting of the same primitive display class, as in DP37/DP38. No arbitrary rational bilinear term has been inserted.

## 4. Exact minimum of the contracted logarithm

Fix rational `a≥p−1`. In a finite ramified extension, choose a uniformizer power `π` so that all numbers `a r_i` occur as valuations of powers `α_i` of `π`. Scale `S` by `α_0` and each `Y_i` by `α_i`. Write

`b_a(S,Y)=b(α_0S,α_1Y_1,…,α_dY_d)`,

`t=a s−1≥0`.

Choose the powers consistently so that all first monomials of weight `s` have the same scalar multiplier `μ` after division by `p`, with `v(μ)=t`. We prove

\[
\nu(b_a)=t,\qquad
\overline{\mu^{-1}b_a}
=Q:=-\sum_{j=1}^d S^{p^j}Y_j+SY_d^p. \tag{ER11}
\]

The bar denotes reduction modulo the extension's uniformizer. This also asserts that every other displayed summand in (ER10) has valuation strictly greater than `t`.

### First sum

Its monomial with indices `j,l,n` has unscaled weighted degree

\[
W_{jln}=p^n\bigl(s+p^j\rho(q^l-1)\bigr),
\]

and coefficient valuation `−n−l−1`. After subtracting `t`, its contracted valuation is

\[
a s(p^n-1)-n+a p^{n+j}\rho(q^l-1)-l. \tag{ER12}
\]

Since `a≥p−1`, the first part is at least `p^n−1−n`, which is zero when `n=0` and strictly positive for `n≥1` because `p` is odd. The second part is at least `((p−1)p^(n+j)−1)l`, using `(q^l−1)/(q−1)≥l`; it is strictly positive for `l≥1`. Thus equality occurs exactly at `n=l=0`. These are the terms `−μ S^(p^j)Y_j`.

### Product L_0 C

Write `u≥0` for the index in `L_0`, and put `k=h−j`, so `1≤k≤d`. Its coefficient valuation is `−u−dl−k`, and its weighted degree is

\[
W=\rho q^u+q^l(s p^k-q\rho).
\]

The baseline `u=l=0,k=1` has `W=s`. More generally

\[
W-s=\rho(q^u-1)+(q^l-1)(s p^k-q\rho)+s(p^k-p)\ge0.
\tag{ER13}
\]

Multiplying by `p−1`, the three terms are bounded below respectively by

`(p−1)u`, `(q−p)l`, and `p^k−p`.

The second bound uses `s p^k−qρ≥s p−qρ=s−ρ>0`. Hence

\[
a(W-s)-(u+dl+k-1)
\ge(p-2)u+(q-p-d)l+(p^k-p-k+1). \tag{ER14}
\]

All terms are nonnegative. The first is strictly positive if `u≥1`; the second if `l≥1`; and the last if `k>1`. Here `q−p>d` for every odd `p` and `h≥2`. Consequently equality occurs exactly at `u=l=0,k=1`, giving `+μ S Y_d^p`.

These surviving monomials are distinct, so cancellation cannot remove them. This proves (ER11). In particular its residue polynomial is not a `p`th power:

`∂Q/∂Y_1=−S^p≠0`

in residue characteristic `p`; this remains true when `d=1`, because the derivative of `Y_1^p` is zero.

## 5. A non-pth-power initial form obstructs the exponential

We use the following elementary lemma over any complete discretely valued extension of `Q_p`, with `p` odd.

**Lemma.** Let `z` be a formal series with zero constant term, bounded coefficients, `ν(z)=t` satisfying `0≤t<s=1/(p−1)`. Suppose its initial form after division by a scalar of valuation `t` has a nonzero formal partial derivative, equivalently a nonzero monomial whose exponents are not all divisible by `p`. Then `exp z` has unbounded coefficient denominators. Over a perfect residue field this is exactly the condition that the initial form is not a `p`th power; the derivative formulation also covers imperfect residue fields without a scalar-normalization ambiguity.

**Proof.** The series `exp(pz)` is integral. Moreover

\[
\nu(\exp(pz)-1)=1+t,
\tag{ER15}
\]

and its initial form is the initial form of `pz`. Indeed, the term of exponential order `n≥2` has valuation at least `n(1+t)−v_p(n!)`, strictly larger than `1+t`, since `v_p(n!)≤(n−1)/(p−1)` and `1+t−s>0` for odd `p`.

Suppose first that `E=exp z` were integral. The equality `E^p=exp(pz)` reduces to `bar E^p=1` in the residue power-series domain, so `bar E=1`. Put `δ=ν(E−1)>0`; the minimum exists by discreteness. If `δ≥s`, the binomial expansion gives `ν(E^p−1)≥1+s>1+t`, contradicting (ER15). If `δ<s`, the last binomial term `(E−1)^p` has valuation `pδ`, strictly smaller than every other term `binomial(p,j)(E−1)^j`. Thus the initial form of `E^p−1` is a scalar multiple of a `p`th power. Equation (ER15) identifies it with the non-`p`th-power initial form of `pz`, a contradiction. Multiplication by a nonzero scalar cannot change the vanishing of all formal partial derivatives, so the scalar normalization introduces no issue.

Finally, if `E` merely had bounded denominators, Gauss multiplicativity would give `pν(E)=ν(E^p)=0`, since `E^p=exp(pz)` is an integral unit with constant coefficient one. Thus `ν(E)=0` and `E` would be integral, already impossible. Hence its coefficient infimum is `−∞`. ∎

Apply this lemma to `z=λb_a`. The initial form in (ER11) remains non-`p`th-power after multiplication by the residue of the unit `λ`. If `p−1≤a<p`, then `0≤t=a s−1<s`, so the coefficients of `exp(λb_a)` have infimum `−∞`.

For `a≥p`, (ER11) gives every coefficient of `λb_a` valuation at least `s`. The ordinary factorial estimate proves integrality of its exponential:

`ν((λb_a)^n/n!)≥ns−v_p(n!)=s_p(n)/(p−1)≥0`.

Its constant coefficient is one, so its coefficient infimum is exactly zero. For `0≤a<p−1`, monotonicity of weighted infima and positivity of all the `r_i` give `w_(a r)≤w_((p−1)r)=−∞`. This proves (ER1) in the integral group coordinates.

## 6. Passage to logarithm coordinates and integral unit factors

For every `a≥1`, the coordinatewise contractions of `L_0` and `L_H`, with the same input and output scales `α_i`, are integral formal maps with identity linear term, and their inverses are integral. For the line this follows from

`a(q^m−1)/(q−1)−m≥0`.

For the dual, DP32's iterate coefficient has weight increment `δ_m≥m`; after contraction its valuation is `aδ_m−m≥0`. The exact ghost derivation in §2 has identified these logarithms with the present Teichmüller model.

Substitution by an integral formal map with an integral inverse preserves the extended Gauss infimum. In the bounded case this follows by applying the two substitution inequalities in opposite directions. In the unbounded case, boundedness after substitution would imply boundedness before it by applying the inverse, a contradiction. Therefore the contracted original-coordinate exponential and the contracted additive-coordinate exponential have the same extended infimum for `a≥1`.

This proves (ER1) for `exp(λβ)` whenever `a≥1`. For `0≤a<1`, monotonicity from `a=1` supplies `−∞`, completing the claim. The odd-prime assumption ensures `p−1≥2`, so every `a` needed in the non-pth-power argument is already in the range of integral coordinate equivalence.

If `U` is an integral formal unit, its contraction in the group coordinates is an integral unit for every `a≥0`. For `a≥1`, its expression after the contracted exponential substitution is also an integral unit with integral inverse. Multiplication by that unit preserves boundedness, unboundedness and, in the bounded case, the Gauss infimum. For `a<1`, monotonicity again suffices. Hence the same exact threshold holds for the stated unit-prefactored kernel.

## 7. Consequence and limitation

DP36's uniform inflation by `p` is not an artifact of a loose logarithm-to-exponential estimate for the primitive actual-dual kernel. The full display formula proves it is exact in the family of anisotropic weights `a(r_0,…,r_d)`. The earlier first denominator only gave `a≥p−1`; the non-`p`th-power initial-form argument closes the entire interval `[p−1,p)`.

This multivariate statement still does not identify the optimal rate on a fixed geometric path. Restriction can remove or cancel whole initial forms; the height-two diagonal with identical coordinates already illustrates that phenomenon. It also does not prove that a prescribed geometric theta section is a local unit, or that its selected harmonic operators retain the same worst coefficients. DP39 addresses a particular harmonic shortcut, and the source's conjugated-connection identities remain relevant to any actual global construction.

## 8. Sources and actual check scope

Zink, *The display of a formal p-divisible group*, Astérisque **278** (2002): (147)–(156), pp.204–207 for divided ghosts and the display exponential; Proposition106, p.226 for the quotient section rule; (196), p.232 and (211), p.236 for the **negative** Artin–Hasse normalization; (218), p.239 for the pairing cocycles. Primary PDF `https://www.numdam.org/article/AST_2002__278__127_0.pdf`, local SHA-256 `2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69`.

The actual group and dual are those established in DP32 and the explicit display of DP38. The whole rational ghost formula, its two cycle counts, each termwise valuation bound, the non-pth-power lemma, and the integral coordinate equivalence were derived during this turn. The root independently checked the norm obstruction after receiving its statement. The exact full-saved-proof reread and independent reviews are recorded separately; they are not presumed from a request. No numerical test, Lean execution, or machine formalization is claimed.
