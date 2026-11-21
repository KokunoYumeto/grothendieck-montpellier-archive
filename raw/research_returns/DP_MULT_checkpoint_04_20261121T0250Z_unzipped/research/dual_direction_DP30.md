# DP30: an actual Cartier-dual direction with no order-p divisibility

Date: **2026-11-21 UTC**. Author: `/root/step2_higher`, **GPT-6 Astra Pro**; runtime effort setting not exposed. This is a local mathematical result for the actual Cartier dual of a strict unramified CM line. It does not use the proposed two-dimensional logarithm as an unproved model for that dual, and it does not assert a global theta-pairing cost.

## 1. Result and scope

Let `A` be a complete mixed-characteristic discrete valuation ring with perfect residue field `k`. Suppose `A` contains the ring of integers `O` of the unramified degree-`h` extension of `Q_p`, where `h≥2`, and let `G` be a one-dimensional commutative formal `O`-module over `A`, strict for this embedding `O→A`, whose special fibre has p-height exactly `h`. Let `H=G[p^∞]^D` be its Cartier-dual p-divisible group. Write `widehat H` for the formal group belonging to the connected component of `H`; its dimension is `h−1`.

**DP30.** On `Lie(H_k)`, the restricted p-power operation has kernel dimension `1` and image dimension `h−2`. More precisely, it has a basis `e_0,…,e_(h−2)` in which

`e_i^[p]=e_(i+1)` for `0≤i<h−2`, and `e_(h−2)^[p]=0`.

The operation is Frobenius-semilinear, so this basis formula is understood with `(a e_i)^[p]=a^p e_i^[p]`. In particular, if `h>2`, there are a primitive integral invariant derivation `D` on `widehat H` and an integral formal coordinate `f` such that

\[
D^p f(0)\in A^\times,
\qquad v_p(D^p f(0))=0.
\]

Here primitive means that the tangent vector defining `D` is not in the maximal ideal times the tangent lattice. This is stronger than a toy rational-logarithm calculation: `H` is the actual Cartier dual. It shows that the positive order-p bound on the original one-dimensional height-`h` factor cannot be assigned to every primitive direction of its `(h−1)`-dimensional dual.

The statement does **not** say that an actual theta section has this coordinate as an entry, that the global chain uses this direction, that this unit forces a specified denominator or pairing loss, or that all shorter theta chains are impossible. Those statements would require additional geometric input.

## 2. Full proof

### 2.1. An integral coordinate makes the original law additive below degree q

Put `q=p^h`. For the Teichmüller roots `zeta∈mu_(q−1)⊂O^×`, strictness gives `[zeta]'(0)=zeta`. Starting from any integral coordinate `t`, define

\[
x(t)=\frac1{q-1}\sum_{\zeta\in\mu_{q-1}}\zeta^{-1}[\zeta](t).
\]

Since `q−1` is a unit and `x'(0)=1`, this is an integral strict change of coordinate. Reindexing the sum gives `x([eta](t))=eta x(t)` for every Teichmüller `eta`. Thus these endomorphisms are exactly linear in the coordinate `x`.

Let `F(X,Y)` denote the law in this coordinate. The endomorphism identity gives

\[
F(\zeta X,\zeta Y)=\zeta F(X,Y).
\]

A nonzero coefficient of total degree `n` therefore requires `n≡1 mod(q−1)`. In particular,

\[
F(X,Y)=X+Y+\text{terms of total degree at least }q. \tag{30.1}
\]

This holds integrally, hence also after reduction and after any Frobenius twist. No assertion about the integral logarithm of the dual has been used.

### 2.2. Compute the dual of the Frobenius kernel of H

For this subsection all groups are over `k`; suppress the reduction subscript. Let

`F_G:G→G^(p)`, `V_G:G^(p)→G`

be relative Frobenius and Verschiebung. They are Cartier dual to the corresponding Verschiebung and Frobenius of `H`, and their two compositions are multiplication by `p`. As `G` has dimension one and height `h`,

\[
|\ker F_G|=p,\qquad |\ker V_G|=p^{h-1}. \tag{30.2}
\]

