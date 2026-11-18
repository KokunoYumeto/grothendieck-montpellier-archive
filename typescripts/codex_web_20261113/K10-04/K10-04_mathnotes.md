# K10-04 • Mathematical notes

## What the pages do

**139, change of coefficients.** In a tensor category over $K$, an action of $K'$ on an object $X$ is given by a map to $\operatorname{End}(X)$. The relative tensor product imposes equality between the two scalar actions. The underlined Hom uses the corresponding kernel. For an affine group and a fibre functor the sheet identifies the base-changed group and writes down the coefficient-extension and forgetful functors.

**139–140, motives and duals.** An ordinary motive with an action of a number field provides the example. The action on its dual involves transposition. A polarization supplies an involution, and the boxed formula relates the dual of $E_\varphi$ to the motive with modified action $\varphi'$, with a weight twist. For level zero and rank one, duality takes a character $\chi(g)$ to $\chi(g^{-1})$. The sheet ends with the condition that its values lie in $\{\pm1\}$.

**141, cover.** The two live titles name structures on vector spaces and representation rings of certain algebraic groups. Neither title gives a date.

**143–144, change of finite group.** The category of finite-dimensional vector spaces with a $G$-action carries a tensor product. Restriction is contravariant. Pullback along two projections gives an external product, and pullback along the diagonal recovers the internal product. Induction supplies maps in the other direction. The author records unit maps, inversion for an isomorphism, interchange of factors and the action of an inner automorphism.

**144, the product $*$.** For symmetric groups, induction along the inclusion of a product of smaller groups defines a product on representations of different degrees. The interchange of two blocks is used to compare $M*M'$ and $M'*M$. A three-block formula expresses associativity. A sloping note relates this product to the external one.

**145–147, tensor powers.** $T^n(M)$ acquires a symmetric-group action. Formula (16) decomposes the tensor power of a sum using $*$. The square (17) expresses compatibility with restriction. Block permutations enter the comparison of iterated tensor powers in (18)–(20). Scan 146 consists of the tensor-product identity (21). The next sheet records biadditivity of $*$ and its degree-zero unit.

**147–148, passage to classes.** The class ring $A(G)$ inherits restriction and additive induction. The author recovers its multiplication from the external operation and then assembles the components associated to symmetric groups into a graded ring. Equations (29) and (30) compare restriction of $*$ to an external or ordinary product using a factorial coefficient.

**148–150, total operation.** The maps $T^n$ are collected into a map with target in a completion. Two formulas both numbered (33) describe its behaviour on sums and products. The square on 149 gives naturality. Scan 150 recapitulates the ingredients in four items and has an inverted, diagonally cancelled working block below them.

**151–152, characters of a torus.** The author expresses the Chern components of a representation as elementary symmetric functions in its weights. The rank and total class of a single character determine the displayed homomorphism. For injectivity he invokes the independence of exponentials. For density he turns to prescribing finitely many homogeneous components through integral linear forms. The lemma and the pencil diagrams with $B_T$ and $X$ are followed by an explicit request for a proof.

**153–154, characteristic maps.** $K(G)$ is introduced through irreducible rational representations, together with its graded ring of Chern classes $CK(G)$. A principal $G$-bundle $P$ on $X$ takes a representation to an associated vector bundle. This gives $K(G)\to K(X)$ and a characteristic homomorphism $CK(G)\to A(X)$. The square and triangle on 154 describe their compatibility with the total class and with change of group.

**154, torus proposition.** The representation ring of a torus is identified with the group algebra of its character lattice. A basis gives a localized polynomial presentation. The sheet also identifies the Chern ring with the symmetric algebra on that lattice and writes the separate Chern components of a character.

## Statements left without proof

