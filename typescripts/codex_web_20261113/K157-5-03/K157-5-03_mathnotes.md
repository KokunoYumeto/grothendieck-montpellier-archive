# Mathematical notes on scans 036–051

The headings and references below follow the manuscript. Identifiers connect individual comparisons with CHECK_EVENTS.tsv.

## What the pages do

**036–037. Preliminary question and induction on points.** Grothendieck asks for a common hypothesis covering two earlier situations. He draws the relative map for an open part of $I_{/i_0}$ and asks about a test at its punctured open under local finiteness. He then forms a set $P$ of points where the map condition holds for every open. The lemma passes from all strict predecessors of $i_0$ to $i_0$ itself. Its corollary identifies $P$ with $I$ when $I$ is Artinian.

**038–039. The definition [D38].** Section 2 takes a class $C$ of arrows in $M$ containing the isomorphisms and stable under change by pushout and transfinite composition. For diagrams $X_\bullet,Y_\bullet$, their colimits over an open $J$ are $X_J,Y_J$. For $K\subset J$, the central object in (2.4.) is the pushout of $Y_K$ and $X_J$ over $X_K$. Its arrow to $Y_J$ is $u_{K,J}$. The definition of $C_I$ tests these arrows when $J$ is a principal open.

**039–040. Theorem 2.1.** Part 1° extends the test to every pair of opens. Part 2° assumes $I$ Artinian and reduces the test to deleting the greatest point from a principal open. Part 3° introduces $W$ and $TC=C\cap W$, with stability hypotheses on $TC$. It identifies $(TC)_I$ with the arrows of $C_I$ that belong to $W$ at each point. The added Artinian hypothesis on this part has a starred marginal comment.

**040–041. Corollaries 2.2 and 2.3 [C41].** A $C_I$ arrow gives arrows in $C$ on components, on the colimit over $I$ and on the colimit over any open $J$. Three displayed identifications on 041 relate these maps to the case with empty first open. The next corollary gives the corresponding $TC$ conclusions for an arrow in $C_I\cap W_{I^o}$.

**041–042. Cofibrant diagrams and Corollary 2.5 [C42].** Corollary 2.4 applies the result to the map from the initial diagram to $X_\bullet$. It describes the transition maps on opens and on points. The continuation gives a corresponding statement for $W$-coaspherical objects and $TC$. Corollary 2.5 says that ordinary composition suffices in the stability hypotheses when the space of opens is Noetherian.

**043–044. Filtration by opens.** A cancelled start would collect good opens and take unions of chains. The replacement starts at $K$, adjoins a principal open at each successor step, and takes the union at a limit ordinal. The successor map is related by pushout to the map made from the new principal open and its intersection with the preceding open.

**044–046. Lemma 2.6 [L26].** From a morphism of cocartesian squares, Grothendieck takes the two side faces $Z_0,Z_1$ and their comparison arrows. The lemma says $u_{Z_1}$ is obtained from $u_{Z_0}$ by change by pushout. The faces $T,T'$ and the expanded cube on 045 identify the square whose cocartesianness is needed. The opening of 046 concludes the cube argument.

**046–047. Lemma 2.7.** An ordinal sequence of opens gives a transfinite composite. The objects $Z_\alpha$ and the two diagrams compare its successor arrows with those for adjacent opens. Grothendieck then observes that the strictly increasing construction must be finite when the underlying space is Noetherian. An earlier attempted application remains visible under cancellation.

**048–049. Lemma 2.8 and its corollary.** Here $P$ consists of points on whose principal open the restricted arrow belongs to the corresponding $C$ class. Passage from the strict lower segment to its endpoint is proved without an Artinian assumption on $I$. The ensuing corollary uses that assumption to get $P=I$ and finishes part 2°. The Noetherian qualification continues onto 049.

**049–050. Part 3° [P49].** Grothendieck treats the two implications separately. For the reverse implication, the square on 049 relates $u_K$, its pushout and the composite $u_J$. The text invokes saturation. A first Lemma 2.9 is cancelled. The replacement on 050 uses the points where the restriction belongs to the corresponding $TC$ class. The Artinian case gives $P=I$. The last paragraph returns to Corollary 2.5.

**050–051. First remark.** The example takes $I=\mathbb N^{\mathrm{opp}}\simeq\mathbb Z^{\leq 0}$. A constant inductive system with a non-cofibrant value separates the transition test from cofibrancy of its values. Grothendieck then considers a general arrow for this same $I$ and records that the equality in part 3° still holds here.

**051. Second remark.** An arrow of diagrams is viewed as an object of a diagram category indexed by a product with the interval. The margin identifies the two ways of writing the opposite. The last lines state a cofibrancy criterion in terms of $X_\bullet$ and the arrow $u_\bullet$, followed by the consequence for $Y_\bullet$.

## Statements left without proof

