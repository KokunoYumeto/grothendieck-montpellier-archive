# Targeted audit of the general topology arguments

**Date:** 19 November 2026. **Reviewer:** GPT-6 Astra (OpenAI), inherited effort, subrun `/root/counts`. This is a targeted proof check, not an assertion of independent priority.

## Verdict

The marked puncture/blow-up argument E4 in `sections/A2.tex` passes the targeted audit, conditional on the stated rank-three pseudoline scope and the actual contraction map `Pi_g`. I opened and checked the relevant source text in Sturmfels–Ziegler (1993), Lemma 3.2 (p. 29), Lemma 4.1 and Proposition 4.2 (pp. 37–38), and Corollary 4.5 (p. 40). In particular, the restricted-fiber argument used by E3 and E4 is valid; it is stronger than restricting an arbitrary homotopy equivalence, and the proof correctly uses that stronger property.

The remaining ordinary-vertex four-cycle argument has a complete route, but the local packet convention must be stated accurately. The chosen G packet reverses its endpoint labels when it becomes S. The selected reflection gluing exchanges chord names and thereby preserves its *spatial sides*. New transition opportunities can arise at the opposite, disappearing G packet, which lies outside the chosen inertia gap. Saying only that the opposite packet changes would be inaccurate without distinguishing label order from the appearance of transition arcs.

I found no counterexample to the general four-cycle claim. The proof needs the lens lemma below to exclude the only exceptional ordinary GG configuration. Multiple intersections do not obstruct that lemma or the commuting-resolution argument.

## 1. Why E4's restricted-fiber step works

Let `f:P→Q` satisfy the two hypotheses of Sturmfels–Ziegler Lemma 3.2:

1. Every point fiber `f^{-1}(q)` is contractible.
2. For `f(p)<q`, the slice `f^{-1}(q)∩P_{≥p}` is contractible.

For an arbitrary subposet `Q'⊂Q`, set `P'=f^{-1}(Q')`. If `q∈Q'`, its point fiber in `P'` is exactly its old point fiber. If `p∈P'`, the corresponding slice in `P'` is exactly its old slice. Thus the same criterion applies to the restricted map `P'→Q'`. No order-convexity assumption on `Q'` is required.

Proposition 4.2 explicitly proves both hypotheses for the contraction map `Pi_g`, under Euclideanness of every program `(M∪f,g,f)`. Rank three supplies precisely this hypothesis. Its extra fibers at `g+` and `g−` are singletons, and the upper slices from either tip are the singletons supplied by `kappa_±` in Lemma 4.1.

This justifies the contractibility of every full inverse-image meridian `A_rho` and sector `R_gamma` used in E4.

## 2. E4 local marked geometry

The following points are all needed and are correctly available.

- A parallel localization `[h]` is minimal in `P`, and its strict upper interval is the actual rank-two extension circle. Therefore its open star in the *whole* order complex is an actual open two-disk; this is not merely a homotopy statement about a link.
- For `h≠g`, the image is the parallel rank-two localization `rho` at `v=g∩h`. In the link at `[h]`, evaluation at the cocircuit for `v` has exactly two zeros. Those two points form the meridian link; the two intervening arcs form the adjacent sector links. Thus `[h]` has a local interval neighborhood in the meridian and a local half-disk neighborhood in each of the two sectors.
- At `[g±]`, the meridian link is a singleton, and the sector link is a closed interval. Hence these are genuine meridian endpoints and genuine boundary points of sectors.
- Multiple old lines through `v` simply give several separate marked points on the same meridian. They do not create a branch in the local link at any of those marked points.
- Rank three implies every old line has at least two distinct old vertices. Indeed, if all other lines meet an old line only at `v`, every old line passes through `v`. Thus the choice of `w≠v` in E4 is always possible, including near-pencil arrangements.

The evaluation `e_w` has zero set exactly `{[h]}` inside `A_rho`: an ordinary added pseudoline cannot pass through two distinct vertices `v,w` of the same old line, and no other old parallel point in the meridian can vanish at both. Since its values at the two tips have opposite signs, every marked point separates the tips.

