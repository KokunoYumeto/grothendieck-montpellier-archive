# A1 global-domain, inverse and quotient audit

Reviewer: GPT-6 Astra Pro, OpenAI, agent part_a567. Date:2026-11-19. This is the requested proof-risk audit after the Fatcat route stopped. No finite mathematical check was rerun. Existing A1 TeX was not edited; the coordinated addition is the separate `sections/part_a567_toric_unequal.tex`.

## Material finding and exact repair

The current equal-length/geodesic graph theorem is sound under its stated hypotheses. The introductory claim that three readings settle the cut definitions, however, omitted a genuine intermediate case: **canonical toric compatibility with unequal paired hyperbolic lengths**. The sentence in `part_a1_cut_choice.tex` allowing “an explicit toric compatibility condition” cannot by itself license the geodesic range theorem. Toric compatibility identifies normalized angles, whereas smooth hyperbolic gluing additionally requires equal circumferences.

This distinction is relevant to the actual manuscript. In `inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex`:

| Exact attached-input lines | Content checked | Consequence |
| --- | --- | --- |
|799–810 (scan074) | Cut first, then use each cut component's own canonical metric and toric boundary structure | It does not state equality of the paired lengths. |
|820–847 (scan075) | Tensor extracted from the pointed-disc antiisomorphism; external admissible discs retained | The tensor only records the product of the two branch radii and the phase. |
|852–896 (scans076–077) | Real-analytic bordered and proposed complex-algebraic unbordered maps, with locally constant stable type | The fixed-graph scope is essential; no cross-stratum compactification claim follows. |
|923–960 (scans078–080) | Freely split mutually polar branch shadows; allow possibly nongeodesic seams and question rescaling independence | This is precisely where unequal paired lengths must be separated from the geodesic section. |
|994–1015 (scans081–082) | Ask about fundamental groups and tangent/étale behavior | These two conclusions differ in the broader toric model: π1 is unchanged, but the tangent kernel has dimensionE. |

I read all these transcription passages. Original scans079,080,081,082 were also rendered from the already fetched official PDF and **visually read**, confirming the nongeodesic qualification, polar rescaling discussion, fixed-type fundamental-group question and tangent/étale question. Physical PDF page numbers equal scan numbers; the PDF's printed footer is one less and archival pencil foliation is two greater in these images. No interpretation of the uncertain notation on081 is needed for the proof.

## Complete counterexample

Let P(r),0<r<4, be the unique canonical two-cusp/one-boundary pant whose capped normalization has node0, external labels1,∞ and cap radiusr at0. This object is fixed exactly by the established one-cap gradient inverse and Koebe endpoint; it is not a numerical approximation. Normalize its cap map f_r by f_r(0)=0,f'_r(0)=r>0.

