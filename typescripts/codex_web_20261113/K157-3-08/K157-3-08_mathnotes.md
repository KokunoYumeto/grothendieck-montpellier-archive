# Mathematical notes on scans 114–129

## What the pages do

**U1 · A gluing criterion for toposes (114–115, manuscript pp. 63–64).** Proposition 2 starts with a left-exact gluing functor $\varphi$ between the sheaf categories of two toposes of the form $\operatorname{Top}(U)$ and $\operatorname{Top}(T)$. It says that the glued topos has the same form precisely when $\varphi$ preserves arbitrary inverse limits, or equivalently admits a left adjoint $\psi$. Restricting $\psi$ to $T$ gives the datum $H:U^{\mathrm o}\times T\to\mathrm{Ens}$. The corollary expresses $\varphi(F)(t)$ as $\operatorname{Hom}_{U^\wedge}(H(t),F)$ and identifies $\varphi$ with $j^*i_*$.

**U2 · Maps into a glued category (116, p. 65).** A map into $X$ picks out an open part $U'$ of its source and the complementary closed part $T'$. The restrictions to those parts come with a map from their gluing datum to the pullback of $H$. The author writes the datum on the source as $\operatorname{Hom}_{X'}(u',t')$.

**U3 · Maps out of a glued category (117, p. 66).** Proposition 3 describes a map $X\to X'$ by two maps $f_U,f_T$ to $X'$ and a map from $H$ to the Hom bifunctor of $X'$ evaluated on their images. He states a bijection functorial in $X'$ and then writes a prospective isomorphism of categories of such data.

**U4 · The diagram to be completed (117–118, pp. 66–67).** Section 1.4 allows the open and closed parts to change at the same time. Its diagram has specified maps $U\to U'$ and $T\to T'$. Maps from the sought object to a test category $X''$ should be triples of maps from $X,U',T'$ agreeing on the original parts. When the map on $T$ is the identity, he identifies the construction as an amalgamated sum on the open side.

**U5 · Construction of the new gluing datum (119–121, pp. 68–70).** Precomposition by $F=f_U^{\mathrm o}\times f_T$ gives $F^*$ on categories of bifunctors. The adjunction with $F_!$ rewrites the compatibility map $H\to F^*H''$ as a map $F_!H\to H''$. This supplies the datum $H'=F_!H$ for gluing $U'$ to $T'$. Theorem 1 identifies the resulting $X'$ with the colimit of the original diagram and identifies its complementary open and closed immersions.

**U6 · The arrows from $u'$ to $t'$ (121–123, pp. 70–72).** The value of $F_!H$ is expressed as a direct limit of $\operatorname{Hom}_X(u,t)$. An arrow $u'\to f_U(u)$ acts at the source, and an arrow $f_T(t)\to t'$ acts at the target. He uses the connected components of the category over a presheaf to rewrite this colimit. The first boxed formula on scan 123 gives the resulting description of $\operatorname{Hom}_{X'}(u',t')$.

**U7 · Fixing the closed part (123–125, pp. 72–74).** For $T'=T$ and $f_T=\mathrm{id}_T$, the second boxed formula uses triples $(u,\alpha,\beta')$ with $\alpha:u\to t$ and $\beta':u'\to f_U(u)$. To compare the two component sets, he identifies the smaller category as a fibre at $(t,\mathrm{id}_t)$, initial in the opposite of the slice on $T$. The argument ends by invoking asphericity of an initial-object inclusion and its stability under products.

**U8 · The boundary and the pushout square (125–126, pp. 74–75).** Writing $p$ and $q$ for the vertical maps, Proposition 4 compares the boundaries on the closed part. Membership in the closure is detected by the nonemptiness of $U_{/t}$. For the reverse implication the proof uses the mixed Hom formula. The sideways Proposition 5 states stability of an open or closed immersion under pushout, says the square is also cartesian, and describes the case of two open or two closed immersions. The separate NB specifies the strict sense of immersion used here.

**U9 · The square axiom (126–127, pp. 75–76).** Section 2 introduces a class $W$ of arrows in $\mathrm{Cat}$. For two opens with union $X$, $W(7\mathrm{bis})$ relates membership of the intersection inclusion $i_0$ in $W$ to membership of $i$. There is a symmetric primed assertion and a dual formulation with closed parts. The corollary relates asphericity of the intersection, the two opens, and the union.

**U10 · The cube axiom (127–128, pp. 76–77).** A map between two such squares gives four vertical maps. The three conditions concern the intersection map, the pair of maps of opens, and the map of unions. Any two conditions are to imply the third. Applying this to the map into the diagram with all four vertices equal to $e$ gives the full three-condition result for asphericity.

**U11 · The cube implies the square (129, p. 78).** Proposition 6 uses a second cube. Its lower square repeats $U'$ twice and $X$ twice. Two vertical maps are identities, leaving the membership of $i_0$ and $i$ to be compared.

**U12 · The fundamental localizer (129, p. 78).** Theorem 2 says that $W_\infty$ satisfies the axiom written $W(7)$ here. The author sketches a route through an Artin–Mazur criterion, the exact sequences for the two squares, and noncommutative variants. The page closes with his assessment of the missing verification.

## Statements left without proof

- **P1 (114–115).** The criterion begins “Pour que le topos recollé … il f. et s.” The pages explain how the adjoint produces $H$ and invoke “on sait bien que” for extension from $T$ by direct limits. They give no separate proof of that extension equivalence.
- **P2 (117).** “On trouve tautologiquement” introduces Proposition 3. The set-level description is stated. The stronger claim about categories is left as an expectation.
- **P3 (119, 122).** “Or le foncteur $F^*$ a un adjoint à gauche” and “Notons pour mémoire … on a la formule” introduce, respectively, the adjoint used for the construction and the connected-component formula for a presheaf. Both serve as ingredients.
- **P4 (125–126).** “l’inclusion d’un objet initial est toujours asphérique” and “le reste par produit” close the comparison. The assertion in the margin that “le carré est aussi cartésien” has a reference to Proposition 15 and its corollary.
- **P5 (127–128).** “Par dualité cet axiome est équivalent à l’axiome similaire” and “Cet axiome est équivalent à l’axiome dual” state the closed versions of the square and cube axioms.
- **P6 (129).** “Je n’ai pas fait la vérification en forme” applies to Theorem 2. Its proposed justification is written as “C’est sûrement une conséquence”.

## Questions and conjectures

- **Q1 (114, 117).** “On s’attend dès lors” anticipates the description by $H$ that follows. “Sûrement on aura = un … isomorphisme de catégories” goes beyond the bijection in Proposition 3. The exact opening verb phrase on 117 is marked as doubtful.
- **Q2 (118, 121).** “qu’on aimerait compléter ‘canoniquement’, si faire se peut” is the colimit problem of Theorem 1. “il reste à expliciter” asks for the value of the gluing datum just constructed.
- **Q3 (123–125).** “Je voudrais faire le lien entre les deux formules” leads to “Il faut voir que l’inclusion de la fibre donne une bijection”. The following initial-object argument ends with “d’où la conclusion”.
- **Q4 (125, 127–128).** The two implications on scan 125 each have a parenthetical two-way version. On scan 127 he writes “Moralement, il faudrait aussi que” and “il ne semble pas que l’axiome du carré cocartésien permette de le prouver” about the missing asphericity implication. The cube gives that implication. A distinction remains between proving one axiom implies another and producing an example which separates them.
- **Q5 (129).** “et devrais sans doute réparer cette omission” records the outstanding verification of Theorem 2 at the end of these sheets.

## Slips

| ID and scan | Frozen reading | Suggested reading and basis |
| --- | --- | --- |
| S1 · 116, L10 and L25 | The first inverse-image stem is marked $j/f$. The final triple has a possible double prime on $U$. | In context both inverse images are taken under $f$, and the earlier triple has $U'$. Both suggestions are low confidence because the relevant strokes are doubtful. |
| S2 · 121, L12–17 | $F=f_U^{\mathrm o}\times f_T$ is the subject immediately before the text speaks of interpreting a functor as a presheaf. | Retain that definition of $F$, then read $H$ as the subject of the presheaf interpretation. On 119 the target of $F$ is a product of categories. The datum $H$ takes values in sets, and the colimit on 121 is over values of $H$. Confidence is medium for a change of subject. |
| S3 · 122, L12 | The symbol before membership in $\operatorname{Ob}Z^\wedge$ is marked $C/G$. | $G$ would refer to the presheaf of the preceding formula. The individual glyph favours $C$. Low confidence for a slip. |
| S4 · 126, sideways Proposition 5 | “$X$ s’identifie” is followed by a formula with $X'$ on the left. | The stated pushout is $X'$. A prime on the first $X$ would agree with the formula and the square. |
| S5 · 127–129 | Both $W(7)$ and $W(8)$ occur for the cube discussion. Several numerals are overwritten. | The two designations apparently overlap in this draft. The wording “Lemme des cinq” identifies the axiom without choosing a definitive number. Low confidence for any proposed renumbering. |

## Pointers

- **116, 119 and 120.** “par 1.1.” and “en vertu de 1.3” refer to descriptions of maps of triples.
- **120, 123, 125 and 128.** “page 67” points to the diagram on scan 118. “p. 70” points to the colimit formula on 121, “p. 72” to the special case on 123, and “p. 76” to the square on 127.
- **126.** The sideways text refers to “la prop 15, page 158, et son cor.” Its neighbouring words are among the least secure readings. The main text also refers to “prop. 5” at the introduction of the open square.
- **128.** “cf le NB qui le suit” points back to the remark about the missing implication in the asphericity corollary.
- **129.** “du critère … d’Artin-Mazur” and the two mentions of Mayer/Meyer–Vietoris are pointers supplied by the author. The adjective naming the criterion and the first vowel of the name are marked in the transcription. These sheets give no title or bibliographical details.

## Remarks of the model

**R1 · Model remark, high confidence (123–124).** The two arrows in the triple have different jobs. Checking their endpoints shows that $\beta'$ supplies the structure map of $\bar u=(u,\beta')$, while $\alpha$ supplies the element of the mixed Hom set when $\bar t=(t,\mathrm{id}_t)$. This explains the vertical equality beneath the wavy Greek letter without settling whether it is ξ or ζ.

**R2 · Model remark, high confidence (128–129).** The two applications of the cube use different target diagrams. In Proposition 6 the conditions reduce to $i_0\in W$, $i\in W$ together with an identity in $W$, and another identity in $W$. Checking the four possible truth assignments for the first two memberships gives exactly their equivalence. This checks only the specialization displayed on scan 129.

**R3 · Model remark, high confidence about the scope of these sheets (127–129).** Proposition 6 establishes the direction from the cube axiom to the square axiom. The guarded phrase “sans doute plus fort” on 128 raises the further issue of strictness. These sheets end without a converse proof or an example separating the axioms.
