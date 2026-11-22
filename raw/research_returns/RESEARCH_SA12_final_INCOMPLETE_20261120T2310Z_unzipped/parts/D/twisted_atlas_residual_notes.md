# Growing central obstruction: exact remaining presentation requirement

Research notes after checkpoint13, 2026-11-20. No new theorem is promoted here.

## What is already proved

For the original-boundary tame group of a normal proper surface, prime-to-characteristic constant second cohomology has polynomial cardinality in the coefficient order. Every fixed bound on the order of a cyclic central kernel can therefore be killed on one fixed open subgroup. Together with the hereditary quadratic defining-characteristic representation count this gives the checked bounded-scalar theorem, and hence the named linear/unitary bounded-centre and symplectic/orthogonal simple-product consequences.

The unresolved extension is a representation count uniform as the central order grows. Counting the obstruction classes alone is insufficient: one also needs the correct estimate inside each class.

## A concrete algebra-linear formulation

Let a fixed obstruction class admit a locally free twisted generator G of rank d, and let F be a twisted object of rank r in the same class, where d divides r in the generic division-algebra situation. Write A=End(G) and M=Hom(G,F). Then M has ordinary rank dr and generic A-rank r/d. If we had a fixed-twist global-generation theorem, uniform in d,r and the relevant unit structures, a general A-linear generating set would need only ceil(r/d)+O(1) sections: on a splitting chart this is the usual degeneracy-codimension estimate for a map from copies of a rank-d bundle to a rank-r bundle. With h0(M(m))=O(dr), those generator parameters would have size O((r/d+1)dr)=O(r^2), because d<=r.

This conditional parameter calculation is useful, but the required uniform A-linear generation and fixed-length A-linear resolution have not been proved. The ordinary Beilinson construction controls cohomology of M in size O(dr); it does not divide the number of object coordinates by d^2. Taking End(F) instead has rank r^2 and leads to an ordinary quadratic atlas of size O(r^4). Likewise a dg generator G has Ext(G,F) of size O(dr); Morita terminology alone does not make its global presentation have A-rank O(r/d). The period/index and the chosen generator must remain visible in every proposed bound.

## Fresh primary-source quantifier check

We opened the complete relevant primary passages below. These establish boundedness for fixed geometric data; they do not state the missing uniform quadratic estimate.

1. Fabio Nironi, *Moduli Spaces of Semistable Sheaves on Projective Deligne-Mumford Stacks*, arXiv:0811.1949v2 (22 September2009), <https://arxiv.org/pdf/0811.1949>. Definition4.2, printedp27, defines regularity using the chosen generating sheaf. Theorem4.12 and its complete proof, printedpp29--30, fix the polarized stack and generator E. In the implication(3)=>(4), N is the maximum of h0(F_E(F)(m)); the further presentation in(5) also depends on that bounded family. Corollary4.17, printedp31, transfers boundedness between the stack family and its F_E image. Web primary refs: turn634527455view1, turn903033882view1; full theorem/proof at source lines1752--1850.

2. Max Lieblich, *Moduli of twisted sheaves*, arXiv:math/0411337v2 (8 July2005), <https://arxiv.org/pdf/math/0411337>. Lemma2.3.2.8 and Proposition2.3.2.9 with the full displayed proof, printedpp29--30, choose a fixed locally free twisted generator and fixed geometric Hilbert polynomial before applying ordinary boundedness to Hom(V,F). The passage does not supply uniformity in generator rank or gerbe index. The Frobenius weight change is stated separately in Lemma3.2.3.10, printedpp48--49. Web primary refs: turn634527455view0, turn903033882view0. We use this audit only to identify the quantifiers and the Morita-rank cost; we do not import a quantitative theorem from it.

No new page-image inspection, numerical experiment, or proof of a growing-centre bound is claimed. C is independently studying the related linear-in-cover-degree object-atlas issue; its intrinsic Hom-space estimate alone does not presently supply the missing object presentation here.

## Principal-bundle boundedness checked at 10:27 UTC, 2026-11-20

We freshly opened the primary arXiv PDFs and read the following complete passages; these are source-quantifier checks, not new finite-generation theorems.

1. Langer, A. (2004, September 27). *Semistable principal G-bundles in positive characteristic* (arXiv:math/0312260v4), Section 7.1--7.4, printed pp. 18--19. https://arxiv.org/pdf/math/0312260 . Theorem 7.3 and its complete proof first bound the associated adjoint vector bundles, then parametrize reductions of structure group by a finite-type scheme of sections. Theorem 7.4 retains a fixed reductive group and fixed numerical bounds. This proves qualitative boundedness but supplies no coordinate/degree bound uniform as G=PGL_r varies. We do not infer an O(r^2) atlas from this result. Opened web references: turn763756358view0, turn772066212view0.

2. Langer, A., Schmitt, A. H. W., & Sols, I. (2008, June 26). *Moduli spaces for principal bundles in arbitrary characteristic* (arXiv:math/0506511v4), Section 5.3.1, printed pp. 55--56, read in full, including Proposition 5.3.3. https://arxiv.org/pdf/math/0506511 . The construction fixes a faithful representation and a Hilbert polynomial, then selects an invariant-generator degree s and regularity n; its ambient coordinates include Hom(Sym^i(U tensor V)^G,H^0(O(in))). Neither the number of these coordinates nor the equations is bounded quadratically in varying PGL rank in the cited passage. The qualitative moduli construction therefore does not discharge our quantitative gerbe gate. Opened references: turn763756358view1, turn772066212view1.

The direct principal-PGL formulation may still be useful: deformation spaces involve the adjoint bundle, of rank r^2, so their dimensions can be O(r^2). However, a tangent-space bound does not bound the number or degree of connected components of a global atlas. Treating the adjoint bundle as an arbitrary rank-r^2 vector bundle again costs O(r^4) raw matrix coordinates. A uniform intrinsic algebra-linear/Morita presentation remains unproved. B independently reports no verified theorem giving the required quantitative presentation.
