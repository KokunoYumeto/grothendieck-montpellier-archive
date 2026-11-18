# CTRL-148 — mathematical notes

Written after the transcription freeze at 2026-11-17T18:28:06.242005+00:00. These light notes use only scans 44–58. Tentative readings are identified where they affect interpretation; they do not authorize changes to the frozen transcription.

## What the pages do

**Topological groupoids (44–46).** The notes introduce an oriented topological Teichmüller groupoid, an orientation-changing variant and a signature map to the one-object groupoid of signs. A richer groupoid has objects described by a compact oriented surface, a compact one-dimensional submanifold and finitely many marks. The author distinguishes cutting circles, boundary circles and rigidification vertices, and lists several full subgroupoids. Scan 45 is a cancelled preliminary fragment about an enriched weighted graph.

**Weighted graphs (47–49).** Finite graphs are encoded by vertices, oriented arcs, an involution and an origin map, allowing free edges and isolated vertices. Vertex genera and an edge-related weight are added amid revisions. A functor associates such a graph to the surface data. Connectedness, discrete sums, total genus and the special cases without cutting circles or without marks are discussed. The drawings show allowable graph shapes and weighted components.

**Refined marking data (50–52).** Numerical edge weights are refined to finite sets with orientation-dependent cyclic permutations, also described using torsors. The author then discusses polygons and combinatorial “cartons”, with an action of a group presented by two involutions, a map to oriented arcs and additional orientation data over free edges. He asks that a combinatorial description recover the resulting graph functor.

**Erasure operations (52–55).** Four operations are set out: erasing selected marks; erasing cutting circles and contracting corresponding edges; filling boundary holes and deleting free edges; and a mixed operation combining these. Scan 53 specifies the additional marked subset needed to express forgetting and erasure functorially. Its long marginal discussion distinguishes different kinds of erasure, but the reading is too uncertain to make its detailed classification secure.

**Adding marks (56–57).** Surmarking is described by choosing numbers of new rigidification points in the open intervals between existing marks. The next page considers uniform versions using contractions or extensions of the cyclic operator groups, with divisibility and multiplier conditions. The author contrasts the structural effects of partial erasure and uniform surmarking.

**Cutting (58).** Cutting along selected circles is described on graphs by cutting a linked edge in the middle to produce two free edges, carrying the marking along. The author distinguishes marked and unmarked circles and discusses possible recovery of the original data. The page ends in an unfinished sentence.

## Statements left without proof

| Scans | Claim or deferred assertion | His words / formula |
|---|---|---|
| 44, 46 | Signature fibre and component comparison for the orientation variants are asserted without a separate proof. | “dont la fibre … (ou noyau) est” followed by the oriented groupoid; the displayed isomorphism of the two pi-zero sets on 46. The omitted word in the quotation is the deleted **est**. |
| 48 | The graph functor gives an isomorphism on components and a surjection on fundamental groups. | “induit un iso sur les” `π₀`, “et un surjectif sur les” `π₁`; “0-isomorphisme”. |
| 48–49 | The functor respects discrete sums; surface and graph connectedness agree. | “et (*) y commute”; `π₀(X) ≃ π₀(ΓMD(X,Σ̃,R))`. |
| 49, margin | The total genus is expressed using vertex weights and a graph invariant, without a derivation. | “le genre total est donné par” `g = Σ_{s∈S} g_s + c(Γ)`. The identification of c with rank/dimension of H¹ is itself a doubtful reading. |
| 50–51 | The cyclic marking data and polygon/carton description are stated as canonically recoverable. | “défini de façon évidente”; “peut se décrire … de façon canonique”. |
| 54 | How the weight changes under contraction is left to be explained. | “Il convient ici d'expliciter comment la pondération suit...” |
| 55 | Filling boundary holes does not change vertex weights. | “les pondérations des sommets restent inchangées”. |
| 56 | Surmarking produces an object with a strong uniqueness assertion. | “défini à isom unique près”. No separate argument for the uniqueness is given here. |
| 57 | Partial erasure and uniform surmarking have opposite effects on structural strength. | “le gommage partiel est en fait un” followed by tentative **renforcement**; “et inversement pour le surmarquage uniforme”. The following **pas/par** is also doubtful. |
| 58 | The operation in the marked case is recoverable up to a finite ambiguity. | “à peu de choses près” and “peut se récupérer, à l'aide du produit de cette opération”. The spelling of the ambiguity word and the small isomorphism qualification are uncertain. |

