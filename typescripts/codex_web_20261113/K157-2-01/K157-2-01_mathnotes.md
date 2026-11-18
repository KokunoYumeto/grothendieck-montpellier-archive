# Mathematical notes on cote 157-2, scans 2–17

## What the pages do

**Scans 2–3 — The indexing categories (D1).** After the chapter cover, Grothendieck draws the ordered category Φ on the integers. Its nonidentity arrows alternate. The full subcategory Φₙ runs from −n to n. He draws Φ₁ and its dual Ψ₁ and brackets the infinite zigzag in two ways, according to which adjacent pairs of arrows are grouped together.

**Scans 3–4 — Finite paths and their extensions (D2).** The inclusions of the Φₙ describe Φ as a direct limit. For the construction to follow he also uses retractions between the finite indexing categories, recording the resulting projective system as a pro-object. A diagram of shape Φₙ in X is a path with 2n arrows. Precomposition with a retraction extends a diagram by identities at both ends.

**Scans 5–7 — The category of all paths and its endpoints (D3).** In the two-sided infinite diagrams, the paths under consideration have only identity arrows sufficiently far out on either side. A slanted note distinguishes the category from its set of objects. The author renames the arrows on the negative side to display the symmetry about the origin. The two inclusions at the endpoints give the source-and-target functor to X × X and its fibre over (x,y).

**Scans 7–9 — Paths allowed by Σ (D4).** The class Σ of arrows contains the identities. A Σ-path has all its retrograde segments in Σ. After localization the author reverses those segments and composes the resulting direct path. He uses a square between adjacent segments to explain how a map of paths gives a map of arrows. The fibre of the arrow category with fixed source and target is discrete.

**Scans 9–10 — Passage to connected components (Q1).** The functor on paths yields the boxed map from the connected components of the category of Σ-paths from x to y to the set of arrows from x to y in the localization. He proposes to construct the localized category with these connected components as its Hom sets. This makes composition the next task.

**Scans 10–12 — Composition for finite lengths (D5).** Placing two paths end to end is expressed using two functors of indexing categories and a common endpoint. Their integer translations are written i ↦ i−m and i ↦ i+n. The resulting length-specific composition is to pass to the limit. Scan 12 draws the compatibility square and recasts it as a comparison between extending a composite and composing extended paths.

**Scans 12–14 — Homotopy of the two composites (D6).** The desired comparison is a path in the category of functors from A to B. Grothendieck draws the two routes round the square and calls the path h. In Cathot the morphisms are the connected components of the functor category. Assuming the comparison exists, the length-indexed path categories give ind-objects there, with an ind-morphism of composition.

**Scans 14–15 — A possible ordinary composition (Q2).** A question mark replaces the star over a proposed arrow between the ordinary path categories. The next diagram introduces an intermediate length N and specifies a factorization and a triangle that would have to commute in Cathot.

**Scans 15–16 — The parity correction (P1, P2).** A trial computation for odd m,n is crossed out. In the four-arrow example the glued path has the dual shape. Grothendieck restricts to even m,n and now enlarges one index by two while fixing the other path. He starts an explicit comparison using nonnegative vertex indices, strikes the longer calculation, and turns to a conceptual construction.

**Scan 17 — Endpoint-preserving functors (D7).** The two composites are named f and g. Two functors between finite path shapes give transposed functors F and G on diagram categories. Diagram (3) records their common action on the two marked endpoints. The final sentence begins to describe the full subcategory furnishing the target B and breaks off after *formée*.

## Statements left without proof

- **D2, scan 4.** «C’est un foncteur pleinement fidèle». He supplies the reason about surjectivity on objects and arrows in parentheses, without working through the full-faithfulness argument.
- **D3, scans 5–6.** «On a une inclusion pleinement fidèle» is followed by identification of its image. The assertion about the automorphism group of Φₙ is accompanied by the reflection, without a general proof here.
- **Q1, scan 10.** «Je dis que cette application est toujours bijective.» These sheets begin the proposed construction; they do not finish the proof of the displayed bijection.
- **D5, scan 11.** He calls the longer shape a «somme amalgamée» obtained by «recollant» the two shapes. He writes the maps and their common endpoint. The odd-length trial later limits the use of this description.
- **D6, scans 12–14 and 17.** «il faut prouver … la commutativité», «on va en fait trouver une homotopie», and later «Cette existence admise (cf ci-dessous la preuve)». At the end of scan 17 the conceptual argument has only begun.

