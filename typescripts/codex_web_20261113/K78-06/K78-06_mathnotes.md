# K78-06 · Mathematical notes

The references below use scan numbers and the equation labels as written. “First (33)” means the discriminant on scan 88. “Second (33)” means the formula for α on the same scan. The identifiers are also used in CHECK_EVENTS.tsv.

## What the pages do

**U1 · Scans 75–77.** A combinatorial polyhedron Π and a frame in it are the starting data. The programme is to classify regular geometric realizations in variable affine planes, attach a numerical invariant to an isomorphism class, and recover the realization from that invariant. The infinite polygon is considered first. Factorization through Πₙ, faithfulness of the finite realization and the removal of the choice of frame are separate steps.

**U2 · Scans 77–79.** The two involutions σ₀ and σ₁ represent the generators of the infinite dihedral group. The image of a frame is an incident point and line, (s₀,a₀). Iterating u = σ₀σ₁ gives the vertex and edge maps. The two diagrams relate them to the projections from the space of frames. Equivariance and incidence require σ₁s₀ = s₀ and σ₀a₀ = a₀.

**U3 · Scans 79–81.** The manuscript asks when the vertices generate the plane. Its lemma compares three conditions, including nonconstancy of both maps and affine independence of s₀, s₁, s₋₁. The resulting proposition describes the realization by the triple (σ₀,σ₁,s₀). Its edges are the lines through consecutive vertices.

**U4 · Scans 82–84.** Setting the origin at s₀ and using s₁−s₀ and s₋₁−s₀ as basis vectors produces coordinates for both involutions. Two coefficients α and β occur in σ₀. The condition σ₀² = id gives αβ = 0 and β(β+2) = 0. The proposition on 84 uses these equations to describe the pairs of parameters.

**U5 · Scans 83–85.** The example with vertices (ζⁱ,ζ⁻ⁱ) gives α = ζ + ζ⁻¹ and illustrates the parallelism motivating β = 0. A list of equivalent conditions uses vertex differences, determinants, a trace, and exclusion of the exceptional case. The proof moves between a condition at the starting vertices and its translates by powers of u.

**U6 · Scans 85–86.** For the improper case, α = 0 and β = −2 in characteristic different from 2. The affine map u sends (x,y) to (1−y,−x). Its square is translation by (1,−1). The prose distinguishes infinite order in characteristic zero and a realization through Π₂ₚ in positive characteristic. The scholium returns to proper realizations, with α free in k.

**U7 · Scans 87–88.** In the proper case, the two affine fixed loci have equations 2x−αy−1 = 0 and x−y = 0. The sheet discusses the translation exception in characteristic 2 and the fixed line at infinity. Their common affine fixed point, called the centre in the margin, has x₀ = y₀ = 1/(2−α) when α ≠ 2.

**U8 · Scan 88.** The linear part of u has rows (α,−1) and (1,0). Its determinant and trace give the characteristic polynomial, the factored discriminant and the relation α = ζ + ζ⁻¹ between its roots and the invariant introduced at the start.

## Statements left without proof

| ID | Scan | Manuscript words | What is left to the reader or to later work |
| --- | --- | --- | --- |
| P1 | 75 | “il y a un Π-isom unique entre elles, par définition” | Uniqueness is referred to the definition. These sheets do not reproduce the definition on which it rests. |
| P2 | 76–77 | “se plonge (comme sous-catégorie pleine)” and “Cette étape est essentiellement triviale” | The full-subcategory assertion and the last step that removes the frame receive no separate argument here. |
| P3 | 80 | “En effet, b ⇒ (a) ⇒ (c) sont …” | These two implications are dispatched in a phrase. The adjective after “sont” is doubtful. The ensuing argument works in the reverse direction. |
| P4 | 85–86 | “À isom unique près, il y en a un et un seul” and “on trouve qu'elle est fidèle” | The improper example is written explicitly. Uniqueness up to the indicated isomorphism and the characteristic-zero faithfulness assertion are not proved separately. |
| P5 | 86 | “On vérifie aisément que la réalisation géom de Π₂ₚ est bel et bien fidèle” | The order calculation is given. The passage from that calculation to faithfulness of the polygon realization is asserted. |
| P6 | 86–87 | “Avec la théorie projective … s'explique complètement” and “encore une réflexion projective” | The projective viewpoint is invoked. The exceptional line at infinity is identified on 87, without a development of the projective theory. |

## Questions and conjectures

**Q1 · Scans 75–77.** “il faudra pouvoir expliciter” asks for the realization to be recovered from Π and the invariant. “Expliciter les conditions sur α” calls for the factorization and faithfulness criteria for a finite polygon. The ending on 88 still deals with eigenvalues of u.

