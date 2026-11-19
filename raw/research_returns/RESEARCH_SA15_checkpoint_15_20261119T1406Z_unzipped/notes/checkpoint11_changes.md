## Current state

This checkpoint remains **INCOMPLETE**. The open main rows remain A.3, A.4, B.3 in higher dimension, and B.4. No arbitrary-ambient classification is inferred from the new abelian-surface theorems. This note records only fully audited mathematics; pending further candidates are listed separately.

## Exact rank formula for all principal surfaces

For every principally polarized abelian surface (A,Theta) in characteristic two, let L=3Theta and let f_A be its geometric2-rank. In the complete linear system |L^d|, every positive degree has generic relative stable rank9d²−1 when d is odd and9d²−3+f_A when d is even. The coherent relative dimension is9d²−1. Thus Frobenius is generically bijective precisely in odd degree or when A is ordinary. This closes the previously explicit algebraic mixed-factor refinement, including every ordinary j-invariant. For the fixed ambient embedding, surjective restriction is guaranteed at d≥max(1,reg(I_A)−1); products have surjective restriction in every degree. The entire proof, including the exceptional Pfaffian tensors, the relative determinant, odd norm construction and even connected-Prym bound, passed root and independent monodromy audits.

## Entire invariant quotients on nonordinary principal surfaces

For every nonordinary principally polarized abelian surface in characteristic two, the complete geometric and arithmetic invariant-covector spaces have dimension0 in every odd degree and2^{f_A} in every even degree. In particular the two-rank-zero cases both have one covector, including the nonzero nilpotent chain, and the two-rank-one cases have two. The arithmetic action on these invariant spaces is trivial over the original perfect field. The proof handles an arbitrary persistent nilpotent length before reducing to the entire four-dimensional distribution algebra of the Frobenius kernel. Both other Part-A agents independently audited the complete proof, its relative-Frobenius conventions, the local identities and arithmetic descent. The whole group in these general nonordinary families remains open.

## Two further exact supersingular groups

On the fixed product E0×E0, E0:y²+y=x³ overF2, with the cubic Segre embedding, the degree-two rank is33 and both complete images areF2^{32} semidirect GL32(F2), the full pointwise stabilizer of the unique covector. The proof uses one irreducible nonreciprocal degree32 Frobenius polynomial with primitive prime65537, and a second literal matrix witness showing that an arithmetic Frobenius has no fixed lift of the invariant quotient. The already proved actual geometricGL8 block and the self-normalizing-complement argument force the full geometric group.

The degree-three geometric and arithmetic groups are bothGL80(F2). Its retained Frobenius certificate has an irreducible nonreciprocal degree80 polynomial with primitive prime4278255361. Together with the same actual geometric block this gives the entire group. These two proofs passed independent root and reduction/descent audits. Exact full groups in degrees one through three are settled; no conclusion for every higher degree is inferred from the finite searches.

## The height-two comparison graph

In the remaining norm-one, potentially supersingular height-two comparison with different tame special-inertia orders, a level3^n isomorphism forces the special graph at every smaller level r to be ker(F_M^r)×ker(F_N^r). Its rank-nine successive finite-flat quotients have special fibre alpha3²; multiplication by3 is generically an isomorphism and specially zero. This is proved using integral pairings on full Barsotti–Tate groups, flat graph orthogonality and tame projectors. It is not by itself counted as a new numerical exclusion of a least index.

## Retained root computations

| Program | Exact scope | Root runtime, seconds | Complete root output |
|---|---|---:|---|
| A3_ppav_rank_checks.py | Nine symbolic Pfaffians,945 matchings,40 actual exceptional projectors,1700 supplementary determinant values,30000 dimension identities |0.29324621799969464|outputs/root_A3_ppav_rank_checks.json|
| ppav_nonordinary_covector_checks.py | Sixteen universal local operator identities; twelve finite illustrations of the separately proved monomial elimination |0.09968187000049511|outputs/root_ppav_nonordinary_covector_checks.json|
| verify_supersingular_degree_two_group.py | Two independently reconstructed36×36 integer characteristic polynomials; primitive prime and fixed-lift equation |0.08990957599962712|outputs/root_verify_supersingular_degree_two_group.json|
| verify_supersingular_degree_three_group.py | Independently reconstructed81×81 integer characteristic polynomial; Rabin and primitive-prime checks |0.4399738840002101|outputs/root_verify_supersingular_degree_three_group.json|
| A3_separable_rank_checks.py | Integral dual-polarization matrices for65 odd types and24960 exact degree/genus/rank identities |0.022721224999258993|outputs/root_A3_separable_rank_checks.json|
| verify_supersingular_log_bound.py |282 multivariable monomials,18432 coefficient cases,40000 logarithm-degree cases and every surviving small ramification value |0.04593844600094599|outputs/root_verify_supersingular_log_bound.json|

