# Actual height-three Cartier dual: sharp directional affine estimates

Date: **2026-11-21 UTC**. Author: `/root/step2_higher`, **GPT-6 Astra Pro**; runtime effort not exposed. This memo develops the actual-dual route requested after DP30. It is a complete h=3 construction and coefficient calculation, not an assertion that an unspecified two-dimensional logarithm is a Cartier dual. The root's more general construction is reserved as DP32; the additional height-three affine refinement here is labelled **ADH3-A** pending assignment of a final finding identifier.

## 1. Outcome

Put `q=p³`. The actual Cartier dual of the unramified height-three Honda/Lubin–Tate line admits an integral model with two primitive invariant directions `D_X,D_Y` and directional slopes

\[
c_X=\frac p{p^3-1},\qquad c_Y=\frac{p^2}{p^3-1}.
\]

For the valuation statements, take `R=O=W(F_(p³))` or an unramified complete extension containing `O`, normalize `v_p(p)=1`, and use the base-changed integral model over `R`. The proved p-power operator divisibilities also persist under further integral base change.

For every integral formal function `f` and every `n≥0`, these directions satisfy the stronger uniform affine estimates

\[
v_p(D_X^n f(0))\ge\max\{0,\lceil c_Xn-1\rceil\},
\qquad
v_p(D_Y^n f(0))\ge\max\{0,\lceil c_Yn-1\rceil\}. \tag{A1}
\]

Both slopes are optimal and both affine constants `1` are optimal. In particular DP30's order-p unit is compatible with positive asymptotic divisibility: it does not show that the dual has zero asymptotic gain.

The model also gives exact infinite derivative sequences:

\[
v_p(D_X^{q^r}X(0))=c_X(q^r-1),\qquad
v_p(D_Y^{q^r}Y(0))=c_Y(q^r-1),\qquad r\ge0. \tag{A2}
\]

The local mixed bound for an arbitrary integral function of the two dual coordinates follows by composing the integral divisibility operators:

\[
v_p(D_X^aD_Y^b f(0))
\ge \max\{0,\lceil c_Xa-1\rceil\}
   +\max\{0,\lceil c_Yb-1\rceil\}. \tag{A3}
\]

These are actual formal-group estimates. A normalized geometric Poincaré/theta kernel has not been identified with a function satisfying the required integral frame and period conditions. No lift saving or global cost follows merely from (A1)–(A3).

## 2. The integral model and its identification with the actual dual

### 2.1. A two-variable logarithm with a verified integrality theorem

Over `Q_p`, define

\[
\begin{aligned}
L_1(X,Y)&=\sum_{r\ge0}\frac{X^{q^r}}{p^{2r}}
             +\sum_{r\ge0}\frac{Y^{p^2q^r}}{p^{2r+1}},\\
L_2(X,Y)&=\sum_{r\ge0}\frac{Y^{q^r}}{p^{2r}}
             +\sum_{r\ge0}\frac{X^{pq^r}}{p^{2r+1}}.
\end{aligned} \tag{A4}
\]

Equivalently,

`L_1=X+p^(−1)L_2(X^(p²),Y^(p²))`,

`L_2=Y+p^(−1)L_1(X^p,Y^p)`.

Apply Hazewinkel's Functional Equation Lemma, Lemma 2.3 and formula (2.5), printed p. 74, with coefficient ring `B=Z_p`, fraction field `Q_p`, ideal `pZ_p`, endomorphism `sigma=id`, and the lemma's power parameter equal to `p`. Its only nonzero matrices are

\[
s_1=\begin{pmatrix}0&0\\1/p&0\end{pmatrix},
\qquad
s_2=\begin{pmatrix}0&1/p\\0&0\end{pmatrix}.
\]

The hypotheses (2.2) hold: `b^p≡b mod p` for `b∈Z_p`, and multiplying any matrix entry by `p` makes it integral. Equation (2.4) has integral remainder `(X,Y)` and the linear coefficient matrix is the identity. The lemma therefore proves that

\[
\mathcal H(\mathbf U,\mathbf V)
=L^{-1}\bigl(L(\mathbf U)+L(\mathbf V)\bigr)
\]

is an integral two-dimensional commutative formal group over `Z_p`.

### 2.2. Its p-series is finite free of rank p³

Let `M(X,Y)=(Y^(p²),X^p)`. Directly from (A4),

\[
pL(X,Y)-L(M(X,Y))=p(X,Y). \tag{A5}
\]

