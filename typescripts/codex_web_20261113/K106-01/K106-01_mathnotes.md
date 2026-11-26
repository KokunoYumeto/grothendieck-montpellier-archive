# Mathematical notes on cote 106, scans 2–17

## What the pages do

**Scans 2–4, localization and cofibrant replacements.** The question is whether passing to cofibrant objects before inverting weak equivalences gives the same category. On scan 2 an initial object and axiom C3 give a replacement \(\widetilde x\to x\). For an arrow \(f\) the weak lifting lemma gives a lift into a further replacement of its target. The proposed arrow in the localized category is obtained by inverting \(i\). The small diagrams on scan 3 try different arrangements of replacements, parallel arrows and sums. Scan 4 calculates with the two comparison functors and the maps \(\alpha_x\).

**Scan 6, the criterion.** The proposition isolates the equality that the preceding argument needs. For parallel maps \(\varphi,\psi\) of cofibrant objects with \(f\varphi=f\psi\) and \(f\in W\), their classes must already agree in the localization of the cofibrant objects. The author then works in a category in which every object is cofibrant.

**Scans 6–8, a category built from diagrams.** An object of \(\underline{\mathrm{Ch}}_0(x,y)\) is drawn as \(x\to\bar y\leftarrow y\), with a condition on the leg out of \(y\). Composition uses an amalgamated sum. Connected components provide the morphisms of a new category, written \(\widetilde C\). The diagram of three copies of \(x\) represents the identity. The manuscript also writes down the assignment on the ordinary arrows of \(C\).

**Scans 8–10, an attempted inverse and a comparison that works in one direction.** The author tries to show directly that a weak equivalence becomes invertible in \(\widetilde C\). The attempted comparison requires a cofibration that the weak lifting lemma does not supply. He then sends a pair \((f,i)\) to \([i]^{-1}[f]\) in \(W^{-1}C\). The functor is the identity on objects. The calculation with a section \(g\) places the inverse of an arrow of \(W\) in its image, as needed for surjectivity on arrows.

**Scans 12–15, a revision of the diagrams.** Scan 12 singles out faithfulness as the remaining problem. The first construction visibly factors through localization at \(W_0=W\cap\mathrm{cof}\). The author questions whether that localization suffices. He keeps the name \(\widetilde C\) but changes the leg conditions to \(f\in\mathrm{cof}\) and \(i\in W\). Scan 13 has independent trial diagrams. Scan 14 proposes a factorization and a choice of section to construct an arrow in the revised category. The crossed calculation and slanted note are separate attempts. The coproduct squares on scan 15 provide comparisons for two choices.

**Scan 16, comparing choices.** The first diagram builds a third factorization over the common target. The prose first compares factorizations with compatible choices of section, then fixes one factorization and isolates independence of the section. The final condition concerns a weak equivalence with section \(i\) and the class represented by \((1_x,i)\). The page ends by referring back to the construction of \(C\to\widetilde C\).

The machine forms on scans 5, 7, 9 and 11, and the program listing on scan 17, are separate from these mathematical units.

## Statements left without proof

| ID | Scan | Passage and scope |
|---|---|---|
| C1 | 2, 4, 6 | « Alors il est connu que […] est une équivalence de catégories. » The proposed functor requires the choice-independence lemma. Scan 2 still says « Si ce lemme est valable ». Scan 6 states « il f. et s. que la condition suivante soit vérifiée » and relates it to faithfulness. The pages contain the comparison calculation on scan 4, but no general verification of that condition from the initial axioms. |
| C2 | 8 | « Cette composition est associative à iso can. près » and « compatibles aux compositions ». The pushout diagram is supplied; an explicit comparison of three composable diagrams is absent here. |
| C3 | 10 | « il est immédiat que c'est compatible avec les identités et la composition ». This concerns the comparison \((f,i)\mapsto[i]^{-1}[f]\). The following argument addresses surjectivity instead. |
| C4 | 12, 14 | « qui se composent encore comme précédemment » and « il faut montrer que ça ne dépend pas des choix faits ». The comparison with a third factorization is begun on scans 14–16. |
| C5 | 16 | « Donc il reste à prouver que […] [\(f_0,i\)] ne dépend pas du choix de la section \(i\) ». The last paragraph calls the condition « (néc. et) » sufficient for faithfulness, « comme on doit pouvoir vérifier aisément, en construisant bel et bien le foncteur cherché ». That construction is still prospective at the end of the supplied sequence. |

## Questions and conjectures

| Scan | Author’s words and the question they concern |
|---|---|
| 2 | « prouver que si […] alors \([\varphi]=[\psi]\) ». This is equality in the localization of the cofibrant objects after a weak equivalence equalizes the two arrows. |
| 8 | « on cherche \(g,i\) tels que » the two composites belong to the identity components. Both proposed arrow labels carry a question mark. |
| 10 | « Ça marcherait si on pouvait trouver » a \(\beta\) for which \(\beta f\) is also a cofibration. « Ça se présente mal ! » follows the example using monomorphisms. |
| 12 | « La difficulté, c'est qu'il n'est pas clair que le foncteur […] précédent soit aussi fidèle ». Of the consequence for \(W_0\) he writes « semble-t-il », then « Mais je doute qu'il suffise d'inverser les équiv. faibles cofibrantes, pour que ttes les équiv. faibles deviennent inversibles ! » |
| 14, 16 | « il faut voir qu'ils sont dans une = composante connexe ». The comparison ultimately leaves open whether the class « ne dépend pas du choix de la section \(i\) ». |

