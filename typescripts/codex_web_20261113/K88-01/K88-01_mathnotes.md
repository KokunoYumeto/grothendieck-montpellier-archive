# K88-01 · Mathematical notes

The two runs concern different constructions. The first ends with the order of a permutation. The second starts afresh with « Théorème (à prouver) ». Scan numbers below are PDF scan numbers. Each quotation is local to the indicated sheet. The check identifiers refer to CHECK_EVENTS.tsv.

## What the pages do

**The root-system functor (scan 3).** A root system gives data $(W,R,I,\varphi)$ with $R$ a torsor for $W$ and $I$ finite. Equivariance, a system of generators indexed by $I$, involution and pair-product relations, and a Dynkin diagram are written on the right. At the left the author sends a frame to an admissible set of generators. He relates the possible failure of injectivity to the centre of $W$.

**Automorphisms (scans 3–5).** To answer the question about the functor, the author compares the automorphism groups of $\Sigma$ and $\Phi(\Sigma)$. He writes $\alpha(w)=(\operatorname{int}(w),w_R,\operatorname{id}_I)$, chooses a point $r_0$ and computes the form of an automorphism that fixes $I$. Two exact rows compare the actions on $I$. The middle vertical arrow is the desired comparison. The calculation of $u_R$ has a finite check under M4 below.

**Parabolics, facets and frames (scans 5–7).** The lower part of scan 5 passes from parabolic subsets of roots to closed facets of the hyperplane system in the dual space. Reversing inclusion gives strict flags. Scan 6 describes the resulting simplicial object as a triangulation of $S^{l-1}$ and identifies its frames with a product of $R$ and the total orderings of $I$. The adjective qualifying one class of parabolics on 6 remains doubtful.

**The operations on frames (scans 7–9).** Most of the $\sigma$'s change the ordering by a transposition. The distinguished last operation changes the point in $R$. The sheet examines squares, commutation of distant operations and an adjacent product. Writing $a=\varphi(r,u(l-1))$ and $b=\varphi(r,u(l))$ gives even iterates with first coordinate $(ab)^nr$ and odd ones with first coordinate $(ab)^nar$. The second coordinate alternates. Scan 9 gives the order as twice the least common multiple of the $n_{ij}$ for distinct indices. M1 and M2 concern the algebraic ordering and an explicit finite example.

**Proposed theorem on standard maps (scans 11–12).** Items 1–3 concern completeness and regularity of a nonempty simply connected cellular map, classification by vertex and face orders $(p,q)$, the pinned map $C_{p,q}$, and its automorphism group as a quotient of a cartographic group. The written exception involving an order of 1 is partly ambiguous. Item 4 describes the universal cover of a complete connected quasi-regular map, its fundamental group as a subgroup, and the mixed fundamental group attached to the automorphism action in the regular pinned case.

**The metric realization (scans 12–14).** Item 5 introduces a homogeneous simply connected Riemannian surface and lists three models. For a cellular map on such a surface the open edges are to be geodesic arcs. Metric regularity requires the isometric automorphisms of the map to act transitively on frames. The author sets out an existence assertion, uniqueness of the similarity in an isotopy class, and a proper-action assertion in the small writing on 14. Normalization fixes the model metric in two cases and fixes edge length in the Euclidean case. The proposed corollary gives an equivalence on forgetting the metric.

**The list of types (scans 14–15).** Pinning is linked to canonical identification of the ambient models. Item 6 lists the spherical, Euclidean and hyperbolic types. The five finite pairs are individually aligned with tétraèdre, cube, octaèdre, dodécaèdre and icosaèdre. The Euclidean list includes two raised pairs involving infinity and the three named tilings. Conditions on $\Gamma_{pq}$ accompany the numerical tests. The product order and the range of those tests matter (M3).

**Quotients and outstanding work (scans 15–16).** Item 7 constructs pinned quasi-regular maps as quotients by subgroups acting freely on the ambient model. Regularity is related to invariance of the subgroup. The slanted margin warns about new finite-order vertices in a quotient if one order is infinite. The author asks for point stabilizers and returns to the complex structure in the oriented case. The compact case leads to a projective algebraic curve and a closing assertion about its metric.

## Statements left without proof