Since `L([p]_H)=pL`, Hazewinkel's congruence clause (2.8), printed p. 75, implies

\[
[p]_{\mathcal H}(X,Y)\equiv (Y^{p^2},X^p)\pmod p. \tag{A6}
\]

Here the congruence clause is applied to the already integral series `[p]_H` and the integral series `M`; it is not an unsupported inference from the rational logarithm.

For completeness, the finite-flat step can be proved directly. Map

`B=Z_p[[U,V]] → C=Z_p[[X,Y]]`

by sending `(U,V)` to `[p]_H(X,Y)`. Modulo `p`, this is `(U,V)↦(Y^(p²),X^p)`. The target is then free over the source with basis

`X^i Y^j`, `0≤i<p`, `0≤j<p²`.

Lift these `p³` basis monomials to `C`. They give a map `B^(p³)→C`. It is surjective by successively lifting a coefficient expression modulo `p`, dividing the remainder by `p`, and summing the resulting coefficients in the p-adically complete ring `B`. It is injective: any relation reduces to zero modulo `p`, hence all its coefficients are divisible by `p`; because `C` is p-torsion-free, division produces another relation. Repeating gives coefficients in every `p^nB`, hence zero. Thus `[p]_H` is finite free of rank `p³`.

Tate's formal-group/p-divisible-group construction, §2.2, therefore gives a height-three, dimension-two p-divisible group `H` over `Z_p`.

### 2.3. Cartier duality identifies the model without a display convention

Over `F_p`, (A6) and `M∘M=(X^q,Y^q)` give the identity of endomorphisms

\[
[p]_H^2=F_H^3. \tag{A7}
\]

Let `G=H^D`. Cartier duality sends Frobenius to Verschiebung, so

`V_G^3=[p]_G²`.

Since `F_GV_G=V_GF_G=[p]`, multiplying by `F_G³` gives

`[p]² F_G³=[p]³`.

Multiplication by `p²` can be cancelled in homomorphisms of p-divisible groups: if `u∘[p]²=0`, the fppf surjectivity of `[p]²` implies `u=0`. Hence

\[
F_G^3=[p]_G. \tag{A8}
\]

Every `G[p^n]` is consequently the kernel of `F_G^(3n)` on the special fibre, so it is connected. Connectedness of the finite groups over the complete local base follows from their connected special fibres. Tate §2.2 Proposition 1 supplies a formal group for all of `G`. Tate §2.3 Proposition 3 gives its dimension `3−2=1`; Cartier duality preserves height, so its height is three.

Choose an integral coordinate `T` for this one-dimensional group over `Z_p`. Equation (A8), which is over `F_p`, says exactly

\[
[p]_G(T)\equiv T^{p^3}\pmod p,
\qquad [p]_G(T)=pT+O(T^2). \tag{A9}
\]

After base change to `O=W(F_(p³))`, (A9) places this p-series in the Lubin–Tate class for uniformizer `p`. Hazewinkel §5, (5.1) and the following uniqueness/strict-isomorphism statements, printed p. 77, assert that the formal law commuting with such a series is unique and that all resulting laws for the same uniformizer are integrally strictly isomorphic. The Honda line with logarithm

`ell(T)=sum_(r≥0) T^(q^r)/p^r`

is one of those laws by (5.2)–(5.4). Therefore `G` is integrally strictly isomorphic to that Honda/Lubin–Tate line. Dualizing gives an integral isomorphism from the model `H` to its actual Cartier dual.

This argument identifies the model as an actual dual over the unramified cubic coefficient ring. It does not merely compare dimensions, slopes, or the first restricted p-operation. Coordinates and primitive invariant directions may be transported through this integral isomorphism. The same construction and inequalities persist after further base change.

## 3. Scaled inverse and the exact derivative sequences

Let

`a_X=p²+1`, `a_Y=p+1`,

and adjoin `pi` with `pi^(q−1)=p`. Set

\[
\widetilde L_1(x,y)=\pi^{-a_X}L_1(\pi^{a_X}x,\pi^{a_Y}y),
\qquad
\widetilde L_2(x,y)=\pi^{-a_Y}L_2(\pi^{a_X}x,\pi^{a_Y}y).
\]

The equalities

`p a_X−a_Y=q−1`, `p² a_Y−a_X=q−1`

make the first off-diagonal coefficients units. Every other nonlinear term has positive pi-valuation. For example the diagonal term at degree `q^r`, `r≥1`, has pi-exponent

