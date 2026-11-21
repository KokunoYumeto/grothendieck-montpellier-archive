# DP63 — scalable HC partitions, a constant factorial prefactor, and allowed translates

Author: `/root/step2_higher`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Reasoning effort is not exposed. This memo builds on the complete checked DP61 row classification, DP58 sharp kernel value, and DP59 integral allowed-translate span. It does not instantiate the old `Datum.dom`/`CMObj.HasType`, or a replacement iterated theta image. In the geometric realization below the two abstract row blocks are explicitly labelled chosen formal directions; they are not asserted to be the actual conjugate CM-embedding blocks. That distinction is essential and is the separate DP65 task.

## 1. Statement

Fix rank parameters `k,m,t` satisfying the source `Ranks` conditions and fix a nonfinal stage `1≤j<m`. Put

\[
P=k+j-1,\qquad Q=m-j,\qquad n_V=P+Q+t,
\qquad H=(t+3)/2.
\tag{SF1}
\]

**DP63(a).** There are fixed antitone nonnegative integral partitions `A*` of length `P` and `B*` of length `Q` such that, for every pair of integers `a≥0` and `b≥t+2`, there is an actual `HCParam` whose selected partitions at stage `j` are

\[
A=A^*+ae_0,\qquad B=B^*+be_0.
\tag{SF2}
\]

These data also supply the literal algebraic `Wts.Ok` record by taking the same data for every word (and, if desired, every embedding). Both `A*,B*`, and thus their total degree and factorial product,

\[
D=|A^*|+|B^*|,\qquad
\mathcal F=\prod_{i=0}^{P-1}A_i^*!\prod_{s=0}^{Q-1}B_s^*!,
\tag{SF3}
\]

are independent of `a,b`. All active entries of the full partitions are positive.

**DP63(b).** The DP61 harmonic completion can be made nonzero by an integral prefactor of exactly the fixed degree `D`. In any product of smooth integral formal groups with normalized additive coordinates and identity-linear integral algebraic coordinates, the selected evaluation equals exactly

\[
\boxed{\mathcal F\,H_{a,b}(\lambda)},
\tag{SF4}
\]

provided the first two columns have the DP58 kernel and the other columns have normalized kernels with constant coefficient one. The prefactor is a monomial in integral algebraic coordinates on the filler columns. The equality is in additive coordinates, equivalently for the corresponding invariant differential operators.

**DP63(c).** On the actual Jacobian `J` at `p=11`, use `h=3` and the first dual direction of DP49. Let

\[
a_r=11^r,\qquad b_r=121\,11^r,
\qquad T_r=122\,11^r+D.
\tag{SF5}
\]

For all sufficiently large `r`, the preceding full numerical HC row partitions have a geometric normalized jet on a fixed product of copies of `J` with valuation exactly

\[
V_r=(11^r-1)/10+v_{11}(\mathcal F).
\tag{SF6}
\]

Moreover one can choose an actual tuple of the generic permitted translates of DP59, at an arithmetic level `M=29^e=O(T_r)` and tensor power `κ=M²=O(T_r²)`, for which this same full-row polynomial evaluation, including the normalization `M^(-T_r)`, has valuation at most `V_r`. Thus no uniform lower bound of the form `γT_r-C`, with `γ>1/1220` and fixed `C`, holds for all these chosen-direction, full-row, allowed-translate evaluations as the HC datum varies.

This is a statement about explicit chosen-direction row polynomials on actual geometric products, and the exact generic allowed-translate relation. It is not a statement that those direction labels are the old source's conjugate CM-embedding labels. The full `SizeData₂` scale, image membership, and global lift comparison are not supplied by this construction.

## 2. Explicit HC parameters and fixed residual partitions

Use `β_s,ε_s` for the source arrays ordinarily called `b_s,e_s`, to avoid collision with the sharp exponent `b`. Set

