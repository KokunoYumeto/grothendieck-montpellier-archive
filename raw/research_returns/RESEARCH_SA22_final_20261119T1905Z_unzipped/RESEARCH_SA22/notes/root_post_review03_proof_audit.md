# Root proof review after hourly review3

## A1 raw toric descent

Root read the entire three-statement fragment and Part B's independent coefficient derivation. The cusp form of the Schwarzian is explicitly justified by the parabolic developing coordinate, rather than silently applying a positive-length-only statement at zero. The third cap jet is 5/16+1/[16(lambda²+4)]. The normalized four-point plumbing coefficient is symmetric in the two third jets; the general hand checks include a single changed coordinate and the Möbius special case. The Laurent calculation is made with small fixed node discs, so evaluation at the marked points is legitimate.

The cap collars give honest coordinate discs of radii r exp(delta/(2lambda)), strictly greater than r. Hence the phase circle lies inside the holomorphic plumbing parameter disc. A nonzero cubic coefficient proves that the two cross-ratio functions differ, and only finitely many unit phases can be exceptional. The exact choice N=min{n>=1:Delta(exp(i/n))!=0} exists by the identity theorem at the accumulation point1. This is a fully specified analytic rule; no numeral for N or numerical cross-ratio value is asserted.

The balanced comparator has a geodesic seam. The unequal surface's own seam and its own unique geodesic are thus the two cuts in the same fixed labelled X: equality of their raw tensor would contradict the already proved injectivity of geodesic reconstruction and the cross-ratio difference. This avoids the invalid inference from fixed-target fiber dimension to fixed-X variation. The case uses stable type(0,4), analytic seams, positive radii in(0,4), fixed external labels and the actual tensor phase. Root found no remaining gap after the two local typing clarifications were applied.

## A6 source and proof review

Root separately read the full three-statement mixed-characteristic/branch-character supplement. The Hoshi author preprint RIMS1558 was reopened directly: Corollary3.9 printedpp31–32 (web lines2451–2478, followed by its proof) and PropositionA.10 printedpp57–58 (lines5201–5329). The latter's definition uses codimension-one boundary valuations, its proof identifies the divisorial log structure, and its essential-surjectivity step invokes log purity. These are the exact hypotheses used in the supplement.

Root checked the valuative comparison between any two existing proper log-regular models, the log morphism from each boundary valuation trait, the tame Galois quotient and uniformizer-framed section, the Q2(sqrt2) constant-cover obstruction, and the nonsplit nodal cubic with branch sign. All are correctly distinguished from full geometric fundamental groups, existence of arbitrary mixed-characteristic regular models and preservation of a strict Isom-anabelian definition. The last issue is being treated as its own explicit relative-Frobenius counterexample, not assumed from the category equivalence.

Source retrieval references for the root reopening: turn824068644view0; turn751185945view0 and turn751185945view1. This note records source access and proof review, not a claim to have checked the entire Hoshi paper. Literature search metadata is in `code/root_a6_scope_literature_search.json`; related Kerz–Schmidt work was identified but not added as an unopened proof premise.


## Strict anabelian preservation under specialization

Root read the completed fourth proposition and the20-assertion F16 output, then reopened Stacks Proposition58.8.4, Tag0BQN, including its proof (turn551278569view0). The map is relative Frobenius over k, fixing constants and sending w to z²; it is a finite radicial surjection, so the category equivalence commutes with G_k augmentation. The irreducible quartic is T⁴+T+1. The six computed crossratio values exclude a²; the proof also excludes them uniformly by the degree≤3 equations they would imply. The primitive order15 element gives the stated prime of Z[zeta15] over2 with residue F16, and the separable reduction of T¹⁵−1 proves the unramified DVR/lift claim. Both four-point complements lift with disjoint sections. The conclusion refutes preservation of the same strict Isom-anabelian definition; it does not deny formulations which explicitly allow Frobenius ambiguity.

The21 rational/integer assertions and20 finite-field assertions check the advertised counterexample data only. The actual local Kummer, log-category, valuation, stability and source-theorem deductions remain written proofs, not claims that a script verified those theorems. No certificate was rerun by root.