`a_i(q^r−1)−2r(q−1)>0`,

because `(q^r−1)/(q−1)≥r` and each `a_i>2`. The higher off-diagonal terms have the same positivity after their initial zero exponent is removed. Thus the scaled logarithm is integral, with reduction

\[
\overline{\widetilde L}(x,y)=(x+y^{p^2},\ y+x^p). \tag{A10}
\]

Its formal inverse `widetilde E` is integral because its linear coefficient matrix is the identity. Over the residue field the displayed polynomial is additive, and its inverse is

\[
\begin{aligned}
\overline{\widetilde E}_1(u,v)
 &=\sum_{r\ge0}u^{q^r}-\sum_{r\ge0}v^{p^2q^r},\\
\overline{\widetilde E}_2(u,v)
 &=\sum_{r\ge0}v^{q^r}-\sum_{r\ge0}u^{pq^r}.
\end{aligned} \tag{A11}
\]

The signs are read in the residue characteristic, so this also covers `p=2`. Substitution into (A10) verifies the inverse by telescoping.

Write `E=L^(-1)`. In logarithmic coordinates `D_X=partial/partial u` and `D_Y=partial/partial v`. Therefore

`D_X^n f(0)=n! [u^n]f(E(u,0))`,

and similarly in the other direction. The `q^r` diagonal coefficients in (A11) are units, giving

\[
v_p([u^{q^r}]E_1(u,0))
=-\frac{a_X(q^r-1)}{q-1},
\quad
v_p([v^{q^r}]E_2(0,v))
=-\frac{a_Y(q^r-1)}{q-1}.
\]

Since `v_p((q^r)!)=(q^r−1)/(p−1)`, (A2) follows with

\[
\frac1{p-1}-\frac{a_X}{q-1}=c_X,
\qquad
\frac1{p-1}-\frac{a_Y}{q-1}=c_Y.
\]

The off-diagonal sequences are also exact:

\[
v_p(D_X^{p q^r}Y(0))
=\frac{p^2(q^r-1)}{q-1},
\qquad
v_p(D_Y^{p^2 q^r}X(0))
=\frac{p(q^{r+1}-1)}{q-1}. \tag{A12}
\]

In particular `D_X^pY(0)=−(p−1)!` is a unit. Its existence is compatible with (A2)'s positive slope `c_X`. The exact diagonal sequences prove that no larger asymptotic directional slope can hold uniformly for integral functions.

## 4. Integral translation operators improve the error to the optimal constant 1

All operator identities below hold on the **whole integral formal function ring**, not only after evaluation at zero. Work first over `Z_p` and then extend coefficients.

### 4.1. Low-degree identities

For `(a,b)∈N²`, let `Delta_(a,b)` be the coefficient of `S^aT^b` in translation of a function by the integral formal point `(S,T)`. It preserves the integral function ring. Commutativity of the formal group implies that all these translation-coefficient operators commute with one another and with the invariant derivations.

In characteristic zero, the translation operator is

\[
\exp\bigl(L_1(S,T)D_X+L_2(S,T)D_Y\bigr).
\]

Comparing the indicated coefficients in (A4) gives

\[
\Delta_{(p,0)}=\frac{D_X^p}{p!}+\frac{D_Y}{p},
\quad
\Delta_{(0,p^2)}=\frac{D_Y^{p^2}}{(p^2)!}+\frac{D_X}{p},
\quad
\Delta_{(0,p)}=\frac{D_Y^p}{p!}. \tag{A13}
\]

Consequently there are integral commuting operators `T,S` and units `a,b∈Z_p^×` such that

\[
D_X^p=aD_Y+pT,\qquad a=-(p-1)!, \tag{A14}
\]

\[
D_Y^{p^2}=p^p bD_X+p^{p+1}S,
\qquad b=-\frac{(p^2)!}{p^{p+1}}. \tag{A15}
\]

Also `D_Y^p` is divisible by `p` as an integral operator. Raising (A14) to `p` shows `D_X^(p²)` is divisible by `p`: its pure `D_Y^p` term is divisible by `p`, its mixed terms have factors `p^j binomial(p,j)`, and its final term has factor `p^p`. Therefore

\[
D_X^n(R[[X,Y]])\subseteq p^{\lfloor n/p^2\rfloor}R[[X,Y]],
\qquad
D_Y^n(R[[X,Y]])\subseteq p^{\lfloor n/p\rfloor}R[[X,Y]]. \tag{A16}
\]

### 4.2. q-order recurrences

