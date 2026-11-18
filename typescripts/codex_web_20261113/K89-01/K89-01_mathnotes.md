# Mathematical notes on K89-01

The labels in brackets identify statements in CHECK_EVENTS.tsv. Scan numbers are those of the archive PDF.

## What the pages do

**Scans 3–4 [H1, H2].** A combinatorial hexagon gives a two-element set of orientations and a six-element torsor. The displayed decomposition separates the factors of orders three and two. Its three long diagonals form Δ and its two inscribed triangles form τ. Each vertex belongs to one of each, giving the displayed $S\simeq\Delta\times\tau$. The manuscript then regards the vertices as two triples $S_i$ with a common orientation torsor. A marginal sentence makes the equivalence of groupoids explicit.

**Scans 4–5 [G1, G2].** A partition into two triples together with compatible identifications of their orientations has an automorphism group $G$ of order 36. To recover a hexagon the author chooses an involution exchanging the triples. The note in the left margin imposes a further condition on its action on the common orientation. There are three compatible choices. The automorphism group of the chosen hexagon is the centralizer of that involution, of index three in $G$.

**Scans 5–6 [G3, G4].** The three antipodisms generate $G'$. Conjugating one generator by another gives the third. The page writes both the three-generator relations and the two-generator form $\sigma^2=\sigma'^2=(\sigma\sigma')^3=1$, and identifies the action of $G'$ on the three antipodisms. It then asks about $G/G'$.

**Scan 7 [T1, T2].** The two triples are treated as torsors for the same group $\Gamma_\omega$. Their contracted product is a torsor $T$. Using $u$ to transport an element from one triple to the other, the displayed calculation exchanges the scalar factors $\gamma$ and $\gamma'$. This is the author's check that $G'$ acts trivially. He then associates $T$ with three other involutions, acting by transposition on both the pair of triples and the common orientation.

**Scans 8–9 [S1].** Starting again with the partition alone gives an automorphism group of order 72. An involution interchanging the triples amounts to a bijection between them, described also by its graph. The six choices form $S'$. Their actions on the orientations split them into two triples. The author relates a choice of an element of $S'$ to a hexagon structure. The next clause about a hexagon with a chosen vertex stops at “à un”.

**Scan 10 [V1, V2].** The projective line of a two-dimensional vector space over $\mathbb F_3$ has four directions. A pair of directions and its complementary pair give the two direct-sum presentations (1) and (2). In (3)–(4) a tuple from the starred lines determines the line through the sum of its entries. The same pairs give product decompositions of an affine torsor $P$ in (5).

**Scan 11 [A1, A2].** Formula (6) defines the affine factor $P_i$ by taking the quotient by the other direction in its pair. The resulting pair of partitions of the nine points is called “d’équerre”. Each class of one meets each class of the other in exactly one point. A second pair is supplied by the complementary two directions.

## Statements left without proof

| ID | Scan | Author's words and scope of what is left implicit |
| --- | --- | --- |
| H2 | 3 | “Le groupoïde des hexagones combinatoires est équivalent à la catégorie …” The reconstruction of a vertex is given. The action on morphisms for the whole equivalence is left implicit. |
| G1 | 4 | “Le groupe des autom. de cette structure est d'ordre 36”. A diagram gives the sign map and the two extensions. No separate count is written out. The expansion of *autom.* is uncertain. |
| G2 | 5 | “et en fait est son propre normalisateur”. This is inserted at “non distingué”. No separate argument for the normalizer follows. |
| G4 | 6 | “$G'$ est présenté par les gén. … et les … relations”. The page derives the cube relation by cyclic permutation. It gives no separate argument that the listed relations suffice. |
| T2 | 7 | “et on vérifie que … conjugue … en … (en fait, on l'a déjà fait …)”. The last conjugation assertion refers back. The two primed subscripts are graphically uncertain. |
| S1 | 9 | “qui est de degré 3”. The surjection and resulting partition are stated without a separate fibre count. |
| V2 | 10 | “Notons les relations” in (3). Formula (4) gives a map. The descent to the contracted product and the symmetric identification from the other pair are left implicit. |
| A2 | 11 | “il suffit de supposer qu'elle est tjrs non vide; ou qu'elle a tjrs au plus un élément …”. Neither of the two sufficient conditions is expanded. |

## Questions and conjectures

**Scan 6 [Q1].** “Quel est le groupe quotient $G/G'$ (d'ordre $6$) ?” Scan 7 constructs an action of the quotient. These pages do not supply a separate explicit isomorphism type as an answer. No further conjecture is marked.

## Slips

| ID | Scan and written form | Possible correction and reason |
| --- | --- | --- |
| L1 | 3, “que il” or “qu’il” | *qu’il* would give the conventional elision. Low confidence because the apostrophe and spacing are uncertain. |
| L2 | 8, “ses deux classes” appears twice | The second occurrence could be omitted without loss. It may be an intentional restatement after the indexed notation. Low confidence as a slip. |
| L3 | 8, curled group letters in Isom and in the following indexed family | Plain $S_i,S_{\bar i}$ would name the two triples whose points a bijection matches. The later graph lies in a product of sets. Low confidence because the alphabet and second index are partly overwritten. |
| L4 | 10, a small $i$ above the wedge in the line after (3) | Omitting the upper $i$ would agree with the preceding display. Low confidence that it is redundant. |
| L5 | 11, second pair “de type (3,3)” | Read as class sizes, this should be $(3,3,3)$. The corrected partition is the one in [A1]. Both decompositions are on the same nine points, and each quotient by a direction has three classes of three. High confidence under the meaning of type used in the first decomposition. |

## Pointers

No person, separate paper or other cote is cited. Internal pointers include “grâce à” followed by a doubtful label on scan 5, “en fait, on l'a déjà fait …” on scan 7, the earlier name $\omega$ referenced under the surjection on scan 9, and “les formules (1) et (2)” on scan 10. Scan 11 continues (5) with (6).

## Remarks of the model

**My answer to the question on scan 6 [Q1], high confidence for the groups specified on scans 4–6.** The quotient is isomorphic to the symmetric group on three letters. In a permutation model of the two triples I let $G$ act by conjugation on the three block-swapping involutions that reverse the common orientation. All six permutations occur. The kernel is precisely the six-element subgroup generated by the three orientation-preserving antipodisms. This also distinguishes the two sets of three that occur in the margin of scan 5.

**My reading of (4) [V2], medium confidence.** If $D_i^*$ denotes the nonzero vectors of a direction here, each input line offers two choices. For every pair of directions, the four possible sums span the two complementary directions, twice each. This checks the formula with that interpretation of the star. The page gives no separate definition of the star.

**My reading of the two sufficient conditions [A2], high confidence.** The two sets of three classes give nine possible intersections, sharing the nine points between them. Having all nine occupied or having at most one point in each forces one point in every intersection.