\[
v_i=k-2-i\quad(1\le i\le k-2),\qquad
v_0=v_1+a+1=k-2+a,
\tag{SF7}
\]

and

\[
u_i=v_i+1/2\quad(0\le i\le k-2),\qquad
u_{k-1}=-1/2.
\tag{SF8}
\]

Put `β_0=1`. For the first `m-2` gaps set

\[
\beta_{s+1}-\beta_s=2H\quad(0\le s<m-2).
\tag{SF9}
\]

For the final gap use

\[
\beta_{m-1}-\beta_{m-2}=
\begin{cases}
b+1&Q\ge2,\\
b+2H-1&Q=1,
\end{cases}
\qquad \epsilon_{m-1}=\beta_{m-1}+H.
\tag{SF10}
\]

Independently of the gap ranges, define `epsilon_s=beta_s+H` for every index `0≤s<m`, including `s=m−2`. These formulas include `m=2`, in which the range of ordinary gaps in (SF9) is empty.

### Verification of every HC field

The `v,β,ε` are integral and the `u` are half-integral. Each `u_i` is strictly above `v_i`; each `v_i` is strictly above `u_(i+1)`, since consecutive `v` gaps are one except for the first gap `a+1`. At the last index `v_(k-2)=0>−1/2=u_(k-1)`. Also `u_(k-1)=−1/2>−β_0=−1`. Every `ε_s−β_s=H`, and every `β_(s+1)−ε_s` is at least `H`: ordinary gaps are `2H`, the final gap in the first case is `b+1≥t+3=2H`, and the second case is `b+2H−1≥2H`. These are all fields in `Params.lean:50–69`.

At the fixed stage `j<m`, the formula for the positive partition involves only `ε_(j-1)`, the initial `β_0,…,β_(j-1)`, and `v`. None of those `β,ε` entries is the variable last entry `β_(m-1),ε_(m-1)`. Thus only `A_0` changes, and it changes by `a`. The DP61 identity gives `A_0−A_1=a`, so its residual first entry is `A_1`, fixed and positive.

If `Q≥2`, only the first reversed negative entry uses `β_(m-1)`. The identity `B_0−B_1=β_(m-1)−β_(m-2)−1` gives `B_0−B_1=b`. Thus `B_0−b=B_1`, fixed. If `Q=1`,

\[
B_0=\beta_{m-1}-\epsilon_{m-2}-(t+1)/2
=(b+2H-1)-H-(H-1)=b.
\]

Here the residual negative partition is the one-entry zero partition. All other entries are fixed. This proves (SF2) with antitone nonnegative residual partitions. The full partitions are positive by DP61(a), also directly by the verified HC fields.

For `Wts.Ok`, put the same HC tuple at every word and take its `RowPar` as the common row. The `row_ok` witness is that tuple, `hc_row` is reflexive, and first and last `u` coincide across words. This checks all four fields of `Columns/AbelianHostFieldConditions.lean:455–460`. It does not claim that the larger source construction `D7` or `SizeData₂` is thereby realized.

## 3. Exact factorial evaluation of the determinant filler

Use DP61's disjoint filler columns `C_+={c_0,…,c_(P-1)}` and `C_-={d_0,…,d_(Q-1)}`. The determinant polynomial

\[
Q=\mathcal D_{A^*}(X)\mathcal D_{B^*}(Y)
\]

has the diagonal monomial

\[
Z^\nu=\prod_{i=0}^{P-1}X_{i,c_i}^{A_i^*}
       \prod_{s=0}^{Q-1}Y_{s,d_s}^{B_s^*}
\tag{SF11}
\]

with coefficient exactly one. Indeed every chosen term from each determinant must be its diagonal term to avoid an off-diagonal variable. This argument also applies to powers of those determinants. Its total degree is `D`.

Choose integral formal coordinates `z` on the product formal groups whose differentials are the selected normalized tangent basis. In their additive logarithm parameters `Z`, one has `z=Z+terms of ordinary degree≥2`. The algebraic-coordinate monomial

