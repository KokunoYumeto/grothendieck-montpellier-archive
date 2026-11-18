# K76-04 · Mathematical notes

## What the pages do

**U1 · Cube symmetries (51).** Starting from the pair $(B,\sigma)$, the corollary compares isomorphisms of the pairs, affine isomorphisms of the cubes and order isomorphisms of their face structures. The proof uses the composite and the determining action on vertices. Below the automorphism diagram the commutant of $\sigma$ is related noncanonically to permutations of $I$ and independent signs. A final corollary says the facets are cubes.

**U2 · Flags and torsors (52–53).** The number of completions of a flag gives $2^n n!$. To show the action is free, the writer fixes a flag and inducts on its last proper face. An affine symmetry fixing that hyperplane pointwise must preserve the side containing the polytope. A based cube then makes the flags of another cube into a right torsor, with a commuting left action. The standard model uses $[1,n]\times\{\pm1\}$ and an increasing sequence of intervals.

**U3 · Antipodes and face counts (54).** The central symmetry acts on partial sections by $I'\mapsto\sigma I'$. A cancelled proposal about intersections of arbitrary closed faces gives way to a characterization using disjoint hyperfaces. The page records the centre and computes the alternating sum from $c_d=\binom nd2^{n-d}$, including the full cube as a face.

**U4 · Orientation from frames (55, 57).** The antipodism acts on orientations by $(-1)^n$. In odd dimension the text separates off the sign factor from the orientation-preserving automorphisms. An orientation picks out a set of direct frames. The changes $\sigma_i$ must exchange this set with its complement. Scan 57 returns to how a face-poset isomorphism acts on the two orientations.

**U5 · General convex polytopes (56–57).** The affine action maps to order automorphisms and then to permutations of frames. The induction for a flag stabilizer propagates identity across facets sharing a codimension-two face. Regularity is defined using transitivity on frames, and homogeneity by uniform incidence numbers $d_i$. With $N$, $N_c$, and $R$ the two group orders and the number of frames, he writes $N\mid N_c\mid R$ and relates $N=R$ to regularity.

**U6 · Conjugacy data (58–59).** Decompose $I$ into orbits of $u_I$ and look above each orbit in $B$. Over an orbit of length $i$, the lift consists of two cycles of length $i$ or one cycle of length $2i$. The table with $b_j,b'_j,i_j$ illustrates the second case. Two arrays of counts $\alpha_i^+,\alpha_i^-$ give the conjugacy data, with weighted sum $n$.

**U7 · Fixed faces (59–60).** Over a twisted orbit the invariant partial section must be empty. Over an untwisted one there are three choices. This gives the total $3^{\sum\alpha_i^+}$ and a product generating fixed faces by codimension. The constant term counts the full cube.

**U8 · The three-cube (60–61).** The example separates one-, two- and three-cycle cases on $I$, listing coordinate actions, orders, geometric descriptions and signed marginal counts. The two one-cycle rows give a diagonal rotation of order 3 and an order-6 symmetry. The enumeration closes with $10=2+4+4$.

**U9 · Opposite-vertex pairs (61–62).** If $ux=\pm x$ for every vertex, the proposition identifies $u$ as the identity or the antipodism, with the inserted hypothesis $n\ge3$. For a three-cube the four opposite-vertex pairs recover the orientation-preserving group. The next corollary states an equivalence between oriented three-cubes and four-element sets, with isomorphisms as morphisms.

**U10 · The “cube (combinatoire) gauche” (62–63).** Taking the antipodal quotient of the boundary gives real projective space. The projected cells need not meet along a single cell. The square and its two arcs illustrate distinct pieces of an intersection. The face order is compared with the opposite order on partial sections modulo $\sigma$. The final question compares the projective and order automorphisms. The odd-dimensional discussion invokes the orientation cover.

## Statements left without proof

| ID | Scan | His words | Scope |
|---|---:|---|---|
| P1 | 51 | “Au lieu de … Isom_aff … aussi d'écrire … Isom_proj”; “Les facettes du cube sont des cubes” | Both are appended to the isomorphism proof. |
| P2 | 53 | “est une équivalence de catégories” | The functor to right torsors is displayed. Essential surjectivity is left implicit. |
| P3 | 54 | “le centre de Aut(C) est le groupe {1,σ}”; “valable en fait pour tt polyèdre convexe de dim n!” | The binomial calculation establishes the cube case. The general polytope assertion and the centre description have no separate proofs here. |
| P4 | 55, 57 | “2 telles parties”; “ne dépend, à isom canonique près, que de Φ(C)” | The exchange test is given, and the induced maps are displayed. Neither the count of the two subsets nor the canonicity is proved in detail. |
| P5 | 56 | “Argument topologique de connexité…” | The last step needed for propagation across all facets is named. |
| P6 | 59 | “Cette situation est aussi uniquement déterminée”; “sont donnés par 2 suites” | The picture and orbit reduction motivate uniqueness and classification. The converse realization of the arrays is left implicit. |
| P7 | 61–62 | “u est l'identité ou l'antipodisme”; “Le foncteur … est une équivalence” | The vertex-action proposition is stated, followed by the two corollaries in dimension 3. |
| P8 | 62–63 | “est injectif”; “il est évident que la seconde l'est” | The first concerns a closed face mapping to projective space; the second concerns the map from projective to order automorphisms. |

