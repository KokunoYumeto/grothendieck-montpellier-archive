# Independent whole-proof audit of SF-E826

**Verdict: PASS for the complete stated two-slope architecture and the actual indecomposable example.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. Actual clock record: **2026-11-21 20:09:16 UTC**. The complete mathematical reading, original-input arithmetic reconstruction, and source rereading described below were completed before this timestamp.

The entire 473-line frozen draft `agents/sixfolds/rm_two_slope_extension_obstruction_draft.md` was read. Reviewed SHA-256: `58eb0b23279e278860bf305a8038231897d5359ed1441e4f0c9bd797a98727ce`. Both complete author certificates and the eight-orbit input were also read. The result excludes the specified architecture. It does not exclude every positive-determinant form surviving E825, every unstable object, or every coherent sheaf with the same character.

## 1. The actual triangle inequality

I checked all three long exact sequences, including their composite maps. Ext1(A,B)=0 gives both the surjection Ext1(A,A) to Ext1(A,E) and the injection Ext2(A,A) to Ext2(A,E). Ext3(B,A)=0 gives the surjection Ext2(B,E) to Ext2(B,B). The boundary of a class lifted from Ext1(A,A) factors through Ext2(B,A), hence is killed on Ext2(B,B). The quotient Q used in the proof therefore still surjects onto Ext2(B,B) and injects into Ext2(E,E).

The second boundary on the injected Ext2(A,A) factors through Ext3(B,A), hence vanishes. Exactness identifies Ext2(E,E)/Q with the kernel of this second boundary, which contains the injected Ext2(A,A). This proves the sum lower bound without a spectral-sequence degeneration claim. Every map is natural under the actual action on the triangle. Taking finite invariants is exact over C, so the same proof gives the invariant inequality. On an abelian fourfold, ordinary Serre duality supplies the required Ext1(A,B) vanishing from Ext3(B,A)=0. No equivariant splitting is assumed.

## 2. The intrinsic filtration and actual block actions

Since B is locally free, the extension splits over local rings, and its torsion is exactly the torsion of A. The quotient A/T is a direct sum of rank-one torsionfree sheaves of slope 14 theta^4, whereas B is semistable of slope minus 14 theta^4. These are exactly the two HN steps. The stated characterization by images of positive-slope semistable sheaves is valid: any nonzero composite into B would have an image that is simultaneously a positive-slope quotient and a negative-slope subsheaf. Therefore every translation/degree-zero tensor action preserves the actual inverse image A, not merely its class.

I reread the unit-module algebra used here. F dual is O_X because every map into a torsionfree line factors through its rank-one ideal quotient and its double dual. Its endomorphism sheaf is O_X plus O_S(-D)^2, and the latter has no global sections. Thus End(U)=C. For a same-slope line L_alpha, Hom(U,L_alpha)=0 follows from the nontrivial degree-zero-with-respect-to-theta difference class. In the reverse direction the ideal/hull term has no section, and the torsion term on S has strictly negative theta-degree. The same argument gives Hom orthogonality between every distinct line-class block.

The projections onto these orthogonal isotypic blocks are the actual central block projections. Translations and degree-zero tensor operations preserve Chern classes and the presence of torsion, so they cannot permute distinct line-class blocks or exchange the unit block with a line block. The finite action consequently induces actual actions on each required block. This argument does not choose additional linearizations or pass to an isogeny.

## 3. The invariant cap-rank comparison

For a positive-rank block n L_alpha, the full character is n exp(alpha). The exterior shear by exp(alpha) identifies its degree-two cap image with H2(O_X), of dimension six. Published BF trace/evaluation composition then gives rank at least six for the evaluation map into its invariant self-Ext2. Naturality puts evaluation in invariants even if that individual block is not semiregular and even if its action has a kernel.

Summing over the distinct actual line blocks gives the lower bound 6(u+v), which survives the triangle inequality. I freshly reread the complete supplied S21 argument from its statement through (S21.8), including vanishing nonidentity coefficient sectors, invariant Serre duality, the forgetting/induction comparison, and the final invariant adjunction. In exactly its specified effective coherent finite-action scope, semiregularity forces invariant Ext2 dimension equal to the complete degree-two cap rank. The supplied status is retained; it is not renamed as a newly proved published theorem.

For the balanced character the exterior model has rank 1+16+1=18. I independently reconstructed this rank and the line rank six by exact wedge matrices. A rational algebraic B acts by an invertible shear preserving total Hochschild degree two, so the rank is unchanged. This argument concerns the character and evaluation on the original object; it does not assert that semiregularity or the action survives a pullback. The contradiction for u+v at least four is valid.

## 4. The full character and geometric line data

The symmetric integral matrices I,U,S,US on E_i^4 define actual line bundles by coordinate and Poincare constructions. Their simultaneous real eigenbasis gives the four displayed Q(sqrt(2)) eigenvalues. D=4 theta is very ample; the already checked regular Bertini/Koszul construction supplies the smooth integral complete intersection and the actual unit sheaf. The unit resolution gives exactly 2 exp(10 theta)-2 exp(2 theta)+exp(-2 theta) after twisting by 14 theta.