- **041, margin beside Corollary 2.4.** “et réciproquement, cela caractérise les objets $C$-cofibrants”. The converse is stated in the margin. Corollary 2.3 and the $TC$ and coasphericity consequences on 041–042 are also given as consequences of the theorem.
- **043, cancelled argument.** “il existe, pour tt ens. tot. ordonné, … une partie bien ordonnée cofinale”. The claimed cofinal subset belongs to the abandoned proof. The replacement construction says “Il existe un $\alpha_0$ tel qu'on ait $I_{\alpha_0}=I$”, without a separate argument for termination.
- **047–049, Noetherian qualification.** “la construction transfinie est forcément finie” is the reason given on 047. On 048, “il en est de même de tout ouvert (tel $J'$ ci-dessus)” invokes inheritance by an open.
- **051, first remark.** “on voit que” introduces the two conditions a) and b) for an arrow on this particular order. The text appeals to the preceding argument for the $TC$ conclusion.
- **051, last lines.** “On vérifie que pour que cet objet soit $C$-cofibrant, il f. et s.” introduces the criterion that $X_\bullet$ be $C$-cofibrant and $u_\bullet\in C_I$. The parenthesis adds that $Y_\bullet$ is then cofibrant. The sheet ends there.

## Questions and conjectures

- **036.** “Question : est-il exact qu'il suffit” refers to condition a) on the principal open and its puncture, together with b) “$I$ loc. fini”. The question asks whether these imply the condition drawn above.
- **040, upper left.** “J'ignore si cette hypothèse est nécessaire” qualifies “Supposons encore $I$ artinien” in 2.1, 3°.
- **051, just above 2).** “J'ignore si l'hypothèse artinienne dans 2.1. 3° est superflue ou non.” This follows the displayed equality for one non-Artinian order.

## Slips

| ID and scan | As written | Apparent intention and reason | Confidence |
|---|---|---|---|
| S37 · 037, bottom | $x_1<x_0$ avec $x_0\notin P$ | The membership after “avec” would be $x_1\notin P$. The chosen smaller witness is the point needed for the descent. Both written zeros are visible. | High |
| S39-edges · 039, (2.4.) | $\tau^X_{J,K},\tau^Y_{J,K}$ | Possibly $K,J$ after revision. The columns run from $K$ to $J$ and many adjacent labels were rewritten. | Low |
| S40-ref · 040, stability conditions | (1.1.) | Possibly (2.1.), the matching list on 038. Section 1 may contain a second applicable list. | Medium |
| S41-point · 041, foot | $h\le j$ or $k\le j$ | If the first letter is $h$, the adjacent $K=I_{/k}$ and “si $k\le j$” suggest $k$. | Low |
| S47-stage · 046–047 | $Z_0=Y_{I_0,I_{\alpha_0}}$ on 046, $X_{I_{\alpha_0}}=Z_0$ on 047 | Possibly $Z_{-1}$ at the upper right of the successor diagram. The lower bound $-1$ was inserted on 046. The two constructions may be at different stages of revision. | Low |
| S49-ref · 049, first implication | “cf cor. 2.1. a” | The component conclusion is in a) of the corollary on 040, apparently 2.2. Both the earlier heading and the terminal a in this pointer have doubtful ink. | Low |
| S49-class · 049, reverse implication | $C\cap W_{I^o}$ | The first factor would be $C_I$. Part b) on 040 and the next paragraph of 049 both give the subscript explicitly. | High |
| S50-first · 050, before “on conclut” | “Th. 1, 1°” | Probably Th. 2.1, 1°. Its open-set conclusion is applied in the neighbouring proof on 048. | Medium |
| S50-number · 050, lower middle | “il résulte de 3.9.” | 2.9. is the heading of the lemma on this sheet that supplies the condition on $P$. | High |
| S51-part · 051, upper third | “2.1. 1°)” or “2.1. 2°)” | The example begins under 2.1 2° on 050. If the first reading is correct, 2° appears intended. | Low |
| S51-class · 051, middle | “est dans $C$ ssi” | Possibly $C_I$. The subject is an arrow of diagrams and the two ensuing tests concern that entire arrow. | Medium |

## Pointers

- **036–037.** “dans un cas, loc fini dans un autre” and “ce qui a été prouvé pour le cas de $J'$” look back to earlier cases. No external text is named.
- **039–042.** Theorem 2.1 cites (2.2.) for membership and (2.4.) for the comparison map. The corollaries refer to “$1^\circ$)”, “la déf. de $C_I$” and “2.1.$3^\circ$”. The upper-left note on 040 adds “cf commentaire p.” with a number read as 39 or 35. The packet ends on manuscript p. 38.
- **043–044.** “comme au § 1” continues across the page turn into “cf diagramme 6 p. 17”. Grothendieck writes that it should be drawn out as a lemma, “débarrassé des particularités techniques de la situation”. Manuscript p. 17 is outside these sixteen sheets.
- **045–050.** “du cube (2.6.1)”, “par les 2 lemmes précédents”, “par le Th. 2.1, 1°”, “cf cor. 2.1. a” and “du cor. 2.5” refer to the diagrams and successive proof steps. The two uncertain or mismatched references on 049–050 are recorded above.

## Remarks of the model

- **C41 · 038–041. High confidence.** The empty-open specialization explains why a single pushout construction supplies both the component and colimit statements. Substitution in (2.4.) gives an arrow with source $X_J$. The three identifications written on 041 agree with that check.
- **R48-points · 048 and 050. High confidence.** The two definitions of $P$ distinguish the two induction arguments. In the first, the restricted arrow belongs to the $C$ class on a principal open. In the second it belongs to the $TC$ class there. Both definitions are visible in the lemma statements.
- **R51-example · 050–051. High confidence for the constant-system test.** Identity transitions meet the isomorphism condition on $C$ from 038 even when the chosen value is non-cofibrant. This accounts for the specific failure in the first remark. The manuscript’s separate question about 3° remains open on these pages.
