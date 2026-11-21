# DP34: independent review of the complete integrated proof

Reviewer: `/root/archive_binomial`, GPT-6 Astra Pro, inherited model; runtime reasoning effort not exposed. Date: 2026-11-21 UTC. Complete reading and challenge: **01:27:59--01:31:08 UTC**. Main event **ABA-CE28**; accompanying DP32 content/version comparison **ABA-CE29**. No main-paper edits were made by this reviewer.

## Outcome and scope

**PASS. The entire integrated DP34 statement and proof are valid under the actual-dual model and normalization already proved in DP32.** I read every paragraph of the integrated proof, the complete draft `actual_dual_general_affine.md`, and the integrated DP33 translation-operator calculation used at its start. The chain remainder, exceptional wrap, induction, exact first degrees and common witness all withstand the challenge. In particular the proof includes $p=2$ and $h=2$; it does not rely on an omitted ordinary arrow when $d=1$.

This is a manual mathematical review of the exact statement/proof block identified below. It is not machine formalization, a new audit of the cited classical theorem proofs, or a proof that a particular theta construction uses these coordinates.

## 1. Low-order identities and preliminary divisibility

The ordinary source axis $S_i$, $i<d$, has exactly one nonlinear logarithm contribution at degree $p$: $S_i^p/p$ in component (i+1). Every later path has strictly greater degree. The exceptional axis $S_d$ has no degree-$p$ nonlinear term and its first nonlinear term is $S_d^{p^2}/p$ in component 1. Consequently the displayed translation coefficients have precisely the two contributions used in the proof. This remains correct when $d=1$, where the exceptional term lies in the same logarithm component as the linear term.

The translation coefficient operators are integral and mutually commuting. They commute with the invariant derivatives because the formal group is commutative. Multiplying the coefficient identities by the relevant factorials gives the stated units (a=-(p-1)!) and (b=-$p^2$!/p^{p+1}). Here (v_p($p^2$!)=p+1), so $b$ is indeed a unit for every prime. Each remainder is an integral scalar multiple of a translation coefficient operator. No unproved commutativity of arbitrary integral endomorphisms is being used.

The descending argument for $D_i^{R_i}\in p\operatorname{End}_{\rm int}$ uses $R_i/p=R_{i+1}$. Its leading term is divisible by $p$ by induction; every other term has an explicit positive power of $p$. The base direction has $R_d=p$ and follows directly from its degree-$p$ translation coefficient. Iterating this operator inclusion supplies the preliminary floor bound on the whole function ring.

## 2. Chain remainder and the exceptional wrap

At step $j=i+t$, the exponent is $N=p^{h-t-1}$, while $R_{j+1}=p^{h-i-t-1}$; hence $N/R_{j+1}=p^i=B$ exactly. The conversion

\[
\left\lfloor\frac{N-m}{R_{j+1}}\right\rfloor
=B-\left\lceil\frac m{R_{j+1}}\right\rceil
\]

is therefore exact. For $0<m<N$, all interior binomial coefficients of the $p$-power $N$ are divisible by $p$, and $m-\lceil m/R_{j+1}\rceil\ge0$. This proves the asserted (B+1) divisibility without requiring the sharper exact binomial valuation. At $m=N$, the binomial coefficient is a unit, so it is essential to use the separate bound $N\ge p^{i+1}\ge B+1$; the proof does so. Each chain substitution changes only the surviving leading term, so previously discarded errors remain in the same ideal.

After the ordinary chain, the exponent on $D_d$ is $p^{i+1}$. Raising its exceptional identity to $p^{i-1}$ extracts exactly the factor $p^{p^i}$. Modulo the next power of $p$, the remaining power of $D_1$ is $D_1^{p^{i-1}}$. Repeated reduction of the ordinary identities identifies it with a unit multiple of $D_i$. All accumulated coefficients are units in $\mathbf Z_p$.

For $i=d$, the direct exceptional step is raised to $p^{d-1}$, whose left side is $D_d^{p^{d+1}}=D_d^q$. For $d=1$, this exponent is one and the recurrence is already the exceptional low-order identity. Thus the full recurrence has the stated power of $p$ in every direction, including the wrap and the smallest height.

## 3. Affine induction and base change

Because $q=BR_i$, the initial range $0\le n<q$ consists of $B$ complete blocks of length $R_i$. Within each block, $c_i n-\lfloor n/R_i\rfloor$ increases. Successive block maxima increase by (c_iR_i-1=1/(q-1)>0). The final point $n=q-1$ gives exactly (B-(B-1)=1). This verifies the complete base range, including $n=0$.

For $n\ge q$, the two recursive orders are (n-q+1) and (n-q), both smaller than $n$. The leading term has the desired bound because (B=c_i(q-1)); the remainder has the additional margin $1-c_i>0$. The integral operator remainder preserves every integral power of $p$. Thus induction proves the real affine inequality, and integer coefficient valuations over $\mathbf Z_p$ give precisely the ceiling in the statement.