## Questions and conjectures

- **Q2, scans 14–15.** «On aurait aimé le déduire d’un honnête foncteur» and «je doute qu’un tel foncteur existe». This is the ordinary composition on path categories. The question mark in the diagram labels that arrow. Scan 15 adds a condition with «Il faut supposer que pour N assez grand».
- **Q3, scans 12–13.** After inspecting a small case the author looks for a «chemin» in a functor category. The reading of the last numeral in that example is uncertain. The pages do not name a specific intermediate functor there.
- **Q4, scan 16.** «Je … vais essayer de donner une démonstration conceptuelle, sans “calcul” fastidieux». The crossed verb precedes *vais essayer*. This announces the approach begun on scan 17.

## Slips

| ID | Scan | Frozen reading | Suggested correction and reason | Confidence |
|---|---|---|---|---|
| S1 | 4 | The starred path has 2n arrows, with the added index range −n ≤ i ≤ n. | If i designates an interval by its left endpoint, the last such index is n−1. There are 2n+1 vertices. | High for the count. |
| S2 | 4 | The target of the extension ends in (Y). | (X) would keep the diagram in the category in which its identities are adjoined. The target category name immediately before the parenthesis is overwritten. | Low. |
| S3 | 8–9 | «i impair» and «(i pair)» accompany a leftward arrow with the index i. | Using its right endpoint for i gives the even index for the leftward edge in the original integer zigzag. The arrow on scan 8 and the cancelled condition around it have been reworked. | Low. |
| S4 | 11 | Hom with length n is defined using an underlined Ch with length m. | A common length on both sides would agree with the roles of the two expressions. Other nearby length subscripts are overwritten. | Low. |
| S5 | 12 | Both targets of the drawn square have arguments (x,y). | (x,z) fits the outer endpoints of the two inputs. The preceding map to the limit uses those endpoints. | High for the endpoint pair. |
| P1 → P2 | 10, 15–16 | The initial condition is «la = parité». The attempted odd case is struck through. | The author’s replacement is to take m,n both even. His live example for m=n=1 shows the dual orientation. | Low for reconstructing the discarded construction. |
| S6 | 17 | «source et et but». | A single *et* gives the ordinary phrase. The crop shows the two full signs separately. | High. |
| S7 | 17 | The source Hom expressions use Φ with subscript m,n. | The sum m+n would match the target of (1) and (3) before precomposition. The two comma forms remain in the transcription. | Medium. |

The two occurrences of *standart* on scan 5 are recorded in the doubts file. The first ending is uncertain, so this is a spelling question. The unusual source-and-composition wording on scan 3 and the endpoint arguments on scan 7 are also reading questions. They do not justify attributing a stronger mathematical error to the author.

## Pointers

- **Scan 4.** «diagramme (*)» refers to the path drawn on that sheet. Scans 6–7 use (*) again for the renamed path.
- **Scan 13.** «le diagramme carré ci-dessus» points to the large square of functors on that manuscript page.
- **Scan 14.** «cf ci-dessous la preuve» is an internal forward reference to the promised homotopy argument.
- **Scan 17.** «carré pag[e] 11» points to the square on manuscript page 11, which is scan 13. The page also refers to its own «foncteurs envisagés (1)».
- No external paper, correspondent or archive cote is cited in these sheets.

## Remarks of the model

- **R1, mine, high confidence.** The two written translations agree on the claimed common endpoint. Substituting n in the first and −m in the second gives n−m in both cases. This checks the endpoint equality in D5.
- **R2, mine, high confidence for the pictured case.** Reading the four arrows left to right in the live example on scan 16 gives left, right, left, right. The Φ₂ diagram from the indexing rule gives right, left, right, left. This independently checks the orientation that motivates P2. It does not settle the existence question Q2.
- **R3, mine, low confidence as a qualification of the text.** If 0 is admitted among the lengths in the automorphism assertion on scan 6, Φ₀ has one object and only its identity. In the finite shapes at n=1,2,3, identity and reflection are the only automorphisms. The scope intended by the parenthetical remark is unstated.
- **R4, mine, medium confidence.** Diagram (3) on scan 17 explains why endpoint agreement matters separately from comparison of the interiors: it fixes what happens on the two objects of the discrete source. The unfinished sentence prevents identification of all the conditions he planned to impose on the full subcategory.
