# Archive audit ledger

Run: GCT_KRON_20261120. Agent: /root/archive_audit. Model: GPT-6 Astra Pro; effort not exposed. Updated 2026-11-20 23:43 UTC.

## Completed mathematical gates

- A-001–A-004: subset/opposite operations separated; explicit C2 and V4 counterexamples; no effective permutation lift of a nontrivial irreducible; monomial Cauchy coefficients can be virtual. These rule out the proposed automatic positive-cone argument.
- A-005–A-009: split quadratic group question answered negatively; characteristic-two exterior failure; Witt lambda descent refuted; general-topos hyperbolic and stable-hyperbolic claims corrected; standard etale Stiefel–Whitney formulas placed with primary sources.
- A-010/A-017: integral tensor Cauchy identity proved in exact K0 through universal equivariant flag splitting; exact-K0 product lemma removes the global rank bound. Actual summand assertion separately refuted by A-004.
- A-011–A-012: every determinate finite-injection statement reported in SA17 checked; wreath stabilizer formula supplied; single-map-functor summand equivalence refuted and corrected.
- A-013: universal local-ring polynomial assertion refuted in F2 and an explicit characteristic-zero singular local ring. Q-algebra locals and Zp exact lattices proved affirmative. Exact K0 versus split K0 explicit throughout.
- A-014–A-016: Witt-series formulas checked; representation functor identities proved with hypotheses; Borger transfer limits identified. Inactive source after end-document separated.

## Inventory and verification

ARCHIVE_INVENTORY.tsv contains 76 rows, including every supplied archive file and all relevant SA17 claims. CHECK_EVENTS.tsv records whole-proof self-read checks, exact finite computations, source scope checks, and a targeted check of root M003. These are not labelled independent-agent re-proofs. SOURCE_LOCATORS.tsv records exact primary locators, including original SGA6 page images.

The exact James locator for classification is Theorem 11.5 p40. The earlier incomplete Theorem11.1/Definition11.2 locator was corrected after reading original pp39–43; the correction is retained in CHECK_EVENTS.tsv.

## Availability and scope gates

1. Manuscript images were not supplied. Statements are conditional on the provided transcriptions. In particular P_i, the deleted material, the name on scan008, and the endpoint of the product polynomial are not authenticated ink readings.
2. SA17 mentions q_H^n without defining it. No determinate assertion about these operators can be proved or refuted from the supplied material.
3. The complete classification of all local coefficient rings with polynomial induction representation ring is not asserted. The actual universal-local claim is refuted; the separately posed Zp case is closed.
4. CLOSED by A-017: exact K0 commutes with products of exact categories, so infinite rank-stratum decomposition extends A-010 to finite local ranks without global bound.
5. Scan009's arbitrary strictly local ringed-topos shorthand lacks specified cohomological topology. The proved correction uses schemes etale over Z[1/2], where cited splitting results apply.

## Main-question implication

The archive constructions give precise operations, virtual identities, and useful finite-group dictionaries. They do not themselves give a positive irreducible-basis rule or a saturation theorem. Main Kronecker families and actual determinant-closure comparisons are handled by the parent and sibling agents; this audit provides their valid input and pinpoints invalid shortcuts.

## Further contributions, 2026-11-20T23:56:12.743478+00:00

- A-018 supplies an explicit positive-root kernel model for all fixed-height Kronecker triples, extending the binary F-001 construction. Its exact rank algorithm is polynomial in N for fixed heights, with table count at most (N+1)^(pqr-p-q-r+2).
- A-019 proves that a normal domain with one-dimensional lattice-graded pieces is a semigroup algebra with support saturated in its generated lattice; ambient saturation additionally follows from lattice primitivity. The proof identifies the missing positive-basis data and the separate grading-projection requirement.
- M-009 complete proof received targeted independent-agent reading and passed; event recorded. New Foulkes-Howe preprint audit is next.

## Shape-sensitive Chow gate, 2026-11-21T00:02:30.482359+00:00

A-020 proved in SHAPE_CHOW_BOUND.tex and fully self-read: the complete lambda isotypic part of I(Chow_n)_d vanishes if n >= lambda_2 + binom(d,2). Consequently the actual determinant multiplicity equals the ambient multiplicity there. The proof refines the verified differential argument by identifying the kernel as S_(q,p) and controlling its second row under polynomial spectators. Combined with M-010, surviving actual obstructions require d(d−1)>n and lambda_2>n−binom(d,2). Independent-agent stress check requested.

## Adaptive differential gate, 2026-11-21T00:06:14.373056+00:00

A-021 in ADAPTIVE_CHOW_BOUND.tex strengthens A-020: K_n(lambda)=ambient when n>=B_d(lambda_2), where B_d(L)=L+sum_{j=2}^{d-1}min(j,L). In particular n>=(d−1)lambda_2 suffices. Choosing exponent s=min(d−1,lambda_2) in the binary factorization makes both differential sequences injective on the required isotypic type. Root proposed the adaptive choice; full proof and self-read check completed here. Exact sum/closed-form/recurrence checks recorded. The surviving actual obstruction gate includes B_d(lambda_2)>n and therefore (d−1)lambda_2>n.

## Optimized recurrence and broad degree gate, 2026-11-21T00:24:12.345810+00:00

