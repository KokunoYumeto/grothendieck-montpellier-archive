# Root audit of A.131: complete effective concordance models

Date: 19 November 2026, after checkpoint 10. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); inherited effort configuration, numeric effort not exposed; root run RESEARCH_SA20. No priority claim.

## Decision and exact scope

**PASS.** We accept A.131 as an explicit whole-space computation in the precise form of a countable effective simplicial group, and as complete recursive presentations of every homotopy group. The input is a finite ordered abstract complex promised to realize a closed PL manifold. No manifold-recognition algorithm is assumed. The output is substantially more explicit than a definition indexed by arbitrary homeomorphisms: valid finite integer codes and equality are decidable, every structure operation is a total algorithm, and all generators and relations are enumerated by specified finite algebraic procedures.

This resolves the previously separate *effective full PL/semialgebraic model* gate, including unstable dimensions. It does not evaluate those presentations into finite classical invariants or decide every isotopy question. We retain the higher PL-to-SA and arbitrary o-minimal comparison gate, and the real low-dimensional PL-to-TOP comparison gate. We do not mark the whole original A.1(b) task complete.

The previous E(K) component presentations remain useful structural descriptions. A.131 neither invalidates nor needs a backdated change to the earlier review decisions. The new reduction is counted only after the present full audit and integration.

## Complete mathematical audit

1. **Effective coefficient field.** A nonzero integer polynomial and rational isolating interval are finite data for one real algebraic root. Sturm counting validates the interval. Operations and signs reduce to real-closed-field sentences with uniquely specified root variables. Enumeration for an output root code terminates because the algebraic numbers form a field. The proof never invokes arbitrary real-number computation or a rational realization of a merely algebraic configuration.

2. **PL validity.** A finite union of closed graph simplices has a linear membership formula. Both projections being bijective implies injectivity on every simplex and its affine hull; hence each inverse restriction is affine. Finite closed-cover gluing supplies continuity over any ordered field without ordinary topological compactness. The projected simplices admit a common polyhedral subdivision over the coefficient field. The repaired text explicitly uses affine-hull equations as well as extensions of facet hyperplanes, so lower-dimensional projected simplices in different spans are covered. The bottom and top clauses are separately imposed.

3. **Exact operations and canonical codes.** Inversion swaps coordinates. Composition quantifies over the intermediate point with the same parameter. Face and degeneracy operators pull back along the standard affine simplex maps. Every resulting graph has a finite PL code by common refinement, so search for its least valid equal code terminates. Length-lexicographic order has finitely many predecessors of each word; deciding that a valid code is canonical is therefore a finite test. Equality is equality of complete graphs, not equality on sample points. These constructions establish strict simplicial and group identities.

4. **Semialgebraic validity.** The test includes joint continuity of the total map and total inverse. They are finite epsilon-delta field sentences, with the parameter included in the source metric. Quantifier elimination decides them. This is stronger than checking each individual fibre map, and the proof does not confuse the two notions. Polynomial formulas, projection and canonicalization give the computable PL-to-SA simplicial homomorphism.

5. **Whole field-independent spaces.** We reread A.115 and A.116, including their previously checked source inputs. A.115 cones on the *total product cell*: the unchanged parameter on the boundary makes the coned parameter unchanged by the displayed affine identity. It does not interpolate arbitrary vertex coordinates and silently produce bilinear maps. A simultaneous subdivision of a one-way chain yields the matched source, target and parameter complexes. Cell-preserving corrections and the common-boundary extension give the required relative PL isotopy. A.116 partitions a coefficient space by Hardt triviality of the graph projection. The graph fibre is definably compact; this makes the continuous bijection to the product a homeomorphism. It yields joint evaluation and joint inverse evaluation on each coefficient cell. A path within that cell then descends an entire parameter family. Both injectivity arguments transfer the exact prescribed boundary formula. These are the comparisons needed by A.131, not a mere existence comparison for individual maps.

6. **CW data.** Degeneracy is detected by testing the finite list of equations `a = s_i d_i a`. Faces and their canonical codes are computable. The nondegenerate simplices and these attachments determine the entire realization, with its higher homotopy data. The claim is an effective countable CW model, not effective homology with finite reductions.

