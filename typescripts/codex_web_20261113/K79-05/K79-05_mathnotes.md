# Mathematical notes · cote 79, scans 65–80

Formula numbers refer to the handwritten sheets. The subsection starting on scan 72 restarts the numbering at (1). Quoted French is from this transcription. The identifiers connect individual observations to the check-events file.

## What the pages do

**Transitivity and the first faces, scan 65.** Two ordered bases with the same determinant up to sign are related by a unique linear transformation whose determinant is a sign. Grothendieck uses this to discuss transitivity on edges of a given type, then transitivity on all edges. He strikes “simplement” in the assertion about oriented edges and explains the exception when $2\,1_\Lambda=0$. He introduces faces of the quotient structure as triples of classes admitting representatives $x,y,z$ with $x+y+z=0$ and $x\wedge y$ a determinant generator. All three edges of such a face have the same type. This is the face definition used in **E1**.

**Counting faces and defining a frame, scans 66–67.** In case A, $2\,1_\Lambda=0$, an edge belongs to one face, and the edge-to-face map has degree three. In case B an edge belongs to two faces. The map from ordered module bases modulo simultaneous negation to oriented edges has degree two in case B. It factors through the ordered triples that are frames of the polyhedron. In case A an oriented edge already serves as a frame. The manuscript calls the frame set a torsor under $G_M$ in both cases.

**Recovering quotient faces, scans 67–68.** Taking the pairs contained in faces recovers the edge set. Grothendieck tries the converse with the requirement that all three pairs be edges and writes “relation fausse !!” in the margin (**E1**). His revised test requires all three edges to have the same type. With $i=\{e,-e\}$, he compares wedges in the basis $(x,y)$ and obtains coefficients in $\{\pm1_\Lambda\}$ (**E2**). Signs can be absorbed in the choice of representatives for a quotient face. His explicit inclusion of the integer ring in the rejected case is considered under **S5**.

**Gauges in characteristic two, scan 69.** Grothendieck asks whether a permutation of nonzero vectors might preserve collinear pairs, bases and equality of gauges while failing to preserve the ternary relation $x+y+z=0$. In the margin he proposes requiring respect for the partially defined addition on the set of determinant generators. The point is marked “à élucider”. The bottom of the page returns to actual vectors and defines the face label by their common cyclic wedge.

**Oriented determinant labels, scans 70–71.** For a general ring an unordered face receives a determinant generator modulo sign. Retaining a cyclic order on its three vertices selects the actual generator. Simultaneous negation of the three vectors preserves this oriented label, which therefore descends to the quotient. The square (181) compares forgetting orientation with taking a generator modulo sign. Scan 71 asks whether the other structures determine this extra one.

**The recapitulation and its two structures, scan 72.** Section V begins with a nonzero commutative ring and a free rank-two module. A triangulated structure consists of vertices and three-element faces, with a partition of faces. The author describes two structures attached to $M$, the second the quotient of the first by $\{\pm\mathrm{id}_M\}$. In (1) the vertices of the first are precisely the vectors belonging to a basis. Its faces are actual zero-sum triples with generating wedge (**T1**). Formula (2) gives both sets of determinant labels.

**Cyclic order and reversal, scan 73.** An oriented face in (3) is a face together with a cyclic order. The check in (4) means reversal of that order. Grothendieck explicitly reserves the minus sign for transport of the ordered face by $-\mathrm{id}_M$. Reversal negates the determinant label. Passing to sign classes gives (6), and taking its fibres gives the polyhedra indexed by $i$ in (7).

**Edges, incidence and parameter torsors, scans 73–74.** In (8) the edges are unordered pairs belonging to a face, equivalently pairs that form a basis. In the tilde structure an edge lies in a unique face, with three choices of edge over a given face. Diagrams (10) and (11) give the unoriented and oriented incidence and type maps. The marginal note says how to pass between them. After cancelling a boxed mutual-recovery assertion, the author identifies the unoriented parameter set as a torsor under $\Lambda^*/\{\pm1_\Lambda\}$ and its oriented lift as a torsor under $\Lambda^*$.

