# K79-04 · Mathematical notes

## What the pages do

**U1 · The type of an edge (049–050).** An ordered pair belongs to $\widetilde A$ if its wedge has a value in the index set $\Pi$. The author uses symmetry and exclusion of the diagonal to pass to unordered edges $A$. The fibre of the type map at $i$ is the edge set of the triangulation $\Sigma(i)$. The sentence continues onto 050, where (122) and (123) are imposed on the fibres.

**U2 · Compatibility of two actions (050–051).** The torsor structure on $\Pi$ raises a question about extending the symmetric operation. Equation (125′) relates the action $T_\lambda$ on a single vertex to multiplication by $\lambda$ on an edge type. In (127) on 051, acting on both vertices multiplies the type by $\lambda^2$. The author cites separation of vertices by their stars in (126) and says in the margin that the two actions determine each other. He strikes out a proposed relation involving the three vertices of a face.

**U3 · Starting from one polyhedron (051–053).** Fix a finite regular triangulated polyhedron $P_0=(S,A_0,F_0)$ and write $G_0=\operatorname{Aut}(P_0)$. The commutant $Z$ consists of the permutations of $S$ centralizing $G_0$. Equations (130) and (131) take its intersection with $G_0$ and form the quotient $Z'$ by that intersection. The action moves the initial structure to $\Sigma_\lambda$. Equations (132bis) and (133) assert disjointness of edge and face sets for distinct indices and injectivity of the indexing map.

**U4 · Equivalence of triangulated structures (053–054).** A permutation transporting one structure to another must commute with the automorphism group of the first. The author gives the common automorphism groups in (134), writes the inverse transport in (135), and equips an equivalence class with a torsor structure. Diagram (137) records the automorphisms inducing the identity on $Z'$. In the module example this process reaches only the square indices.

**U5 · Transporting one endpoint (055).** The proposed smaller group $Z_0$ is defined by (138). A permutation $\lambda$ centralizes $G_0$, and a second permutation $f_\lambda$ must exist with the displayed edge property. The definition of $A_\lambda$ keeps the first endpoint and moves the second by $\lambda$. Requiring $f_\lambda(A_0)=A_\lambda$ gives (140) and its expression in terms of unordered pairs, (141).

**U6 · Equivalence of graphs (056–057).** Equation (142) uses the commutation of $u\in G_0$ with $\lambda^{-1}$ to express invariance of $A_\lambda$. The author writes $G_\lambda=G_0$ in (143). He then defines equivalence for strict graphs on a common vertex set, with $\lambda$ called a *transporteur*. Applying the inverse to the second endpoint gives symmetry. He describes transitivity by composing two transporters through the intermediate edge set.

**U7 · When the transporters form a group (057–058).** For fixed $A_0$, (144) describes $\widetilde Z_0$, the permutations transporting it to some equivalent edge set. Formula (145) records the identity, inversion and multiplication for a commuting pair. Strict equivalence adds the requirement that the two graphs be isomorphic. The author writes $Z_0$ for transporters giving such graphs, assumes commutation, and describes $\mathfrak z_0=Z_0\cap G_0$ by a centre condition and equality of stars at $s$ and $u^2s$.

**U8 · An admissible class (059).** The strictly equivalent structures form a torsor under $Z'_0=Z_0/\mathfrak z_0$. An admissible class $\Pi$ is one for which the set of transporters is a group. Equation (148) defines the permutations preserving the whole class. Equation (149) describes them using a single chosen $A_0$, its image and preservation of $Z_0$.

**U9 · The type map from an admissible class (060–061).** Inside $\operatorname{Aut}(S,\Pi)$, (150) takes those permutations whose conjugation acts trivially on $Z_0/\mathfrak z_0$. Diagram (151) relates the resulting sequence to the quotient sequence for $Z_0$. Assuming edge transitivity, the author makes the union of edge sets disjoint. An edge is then sent to the unique member of $\Pi$ that contains it. He says at the top of 061 that this generalizes (126).

**U10 · The residue-ring test (061).** For a rank-two module over $\mathbb Z/n\mathbb Z$, (154) and (155) propose two increasingly strong identifications with the permutations induced by scalars modulo sign. The author then drops the residue-ring hypothesis. A brace under the numerator of $S_M$ describes elements of $M$ that belong to a basis.

