# Full source, hypothesis and proof match: F59 scalar closure in every type-A rank

Reviewer: `/root/rectangular_and_theta`, GPT-6 Astra Pro; inherited reasoning effort not exposed. Date: 2026-11-21 UTC.

## Exact target and verdict

I read every section of `agent_soergel_allrank_scalar_closure.md`, SHA256 `475bd56d0486831328193453faec89612ea1c97a8bb81786d12970053eb34f27`, including all proofs, source statements, limits and dictionary. **Complete source/hypothesis/application match PASS. No correction requested.**

The all-variable module input is my own separately saved report, and the descent was jointly proposed and reconstructed; this record is a fresh whole-text check and explicit source match, not a claim of independent conception. `/root/gct_statements` is assigned the additional independent whole-proof review. The elementary two-variable proof remains separately complete and reviewed.

## Primary theorem and its precise application

I re-read the exact saved primary extraction of Lichtenbaum's original article, Theorem2, printed pp222--223, particularly the complete-unramified-regular-local hypothesis, finite generation, nonnegative higher Euler characteristics, the torsion-free equality case and positive Tor rigidity. The original extraction loses some mathematical subscripts. I checked the exact field-case indices again against Hochster's primary-author lecture notes, printed p169, Corollary (S. Lichtenbaum), case(1), and its surrounding Koszul reduction. No unverified general ramified equality case or inaccessible later paper is used.

The saved source files are `primary_sources/Lichtenbaum_1966_primary_web_excerpt.txt`, SHA256 `5e56160785f60553baa9f7756ff3940b796212298098988106773217d85051ae`, and `primary_sources/Hochster_2012_primary_web_excerpt.txt`, SHA256 `f36c07f365bae2dd27455b4ec3a12512c95362cba8bd09681160919786689b15`. Their URLs and honest retrieval status are recorded in `agent_soergel_top_module_all_variables.md`, SHA256 `b5a655cbc1748433c10cb29912d07f4af929ed60c03b52314f97cec739925de1`. The original article was read as author-upload web text; no downloaded or visually inspected original PDF is claimed. The lecture PDF was opened through the web extraction. Stacks tags00MB/00MC supply the separately checked completion facts.

The assembled application checks every condition. The actual ring is a polynomial ring over a characteristic-zero field; its completed origin ring is a complete equicharacteristic unramified regular local power-series ring. The torsion-free quotient embeds in a finite free module by clearing denominators, and flat completion preserves this injection. The finite graded right module is killed by a power of the homogeneous maximal ideal, so completion does not change it or the finite-dimensional tensor complex. All Tor lengths are finite and equal their vector-space dimensions because the residue field remains k.

The N-variable Koszul resolution bounds the minimal free resolution without a false projective-dimension-one assertion. Its Euler ranks give exactly `chi1=dim(V tensor Q)-rank(Q) dim(V)`. Lichtenbaum gives nonnegativity and, in the equality case with Q torsion-free, vanishing of all positive Tor. A nonzero last minimal free term would contain copies of the nonzero socle of V in its final tensor kernel, contradicting that vanishing. Thus equality forces freeness. The graded torsion quotient proof then extends the result to every finite module, with only a left-module splitting when that quotient is free.

## Ambient-group and geometric-support hypotheses

For either ordinary standard type-A realization, the product involution tau=(s,s) has a two-dimensional minus eigenspace. Over characteristic zero one can choose the two independent root coordinates x,y and fixed spectator coordinates as in AR1. All have the same positive grading. The finite group is the actual full product `S_n times S_n`; the proof never restricts the complex to a rank-one subcategory.

The ordinary exact graph localization gives a positive cohomological group-algebra polynomial. The Euler class is exactly `2(e+tau)` after internal grading is forgotten. The augmentation and uniform idempotent-probability argument apply to any finite group, so actual generic cohomology has precisely the two possible graph labels, with the scalar dimension rank identity in every cohomological degree. This step does not retain internal grading and does not exclude torsion on its own.