\[
f=\prod_i z_{X_i,c_i}^{A_i^*}\prod_s z_{Y_s,d_s}^{B_s^*}
\tag{SF12}
\]

is integral. Its lowest homogeneous part is (SF11), of degree exactly `D`; all remaining parts have degree greater than `D`. It factors into one integral monomial for each filler column.

Every filler-column kernel has constant term one. Therefore the degree-`D` homogeneous part of `f` times the product of those kernels is still exactly `Z^ν`, irrespective of higher kernel coefficients. Since `Q(∂)` is homogeneous of degree `D`,

\[
Q(\partial)\left(f\prod_{c\in C_+\cup C_-}K_c\right)\big|_0
=Q(\partial)Z^\nu\big|_0
=\prod_i A_i^*!\prod_s B_s^*!=\mathcal F.
\tag{SF13}
\]

The remaining differential factor `P_(a,b)` uses only columns 1 and 2, so the whole evaluation factors as (SF4). Unused columns contribute their constant coefficient one. This proves (b). It uses a lowest ordinary degree argument, not a false assertion that additive logarithm coordinates are integral functions.

Combining (SF4) with DP58 at `a=ell^r,b=ell^(h-1+r)` gives the general fixed-prefactor valuation

\[
v_\ell(\mathcal F H_{a,b}(\lambda))
=\frac{\ell^r-1}{\ell-1}+v_\ell(\mathcal F),
\qquad\lambda\in R^\times.
\tag{SF14}
\]

In particular the limiting rate divided by total full row degree is

\[
\frac{1}{(\ell-1)(\ell^{h-1}+1)}.
\tag{SF15}
\]

The residual degree and factorial cost do not grow in this HC family. This demonstrates why the fixed-window exclusion in DP61 cannot be promoted to an exclusion for all varying HC data.

## 4. Actual product geometry and explicit copy indexing

For the geometric statement, use the actual good Jacobian `J` of DP49 at11, its normalized height-three line coordinate `x`, and its first dual coordinate `y_1`. DP49 identifies their actual original Jacobian characters as `3` and `2` respectively. They are both in `Φ123` and are not conjugate to one another. The following abstract two-row placement therefore must not be called the literal old conjugate-embedding placement.

Let

\[
B=J^{L},\qquad L=P+Q-1,
\tag{SF16}
\]

with product principal polarization, product trace-one line, and diagonal CM endomorphisms. In every column, choose the following distinct formal directions:

* `X_0=x` and `Y_0=y_1` in copy0;
* `X_i=x` in copy `i` for `1≤i<P`;
* `Y_s=y_1` in copy `P+s-1` for `1≤s<Q`.

All their unused formal partners and other directions are set to zero when the derivative is evaluated. The product primitive normalized kernel then restricts to the single sharp kernel in `X_0,Y_0`, since each other copy is restricted to one of its normalized axes. Thus columns1 and2 give exactly the DP58 two-column evaluation. Each filler column has constant term one, as required in (SF13). There are `n_V` independent copies of `B` in the column product. The geometric dimension and number of copies are fixed while `r` increases.

The invariant differential operator obtained from this coordinate assignment is an actual operator on that geometric product. The polynomial in the abstract labels satisfies every contraction, row-invariance and row-degree condition proved in DP61. The assignment does not claim those abstract two-block labels equal the full actual CM-embedding partition of `B`.

## 5. Realization by the generic permitted translate family

Give `B` its product line `L_B` and primitive product base section `s_B`. The DP59 construction extends directly to this fixed product. Here is a proof of the needed extension, including column counts.