Raise (A14) to `p²`. For `1≤j≤p²`, the jth nonleading binomial term is

`binomial(p²,j) a^(p²−j) p^j D_Y^(p²−j) T^j`.

By (A16), its p-divisibility is at least

\[
v_p\binom{p^2}{j}+j+\left\lfloor\frac{p^2-j}{p}\right\rfloor.
\]

This is at least `p+1`. At `j=p²` it equals `p²≥p+1`. For `1≤j<p²`, use `v_p binomial(p²,j)=2−v_p(j)`. If `j=ap+b` with `1≤b<p`, the expression is `p+1+a(p−1)+b`. If `j=ap` with `1≤a<p`, it is `p+1+a(p−1)`. These formulas include `p=2`.

The leading term uses (A15), giving a unit `u_X` and an integral operator `U_X` with

\[
D_X^q=p^p u_XD_X+p^{p+1}U_X. \tag{A17}
\]

Raise (A15) to `p`. Its leading term is `p^(p²)b^pD_X^p`, to which (A14) applies. For `1≤j<p`, every mixed term has valuation at least

`1+p(p−j)+(p+1)j=p²+j+1≥p²+2`;

the final term has valuation `p(p+1)≥p²+1`. Thus

\[
D_Y^q=p^{p^2}u_YD_Y+p^{p^2+1}U_Y, \tag{A18}
\]

with `u_Y` a unit and `U_Y` integral. These operator identities do not assert that the U-operators are derivations.

### 4.3. Induction for the affine estimates

For the X direction set `(r,B,c)=(p²,p,c_X)`, and for the Y direction set `(r,B,c)=(p,p²,c_Y)`. In either case

`c=B/(q−1)`, `cr=q/(q−1)`, and `c<1`.

For `0≤n<q`, the floor estimate (A16) implies

\[
v_p(D^n f)\ge\lfloor n/r\rfloor\ge cn-1. \tag{A19}
\]

Indeed the maximum of `cn−floor(n/r)` over these integers occurs at `n=q−1`, where its value is exactly `1`: within each block it increases with `n`, and its block maxima increase because `cr−1=1/(q−1)>0`.

For `n≥q`, use (A17) or (A18), in the common form

`D^q=p^B uD+p^(B+1)U`,

and apply it to `D^(n−q)f`. By induction, the first term has valuation at least

`B+c(n−q+1)−1=cn−1`.

The second has valuation at least

`B+1+c(n−q)−1=cn−1+(1−c)≥cn−1`.

Integrality and integer valuations yield (A1). Because every argument was an operator divisibility on the entire integral ring, composing the two estimates proves (A3).

### 4.4. The constant cannot be improved

Set `n=q−1` and take the single integral monomial

\[
f(X,Y)=X^{p-1}Y^{p^2-1}. \tag{A20}
\]

Along the X logarithmic axis, (A4) gives

`E_1(t,0)=t+terms of higher degree`,

`E_2(t,0)=−t^p/p+terms of higher degree`.

The lowest degree of `f(E(t,0))` is `(p−1)+p(p²−1)=q−1`; its coefficient is exactly `(-1/p)^(p²−1)`. There is no other contribution at that lowest degree. Legendre's formula gives

\[
v_p((q-1)!)=p^2+p-2,
\qquad
v_p(D_X^{q-1}f(0))=p-1=c_X(q-1)-1. \tag{A21}
\]

Along the Y logarithmic axis the leading terms are `E_1(0,t)=−t^(p²)/p+…`, `E_2(0,t)=t+…`. The same monomial again has lowest degree `p²(p−1)+(p²−1)=q−1`, now with coefficient `(-1/p)^(p−1)`. Hence

\[
v_p(D_Y^{q-1}f(0))=p^2-1=c_Y(q-1)-1. \tag{A22}
\]

Thus the affine constant `1` is attained for each direction. This is an exact witness, not a claim that every derivative order attains its lower bound.

## 5. What this settles about a kernel, and the precise remaining datum

The original height-three line has slope

`c_3=p(p+1)/(p³−1)=c_X+c_Y`.

For the actual product of the line with its dual, the three coordinate directions therefore have positive slopes `c_3,c_X,c_Y`. If a particular normalized theta or biextension expression is proved to be an integral formal function in this product's chosen integral frame, the line estimate and (A3) give a genuine multivariate derivative bound for that expression. Thus there is no remaining uncertainty about the existence of an actual dual formal group or about these primitive directional operator bounds.

