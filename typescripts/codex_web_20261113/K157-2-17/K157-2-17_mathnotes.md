# Mathematical notes on scans 259–274

The scan numbers below refer to the sixteen supplied images of whole sheets. Statement identifiers connect the passages discussed here to their entries in CHECK_EVENTS.tsv. The marks of uncertainty in the transcription apply to quotations here as well.

## What the pages do

**Scans 259–261.** The cover carries a title about paths. The “nouvelle version” opens by assigning the vertices of a standard interval the numbers $0,\ldots,n$. A generating arrow joins each successive pair. Its sign records whether it points towards the larger or the smaller number. This gives $2^n$ sign systems. The order in which the vertices are numbered also orders the transition arrows. `I260-ORDER`, `S261-COUNT`.

**Scans 261–263.** Adjacency of successive integers defines connected sets of transition arrows. A composable chain runs in one direction. The ordered maximal runs $C_1,\ldots,C_r$ define the “longueur utile” $r$. The initial and final directions agree for odd $r$ and differ for even $r$. The point has neither direction. A chain is then compared with a functor from an ordinal simplex. `R263-ADJ`, `S263-PAR`.

**Scans 264–266.** Proposition 1(a) recognizes an endpoint using its incoming and outgoing slices. One must be a point and the other an ordinal simplex. The fork on scan 265 explains the second condition. At an interior source, the two outgoing branches give a category with no final object. The text then recovers the next vertex by removing the ones already passed and inspecting the remaining endpoint. Proposition 1(b) and its corollary concern what fixing or exchanging both ends implies. `S264-END`, `S264-F`, `R264-A`.

**Scans 266–268.** The live Proposition 2 reverses the numbering by $i\mapsto n-i$. This gives the other orientation of the same underlying category. The slanted note on scan 267 distinguishes this operation from taking the opposite category, which reverses every transition arrow. The two fork diagrams and the two orientations of a simplex illustrate the distinction. The versions of propositions crossed out on scans 264–265 and 268 are drafts. `S267-OPP`.

**Scan 269.** The domain of a chain consists of the vertices touched by its arrows. Adjacent structural chains have disjoint sets of arrows, and their domains share an endpoint. The endpoints of these structural intervals are the critical vertices. Proposition 3 compares criticality with removing a vertex and taking a categorical sum of punctured slices. `S269-SUM`.

**Scan 270.** Proposition 4 characterizes the existence of an arrow between two ordered vertices by their membership in one structural interval. Proposition 5 describes the connected components of a full subcategory and gives a criterion for it to be an interval. It must contain the critical vertices between its least and greatest vertices. `S270-DIRECT`, `S270-SUB`.

**Scan 271.** The smallest subinterval containing two given vertices contains those two and the critical vertices strictly between them. In a reduced interval every vertex is critical. The two diagrams give the alternating directions and their last arrows for each parity. The surviving text of Proposition 6 tests reducedness using the interior vertices of a subinterval. The last corollary names $I_{\mathrm{red}}$. `S271-RED`.

**Scans 272–273.** A path of type $I$ in $X$ is a functor $I\to X$. The path category is the functor category. The page specifies objects and arrows for each sign. A morphism of paths gives one component per vertex, with a commuting square at each transition. The final two diagrams treat longer composites in a single structural interval. `D272-PATH`.

**Scan 274.** After a cancelled beginning of Proposition 7, the examples identify paths of length zero with objects of $X$ and direct paths of length one with arrows of $X$. For the retrograde type the target of that same arrow serves as the source of the path. The canonical isomorphism of the two path categories exchanges their designated endpoints. `S274-REINDEX`.

## Statements left without proof

Scan | Words on the sheet | Extent of the argument here
--- | --- | ---
263 | “n’a pas d’autre automorphisme que l’identité” | Asserted for $\mathbb{\Delta}_i$. `S263-ORD`. The subsequent correspondence with functors “injectifs sur les sommets” is stated directly. See `S263-EMBED`.
264–266 | “Tout foncteur” and “Pour prouver b, il suffit de prouver que l’ordre total sur $I$ est déterminé de façon intrinsèque” | An argument is given. Its recovery of the order addresses isomorphisms. It leaves the assertion about arbitrary endofunctors unsupported. `S264-F`.
269 | “Pour que $s$ soit critique, il f. et s.” | The margin restates part of the categorical-sum condition. No general proof is developed in the legible passage. `S269-SUM`.
270 | “Conditions équivalentes” | Proposition 4 gives (a), (b), (c) without a separate demonstration. `S270-DIRECT`.
270 | “Les composantes connexes … de $J$ sont des intervalles” | Proposition 5(a) is stated directly. The NB after (b) explains necessity by disconnection. The converse is not separately argued. `S270-SUB`.
270 | “est nécessairement pleine” | The slanted note refers the reader to a later section for this assertion about an interval-shaped subcategory. `S270-FULL`.
271 | “le plus petit” and “à isom unique près” | The first corollary and the classification of a reduced oriented interval by length and initial direction have no separate proofs. The two drawn models illustrate the classification. `S271-RED`.
271 | “réduit sss … est critique” and “est un sous-intervalle” | The surviving condition of Proposition 6 and the final corollary are stated here. The preceding long alternative formulation is struck. `S271-RED`.

## Questions and conjectures

On scan 265, “Comment déterminer $s_{i+1}$ ?” is followed by the insertion “(quand $i<n$)”. Scan 266 answers by choosing the immediate successor of an initial object or the immediate predecessor of a final object in the simplex that remains.