A-022 in OPTIMIZED_CHOW_BOUND.tex is proved and self-read. It replaces the final derivative condition p>lambda_2 by p>min(q,lambda_2), giving N2(L)=1 and N_a(L)=s+max(N_(a−1)(L),min((a−1)s−1,L)), s=min(a−1,L). Since positive padded-permanent types have lambda_2<=dm, n>=N_d(dm) excludes every actual multiplicity obstruction of degree d. The weaker clean sufficient bound n>=dm+binom(d,2)−1 is already a consequence of A021. An exact two-candidate integer formula and square-root upper bound are proved. 29302 integer consistency checks passed.

## Grouped derivative improvement, 2026-11-21T00:32:10.200679+00:00

A-023 in GROUPED_CHOW_BOUND.tex proves a sharper bound by checking each power D^s at once, using its exact Pieri kernel. The recurrence replaces min((a−1)s−1,L) by min((a−2)s,L). For L=dm>=d it unrolls to binom(d,2)+max(0,max_j min(binom(j,2),dm−binom(j,2))). Hence n>=floor(d(d+m−1)/2) excludes every actual multiplicity obstruction in degree d; the exact maximum can be stronger. The uniform Chow bound also improves to (d−1)^2. Full proof/self-reading and29302 exact arithmetic checks are saved.

## Constructive positive algebra and joint profile gate, 2026-11-21T00:56:54.320567+00:00

F-019 records the known full rectangle-square zero/one rule and exact stretching parity; supplied GCT IV locators are independently checked. A-024 constructs the explicit normal polynomial highest-weight algebra C[Delta1,Delta2,Delta3,D4], showing relative saturation and the index4 defect in the ordinary even-total weight lattice. Both parent and formulas independently read these complete proofs PASS. A-025 proves the joint actual-obstruction gate lambda3>=420 OR lambda52>=3 in the BIP range, using the root-proposed two-tree support cover; proof and exact integer certificate are saved. Further total-degree pruning is under investigation, with no stronger bound yet claimed.

## Total-degree-pruned joint gate, 2026-11-21T00:59:41.133391+00:00

A-025 now strengthens its complete coarse420 result to lambda3>=539 OR lambda52>=3. Fixed caps u325,v212 cover B538. The proof counts the actual total-degree-pruned order ideals, checks142 exact integer cases m190..331, and proves the normalized bound decreases for every real m>=331. Code and expanded certificate are saved. An alternative allocation of the early variable to the other tree is being investigated; no further result is yet claimed.

## Final fixed-cap refinement, 2026-11-21T01:02:58.666801+00:00

A-025 final explicit joint gate is lambda3>=557 OR lambda52>=3. The alternative allocation places all early degree in Q and uses caps u360,v195. Its proof checks171 exact integer cases m190..360 and a termwise decreasing tail. The previous420/539 intermediate bounds are retained with their proofs. Per root direction, further constant-only optimization stops here; these are explicit corollaries of the already stronger full F018 kappa criterion. The next substantive question is whether A024 extends to height-three rectangles.

## Height-three positive family, 2026-11-21T01:10:48.504895+00:00

A-026 in HEIGHT_THREE_RECTANGLES.tex proves g((h,h,h),(h,h,h),(h,h,h))=# {(a,b,c)>=0:2a+3b+4c=h}, with explicit parity-dependent floor formulas. Known primary input: Domokos-Drensky Section2, Theorem1 and Remark2(ii), p6, polynomial SL3-cubed invariant ring of degrees6,9,12. The extraction, all-copy basis, residue calculation and saturation analysis are fully proved/self-read. Its scalar support is {0,2,3,...}, has primitive group Z, yet misses1 although the actual Kronecker invariant ring is smooth normal affine3-space. Higher multiplicities (already two at h4) show precisely why A019/A024 multiplicity-free hypotheses do not extend. Seven character checks through S18 and241 arithmetic checks saved.

## Growing-height rectangular families, 2026-11-21T01:19:08.522393+00:00

A-027 in CASTLING_RECTANGLE_FAMILY.tex proves the complement identity via rectangular Schur duality and transports A026 along positive Markov mutations. Formula g(((yz h)^(3x)),((xz h)^(3y)),((xy h)^(3z))) equals the same nonnegative solution count for every mutation triple from(1,1,1); all three heights grow without bound along smallest-coordinate mutation. It also gives coefficient-one families from allowed positive complements of format(1,2,2), with all heights unbounded. Proof preserves whole coefficient spaces by perfect duality; multiplication compatibility and polynomial ring isomorphisms are explicitly not claimed. Full self-read and finite convention checks saved.

## 2026-11-21T01:51:20.229539+00:00 — A028 checked extraction

Wrote and fully self-read ORBIT_CLOSURE_GAP.tex. The transposition action on DD2011 polynomial generators is (+,-,+); homogeneous invariant degree3h is pure sign(-1)^h. Double conjugation preserves the symmetric-square involution. Combining F011 and O007 yields an explicit unbounded orbit-versus-closure loss, without claiming q>K. Independent root reading requested.

## 2026-11-21T01:59:12.516208+00:00 — Original cote133 recovered

Downloaded official54-page PDF (53manuscript/offprint pages pluscover); all relevant originals006,008,009,019–029 visuallyread. q_H^n is no longer an undefined-name gate: A029 proves its recovered injection-orbit construction and distinguishes polynomialdegree from ordinary homogeneity. Previous mathematical corrections remain valid. Othercote originals remain unverified and are explicitly tracked in QA030. No extra checkpoint or redistributed facsimile was created.
