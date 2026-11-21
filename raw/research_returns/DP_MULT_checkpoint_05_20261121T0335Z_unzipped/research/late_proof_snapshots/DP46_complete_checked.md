# DP46: exact mixed-line radius for arbitrary unit arrows and invariant integral frames

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. The root reserved **DP46**. The proof directly treats the arbitrary-unit singleton/complement displays. It requires no assertion that an unramified twist becomes trivial over a finite unramified extension.

## 1. Statement

Let `p` be odd, `h≥3`, `q=p^h`, `d=h−1`, and `R=W(k)` with perfect `k⊃F_q`. Normalize `v(p)=1` and put `s=1/(p−1)`. Take the cyclic display with normal summands

`T=W(R)e_0`, `L=⊕_(i=1)^d W(R)e_i`

and arbitrary units `u_i∈W(R)^×`, with arrows

\[
Fe_0=u_0e_1,\qquad Fe_i=p u_i e_{i+1}\quad(1\le i\le d),
\tag{UI1}
\]

where the indices are cyclic. Let `G` be its actual one-dimensional formal p-divisible group, and `H=G^D` the actual connected Cartier dual. DP40 constructs both integrally and identifies the dual display as the complementary display with reciprocal units. Write

\[
a_i=w_0(u_i)\in R^\times.
\tag{UI2}
\]

Use the integral Teichmüller coordinates `S` on `G` and `Y_1,…,Y_d` on `H`. Let `L_G,L_H` be their normalized logarithms, and `E_G,E_H` their inverse maps. The canonical display pairing supplies a normalized integral frame of the primitive Poincaré biextension, and a unique invariant rational logarithmic splitting `b(S,Y)`. In additive coordinates write

`β(x,y)=b(E_G(x),E_H(y))`.

Choose a unit `u∈R^×`, a primitive vector `v∈R^d`, and `λ∈R^×`. Let

\[
j=\min\{i:v_i\in R^\times\},\quad k_*=h-j,\quad
N=p^{k_*}+1,\quad S_{k_*}=\frac{p^{k_*}-1}{p-1},
\]

and define

\[
w_* =\frac{p^{k_*}}{(p-1)(p^{k_*}+1)},\qquad
c_* =s-w_* =\frac1{(p-1)(p^{k_*}+1)}.
\tag{UI3}
\]

For every integral formal function `U` whose restriction

`V(t)=U(E_G(ut),E_H(vt))`

is not identically zero, put `Θ(t)=V(t)exp(λβ(ut,vt))=Σ_n A_nt^n`. Then DP42's exact result remains valid:

\[
\boxed{
\nu_w(\Theta)=
\begin{cases}
-\infty,&0\le w<w_*,\\
\nu_w(V)\in[0,\infty),&w\ge w_*,
\end{cases}}
\tag{UI4}
\]

for every rational `w≥0`, with a finite value in the second line. Consequently

\[
v(n!A_n)\ge c_*n-\frac{s_p(n)}{p-1},\qquad
\boxed{\liminf_{n\to\infty}\frac{v(n!A_n)}n=c_*.}
\tag{UI5}
\]

The nilpotency length of the reduced dual tangent vector under its restricted `p`-operation is exactly `k_*`; thus the index governing the answer is intrinsic. In particular the best possible slope among lines with both projections primitive is still `ρ_2=1/(p²−1)`.

The exact logarithmic coefficient becomes

\[
\boxed{
p^{S_{k_*}}[t^{N}]\beta(ut,vt)
\equiv(-1)^{k_*-1}\theta_j u v_j^{p^{k_*}}\pmod p,
\quad
\theta_j=\prod_{r=j}^{d}a_r^{-p^{d-r}}\in R^\times.}
\tag{UI6}
\]

All these statements persist for any other **normalized invariant integral frame** of the same primitive Poincaré biextension, with its invariant logarithmic splitting. Integral prefactors may vanish at the origin, provided their path restriction is nonzero.

