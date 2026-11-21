# DP40 model theorem: actual cyclic displays and their sharp directional slopes

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. This is the formal-group realization accompanying `cyclic_cm_type_sum_DP40.md`. It applies to explicit integral cyclic displays, and to rank-one unramified CM displays once the displayed normal-form hypotheses are supplied. It does not identify a global theta cost with an equally weighted directional sum.

## 1. Model and theorem

Let `p` be prime, `h≥2`, `q=p^h`, and let `A` be a nonempty proper subset of `Z/hZ`. Write `m=|A|`. Work over an unramified complete valuation ring `R=W(k)`, with perfect residue field. On a free Witt module with cyclic basis `e_i`, put

`T=⊕_(i∈A)W(R)e_i`, `L=⊕_(i∉A)W(R)e_i`, `Q=L⊕I T`.

Choose arbitrary units `u_i∈W(R)^×` and define the Frobenius-semilinear display operators by

\[
F e_i=u_i p^{\epsilon_i}e_{i+1},\qquad
\epsilon_i=\begin{cases}0&i\in A,\\1&i\notin A,\end{cases}
\tag{CD1}
\]

with `V^(−1)e_i=u_i e_(i+1)` on `L` and the required rule on `I T`. Indices are modulo `h`. Let `H_(A,u)` be the resulting formal p-divisible group. In its Teichmüller coordinates `X_i` for `i∈A`, define

\[
r_j=\frac{\sum_{i\in A}p^{[j-i]_h}}{q-1},\qquad
c_j=\frac1{p-1}-r_j
=\frac{\sum_{i\notin A}p^{[j-i]_h}}{q-1},\quad j\in A.
\tag{CD2}
\]

Then `H_(A,u)` has height `h`, dimension `m`, and its actual Cartier dual is the complementary cyclic display

\[
H_{(A,u)}^D\simeq H_{(A^c,u^{-1})}. \tag{CD3}
\]

The normalized integral invariant directions `D_j`, `j∈A`, satisfy the coefficientwise mixed estimate

\[
v_p\left(\prod_{j\in A}D_j^{n_j}f\right)
\ge\max\left\{0,\sum_{j\in A}c_jn_j
-\frac{\sum_{j\in A}s_p(n_j)}{p-1}\right\}
\tag{CD4}
\]

for every integral formal function `f`. Each directional slope is sharp:

\[
v_p(D_j^{q^r}X_j(0))=c_j(q^r-1),\qquad r\ge0. \tag{CD5}
\]

No assumption that the units equal one is needed for these inequalities or sharp sequences.

For `u_i=1`, let `prev(j)` be the preceding member of `A` in cyclic order and let `g_j∈{1,…,h}` be the positive gap from `prev(j)` to `j`. Define

`M_j(X)=X_(prev(j))^(p^(g_j))`.

Then the normalized logarithm is explicitly

\[
L_A(X)=\sum_{n\ge0}\frac{M^{\circ n}(X)}{p^n}. \tag{CD6}
\]

This includes the Honda line when `A` has one element, and DP32's actual dual when `A` is its complement, after cyclic reindexing.

## 2. Integral displays, height, dimension and actual duality

The linearized normal-decomposition map `V^(−1)⊕F:L⊕T→P` is a monomial matrix with unit entries `u_i`. It is invertible. Thus (CD1) satisfies the display axioms, including `F=pV^(−1)` on `L` and the defining relation on `I T`.

On each complete cycle, Frobenius accumulates `h−m` powers of `p` times a unit. The dual accumulates `m` such powers. Because `0<m<h`, the corresponding Frobenius/Verschiebung nilpotence conditions hold after reduction modulo each `p^n`. More explicitly, repeated cycles eventually have first Witt component zero modulo that base's `p^n`, so their matrices lie in the Witt augmentation ideal, which is the required nilpotence condition. Zink's **Theorem5, printed p.131**, asserts that the associated group of a display is a formal p-divisible group of height equal to the rank of `P`, here `h`. Its tangent space is `P/Q`, of rank `m`, by Theorem4 and the exponential paragraph on the same page, or Theorem81/(155) later in the paper. The compatible reductions produce the group over the complete unramified ring.

For the evaluation pairing with the dual basis, the dual matrix is the same cyclic permutation with coefficients

`u_i^(−1) p^(1−ε_i)`.

Indeed `<F e_i,F′ e_j^*>=p δ_ij`, and the other identities in Zink Definition19, (22), follow on the normal-decomposition generators. The dual normal submodule has `T′=L^*` and `L′=T^*`. Thus its type is precisely `A^c`, with reciprocal units. Both groups are connected, so Zink's duality theorem, Proposition121 and Theorem122, identifies this as the actual Cartier dual. This proves (CD3), not merely an equality of Newton slopes.

