# DP43: optimal affine loss and periodic floor sums for cyclic CM displays

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. The root reserved finding **DP43**. This is a local formal-group theorem for the actual cyclic displays of DP40, including arbitrary unit arrow coefficients. It does not identify a global theta cost with a directional derivative bound.

## 1. Statement and hypotheses

Let `p` be any prime, `h≥2`, `q=p^h`, and let `A` be a nonempty proper subset of `Z/hZ`. Put

`m=|A|`, `l=h−m`, `s=1/(p−1)`.

Let `R=W(k)` for a perfect field `k` of characteristic `p`, with `v(p)=1`. Use the formal p-divisible group `H_(A,u)` of DP40, whose integral cyclic display has basis `e_a`, normal summand `T=⊕_(a∈A)W(R)e_a`, and arrows

`F e_a=u_a p^(1−1_A(a))e_(a+1)`, with `u_a∈W(R)^×`.

Its actual Cartier dual is the complementary type with reciprocal unit arrows, as proved in DP40. For each selected position `i∈A`, let `X_i` be the Teichmüller coordinate and `D_i` the normalized invariant derivation, so `D_iX_j(0)=δ_ij`.

For the digit calculation, define weights at **all** cyclic positions `a∈Z/hZ`, whether or not they are selected:

\[
r_a=\frac{\sum_{b\in A}p^{[a-b]_h}}{q-1},\qquad
c_a=s-r_a=\frac{\sum_{b\notin A}p^{[a-b]_h}}{q-1}.
\tag{CA1}
\]

Here `[a-b]_h` is the representative in `{0,…,h−1}`. In particular, the complement sum includes an exponent-zero term when `a∉A`. All these numbers satisfy `0<r_a,c_a<s`. Only the `c_i` with `i∈A` refer to invariant eigendirections.

For `i∈A` and `n≥0`, define the finite periodic floor sum

\[
E_i(n)=\sum_{\substack{u\ge1\\i+u\notin A}}
\left\lfloor\frac n{p^u}\right\rfloor,
\tag{CA2}
\]

where the membership condition is read modulo `h`. Then every integral formal function `f` satisfies, coefficientwise on the full formal group,

\[
\boxed{
v(D_i^n f)\ge
\max\left\{E_i(n),\;\left\lceil c_i n-(h-m)\right\rceil\right\}.}
\tag{CA3}
\]

Since `E_i(n)≥0`, this includes the optimal uniform affine estimate

\[
\boxed{v(D_i^n f)\ge\max\{0,\lceil c_i n-(h-m)\rceil\}.}
\tag{CA4}
\]

The constant `h−m` is exactly optimal for **every** selected direction, independently of the unit arrow coefficients. There is one common integral monomial witnessing optimality in all directions. If `next(a)` is the next selected position after `a` and `g_a∈{1,…,h}` is that forward gap, put

\[
f_A=\prod_{a\in A}X_a^{p^{g_a}-1}.
\tag{CA5}
\]

Then for every `i∈A`,

\[
\boxed{v(D_i^{q-1}f_A(0))=c_i(q-1)-(h-m).}
\tag{CA6}
\]

Consequently no smaller real constant can replace `h−m` in (CA4), even in a single fixed normalized eigendirection. The slopes themselves are sharp by DP40's sequence `v(D_i^(q^r)X_i(0))=c_i(q^r−1)`. Formula (CA2) is not asserted to be the exact universal optimum at every `n`; (CA3) combines two proved lower bounds.

## 2. Inputs from the already proved cyclic-display model

The following DP40 conclusions are used, including its arbitrary-unit-arrow extension:

1. The formal group and its Teichmüller coordinates are integral. The normalized invariant derivations commute and preserve integral functions.
2. Scaling coordinate `a∈A` by a scalar of valuation `r_a` makes the normalized logarithm and its inverse integral. The reduced scaled logarithm is `Id+M_η`, where

   `(M_η)_a=η_a X_(prev(a))^(p^(gap from prev(a) to a))`, with `η_a≠0` in the residue field.

   Its reduced inverse is `Σ_(t≥0)(−1)^t M_η^(∘t)`.