The phrase “Pour que $i$ soit la source, il f. et s. que” on scan 264 breaks off. The sign after “est critique” on scan 271 might be a closing brace or a question mark. The small hooked mark in the margin of scan 274 has no clear object. None of these supplies an identifiable further conjecture.

## Slips

Scan and place | Written form | Corrected form or reading question
--- | --- | ---
260, lines 15–20 | The first inline arrow joins $i$ to $i+1$. | For the named edge $\underline u_i$ the endpoints would be $i-1,i$, as in the diagram below. The second inline alternative is overworked. `I260-ORDER`.
262, lines 17–19 | The displayed order in the inserted composite ends with $\circ\,\underline u_i$ and the sentence includes retrograde chains. | With retrograde arrows the composite in this order is undefined already at length two. Their order in the product should be reversed. `S262-COMP`, `R262-COMP`.
262, line 26 | $1\le r\le n$ | The lower bound presupposes $n\ge1$. Scan 264 explicitly gives $r=0$ for the point. `R262-ZERO`.
263, lines 3–10 | “Deux chaînes composables maximales sont toujours de” opposite sign. | Insert the qualification *consecutive*. In the word $+,-,+$ the first and third maximal chains have the same sign. The doubtful inflections have no bearing on this example. `S263-ALT`, `R263-ADJ`.
263, lines 18–28 | “les chaînes maximales … correspondent exactement” to vertex-injective simplex functors. | The image must also be an entire maximal run. In $0\to1\to2$ the inclusion of $0\to1$ is vertex-injective and extends further. `S263-EMBED`, `R263-EMBED`.
264, lines 16–17 | “Tout foncteur” fixing both ends is the identity. | “Tout automorphisme” fits the argument. On $0<1<2$, the order-preserving map with values $(0,0,2)$ fixes both ends. The counterexample uses the legible word *foncteur*. `S264-F`, `R264-A`.
266, lines 1–10 | Slices at $i$ in $I$, after passing to $I'$. | The induction needs the slices at $s_i$ in $I'$. At vertex 1 in $0\to1\to2$, both ambient slices have two objects. In the remaining interval on 1 and 2 the incoming slice is a point. The prime-like mark in the later predecessor $j'-1$ remains a separate, low-confidence reading question. `R266-TAIL`.
269, lines 28–31 | The definition of $I''$ appears to repeat the incoming slice. | An outgoing slice would match the later punctured pair. The overwritten insertion supports only low confidence about the intended change. See also `S269-SUM`.
271, lines 15–16 | “que que” after the abbreviation for même. | The two visible words perform the work of one “que”. Both groups remain in the transcription.
272, lines 8–13 | “de longueur $n$ ($=\operatorname{card} I$)” | For the vertex set on these pages, $n=\operatorname{card}(\operatorname{Ob}I)-1$. Equivalently, $n$ counts the transitions. Scan 272 itself supplies $n+1$ objects. `S272-CARD`, `R272-CARD`.
273, lines 1–6 and 21 | The inline target appears as $A$. The forward chain starts with two subscripts $i+1$. | $A'$ fits the component formula, but the target is overwritten, so this is a low-confidence reading question. In the forward chain the second label would be $\underline u_{i+2}$, since the arrow leaves $i+1$. `R273-EDGE`.

## Pointers

- Scan 265 points back to Proposition 1 with “Cette observation prouve a). Pour prouver b”.
- Scan 268 refers to the two fork categories as “ci-dessus”. In the same paragraph, $\mathbb{\Delta}_i$ refers back to the ordinal simplex.
- Scan 270 invokes “par prop. 3” in the NB. Its slanted note reads “cf plus bas § des foncteurs d’intervalles”. The cited section is outside these sheets. No other cote, published work or named person is cited.

## Remarks of the model

- **High confidence in the distinction of operations.** For a positive-length standard interval with sign word $w$, reversal of the numbering gives the word obtained by reversing $w$ and changing its signs. Taking the opposite category with the numbering fixed changes the signs in place. The fork examples distinguish the two operations already at length two. On scan 268, lines 6–15, the frozen wording “l’intervalle opposé” follows a cancelled formula. “La catégorie opposée” would continue the preceding comparison. That attribution has **low confidence**. The argument with $u_1,u_n$ presupposes positive length. `S267-OPP`, `R268-NAMES`.
- **High confidence in the example, low confidence about the intended Proposition 3.** In $0\to1\leftarrow2\to3$, vertex 1 is critical. Its punctured incoming slice has vertices 0 and 2 and its punctured outgoing slice is empty. Vertex 3 still belongs to $I\setminus\{1\}$. Even the natural dual reading of the two slices therefore misses an object. A criterion that fits the later disconnection argument asks whether any arrow joins a vertex strictly before $s$ to one strictly after $s$. `S269-SUM`, `R269-CUT`.
- **High confidence in the example, medium confidence about the scope of the margin note.** The subcategory of $0<1<2$ consisting of all identities and just $0\to1,0\to2$ is an interval when ordered along $1,0,2$. It omits the ambient arrow $1\to2$. The later section cited on scan 270 might impose a further condition on interval functors. `S270-FULL`, `R270-EXAMPLE`.

The finite checks used the sign words and definitions in these sheets. CHECK_EVENTS.tsv gives their bounds and distinguishes a counterexample from testing a family of examples.