Consider `V_G` restricted to `G^(p)[p]`. Its kernel is all of `ker V_G`, because this kernel is killed by `p`. Thus its image has order `p`. The identity `F_G V_G=[p]` shows that this image lies in `G[F]`. Both groups have order `p`, so

\[
\operatorname{im}\bigl(V_G:G^{(p)}[p]\longrightarrow G[p]\bigr)=G[F]. \tag{30.3}
\]

Apply exact Cartier duality to the kernel of the restricted map

`F_H:H[p]→H^(p)[p]`.

Its kernel is `H[F]`, and its dual map is the restricted `V_G` just computed. Consequently

\[
H[F]^D\simeq G[p]/G[F]. \tag{30.4}
\]

Height exactly `h` says `[p](x)=u(x)x^q` over `k`, with `u(0)≠0`; hence `G[p]` has coordinate algebra `k[x]/(x^q)`. The kernel of the iterated relative Frobenius `F_G^h` has the same defining ideal, so `G[p]=G[F^h]` as subgroup schemes.

Relative Frobenius induces a quotient isomorphism

\[
G[p]/G[F]\simeq G^{(p)}[F^{h-1}]. \tag{30.5}
\]

For clarity, this quotient statement can be checked directly on coordinates: if `r=p^(h−1)`, the map

\[
k[z]/(z^r)\longrightarrow k[x]/(x^q),\qquad z\longmapsto x^p,
\]

is injective and makes the target free of rank `p` with basis `1,x,…,x^(p−1)`. The morphism is therefore faithfully flat, with kernel `G[F]`.

By (30.1), the law on `G^(p)` is additive below total degree `q`. In the tensor coordinate algebra

`k[X,Y]/(X^r,Y^r)`,

every surviving monomial has total degree at most `2r−2<q` (also when `p=2`). All nonlinear terms of its group law therefore vanish. It follows that

\[
G^{(p)}[F^{h-1}]\simeq\alpha_{p^{h-1}},
\qquad
\boxed{H[F]^D\simeq\alpha_{p^{h-1}}}. \tag{30.6}
\]

Here `alpha_(p^(h−1))` means the kernel of the `(h−1)`st Frobenius on the additive group, with coordinate algebra `k[t]/(t^r)` and primitive coordinate `t`.

### 2.3. Compute the restricted Lie algebra without a Dieudonné convention

Set `P=H[F]`. Cartier duality interchanges multiplication and comultiplication in finite-dimensional Hopf algebras. By (30.6), the distribution Hopf algebra of `P` is

\[
\operatorname{Dist}(P)=k[t]/(t^r),\qquad
\Delta(t)=t\otimes1+1\otimes t. \tag{30.7}
\]

The Lie algebra of a finite group scheme is the space of primitive elements of its distribution algebra. This identification follows directly from the definition: a tangent vector is a `k`-linear map `u:O(P)→k` satisfying the augmentation Leibniz rule, and that rule is precisely `Delta(u)=u⊗1+1⊗u` in the dual Hopf algebra.

The primitive elements in (30.7) have basis

\[
t,t^p,\ldots,t^{p^{h-2}}. \tag{30.8}
\]

Here is a direct verification of completeness. The displayed powers are primitive by the characteristic-p binomial formula. Conversely, if `1≤n<r` is not a power of `p`, choose a nonzero base-p digit of `n` at an index `j` with `p^j<n`. The coefficient of `Z^(p^j)` in

`(1+Z)^n=product_i(1+Z^(p^i))^(n_i)`

is the nonzero digit `n_j`; equivalently `binomial(n,p^j)≠0 mod p`. Thus `Delta(t^n)` contains a nonzero mixed monomial `t^(p^j)⊗t^(n−p^j)`. Neither exponent reaches `r`, and terms from different `n` have different total degrees and cannot cancel this term. Constants are not primitive. This proves (30.8).