3. The contraction yields the coefficientwise estimate

   `v(D_i^n f)≥v(n!)−n r_i`.

4. The diagonal `q`-power coefficient is sharp:

   `v(D_i^qX_i(0))=c_i(q−1)`.

These inputs were proved from Zink's integral display construction, the exact divided-ghost logarithm and its unit path coefficients. No additional assertion about arbitrary deformations of the same Newton slopes is used here.

## 3. The periodic floor sum from integral rounding

Write `ε_a=1` when `a∉A` and `ε_a=0` otherwise. Formula (CA1) has the convergent base-`p` expansion

\[
c_a=\sum_{u\ge1}\varepsilon_{a+u}p^{-u}.
\tag{CA7}
\]

It follows that, for every `t≥0`,

\[
p^t c_i=b_i(t)+c_{i+t},\qquad
b_i(t)=\sum_{u=1}^t\varepsilon_{i+u}p^{t-u}\in\mathbb Z_{\ge0}.
\tag{CA8}
\]

Apply the scaled derivative bound to `n=p^t`. Legendre's formula gives

\[
v(D_i^{p^t}f)\ge p^t c_i-s=b_i(t)+(c_{i+t}-s).
\]

Because the coefficient ring is unramified, every finite coefficient valuation is an integer. Moreover `−1<c_(i+t)−s<0`, including `p=2`, where `s=1`. Thus rounding upward proves the integral operator inclusion

\[
D_i^{p^t}\bigl(R[[\mathbf X]]\bigr)
\subset p^{b_i(t)}R[[\mathbf X]].
\tag{CA9}
\]

For the base-`p` expansion `n=Σ_t n_t p^t`, compose these operators to obtain

\[
v(D_i^n f)\ge\sum_t n_t b_i(t)
=\sum_{u\ge1}\varepsilon_{i+u}\left\lfloor\frac n{p^u}\right\rfloor
=E_i(n).
\tag{CA10}
\]

The equality follows by interchanging finite sums and using `floor(n/p^u)=Σ_(t≥u)n_t p^(t−u)`. This proves the first part of (CA3) coefficientwise, with no asymptotic error.

## 4. A normalized qth derivative reduces to a primitive invariant derivation

Fix `i∈A` and write

\[
C_i=c_i(q-1)=\sum_{\substack{1\le u<h\\i+u\notin A}}p^{h-u}\in\mathbb Z_{>0}.
\tag{CA11}
\]

Since `i` is selected, `ε_(i+h)=0`; consequently `b_i(h)=E_i(q)=C_i`. By (CA9), the continuous `R`-linear operator

\[
\mathscr T_i=p^{-C_i}D_i^q
\tag{CA12}
\]

preserves the integral formal function ring. It commutes with translations, because `D_i` does.

We show that its reduction modulo `p` satisfies Leibniz's rule. For `0<k<q`, put `t=v_p(k)`. The exact binomial valuation is

\[
v_p\binom qk=h-t.
\tag{CA13}
\]

For example, write `binom(q,k)=(q/k)binom(q−1,k−1)`. The latter binomial coefficient is a unit modulo `p`, since `(1+Z)^(q−1)≡Σ_(a=0)^(q−1)(−1)^aZ^a` modulo `p`.

For each `1≤u<h`,

`floor(k/p^u)+floor((q−k)/p^u)=q/p^u−1_(u>t)`.

Therefore

\[
E_i(k)+E_i(q-k)
=C_i-\#\{u:t<u<h,\ i+u\notin A\}.
\tag{CA14}
\]

Combining (CA10), (CA13) and (CA14), every cross term of `p^(−C_i)D_i^q(fg)` has coefficient valuation at least

\[
h-t-\#\{u:t<u<h,\ i+u\notin A\}\ge1.
\tag{CA15}
\]