**U11 · Vertices for a general ring (062).** Section IV starts with a nonzero ring $\Lambda$ and a free rank-two module $M$. A vertex before taking signs is a vector that occurs in an ordered basis. Formula (156) identifies a vector with its negative to obtain $S_M$. Formula (157) distinguishes the two possible degrees of the projection according as $2\cdot1_\Lambda\ne0$ or $2\cdot1_\Lambda=0$.

**U12 · Edges from bases (062).** The surviving definition in (158) uses unordered pairs of distinct vertices represented by a basis. The author crosses out a definition using unordered bases, two quotient expressions, a degree calculation and a proposed inclusion. The marginal NB distinguishes prescribing the images of $x,y$ in order from prescribing only their unordered pair.

**U13 · Determinant types and graphs (063).** Equation (161) sends an edge to its type in $\Pi_M=(\det M)^*/\{\pm1_\Lambda\}$. In (162) the rule on representatives is $x\wedge y$ modulo sign. The right margin explicitly treats exchanging the vectors, changing either sign, or changing both. Equation (163) makes each fibre an edge set $A_{M,i}$ and hence a graph $\Sigma(i)$ on $S_M$.

**U14 · The stabilizer of a type (063–064).** Transport by $\operatorname{Gl}_\Lambda(M)$ preserves the full edge set and permutes its fibres according to the action on determinant types. The scalar subgroup $\{\pm\mathrm{id}_M\}$ acts trivially, giving the quotient $G_M$. The composite $\delta_M$ in (165) takes determinant and then divides units by sign. The last sequence identifies the stabilizer of a point of $\Pi_M$, and of the corresponding graph, with $\ker\delta_M$.

## Statements left without proof

| ID and scan | Author's words | Statement and scope |
| --- | --- | --- |
| P1 · 049–050 | “déterminées par les structures de graphes correspondantes via (121)” | Reconstruction of the triangulations from their graphs is invoked from a preceding formula. The two further conditions (122) and (123) are referenced without restatement. |
| P2 · 050–051 | “est uniquement déterminée”, “Il revient au $=$ de se donner l'op.” | Uniqueness uses the star-separation assertion (126), including the parenthetical alternative “pour un $i\in\Pi$”. The marginal claim about recovering either of two compatible actions has no separate construction here. |
| P3 · 052–053 | “on doit avoir”, “est une application injective” | Edge and face transitivity motivates (132bis). The construction (133) and the two group equalities in (134) are stated without a separate proof of each. The unqualified version (132) has the exception in S1 below. |
| P4 · 054 | “se trouve alors … de façon naturelle d'une structure de torseur”, “s'insère alors dans une suite exacte” | The torsor assertion and diagram (137) are given after the equivalence relation. Exactness is stated without a term-by-term check. |
| P5 · 056–057 | “Donc on trouve encore”, “L'argument précédent montre que l'on a alors” | The displayed calculation checks preservation by $u\in G_0$. Equation (143) and the later statement $G_0=G_1$ give equality of the full automorphism groups. The reverse containment is not distinguished in that calculation. |
| P6 · 057–058 | “On voit en tous cas que”, “C'est encore une relation d'équivalence.” | Closure statements (145) and the assertion about strict equivalence follow the transporter argument. The two marginal consequences of injectivity of the star map receive no separate proof. |
| P7 · 059 | “est un torseur sous”, “Ce groupe ne dépend pas du choix de $A_0$” | The strict class is a $Z'_0$-torsor. The transporter group is declared independent of the chosen graph. The description (149) is also stated from one graph without a separate derivation. |
| P8 · 060 | “Donc on trouve une suite exacte canonique”, “On voit alors que” | The exactness of (151), independence of an origin and disjointness of distinct edge sets under edge transitivity are asserted. The surjectivity reservation has been crossed out. |
| P9 · 061 | “il faudrait vérifier”, “on suspecte même” | Both scalar identifications are left open. See Q5. |
| P10 · 062–064 | “est de degré constant”, “ne change pas”, “le noyau”, “et il en résulte” | The degree in (157), invariance of the edge type, and the exact sequence and graph stabilizer on 064 have brief explanations or formulas. The algebraic checks in R1–R3 are editorial. |

