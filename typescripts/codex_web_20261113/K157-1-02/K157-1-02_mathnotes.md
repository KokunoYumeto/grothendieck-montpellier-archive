# Mathematical notes on cote 157-1, scans 18–33

## What the pages do

**Scans 18–19 · A18, C19.** Grothendieck starts with abélianisation from Hot to Hotab. He asks what compatibility with direct image would imply for a cartesian square with a fibration on one side. The slanted note on 18 objects already when $Y$ is a point. On 19 he writes down two comparisons for a morphism $u$ of derivators. One goes from $u_J f_*$ to $f_*u_I$, the other from $f_!u_I$ to $u_J f_!$. Their invertibility becomes the question. The margin distinguishes exactness on the left, on the right, and on both sides.

**Scan 20 · D20.** The dual derivator has value $\mathbb D^\circ(I)=\mathbb D(I^\circ)^\circ$. The square of Hom categories gives its action on functors and their transformations. The last two displays relate the construction to taking the opposite of a category $\mathcal M$ with distinguished arrows $\Sigma$.

**Scans 21–22 · L21, I22.** A functor on fundamental categories prompts the question of lifting it to a morphism of derivators. To apply this to the operations attached to a functor of indices, the notes introduce $\mathbb D_I(J)=\mathbb D(I\times J)$. Their formula for the action in $J$ comes from $h\mapsto\mathrm{id}_I\times h$. Grothendieck then considers which adjoints and axioms pass to $\mathbb D_I$.

**Scans 23–25 · F23, X25.** For $f:I\to I'$, the three operations on the shifted derivators are specified at $J$ using $f\times\mathrm{id}_J$. The two direct images require the respective adjoints to exist. The same symbols then serve at both levels. Introducing $g:J\to J'$ gives a square of four product categories. A comparison across that square expresses commutation in the two independent variables.

**Scans 25–27 · C26.** The square involving only direct images with lower stars commutes up to canonical isomorphism. Grothendieck then puts lower stars in one direction and lower exclamation marks in the other. He constructs a map $G'_!F_*\to F'_*G_!$ using a previously invoked comparison and a unit of adjunction. Scan 27 asks when this new map is invertible.

**Scans 27–28 · N27, P27.** For presheaves of sets, extension along the indicated closed immersion has terminal value on its complement. This obstructs preservation of the initial presheaf when the complement is nonempty. The proposition pairs left exactness with finite products and right exactness with finite sums, including the empty cases. The next sheet discusses the diagonal indexed by a finite discrete category.

**Scans 28–29 · H28, H29.** The derivator represented by $\mathcal M$ has value $\underline{\mathrm{Hom}}(I^\circ,\mathcal M)$. Writing this category as $\mathcal M(I)$ identifies the shifted derivator with the one represented by $\mathcal M(I)$. Grothendieck invokes an equivalence of Hom categories to pass from morphisms of represented derivators to functors, and states the corresponding exactness criterion.

**Scans 30–31 · K30.** Removing the final vertex of a square leaves three indexing objects. On contravariant diagrams, the direct image completes the missing vertex by $F_a\times_{F_0}F_b$. In the abelian example this is a kernel. Replacing $F_0$ by zero gives an epimorphism of the original diagrams, but the map at the missing vertex is the inclusion of the fibre product into $F_a\times F_b$. The heading “Perplexité” introduces a possible stronger, triangulated notion of additive derivator.

**Scans 31–32 · B32.** To calculate $f_*(F)$ at $j_0$, the notes introduce the category of pairs $(i,\varphi:f(i)\to j_0)$. Its projection $q$ forgets $\varphi$. The square with the point selecting $j_0$ has a comparison $fq\to pf'$ whose component at the displayed pair is $\varphi$. The boxed formula extends the construction to a square equipped with such a comparison.

