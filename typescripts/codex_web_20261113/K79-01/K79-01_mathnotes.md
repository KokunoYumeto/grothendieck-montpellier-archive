# Mathematical notes on K79-01

## What the pages do

**U01 · Scans 2–3.** The title singles out free rank-two modules over the integers and their residue rings. The contents sheet situates the construction before sections on varying the symplectic structure, commutants, graphs, antipodisms and contours. This batch reaches the first construction.

**U02 · Scan 4, (1)–(5).** A triple $x,y,z$ has sum zero. If one of its pairs is a basis of $M$, so are the other two. Grothendieck calls the set of ordered triples $B(M)$, takes the quotient by permutations to get unordered triples, and identifies $B(M)$ with the ordered bases by forgetting $z$.

**U03 · Scan 5, (6)–(8).** The diagonal quotient $\Lambda^3/\Lambda$ carries the action permuting the three coordinates. The map $(x,y)\mapsto(x,y,0)\bmod\Lambda$ identifies that quotient with $\Lambda^2$ and gives a description of the action on frames.

**U04 · Scans 5–6, (9)–(12).** For each triple, the cyclically ordered pairs give the same element $x\wedge y=y\wedge z=z\wedge x$ of the set of determinant bases. The map $\alpha_A$ assigns it to the cyclic order. Reversing the order negates the determinant. Formula (12) expresses this sign dependence using the product over $\mu_2$.

**U05 · Scans 6–7, (13)–(14).** A gauge is a chosen basis $e_M$ of $\det M$. Grothendieck selects the triples giving the two signed values $\{\pm e_M\}$. Under $2\ne0$, the order with value $e_M$ is distinguished and written $\omega_A$.

**U06 · Scan 7, (15)–(17).** The initial vertex set consists of vectors nonzero in every fibre. A second description uses the invertible quotient $M/\Lambda x$. With $\operatorname{Pic}(\Lambda)=0$, the displayed union ranges over the unordered triples. The closing observation concerns uniqueness of a triple containing a prescribed pair of vectors.

**U07 · Scans 8–9, (18)–(19).** After noting the actions of $\mathrm{Gl}$ and $\mathrm{Sl}$, Grothendieck identifies a vector with its negative and a triple with its simultaneous negative. He argues that the three projected vertices determine the face. An independent sign change would give two zero-sum equations and hence $2z=0$ for a primitive vector. A marginal note returns to the Picard hypothesis.

**U08 · Scans 9–11, (20)–(23).** An edge is a pair contained in a face. Lifting the pair to a basis gives two incident faces, from sign choices modulo simultaneous reversal. The proposition collects the vertex, edge and face sets as $P_M=(S_M,A_M,F_M)$. Its revised definition uses vectors that occur in bases. The marginal addition on scan 11 asks for a further check at each vertex.

**U09 · Scan 11, Remarque.** In the semi-local case the text uses a common vector $z$ completing each of $x,y$ to a basis. From the corresponding pairs of vertices it concludes that the graph distance is at most two.

**U10 · Scan 12, (24)–(30).** With a fixed gauge, (25) selects the lifted faces and (26) projects them. Grothendieck rescales a basis partner by a unit to obtain determinant $e_M$, so these faces still cover the vertices. He defines the restricted edge set $SA_M$ and records its inclusion in $A_M$.

**U11 · Scan 13, (31)–(33).** The first diagram transfers the determinant map from a lift of a face to the cyclic orders of the projected face. The next construction fixes an edge, writes down its two adjacent faces, and compares the two maps into the determinant bases in the diamond (33).

**U12 · Scan 14, (34)–(35).** At the chosen end of the edge, the two composites give $x\wedge y$ and $x\wedge(-y)$. Their opposite signs give the equivalent membership tests in (34). Each restricted edge still belongs to two restricted faces. The resulting triple of sets is denoted $SP_M$.

