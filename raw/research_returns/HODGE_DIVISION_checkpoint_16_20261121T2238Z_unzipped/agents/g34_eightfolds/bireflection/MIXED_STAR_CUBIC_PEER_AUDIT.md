# Independent whole-proof audit of SF-E833

**Outcome: PASS. No mathematical repair requested.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION. Actual completed-check time: **2026-11-21 21:10:42 UTC**. I read the entire 256-line frozen draft `agents/sixfolds/rm_mixed_star_cubic_obstruction_draft.md`, SHA-256 **`2a74ada9fb1a9894ffc7c1f402e8eeb4d470af5a7d6d63923951055b99f4b58f`**, the whole author checker, its output and its retained failed-attempt record. The directly preceding E832/E832R and original E825 complete proofs had already passed my independent whole-proof reviews, so their new interface is checked against actual reviewed statements.

## The compound lemma does not require positivity

The two adjusted unit blocks are nonzero because their traces are strictly positive. If both have rank one, the right-hand compound has rank three and contains both pure-plane bivectors in its image. These force both full support planes into the image of B, making B invertible and its compound rank six, a contradiction.

The rank-one/rank-two case is also complete even when the second pure-line coefficient vanishes. The nonzero first pure line places the entire first plane inside im(B). The mixed image is im(U) tensor V_minus; its bivectors a wedge v, for every v in the second plane, then place that plane inside im(B) as well. Thus B is invertible, contrary to the right-hand rank at most four. This uses the actual support of decomposable bivectors and is valid without semipositivity.

When U and V are invertible, the mixed rank four forces B invertible. Its compound preserves each pure line with a nonzero scalar, so B preserves each supporting plane individually. Equality of the mixed simple tensors gives C=tU and D=κV/t. Taking adjoints shows t is real, and invertibility shows it is nonzero. This establishes the exact block form required for the cubic argument; no positivity or determinant sign has been inferred.

## Complete character and cubic normalization

The unit character is exactly 1−2D³+4D⁴ in dimension four. Twisting it contributes u³/6−2D³ in character degree three. For the free star the identity exp(α)(m+H) is exact because every individual difference has square zero. The first Chern equation gives H=−ru−mα. The free cubic consequently becomes −ruα²/2−mα³/3, with the stated signs and coefficients.

The completed square and its κ=x(1+x), d=(1+x)q agree with the independently checked E832 calculation. After α=(t−x)p+(κ/t−x)z, the cubic has precisely the displayed two coefficients A_plus and A_minus of p²z and pz². I independently expanded the entire expression in the full eight-generator exterior algebra, with eight independent real Hermitian block variables; this checks the coefficients before any scalar specialization.

The two mixed cubic components belong to complementary invariant exterior-algebra summands. This is linear algebra on the RM tangent decomposition and does not assert that its planes are rational subspaces or tangent spaces of abelian subvarieties. On each plane p²=det(U)θ_plus² and z²=det(V)θ_minus². Therefore the cubic equation gives exactly
A_plus det(U) z=6xk³ θ_minus and A_minus det(V) p=6xk³ θ_plus.

The right sides are nonzero. If either A coefficient vanishes there is already a contradiction; otherwise each block form is forced to be a scalar polarization form. Their equal trace 7k then makes both scalars 7k/2. Thus u is the scalar form (7k/2)θ, and the already proved scalar-unit lemma contradicts the second-character equation. The proof does not divide by an unproved nonzero coefficient and does not need the fourth-character equation.

## Actual sheaf and determinant interface

The given quotient B is locally free, including the allowed zero-rank case. Local splittings preserving the included A give block-triangular transition matrices. After the fixed unit F comparison is removed, the unit FF diagonal is exactly the scalar transition of L on r copies. The remaining terms pass through the free part.

E825 supplies a genuine multiplicative ring map on these endomorphism blocks, killing all FF factorizations through free modules. Thus its defect cocycle is exactly that of L on r copies, and its determinant extends as r c1(L) on X. There is no additional O(D) twist and no rank assumption on extension matrices. This interface remains valid when either free sum in A or B is empty.

Under a rational algebraic B shift, the intrinsic E825 condition gives u−7D/2 with zero mixed blocks and zero trace on each plane, precisely the equal trace 7k used in the cubic argument. No extra finite-group action on the selected filtration or summands is imposed. Published BF compatibility and supplied S21 retain their previously reviewed exact scopes; they are not relabelled as a new external theorem. No pullback preservation of semiregularity is assumed.

The permitted real star center need not be an actual line bundle: it is used only in an identity of invariant forms. Positive multiplicities and r,m>0 are retained. The conclusion genuinely removes the mixed-sign single-center case, while multiple centers, different units, signed virtual multiplicities and unproved defect determinants remain outside the theorem.

## Independent exact supplement and failures record

`audit_mixed_star_cubic.py/.json` passed on its first run in **0.2858775999993668 seconds**. It imports no author helpers or outputs; I read the author code before writing it. It reconstructs the full exterior product on eight generators, two arbitrary Hermitian 2×2 blocks with eight independent real variables, all eight nonzero cubic components, both determinant-volume identities, and injectivity of both plane-to-mixed-cubic maps (rank four each). It then verifies the equal-trace scalar conclusion. The universal support-plane argument and actual sheaf/action interface are mathematical checks, not consequences of these finite symbolic computations.

The author's earlier raw structural equality failure compared expanded and factored versions of the same polynomial. Its retained attempts record identifies this, and the corrected exact-difference predicate passes. This is not a mathematical failure. No new numerical seed, group action or semiregular object is constructed or claimed.

