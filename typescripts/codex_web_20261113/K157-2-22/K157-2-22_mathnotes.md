# K157-2-22 · Mathematical notes

## What the pages do

**U1 · Composition of paths, 338–339.** Starting from a functor invoked on manuscript page 61, Grothendieck describes composition on the fibres over a pair of types. Paths from \(a\) to \(b\) and from \(b\) to \(c\) give a path of the concatenated type from \(a\) to \(c\). A diamond glues the intervals at their endpoints. The second diagram tracks maps between pairs of paths; the operation on these maps is written \(w''=w*w'\).

**U2 · Passage to the total categories, 339–342.** The two projections from the product of type categories and the composition map \(\Pi\) define three pullbacks. A square expresses compatibility with change of type. The author crosses out a direct construction on arrows when he recognizes the source as an ordinary product of path categories. Projection from the target fibre product then supplies the desired functor. He formulates a further associativity check.

**U3 · Uses of the path formalism, 343.** A three-part list returns to composition, categories of fractions and composition of homotopies. For a variable indexing category \(X\), the author introduces \(M(X)\) with its displayed identification with \(\underline{\mathrm{Hom}}(X,M)\). Comparing different path categories and retaining the dependence on \(X\) remain future work.

**U4 · Lemma 1 and its mapping category, 344–345.** Lemma 1 says that two morphisms of types \(f,g:\tau\rightrightarrows\tau'\) are homotopic. The category in question has increasing maps of oriented intervals as objects. The author describes an arrow by its components at vertices, its identity condition at the endpoints, and the naturality square. He also identifies the larger fixed-endpoint category with a category of paths in \(I_{\tau'}\).

**U5 · Nonemptiness, 345.** Proposition 1 uses the lengths \(r,r'\). One possibility is \(r\geq r'+1\); the other is \(r=r'\), with matching initial direction when \(r\ne0\). If the initial directions differ, a morphism is forced to degenerate on the first critical interval. Removing it gives the displayed comparison with \(\underline{\mathrm{Hom}}(\tau_0,\tau')\).

**U6 · The chosen map, 345–347.** After the reduction, \(F_0\) pairs the first \(r'\) critical source intervals with the target intervals and is trivial on the remaining ones. In the positive coordinates on 346, \(f_\alpha(0)=0\) and \(f_\alpha(i)=\ell'_\alpha\) for \(1\leq i\leq\ell_\alpha\). The traveller on 347 goes to the far end on the first step, then waits. This explains the extremal property for the numerical order of vertices.

**U7 · Three conditions for the normal form, 348–349.** The nondegenerate transition arrows record where \(F\) moves; their positive extents record how far. In a), successive signs alternate. In b), the active arrow is the first transition in its critical source interval. In c), those intervals are the first \(r'\) source intervals, in order. The restriction \(F_\alpha\) names the map on each chosen interval.

**U8 · Induction on the source length, 350–351.** Grothendieck proposes successive homotopies imposing a), b), c). A long cancelled draft groups consecutive critical arrows of one sign and restricts to the subinterval between their outer endpoints. The live restart on 351 singles out the difficulty when the group includes the first and last transitions.

**U9 · Exceptional sources, 352.** The two source shapes recur with different targets. First the author wants to combine critical transitions; later he wants to move a single one to the beginning. He then returns to the maps on individual critical intervals. The supplied sequence stops at “Donc”.

## Statements left without proof

| Scan | Manuscript wording | Step left open or abbreviated |
|---|---|---|
| 338–339 | “assez évident”; “une transitivité évidente à vérifier” | Functoriality on morphisms of composable paths. The diagrams specify the proposed operation. |
| 342–343 | “il faudrait prouver l’associativité”; “fastidieux à expliciter” | Associativity on morphisms. The displayed relation gives the check to be made. |
| 345 | “Démonstration ± immédiate” | The proof of the nonemptiness criterion is omitted. |
| 350 | “le théorème de connexité est déjà prouvé”; “th. est trivial pour …” | Connectedness for a shorter source is the induction hypothesis. The smallest-length assertion is supported only by the description “vides, ou bien ponctuelles”. The letter in the length bound is doubtful. |
| 352 | “les deux cas irréductibles, qu’il faudra traiter … à part”; “Ces cas admis”; “Sous réserve de traiter ces deux nouveaux cas irréductibles” | The exceptional cases in the table below. The concluding reduction also invokes a “cas supposé traité en 2º)”. |

The first source letter in the top box on 352 looks like \(I\) or \(\tau\). The shapes and the annotations giving their targets can be distinguished independently of that letter.

