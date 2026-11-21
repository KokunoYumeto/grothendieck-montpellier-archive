# DP65 — actual CM-embedding-labelled full-row witnesses

Author: `/root/step2_higher`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Reasoning effort is not exposed. This result removes DP63's abstract-row-label limitation. It uses the actual CM embedding labels of an explicit polarized product and the source harmonic/row equations with the CM type `Φ={1,2,3}`. That type is not induced from the old imaginary quadratic subfield; no old `Datum.dom`/`CMObj.HasType` or replacement theta correspondence is asserted.

## 1. Statement and precise generalized harmonic module

Let `E=Q(ζ_7)` and let `(J,ι,λ)` be the actual principally polarized Jacobian of DP49. Label the embeddings by `τ_a(ζ_7)=ζ_7^a`, for `a=1,…,6`, with conjugation `a↦7−a`. Put `Φ={1,2,3}`. The conjugate-action object `barJ` is the same underlying abelian variety and polarization with E-action `barι(u)=ι(bar u)`. Thus its tangent characters are `{4,5,6}`.

Fix source rank data `k,m,t` and a stage `1≤j<m`, and put

\[
P=k+j-1,\quad Q=m-j,\quad n_V=P+Q+t,\quad
H=(t+3)/2,\quad d=t+2.
\tag{EH1}
\]

Consider the actual polarized E-abelian variety

\[
C=J^P\times\overline J^{\,Q}.
\tag{EH2}
\]

Its tangent multiplicities are `P` at each embedding in `Φ` and `Q` at each conjugate embedding. For `n_V` columns use variables `Z_(a,i,c)` indexed by these actual embeddings, their actual multiplicity rows, and the columns. Define the generalized harmonic module by exactly the source `RowDeg.lean` equations:

\[
\Delta_{a,i,s}=\sum_c
\partial_{Z_{a,i,c}}\partial_{Z_{7-a,s,c}}
\quad(a\in\Phi),
\tag{EH3}
\]

together with invariance under adding an earlier row to a later row at each fixed embedding, prescribed row degrees in each supported monomial, and integral coefficients. The only changed type predicate is `a∈Φ`, in place of the old `InPsi` defined from an imaginary quadratic root. Here the variables are actual CM eigenvectors, not arbitrary labels assigned across different characters.

**DP65.** There are fixed nonnegative antitone partitions `A*` of length `P`, `B*` of length `Q`, with every entry positive, and fixed constants

\[
D_0=3(|A^*|+|B^*|),\qquad
\mathcal F_0=\left(\prod_iA_i^*!\prod_sB_s^*!\right)^3,
\tag{EH4}
\]

such that the following holds for every integer `r≥0`. Let

\[
a_r=11^r,\qquad b_r=121\,11^r,
\qquad T_r=122\,11^r+D_0.
\tag{EH5}
\]

There are embedding-by-embedding source HC parameters whose selected partitions are

\[
A^{(3)}=A^*+a_re_0,\quad A^{(2)}=A^*+b_re_0,
\quad A^{(1)}=A^*,\qquad B^{(a)}=B^*\ (a\in\Phi).
\tag{EH6}
\]

All row data are word-independent, so the source's `Wts.Ok` row-compatibility equations hold. There is a primitive integral polynomial in the full actual embedding-labelled harmonic component (EH3) with these partitions, and a normalized integral-prefactor theta jet on `C^(n_V)` whose selected evaluation has valuation exactly

\[
V_r=(11^r-1)/10+v_{11}(\mathcal F_0).
\tag{EH7}
\]

There also exists an actual tuple of the generic permitted translates of the product trace-one theta section, with `M=29^e=O(T_r)` and `κ=M²=O(T_r²)`, whose same normalized evaluation has valuation at most `V_r`. The factor `M^(-T_r)` is included. In particular a uniform lower bound `γT_r-C_0` with `γ>1/1220` and constant `C_0` cannot hold for all these full-row evaluations as this HC family varies.

The geometric dimension `3(P+Q)`, the number of columns `n_V`, the residual partitions, and the factorial cost are fixed in this family. No full `SizeData₂` scaling, prescribed theta-image membership, or global multiplicity/lift conclusion is included.

## 2. Actual E-action, polarization, and character labels

The original `J` has tangent characters `1,2,3`; this is proved in DP22 and recorded in DP49. Twisting its E-action by conjugation changes them to `6,5,4`, with no change to the underlying abelian scheme or its good reduction. The product therefore has exactly the multiplicities asserted in (EH2).

The product polarization still has Rosati conjugation on E: on a twisted factor, the adjoint of `ι(bar u)` is `ι(u)=barι(bar u)`. It is principal. The trace-one element `w_0` acts as `ι(w_0)` on each ordinary factor and `ι(bar w_0)` on each twisted factor; both are integral and satisfy `w_0+w_0^dagger=1`. Their trace-one lines are integrally isomorphic. Indeed adjunction and symmetry of the normalized Poincaré biextension give

\[
(1,\bar w_0)^*\mathcal P_\lambda
\simeq(w_0,1)^*\mathcal P_\lambda
\simeq(1,w_0)^*\mathcal P_\lambda,
\tag{EH8}
\]

