# Mathematical notes on scans 133–148

## What the pages do

**Scan 133. Contents.** A revised contents list places the reminders on Quillen couples and triples before section 4 on paratoposes. Within section 4, the proposed product leads into indexed representations, accessible categories and functors, examples, and a later return to the product. Some page ranges have two or three layers of writing.

**Scans 134–135. The category and its opposite.** A pseudo-$U$-topos category $M$ has small $U$-colimits and a small strictly generating subcategory. Grothendieck asks what this supplies on passing to $M^{\mathrm{o}}$. A small strictly cogenerating subcategory would provide the missing generator on the opposite side. He refers to enough injectives and to an earlier theorem.

**Scans 135–137. Morphisms and adjunction data (D1).** Grothendieck writes $X$ for the pseudo-topos and $M$ for its category of “faisceaux”. For $f:X\to Y$ the functor $f^*$ goes from $N$ to $M$ and preserves small colimits. He calls the morphism exact when $f^*$ is also left exact. He gives the adjoint $f_*$, then packages the two functors and their adjunction maps as $(f^*,f_*,\alpha,\beta)$. He uses equivalence of the adjoints to define equivalence of pseudo-toposes.

**Scans 137–138. The proposed product (D2).** The body introduces $X\times Y$ by a 2-product property. To study maps from a third pseudo-topos $Z$, it writes $M=F(X)$, $N=F(Y)$ and $P=F(Z)$. A trial formula combining two inverse-image functors by a Cartesian product is crossed out. The margin qualifies the proposed universal property and uses $X\boxtimes Y$.

**Scans 139–141. Three descriptions (D3).** An object of $M\boxtimes N$ is presented as a set-valued bifunctor on $M^{\mathrm{o}}\times N^{\mathrm{o}}$ satisfying the limit condition in each variable. Partial representability gives the two one-variable descriptions. A further description records a pair $(\varphi,\psi)$ with its adjunction maps. The four equivalences of (4.1.16) connect these descriptions. The top vertex carries a bar above the product sign. Grothendieck then asks for the colimits and small strict generating subcategory needed to make $M\boxtimes N$ a pseudo-topos category.

**Scans 141–143. Sheaves with coefficients (D4).** With a general coefficient category $N$, the definition on scan 142 is $F(X,N)=\underline{\mathrm{Hom}}^{!}(M^{\mathrm{o}},N)$. The author uses the subcategory of representables in $M^\wedge$ to construct (4.2.3). He describes its essential image by a representability test, continued on scan 143 as the existence of a left adjoint.

**Scans 143–145. Restriction to one small category (D5).** With $S$ a small strictly generating subcategory of $M$, the basic restriction embeds $M$ in $S^\wedge$. A square relates this embedding to restriction of $N$-valued functors. In (4.2.8) the author identifies the category of functors on $S^{\mathrm{o}}$ with sheaves on $\operatorname{Top}(S)$ with values in $N$. Proposition 4.2.1 on scan 145 is the live formulation. The preceding draft is struck.

**Scans 145–146. Restriction in both variables (D6).** Corollary 4.2.2 assumes that $N$ too is a pseudo-topos category with a small strict generating subcategory $T$. Its argument restricts first in one variable, then in the other using symmetry. It yields the embedding $\rho:M\boxtimes N\hookrightarrow(S\times T)^\wedge$. The author compares it with a direct image associated with the two maps into presheaf toposes.

**Scans 146–147. A left adjoint to the joint embedding (D7).** The two individual direct images have left adjoints extending the inclusions of $S$ and $T$. For the joint embedding the author asks for objects $s\boxtimes t$ representing evaluation. The required identity is $\mathrm{Hom}(s\boxtimes t,F)\simeq F(s,t)$. He states Lemme 4.2.3 and adds a warning in the margin.

**Scans 147–148. A test and a new hypothesis (D8).** The trial value at $(x,y)$ is the Cartesian product of two Hom sets. Fixing one variable, the author tests a terminal object and finds the residual value $t(y)$. He considers two functors into $M\boxtimes N$ associated with the projections. Section 4.3 begins with the report that an additional accessibility hypothesis was needed in his attempt.

## Statements left without proof