My independent rational-pair Q(sqrt(2)) implementation expands all sixteen subset coordinates from the eight orbit weights. It reproduces the seven displayed free coefficients, every printed positive integral multiplicity, r=341355757056, R=10923384225792, ranks 16r on both sides, and the full identity ch(A)+ch(B)=R v_(1/2). No floating optimization output is imported. The triangular free couplings disappear under E825's actual ell ring map, so the defect bundle on S2 is the stated O_X(14 theta)^r and its determinant has the asserted positive class.

## 5. Cross Ext vanishing and the actual capacities

The index of each nondegenerate line difference is correctly obtained from the two symmetric 2-by-2 blocks. I independently recovered all 240 cross differences: 36 have index zero, 144 index one, and 60 index two, with none degenerate and none index three. Thus every line-to-line opposite Ext3 vanishes by the abelian index theorem.

For the unit target, the resolution terms lie in degrees zero, minus one, and minus two. Total cohomological degree three can receive only H3 of the first term and H4 of the middle term. The former has index at most two for every negative line; the latter vanishes by its positive theta-degree and Serre duality, whether or not it is nondegenerate. No claimed rank of a resolution differential is needed. For the four chosen unit-edge sources all three line terms have index one. Their dimensions are independently 4718592,3174400,2467584, giving the valid cokernel lower bound 3088384.

There was one initial error in my independent checker, not in the proof: I asserted nondegeneracy of every auxiliary resolution term for all twenty sources. That assertion is unnecessary and false. I repaired the checker to record a degenerate unused term with null index and to test precisely the hypotheses above. The failed attempt and its explanation are retained in `audit_two_slope_extension_attempts.json`; no author data or mathematical statement was changed.

## 6. The universal rectangular brick construction

For n at least m, the coordinate injections cover C^n. The equations for the first injection and its products with J and J transpose force the source endomorphism to commute with both shifts, because that injection is injective. Those shifts generate the entire matrix algebra, including the one-dimensional case, so the source endomorphism is scalar. The spanning images then force the target endomorphism to be the same scalar. The dual argument uses a surjective first projection and jointly injective projections when m exceeds n. This proves the all-size claim with ceil(max(n/m,m/n))+2 independent classes.

The proof uses independent classes in the actual Ext1 space on each edge. I reconstructed the 148 admissible capacities and checked exactly the 32 edges printed in the draft, including their stated required and available dimensions. They form a connected acyclic graph on all 33 vertices. Hence applying the independently proved brick construction on each edge forces a single scalar on every vertex. The finite matrix checks over the prime 1009 independently confirm all 36 dimension pairs from one to six; these checks supplement rather than replace the universal proof.

## 7. Actual gluing and indecomposability

B is locally free, so Ext1(B,A)=H1(Hom(B,A)). Choosing the indicated class gives an actual coherent extension, represented by upper triangular Cech transition matrices. Their strictly upper blocks multiply to zero, so the additive cocycle condition is the entire gluing condition. There is no omitted Yoneda relation, generic multiplication assumption, or dg formality premise.

Hom(A,B)=0 follows from the slope comparison, using the unit's torsionfree hull for maps to a locally free target. Thus every endomorphism of E preserves A. Pairwise Hom orthogonality reduces its restrictions to the vertex matrices, and compatibility with the chosen extension is exactly a e=e b. The brick construction forces these restrictions to be one common scalar. The kernel of restriction is exactly Hom(B,A), embedded as i f p, and its square is zero. Conversely a compatible pair lifts by the actual Cech coboundary equation. Hence End(E) has quotient C by this square-zero ideal and has no nontrivial idempotent. This proves indecomposability of the constructed coherent sheaf. Simplicity is correctly not claimed.

The entire family, including this indecomposable member, has 32 canonical line-class blocks and therefore invariant Ext2 at least 192, contradicting cap rank 18 under semiregularity. This is an actual Ext obstruction and does not infer failure from the split starting character.

## 8. Exact computation and source boundaries

`audit_two_slope_extension.py` imports no author code, capacities, tree output, or selected cases. Its final actual run passed in **0.04080445999716176 seconds**, with `audit_two_slope_extension.json`. It reads only the eight rational orbit weights and the actual printed tree. It checks all sixteen character coordinates, eight multiplicity rows, all 240 line indices and twenty unit-resolution cases, all 148 admissible capacities, the exact printed 33-vertex tree, 36 independently built rectangle/Jordan systems, and both cap ranks.

The Mumford original retained text was freshly reread at section16, printed pages150–153 and162–163: the full nondegenerate-line vanishing/Riemann–Roch statements and the eigenvalue-index corollary with proof. The original image/text provenance remains that recorded for the earlier audits. BF2008 Theorem5.1.3, Proposition5.2.2, Corollary5.2.3, Proposition6.2.1, Theorem6.4.2 and Proposition6.4.4 retain their earlier complete primary-source readings, including the fresh E825 check of author pages24–27. The unit algebra/resolution and E825 ell map were reread in full relevant scope. Supplied S21 was freshly reread through (S21.8) and retains its precise supplied status. No new Severn, Markman, or unrefereed032 theorem premise is accepted.

No TeX compilation, constructed finite action, semiregular seed, or exclusion outside the specified two-slope architecture is claimed. No defect was found in the frozen proof.
