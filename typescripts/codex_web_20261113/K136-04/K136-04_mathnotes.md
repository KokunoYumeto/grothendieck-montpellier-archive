# Mathematical notes · cote 136, scans 002–016

## What the pages do

**003–004 · From differential forms to rational homotopy.** The historical outline starts with Stokes’ formula and the comparison from de Rham to singular cohomology. Grothendieck passes through harmonic forms, Stein varieties and algebraic and crystalline cohomology to Sullivan’s singular differential forms. The next sheet moves from computing rational cohomology to recovering rational homotopy by a minimal model. It ends that discussion with “Mais à nouveau, on perd la torsion !”

**004–005 · The rational simplex model.** To a simplex $[n]$ Grothendieck attaches the rational algebraic de Rham complex of its affine span. The resulting family represents cochains by taking maps out of the singular semisimplicial set. He gives two ingredients for the comparison theorem. They are a resolution of the constant coefficients simplex by simplex, and acyclicity of each semisimplicial object of forms of fixed degree.

**005–006 · The obstruction over the integers.** Integrating $x^n\,dx$ requires a denominator. Divided powers suggest a substitute, but eliminating the last affine coordinate would require taking divided powers of $1-\sum_{i=0}^{n-1} X_i$. The preceding divided-power ideal does not contain this element. This is where the constant 1 in the simplex relation becomes an obstacle.

**006–007 · A divided-power parameter.** Grothendieck chooses a ring $S$, a divided-power ideal $J$ and an element $t\in J$. The new relations are $\sum X_i=t$ and $\sum dX_i=0$. He describes the quotient, its augmentation to $S/J$, and compatibility of the divided powers with the differential. Varying $[n]$ and applying $\mathrm{Hom}$ from a semisimplicial object gives a contravariant complex. For a topological space he first takes its singular complex. The general comparison with ordinary cohomology is qualified.

**008 · The universal coefficient example.** He takes $S=k\{T\}$, its positive-degree ideal $J$ and $t=T$. The module $\Phi$ is given simplexwise by $k^{[n]}$, and $\Psi$ is its quotient by the diagonal copy of $k$. The boxed formula combines divided powers on $\Phi$ and exterior powers on $\Psi$. Its two degrees keep track of the differential of bidegree $(-1,+1)$.

**009–010 · Truncation and reindexing.** In a fixed total degree $n$ the diagram has terms from $(n,0)$ through $(0,n)$. Grothendieck treats it as a truncated resolution. Its sections give the indicated ordinary cohomology groups in the permitted range. He then fixes $q$, uses $(n,q)=(p+q,q)$, and describes a truncated graded $k\{T\}$-module. The upper and lower occurrences of ordinary cohomology on 010 have different superscripts, recorded under Slips.

**011–012 · Shadows.** Grothendieck calls a truncation of $M\otimes_k S$ a $q$th shadow. He proposes to recover a module and its pairings from such truncations. Assuming this reconstruction, he describes what the bigraded algebra remembers about the ordinary cohomology algebra, derived sections, and cup product. The cup-product display on 012 completes the sentence begun on 011.

**012 a · Specialization.** He recovers the rational Sullivan complex by quotienting by $T-1$. The next formula allows arbitrary $k$ and writes the Sullivan coefficients as $k\otimes_{\mathbb Z}\mathbb Q$. The further formula for $(S,J,t)$ uses $t-1$. Its right-hand coefficient is overwritten and its margin carries a question mark.

**012 b–013 · Virtual complexes.** He asks how much homotopy information the augmentation ideal and its divided powers preserve. A virtual divided-power de Rham complex carries the indicated bigrading, multiplication, augmentation, differential and compatible divided powers. Its shifted groups in each exterior degree must be shadows. Inverting a class of arrows leads to the diagram from homotopy types to a derived category of these complexes, and then to an integral equivalence question.

**014 c–d · Operations, minimal models and products.** Grothendieck reports a limited negative result on reconstructing cohomology operations. He proposes minimal models as a route to homotopy groups. The product question leads to the missing Künneth formula and a possible failure of flatness over $k\{T\}$.

**015 e · A chain object.** The familiar passage from chains to cochains motivates a differential, coaugmented object with divided copowers. Grothendieck writes a Hom formula for the cochains and a tensor-product formula for changing coefficients. He singles out the integral chain object when finiteness hypotheses are to be dropped. The final comparison concerns the directions of limits on chains and cochains.

**016 g · Sheafification.** Grothendieck puts the coefficient ring in a topos and asks how to define a derived direct image for the resulting complexes. He asks specifically for a quasi-isomorphic replacement with flasque components. He relates this problem to one posed by Deligne for rational Sullivan complexes and closes with a qualified recollection about paracompact spaces.