| ID and scans | His words | Status on these pages |
| --- | --- | --- |
| U1 · 134–135 | “Alors $M$ admet aussi … $U$-limites projectives”; “ce qui implique alors l'existence d'une petite sous-catégorie strictement cogénératrice” | The existence of limits and the step from enough injectives to cogeneration are cited or asserted here. |
| U2 · 135–136 | “C'est le cas notamment si $M$ est un topos”; “En vertu du dual de loc cit 8.12.7” | The marginal special case and the right-adjoint existence statement are given without their own proofs here. |
| U3 · 137 | “ce qui équivaut à $f_*$ une équivalence, ou $\alpha$ et $\beta$ des iso”; “est un 2-produit dans la 2-catégorie des topos” | The equivalence criterion and the topos-only assertion in the margin are stated. |
| U4 · 139–141 | “ces foncteurs sont représentables”; “donne une équivalence de la catégorie de ces couples”; “se calculent argument par argument” | The text passes from separate representability to the equivalences and uses pointwise calculation of small projective limits. |
| U5 · 141 | “Je dis que … est une catégorie pseudo-topos”; “chose de non trivial à démontrer !” | Colimits and a small strictly generating subcategory are still wanted. |
| U6 · 142–144 | “On a donc un foncteur pleinement fidèle”; “cette condition est automatique”; “On sait que cela signifie que le foncteur composé … est pleinement fidèle” | The representable embedding and the starting restriction are used. The text gives a limit-preservation reason for automaticity, then builds the restriction square. |
| U7 · 146–147 | “qu'on interprétera par la suite comme”; “lesquels admettent bel et bien des adjoints à gauche” | The product direct-image interpretation is deferred. The left adjoints of the individual embeddings are identified as canonical extensions. |
| U8 · 147 | “Ce foncteur est représentable”; “Pas prouvé, peut-être faux !” | The author explicitly leaves the evaluation lemma unproved. |

## Questions and conjectures

| ID and scans | His words | Question or qualification |
| --- | --- | --- |
| Q1 · 134 | “Il faudrait en faire une étude systématique” | The abandoned opening asks for a systematic study of the functoriality between two sets. |
| Q2 · 136 | “pour ceci, il faudrait qu'on sache que les foncteurs … sont représentables” | Under what hypotheses does a proposed direct image have the adjoint required of a morphism? |
| Q3 · 137 | “j'ai envie d'introduire … un pseudo-topos produit”; “ce qu'on construit n'est pas un 2-produit” | The margin withdraws the original expectation for the proposed 2-category. |
| Q4 · 141 | “Comment construire des petites” followed by the direct-limit sign and a question mark; “Il faut d'ailleurs trouver aussi une petite sous-catégorie strictement génératrice.” | The definition imposes both pieces of structure. |
| Q5 · 147 | “La question essentielle, à présent, c'est évidemment de construire un … adjoint à gauche”; “Donc il faut prouver ceci” | The author turns the desired left adjoint into a problem about representing evaluation. |
| Q6 · 147–148 | “L'idée naturelle serait de définir”; “Néanmoins, je pense que”; “également faux, cf. plus bas” | He tests a pointwise candidate and then proposes a product of two objects in the target category. The short margin qualifies this latter proposal. |
| Q7 · 148 | “il n'est pas clair”; “en dehors du cas des topos”; “la formule (valable pour les topos)” | The long margin asks about the factorisation using $e_M$ and $e_N$, even on assuming the boxed products exist. |
| Q8 · 148 | “sans y parvenir”; “une hypothèse supplémentaire d'accessibilité” | Section 4.3 reopens the existence question. The continuation falls outside these scans. |

## Slips

The proposed forms below are local comparisons. The visible formulas remain in the transcription.

