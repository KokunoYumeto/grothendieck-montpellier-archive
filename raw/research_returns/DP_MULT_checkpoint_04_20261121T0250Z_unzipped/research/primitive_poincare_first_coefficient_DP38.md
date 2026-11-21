# DP38: the first primitive Poincaré denominator and exact mixed jets

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. The root reserved finding identifier DP38. This is an explicit calculation in a cyclic display and its actual Cartier dual. It does not assume that the Poincaré class is represented by a guessed scalar bilinear logarithm, and does not require an unproved identification of every display coordinate with DP32's entire logarithm.

## 1. Statement

Let `p` be any prime, `h≥2`, `q=p^h`, `d=h−1`, and `O=W(F_q)`. There are explicit integral Teichmüller coordinates `S` on the height-`h` Honda/Lubin–Tate line `G`, coordinates `Y_1,…,Y_d` on its actual Cartier dual `H`, and a normalized integral frame of the primitive Poincaré biextension such that every rational normalized compatible splitting `B(S,Y)` has

\[
[S^pY_1]B=-\frac1p,\qquad [SY_d^p]B=\frac1p. \tag{PP1}
\]

The same coefficients occur in `log B`. An axes-normalized integral unit change of frame changes either coefficient by an integral amount, so its valuation remains exactly `−1`. A rational bilinear change of compatible splitting does not change either coefficient.

The frame has the true Poincaré Teichmüller symmetry

\[
(S,Y_1,\ldots,Y_d)\longmapsto
(\zeta S,\zeta^{-p}Y_1,\ldots,\zeta^{-p^d}Y_d),
\qquad\zeta^{q-1}=1. \tag{PP2}
\]

There is a unique invariant rational logarithmic splitting `b=log B`. It has no positive term of total degree less than `p+1`, and its first homogeneous part is exactly

\[
b_{p+1}=B_{p+1}=\frac{-S^pY_1+SY_d^p}{p}. \tag{PP3}
\]

In normalized logarithm coordinates, with invariant directions `D_G,D_1,…,D_d`, the exact mixed derivatives are

\[
D_G^pD_1B(0)=-(p-1)!,\qquad
D_GD_d^pB(0)=(p-1)!. \tag{PP4}
\]

Both are units. For every integral formal function on `G×H`, the same two differential operators have values divisible by `p`.

Combining the degree-`p+1` pole with DP35 gives the numerical denominator-growth conclusion

\[
w_t(B)=-\infty\quad\text{for all rational }0<t<\frac1{p+1},
\qquad
\liminf_{|\alpha|\to\infty}\frac{v_p(B_\alpha)}{|\alpha|}
\le-\frac1{p+1}. \tag{PP5}
\]

This is a lower bound for the necessary denominator rate, not a proof that the optimal rate equals `1/(p+1)`.

## 2. The cyclic display and the actual-dual coordinates

Work compatibly over `O/p^n`, and then pass to the inverse limit. Let `P` be free over the Witt ring on `e_0,…,e_d`, with normal decomposition

`T=W e_0`, `L=⊕_(j=1)^d W e_j`, `Q=L⊕I T`.

Use cyclic indices `e_h=e_0`, and define

\[
F e_0=e_1,\qquad V^{-1}e_j=e_{j+1}\ (1\le j\le d),
\qquad F e_j=p e_{j+1}\ (j\ge1). \tag{PP6}
\]

The maps are Frobenius-semilinear, and on `I T` use the required relation `V^(−1)(Vξ·e_0)=ξF e_0`. The linearized map `V^(−1)⊕F` on `L⊕T` is a cyclic permutation matrix, hence an isomorphism. The dual display has

`L′=W e_0^*`, `T′=⊕_(j=1)^d W e_j^*`,

\[
V'^{-1}e_0^*=e_1^*,\qquad F'e_0^*=p e_1^*,\qquad
F'e_j^*=e_{j+1}^*\ (j\ge1), \tag{PP7}
\]

where `e_h^*=e_0^*`. These formulas satisfy Zink's dual-pairing identities (22), p.143. In particular they are the actual dual display, not an independently guessed formal group. The Frobenius cycles send each basis vector to `p^(h−1)` times itself in the first display and to `p` times itself in the dual, with the corresponding `h`th Frobenius on coefficients. Thus both displays and their duals meet the nilpotence conditions when `h≥2`.

Zink's Theorem81, (145)–(146), p.204, realizes their formal groups as the cokernels of `V^(−1)−id`. The natural maps

\[
\sigma(S)=[S]e_0,\qquad
\tau(Y)=\sum_{j=1}^d[Y_j]e_j^* \tag{PP8}
\]