Write `W_M(J)` for the integral translate module of DP59. With `alpha=(1+2delta)^e` and `M=29^e`, the allowed translates of `s_B` are tensor products of the allowed translates of `s` on the factors. Their points lie in `B[alpha²]`, and their symmetric theta lifts are tensor products of the individual symmetric lifts. The multiplication and rigidification identities multiply as well, so they satisfy the same generic `IsVtOver` relation with the product line.

For each factor, DP59 gives an integral basis of `W_M(J)` and surjectivity onto jets of order `T` as soon as `M≥cT+d`, with constants for that fixed factor. Tensor products of the factor basis sections give a finite integral generating family for their product span, which is exactly the span of the allowed product translates on `B`. No identification of the entire product section space is needed. This span has jets containing every monomial of total degree≤`T`: factor the monomial among the `L` factor-coordinate sets, choose a realizing jet of order `T` in each factor, and multiply. Each error has total order≥`T+1`, so the product agrees modulo that order. Linear combinations then realize every integral jet. Thus the same type of linear bound on `M` gives product jet surjectivity, with fixed constants because `L` is fixed.

Fix `r` and put `T=T_r`. In each column prescribe the integral algebraic prefactor jet which gives the desired normalized kernel times the monomial factor in (SF12), or just the pure kernel in columns1 and2 and unused columns. More precisely, in the exact integral frame of DP59, the actual normalized section has an integral unit frame factor `U^κ`; prescribe `U^(-κ)` times the desired monomial through order `T`. This is an integral jet. The compatible gauge and normalization are the ones in DP59; no claim is made for an arbitrary additional rational quadratic gauge.

Choose a section `F_c` from the product translate module realizing that jet in column `c`. Its full normalized germ agrees with the desired one through total degree `T`; all normalized kernels have zero negative ordinary degrees, so multiplication preserves this agreement. Applying the degree-`T` operator therefore gives exactly (SF6), by (SF13–14). Multiplication by the source normalization `M^(-T)` leaves its valuation unchanged because `M` is a11-adic unit.

Each `F_c` has an integral expansion in the finite product-translate generating family. Expand the `n_V`-fold product. The operator is multilinear in these sections, so the known nonzero value of valuation `V_r` is a finite sum of individual allowed-translate tuple values with integral scalar coefficients. If all those tuple values had valuation greater than `V_r`, the sum would have greater valuation. Hence at least one tuple has valuation at most `V_r`. We do not assert equality for this full-row tuple: DP59's special first-row rounding argument has not been extended here and is not needed.

Choose the least power29 satisfying the linear jet threshold. Then `M=O(T_r)` and `κ=M²=O(T_r²)`. Torsion and symmetric lifts are algebraic and integral after finite unramified extensions exactly as in DP59. The interpolation coefficients may lie in the completed coefficient ring; the witness tuple itself consists of the algebraic allowed generating translates, which is all the final assertion requires.

Finally `T_r=122·11^r+D`, while `V_r=(11^r−1)/10+v_11(F)`. Thus `V_r/T_r→1/1220`. A bound `v≥γT_r−C` for all these tuples, with `γ>1/1220` and fixed `C`, contradicts the tuple whose valuation is at most `V_r` for sufficiently large `r`. This proves (c).

## 6. Remaining scope

The HC data vary with `r`. The first positive gap and the last negative gap grow, so the fixed `SizeData₂` windows from DP61 cannot be held fixed. No source analytic cost estimate is supplied for this varying family. The old induced-quadratic CM type is not realized by the product, and its embedding labels are not silently replaced by chosen coordinate labels. Generic allowed translations and nonzero full-row evaluations do not imply membership in a chosen global theta image or nonvanishing of a specified final period. These are the exact remaining interfaces.

## 7. Provenance and checks

The HC and harmonic source locators and original archive hashes are those recorded for DP61. The mathematical dependencies are the complete saved proofs of DP58 and DP59; exact versions and actual whole-proof rereads are recorded separately. No Lean execution, machine certification, or new primary-source theorem is asserted. Complete saved-version checks are recorded only after they occur.
