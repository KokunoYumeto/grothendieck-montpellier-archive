# SF-E839 independent whole-proof audit

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, inherited effort not exposed, HODGE_DIVISION. Result: **PASS**. The complete frozen 170-line draft, complete author certificate and its actual output, and the invoked E838/E836 interface passages were read. No repair was requested.

Reviewed draft: `agents/sixfolds/rm_rank_five_jet_obstruction_draft.md`, SHA-256 `7d17ecc2d6f858127b01d6b62537a11e1e3991e72619047ded837fd69d687fbb`. This report concerns that frozen mathematical text; a later status-only conversion does not silently change its hash.

## Universal matrix argument

I independently checked the elimination over an arbitrary commutative Artinian local algebra. Splitting unit pivots gives a square residual block with entries in the maximal ideal and preserves its cokernel. Modulo the third filtration step, its image in the pure quadratic part is precisely `C2(ker L) + V im L`: a constant input must lie in the kernel of the linear coefficient map, linear inputs contribute through multiplication by that map, and quadratic inputs contribute zero. Its dimension is at most `(k-a)+ea ≤ ek`. An actual annihilator whose leading classes span a space of dimension `rho` puts that space tensored with all `k` target constants in the image; this has dimension `rho k`. The contradiction when `rho>e` is valid for every size. It does not require a grading, commuting coefficient matrices, an algebra splitting, or generation of the whole square of the maximal ideal.

The equality boundary is correctly limited to the abstract matrix lemma. In the four-variable square algebra, the four products of the sum of the variables with the individual variables are independent and annihilate the nonzero cokernel of multiplication by that sum. No simultaneous deformation follows from that example, and none is claimed.

## Actual module and filtered-jet interfaces

I reread E836's extension matrices, the lifting of the map to the free hull, and both orders of the companion identity. Their sizes and common extension matrices agree with E839. E819's signed-length equality makes the two multiplicities equal and positive; a nontrivial modification with only one side cannot escape this reduction. A linear combination of the two already obtained companion equations annihilates the cokernel of the corresponding matrix. Invertibility therefore follows from five independent leading brackets in embedding dimension four, without assuming a deformation in a third pencil direction.

After inverting this matrix, passage to the second filtration quotient uses only the constant part of each remaining matrix. Applying a linear functional nonzero on one bracket gives a scalar matrix. All six equations then make both complete leading tuples proportional. The contradiction is to the independently checked Jacobian-socle argument in E838, not to a false proportionality statement over a nonreduced ring.

I read the entire E838 associated-graded argument: successive regular initial forms give the associated graded quotient, preserve regularity, and give Hilbert function `(1,4,6,4,1)`. The bracket tuples are tested in the separate homogeneous algebra, where the two self-wedges vanish and the mixed wedge is the nonzero Jacobian socle. This precisely covers all higher-order perturbations with the stated regular quadratic jets. No Ext group or deformation is base changed to an easier quotient.

The invariant-to-ordinary, completion, and algebraic rational B-shear steps retain the previously reviewed E819 hypotheses. E839 adds no equivariance requirement on a chosen ideal-generator basis, and adds no new categorical premise.

## Intrinsic residual locus

The bracket map is a well-defined linear map from the exterior square of the actual four-dimensional relation space to its degree-two quotient. On a standard Grassmannian chart it is a 6 by 6 matrix linear in the two pencil coefficients. Rank at most four is equivalent to the vanishing of all 36 minors of size five, and identically vanishing pencils give at most six coefficients for each minor: 216 equations. The augmented 9 by 9 determinant consists of four degree-one generator columns and five degree-two bracket columns, so its coefficient degree is at most fourteen. Pivot elimination is legitimate on the normalized chart. Change of either basis preserves rank, giving the stated intrinsic closed residual locus. No codimension, independence, sufficiency, or existence assertion was inserted.

## Exact witness and strict scope

I checked the change-of-parameter matrix, transformed decomposable bivectors, and the actual quadratic relation space. The quotient is free of rank two over the three-variable square algebra. Its relation space has exactly three projective rank-one points: the displayed mixed 2 by 2 minor forces the first coefficient to vanish, and the remaining diagonal matrix has only the three coordinate axes. This invariant is preserved by local algebra isomorphisms, so the example is outside the formal square-algebra family.

The two bracket maps each have rank exactly five; their full pencil has an identically zero determinant. The nonzero five-minor is the printed factorization, so the criterion is strictly stronger than E838's determinant test. The kernel at each pure endpoint is one-dimensional. An independent triple of leading generators has three-dimensional exterior square, so it cannot consist of commuting generators modulo the ideal. This applies to every minimal regular presentation and to all higher perturbations with the same jets, giving the stated exclusion from E836's commuting-triple family.

The global coherent examples have exactly the specified torsion and hull quotient, since their kernel is torsion free. Their characters cancel the two identical finite defects. The global Ext calculation reduces to the local Koszul calculation, giving `6 × 16 × m² = 96m²`; positive Ext from the locally free hull to the point-supported sheaf vanishes. The example is an actual coherent extension, with no assertion of simplicity, a finite action, or weak semiregularity.

## Separate exact reconstruction

`audit_rank_five_jet.py` and `audit_rank_five_jet.json` were written separately after reading the author's whole program. No author code, computed matrix, or output is imported. The implementation builds the actual length-sixteen quotient with `x1² = -x2 x3`, constructs its complete multiplication table, checks all 4,096 basis associativity triples and its one-dimensional socle, and derives both bracket maps from the four parameter columns. It computes all 36 five-minors, identifies their two nonzero entries, and confirms both endpoint ranks, mixed socle coefficient, rank-one relation conditions and the four-annihilator equality boundary.

Actual successful execution: **2026-11-21 22:18:11.790138 UTC**, **0.274954087 seconds**. No failed assertion or failed run preceded this execution. This is a finite witness supplement only; the universal matrix, module-lifting and geometric claims were checked as proofs.

## Fresh primary-source check

I freshly read the published Eisenbud–Ulrich, *Duality and socle generators for residual intersections*, J. reine angew. Math. 756 (2019), 183–226, DOI `10.1515/crelle-2017-0045`: Theorem 7.1 on p.210, the complete Theorem A.1 proof on pp.222–223, Theorem A.3 and its complete proof on p.224, Theorem A.5 and its complete proof on pp.224–225, and the concluding proof of Theorem 7.1 on p.225. The exact characteristic-zero complete-local and finite-complete-intersection hypotheses apply. This is a fresh reading of the invoked published proofs, not a claim to have independently rebuilt all upstream different theory.

Primary author-hosted published PDF:
<https://www.math.purdue.edu/~bulrich/papers/published%20version%20of%20Duality%20for%20Residual%20Intersections.pdf>.
The web retrieval confirmed the journal metadata and 44-page document; the full invoked proof was read from the cached published PDF's local text extraction, `sources/EisenbudUlrich2019.txt`. No visual page-render inspection is claimed. The sibling's frozen PDF hash is `fa8959341544a1dd80f7789709039ba401dabc9972d935da753ac3fe9abdd949` and is checked in the accompanying source record.

## Boundary

The result leaves rank-at-most-four leading pencils, higher initial degrees, unequal or nonfree Artinian defect modules, and unrelated complexes open. Neither a zero determinant nor the rank-at-most-four necessary condition is interpreted as evidence that a semiregular object exists. No TeX compilation is claimed.
