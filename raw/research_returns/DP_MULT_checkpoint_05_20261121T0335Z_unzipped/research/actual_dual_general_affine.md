# DP34: sharp constant-one affine estimates on the actual Honda dual in every height

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. Root independently derived the same strengthening and suggested preserving the already checked height-three finding DP33 while assigning this all-height result DP34. This memo proves the additional operator estimate using the integral actual-dual model established in DP32. It does not identify a normalized theta kernel or prove a global cost estimate.

## 1. Statement and fixed model

Let `p` be prime, `h≥2`, `q=p^h`, `d=h−1`, and `R=W(k)` with `F_q⊂k`. Take the actual Cartier dual `H=G_h^D` of the Honda/Lubin–Tate line, in the integral coordinates supplied by DP32:

`M_1(X)=X_d^(p²)`, `M_i(X)=X_(i−1)^p` for `2≤i≤d`,

`L(X)=Σ_(n≥0) M^(∘n)(X)/p^n`.

When `d=1`, this means `M_1=X_1^(p²)`. Write `E=L^(-1)` and let `D_i` be the integral invariant derivations normalized by `D_iX_j(0)=δ_ij`. Put

`c_i=p^i/(q−1)`, `r_i=1/(p−1)−c_i`, `1≤i≤d`.

Then, for every integral formal function `f` and every `n≥0`, coefficientwise,

\[
D_i^n f\in p^{b_i(n)}R[[X_1,\ldots,X_d]],\qquad
b_i(n)=\max\{0,\lceil c_i n-1\rceil\}. \tag{GA1}
\]

The slopes `c_i` are optimal, by DP32's exact sequences

\[
v_p(D_i^{q^r}X_i(0))=c_i(q^r-1). \tag{GA2}
\]

The affine constant `1` is also optimal in every direction, attained at `n=q−1` by the single common monomial

\[
f_*(X)=\left(\prod_{j=1}^{d-1}X_j^{p-1}\right)X_d^{p^2-1}:
\qquad v_p(D_i^{q-1}f_*(0))=p^i-1=c_i(q-1)-1. \tag{GA3}
\]

For a multiindex `a`, composition gives the integral operator bound

\[
D_1^{a_1}\cdots D_d^{a_d}f
\in p^{\sum_i b_i(a_i)}R[[X]]. \tag{GA4}
\]

The operator inclusions are proved first over `Z_p` and persist after every integral base change. Thus they remain meaningful over ramified bases; no ceiling of an arbitrary ramified valuation is used in their proof.

## 2. Translation operators and the first cycle

Let `Δ_a` be the coefficient of the source monomial `S^a` in `f(F_H(X,S))`. All `Δ_a` preserve the integral ring. Since the formal group is commutative, they commute with one another and with the `D_i`. In characteristic zero the translation operator is

`exp(Σ_j L_j(S)D_j)`.

Along the source coordinate `S_i`, for `i<d`, the first nonlinear logarithm contribution is `S_i^p/p` in component `i+1`. Therefore

`Δ_(p e_i)=D_i^p/p!+D_(i+1)/p`.

Along coordinate `S_d`, the first nonlinear contribution is `S_d^(p²)/p` in component `1`, and there is no degree-`p` contribution. Hence

`Δ_(p² e_d)=D_d^(p²)/(p²)!+D_1/p`,

`Δ_(p e_d)=D_d^p/p!`.

For `d=1`, these last two formulas remain the correct formulas. In particular, with integral commuting operators `T_i` and units `a,b∈Z_p^×`,

\[
D_i^p=aD_{i+1}+pT_i\quad(i<d),\qquad a=-(p-1)!, \tag{GA5}
\]

\[
D_d^{p^2}=p^p bD_1+p^{p+1}T_d,\qquad
b=-\frac{(p^2)!}{p^{p+1}}\in\mathbf Z_p^\times, \tag{GA6}
\]

and `D_d^p∈p End_int`. Here `End_int` denotes the `Z_p`-linear operators preserving the integral formal function ring, and every displayed remainder commutes with the other displayed operators.