## 3. E4 cutting and gluing facts

The meridian cut lemma is valid. For a contractible finite polyhedron `A`, remove an open interval whose midpoint has a genuine interval neighborhood. If the point separates the specified tips, the complement `Y` has exactly two components. Restoring the interval attaches one one-cell between these components. Equivalently, the exact sequence of `(A,Y)` gives `H_0(Y)=Z²` and zero reduced positive homology in each component. Van Kampen expresses `pi_1(A)` as the free product of the component groups, so each group is trivial. Simply connected acyclic CW complexes are contractible by Hurewicz and Whitehead. The separating marks therefore occur in a linear order between the tips, even if the rest of the meridian has higher-dimensional contractible pieces.

Deleting a sufficiently small boundary half-disk from a sector preserves its homotopy type: the deleted closed half-disk deformation retracts onto its frontier semicircle, fixing that semicircle. Use small PL cuts in the actual stars, so every complement and intersection remains a finite subpolyhedron. This supplies the cofibration hypothesis explicitly.

After the two tip neighborhoods are removed, nonadjacent sectors are disjoint and there are no triple intersections. Adjacent intersections are precisely the cut meridian components. There are at least four sectors in the oriented rank-two circle, because the contraction has rank two and therefore at least two unoriented directions. Thus no exceptional two-edge circle case needs separate handling.

The map constructed sector by sector is a homotopy equivalence on every sector and every intersection component, and matches boundary circles homeomorphically. The finite cofibration gluing argument is legitimate. An induction around the cycle of sectors uses the disjoint union of the already present meridian components as the attaching subspace. At the last sector, it attaches along both neighboring meridians; this remains a cofibration pushout.

The quotient argument also works although the punctured oriented cover is not simply connected. The exact sequence

`1 → pi_1(oriented complement) → pi_1(quotient complement) → C_2 → 1`

is natural for the equivariant map. Its left map is an isomorphism, and its right map is the identity on the deck group; hence the middle map is an isomorphism. Higher homotopy groups are handled by covering-space lifting, followed by CW Whitehead. The boundary homeomorphisms and cofibrations are sufficient for subsequent Möbius-band attachment. If “homotopy equivalence of pairs” is meant in the strict category-of-pairs sense, cite relative CW Whitehead or note that an absolute equivalence with boundary homeomorphism between cofibrant pairs yields that relative equivalence. The attachment conclusion already follows from the stated homotopy-pushout argument.

## 4. Correct local ordinary-corner normal form

Fix a non-supercritical `D`, and let `A,B` be consecutive G ports at *distinct* old vertices `v,w`. Their incident old-line sets are disjoint, since an old line cannot meet `D` twice. Choose disjoint sufficiently small disks about `v,w`, meeting no other old lines.

Resolve `v` through the side represented by `A`. In the cut disk, the selected packet becomes the empty S fan at `v`; its endpoint label order reverses. The opposite G packet disappears. The reflection gluing of scan 39 exchanges the endpoint chord names, so the two spatial sides of the selected interval are the same on the two polygons. This is the side identification that the corner proof must use.

Why does the adjacent inertia gap survive? A newly possible specialization fan has to involve an endpoint whose old G constraint disappeared, because all other boundary endpoints and all old chord intersections outside the small disk remain unchanged. At the selected packet, the newly interior vertex `v` is the first intersection on each incident chord. Hence the only specialization fan using those endpoints is the selected S fan itself; no new fan can interrupt the adjacent inertia gap. Other new fans can only arise at the opposite packet. That opposite packet is outside the chosen gap: the other zero vertex `w` supplies one G packet in each half of the boundary between the two packets over `v`. The same applies with `A,B` reversed.

Consequently the two local resolutions preserve the chosen gap in both orders. They commute because their support disks and old-line classes are disjoint. The circuit is exactly

`D → D_v → D_vw → D_w → D`.

Its four labels are distinct: their zero sets are respectively `Z`, `Z\{v}`, `Z\{v,w}`, `Z\{w}`. The four corners are GG, SG, SS, GS. This is a complete local proof of the four-cycle once the side convention is fixed.