| Task on scan 352 | Source shape | Written target | Critical transition(s) |
|---|---|---|---|
| Impose a), first case | \(\Delta_\varepsilon^2\) | \(\Delta_\varepsilon^2\) | First and last |
| Impose a), second case | \(\Delta_\varepsilon\Delta_{-\varepsilon}^{\ell_2}\Delta_\varepsilon\) | \(\Delta_\varepsilon^2\) | First and last |
| Move the single critical arrow, first case | \(\Delta_\varepsilon^2\) | \(\Delta_\varepsilon\) | Move \(\underline u_2\) to \(\underline u_1\) |
| Move the single critical arrow, second case | \(\Delta_\varepsilon\Delta_{-\varepsilon}^{\ell_2}\Delta_\varepsilon\) | \(\Delta_\varepsilon\) | Move \(\underline u_{\ell_2+2}\) to \(\underline u_1\) |

## Questions and conjectures

- **340–342.** “Mais cela se prolonge-t-il de façon naturelle aux morphismes ?” The question concerns the formula on objects. The subsequent product construction answers it within these sheets. The ending of the demonstrative is uncertain.
- **343.** “il me faudra développer des énoncés de comparaison” and “on sera sûrement obligé d’en venir à des Ind-catégories” concern the proposed treatment with variable \(X\).
- **347.** “Si cet espoir était justifié” introduces the hope that \(F_0\) is a final object. The possible contractibility of the mapping category is “chose peut-être vraie”. The author withdraws the inference from the numerical order and distinguishes it from the categorical order.
- **348–352.** “L’idée pour prouver la connexité … c’est de ramener tout \(F\) … à la forme normale.” Moving each critical arrow into position is the proposed route to the lemma. The exceptional cases remain explicitly assumed at the end of this batch.

## Slips

| Scan and place | Frozen form and possible correction | Assessment |
|---|---|---|
| 339, (**) | The first projection factor has a second closing parenthesis after \((a,b)\). An opening parenthesis before CH would pair with it. All three CH subscripts appear as \(\tau\); the fibre line above instead distinguishes \(\tau,\tau',\tau\tau'\). | The parenthesis is visible. The amount of intentional abbreviation in the subscripts is uncertain. |
| 340, square | Upper target \(\mathrm{Ch}_{\Sigma,\tau}(a,c)\); a target of type \(\tau\tau'\) agrees with the incoming paths and the lower row. | Medium confidence in the proposed completion. |
| 340, object sets | The addition “les ens. d’objets de” leaves “se décompose” in the running line. A plural verb would agree with the inserted subject. | Low confidence in attributing an agreement slip after the insertion. |
| 341–342 | The cancelled product on 341 puts the primed term first. The associativity line on 342 has a looped operation and a dark superscript. Uniform stars and an unadorned last \(w\) on the left would match the right side. | Low confidence. The first passage is cancelled and the second has doubtful marks. |
| 344, endpoint equality | The mark on \(w\) stands high. A lower \(i\) would repeat the component index from the preceding line. | Low confidence. Prime and raised \(i\) are the recorded readings. |
| 346, signature comparison | The running text has \(I_{\alpha'}\); the definition below has \(I'_\alpha\). The latter placement agrees with the target intervals listed above. | Medium confidence in the intended placement. |
| 348–349 | The final subscript in the first index chain on 348 resembles 2; \(s\) matches the accompanying list. The text announces “a) et b)” before giving a third condition on 349. | Low confidence about the index. The open-ended enumeration is visible, although the third condition may have occurred to the author later. |
| 350, cancelled last lines | \(I'=[f(p),f(q)]\subset I\). The surrounding construction suggests a target interval at the right. | Low confidence in any correction to the final \(I\). |
| 351–352, first interval | Scan 351 glosses the longer interval by “est de longueur 2”. The condition on 352 is “de longueur \(>1\)”, equivalent here to length at least 2. | Medium confidence in a missing comparison sign on 351. |

## Pointers

- **338.** “À la page 61, j’ai invoqué l’existence d’un foncteur” and “qui était celui de la p. 61” refer back to the path construction, specifically to the case \(\Sigma=\mathrm{Fl}(X)\).
- **340.** “(*) page 77” points to the fibrewise composition on manuscript page 77, scan 338. The inserted “cartésien (**)” recalls the preceding sheet’s starred product formula.
- **343.** “comme dans l’état premier de la question” recalls an earlier approach without giving a page or naming a text.
- **352.** “cas supposé traité en 2º)” is an internal pointer to the second step of the reduction. The supplied pages name no external author or publication.

## Remarks of the model

**R1 · Model remark, high confidence.** In the positive three-vertex case \(0\to1\to2\), an enumeration of endpoint-fixing maps gives the value triples \((0,0,2)\), \((0,1,2)\), and \((0,2,2)\). The coordinate prescription on 346 selects \((0,2,2)\). The enumeration checked all vertex assignments and the endpoint conditions for this instance of the first source shape on 352.

**R2 · Model remark, high confidence.** Reverse the arrows in both three-vertex intervals. The same three value triples define maps. With the original numbering, their numerical order still follows their middle values \(0,1,2\). The arrows of the mapping category now run from a larger middle value to a smaller one. Checking every component and naturality square gives six ordered pairs in each orientation, including the three identities. This illustrates the distinction on 347 in a finite example.