**U13 · Scans 15–16, through (38).** Fix a representative $x$ of a vertex. Neighbours correspond to the affine line $L_x$ defined by $x\wedge y=e_M$. After normalising a signed sum and comparing two exterior products, Grothendieck obtains $z=x+y$ or $y=x+z$. The edges of the contour join points of $L_x$ differing by $\pm x$. Formula (38) describes a component through $y$ by successive integral translates, also written $y+\Lambda_0x$. This is the last displayed line in the batch.

## Statements left without proof

| ID | Scan | Author's words or formula | Extent of the argument on these sheets |
| --- | --- | --- | --- |
| U06a | 7, (15) | “$M/\Lambda x$ est un $\Lambda$-module inversible” | The second set is equated with the fibrewise definition. No separate argument for this equality is supplied. |
| U06b | 7, (17) and last line | “Si $\mathrm{Pic}(\Lambda)=0$ …”; “il existe au plus un $A\in\widetilde F_M$ le contenant” | The union and the uniqueness for a given pair are stated here. The zero-sum condition used for uniqueness was written on scan 4. |
| U07a | 8, opening | “$\mathrm{Gl}_{\Lambda}(M)$ opère … en stabilisant $\widetilde F_M$”, and $\mathrm{Sl}$ acts “en stabilisant de plus le système…” | Both stabilisation assertions are recorded before the quotient by signs. |
| U09a | 11, Remarque | “$\exists\,z\in\widetilde S_M$ tel que $(x,z)\in\mathrm{Rep}(M)$, $(y,z)\in\mathrm{Rep}(M)$” | The existence of this common partner is asserted. The next sentence uses it to give the distance bound. |
| U11a | 13, immediately before (31) | “est indépendante de $\widetilde f$” | Independence of the choice of lift is stated after the span. |

## Questions and conjectures

| ID | Scan | Words on the sheet | Question |
| --- | --- | --- | --- |
| Q1 | 9, beside (19) | “inutile?, tout élément de $M^*$ fait tjrs partie d'une base” | Is $\mathrm{Pic}(\Lambda)=0$ needed at this point? The question mark is uncertain. A further slanted passage considers what to define without the hypothesis. |
| Q2 | 11, beside (23) | “Attention, il manque encore la condition de connexité … à un sommet…” | The author flags the surrounding edges and faces at a vertex. The main remark about distance concerns the whole graph. |
| Q3 | 14–16 | “Il reste cependant à examiner la question de la connexité du contour combinatoire … associé à un sommet” | Scans 15–16 take up this question for the restricted complex. The final formula describes the individual components. |

## Slips

Here an intended reading is an editorial inference. The LaTeX preserves the page.

| ID | Scan | Written form | Likely intention and reason | Confidence |
| --- | --- | --- | --- | --- |
| S1 | 4, (4) | $A\subset\mathfrak P_3(M)$ | $A\in\mathfrak P_3(M)$ would make $A$ an unordered triple of vectors, as in the adjacent conditions. The P's typeface is doubtful. | Low |
| S2 | 5, before (8) | “déduit de l'isomorphisme” | *Déduite* would agree with the preceding *bijection*. | Medium |
| S3 | 7, last paragraph | “d'une ensemble” | *D'un ensemble* would give the usual agreement. The final small loop is inked heavily. | Low |
| S4 | 8, opening | $\alpha_A\in\underline{\omega}_A$ | The distinguished element of the underlined set on scan 7 is $\omega_A$; $\alpha_A$ is its determinant map. | Medium |
| S5 | 8, interlinear addition | $S_F$ | The antecedent of the sign argument suggests $\widetilde F_M$. The interlinear symbol is compressed. | Low |
| S6 | 9, (19) | Union over $A\in\mathfrak P_3(S_M)$ | The covering assertion being discussed uses the face family $F_M$. Indexing by all three-element subsets makes a broader union. | Low |
| S7 | 9–10 | Two separate displays labelled (20) | The label is repeated. The second collects revised definitions, and (21) follows. The pages do not give a unique replacement number. | High |
| S8 | 10, second (20) | A plus-like mark between $x$ and $y$ before $\mathrm{Rep}(M)$ | A comma would give the same ordered-pair syntax as the two following glosses. The sign is overdrawn. | Low |
| S9 | 13, formula for $f'$ | The first projected $x$ has a prime as well as a dot. | The comparison in (33) uses the same chosen end of the edge. The prime may be unintended. | Low |
| S10 | 14, first paragraph | “a l'élément” | *À* is the preposition in the phrase. The isolated lower-case a has no visible accent. | High |
| S11 | 15, first paragraph | $\dot t\in S_M$, followed by $\{s,t\}$ | An undotted $t$ would agree with the pair on the same line. | Low |
| S12 | 15–16 | The determinant condition is labelled (35) just before (36′). Scan 16 refers to (36). | (36) is the likely intended unprimed label; (35) has already been used for $SP_M$. | Medium |
| S13 | 15, above $t$ | $t=\dot x$ | $t=\dot y$ would give the neighbour represented by $y$ in the next clause. Here $s$ already denotes $\dot x$. | Medium |
| S14 | 15, face of the contour | A membership-like sign between $\{s,t,u\}$ and $\{\dot x,\dot y,\dot z\}$ | The context identifies the two descriptions of the face. The sign is doubtful. | Low |
| S15 | 16, last paragraph | “correspondent” followed by the addition “sont” | The added verb fits “les parties de $L_x$”. The preceding verb appears to survive the revision. | Low |