For a globally left-free module with this generic support, the right root-coordinate matrices satisfy the same coprimality identities as in two variables. The extra coordinates act by their left scalars on both generic graph types and hence globally by torsion-freeness. Thus the two homogeneous involution idempotents split the module into actual free graph summands. Graded projective freeness follows by lifting an origin basis and graded Nakayama, independent of the number of variables. No specialization of spectator variables is performed.

## Complete cohomological proof match

I independently reconstructed the remaining chain in the complete report:

- The left-origin quotient proves the tensor square of every nonzero finite graded bimodule is nonzero, including torsion modules.
- The highest global cohomology degree therefore equals the highest scalar degree; comparison with the actual generic graph tensor forces that same highest degree to survive generically.
- The highest module has positive rank equal to the highest scalar multiplicity. Its actual tensor-square relation and the new module inequality force left freeness, then the two-graph lemma forces right freeness.
- In every descent step the higher projective cohomology is split only in the right-module complex category. The resulting map on the near-top cohomology is the intrinsic cycle cross-product, so underlying bijectivity gives a bimodule isomorphism without bimodule formality.
- The two exceptional origin-fiber terms each have size `r phi(M_s)`. All higher terms match by the known rank identity. Their cancellation gives `phi(M_s)=rank M_s`. A minimal free surjection has a rank-zero kernel inside a free domain module, so the kernel vanishes. This removes generically invisible torsion too.
- Once all cohomology is actual globally graph-free, the full internal/cohomological multiplicity polynomials are valid. The canonical Künneth map gives `a²+b²=da` and `2ab=db`. The nonzero tau coefficient forces `d=2a` in the integral Laurent domain, contradicting the odd outer coefficients of the prescribed scalar Euler polynomial.

No step in that chain after the module inequality uses total dimension two. Therefore the conclusion applies directly in each stated ambient type-A polynomial ring, including the permutation realization's fixed coordinates, and excludes an isolated bounded derived construction there as well as a compatible uniform one.

## Scope and dictionary

The report keeps the scalar coefficient a bounded complex of finite graded k-vector spaces. It does not include arbitrary polynomial differentials in a central bimodule coefficient, changed ambient Euler embeddings, unbounded objects, localization away from the origin or another geometric category. It asserts no purity, arithmetic trace or canonical-label comparison. The old residual nonflat case is closed under these precise scalar hypotheses; larger alternatives are correctly left outside the theorem.

The EGA affine sheaf dictionary, SGA6 perfect-complex language and SGA3/SGA6 grading/K0 anchors remain framework references. The new known local input is identified separately and accurately as Lichtenbaum's theorem. The ordinary Soergel and graph-localization source conditions are those already fully audited for F59. No unpublished Grothendieck statement is credited with this deduction.

No master file or shared event log was edited. An eventual generated all-rank fragment still needs a complete exact text match.

## Entire generated-fragment and bibliography match

I read every line of `finding_F59_allrank_scalar.tex`, SHA256 `956b51070bd4cfc30b208512912bf0501d2da8d38a43ec94c65bbd56bd763b77`, together with the complete `finding_F59_allrank_bib.tex`, SHA256 `49f61afe0214ec14d4b7e666f943e04a6c64674373277aa6bf68a254ef416e17`. **Final source/hypothesis and whole-text match PASS.**

The fragment preserves the exact Lichtenbaum clauses and the full completed torsion-free module application, including the explicit alternating definition of chi1. It preserves the actual full-group generic calculation, top-degree argument, extra-coordinate global graph action, one-sided canonical Künneth proof, entire origin-fiber descent, and the final global grading parity contradiction. The theorem remains limited to the specified ordinary type-A realization, scalar complex, ambient Euler class and actual quadratic. The bibliography uses the original 1966 theorem, the primary-author field-case corroboration and the two exact Stacks completion statements, and honestly describes original-article access as web extraction. No known theorem is presented as a new result, and no new assertion appears only in the generated fragment.
