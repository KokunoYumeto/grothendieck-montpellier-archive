# DP67 — one unramified CM host for the endpoint and full-row theta witnesses

Author: `/root/step2_higher`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Reasoning effort is not exposed. This combines the actual field and product of DP57 with the actual embedding-labelled harmonic construction of DP65. The key new point is a complete calculation in the genuine `Q(ζ_28)` eigencoordinates, not an assumption that its height-six factors split into one-dimensional `Q(ζ_28)` formal groups.

## 1. Statement

Let

\[
E'=\mathbf Q(\zeta_{28})=\mathbf Q(\zeta_7,i),\qquad
F'=(E')^+=\mathbf Q(\zeta_7)^+(\sqrt7),
\]

and give `A=J²` the integral action of DP57: `ζ_7` acts diagonally, while

\[
I=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\tag{CH1}
\]

acts as `i`. Use the product principal polarization and the product trace-one line. Write `ξ=ζ_7² i^(-1)`; then `ξ^4=ζ_7` and `ξ^7=i`. Its actual CM type is

\[
\Phi'=\{1,3,9,15,17,23\}\subset(\mathbf Z/28)^\times.
\tag{CH2}
\]

Work at11 over an unramified ring containing both the coefficients of DP49 and `i`, for example after `W(F_(11^6))` and the further finite unramified extensions needed for the allowed translates.

**DP67(a).** There are primitive integral tangent eigenvectors of actual E'-characters3 and9, both in `Φ'`, whose additive parameters `S,T` restrict the two copies' DP49 line/first-dual parameters as

\[
(x_1,x_2)=(S,iS),\qquad (y_{1,1},y_{1,2})=(T,-iT),
\quad y_{2,1}=y_{2,2}=0.
\tag{CH3}
\]

For the actual product primitive normalized kernel, every unit exponent `lambda` gives the exact mixed-derivative valuations

\[
v_{11}\!\left(\partial_S^{11^r}\partial_T^{121\,11^r}
 \exp\bigl(\lambda(\beta_1+\beta_2)\bigr)\big|_0\right)
=\frac{11^r-1}{10}\qquad(r\ge0),
\tag{CH4}
\]

where the logarithm is restricted by (CH3).

**DP67(b).** Fix the rank data and a nonfinal stage of DP65. Put `P=k+j−1`, `Q=m−j`, `n_V=P+Q+t`, and let `A*,B*` be the fixed residual partitions in (EH12–13). On

\[
C'=A^P\times\overline A^{\,Q},
\tag{CH5}
\]

where the bar means the conjugated E'-action, there is an actual E'-embedding-labelled generalized harmonic polynomial with all rows filled and source HC equations, with growing first positive degrees `11^r` at character3 and `121·11^r` at character9. Every other positive and negative row has fixed residual degree. Set

\[
D'=6(|A^*|+|B^*|),\quad
\mathcal F'=\left(\prod_i A_i^*!\prod_s B_s^*!\right)^6,
\quad T_r=122\,11^r+D'.
\tag{CH6}
\]

Its integral-prefactor normalized theta evaluation has valuation exactly

\[
V_r=\frac{11^r-1}{10}+v_{11}(\mathcal F').
\tag{CH7}
\]

Some actual generic allowed-translate tuple has valuation at most `V_r`, including `M^(-T_r)`, with `M=29^e=O(T_r)` and `κ=M²=O(T_r²)`. Therefore no uniform lower bound `γT_r-C_0`, for fixed `γ>1/1220,C_0`, holds for all these evaluations in this varying-HC family.

**DP67(c).** This construction uses the same actual field `E'`, trace-one element, and principal polarization data as DP57. Thus the source's generic `CMData`/relative-unramified-field and toroidal `Host` inputs, and the separately constructed generic adelic endpoint over `E'`, are available over the same field as these actual full-row geometric witnesses. It does not identify their theta image with that endpoint or assert equality of separately chosen level records. The type remains `Φ'`, not the old quadratic-induced type. No old `Datum.dom`/`CMObj.HasType`, complete `SizeData₂` comparison, or global multiplicity conclusion is inferred.

## 2. Actual eigencoordinates and their integral change of basis

DP49 identifies the original tangent characters `x:3,y_1:2,y_2:1` under the `ζ_7` action. On the two copies of `J`, the differential of (CH1) is exactly the same rotation matrix in each of these three coordinate pairs. It has eigenvectors

\[
v_-=(1,i)\quad\text{with eigenvalue }-i,
\qquad v_+=(1,-i)\quad\text{with eigenvalue }i.
\tag{CH8}
\]