with the rigidifications respected. Thus the product trace-one line is ample and principal, and a primitive base section is the external product of the sections used in DP59.

At11, DP49 equation (JT7) gives the actual tangent directions

\[
x:\tau_3,\qquad y_1:\tau_2,\qquad y_2:\tau_1.
\tag{EH9}
\]

Use the first ordinary `J` factor (row0) in column1 for `x,y_1`. Both are positive-type directions, but belong to distinct, nonconjugate embeddings. In particular `τ_3` and `τ_2` are not a pair appearing in any contraction (EH3). On every factor choose primitive integral eigenbases. The order7 eigenspace projectors are integral at11, and the eigenvalues are distinct after the fixed unramified splitting extension, so these are actual integral direct summands. Rescaling any such basis vector by a unit does not change the valuations below: row degree is fixed in each supported monomial, and the sharp mixed coefficient is multiplied by a unit power.

## 3. HC data with only two positive first degrees growing

For each `a∈Φ`, assign a nonnegative integer `η_a`, and set

\[
v_i^{(a)}=k-2-i\quad(1\le i\le k-2),\qquad
v_0^{(a)}=k-2+\eta_a,
\]
\[
u_i^{(a)}=v_i^{(a)}+1/2\quad(0\le i\le k-2),
\qquad u_{k-1}^{(a)}=-1/2,
\tag{EH10}
\]

and keep every source `b,e` entry fixed:

\[
\beta_s=1+2Hs,\qquad \epsilon_s=\beta_s+H
\quad(0\le s<m).
\tag{EH11}
\]

All HC fields hold by direct inspection. Consecutive `v` gaps are one except for the first gap `η_a+1`; the half-integer `u` lies strictly between the neighboring integers. At the last index `0>−1/2>−1=−β_0`. Both HC gap inequalities are equalities `H`, and all integrality fields hold. This is the same exact source `HCParam` of `Params.lean:50–69`, independently at each embedding.

Put `c_j=1+d(j−1)`. Substitution in DP61's formulas gives the fixed positive residual partition

\[
A_i^*=\begin{cases}
c_j&0\le i<k-1,\\
1+d(P-1-i)&k-1\le i<P,
\end{cases}
\tag{EH12}
\]

and the fixed reversed negative partition

\[
B_s^*=1+d(Q-1-s)\quad(0\le s<Q).
\tag{EH13}
\]

The selected positive partition at embedding `a` is `A*+η_a e_0`; the conjugate negative partition is `B*`. The first `k` entries of `A*` are `c_j`, and then the remaining entries decrease by `d` to1, so it is antitone. `B*` is also antitone with last entry1. Setting `η_3=a_r,η_2=b_r,η_1=0` proves (EH6).

Taking the same HC data for all words checks the source common-row, first-u and last-u equations exactly. Here the representative set is the actual type `Φ`; it is not asserted to be the old quadratic `Fields.Tau` package. The claim is the same HC and word-compatibility equations on this explicitly changed type.

## 4. A genuine embedding-labelled full harmonic polynomial

Reserve column1 for the monomial

\[
P_r^0=Z_{3,0,1}^{a_r}Z_{2,0,1}^{b_r}.
\tag{EH14}
\]

This monomial is killed by every contraction (EH3), because it contains no variable at any conjugate embedding `4,5,6`. It is invariant under later-row additions because it uses only row0 at its two embeddings.

Choose disjoint further column sets `C_+` of size `P` and `C_-` of size `Q`; they fit because `n_V≥P+Q+1`. For each `a∈Φ`, form the prefix-minor determinant polynomial of DP61 with partition `A*` on the rows of embedding `a` and columns `C_+`, and the corresponding polynomial with partition `B*` on embedding `7−a` and columns `C_-`. Put

\[
Q_0=\prod_{a\in\Phi}\mathcal D_{A^*}(Z_a;C_+)
                  \mathcal D_{B^*}(Z_{7-a};C_-),
\qquad P_r=P_r^0Q_0.
\tag{EH15}
\]

Prefix-minor row invariance and telescoping row degrees prove the exact partitions (EH6). On `C_+` every conjugate negative variable is absent; on `C_-` every positive variable is absent; on column1 only the positive variables in (EH14) occur. Thus every contraction vanishes, including every cross term of the product rule. The column assignments may be reused across all three embedding pairs because each contraction pairs only an embedding with its own conjugate. All coefficients are integral. The product of the determinant diagonal terms and (EH14) has coefficient one, so `P_r` is primitive and nonzero. It belongs to the actual embedding-labelled generalized `HaO` component just defined.

Its total degree is `T_r`, and the filler degree is `D_0`. The filler has a diagonal monomial with coefficient one and exponents `A_i*` at each of the three positive embeddings and `B_s*` at each negative embedding. Choose the matching monomial in integral algebraic coordinates on the filler columns. Its leading additive-coordinate form is that monomial. Exactly as in DP63, applying `Q_0(∂)` to this prefactor times all the filler kernels yields exactly `F_0`. Higher-degree terms cannot contribute. This is an actual integral formal prefactor of fixed degree `D_0` on the full product `C^(n_V)`.