## Slips

| ID | Scan | Written and proposed reading | Reason and confidence |
|---|---|---|---|
| S1 | 6, foot | The written first component of the product is \(g'g\). The displayed arrows would give \(g'f\). | The incoming arrow is labelled \(f\), and the outgoing diagonal from its target is \(g'\). High confidence in this type comparison. Both live g’s were checked separately from the adjacent crossing-out. The unusual closing parenthesis and dot are retained. |
| S2 | 8, arrow from the discrete Hom | \(f\mapsto(f,\mathrm{id}_x)\); apparently \((f,\mathrm{id}_y)\). | For \(f:x\to y\), the identity is the second leg of a diagram whose second leg starts at \(y\). The subscript in the assignment is visibly x. High confidence. |
| S3 | 10, last paragraph | \([f][i]^{-1}[g)\); apparently \([f][i]^{-1}[g]\). | In the same calculation the class of \(g\) recurs with square brackets. The first closing stroke is curved. High confidence about the mismatch. |
| S4 | 16, line beginning « Comme » | \((f,\mathrm{id}_{\bar y}]\); matching delimiters appear intended. | The left delimiter is curved and the right one has corners. The same formula has square brackets around the preceding pair. Medium confidence about the intended delimiters. The facsimile does not establish whether a change to the first \(f\) was intended. |

## Pointers

| Scan | Words on the sheet | Reference |
|---|---|---|
| 2 | « C1 à C3 de Baues, (pas néc. C4) » | Baues is named for his axioms. The sheet supplies no title or publication details. |
| 2, 10, 14 | « weak lifting lemma » | Used to produce a lift or a factorization with a section. No numbered external reference is given. |
| 4, 12, 14 | « les deux composés », « précédent », « comme précédemment » | Internal references to the comparison functors and to the earlier rule for composing the diagrams. |

## Remarks of the model

- **R1 · Model remark, high confidence, scans 8–10.** When cofibrations are monomorphisms and \(f\) is not monic, no choice of \(\beta\) can make \(\beta f\) monic. A pair of distinct arrows equalized by \(f\) remains equalized after postcomposition. This explains the particular obstruction the author points out.
- **R2 · Model remark, high confidence, scan 10.** The author’s local calculation uses \(\alpha i=f\) and \(\alpha g=1_y\). In the localization they give \([f][i]^{-1}[g]=1_y\). Since \([f]\) is invertible there, this identifies its inverse. The calculation takes place in \(W^{-1}C\); the manuscript’s separate question about faithfulness of the comparison remains on scan 12.
- **R3 · Model remark, medium confidence, scans 12–16.** In the revised definition the first leg of a span must be a cofibration. Thus the subsequent choice of a factorization for an arbitrary arrow of \(C\) has a concrete job: to produce an allowed first leg. The discussion of sections is what remains after trying to compare two such choices.

**Reading questions from the final comparison.** These are observations on the images made after the witness hashes were recorded.

| Scan and line of the locked page | Recorded reading | Other reading or graphical detail | Evidence |
|---|---|---|---|
| 6, line 46, first downward diagonal in the composition diagram | One \(f\) above the arrow from \(a\) to \(\bar y\). | A second, heavily inked \(f\)- or \(\varphi\)-shaped label below the same shaft, possibly cancelled. | The separate mark has a loop, a thick descending stem and a short rightward cross-stroke. Its existence is clear, its letter and state are uncertain. It is absent from the page TeX. See **006-under-first-leg.jpg**. The plain upper \(f\) used in S1 is clear. |
| 14, line 50, left vertex of the retraction diagram | \(a\) | \(x\) | The dark point has a small rounded foot, as on the first diagram's \(a\), but the identifying strokes coalesce. The preceding \(f:x\to y\) favours \(x\). The independent slip also read \(x\). See **014-return-source.jpg**. |
| 15, line 39, last horizontal arrow in the first diagram | Single rightward arrow with a hooked tail from the black \(p/\rho/\bullet\) to \(y\). | The single shaft has an additional **right-pointing head about two-thirds of the way along**, as well as its final head. It may record a shorter arrow extended to \(y\). | The two separate tips and the uninterrupted shaft are clear. The pen sequence is uncertain. The intermediate head is absent from the page TeX. See **015-right-shaft.jpg**. |

The two additional details have the following local TikZ-CD readings. The alternatives in the first line concern the lower label, including its possible cancellation. In the second example the two coincident shafts draw the intermediate and final tips.

- **Scan 6, line 46.** For the first diagonal, the two positions can be set as `\arrow[dr,"f","{\unsure{f|\varphi}}"']`. A reading of the lower mark as cancelled would wrap its contents in `\deleted`.
- **Scan 15, line 39.** At the black object, the local arrow can be set as `\arrow[r,tail] \arrow[r,shorten >=1em]`. The shorter overlaid arrow places its tip on the same shaft as the arrow to \(y\).
