# Independent whole-proof audit of SF-E827

**Verdict: PASS for the actual equivariant extension and the stated nonzero line-difference settings.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. Actual clock record: **2026-11-21 20:16:14 UTC**. The complete mathematical reading was completed before this timestamp.

The whole 265-line proof `agents/sixfolds/rm_diagonal_yoneda_obstruction_draft.md` was read, including all assertions, boundary maps, multiplicity conventions, invariant statements, applications and source limitations. The final reviewed hash is `abe42293fb48da62436bfe7fafd7ae19a2546a768ad294f6f89ed4ec451f8a27`. The only clarification requested in this audit was to repeat the word **nonzero** in the cross-difference conclusion before E827.10. Opposite slopes already imply it in the application, but the literal qualification is necessary: a zero difference would not satisfy the stated product hypotheses. The author inserted this clarification; no mathematical repair was required.

## 1. A-side diagonal injection

The actual Hom(A,triangle) sequence identifies the kernel of Ext2(A,A) to Ext2(A,E) with the image of Ext1(A,B). Its diagonal line block is exactly the sum over b of e_ab[1] gamma_ba, with ordinary multiplicity-matrix composition. Hypothesis1 puts every coefficient in Z. The selected diagonal space W tensor the identity matrix has zero intersection with this subspace because W intersects Z trivially. Thus the direct sum D_A injects, regardless of other diagonal or off-diagonal components in the boundary image. In particular no assumption that Ext1(A,B) itself vanishes has entered.

There is no hidden path through A0 in this diagonal calculation: the intermediate object in this boundary is B, which contains only the displayed M_b blocks. Projecting the output to L_a removes the A0 target. This is why the stated structure of B matters.

The next actual Hom(-,E) boundary, restricted to i_*D_A, is i[3]d[1]e. Its line-target components are multiplication of e_ab by the selected W class, and its A0 component is zero because d has zero A0 block. Hypothesis2 kills these components. Consequently D_A lies in the actual image I of Ext2(E,E) in Ext2(A,E), not merely in an associated graded space.

## 2. B-side lifts and the preceding boundary

For D_B, the connecting map Ext2(B,B) to Ext3(B,A) is e[2]h. Hypothesis2 kills every line-target component. The explicitly imposed Ext3(M_b,A0)=0 kills the A0 component for each selected b in J. Exactness therefore gives lifts to Ext2(B,E).

The preceding Hom(-,E) boundary from Ext1(A,E), projected to Ext2(B,B), is (p[1]alpha)[1]e. Its b-th diagonal coefficient consists of reverse line-pair products, which lie in Z, and a possible term through A0. Fourfold Serre duality identifies Ext1(A0,M_b) with the dual of Ext3(M_b,A0), so that extra term is indeed zero on selected b. This is an ordinary perfect-Ext duality statement and remains valid with the stated multiplicities.

Taking the b-th diagonal projection and the matrix trace divided by m_b gives exactly the identity coefficient on W tensor I_m. Passing to H2(O_X)/Z kills every projected preceding boundary. The quotient Q consequently has an image containing the direct sum of the selected W spaces. Q injects into Ext2(E,E), whose quotient is I. Their independent contributions give the required dimension sum. No arbitrary splitting of Ext2(E,E) is asserted or needed.

## 3. Equivariance and averaging

The lemma explicitly assumes preservation of the actual extension and the displayed blocks. Under those hypotheses every projection and boundary used above is equivariant. Translations and degree-zero tensor functors act trivially on H2(O_X), and conjugation fixes the identity in each multiplicity matrix algebra, even when choices of individual line linearizations give projective matrices. The normalized trace is conjugation-invariant. Thus D_A and D_B are fixed spaces.

Finite invariants are exact over C. A fixed diagonal class that has some lift has a fixed lift after averaging, while the quotient maps remain equivariant. Therefore the lower bounds on Q and I remain valid on invariants. The proof does not silently infer invariance of an arbitrary lift without averaging.

For the two-slope applications, I retained and reread the actual torsion/HN and Hom-orthogonality argument from the just-audited E826. It supplies preservation of the filtration and blocks for every specified action on E. No claim is made that an arbitrary unstable object possesses this filtration.

