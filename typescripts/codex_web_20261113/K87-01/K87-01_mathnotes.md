# Mathematical notes on cote 87, scans 3–14

## What the pages do

**Convex sets and lines (scan 3).** The opening programme treats convex hulls through barycentric combinations and simplices, then tests convexity by intersection with each line. It introduces the dimension of a convex set. For a set spanning the ambient space, a) and b) relate interior, boundary and closure to sections along lines through an interior point. In c) a proposed homeomorphism between two compact convex sets takes a chosen point to another and is affine on each outgoing ray.

**Facettes and their order (scan 4).** Two points are related when they coincide or when both are interior to the section by their joining line. A nonempty *facette* is a class of this relation. The empty set is also allowed. A singleton facette defines an extreme point. Assertions ①–③ describe the largest-dimensional class, recover a class from its affine span and give equivalent comparisons of two classes. The page compares these relatively open pieces through their spans and closures.

**Joins and closed unions of facettes (scan 5).** In ④, a positive barycentric combination of finitely many points belongs to the facette that is the supremum of their facettes. In ⑤ a union of facettes determines a subset Φ of the ordered set. The text gives separate criteria for convexity and relative closedness. Assertion ⑥ and the sentence following it examine sets of the form $\overline F\cap C$ and arbitrary intersections.

**Extreme points and finiteness (scan 6).** Assertion ⑦ states that a compact convex set in finite dimension is the convex hull of its extreme points. Assertion ⑧ gives finiteness of the facettes of a finite union of simplices as described there. The corollary characterizes convex polyhedra through finiteness of the facettes or of the extreme points.

**Polarity (scans 6–7).** For dual spaces $E,E'$, the polar of $A$ is given by all $x'$ with $\langle x,x'\rangle\geq-1$ for all $x$ in $A$. It is written as an intersection of half-spaces $H(x)$. Th. 1 identifies the bipolar with the closed convex hull of $A\cup\{0\}$. Its corollary describes reciprocal, order-reversing maps. Scan 7 then relates hulls to intersections, and interior containment of the origin to compactness of the polar.

**Separation and the planar reduction (scans 7–8).** Théorème 1′ characterizes closed convex sets as intersections of closed half-spaces. Théorème 1″, labelled « Hahn-Banach », seeks a hyperplane containing a given subspace and disjoint from a given open convex set. The argument replaces the set by its positive dilates, enlarges the subspace, then passes to a quotient. In the plane it distinguishes an open half-plane from a cone of positive combinations of two basis vectors. Two rays are drawn beside the formula.

**Secteurs polyédraux (scans 8–11).** A proposition equates a finite intersection of closed half-spaces with the closed convex hull of finitely many points and closed rays. The compact case singles out convex polyhedra. Scan 9 chooses a relative interior point as origin, brings in a compact polar, and develops b) ⇒ a) through two cancelled drafts and a surviving argument. Scan 10 gives the converse and uses the lemma below. Scan 11 gives the name « Secteur polyédral » and states how the sectors containing the origin correspond under polarity.

**Cutting a convex set by one half-space (scan 10).** The lemma concerns the number of extreme points. The rewritten proof uses induction first on the ambient dimension and then on the number of half-spaces. For $C=C_1\cap H$, it distinguishes points off the boundary hyperplane $H_0$, which are tested in $C_1$, from points on it, which are tested in $H_0\cap C$. This is where the dimension can decrease.

**Affine subspaces and facettes under polarity (scans 11–12).** The notes pair affine subspaces avoiding the origin with affine subspaces of the dual space. The paired dimensions sum to $n-1$. Incidence is expressed by reversal of inclusion and a formula for the image of a singleton. Scan 12 calls the affine span $E_F$ of a facette a « variété d’appui ». Its theorem specifies the corresponding facette of a polar sector by the affine subspace associated to $E_F$. Cor. 1 and 2 draw conclusions about finiteness and an order anti-isomorphism for polyhedra.