| ID | Scan | Author's words and scope |
|---|---|---|
| U1 | 3 | « Or ce stabilisateur est évidemment le centre de W ». The identification is asserted in the discussion of the admissible generators. |
| U2 | 5–6 | « correspondent ... par ... polarité aux facettes ... fermées » and « il s'agit manifestement d'une triangulation de la sphère ». The correspondence and topological identification are described without a proof here. |
| U3 | 11, item 1 | « Toute carte cellulaire ... quasi régulière ... est régulière, et elle est complète ... sauf dans le cas d'une carte isomorphe à » $(\mathbb R^2\supset\mathbb R)$. The heading explicitly calls for proof. |
| U4 | 11, items 2–3 | « est déterminée, à isomorphisme près, par ... le couple $(p,q)$ ». The text also gives the allowable orders, a pinned object determined up to unique isomorphism, and the displayed group quotient by $(\rho_s^p,\rho_f^q)$. |
| U5 | 11–12, item 4 | « Alors le revêtement universel ... est ... une carte standart »; the continuation says the fundamental group « s'identifie à un sous-groupe » and the mixed group « s'identifie à » $\Gamma_{p,q}$. |
| U6 | 12–13, item 5 | « On sait alors que, à un facteur constant près sur la métrique, E est isomorphe à un des trois espaces ». The list follows. The normalization for cases 1° and 3° uses the assertion « les similitudes sont des isométries ». |
| U7 | 13–14, a–c | « il existe ... une carte géodésique standard ... (topologiquement) isomorphe »; « il y a un isomorphisme topologique unique qui soit une ... similitude »; the automorphism group « opère proprement sur X » and is called a discrete subgroup of $\operatorname{Aut}(X,g)$. |
| U8 | 14–15 | The forgetful functor « est une équivalence de catégories ». The next NB says that the ambient surfaces of a pinned normalized geodesic map identify « canoniquement » with its model; the verb at the page break is uncertain. |
| U9 | 15, item 6 | « sphérique ... exactement dans les cas suivants », « est euclidien exactement dans les cas suivants », « est hyperbolique dans les autres cas ». Finiteness, infinite solvability, and a free subgroup on two generators occur in the accompanying group tests. The classification is listed here. |
| U10 | 15–16, item 7 | « s'obtiennent ... à partir des sous-groupes » acting « librement »; « Elle est régulière sss le sous-groupe ... est invariant ». The canonical quotient metric and the criterion are asserted. |
| U11 | 16, last NB | « muni canoniquement d'une structure complexe », « dans le cas compact ... une courbe algébrique projective » and « métrique est celle de Bergman ». The line before the closing metric statement contains a very doubtful exclamation. |

## Questions and conjectures

- **Q1 (scans 3–5).** « Le foncteur précédent est-il une équivalence de catégories ? » and « est-il pl. fidèle ? » The automorphism argument on the next two sheets ends with « cqfd. ».
- **Q2 (scans 11–14).** « Théorème (à prouver) » introduces the second run. « Ceci posé, on doit avoir ceci » (scan 13) introduces the metric realization statements. A doubtful ?-shaped correction follows the definition above them.
- **Q3 (scan 16).** « attention au cas où p ou q est infini ! » The marginal possibility is « création de nouveaux sommets comb. d'ordre fini ». The adjacent note asks to « Donner encore th. d'équiv. de cat. ».
- **Q4 (scan 16).** « pour déterminer les π possibles, d'étudier ... l'op. de Γ » and « de trouver les ... stabilisateurs ... des pts ». These are tasks for the classification of free actions.

## Slips