## Questions and conjectures

No clearly labelled conjecture appears. The following are explicit proposals, qualifications or unfinished intentions.

- **47, margin:** “pas assez précis, comme donnée” is the tentative reading introducing a refinement of the edge data. The exact phrase is doubted.
- **49:** “les opérations qu'il nous faudra expliciter et transcrire (combinatoirement) dans la suite”.
- **52–53:** “il faut reconstituer le foncteur canonique”; “il nous faudra donc décrire un foncteur”. These are requirements for the intended combinatorial reconstruction.
- **53, margin:** “Il faudrait” is followed by tentative readings **distinguer les deux cas**. The distinction between weak and strong erasure should not be treated as a securely transcribed theorem.
- **57:** “On va peut-être se borner par la suite” introduces the proposed restriction to special uniform operations.
- **58:** “Mais il semble que dans la façon dont nous allons travailler” remains unfinished in this packet.

## Slips

These are plausible editorial diagnoses, not certain corrections of the author's mathematics. The frozen text keeps the written forms.

| Scan / place | Frozen form | Possible correction | Reason / confidence |
|---|---|---|---|
| 49, second diagram | `A=A_0` | `A=A_ℓ` | The case immediately preceding it has only free edges, for which ell is used elsewhere. The zero is readable. Medium. |
| 50, last line | `r(ω)=1` | `r(a)=1` | The displayed weight map has domain A, whereas omega denotes orientation data. Medium. |
| 54, middle | `π₀(Σ′)=A_0` | Either `π₀(Σ)=A_0` or `π₀(Σ′)=A′_0` | The same sentence introduces a selected subset A-prime-zero. The intended repair is not uniquely determined. Medium that there is a mismatch; low for choosing a repair. |
| 56, action sentence | “l'opération qui … r′(b) nouveaux sommets” | Possibly supply **adjoint** or another verb | The ink at this point does not contain the supplied verb that appeared in the first transcription pass. This is a possible syntactic omission, not permission to complete the frozen reading. Low. |

## Pointers

- **46, left margin:** “MD = ‘modulaire’ ou Mumford-Deligne” (the parentheses around MD are doubtful). This marginal attribution does not identify a particular paper. The name Teichmüller also appears in the title and the names of the groupoids, without a bibliographical citation.
- **49, 57:** “dans la suite” / “par la suite” point forward in the author's project without a bibliographical reference.
- **53, margin:** a tentative “plus bas” occurs near the tentative surmarquage passage; 56–57 indeed discuss that operation within this packet. The marginal wording remains insecure.
- No explicit reference to another cote, dated text or numbered external paper was securely read.

## Remarks of the model

- **Model remark — high confidence:** The movement from edge cardinalities to actual finite cyclic marking data is explicit across 50–52. The later erasure and addition operations use precisely these finer data; this explains the stated need to recover the graph functor, without supplying a reconstruction proof.
- **Model remark — medium confidence:** Erasing a selected subset requires retaining that selection as extra data before applying the erasure functor. Scan 53's main diagrams make this distinction visible even though its marginal account of structural strength is difficult to read.
- **Model remark — medium confidence:** The “isom unique” wording on 56 deserves clarification about what data an isomorphism must fix. These pages do not state enough here to certify or refute that uniqueness claim. This is a mathematical question, not a proposed transcription change.
- **Model remark — high confidence:** No conclusion should be drawn from the unfinished final sentence on 58. Its continuation lies outside this packet.
- **Post-freeze reading questions:** None newly identified while writing these notes. Existing doubts, especially the note on 53, remain unresolved.