Put `R_i=p^(h−i)`. We claim

\[
D_i^{R_i}\in p\operatorname{End}_{\rm int}. \tag{GA7}
\]

For `i=d`, `R_d=p`, which was just proved. Descending induction uses (GA5), raised to `p^(h−i−1)=R_(i+1)`. Its leading term is a unit times `D_(i+1)^(R_(i+1))`, divisible by `p`; every other term has an explicit factor of `p`. This proves (GA7). Iteration gives

\[
D_i^n\in p^{\lfloor n/R_i\rfloor}\operatorname{End}_{\rm int}. \tag{GA8}
\]

## 3. The full q-order recurrence

For every `i`, we prove the more precise relation

\[
D_i^q=p^{p^i}u_iD_i+p^{p^i+1}U_i,
\qquad u_i\in\mathbf Z_p^\times,\quad U_i\in\operatorname{End}_{\rm int}. \tag{GA9}
\]

Fix `i<d` and put `B=p^i`. Start with `D_i^q`, and successively use (GA5) to move the leading term from `D_j` to `D_(j+1)` for `j=i,…,d−1`. At the step `j=i+t`, the power of `D_j` is `p^(h−t)`. Thus (GA5) is raised to

`N=p^(h−t−1)`,

where `N/R_(j+1)=p^i=B`. The `m`th nonleading binomial term, `1≤m≤N`, has divisibility at least

\[
v_p\binom Nm+m+\left\lfloor\frac{N-m}{R_{j+1}}\right\rfloor
=B+v_p\binom Nm+m-\left\lceil\frac m{R_{j+1}}\right\rceil. \tag{GA10}
\]

For `1≤m<N`, `N` is a power of `p`, so `v_p(binomial(N,m))≥1`; also `m−ceil(m/R_(j+1))≥0`. Thus the valuation is at least `B+1`. At `m=N`, the exact lower bound is `N`, and `N≥p^(i+1)≥p^i+1=B+1` because this is a step before the last direction. Consequently every step is valid modulo `p^(B+1) End_int`, and

`D_i^q ≡ (unit) D_d^(p^(i+1)) mod p^(B+1) End_int`.

Raise (GA6) to `p^(i−1)`. Factoring out `p^(p·p^(i−1))=p^B`, the remaining expression modulo `p` is a unit times `D_1^(p^(i−1))`. The chain (GA5), reduced modulo `p`, identifies that power with a unit times `D_i`. This proves (GA9) for `i<d`.

For `i=d`, apply the same final argument directly: raise (GA6) to `p^(d−1)`, obtaining `D_d^q`, factor out `p^(p^d)`, and use the chain modulo `p` to identify `D_1^(p^(d−1))` with a unit times `D_d`. This also covers `d=1`, where the exponent is `1` and (GA9) is simply (GA6). No endpoint case is omitted, and all inequalities hold for `p=2`.

## 4. Affine induction and the integer exponent

Fix `i`, and abbreviate `c=c_i`, `R=R_i`, `B=p^i`. Then

`B=c(q−1)`, `cR=q/(q−1)`, and `0<c<1`.

For `0≤n<q`,

\[
\lfloor n/R\rfloor\ge cn-1. \tag{GA11}
\]

Indeed, within each interval `kR≤n<(k+1)R`, the difference `cn−floor(n/R)` increases with `n`. Its maximum at the last point of each interval increases with `k`, because `cR−1=1/(q−1)>0`. The final point `n=q−1` gives exactly `1`. Thus (GA8) proves (GA1) for the base range.

For `n≥q`, apply (GA9) to `D_i^(n−q)f`. Induction in the first term gives the real lower bound

`B+c(n−q+1)−1=cn−1`.

In the second term, integrality of `U_i` gives

`B+1+c(n−q)−1=cn−1+(1−c)≥cn−1`.

