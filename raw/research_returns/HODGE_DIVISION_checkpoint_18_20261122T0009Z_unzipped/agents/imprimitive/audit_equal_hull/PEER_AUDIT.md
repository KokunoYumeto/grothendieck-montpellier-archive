# Independent whole-proof audit of SF-E828

**Result: PASS.** Final audit time: 2026-11-21 20:29:12 UTC. Checker: /root/imprimitive, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION.

## Frozen input and exact scope

Entire 151-line draft read:
`agents/sixfolds/rm_equal_hull_equivariance_draft.md`,
SHA-256 **d57b98f4adff0567e2ee52c2866ca8d418064f79c815b86b25e14ff149552260**.

This independently checks all new mathematical arguments in E828. I also reread the full relevant E826 torsion/HN and line-block argument, the E827 actual equivariant-block hypotheses and their use in its triangle proof, and the already reviewed unit-sheaf local model. The whole E826/E827 theorems and their BF/S21 source statuses remain prior inputs; this event is not mislabeled as a fresh audit or numerical rerun of all those constructions.

## Independent reasoning

1. **Vanishing for every same-slope source line.** For any line M with the same theta slope as L, set N=L tensor M inverse. Then theta-degree of N is zero. A nonzero section would have either a nonzero effective divisor, contradicting ampleness and degree zero, or be nowhere vanishing and make N trivial. Thus H0(I_S tensor N)=0, including the trivial N case because S is nonempty on connected projective X. On the smooth integral surface, the torsion line has theta-degree
   \[
   (-2D+c_1(N))D^2\theta=-2k^3\int_X\theta^4<0.
   \]
   Its H0 is zero. The unit exact sequence therefore gives Hom(M,U)=0 for **every** such M. This includes M=L and all nontrivial flat twists, and does not use a false converse from restrictions to S.

2. **Intrinsic actual subobjects.** The same effective-divisor argument makes Hom(L_a,L_b)=0 for distinct equal-slope Chern classes, while End(L_a)=C. Therefore Hom(L_a,A)=C^{n_a} and its evaluation image is precisely the displayed line block as an actual subsheaf. The image is independent of all basis choices.

3. **Preservation of the isomorphism type, not merely Chern class.** Apply one given translation/Pic0-tensor functor to a nonzero inclusion L_a into A, then use the given equivariant isomorphism back to A. The resulting line M has the same slope and Chern class as L_a. Every component into U vanishes by item1, so one component into a free line is nonzero. A nonzero map of same-slope lines is an isomorphism (an effective zero divisor must be empty). Distinctness of the displayed Chern classes forces that target to be L_a. Thus the actual isomorphism type is preserved, and the evaluation image is invariant. No individual line linearization is chosen.

4. **Honest averaging under the coherent functors.** If j:P→A is the resulting equivariant inclusion, the action on Hom(A,P) is
   \[
   q\longmapsto\phi^P_g\,T_g(q)\,(\phi^A_g)^{-1}.
   \]
   The coherence isomorphisms for compositions cancel between source and target. This is an honest linear group action even if chosen multiplicity matrices are projective. The identity qj=Id is preserved. Averaging an existing ordinary retraction therefore gives an invariant retraction, not a merely projective splitting.

5. **Complement and underlying unit block.** The kernel of the averaged retraction is an actual invariant coherent subsheaf. In the original decomposition A=U^r⊕P, every retraction is (h,Id), and its kernel is the graph of −h. Hence its ordinary sheaf is U^r. Nonzero Hom(U,L) causes no problem, and the complement is correctly not claimed canonical.

6. **Application boundary.** Torsion and the two-slope HN part remain intrinsic under translations and degree-zero tensoring. Equality of a free class with the hull class changes neither slope nor the rank-one torsionfree semistability argument. The new equivariant splitting supplies exactly the A-block hypotheses of E826/E827; all their remaining Ext/cap assumptions are explicitly retained. No splitting of the middle extension E is inferred.

## Limits and source boundary

The result assumes the ordinary positive factor is the displayed direct sum, and averaging cannot create a retraction for a genuinely nonsplit positive factor. Distinct displayed Chern classes remain part of the theorem. If several distinct flat types with the same Chern class are allowed, this draft correctly does not assert that each is individually invariant. It constructs neither a new action nor a new isogeny and asserts no semiregular seed.

No new external classification theorem, numerical rank premise, or computation is required. The only additional inputs are the given unit exact sequence, positivity of an ample class, and characteristic-zero finite averaging, each used with its stated hypotheses. No mathematical defect or required repair was found.