## 2. Variable ghost matrices and the primitive splitting

Let `B_n` be the matrix obtained by applying the `n`th Witt ghost to the coefficients of the Frobenius matrix in (UI1). Let `B'_n` be the analogous complementary reciprocal-unit matrix. Every ghost `w_n(u_i)` is a unit: modulo `p` it is `a_i^(p^n)`. The pairing identity is

\[
B_n^{\mathsf t}B'_n=pI.
\tag{UI7}
\]

For `r≥0` put `P_(n,0)=I` and `P_(n,r)=B_nB_(n+1)⋯B_(n+r−1)`. Use analogous notation `P'` for the dual. On divided ghosts `z_n=w_n(z)/p^n`, the display resolution is

`z_n↦B_n z_(n+1)−z_n`.

Its inverse on the rational finite ghost sequences used here is

\[
(d^{-1}z)_n=-\sum_{r\ge0}P_{n,r}z_{n+r}.
\tag{UI8}
\]

The logarithms of lifted points are the selected components of

\[
\sum_{n\ge0}P_{0,n}z_n,
\qquad
\sum_{n\ge0}P'_{0,n}z_n.
\tag{UI9}
\]

These are the variable-matrix identities already justified in DP40. On a fixed nilpotent degree truncation, integral divided ghosts have a uniform denominator bound, and every complete matrix cycle contributes respectively `d` or one powers of `p` times units. Thus the sums converge on the completed integral resolution, their telescoping boundaries vanish, and the quotient identities descend before inverting `p`. The Teichmüller and rational zeroth-ghost lifts below have finite ghost support at every such degree truncation.

Write the Teichmüller ghost lifts as

\[
\xi_n=S^{p^n}e_0/p^n,
\qquad
\upsilon_n=\sum_{i=1}^dY_i^{p^n}e_i^*/p^n.
\]

Let `C_H(Y)` be the `e_0^*` component of `Σ_nP'_(0,n)υ_n`. Put `x=L_G(S)` and `y=L_H(Y)`. Comparing the Teichmüller lifts with the rational additive lifts whose only ghost is `xe_0` or `Σy_i e_i^*` gives

`k_n=−Σ_r P_(n,r)ξ_(n+r)+1_(n=0)xe_0`,

`l_n=−Σ_r P'_(n,r)υ_(n+r)+1_(n=0)Σ_i y_i e_i^*`.

Their zeroth ghosts have zero selected component, so these are the required rational relation-module elements. Zink's quotient frame rule, Proposition106 and (218), and his negative Artin–Hasse normalization give exactly

\[
\boxed{
b(S,Y)=-\sum_{n,r\ge0}p^n
\langle P_{n,r+1}\xi_{n+r+1},\upsilon_n\rangle
\; + L_G(S)C_H(Y).}
\tag{UI10}
\]

For clarity about the sign: the Teichmüller frame differs from the additive bilinear frame by `hex⟨V^(−1)k,τ⟩ hex⟨g_0,l⟩^(−1)`, whereas the scalar splitting is its inverse. Zink's convention is `log hex(z)=−Σ_n w_n(z)/p^n`. Substitution yields (UI10), exactly as in DP41 with constant matrices replaced by prefix products. No commutation of different `B_n` matrices is assumed.

## 3. Exact supports and denominator valuations

Every prefix product follows a unique cyclic path. A path of length `lh+i` from `e_0` to `e_i`, `1≤i≤d`, contains `dl+i−1` arrows carrying `p`. Consequently the first family in (UI10) is

\[
-\sum_{i=1}^d\sum_{l,n\ge0}
\eta_{i,l,n}\frac{S^{p^{n+lh+i}}Y_i^{p^n}}{p^{n+l+1}},
\qquad \eta_{i,l,n}\in R^\times.
\tag{UI11}
\]

The line logarithm and the complementary component are

