# Mathematical notes on cote 157-4, scans 212–227

## What the pages do

**Theorem 7.1, scans 212–214.** Starting with objects $M_0$ in a category $M$, Grothendieck asks how to build its monomorphisms. For a nonisomorphism $A\hookrightarrow B$, (7.1.1) calls for a subobject $B'$ which does not factor through $A$. Its intersection $A'$ with $A$ belongs to $M_0$, and the canonical map $A\amalg_{A'}B'\to B$ must be mono. Part 1° compares the closures and the right classes of $\mathrm{Mon}$ and $\mathrm{Mon}_0$. Part 2° gives a functorial factorization and interprets the right class by injectivity in slices. Part 3° introduces an accessible class $W$ and small generators for the closure of $W\cap\mathrm{Mon}$.

**Corollary 7.2, scans 214–215.** The author sets out extra exactness and base-change hypotheses. He identifies $\mathrm{Mon}\cap W$ with its closure and exhibits a small generating part $\mathrm{TC}_0$. He gives the resulting Quillen pair and the additional conditions for a closed Quillen triple. The last condition is expressed using injective objects in $M_{/Y}$.

**Reformulation and Lemma 7.3, scans 216–219.** The proof starts directly with a class of generating arrows. The general lemma concerns classes $C_0,C$ with $C$ made up of monos. Its pushout condition supplies a strictly larger subobject of a fixed $B$ while keeping the map to $B$ in $C$. The construction takes a filtered colimit at a limit ordinal. The size of the set of subobjects bounds the strictly increasing construction. The conclusion is $C\subset\widetilde C_0$, with equality of the closures when $C_0\subset C$. The author returns to factorization at the foot of 219.

**Application to $W\cap\mathrm{Mon}$, scans 220–222.** He writes $B$ as a filtered colimit of small subobjects $B_i$ and forms $A_i=A\times_B B_i$. For a cofinal set of indices the induced $f_i$ lies in $W$. A pushout furnishes a candidate intermediate object $C_i$. The proof distinguishes the requisite facts about $A\to C_i$ and $C_i\to B$. Here the author explicitly strengthens the earlier hypotheses.

**Proof of the corollary, scans 222–224.** To obtain the equality with the closure of $\mathrm{TC}_0$, he checks the stability properties of $\mathrm{TC}=C\cap W$. He then uses the two Quillen pairs and an earlier proposition to obtain the triple. The proof ends on 224 with “Cela achève la dém. de 7.1 et 7.2.”

**Corollary 7.4, scans 224–226.** The author collects five conclusions. The first three concern the two pairs and the triple. The fourth tests left properness by pushing a map in $W$ across a mono. The fifth adds the pullback test along a map of $F$. A short argument for 4° uses $W^{\mathrm{univ}}$ and continues onto 226. The left margin of 224 singles out this corollary as the principal result of the section.

**Section 8, scans 226–227.** The functor $i_A$ takes $F$ to $A/F$. The localizer $W_A$ is the inverse image of $W$ under this functor. Having listed properties of $W$, Grothendieck turns to the cardinal filtrations of $\widehat A$ and $\mathrm{Cat}$. Formula (8.4) measures the size of a category by its set of arrows. The small subcategories of $X$ give a filtered presentation of $X$. The page ends with claims about condition d) and filtered colimits of monos.

## Statements left without proof

| Scans | His words | What is asserted or invoked |
|---|---|---|
| 212–213 | “Ces conditions sont satisfaites si on suppose” | The bracketed NB gives sufficient closure and exactness conditions for the object-generator hypothesis. There is no separate proof of this criterion here. |
| 213, 215, 219 | “il y a assez d'injectifs”; “Donc (th. 1 du § 1)”; “L'énoncé de factorisation est le th 1 du §1.” | The slices interpret the right class. The general functorial factorization theorem used for the pairs is invoked from §1. [B1] |
| 218–219 | “Si i est un iso, on sait”; “Il suffit de la condition” | Membership of an isomorphism in the indicated closure is taken for granted. The author also says that testing successor transitions suffices for all transitions. |
| 220–222 | “C'est clair pour toutes, sauf pour b)”; “Cette condition est vérifiée”; “Or les deux dernières sont induites par le fait” | The other hypotheses of the lemma are taken as immediate. The new pushout condition is referred back to the strengthened hypothesis. Stability under filtered limits is invoked for the last two closure properties listed on 222. |
| 223–224 | “La nécessité est évidente, par définition”; “(prop. 4.3, cor. 4, page 36) qu'il en résulte que” | The necessity of the two conditions on the triple is taken from the definition. The final implication uses a result on an earlier page. [B2] |
| 226 | “Quant à 5°) c'est une tautologie”; “Bien connue pour” | The author dismisses the last properness test after treating 4°. For the cardinal filtration of $\widehat A$, he refers to that of sets and gives an SGA reference. [B3] |
| 227 | “La condition a) est évidente”; “Notons que”; “il est clair aussi que”; “se vérifie immédiatement”; “Ainsi que les mono sont stables” | These introduce the assertions about the filtration of categories, its stability under the specified limits, a cardinal bound on small subcategories, and the last two checks. The page does not develop a separate proof of each assertion. |

