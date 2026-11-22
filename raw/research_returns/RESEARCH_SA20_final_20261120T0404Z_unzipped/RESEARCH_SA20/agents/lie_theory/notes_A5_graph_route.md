# Pending graph-fibre recognition route

Written 2026-11-19 during checkpoint07 freeze. Not yet a checked result.

## Intended statement

For every continuous definably proper map with all fibres of dimension at most one, over any real closed field, the maximal open definable-manifold local-triviality locus is definable. More generally the part of that locus whose fibres have dimension at most one is definable for an arbitrary proper map, by restricting to the interior of the definable fibre-dimension-at-most-one set.

## Complete regularity and finite canonical formats

Define CR(y): for every epsilon>0, there is delta>0 such that every nearby fibre F_z has a definable homeomorphism h:F_y→F_z with sup_x ||h(x)-x||<epsilon. This is not initially a first-order definition.

Use Hardt and triangulation of representative fibres to give finite formula families of graph parameterizations. Coalesce bivalent subdivisions. Intrinsic vertices have valence unequal to two; components with no such vertex are circles. A graph homeomorphism is a finite intrinsic graph isomorphism, followed by increasing reparameterizations of edges and rotations/reflections of circle components.

For an oriented arc gamma, use L1 length: sum of the total variations of its ambient coordinate functions. It is definable. In a fixed definable family every coordinate of every intrinsic edge (and every cut circle) has a uniform finite bound N on its number of monotonicity intervals. Variation on a subarc is the maximum of sums over at most N+1 partition points, a first-order formula over a compact simplex.

If h is epsilon-close, transport the target coordinates along h to the source arc. Both coordinate functions have at most N monotonicity intervals. Refining their breaks gives at most 2N+2 intervals; each endpoint difference is at most epsilon. Thus prefix L1 lengths differ by at most C epsilon, C=4n(N+1). Total lengths satisfy the same bound. Replace h on an edge by the homeomorphism linear in normalized L1 arc length. At any point its target length parameter differs from the h-image parameter by at most 2C epsilon; since ambient distance is at most L1 arc length, the replacement is (1+2C)epsilon-close.

On each circle, choose a fixed source base point and allow its image as a parameter; the same replacement is a normalized L1 circle isometry. All canonical replacements form finitely many first-order formula formats, with variable circle image points. Hence CR is definable by quantifying only these formats. This does not use an unproved uniform-complexity theorem for arbitrary homeomorphisms.

## CR interior should be the bundle locus

Necessity follows by uniform continuity of a local product chart over its compact fibre. Sufficiency will be proved constructively, without relying on Dyer-Hamstrom over ordinary real fields.

Fix F_0 and a neighbourhood contained in Int(CR). CR at 0 identifies every nearby fibre with F_0 by arbitrarily small canonical maps. Their circle components can be labelled by disjoint fixed ambient tubular neighbourhoods of the reference components. Intrinsic vertices/edges match by smallness; no continuously chosen Hardt parameterization is assumed across its artificial boundaries.

The finite canonical automorphism group of a graph with one marked point on each circle has positive minimum displacement among nonidentity members. Thus, once continuous circle anchors are supplied, there is a unique sufficiently small anchored canonical map F_0→F_y. Its existence follows from CR and the replacement estimate; its uniqueness follows because the ratio of two such maps is a nontrivial canonical self-map, which cannot move every point less than twice the chosen displacement threshold.

To prove continuity at any y, choose a small canonical comparison k:F_y→F_z supplied by CR(y). On each circle rotate k by the small intrinsic amount needed to carry the anchor at y to the anchor at z. This remains small. Composing k with the selected F_0→F_y map is an anchored canonical map and remains under the displacement threshold for z near y. Uniqueness makes it the selected map at z. This proves uniform, hence joint, continuity. The inverse follows from relative properness and compactness, or directly from the same comparisons.

## Circle anchors via a definable strictly convex optimization

For the circle component C_y let L_y be its L1 length and d_y its shorter-arc L1 metric. CR and the replacement estimate imply continuity of L_y and joint continuity of d_y on the fibre-pair family. Indeed a canonical small comparison is an exact isometry after multiplying lengths by L_z/L_y.

Choose a C1 regular point p on C_0. The ratio d_0(p,z)/||z-p|| is bounded: locally choose a coordinate with nonzero tangent derivative; away from p use compactness. For a sufficiently large fixed M define

    E_y(x) = max_{z in C_y} [ d_y(x,z)^2 - M ||z-p||^2 ].

This is definable using maxima on compact fibres. Choose M larger than the squared ratio bound. Then E_0(p)=0 and E_0(x)≥d_0(x,p)^2, so p is the unique global minimizer. Under small canonical comparisons, E_y converges uniformly to E_0. Thus every minimizer is in a short intrinsic arc J_y near p.

Choose a slightly larger short arc I_0 around p, of radius less than L_0/8. Points outside I_0 have ambient distance from p at least m>0. Increase M so that their contribution is uniformly negative, while a point close to p contributes a value near zero. For nearby y all maximizers defining E_y on J_y therefore lie in I_y, the corresponding short arc. For x,z in those arcs there is no circle wrap-around, so with intrinsic coordinates u,v:

    E_y(u)=u^2 + max_z[-2uv+v^2-M||z-p||^2].

The second summand is convex; hence E_y is strictly convex on J_y. Every global minimizer lies there, so it is unique. Call it s(y). Compactness, CR continuity of the energies, and uniqueness imply continuity of s at every y of the chosen CR-open neighbourhood. This argument uses only definable maxima/minima and finite variation, not integration or ordinary sequential compactness.

## Items still to audit in the full writeup

1. First-order formula family of all canonical graph maps, including loops and circle component permutations.
2. Uniform variation estimate with possibly nonmonotone ambient embeddings and source/target graph parameterizations.
3. Circle-energy exclusion of far maximizers on the entire short minimizer arc, ensuring strict convexity.
4. Definable continuity of metric and energy families over arbitrary real closed fields, using epsilon-delta comparisons or curve selection rather than ordinary compactness.
5. Properness and the empty-fibre case; final locus Int(CR) inside the chosen definable manifold base.

The classical Dyer-Hamstrom graph-fibre theorem is supportive context only; this route must supply the definable construction above in full.
