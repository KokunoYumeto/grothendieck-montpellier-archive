# Mathematical notes on scans 353–367

## What the pages do

**353–354, the remaining cases.** For source type $\Delta_\varepsilon^2$, the two choices of target give categories of maps identified with the one-step and two-step ordinals. The diagrams track the image of the middle vertex. In either case, Grothendieck says that any two maps are joined by a simple homotopy. In case B the source has a retrograde middle interval $I_2$. The maps are trivial there, so contraction takes the calculation back to case A. He closes with “On a gagné !”

**355–357, pullback of paths.** Section 9 fixes a category $X$ and an admissible set $\Sigma$ of its arrows. Paths of variable type form a category fibred over $\mathrm{Ty}$, as do paths with fixed source $a$ and target $b$. A map of types $\varphi:\tau\to\tau'$ gives inverse-image functors in both cases. To explain their dependence on $\varphi$, Grothendieck describes paths as functors out of $I_\tau$ taking its invertible or retrograde arrows into $\Sigma$. Composition then gives the functor drawn as $\gamma=\gamma_0\circ\mathrm{can}$ on 357.

**357–359, the homotopy theorem.** Homotopic maps of types give homotopic inverse-image functors. The homotopy lemma thus gives independence of $\varphi$ up to homotopy whenever $\mathrm{Hom}(\tau,\tau')$ is nonempty. The refinement remembers both endpoints. The functors commute with projection to $X\times X$, and the arrows between them lie over identities there. This yields the assertion for fixed endpoints.

**360–361, passage to an ind-object.** Section 10 starts with $C\to T$ and assumes that any two parallel arrows of $T$ induce homotopic inverse-image functors. It puts $t\leq t'$ when $\mathrm{Hom}_T(t,t')$ is nonempty and denotes the resulting ordered category by $T_0$. The diagram of fibres gives $H_C:T_0^\circ\to\mathrm{Cat\,hot}$. Under the left filtration hypothesis this defines an ind-object. For types, the concatenation $\tau\tau'$ maps to both $\tau$ and $\tau'$. Countable left cofinality is a further hypothesis.

**361–363, a sequential realization.** A left-cofinal chain $t_0\leftarrow t_1\leftarrow\cdots$ gives a direct system of categories $C_n=C_{t_n}$. Its colimit is $C_\infty$. Strict transitivity allows the use of inverse image by a composite. Without strict transitivity the author uses the composite of the successive functors and records the canonical isomorphism. The opposite directions of the two systems are checked in event E1.

**363–366, the comparison problem.** Grothendieck distinguishes (a) the total category $C$ regarded as an object of $\mathrm{Cat}$, (b) the chosen colimit $C_\infty$, and (c) the ind-object $H_C$. He asks about their images in $\mathrm{Cat\,hot}$ and $\mathrm{Hot}$. He considers left-cofinal base changes, the slice $T_{/t_0}$, and replacement of the base by $\mathbb N^\circ$ along a chosen chain. The question about the canonical map is continued from the bottom of 365 onto 366.

**366–367, testing with a category $S$.** The categories $\underline{\mathrm{Hom}}_{\mathrm{Cat}}(S,C_t)$ form a fibred category denoted by a relative Hom over $T$, with $S_T=S\times T$. Its $\pi_0$ defines a contravariant set-valued functor $H$ of $S$. Grothendieck proposes $H(S)\simeq\mathrm{Hom}_{\mathrm{Ind}(\mathrm{Cat\,hot})}(\gamma(S),H_C)$. He then returns to the path example, where he also writes a comparison with $\mathrm{Hom}_{\mathrm{Cat\,hot}}(S,C_\infty)$ for finite $S$. The last sentence stops at “les objets”.

## Statements left without proof

| Scan | His words | Scope |
|---|---|---|
| 356 | “Cet ens. de flèches est admissible, car stable par composition.” | Closure under composition is the reason given for admissibility of $\Sigma_\tau$. |
| 358 | “le lemme d'homotopie nous assure que l'hyp. … est toujours satisfaite” | The theorem invokes the lemma for pairs of type maps. The last cases of its argument appear on 353–354. |
| 360–361 | “se factorise (évidemment de façon unique)” | Uniqueness of the factorization through $T_0^\circ$ is asserted. |
| 361 | “tjrs satisfaite si $\mathrm{card}\,T_0\leq\aleph_0$” | The margin gives this sufficient condition for the countability hypothesis. |
| 362 | “cas auquel on peut tjrs se ramener d'ailleurs par l'astuce de Giraud” and “Cette hypothèse est d'ailleurs vérifiée dans le cas” | The sheet cites strictification and asserts strict transitivity for the fibred category of paths with fixed endpoints. |
| 364 | “ne changent pas quand on remplace $T$ par une sous-catégorie … cofinale à gauche” | The observation concerns $H_C$ and the $C_\infty$ constructed above. The same paragraph mentions the slice. |
| 366 | “Il est immédiat que … la propriété d'homotopie (p. 99) est stable” | Stability is asserted for the passage to the relative Hom with $S_T$. |
| 367 | “Les trois types d'objets a) b) c) ont le … $\pi_0$” and “isomorphe aussi, … à” | In the path example he affirms agreement on $\pi_0$ and writes a further comparison for finite parameters. The sign before $\pi_0$ and the overwritten parameter in the finite condition are marked in the transcription. |