**Intervals in a combinatorial polyhedron (scans 12–13).** Corollaire 3 applies the anti-isomorphism to a « polyèdre combinatoire strict ». It states that the opposite ordered set and the specified intervals have the same property. The short argument starts with an interval at a least element, uses duality at a greatest element, then applies the result inside another interval. Small glosses identify both endpoints.

**Dimension on the ordered set of facettes (scans 13–14).** A cancelled Cor. 4 asks for an incident facette in a prescribed dimension. Its cancelled proof continues at the top of scan 14. The surviving Cor. 4 identifies a successor by a dimension increase of one. It reduces necessity to a polyhedron with no intervening facette between its interior and the empty facette. In Cor. 5 the dimension function is characterized by its change at successors and by $d(\varnothing)=-1$.

## Statements left without proof

| Scans | Passage | Extent of the argument on these sheets |
|---|---|---|
| 3 | « stabilité par intersection », « Stabilité par images inv et directes », and the line test ending « un intervalle de ladite » | These properties and the barycentric and simplex descriptions are listed without derivations. |
| 3 | a) $\mathring C\ne\varnothing$, b) « Si … alors », and c) « ∃ homéom. unique » | The three interior and ray assertions have no proof here. There is a crossed qualification beside b). |
| 4 | « est une relation d’équivalence » and « Point extrémal » | The equivalence relation and the line criterion for a singleton facette are asserted. |
| 4 | ① « ∃! facette de dim d », ② « est une réunion de facettes », ③ « conditions équivalentes » | No proofs are given for these assertions about dimension, affine spans, closures or the ensuing pointwise order criterion. |
| 5 | ④ $F_x=\operatorname{Sup}F_{x_i}$, ⑤ « stable par sup finis », ⑥ « de la forme » $\overline F\cap C$ | The supremum formula, both union criteria, the relative closedness criterion and the final claim about infima are stated without proof. |
| 6 | ⑦ « l’enveloppe convexe de l’ens. de ses pts extrémaux », ⑧ « l’ens des facettes de C est fini » | Both assertions and the following characterization of compact polyhedra are presented without a derivation here. |
| 6–7 | « Th. 1 », « Le théorème est conséquence… », « Résulte du » | A chain of implications points from bipolarity through the half-space characterization to separation. The intermediate deductions and the two polar corollaries are not worked out. |
| 8 | « Il suffit de prouver que si F n’est pas un hyperplan… », « On montre alors que », « Dans les deux cas on gagne » | The quotient reduction is indicated. The dichotomy for the planar cone and the final choice of separating hyperplane are left to the reader. |
| 10 | « Récurrence », « Trivial si », « On gagne » | The cut by $H_0$ supplies the inductive step. The base cases and the passage from both extreme-point tests to the count are brief assertions. |
| 11 | « on trouve des correspondances 1-1 », « Correspondance biunivoque », « Correspondance caractérisée par les propriétés » | The sector correspondence is stated after the proof on the preceding pages. The affine-subspace correspondence, dimension identity and characterization have no separate proof here. |
| 12 | « il existe une unique … application », « Cette application est bijective, et renverse la relation d’ordre » | The facet-duality theorem is stated. Cor. 1 gives a parenthetic instruction to apply duality. Cor. 2 states the anti-isomorphism. |
| 13 | « On sait que », « donc par dualité aussi » | The initial interval assertion is invoked. The other intervals are obtained from it. The later crossed corollary has a crossed, unfinished proof. |
| 14 | « la suffisance est claire », « La fonction … est caractérisée par les conditions » | Cor. 4 gives a reduction for necessity. Cor. 5 states the characterization and the final strict growth assertion without a further demonstration. |

## Questions and conjectures

None is explicitly posed. Scan 5 qualifies arbitrary suprema by « sous réserve que » followed by a dimension bound. On scan 3 the small crossed note appears to qualify the preceding formulas. Its uncertain wording and scope do not establish a separate conjecture.

## Slips