## Questions and conjectures

| ID | Scan | His words | Status |
|---|---:|---|---|
| Q1 | 54 | “Ceci caractérise l'autom σ ?” | Inside a cancelled statement about arbitrary pairs of closed faces. |
| Q2 | 55 | “Il faut donc décrire … quelles sont les parties … qui sont de la forme D(ω)” | Answered under “Solution” by requiring exchange under each $\sigma_i$. |
| Q3 | 61 | “En tout il y a 10 classes” | The following punctuation is doubtful; the addition on the next line is clear. |
| Q4 | 63 | “le composé … surjectif ?”; “Cas n pair : à examiner …” | The surjectivity question is followed by an odd-dimensional argument. The even case is expressly left for examination. |

## Slips

| ID | Scan | Written form | Apparent intention and reason |
|---|---:|---|---|
| S1 | 51 | “on [peut, struck] aussi d'écrire” | Possibly *on peut aussi écrire*. The revision leaves a sentence fragment. **Low confidence** because the verb is cancelled. |
| S2 | 56–57 | $\forall F$ … “qui majorent $x$” | Use one bound variable, either $F$ or $x$, for the face being extended. The definition introduces no new $x$ between the two clauses. |
| S3 | 59 | “stables par $I$” | Apparently *stables par $u$*. The drawn $I$ is the set below the fibres, and $u$ provides the action. |
| S4 | 59–60 | “parties non vides” and “y inclus la facette $C$” | If the full cube is counted, allow the empty partial section. Its codimension is zero in the following series. |
| S5 | 60 | $\sum_{i=0}^n f_d t^d$ | Put $d=0$ under the left sum. The coefficient and the exponent both carry $d$. |
| S6 | 62 | $C$ followed by a short shaft labelled $p$, then $\partial C$ | Possibly $\partial C\longrightarrow\partial C/\sigma$. The next lines apply $p$ to faces on the boundary. **Low confidence** because the shaft is doubtful. |
| S7 | 63 | $p(\bar F)\subset p(\bar F')\Longleftrightarrow\bar F\subset\bar F'$ | For fixed representatives, the right side must allow $\sigma\bar F'$ as well. The square below the formula gives a proper vertex–edge example (R3). |

## Pointers

| Scan | His words | Referent |
|---:|---|---|
| 51 | “histoire combinatoire – cf cor. précédents” | Earlier corollaries. No title, person, cote or page number is given. |
| 54 | “la formule d'EP” | The alternating face-count relation named by initials on this sheet. |
| 61 | “conjugué au précédent”; “suivi de … antipodisme” | The immediately preceding symmetry in the local example. |

## Remarks of the model

**R1 · Model, high confidence (54, 59–61).** For $n=0,\ldots,8$ the stated face counts give alternating sum 1. In dimension 3 an enumeration of all 48 signed coordinate permutations gives the ten marginal counts $8,8,6,6,6,6,1,3,3,1$ up to order. For each permutation, counting fixed ternary face labels by codimension gives the coefficients of the product on scan 60.

**R2 · Model, high confidence (61–62).** Acting on the four opposite-vertex pairs of the three-cube gives 24 distinct permutations from the orientation-preserving subgroup. In the full group only the identity and central inversion fix all four pairs. This checks the group calculation in the first corollary in its stated dimension.

**R3 · Model, high confidence (63, first display).** Choose the lower-left vertex of the drawn square and take the top edge as the second representative. The projected vertex is an endpoint of the projected top edge, but the vertex is not on the top edge in the square. Permitting an antipodal change of representative on the right restores this incidence.

**R4 · Model, low confidence as an interpretation of the cancelled text (54).** Two adjacent vertices of a square are distinct and are not antipodes. Both intersections in the cancelled proposition can therefore be empty. The example helps explain the later restriction to hyperfaces; the manuscript gives no reason for the cancellation.

**Reading questions after the witness check.** On 51, the frozen opening “l'un des sommets” might read “l'ens des sommets” because the small group lies directly under the line striking the whole paragraph. On 63, in the first NB, a small mark beside the P in the frozen $P(E)$ might be a subscript. The scan does not give a clean separation from the parenthesis. On 63, in the odd-dimensional argument, the frozen pair begins with a looped sign whose candidates include $\mathcal X$, $\partial C$, $X$ and $\mathcal H$. It is unsafe to name the covering object from that sign alone. These questions are recorded here without changing the text.
