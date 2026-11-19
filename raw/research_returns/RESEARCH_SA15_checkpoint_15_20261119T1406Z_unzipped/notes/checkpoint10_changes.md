# Checkpoint10 changes

This checkpoint remains **INCOMPLETE**. The open main rows areA.3,A.4,B.3 in higher dimension, andB.4. Every previous completed case remains in the paper. The actual review05 was performed09:53:35UTC; movement was present and the no-movement streak remained0. The next review is due10:50:40UTC. Review05 deliberately excluded the post-checkpoint09 candidates from its movement count.

## New proved reductions

For the fixed supersingular product E0×E0 in characteristic two, the complete invariant-covector space is now determined in every degree: dimension0 in odd degree and1 in even degree, for both geometric and arithmetic monodromy. The even covector is the explicit double invariant derivative of the defining section. A separate complete proof places an actual naturalGL8(F2) block with trivial complement in every degree. This excludes invariant nondegenerate alternating forms on the full representation and on the even common kernel. Full higher-degree images and irreducibility remain unresolved; neither statement is promoted beyond its scope.

One fixed mixed surface is now settled in all degrees over the perfect fieldF2(t)^perf: Et:y²+txy+y=x³ times E0:y²+y=x³, embedded by the cubic product polarization. Its relative ranks are9d²−1 in odd degree and9d²−2 in even degree. The same proof applies to every transcendental ordinaryj; it does not include all algebraicj. The proof uses specialization of a relative coherent vector bundle at the supersingular fibre and a connected-Prym upper bound. The same generic elliptic factor is used in every degree.

The characteristic-two theta-surface prerequisites have complete proofs: a direct genus-two second-jet construction at every point; all two-first-jet rank strata and their dimensions; finite exceptional second points for ordinary surfaces; three distinct value separation; an irreducible discriminant with generic integral one-node ordinary curve; and ordinary generic members in every degree. The elementary product-versus-Jacobian dichotomy covers every principally polarized surface over the algebraic closure. These proofs do not import a characteristic-zero jet theorem.

The level-three theta-group calculation gives a symmetric Cartier matrix in every dimension, with diagonal equal to the coefficient vector after ordinary Cartier normalization. Its determinant is geometrically squarefree. The Frobenius-twisted target is typed explicitly and the dual identification uses only the finite centralmu3. This supplies the degree-one Hasse input for the broader ordinary-ppav image theorem. The combined theorem has now passed three complete proof audits (root, obstruction/crystal, reduction/descent) and is included as proved. For every ordinary principally polarized abelian surface in characteristic2, in the3Theta embedding, the eventual geometric image is GL_(9d²−1)(F2) in odd degree and the full pointwise stabilizer of three independent covectors in even degree. The entire arithmetic even image is the preimage of the actual Galois permutation subgroupGamma ofS3 on those three characters. The terminating polarized3-isogeny search supplies multipliern, and the explicit ambient threshold ismax(n+1,reg(I_A)−1). The auxiliary isogeny is allowed over a finite extension; the arithmetic conclusion remains over the original perfect field. Hasse and common-kernel irreducibility hold fromd2 in the complete systems. No arbitrary-surface or characteristic-odd extension is claimed.

B.4 now has a sharper universal finite upper bound from Bondarko's exact exponent, and the small casep3,e2,h2 satisfies2<=nu_min<=4 in manuscript indexingM(nu)=M[3^(nu+1)]. A27-torsion comparison already separates a potentially supersingular group from a height-one-filtered group. Any possible81-torsion character failure must involve two potentially supersingular groups with faithful inertia orders12 versus3 or6, and joint faithful image of order36. This is a strict restriction on the remaining tests, not an existence or exact-index claim.

## Checks, source access and retained execution evidence

All new full proofs were read by the root and independently audited by another agent. The root's new jet proof was audited in full by the obstruction/crystal agent, including its later additions. Root exact executions are retained with their scopes and inputs in their programs and JSON outputs:

| Program | Exact scope | Root time in seconds | Retained root output |
|---|---|---:|---|
| supersingular_cartier_operator_checks.py | Four local Cartier identities; six bounded one-factor symmetrizer systems |0.06592429800002719|outputs/root_supersingular_cartier_operator_checks.json|
| verify_height_two_small_bounds.py | Quaternion identities,16000 valuation cases,49 joint bounds,36 determinant comparisons |0.05361534700205084|outputs/root_verify_height_two_small_bounds.json|
| level3_theta_tensor_checks.py |243 Heisenberg matrices,81 triples,5 tensor orbits, universal diagonal |0.09402520599905984|outputs/root_level3_theta_tensor_checks.json|
| verify_height_two_character_gate.py |8 cyclotomic trace/norm cases,27 joint-order cases, two possible81 pairs |0.03912722799941548|outputs/root_verify_height_two_character_gate.json|
| ordinary_ppav_group_checks.py |Six Galois permutation actions, exactGL8 prime factors,5100 degree bounds |0.0008845510019455105|outputs/root_ordinary_ppav_group_checks.json|
| A3_mixed_generic_checks.py | Weierstrass invariants,j denominator exclusion,10000 nodal identities |0.03762406500027282|outputs/root_A3_mixed_generic_checks.json|

The initial root runs of the theta and small-character gate programs took0.10192141500010621 and0.046019093999348115 seconds respectively. They were rerun when the checkpoint wrapper added the mixed-surface certificate; the mathematical outputs agree. The author outputs were preserved. The finite cases are not substituted for any geometric proof.

The source log ROOT_SEARCH_LOG_10.md records the full searches, exact primary passages and access limits. In particular, BondarkoA/B/E and the required proof were read; LazardIV was read for arbitrary algebraically closed residue fields; the theta-group theorems and Jacobian-theta facts were checked in the AV draft; Oda1971Section1/Theorem1.2 was checked in arbitrary dimension and characteristic. The two characteristic-zero jet papers found in the search are explicitly excluded from the characteristic-two proof.

## Superseded candidates and preserved limits

supersingular_even_covector.tex is retained as a preliminary but superseded in the paper by supersingular_exact_covectors.tex, which determines the entire invariant space. No earlier checkpoint is overwritten or removed. The exploratory fixed-algebraic mixed-factor probes remain finite checks only. The generic all-ambient rank and full-image questions remain on the outcome table, as do higher-dimensional sharp reduction thresholds and the least character index. No original scans have been obtained; no priority claim is made.

## Typesetting verification

Initial builds exposed three typesetting issues before publication: the mixed-family file used an undefined mathscr macro, replaced by mathcal, and B32 lacked the closing display delimiter after(B-RD32.2), now inserted; and the undated Conrad exposition needed an explicit n.d. bibliography year for author-year citation formatting, now supplied. These corrections do not change the mathematics. The successful final build and actual rendered-page inspection will be recorded below.

Final build passed in27.433 seconds:258 pages,1,979,949 bytes, no overfull boxes, no undefined references, and no undefined citations. All38 selected rendered pages were actually inspected:24 by the root,8 by the obstruction/crystal agent, and6 by the reduction/descent agent. Typography, displayed formulas, page breaks, and bibliography passed. A truncated multi-image tool response was not counted; the root subsequently viewed all six assigned montages individually. The exact page lists and observation time are retained in outputs/visual_qa_checkpoint10.json.
