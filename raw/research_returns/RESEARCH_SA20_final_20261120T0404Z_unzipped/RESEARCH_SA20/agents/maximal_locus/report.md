# A.5 maximal-locus research report

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort configuration, agent `/root/maximal_locus`, RESEARCH_SA20 run of 19 November 2026. We claim no priority. Parent owns final assembly, persistence, and qualification of progress.

## Current mathematical status

The original maximal-locus gate remains unresolved when target dimension is at least three and fibre dimension is at least two. A5.012, A5.013 and A5.014 already cover finite fibres, targets of dimension at most two, and graph fibres respectively. The rare-complement part is already proved. We have not promoted any of the new method investigations into a proof or refutation of the original general statement.

## A5.015: a smooth-source proper product without a Thom stratification

We prove A5.015 in `part_A5_method.tex`, over every real closed field and every o-minimal expansion. Put `X = R² × S² × R` and define

\[
f(a,b,x,u)=(a,b,u^3-bx_1).
\]

The source is a smooth algebraic 5-manifold. The exact semialgebraic product trivialization is

\[
(a,b,c,x)\longmapsto(a,b,x,\sqrt[3]{c+bx_1}).
\]

The fibres are closed 2-spheres, and bounded target coordinates bound `u³=c+bx1`, proving definable properness. The maximal bundle locus is the whole 3-dimensional base.

Nevertheless, no neighbourhood of any `(a0,0,0)` admits a finite compatible ambient C1 Thom stratification. Any finite source partition leaves an open part of the central sphere in one stratum. At a point where the height differential is nonzero, the central kernel contains the whole sphere tangent plane. Along `(a0,t,x0,0)`, the full vertical plane is `ker(dh) ⊕ R∂u`, which excludes one of those sphere directions. A tail belongs to one stratum. If it is the central stratum, constant-rank kernel continuity fails; if it is another stratum, Thom's incident-stratum inclusion fails. Orthogonal projection matrices give the required Grassmannian limit over the given real closed field, with no use of ordinary sequential compactness.

The full proof handles every finite compatible source and target refinement and does not assume that the central fibre is a stratum in advance. This disproves the proposed necessity of ambient Thom stratifiability for an actual proper definable bundle. It is a **method obstruction only** and receives **no original-row movement credit**.

## Verification and earlier construction

The exact checker `code/check_smooth_product_without_thom.py` records **12 PASS** in **0.04600877300254069 seconds**. It checks product, tangent, derivative, approach-curve and rank-minor identities. It does not claim to enumerate stratifications; their nonexistence is proved in the paper. Output is in `logs/check_smooth_product_without_thom.json`.

The earlier rational graph construction, including complete interval and S² proofs, remains in `notes/product_without_thom.tex`. Root independently audited both earlier proofs as PASS and reran their 12 checks in **0.09250224501010962 seconds**; the root audit is `notes/root_product_without_thom_audit.md`. The new polynomial example strengthens that construction by making the source smooth and simplifying the proof. Root subsequently read the complete new proof and checker and recorded PASS. Its independent rerun is managed separately by root.

For definitions we opened the original publisher article Giménez Conejero–Lê–Nuño-Ballesteros, *Thom condition and monodromy*, RACSAM 117 (2023), article 18, DOI 10.1007/s13398-022-01353-y, Definitions 2.1–2.2. Root independently reopened those definitions. This reference fixes the ambient stratified-submersion and tangent-kernel convention; it is not an attribution of our construction.

## Unfinished actual-gate routes

We checked the existing source audit before drawing source conclusions. Valette's generalized-critical-value theorem and the Koike–Shiota map-moduli example do not identify the exact bundle locus. The latter's exceptional circle has nearby finite fibres; the obvious parameterized master map consequently fails to be a bundle throughout its exceptional parameter axis. Mapping-torus encodings retain isotopy rather than the required conjugacy data.

A mapping-cylinder approach may instead encode approximation of a fixed surjection by definable homeomorphisms. The necessary parametric approximation and finite-format selection statements remain unproved. The low-dimensional complete-regularity results of Dyer–Hamstrom likewise do not automatically provide definable parameter families over arbitrary real closed fields. We have not substituted either missing claim for a proof.


## A5.016: coherent approximation for one cell-like surface map

We prove that an individual continuous definable cell-like surjection between compact closed surfaces over the real numbers is the endpoint of one jointly definable continuous family of homeomorphisms. Equivalently, its double mapping-cylinder height projection has a definable product chart at zero. This is a **special-model method result**, with **no original A5 movement credit**; the multidimensional parameter family and arbitrary-real-closed-field extensions are not claimed.

The proof first uses Siebenmann's original Theorem A and Complement (1972, pp. 271–272) to identify the mapping cylinder topologically as a three-manifold. Shiota's exact scalar triangulation (2010, Theorem 2.2(1), p. 6) makes its height PL. A direct finite link argument shows that this triangulation is a PL three-manifold, using local homology and compact surface classification, including the boundary count. A finite matched-stellar subdivision argument then levels an ordinary PL collar to the prescribed height. This last lemma works over every real closed field and is inspired by Rourke–Sanderson Lemma 4.23, p. 58. It does not use an infinite sequence of increasingly fine meshes.

The included proof is `part_A5_surface_method.tex`. Root read the complete candidate and provisionally passed all three proofs before promotion. The parameter-fold example shows that a PL collar over parameters alone does not imply a height collar over those parameters; it has three positive-level preimages accumulating at a central singleton. The special family of surface mapping cylinders retains fixed positive-level fibres, so that example is not a counterexample to the remaining family question.

The exact checker `code/check_surface_collar_parameter_fold.py` records **21 PASS in 0.06886558799305931 seconds**, with output in `logs/check_surface_collar_parameter_fold.json`. It verifies all three affine pieces, boundary matching, three preimages and their strict region/distinctness inequalities using positive-coefficient rational certificates. It certifies only the finite displayed algebra; the collar and surface theorems are proved mathematically.
