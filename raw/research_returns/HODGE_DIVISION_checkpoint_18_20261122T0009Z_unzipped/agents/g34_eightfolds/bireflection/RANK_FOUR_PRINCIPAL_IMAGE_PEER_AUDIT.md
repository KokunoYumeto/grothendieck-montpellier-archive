# SF-E840 independent whole-proof audit

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. Result: **PASS**. I read the complete frozen draft, every line of the author's exact checker and its actual output, and the complete invoked companion/filtered-jet passages. No mathematical or wording repair was requested.

Reviewed draft: `agents/sixfolds/rm_rank_four_principal_image_draft.md`, SHA-256 `d29300c26b59b71edd4b14381faad4713f3982c884e8da68047b62f641c199b8`. Author checker SHA-256: `05946f6d4d44083276c0a963b8c15323fdc9cf5fd9fdc5ebc04f325974f15e0a`. The author's reported successful execution was 2026-11-21 22:34:55.291542 UTC, 0.092761750 seconds. I read that output; I did not rerun the author's program in its owned directory.

## Universal multiplication argument

For a two-dimensional subspace `L` of the four-dimensional cotangent space, the degree-two ideal `VL` has dimension seven. If its image modulo the four regular quadratic relations had dimension at most four, at least three independent relations would lie in `VL`. The restrictions of all four relations to the two-dimensional quotient would then span at most one binary quadratic. Over the complex numbers they have a common nonzero projective zero, including when every restriction vanishes. This contradicts the finite-length homogeneous complete-intersection hypothesis. Thus every subspace of dimension at least two has multiplication image of dimension at least five.

The argument uses the quotient's dual projective line correctly: a point of `(V/L)^*` is a functional on `V` vanishing on `L`. It therefore gives an actual common zero of the original relations. The hypothesis is not replaced by linear independence of the quadrics, which would be insufficient. It follows immediately that `K(J)` has dimension at most one whenever `J` has dimension four.

## Equality in the filtered square-matrix estimate

I checked the complete elimination and equality argument over an arbitrary commutative local Artinian algebra with the specified first two graded pieces. Invertible row and column operations split unit pivots and preserve the cokernel and its scalar annihilators. A noninvertible square matrix leaves a nonempty square residual block with entries in the maximal ideal.

Choose only vector-space splittings modulo the third filtration step. For a constant input, the first-order image vanishes exactly on the kernel of the linear coefficient map. Linear inputs contribute through multiplication by its image, and higher inputs contribute nothing at this order. Consequently the pure quadratic image is exactly `C2(ker L1) + mu(V im L1)`. This is an equality of vector subspaces, not an assumed algebra or grading splitting.

Each actual scalar annihilator times every constant target basis vector is a column image. Its leading term puts `J tensor C^k` in the pure quadratic image. The inequalities

`4k <= dim(image) <= (k-a)+4a <= 4k`

force `a=k`, zero kernel of the linear coefficient map, and equality of its multiplication image with `J tensor C^k`. Contracting by every target linear functional shows that the multiplication image of the span of all coefficient vectors lies in `J`. That coefficient span is nonzero. The preceding multiplication lemma forces it to be a line. Dimension then makes the full linear coefficient image precisely that line tensored with the entire target space. It follows that `J=ell V` and multiplication by `ell` is injective on `V`.

The same multiplication lemma proves uniqueness of the line and `dim K(J)=1`. This checks every equality implication, including the passage from a matrix coefficient image to a common scalar factor. Arbitrary higher-order entries and noncommuting coefficient matrices are allowed. No deformation or Ext group is base changed to a simpler quotient.

## Actual companion and geometric interfaces

I reread E836's complete construction of the extension matrices, the map to the lifted free hull, and both companion equations, including their order conventions. E819 supplies the equality and positivity of the two common multiplicities through its finite-perfect-cone supertrace argument. E840 retains the same actual finite modification, coherent finite action and rational algebraic B-field hypotheses. It does not require equivariance of a chosen generator or module basis.

For a rank-four pencil direction, the linear combination of the two existing companion matrices satisfies an actual annihilator equation. No deformation in a third pencil direction is presumed. If that matrix were invertible, solving for the common extension matrices and then passing to the quadratic filtration quotient would involve only the constant parts of the other matrices. A linear functional nonzero on one pencil component forces those constant matrices to be scalar. All six identities then make both entire initial bracket tuples proportional to the chosen tuple, a contradiction.

I reread E838's complete successive-initial-form argument and homogeneous Jacobian argument. Regular quadratic initial forms give the associated graded complete intersection and cover arbitrary higher-order perturbations. In that separate homogeneous algebra, the two self-wedges vanish and the mixed wedge is the nonzero Jacobian socle times the transverse bivector wedge. This proves linear independence over the complex numbers. It is not an unjustified statement about proportionality over a nonreduced ring or about the perturbed Jacobian.

The noninvertible matrix therefore satisfies precisely the equality lemma's hypotheses. The new necessary condition is intrinsic under relation-basis and local-coordinate changes. Rank at most three, or a principal rank-four image, is not treated as sufficient for a deformation.