## Questions and conjectures

| ID and scan | Author's words | Question or qualification |
| --- | --- | --- |
| Q1 · 050 | “la question se pose de décrire, en termes des données précédentes”, and in the margin “pas tellement, finalement !” | How much of the symmetric operation can be reconstructed? The marginal qualification stands beside the relation to the $Z'_n$-action. |
| Q2 · 051 | “il faut y revenir ultérieurement !” and “J'aimerais comprendre comment … une des structures … détermine toutes les autres” | One attempt involving the three vertices of a face is crossed out. The question of reconstructing the family and its action remains. |
| Q3 · 052, 054 | “son commutant sauf erreur est réduit à $Z'_n$”, “à vérifier”, then “on est encore loin du compte !” | The proposed size of the commutant requires checking. Even the indicated construction of the orbit produces only square types in the example. |
| Q4 · 057–058 | “On aimerait que ce soit un sous-groupe”, “sous réserve que”, “dorénavant qu'il en est ainsi !” | There is a subgroup question for the transporter sets. The hypothesis about commuting elements is explicit. |
| Q5 · 061 | “il faudrait vérifier que”, “et on suspecte même que l'on a déjà” | (154) asks whether all the transporters in the specified group are the displayed scalars. (155) asks this of the entire commutant and places a question mark above the equality. Neither identification is checked in these editorial notes. |
| Q6 · 060, crossed out | “sans que je sois sûr si … est surjectif” | A former doubt about $G\to Z'_0$ remains legible beneath the cancellation in the text following (151). |

## Slips