## 5. Exact sharp value of the first-column mixed monomial

Let `F_lambda(x,y)=exp(lambda beta(x,e_1 y))` be the actual arbitrary-unit primitive kernel in the first ordinary `J` factor, in the normalization fixed in DP59. The entire critical initial form in DP58, equations (ES11–12), gives

\[
v_{11}([x^{a_r}y^{b_r}]F_\lambda)
=s-w(a_r+b_r),\qquad
s=1/10,\quad w=121/1220,
\tag{EH16}
\]

for every unit `lambda`, since the selected monomial has nonzero residue in (ES12). There is no harmonic diagonal correction here. Both `a_r` and `b_r` are powers of11, so Legendre's formula yields

\[
v_{11}(a_r!b_r!)=s(a_r+b_r-2).
\]

Therefore

\[
v_{11}\bigl(\partial_x^{a_r}\partial_y^{b_r}F_\lambda(0)\bigr)
=(s-w)(a_r+b_r)-s
=(11^r-1)/10.
\tag{EH17}
\]

The actual trace-one normalization uses a unit parameter `lambda=−κ`, with any fixed unit conventions absorbed, because `κ=M²` is prime to11. Unit rescalings of `x,y` multiply this derivative by unit powers and leave (EH17) unchanged. Unused factors in the first column contribute their normalized value1. Multiplying by the exact filler evaluation gives (EH7).

## 6. Actual permitted translates and polynomially bounded levels

On an ordinary `J` factor use the DP59 level `alpha=(1+2delta)^e`, `M=29^e`. On a conjugate-action factor, the same E-element acts by `bar alpha` on the underlying `J`. The DP59 proof is symmetric under exchanging `alpha` and `bar alpha`: their norm is `M`, their ideals are coprime, their isogenies are prime to11, and the product-line isomorphisms are (EH8). Consequently the allowed span on this factor is `[bar alpha]^*H^0(J,L^M)`, with an integral allowed-translate basis and the same linear jet-surjectivity bound. Its roots are killed by `(bar alpha²)`, precisely the physical action of the same ideal `(alpha²)` on the conjugate E-object.

Take the product span of these modules over the `P+Q` factors of `C`; tensor products of the factor basis sections form a finite integral generating family of that span. No claim about an identification with the entire product section space is required. The allowed roots then lie in `C[alpha²]`, with `alpha` understood as its actual E-action. The tensor-product symmetric lifts and multiplication isomorphisms satisfy the generic source `IsVtOver` conditions, as in DP63. Products of factor jets realize every integral jet of a given total order, so for fixed `C` there are constants `c,d` such that `M≥cT+d` suffices. This uses only a fixed number of factors.

For `T=T_r`, prescribe the algebraic prefactor jets giving the pure first-column kernel and the diagonal filler monomials in all other columns, including the inverse integral unit frame factors from DP59. Choose realizing sections in the allowed spans. The resulting normalized selected evaluation has valuation exactly (EH7). Expand all `n_V` sections in these finite integral allowed-translate generating families. Multilinearity and the ultrametric inequality imply that at least one actual allowed-translate tuple has valuation at most (EH7). The normalization `M^(-T_r)` is a unit and has no valuation cost. The least sufficient power29 gives `M=O(T_r)` and `κ=O(T_r²)`.

As in DP59, the generating translates and their lifts are algebraic over finite extensions, integral after finite unramified extension at11. The interpolation coefficients may be complete-local, but the extracted witness is a tuple of those algebraic generating translates. No coefficient-height bound for the interpolation expansion is needed for this local existence conclusion, and none is asserted.

Finally `V_r/T_r→1/1220`, proving the stated exclusion of a larger uniform local rate. The parameters `P,Q,n_V` and the product variety are fixed; the positive first row gaps and the overall theta level vary.

## 7. Exact scope of the improvement

Unlike DP63, the variables and row multiplicities now agree with the actual CM eigenspaces on the geometric product. All embedding rows, including every negative row, are filled, and the full polynomial is harmonic for every actual conjugate-pair contraction in the generalized module. The exponent ratio is realized in two different positive embeddings rather than by relabelling one direction as a negative conjugate row.

The type predicate is still `Φ123`, so DP25/DP52/DP57's old quadratic-induced-type obstruction has not disappeared. This result constructs the generalized local algebraic/section interface, not its identification with the old moduli space or with a new automorphic theta image. The growing first row gaps require growing source windows; no full `SizeData₂` construction or net global cost comparison is supplied. The finding therefore narrows the remaining lift question without asserting that every shorter-chain proposal is impossible.

## 8. Sources and genuine check events

The exact source harmonic equations and HC/Wts records were read and hashed in DP61; their replacement of the type predicate is stated explicitly above. The actual character table is DP49 (JT7) with its proof in §3, and the sharp coefficient input is DP58 (ES11–12). The integral allowed-translate theorem and its complete proof are DP59. Current dependency hashes and complete saved-version check events are recorded separately. No Lean execution or machine formalization is claimed.