The determinant of the two-column eigenvector matrix is `−2i`, a unit at11. It therefore gives a genuine integral change of tangent basis, not a division by11 or a mere rational decomposition.

For the line pair, choose `v_-`; its `ζ_7` character is3 and its `i` character is `−i`. The unique exponent modulo28 satisfying `a≡3 mod7` and `a≡3 mod4` is3. For the first dual pair choose `v_+`; its `ζ_7` character is2 and its `i` character is `i`. The unique exponent satisfying `a≡2 mod7`, `a≡1 mod4` is9. This proves the character labels in (a). Their conjugates are25 and19, neither in `Φ'`.

Normalized logarithms intertwine every formal-group homomorphism with its differential in characteristic zero. To verify this here directly, composition of a normalized logarithm with a homomorphism is an additive formal map after the exponential change; an additive formal map over a characteristic-zero field has no terms of degree at least two, since substitution of scalar integer multiples forces every such coefficient to vanish. Its linear term is the differential. Hence the rotation acts exactly linearly on the additive parameters. Setting the other eigenparameters to zero gives precisely (CH3).

One can also choose integral algebraic formal coordinates with this same tangent basis: apply the inverse unit matrix to the original integral coordinates. Their relation to the additive parameters has identity linear term, with higher ordinary degree terms; it need not be an integral logarithm. That is exactly the input needed for the later integral monomial filler. If literal eigenfunctions are desired, average coordinates using the order28 projectors; since28 is a unit at11 and the tangent characters are distinct, the resulting coordinate system is integral and retains its unit Jacobian. Neither construction claims that these eigendirections integrate to one-dimensional E'-stable formal summands.

## 3. Entire critical initial form after the change of eigencoordinates

Choose the two copies' integral frames and normalizations identically. The normalized product kernel is the product of the two identical single-copy primitive kernels, so its logarithm is `β_1+β_2` exactly. This is the external-product trace-one line; any integral unit frame factors are handled by the prefactor interpolation exactly as in DP59. Fix this product compatible normalization, without adding an arbitrary rational quadratic gauge.

Let

\[
s=1/10,\qquad w=121/1220,
\]

and, in a finite ramified extension used only for coefficient analysis, choose `gamma,mu` with `v(gamma)=w`, `v(mu)=s`. DP58's full two-variable initial-form theorem (ES11–12), with DP46's actual arbitrary-unit calculation, says for a single copy

\[
\mu^{-1}\lambda\beta(\gamma X,e_1\gamma Y)
\in\mathcal O[[X,Y]],\qquad
\overline{\mu^{-1}\lambda\beta(\gamma X,e_1\gamma Y)}
=c_\lambda XY^{121},\quad c_\lambda\ne0.
\tag{CH9}
\]

This is an assertion about every coefficient at the least valuation, not only a first ordinary degree term. It applies with exactly the same `c_lambda` to both identical copies. Multiplying the input variables by `i` or `−i` is an integral unit substitution and therefore preserves the assertion and commutes with reduction.

By (CH3), the scaled logarithm restricted to the actual chosen E'-eigenparameters has reduction

\[
 c_\lambda ST^{121}
 +c_\lambda(iS)(-iT)^{121}
 =2c_\lambda ST^{121},
\tag{CH10}
\]

because `121≡1 mod4`. The coefficient2 is a unit at11. Thus there is no cancellation of the unique entire initial monomial. Every coefficient of the scaled logarithm remains at least `s` in valuation, and its complete normalized reduction is exactly the one nonzero monomial (CH10).

This computation does not infer the initial form from a diagonal one-variable restriction. It substitutes actual linear eigencoordinates into the already proved entire two-variable initial form, so no unexamined lower-weight term or other monomial can enter at valuation `s`.

Apply the critical-exponential lemma proved in DP58 to this logarithm. It gives nonzero coefficients at every monomial

\[
S^{11^r}T^{121\,11^r}
\]

in the reduction of `mu^(-1)(exp(logarithm)−1)`. Consequently their original coefficients have exact valuation

\[
s-w(122\,11^r).
\tag{CH11}
\]

Both exponents are powers of11. Multiplying by their factorials contributes `s(122·11^r−2)`, so the derivative valuation is `(s−w)122·11^r−s=(11^r−1)/10`. This proves (CH4). The ramified extension used for the coefficient comparison changes no normalized valuation of an original coefficient. The geometric section and the derivative evaluation lie over the original unramified coefficient ring (extended unramifiedly for `i` and torsion); no ramified change of the integral lattice is made.

## 4. Genuine E'-labelled HC rows and harmonicity

