# Independent audit of the axiom comparison

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), 19 November 2026. Auditor: /root/bmodels. Targets: parts/axioms/axioms.tex and its finite certificates. No edits were made to those targets.

## Priority results

- SA21-B-C6-C8: proof passes under the explicitly stated literal C6(a). Applying uniqueness to H subdividing F and the whole subfigure F permits both H and F when F is incident below H. The derived refinement's transitivity and antisymmetry then follow from C7_0 exactly as written. The weaker uniqueness among candidates satisfying an extra formula would not justify this argument; the text separates that reading.
- SA21-B-C-carriers: six figures with common bottom d pass. Restriction for da subdividing dyz takes dy,dz,dyz all to da, uniquely, and preserves joins. Every C7_0 extension is enumerated. The elementary object a refines both y and z but not d, so no least carrier exists in dyz. The distinct final C8 gluing fails on the matching da/dz data, as explicitly stated.
- SA21-B-Cont-counter: the five-object model has nonempty open lieu sets and independent compatibility precisely on pq,qz,zt. Incidence is compatible refinement; all principal families are clique downsets. Only the pq,qz pairs are nonzero disjoint, and their refinements remain so. Internal refinement fails exactly at p rho u rho t but not p rho t. This checks the need to add transitivity even after Cont6 and Cond7.
- SA21-B-Sigma-counter: the seven objects give 21 figures, and the extra compatibility restriction removes precisely the two-point common-deployment obstruction. The parents k≤x and refinements k,x-prime have compatible restrictions k,{a,b}, but their common deployment {a,b} has no greatest element. Disjointness detection, AtD and matching gluing remain valid. The finite code checks these quantifiers over all figures.
- SA21-B-extension-unique: the two-object incidence-discrete refinement chain has one lieu, no nonzero figure disjointness, and both objects subdivide x. For empty boundary both deployment squares satisfy even the literal mixed clause, so diagram uniqueness does not imply object uniqueness. All six extension and twelve gluing diagrams pass.
- SA21-B-deployment-unique: the poset disjoint union with the prescribed interior/exterior relation is uniquely determined. There are no reverse mixed pairs because the interior is a downset, and all transitivity cases reduce to monotonicity or the original orders.

## Broader proof audit

The prime representation criterion, the repaired strong primed equivalence, the weak-comparable and weak-divisibility counterexamples, the local MogL2 equivalence, the gluing/D0-not-D example, and the AtFil restricted-atlas example pass. The At9-Sigma gate proof correctly separates the automatic exterior-lieu condition from membership of the intersection deployment in Sigma. The corrected At-star representation passes when canonical subfigure membership is retained; the membership-free two-point counterexample passes under the stated ambient-relation typing. The modern-to-subdivision bridge explicitly assumes the relative calculus needed to identify subdivisions with maximal refinements. The exact global incidence-component classification and the single-figure component argument pass for infinite as well as finite underlying sets.

One minor exposition improvement was sent to the author: in the proof L3+CL(spac) implies C, explicitly reduce arbitrary figure refinements to elementary strata before applying the elementary compatibility criterion. The equivalence is already stated earlier, so this is not a mathematical gap.

## Original manuscript verification

Fetched the full official 156-4.pdf (37,603,160 bytes, 89 PDF pages) from https://grothendieck.umontpellier.fr/156-4.pdf. Independently inspected the images, not just transcriptions:

- PDF page54, manuscript/printed53: the final definition says F=Sup_i F_i implies some F_i=F. It is join irreducibility, not join primality.
- PDF page55, manuscript/printed54: the corollary explicitly asserts that the deployment transforms Sup into union.
- PDF page72, manuscript/printed71: C6(a) says there exists a unique H in the figure poset satisfying the incidence/subdivision square. Its separate marginal (b) gives the stratum formula; the main uniqueness sentence has no restriction to candidates satisfying (b).
- PDF page73, manuscript/printed72: C7_0 extension is separately stated.

Full source files and images are excluded from the deliverable tree, at SA21_sources/bmodels/. The high-resolution crop is 156-4-scan72-bottom.png. This source inspection supports the text's distinction between literal C6(a) and an intended qualified uniqueness reading.

## Independent certificate reruns

All four programs exited with code0. Captured output is in AXIOMS_CERTIFICATE_RERUN.txt. Scope is the stated finite models; general theorem proofs were checked separately.

- legacy_subdivision.py: C1–C4, prime generation, C5, literal C6(a,b,c), C7_0 and C8_0 pass; least carrier and final full C8 fail as claimed.
- literal_systems.py: M3, missing At-star membership, missing internal transitivity and final Cont counterexample pass.
- finite_axioms.py: seven-object core, At8–10, At9-Sigma, AtD and matching finite gluing pass; At12 fails with the displayed witness.
- core_models.py: all claimed positive clauses and all displayed failures pass, including extension uniqueness and the 26 gluing assignments for the D0-not-D model.


## Final spatial separations

SA21-B-spatial-separations passes. In the tiny two-object local model, empty internal orthogonality gives cl{a}=cl{x}=M. Both elementary deployments are one-label families with that same top label, so Atspat3 injectivity fails despite the local and extension hypotheses. Conversely, with incidence a<t, rho identity and internal disjunction unequal, the singleton supports are {a} and {t}. The principal labelled deployments are respectively the one-element family and the two-element ordered orthogonal family, so their map is injective into the typed spatial target. Support containment reconstructs rho as identity. Full refinement is incidence; a is the only lieu and the open-lieu set of t is empty. Thus typed spatial Atspat1–3 do not imply divisibility.

## Final source-history qualification:156-6 versus156-4 and156-8

The earlier audit of M3 as a literal core counterexample must be read with the explicit equality-based definition. Original156-6(1.20), supplied J156-6-02 lines77–84, defines multistrates by bounded-join primality and excludes M3. Its deployment-union consequence and SA21-R6-12 are valid. The axioms agent visually checked scan12. In contrast, the independent156-8 atlas list at J156-8-03 lines108–112 explicitly defines elementary figures by equality irreducibility again, so the M3 counterexample to that list remains valid. The corrected At-star theorem uses the already prime156-6 source convention, with canonical-subfigure membership still required. All old bmodels refutation events forR6-12 are marked superseded.