**Q2 · Scans 82–83.** The note “on s'attend à” places β = 0 and α = ζ + ζ⁻¹ = 2 cos θ together. The following example supplies a calculation. “On a donc envie d'imposer la condition” then selects β = 0. On 85 the excluded case has β = −2 in characteristic different from 2, so the initial expectation is not a claim about every realization.

## Slips

The doubts register also gives the approximate line of each item.

| ID | Scan | Manuscript and possible correction | Confidence and reason |
| --- | --- | --- | --- |
| S01 | 75 | The title can read “Réalisation géométriques”. If the noun is singular, the adjective would be géométrique. A plural reading for the noun also removes the apparent disagreement. | Low. The last stroke of the noun is ambiguous. |
| S02 | 76 | After n ∣ n′ the source is written Π∞. Πₙ′ would make the divisibility hypothesis relevant. | Medium. Π∞ has already been introduced as a source for all the quotients. |
| S03–S05 | 76–78 | On 76 “par un l'invariant” contains two articles. On 77 “par des … un invariant” retains an article from the earlier wording. On 78 the two maps would ordinarily take the plural définis. | High for the two live articles on 76, low for the struck context on 77, medium for the agreement on 78. |
| S06, S08 | 79–80 | The flag datum on 79 may point to (3) rather than the apparent (4). The maps called “de (3)” on 80 have their formulas in (4). | Low on 79 because the numeral is reworked. Medium on 80 because (3) specifies a flag. |
| S07 / S07r | 80 | “les sₙ … sont affinement indépendants” apparently means that the sₙ generate E affinely. | High. An indexed family with more than three members in an affine plane is affinely dependent. The preceding scan explicitly asks for generation. |
| S09 | 80 | The two entries for the image of a line use different generators. Applying σ₁ gives dr(s₀,s₋₁). In the next line s₋₁ ∈ a₀ would make that image equal a₀. | Low for reconstructing the passage. These follow from the fixed vertex and the definition of a₀. The subscript of the final stabilizer is separately doubtful. |
| S10 | 81 | The sentence ending “s₀,s₁ et s₋₁” lacks its predicate. The ensuing proposition has “forment une base affine de E”. | Medium. The words recur a little below, but the abandoned sentence has no written ending. |
| S11 / S11r | 82 | The coordinate list has s₂ = (0,1). The basis in (15) gives s₋₁ = (0,1). | High. The other value assigned to s₂ in (16) depends on the parameters. |
| S12, S13 | 83 | The positive power in the example should be 2 by substitution. In (iii′) a parallelism would reproduce the distinction between (ii) and (ii′). | Low for each. The tiny exponent is doubtful and the sign in the adjoining version of (iii) is reworked. |
| S14 | 85 | At n = −1 the two local conditions are (ii), (ii′). Translating them gives (iii), (iii′). The running text mixes the primed and unprimed pairs. | Low for the intended labels in this reworked proof. Direct substitution produces the local indices 2, −1, 1, 0. |
| S15 / S15r | 86 | Both left sides of (25) read u(x,y). The second should read u²(x,y). | High. Composition gives its right side, and the prose explicitly names the square. |
| S16, S17 | 88 | There is a comma-like mark in “ζ, ∈” before the field symbol. Two distinct displays, the discriminant and the root sum, both carry (33). One could cite them as (33a) and (33b). | Medium for the stray punctuation. The repeated number is visible. Confidence about the intended numbering is low because the second label is reinked and the following relation already carries (34). |

## Pointers

- **T1 · Scan 75.** “déjà envisagé précédemment” points back to an earlier occurrence of the numerical invariant. There is no title, cote or author attached to the reference.
- **T2 · Scan 86.** “Avec la théorie projective des polygônes réguliers” points to the projective treatment of the improper case. No separate work is named.
- **T3 · Scan 88.** “Comparaison avec les …” announces a comparison. The short mathematical expression after “les” is doubtful. These pages end before the comparison is carried out.

## Remarks of the model

- **R1 · Model, high confidence, scans 84–86.** Over a field of characteristic different from 2, equation (22) leaves exactly one pair with β ≠ 0. Indeed β must be −2, and then αβ = 0 forces α = 0. The field assumption matters to that short inference.
- **R2 · Model, high confidence, scans 87–88.** On the diagonal x = y the first fixed-line equation becomes (2−α)x = 1. This explains at once the denominator on 88 and the absence of an affine centre when α = 2. In characteristic 2 the manuscript's exceptional values α = 2 and α = 0 denote the same scalar.
- **R3 · Model, high confidence, scan 88.** Determinant one gives ζζ′ = 1 for the two roots with multiplicity. This connects the reciprocal in the second (33) directly to the earlier numerical invariant. The conclusion also covers a repeated root.
