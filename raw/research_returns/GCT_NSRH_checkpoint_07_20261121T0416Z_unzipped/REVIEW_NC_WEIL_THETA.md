# Independent F39 review: the actual collision fiber and the smooth proper dg gate

Reviewer: `/root/rectangular_and_theta`. Completed 2026-11-21, approximately 00:55 UTC.

## Reviewed versions and scope

- Complete final fragment `finding_F39.tex`, SHA256 `f1dc5eccaa3cb5e3bb8ba262e0f40ee6876f45a2f2594186d9be63311fd0e2c4`.
- Gonçalo Tabuada, *Noncommutative Weil conjecture*, arXiv:1808.00950v7, primary https://arxiv.org/pdf/1808.00950v7 . Local `primary_sources/Tabuada_Weil_1808_00950v7.pdf`, SHA256 `765fc2b7f608fa47c2a386b57a7e3790ce6704581f566b9633ea1e54a85a31e5`.

I read the complete fragment and independently reconstructed its diagonal resolution, all homology groups, the nonsmoothness implication, the matrix-block transfer, and the good-fiber calculation. I directly inspected the cited primary statement contexts and the additional finite-dimensional-algebra application hypotheses. I did not independently reprove the general cyclotomic comparison theorem. This is a fragment review, not a verification of a later main-paper insertion.

**Verdict: PASS, no mathematical blocker.** One recommended locator refinement is to cite §7, equations (7.1)–(7.4), p.17, for the normalized Frobenius calculation: (7.1)–(7.2) give vector-space comparisons and (7.3)–(7.4) give Frobenius normalization. This is a citation precision improvement, not a mathematical change.

## Primary source hypotheses

In the exact v7 version, §1, pp.2–3, explicitly starts with a smooth proper \(k\)-linear dg category and defines its two finite-dimensional rational TP groups and cyclotomic Frobenius. Its conjectural absolute values are 1 in even degree and \(\sqrt q\) in odd degree. Theorem 1.5 compares this conjecture with the Weil conjecture of a smooth proper scheme. The source itself emphasizes that this cyclotomic Frobenius is not induced by an endomorphism of the dg category.

§5.1, pp.13–14, defines properness by perfect Hom complexes over the base and smoothness by a perfect diagonal bimodule, in the Morita-invariant framework. §6.1, pp.15–16, constructs cyclotomic Frobenius through TC/TP and semilinear Frobenius, not a matrix-power map. The periodic variable has its own prescribed Frobenius scaling; identifying it with a GCT quantum parameter is not part of this source.

I also inspected the application paragraphs immediately before Theorems 2.12–2.13. The connective dg application assumes **smooth proper**, and the finite-dimensional dg application retains **smooth**. Thus their wording does not create a loophole making the nonsmooth dual-number algebra an admitted example merely because it is finite dimensional.

## Full algebra calculation

For \(B=k[\epsilon]/\epsilon^2\), put \(S=B\otimes B=k[x,y]/(x^2,y^2)\), \(u=x-y\), \(w=x+y\). In the basis \(1,x,y,xy\), the diagonal augmentation has kernel \(\langle u,xy\rangle\). Multiplication by \(u\) has kernel \(\langle w,xy\rangle\), and multiplication by \(w\) has kernel \(\langle u,xy\rangle\). These equal the alternating preceding images. The displayed infinite two-periodic free resolution is therefore exact in every degree.

After tensoring with the diagonal \(B\), its maps alternate between zero and multiplication by \(2\epsilon\). Since characteristic is greater than three, multiplication by 2 is invertible. The resulting homology is exactly

\[
HH_0(B)=B,\qquad HH_{2j+1}(B)=B/(\epsilon),\qquad
HH_{2j}(B)=k\epsilon\quad(j\ge1).
\]

In particular every positive Tor degree is nonzero. A perfect diagonal would give a bounded derived tensor product with \(B\), contradicting these groups. Therefore \(B\) is not homologically smooth.

For \(A_1=k^2\times M_2(B)\), restriction of a hypothetical perfect diagonal to the central matrix block is exact and preserves finite projectives. The two-sided full matrix-unit Morita equivalence would then give a perfect diagonal for \(B\), which has just been excluded. Conversely finite dimension proves properness. The perfect dg category has the same conclusion by the stated Morita invariance. The claim is specifically that this category fails the domain hypothesis of the cited smooth proper theory; it does not assert that TP cannot be attached to any nonsmooth algebra.

## Good fibers and normalized spectra

At a split parameter with distinct center roots and invertible stated denominators, the Chinese remainder decomposition gives \(k^2\times M_2(k)^2\). Ordinary matrix Morita equivalence identifies its perfect category with four rational points. In §7, (7.1)–(7.4), TP even/odd groups are sums of even/odd crystalline groups, with factors \(q^{-w/2}\) and \(q^{-(w-1)/2}\). Four points have only four degree-zero classes, and every normalization factor and Frobenius eigenvalue is one. The odd group vanishes. No nontrivial weight claim is hidden in this computation.

The radical at the collision is \(M_2(k\epsilon)\), so its semisimple quotient is \(k^2\times M_2(k)\), Morita equivalent to three points. This explicitly loses the nilpotent collision datum. The text correctly leaves smooth replacements or relative theories open and requires an additional comparison before they could address the actual coherent family and designated basis.

The separate Grothendieck paragraph accurately distinguishes affine-scheme and perfect-complex language from the modern dg/noncommutative-motive extension. It does not attribute these computations to the historical manuscript leaves.

Check event: `F39-FINAL-FULL-READ-THETA-PASS`.

## Final correction and insertion match

The corrected fragment was freshly reread in full at SHA256 `e67bdffef7b54e109217490bc8518807d4bcdfd595cd3b7018c0d4e504e21da7`. It now cites §7 (7.1)–(7.4), as recommended, and places the textual ell in math mode. All mathematics and scope remain as checked above. **PASS**.

At main-paper SHA256 `0d2604a625f4210e29cfd786f8934a13cfab786a07365fbbbb95a961e2cd8a9d`, the entire F39 subsection/proof/scope body matches the corrected fragment exactly, and the separately relocated Grothendieck paragraph also matches exactly. This is an exact scoped insertion check, not a new full-paper review.