The integral action and principal polarization of `A=J²`, including its full ring of integers and type (CH2), are established in DP57. Conjugating that action gives type `−Φ'` with the same underlying abelian scheme and polarization. Thus (CH5) has multiplicities `P` at each of the six embeddings of `Φ'` and `Q` at each conjugate embedding.

For every representative `a∈Φ'`, use the HC construction (EH10–11), with all `beta,epsilon` fixed. Set

\[
\eta_3=11^r,\qquad\eta_9=121\,11^r,
\qquad\eta_a=0\quad(a\in\Phi'\setminus\{3,9\}).
\tag{CH12}
\]

The source HC inequalities, integer/half-integer fields, and common-row word equations are proved exactly as in DP65, separately at each of these six embeddings. Their selected residual partitions are the same `A*,B*`; no change of the old quadratic `Fields.Tau` package is silently asserted.

In the first ordinary `A` factor of the first column take the monomial in the actual eigenparameters of (CH3), of exponents in (CH12). Its characters3 and9 both lie in `Φ'`, so every conjugate-pair contraction annihilates it. Fill all twelve embedding blocks by the prefix determinant products of DP65, using common disjoint positive and negative filler column sets of sizes `P,Q`, disjoint from the first column. This needs only `P+Q+1≤n_V` columns.

Exactly the row-invariance, telescoping degree, disjoint-column contraction, and coefficient-one diagonal-monomial proofs of DP65 apply to these six pairs. The actual generalized harmonic polynomial has all rows prescribed and is primitive. The integral algebraic-coordinate diagonal prefactor has fixed degree `D'`; applying the filler part of the operator gives exactly `F'`. The first-column mixed derivative has value (CH4), with unit parameter `lambda=−κ`. This proves (CH7).

The local E'-factors at11 have height six and dimensions two and four, as DP57 proves. The eigencoordinate computation above uses the underlying actual product of two height-three line/dual pairs. It does not apply a hypothetical one-dimensional height-six theorem to a tangent line of one of those higher-dimensional E'-factors.

## 5. Allowed translates, field compatibility, and the remaining interface

The element `alpha=(1+2delta)^e` from DP59 lies in the original subfield E and hence in E'. It acts diagonally on the two copies of `J` in each ordinary `A` factor. On a conjugate-action factor it acts as `bar alpha` on both copies. In E' one still has

\[
\alpha\bar\alpha=M=29^e,\qquad
(\alpha)+(\bar\alpha)=\mathcal O_{E'},
\]

because the original Bezout identity remains valid after extending scalars. It is generated from the same trace-one quadratic subring, so the exact arithmetic `Level.fromK`, norm and coprimality conditions used in DP59 persist.

The allowed translates on all underlying `J` factors therefore give a finite integral generating family for the product span on `C'`, with roots killed by the actual ideal `(alpha²)`. Products of symmetric lifts, multiplication isomorphisms and rigidifications satisfy the generic source `IsVtOver` relation. DP59 on each fixed factor, with `alpha` and `bar alpha` exchanged where needed, gives total-order jet surjectivity at a linear threshold `M≥cT+d`. A product monomial factors among the fixed number of factors, so the factorwise jet proof from DP63 applies without asserting any unnecessary identification of the full section space.

Choose the least power29 meeting this threshold for `T=T_r`. Realize the normalized first-column kernel and the fixed diagonal filler jets, including the inverse integral frame units. The resulting interpolating-section tuple has value (CH7). Its finite integral expansion in the allowed generating tuples shows that some actual tuple has valuation at most (CH7). The factor `M^(-T_r)` is a unit. Algebraicity and finite unramified completions of the extracted translates are precisely as in DP59. This proves the asserted polynomial levels and rate.

Finally DP57 supplies `O_E'/O_F'` finite étale, the literal generic source `CMData`, the toroidal field-level `Host` with the same trace-one `w_0`, and the independent generic adelic endpoint construction at its explicit auxiliary principal level. The present actual geometric object uses that same field and integral action, and the same field-level Host data can be reused. The separate source `Datum.dom` still selects an imaginary-quadratic induced type, whereas `Φ'` is not induced from any such subfield. No point in that old moduli space, equality of independently chosen levels, map into a prescribed automorphic theta image, or analytic cost package is inferred from sharing the field. This is the exact limit of the unification claim.

## 6. Check and source record

No new outside theorem is used beyond the checked DP57 field/action construction, DP49 actual unit-arrow character data, DP58 entire initial-form/exponential lemma, DP59 allowed-translate theorem, and DP61/DP65 row algebra. Dependency hashes and complete saved-version mathematical rereads are recorded separately. No Lean execution or machine formalization is asserted.