## 5. Why every all-ordinary circuit reaches that normal form

Every transition changes the number of old zero vertices by one. On a finite closed circuit consisting entirely of ordinary transitions, choose a corner whose face label has maximal zero count. Its two incident transitions must both be generizations, so it is a GG corner.

If the two G ports come from the same old vertex, they are the two opposite packets over that vertex. Any second zero vertex contributes a G packet in each complementary half of the boundary and prevents adjacency. Thus the same-vertex possibility requires `nu=1`.

The lens lemma in the next section rules out this last possibility after exceptional intervals have been inserted. Therefore the circuit reaches a GG corner at two distinct vertices, and the preceding four-step normal form determines the whole orbit. This maximum argument does not require the ordinary transition graph to be a surface or to be planar in advance.

## 6. Complete lens lemma route, including multiple intersections

Suppose `D` passes through exactly one old vertex `v`. Let `C` be the old lines through `v`; in the cut disk they are a disjoint parallel class. Fix one of the two boundary half-arcs `P` between the opposite G packets. Let `g∈C` be the outermost chord facing `P`, and let `U` be the closed disk bounded by `g` and `P` (with endpoints moved slightly off the G packets if needed).

Every old line outside `C` meets `U` in one arc running from `P` to `g`: its two boundary endpoints lie on the opposite boundary half-arcs, and it crosses every member of `C` once. No member of `C` except the wall `g` lies inside `U`.

Orient each such arc from `P` toward `g`. These are exactly the directed edges in the positive affine sector of the rank-three oriented-matroid program with horizon `g` and objective `D`. In the `g`-affine chart, `D` is the zero-objective line, the chosen region is its positive side, and the arc heads toward positive infinity. No arc inside `U` is parallel to `D`, since its old line is not in `C`. Thus the graph on old vertices inside `U` has only directed edges. Rank-three Euclideanness gives no directed circuit (Sturmfels–Ziegler, definition of `G_f`, pp. 30–31; Corollary 4.5, p. 40).

If `U` contains any old vertex, its finite directed graph has a source. Along every strand through that source, there is no old vertex between the source and `P`. The endpoints of those strands on `P` are consecutive: an endpoint of another strand between the two extreme endpoints would have to leave the disk fan through an extreme incoming strand before reaching `g`, creating an earlier vertex on that incoming strand. Include every strand through the concurrent source. Their fan therefore gives an empty ordinary specialization triangle with base wholly on `P`, and none of its endpoints lies in a G packet.

It follows that if `P` contains no ordinary S port, then `U` contains no old vertex. This is precisely the empty exceptional corridor bounded by `D` and `g`; its E interval is inserted between the two G ports. Conversely an empty corridor forbids an ordinary specialization fan in that half: a fan apex inside the corridor is absent, and an apex outside it would require crossing the wall before reaching the apex. Hence a same-vertex GG corner cannot remain in the completed surface.

This proof uses a source vertex, not a generic double crossing. It therefore applies unchanged when the source has arbitrary multiplicity and when the original arrangement has near-pencil degeneracies. The program is nontrivial because `D` and `g` are distinct; its new objective is not a coloop because deleting it leaves the original rank-three arrangement.

## 7. Exceptional corners and the non-simple case

The exceptional local form should be stated as a separate lemma, rather than folded into the ordinary maximum argument.

For each old flag `(v,e⊂D_i)`, the four positions are the two stable near-`D_i` positions whose virtual intersection lies in `e`, and the two near-`D_i` semi-stable positions through `v`. The two ordinary moves resolve the whole concurrent fan at `v`; the two exceptional moves sweep across `D_i`. Shrinking the corridor produces the four-sector neighborhood.

All four labels are distinct even for a multiple vertex. The old line `D_i` has at least two distinct old vertices. There is also an old vertex off `D_i`, since otherwise all old lines would be concurrent. A sweep changes the signs at old vertices on `D_i` away from the contact, while leaving some nonzero off-`D_i` sign fixed; hence it cannot equal its starting extension, even modulo reorientation of the new element. Stable and semi-stable labels have different zero counts.