\[
L_G(S)=\sum_{a\ge0}A_a\frac{S^{q^a}}{p^a},\qquad A_0=1,\quad A_a\in R^\times,
\tag{UI12}
\]

\[
C_H(Y)=\sum_{i=1}^d\sum_{l\ge0}
C_{i,l}\frac{Y_i^{p^{lh+h-i}}}{p^{dl+h-i}},
\qquad C_{i,l}\in R^\times.
\tag{UI13}
\]

For (UI12), each complete line cycle supplies `d` numerator powers of `p` against `h` ghost denominators. For (UI13), the first path from `e_i^*` to `e_0^*` has length `h−i` and no numerator `p`; each additional cycle supplies one numerator `p`. Thus the supports and exact valuations of the two primitive-logarithm families are exactly those of DP42. Units may vary independently among paths; the argument does not require them to be one or Frobenius-fixed.

The coefficient at `SY_d^p` is particularly explicit. The first family cannot contain a term linear in `S`. In the product family, its unique source is `S` times the length-one dual path from `d` to zero. Hence

\[
[SY_d^p]b=a_d^{-1}/p.
\tag{UI14}
\]

The dual logarithm has ordinary first arrows

\[
(L_H)_i=Y_i+\frac{a_{i-1}^{-1}}pY_{i-1}^p+\text{higher path terms}
\quad(2\le i\le d).
\tag{UI15}
\]

The exceptional first selected arrow into coordinate one has degree `p²` and coefficient a unit divided by `p`. Every path through `r` selected gaps has coefficient a unit divided by `p^r`, as in DP40.

## 4. The mixed-line weight argument with unit coefficients

Fix `j,k_*` as in §1. Use the interval

\[
\frac{S_{k_*}}{p^{k_*}+1}\le w\le w_*,\qquad
\delta=s-w,\qquad
\omega_0=w,\quad\omega_i=s-p^{i-j}\delta.
\tag{UI16}
\]

These are DP42's weights. They are positive; they strictly dominate the original contraction weights `r_0=1/(q−1)` and `r_i=s−p^i/(q−1)`. The ordinary dual arrows have defect `pω_(i−1)−ω_i=1`, while the exceptional defect is greater than one. The scalar nonlinear log coefficients have positive scaled valuation. Paths through at least two selected arrows also have positive scaled valuation. Choose an integer `e` clearing all weight denominators, adjoin `π` with `π^e=p`, and set `α_i=π^(eω_i)`. These common scales have `v(α_i)=ω_i` and make `α_(i−1)^p/(pα_i)=1` for every ordinary arrow. The scaled logarithms and inverse maps are integral, and their reductions are

\[
\overline{\widetilde L}_G=S,\qquad
\overline{\widetilde L}_{H,1}=Y_1,\qquad
\overline{\widetilde L}_{H,i}=Y_i+\bar a_{i-1}^{-1}Y_{i-1}^p.
\tag{UI17}
\]

Every valuation calculation in DP42 (PL18)–(PL21) applies term by term to (UI11)–(UI13), since all additional coefficients are units. Explicitly, putting `τ=(p^(k_*)+1)w−S_(k_*)∈[0,s]`, all first-family baselines are strictly greater than `τ`; the smallest gap is

`δ(p^(k_*)−p+1−p^(1−j))>0`.

For the product family, with `e=h−i`, the excess of its baseline over `τ` is `(p^e−1)/(p−1)−e`, zero only when `e=1`. Additional line cycles and dual cycles strictly increase valuation, because

`w(q−1)>1`, `p^(h−i)ω_i(q−1)>d`.

Thus the unique weighted minimum remains the term (UI14). For `μ=α_0α_d^p/p`,

\[
\overline{\mu^{-1}b(\alpha_0S,\alpha_1Y_1,\ldots,\alpha_dY_d)}
=\bar a_d^{-1}SY_d^p.
\tag{UI18}
\]

