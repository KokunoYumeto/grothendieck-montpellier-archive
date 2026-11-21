# DP35: denominator rigidity for an actual Poincaré splitting

Date: **2026-11-21 UTC**. Written and independently challenged by `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. The root independently supplied the bounded-denominator argument, its uniform-contraction strengthening, the characteristic-zero integration, and the primitive-initial-form extension. This memo gives complete proofs with the hypotheses separated. It concerns rational splittings compatible with both group laws, not the existence of an integral local frame of the underlying line bundle.

## 1. Algebraic statement using only the first coboundary

Let `R` be a complete discretely valued extension ring of `Z_p`, with fraction field `K` and valuation `v(p)=1`. Let `F` be an integral commutative formal group, in `a≥1` variables `S`; let `T` be an additional list of formal variables. Suppose

`B(S,T)∈K[[S,T]]`, `B(0,T)=B(S,0)=1`,

and the first multiplicative coboundary

\[
C_F(S,S',T)=\frac{B(F(S,S'),T)}{B(S,T)B(S',T)}
\tag{P1}
\]

belongs to `R[[S,S′,T]]^×`. Its constant coefficient is `1`. Then:

**DP35(a).** If the coefficients of `B` have bounded denominators, then `B∈R[[S,T]]^×`.

Equivalently, if `B` is not integral, its coefficient valuations have infimum `−∞`. No second group law, biextension classification, or nontriviality assumption is needed for this statement.

### Proof

For a nonzero bounded-denominator series `A`, write

`ν(A)=min_α v(A_α)`.

The minimum exists because the value group is discrete. It satisfies `ν(AA′)=ν(A)+ν(A′)`: multiply each factor by a suitable power of a uniformizer to make its least valuation zero, and reduce modulo that uniformizer. Both reductions are nonzero in a power-series ring over the residue field, which is a domain. Thus their product is nonzero. This proof applies in any finite number of variables and does not require a coefficient of least *degree* to attain the least valuation.

If `φ(S)` is an integral formal substitution with zero constant term, then `ν(A(φ(S),T))≥ν(A)`; the substituted series remains bounded, since each fixed coefficient is a finite integral linear combination of coefficients of `A`. If `U` is an integral unit with constant coefficient `1`, then `ν(U)=0`.

Iterating (P1) through `p` additions gives

\[
B([p]_F(S),T)=B(S,T)^p U(S,T),\qquad
U=\prod_{j=1}^{p-1}C_F([j]_F(S),S,T)\in R[[S,T]]^\times.
\tag{P2}
\]

Consequently

`ν(B)≤ν(B([p]_F(S),T))=pν(B)`.

It follows that `(p−1)ν(B)≥0`, hence `ν(B)≥0`. Since `B(0,0)=1`, the minimum is exactly zero and `B` is an integral unit. This proves DP35(a), including the ramified case.

## 2. Uniform contraction forces a positive linear denominator rate

For a real number `t≥0`, define the uniform weighted infimum

\[
w_t(B)=\inf_\alpha\{v(B_\alpha)+t|\alpha|\}. \tag{P3}
\]

**DP35(b).** For every rational `t>0`, `w_t(B)` is either `0` or `−∞`. If some coefficient of positive total degree `N` has valuation `−m<0`, then for every rational `0<t<m/N` and every real `M`, there is a coefficient with

\[
v(B_\alpha)+t|\alpha|<-M. \tag{P4}
\]

In particular the denominators grow at least linearly along a sequence of degrees:

\[
\liminf_{|\alpha|\to\infty}\frac{v(B_\alpha)}{|\alpha|}\le-\frac mN.
\tag{P5}
\]

Here the liminf is taken over nonzero coefficients; absent coefficients can equivalently be assigned valuation `+∞`. This gives a definite positive rate after one nonintegral coefficient is known, but it does not canonically identify the best rate.

### Proof

Choose a finite ramified extension with an element `λ` of valuation `t`. The contracted formal group

`F_λ(S,S′)=λ^(−1)F(λS,λS′)`

is integral: its linear terms are unchanged and every coefficient of total degree `d≥2` is multiplied by `λ^(d−1)`. Define

`B_λ(S,T)=B(λS,λT)`.

Its first coboundary for `F_λ` is exactly `C_F(λS,λS′,λT)`, an integral unit. If `w_t(B)>−∞`, then `B_λ` has bounded denominators. Part (a), over this discretely valued extension, makes `B_λ` integral. Its constant term is `1`, so `w_t(B)=0`.

If a degree-`N` coefficient has valuation `−m`, then for `t<m/N` it has negative weighted valuation. Thus `w_t(B)≠0`, forcing `w_t(B)=−∞` and proving (P4). Any sequence supplied by (P4) with `M→∞` has degrees tending to infinity, because only finitely many coefficients have bounded total degree. It yields liminf at most `−t`. Letting rational `t` increase to `m/N` proves (P5).

## 3. Unit frames, powers of p, and a useful class of vanishing sections

Multiplication by an integral unit `I∈R[[S,T]]^×` cannot make the coefficients of a nonintegral `B` bounded: if `p^M IB` is integral, then multiplication by the integral inverse `I^(−1)` makes `p^M B` integral, contradicting (a). Thus no fixed `p^M` and no integral unit change of frame repairs such a splitting.

There is also a precise extension to certain vanishing sections. Let `f∈R[[z_1,…,z_n]]` be nonzero, and let `f_m` be its first nonzero homogeneous part. Suppose `f_m` is primitive, meaning at least one of its coefficients is a unit. Then

\[
p^M fB\in R[[z]]\quad\Longrightarrow\quad p^M B\in R[[z]]. \tag{P6}
\]

To prove this, set `A=p^M B` and induct on the degree `n` of its homogeneous parts. In degree `m+n`, the product is

`f_m A_n + Σ_(j>m) f_j A_(m+n−j)`.

Every `A` term in the sum has degree less than `n`, and is integral by induction. Therefore `f_mA_n` is integral. The polynomial Gauss valuation is multiplicative by the same residue-domain argument, and `ν(f_m)=0`; hence `A_n` is integral. The induction begins in degree zero and proves (P6).

This argument does **not** apply to every vanishing theta section. For example `f=p−z` and `B=(1−z/p)^(−1)` satisfy `fB=p`, although `B` has unbounded denominators; the first homogeneous part of `f` is the nonprimitive constant `p`. This example is an algebraic warning about arbitrary multipliers, not an assertion that this `B` satisfies a formal-group coboundary hypothesis. A prescribed theta section must be checked for the primitive-initial-form condition or another specific cancellation mechanism. A unit minor somewhere in a larger jet matrix is not automatically this condition for the chosen scalar section.

## 4. Existence of rational compatible splittings in characteristic zero

Assume now that `F` is one-dimensional and `H` is a formal group of dimension `d`. An integral normalized frame of a biextension gives symmetric normalized integral unit cocycles `C_F(S,S′,T)` and `C_H(S,T,T′)`, satisfying their two cocycle identities and the interchange identity. We show explicitly that a rational normalized splitting `B` exists.

Use characteristic-zero logarithmic coordinates `x∈K`, `y∈K^d`, so both group laws become addition. Let `A=log C_F`, `C=log C_H`. Their axes vanish. Use the convention

`δ_xβ=β(x+x′,y)−β(x,y)−β(x′,y)`,

and the corresponding convention in the `y` variables. The interchange identity is `δ_yA=δ_xC`.

Define

`a(x,y)=∂_(x′)A(x,x′,y)|_(x′=0)`,

`β_0(x,y)=∫_0^x a(u,y)du`.

Differentiating the normalized two-cocycle identity gives

`∂_(x′)A(x,x′,y)=a(x+x′,y)−a(x′,y)`.

As `a(0,y)=0`, integration and normalization give `δ_xβ_0=A`. The interchange identity implies

`δ_x(δ_yβ_0−C)=0`.

A characteristic-zero series additive in the scalar variable `x` is linear in `x`, so

`δ_yβ_0−C=x d(y,y′)`

for a symmetric normalized additive two-cocycle `d` in the `d`-dimensional group. Put

`b_i(y)=∂_(y′_i)d(y,y′)|_(y′=0)`.

Differentiating its cocycle identity gives

`∂_(y′_i)d(y,y′)=b_i(y+y′)−b_i(y′)`.

Commuting these derivatives shows that `∂_j b_i−∂_i b_j` is constant. Symmetry of `d` makes that constant zero by evaluating mixed derivatives at the origin. Hence the formal one-form `Σb_i(y)dy_i` is closed. Its characteristic-zero radial primitive

`γ(y)=∫_0^1 Σ_i y_i b_i(ty)dt`

has derivative `b_i` and `γ(0)=0`. The same differentiated identity and normalization show `δ_yγ=d`. Therefore

\[
\beta=\beta_0-x\gamma(y),\qquad B=\exp\beta \tag{P7}
\]

solve both multiplicative coboundary equations in additive coordinates. In the original integral group coordinates, the required series is explicitly `B(S,T)=exp β(log_F(S),log_H(T))`. All integrals are coefficientwise formal integrals in characteristic zero. The axes are normalized. Two solutions differ, after taking logarithms, by a bilinear form `x Σ_i a_i y_i`; no integrality of such a rational bilinear gauge is asserted.

## 5. Application to the actual primitive Poincaré class

Let `G=G_h` be the Honda/Lubin–Tate line over `R=W(F_(p^h))`, with `h≥2`, and let `H=G^D` be its actual connected Cartier dual. Use the integral actual-dual model from DP32 if explicit coordinates are required. The following exact primary results justify the application:

* Zink, *The display of a formal p-divisible group*, Astérisque **278** (2002), §4.2, **Lemma 111, p.230**: a torsor under an exact functor over a prorepresentable formal object is trivial. Applied to the formal multiplicative group and the product formal disc, this gives an underlying integral local frame. Its restrictions to the two axes can be adjusted by integral units to agree with the canonical rigidifications. This is a frame, not a bilinear section.
* Zink, §4.3, **(216)–(218), pp.238–239**: a bilinear pairing of displays defines the biextension through explicit Artin–Hasse cocycles on the two display resolutions.
* Zink, §4.4, **Proposition 121, p.241**, **(243), p.246**, **diagram (244) and Theorem 122, p.247**: for connected dual displays over the nilpotent rings `R/p^n`, the pairing construction identifies the evaluation pairing with the identity in `Hom(G,H^D)=End(G)`. Both connectedness conditions hold for the slopes `1/h` and `(h−1)/h`. The nilradical of `R/p^n` is nilpotent, as the theorem requires. The pairing classes are functorially compatible under reduction. The frames can be chosen compatibly as well: start with a frame modulo `p`; at each step choose a frame one level higher, compare its reduction with the already selected frame, and lift the comparison unit using the surjection `(R/p^(n+1))[[z]]^×→(R/p^n)[[z]]^×`. Adjusting by that lift gives a compatible frame. Axis rigidifications may be maintained by the same normalized-unit adjustment. Taking the inverse limit therefore supplies integral cocycles over `R`, rather than merely unrelated frames at each finite level.

The evaluation pairing is primitive: its associated homomorphism is the identity, which cannot be `p` times an integral endomorphism because its differential is `1`, whereas the latter differential would be divisible by `p`. Its class also remains nonzero already on the special fibre; this nonvanishing is a separate assertion, not the criterion for primitivity. Therefore the actual integral Poincaré biextension has no integral bilinear splitting. Its integral local frame supplies cocycles; §4 supplies rational normalized splittings. Every such `B` is nonintegral, since an integral `B` with constant term `1` would be an integral unit and trivialize both group laws, making the class zero. Sections 1–2 then imply that **every rational compatible splitting of this primitive class has unbounded denominators and a positive linear denominator rate**. Sections 1–3 also show that no fixed power of `p`, integral unit frame, or multiplier with primitive first homogeneous part can remove those unbounded denominators.

This is a one-way obstruction. A trivial biextension can also acquire a rational bilinear gauge with unbounded denominators. Thus the condition is not a test characterizing nontrivial classes, and a particular rate is not determined until a normalization is fixed. The theorem does not by itself compute the selected harmonic jets of a geometric theta section multiplied by its specified exponential gauge.

The same conclusion applies to `B^k` for every nonzero integer `k`, and, if `p` is odd, to `B^(k/2)`. Its cocycles are the corresponding powers of the integral cocycles; a square root with constant term `1` is integral when `2` is a unit, by formal coefficient recursion. The associated class is the nonzero scalar multiple `k·id` or `(k/2)·id`. Such a homomorphism is nonzero: the endomorphism group of a p-divisible group is torsion-free, since multiplication by `p` is an epimorphism as an fppf sheaf and multiplication by integers prime to `p` is invertible. Thus each power is again nonintegral and §§1–2 apply. This does not assert a uniform numerical rate for all multiples, or an obstruction to harmonic jet cancellation.

## 6. Exact display-to-cocycle formula and concrete next choice

Write the display resolutions as

`0→Q --d=V^(−1)−id→ P →G→0`,

`0→Q′ --d′=V′^(−1)−id→ P′ →H→0`.

The symbols include the Witt-vector functors on nilpotent test algebras as in Zink (217). Choose normalized formal set-theoretic lifts `σ:G→P` and `τ:H→P′`. Such lifts exist by Lemma111: `Q` and `Q′` are exact functors by the normal decomposition (145), so their torsors over the formal discs have sections. Define their defects uniquely by

`d κ_G(g,g′)=σ(g)+σ(g′)−σ(g+g′)`,

`d′ κ_H(h,h′)=τ(h)+τ(h′)−τ(h+h′)`.

Uniqueness uses injectivity in Zink Theorem81/(146). Proposition106, p.226, and (218) then give the two multiplicative cocycles in the induced frame:

\[
C_G(g,g',h)=\operatorname{hex}\langle V^{-1}\kappa_G(g,g'),\tau(h)\rangle,
\tag{P8}
\]

\[
C_H(g,h,h')=\operatorname{hex}\langle\sigma(g),\kappa_H(h,h')\rangle^{-1}.
\tag{P9}
\]

Here the minus sign in Zink's additively written formal multiplicative group becomes an inverse. The first formula is checked directly by adding two lifted sections and replacing `σ(g)+σ(g′)` by `σ(g+g′)+dκ_G`; the quotient relation of Proposition106 multiplies the scalar by `α_1`. The second formula is the same calculation with `α_2`.

Thus the remaining computational choice is precise: select a normal decomposition of the actual Honda display, choose its Teichmüller-coordinate lifts, solve the two defect equations, and apply `hex`. These formulas are more information than the abstract nonzero class. A separate calculation below or in a successor memo will test the first nonintegral coefficients; no guessed coefficient is included in the present proved statement.

## 7. Primary-source provenance and check scope

Published primary PDF: `https://www.numdam.org/article/AST_2002__278__127_0.pdf`.

Local file `Zink_2002_Display.pdf`, SHA-256 `2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69`. Exact source sections were reread at the observed clocks **01:41:28 UTC** and **01:42:33 UTC** on 2026-11-21. A new web-open attempt at that time was rejected by the retrieval service because the PDF is 11,718,483 bytes; the already downloaded and previously visually inspected primary PDF supplied the actual source text. Failed web retrieval is not counted as a fresh source verification.

The complete arguments in §§1–5 were independently challenged before writing: discrete Gauss minima and multiplicativity, integral substitution, the ramified contraction, limiting degree argument, homogeneous induction, all characteristic-zero integrability signs, and the distinction between a frame and bilinear splitting were checked. A whole-saved-draft reread and exact hash are recorded separately. No computation, Lean execution, or formalization is claimed.