## Questions and conjectures

- **216–217.** “il y a des chances” carries over the sheet boundary to “sera alors bel et bien mono...”. The hope concerns the map from the pushout to $B$ in the example formed from $B'\to B$.
- **220–221.** “On a besoin de savoir que le syst. inductif des flèches $f_i$ est $\Pi$-adapté”. The response is to postulate e′, concerning filtered colimits and change of base.
- **221–222.** “a besoin de savoir que $\alpha_i\in W$” and “Il faudra que nous sachions de plus que $\beta_i$ est mono” are successive proof obligations. The author records the strengthened assumptions and continues with “Ayant fait cela”.
- **226–227.** “il faut vérifier les conditions a) b) c) d) e) du §5”. The author begins and discusses those checks on the two sheets. The words introduce a task within the proof.

## Slips

| ID | Scan, location and reading retained | Apparent correction or question | Confidence and reason |
|---|---|---|---|
| S1 | 212, foot, $A_1\times_A A_2$ | $A_1\times_B A_2$ | High. The two subobjects have just been assigned the same ambient $B$, and the continuation maps their amalgamated sum to $B$. |
| S2 | 215, upper and middle displays, two labels with final 5 | Possibly two distinct numbers were intended | Low. There are cancelled digits and a possible prime on a nearby 4. A complete renumbering cannot be recovered. |
| S3 | 216, “Pour” followed by the doubtful abbreviation tte/tt, a cancelled flèche and live “mono” in (7.2) | Possibly add the nonisomorphism restriction | Low. If $i$ is an isomorphism, a map to its target factors through it. The parallel clause on 217 has the restriction. The abbreviation on 216 is doubtful. |
| S4 | 217, central pushout, possible $A'\amalg_{A'}B'$ | $A\amalg_{A'}B'$ | Low. The lower-left object is $A$ and the displayed formula on 216 uses it. The mark after the first $A$ on 217 could be a prime. |
| S5 | 219, “morphismes de transition” $j_{\beta',\beta}$ | Possibly $i_{\beta',\beta}$ | Low. The preceding successor is labelled $i_{\beta+1,\beta}$, and the earlier $j_\beta$ leads to $B$. The author could simply have chosen a different letter. |
| S6 | 222, “par 7.1.4. a)” | Possibly (7.1.4) b) | Low. On 214 a) asserts accessibility. The following b) concerns a composite and its factors, but the Greek letters in that clause overlap. |
| S7 | 223, foot, “$\mathrm{TF}\subset W$ par 7.1.7” | (7.2.7) | High. The brace on this same sheet explicitly includes $\mathrm{TF}\subset W$ and is labelled (7.2.7). On 214 the live (7.1.7) gives an equality of closures. |

## Pointers

- **213–215, 222, 224.** The notes point to “la condition ⓔ p. 76”, the lettered “conditions a) b) c) d) e) de p. 76”, and “((7.2.1.) p. 88)”. Manuscript p. 88 is scan 214.
- **215, 219, 222.** “th. 1 du § 1”, “le cor. 2 du th. 1, §1” and the foot of 222 refer to the earlier factorization/closure result. The inserted page number on 219 looks like 19 or 18. On 222 the final page number is 12 and the corollary number is doubtful.
- **223–225.** “prop. 4.3, cor. 4, page 36” is the reference completed at the top of 224. Quillen is named throughout the statements about closed pairs and triples.
- **226.** “du §5” points back to the treatment of accessible parts of a large category. The bracketed reference reads “cf SGA 4 I 9.2[4 or .4], p. 172”. Under “7 bis” appears the quoted abbreviation “M.V.”.
- **227.** “loc. cit 9.12”, “de ces notes, p. 45-46”, “par la méthode du §5”, “de p. 45” and “(condition e) page 46)” identify the sources of the earlier filtration tests. The distinction between the two written SGA locators is retained.

## Remarks of the model

- **R1 · My remark, high confidence, 217–219.** The smallness assumption added at the edge of 217 does work at a precise point on 219. A strictly increasing sequence of subobjects gives distinct values for distinct earlier ordinals. Its index set therefore has cardinality at most that of the set of subobjects. This local check concerns the displayed inequality.
- **R2 · My remark, high confidence, 220–222.** Following the two labelled arrows in the central diagram explains the two amendments. The pushout supplies the map labelled $\alpha_i$. The further mono assertion refers to $\beta_i$, the next map to $B$. These are separate obligations even though their composite is the original $f$.
- **Reading question, 226, b).** The frozen formula for $\widehat A$ has an unmarked $A$ in the first argument of underlined Hom. An alternative would be an $A$ carrying a very small variance mark. I see no distinct such mark in the crop, and the two pages supply no second spelling of this formula. I have retained the plain $A$.