**The sign problem for actual vectors, scan 75.** Grothendieck explains the cancellation on scan 74. The monochromatic-edge condition on three actual vectors yields $z=\pm x\pm y$. A face of the tilde structure requires $z=-(x+y)$. When $2\,1_\Lambda=0$, the choices coincide and the edge test does recover the faces, as (15) states (**T2**). The difference from scan 68 lies in whether a vertex can be replaced by its negative.

**Propagation from a fixed frame, scans 75–77.** The “Question de connexité” asks how far an automorphism fixing a frame is determined. The working hypothesis is that it commutes with antipodism. Fixing $x$ and $y$ of the prescribed type then fixes the third vertex $-(x+y)$ and also $x+y$. Grothendieck describes moves on triples, writes a frame as an isomorphism $r:\Lambda^2\to M$ and follows it under the indexed transformations $\tau$. By invoking the subgroup generated over the integers and its image under reduction (**G1**, **G2**), he obtains his lemma. It fixes vectors $ax+by$ with $a,b$ in the image $\Lambda_0$ of the integers and $a\Lambda+b\Lambda=\Lambda$.

**The absolute-ring theorem, scan 78.** If $\Lambda=\Lambda_0$, the corollary says that an automorphism fixing a frame and commuting with antipodism is the identity. For $\mathbb Z$ or $\mathbb Z/n\mathbb Z$, (16) identifies the sign-determinant group with the automorphisms of a fixed half-symplectic structure that commute with antipodism. Allowing the whole family of face types in (17) gives the full general linear group. The margin proposes that the set of faces by itself may suffice.

**Equivalences and reconstruction, scans 79–80.** The scholium writes $\Lambda_n\simeq\mathbb Z$ when $n=0$ and $\Lambda_n\simeq\mathbb Z/n\mathbb Z$ otherwise, with $n=1$ excluded. Formulas (18) and (19) send $(M,i)$ and $M$ respectively to their associated structures. The author presents equivalences of groupoids, then asks for intrinsic conditions on the structures that occur on the right, a reconstruction of $M$, and a recovery of the data connecting vertices and faces to the ring. In the margin he distinguishes the identity antipodism in characteristic two from an involution with no fixed vertices in the other case.

**The action of units, scan 80.** For a general ring, Grothendieck considers adding the action of $\Lambda^*$ as structure. A separate draft paragraph B about simultaneous negation of vertices, edges and faces is crossed through. The live text returns to general $\Lambda$ and writes $\widetilde T_\lambda x=\lambda.x$ in (20). It discusses the unit action on the partitioned face family and the centre of the linear group. Its last clause, “en respectant aussi”, continues beyond the supplied scans.

## Statements left without proof

| ID | Scan | His words | What is left implicit |
| --- | --- | --- | --- |
| A1 | 65–66 | “La simple transitivité est fausse, sauf si …” and “exactement deux” | The bracket gives the exception. The two incidence counts and the degree of the map in (173) are stated here, without separate proofs for arbitrary rings. |
| A2 | 67 | “Dans tous les cas, l'ens des repères … est un torseur sous $G_M$.” | The text relies on the two definitions of a frame and the preceding action. |
| A3 | 72 | “Les deux structures envisagées dépendent fonctoriellement de $M$” | The quotient is specified, but the action on morphisms is not separately worked out here. |
| A4 | 74 | “Toute arête … est contenue dans … une unique face” | The degree-three assertion and the oriented diagram are recorded directly after the edge definition. |
| G1 | 77 | “Comme on sait que ce sous-groupe est $\mathrm{Sl}(2,\mathbb Z)$ tout entier” | The generation result is invoked. The actual matrices are referred to an earlier page. |
| G2 | 77 | “l'hom … est surjectif” | Surjectivity onto $\mathrm{Sl}(2,\Lambda_0)$ is used in identifying the subgroup. No proof of this reduction statement is given here. |
| A5 | 78 | “est un isomorphisme [car … est simplement transitif …]” | Part (a) gives a reason in brackets. Part (b) writes (17) after describing the structure, without a separate argument. |
| A6 | 78 | “il suffit … de ne regarder que la structure donnée par … tout seul” | The marginal claim would dispense with the partition in (b). The connective before “sa partition” is doubtful. |
| A7 | 79 | “Par les principes généraux, il s'ensuit qu'on a … équivalences de groupoïdes” | The equivalences are presented as consequences. The author calls for an intrinsic description of their images. |
| A8 | 79 | “une involution ss pts fixes” | The margin states this for the second case without a separate argument there. |
| A9 | 80 | “alors $\Lambda^*$ respecte toutes les structures” | The manuscript names the face family and its partition and identifies the scalar units with the centre. The discussion continues off the last scan. |

