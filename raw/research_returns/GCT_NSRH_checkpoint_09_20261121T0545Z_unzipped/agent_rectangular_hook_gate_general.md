# Strengthened F28: every rectangle with both sides at least two

Author/checker: /root/rectangular_and_theta, GPT-6 Astra Pro. Date: 2026-11-21 UTC. The strengthening below was independently identified by the root and this agent from the same checked hook-multiplicity lemma. It supersedes the height-two restriction on the obstruction in agent_rectangular_hook_gate.md. That earlier note's known Manivel formula, rational-point rule and non-Young signed example remain valid applications.

## 1. General isolated-hook obstruction

Work in characteristic zero. Let \(M\) be an \(S_N\)-module. Suppose for some internal hook degree \(1\le k\le N-2\),
\[
[M:[(N-k,1^k)]]>0,
\]
but
\[
[M:[(N-k+1,1^{k-1})]]
=[M:[(N-k-1,1^{k+1})]]=0.
\tag{IH1}
\]
Then \(M\) has no scalar-monomial basis whose every label stabilizer is conjugate to a Young subgroup. In particular it has no such signed permutation basis.

Here a scalar-monomial basis means that each group element takes each basis vector to a nonzero scalar times another basis vector. This does not restrict arbitrary stabilizers, nor prohibit positive formulas obtained from another representation-theoretic model.

### Full proof

Let \(B\) be a proposed basis. On an underlying-label orbit \(O\), choose \(b_O\) and let \(H_O\) stabilize its label. The equality \(h b_O=\chi_O(h)b_O\) makes \(\chi_O\) a one-dimensional character. The map
\[
k[S_N]\otimes_{k[H_O]}k_{\chi_O}\longrightarrow kO,\qquad
g\otimes1\longmapsto gb_O
\]
is well defined, equivariant and surjective; its dimensions agree, so it is an isomorphism. Thus
\[
M\simeq\bigoplus_O\operatorname{Ind}_{H_O}^{S_N}\chi_O.
\tag{IH2}
\]

A one-dimensional characteristic-zero character of \(S_a\) is trivial or sign, with these coinciding for \(a=1\). Therefore for a Young subgroup
\[
H=S_{a_1}\times\cdots\times S_{a_r},\qquad
a_i\ge1,\quad\sum_i a_i=N,
\]
its character is a product of trivial/sign factors. Put
\[
s=\sum_{\text{sign blocks }i}(a_i-1).
\]
The designation of a singleton as trivial or sign does not change \(s\).

Let \(U_a\) be the standard sum-zero representation of \(S_a\), with \(U_1=0\). Restriction gives
\[
\operatorname{Res}_H U_N
=\bigoplus_i U_{a_i}\oplus k^{r-1}.
\]
The classical hook identification \(\bigwedge^jU_a=[(a-j,1^j)]\) gives, after taking exterior powers and Frobenius reciprocity,
\[
\left[\operatorname{Ind}_H^{S_N}\chi:[(N-j,1^j)]\right]
=\binom{r-1}{j-s}.
\tag{IH3}
\]
In detail, the trivial factor on block \(i\) forces exterior degree zero and the sign factor forces degree \(a_i-1\). Each singleton contributes degree zero under either designation. The remaining degree \(j-s\) comes from the trivial \((r-1)\)-space, giving the binomial multiplicity. This is the previously fully checked RH5 lemma. Its hook identification also follows directly from Pieri: for \(1\le j\le a-1\), \(\bigwedge^j k^a=\operatorname{Ind}_{S_j\times S_{a-j}}^{S_a}(\mathrm{sgn}\boxtimes1)\) is the sum of the two adjacent hooks, and \(k^a=1\oplus U_a\), starting in degree zero, identifies the desired hook by induction.

The positive hook support of an orbit summand is therefore exactly the interval
\[
s,s+1,\ldots,s+r-1.
\]
It lies in \(0,\ldots,N-1\), since \(0\le s\le N-r\).

By IH1 and the effective direct sum IH2, some orbit summand must contain degree \(k\). If \(r\ge2\), its interval contains \(k-1\) or \(k+1\), contrary to one of the zero multiplicities in IH1. No cancellation is possible in a direct sum of actual modules. Thus that orbit has \(r=1\), so \(H=S_N\), and its induced character is just trivial or sign. Its only possible hook degrees are \(0\) and \(N-1\), contradicting that \(k\) is internal. ∎

## 2. Exact existing source input for all rectangle squares

