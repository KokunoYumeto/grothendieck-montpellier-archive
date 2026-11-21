# DP61 — prescribed row degrees, fixed windows, and a harmonic completion

Author: `/root/step2_higher`, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Reasoning effort is not exposed. This is a source-interface classification and an elementary polynomial proof. It does not run Lean, audit Alpoge's accepted theorems, or instantiate the old CM-object interface with the new mixed type.

## 1. Exact source interface

Write the source rank parameters as `k,m,t`, and fix a nonfinal stage `1 ≤ j < m`. Put

\[
P=k+j-1,\qquad Q=m-j,\qquad r_0=P+Q=k+m-1,
\qquad n_V=r_0+t.
\tag{RG1}
\]

Here `n_V`, not the growing endpoint rank `N(j)`, is the number of columns in the selected harmonic polynomial. The source requires even `k,m`, odd `t`, `m≥2`, `k≥m+3`, and `t≥r_0+5`; in particular `P≥5` and `n_V≥P+Q+2`. Exact definitions: `Formalism/LocalRingCardinality/Params.lean:6–22,32–46`.

At one embedding, let `u,v,b,e` denote the `HCParam` data. All `v,b,e` are integers and the `u` are half-integers. The inequalities are

\[
u_i>v_i>u_{i+1},\quad u_{k-1}>-b_0,\quad
 e_s-b_s\ge H,\quad b_{s+1}-e_s\ge H,
\qquad H=(t+3)/2.
\tag{RG2}
\]

These are exactly `Params.lean:50–69`. For zero-based indices define

\[
\sigma_i=\begin{cases}v_i&i<k-1,\\-b_{i-(k-1)}&i\ge k-1,\end{cases}
\quad
A_i=\sigma_i+e_{j-1}-(P-1-i)-(t+1)/2,
\tag{RG3}
\]

and

\[
C_c=b_{j+c}-e_{j-1}-(t+1)/2-c,\qquad
B_n=C_{Q-1-n}.
\tag{RG4}
\]

The actual negative rows are reversed. There is no discretionary reordering here.

The source bridge is explicit:

* `DataKap.lean:13–34,60–87` defines `aPlusQ,aMinusQ,KapDef` and proves the simplified integral formulas (RG3–4).
* `IndefiniteReal/LinksDefs.lean:341–348` defines the actual selected row functions `aPl,aMi`.
* `Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/AMiEqAMinusQ.lean:20–42` identifies those functions with `aPlusQ` and the reversed `aMinusQ`; `44–66` proves `wtOf_kapTop` under `KapDef`.
* `IndefiniteReal/FWExist.lean:518–580` defines `KapIs`, constructs `kapTop`, and proves uniqueness of a weight family satisfying `KapIs` when the embedding set is nonempty. Its column count is exactly `n_V`.
* `ProjectiveLattices/PartitionExtendByZeroAntitone.lean:67–69` defines `wtA`: it puts the positive partition at each selected embedding and the negative partition at its conjugate, extended by zero outside active rows.
* `ProjectiveLattices/IsThRule.lean:84–91` defines `harmA` as the integral `HaO` component and `thGen` using precisely that component. `RecPJThAllNeBot.lean:31` uses `thGen(...)(wtA w) w.n`; `80–87` gives the source nonvanishing implication under its stated rank, level, last-positive-row, harmonic-existence, and global-law hypotheses.

The word family does not make these degrees arbitrary: `Columns/AbelianHostFieldConditions.lean:443–460` fixes `v,b,e` across words, and also fixes the first and last `u`; internal `u` can vary. This is different from varying the entire datum.

## 2. Statement DP61(a): positivity, dominance, and the literal exclusion

For every active stage, `A` and `B` are antitone integral partitions and every active entry is at least one. For `Q≥2`,

\[
A_0-A_1=v_0-v_1-1\ge0,\qquad
B_0-B_1=b_{m-1}-b_{m-2}-1\ge t+2.
\tag{RG5}
\]

For `Q=1`, the last relevant negative gap is `B_0`, with the convention `B_1=0`.

Consequently the unchanged DP58 first-row polynomial, having positive degree in only the first positive and first negative rows and degree zero in every other active row, does not belong to this prescribed row-degree component. This excludes that unchanged polynomial only. It neither proves a lower bound for all polynomials in the component nor rules out completing it.