**Scan 33 · B33.** The desired transformation is $p^*f_*\to f'_*q^*$. The sheet gives two routes by adjunction. The first uses the unit for $q$ and a comparison of direct images. The second uses the comparison of pullbacks and the counit for $f$. The special case $pf'=fq$ has the identity transformation on this composite.

## Statements left without proof

| ID and scan | Grothendieck’s words | Scope on these sheets |
|---|---|---|
| A18 · 18 | “se prolonge en un morphisme de dérivateurs” | The extension of classical abélianisation is asserted. Its compatibility with direct image is raised separately. |
| C19 · 19 | “on trouve en tous cas des morphismes canoniques” | Both arrows are displayed. Their construction is referred to the base-change analogy. |
| L21 · 21 | “en pratique, tjrs déterminé canoniquement, à iso. canonique près” | This is a qualified observation about lifts. |
| I22 · 22 | “ils existent pour $\mathbb D_I$”, “est stable par passage de $\mathbb D$ à $\mathbb D_I$. De même pour $\mathrm{Der}_3$.” | The product-index formula is given. The individual ingredients of the axiom and the multiadjoint variant are not worked through. |
| F23 · 24 | “alors on trouve … un morphisme de dérivateurs” | The statement for $f^!$ assumes existence for closed immersions. |
| X25 · 25 | “Cette commutativité sera assurée par des axiomes ultérieurs” | The dashed comparison marked “iso?” depends on further axioms. |
| C26 · 27 | “On voit en tous cas que si pour tout $f$ … alors pour tout $g$ …” | The implication exchanges universal right exactness of the lower-star operations for left exactness of the lower-shriek operations. |
| H29 · 29 | “est 2-fidèle”, “est une équivalence de catégories”, “on vérifie tout de suite que” | The sheet states the Hom equivalence and the test of exactness for $u$ and $\mathbb D_u$. |
| B33 · 33 | “de deux façons, qui donnent le $=$ résultat”, “à expliciter une bonne fois” | Both routes are sketched. The general verification of their equality is left implicit. |

## Questions and conjectures

| Scan | Words on the sheet | Question |
|---|---|---|
| 18–19 | “ne semble pas tautologique”, “C’est faux déjà si … $Y$ est l’espace ponctuel”, “la question est de savoir si c’est des iso.” | Does abélianisation commute with the operations in question? The marginal objection concerns the proposed cartesian consequence. The two comparison arrows on 19 are available more generally. |
| 19 | “Questions analogues pour les $f^!$”, “Non ! Le cas des cat. triangulées est ‘misleading’”, “ou les deux !” | Which exceptional operations should commute, and which exactness conditions should be required of a morphism? |
| 21–22 | “il se pose la question d’interpréter $u_0$”, “je doute pourtant que … soit pleinement fidèle”, “il faudra vérifier la stabilité” | Can a functor be lifted? How much of a morphism can restriction detect? Which later axioms survive a shift? |
| 23–25 | “Peut on les interpréter en termes de morphismes de dérivateurs”, “Il s’impose de regarder si … sont exacts”, “iso?” | Do the lifted operations commute with both direct images in the other variable? |
| 26–27 | “Mais est-ce que … est aussi exact à droite ?”, “Mais ce morphisme est-il un isomorphisme ?”, “Je pense que dans le cas additif ça peut être raisonnable” | The mixed comparison exists. Its invertibility is tentative even in the additive case. Scans 30–31 give the qualification that leads to “Perplexité”. |
| 27 | “sauf erreur. (Cf plus bas)” | The proposed consequence of right exactness is preservation of an initial object. |
| 31 | “On devrait pouvoir définir une notion de dérivateur (additif) ‘triangulé’” | Could stronger axioms make left and right exactness equivalent for morphisms between such derivators? |
| 31–33 | “on se propose de ‘calculer’ le foncteur”, “Et on peut au lieu de ceci chercher” | The component calculation leads to the base-change map. The question marks in the two routes on 33 mark the arrows being sought. |

## Slips

