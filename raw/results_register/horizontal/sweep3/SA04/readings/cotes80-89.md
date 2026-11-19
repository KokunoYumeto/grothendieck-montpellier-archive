# Cotes 80, 82, 85-89 (combinatorial geometry) and cote 161 parts 1-4 and 6: the reading

- **Who:** Claude Opus 5.5 at effort max, reader R1 of the deep-sweep agent a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max), horizontal sweep 3, wave 1, topic SA04.
- **Date:** 19 Nov 2026.
- **The stretch, from the lead's message:** cotes 80 and 82-89 (Codex-web folders K80-*, K82-* to K89-*); the K161 folders not read before (K161-1 to -4 and K161-6); and the six divergent scans of cote 100, whose decisions are in `cotes94-102*`.
- **Cotes 83 and 84 are not SA04's:** all fourteen K83 folders are placed in SA01, and the twelve K84 folders in SA02 (K84-10 also in SA01), by the sweep-2 placements (`sweep2/SA01`, `sweep2/SA02`). Not read here.
- **How:** 45 Codex-web folders (24 for cotes 80-89, 21 for cote 161; about 990,000 characters of cleaned text) were read through a compact view of the lead's cleaned text, by my script `brief.py` (scratchpad): the first two to seven lines of every scan, cut at 95-120 characters, with a few pages in full. Every scan was seen at that depth, but much of every page was not read, and the counts and formulas checked below are the only checks. No scan image of these cotes was viewed. The Work and Codex math notes were not opened. This is a survey reading. A full reading of these folders needs about three times this budget; see DELIVERABLES.

## Cote 80: pseudoline systems (SA04-28), K80-01 to -04, scans 3-73

**How read.** Every scan, through the cleaned Codex-web text in a compact view (the first five to seven lines of each scan, cut at 115-120 characters), with the full text of 023. No scan image viewed.

**What he does.**
- **003-008:** classification of pseudoline systems. C(I), C_aff(I_0) and the stable classes; the passage from affine arrangements of n pseudolines to projective arrangements of n+1 with a marked line; the count card α^{-1}(ξ) = 2n/N(ξ), and 4n/N(ξ) for the pinned version; "n = 4, card C_aff(n) = 1"; "n = 5, card C_aff(n) = 6".
- **011:** a stray page on Stein arrows and base change.
- **017-019:** finite families of real hyperplanes as a stratification of the sphere indexed by an ordered set Σ ⊂ E = Π D_{H_i}, with the closure relation of strata.
- **021, 023, 025, 027, 029:** the "cas cruciaux" of 1-dimensional arrangements of N pseudolines:
  - with a bigonal pseudoline: I_N (a pencil of N−1 lines and a secant) and I_pq (two pencils and the line through their centres);
  - without one: II_pq (two alternating pencils), II_4 and II_5 (the simple arrangements of 4 and 5 lines), III_6 (the tetrahedral arrangement, a complete quadrangle) and IV_7 (a quadrilateral and its three diagonals);
  - the "latticial" case; a theorem and a lemma on reduction to these types.
- **032-040:** three pseudolines and the combinatorial cube and octahedron; the "gauche" (projective) cube and octahedron as quotients by the antipodism; orientations as wedge products of two-element sets ((6), (8), (15 bis)); the orientation of a 1-dimensional arrangement.
- **041-073:** reconstructing the map from the oriented 1-dimensional arrangement. A system of pseudolines is a map on the real projective plane whose vertices have even order ≥ 4. The permutations ρ_{D,s} satisfy axioms a)-f), and Th (071): if no pseudoline is a monogon or a bigon, the system of ρ_{D,s} is unique. 057 and 059 count faces ("25 triangles, 5 carrés, 1 pentagone"; 5 + 15 + 10 + 1 = 31). 073: automorphism groups of standard configurations of 1, 2 and 3 lines.

**Reused sheets (one line each).**
- 022, 024, 026, 030: his own German autobiographical typescript (on writing the autobiographical part in French, on remembering, on "das Verhältnis mit Hanka bis zu ihrem Tod"); SA04-29.
- 028: a Montpellier university administrative notice dated 13 May 1981. The folder is therefore written on sheets reused from 1981 or later.