### Proof

The strict interlacing and integrality give `v_i-v_(i+1)≥1` and `v_(k-2)+b_0≥1`. Two adjacent inequalities in (RG2) give `b_(s+1)-b_s≥2H=t+3`. Hence successive `sigma` entries decrease by at least one. Taking differences in (RG3) shows that `A` is antitone. Its last entry is

\[
A_{P-1}=e_{j-1}-b_{j-1}-(t+1)/2\ge1.
\]

The source separately states this fact in `DataKap.lean:89–106`. From (RG4), `C_0≥1`, as also stated at `108–116`, and

\[
C_{c+1}-C_c=b_{j+c+1}-b_{j+c}-1\ge t+2.
\]

Reversal makes `B` antitone with all entries positive. Formulas (RG5) follow by direct subtraction. Since `P≥5`, there are active later positive rows. The DP58 polynomial is nonzero and has degree zero there, contrary to their strictly positive prescribed degrees. The definition requiring each monomial to have every prescribed row degree is `RowDeg.lean:40–41`. ∎

## 3. Statement DP61(b): an exact sufficient harmonic completion

Let `A=(A_0,…,A_(P-1))` and `B=(B_0,…,B_(Q-1))` be any antitone nonnegative integer partitions. Suppose

\[
0\le a\le A_0-A_1,\qquad 0\le b\le B_0-B_1,
\tag{RG6}
\]

with the next entry interpreted as zero for a one-row partition. If there are at least `P+Q+2` columns, the first-row two-column polynomial

\[
P_{a,b}=\sum_{s=0}^{\min(a,b)}(-1)^s\binom as\binom bs
 X_{0,1}^{a-s}Y_{0,1}^{b-s}X_{0,2}^{s}Y_{0,2}^{s}
\tag{RG7}
\]

can be multiplied by an explicitly defined primitive integral polynomial so that the product satisfies all the source `HaO` conditions with full row partitions `A,B`. This works simultaneously for all conjugate embedding pairs. It is a statement about the algebraic harmonic module, not an identification of a new CM type with the source `Datum`.

### Proof

Put `A'=A-a e_0`, `B'=B-b e_0`. Conditions (RG6) say exactly that these remain antitone nonnegative partitions. Reserve columns 1 and 2 for (RG7), then choose disjoint column sets `C_+` and `C_-` of sizes `P` and `Q`. For a partition `L` of length `d`, define

\[
\mathcal D_L(Z)=\prod_{s=1}^{d}
 \det(Z_{i,c_k})_{0\le i,k<s}^{L_{s-1}-L_s},\qquad L_d=0.
\tag{RG8}
\]

Use the positive rows and `C_+` for `D_(A')`, and the negative rows and `C_-` for `D_(B')`. Let

\[
\widetilde P=P_{a,b}\mathcal D_{A'}(X)\mathcal D_{B'}(Y).
\tag{RG9}
\]

Each prefix-row determinant is unchanged when a later row is altered by adding an earlier row: either that later row is absent, or both rows are present and determinant row addition applies. Thus the determinant products are `RowInv`; (RG7) depends only on the first rows and is also `RowInv`. Their product has this property. The degree of row `i` in (RG8) telescopes to `L_i`, proving the full row degrees in (RG9).

For harmonicity, the source contraction for a pair of rows is the sum of matching-column mixed derivatives. On columns in `C_+`, the polynomial has no negative-row variables; on `C_-`, it has no positive-row variables. On columns 1 and 2, only (RG7) contributes. All other row pairs annihilate it, while the first pair gives zero because the coefficients `c_s=(-1)^s binom(a,s)binom(b,s)` satisfy

\[
(a-s)(b-s)c_s+(s+1)^2c_{s+1}=0.
\]

There are no cross terms from the fillers since their columns are disjoint. The source uses the identity column matrix in `HHa`, so precisely these contractions occur: `RowDeg.lean:21–30,43–48`. Across multiple embedding pairs, contractions only pair an embedding with its conjugate; the same column assignments can therefore be reused in other pairs.

All coefficients are integers. The product of the diagonal terms of the determinants is a monomial with coefficient one: to produce that monomial every individual determinant must use its diagonal term. The `s=0` monomial of (RG7) also has coefficient one and lies in disjoint columns. Thus the product is nonzero and primitive. This proves all `HaO` conditions.