| ID and scan | Frozen wording | Suggested correction and reason | Confidence |
|---|---|---|---|
| S23 · 23 | $f\times\mathrm{id}_J:I\times J\to I\times J'$ | The corrected target (S23-c) is $I'\times J$. The source and target of $f$ are given on the same sheet, and the vertical edge on 25 changes the first coordinate. | High |
| S25 · 25 | “Alors” or “Ainsi”, followed by “est exact à droite” | If this clause names the consequence of commutation with $g_*$ in the square immediately above, the terminology on 26–27 gives “à gauche”. The clause could instead resume an earlier inference in a different order. | Low |
| S28a · 28 | “admet un adjoint à gauche”, then “l’adj. à gauche $f_*$ de $f^*$” | For products the corrected statement (S28a-c) uses “à droite” in both places. Its universal property identifies maps from a test object into the product with maps from a diagonal family into the given family. | High |
| S28b · 28 | “pour les sommes finies, et les dérivateurs gauches” | “droits” would give the dual clause of the proposition on 27. The short connective introducing the clause is uncertain. | Low |
| S32 · 32 | “un foncteur canonique” immediately before $fq\to pf'$ | “une transformation naturelle” gives the intended type. The text names both endpoint functors and specifies the arrow at each pair. | High |
| S33 · 33 | “les foncteurs adj. à g. $f'_*,f_*$ des deux foncteurs verticaux” | “à dr.” agrees with the lower-star adjunctions used here. In particular, the last arrow on the sheet is $f^*f_*\to\mathrm{id}$. | High |

## Pointers

| Scan | His words | Referent |
|---|---|---|
| 19 | “comme pour les morphismes de chgt de base pour les $Rf_*$” | The ordinary base-change construction supplies the analogy. |
| 19 | “devrais demander à Thomason s’il a regardé” | A question for Thomason about functors between model categories, equivalences, fibrations and possibly cofibrations. No work of his is identified. |
| 22 | “cf … marginales p. 7” | Earlier marginal annotations concerning the ingredients of the axiom. Page 7 is outside this packet. |
| 25 | “Cf plus bas”, with “page” and a numeral inserted | The future reference could be 59, 39 or 29 in the handwriting. Its destination is unresolved. |
| 26–28 | “on l’a vu”, “Cf plus bas”, “L’exemple précédent” | Respectively the earlier base-change isomorphism, the forward reference concerning initial objects, and the preceding example with a non-pointed derivator. |

## Remarks of the model

**R27 · Model remark, high confidence, scan 27.** At an object of the nonempty complement, the terminal presheaf has one element and the initial presheaf has none. Evaluation there suffices to distinguish the two objects used in the example.

**R30 · Model remark, high confidence, scans 30–31.** Take $F_a=F_b=F_0=\mathbb F_2$ with $\alpha=\beta=\mathrm{id}$. Enumeration gives just $(0,0)$ and $(1,1)$ at the added vertex. After $F_0$ is replaced by zero, that vertex contains all four pairs. The original component maps are surjective. At the added vertex their image misses $(0,1)$ and $(1,0)$.

**R31 · Model remark, high confidence, scan 31.** In the abelian setting of the example, the inclusion at the fourth vertex can be epic only if $\alpha\mathrm{pr}_1-\beta\mathrm{pr}_2$ vanishes. Its restrictions to the two summands give $\alpha$ and $-\beta$. This checks the condition “que si $\alpha=\beta=0$”.

**R32 · Model remark, high confidence, scan 32.** A morphism of pairs $h:(i,\varphi)\to(i′,\varphi′)$ satisfies $\varphi′ f(h)=\varphi$. This is exactly the naturality condition for the components written on this sheet.

**R33 · Model remark, high confidence, scans 31–33.** The route through $\mathrm{id}\to q_*q^*$ uses direct images also for the horizontal maps $q,p$. They are available in the left derivator introduced on 31. The bottom route singles out the counit for the vertical map $f$, which makes the handedness in S33 visible.
