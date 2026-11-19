# Cote33, scans002–049: full source review

**Review date:** 19November2026. **Reviewer:** GPT-6 Astra Pro, inherited reasoning effort not exposed, subrun `SA12/review_33`.

This review covers all91 indexed Pro-note entries, every line of the1294-line transcription, and the complete doubts file, including all233 marked unsure occurrences. It uses no second-pass changes and no images: none are present for this package. It makes no alteration to the transcription. The judgments in `entries.tsv` were made from the actual passages, including cancelled material, not generated from headings or keywords. The programs serialize those judgments and perform the separately specified exact calculations.

## 1. What the package contains

The opening handwritten programme uses L-functions as the occasion to extend étale cohomology: first torsion duality, Künneth and Lefschetz; then ℓ-adic coefficients; then applications. The actual progression is through sites and geometric points, ordinary-image transitivity, proper and smooth base change, comparison, cohomological dimension, supports and purity, constructibility, compact supports, local fundamental classes, global traces, derived categories and duality examples. The opening sentence does not state a particular L-function rationality theorem. The title-only scan46 promises global duality without writing its statement.

This is also a bundle of reused paper. Of48 scans,24 are ordinary handwritten/text leaves,23 are reused typed leaves, and one is the title-only leaf. The small manuscript foliation runs1–48, whereas scan labels run2–49. The catalogue’s cote title includes1965; that label is not an independent date for every loose or reused sheet.

The typescripts form distinct strands:

| Strand | Observed source markers | Consequence for attribution |
|---|---|---|
| Coxeter/root-system exposition | n°391; discontinuous pages137,179,180,187–194,211–214,216–218 | Subject and organization fit Bourbaki Lie IV–VI, but the exact draft was not identified. Do not assign its claims to Grothendieck solely because it lies in his papers. |
| Group-varieties editorial sheet | Scan9, source22, “Variétés de groupe,” “Tribu n°62,” references3-13 through3-19 | Its questions concern exposition and placement; several missing definitions are essential. |
| Graded-algebra fragment | Scan11, separate earlier proposition assumed | The polynomial reconstruction is checkable, but the missing Proposition1 cannot be supplied from the root-system context. |
| English category-valued sheaves | Source pages34,38,39,40 occur at scans41,43,45,39 | Reorder these for reading; source pages35–37 and ChapterI are absent. A Gray mimeograph is a strong lead, not a proved attribution. |
| EGA draft | Scan47, whole sheet crossed, IV-1007, §19.6, quotient changed to filtered | Publication-family identification is sound; missing conditionsb,c remain unidentified. Cancellation does not prove mathematical retraction. |

The actual note-to-source comparisons are in `items.json`. The source-order coverage map is `SOURCE_COVERAGE.tsv`; the full-read log is `READ_LOG.tsv`.

## 2. What the earlier notes got right and what changed

The earlier notes are generally careful about cancelled passages, incomplete proofs, support conventions, and the danger of importing unrelated project results. They correctly isolate the quasi-finite degree-zero problem, the support-properness question, the geometric-fibre issue for trace, the ordered Cartan-integer obstruction, the exceptional-root sign/dimension alarms, and the false product-of-stalks Hom assertion. Those were checked again against the transcription and, where applicable, by independent calculations.

Five entry verdicts are corrected by this consolidation. Entry4 needs an additional restriction on the literal every-torsion comparison; entry9 needs local constancy separated from free modules; entry17 needs the direction of the primitive-root trivialization checked; entry49’s correct index arithmetic conceals a false partial-duality implication; and entry55 misses an additional E6 quotient-generator error. The unit observation in entry18 and the exponent observation in entry56 remain correct and are merged into their enlarged items. The file has53 kept verdicts,33 merges and5 corrections, totaling91.

There are three distinct levels throughout:

1. **Manuscript evidence:** what the diplomatic transcription actually asserts, cancels or leaves to prove.
2. **Literature evidence:** exact opened statements, with their hypotheses and access limits.
3. **Review reconstruction:** precise modern formulations, independent examples and proposed reading alternatives. These do not decide the ink or the author’s intention.

### 2.1 The nonproper comparison needs a coefficient restriction

Scan6 says that the algebraic-to-classical cohomology comparison holds for every torsion sheaf. Its next sentence changes the relative properness condition to finite type. The exact published statement, [SGA4 XVI4.1](https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf), assumes either properness of the morphism or constructibility of the sheaf. That disjunction matters even in degree0.

Here is the independent test recorded in CL-SA12-607. Let X=A¹_C, let Λ=Fℓ, and let i_m be the closed point m for each integer m. Put F=⊕_{m∈Z}i_{m*}Λ in the algebraic étale topos. The sheaf is killed byℓ, and X is smooth affine of finite type. It is not constructible.