**Checked.**
- The vertex counts in his margins for II_pq (pq + 2), II_4 (6), II_5 (10), III_6 (a complete quadrangle: 6 lines, 4 + 3 = 7 vertices) and IV_7 (a complete quadrilateral with its three diagonals: 7 lines, 6 + 3 = 9 vertices) are right (SA04-R80-01).
- For I_N as described (a pencil of N−1 ≥ 3 lines and one secant) there are N vertices, not the N+1 of the margin. The N−1 pencil lines are all bigonal, so his "(cas où la bigonale est unique)" fits I_pq, not I_N (SA04-K80-01). Whether the margin belongs to I_N is a reading question for the scan.

## Cote 82: rank-three quadratic modules, sl(2) and gp(1), SO(3) = GP(1) over a base (SA04-30), K82-01 to -05, scans 2-79

**How read.** Every scan, through the compact view (four lines per scan, 110 characters). No scan image viewed.

**What he does.**
- **"Algèbres de Lie de rang 3 associées aux formes bil. symétriques de rang 3" (002-032, "29 p").** For a rank-3 module E with a symmetric bilinear form φ and a basis ω of det E, he defines a Lie bracket [ , ]_φ through α': Λ²E' ≅ E. He gives:
  - the maps f: E → E' and f': E' → E with Cramer's formulas f'f = Δ·id, the discriminant δ(φ) = Δ ω^{⊗−2}, and the divided discriminant δ'(q) = −ω^{⊗−2} (in rank 2n or 2n+1, (−1)^n);
  - the example q = xy + z², which gives sl(2) and the isogeny SL(2) → GP(1);
  - the representation ρ_E of E' on E with trace zero; the Casimir forms;
  - characteristic 2: f has kernel O_S·H̃. Forms of sl(2), resp. gp(1), are equivalent to pairs (V, E), and give "fibrés en plans affines symplectiques".
- **034-056:** commutants and centralizers in End(V) for V of rank 2; "Est-il vrai que H est le centralisateur de 𝔥?". Proposition (043): G a form of GP(1), p an odd prime, μ a finite étale subgroup of rank p. Then the centralizer H is smooth, commutative and of relative dimension 1, with connected fibres in residue characteristic ≠ p; N/H ≅ {±1} acts by inversion. Also: quaternion algebras, the quadric Q = V(−det) ⊂ P^∨(M), special subalgebras and the isomorphism Dr(P) ≅ Div^+_2(X) (054), Jacobian subgroups (margin: "à vérifier ! il faut car. rés. ≠ 2").
- **"Dictionnaire lié à GP(1) ≅ SO(3)" (057-079):** equivalences between eleven fibred categories over S: torsors under GP(1), forms of GP(1), SL(2), gp(1) and sl(2), quaternion algebras, rank-3 quadratic modules (E, q, ω) with q ≅ xy + z², P^1-bundles, conic bundles in P², and others. Three of them, marked (*), are valid only over S − {2}. Typical representatives over Z are given; the functors run by twisting; Borel subgroups correspond to points of the P^1-bundle (077), with his question "suffit-il que L soit une sous-algèbre de Lie i.e. stable par crochet ??" (078).

**Checked (SA04-R82-01 to -03).**
- For q = xy + z² the Gram matrix of φ is [[0,1,0],[1,0,0],[0,0,2]]: det = −2, so δ(φ) = −2ω^{⊗2} and the divided discriminant is −1, as on 009 and 074.
- φ' with φ'(X,Y) = 2, φ'(H,H) = 1 gives [H̃, X̃] = 2X̃, [H̃, Ỹ] = −2Ỹ, [X̃, Ỹ] = H̃: sl(2). f'f = Δ id with Δ = −2 matches ff' = −2 id_𝔤 on 076.
- Proposition (043) is the standard fact that a cyclic subgroup of order p ≥ 3 of a form of PGL₂ lies in a unique maximal torus, its centralizer, whose normalizer has Weyl group Z/2. In residue characteristic p its elements are unipotent, whence the restriction to residue characteristic ≠ p.

**Open, his.** 078: whether every corank-one sub-Lie-algebra L of 𝔤 is the Lie algebra of a Borel subgroup. Over a base where 2 is not invertible this needs the quadratic condition (q | L^⊥) = 0 he states. Not settled here.

## Cote 85: regular 2-polyhedra, triangle groups in forms of GP(1), Schwarz systems (SA04-31), K85-01 to -07, scans 2-98

**How read.** Every scan, through the compact view (two or three lines per scan, 100-105 characters). No scan image viewed. This is the thinnest reading of the stretch: the cote holds eight dossiers with written page counts.

