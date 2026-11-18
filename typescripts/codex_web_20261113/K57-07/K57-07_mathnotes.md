# K57-07 · Mathematical notes

The scan numbers below follow the supplied images. Quotations retain the notes’ French wording. Where a reading affects an interpretation, its uncertainty is stated. The statement IDs identify the limited checks in `CHECK_EVENTS.tsv`.

## What the pages do

**210–211 · The prime-to-characteristic part of the Picard functor.** The proposition defines $P'$ fibre by fibre inside $P=\underline{\mathrm{Pic}}_{X/S}$. It uses the inverse image in $P_s^\tau$ of the elements of order prime to the characteristic in $P_s^\tau/P_s^0$. The conclusion calls $P'$ constructible and quasi-compact. The hypotheses above it were added in unusually small writing.

**210–211 · Proof by restriction to an open set.** The author shrinks an integral base, extends the subgroup at the generic point to a group $H$, and compares $H$ with $P'$. The crucial step on 211 involves the left $n$-torsion index. Over the open where $n$ is invertible he uses specialization in an étale scheme to put the relevant points of the special fibre in the closed group $H$.

**211–212 · Two corollaries.** The first concludes « Alors $P^\tau$ est de type fini sur $S$ » under two conditions. The next sheet starts again from $P^0=\bigcup_{s\in S}P_s^0$ and its closedness. The finite-type clause and the proposed final conclusion concerning $P'$ are visibly crossed there.

**214 · A conic over $k[t]$.** The graded equation is $xy-tz^2$. The first lemma concerns the defining ideal and the ring at the augmentation ideal. The corollary states regularity of $X$ and flatness over $S$. The author describes the fibre away from $a=(t=0)$ as a projective line and the fibre at $a$ as two projective lines joined together.

**214 · Cohomology and restriction.** A sequence at the special fibre is followed by a vanishing statement for positive cohomological degrees. The map labelled $(*)$ restricts from a local base change to its special fibre. The text calls it injective and describes its target using one or two copies of $\mathbb Z$. Its target sheaf presents the reading problem S214 below.

**215–217 · Divisors, sections and degrees.** The author assigns degrees to the line bundles of the components $Y_i$. He relates $D_1+D_2$ to $\operatorname{div}(t)$ and writes a sequence with map $\beta$ to $\mathbb Z$. He identifies its kernel using the class of $D_1$. On the affine chart $xy=t$, the choices $(1,t)$ and $(t,1)$ supply the two sections. The proof then restricts to $U$ and uses the Laurent polynomial ring. Lemme e invokes the preceding corollary for surjectivity of $(*)$.

**217–219 · A prescheme representing the functor.** An initial argument using a local ring at a hypothetical point is crossed out. The live construction takes one copy of $S$ for each $i\in I$ and glues the copies over their common open $U$. For each integer $n$ the index set consists of pairs $(p,q)$ with $p+q=n$. The author takes the disjoint union over $n$, describes the fibre over $a$ by $\mathbb Z\times\mathbb Z$ and the other fibres by $\mathbb Z$, and identifies the resulting prescheme with the Picard functor.

**220 · The cone example.** The argument passes from $g:\widehat C_X\to\widehat C$ to a map on $H^1$ of units. Restriction along the zero section isolates the twist $(n)$ in a class written using $\varphi^*(\eta)$. The boxed conclusion gives $\mathbb Z$ with generator the class of $\mathcal O_{\widehat C}(1)$.

**221 · A degeneration of quadrics.** The projective equation is $x^2+y^2+z^2-\lambda t^2$. The calculation over a local base is split into two cases. One gives $\mathbb Z$ with a degree-one generator and invokes a circled vanishing of $H^1$ of the structure sheaf. The other gives $\mathbb Z^2$ with generators $\alpha,\beta$. The last lines concern closed finite-type parts of the Picard scheme and properness over $S$.

**222 and 224 · Three relative lines.** The table identifies the three factors $x,y,x+y+tz$, their ideals and the subschemes $X_i$. The flatness argument uses membership in the three ideals. Scan 224 proves the relative intersection assertion by substitution and divisibility, then lists the components, their pairwise intersections, and the triple intersection over the zero locus of the parameter. The last corollary starts a calculation of $H^1(X,\mathcal O_X)$ by descent along the disjoint union of the components. The last visible display ends at an isomorphism sign.

**225 · Associated débitages and transitivity, typescript p. 58.** In document n° 215 the sections $s_{x,\xi}$ define the associated débitage. The author describes how an isomorphism of structures induces one on an associated species and then on a second associated species. The paragraph concludes with « la transitivité des fûts associés ».

**225 and 223 · Proposition 2, typescript pp. 58–59.** The proposition begins in the last line on 225 and continues in the first line on 223. It concerns a homomorphism of fûts and the resulting homomorphism on their associated fûts. The proof compares associated débitages, proves $f\circ J_y=J'_{y'}\circ f$, and passes to the canonical extensions on the échelons. The supplied p. 59 breaks off while describing a restriction.

## Statements left without proof