## Exact witness and strictness

I independently reconstructed the length-sixteen quotient using a rational Groebner basis, rather than importing the author's replacement rule. Its Hilbert function is `(1,4,6,4,1)`. The actual four parameter columns have determinant four and give the two transverse decomposable bivectors. Matrix multiplication by the actual Jacobian produces the printed two bracket tuples and the full pencil.

The pencil has generic rank four, rank three at `a=b`, and rank two at `a=-b`. Both pure endpoints have rank four. Every one of the 36 five-minors vanishes, while the displayed four-minor is `256(a-b)^2(a+b)^2`. Every one of the 36 ordered scalar cross-minors vanishes in the quotient. The mixed bracket wedge is nevertheless `64xyzw` and the Jacobian socle is `16xyzw`. These assertions are compatible: scalar cross-minors express pairwise proportionality equations over a ring with zero divisors; they do not imply proportionality by a complex scalar.

The quotient functionals were independently derived from the left nullspace of the plus bracket matrix. Stacking multiplication by all four variables gives a rank-four map on the possible common linear factor, so `K(J)=0`. This is the exact obstruction required by the theorem, despite all previous scalar and rank-five tests vanishing. As a separate boundary sanity check, multiplication by `x` has a four-dimensional principal image and common-factor space exactly `C x`; this is only an equality example, not a deformation claim.

The relation space has precisely three projective rank-one quadrics. Its mixed two-by-two Hessian minor forces the coefficient of `x^2+yw` to vanish; the remaining diagonal expression has the three coordinate-square lines. This invariant excludes every formal coordinate-square presentation. Each pure bracket map has a two-dimensional kernel, whereas the exterior square of an independent triple of generators has dimension three. Thus no minimal presentation gives E836's commuting triple, for either pure bivector. The example also lies in the zero-determinant locus of E838 and the rank-at-most-four locus of E839. These are exact strictness statements; they do not claim that the earlier criteria were otherwise exhaustive.

The coherent extensions have the stated torsion, hull and hull quotient: the quotient kernel is torsion free and differs from the locally free hull only at a point. The two finite defects cancel in the full character. The Koszul calculation gives `Ext^1(K,A^m)=Ext^2(A^m,A^m)` and dimension `6*16*m^2`, since positive global Ext from the locally free hull to the point-supported target vanishes. Actual gluing is legitimate. No simplicity, successful finite action or semiregularity is inferred.

## Independent computation and its limited scope

Files: `audit_rank_four_principal.py`, `audit_rank_four_principal.json`, and the retained `audit_rank_four_principal_initial.json` / `audit_rank_four_principal_attempts.json`.

The independent program was written after reading the complete author checker. It imports no author program, bracket matrix or output. It uses Groebner normal forms and Jacobian/skew-matrix multiplication; it derives its quotient functionals by a nullspace calculation. It checks all 256 products, 4,096 associativity triples, all 36 scalar cross-minors, all 36 five-minors and all 225 four-minors, both endpoint and special-direction ranks, the socle identities, the common-factor map, a genuine principal equality example and the rank-one relation invariant.

Final actual successful execution: **2026-11-21 22:42:09.220712 UTC**, **0.210295113 seconds**. The first execution also passed all mathematical assertions. I then noticed an integer conversion in an auxiliary determinant-output list that truncated rational minors obtained from the normalized nullspace basis. The original output and exact correction are retained; the final output preserves the nonzero minors `1/2` and `1`. The rank and nullspace assertions were exact throughout. No failed mathematical assertion or theorem repair occurred.

This computation is a finite witness supplement. It does not purport to certify the universal matrix equality, module lifting, invariants or B-field arguments by finite samples; those were checked as complete proofs.

## Sources and review boundary

The only external algebraic input added through the predecessors is the published Jacobian-socle theorem. Its exact source is Eisenbud–Ulrich, *Duality and socle generators for residual intersections*, J. reine angew. Math. 756 (2019), Theorem 7.1 p.210 and Appendix A.1/A.3/A.5 pp.222–225, DOI `10.1515/crelle-2017-0045`. I had freshly read the full invoked proofs during the immediately preceding E839 audit and checked the cached published PDF hash `fa8959341544a1dd80f7789709039ba401dabc9972d935da753ac3fe9abdd949`. That source reading is reused here, not misreported as a second fresh reading or independent proof of all upstream different theory.

Primary published PDF: <https://www.math.purdue.edu/~bulrich/papers/published%20version%20of%20Duality%20for%20Residual%20Intersections.pdf>. The exact source record and extracted text remain under `sources/EisenbudUlrich2019_source_check.json` and `sources/EisenbudUlrich2019.txt`. No visual page inspection is claimed. The complete E836 companion passage and E838 initial-form/socle passage were reread for this audit.

The theorem leaves rank-at-most-three pencils, principal rank-four images, higher initial degrees, unequal or nonfree Artinian defect modules and unrelated perfect complexes unresolved. No unrestricted complete-intersection exclusion is inferred. No TeX compilation is claimed. The frozen mathematical proof passes without repair.
