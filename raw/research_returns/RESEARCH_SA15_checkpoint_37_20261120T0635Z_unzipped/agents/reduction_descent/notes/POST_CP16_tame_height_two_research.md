# Post-CP16 research: minimal cyclotomic ramification and tame height two

Status: research only; no new theorem or numerical bound promoted. Existing promoted TeX and registers are frozen for CP16.

## Target

For p>=5, e=p-1, h=2 and mu_p contained in K, B18 gives least index >=1. The next exact question is whether p^2 already determines the prime-to-p special-inertia character. It is not legitimate to replace every height-two potentially formal BT group by an elliptic curve: finite tame special inertia can lie in all of F_(p^2)^*, and its reduced norm can be nontrivial.

## Useful deductions to verify fully

Finite inertia in the height-two supersingular division algebra is tame when p>=5 (a p-torsion element would generate a cyclotomic extension of degree p-1>2), hence cyclic and of order dividing p^2-1. Two tame good extensions over a strictly henselian complete base have cyclic compositum, with degree dividing p^2-1. The existing Bondarko comparison with u=2 would therefore give a sharp-to-one-step upper range for whole potentially good height-two pairs at e=p-1; mixed monodromy extensions still require a complete separate proof. No such statement has yet been written or audited.

The logarithm equality boundary is delicate. With m=p+1 and norm-one types, e_L=p^2-1. The general multivariable recurrence has q1=p+1 equal to e_L/(p-1), rather than strictly greater. Individual one-dimensional groups may have a stronger Hasse-coefficient divisibility from tame weights, but the graph quotient can have cross-coefficients of valuation one. The old target-thickness warning from B34 remains applicable; no improved exclusion follows merely from thickness of the original two groups.

## Searches and opened originals

At approximately14:43-14:47UTC searched: potentially Barsotti Tate congruent mod p squared inertial type tame height two ramification Fontaine Laffaille; Breuil tame inertial type mod p representation potential Barsotti Tate height two congruence; Lubin Tate curve level 2 stable reduction inertia ramification types height two p torsion; mod p2 congruence potentially good reduction elliptic curves p>=5 local inertia type.

Opened and read Tong Liu, Potentially Good Reduction of Barsotti-Tate Groups, original arXiv math/0604593v1, https://arxiv.org/pdf/math/0604593, webref turn319625289view0. Read introduction pp2-5, Theorems1.0.1/1.0.3/1.0.5 and Proposition1.0.6, constants discussion, and start of Section2. This supplies general finite-level existence/descent, not the desired least p^2 threshold. No claim to having read all29pages. A Wiley DOI find on local constants returned an internal redirect error and was not read.

Opened and read Ito-Mieda-Tsushima, On the cuspidal representations of GL2(F) of level1 or1/2 in the cohomology of the Lubin-Tate space X(pi^2), arXiv1109.5265v1, https://arxiv.org/pdf/1109.5265, webref turn861747587view0. Read introduction pp1-3 and Sections2.1-2.2 pp4-5 only. It explicitly gives stable-reduction components and division-algebra/inertia actions at level2; a possible future route, not a proved criterion here. Its displayed level-transition indexing appears reversed in the extracted passage, so no formula is imported without checking the scan. The equal-characteristic level-two paper was found but is not the source for the present mixed-characteristic problem.

No new exact experiment has been run for this target. The already retained mixed-monodromy audit outputs are separate and prove no B4 statement.

## 2026-11-19T15:14:32.903964+00:00: completed first gate

B49 now proves the mixed p² exclusion and least-index interval1--2 after root/OC full audits. Its actual source/code/proof files and runtimes are in STATUS_CURRENT/CHECK_EVENTS. Hopkins–Gross original indexed full text was successfully opened as turn137356384view0 and exact5.7/12.10 passages as turn355608354view0--2; direct download503 and screenshot timeout. Original author bibliography item46 confirms volume158pp23--88. The source explicitly allows arbitrary residue-field extensions. Bondarko original E(1)/Prop18/full proof reread via turn974694321view1--2.

Remaining two-formal-pair gate: equal finite determinant and disjoint special tame spectra should split every graph closure by integral idempotents, generalizing B33; at levelp² graph special fibre is M0[p]×N0[p]. QuotientQ special fibre remains a product. The generic one-step logarithm q1=p+1 gives no exclusion when jointdegree m>=p+1. Tame weights constrain Hasse coefficients of Q but cross coefficients may have valuation1; no thickness of original factors is imported into Q. This is an unresolved research route, not an extra theorem.