## 4. Every nondegenerate cross pair

For a nondegenerate difference line on a fourfold, the indices of the line and its inverse are j and 4-j. Their degree-one cohomology groups cannot both be nonzero, so both degree-one Yoneda products vanish. Whenever one degree-one group is nonzero, its own degree-three group is zero; multiplication by all of H2(O_X) therefore kills it. This verifies both hypotheses with Z=0 and W=H2(O_X), of dimension six, separately in every possible index case.

It follows that u positive line blocks already contribute 6u without any A0 condition, by taking J empty. Selected B blocks contribute additionally only under their explicit Ext3 condition. In particular u at least four gives the claimed contradiction to cap rank18, even when other pairs have nonzero index-three groups. The proof follows the same pair in each boundary product, so opposite-direction groups from different pairs cannot produce an unaccounted cancellation.

## 5. The rational four-divisor algebra and all degeneracies

The two factors Y and Z0 are actual abelian surfaces, given by the rational S-block decomposition; they are not the irrational RM embedding planes. A rational block xI+yU2 has determinant x^2-2y^2, which is zero only when x=y=0. Thus a nonzero cross difference has either two nondegenerate blocks or exactly one. The opposite slopes in the application guarantee the difference is nonzero.

If only the Y block is nonzero, the line is an exterior product of a nondegenerate line on Y and a degree-zero line on Z0, after absorbing the other flat twist into the Y line. This follows from the actual product decomposition of Pic0 and the vanishing cross divisor block. A nontrivial flat Z0 factor makes all cohomology of the line and its inverse vanish. If it is trivial, the displayed Kunneth formulas exhaust the three possible surface indices.

For W=H1(O_Y) tensor H1(O_Z0), multiplication raises the Y cohomological degree by one. The nondegenerate Y line has cohomology in only its index degree, so this multiplication vanishes into H3 for the line and its inverse. Both degree-one groups can occur only at surface index one. Their product then belongs to H2(O_Y) tensor H0(O_Z0), a pure component of Z. The identical check with the two factors exchanged gives the other pure component. These are actual cup/Yoneda products, including flat twists and all multiplicity matrices, rather than dimension counts.

The direct decomposition H2(O_X) into the four-dimensional mixed part W and the two-dimensional pure part Z is preserved by the allowed functors. Hence the lemma gives 4(u+|J|) in every claimed nonzero case. The threshold at least five is correct. The additional condition on selected negative blocks is retained; no vanishing for the unit block is inferred merely from its name or local form.

## 6. Balanced consequence, sources and check limits

The complete normalized balanced character has degree-two cap rank18, with contributions1,16,1 in the previously checked exterior model. Rational algebraic B gives an invertible degree-preserving shear. I retain the full E826/S21 audit of the invariant CY4 adjunction, which forces invariant Ext2 dimension18 under weak semiregularity for the specified effective coherent action. Either larger lower bound is therefore a contradiction. The proof does not require preservation of semiregularity by an isogeny.

The source inputs retain their exact status. Original Mumford section16, printed pages150–153 and162–163, was freshly read for the immediately preceding E826 audit, including the complete invoked vanishing and eigenvalue-index statements/proofs. The Pic0 vanishing and product Kunneth facts retain the published/elementary justifications already recorded. Supplied S21 through(S21.8) was freshly reread for E826 and is not relabelled as a new refereed theorem. The published BF composition/evaluation checks retain the complete earlier primary-source readings listed in E825/E826.

No new numerical premise is present in E827, and no new finite test is needed to validate an infinite Yoneda/Kunneth argument. This event is a complete mathematical proof check, not a computational proof or a character-table scan. The prior independent E826 exact certificate supplies an actual example and the cap ranks only in its already recorded scope. No TeX compilation is claimed.

The result strictly enlarges the stated two-slope exclusion. It leaves the explicitly listed gates of insufficient positive/selected blocks, absent required A0 vanishings, divisor directions outside the rational four-divisor algebra, and objects lacking the actual equivariant filtration. It does not produce a semiregular seed or prove general nonexistence. No defect was found in the final frozen proof.