Ikenmeyer–Panova, *Rectangular Kronecker coefficients and plethysms in geometric complexity theory*, arXiv:1512.03798v2, **Proposition 6.4, printed p.15**, gives the following exact hook generating polynomial for a rectangle \(\rho=(a^b)\), where \(m=\min(a,b)\) and \(N=ab\):
\[
\sum_{k=0}^{N-1}g((N-k,1^k),\rho,\rho)t^k
=\prod_{i=2}^{m}(1+t^{2i-1}).
\tag{IH4}
\]

The source states it after exchanging the rectangle sides so that its height is at most its width; transposing both Specht factors preserves their tensor square, which gives the symmetric formulation here. This proposition has no lower bound such as \(m\ge7\); that bound belongs to a different hook-positivity theorem. We use the exact Proposition 6.4.

Exact local locator: sources/LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/main.tex, proposition beginning at line 1381 and proof through line 1427. The numbered statement and full generating-function proof were matched directly to the primary PDF, <https://arxiv.org/pdf/1512.03798>, printed pp.15–16. The source derives the product using Littlewood's identity, rectangular complementary Littlewood–Richardson coefficients and diagonal hooks of self-conjugate partitions. It is cited here as a known theorem rather than re-proved.

For every \(a,b\ge2\), the factor \(1+t^3\) occurs, and every other positive generator has degree at least five. Thus IH4 gives exactly
\[
g((N-2,1^2),\rho,\rho)=0,\qquad
g((N-3,1^3),\rho,\rho)=1,\qquad
g((N-4,1^4),\rho,\rho)=0,
\tag{IH5}
\]
whenever these three hook degrees are in range.

## 3. General rectangular theorem, including the sole small edge

**Proposition F28-general.** For every rectangle \(\rho=(a^b)\) with \(a,b\ge2\), the actual \(S_{ab}\)-module
\[
[\rho]\otimes[\rho]
\]
has no scalar-monomial basis whose every label stabilizer is conjugate to a Young subgroup.

**Proof for \(ab\ge6\).** The three degrees \(2,3,4\) are valid, and degree three is internal because \(3\le ab-2\). Formula IH5 gives the isolated internal hook required by IH1, so the general lemma applies.

**The size-four edge.** The only possibility is \(\rho=(2,2)\). The exact decomposition, either from the already checked S4 character or from Manivel's Theorem 1, is
\[
[(2,2)]^{\otimes2}
=[(4)]\oplus[(2,2)]\oplus[(1^4)].
\]
Its hook support is \(\{0,3\}\). Any Young orbit with two or more nonempty blocks would force consecutive hook degrees by IH3, which is impossible. Thus all label stabilizers would be the whole \(S_4\), giving only trivial/sign summands, which cannot supply \([(2,2)]\). This handles the edge and completes the proof. ∎

There is no size-five rectangle with both sides at least two. If one side is one, the Specht module is trivial or sign and its tensor square is trivial, so the exclusion of those rectangles is necessary.

## 4. Consequence for the actual GCT projector module

For \(U,V\) of dimension \(b\) and \(N=ab\), ordinary Schur–Weyl duality identifies the unprojected rectangular Satake multiplicity module with
\[
\operatorname{Hom}_{GL(U)\times GL(V)}
(\det^a U\boxtimes\det^a V,(U\otimes V)^{\otimes N})
\simeq[(a^b)]\otimes[(a^b)].
\]
The symmetric group acts diagonally on the two Specht factors. Thus the obstruction applies to the actual module whose Schur projectors give all rectangular Kronecker coefficients, including rectangles in large-parameter GCT ranges. It is not an objection based only on an unrelated small representation.

The conclusion is specifically that the F23 mechanism requiring a scalar-monomial basis **and Young label stabilizers** cannot supply all its projector multiplicities through that module. Non-Young stabilizers remain possible; the \(2\times2\) rectangle even has the explicit signed model “three pairings plus a sign line.” Other multiplicity models, direct combinatorial rules, the known height-two semi-invariant monomial algebra, and the existing two-row crystal formulas are unaffected.

In representation \(K_0\), IH2 is an equality in the effective cone, which is why absent neighboring hooks give a contradiction. A virtual alternating sum of induced Young modules could cancel those hooks, but would not be a positive orbit decomposition and is outside the claim.

## 5. Verification status

The full RH5 hook-interval lemma and the size-four case had already passed the independent review recorded in REVIEW_RECTANGULAR_HOOK_GCT.md. The root and this agent independently recognized that only the isolated degree-three hook is needed; hence the whole IP product need not have gap-separated support. Proposition 6.4's actual numbering, parameters, primary PDF and local proof were freshly checked. A new independent review of the general isolated-hook argument and its all-rectangle application has been requested; no earlier review is claimed to cover this extension automatically.