**What he does, dossier by dossier.**
- **002-011, projective representations of G_2 (the non-dihedral case).** Systems τ_0, τ_1, τ_2 of involutions with ρ_0 = τ_0τ_1 and ρ_1 = τ_1τ_2. The discrete category C'(ν_0, ν_1) of pairs (α_0, α_1) subject to an invertibility condition, and a theorem over a base S with a pinned regular 2-polyhedron ("On a un peu salopé la présentation, qui suppose pour le moins car. rés. ≠ 2"). Examples: (3, 3) gives S_4; (3, 5) gives Z/2 × A_5, with α_0 = −1 and α_1 = α, α² + α − 1 = 0.
- **012-022, "(10 p) Représentations projectives de G_1":** the infinite dihedral group, Lemma 1 on its subgroups N_i, the category of pairs (G, φ), Aut(G, φ) ≅ ₂(U_β), and the unique maximal torus containing u.
- **023-032, "(9 p) Invariants des sections des formes de GP(1)":** the invariant A(u), with A(j(λ)) = λ^n + λ^{−n} = G_n(λ + λ^{−1}), and deformation arguments over Artin rings.
- **033-041, "(8 p) Sous-groupes finis de GP(1)":** in characteristic 0, cyclic, dihedral, A_4, S_4 and A_5, with centralizers and normalizers; forms of D_n; a theorem on monomorphisms A_5 → G over a base.
- **042-057, "(14 p) Systèmes de Schwartz dans A_4, S_4, A_5, et classification":** triples (ρ, ρ', ρ'') with ρρ'ρ'' = 1 attached to the flags of a regular polyhedron. The tetrahedron has "24 = 12 + 12" systems (direct and indirect flags), and there are corollaries on the numerical types, e.g. the six orderings of (4, 3, 2) for S_4.
- **058-074, "(16 p) hyperpolygônes réguliers":** pairs of pseudo-reflections in a pinned plane, the invariants (λ_0, λ_1, β), elimination criteria, trigonometric formulas, and the cases (5, 3, 5), (3, 5, 5) and (5, 5, 5) ("À vérifier").
- **075-081, "(6 p) 2-Polyèdres réguliers finis en car. 0 (classification)":** invariants β_i = α_i + 2; finiteness forces the β_i algebraic; three cases I, II, II' through the fundamental group of the sphere minus three points.
- **082-094, "(12 p) Opérations sur systèmes de Schwartz":** Π_0 = ⟨h_0, h_1, h_2 | h_0h_1h_2 = 1⟩, with S_3 and γ = Ẑ^× acting, and semidirect products G_3 · γ(N).
- **095-098, "(3 p) Classes de sous-groupes de S_5":** subgroups matched with faces of a polyhedral figure.

**Checked (SA04-R85-01 to -03).**
- In example C, N(α + 2) = αᾱ + 2(α + ᾱ) + 4 = −1 − 2 + 4 = 1 for α² + α − 1 = 0, as he writes (011). So α + 2 is a unit of Z[(1+√5)/2], and no prime has to be inverted there. For an element of order ν, α = ζ + ζ^{−1}: −1 for ν = 3, a root of α² + α − 1 for ν = 5.
- G_n(λ + λ^{−1}) = λ^n + λ^{−n} defines the polynomials G_n (Chebyshev-Dickson) used for A(j(λ)) (028).
- The counts for the tetrahedron are right: 4 faces × 3 edges × 2 = 24 flags, of which 12 are direct. The finite groups he lists, [3,3] = S_4 and [3,5] = A_5 × Z/2 (009, 011), are the full symmetry groups of the tetrahedron and the icosahedron. In a form of PGL₂ the centre of A_5 × Z/2 acts trivially, since the finite subgroups of PGL₂(C) are cyclic, dihedral, A_4, S_4 and A_5 (033-041).

**Link (hunch H85-1).** The "Opérations sur systèmes de Schwartz" by S_3 and Ẑ^× (082-094) are the operations on regular maps and hypermaps later published by Jones and Thornton: duality and Petrie-type operations, outer automorphisms of the triangle group (G. A. Jones, J. S. Thornton, "Operations on maps, and outer automorphisms", J. Combin. Theory Ser. B 35 (1983), 93-103, locator to be checked). The relation to the dessins d'enfants of the Esquisse should be read on these pages.

## Cote 86: regular polyhedra, incidence geometries, the icosahedron (SA04-32), K86-01, -02, scans 2-33

**How read.** Every scan, through the compact view (three lines per scan). No scan image viewed.

**What he does.**
- **002-009:** combinatorial polyhedra as ordered sets Φ = S ⊔ A ⊔ F, where every face is the sup of its edges and every vertex the inf; the icosahedron "concrete model". The stabilizer of an axis is Z/2 × D_5, of order 20 = 120/6 (6 = 12/2).
- **010-017, "Géométries d'incidences et ensembles à opérateurs":** for a 2-dimensional incidence geometry Π = (S, A, F; R, R') the set of flags Rep(Π) is a set with three involutions σ_0, σ_1, σ_2. Thm: Π ↦ Rep(Π) is fully faithful. Cor: Aut(Π) = Aut(Rep(Π)) as G_2-set, and for Π finite, Card Aut(Π) divides Card Rep(Π). Π is regular iff Aut(Π) is transitive on flags; vertex stabilizers are D_p.
- **018-033, "Cours, Polyèdres réguliers III", the combinatorial icosahedron:**
  - the antipodism a, acting without fixed points;
  - orthogonal edges, the 15 directions, and the set T of 5 "trièdres distingués";
  - G^+ ≅ Alt_T (027);
  - the oriented icosahedron reconstructed from the oriented 5-set T (pentagons Pent^+(T, ω), edges A^+(T, ω));
  - the "icosaèdre gauche" (the hemi-icosahedron) described by a 5-element set (E, ω), with explicit σ_0, σ_1, σ_2: ρ_s = σ_2σ_1 is the 5-cycle and σ_0σ_1 a double transposition (033).

**Checked (SA04-R86-01, -02).**
- Counts: the icosahedron has 12 vertices, 30 edges, 20 faces and 120 flags, equal to the order of its full group A_5 × Z/2. An axis through two opposite vertices has stabilizer of order 120/6 = 20. The 30 edges give 15 directions, grouped into 5 orthogonal triples, and the rotation group acts on these 5 triples as A_5 = Alt_T.
- Card Aut(Π) | Card Rep(Π) holds because Aut(Π) acts freely on the flags of a connected incidence geometry.

## Cote 87: convex polyhedra (SA04-33), K87-01 to -03, scans 3-41

**How read.** Every scan, through the compact view (three lines per scan). No scan image viewed.

**What he does.** "Géométrie des convexes":
- convex sets, hulls and facets, through the equivalence relation R(x, y);
- Fac(C) and its sups, Krein-Milman for compact convex sets of finite dimension, polyhedral parts;
- polarity A ↦ A° reversing inclusion; polyhedral sectors (a finitely generated cone is a finite intersection of half-spaces, and conversely), supporting varieties; polarity as an anti-isomorphism of the face posets (Cor. 3); the dimension function (Cor. 6: every face has faces of every lower dimension);
- an intrinsic characterization of the n-cube by a set of affine subspaces, and the cube over a ring k with 2 invertible (022-023);
- the combinatorial polyhedron of a convex polyhedron; an exercise on partial sections of B → I (026);
- finite ordered sets with the property (Σ) (029-041): for x < y < z with each a successor of the previous, there is exactly one y' ≠ y between x and z, written σ_{x,z}(y). With axiom D (minorized subsets have infs) he derives the chain condition and the rank function δ, and operations σ_0, ..., σ_{n−1} on flags.

**Checked (SA04-R87-01).** (Σ) is the "diamond" property of face lattices of polytopes (G. M. Ziegler, *Lectures on polytopes*, GTM 152, 1995, Thm 2.7, locator to be checked), and polarity reversing the face order is right. Together with the operations σ_i on flags, these pages give the axioms of abstract polytopes later made standard (P. McMullen, E. Schulte, *Abstract regular polytopes*, CUP 2002, ch. 2, locator to be checked).

## Cote 88: maps from root systems, "Cartes standards" (SA04-34), K88-01, scans 2-16

**How read.** Every scan, through the compact view (five lines per scan).

**What he does.**
- **002-009:** "Cartes associées aux syst. de Racines (7)". Data (W, R, I, φ) with R a W-torsor and φ: R × I → W giving Coxeter generators, with φ(wr, i) = int(w)φ(r, i); the associated map with operations σ_i; parabolic subgroups; checks that σ_i² = 1, that σ_i and σ_j commute for |i − j| ≥ 2, and that π^{2n} = 1 when (φ(r, u(l−1))φ(r, u(l)))^n = 1.
- **011-016, "Théorème (à prouver)":**
  - every connected, simply connected, quasi-regular cellular map is a C_{p,q}, with Aut(C_{p,q}) ≅ Γ_{p,q};
  - standard Riemannian surfaces (the sphere, the Euclidean plane, the hyperbolic plane) and geodesic standard maps, unique up to similarity in each isotopy class;
  - C_{p,q} is spherical exactly for p = 2 and for (3,3), (3,4), (4,3), (3,5), (5,3), the five Platonic solids;
  - quotients by groups π acting freely, with his warning "attention au cas où p ou q est infini !".

**Checked (SA04-R88-01).** The spherical list is right: 1/p + 1/q > 1/2 exactly for p = 2 or for (3,3), (3,4), (4,3), (3,5), (5,3). The theorem "à prouver" is the classical description of regular maps as quotients of the universal maps C_{p,q} by subgroups of the triangle group (H. S. M. Coxeter, W. O. J. Moser, *Generators and relations for discrete groups*, 1957, ch. 8, locator to be checked). It is the setting of the dessins d'enfants.

## Cote 89: the combinatorial hexagon and 3-3 sets (SA04-35), K89-01, -02, scans 2-21

**How read.** Every scan, through the compact view (five lines per scan).

**What he does.**
- **002-009, "les ensembles 3-3":** a combinatorial hexagon H = (S, A, R) and its antipodism; 6-element sets with a partition of type (3,3) into S_i, i ∈ τ; the torsor ∧ω_{S_i} = 1; antipodisms σ_i with σ_k = σ_iσ_jσ_i; the automorphism group 𝒢 of order 72; the set S' of involutions above τ, which is again a set with a (3,3)-partition, by a surjection S' → τ' of degree 3. A hexagonal structure is a (3,3)-structure with a point of S'.
- **010-015, F_3-planes:** for V a plane over F_3, P(V) has four points, and a partition of type (2,2) {τ, τ'} gives V ≅ ⊕_{i∈τ} D_i. Torsors P_i = P/D_ī; equivalences of categories Tors(V) ≅ Π_{i∈τ} Tors(D_i) ≅ Π_{i∈τ'} Tors(D_i); combinatorial squares Q correspond to F_3-planes with a pair of lines, the edges being A_Q ≅ Π_{i∈τ} D_i^*.
- **016-019:** a module V of rank 2 over a ring Λ, P(V)^! = V^*/Λ^*, and the reconstruction of V from P, the torsors T_x and ω = det V ("au moins si Λ est un corps").
- **020-021:** topological versus combinatorial polygons; duality; orientations of edges and contours.

**Checked (SA04-R89-01, -02).**
- The order 72 is that of the stabilizer of a (3,3)-partition of six points, (S_3 × S_3) ⋊ Z/2.
- For V = F_3², with τ = {D_1, D_2} and τ' = {D_3, D_4}: u ∈ D_1^* and v ∈ D_2^* give u + v outside D_1 ∪ D_2. So Π_{i∈τ} D_i^* (four elements) ≅ V^* − (D_1^* ∪ D_2^*) = D_3^* ∪ D_4^*, as on 015.

## Cote 161, parts 1-4 and 6 (placed in SA23 by sweep 2; read here at the lead's request)

**How read.** Every scan, through the compact view (two or three lines per scan, 95-105 characters). 161-2 (scans 4-112) was read at two lines per scan only. No scan image viewed. These are mostly teaching and foundational dossiers; the reading identifies the content and checks a few statements.

**161-1 (K161-1-01, scans 4-20), SA23-29:**
- adjoint functors (margin "demander Schanuel"); the largest subcategories on which an adjunction is an equivalence; categories of finite families and their products, contraction and the sign ε(L) of an invertible object;
- "théories finies" forming 2-categories; extending functors from a strictly generating subcategory (020: Hom'(E, F) → Hom'(C, F) fully faithful, an equivalence);
- **a stray crystals page (017):** "M F-cristaux filtrés sur (k, L) ... G = Aut(T̄_p), π → G(Q_p)", the notation of 161-5/023-029 (SA04-15). It belongs with the cote 161-5 notes.

**161-2 (K161-2-01 to -07, scans 4-112), SA23-30, -31, -53, -54:**
- δ-exact envelopes K(C, δ) by transfinite construction, conditions of exactness, and "Ceci résoud à la fois le Pb 1 et le Pb 2" (016);
- "Topos et structures algébriques" (018-053): classifying topoi of algebraic structures as topologies on the category of affine schemes of finite type over Z. The list includes rings, reduced, irreducible and compact rings, algebraically closed fields ("= corps ultralocal", 044), perfect rings of characteristic p, rings with a characteristic, and a question on flatness as a "typical" property;
- accessible categories Ind_π(C) and Fil^π (055-062, "Ref à SGA4 I");
- algebraic theories 2-represented by categories R, worked through four cases of the data (d', d'') (063-110);
- "Topos modulaire pour des structures algébriques sur objets fixés d'un topos fixé X" (112).

**161-3 (K161-3-01 to -03, scans 4-55), SA23-32:**
- products of topoi (004-015): Π(E, F) as sheaves on E with values in F; (Ĉ × Ĉ') ≃ (C × C')^; the comparison Top(X × Y) → Top(X) ×² Top(Y), proved with quasi-compact neighbourhoods;
- filtered limits of essential topoi; functors on a topos commuting with colimits; "Espaces essentiels et ensembles ordonnés" (preorder topologies);
- a locally ringed topos lemma; and English lecture notes (035-055) on direct and inverse images, fibre functors, classifying topoi B_G and sites. One margin names "Prasad Gopal". They include the statement that Ĉ is equivalent to some Top(X) iff C is an ordered category.

**161-4 (K161-4-01, -02, scans 3-32), SA23-33:**
- flat descent: a flat morphism locally of finite presentation is universally open; descent of finiteness properties, quasi-coherent sheaves, subschemes and morphisms; integrality descends (007);
- radicial morphisms; quasi-affine schemes; ampleness ("EGA II 4.5"); irreducible, connected, noetherian, reduced and normal schemes;
- representable functors (Sch)/k → Ens through open immersions of sheaves; the question whether the presheaf topos of C × D is Ĉ × D̂ (018);
- a "Géom. Algébrique" course: limits and sums in Aff_k, topology of spectra;
- a course outline in English, "Prerequisites for the courses I and II" (023).

**161-6 (K161-6-01, -02, scans 2-34), SA23-37 (combinatorial geometry, SA04 in substance):**
- a folder headed "Groupes (Notes sur formes paraboliques prêtées à ...)", margin "Graphes, icosaèdre";
- the icosahedron in Euclidean 3-space (004-022): caps (calottes) of five points around a vertex, the equilateral condition cos(α/2) = ±1/(2 sin(θ/2)), edge lengths ℓ, ℓ' as roots of a quadratic, the group Γ_I of the icosahedron, and the field Z[1/5][ζ] with Galois group (Z/5)^* and γ = ζ + ζ^{−1}; a group of order 60 acting transitively on 15 objects (edge directions);
- isotopy classes of tame embeddings of a compact 1-dimensional X into an oriented surface S (025-031), through regular neighbourhoods U_α, the components of U_α − X, genera, and the groups Isot(S, S) and H;
- graphs as data (S, A, A' → S × S, σ) of half-edges with an involution (033-034).

**Checked (SA04-R161-01 to -04).**
- **161-6/013:** for ζ a primitive fifth root of unity, ζ + ζ² + ζ³ + ζ⁴ = −1. Hence γ = ζ + ζ^{−1} satisfies γ² + γ − 1 = 0, and (Z/5)^* ≅ Z/4 is the Galois group over Z[1/5] (015).
- **161-6/026, his margin "le nb des V^i_α est b_1(X)+1 si X connexe non vide ?":** the components of U_α − X correspond to the boundary circles of the ribbon surface U_α, and χ(U_α) = χ(X) = 1 − b_1(X) = 2 − 2g(U_α) − #∂. So the number is b_1(X) + 1 − 2g(U_α). His guess holds exactly when U_α has genus 0 (e.g. X planar in S) and fails otherwise: a figure-eight on a punctured torus gives one component, not three.
- **161-3/008-015:** the product statements agree with the theory of products of topoi and of locales (sheaves on X × Y are the product of the topoi when one factor is locally compact; P. T. Johnstone, *Sketches of an elephant*, C1.4, locator to be checked).
- **161-4/004:** that a flat morphism locally of finite presentation is universally open is EGA IV₂ 2.4.6.