Let `γ=α_0=α_j`. Along the scaled additive line, every earlier input coordinate has positive valuation because `v_i∈pR` for `i<j` and `ω_i−w<1`. Every later input also has positive valuation because `ω_i<w`. Only the `j`th unit input survives. Recursively inverting (UI17) gives the last coordinate initial term

\[
(-1)^{d-j}
\left(\prod_{r=j}^{d-1}\bar a_r^{-p^{d-r-1}}\right)
\bar v_j^{p^{d-j}}T^{p^{d-j}}.
\]

Substitution into (UI18) therefore gives

\[
\boxed{
\overline{\mu^{-1}\beta(u\gamma T,v\gamma T)}
=(-1)^{k_*-1}\bar\theta_j\bar u\bar v_j^{p^{k_*}}T^{p^{k_*}+1}.}
\tag{UI19}
\]

It has a nonzero derivative in residue characteristic `p`. With the common uniformizer choice, `μ=γ^(p^(k_*)+1)/p^(S_(k_*))`. Coefficient comparison proves (UI6); the original unramified valuation turns a positive residue error into divisibility by `p`.

For `w<w_*` in the interval (UI16), the minimum of the restricted logarithm is `τ<s`. The bounded-multiplier lemma of DP41/DP42 applies to (UI19), including every nonzero integral restricted prefactor, and proves infimum `−∞`. At `w=w_*`, the minimum is `s`, so the factorial estimate makes the exponential integral with constant one. Monotonicity treats all smaller and larger nonnegative weights. Gauss multiplicativity and Legendre's formula then prove (UI4)–(UI5), exactly as in DP42. This uses the full weighted initial form after inverse substitution, not merely the unrestricted low coefficient (UI14).

Finally (UI15) gives `D_i^p` equal to a unit times `D_(i+1)` modulo `p` for `i<d`; the last restricted power is zero. The resulting single semilinear chain has length `d−j+1=k_*` on a vector whose first unit coefficient is at `j`. This proves the intrinsic assertion.

## 5. Invariant integral changes of frame

The display automorphisms `e_i↦[ζ^(p^i)]e_i` commute with all arrows, including arbitrary units. On the paired formal groups use the inverse dual on the second factor. Thus the finite torus acts in the chosen coordinates by

`(S,Y_i)↦(ζS,ζ^(−p^i)Y_i)`.

The Teichmüller frame and the rational additive lifts in §2 are equivariant. Therefore `b` is invariant and represents the primitive identity class. Any two rational splittings in a fixed frame differ, in additive coordinates, by a bilinear form `Σ b_i x y_i`. None of these monomials is invariant, since `1−p^i` is nonzero modulo `q−1` for `1≤i<h`. This proves uniqueness of the invariant splitting in a fixed invariant frame.

Let another normalized invariant integral frame differ by `J(S,Y)`, an invariant integral unit with `J(0)=1` and normalized axes. Its invariant splitting differs by `±log J`; the sign depends only on which direction the frame comparison is written. It suffices to prove that `exp(±λ log J)` is an integral unit after each contraction (UI16).

For an invariant nonconstant monomial `S^aY^b`, its original contraction weight is

\[
\rho_h\left(a-\sum_i p^i b_i\right)+s|b|.
\tag{UI20}
\]

Invariance makes the first parenthesis divisible by `q−1`. Hence this positive weight lies in `sZ` and is at least `s`. Since every weight in (UI16) strictly exceeds the corresponding original weight, the contracted `J−1` has coefficient infimum strictly greater than `s`. Uniform strictness follows from the positive minimum of the finitely many weight increments and the positive degree of every monomial.