| ID and scan | As written | Possible intended form and reason |
| --- | --- | --- |
| S1 · 136 | A second “adjoint à droite”, this time for $f_*$. | “À gauche”. The opening of the same page places $f_*$ on the right of the adjunction with $f^*$. Recovering the latter asks for the other side. Medium confidence. |
| S2 · 138 | $(N,Q)$ in (4.1.8). | $(N,P)$. Equation (4.1.7) names $P=F(Z)$ and both functors being described come from the same $Z$. Medium confidence. |
| S3 · 141 | Plain underlined Hom at the right of (4.1.16). | Add upper $!$. It appears on the same Hom in the preceding equivalences and in the ensuing prose. Medium confidence. |
| S4 · 142 | $y\mapsto\mathrm{Hom}(y,\psi(x))$ for fixed $x$ in $M$. | $y\mapsto\mathrm{Hom}_M(x,\psi(y))$. The declared source of $\psi$ is $N^{\mathrm{o}}$ and its declared target is $M$. Low confidence in attributing a slip, since the shaft of the type itself is doubtful. |
| S5 · 143 | The last inner Hom in (4.2.6) uses $N$. | $N^{\mathrm{o}}$. The intervening equivalence above spells out the same inner Hom with the opposite. Medium confidence. |
| S6 · 144 | The lower horizontal arrow in the square is labelled (4.2.4). | Read the reference as “induced by (4.2.4)”. The earlier embedding acts on objects of $M$; this row applies it to functors with values in $M$. It may be an abbreviated reference. Low confidence. |
| S7 · 145 | The initial Hom has no $!$. | The upper $!$ of (4.2.8) would recover the cited comparison, whose left-hand source in the derivation on 144 carries it. Medium confidence. |
| S8 · 145 | Display label (4.2.2-1). | The ensuing paragraph refers to (4.2.2.1). Both identify the same restriction. High confidence in the punctuation difference. |
| S9 · 146 | $N^\wedge$ in the first Hom in (4.2.2.2). | $N^{\mathrm{o}}$ would specialise the definition of $F$ with $N=F(Y)$. In the next formula the exponent is overwritten. Low confidence in attributing the difference to a slip. |
| S10 · 146 | $g_T^N$ in the product before (4.2.10). | $f_T^N$ is the second displayed morphism and the notation for its direct image. Low confidence in the intended correction because the subscript in (4.2.10) was retouched. |
| S11 · 148 | “pour $y$ fixé” followed by “l'objet final de $N^{\mathrm{o}}$”. | With $y$ fixed, the remaining variable $x$ ranges over $M^{\mathrm{o}}$. At an initial object of $M$, the first Hom factor is a singleton and the product reduces to the written $t(y)$. This suggests $M^{\mathrm{o}}$ and $M$ for the two category names in that sentence. Low confidence because the trial formula on 147 has overwritten variables. |

## Pointers

- **Scan 133.** “couples de Quillen”, “Triples de Quillen” and “triples de Q. spéciaux” are listed in the cancelled opening entries. The theorem locators there are 2.3, 2.6 and 2.9. Some accompanying page digits are overwritten.
- **Scan 133.** The contents refer in turn to “th. 4.3.6 p. 70-71”, “th. 4.4.13 p. 95-96”, a doubtful “Cf 4.5.6.” at p. 116, the boxed “4.6.3”, “th 4.9.3 p. 219”, a doubtful last digit in 4.10.1 or 4.10.4 at p. 244, and two 4.13 references, including 4.13.31 at p. 350. The first 4.13 reference and several range endpoints remain doubtful.
- **Scans 134 and 136.** The insertion on 134 reads “SGA 4 I” with a doubtful 8.12.7. The nearby “cf loc cit 8.12.9” is clearer. Scan 136 gives “du dual de loc cit 8.12.7”. The example name on 134 is uncertain.
- **Scans 134–135.** “le th. 2.6.” supplies the reference for the hypotheses concerning injectives. The long margin on 135 ends in a “cf.” without an identifiable destination on that sheet.
- **Scans 144–147.** The square points back to (4.2.3), (4.2.4) and (4.2.5). The corollary proof says “La première assertion a été vue en 4.1”. The problem about the left adjoint on 147 explicitly names “le foncteur (4.2.9)”.
- **Scan 148.** “cf. plus bas” accompanies the short marginal correction. “Hier” points back to the author's own attempt. Neither supplies a dated reference.

## Remarks of the model

**R1 · Scans 146–147 · High confidence.** The individual left adjoints in (4.2.12) target $M$ and $N$. The left adjoint sought for (4.2.9) would target $M\boxtimes N$. Reading the domains and targets explains how the author can affirm the existence of the first pair while calling the third his “question essentielle”. This comparison uses the object names and directions, independently of the short doubtful superscript in the second row.

**R2 · Scans 147–148 · Low confidence.** The terminal-object calculation detects a failure of the proposed pointwise formula whenever $\mathrm{Hom}_N(y,t)$ has cardinality different from one. It leaves open the existence of another object representing evaluation. The distinction matters here because the author expressly doubts the lemma, and because the trial formula contains several overwritten letters.

**R3 · Scans 137–138 · High confidence.** The separate prime in (4.1.5) matters mathematically. Scan 138 assigns the left-adjoint requirement to “l'accent”; scan 137 assigns a limit-preservation condition to the upper exclamation mark. Reading the two signs together accounts for both phrases.
