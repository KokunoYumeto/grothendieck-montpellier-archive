# Cote 76 · mathematical notes

The place references use the scan numbers and manuscript-line descriptions in the transcription. A quotation with an ellipsis is a short excerpt. Statements in the first three sections are reported as the manuscript presents them. The two finite checks in the final sections have identifiers in CHECK_EVENTS.tsv.

## What the pages do

**Faces, incidence and flags, scans 3–4.** Sets of faces of successive ranks are related by incidence. The notes order their disjoint union by chains of incident faces and recover the ranks by successively removing minimal elements. A drapeau is a nonempty totally ordered subset. The manuscript records its length and type and draws attention to the order of inclusion on flags.

**Changes of one face, scans 4–5.** For a maximal flag the notes introduce operators that replace one coordinate at a time. Local cardinality conditions provide the replacements. Under the named group action, the orbit maps are meant to recover faces and then flags of specified types. A proposition describes the resulting functor as fully faithful. The author immediately asks for its essential image.

**Realization, scans 5 and 7.** The last paragraph of 5 defines geometric realization using finite totally ordered parts. Scan 7 describes parts of that realization associated to individual faces, relates incidence to inclusion, and proposes a manifold criterion in terms of the spaces attached to lower faces. A qualification involving the Poincaré hypothesis changes the conditions to be tested.

**Boundary automorphisms, scan 6.** On a sheet crossed diagonally, the definition uses pairs of an automorphism of X and an automorphism of the covered boundary, related by the projection p. The two grids compare restriction to the boundary and variants with a tilde or a quotient. Copies of the group written as ℤ with exponent I recur. At the right the exponent is indexed by the components of the boundary.

**Filtered spaces and combinatorial varieties, scans 7–8.** A filtration of a topological space leads to flags and a group action. A second full-faithfulness proposition concerns filtered spaces and finite sets with operators. The next definition presents a finite combinatorial variety by fixed-point-free involutions, with commutation for nonconsecutive operators.

**Combinatorial complexes and their boundaries, scans 8–9.** The data are sets indexed from n down to zero with group actions and maps between ranks. Equivariance and invariance under specified generators constrain the composites. Four formulas on 9 describe successive boundary objects using quotients by generators. A following attempt to define categories and functors inductively is crossed out as a block.

**Conical maps, scan 10.** A compact filtered space has closed pieces. For a successive pair, its découpage has barred and dotted Z terms. The definition imposes finiteness of the components, a cone description, finiteness of a map back to the preceding piece, and a condition on the filtration. The two small-dimension cases, graphs and restriction diagrams accompany the definition.

**Flag types in low dimensions, scans 12–13.** Diagrams organize the objects attached to subsets of ranks. Some forgetful arrows are marked épi, with a final-segment condition stated beside them. Later diagrams emphasize arrows leading to the rank-three object. The first half of 13 starts again with cases numbered one through four and a cellular graph.

**Finite families of arrows, scan 13.** The lower half forms a category from finite families with a common target. A functor to topological spaces gives a construction involving cones, a coproduct and gluing along the common base. The author mentions finiteness, faithfulness and full faithfulness and writes down an iteration of the construction.

**Paracartes, scan 14.** Functors on finite subsets supply sets indexed by face types. The notes distinguish conditions on restriction to a final segment, conditions involving the largest vertex, and a special degree-two condition. The last lines ask when group actions on the sets indexed by initial intervals recover the full diagram.

**Flag geometries, scan 16.** The lower set of an element is required to have the form of a simplex ordered by inclusion of its nonempty parts. Its vertices are the minimal elements below it. Grouping flags according to these vertices gives a set-valued functor and a disjoint-union reconstruction. The strict case adds a least-upper-bound requirement and is related to the cardinality bound on each fibre.

**Dimension data and ordered flags, scans 17–18.** Starting with a functor whose singleton fibres can have several elements, the author forms the flag geometry and maps its minimal elements to a set I. The map must be injective on the vertices below each flag. The converse groups flags by their image types. The special case I = ℕ supplies dimension terminology. The final paragraph gives compatible total orders on simplices and groups the flags with n+1 minimal elements in D[n].

## Statements left without proof