Glue P(1) to P(1), and separately P(2) to P(1/2), by the same explicit normalized toric rule f_r(e^{iθ})~f_{r'}(e^{-iθ}). Both are analytic cut four-punctured spheres and both yield tensor1 in the fixed branch frames. The four external labels keep the two sides distinct. A cut-preserving conformal isomorphism would preserve the first component's canonical boundary length, but l(1)≠l(2). Therefore the source cut objects are distinct. The second seam cannot be geodesic, because its two cut-component canonical lengths l(2),l(1/2) differ.

This refutes injectivity for actual torically compatible cuts. It does **not** assume that forgetting the cuts yields distinct underlying pointed surfaces, and it must not be advertised as a separate proof that the manuscript's underlying-surface rescaling heuristic always fails.

## Strongest proved replacement in the addition

Write H for all2E node branches and L active external legs. The full logarithmic canonical cap image D_Y in R^H is open and convex by A2. The tensor/shadow map is the linear projection P_* summing the two branch logs at each edge and retaining each external log, together with the tensor phases. Its image is **exactly** the previously proved geodesic support region. One inclusion follows immediately from the component support inequalities applied to P_*^t p; the equal-length inverse gives the reverse inclusion. No closure or missing separation argument is used.

Each fiber in full cap logarithms is the nonempty open convex intersection D_Y∩P_*^{-1}(y), dimensionE. The addition further proves a global real-analytic R^E parametrization by d_e=s_{h+}−s_{h−}, where s_h=(l_h/2π)^2. For prescribed arbitraryd, restrict S to s_{h±}=t_e±d_e/2. On t_e>|d_e|/2 and t_l>0 its Hessian is positive definite; its recession is unchanged; all escaping directions are nonnegative; and every finite boundary face has an inward derivative tending to−∞ from at least one vanishing branch length. Hence every target in the support region has exactly one solution for everyd. The positive Hessian gives joint analytic dependence, including throughd=0.

The resulting map is projection V×R^E→V. It is a submersion with tangent kernelE, whiled=0 is the geodesic section. Scalingd is a fiber-preserving strong deformation retraction. Edge reversal changesd's sign, graph symmetries permute the edge variables, and normalization automorphisms preserve intrinsic lengths. Thus the construction descends equivariantly to the full groupoids/orbifolds, including ineffective isotropy. A coarse fiber may be a finite quotient of R^E; the proof does not call that quotient a smooth vector space. The composite to the unrestricted tensor/shadow target induces π1-isomorphisms by the existing common retract. This settles the broader toric reading's range, tangent and π1 questions without declaring it equivalent to the geodesic source.

The dimension consequence is explicit: the fixed-graph normalization has real dimension6g−6+2n−2|E|; independent caps supply2|E|+|L|length parameters and seams supply|E|phases. The broader toric source therefore has dimension6g−6+2n+|L|+|E|, which exceeds the geodesic/shadow target dimension6g−6+2n+|L| by|E|. For all external ends bordered, this is6g−6+3n+|E|. Thus scan077's stated dimension count is compatible with the geodesic/isotopy model, not the unequal-toric actual-cut model.

For full retained external **disc shapes**, fixed shadows are not sufficient. The exact additional criterion is existence ofd for which the reconstructed external caps equal those prescribed discs. The fiber is that subset ofd-space; no universal R^E-fiber or tangent-submersion claim is transferred to this shape-retaining target. The old geodesic full-shape criterion is exactlyd=0. External-only admissibility remains the separate landing obstruction already proved.

## Remaining all-stable and quotient checks

- A nonzero edge direction survives at least one incidence map; a loop occurs twice at its vertex. Thus both graph Hessian positivity and the shifted-halfedge argument include all self-loops without a missing kernel.
- Stability guarantees every active component is hyperbolic. A component with no active flags contributes no length variables. E=L=∅ is the identity on a one-point radial fiber; it does not require applying the positive-boundary theorem to a closed component.
- The proper-image statement is conditional on at least one active variable. A coordinate unit support vector gives a finite upper log-radius or log-tensor bound. In the unbordered graph theorem this is E≠∅. The zero-complexity(0,3) case and any empty-cut stratum remain distinct from a positive-complexity global refutation.
- For every stable type with3g−3+n>0, the trivalent rational degeneration used in A1-global-refutation exists. The norm17 witness is invariant under flag permutations because swapping the other two normalization points changes the tangent frame by a unit-modulus derivative. It therefore obstructs coarse surjectivity as well as groupoid surjectivity, including unlabelled internal flags and self-nodes.
- On the equal-length model, the full derivative is triangular in normalization, radial and phase coordinates. The claimed tangent isomorphism is real-analytic. No complex-algebraic étaleness is inferred from it.
- Actual toric phases are circles. Fully marked real twists require the explicitly stated Dehn-twist quotient or corresponding lifted phase cover. Omitting this convention would create an independent injectivity failure; the current graph theorem does state it.
- The common tensor-circle retract chooses equal positive lengths, not tangent frames or phase sections. It commutes with component isomorphisms, graph permutations and loop-branch flips. Consequently the homotopy proof applies to orbifold fundamental groups. The statement π1=Z^E is only for the marked fixed-normalization torus before finite automorphism quotient, not the orbifold fiber with nontrivial inertia.
- “Proper image” means a proper subset here, not a claim that the open embedding is a proper map. The manuscript uses locally constant combinatorial type, so no cross-graph or node-smoothing compactification topology is being asserted.

No further surjectivity gap was found in the stated equal-length graph inverse. The new mismatch has been reported to root and repaired in a separate fully proved theorem, not silently absorbed into the old definition.

## Independent review and documentary scope

PartB independently reviewed the new fragment. It caught a compressed converse that said “if a seam is geodesic”: with several cuts this must say **every seam is geodesic**, so all cut components inherit their canonical metrics. That correction is now in the addition; the theorem and one-edge witness are unchanged. The completed independent review found no remaining issue; its exact record and four events are `notes/part_b_unequal_toric_audit.md` and `checks/part_b_unequal_toric_events.tsv`. Root also read the entire draft and approved integration.

The new numbered statements are A1-toric-domain, A1-toric-noninjective and A1-toric-full-discs. Their proofs are analytic and geometric; no finite experiment or numerical certificate was run. The only new program, `code/part_a567_a1_scope_scan_read.py`, rendered4existing scans in0.7716450989973964seconds. Its saved JSON records the exact page numbers and output paths; this is document processing only.
