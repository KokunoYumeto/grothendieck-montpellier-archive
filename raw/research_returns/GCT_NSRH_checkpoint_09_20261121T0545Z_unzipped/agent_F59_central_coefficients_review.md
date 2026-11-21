# Fresh full review: central polynomial coefficients

Reviewer: /root/grothendieck_dictionary, GPT-6 Astra Pro; inherited reasoning-effort setting not exposed. Date: 2026-11-21 UTC.

Complete final report: agent_soergel_central_coefficients.md, SHA256 d276c3b9a8b85081eaab8e7cc7937e4cc4d3abc7c9a449a9137e4ae5301bef03.

Result: PASS, no mathematical correction requested. I read the entire original report at 5a050724d95c9ae94ff104a094ea272c9056b799fabcdd895ad30ea34db0873f, then directly read the final source-only Stacks00NX insertion and checked the final hash. Every proof and the exact remaining scope were independently reconstructed. I then read the entire final 430-line generated fragment and the complete new bibliography entry; their final-text match is recorded below.

## 1. One-Koszul centrality

The ordinary reflection correspondence is the stated commutative ring R_s=k[x,x',y]/(x^2-x'^2), up to its harmless common shift. It is free over both copies of A, so multiplication by either nonzero polynomial is injective. The two tensor complexes therefore have exactly the cyclic degree-zero quotients claimed.

The two A-actions generate R_s; a bimodule isomorphism is an R_s-module isomorphism, so it equates the annihilator principal ideals. If f(x,y)=a f(x',y), homogeneity and regularity of f(x',y) force a to have degree zero. The ring's degree-zero part is k. Restricting to the diagonal forces a=1, and restricting to the reflection graph gives s(f)=f. The converse uses the actual balanced tensor over A^s. This proves the iff without a generic argument.

For f=x, I checked the two quotient modules and the left x action: it is zero on one and nonzero nilpotent on the other. On the separate reflection graph, the sign change is repaired by the displayed degree-minus-one chain map. Both generic complexes are acyclic. These comparisons correctly demonstrate why generic or graph tests miss actual reflection-correspondence centrality.

## 2. Coherent invariant descent

For S=k[x^2,y^2], the basis 1,x,y,xy makes A free over S. Elements of S act equally from the left and right on each ordinary generator, and this persists under all stated constructions and maps. I checked both balanced tensor identifications in PC13, including which A-action is carried onto X.

The signed interchange k tensor x maps to (-1)^(pq) x tensor k. It is a chain map and A-bimodule-linear; naturality uses the equal invariant actions. Moving the same labeled coefficient through an iterated product yields the same order and the sum of the same Koszul signs, giving the unit and half-braiding identities. This is actual central movement of invariant-descended complexes, not a claim that every diagonal complex is central.

The general type-A statement uses the central invariant action, and the coefficient complex is bounded free over the invariant ring before base change. It does not require an unproved descent theorem for arbitrary differential matrices.

## 3. Flat coefficient cohomology

I independently opened and read Stacks Lemma10.78.2, tag00NX, parts(1)--(3), at https://stacks.math.columbia.edu/tag/00NX, direct source turn425734029view0. It supplies exactly finite-presented flat equals finite projective equals a summand of finite free. The polynomial ring is Noetherian, so the finite cohomology modules are finitely presented.

The homogeneous degree-zero component of an ordinary splitting is a graded splitting. Lifting a homogeneous origin basis and applying graded Nakayama proves graded freeness. A bounded complex with projective cohomology splits as a module complex; because the entire coefficient complex has diagonal action, those A-linear maps and homotopies are automatically bimodule-linear. Therefore PC14 really replaces C by a scalar coefficient complex of the same Euler class. The all-rank scalar theorem applies independently of any separately chosen central structure.

## 4. PC-D: no flatness assumption on C

I reconstructed the complete proof of the delicate PC17 step. Localization of diagonal C is a scalar Q-vector-space complex. The generic positive-measure calculation determines only the two graph supports of X and does not retain internal grading. Assumed left-flat cohomology of X becomes actual graded free graph modules by the global two-root lemma, hence is also right-free.