7. **Moore quotient, including degree zero.** We checked all face indices in the first-face convention. For `N_(r+1) = intersection_(i=1..r+1) ker d_i`, `d_0 N_(r+1)` lies in the cycles and is normal, by conjugation with `s_0 a`. An elementary homotopy with first two faces x and y is converted to a Moore element by `z (s_0 y)^(-1)`. The reverse construction is exact. Degree zero uses the same edge calculation and Kan horn filling to compose paths. The degreewise product gives the homotopy-group law. For positive degree the quotient is abelian, including degree one.

8. **Entire presentations, not a subgroup calculation.** The multiplication-table relations present the complete decidable cycle group. The last relator family kills exactly the normal subgroup of Moore boundaries. Every boundary is enumerated by its finite filler code. Negative boundary membership is not asserted decidable. The abelian relation matrix presents the same group because the quotient has already been proved abelian. Translation accounts for other components.

9. **Comparison scope.** The definable component identification is A.113. In the live text A.113 also explicitly proves real PL-to-TOP weak equivalence when every base component has dimension at least five; A.114 uses it. Thus the draft's A.113 cross-reference is correct. There is no literal map from arbitrary non-Archimedean real points to the real TOP space. The field comparisons and singular-complex comparison provide the stated zigzag. No inference of a PL-to-SA weak equivalence is made.

## Opened originals and exact locators

We opened the actual full text of Basu, Pollack and Roy, *Algorithms in Real Algebraic Geometry*, online edition dated 26 June 2016, through the Academia full-book copy at <https://www.academia.edu/98168062/Algorithms_in_Real_Algebraic_Geometry>. We checked Theorem 2.62, printed p. 62 (root counting), Theorem 2.94, p. 80 (quantifier elimination), and Algorithm 14.21 with its correctness and Theorem 14.22, pp. 591–593 (effective elimination). The institutional URL timed out and is not represented as the opened copy. Root web records: turn234779768view0, turn738975497view0; the earlier original opening is turn357414463view0. The source is used for these standard algorithmic inputs, not as an attribution for the new concordance-code construction.

We downloaded May's original *Simplicial Objects in Algebraic Topology* scan from <https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/May-simp-ocr.pdf>, extracted the relevant text, and **explicitly viewed the actual rendered spreads** with printed pp. 64–65, 66–67 and 68–69. Theorem 16.6, p. 65 supplies realization comparison; Theorem 17.1, pp. 67–68 supplies Kan filling; Proposition 17.2, p. 68 supplies the group product; the first Proposition 17.3, p. 68 says abelian for q ≥ 1; the second Proposition 17.3, pp. 68–69 supplies the Moore normal subgroup; Proposition 17.4, p. 69 gives the full homotopy quotient. The duplicate numbering and the ≥ sign were visually checked, not inferred from damaged OCR. The first-face conversion is proved in A.131. Root original opening: turn386748217view0. Local original and audit images are in `source_external`, outside the research deliverable tree.

## Finite certificate and limits

We read the full 418-line independent checker and reran it:

- Program: `agents/tensor_and_finite/code/check_A131_pl_codes.py`.
- Root output: `logs/root_A131_pl_codes.json`.
- **30 checks passed; elapsed 0.778375 seconds.**
- Exact `Fraction` arithmetic throughout; B is a point and parameter dimensions are 0, 1 and 2.
- The nonidentity one-parameter graph has four triangles, its square ten, and its stellar subdivision twelve. The genuine two-parameter graph has eleven tetrahedra, with all faces equal to the identity. The checker constructs actual intersection refinements for products and affine inverse images for simplicial operators.
- Both inverse identities, graph equality under subdivision and the simplicial identities in scope pass. Five invalid graphs are rejected for explicit failed conditions.

This is a finite implementation check of a substantial rational subclass, not an implementation of general polynomial quantifier elimination and not a computation of nonzero homotopy classes. The proof supplies the general algorithm and the infinite Moore calculation. Earlier agent timings remain distinct in their own logs; we do not replace them by the root timing.