## Statements left without proof

The identifiers also locate entries in <code>CHECK_EVENTS.tsv</code>. Reporting an attribution or an open problem does not constitute checking it.

| ID and scan | Words on the page | What is left to the reader |
|---|---|---|
| B1 · 003–004 | “Sullivan montre mieux” · “le $\mathbb Q$-type d'homotopie de $X$ est récupéré” · “On renvoie au papier de Sullivan” | The categorical form, minimal models and the extraction of the rational homotopy groups are referred elsewhere. The precise equivalence has the insertion “sauf erreur”. |
| B2 · 004–005 | “lemme de Poincaré algébrique” · “ce qui se vérifie facilement” · “Cela serait itou” | He outlines the cohomology comparison but does not supply the calculation of the $\pi_j$ of the fixed-degree forms or the proposed variants for smooth and analytic forms. |
| B3 · 007 | “est une résolution de $S$” · “Elle dépend fonctoriellement de $(S,J,t)$” | He gives the free-coordinate description and the differential identity. A contracting calculation and the verification of functoriality are implicit. |
| B4 · 009–010 | “homotope à 0” · “acycliques sauf le dernier” · “Ces isom. sont compatibles avec les structures multiplicatives” | The homotopy of $\Phi$, the passage to the factors of the resolution, and multiplicative compatibility are used without an explicit homotopy or a calculation of the products. |
| B5 · 011–012 | “on récupère $M$ à isom canonique près” · “Cette […] théorie des ombres […] étant supposée acquise” | The recovery from any one truncation and of a pairing for sufficiently large $q$ underlies the passage to cohomology and derived cup product. No inverse construction is supplied here. |
| B6 · 012 a | “on le reconstruit […] par la formule” · “quel que soit $k$, on a” | The two $T-1$ comparisons are displayed without derivation. The more general $t-1$ formula has its own doubt in the margin. |
| B7 · 015 | “Il est possible de […] de définir une cobigèbre” · “On aura d'ailleurs” · “commute aux […] quelconques (pas néc. filtrantes)” | He specifies the wanted Hom, base-change and colimit properties. The construction of the object and the verifications are not given on this sheet. |

## Questions and conjectures

| Scan | Grothendieck’s wording | Scope |
|---|---|---|
| 003–005 | “Poincaré ?”, “Conjecturé par É. Cartan”, “(sauf erreur)”, “On aimerait avoir une $\mathbb Z$-algèbre diff. […] alternée”, “il paraît qu'il y a des ths contre !” | Historical attribution, the precise rational equivalence, then the possibility of an integral model. |
| 006–007 | “on ne voit pas comment envoyer” · “Mais on ne peut dire en général […] quelle est sa cohomologie” | Elimination of a generator in a divided-power algebra and the cohomology for a general triple. |
| 010–011 | “Mais quelle est (pour $q$ fixé) la structure” · “Ce qui donne un espoir” | The graded-module question motivates the calculation. The hope concerns the additional homotopy information the result might carry. |
| 012–013 | “Je suis convaincu que la structure à p.d. […] est importante” · “avec ttes ces structures” · “on peut se demander si sa restriction […] induit une équivalence” | Does the integral complex recover the homotopy type? For the proposed equivalence he asks for connected and simply connected spaces of finite type and specifies degree-zero, degree-one and finiteness conditions on the complexes. The general specialization in 012 a is separately questioned. |
| 014 c–d | “si on peut réconstruire les op. coh.” · “n'ai que des résultats partiels négatifs” · “Il faudrait sans doute chercher des modèles minimaux à la Sullivan” · “Je n'ai rien fait dans cette direction” | Operations of Steenrod or Whitney, homotopy groups, and a Künneth formula are three distinct issues. The negative observation concerns the multiplicative operations tried. |
| 015 e | “si on veut aborder b) c) d) sans conditions de finitude” | He suggests studying the integral chain object to revisit those questions. |
| 016 g | “mais y en a-t-il tjrs ?” · “le Pb est ouvert -- et posé par Deligne” · “Mais sauf erreur (si souvenirs sont exacts)” | Existence of flasque replacements and direct images. The recollection about paracompact spaces is qualified twice. |

## Slips