followed by passage to the cokernel give integral formal coordinate systems. Their tangent maps are the identity maps to `P/Q` and `P′/Q′`; the formal inverse function theorem therefore makes them isomorphisms of formal schemes. They are set-theoretic/formal coordinate sections, not group homomorphisms.

On the special fibre, `p[S]=V[S^p]`. The display relations move `V[S^p]e_0` successively around the cycle to `[S^(p^h)]e_0`. Thus `[p]_G(S)=S^q mod p`, while the linear coefficient over `O` is `p`. This is the Lubin–Tate class with uniformizer `p` and residue cardinality `q`. Hazewinkel's §5 uniqueness and strict-isomorphism theorem identifies the line integrally with `G_h`. The dual display therefore gives its actual Cartier dual. The same relations give the familiar dual special-fibre map `(Y_d^(p²),Y_1^p,…,Y_(d−1)^p)`. The calculation below only uses (PP6)–(PP8), so does not presume more than this actual-dual identification.

## 3. The frame and its cocycles

Use the evaluation pairing `P×P^*→W`. Zink (218), p.239, constructs its primitive biextension from

`α_1(κ,z′)=hex⟨V^(−1)κ,z′⟩`,

`α_2(z,κ′)=hex⟨z,κ′⟩^(−1)`.

Here `hex` is **Zink's normalization**, which has linear coefficient `−1` on the Teichmüller curve: `hex([Z])=exp(−Σ_(r≥0)Z^(p^r)/p^r)`. This sign follows from the embedding `z↦1−zt` and the projector in (196), p.232, followed by evaluation at `t=1` in (211), p.236. It is the inverse of the positive Artin–Hasse exponential often denoted `E_p`. The inverse in the second expression is Zink's minus sign when the formal multiplicative group is written additively. The section represented by `(1,σ(S),τ(Y))` in the quotient construction of Proposition106, p.226, gives a normalized integral frame. If `κ_G` and `κ_H` are the unique defects of these two lifts, its cocycles are

\[
C_G=\operatorname{hex}\langle V^{-1}\kappa_G,\tau(Y)\rangle,
\qquad
C_H=\operatorname{hex}\langle\sigma(S),\kappa_H\rangle^{-1}. \tag{PP9}
\]

The precise defect equations and the quotient sign are written out in DP35, (P8)–(P9). A rational compatible splitting exists by DP35's characteristic-zero integration; write `b=log B`. Our convention is `δ_G b=log C_G`, so `δ_G b=b(F_G(S,S′),Y)−b(S,Y)−b(S′,Y)`. This fixes the signs in (PP1).

## 4. Horizontal carry: the coefficient −S^pY_1/p

For two scalar variables `S,S′`, define the integral polynomial

\[
C_p(S,S')=\frac{(S+S')^p-S^p-S'^p}{p}. \tag{PP10}
\]

In Witt coordinates write

`[S]+[S′]−[S+S′]=Vξ`.

The first two ghost polynomials give exactly `ξ_0=−C_p(S,S′)`. More generally `ξ_i` is a homogeneous integral polynomial of ordinary degree `p^(i+1)` in `S,S′`. This follows from the weighted homogeneity of the Witt addition/subtraction polynomials. Every component of `F^rξ` has degree at least `p^(r+1)`; here one uses this particular homogeneous Witt vector, not the false assertion that Frobenius raises the degree of every arbitrary Witt vector.

Let `d_G=V^(−1)−id`. The explicit element of `Q`

\[
\kappa_0=-V\xi\,e_0-\sum_{j=1}^dF^{j-1}\xi\,e_j \tag{PP11}
\]

satisfies the exact telescoping identity

\[
d_G\kappa_0=V\xi\,e_0-F^d\xi\,e_0. \tag{PP12}
\]

The endpoint has ordinary degree at least `p^(d+1)=q`. Therefore the group sum of the two Teichmüller sections agrees with `[S+S′]e_0` modulo degree `q`, so