The restricted p-operation is the pth power in the distribution algebra. Indeed, if `u` is a tangent vector, its invariant derivation on the coordinate Hopf algebra is obtained from `(id⊗u)Delta`. Its pfold composition corresponds to the convolution power `u^p`; in characteristic `p`, this composition is again a derivation, by the iterated Leibniz formula. Therefore

\[
(t^{p^i})^{[p]}=t^{p^{i+1}},\quad 0\le i<h-2,
\qquad
(t^{p^{h-2}})^{[p]}=t^r=0. \tag{30.9}
\]

Since `k` is perfect, this semilinear map has image dimension `h−2` and kernel dimension one.

Finally, `P=ker F_H` has the same tangent space as `H`: the differential of relative Frobenius is zero, so `Lie(P)=ker(dF_H)=Lie(H)`. The inclusion respects the restricted p-operation, as follows from the functorial map on distribution algebras (or directly from invariant derivations). This proves the asserted restricted Lie algebra of `H_k`.

### 2.4. Lift to an integral invariant derivation with a unit pth derivative

The connected-component/formal-group equivalence gives an integral smooth formal group `widehat H` over `A`. Its dimension is `h−1`, since the dimensions of a p-divisible group and its Cartier dual add to their common height. The tangent lattice `Lie(widehat H/A)` is therefore free of rank `h−1`.

When `h>2`, choose `v∈Lie(H_k)` with `v^[p]≠0`, for example `e_0` in the displayed basis. Lift `v` to the integral tangent lattice and let `D` be its invariant derivation. The lift is primitive because its reduction is nonzero. Choose an integral coordinate `f` whose linear differential detects the nonzero tangent vector `v^[p]`; such a coordinate exists because coordinate differentials form a basis of the cotangent lattice. Reduction commutes with the integral derivation and its iterates, so

\[
\overline{D^p f(0)}
=\overline D^{p}\overline f(0)
=df_0\bigl(v^{[p]}\bigr)\ne0.
\]

Thus `D^p f(0)` is a unit of `A`, proving DP30. The argument uses the formal connected component only, so it needs no additional claim about all of `H` being connected. For the unramified Lubin–Tate example the full dual is connected as well, but that fact is not needed here. ∎

## 3. Interpretation for the original proposal

For a one-dimensional group of height `h>1`, the factorial-floor estimate at derivative order `p` gives `v_p(D^p f(0))≥1` for every integral function in a normalized primitive direction. DP30 gives a dual direction and an integral coordinate with valuation zero. Consequently one cannot replace a height-two line by a height-`h` line and then assign its improved one-dimensional divisibility to all directions of the accompanying dual factor.

The result is a local obstruction to that free-gain assumption. It is **not** a computation of a theta derivative, determinant, biextension logarithm, archimedean norm or global period. To turn it into a quantitative cost, one must prove that a required entry of the chosen mixed-type geometric theta kernel actually detects this nonzero restricted-p direction. None of that is established by the local Hopf argument.

The h=3 case is particularly concrete: `Lie(H_k)` has two basis vectors `e_0,e_1` with `e_0^[p]=e_1` and `e_1^[p]=0`. Thus a primitive dual direction loses the order-p divisibility, while the other lies in the restricted-p kernel. This also explains the degree-p unit seen in the previously proposed two-variable rational logarithm, without identifying that logarithm with the actual dual.

## 4. Exact primary sources and what was actually checked

The required external p-divisible-group facts are all in J. Tate, **p-Divisible Groups**, *Proceedings of a Conference on Local Fields* (1967), pp. 158–183. The inspected local file is

`research/Tate_PDivisible_1967.pdf`,

SHA-256 `720bf7128d4f048853435b083d18d0d863056c1f991942192a7f00daa7e424aa`.

Public source: `https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf`.