The root rerun wrapper redirected each output, preserving author files byte-for-byte. All discovery programs, original outputs, independent verifiers and their actual runtimes are retained. The original degree-two read-only discovery output was preserved separately after the checkpoint10 freeze. No unsuccessful route is silently removed.

## Sources and limits

ROOT_SEARCH_LOG_11.md records every new root query, exact opened source passage, access limitation and proof audit. The new rank proof uses Debarre1994 Section3 equations3.2–3.3, printed pp346–347, after checking the arbitrary-characteristic scope. The endomorphism proof uses the explicit torsor/adjunction calculation and the opened finite-isogeny duality and Frobenius/Verschiebung duality in the AV draft. The graph proof uses Tate1967 Theorem4/Corollaries1–2, pp181–182, on full p-divisible groups, and Sections1.2–1.3, pp159–160, on finite-flat duality. No original manuscript scans were supplied. Michel Hua's project remains unused. No priority claim is made.

## Further promotions after the actual hourly review

The full rank theorem now extends to every abelian surface in characteristic two with ampleM of odd Euler characteristicD=chi(M), in the complete linear systems of L=M³. The exact ranks are9Dd²−1 in odd degree and9Dd²−3+f_A in even degree. The integral dual polarization produces a finite étale principal source of degreeD, and its norm construction supplies the sharp odd-degree rank. The even-degree obstruction uses the dual polarizationmD lambda_M^{-1} on the connected Prym. Root and monodromy independently checked the entire proof and certificate. Even-degree polarizations and arbitrary embeddings outside the stated third-power/regularity scope remain unresolved.

The sharpened height-two logarithm estimate is also proved after complete root and obstruction/crystal proof, primary-source and certificate audits. For a target whose special fibre is a product of height-two one-dimensional formal groups, the coefficient valuations followq0=1 andq(i+1)=min(a+q(i),1+3q(i),9q(i)). The completed Cartier-module argument kills the special kernel byFrob^u as soon asq(u)>a/2. At absolute ramification72, q3=40>36; combined with the exact graph this excludes every81-torsion ambiguity. Consequently2≤nu_min(3,2,2)≤3. A27-torsion failure, if it exists, has joint good-reduction image of order18 or36. No such example or a decision between indices2 and3 is asserted.

The actual hourly review06 was recorded at10:54:50.999203UTC, against review05, and found mathematical movement with no-progress streak0. It explicitly excluded the two extensions just described at its drafting stage. Its original record is retained unchanged; these later promotions will be assessed only at the next actual review. The next hourly review is due11:50:40UTC.

## Final checkpoint verification

The final paper has281 pages and2,133,847 bytes. The reproducible build passed in28.172 seconds with no overfull boxes, unresolved references or unresolved citations. All35 selected rendered pages were actually inspected, including the complete new sections:16 by the root,8 by the obstruction/crystal agent,8 by reduction/descent and3 by monodromy. The exact page lists and observation time are retained in outputs/visual_qa_checkpoint11.json. An initial bibliography-underscore build failure was repaired; its complete transcript remains in outputs/build_console_cp11_failed_bib_underscore.txt.

The final register contains319 numbered statements; the source census has139 rows, including the explicit unused Hua witness. The code export copied106 agent program/output files verbatim in addition to root programs and outputs. The local self-tacnode monodromy argument remains a clearly labelled, unintegrated candidate; no global Hasse-divisor or higher-degree full-image conclusion is inferred from it.