\[
F_G(S,S')=S+S'+O((S,S')^q). \tag{PP13}
\]

The true lift defect `κ_G` differs from `κ_0` only in degree at least `q`. To see this without assuming continuity of an uncomputed inverse, reduce the exact sequence (146) modulo the degree-`q` ideal: the two images under `d_G` agree, and `d_G` is injective on that nilpotent test algebra. Hence the two reductions of `κ` agree.

By (PP11), the `e_1` component of `V^(−1)κ_0` is exactly the Witt-vector negative `w=−ξ`. All other terms have components either in the other basis directions or of larger `S`-degree. Multiplication by the Teichmüller vector `[Y_1]` sends Witt coordinate `w_i` to `w_iY_1^(p^i)`; it is not necessary, or correct at `p=2`, to identify every `w_i` with `−ξ_i`. Only `w_0=−ξ_0` contributes linearly in `Y_1`. Zink's `hex` has linear coefficient `−1`, so

\[
[Y_1]\log C_G=-C_p(S,S')+O((S,S')^q). \tag{PP14}
\]

The logarithm and the unit have the same `Y_1`-linear coefficient because the axis value at `Y=0` is `1`. Put `b_1(S)=[Y_1]b(S,Y)`. Extracting `S^(p−1)S′` from `δ_G b_1` uses only ordinary addition, by (PP13), and gives

`p[S^p]b_1=−1`.

Thus `[S^pY_1]b=−1/p`. Every positive term of `b` has positive `Y`-degree, so exponentiation cannot add another contribution with `Y`-degree one. Hence `[S^pY_1]B=−1/p` as well.

## 5. Vertical last-coordinate carry: the coefficient SY_d^p/p

Now restrict both dual inputs to the last coordinate. For variables `Y,Y′`, again write

`[Y]+[Y′]−[Y+Y′]=Vξ`, with `ξ_0=−C_p(Y,Y′)`.

Let `d_H=V′^(−1)−id`. The explicit defect approximation

\[
\kappa'_0=-V\xi\,e_d^*-\xi\,e_0^* \tag{PP15}
\]

satisfies

`d_Hκ′_0=Vξ e_d^*−Fξ e_1^*`.

The endpoint has degree at least `p²`. Hence addition on this source axis is ordinary addition modulo degree `p²`, and the actual defect agrees with (PP15) to that precision, by the same injectivity argument. Pairing with `[S]e_0` and taking the inverse in the second formula of (PP9) gives

\[
[S]\log C_H=C_p(Y,Y')+O((Y,Y')^{p^2}). \tag{PP16}
\]

Therefore extraction of `Y^(p−1)Y′` yields `[SY_d^p]b=1/p`. Exponentiation leaves a term of `S`-degree one unchanged, proving the second formula of (PP1).

For later use, these same degree computations imply

`log_G(S)=S+O(S^q)`,

`log_H(Ye_d)=Ye_d+O(Y^(p²))`.

In particular a rational bilinear change `log_G(S)·Σa_j log_(H,j)(Y)` contributes neither `S^pY_1` nor `SY_d^p`. An axes-normalized integral unit frame change adds or subtracts `log I`; its coefficient with `Y`-degree one, or with `S`-degree one, is integral because higher powers of `I−1` cannot contribute. This proves all invariance assertions following (PP1).

## 6. Actual torus action and the whole first homogeneous term

For `ζ^(q−1)=1`, put `a_j=[ζ^(p^j)]` in the coefficient Witt ring. The diagonal map `e_j↦a_j e_j` commutes with the display operators: `F(a_j)=a_(j+1)` with cyclic indices. Its action on the line's Teichmüller section is `S↦ζS`, so it is the Lubin–Tate `[ζ]`. The dual acts by the transpose diagonal matrix on `e_j^*`; the inverse dual therefore gives `Y_j↦ζ^(−p^j)Y_j`. The evaluation pairing is invariant under the line action and its inverse dual. Both lifts (PP8), their defects, and the scalar-one quotient frame are equivariant. Thus the cocycles in this very frame are invariant under (PP2).

Average any rational logarithmic splitting over this group of order `q−1`. It still splits the same cocycles. Its difference from any other invariant splitting is bilinear in the logarithm variables, but no monomial `x y_j` is invariant because `1−p^j` is nonzero modulo `q−1`. The invariant splitting is therefore unique.

For a mixed invariant monomial `S^a∏Y_j^(b_j)` of total degree at most `p+1`, put `b=Σb_j`, so `a,b≥1` and `a+b≤p+1`. Invariance requires

`a−Σp^j b_j≡0 mod (q−1)`.

The weighted sum lies between `pb` and `p^d b≤q`. If it equals `a`, the total-degree restriction forces `b=1`, `a=p`, and `j=1`. If it exceeds `a`, the only possible multiple of `q−1` is exactly `q−1`; the upper bound forces `a=1`, `b=p`, and every dual factor to be `Y_d`. Thus the only such monomials are `S^pY_1` and `SY_d^p`, both of degree `p+1`. There is none at smaller positive degree. Together with (PP1), this proves (PP3).

Changing from integral group coordinates to normalized logarithm coordinates has identity linear term. Since there is no smaller positive homogeneous term to feed into degree `p+1`, (PP3) is unchanged by this substitution. Taking the indicated derivatives yields (PP4).

For an integral function, `D_G^p` is divisible by `p` as an integral operator: translation coefficient at source degree `p` is `D_G^p/p!` because the scalar logarithm has no such nonlinear term. Similarly `D_d^p/p!` is an integral translation coefficient by the last-axis logarithm computation in §5. Thus both operators in (PP4) would give values divisible by `p` on integral functions. The primitive splitting gives explicit unit-valued exceptions to that integral-function hypothesis.

## 7. Numerical rate and diagonal consequences

Equation (PP5) follows directly from DP35 applied to the coefficient `−1/p` in total degree `p+1`. It holds in the stated frame and in every normalized integral unit frame because that coefficient retains valuation `−1`.

If `h>2`, then `d>1`. On the last-dual logarithmic diagonal

`x=t`, `y_d=εt`, `y_j=0` for `j<d`,

with `ε` a unit, the invariant splitting has the exact first term

\[
B(E_G(t),E_H(\varepsilon t e_d))
=1+\frac{\varepsilon^p}{p}t^{p+1}+O(t^{p+2}). \tag{PP17}
\]

For height two the two monomials occur on the same dual axis, and the coefficient is `(−ε+ε^p)/p`; it can vanish. Thus (PP17) is deliberately restricted to `h>2`.

For odd `p`, **still assuming `h>2`**, let `U` be any integral formal function on `G×H` with `U(0)` a unit, and put

`Θ(t)=U(E_G(t),E_H(εt e_d))·exp(b(E_G(t),E_H(εt e_d))/2)`.

Then

\[
v_p\bigl((p+1)![t^{p+1}]\Theta(t)\bigr)=0. \tag{PP18}
\]

Indeed `D=D_G+εD_d` has `D^p∈p End_int`: the pure powers are divisible by `p` as proved above, and every interior binomial coefficient is divisible by `p`. Thus the contribution from the integral `U` factor to its `(p+1)`st derivative is divisible by `p`. There are no earlier positive terms in the exponential gauge. Its degree-`p+1` contribution is

`U(0) ε^p (p+1)!/(2p)`,

a unit when `p` is odd. It cannot cancel the first, `p`-divisible contribution. For any prime, **with the same `h>2` restriction**, the statement holds with `exp(b/2)` replaced by `exp(kb)` for a unit scalar `k∈O`.

This is an exact finite-order obstruction to treating that normalized exponential as an integral formal function, including after multiplication by an integral local unit. It is not an asymptotic lower bound along every fixed diagonal and does not rule out cancellation in the specific harmonic operators of a theta construction. The opposite signs in (PP4) already exhibit why selected combinations require their own calculation.

A generic-path variant of the asymptotic rate is available after adjoining algebraically independent residue units. Restrict first to `S,Y_1`; its first coboundary remains integral and the `−S^pY_1/p` coefficient remains, so DP35 gives the same rate for this restricted two-variable series. Then set `S=t`, `Y_1=εt`, with the residue of `ε` transcendental over the coefficient residue field. Each nonzero homogeneous part gives a nonzero polynomial in `ε`; reduction of its least-valuation part cannot vanish. Consequently the degreewise minimum valuation is preserved on this formal generic diagonal, and the rate in (PP5) survives there. This requires the stated unramified residue-field extension and makes no assertion for a prescribed algebraic CM parameter.

## 8. Source locators and check status

Primary display source: T. Zink, *The display of a formal p-divisible group*, Astérisque **278** (2002), `https://www.numdam.org/article/AST_2002__278__127_0.pdf`. Exact locators: Definition19 and (22), p.143; Theorem81 and (145)–(146), p.204; Proposition106, p.226; the sign-defining embedding and (196), p.232; Artin–Hasse definition (210)–(211) and Proposition117, p.236; display pairing (216)–(218), pp.238–239; Proposition121, p.241; (243), p.246, and Theorem122, p.247. Local PDF SHA-256: `2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69`.

Actual Honda-line identification uses M. Hazewinkel, *On formal groups. The functional equation lemma and some of its applications*, Astérisque **63** (1979), §5, (5.1)–(5.4) and the accompanying uniqueness statement, p.77; `https://www.numdam.org/item/AST_1979__63__73_0.pdf`.

The display identities, dual orientation, Witt carry sign, degree filtration and first coefficients were derived and repeatedly challenged before writing at observed clocks between **01:45:31 UTC** and **01:50:38 UTC** on 2026-11-21. The root supplied the unit-factor derivative corollary after receiving the primitive coefficients. An independent primary-page review by `/root/archive_binomial` subsequently caught that Zink uses the negative Artin–Hasse normalization. This corrected version reverses both exact coefficient and derivative signs consistently; all valuations, nonintegrality, growth and unit conclusions are unchanged. The earlier positive-sign version described the inverse primitive class but did not explicitly identify that convention change. The source's Witt-vector negative has also been kept distinct from componentwise negation, including at `p=2`. Exact corrected hashes and reread events are recorded separately. No numerical computation or Lean formalization is claimed.