A stable exceptional interval is bordered by two ordinary S fans at the two endpoints of its original edge. They are distinct old vertices. Two different empty corridors cannot produce E intervals in the same inertia gap: both old wall lines would then contain those same two vertices. A semi-stable exceptional interval is bordered by the two G packets over its single vertex; the outermost parallel wall facing a given half-arc is unique. Thus no unaccounted E–E corner remains. This supplies the exhaustion step needed before asserting that every exceptional corner is one of the flagged four-cycles.

The total number of exceptional edges is consequently `sum_i(n_i+n_i)=2 sum_i n_i`: one stable sweep per old edge and one unstable sweep per old vertex on each old line. A projective old line with `n_i` distinct vertices has exactly `n_i` edges, including the case `n_i=2`.

## 8. Embeddings, connectedness, and orientation cautions

After the four-cycle proof, each vertex orbit has four distinct face labels by the ordinary zero-set argument or the exceptional flag argument. Edge interiors are paired exactly once, between distinct face labels. Therefore no two distinct points of one closed polygon become identified: interiors are untouched, edge interiors have just their one pairing, and polygon vertices have no same-face repetition in an equivalence class. This is the concrete no-zigzag verification required by SA10 A4.3.

Connectedness can be proved without assuming the surface classification: the full extension complex is connected; removing sufficiently small disks at its genuine two-dimensional parallel points cannot disconnect it, since paths through any such disk can be rerouted along its connected boundary circle. The ordinary extension incidence complex is a deformation retract of the punctured complex by retracting each residual collar onto its boundary. Its ordinary cover-relation graph is therefore connected, and so is the polygon adjacency graph.

Non-orientability still needs the explicit exceptional Möbius-neighborhood argument (or the independently proved orientation-character statement). Do not infer it from the numerical Euler formula alone. If the construction is presented by removing a supercritical face and identifying its boundary antipodally, the quotient of its boundary collar is a Möbius-band neighborhood, which proves non-orientability. The root must establish that this is the same exceptional pairing as the flag construction. The finite certificates already verify this orientation property for the five explicit test inputs but are not a proof for every arrangement.

## 9. Completing the general non-orientability argument

There is a direct completion of the caution in §8. Fix an old line `i` and temporarily leave its exceptional intervals unpaired, while applying all ordinary identifications. Choose the orientation of a nearby extension so that it lies above `[i+]`. This choice is unique on its unoriented class because there is an old vertex off `i`, and its localization has a prescribed nonzero sign there.

Lemma 4.1 identifies these nearby extensions with the actual rank-two circle `C=E(M/i)` by `kappa_+`. Its `2n_i` zero-dimensional and `2n_i` one-dimensional cells are exactly the stable and semi-stable nearby positions. Under an ordinary fan resolution at a vertex of `i`, the empty corridor with wall `i` stays that same corridor. The reflection endpoint rule preserves the two spatial sides, so the free exceptional interval at one nearby position joins at its ends to the free intervals at the two adjacent positions in this rank-two circle. Thus these free intervals form one boundary circle, with its incidence identified with the barycentric subdivision of `C`. They do not mix with intervals carrying another old-wall label.

The sweep across `i` changes the localization on cocircuits with zero `i`-coordinate and leaves the prescribed signs on the other cocircuits unchanged. In Lemma 4.1 notation it is exactly

`kappa_+(rho) → kappa_+(-rho)`.

Hence the actual exceptional interval pairing is the antipodal involution of this boundary circle. A collar before pairing is `S¹×[0,epsilon]`; after identifying `(z,0)~(-z,0)` its quotient is a Möbius band. This is the explicit equality between the flag pairing and the real blow-up collar operation needed for the general proof. It proves non-orientability without assuming the whole auxiliary X1 surface exists in advance. It also yields the correct edge count: `4n_i` interval incidences paired into `2n_i` exceptional edges.

The finite certificates corroborate the old-wall-label exhaustion: every exceptional vertex orbit in the six-line test has four exceptional interval incidences, all carrying the same old-line label, and there are exactly sixty such orbits. The general proof above rests on the rank-two circle and the local corridor persistence, not on extrapolating that computation.