| Scan | His words | Statement or remaining step |
|---:|---|---|
| 139 | « alors … est défini par le groupe affine » | The fibre-functor description persists after the indicated field extension. |
| 143–144 | « Cela permet de définir de façon purement formelle » and « On a un isomorphisme canonique » | The product constructions and their coherence maps are written down. Their coherence identities are not proved here. |
| 144, (5), 147, (26) | « Les relations … sont », « multiplication par » | The composites of induction and restriction are assigned an index factor. See R1 and R2 below. |
| 145–146 | « Sa propriété essentielle est », « Sous ces conditions, on a », « On a aussi » | The sum, iteration and tensor-product laws for the tensor-power functors are stated in (16), (20) and (21). |
| 147 | « grâce au th. de Jordan-Hölder » | The marginal note asserts injectivity on classes for restriction along a surjection. |
| 148 | « Ces propriétés suffisent », « D’ailleurs, on a » | The graded-ring construction and the comparison with factorial multiples are asserted. See R3. |
| 151–152 | « Je dis que cet hom (1) est injectif … et à image … dense », « donc à prouver le Lemme » | The text gives an injectivity argument and reduces the density assertion to existence of suitable forms. A proof of the displayed lemma does not follow on 152. |
| 153–154 | « c’est un anneau gradué », « on a un homomorphisme canonique », « Proposition » | The functorial Chern-ring constructions and the torus proposition are recorded without a full derivation on these sheets. |

## Questions and conjectures

- **143–144.** « à préciser !! » and the doubtful « formuler la propriété de cet isomorphisme » concern the sense of the external-product compatibilities and the isomorphism induced by an inner automorphism.
- **145.** The marginal « et propriété analogue pour les … ? » asks for a further analogue. The final noun remains uncertain. After (17), « à préciser les compatibilités … éventuelles d’hom. fonctoriels » leaves the compatibility data open.
- **147.** « Mais pas leur structure de λ-anneau pour l’instant » limits what the preceding reconstruction has established.
- **149.** « Il faut voir comment s’expriment les $T^n(\lambda^i(\alpha))$, on y reviendra. »
- **152.** « Il faudrait prouver que » introduces the identification of $\mathbb Z[\widehat T]$ with the Chern ring attached to $A(T)$.
- **154.** « Il reste à calculer explicitement $CK(G)$. » A result for tori follows.

## Slips