## 3. Teichmüller coordinates and the logarithm

The map

`X↦Σ_(i∈A)[X_i]e_i`

into the display quotient is an integral formal coordinate system: its tangent map to `P/Q` is the identity. This is the same Teichmüller-section construction as in DP38.

First suppose `u_i=1`, and let `B` be the constant Frobenius matrix. On rational divided ghosts `z_n=w_n(z)/p^n`, the display resolution operator is `B·shift−1`. The logarithm of a lifted point is

\[
\operatorname{pr}_T\sum_{n\ge0}B^n z_n. \tag{CD7}
\]

It vanishes on the image of the normal resolution by telescoping and has identity differential. The finite-support and p-adic completion justifications are those established in DP41 §2. In the present general cycle, `B^h=p^(h−m)I`, so the same p-adic convergence argument applies.

For a Teichmüller coordinate `X_i`, its `n`th divided ghost is `X_i^(p^n)e_i/p^n`. A path from one selected position to the next selected position has length `g_j`, and exactly one unit Frobenius arrow: its starting position. Its numerator contains `p^(g_j−1)`, leaving coefficient `1/p`. A path crossing `k` such selected-to-selected gaps leaves denominator `p^k`. Projecting onto `T` therefore gives exactly (CD6).

For arbitrary unit arrows, let `B_n` be the matrix obtained by applying the `n`th Witt ghost to the unit entries of (CD1). Its nonzero entries are `w_n(u_i)p^(ε_i)`. Every `w_n(u_i)` is a unit in `R`: modulo `p` it is `w_0(u_i)^(p^n)`, and `w_0(u_i)` is a unit. The rational resolution operator is now the nonconstant shift

`z_n↦B_n z_(n+1)−z_n`.

Consequently the logarithm formula becomes

\[
\operatorname{pr}_T\left(z_0+\sum_{n\ge1}B_0B_1\cdots B_{n-1}z_n\right).
\tag{CD8}
\]

Every product follows a unique cyclic path. Each complete cycle has the same positive number `h−m` of powers of `p`, with an additional unit multiplier; convergence and the telescoping argument remain valid. Every logarithm monomial associated to a path crossing `k` selected gaps thus has coefficient

\[
\frac{\eta_{j,k}}{p^k},\qquad \eta_{j,k}\in R^\times. \tag{CD9}
\]

There is a unique path for the specified starting coordinate and ordinary degree, so distinct paths cannot cancel that coefficient. Formula (CD9), with its exact unit valuation, is all that the estimates below require. No false equality between the general unit-coefficient logarithm and an ordinary iterate of a fixed monomial map is asserted.

## 4. Weights and integral contraction

Since `A` is nonempty and proper, `0<r_j<s=1/(p−1)`, and hence `c_j>0`. The defining weights obey the exact selected-edge identities

\[
p^{g_j}r_{prev(j)}-r_j=1. \tag{CD10}
\]

To verify this, multiply the numerator of `r_(prev(j))` by `p^(g_j)`. For every selected index except `j`, its cyclic distance becomes the corresponding distance from `j` without wrapping; there is no selected index in the intervening open arc. The term belonging to `j` wraps once from exponent `h−g_j` to `h`. It changes from `1` to `q`, producing the difference `q−1`. This argument also covers the singleton type, where `prev(j)=j` and `g_j=h`.

Adjoin `π` with `π^(q−1)=p` and scale coordinate `j` by

`α_j=π^(Σ_(i∈A)p^([j−i]_h))`, so `v_p(α_j)=r_j`.

Scale both inputs and outputs of the logarithm by these factors. A path of one selected gap has coefficient of valuation zero by (CD9)–(CD10). A path of `k≥2` selected gaps has scaled coefficient valuation

\[
1+p^{g_1}+p^{g_1+g_2}+\cdots+p^{g_1+\cdots+g_{k-1}}-k>0.
\tag{CD11}
\]

The order of the gaps here follows the path backwards from its output; only positivity and the exact first-edge value are used. Therefore the contracted logarithm is integral with identity linear part and residue