The last inequality holds because there are only `h−t−1` positions in the indicated open interval. Hence

\[
\overline{\mathscr T}_i(fg)
=f\,\overline{\mathscr T}_i(g)+g\,\overline{\mathscr T}_i(f).
\tag{CA16}
\]

It is a continuous invariant derivation of the special-fibre formal group. An invariant derivation is determined by its tangent value at the identity: differentiating the translation identity expresses it as the invariant extension of that tangent vector. Consequently it is a residue-field linear combination of the normalized invariant directions `bar D_a`, `a∈A`.

## 5. The cyclic torus isolates the original direction

We may make a finite unramified coefficient extension containing `F_q`. Such an extension preserves all valuations, integral coefficient inclusions and their descent. Choose a primitive `(q−1)`st root `ζ` in the extended ring.

The cyclic display has the automorphism

\[
e_a\longmapsto[\zeta^{p^a}]e_a.
\tag{CA17}
\]

Here brackets denote the Witt Teichmüller lift. Witt Frobenius sends `[ζ^(p^a)]` to `[ζ^(p^(a+1))]`, so this automorphism commutes with all Frobenius and `V^(−1)` arrows, even with arbitrary unit coefficients `u_a`. It preserves the normal decomposition. On the integral Teichmüller coordinate system its induced action is exactly `X_a↦ζ^(p^a)X_a`.

The normalized invariant direction `D_a` has the corresponding character `ζ^(p^a)` in the identity `D_a a_ζ^*=ζ^(p^a)a_ζ^*D_a`. The operator `mathscr T_i` has character `ζ^(q p^i)=ζ^(p^i)`. The characters `ζ^(p^a)` for `0≤a<h` are pairwise distinct, including modulo `p`. Thus the invariant derivation in (CA16) must have the form

\[
\overline{\mathscr T}_i=\bar a_i\bar D_i.
\tag{CA18}
\]

DP40's sharp coordinate coefficient gives

`mathscr T_iX_i(0)=D_i^qX_i(0)/p^(C_i)∈R^×`.

Choose `a_i` to be that unit, which already belongs to the original ring. The identity (CA18) descends from the unramified extension, so

\[
D_i^q=p^{C_i}a_iD_i+p^{C_i+1}\mathscr R_i,
\tag{CA19}
\]

where `mathscr R_i` is an integral continuous `R`-linear operator. It commutes with `D_i`, being a scalar combination of `D_i^q` and `D_i`. This proves the full operator recurrence, including the extra factor of `p` on the error; a sharp value on one coordinate alone would not have proved that recurrence.

## 6. Uniform affine bound

First let `0≤n<q`, with digits `n=Σ_(t=0)^(h−1)n_t p^t`. From (CA8) and (CA10),

\[
c_i n-E_i(n)=\sum_{t=0}^{h-1}n_t c_{i+t}
\le(p-1)\sum_{t=0}^{h-1}c_{i+t}=l.
\tag{CA20}
\]

For the last equality, summing (CA1) over all cyclic positions counts each of the `l` complementary positions against `Σ_(a=0)^(h−1)p^a=(q−1)/(p−1)`. Thus `Σ_(a∈Z/h)c_a=l/(p−1)`. This establishes the affine bound for all base orders `n<q`.

For `n≥q`, use (CA19):

\[
D_i^n f=p^{C_i}a_iD_i^{n-q+1}f
       +p^{C_i+1}\mathscr R_iD_i^{n-q}f.
\tag{CA21}
\]

Suppose by induction that the affine bound holds at every smaller nonnegative order. The first summand has coefficient valuation at least

`C_i+c_i(n−q+1)−l=c_i n−l`.

The second has valuation at least

`C_i+1+c_i(n−q)−l=c_i n−l+(1−c_i)`.

Since `0<c_i<s≤1`, this is at least `c_i n−l`. The operator `mathscr R_i` preserves every integral coefficient ideal, so the induction is coefficientwise. Integrality and upward integer rounding give (CA4). Combining it with the independently proved floor sum gives (CA3).