| ID and scan | As written and proposed correction | Reason and confidence |
| --- | --- | --- |
| S1 · 052, (132) | The condition is $\lambda\in Z'$. Read $\lambda\ne1$ as an additional hypothesis (S1r). | High for the missing identity exception whenever the edge or face set is nonempty. At the identity both intersections are self-intersections. The next sheet actually writes $\lambda\ne\lambda'$ in (132bis). This check does not establish disjointness for all other indices. |
| S2 · 054, (136) | $\mathfrak z=Z'\cap G$ apparently needs $Z\cap G$. | Low. The earlier intersection lives in the permutation group, while $Z'$ is a quotient. The neighbouring definition on this sheet is overwritten. |
| S3 · 055, (139) | The page brackets the biconditional $P\Leftrightarrow Q$ and makes it imply $s'\ne t'$. A possible repair (S3r) is to impose symmetry $P\Leftrightarrow Q$ and loop exclusion $P\Rightarrow s'\ne t'$ separately. | High for the failure of the literal bracketed implication on a nonempty vertex set. At equal inputs the unordered pairs are identical. Medium for the proposed repair. The chain in (144) on 057 has different punctuation. |
| S4 · 056, definition | $A_1\in\mathscr P_2(S)$ apparently needs $A_1\subset\mathscr P_2(S)$. | Low. In the following condition an unordered pair can belong to $A_1$, which is therefore being used as an edge set. The relation after $A_1$ is heavily inked. |
| S5 · 057, composition display | The composite is $\lambda\mu$. Ordinary composition of left-acting permutations would give $\mu\lambda$. | Low. The second endpoint changes from $t$ to $\lambda t$ and then to $\mu(\lambda t)$. The text has not yet assumed pairwise commutativity, but a different convention for writing products is possible. The connector beside the composite is also marked. |
| S6 · 053, (135) | $\Sigma$ has a doubtful raised mark on the left. The inverse transport would give bare $\Sigma=\lambda^{-1}.(\Sigma')$. | Low. The preceding equation determines the formal inverse, while the strokes for the superscript do not give a secure reading. |
| S7 · 059, (148) | In $f(F_0)$ or $f(A_0)$, the quantified variable gives $A_0$ as the expected argument. | Low. The capital is overwritten. The second line explicitly contains $f^{-1}(A_0)$. |
| S8 · 061, final paragraph | The parenthetical specification of $i$ ends with two closing parentheses. One would complete the expression. | Medium. The parentheses around the determinant have already closed. |
| S9 · 049–051, 060 | Scan 049 refers to “une application (surjective) (127)”, perhaps the arrow (126). Labels (124)–(128) recur, and two displays on 060 carry (152). | Low for changing the reference on 049, since (127) describes the fibres. The repeated labels are identifiable by scan and opening symbols. The sheets do not prescribe a replacement numbering. |
| S10 · 051, inserted tuple | $A\subset S\times S$ is written where the distinction on 049 would give $\widetilde A\subset S\times S$. | Low. The author may have chosen the shorter letter inside the tuple. |
| S11 · 062, struck (159) | A degree 2 in the abandoned sketch stands beside “4 choix (et non 2 !)”. | Low for identifying precisely which quotient he meant to correct. Ordered lifts of two specified vertex images have independent signs when $2\cdot1_\Lambda\ne0$. The marginal 8 also allows the order of the two images to change. |

## Pointers

No other manuscript title, archive cote, named paper or person is cited on these sheets. There are explicit pointers within the working notes.

- **049–051.** “il suffirait de connaître (118)”, “via (121)”, “satisfassent (122) et (123)” and “qui prolonge (125)” refer back to the wedge operation, reconstruction from graphs and conditions on the fibres. The first four numbers refer to material earlier than scan 049. “On a vu tantôt” invokes uniqueness in the discussion on 050.
- **053.** The margin says that the notation $\Sigma_\lambda$ “n'est pas cohérente avec la $\Sigma(i)$ de tantôt”. The proposed subscript at the end of the note is difficult to read.
- **055–056.** “revenons sur la définition de $Z$ tantôt” returns to the group on 052. “L'argument précédent” refers to the calculation with $u$ and $\lambda^{-1}$ on 056.
- **061, 063.** “qui généralise (126)” follows the edge-type map at the bottom of 060. On 063 “$\tau$ (161)” points back to that sheet's determinant-type map.

## Remarks of the model

**R1 · Independent signs (062), high confidence for the count.** A vector belonging to a basis can equal its negative only if $2\cdot1_\Lambda=0$. For two distinct ordered vertex images, the numbers of lifted bases are therefore four and one in the two cases of (157). Forgetting their order doubles those numbers to eight and two. The cancelled source of (159) makes attribution of this correction to that specific map uncertain.

**R2 · The type of an unordered edge (063), high confidence.** Swapping the two basis vectors multiplies their wedge by $-1$, as does negating either one. Consequently the class of the wedge modulo sign gives the same answer for every representative of an edge. This directly checks the right-hand marginal NB against (162).

**R3 · Two different sign quotients (064), high confidence.** In rank two, replacing a matrix by its negative preserves its determinant. The first arrow in (165) therefore already has values in $\Lambda^*$. The next arrow sends units to their classes modulo sign. Its composite has as kernel the classes represented by matrices of determinant $1$ or $-1$. The diagonal matrix with entries $u,1$ realizes every unit $u$. This calculation uses the arrows of (165) and does not depend on deciphering the labels underneath the last sequence.

**R4 · Reading question, 063 L7–9, low confidence about the referent.** The final reading in (162) is $\widetilde A_M$. One might expect $\operatorname{Rep}(M)$, or its quotient by exchange, as the source of a formula written on representatives. The two are different sets. The only explicit definition of $\widetilde A_M$ in this extract is crossed out on 062. The tilde in (162) is visible, and the frozen reading stands.

**R5 · Reading question, 064 L6–9, low confidence about the shorthand.** The final reading is “pour $i\in\Pi$”. The other possible intended designation is $\Pi_M$, which appears at the end of the same sheet. It is unclear whether the author deliberately omits the subscript in this phrase. The transcription retains the shorter form.


**R6 · Reading question, 064 L11–15, low confidence.** The frozen superscript in $G_M^0$ is a zero. A small circle, $G_M^{\circ}$, is also possible. In the last sequence the stroke is round with an open centre. The insertion above the definition of the kernel offers no more distinctive numeral. Neither reading changes the displayed definition of the subgroup.
