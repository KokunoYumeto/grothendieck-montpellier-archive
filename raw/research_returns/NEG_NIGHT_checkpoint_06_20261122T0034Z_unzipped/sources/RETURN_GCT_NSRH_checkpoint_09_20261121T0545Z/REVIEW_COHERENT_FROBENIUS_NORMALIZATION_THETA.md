# F36 normalization supplement and complete final-fragment review

Reviewer: `/root/rectangular_and_theta`. Completed 2026-11-21, approximately 00:58 UTC.

## Exact versions and check scope

- New constructive supplement `agent_coherent_frobenius_normalization.md`, SHA256 `d6739a0dbd4b2017e461411936ddc10202e25f36cab3685a9390113ac0c8ab76`.
- Complete generated fragment `finding_F36.tex`, SHA256 `45762e78c84d6a7235bb301ae9e3a203bf6e94106cdf8edc4ccb9406baf4f276`, 260 lines.
- Previously reviewed complete original report `agent_coherent_frobenius_gate.md`, SHA256 `0505059c15c9cafe19372b2f6c6dd5205a951617ac961d5c403fa11b16bb2fd0`; its full independent review is `REVIEW_COHERENT_FROBENIUS_THETA.md`, SHA256 `faeb23c16f2462c9875c58d56bc09f8353e1b56c2f7d8b910f93aafdcb2f4930`.

I freshly read the complete normalization supplement and independently reconstructed every assertion. I also read all 260 lines of the final fragment and checked the full proofs, including the original-report material, against the actual formulas and its prior full review. This is a mathematical review, not proof-kernel verification. It is a fragment check, not a later main-paper insertion check.

**Verdict: PASS. No mathematical blocker or correction is required.** For stylistic precision only, “rank-64 module over \(R\)” is preferable to “64-dimensional module” when referring to the lattice. The free rank, residue-field dimension, and all lengths in the proof are nevertheless unambiguous and correct.

## Normalization and exact preservation of the action

For \(C=R[x]/x(x-\Delta)\), the map \(a+bx\mapsto(a,a+b\Delta)\) is injective because \(\Delta\ne0\) in the domain \(R\). Its image is exactly the pairs congruent modulo \(\Delta\). The cokernel is \(R/(\Delta)\), of length \(m\). This really is the normalization: after inverting the parameter its total fraction ring is the product of the two fraction fields, the branch idempotents are integral, and each factor \(R\) is integrally closed.

Applying the construction entrywise to the matrix block gives \(A\hookrightarrow\bar A=R^2\times M_2(R)^2\), with quotient four copies of \(R/(\Delta)\), hence length \(4m\). Neither the new branch idempotents nor their unit action is incorrectly asserted to belong to the original integral order.

On the four normalized components, the prescribed bundles have ranks \((1,1,2,2)\) and \((20,4,16,4)\). Their finite pushforward gives exactly \((R^{20},R^4,L_1^{16}\oplus L_2^4)\). For the finite locally free \(E\), the displayed pushforward–Hom isomorphism follows from ordinary adjunction and local freeness. In affine coordinates it is the equality of the two branch row modules with the row module having coefficients \(L_1^{16}\oplus L_2^4\). The right endomorphism action is precomposition, so its restriction is exactly the original \(A\)-action. This preserves the specified module through the previously established regular F21 identification, not merely its dimension or generic character.

## Unit Frobenius upstairs and its nonunit pushforward

Each normalized component is \(\operatorname{Spec}R\), and a chosen free basis gives the unit map \(F_R^*R^r\to R^r\) by \(1\otimes e_j\mapsto e_j\). This applies to both bundles and hence their row-Hom module. Entrywise Frobenius is a ring endomorphism of the matrix rings because their coefficient rings are commutative of characteristic \(p\). It is not the noncommutative matrix-power operation.

The normalization inclusion commutes with Frobenius: evaluation on either root followed by \(r\mapsto r^p\) equals evaluation of the absolute Frobenius of \(C\). Thus the normalized unit model retains the original action after restriction.

The finite-map Frobenius square is commuting; it need not be Cartesian for the displayed natural comparison map. On branch \(i\), its algebraic formula is exactly

\[
C/(x_i^p)\longrightarrow C/(x_i),\qquad 1\otimes c\longmapsto c\bmod x_i.
\]