## 7. One common monomial proves the constant is optimal

Let `g_a` be the forward gap from selected position `a` to `next(a)`, and put `e_a=p^(g_a)−1`. The contraction weights obey the selected-edge identity

\[
p^{g_a}r_a-r_{next(a)}=1.
\tag{CA22}
\]

Summing after subtracting `r_a` gives

\[
\sum_{a\in A}e_a r_a=m.
\tag{CA23}
\]

Fix input direction `i∈A`. For each selected position `a`, let `d(i,a)∈{0,…,h−1}` be its forward cyclic distance from `i`, and put `N_a=p^(d(i,a))`. The first nonzero term in the inverse coordinate `E_a(t e_i)` has degree exactly `N_a`, and its coefficient has valuation

\[
r_a-N_a r_i.
\tag{CA24}
\]

Here are both required parts of that assertion. The torus action (CA17) forces every nonzero pure-`t` degree `N` in this coordinate to satisfy `N p^i≡p^a (mod q−1)`; the least positive possibility is `N=N_a`. In the reduced contracted inverse `Σ_(k≥0)(−1)^kM_η^(∘k)`, the unique path from `i` to `a` before completing a cycle has precisely that degree and a nonzero unit coefficient. Thus the least permitted term actually occurs, and scaling back gives its exact valuation. Arbitrary unit arrow coefficients cannot cancel this unique path.

Reading the selected positions cyclically from `i`, multiplication by `p^(g_a)` takes `N_a` to the next such degree, with the last degree going to `q`. Hence the telescope gives

\[
\sum_{a\in A}e_aN_a=q-1.
\tag{CA25}
\]

For the integral monomial `f_A=∏_a X_a^(e_a)`, the first nonzero coefficient of `f_A(E(t e_i))` therefore occurs at degree `q−1`. It is the product of the indicated leading coefficients, so there is no cancellation. Its exact valuation is

\[
\sum_a e_a(r_a-N_a r_i)=m-(q-1)r_i.
\tag{CA26}
\]

The digit sum of `q−1` is `h(p−1)`, so

`v((q−1)!)=s(q−1)−h`.

Multiplying the coefficient in (CA26) by this factorial proves

\[
v(D_i^{q-1}f_A(0))
=s(q-1)-h+m-(q-1)r_i
=c_i(q-1)-(h-m),
\]

which is (CA6). Because `c_i(q−1)=C_i` is an integer, a smaller real affine constant would contradict the ceiling bound already at this order. The optimal constant depends only on `h−m`, not on the arrangement of the selected gaps, although the slope `c_i` and the periodic floor sum depend on the entire cyclic type.

## 8. Boundary cases, sources and check scope

For a singleton type `m=1`, the witness is `X^(q−1)` and the affine loss is `h−1`, recovering the sharp one-dimensional result. For the complementary singleton type `m=h−1`, the affine loss is one, recovering DP34. The proof covers `p=2`: it uses neither division by two nor an exponential-radius lemma; the strict bound `0<c_a<s=1` suffices for rounding and induction.

The genuine formal-group inputs are the already checked DP40 cyclic-display construction. Its primary source is Zink, *The display of a formal p-divisible group*, Astérisque **278** (2002): normal-decomposition construction p.129, Theorem5 p.131 for height, Definition19/(22) p.143 for duality, Theorem81/(145)–(156) pp.204–207 for coordinates and divided ghosts, Proposition121 and Theorem122 pp.241 and247 for actual Cartier duality. Primary PDF: `https://www.numdam.org/article/AST_2002__278__127_0.pdf`; SHA-256 `2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69`.

The new proof consists of the periodic digit rounding, the normalized-q-operator Leibniz calculation, its torus character, affine induction and common sharp monomial. Actual complete saved-proof readings and independent challenges are recorded separately with hashes and observed times. No Lean execution, machine formalization or numerical test is claimed.