On the quasi-compact algebraic site, a section of this direct-sum sheaf uses only finitely many summands. Indeed, it is locally represented by finite sums; a finite subcover suffices to cover X, and the union of the finitely many occurring indices is finite. Thus H0(X,F)=⊕_ZΛ. Analytification is an inverse-image functor and preserves direct sums. The integer set is closed and discrete in C, so an arbitrary value at each integer defines a locally finite section of the analytic sum. Consequently H0(Xan,Fan)=∏_ZΛ. The comparison is the proper inclusion of the direct sum into the product.

This refutes the unrestricted literal quantifier. It does not refute the constructible comparison theorem, and an inherited convention might already restrict the intended coefficients. That convention or the ink must be checked. This example is distinct from the earlier run’s exponential-graph example: the latter concerns a proposed equivalence with analytically constructible sheaves using arbitrary analytic strata. Both examples are useful, but they address different assertions.

### 2.2 Proper smooth local constancy does not imply freeness

The scan10 formulation uses locally free. The established proper smooth conclusion is finite local constancy; see [SGA4 XVI2.1–2.2](https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf) and [Milne20.2](https://www.jmilne.org/math/CourseNotes/LEC.pdf). If the source means free modules over a chosen Z/n, it is stronger and false.

Take a smooth proper complex elliptic curve and the rank-one Z/4 local system whose monodromy along one generator is multiplication by−1 and whose other generator acts trivially. This finite representation is algebraizable by the Riemann-existence comparison. Its H0 consists of x with−x=x, namely{0,2}. That two-element module is not free over Z/4. The structural morphism to Spec C is smooth and proper,4 is invertible, and the coefficient sheaf is locally free of rank one. The conclusion is still locally constant, since the base is a point. The invariant calculation is saved in the exact output. This is a correction of the coefficient interpretation, not evidence that proper smooth local constancy fails.

### 2.3 The all-degree duality statement is stronger than a field-only formulation

Scan48 passes from compact-support cohomology to ordinary cohomology of the dual. Both displayed right-hand shrieks are cancelled, while one shriek survives in the parenthetical sentence. The coefficient sheaf on the base is written with a source suffixX. Those are separate scan alarms.

An earlier finite-ring caution needs refinement: projectivity of all locally constant stalks is **not** required merely to dualize into Λ=Z/n. This ring is injective as a module over itself. The fact is explicitly used in [SGA4 XVIII3.2.6](https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf). A short independent proof uses [Baer’s criterion, Stacks05NU](https://stacks.math.columbia.edu/tag/05NU): an ideal of Z/n has the form(d), with d dividing n. If a homomorphism sends d to a, the relation(n/d)a=0 forces a=db for some b in Z/n. Multiplication byb on the whole ring extends the homomorphism.

For a finite locally constant sheaf M of Λ-modules, this calculation applies étale locally, so internal higher Ext from M intoΛ vanishes. If **all** cohomology sheaves of K=Rf!F are finite locally constant, the internal hyper-Ext spectral sequence collapses to the ordinary module duals in reversed degrees. Combined with smooth duality and the orientation twist, this yields the all-degree conclusion of CL-SA12-651. Requiring free stalks would lose valid cases and would not accurately reflect the published argument.

### 2.4 The partial-range extrapolation is false

The last sentence of scan48 claims that local constancy only for compact-support degrees i≤i0 suffices for the corresponding ordinary degrees j≥2d−i0. The reversal of inequalities is correct arithmetic. The asserted transfer of local constancy is not a valid consequence of duality.

The independent counterexample in CL-SA12-678 uses

\[
S=\mathbf A^1_{\mathbf C},\qquad
X=\mathbf G_m\times\mathbf A^1_{\mathbf C},\qquad
f(u,v)=u.
\]

Let j:G_m→A¹ be the open immersion, p:X→G_m the projection, i:{0}→A¹, and F=Λ=Fℓ for any primeℓ. Then f=jp. The morphism is separated, of finite type, smooth of pure relative dimensiond=1, and compactifiable: X is an open subscheme of P¹×A¹ over the base A¹. Every coefficient requirement in the source is met; F is constant and free of rank one. The source imposes no surjectivity hypothesis.

The relative affine line has ordinary cohomology Λ in degree0 and compact-support cohomology Λ(−1) in degree2. These statements follow, for example, from the constructible complex comparison and the P¹ localization/trace normalization. For the product projection they give Rp_*Λ=Λ and Rp!Λ=Λ(−1)[−2]. Composition therefore gives

\[
Rf_!\Lambda=j_!\Lambda(-1)[-2],\qquad
Rf_*\Lambda=Rj_*\Lambda.
\]

Thus R0f!Λ and R1f!Λ are both zero and hence locally constant. For the punctured line, the exact regular-divisor computation in [Riou XVI3.1.3](https://www.cmls.polytechnique.fr/perso/orgogozo/travaux_de_Gabber/16-classes-de-Chern/gysin.pdf) gives

\[
j_*\Lambda=\Lambda,\qquad
R^1j_*\Lambda=i_*\Lambda(-1),\qquad
R^qj_*\Lambda=0\quad(q\ge2).
\]

Taking i0=1, the proposed range begins at2d−i0=1. But R1f_*Λ(1)=i_*Λ is a nonzero skyscraper at0 and is not locally constant onA¹. This is the required failure inside the claimed range. The compact-support sheaf in degree2 is j!Λ(−1), which is not locally constant; the all-degree hypothesis is therefore correctly absent.

Even adding surjectivity would not repair the implication: take the disjoint union with the projection A¹×A¹→A¹. Both lower compact-support degrees still vanish, the map is smooth pure-dimensional and surjective, and the ordinary degree-one skyscraper remains. This variant is unnecessary for the stated hypotheses but checks that the empty fibre is not the sole issue.

The code checks the degree bookkeeping; it does not pretend to compute an étale topos numerically. The geometric argument and its cited inputs are the substantive proof. A corrected partial criterion is a new research direction in `directions.md`, not an authorial open question invented for `problems.json`.

## 3. Fundamental classes, supports and trace

The class programme is a coherent developing argument. Scan12 asks for a local fundamental class; scans22–24 construct the divisor class from a regular equation and Kummer, then multiply divisor classes for a regular sequence. Independence of the equations is asserted, not proved. Scan26 lists base change, product and coefficient compatibility; scan28 uses low local-cohomology vanishing to extract a global supported class. The explicit edge-map deduction is correct: in the first-quadrant support spectral sequence, all entries below total degree2d vanish and only(0,2d) survives in degree2d. The Kummer class maps to zero in the following Gm cohomology group by exactness.

The modern matches are [SGA4 XVIII](https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf) and [Riou XVI2.3/2.5.13](https://www.cmls.polytechnique.fr/perso/orgogozo/travaux_de_Gabber/16-classes-de-Chern/gysin.pdf). Their admissibility and regularity hypotheses matter. A pullback can destroy a regular equation; a product formula without excess is not an arbitrary-intersection formula. Finite-level compatibility in n produces a compatible ℓ-adic system, but the single sentence does not settle derived inverse-limit issues.

The proper-support map requires support proper over the base. If X=Y=A¹ over an algebraically closed field, H0_Y(X,Λ)=Λ whereas H_c^0(X,Λ)=0. The properness clause on scan28 may already supply the intended hypothesis for the later construction, so the example is a scope test rather than an accusation of an authorial error.

The trace is normalized by base change, transitivity, the identity map and the P¹ Kummer class. The point-class basis statement is explicitly promised as a consequence of a forthcoming theorem. The isomorphism criterion for trace requires geometric connectedness. Spec C→Spec R is finite étale, smooth and proper of relative dimension0, with a connected nonempty ordinary scheme fibre. Its geometric fibre has two points, and the F3 trace is summationF3²→F3 with a nonzero kernel. [SGA4 XVIII2.10.1](https://pi.math.cornell.edu/~dkmiller/bin/sga4-3.pdf) uses the geometric-fibre condition. The source may have a convention making this implicit; the mathematical dependence is nevertheless real.

Two local reading details also matter. A regular equation defines a codimension-one immersion, not relative dimension+1. The global class labelledγ_{X/Y} in a group supported onY insideX appears to reverse the established indices. Neither is silently corrected here.

## 4. Exceptional-root and reused-source checks

The exact program reconstructs the exceptional simple-root data from the supplied coordinate tables and independently checks lattice/root membership, dual pairings and reflections. It verifies the listed root counts72,126,240; Coxeter numbers12,18,30; determinants3,2,1; highest-root heights11,17,29; nonorthogonal-root counts42,66,114; the displayed fundamental weights andρ; and the arithmetic of the Weyl-order factors. It does not enumerate all696729600 elements of the E8 Weyl group.

### The additional E6 quotient-generator error

Write v=ε8−ε7−ε6 in the supplied realization. Scan23 proposes μ=v/3 as a weight-lattice quotient generator and says3μ belongs to the root lattice. In the supplied simple-root basis,

\[
\mu=(2/3,1/2,5/6,1,2/3,1/3),\qquad
3\mu=(2,3/2,5/2,3,2,1).
\]

The latter coordinates are not integral; moreover μ has simple-coroot pairing1/2 withα1, so it is not even a weight. The supplied first fundamental weight is2v/3. Its triple is in the root lattice and it is itself not in that lattice, giving a coherent order-three candidate. The quotient index3 is independently confirmed by the Cartan determinant. This does not prove that a factor2 was visible in the original ink: it states exactly which candidate the mathematics supports.

The separate exponent error is also real. A factor12+1 cannot divide51840, since the remainder modulo13 is9. Replacing that factor by11+1 makes the remaining equations yield4 and8. Other alarms include E7’s ε6-versus-ε8 branch, E8’s−1 versus+1 highest-root pairing, and E8’s printed R4 versus rank8. The A_l endpoint-pairing formula also needs its l=1 exception: that pairing is2 when the two endpoints coincide.

The ordered-Cartan issue is not an arithmetic typo in a table. In B2, choosing u long and v short gives n(u,v)=−1 but n(v,u)=−2, length ratio1/√2 and reflection-product order4. One ordered entry alone cannot imply equal lengths and order3. Likewise{±e1,±2e2} is a valid reduced crystallographic root system whose two orthogonal components have length ratio2. A single minimum-length normalization needs irreducibility or independent component normalization. The linear root-system classification can still be correct while an intermediate one-scalar Euclidean proof needs qualification.

The historical classification is already present in [Coxeter1934, Theorem9 and §9](https://sites.math.washington.edu/~billey/classes/reflection.groups/references/Coxeter.1934.pdf), received16June1933 and publishedJuly1934. Bourbaki’s official bibliography confirms the1968 publication of Lie IV–VI; the opened publisher records do not identify n°391 or collate its tables. These different levels of verification remain explicit.

### The English Hom assertion

The product-of-stalks construction itself is a sheaf, and a sheaf embeds into it by its germs. Faithfulness and left exactness are valid in ordinary module categories. The asserted equality of all Hom sets with a product of stalkwise Hom sets is stronger and fails.

Use the Sierpinski space with opens∅,{1},{0,1} and coefficientsF2. For a constant rank-one sheafF, PF has global sectionsF2², sectionsF2 on{1}, and restriction the second-coordinate projection. An endomorphism consists of a matrixA onF2² and a scalarb onF2 satisfyingπ2A=bπ2. Its lower-left entry is zero, leaving three free entries: there are8 endomorphisms. Independent endomorphisms of the two original stalks give only the4 diagonal matrices. The map(s,t)↦(t,0) is an explicit extra sheaf morphism. The proposed inverse in the fragment extracts a different diagonal map, so the inverse calculation itself fails.

The earlier run’s example is independently enumerated in the exact code. The missing ChapterI might impose a special category, but vector spaces satisfy the ordinary completeness/exactness assumptions suggested by the fragment. [Kleisli–Wu1964](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0008439500052309) names the right-perfect/enough-small-objects setting and cites Gray’s Columbia mimeograph. This supplies a source lead, not a license to invent a rescuing hypothesis. Gray’s1965 primary article was not successfully opened.

### The filtered-module fragment

The distinct filtrations on scan47 must not be conflated. For A=k[t], R=tA, N0=A and Nk=0 for k>0, with J=tA, one obtains N′_k=t^kA, R′_k=t^{max(1,k)}A, and R″_k=t^{k+1}A. They differ already at k=1. Exactness of the associated graded rows follows from using the induced and quotient filtrations; the polynomial mapψ is surjective because each enlarged-filtration term is generated by the indicated powers ofJ.

That verified calculation says nothing about the preceding unidentified b⇒c question. The official [EGA IV4 publication record](https://www.numdam.org/item/PMIHES_1967__32__5_0/) was opened; the large primary PDF could not be retrieved through the available open operation. The unknown implication remains classF, with the access limitation stated rather than filled from familiar regular-sequence terminology.

## 5. Fate of the authorial problems

The22-record problem index includes explicit hopes, proof requests, deferred exposition and editorial uncertainties. It does not turn every theorem lacking a proof into a surviving research problem. In particular:

| Programme or problem | Exact modern status established by the review |
|---|---|
| Proper/smooth base change and strict-local stalks | Established with the separate torsion/invertibility hypotheses; opened Stacks095T,0EYU,03Q9 and SGA4 statements. |
| Relative analytic comparison and local-ring continuity | Algebraic-base specialization established; exact analytic-base category/formulation not identified. ClassF/C records are limits of identification, not claims of an open theorem. |
| Absolute purity | Settled by Gabber in the regular invertible-torsion setting; exact Riou3.1.1 opened. The2002 Fujiwara article is real but its primary text was not opened. |
| Normal crossings | Riou3.1.3–3.1.4 gives the divisor and exterior-algebra formulas; no blanket one-stratum purity assertion is substituted. |
| Nonproper finiteness | ILO XIII1.1.1 proves constructibility and eventual vanishing over a noetherian quasi-excellent base with invertible coefficients. |
| Local/global Gysin and trace | Established in SGA4 XVIII/Riou; source normalization and overwritten diagram remain critical-edition tasks. |
| Flat resolutions | Classical bounded construction has a modern unbounded K-flat formulation in Stacks06YV; these are not retrospectively identical expositions. |
| Coxeter realization and lattice-shell checks | Classical established mathematics plus exact checks here; the source’s deferrals are exposition order. |
| Hyperalgebra placement and formal-point sorites | Editorial problem and missing topological-category definitions; no unrestricted quotient surjectivity inferred. |
| EGA b⇒c | Unidentifiable until the absent antecedents are recovered. |

Dates are not collapsed. SGA4’s1963–1964 seminar differs from1972–1973 publication. Hartshorne’s1967 book explicitly reports the Harvard1961 seminar. The Gabber collection reflects seminars2006–2008, first arXiv posting16July2012 and publication2014; Riou distinguishes an earlier2002 exposition from Gabber’s new proof announced2005. Hansen’s opened rigid-comparison version is the24August2017 arXiv v1, not an unexamined substitution of the differently titled2020 journal revision. The source-backed historical explanation for the purity/finiteness delay is the resolution-of-singularities limitation discussed in SGA4 XVI3.10 and XIX’s introduction. No unsupported psychological or editorial explanation is supplied for other omissions.

## 6. Search, verification and links

Every one of the79 claim families has a nonempty mapping to actual saved search calls in `CLAIM_SEARCH_MAP.json`. `SEARCH_LOG.md` gives every exact call, `SEARCH_CALLS.tsv` indexes operations, `SEARCH_RESULTS.tsv` distinguishes search hits, returned pages and failed access, and `outputs/web_01.json` onward retain full returns. Searches include the requested mathematical source families, bibliographies and backwards references. Failed searches did not produce any classD verdict. The eight classF records include mathematically refuted literal assertions whose exact published/source formulation remains unidentified; the class describes bibliographic fate, not correctness.

The bibliography’s `verified` flag means an actual linked page was opened. It is refined by `annote` and `REFERENCE_ACCESS.json`: some references have exact theorem text inspected, some only official metadata, and some only a targeted excerpt. Fujiwara2002 and Gray1965 remain `unverified`. Reading a theorem statement is recorded as source/hypothesis comparison, not independent proof. The229 original check events grew to231 with the final ordinary-Leray coverage/reference entry; `CHECK_EVENTS.tsv` is the authoritative count and identifies source comparisons, independent proofs, exact computations, narrow proof checks and literal refutations separately.

Stage5 has29 checked local/published comparisons and133 quarantined earlier-run records:53 register rows and80 individual context-comparison paragraphs, retained with their exact note ids and locators. These may repeat a target for different reasons; that is deliberate provenance. The current note and associated source passage were read. The external context files and target projects are absent from the attachment, so their proofs and reported statuses were not checked or promoted. In particular the broad étale, lattice or Lefschetz vocabulary here does not solve LM4/LM7/WG questions. Cross-package comparisons within the supplied cote29/31 material are to be added only when both actual passages have been read.

## 7. Deliverable counts and completion

| Record | Count |
|---|---:|
| Indexed source entries, all with read verdicts | 91 |
| Consolidated items | 57 |
| Kept / merged / corrected entry verdicts | 53 / 33 / 5 |
| Claim families | 79 |
| Claim classes A / B / C / D / E / F | 47 / 13 / 3 / 0 / 8 / 8 |
| Explicit problems/deferred steps | 22 |
| Mathematical scan alarms | 46 |
| Local/published links | 29 |
| Quarantined project/register/context records | 133 |
| Ranked directions | 8 |
| Bibliographic records | 37 |
| Saved web calls at core completion | 36 |

`COUNTS.json` provides exact machine counts, including detailed source-status wording. All source claims have searched fates; uncertainty in an unidentified antecedent or inaccessible target is an explicit substantive result, not an unperformed verdict. The exact calculations completed successfully. The source text, earlier-run ideas and this review’s new examples remain separately attributed. No claim is made that unavailable ink or absent external project documents have been inspected.