| ID and confidence | Scan and wording | Possible correction and reason |
|---|---|---|
| S1 · high | 7, « σ₀,…,σ_l » followed by the enumeration ending at $\sigma_{l-1}$ | If the two lists denote the same operators, the last index of the first list should be $l-1$. |
| S2 · low for the disputed subscript; high for the endpoint calculation | 7, upper formula for order transpositions and the later range $0\le i\le l-2$ in the cubic relation | For the ordinary adjacent-transposition argument take $i\le l-3$ in that relation. At $i=l-2$ the pair $\tau_{i+1},\tau_{i+2}$ includes $\tau_l$, which would exchange positions $l$ and $l+1$ in an ordering of [1,l]. The earlier single-transposition formula extends one index into the exceptional case. |
| S3 · high for the reversal | 7, product used to form π; 9, last display | For the same operator, repeat $\sigma_{l-1}\sigma_{l-2}$ on 9. The displayed product there is in the opposite order. M1 explains how the order can still agree. |
| S4 · low | 8, lower first bracketed exponent and the following exponent | The written pair of second coordinates suggests $2n+2$ and $2n+3$ respectively. The exponents themselves are difficult and the reasoning cannot settle their ink. |
| S5 · low | 8, margin, « u ... ≡0 » (u, i or n) | Read i for the exponent of π if referring back to $i=2n$ in the main condition. The main and marginal letters are not equally clear. |
| S6 · high | 9, « Ordre de π = σ…σ… = 2ν » | Place « ordre de » around the product if the last member is to equal a number. A product of permutations stands between the two equals signs as written. |
| S7 · conditional, high for the specific counterexample | 15, $p+q\ge10$ and the neighbouring alternative | As standalone hyperbolicity tests these need the earlier restrictions. For example $(2,8)$ passes both sum tests but is explicitly included in the spherical family. The page may carry the exclusion forward implicitly (M3). |
| S8 · high for the spelling on 13; low for the ending on 14 | 4, « son image est formé »; 13, « répères »; 14, « surfaces ambiantes s'identifie- » | Ordinary agreement gives formée and s'identifient; the usual word is repères. The two accents on the first occurrence on 13 are visible. The terminal stroke on 14 is doubtful. |

## Pointers

| Scan | Words | Referent on these sheets |
|---|---|---|
| 3, 5–6 | « diagramme de Dynkin », « groupe de Weyl épinglé », « Borels » | Named mathematical objects. No publication is cited alongside them. |
| 4 | « par a) » | The equivariance axiom on scan 3. |
| 11 | « groupe cartographique » (the abbreviation is uncertain) | The group in the quotient defining $\Gamma_{p,q}$. |
| 12 | « demi-plan de Poincaré » | The third Riemannian model. |
| 13 | « cf. 1° » | A numbered cross-reference in the completeness insertion. |
| 14 | « cf plus bas » | Points forward in the discussion of the Euclidean case. |
| 16 | « métrique est celle de Bergman » | A named metric in the last line, transcribed as read. |

No explicit cote number, named paper, date or bibliographic reference is given in these passages.

## Remarks of the model

**M1 (model, high; scans 7 and 9).** Reversing two involutions replaces their product by its inverse. This follows directly from $(st)^{-1}=t^{-1}s^{-1}=ts$. Thus the reversal matters for the operator, though the two orders agree. In the two-generator example checked under M2, the two products differ on all 12 frames and both have order 6.

**M2 (model, high for this finite example; scans 7–9).** Using the six permutations of three objects for $R=W$, the adjacent transpositions $(12),(23)$ for the generators, and both orderings, I iterated the distinguished product on all 12 frames. For $n=0,\ldots,6$, its even and odd outputs matched the two stated coordinate formulas in all 168 comparisons. This checks an instance of the recurrence. The order of the basic generator product is 3, giving the displayed factor of two in this example.

**M3 (model, high for the stated arithmetic; scan 15).** For $p,q$ between 3 and 20 inclusive, all 324 pairs give the same answer under the three written tests: the product-order cases, the sum-at-least-10 cases including $(4,5),(5,4)$, and the sum-at-least-9 cases with $(3,6),(6,3)$ excluded. At $(2,8)$ the product-order test is false and both sum tests are true. This identifies the role of the preceding cases without deciding the writer's intended scope.

**M4 (model, high; scans 4–5).** In the reduction of $u_R$, the adjacent factors $a^{-1}a$ cancel in $(awa^{-1})(ar_0)$. I also checked the resulting equality on all 216 triples $(a,w,r_0)$ of permutations of three objects. This addresses only that step of the automorphism argument.

**M5 (model, low; scan 11, item 2).** The condition on the order-one exceptions may have been meant symmetrically. The witness check left the first second-coordinate letter ambiguous, and the qualifier « si $p\ne2$ » is on the insertion. Scan 15 includes finite types with one order 2 and the other starting at 1; it suggests the question without resolving the syntax or the ink.