The first unsupplied local geometric datum is now more precise: an explicit integral trivialization and period normalization for the required Poincaré/theta kernel, with its derivative expression identified in these coordinates and with any nonintegral gauge or exponential factors controlled. The canonical Poincaré biextension exists, but its existence alone does not select that scalar kernel or establish its integral connection/jet formula. The general source on display biextensions identifies the construction, not the missing normalized scalar function in this calculation.

For a hypothetical cost that weights all three actual dimensions equally, the average of these directional slopes is

`2c_3/3<c_2`.

Indeed `c_3/c_2=(p+1)²/(p²+p+1)` and `2(p+1)²<3(p²+p+1)` is `0<p²−p+1`. This is only a comparison under that specified cost model. It is not a theorem about the actual theta-lift budget, whose entries, weights and geometric endpoint data require separate identification.

## 6. Sources and actual check records

Primary source 1: M. Hazewinkel, *On formal groups. The functional equation lemma and some of its applications*, Astérisque **63** (1979), 73–82. Exact locators: Lemma 2.3, (2.2)–(2.5), p. 74; congruence statement (2.8), p. 75; Lubin–Tate uniqueness, strict isomorphism and (5.1)–(5.4), p. 77. URL: `https://www.numdam.org/item/AST_1979__63__73_0.pdf`. Local PDF SHA-256: `148cf0c8fb88c38e00eb31b10e4e596c375c978c24f3b8db77defa3ac0451061`.

Primary source 2: J. Tate, *p-Divisible Groups* (1967), §1.2–1.4, pp. 159–160; §2.2, Proposition 1 and diagram (3), pp. 162–164; §2.3, Proposition 3 and its proof, p. 166. These support the formal/BT correspondence, connected components, exact Cartier duality, F/V duality and dimensions. The finite-free proof and p-cancellation are supplied above. Local PDF SHA-256: `720bf7128d4f048853435b083d18d0d863056c1f991942192a7f00daa7e424aa`.

All events below are by `/root/step2_higher`, **GPT-6 Astra Pro**, runtime effort not exposed, on **2026-11-21 UTC**. A report of another agent's check is explicitly attributed, never presented as an additional self-check.

| Event | Type | Actual work | Result |
|---|---|---|---|
| ADH3-S-001 | Primary source | Downloaded Hazewinkel's official PDF, extracted pp. 74–77 and visually inspected p. 74, p. 75 and p. 77 | Exact integrality, congruence and Lubin–Tate identification clauses confirmed |
| ADH3-S-002 | Primary source | Read and visually inspected the Tate pages listed above during DP30, including p. 160 exactness and p. 166 duality proof | The same already-checked facts support §2; no new Dieudonné/display convention is asserted |
| ADH3-P-001 | Construction | Derived (A5)–(A9), gave the explicit p-adic lift proof of finite freeness, and checked cancellation and connectedness before applying Lubin–Tate uniqueness | Actual dual identification established under the stated coefficient base |
| ADH3-P-002 | Scaling and exact coefficients | Solved the two weight equations, checked every family of scaled coefficients, verified the inverse (A11), and derived the exact diagonal/off-diagonal valuations | Positive unequal slopes and exact infinite sequences |
| ADH3-P-003 | Operator proof | Derived (A13) coefficient by coefficient, tracked integrality/commutation, split every binomial valuation case including p=2, and proved the q-order recurrences and induction | Uniform affine error 1 for each direction |
| ADH3-P-004 | Sharpness/scope | Checked the two lowest-degree substitutions of the same monomial, factorial valuations, and the distinction between integral formal functions and an unidentified normalized Poincaré/theta kernel | Constants and slopes sharp; no global kernel or lift-count implication asserted |
| ADH3-P-005 | Whole-saved-draft reread | Reread the entire saved statement and §§2–5, including every equation (A1)–(A22), the full finite-free argument, the exact Lubin–Tate scope, all binomial cases, and both witnesses | Passed; made the coefficient ring `R` explicit in §1 |
| ADH3-I-001 | Reported independent whole-proof review | `/root/formal_bound` read and independently challenged every statement (A1)–(A22), including finite freeness, duality/cancellation, LT identification, all scaling families, off-diagonal sequences, translation identities, both binomial cases, p=2, induction and both constant witnesses | Reported PASS with no mathematical correction; their separate review records the checked math-block hash and observed UTC time |

No finite diagnostic computation is used as a substitute for these proofs, and no Lean execution is claimed.