The tensor square consequently has free graph cohomology by the canonical Kunneth map. On the other side, the projective cohomology of the second X is split only as a left A-module complex. Tensoring by the right A-complex C preserves this homotopy decomposition. Each resulting tensor with a left-projective M_i has cohomology H^j(C) tensor M_i, with no flatness required of H^j(C). The surviving left action is the left action on C, so the auxiliary computation is left-linear. The intrinsic cycle cross-product is itself a bimodule map; only its left-module isomorphism is needed.

Choose one nonzero actual graph summand in one M_i. For each j, the corresponding total-degree direct sum contains a shifted copy of H^j(C) as an actual left-module direct summand, because right tensoring with a graph only changes that module's right action. The quadratic identifies the whole direct sum with a free left module. Thus each H^j(C) is projective, then graded free. This is an actual summand argument, not an Euler-rank comparison and not bimodule formality.

The conclusion is correct: under the designated target class, flat cohomology on either side is impossible. The explicit coupled Rouquier object is thereby excluded for every perfect diagonal coefficient of the specified Euler class.

## 5. The actual different-class quadratic

The invariant polynomial x^2 is regular in S. The Koszul complex has H^0=S/(x^2); its shift contributes that quotient in degree -1. Thus U_S has the stated cohomology and Euler class1. Flat pullback gives nonzero A/(x^2) torsion.

Every term of U tensor B_1B_2 is an ordinary Soergel term, and the differentials are actual invariant polynomial bimodule maps. Central movement of U and the ordinary two-reflection square decomposition supply the full chain isomorphisms in PC23. The scalar coefficient D_sc has character delta squared and occurs in cohomological degree zero, so no unmentioned Koszul sign changes this relation.

I checked both Euler classes separately. C' has the required coefficient Euler class, but X' has b_1b_2, whose generic Euler support differs from the designated P. The construction therefore does not contradict or solve the target problem. Its nonflat cohomology is explicit on both sides, consistent with the precise premises of PC-C and PC-D.

## 6. Remaining scope and dictionary

The nonflat/nonflat case with the target generator class remains open in this note. Specializing invariant parameters does not preserve the regular polynomial ambient ring or the equality of global and generic highest coefficient degrees, so the scalar proof is not silently reused. The natural singular invariant correspondence is not promoted to a derived quadratic by ordinary reassociation.

The EGA affine, SGA6 perfect, and SGA3/SGA6 grading/K0 locators remain framework anchors. Ordinary Soergel normalization and graph-source locators are the already audited ones. The known Stacks equivalence is cited accurately; no archive or source is credited with the new centrality and nonflatness deductions.

This is a full manual proof review plus the stated fresh primary-source check. No numerical test, compilation or visual-layout audit was performed for this report. No main paper or shared master log was edited.

## 7. Complete generated-fragment and bibliography match

PASS at the final hashes:

- finding_F59_central_coefficients.tex, SHA256 69963bc08fc1d5c6385bcdc06f40a701ba1b8e2fc5d5a325d1e4d268551fdf3c.
- finding_F59_central_bib.tex, SHA256 0714bea556c15ee85bc01dfc683c44fa3a69a8e34316468a9e1528ab7f8761c6.

I read every line of the complete fragment, including both centrality directions, all chain and coherence maps, the two flatness arguments, the nonflat different-class example, every residual-scope paragraph and the separate dictionary. The final title-only delta explicitly names F59 in the dictionary heading. The proofs retain the exact premises and claims of the reviewed report, especially the use of only one-sided splitting in the nonflat-C Kunneth step and the different Euler class of the constructed generator.

The bibliography gives the same Stacks00NX parts(1)--(3) that I freshly opened. No additional mathematical claim, source attribution or scope change appears in the generated text. I did not independently compile or visually inspect this peer fragment; the author's reported isolated compile is not represented here as my own check.
