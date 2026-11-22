# Independent whole-proof review of K-015

Reviewer: `/root/plethysm_proof`; GPT-6 Astra Pro; effort setting not exposed. Date: 2026-11-21 UTC.

**Result: PASS.** I read the complete `branches/kronecker/LIE_EXTENSION.tex`, reread the full K-006 character-lattice doubling proof, and checked the application against the already independently reviewed K-013 criterion. The rank-73 certificate for the n=5 seed remains an explicit finite input, independently checked by root.

## Infinitesimal extension lemma

For an old index a different from i, the coefficient at (a,N,N) can arise only from applying the old-to-new block u_A to the all-new edge. The other replacement edges can contribute there only when a=i. Thus u_A is supported at i, and cyclically in the other modes. For a≠i and b≠j, the coefficient at (a,b,N) comes solely from v_C applied to old support edges. Freeness gives at most one summand for the fixed pair (a,b), while pair-deletion coverage supplies such a pair for every c. Therefore every coordinate of v_C vanishes, and likewise v_A,v_B. The remaining (i,N,N) equations then force the last possible u-coordinates to vanish.

The block-diagonal equations are correctly separated by the number and positions of new indices. The old block fixes T with the selected edge deleted. The third-new block forces Ae_i and Be_j to lie in their indicated lines, and the cyclic blocks do the same for Ce_k. The four scalar equations give 2(a+b+c)=0, hence a+b+c=0 over characteristic zero. The old matrices consequently fix the deleted edge as well, so the original rigidity assumption makes them scalar. The new diagonal entries then equal those old scalars. This proves the lemma without a hidden nondegeneracy or invertible-slice assumption.

## Induction for the explicit family

The four replacement edges preserve freeness. In a linear relation among incidence columns, the new coordinate rows force the three one-new coefficients to equal q and the diagonal coefficient to equal −q. The old rows then give an old relation with coefficient 2q on the deleted edge. Old column independence forces q=0 and then all other coefficients vanish. Thus the support size and incidence rank remain 3n−2.

The mass replacement r↦(r/2,r/2,r/2,1−r/2) preserves every margin and strict positivity. Since every mass is strictly below one, every coordinate has degree at least two. At a newest diagonal edge, every old coordinate has a surviving all-old edge after deleting the previously chosen edge; the newest coordinate has a one-new edge with both other indices old. This proves the pair-deletion hypothesis at every induction step. The n=5 base, supplied by the exact rank-73 certificate, therefore gives scalar Lie stabilizer for all n≥5, with no parity restriction.

The square-root mass representatives are critical because freeness eliminates all off-diagonal reduced-density entries. Full incidence rank makes the complex diagonal torus transitive on nonzero coefficient assignments, so the coefficient-one tensors are in the same product-linear orbits and are polystable.

The K-006 diagonal character argument also applies at every step. Initially M r=3 is odd on the chosen edge; on the next diagonal edge the new numerator is 2M−Mr, again odd. Replacing the independent lattice relation s=0 by 2s=0 doubles the torsion order, and the determinant character has the new full order. Thus the diagonal stabilizer is S×μ_(2^(n−1)) with faithful determinant character.

## Spectrum and fixed support

The displayed seed weights are distinct and have two-adic valuations at most three; the tail weights have distinct increasing valuations at least four, ending in zero modulo M. There is precisely one antipodal pair in each factor: the old weight 8 and the new zero at n=5, then the last two tail entries for n≥6. No other scalar coincidences or antipodal pairs can occur.

The fixed-support classification covers every possible number of tail entries. The finite seed triples give exactly the nine undeleted seed edges. Cross-factor seed pairs have no sum zero and have only one nonzero sum divisible by sixteen, namely 8+8=16. One tail entry therefore gives exactly the first three replacements. Two tail entries and one seed entry are excluded modulo sixteen. For three tail entries, the least nonzero two-adic valuation must occur twice; the remaining entry is the next tail weight because t_(r+1)=−2t_r. Three equal nonzero tail weights do not sum to zero; the newest all-zero triple does. This gives exactly the recursively constructed support of size 3n−2.

For the K-013 hypothesis, at n=5 the surviving edge 121 meets exactly one paired plane. At n=6 a first replacement edge does so. For n≥7, two entries at zero-based index n−3 and one at index n−2 meet exactly one of the two newest paired planes. Simple spectra make the literal centralizer of the diagonal element equal to its diagonal stabilizer. The scalar Lie result supplies the connected-stabilizer hypothesis. Consequently the previously reviewed K-013 theorem applies for every odd n≥5, giving the full stabilizer claimed in K-015.

The smooth quotient/fixed-curve/density-one consequences are the same checked slice and numerical-semigroup arguments used in K-014. The file correctly leaves the even-dimensional full-stabilizer step to K-016; its all-parity Lie theorem is unconditional. No all-n global Hilbert pole is inferred from a single local curve.