## Questions and conjectures

| Scan | His words | Mathematical question |
| --- | --- | --- |
| 67–68 | “Je voudrais m'assurer que ces données … se déterminent mutuellement” and “inversement … a-t-on … ?” | Which edge and face data recover one another? The first proposed converse is crossed and annotated, then replaced by the type-sensitive criterion. |
| 69 | “il semblerait”, “je suppose”, “à élucider éventuellement” | Can a permutation preserve collinearity and gauges but lose the addition relation? Would preserving partial addition on the labels recover it? |
| 71 | “dans quelle mesure cette structure supplémentaire se déduit des autres structures” | Can the oriented data in (181) be recovered intrinsically? |
| 74 | “Il faudra à l'occasion interpréter la structure” and “tirer au clair” | What do the torsor of types and its lift mean in terms of the triangulation? |
| 75–76 | “Question de connexité …”, “on aimerait qu'un autom. … qui fixe un repère … soit l'identité” | Does fixing a frame determine an automorphism? The manuscript adds commutation with antipodism for the propagation argument. A crossed marginal word on 76 may read “inutile ?”. |
| 79–80 | “Il conviendrait de caractériser axiomatiquement”, “il faudrait comprendre … comment reconstruire $M$” | Which objects occur in the two target groupoids, and how can the module and the ring-dependent structure be recovered from them? |
| 80 | “on voudrait introduire … un élément de structure supplémentaire (peut-être l'opération de $\Lambda^*$ …)” | What extra data over a general ring recover the two linear automorphism groups? |

## Slips

The suggested forms below are editorial. Their confidence concerns the proposed diagnosis. The page files preserve the readings given in the transcription.

| ID | Scan and place | Written and suggested forms | Reason and confidence |
| --- | --- | --- | --- |
| S1 | 65, label of the face definition | (157), possibly (167) | The next labels are (168) and (169). Medium. |
| S2 | 66, (170) and (171) | $f\ni F_M$, apparently $f\in F_M$ | The variable is a face drawn from the set of faces. High. |
| S3 | 66, (174) | $(s,t,u)\in S_M$, apparently $(s,t,u)\in S_M^3$ | The source of (175) consists of ordered triples. High. |
| S4 | 67, both displays marked (177) | Repeated label, perhaps an omitted “bis” or an unrevised number | The bracketed data and the expression for the edge set are different displays. There is no uniquely reconstructable replacement. Medium for the repetition as a numbering slip. |
| S5 | 67–68, “même sur … $\mathbb Z$” | For the unlabelled quotient-edge criterion, remove the integer ring from the assertion of failure | Over $\mathbb Z$ the determinant generators have just one type modulo sign. The argument on scan 68 then applies already to all edges. The check concerns that displayed implication. High. See R2. |
| S6 | 70, opening sentence | “pas néc. de car. 2 i.e. tel que $2\,1_\Lambda=0$” | Attaching the i.e. clause to “de car. 2” gives a coherent reading. Attaching it to the whole description would conflict with “quelconque”. Low for an actual slip. |
| S7 | 74, definition after (11) | The type map carries an arrow above $\tau_A$ where the unoriented map of (10) would be expected | The inverse image is indexed by a class modulo sign. This may abbreviate the passage to the quotient. Low. |
| S8 | 75, end of the first paragraph | “(et non $z=-(x+y)$.”, apparently “(et non $z=-(x+y)$).” | The displayed sum has its closing parenthesis. The parenthesis beginning the prose aside is left open. Medium. |
| S9 | 75, first sentence | “récette” or “recette”, ordinarily “recette” | A detached accent is hard to place. Low. |
| S10 | 77, end of the lemma | $ad-cc=1$ or $ad-ce=1$, apparently $ad-bc=1$ | Compare the unequivocal $ad-bc=1$ below the matrix earlier on the sheet. The two letters after the last minus remain marked. Low. |
| S11 | 77–78, lemma and corollary | $P_{M,i}$ without the tilde used in (16), possibly $\widetilde P_{M,i}$ | The discussion concerns basis vectors and antipodism. A shortened name is possible. Low. |
| S12 | 78, start of (b) | $\widetilde S_M=M^*$, possibly $\widetilde S_M=M^{**}$ | The defining description on scans 69 and 72 uses vectors belonging to a basis. A preceding capital is overwritten and the second star on scan 72 is doubtful. Low. |

**Reading question raised during the notes · scan 74, L18 (S7).** The frozen reading of the map after “par” is $\widetilde{\overrightarrow\tau}_A$. An enlarged crop separates the wavy tilde, a short horizontal mark and the cross-stroke of $\tau$. The middle mark ends in a dark nub with no distinct pair of barbs. A barred $\widetilde{\overline\tau}_A$ is also possible. The unoriented map of (10) explains the contextual expectation but cannot settle that stroke. Low confidence.

## Pointers

| Scan | His words or reference | Destination visible in these pages |
| --- | --- | --- |
| 65 | “cf plus bas” | The qualification about simple transitivity is followed by the two cases on scan 66. |
| 66–69 | “par (171)”, “par (174)”, “(168, 170, 171)”, “via (177) (168)” | Local references connecting incidence counts, frames and recovery of edges. The repeated (177) is recorded under S4. |
| 68 | “une relation $(*)$ ci dessus” | The signed expression for $z$ at the top of the same sheet. |
| 74 | “(10) … déduit de (11)” | A marginal reference from the unoriented diagram to its oriented version. |
| 76 | “cf (82) p. 15'” | Earlier matrices. The cited sheet is outside scans 65–80. |
| 79 | “cf suggestion (23) ci-dessous” | A forward reference beside the reconstruction question. These scans end at (20). |
| 80 | “(cf. (13)(14)(5) et aussi (118) p. 23)” | (13) and (14) label the two torsors on scan 74. (5) gives the oriented determinant on scan 73. The earlier item (118) is outside the supplied pages. |

No person, published paper or other cote is named on these sixteen scans.

## Remarks of the model

**R1 · Model · high confidence · scans 67–68.** Over $\mathbb F_5$, take $x=(1,0)$, $y=(0,1)$ and $z=(1,2)$. Their three cyclic determinants are $1,4,3$, all units. The four vectors $\pm x\pm y$ have second coordinate $1$ or $4$, so none equals $z$. This computation exhibits exactly the failure of the unlabelled-edge converse on scan 67. The three edges do not all have the same type.

**R2 · Model · high confidence · scans 67–68.** The integer qualification in S5 can be checked without relying on the overwritten formula number. In a unimodular basis, the other two cyclic determinants are the signed coordinates of $z$ times the basis determinant. Over the integers all three can be units only when both coordinates are signs. The calculation log records a symbolic check of the two determinant identities. This is the quotient-triple criterion discussed in E1.

**R3 · Model · high confidence · scans 74–75.** Take the same basis over $\mathbb Z$ and now put $z=(1,1)$. The cyclic determinants are $1,-1,-1$, all of one type, but the three actual vectors sum to $(2,2)$. Reducing the same three vectors modulo 2 gives sum zero. These two computations distinguish the crossed assertion on scan 74 from (15), with the vertex representatives held fixed.

**R4 · Model · high confidence · scan 80.** The scalar action can move a face to another part of the partition. Over $\mathbb F_7$, multiplication of both basis vectors by $2$ changes their determinant from $1$ to $4$, moving the sign class $\{1,6\}$ to $\{3,4\}$. This example spells out how an action preserving the partition in (20) can permute its parts.