| ID and place | Preserved reading | Suggested correction and reason | Confidence |
|---|---|---|---|
| S1 · 005, between the rules | “la coh. entière de $\mathbb Z$” | Possibly “de $X$”. The subject is a cochain construction on the space $X$. The written letter has the double stroke of $\mathbb Z$. | Medium for the intended referent |
| S2 · 006, line beginning “donc on ne voit pas comment envoyer” | Both the source and the target lists end at $X_{n-1}$. | Possibly end the source list at $X_n$. The preceding substitution is for $X_n$ and takes values in the algebra on the first $n$ generators. | Medium |
| S3 · 008, first formula after “On a alors” | Last argument $k$ in $(k\{T\},k\{T\}^{+},k)$ | Read $T$ for the intended parameter. Above it stands $t=T$, and the defining display on 009 has $T$ at the same place. | High |
| S4 · 009, line before the diagram | “si $p=0$” | The preceding sentence gives $p\ne0$ for homotopy to zero. The last term of the displayed resolution is the exception. Intended here, $p\ne0$. | High |
| S5 · 010, two upper occurrences | $H^0$ in the prose and inside the first truncation | For variable $q$ the suggested group is $H^q$, as in the lower display and the conclusion of 009. The two upper zeros and the lower descending $q$ are distinct in the ink. | High |

## Pointers

| Scan | Names or words as they occur | Reference on the sheet |
|---|---|---|
| 003 a–d | “Poincaré ?”, “Stokes”, “De Rham”, “É. Cartan”, “Hodge”, “H. Cartan-Serre”, “variétés de Stein” | The historical survey of forms, comparison theorems and harmonic integrals. |
| 003 e–f | “Dwork”, “Washnitzer-Monsky”, “Berthelot”, “Illusie”, “Messing”, “Mazur” · “cf aussi Hartshorne Herrera Ogus, Bloch (?)” · “Du pt de vue Weil” | The algebraic and crystalline branches of the survey, including the marginal additions. The next item names “Grothendieck”, “Deligne”, and “Hartshorne” for the comparison over $\mathbb C$. |
| 003–004, 014 | “Sullivan” · “On renvoie au papier de Sullivan” · “modèles minimaux à la Sullivan” | The explicit paper reference is on 004. Neither a title nor a publication date is given. The minimal-model question returns on 014. |
| 003, 005 | “Plan conf. IHES en 1976” · “lemme de Poincaré algébrique” | The marginal conference reference and the named lemma used in the simplex resolution. |
| 014–015 | “type Steenrod ou Whitney” · “une formule de Künneth” · “aborder b) c) d)” | Named operations and product formula, followed by a cross-reference to the preceding problems. |
| 016 | “après f) ci-dessous” · “le Pb est ouvert -- et posé par Deligne” | A marginal ordering direction and a reference to Deligne’s problem. The concluding series of problems has no separate f) in the supplied sheets. The notes give no reference to another archive cote. |

## Remarks of the model

- **R1 · Model, high confidence, scan 005.** The single case $x\,dx$ already exhibits the integral denominator. The coefficient of $x$ in the derivative of an integral polynomial is twice its quadratic coefficient, so it cannot be 1. This checks the example of the obstruction. It does not establish the unspecified theorems mentioned between the rules.
- **R2 · Model, high confidence, scans 008 and 010.** The change $(p,q)\mapsto(p+q,q)$ sends the increment $(-1,1)$ to $(0,1)$. Its inverse gives $p=n-q$. This accounts for both the bidegree and the range $n\ge q\ge0$ written on 010, independently of the upper $H^0$ readings.
- **R3 · Model, high confidence, scans 007, 008 and 012.** Two operations on $T$ occur here. In the augmentation to $S/J$ its image is zero, since $T\in J$. In the comparison with Sullivan forms the quotient imposes $T=1$. Keeping both operations visible helps distinguish the augmentation ideal in problem b) from the specialization in problem a).
- **R4 · Model, low confidence, scans 012–013.** The slanted finiteness condition on 012 names $H_i$ of the space. The question on 013 uses a live upper $i$ on $H^i(X,\mathbb Z)$ and has a cancelled lower mark. The two sheets formulate their hypotheses differently. Whether the change was deliberate is a reading question of low confidence.
- **R5 · Model, low confidence, scan 006, differential relation and kernel sentence.** The frozen lower-limit readings are <code>\unsure{1|0}</code> at both places. Starting at zero would agree with the coordinate list and the adjacent sum. The small low ink could also be a single upright. This is a reading question.
- **R6 · Model, low confidence, scan 015, first Hom formula.** The frozen source reads <code>C_\bullet(\mathscr X_\ast,\deleted{\unsure{\mathbb Z}}k)</code> there. A live integral coefficient in place of $k$ would fit the subscript on Hom and the following parenthesis. The overlapping letters prevent a reliable decision about their order. The status of the coefficient limits any mathematical inference from this line.