The same determinant facts are supplied by the inspected source `Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsBlockProductMemIntegralHarmonic.lean`: `minor/minorsP` at `28–33`, integral coefficients `43–46`, harmonicity `71–94`, row invariance `97–137`, and row degree `154–200`. The elementary proof above does not require any uninspected part of that module. ∎

## 4. Statement DP61(c): exact vanishing for the pure-kernel completion

Suppose each column carries a formal kernel `K_c(X,Y)` with

\[
K_c(X,0)=K_c(0,Y)=1.
\tag{RG10}
\]

If the filler in (RG9) is nonconstant, then

\[
\widetilde P(\partial)\prod_c K_c\big|_0=0.
\tag{RG11}
\]

### Proof

In every monomial differential operator of a nonconstant filler there is a positive-order derivative in a filler column. In a positive filler column only positive derivatives occur, and in a negative filler column only negative derivatives occur. In either case (RG10) makes its column evaluation zero. The column product factors, so every summand vanishes. In the prescribed source partitions, the positive filler is always nonconstant because later positive rows remain strictly positive after subtracting `a e_0`. ∎

Thus the polynomial completion does not by itself transfer the DP58 sharp nonzero value. Additional prefactor jets can prevent this vanishing, but their valuation must be computed. That is the separate DP63 construction, not an omitted implication of DP61.

## 5. Statement DP61(d): finite source-window bounds

For a fixed `SizeData₂` datum, its `cloud_v` and `be_close` fields imply

\[
A_0-A_1\le Sc-1.
\tag{RG12}
\]

If `Q≥2`, one has both the simple bound and a useful sharper bound

\[
B_0-B_1\le2\eta-1,
\qquad
B_0-B_1\le \eta-H-(Q-2)(t+3)-1,
\tag{RG13}
\]

where `eta=etaSz`. If `Q=1`,

\[
B_0\le\eta-(t+1)/2.
\tag{RG14}
\]

In particular, a fixed pair of source partitions admits only finitely many of the sufficient completions (RG6) for the ray `a=ell^s`, `b=ell^(h-1+s)`. This is not a restriction on all possible harmonic polynomials, and it is not a restriction on families in which the global datum changes.

### Proof

The exact source inequalities are `DataParams₂.lean:160` (`0≤v_i≤Sc`) and `163` (`|b_i-e_l|≤eta`); positivity of `eta` is `164`, and `Sc` is tied to the datum at `148`. Subtracting the two bounds for `v` gives (RG12). Bounding both `b_(m-1)-e_(j-1)` and `b_(m-2)-e_(j-1)` in absolute value gives the first bound (RG13). For the sharper version, (RG2) gives

\[
b_{m-2}-e_{j-1}\ge H+(Q-2)(t+3),
\]

whereas `b_(m-1)-e_(j-1)≤eta`; subtract and then subtract one as in (RG5). For `Q=1`, (RG4) directly gives (RG14). ∎

## 6. Precisely what has and has not been decided

The actual source selected degree component has now been identified through its definitions and explicit bridge theorems. The first-row DP58 witness is not already in that component. A sufficient completion is available with explicit row-gap conditions and ample actual column count, but the pure-kernel evaluation of that completion is zero. Fixed source windows bound the available gaps. These facts do not establish a new multiplicity/lift bound or a universal obstruction to a shorter lift chain.

The old `Datum.dom`/`CMObj.HasType` mismatch remains distinct from this polynomial analysis. DP57's field and adelic-level repair does not make its type induced from the old imaginary quadratic type. Nor does constructing a harmonic polynomial identify its theta expression with the required automorphic image or supply the new `SizeData₂` estimates.

## 7. Provenance and check policy

All Lean modules cited here were read as source text, not executed. New modules were extracted directly from the 14-part original author archive, with exact archive member, byte length and SHA-256 recorded in `selected_row_degrees_sources_pass1.json` and `selected_row_degrees_sources_pass2.json`. Those manifests also include recovery-only files; recovery is not counted as a source read. A consolidated incremental manifest and exact actual source-read ranges are saved separately. Complete proof-check events are recorded only after a whole saved-version reread.