\[
\overline{L'}=\operatorname{Id}+M_\eta,
\qquad (M_\eta)_j=\bar\eta_j X_{prev(j)}^{p^{g_j}},
\quad \bar\eta_j\ne0. \tag{CD12}
\]

When all original units are one, every `η_j=1`. In general `M_η` is still an additive polynomial map in characteristic `p`. It is topologically nilpotent for ordinary degree. Thus the contracted inverse is integral and has exact reduction

\[
\overline{E'}=\sum_{k\ge0}(-1)^kM_\eta^{\circ k}. \tag{CD13}
\]

At each fixed degree the sum is finite. After `m=|A|` selected arrows, a coordinate returns to itself with total Frobenius exponent `h`, hence degree `q`, and with a nonzero unit coefficient. In component `j`, after retaining only input coordinate `j`, the coefficient at degree `q^r` comes from exactly `mr` arrows and is a product of nonzero residue units, up to sign. It cannot cancel. Consequently

\[
v_p([t^{q^r}]E_j(t e_j))=-(q^r-1)r_j. \tag{CD14}
\]

These arguments include `p=2`; signs in characteristic two are read in the residue field, and no step divides by `2`.

## 5. Derivative bounds and exact sharpness

The formal-group law is integral, so the normalized invariant derivations are integral and commute. In logarithm coordinates they are ordinary partial derivatives. Integral contraction gives the coefficient estimate

`v_p([t^n]f(E(t)))≥−Σ_j r_j n_j`

for every integral `f`. Multiplying by the factorial and using Legendre's exact formula yields (CD4) at zero. Applying the same calculation to the integral translated function `f(F_H(X,Y))`, treating `X` as coefficient variables, proves it coefficientwise on the whole integral function ring. Integrality also supplies the lower bound zero.

For `f=X_j` and `n=q^r`, the exact inverse coefficient (CD14) gives

`v_p(D_j^nX_j(0))=v_p(n!)−(n−1)r_j=(n−1)(s−r_j)`,

because `s_p(n)=1`. This is (CD5), and proves that no larger asymptotic slope is valid for all integral functions in that primitive direction with a sublinear error.

For the complementary display, the same calculation interchanges `A` and `A^c`. Across the actual pair, all the sharp directional slopes are exactly

\[
\gamma_i(A)=\frac{1}{q-1}
\sum_{j:\,1_A(j)\ne1_A(i)}p^{[i-j]_h}.
\tag{CD15}
\]

The Fourier theorem in `cyclic_cm_type_sum_DP40.md` therefore applies to genuine sharp directional slopes of these actual dual display models. Its total is at most `h c_2`, with equality precisely for even alternating type; either type's partial sum is half the total. This remains an equal-direction local comparison and is not a global theta-cost theorem.

## 6. What rank-one unramified CM input suffices

The unit-arrow extension gives a precise sufficient interface. Suppose an integral display carries an action of an unramified degree-`h` order, and after a coefficient extension its underlying module decomposes into rank-one eigenspaces `P_i`, cyclically permuted by semilinear Frobenius. Suppose the Hodge filtration has the type prescribed above: `Q_i=I P_i` at the positions in `A` and `Q_i=P_i` elsewhere. Choose generators `e_i` of these free lines.

Commutation with the order action forces Frobenius and `V^(−1)` to move to the next eigenspace. Invertibility of the normal-decomposition map `V^(−1)⊕F` forces their nonzero arrow coefficients to be units. Thus the display has exactly form (CD1), and all the conclusions apply. This is an elementary normal-form consequence of the stated eigenspace and filtration hypotheses.

This memo does not silently supply those hypotheses for an arbitrary global CM object, nor assert that every deformation of the same height has this shape. A geometric application must identify its integral CM action, rank-one eigenspaces, cyclic Frobenius orbit and Hodge type. Once that data is proved, changing the unit arrow coefficients has no effect on the sharp local slopes computed here.

## 7. Primary sources and check scope

Zink, *The display of a formal p-divisible group*, Astérisque **278** (2002), exact locators: normal-decomposition matrix construction, p.129; **Theorem5, p.131** for height; Definition19/(22), p.143 for the dual; Theorem81/(145)–(156), pp.204–207 for the quotient, tangent space and divided-ghost logarithm; Proposition121 and Theorem122, pp.241 and247 for actual duality. Primary PDF `https://www.numdam.org/article/AST_2002__278__127_0.pdf`, local SHA-256 `2293c932bb6147a116eab9418b47646b34756d6b946e799d5eb16366c6b8ba69`.

The root independently proposed the unit-one model, weights and sharpness argument. This memo checked them, supplied the explicit unit-arrow extension and its source-normal-form scope, and read the exact height theorem in the primary text. The Fourier memo was independently read in full at observed clock **2026-11-21 02:12:28 UTC**: counting, orientation, Fourier eigenvalues, gap certificate, equality cases, cardinality refinement and all displayed height-six values passed. Separate metadata records the whole saved model-proof reading and exact hashes. No Lean execution or global theta-cost computation is claimed.