The base-change claim is legitimate. The starting operators are invariant derivations and integral translation coefficient operators over $\mathbf Z_p$; all derived operator inclusions concern their integral coefficient matrices, rather than an arbitrary noncontinuous endomorphism. For any fixed output coefficient of a finite derivative, only finitely many input coefficients are used. The divisibility of those coefficients persists after integral scalar extension. This justifies the assertion even over a ramified base without rounding its potentially fractional valuations. Composition yields the sum of the one-direction integer exponents.

## 4. Exact first degrees from Teichmüller equivariance

The character assignment $X_j\mapsto\zeta^{p^j}X_j$ commutes with every ordinary arrow. At the exceptional arrow, $p^2p^d=p^{h+1}\equiv p\pmod{q-1}$, so it commutes there too. The logarithm and its inverse are consequently **exactly** equivariant over the characteristic-zero unramified extension; this is stronger than an equivariance statement only after reduction.

For a nonzero coefficient of $t^n$ in (E_j(te_i)), the congruence $np^i\equiv p^j\pmod{q-1}$ follows. Since $p$ is invertible modulo (q-1), its least positive solution is the displayed $m_{ij}$. The asserted representatives lie strictly between zero and (q-1), including the boundary $p=2,h=2$. Therefore no lower-degree coefficient can have merely positive valuation and escape detection by the scaled reduction: it must vanish exactly.

The first path from input $i$ to output $j$ uses only ordinary arrows if $j\ge i$, and one exceptional arrow otherwise. Its degree is exactly $m_{ij}$. In the scaled inverse's reduction, precisely this first path contributes at that degree; further full cycles multiply the degree by $q$. Its coefficient is a nonzero sign. Undoing both scales therefore gives the exact valuation $r_j-m_{ij}r_i$ of the genuine first nonzero term.

## 5. The simultaneous sharp witness

All exponents $e_j$ are positive, so the lowest-degree coefficient of the product $f_*(E(te_i))$ is the product of the individual lowest-degree coefficients. It has no competing terms at that degree and no cancellation. The three stated telescoping contributions sum to (q-1). Empty ranges at $i=1$ or $i=d$, and both empty ordinary ranges when $d=1$, have the advertised zero values.

The other two sums are also exact:

\[
\sum_j e_j=(p-1)(h+p-1),\qquad
\sum_j e_jp^j=p(q-1),\qquad
\sum_j e_jr_j=h-1=d.
\]

The coefficient valuation is consequently (d-(q-1)r_i). Adding the exact factorial valuation at (q-1), whose $h$ base-$p$ digits are all (p-1), gives $p^i-1$. Any affine error constant strictly smaller than one at the same slope would require valuation at least $p^i$ at this order. Thus this single common monomial proves the claimed sharpness in every direction. The unbounded diagonal sequence from DP32 independently fixes the optimal slope.

## 6. DP32 integrated-content comparison

I read the integrated DP32 block while comparing it with the draft already independently checked in ABA-CE27. The statement and complete argument preserve the reviewed finite-free construction, special-fibre duality and cancellation, Lubin--Tate identification, contraction, exact inverse coefficients, coefficientwise translation and slope witnesses. The draft's equally weighted mean comparison is retained as the separate paragraph immediately after the proof, with its scope limitation intact.

One source locator from the draft was initially absent at the sentence using dual dimensions. I reported this to the parent, who inserted **Tate 1967, §2.3 Proposition 3, p. 166**. I read that exact change. Removing only the inserted citation from the current block reproduces the original integrated hash, confirming that this intervening edit was citation-only. The mathematical content remains unchanged. This is recorded separately as content/version check ABA-CE29, not presented as another independent derivation of DP32.

## Exact reviewed versions

Blocks begin at their theorem environment and end after the complete proof environment, with one trailing LF. Proof-only hashes begin at the proof environment and use the same ending. Hashes are SHA-256 of UTF-8 bytes.

| Scope | Statement and complete proof SHA-256 | Complete proof-only SHA-256 |
|---|---|---|
| DP34 integrated whole-proof review | `eb5be984ea9f34075f00480ee997f6d19af47421ba58b48ed0feb9328502c110` | `c786bafeed90743561717af81cbc13b8070bc1600cb3327237795cc731709496` |
| DP32 integrated content/version check, after the citation restoration | `8a4b04104fe06d196f3ec0402270a7326c7931b3ded661bc28ded6a8702075a4` | `3073895f3fd743831aad2c68df3a6d2ca0deff1bb38be8827c986266c30921cf` |

Snapshots are `late_proof_snapshots/DP34_integrated_archive_checked.tex` (4,632 bytes) and `late_proof_snapshots/DP32_integrated_archive_checked.tex` (6,677 bytes). The initially read DP32 whole-block hash was `58ed3d5d2c8f836987bc1453bde5733782fbe6c748f2091a54d698a4cb2d46ed`; the single citation restoration accounts exactly for its change.