## Pointers

**P1 · Scan 3.** The contents points ahead within this manuscript. Examples include “Relation avec l'isom” (II, p. 12′), “Re-récapitulation, avec programme de travail” (V, p. 35), “Axiomatique : reformulation” (VIII, p. 65) and “Récapitulation des notions obtenues” (XI, p. 114). The isolated “p. 79/90/95…” has an uncertain final stroke and no named target.

**P2 · Scans 9–10 and 14–16.** Internal references include the slanted “on a donc modifié légèrement la définition (15)” on scan 10, “par (36′)” on scan 15, and “satisfaisant (36)” on scan 16. An identifiable pointer to another cote, a published paper or another mathematician: none.

## Remarks of the model

**R1 · Model remark, high confidence.** For a free module of rank two over a commutative ring with identity, the fibre criterion in (15) is enough to complete $x$ to a basis. Its two coordinates generate the unit ideal, and a Bézout relation supplies a partner of determinant one. This addresses the content of the note beside (19) independently of the uncertain question mark.

**R2 · Model remark, high confidence for the two examples computed.** I enumerated the determinant-normalised faces from signed classes of zero-sum triples, then formed the graph around the class of $(1,0)$ from face incidence. In both examples each restricted edge had two incident faces. For the nine-element field the contour at that vertex had three components. The calculation used $\mathbb F_3[T]/(T^2+1)$ and checked that every nonzero element of the chosen representation had an inverse.

| Ring for $\Lambda$ | Vertices of $SP_M$ | Edges | Faces | Component sizes in the contour at $(1,0)$ |
| --- | ---: | ---: | ---: | --- |
| $\mathbb F_3$ | 4 | 6 | 4 | 3 |
| $\mathbb F_9$ | 40 | 180 | 120 | 3, 3, 3 |

**R3 · Model remark, high confidence under the stated characteristic hypothesis.** For the rings named on the title sheet, $\mathbb Z$ and $\mathbb Z/n\mathbb Z$ with $2\cdot1\ne0$, integral translates by $x$ exhaust the affine line $L_x$. Thus the contour described on scan 16 is connected in these cases. This follows from the explicit adjacency $y-z\in\{\pm x\}$ and the fact that the additive group of each ring is generated by $1$. It is independent of the shape of the overwritten integer parameter in (38).

**RQ1 · Model reading question, low confidence.** On scan 3, XI.3, the frozen page reference is `\unsure{122|123}`. It might read `12?`. Its last mark has a rounded upper stroke and a detached dot, unlike the continuous 2 just before it. A literal question would concern pagination.

**RQ2 · Model reading question, low confidence.** On scan 5, in the gloss beneath (9), the frozen reading is `\Lambda^2 M`. The alternative `\bigwedge^2 M` would denote the determinant line. The initial sign has the same two straight sloping strokes as the ring letter in the line above. The two typographic readings can represent almost the same handwritten shape.