The ordinary logarithm series therefore shows `ν(log J)>s`: for its `n`th term, the valuation is at least `nν(J−1)−v_p(n)`, and `v_p(n)≤(n−1)/(p−1)`. The exponential factorial estimate then makes `exp(±λ log J)` an integral unit for **every integral λ**, in particular every `λ∈R^×`. Its value at the origin is one. Multiplication by this unit preserves the weighted threshold and the finite Gauss infimum, and the additional logarithm is strictly above the initial form (UI19). Thus (UI4)–(UI6) are unchanged by the invariant frame change.

This proof does not assume that binomial powers `J^λ` are integral without contraction for arbitrary `λ∈R`. That assertion can fail when the residue of `λ` is not in `F_p`. For completely arbitrary integral frames with the compatibly transported splitting, the same conclusion is still immediate when `λ∈Z_p`, by integral binomial powers; invariant frames give the stated stronger result for all integral λ through (UI20).

## 6. Transport under integral CM isomorphisms

There is also a coordinate-independent transport statement. Suppose an integral `O_q`-linear isomorphism `φ:G→G_0` is supplied over an unramified coefficient extension, and let `ψ=(φ^(−1))^D:H→H_0`. Naturality of the Poincaré pairing transports the primitive identity class. The tangent maps are a unit scalar `a=dφ` and an invertible integral matrix `B=dψ`; an isomorphism introduces no nonunit tangent factor.

Normalized logarithms satisfy

`L_(G_0)∘φ=a L_G`, `L_(H_0)∘ψ=B L_H`.

Thus a logarithmic line with primitive projections is carried to a logarithmic line with primitive projections. The reduced restricted-`p` operation commutes with the tangent map, so its nilpotency length `k_*` is unchanged. Integral prefactors remain integral under the isomorphism and its inverse, and a nonzero path restriction remains nonzero. Invariant integral frames compare by the invariant unit treated in §5. Consequently the exact threshold and factorial limit transport without alteration. Coefficient valuations are unchanged by an unramified extension, so the numerical conclusions descend to the original coefficient field when the original expression is defined there.

This transport theorem uses a supplied integral isomorphism; it does not assert that every twist is trivial over a finite unramified extension. The direct proof in §§2–5 already treats every arbitrary-unit singleton/complement display, so no twist-trivialization theorem is needed for that entire class. Combined with DP40's rank-one integral CM normal-form interface, it applies whenever the actual local CM data supply that singleton type and its actual Cartier dual.

## 7. Sources, attempted alternative and check scope

The primary input is Zink, *The display of a formal p-divisible group*, Astérisque **278** (2002): Theorem5 p.131; Definition19/(22) p.143; divided-ghost and exponential formulas (147)–(156) pp.204–207; Proposition106 p.226; negative Artin–Hasse normalization (196) p.232 and (211) p.236; pairing cocycles (218) p.239; Proposition121 and Theorem122 pp.241 and247. Primary PDF `https://www.numdam.org/article/AST_2002__278__127_0.pdf`, SHA-256 `2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69`. These exact sources and conventions were already directly checked for DP38–DP41.

An alternative approach through height-one formal-`O_q` deformation rigidity was considered. Hazewinkel's §5, pp.77–78, explicitly compares Lubin–Tate laws and allows a completed maximal unramified extension for changes of uniformizer; it does not on its own justify a finite-unramified trivialization of every unit-arrow model over an arbitrary perfect coefficient field. Drinfeld's Proposition4.2 was located in indexed primary text, but the attempted direct PDF retrieval redirected or failed. Neither source is used as an unstated classification premise in this proof.

The new work is the variable-prefix ghost pairing formula, its exact unit-denominator supports, the explicit unit in the first mixed-line coefficient, the intrinsic restricted-power identification and the invariant-frame quantization argument. The reused DP42 valuation calculation is applicable term by term for the precise reasons given in §4. Actual whole saved-proof readings and independent checks are recorded separately with hashes and observed times. No Lean execution, machine formalization or numerical test is claimed. No identification of a global theta normalization, selected harmonic polynomial, or lift-count inequality is inferred.