| ID | Scan | Reading, proposed correction and reason |
|---|---:|---|
| S1 | 143, (2′) | The left side has $M,M'$ and the right $M_1,M'_2$. Matching the argument names on both sides would remove the discrepancy. Medium confidence. |
| S2 | 144, after (13) | The conjugation condition alone does not single out « α unique ». For $p=q=1$ either permutation conjugates the trivial subgroup in the required way. Specifying order-preserving interchange of the two blocks would select one. Low confidence about the intended uniqueness claim because the phrase is next to a revision. |
| S3 | 145, (18)–(19) | In (18) the left side is evaluated at $i$, while the right side still denotes a permutation. In (19) the written upper endpoint $i(q+1)$ makes the interval length $i$. The upper endpoint for consecutive blocks of size $q$ would be $(i+1)q$, with the corresponding change in the image interval. Medium confidence for the missing evaluation, high for the endpoint discrepancy. |
| S4 | 147, (26) | Both orders carry « multiplication par $[G':G]$ ». Each equation requires additional hypotheses if applied to the full representation ring. R1–R2 give concrete failures. High confidence. |
| S5 | 148, (30) | The corrected numerator is $(2p)!$, while the denominator remains $p!q!$. Setting $q=p$ in the index gives $(p!)^2$, as on 150. Low confidence about the author’s intended revision because it rests on an overwrite. |
| S6 | 148, final displays | The two successive labels are both (33). If separate references were wanted they would require distinct labels. The manuscript gives no replacement. High confidence. |
| S7 | 150, (iv) | In the sum formula the second factor is $T^q(\alpha)$. The parallel formula on 148 has $T^q(\beta)$, agreeing with the second summand on the left. High confidence. |
| S8 | 154, proposition | The line for $x^i$ gives $1-x^it$ and the line for a character gives $1+\chi t$. If $x^i$ is the corresponding character, the latter convention calls for $1+x^it$. High confidence in the discrepancy. |
| S9 | 139, lower middle; 151, first paragraph | On 139 the reading « le’objet » may duplicate the article, which is crowded against a cancellation. Low confidence. On 151 « ils ne dépendent » follows « Les fonctions »; « elles » gives agreement if the functions are the antecedent. Medium confidence. |

## Pointers

| Scan | Words on the sheet | Destination |
|---:|---|---|
| 140 | « de niveau zéro », $\pi=\operatorname{Gal}(\bar k/k)$ | The character example on the same sheet. |
| 141 | « algèbres de Hopf top. » | Subject named on the cover. |
| 145 | « De plus », « Sous ces conditions » | From tensor powers and restriction to diagrams (17)–(20). |
| 147 | « grâce au th. de Jordan-Hölder » | The named theorem, cited in the left margin. |
| 148–149 | « la formule 16 », « On déduit de (21) », « compte tenu de (29) », « on y reviendra » | References within the finite-group sheets, followed by a deferred calculation. |
| 151–154 | « anneaux de Chern », « top via Chern », « hom. caractéristique » | The named Chern construction and its topological and algebraic maps. |

The sheets name no external publication by title, volume or page and give no other cote number.

## Remarks of the model

- **R1 — model, high confidence.** For the restriction-of-induction formula on 144 and 147, take $C_3\subset S_3$ over $\mathbb C$ and a nontrivial character with value $\zeta$ on a generator. The restriction of its induction has value $\zeta+\zeta^{-1}=-1$ there. Two copies have value $2\zeta$. **R1a:** the formula can be used for this normal-subgroup situation when conjugation preserves the character.
- **R2 — model, high confidence.** For the reverse composite on 147, take $\{e\}\subset C_2$ and the trivial $C_2$-character. The regular representation has trace zero at the nonidentity element; two trivial copies have trace two. **R2a:** in this example the factor is the permutation representation on the cosets; its dimension is the index.
- **R3 — model, high confidence for (29) and the clean formula on 150.** Take $p=q=2$ and trivial representations in both factors. The induced representation permutes the six two-element subsets of a four-element set. The transposition $(12)$ fixes two of them, and the diagonal element $(12)(34)$ also fixes two. Six trivial copies have trace six at either element. **R3a:** the coefficient counts the dimension in this example. Applying this observation to the author’s amended (30) has low confidence because its coefficient is overwritten.
- **R4 — model, low confidence as an interpretation of the lemma on 152.** For an actual list of integral forms $a_jX$ in one variable, vanishing of their sum gives second elementary coefficient $-\tfrac12\sum a_j^2$. This excludes $+X^2$ for such a list. Scan 151 also speaks about the group $A(T)$, whose virtual elements may change the intended problem. Some argument indices of the lemma carry doubt marks.

**Reading questions noticed after the witness check.** These concern the frozen wording and do not enter the hashed transcription.

| Scan and source line | Frozen wording | Other reading worth checking | Stroke or layout |
|---|---|---|---|
| 145, line 15 | « Sa propriété essentielle » | « La propriété essentielle » | The initial has an open upper loop similar to the initial of « La ». |
| 150, line 9 | « opérations bilinéaires » | « applications bilinéaires » | The pale first word after the deletion has a high group in its middle and an ending compatible with either. |
| 151, line 15 | $A(T)=\mathbb Z(\widehat T)$ | $A(T)\simeq\mathbb Z(\widehat T)$ | In display (1) the upper stroke of the connector looks wavy. The separate heading uses a clearer equals sign. |
| 153, line 30 | « a commutativité des » | « a commutativité dans » | The short terminal word is compressed. The diagram follows on the next sheet. |

