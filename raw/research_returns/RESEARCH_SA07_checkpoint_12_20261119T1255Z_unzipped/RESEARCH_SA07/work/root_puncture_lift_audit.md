# The exact target of the cuspidally central lifting theorem

Root continuation, 19 November 2026. This records an attempted extension of the actual CM-quotient map in F.3.18. It does not change the A.22 status.

The primary author preprint Borne--Emsalem--Stix, *Lifting Galois sections along torsors*, arXiv:1301.4429v2, was opened in full. Section3.2 and Proposition3.5 (authorp6) identify the cuspidally central quotient with the fundamental group of the explicitly constructed torus torsor F_D. Theorem5.10 and its proof (authorpp12--13) lift an existing section over Q for a divisor that is a union of torsion sub-packets. The proof passes through the pullback of the arithmetic first Chern class, its torsion-free cohomology target, and the relative Brauer-group vanishing over Q. These hypotheses and this target are retained.

For the target needed in F.3.15, the effect of the quotient can be computed exactly. Let E be an elliptic curve in characteristic zero, U=E minus its origin, and P_l the geometric pro-l fundamental group of U. It is the free pro-l group on x,y. The filling map P_l to the geometric pro-l fundamental group of E is its abelianization, with kernel P_l' and target Z_l squared. The maximal cuspidally central geometric quotient is

    P_l / closure([P_l,P_l']) = P_l / Gamma_3(P_l).

Indeed this quotient makes the filling kernel central; every quotient with that property kills all displayed commutators, which proves the converse factorization and the universal property. Its completed rational Lie algebra is the free Lie algebra on x,y modulo all degrees at least3. Consequently the boundary-fixing degree4 derivation T4 of F.3.15, whose values on x,y have degree5, maps to zero under the induced derivation map. The degree5 conjugacy equation that produces the CM normalizer obstruction therefore has zero image under this particular quotient map.

Thus the opened lifting theorem supplies a precisely typed intermediate lift. Applying that intermediate lift to the present argument still requires a further lift to the full punctured fundamental group that retains both the procyclic subgroup and an open arithmetic normalizer. No such further lift has been constructed here. Moreover the present normalizer extension has not been supplied with the Galois section that is an input to Theorem5.10. The theorem is recorded as a checked source route; neither missing input is asserted impossible.

For the geometric map b from F.3.18, the necessary domain remains the inverse image of E minus its origin. Removing that whole fibre gives an actual map to U, but the present subgroup is given in the group before this extra removal. The exact quotient above shows why replacing the required lift by the available cuspidally central target loses the already proved degree4 obstruction.