| Scan | Author’s words | What the sheets leave implicit |
|---|---|---|
| 210–211 | « Il provient d’un groupe … de type fini sur un voisinage » and « on sait … que sur l’ouvert … » | Spreading out the group and the étale assertion for the cohomology sheaf are used without their own proofs. The parenthetical reference after « on sait » is uncertain. |
| 212 | « supposons $P^0$ fermé. Alors $P^\tau$ est fermé » | The short corollary contains no separate argument. Its later clauses are revised. |
| 214 | « est un idéal premier », « $X$ est … régulier, et $f:X\to S$ est plat » | The ring and morphism assertions are stated directly. The fibre descriptions and the displayed vanishing also have no detailed proofs on this sheet. |
| 214, 217 | « est injectif » and « est en effet surjectif grâce au corollaire précédent » | Injectivity and the description of the target are announced on 214. The later surjectivity argument refers back to the computed restriction. |
| 215 | « par un calcul immédiat [qu’il faut savoir faire] » | The calculation of the degree on the other component is invoked at precisely this point. |
| 219 | « représente le foncteur Picard » | After identifying the fibres the author asserts representability. These lines do not construct a universal bundle or write out the functorial identification. |
| 220 | « est injectif », « Or [réf] » | The direct-image statement, the induced injection and the projective-bundle expression for a class rely on brief reference marks. |
| 221 | « on déduit que c’est encore vrai pour $A$ quelconque », « la même méthode donne … $\mathbb Z^2$ » | The circled cohomology vanishing is invoked. The lifting argument and the calculation for the second case are left short. |
| 222, 224 | « les idéaux … sont … premiers », « Lemme 2 … On a » | The three prime ideals and injectivity from the base ring are used on 222. The three quotient-ring identifications on 224 are tabulated. |
| 224 | « justification … est un morphisme de descente … » | A compressed insertion appeals to descent. The calculation after the final isomorphism sign is outside the supplied text. |
| 225 | « il résulte immédiatement que ce débitage ne dépend pas du choix de $x$ », « Il est clair que » | Independence of the choice of $x$ and the identification of the two successive induced isomorphisms are asserted in the typescript. |

## Questions and conjectures

None explicitly formulated. The working reminders « qu’il faut savoir faire » (215), the possible « vérif » (220), and the placement instruction in the margin of 221 are recorded in the sheet notes. The question-like overwritten sign beside $S_I$ on 218 cannot be read as a mathematical question with confidence.

## Slips

| ID and scan | As written | Apparent intention and reason |
|---|---|---|
| **S214 · 214** | In $(*)$ the target is $H^1(X'_0,\underline{\mathcal O}_{X'_0})$. | A star on the target sheaf would make this a restriction of units, matching the explicit map on 215. Possible omission, low confidence. |
| **S215 · 215** | The calculation ends $L_{D_1}\mid D_1=1$. | If this denotes the same component restriction as above, the expected degree is $-1$. The preceding restriction is the negative of one whose degree is 1. The component letters have been overwritten, so the slip attribution has low confidence. |
| **S216 · 216** | « Démonstration du lemme d. » introduces the two sections. | The sections are announced in « Lemme c » on 215. The intended reference appears to be c. The nearby lettering was revised, so confidence is low. |
| **S218 · 218** | $S_i\cap S_j=U\times\{I\}$, with no condition on the indices. | Read the assertion for $i\ne j$ (**S218r**). By the immediately preceding definition, the point $i$ remains in $S_i\cap S_i$. High confidence in the need for distinct indices. |
| **S221 · 221** | The first case uses $\lambda$ and the second starts « Si au contraire $\xi$ … ». | The complementary case appears to call for $\lambda$. No new parameter is defined between them. The ideal letter in the first condition is doubtful. Low confidence in the slip attribution. |
| **S223 · 223** | The isomorphism from the fibre at $x$ to that at $y$ is first named $J_x$. | $J_y$ would agree with the displayed identity and with the later words « $J_x$ est l’automorphisme identique ». Medium confidence. |
| **S224 · 224** | The sign between $-x$ and $z\tau$ in the first $G$ may be plus. | Minus would agree with $y=-(x+z\tau)$ and with the subsequent $G(x,-x-\tau z,z)$. The sign itself is unclear. Low confidence. |
| **S225 · 225** | « Nobs » or « Nous l’appellerons ». | The verb calls for « Nous ». Whether the typewriter actually struck b is uncertain. Low confidence. |

## Pointers

- **211** has « on sait (réf) » or « (cf) » before the étale cohomology assertion. No title or number follows it.
- **214–217** repeatedly cite « (*) », « corollaire 1 », « lemme c », « cor. 2 » and « Corollaire 3 ». On 215, « cf … » after the special fibre has no completed reference. On 216, « du th. … sur $H^1(S,P^1_S)$ » identifies a subject without a bibliographical title.
- **220** has short bracketed references or verification marks by the direct image, the injection and the twist formula. The longer one ends « sur … loc. libres quelconques ».
- **221** has a marginal direction « à mettre au lemme » or « à mettre ailleurs ». **224** explicitly calls back to « ce dernier lemme » and « Corollaire du lemme 0 ».
- **223 and 225** are numbered n° 215. « ci-dessus » on printed p. 58 and « ce qui suit » on p. 59 refer within the typescript.

No named correspondent, author, publication or other archive cote is cited on these sheets.

## Remarks of the model

- **M216 · Scans 215–216. Model remark, high confidence.** Both listed coordinate pairs satisfy $xy=t$ identically. At $t=0$ they become $(1,0)$ and $(0,1)$. This connects the two concrete sections on 216 with the two components used in the degree calculation on 215.
- **M219 · Scans 218–219. Model remark, high confidence.** The two descriptions carry different labels because gluing identifies points over $U$ with the same total degree. Over $a$ the pair $(p,q)$ survives. This follows directly from the stated index set and the common-open construction.
- **M225 · Scans 223 and 225. Model remark, high confidence.** Reading printed p. 58 followed by p. 59 joins « une espèce de » to « structures associée à $S$ ». « associée » can agree with « espèce » across that page break. The singular ending alone supplies no reason to emend the typescript.
- **Reading question, 220, pullback formula.** The frozen composite is $\varphi\varepsilon$. Its second character also resembles $g$ in the direct-image identity above. Both compressed characters lose part of their loop on the baseline. The geometric argument would favour the zero section, but that consideration cannot settle a glyph. Confidence in the alternative is low.