## Questions and conjectures

- **363.** “Elle sera surtout sympa si on a pu choisir le système … de telle façon que les foncteurs de transition … soient pleinement fidèles, et peut-être même …”. The stronger word looks like “mono” or “monos”. The hope is to identify each $C_n$ with a full subcategory of its colimit.
- **363–364.** “Je voudrais comprendre les relations précises”, “Dans quelle mesure ces derniers sont ils indépendants du choix”, “Quel est le rôle de $C_\infty$ ?” and “Est-elle canoniquement isomorphe à $C$ dans $\mathrm{Cat\,hot}$, ou dans $\mathrm{Hot}$ ?” These concern the effect of choosing the chain and the meaning of the resulting colimit.
- **364–366.** “Si la relation … est très étroite, on en conclurait” and “Bien mieux, elle ne changerait pas”. The possible consequence is invariance of the type of the total category after changing the base. He asks specifically whether the canonical $C'\to C$ is “également tjrs un iso.” in $\mathrm{Cat\,hot}$, or at least in $\mathrm{Hot}$.
- **366.** “Sauf erreur, elle s'interprète comme la catégorie fibrée sur $T$ correspondant au champ”. He qualifies the stack interpretation of the relative Hom.
- **367.** “formule hypothétique” and “Si on avait un tel isomorphisme” introduce the proposed description of $H$. A canonical isomorphism functorial in $S$ would, he says, describe $H_C$ up to unique isomorphism. “Il me vient un doute ici” introduces the return to the path example.

## Slips

| Event | Scan and confidence | Frozen wording and possible correction |
|---|---|---|
| E2 | 354, medium | The displayed target has $(\tau'{}^\circ,\tau^\circ)$. The following connectedness assertion has $(\tau^\circ,\tau'{}^\circ)$. Interchanging the arguments in the latter would make it repeat the display. The page supplies no decision about which occurrence the author intended to change. |
| E3 | 356, high | The last product has $\underline{\mathrm{Hom}}_{\Sigma_I,\Sigma}(I',X)$. The preceding display explicitly designates $\Sigma_{I'}$ for a functor with source $I'$. Supplying the prime in the subscript gives $\underline{\mathrm{Hom}}_{\Sigma_{I'},\Sigma}(I',X)$. |
| E4 | 358–359, medium | The prose reads “au dessus de $X$”. For the joint endpoint functor, “au dessus de $X\times X$” agrees with the target drawn immediately below and with the relative Hom on 359. |

The first middle-vertex digit on 353, the two short index signs on 363 and the set-builder formula on 364 are low-confidence reading questions. None supplies a secure correction.

## Pointers

- **354.** “et pareil dans A !” and “Or dans A on a vu” refer to the immediately preceding calculation on 353.
- **357 and 359 (E5).** On 357 the two references to “$(*)$ … p. 94” identify the two branches of the diagram on scan 355. Scan 359 again gives “(p. 94)”. The preceding sign there could be alpha or a star.
- **358.** “le lemme d'homotopie” refers back to the result about maps of types that the author applies in the theorem.
- **362.** “l'astuce de Giraud” is the reference for the reduction to a strict fibration. The page gives no title or bibliographic detail.
- **366 (E5).** “la propriété d'homotopie (p. 99)” points to scan 360, where the hypothesis appears in the margin beside its statement.

## Remarks of the model

- **My reading, high confidence (E6, 358–359).** Verticality explains the fixed-endpoint conclusion. A component above the identity of $(a,b)$ stays in the fibre at $(a,b)$, so the successive transformations restrict there. The definition of “verticales” on 359 specifies exactly which identity is involved.
- **My reading, medium confidence (E7, 364–365).** The assertion of cofinal invariance on 364 can be read as concerning the family of possible colimits. This leaves a question about a particular choice of $C_\infty$. On 365 the author says that the colimits constructed after base change “font partie” of those for the original base. The number of the verb is doubtful, but the membership phrase is clear.
- **My reading, high confidence about scope (E8, 367).** Finiteness qualifies the comparison with $\mathrm{Hom}_{\mathrm{Cat\,hot}}(S,C_\infty)$. The final line explicitly says “pour des arguments $S$ … qui sont des cat. finies”, which fixes the scope even with the overwritten parameter a few lines earlier. The consequence he draws from it continues beyond these scans.