| ID | Scan and place | Reading, possible correction and reason |
|---|---|---|
| S3 | 3, b), lines 17–20 | The large signs are intersections. For the closed square with $x=(0,0)$, the interior point $(1/2,0)$ is absent from the vertical line through $x$. The boundary point $(1,0)$ is absent from it too. Thus the intersections cannot give the three sets as displayed. **High** confidence in this counterexample. Taking the union of the line sections is a plausible intended operation (S3r). The crossed marginal qualification has low reading confidence. |
| S5 | 5, ⑤, line 10 | The display has Fac(E) where the preceding definition uses Fac(C). For $E=\mathbb R$ and $C=[0,1]$, the singleton $\{0\}$ is a facette of $C$ by the line criterion on scan 4, but 0 is interior to the ambient line. Fac(C) is the likely intended set. **High** confidence. |
| S6 | 6, Th. 1, line 15 | « Pour $A\in E$ » appears to require $A\subset E$. The polar definition quantifies over the elements of $A$. An interval in the real line is a permitted input there. **High** confidence. |
| S7a, S7b | 7, first Cor, lines 4–5 | The first closed hull is missing the polar that would equate it to the intersection of the polars (S7ar). In the second line, the hull arguments appear to need polar signs (S7br). Set $A_1=A_2=[-2,2]$. The polar is $[-1/2,1/2]$, so either equality as written places 1 on only one side. **High** confidence for the first equality. **Low** confidence for an error claim about the second as a whole, since the operator name itself is marked. |
| S10 | 10, end of a) ⇒ b), line 7 | « b) pour E » appears to refer to condition b) for $C$. The proposition on scan 8 introduces $C$ as its subject and $E$ as its ambient space. **High** confidence. |
| S12a, S12b | 12, theorem, lines 8–10 | Each parenthesis uses membership in the affine span, after a condition excluding the origin from the closure. Consider an endpoint of $[-1,1]$: its affine span and its closure both consist of that endpoint. Both exclude 0. The same test works with the other endpoint in the dual line. A slashed membership is the likely intended sign in each parenthesis (S12ar, S12br). **High** confidence. |

**Reading questions.** On scan 13, b), the frozen lower comparison offers $<$ and $\leq$. The upper bound and the use of least elements favour the inclusive alternative, but a cancelled line overlaps the lower comparison. Confidence in calling this a slip is **low**. On scan 14, near the end of Cor. 4, the frozen comparison before « 0 ou −1 » offers $\leq$ and $=$. The upper stroke is slanted. The wording favours listing two dimensions. Confidence in a claim about the intended sign is **low**. The endings of *strict* on scan 13 and *croissant* on scan 14 were reread at the word edge. Their remaining marks permit no attribution of an agreement slip.

## Pointers

- **Scan 7.** « Théorème 1″ (Hahn-Banach) » is the sole named external attribution on these pages.
- **Scans 7–10.** « Résulte du » links the half-space assertion to separation. « lemme ci-dessous » on scan 9 points forward to the finite-extreme-point lemma on scan 10. The converse argument on scan 10 refers back with « d’après ce qui précède ».
- **Scans 12–14.** « appliquer dualité », « Résulte du Cor. 2 », « Appliquant ce dernier résultat » and « du cor. 4 » are internal references. No other cote, paper title, date or bibliographic reference is given.

## Remarks of the model

- **R3, model remark, medium confidence.** Replacing the common intersection signs by unions accounts for the missing points in the square example. This local test does not establish the full scope of the three identities or the author’s crossed qualification.
- **R11, model remark, medium confidence.** The margins of scan 11 and the formula on scan 12 give a way to read the exponent on affine subspaces across the page turn. Its top is open in those places. The polar on a set and the filled dot on $H(x)$ have different shapes. The character choice for the open mark stays doubtful.
- **R14, model remark, high confidence.** The segment gives a small check on both conditions in Cor. 5. Its empty face has rank −1, its two endpoint faces have rank 0, and its one-dimensional face has rank 1. Each of its four successor pairs increases the rank by one. This checks the stated normalization and increment in that example.