This is the reduction surjection, whose kernel is the opposite branch modulo \(\Delta^{p-1}\). The multiplicity sheaf has 20 branch copies; the actual row module has 40. Thus the respective lengths are \(20m(p-1)\) and \(40m(p-1)\), giving \(80(p-1)\) at the actual order-two collision. Inverting the parameter kills the complete defect. The normalization repair is therefore an actual unit model upstairs, while the comparison explicitly prevents a unit structure on the original branch sheaf downstairs.

## Final fragment: full recheck of the original obstruction

The identities \(x^p=\Delta^{p-1}x\) and \((x-\Delta)^p=\Delta^{p-1}(x-\Delta)\) give the cyclic pullbacks and their \(R\oplus R/(\Delta^{p-1})\) structure. The fragment explicitly calls this only an \(R\)-module splitting. Its precise kernels under reduction are correctly oriented to the opposite branches.

In the periodic free resolution of \(L_1\), the rightmost differential is \(f_1=x\), followed by \(f_2=x-\Delta\). The annihilators are the opposite ideals. Twisting multiplies each map by the regular scalar \(d=\Delta^{p-1}\), leaving kernels unchanged and shrinking images by \(d\). Therefore odd positive Tor is \(L_1/d\), even positive Tor is \(L_2/d\), with the branches exchanged for \(L_2\). The first positive Tor is the same branch, unlike the underived reduction kernel; the fragment keeps this essential distinction correct.

Intrinsic entrywise Frobenius fixes the matrix units, so Morita extension of scalars transfers the cyclic calculation. The module has scalar ranks 20 and 4 and branch-row ranks 32 and 8. Hence its underlying pullback is exactly \(R^{64}\oplus(R/d)^{40}\), and every positive derived Tor has the 40 torsion copies. The scalar sectors have no higher contribution. The coefficient \(\Delta=\frac34t^2+O(t^3)\) remains a unit times \(t^2\) in characteristic greater than three, so the specialization length is correct.

The parameter-base pullback \(C^{(p)}\) has equation \(X(X-\Delta^p)\), and relative Frobenius sends \(X\) to \(dx\). Its two-basis matrix is \(\operatorname{diag}(1,d)\), with injective map and cokernel length \(m(p-1)\). In normalized-pair coordinates it is the inclusion of congruence order \(mp\) into congruence order \(m\). This is finite and universally homeomorphic, as in F22, while its coherent cokernel is nonzero.

Finally the adapted row convention is checked with its correct order:

\[
r_{\rm old}=r_{\rm ad}B,\quad
\rho_{\rm ad}=B\rho_{\rm old}B^{-1},\quad
U=(B^{[p]})^{-1}B.
\]

It gives \(\tau_{\rm old}(r)=r^{[p]}U\) and
\(\rho_{\rm old}(\phi_A(a))=U^{-1}\rho_{\rm old}(a)^{[p]}U\).
Substitution verifies action compatibility. The inverse exists since the adapted basis is regular and invertible. The source does not assume that uncorrected original-basis entrywise Frobenius preserves the embedded algebra, and the fragment explicitly preserves this qualification.

## Scope check

The theorem distinguishes three objects: algebra/center pullback, parameter-base pullback, and coherent pullback on the normalization. Their outcomes differ for proved reasons, not by a change of terminology. Absolute coherent Frobenius is distinguished from geometric Frobenius on an \(\ell\)-adic realization. Neither the module model nor its unit repair is claimed to identify the quantum grading with weights, supply VIII's designated basis, or establish a path-output sign. The separate Grothendieck paragraph accurately states the coherent versus ordinary étale length distinction.

Check events: `F36-NORMALIZATION-FULL-THETA-PASS`; `F36-FINAL-FRAGMENT-FULL-THETA-PASS`.

## Scoped main-paper insertion check

At main-paper SHA256 `0d2604a625f4210e29cfd786f8934a13cfab786a07365fbbbb95a961e2cd8a9d`, the complete F36 subsection, finding and proof body matches the reviewed final fragment exactly. The relocated dictionary paragraph is edited and augmented with specific EGA/SGA/archive citations, so it is **not** covered by an exact fragment-match claim. Its opening mathematical paragraph matches the checked substance above; I do not extend this check to independently verifying the added archival/source locators.