| Scan | His words or notation | Scope on the page |
|---|---|---|
| 3 | “se réconstituent à partir de l’ens. ordonné” | The reconstruction is described by successive minima. The following characterization by chains has a marginal request to check it. |
| 4 | “les relations de commutation évidentes”; “Cette application est bijective.” | The commuting relation is stated for nonadjacent operators. The bijection to the faces is labelled Axiome 4. The parenthesis reduces the injectivity question to moving between flags with one coordinate fixed. |
| 5 | “Le foncteur … est pl. fidèle.” | Full faithfulness for the passage from the cellular data to the operator set. The axiom list is qualified by a question. |
| 7 | “Si … est une variété top. … alors … satisfait les conditions …”; “il f. et s.” | The manifold implication and the following criterion are stated without a proof on these sheets. |
| 8 | “le foncteur de la catégorie isotopique … est pl. fidèle.” | Full faithfulness for the filtered-space construction. |
| 9 | “est une … variété combinatoire qui est” | Four boundary formulas follow the assertion. Their derivation is not given. |
| 12 | “épi si … Sup I”; “épi si … est segment final” | The statements accompany restriction arrows. The page supplies examples. |
| 13 | “implique un foncteur”; “Si … fidèle (resp. pl. fidèle) … idem” | A formula specifies the object construction. There is no accompanying proof of its functoriality or faithfulness. |
| 16 | “dont la connaissance permet de reconstituer”; “il f. et s.” | Disjoint-union reconstruction and characterization of the strict case by subsets. |
| 17–18 | “se réconstitue à partir de”; the equivalence at the head of 18 | The two constructions are written down. The sheets give no separate verification of their mutual inverse property. |

## Questions and conjectures

- **3, margins.** “Axiome 1′ … surjectif” is introduced by an uncertain question. “vérifier” is written beside the chain characterization.
- **4, right column.** “est-ce une conséquence de l’axiome 4 et des précédents?” concerns the bijectivity of the orbit map for a general type.
- **5, proposition.** “(renforcé ?)” qualifies the last axiom. “Il faudrait déterminer l’image essentielle.”
- **7, realization and filtration.** “à dégager” follows the claimed equivalence of categories. “si on a l’hyp. de Poincaré” conditions a proposed replacement of the sphere requirement. The relative flags are “à définir avec soin”.
- **8, after the proposition.** “Déterminer l’image essentielle … et montrer qu’elle est plus grande que celle correspondant aux complexes cellulaires …”.
- **14, final paragraphs.** “Question … tjs de degré 2 ??”, followed by the case from 123 to 13. “On veut condition assurant qu’on récupère …” asks for reconstruction from the interval-indexed objects, their actions and their maps.

## Slips

| ID | Scan | As written and possible correction | Reason and confidence |
|---|---|---|---|
| S3a | 3, lines 6–9 | The principal comparison looks like x < y, while its first branch is x = y. A reflexive reading would use x ≤ y. | High for the incompatibility if the angle is read strictly. Substituting a single rank-zero face makes the displayed equality branch true for the pair (x,x). |
| S3b | 3, flag type | The type is first placed in the parts of [0,n] and then called a nonempty part of [1,n]. The latter would read [0,n] for the ranks already used. | Medium. The two lower endpoints are written differently and rank zero occurs on the same page. |
| S3c | 3, recovered incidence | In the first product the second rank may read α−1. The displayed condition on y favours α+1. | Low. The sign is marked doubtful. |
| S4 | 4, left, first operator | “cf Axiome 2” after the replacement of x₀. Axiome 3 is the neighbouring two-element condition on F(x₁)₀. | Low. The numbering is revised in these notes. |
| S16 | 16, middle equivalence | The singleton cardinal looks like 4 or 1. The final variable looks like I or Φ. The preceding condition reads 1 and Φ. | Low. These are doubtful strokes in the second occurrence. |
| S17 | 17, last coproduct | The argument of the part-symbol looks like I. The restriction of δ in the next line suggests Φ. | Low. The letter is marked in the transcription. |
| S18 | 18, dimension paragraph | The written supremum uses δ(I). With the displayed δ from Φ to I, δ(Φ) would denote its image. | Medium. I₀ = δ(Φ) occurs in the upper note. The manuscript does not introduce another domain for δ here. |

## Pointers

- **3–5.** The author returns to “Axiome 1′”, “cf Axiome 2”, “par l’axiome 1”, and “l’axiome 4 et des précédents”. These refer to this sequence of notes.
- **7–8.** “l’hyp. de Poincaré” is named in connection with the sphere criterion and again in the problem about the essential image.
- **12–14.** The index examples, including the arrow from 123 to 13, point back to the immediately preceding flag diagrams.
- No work title, bibliographic citation, date or external archive cote is explicitly supplied in these mathematical passages.

## Remarks of the model

- **M16, scan 16. High confidence for the finite example.** The strictness condition distinguishes geometries that have two flags with the same vertices. Take two incomparable minima a,b and two incomparable upper elements d,e, each above both minima. Each upper element has a lower set of the required two-vertex simplex shape. The common upper bounds of a,b are d and e, and neither is least. Enumeration confirms this example. It uses the clear supremum formula on scan 16.
- **M18, scans 17–18. Medium confidence as an interpretation.** The map from the minimal elements to I allows distinct vertices to have the same label while forbidding that coincidence within any one flag. This follows directly from the written restriction condition. It explains why the singleton fibres in the opening of 17 are allowed to be larger than one. The uncertain final coproduct index on 17 is unnecessary for this observation.