All coefficients are integral and have integer valuations over `Z_p`, so the actual integral power of `p` is at least `max(0,ceil(cn−1))`. This proves the integral operator inclusion over `Z_p`; scalar extension proves it over `R` and every further integral base. Composing the inclusions gives (GA4).

## 5. A simultaneous sharp witness in all directions

Let `e_j=p−1` for `j<d`, and `e_d=p²−1`, so `f_*=∏X_j^(e_j)`. We need the first nonzero term of each `E_j(te_i)`, not merely the first unit term in a scaled reduction.

The logarithm satisfies the exact Teichmüller equivariance

\[
L_j(\zeta^pX_1,\zeta^{p^2}X_2,\ldots,\zeta^{p^d}X_d)
=\zeta^{p^j}L_j(X),\qquad \zeta^{q-1}=1. \tag{GA12}
\]

For an ordinary arrow the exponent identity is `p·p^(j−1)=p^j`; for the exceptional arrow it is `p²·p^d=p^(h+1)≡p mod (q−1)`. Hence every iterate of `M` has the required character. The inverse `E` has the same equivariance.

It follows that a nonzero coefficient of degree `n` in `E_j(te_i)` must satisfy `np^i≡p^j mod (q−1)`. Its smallest possible positive degree is therefore

\[
m_{ij}=\begin{cases}
p^{j-i},&j\ge i,\\
p^{h+j-i},&j<i.
\end{cases} \tag{GA13}
\]

DP32's scaled inverse has reduction `Σ_(n≥0)(−1)^n M^n`. The first path from coordinate `i` to coordinate `j` contributes exactly a nonzero sign at degree `m_ij`, with no other contribution at that degree. Therefore the coefficient of `t^(m_ij)` in `E_j(te_i)` has exact valuation

\[
r_j-m_{ij}r_i. \tag{GA14}
\]

Equivariance excludes every lower degree, so the lowest-degree term of `f_*(E(te_i))` is the product of these leading terms and is unique. Direct telescoping yields

\[
\sum_j e_jm_{ij}=q-1\quad\text{for every }i. \tag{GA15}
\]

For clarity, the three ranges `i≤j<d`, `j=d`, and `j<i` contribute respectively

`p^(d−i)−1`, `p^(h−i+1)−p^(d−i)`, and `q−p^(h−i+1)`.

Their sum is `q−1`, with an empty range contributing zero. Also

`Σe_j=(p−1)(h+p−1)` and `Σe_jp^j=p(q−1)`,

so

\[
\sum_j e_jr_j=h-1=d. \tag{GA16}
\]

Thus the coefficient of degree `q−1` in the substituted monomial has valuation `d−(q−1)r_i`. Since the base-`p` digits of `q−1` are all `p−1`,

`v_p((q−1)!)=(q−1)/(p−1)−h`.

Adding this factorial valuation gives

\[
v_p(D_i^{q-1}f_*(0))=c_i(q-1)-h+d=p^i-1,
\]

which proves (GA3). This argument includes height two and characteristic two and proves sharpness without any numerical experiment.

## 6. Sources, dependency and check status

The integral model and its identification as the **actual** Cartier dual are used from DP32, independently reviewed in `actual_dual_independent_review.md`. That construction cites Hazewinkel, *On formal groups. The functional equation lemma and some of its applications*, Astérisque 63 (1979), Lemma 2.3, pp. 74–75, and §5, p. 77; and Tate, *p-Divisible Groups* (1967), §2.2–2.3. The new affine argument itself is the explicit translation-operator proof above; no claim of historical novelty is made.

**GA-C1 (independent derivation):** `/root/formal_bound` derived the all-height recurrence and common witness before messaging the root at the observed clock interval beginning **01:21:39 UTC**, after the earlier height-three review. The root replied that it had independently derived the same result and supplied another recurrence induction. The sibling `/root/step2_higher` independently verified the common witness and its two sums; this is an attributed check, not a self-check.

The complete saved proof receives a subsequent reread/hash event. No Lean compilation, formalization, or computational verification is claimed here.