| Exact locator | Fact used | Inspection |
|---|---|---|
| §1.2, printed p. 159 (PDF p. 1, right half) | Cartier dual Hopf algebra; multiplication and comultiplication are dual; double dual is the original finite group | Extracted text and visually inspected the rendered page |
| §1.3, printed p. 160 (PDF p. 2, left half) | Exact finite group sequences, multiplicativity of orders, and exactness of Cartier duality | Extracted text and visually inspected the rendered page |
| §2.2, Proposition 1, printed p. 162, with connected-component sequence (4) on p. 164 | Connected p-divisible groups over a complete noetherian local base correspond to divisible commutative formal groups; the connected component has the dimension of the p-divisible group | Extracted text and visually inspected PDF pp. 3–4 |
| §2.2, diagram (3), printed p. 163 and continuation p. 164 | Frobenius and Verschiebung, both compositions equal p, finite kernels and surjectivity | Extracted text and visually inspected PDF pp. 3–4; the printed diagram number is (3) |
| §2.3, Proposition 3 and its proof, printed p. 166 (PDF p. 5, left half) | Dimensions of dual p-divisible groups add to height; Frobenius kernel has order p^dimension; F and V are Cartier dual | Extracted text and visually inspected the rendered page |

The coordinate averaging, quotient identification (30.5), additive truncation, primitive-element computation and integral derivative lift are proved in full here. They are not attributed to an unread Dieudonné equivalence, SGA3 theorem, or the proposed Hazewinkel logarithm. No Lean implementation or Lean execution of DP30 is claimed.

## 5. Actual check records

All records are by `/root/step2_higher`, **GPT-6 Astra Pro**, runtime effort not exposed, on **2026-11-21 UTC**. UTC times and hashes below identify observations, not fictitious independent reviewers.

| ID | Type | Object and actual work | Result |
|---|---|---|---|
| DD30-S-001 | Primary-source reading | Read Tate §1.2, §2.2 and §2.3 in extracted text and visually inspected PDF pp. 1, 3, 4 and 5; corrected the duality locator to printed p. 159 | Source supports the exact Hopf/F/V facts listed above |
| DD30-P-001 | Proof derivation/challenge | Derived (30.1)–(30.9); checked the orientation of finite Cartier duality, the rank-p image of restricted V, faithful flatness of the explicit quotient, the p=2 inequality, and semilinearity | No gap found in these steps; stated assumptions retained |
| DD30-P-002 | Integral-lattice and scope challenge | Verified that nonzero special-fibre tangent lifts primitively; a coordinate detects its nonzero restricted p-power; reduction of the integral derivative gives a unit; checked that no global theta conclusion follows without an entry identification | Local result only, with the geometric limitation explicit |
| DD30-S-002 | Additional primary-source reading | Visually inspected Tate PDF p. 2 / printed p. 160, confirming the exactness and order statements used in the finite quotient argument | Confirmed |
| DD30-P-003 | Whole-draft reread | Reread the complete statement and §§2.1–2.4, including all formulas, and §§3–4 for scope/source agreement; checked that the quotient argument identifies kernels, never V with an iterated Frobenius as a morphism | Passed; corrected only a displayed-TeX spacing artifact |
| DD30-I-001 | Reported independent review | `/root/formal_bound` independently challenged duality orientation, finite orders, the quotient, the degree cutoff, primitive dimension and lifting, and reported no flaw | Independent message retained in the conversation; not represented as this agent's own check |

These checks occurred before the new asymptotic-dual investigation. A file hash can be computed from this final saved version; it is intentionally not embedded into its own hash input. No Lean execution or general theta-kernel verification is claimed.

## 6. Separate archive-page observation

At **2026-11-21T00:59:53Z**, this agent independently viewed `archive_public/cote153_pdfpage003.png` from the official Montpellier cote 153 PDF (PDF p. 3, manuscript/page label 2), SHA-256 `48cadb02aaafc29540778b556dfe3e6fa890c914e8be9a84d2df3bc7e1456805`.

The page explicitly defines `F_n(T)=T(T−1)…(T−n+1)/n!`, gives product and composition expansions in that basis, and displays `direct_sum Z·F_n ⊂ Q[T]`. Integer product coefficients are explicitly annotated. No separate integer annotation is visible beneath the composition coefficients. This is direct binomial/composition source evidence; the page does not state the proposed B7 multiplicity transfer or a theta-lift comparison. This observation was sent separately to `/root/archive_binomial` and `/root` and must not be conflated with DP30's proof or sources.
