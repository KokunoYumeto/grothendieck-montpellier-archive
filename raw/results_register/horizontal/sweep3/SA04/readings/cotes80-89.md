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

## Full pass, cote 80 (K80-01 to -04, Codex-web, GPT-6 Astra at reasoning effort max)

### 003-012: classification of pseudoline systems with a marked line; S-pinned stable chord systems; Stein factorization

**What he does.**
- **003.**
  - C(I) ≅ C_aff(I_0), the classes of pseudoline systems (X, Σ, Δ) with Σ indexed by I = I_0 ⊔ {i_0} and Δ = Δ_{i_0}.
  - Two maps: β, forgetting the marking of Δ, onto C(n + 1) = C(I)/S_I, with fibre Σ/G_{X,Σ}; and β', erasing Δ, onto C(n), with fibre the types of relative position.
  - For n = 5: "deux fibres qui sont de card 1, deux de card 2"; C(5) has one element and its fibre card 6 (or 5).
- **004-005.**
  - A stable class ξ gives I_0 a polygonal structure and a double cover Ĩ_0(ξ). The system becomes a disc D = Déc(X, Δ) with a stable chord system Σ̃ indexed by Ĩ_0(ξ).
  - For a fixed combinatorial polygon S of order 2n: C̃_st(S) → C^!_{aff st}(I_0) with I_0 = S/a_S. The fibres have 2 elements, exchanged by the antipodism.
- **006-008.**
  - Card α^{−1}(ξ♮) = (n!/2n)·card α^{!−1}(ξ♮), where n!/2n = (n − 1)!/2 is the number of polygonal structures on I_0.
  - card α^{!−1}(ξ♮) = 2n/N(ξ♮), with N = |Aut(X, Σ, Δ)| the stabilizer, so card α̃^{−1}(ξ♮) = 4n/N(ξ♮).
  - Examples: n = 3 (Aut ≅ S_3, one orbit of order 12/6 = 2); n = 4 (Aut ≅ Z/2, card C̃_st(S) = 8); n = 5 (card C_aff(5) = 6). Then a résumé.
- **010** is blank. **012** is a drawing.
- **011.** Stein factorization: for "flèches steiniennes" Z' → X' over Z → X there is an initial object Z → Z̃. The question is when the factorization commutes with base change: a) Z → X proper? b) X' → X locally O-acyclic?

**Checked (SA04-R80-02).**
- (n − 1)!/2 counts the cyclic orders of n points up to reflection.
- n = 3: 4n/N = 12/6 = 2. n = 4: 16/2 = 8. For n = 4, the unique simple arrangement of five pseudolines has symmetry D_5, transitive on the lines with stabilizer of order 2, so C_aff(4) has one element and N = 2.
- n = 5: the four simple arrangements of six pseudolines have line-orbit counts adding to 6 (1 + 1 + 2 + 2, as on 003), which agrees with card C_aff(5) = 6. The counts of simple projective arrangements (1, 1, 4 for 5, 6 lines) are classical: Grünbaum, *Arrangements and spreads*, CBMS 10 (1972) (locator to be checked).

### 013-021: real hyperplane systems as an F_3-sign stratification; bigonal pseudoline arrangements

**What he does.**
- **014.** Inequalities a + a' < 2, b + b' > 2 and a' + b > 2, "d'où b > a".
- **017-019, "Système d'hyperplans (projectifs) réels".**
  - For a hyperplane H of V, D_H = {H, V'_H, V''_H} is seen as F_3 = {−1, 0, 1}. φ: S = V^*/R^{*+} → E = ΠD_{H_i} has convex fibres Z^*_α, indexed by Σ = φ(S), which is stable under −1.
  - The closure of Z^*_α is the union of the Z^*_β with β ≤ α, for the order 0 < ±1 on each factor. So Σ indexes a finite stratification of the sphere with the faithfulness and density axioms.
  - Then "Σ est une partie ouverte de E (α ∈ Σ, β > α ⇒ β ∈ Σ)", with his margin "?".
- **021.** Every bigonal 1-dimensional pseudoline arrangement other than the four-line one contains one of the configurations (2), (3). Otherwise it is of type (4), or of type (5): the seven pseudolines of a quadrilateral and its three diagonals, "qui mérite d'être étudié".

**Checked (SA04-R80-03).**
- Σ is the set of covectors of the oriented matroid of the arrangement, and the closure formula is the face order. This is the Folkman-Lawrence setting: J. Folkman, J. Lawrence, "Oriented matroids", J. Combin. Theory B 25 (1978); Björner, Las Vergnas, Sturmfels, White, Ziegler, *Oriented Matroids* (1993), ch. 4 (locators to be checked).
- **The openness he doubts is false in general (correction SA04-K80-02).** In R³ with three planes through one line L, the cell L has zeros in all three coordinates. Of its 26 sign completions only 12 occur (6 regions and 6 half-planes).
- Openness does hold when the arrangement is simple, since near a cell of codimension k it looks like the k coordinate hyperplanes. So the statement is right for simple (generic) systems.

### 022-030: the crucial arrangements I_N, I_pq, II_pq, II_4, II_5, III_6, IV_7; the lattice case

**Reused leaves (one line).** 022, 024, 026, 030 are a German autobiographical draft ("liest Deutsch …", the letters with Hanka). 028 is a university notice of a thesis defence (Montpellier, 13 May 1981), used as scrap paper.

**What he does.**
- **023, "Cas cruciaux d'arrangements 1-dimensionnels de N ps. droites", N ≥ 4.**
  - With a bigonal pseudoline:
    - I_N: a pencil of N − 1 concurrent pseudolines and one secant;
    - I_pq: two pencils of p and q (p ≥ q ≥ 2) with the line through their two centres, p + q + 1 = N, pq + 2 vertices.
  - Without one:
    - II_pq: two pencils with alternating centres, p + q = N ≥ 5, pq + 2 vertices;
    - II_4, the simple arrangement of 4 pseudolines (6 vertices);
    - II_5, the simple arrangement of 5 (10 vertices).
- **025, Théorème.** If no two vertices meet every pseudoline (not I_N, I_pq, II_pq), there are further cases:
  - III_6, the tetrahedral arrangement (4 + 3 = 7 vertices);
  - IV_7, a quadrilateral with its three diagonals (6 + 3 = 9 vertices).
  These, with I_{2,2} and the I_N (N ≥ 5), are the exceptions he lists.
- **027.** The "cas latticiel": the intersection of two closed facets is empty or a closed facet. Proposition: this holds iff there is no bigonal pseudoline and the arrangement is not of type II_4. Then a proposition on adding a non-bigonal (N + 1)-th pseudoline.
- **029, Lemme.** Without bigonal pseudolines and with N ≥ 5, the lines can be ordered so that D_1-D_4 is of type II_4 (or D_1-D_6 of type III_6), each further D_i not bigonal in K_i. The cases are mutually exclusive: K_5 of type II_5 or II_32, or K ≅ III_6 or IV_7. "Les pts de départ sont II_4 ou III_6."

**Checked (SA04-R80-04).**
- The vertex counts:
  - I_N has N vertices: the centre and the N − 1 crossings of the secant. This is SA04-K80-01; the margin "N + 1" counts one too many.
  - I_pq and II_pq have pq + 2; II_4 has C(4, 2) = 6 and II_5 has C(5, 2) = 10.
  - III_6: the six lines through four points in general position meet in the 4 triple points and the 3 diagonal points, 7.
  - IV_7: the four lines of a quadrilateral meet in 6 points. Each diagonal passes through two opposite ones, and the diagonals meet each other in 3 new points: 9.

### 031-038: arrangements of three pseudolines as the hemi-octahedron; orientations as contracted products of Z/2-torsors

**What he does.**
- **032.** The combinatorial cube is given by three 2-element sets Φ_i (i ∈ I, |I| = 3). Its faces are Φ = ⊔Φ_i, its edges the injective 2-element subsets, and its vertices the full sections (2). The octahedron is the dual (3). The antipodism a is central.
- **033-034.**
  - The quotients by a are the "left" (projective) cube C̃ and octahedron Õ (4). The left octahedron has 3 vertices, 6 edges and 4 faces, "la décomposition du plan projectif réel par un système de trois droites".
  - The ordinary figures are not recovered canonically from the left ones, since a acts trivially below. But oriented cubes, left cubes, oriented octahedra and left octahedra are equivalent categories (5).
  - or(C) = or(O) = (∧Φ_i) ∧ or(I) (6), where or(I) is the set of the two cyclic orders of I.
- **034-037.**
  - For the pseudoline D_i of Õ: its edges A_i = ∧_{α≠i}Φ_α (7), i.e. the bijections Φ_j ≅ Φ_k; its vertices S_i = I ∖ {i} (8); its orientations Ω_i = S_i ∧ A_i (9).
  - ∧A_i ≅ 1 and ∧Φ_α² ≅ 1 (10), so ∧Ω_i ≅ ∧S_i ≅ or(I) (11).
  - The Ω_i and Φ_i determine each other (13), with ∧Ω_i ≅ ∧Φ_i (14).
  - Proposition: the combinatorial map with 3 vertices, 6 edges and 4 triangles is the same as an arrangement of three pseudolines with its 1-skeleton and the three bigons D_i.

**Checked (SA04-R80-05).**
- Cube: 6 faces, 3·2·2 = 12 edges, 2³ = 8 vertices.
- Quotient by a: the hemi-cube has 4 vertices, 6 edges and 3 faces; the hemi-octahedron 3, 6 and 4. Both have Euler characteristic 1 = χ(RP²), the latter being three lines in general position in RP².
- The two edges on D_i are the two bijections between the 2-element sets Φ_j and Φ_k, a torsor isomorphic to Φ_j ∧ Φ_k, as (7) says.

### 038-043: the cube of categories; oriented 1-dimensional arrangements; reconstructing the map

**What he does.**
- **039.** A cube of categories: oriented against non-oriented, spherical against projective ("gauche"), 2-dimensional against 1-dimensional configurations. He says which arrows are equivalences, which are faithful or surjective on Hom, and that oct. g. → gr. oct. gauche is faithful ("l'énoncé (16)").
- **041, definition.** A 1-dimensional arrangement of pseudolines: a finite 1-complex K with polygonal subcomplexes D_i that partition the edges, any two meeting in exactly one vertex, every vertex on at least two of them, and ∩D_i = ∅.
  - Then some 3-element I ⊂ J has no common point. K_I is then a left octahedral graph (the transcription has "octogonal"), which can be oriented.
- **040.** An orientation ω of (K, (D_i)) is an orientation of each left octahedral graph K_I. A pseudoline arrangement 𝒳 gives the functor 𝒳 ↦ (K, (D_i), ω) (18). Proposition: the functor is fully faithful (Isom(𝒳, 𝒳') ≅ Isom of the oriented 1-dimensional data).
- **042-043.** The proof reconstructs the map from:
  - the two circular orders Z⃗_s on the arcs at each vertex s (19);
  - the transports ψ_a along arcs, with ψ_{−a} = ψ_a^{−1} (20, 21);
  - the condition ρ^{ν_s}(D⃗_i) = −D⃗_i for ρ ∈ Z⃗_s (22), ν_s being the number of lines through s.
  This gives a cellular immersion of K into a map, "peut être pas le plan projectif !".

**Checked (SA04-R80-06).**
- 041, existence of a non-concurrent triple. If every triple were concurrent, take D_1, D_2 meeting in their only common vertex p. Every triple {1, 2, k} would be concurrent at p, so all D_k would pass through p, contradicting ∩D_i = ∅.
- 043: at a vertex where ν_s lines cross there are 2ν_s arcs. Turning ν_s steps leads from an arc to the opposite arc of the same line, which is (22).

### 044-049: the axioms (A1)-(A4) for reconstructing the circular orders at the vertices and their transport along edges

**What he does.**
- **044.** For a pseudoline Δ not through s, the injection φ_{s,Δ}: I_s → S_Δ (25) induces a polygonal structure Z'_{s,Δ} on I_s. (A1): it does not depend on Δ, giving Z'_s.
- **044-045.** The circular orders on the oriented lines I⃗_s must lie over Z'_s (27), "une condition restrictive importante". Once an orientation u_0 is fixed this leaves 2^{ν_s−1} possibilities: the bijections α_i: ω_i → ω_{u_0(i)}, subject to the closing condition (28).
- **046-047.**
  - An oriented Δ⃗ gives u_{s,Δ⃗}; for ν_s = 2 this is the transposition, "le compte est bon, même pour ν_s = 2".
  - The lift u⃗_{s,Δ⃗} is fixed by the triangle rule: the edges s → t, s → u and t → u bound one triangle of the arrangement of Δ, D, D', oriented as ω_{{i,j,Δ}}.
  - (A2): the lift is circular, i.e. its ν_s-th power is the transposition on each fibre. u⃗_{s,−Δ⃗} = u⃗_{s,Δ⃗}^{−1} (30).
  - (A3): Z⃗_{s,Δ'} = Z⃗_{s,Δ}.
- **048.** A surjection from the oriented pseudolines not through s onto Z⃗_s, compatible with ±1 (31). Along an arc a from s to s', ψ_a is defined through the lines avoiding both ends (32). (A4): two such lines inducing the same orientation at s induce the same one at s'.
- **049.** "Reste à traiter le cas (très particulier !) où ∄ ps. droite Δ qui ne passe ni par s ni par s'".

**Checked (SA04-R80-07).** The 2^ν choices of the bijections α_i give a permutation of the 2ν oriented lines over the ν-cycle u_0. Its ν-th power acts on each 2-element fibre by the composite of the α's around the cycle. Transitivity (a single 2ν-cycle) forces this composite to be the transposition, which is half of the choices: 2^{ν−1}, as he says. For ν = 2, u_0 is the transposition and there are 2 lifts.

### 049-053: the exceptional case, and the canonical orientation of a triangle K_J

**What he does.**
- **049-050.**
  - When no pseudoline avoids s and s', he goes round through a third line: ψ_a = u_{b'}u_b (34), with "(A5) — savoir que ce u_a ne dépend pas des choix arbitraires".
  - "Je n'ai donc pas vérifié que la proposition énoncée soit correcte, sans exclure le cas où K est formé de n pseudo-droites concourantes, coupées par une seule autre". This is the case I_N; his margin answers it: "mais si, par l'argument en marge de la page précédente".
- **051-053, the canonical orientation of K_J.**
  - Case 1: some Δ avoids the three vertices, so K_{J∪{i}} is a simple arrangement of four pseudolines.
    - Proposition: simple arrangements of 4 pseudolines are equivalent to simple 1-dimensional ones, by comparing both groupoids with that of 4-element sets.
    - So K_J inherits ω_{J,i}, and (A5) says it does not depend on i.
  - Case 2: every line passes through a vertex of K_J.
    - A 9-vertex configuration of six lines D_i, D_{a_i}. Either a circular order on J puts a_i opposite a'_{i+1} on D_{a_i} (case I), or a_i is opposite α_i (case II).
    - The edges λ_i are compatible with the orientation in case I and not in case II. (A6) follows on 054.
  - (On 051 "trois ps. droites concourantes" must mean non-concurrent, since K_J is a triangle.)

**Checked (SA04-R80-08).** The Proposition of 051 holds.
- Four pseudolines in general position in RP² (realizable by lines) are a projective frame of the dual plane. Every permutation of them is induced, so the automorphism group is S_4, acting faithfully on the lines.
- The 1-dimensional arrangement is the octahedron graph (6 vertices, 12 edges) with four alternate triangles as lines. Its automorphisms preserving these triangles form the stabilizer of order 48/2 = 24 ≅ S_4, again faithful on the lines.
- The functor is therefore an isomorphism on automorphism groups between two connected groupoids: an equivalence.

### 054-062: the standard exception; the theorem of full faithfulness; "Système de Pseudodroites"

**What he does.**
- **054-055.**
  - The last case of the orientation problem forces card I = 6: the standard arrangement III_6, with 4 triple points, 6 lines and 3 further points. Its automorphism group is S_4, and it is described by its four triple points.
  - **Théorème:** the canonical functor from the groupoid of pseudoline arrangements without bigons to that of 1-dimensional arrangements without bigons is fully faithful.
  - (A1)-(A6) give "en principe" the essential image, "mais il faut arriver à simplifier les conditions"; the Euler-Poincaré relation (23) "je soupçonne que cette dernière est automatique".
- **057, 059, margins and counts.**
  - "+ 9 triangles + 1 carré", "25 triangles, 5 carrés, 1 pentagone".
  - "31 = 5 + 15 + 10 + 1", with types 1_6 ≡ icosaèdre, 5_1 ≡ hexagone, 5_4, 5_2 ≡ triangle bordé, 5_5, 10_3 ≡ carré gammé.
- **061-062, "Système de Pseudodroites".**
  - The definition: a map on the real projective plane (compact, non-orientable, χ = 1) with all vertex orders even and ≥ 4, whose edge classes (the pseudolines) meet pairwise in exactly one point. Each pseudoline is not null-homotopic.
  - "On montre que pour des psdr en position générale … et en nb n ≤ 6, la situation peut être réalisée par un système de vraies droites."
  - On the orientation cover X̃ ≅ S², D̃ splits X̃ into two hemispheres, one for each orientation of D. The orientations of X at a vertex s correspond to those of any D not through s, and he asks how to compare two such D, D'.

**Checked (SA04-R80-09).**
- 055: III_6 is the complete quadrangle. Four points in general position give 6 lines meeting in the 4 points (triply) and 3 diagonal points. Its automorphisms permute the four points: S_4.
- 059: 5 + 15 + 10 + 1 = 31.
- For five lines in general position: 10 vertices, 20 edges and 11 faces (χ = 1), namely 5 triangles, 5 quadrilaterals and 1 pentagon. The "25 triangles" of 057 belongs to another figure, which is not identified here.
- 061: his realizability claim for n ≤ 6 is true and is weaker than the known result. All simple arrangements of at most 8 pseudolines are stretchable, and the first non-stretchable simple one has 9: J. E. Goodman, R. Pollack, J. Combin. Theory A 29 (1980) 385-390; G. Ringel (1956) (locators to be checked).

### 063-073: comparing the orientation sets Ω(D); the axioms a)-f) for the circular orders ρ_{D⃗,s}; uniqueness; standard small configurations

**What he does.**
- **063-066.**
  - Through a vertex s not on D, D', the lines Δ_i through s define the bijection φ_{s;D,D'}: Ω(D) ≅ Ω(D'), by the matching order of the u_i on D and the u'_i on D'.
  - Special cases: a single line through s missing t, and the double pencils. In the last of them the six lines join four points u, u', r, t, and φ_s agrees with φ_r.
  - Properties: a) on the lines missing s the φ_{s;D,D'} form a simply transitive system; b) for s, s' on Δ, φ_s = φ_{s'} iff s, s' lie on the same arc cut out by x, x'; c) a relation of the same kind.
  - There is no uniqueness in the presence of a bigon or a monogon (a double pencil with the joining line, or a pencil).
  - Otherwise Ω(s) is a 2-element set forming a local system on K^1 (066). "Pour finir de récupérer la carte" the polygonal structure at the vertices is still needed (067).
- **068-071.**
  - Oriented pseudolines D⃗ and circular permutations ρ_{D⃗,s} of the oriented lines through s, with axioms a) ρ_{−D⃗,s} = ρ_{D⃗,s}^{−1}; b) equal or opposite for two lines; c) the arc condition; d) successors of intersections along D⃗; e) adjacency; f) (ρ_{D⃗,s})^n(Δ⃗) = −Δ⃗ at a vertex of order 2n.
  - **Th** (071): if there is no monogon or bigon, such a system is unique, and Ω(s) = {ρ_s, ρ_s^{−1}} is a local system in a unique way. His margin: e), f) suffice, and a) probably follows.
- **073, standard configurations.**
  - 1 line; 2 lines (the automorphisms of a square).
  - 3 lines in general position: "aut. proj / comp. conn ≅ autom. comb ≅ aut. cube orienté ≅ autom. de l'ens des quatre faces".
  - 3 concurrent lines: an extension of S_3 by Z/2, "≅ gpe de l'hexagone (!)".
  - 4 lines in general position: projective automorphisms fixing each line are trivial, the combinatorial ones form S_4.

**Checked (SA04-R80-10).**
- 073, three lines in general position. Their projective stabilizer is the monomial group modulo scalars, (R^*)³/R^* ⋊ S_3. Its component group is ({±1}³/{±1}) ⋊ S_3 ≅ (Z/2)² ⋊ S_3 ≅ S_4, the rotation group of the cube, acting on the 4 triangular regions.
- Three concurrent lines: the 6 rays carry the symmetry of the hexagon, the dihedral group of order 12, an extension of S_3 by Z/2 as he says.
- f) of 070 is condition (22) of 043 (SA04-R80-06).

**Still to read for cote 80:** the four K80 math notes. The SA04-K80-01 margin count is settled above (SA04-R80-04).

### Addendum to cote 80: the ends of 037, 043, 053, 062 and 073

My first view of these five scans was cut short at a fixed line width. Their ends were read afterwards.

**What he does.**
- **037 (end).** (15): ∧Ω_i ≅ ∧Φ_i ≅ (∧A_i) ∧ ∧_{α∈I}(I ∖ {α}). This is (9), Ω_i = S_i ∧ A_i, taken over the three i, together with (14).
- **043 (end).**
  - (23): 𝒳 is the projective plane iff c_0 − c_1 + c_2 = 1, i.e. c_2 = c(K). Here 1 − c(K) = c_0 − c_1, and c(K) is "le degré de connexion" of K.
  - His margin: "a priori c_2 ≤ c(K)", and (23) says the bound is attained.
  - Then the construction of the Z⃗_s satisfying (22) begins: for ν_s ≥ 3, Z'_s ⊂ 𝔖_{I_s} is the pair of opposite circular orders (a polygonal structure) on the lines through s, read off on a pseudoline Δ that misses s. The construction continues on 044.
- **053 (end).**
  - (A5) finishes: the edges λ_i of K_J are compatible with the orientation in case I and not in case II.
  - (A6) begins, with three non-concurrent lines such that every other line passes through a vertex of K_J. Both are taken up in the sections on 049-053 and 054-062.
- **062 (end).** He asks how to make the composite bijection Ω(D) ≅ Ω_s(𝒳) ≅ Ω(D') explicit, using two lines Δ, Δ' through s that are non-concurrent with D and D'. This is answered on 063-066.
- **073 (end): the rest of the table of standard configurations.**
  - 4 lines, three of them concurrent: "standard proj.", with aut. proj / comp. ≅ an extension of 𝔖_3 by Z/2 ≅ the combinatorial group ≅ "gr. hexagone".
  - 4 concurrent lines: "pas standard projectif mais st. comb", with "autom comb. groupe de l'octogone (?)".
  - 5 lines in general position: "[pas] standard proj., mais standard comb., groupe des autom comb ≅ groupe du pentagone", with the "pas" struck in the ink.
  - n ≥ 6 lines in general position: "pas standard comb."

**Checked (SA04-R80-11): his margin on 043.**
- The reconstructed 𝒳 is a connected closed surface with K as 1-skeleton and c_2 discs. So c_0 − c_1 + c_2 = χ(𝒳) = 2 − b_1(𝒳; F_2), i.e. c_2 = c(K) + 1 − b_1(𝒳; F_2).
- Two of the D_i meet in exactly one vertex, and they cross there, since by (22) their arcs alternate in the circular order. So their mod-2 intersection number is 1, and b_1(𝒳; F_2) ≥ 1.
- Hence c_2 ≤ c(K), as his margin says. Equality holds iff b_1(𝒳; F_2) = 1, i.e. iff 𝒳 ≅ RP², which is the only closed surface with that Betti number.
- So (23) is exactly the condition that the map be the projective plane. This bears on his suspicion on 055 that (23) is automatic.

**Checked (SA04-R80-12): the end of the table on 073.**
- **4 lines, three of them concurrent.** Let p be the common point and L the fourth line. The configuration is projectively unique, since the stabilizer of (p, L) induces all of PGL(L) on the three points where the pencil meets L.
  - The stabilizer is 𝔖_3 times the homologies with centre p and axis L (≅ R^*). Its component group is 𝔖_3 × Z/2 ≅ D_6, the group of the hexagon of half-lines at p.
  - The combinatorial group acts faithfully on those six half-lines and keeps their cyclic order, so it is at most D_6. Hence equality, as he says.
- **4 concurrent lines.** The cross-ratio of the four lines is a modulus, so the configuration is not projectively standard. It is combinatorially unique: one vertex, four loop edges, four faces.
  - The permutations of the eight half-lines at the vertex that keep the cyclic order and the antipodal pairing are all of D_8, since the half-turn is central in D_8.
  - All of them are realized: the pencil at 45° angles has the rotation by 45° and the reflections. So the answer to his "(?)" is yes: the octagon group, of order 16, acting on flags.
  - On lines, edges and faces alone the half-turn acts trivially (it only reverses each loop edge), and the group seen there is D_4.
- **5 lines in general position.** They carry 2·5 − 8 = 2 projective moduli, so "pas standard proj." is needed (correction SA04-K80-03; Michel Hua's project makes the same point in a footnote).
  - The simple arrangement of 5 lines is unique, and its single pentagon (face vector 5, 5, 1; SA04-R80-09) is preserved by every automorphism.
  - An automorphism fixing that pentagon fixes every line, hence every cell. So the group embeds in D_5, and the regular pentagon realizes all of it: "groupe du pentagone" is right.
- **n = 6.** There are four simple arrangements of six pseudolines, all stretchable, so six lines in general position are not combinatorially standard. Reference: B. Grünbaum, *Arrangements and Spreads*, CBMS Regional Conf. Ser. Math. 10, AMS 1972 (locator to be checked).

## Full pass, cote 82 (K82-01 to -05, Codex-web, GPT-6 Astra at reasoning effort max)

### 002-009: "Formes quadratiques de rang trois et algèbres de Lie"

**What he does.**
- **002-004.**
  - For E, E' of rank 3 in duality over a scheme S, there are isomorphisms Λ²E ≅ E' ⊗ det E (3). For E "spécial" (a basis ω of det E) these become α: Λ²E ≅ E' and α': Λ²E' ≅ E (6, 7), with α(ē_i) = e'_i in bases (10).
  - Observation: bilinear forms φ on E, Hom(E, E') and alternating algebra structures on E' correspond bijectively, by [x', y']_φ = f α'(x' ∧ y') (11, 12).
- **005-006.**
  - In a basis, [e'_2, e'_3] = Σφ_{1j}e'_j, [e'_3, e'_1] = Σφ_{2j}e'_j, [e'_1, e'_2] = Σφ_{3j}e'_j (12). The double brackets (13) and, with the notation (14)-(15), φ = [[a, r, q'], [r', b, p], [q, p', c]], the Jacobiator (17) = [a(p' − p) + (q'r' − qr)]e'_1 + [b(q' − q) + (r'p' − rp)]e'_2 + [c(r' − r) + (p'q' − pq)]e'_3.
  - So E'_φ is a Lie algebra iff (18) holds, i.e. iff certain 2×2 minors of φ and of ^tφ agree (19).
- **007.** Proposition: symmetric bilinear forms define Lie algebra structures on E'. Then an example on O_S³ with a quadratic form q(x, y, z).

**Checked (SA04-R82-04, script `jac82.py`).**
- For 200 random integer matrices φ, the Jacobiator computed from the brackets (12) equals his formula (17) exactly.
- For symmetric φ (p = p', q = q', r = r') all three components vanish, which is the Proposition of 007.
- This is the classical correspondence between ternary quadratic forms and 3-dimensional Lie algebras, i.e. forms of sl_2 = so_3, here over any base with a trivialized determinant.

### 007-013: the example xy + z² gives pgl_2 over Z; discriminants and "structures spéciales orthogonales"; the cofactor map f'

**What he does.**
- **007.** For q = xy + z² (φ = [[0, 1, 0], [1, 0, 0], [0, 0, 2]]) the brackets are [e'_2, e'_3] = e'_2, [e'_3, e'_1] = e'_1 and [e'_1, e'_2] = 2e'_3. So with X = e'_1, Y = e'_2, H = e'_3: [H, X] = X, [H, Y] = −Y, [X, Y] = 2H, "l'algèbre de Lie « universelle » (sur les entiers) de GP(1)".
- **008-009.**
  - δ(φ) = −det(φ_ij)ω'^{⊗2} (27). For q = ax² + by² + cz² + pyz + qzx + rxy, δ(q) = 2(4abc + pqr − ap² − bq² − cr²)ω'^{⊗2} (30), and the divided discriminant δ'(q) = 4abc + pqr − ap² − bq² − cr² (31).
  - For xy + z², δ'(q) = −ω'^{⊗2} (32). Hence the definition of a special orthogonal structure (q, ω) with δ'(q) = −ω^{⊗−2} (33), and in rank 2n or 2n + 1 with δ'(q) = (−1)^nω^{⊗−2} (34-36). Such structures exist locally fppf.
- **009-010.** Exchanging E and E': f' = α'∘Λ²f∘α^{−1}: E' → E (38), whose matrix is made of the nine 2×2 minors of f. [x, y]_{φ'} = α'(f(x) ∧ f(y)) is again a Lie structure.
- **011-013.**
  - Cramer: f'f = Δ·id_E and ff' = Δ·id_E' (42). "On se gardera de croire que les relations entre f, f' sont symétriques": f' = 0 when f has rank ≤ 1.
  - Then f'' = (f')' with f'f'' = Δ'·id (44). For Δ a unit, f' = Δf^{−1} and f'' = (Δ'Δ^{−1})f (45).

**Checked (SA04-R82-05).**
- 007: in pgl_2(Z) = gl_2/scalars, h' = diag(1, 0), e = E_12 and f = E_21 satisfy [h', e] = e, [h', f] = −f and [e, f] = diag(1, −1) = 2h' − 1 ≡ 2h'. So the algebra is Lie(PGL_2) over Z, not sl_2, where [H, X] = 2X. This agrees with his "de GP(1)".
- 008: det[[2a, r, q], [r, 2b, p], [q, p, 2c]] = 2(4abc + pqr − ap² − bq² − cr²), and for xy + z², δ' = −r²c = −1.
  - (27) carries a minus sign, (30) has none. The Codex-web text marks the minus of (27) as doubtful. With δ = +det, (30)-(32) are consistent; this is listed as an open reading.
- 011-013: f' is the adjugate, so f'f = Δ·id. adj(adj f) = (det f)·f in rank 3 and det(adj f) = Δ², so Δ' = Δ² and f'' = Δ·f = (Δ'Δ^{−1})f, as (45) says.

### 014-020: f is a Lie homomorphism; the representation ρ_E of E' on E preserving φ; the example in the basis X, H, Y

**What he does.**
- **014-015.** f[x, y]_{φ'} = [f(x), f(y)]_φ (49), from the definition (40 bis). f' is a homomorphism of algebras only in special cases, even when f is an isomorphism (f' = Δf^{−1}).
- **016-019.**
  - ρ_E: E' → End(E) with φ(ρ_E(x')x, y) + φ(x, ρ_E(x')y) = 0 (52), a Lie homomorphism (55), and f(ρ_E(x')x) = ad(x')f(x) (56). The more precise ρ_E(ξ')x = α'(ξ' ∧ f(x)) (56 bis) is proved using ^tf = f, i.e. φ symmetric: "ce qui est bien vrai, hurrah !".
  - The construction: the contragredient of the adjoint representation (57)-(59), with Tr ρ_E = 0 (60).
- **019-020, the example of (21).** ω' = −X ∧ H ∧ Y (61), X̃ = e_2, Ỹ = e_1, H̃ = e_3 and ω = X̃ ∧ H̃ ∧ Ỹ (62)-(64). Then f(X̃) = X, f(Ỹ) = Y, f(H̃) = 2H (65), "Ici, en vertu de (32), Δ = −2", followed by f'.

**Checked (SA04-R82-06).**
- 019: f(e_i) = Σ_j φ(e_i, e_j)e'_j with φ = [[0, 1, 0], [1, 0, 0], [0, 0, 2]] gives f(e_1) = e'_2, f(e_2) = e'_1 and f(e_3) = 2e'_3, which is (65). det φ = −2.
- The sign of Δ is not stable across these leaves: 014 says "Δ = 2" for the case (21), 019 says Δ = −2, and (27) defines δ = −det. Since det f = −2 in the bases (8), δ' = −1 (32) and δ = 2δ', the consistent convention is δ = +det with Δ = −2. This is noted as an open reading for 008 and 014 (SA04-R82-05).

### 020-026: sl_2 → gp(1) as f, the forms φ', q' = h² + 4xy, and the Casimir forms

**What he does.**
- **020.** f'(X) = 2X̃, f'(Y) = 2Ỹ, f'(H) = H̃ (66). The form φ' has φ'(X, Y) = 2 and φ'(H, H) = 1 (67), so q'(η) = h² + 4xy (69). If 2 is not invertible, φ' does not come from a quadratic form.
- **021-022.**
  - The bracket on E is [H̃, X̃] = 2X̃, [H̃, Ỹ] = −2Ỹ, [X̃, Ỹ] = H̃ (70), i.e. sl(2)_S. f is the differential of SL(2)_S → GP(1)_S, whose kernel μ_2 is the centre. ρ_E is written out in (72).
  - If 2 is invertible f is an isomorphism. If 2 = 0, Ker f = O_S·H̃ is the centre of sl_2, while gp(1) has trivial centre over every base. "Il faudrait par la suite expliciter la structure des formes de 𝔰" (sl_2), which unlike the forms of SL_2 and GP(1) are not equivalent to forms of P^1.
- **023-026.**
  - The Casimir forms: Cas_{E'} = 2φ' and Cas_E = −2Δφ (74). The homogeneity is checked, then the value at H, then conservation of polynomial identities.
  - So for a special orthogonal q (Δ = −2), Cas_E(x, x) = 8q(x) (76) and Cas_{E'}(x', x') = 2q'(x') (77): q is recovered from the Lie structure when 2 is invertible or not a zero divisor.

**Checked (SA04-R82-07).**
- 020: φ'(x', y') = ⟨f'(x'), y'⟩ gives φ'(X, Y) = ⟨2e_2, e'_2⟩ = 2 and φ'(H, H) = 1, hence q' = h² + 4xy. The overall sign of f' depends on his choice ω' = −X ∧ H ∧ Y (61); the plain adjugate of [[0, 1, 0], [1, 0, 0], [0, 0, 2]] has the opposite sign.
- 024: ad H has eigenvalues 1, −1, 0 on gp(1), so Cas_{E'}(H, H) = 2 = 2φ'(H, H). ad H̃ has eigenvalues 2, −2, 0 on sl_2, so Cas_E(H̃, H̃) = 8 = −2·(−2)·φ(H̃, H̃) with φ(e_3, e_3) = 2.
- 022: if 2 = 0, [X̃, H̃] = −2X̃ = 0 and [Ỹ, H̃] = 0, so H̃ is central, and f(H̃) = 2H = 0.

### 026-031: scaling and uniqueness; forms of sl(2) and gp(1) in characteristic 2; SO(q), its simply connected cover and the Lie algebras

**What he does.**
- **026.** Scaling: [ , ]_{λω, μφ} = λμ[ , ]_{ω,φ} and [ , ]_{λω,(μφ)'} = λμ²[ , ]_{ω,φ'} (78). Hence [ , ]_{ω,φ} = [ , ]_{ω_1,φ_1} iff ω_1 = λω and φ_1 = λ^{−1}φ (79). For f invertible, f' = g' iff g = εf with ε² = 1 (80), and the analogue for the primed brackets with λμ² = 1 (81).
- **027-028, characteristic 2.**
  - The forms of sl(2) are the pairs (V, E), with V of rank 2 and E an extension of V by det V; the forms of gp(1) are the dual pairs (V', E'). An accouplement between them makes det V ⊂ E the orthogonal of V' ⊂ E'.
  - The coupled pairs are the triples (V, φ, E), i.e. "un fibré en plans affines symplectiques". The automorphism group of a form of sl(2) or gp(1) is the affine group in two variables, smooth of relative dimension 6.
  - f = E → V → V' → E' and f' = E' → O_S → det V → E.
- **029-031.**
  - G = SO(q) = Aut(E, q, ω) with δ'(q) = −ω^{⊗−2} (82, 83). Its simply connected cover G̃ has kernel μ_2, s = Lie G̃ and g = Lie G (85).
  - F: G̃ → G and the action ρ: G → Aut(G̃) obtained from the adjoint action, with the commutative diagrams. On Lie algebras this gives f_s: s → g and ρ_g: g → Dér(s).

**Checked (SA04-R82-08).**
- 026 (80): if f' = g', then Δ(f)² = det f' = det g' = Δ(g)², so Δ(g) = εΔ(f) with ε² = 1. Since (f')' = Δ(f)·f, g = Δ(g)^{−1}(g')' = εf.
- 028: the affine group GL_2 ⋉ G_a² has dimension 4 + 2 = 6.
- 027: in characteristic 2, sl_2 has the central line O·H̃ (SA04-R82-07). The quotient sl_2/O·H̃ is a rank-2 module V, which is the extension he describes.

### 032-038: faithfulness of ρ_E; the polynomials F_n; tori and centralizers in GP(V)

**What he does.**
- **032.** E' acts faithfully on E. In the basis, ρ_E(xX + hH + yY) sends X̃ ↦ hX̃ − yH̃, Ỹ ↦ xH̃ − hỸ and H̃ ↦ −2xX̃ + 2yỸ, so it is 0 only for x = y = h = 0. Next one must "redéfinir ou préciser, en termes élémentaires, la construction de G̃ sur G".
- **034.** F_3 = T, F_4 = T − 1, F_5 = T² − T − 1, F_6 = T − 2, with F_n the minimal polynomial over Q of 1 + 2cos(2π/n) = 1 + ζ + ζ^{−1}. Then a map u with u(ζ_0) = ζ_0 + e_1, u(e_1) = e_2, u(e_2) = −e_1 + (α − 1)e_2.
- **035.** The smooth connected commutative 1-dimensional subgroups J of G correspond to Div_2^+(X), with Cent(J) = J. N(J)/J contains σ = −id_J, and its inverse image in N(J) is a J-torsor "comme X − Y". In characteristic 2, J_s ≅ G_a for the unipotent ones.
- **037-038.**
  - For u ∈ End(V), V of rank 2 with u_s ∉ k(s)·1, the commutant of u is O·Id + O·u. Indeed det(α + βu) = α² + αβ Tr u + β² det u (2), so the centralizer in GP(V) is P^1 − Q_{Tr u, det u}, a degree-2 divisor removed, étale iff Tr²u − 4 det u is a unit.
  - Question: is H the centralizer of its Lie algebra, or of any section that is nowhere the unit?

**Checked (SA04-R82-09).**
- 032: the kernel is 0 also when 2 = 0: then H̃ ↦ 0 for all, but X̃ ↦ hX̃ − yH̃ and Ỹ ↦ xH̃ − hỸ still force x = y = h = 0.
- 034: 1 + 2cos(2π/n) equals 0, 1, (1 + √5)/2 and 2 for n = 3, 4, 5, 6, with minimal polynomials T, T − 1, T² − T − 1 and T − 2.
  - For u ∈ GL_2 with eigenvalue ratio ζ, Tr²u/det u − 1 = 1 + ζ + ζ^{−1}. So F_n(Tr²/det − 1) = 0 is the condition for order n in PGL_2, the condition used for triangle groups in cote 85.
- 037: α·1 + βu is invertible iff α² + αβ Tr u + β² det u is, and that form's discriminant is Tr²u − 4 det u.

### 039-045: centralizers and normalizers of tori and of μ_p in forms of GP(1)

**What he does.**
- **039.** The commutator map v ↦ [u, v] on M_2 has rank ≤ 2 everywhere, and exactly 2 iff u is nowhere scalar. Again det(α + βu) = α² + αβ Tr u + β² det u.
- **040.**
  - If ghg^{−1} = λh, then gh²g^{−1} = h², so g ∈ C(h²), which suffices unless h² = 1, "(typique de car 2 !)".
  - Using the universal section α + βu_0, g(α + βu_0)g^{−1} = λ(α, β)(α + βu_0) forces λ = 1. So H is its own centralizer, and also the centralizer of any section nowhere of square 1. "Est-il le centralisateur de 𝔥 ?"
- **041.** gug^{−1} = u + λ gives 2λ = 0. In characteristic 2 a translation exchanges the eigenvalues; there the Lie centralizer of X (where [X, Y] = 2H = 0) is too big, while that of H is right.
- **042-043, Proposition.** Let G be a form of GP(1) and μ ⊂ G finite étale of odd prime rank p. Then:
  - a) the centralizer H of μ is smooth and commutative of relative dimension 1, with connected fibres in residue characteristic ≠ p;
  - b) H = N^0 for the normalizer N, and N/H ≅ {±1}_S acts on H by h ↦ h^{−1}.
  The proof lifts μ to SL(V), possible since p is odd. In residue characteristic p, u = id + v with v² = 0, and the commutant is the α + βv with α² = 1.
- **044.** Is every smooth subgroup of relative dimension 1 with connected fibres of the form C(𝔥)? Over a field yes, so this is a question of deformations of subgroups.

**Checked (SA04-R82-10).**
- 040: in α + βλ_0u_0 = λ(α + βu_0) the coefficient of 1 gives λα = α identically, so λ = 1 and then λ_0 = 1.
- 041: the trace of gug^{−1} = u + λ gives 2λ = 0.
- 043 b), over an algebraically closed field of characteristic ≠ p:
  - μ_p lies in a unique maximal torus T, its centralizer.
  - An element normalizing μ_p sends u to u^k, so its eigenvalue ratio ζ goes to ζ^k ∈ {ζ, ζ^{−1}}; hence k = ±1.
  - So N/T ≅ Z/2, acting by inversion.

### 046-052: quaternion algebras and their equivalent incarnations; the quadric Q ≅ P(V) × P(V)

**What he does.**
- **047.**
  - A quaternion algebra ℳ gives a form G of GP(1)_S, G̃ of SL(2)_S, the Lie algebras 𝔤 and 𝔤̃, a special quadratic module (E, q, ω) with E = 𝔤̃, a conic X in a projective plane P, and X as a P^1-bundle. "sont des équivalences de catégories fibrées".
  - The Codex-web text has "Module spécial quadratique de rg 2"; E = 𝔤̃ has rank 3.
  - For ℳ = End(V): X ≅ P(V) by L ↦ L^⊥ ⊗ L (2, 3).
- **048-049.**
  - Q = Var(Δ) ⊂ P^∨(ℳ) with Δ(u) = −det u (4, 5). Q ≅ P(V) × P(V) by u ↦ (Ker u, Im u) (6, 7), with inverse (L, M) ↦ L^⊥ ⊗ M.
  - Q is identified with the pairs (𝒜, ρ): 𝒜 = O_S ⊕ J ⊂ ℳ a special subalgebra with J = O_S·u, and ρ: 𝒜 → O_S the algebra homomorphism with kernel J (8-12).
- **050-051.**
  - The canonical involution of Q, exchanging the two factors, comes from the anti-automorphism u' = α^{−1}(^tu)α (13, 14), independent of ω. It satisfies (uv)' = v'u', u' = Tr u − u, u + u' = Tr u and uu' = det u (15-17), and exchanges Ker and Im. On pairs it is (𝒜, ρ) ↦ (𝒜, ρ∘') (18).
  - Q → P(𝔤̃) is the scheme of special subalgebras, and Q ≅ Spec(𝒜_Σ) for the universal one (19, 20).
- **052.** A proposition on a special subalgebra 𝒜 and an invertible L ⊂ V (continued on 053).

**Checked (SA04-R82-11).**
- 048: the nonzero rank-one 2×2 matrices, up to scalars, form the Segre quadric det = 0 in P³ ≅ P^1 × P^1, through (kernel, image).
- 050: for rank-one u, u' = adj(u) satisfies u·u' = u'·u = det u = 0. So Im u' ⊂ Ker u and Im u ⊂ Ker u', and since both have rank one the involution exchanges kernel and image.
- 047: the rank of E = 𝔤̃ is 3, not 2 (reading question in the Codex-web text).

### 052-058: special subalgebras, lines of the plane and degree-2 divisors on the conic; "jacobian" subgroups; the dictionary GP(1) ≅ SO(3)

**What he does.**
- **052-053, Proposition.** For a special subalgebra A and an invertible L ⊂ V (L̲ = L^⊥ ⊗ L isotropic) these are equivalent:
  - a) L̲ ⊂ A^⊥;
  - b) A preserves L;
  - c) some invertible J ⊂ A kills L;
  - d) L^⊥ ⊗ M ⊂ A for a line M ⊂ V.
  M is then unique, J = Ker(A → End(L)), and L ↦ (A → O) is a bijection.
- **053-054.**
  - AlgSpec(ℳ) ≅ P(𝔤̃) ≅ P̌(𝔤), the scheme of lines of the plane P (21).
  - Dr(P) ≅ Div_2^+(X), D ↦ D ∩ X = Y (22). Y ≅ Spec A (23), and Y = X^u, the fixed points of u (24).
- **055-056.**
  - Prop: g = ū invariates Y iff uAu^{−1} = A, and then g acts on Y as on Spec A.
  - The subgroup 𝒥 = V̌(A)^*/G_m ⊂ G is commutative, smooth and connected of relative dimension 1 (25). If 2 is invertible every such subgroup is of this "jacobien" form, being the centralizer of its Lie algebra. His margin: "à vérifier ! il faut car. rés. ≠ 2".
- **057-058, "Dictionnaire lié à GP(1) ≅ SO(3)".** Nine categories over S, to be shown equivalent: torsors under GP(1)_S, forms of GP(1)_S, forms of SL(2)_S, and so on.

**Checked (SA04-R82-12).**
- 052: for u ∈ End V and the rank-one x' ⊗ x (v ↦ ⟨v, x'⟩x), Tr(u∘(x' ⊗ x)) = ⟨ux, x'⟩. This vanishes iff ux ∈ x'^⊥ = L, which proves a) ⇔ b).
- 054: on a smooth conic X ≅ P^1 in P², every degree-2 divisor spans exactly one line (a secant, or the tangent for a double point), so D ↦ D ∩ X is bijective.
- 056: in characteristic 2 a unipotent G_a ⊂ PGL_2 can have a larger centralizer, as on 041 (the centralizer of X in the Lie algebra). This bears out his restriction "car. rés. ≠ 2".

### 058-064: the dictionary of nine (eleven) equivalent gerbes attached to GP(1) ≅ SO(3)

**What he does.**
- **058-059.** The categories over S:
  - GP(1)-torsors; forms of GP(1) and of SL(2);
  - forms of gp(1) and of sl(2);
  - quaternion algebras;
  - special quadratic modules of rank 3;
  - P^1-bundles (Drpr) and conics in planes (Quad).
  For the three categories marked (∗) the equivalence holds only over S prime to 2. "Un dictionnaire complet devrait comprendre … les 9 × 8 = 72 équivalences".
- **060-061.** Typical representatives over Z: R_0, G_0 = GP(1), G̃_0 = SL(2), gp(1), sl(2), M_0 = M_2(O), (E_0 = O³, q_0 = xy + z², ω), X_0 = P^1 and (P_0 = P², C_0 = V(q_0)).
- **061-063.** The actions of G_0 on each, among them ξ = [[z, x], [y, −z]] ↦ q_0(ξ) = −det ξ = xy + z² on sl(2) ≅ O³ (3)-(6). G_0 acts trivially on det, since Hom(GP(1), G_m) = 0. "Nous admettrons (pour ne pas nous éterniser...)" that all the maps GP(1) → Aut(𝒳_0) are isomorphisms (7), away from 2 in the cases (∗); his margin: "Expliciter le thm d'isomorphie".
- **064.** The functors from torsors are twists R ↦ R ∧^{GP(1)} 𝒳_0 (8). For P^1-bundles the twist is R ↦ R/B_0 (9), with B_0 the Borel subgroup.

**Checked (SA04-R82-13).**
- 062: det[[z, x], [y, −z]] = −z² − xy, so −det ξ = xy + z². This is the form of 007 with the identification (6).
- 063: Hom(PGL_2, G_m) = 0, since PGL_2 = SL_2/μ_2 and SL_2 has no nontrivial characters.
- The restriction "premier à 2" for the (∗) cases agrees with 022 and 027. In characteristic 2, sl_2 has a centre, and Aut(sl_2) is not GP(1) but an affine group of dimension 6.

### 065-071: the functors of the dictionary made explicit; quaternion algebras as the key

**What he does.**
- **065.**
  - The stabilizer of the section at ∞ (the line O·e_2) is the lower-triangular B̃'_0 = {[[λ, 0], [μ, λ^{−1}]]} (11).
  - g ↦ g·s_0 gives G_0/B_0 ≅ X_0 (13), hence R ∧ X_{0S} ≅ R/B_{0S} (14).
- **066-069.** The functors between the categories:
  - 𝒳 ↦ Isom(𝒳_0, 𝒳) to torsors (15-17);
  - 𝒳 ↦ Aut(𝒳) to forms of GP(1) (18);
  - G̃ ↦ G̃/Cent(G̃) (19); "le centre de G̃ est tjrs isom à μ_2 (de façon unique car Aut(μ_2) = 1)";
  - M ↦ V̌(M)^*/G_m (20);
  - G ↦ G̃, its simply connected cover (22);
  - G ↦ Lie G and G ↦ Lie G̃ (23, 24), each marked "∼?";
  - G ↦ Bor(G), the scheme of Borel subgroups, with X ≅ Bor(G) (25, 26);
  - M ↦ G̃ = Ker(det: V̌(M)^* → G_m), the reduced norm (29).
- **069-071.** "c'est M qui semble peut-être la meilleure clef":
  - centre M = O_S, and the reduced norm and trace (32, 33);
  - the exact sequences 1 → G_m → ℒ(M) → G → 1 (34) and 1 → G̃ → ℒ(M) → G_m → 1 (35), with their Lie algebra versions.

**Checked (SA04-R82-14).**
- 065: [[λ, 0], [μ, λ^{−1}]]·e_2 = λ^{−1}e_2, so the lower-triangular group stabilizes O·e_2.
- 066: Aut(μ_2) is trivial: Z[t]/(t² − 1) has only the automorphism t ↦ t^k with k ∈ (Z/2)^* = {1}. So the identification of the centre is unique, as he says.
- The "∼?" on (23)-(24) agree with the (∗) of 059: G ↦ Lie G̃ is an equivalence only where 2 is invertible.

### 071-079: the quaternion description: trace forms, sl_2 ⊂ M ↠ gp(1), f and f', Borels

**What he does.**
- **071-072.**
  - g̃ ↪ M ↠ g gives f: g̃ → g (36)-(38).
  - The form Φ(u, v) = Tr(uv) on M is symmetric and non-degenerate, so M ≅ M^∨ (39, 40). Since g̃ = (O·1)^⊥, this gives the pairing g̃ × g → O and g̃ ≅ g^∨ (41, 42).
  - Q(u) = −det u is smooth with polar form Φ_1(u, v) = −Tr u Tr v + Tr(uv) (43), which equals Φ on g̃.
- **073-074.**
  - q = −det on g̃, with φ(u, u) = 2q(u) (44). φ is dualizing except in characteristic 2.
  - Killing: Tr(ad u ad v) = 4φ(u, v) and Tr(ad u²) = 8q(u) (45).
  - A canonical basis ω of det g̃ = det M, descended from det(V̌ ⊗ V) ≅ O (46, 47), with δ'(q) = −ω^{⊗2} and δ(φ) = −2ω^{⊗2} (48, 49).
- **075-076.**
  - (E, q, ω) = (g̃, q, ω) (50). f is the map g̃ → g̃^∨ of φ (51), with the brackets as before; his margin: "Sans garantie -- il faut vérifier".
  - f': g → g̃, f'(ū) = Tr(u)·1 − 2u (55), with ff' = −2·id and f'f = −2·id (54).
  - P = P̌(g̃) ≅ P(g) and X = V(q) ⊂ P (56).
- **077-078.** Proposition: the Borel subgroups of G correspond to the B̃ = V̌(L̃) ∩ V(M)^*, with B = B̃/G_m (57). Then a criterion for a subbundle L of g of corank 1.

**Checked (SA04-R82-15).**
- 072: det(u + v) = det u + det v + Tr u Tr v − Tr(uv) gives Φ_1 = −Tr u Tr v + Tr(uv), which is Φ on trace-zero elements.
- 076:
  - f'(ū) = Tr u − 2u is well defined on g = M/O·1, since u + λ gives the same value, and it has trace 2Tr u − 2Tr u = 0.
  - For u ∈ g̃, f'f(u) = −2u, and ff'(ū) is the class of −2u. So ff' = f'f = −2·id, with det f = Δ = −2 as on 019.
- 073: on sl_2 the Killing form is 4·Tr(uv). For trace-zero u, u² = −det u, so Tr(ad u²) = 4·(−2 det u) = 8q(u). This agrees with Cas_E = −2Δφ of 023.

### Addendum to cote 82: scan 031, and the ends of 058-079

My first view missed scan 031 and cut 058-079 after about 1,100-1,300 characters. These parts were read afterwards.

**What he does.**
- **031.**
  - The dictionary between the group-theoretic and the bilinear constructions. 𝔰, 𝔤, f_𝔰 and ρ_𝔤 give the bracket [ , ]_{φ'} on E, the bracket [ , ]_φ on E', the map f: E → E' and ρ_E.
  - The composite 𝔤 → Dér(𝔰) ≅ Dér(E) → End(E) is the representation of Lie G coming from the tautological action of G on E.
  - Construction: E' acts on E through endomorphisms that preserve q and ω infinitesimally, i.e. through 𝔤, which gives a bracket-compatible j: E' → 𝔤. "Je dis que c'est un iso": both sides are locally free of rank 3, so injectivity on geometric fibres suffices. That is the faithfulness of ρ_E proved on 032 (checked in the section on 032-038).
- **058-077 (ends).**
  - The rest of the dictionary: C_3 = Quat(O_S), the Azumaya algebras of rank 4; C_5 = Drpr(S), the P^1-bundles; C'_5 = Quad(S), the pairs (P, X) of a P²-bundle and a smooth conic; C_4, the special orthogonal modules (E, q, ω) of rank 3 with d(q) = −ω^{⊗2}.
  - The trivial objects 𝔤_0 = 𝔤𝔭(1), 𝔤̃_0 = 𝔰𝔩(2) and M_0 = M_2(O) (060).
  - GL(2) acting on M_0 through GL(2)/G_m = GP(1) (061, (2)).
  - The sequences (34), (35), (34'), (35') (070); φ = Φ|𝔤̃ × 𝔤̃ = Φ_1|𝔤̃ × 𝔤̃ with φ(u, v) = Tr uv (072, (42)); (47) on 073; (52) on 075 with the margin "Sans garantie"; (57) on 077.
  - All of this is in the sections above except (47): "det(V̌ ⊗ V) ≅ det V̌ ⊗ det V ≅ (det V)^{−1} ⊗ det V ≅ O_S".
- **078.**
  - A corank-1 subbundle L ⊂ 𝔤 is Lie(B) iff its orthogonal L^⊥ ⊂ 𝔤̃ satisfies q|L^⊥ = 0. His margin NB: equivalently, L^⊥ consists of elements of square zero in M.
  - This determines q on 𝔤̃ up to an invertible scalar, hence up to sign if it is to be defined over every base compatibly.
  - His margin question: "suffit-il que L soit une ss-Algèbre de Lie i.e. stable par crochet ??"
- **078-079, characteristic 2.**
  - O_S·1 ⊂ 𝔤̃ (58). The morphism X → P(𝔤̃) (59) sends a Borel, i.e. an isotropic line L of 𝔤̃, to its φ-orthogonal.
  - That orthogonal contains O_S·1, the kernel of φ and of f, so (59) factors through X → P(𝔤̃/O_S) (60), itself a P^1-bundle.
  - If (60) were a monomorphism it would be an isomorphism, and X would be trivial for Brauer, "or il n'est pas vrai qu'en car 2 les fibrés en droites projectives soient tjrs banals !"
  - In fact P(𝔤̃/O_S) ≅ X^{(2)} (61), and (60) is the canonical X → X^{(2)}, radicial and finite locally free of rank 2, "nullement un monomorphisme".

**Checked (SA04-R82-16): 078-079.**
- **078 on the split form.** For L = Lie(B) = ⟨E_11, E_12⟩ mod scalars, the trace pairing gives L^⊥ = O·E_12, which is isotropic: q(E_12) = −det E_12 = 0. Conversely, a nowhere-zero u ∈ 𝔤̃ with u² = −det u = 0 fixes the line ker u = im u, whose stabilizer is a Borel. The NB is Cayley-Hamilton: u² = Tr(u)u − det u.
- **His margin question.**
  - Where 2 is invertible, the answer is yes, even scheme-theoretically. 𝔤̃ ≅ 𝔤 by f, and for L = u^⊥ with basis v, w, the bracket condition is Tr(u[v, w]) = 0. That is a mixed product, a unit multiple of q(u).
  - In characteristic 2 the answer is no, and as badly as possible. In 𝔭𝔤𝔩_2 we have [x̄, ȳ] = E_11 − E_22 = 1 ≡ 0, and ad h̄ is the identity on ⟨x̄, ȳ⟩. So every plane of 𝔭𝔤𝔩_2 is a subalgebra: ⟨x̄, ȳ⟩ itself, and every ⟨h̄ + v, w⟩ with v, w ∈ ⟨x̄, ȳ⟩. The Borel subalgebras are only a conic's worth of them.
- **(61).** On 𝔤̃ = {[[a, b], [c, a]]} in characteristic 2:
  - q = a² + bc and φ(u, u') = bc' + b'c, whose kernel is O·1.
  - X ≅ P^1 by [s : t] ↦ (st, s², t²), and the φ-orthogonal of (st, s², t²) is the line [b : c] = [s² : t²] of 𝔤̃/O·1.
  - So (60) is the relative Frobenius, of degree 2.
  - It agrees with Brauer theory: the Frobenius pull-back multiplies the 2-torsion class of a P^1-bundle by 2, so X^{(2)} is always the projective bundle of a vector bundle, as (61) says.

**Checked (SA04-R82-17): (47) on 073.** For V of rank 2, det(V̌ ⊗ V) ≅ (det V̌)^{⊗2} ⊗ (det V)^{⊗2}, not det V̌ ⊗ det V. The conclusion ≅ O_S, and its GL(V)-invariance, stand (correction SA04-K82-01). The sign ambiguity he discusses on 074 is that of the identification det(A ⊗ B) ≅ (det A)^{rk B} ⊗ (det B)^{rk A}.

## Full pass, cote 85 (K85-01 to -07, Codex-web, GPT-6 Astra at reasoning effort max)

### 002-008: the programme; regular maps from the triangle group; Theorem: representations of Γ = ⟨τ_0, τ_1, τ_2⟩ in forms of GP(1) are classified by (α_0, α_1)

**What he does.**
- **002, the programme.** The centre of Γ = G_2/−; representations of G_0 = Z/2, D_∞ = G_1 and G_2, non-degenerate, singly and doubly degenerate (quaternions, octahedron); projective representations of G_2 over fields, especially finite ones; tame genus-0 covers of the sphere minus three points; finite regular hyperpolygons; Pythagorean Schwarz systems (the case G_5) and the groups of elementary operations.
- **003.**
  - Every epimorphism of L_3 = ⟨ρ_0, ρ_1, ρ_2 | ρ_0ρ_1ρ_2 = 1⟩ onto a finite group gives a finite regular 3-weighted map. So every L_2 → GP(1, k) with finite image does, interpreted by regular hyperpolygons.
  - The Pythagorean Schwarz systems give 44 types of hyperpolygons, stable under S_3 and the elementary operations, with one smallest finite quotient of L_2 covering them all, "et fort gros!". The canonical ones are the Pythagorean n-gons of GP(1) and the regular bipyramids.
- **004-007, Theorem.**
  - Γ is generated by involutions τ_0, τ_1, τ_2 with τ_0τ_2 = τ_2τ_0, and ρ_0 = τ_0τ_1, ρ_1 = τ_1τ_2.
  - The category of pairs (G, φ), with G a form of GP(1)_S and φ: Γ → G(S) such that ρ_0², ρ_1² ≠ 1 and ρ_0, ρ_1 do not commute in every fibre, maps fully faithfully onto the discrete category of (α_0, α_1) ∈ O² with α_0 + 2, α_1 + 2 and α_0 + α_1 invertible (∗), via α_i = A(ρ_i).
  - The proof goes through the regular 2-polyhedron: β_i = α_i + 2, 4cos²θ_i = φ(a_i, a_{i+1})²/(f(a_i)f(a_{i+1})) = β_i, so α_i = 2cos 2θ_i.
  - "On a un peu salopé la présentation, qui suppose car. rés. ≠ 2", with the prolongation principle invoked.

**Checked (SA04-R85-04).**
- For g ∈ PGL_2 with lift u, A(g) = Tr²u/det u − 2 = ζ + ζ^{−1}, with ζ the ratio of eigenvalues; for a rotation by ϑ this is 2cos ϑ. A product of reflections in lines at angle θ is a rotation by 2θ, so α = 2cos 2θ, as on 006.
- Conditions (∗). The unit normals of the three mirrors (with τ_0 ⊥ τ_2) have Gram matrix [[1, −cos θ_0, 0], [−cos θ_0, 1, −cos θ_1], [0, −cos θ_1, 1]], of determinant 1 − cos²θ_0 − cos²θ_1. With cos²θ = (2 + α)/4 this vanishes iff α_0 + α_1 = 0. So "α_0 + α_1 invertible" is the smoothness of the quadratic form, and α_i + 2 ≠ 0 excludes θ_i = π/2, i.e. ρ_i² = 1.
- 007: "(α_0 + 2)(α_0 − 2)(α_0 + α_1) inv." does not match (∗), which needs (α_0 + 2)(α_1 + 2)(α_0 + α_1), as 004-005 and 008 have it. The scan (viewed at 400 dpi) has (α_0 − 2) in the ink, so this is the author's slip (SA04-K85-02), not a misreading. Michel Hua's project notes the same.

### 008-015: prescribed orders ν_0, ν_1; the finite cases S_4, S_4 × Z/2, Z/2 × A_5; the degenerate (dihedral) representations

**What he does.**
- **008.** With prescribed orders: C(ν_0, ν_1) ≅ C'(ν_0, ν_1), the pairs with (α_0 + 2)(α_1 + 2)(α_0 + α_1) invertible and Ψ_{ν_i}(α_i) = 0. This rests on "ρ_i of exact order ν_i ⇔ Ψ_{ν_i}(α_i) = 0", plus ν_i invertible when ν_i is not prime. (This settles the reading of 007: the conditions are (α_0 + 2)(α_1 + 2)(α_0 + α_1).)
- **009-010.**
  - A) ν_0 = ν_1 = 3, Γ ≅ S_4. The category is empty unless 2 is invertible. In characteristic 2, ρ_0 and ρ_1 always commute and the representation factors through S_3. Over Z[1/2] there is exactly one (G, φ), and it is faithful.
  - B) ν_0 = 4, ν_1 = 3, Γ = S_4 × Z/2 (octahedral generators): again characteristic 2 must be excluded.
- **011, C) ν_0 = 3, ν_1 = 5, Γ = Z/2 × A_5.**
  - α_0 = −1 and α_1 = α with α² + α − 1 = 0. Then α + 2 and α − 1 are units with inverses −α + 1 and −α − 2.
  - Thm: the (G, φ) with φ|A_5 nontrivial on every fibre correspond to the sections α with α² + α − 1 = 0, with no restriction on S. φ is trivial on Z/2, and his margin says to leave the Z/2 out of the statement.
- **013-014, Prop.** For involutions τ_i in G = Aut(Y) over an algebraically closed field, with (τ_0τ_2)² = 1, these are equivalent:
  - A) a degree-2 divisor of Y is stable, i.e. the τ_i lie in N(T) or in a Borel;
  - A') their extensions to the enveloping plane fix a line;
  - C) ρ_0² = 1, or ρ_1² = 1, or ρ_0ρ_1 = ρ_1ρ_0;
  - D) they generate D_n, or D_n × Z/2 (n even).
  Then parts of the proof.

**Checked (SA04-R85-05).**
- Exact order ν and α = ζ + ζ^{−1}:
  - order 3 gives α = 2cos(2π/3) = −1, root of Ψ_3 = α + 1;
  - order 4 gives α = 0;
  - order 5 gives α = 2cos(2π/5) or 2cos(4π/5), the two roots of α² + α − 1.
- A): (α_0 + 2)(α_1 + 2)(α_0 + α_1) = 1·1·(−2). B): 2·1·(−1) = −2. So 2 must be invertible in both cases, as he says.
- C):
  - N(α + 2) = 4 + 2(α + α') + αα' = 4 − 2 − 1 = 1, and N(α − 1) = αα' − (α + α') + 1 = 1. Both are units of Z[α], so there is no restriction on S.
  - The inverses: 1/(α + 2) = α' + 2 = 1 − α and 1/(α − 1) = α' − 1 = −α − 2, as he writes.

### Addendum to 002-015: the ends of 002, 003, 005-007, 010, 013-015

My first view cut these scans after about 1,200 characters. Their ends were read afterwards.

**What he does.**
- **002.** The programme also lists the structure of the groups of elementary operations "et relations avec Gal(Q̄/Q)", and ③ the determination of the Pythagorean hyperpolygons.
- **003.** The "degenerate" representations are those that correspond, in three ways, to representations of D_∞ × Z/2. The "hyperdegenerate" ones are the abelian representations of G_2. All of them are stable under 𝔖_3 and the elementary operations.
- **005.** The theorem in full. The functor C → C', (G, φ) ↦ (α_0(φ), α_1(φ)), is fully faithful, and it is an equivalence when Γ = G_2 = ⟨τ_0, τ_1, τ_2 | τ_i² = (τ_0τ_2)² = 1⟩. In other words:
  - a) C is rigid: the centralizer of φ in G(S) is {1};
  - b) two objects are isomorphic iff their α_0 and α_1 agree;
  - c) for Γ = G_2, every (α_0, α_1) satisfying (∗) is realized, uniquely up to unique isomorphism.
- **006.** The proof of A(ρ_Y) = α = 2cos ϑ. Locally fppf f = x² + yz and ρ_ζ(x, y, z) = (x, ζy, ζ^{−1}z), with α = ζ + ζ^{−1}. Since ζ ↦ ρ_ζ is a monomorphism G_m → G, A(ρ_ζ) = ζ + ζ^{−1}: this is the characterization of A given on 024.
- **007.** "[ν_i premier (impair puisque ν_i ≥ 3)]". The subcategory C(ν_0, ν_1) asks, in every fibre, a) ρ_0 and ρ_1 of exact orders ν_0 and ν_1, and b) ρ_0 and ρ_1 not commuting.
- **010.** Case B) (ν_0 = 4, ν_1 = 3):
  - a) in characteristic 2 the representation factors through Z/2 × 𝔖_3 ≅ D_6;
  - b) where 2 is invertible there is exactly one (G, φ) not factoring through D_6 in any fibre. That φ is trivial on the centre Z/2 of Γ and embeds 𝔖_4 in every fibre.
- **013.**
  - NB: in (D), if char k ≠ 2, the D_n × Z/2 may be replaced by D_∞ × Z/2.
  - Proof: A ⟺ A' by the dictionary (degree-2 divisors of Y ↔ lines of C), and A ⟺ B because the stabilizers of degree-2 divisors are the groups in B.
  - The groups H(k) are products T·U with T and U commutative and ₂T of order 1 or 2.
  - B ⟹ C: if ₂T = {1} (a Borel in characteristic 2), the involutions lie in U, so the image Γ' is commutative.
- **014.** A) to C'') are equivalent, and D ⟹ C''. To get B) and C') ⟹ D, it suffices that every subgroup of a Borel or an N(T) that is a quotient of D_∞ × Z/2 be isomorphic to D_∞ × Z/2, to a D_n or to a D_n × Z/2.
- **015.**
  - Cor 1: the quotients of D_∞ are the D_i (i ≥ 1, finite or infinite) and the trivial group.
  - Cor 2: the quotients of D_∞ × Z/2 are the D_i × Z/2 and the D_i. Margin: "D_i × Z/2 ≅ D_{2i} si i impair".

**Checked (SA04-R85-08).**
- **005 a) over a field.** No ρ_i is an involution (α_i + 2 ≠ 0), and ρ_i ≠ 1, since otherwise ρ_0 and ρ_1 would commute. So each centralizer is the torus or unipotent group fixing Fix(ρ_i) pointwise, and an element centralizing φ fixes Fix(ρ_0) ∪ Fix(ρ_1).
  - Since ρ_0 and ρ_1 do not commute, the two fixed sets differ. Either the union has three points, or it is a torus pair {a, c} together with a unipotent fixing c.
  - In both cases only 1 survives.
- **006.** The conic x² + yz = 0 is parametrized by [s : t] ↦ (st, s², −t²). On it ρ_ζ is [s : t] ↦ [ζs : t], with eigenvalue ratio ζ, hence A = ζ + ζ^{−1}.
- **010 b).** W(B_3) = 𝔖_4 × Z/2 acts on R³ with centre −1. The isomorphism O(3) → SO(3) × {±1} followed by the projection (g ↦ det(g)·g) kills the centre and leaves the rotation group 𝔖_4 of the cube.
- **010 a).** Z/2 × 𝔖_3 ≅ D_6.
- **013.** In characteristic 2, k^* has no element of order 2, so every involution of a Borel k^* ⋉ k lies in k, which is commutative.
- **015, Cor 2.** If N ⊄ D_∞ × 0, then N maps onto the factor Z/2. Then D_∞ maps onto Γ, and Cor 1 applies.
- **015, the margin.** For i odd, D_{2i} = ⟨r², s⟩ × ⟨r^i⟩ with ⟨r², s⟩ ≅ D_i.

### 015-021: subgroups of D_∞; which D_i embed in GP(1, k); representations of D_∞ classified by (α, R); the groups U(β)

**What he does.**
- **015, Lemme 1.**
  - The subgroups of D_∞ = ⟨σ_0, σ_1⟩ (u = σ_0σ_1) are:
    - N_i = ⟨u^i⟩, normal with quotient D_i;
    - N_ij = ⟨u^i, σ_0u^{j'}⟩, isomorphic to D_∞ (i ≠ 0) or Z/2 (i = 0), normal iff i ∈ {1, 2}.
  - N_ij contains a conjugate of σ_0 iff j ∈ 2Z/iZ. All these subgroups are distinct and there are no others.
- **016-017, Proposition.** For k algebraically closed of characteristic p, D_i embeds faithfully in GP(1, k):
  - a) always if p = 0 or i = 1;
  - b) for i = 0 (D_∞), iff k is not algebraic over F_p;
  - c) for i ≥ 2, iff p ∤ i or i = p.
- **017-019, Theorem.**
  - It is stated for the pairs (G, φ: D_∞ → G(S)) with u_s² ≠ 1 in every fibre, i.e. τ_0 and τ_1 do not commute. By 017 this forces a_0 ∉ H_1, and by 018 locally fppf a regular polygon with β = α + 2 invertible, i.e. a smooth quadric.
  - The claim: these pairs are equivalent to the pairs (α, R), with α + 2 invertible and R a torsor under U(2 − α).
  - U(β) is the group of λ with 1 + λβ invertible, under λ ⊕ λ' = λ + λ' + λλ'β.
  - The model is the regular polygon of invariant α, with "U_{2−α} ≅ Zentr(φ_α) = Aut(G_α, φ_α)". The twist is formed with "R … un torseur sous G_α" (the ink, viewed at 250 dpi).
  - The quasi-inverse (019) takes α = A(u) and R = H_1 ∖ {c ∪ d}.
  - **This theorem is false as stated (SA04-K85-01).** U_{2−α} is the centralizer of u, not of φ. The automorphism group of (G, φ) is ₂U_{2−α}, as his own Proposition on 020 says. The classification must use torsors under ₂U_{2−α}, which is ≅ μ_2 where 2 − α is invertible. Michel Hua's project found this, with a counterexample over Q checked in Lean, and I re-derived it (SA04-R85-07).
- **019-020.**
  - Aut(G, φ) ≅ ₂(U_β).
  - Cor. 1: if β = 2 − α is invertible, U_β ≅ G_m by λ ↦ 1 + λβ; its image T is the unique maximal torus containing u, and Aut(G, φ) = ₂T ≅ μ_2.
  - Cor. 2: if α = 2 then U ≅ G_a, its image is the unique maximal unipotent subgroup containing u, Aut = 1 when 2 is invertible, and "Aut = U ≅ G_a" in characteristic 2. That last case is empty in C: there α + 2 = 4 = 0 is not invertible, and a unipotent u has u² = 1. Michel Hua's project notes this too.
  - Cor. 3 (020-021): for Γ = D_∞ × γ, the (G, φ) correspond to the triples (α, R, φ_0), with R a torsor under "U_{β=α−2}" and φ_0: γ → ₂U_β(S). The sign α − 2 is harmless, since λ ↦ −λ is an isomorphism U_{−β} ≅ U_β. But R must again be a ₂U-torsor, by SA04-K85-01.
- **021, Proposition.** For n ≥ 3 and φ: D_∞ → G, these are equivalent: a) u^n = 1 with u_s of exact order n in every fibre; b) φ factors through a mono D_n ↪ G. In terms of α: 1°) n·1_S is invertible or n is an odd prime, and 2°) Ψ_n(α) = 0, where Ψ_n is the "half-cyclotomic" polynomial of index n.

**Checked (SA04-R85-06).**
- 018: 1 + (λ ⊕ λ')β = (1 + λβ)(1 + λ'β), so λ ↦ 1 + λβ is a homomorphism to G_m: an isomorphism for β invertible, the additive law for β = 0. ₂U_β is given by λ(2 + λβ) = 0, as on 019: (1 + λβ)² = 1 gives μ_2 when β is a unit, and 2λ = 0 gives 1 or G_a when β = 0.
- 016 c):
  - In PGL_2 over an algebraically closed field of characteristic p, the elements of finite order are the semisimple ones of order prime to p and the unipotent ones of order p.
  - D_p embeds: u = [[1, 1], [0, 1]] is inverted by diag(−1, 1) for p odd; for p = 2, D_2 is a Klein group inside G_a.
  - No element has order 2p, since the centralizer of a unipotent element is unipotent.
- 016 b): an element of infinite order exists iff k^* has one, i.e. iff k is not algebraic over F_p.

**Checked (SA04-R85-07): the theorem of 017-019 is false as stated.**
- **The counterexample.** Over Q take α = −6. Then 2 − α = 8 is invertible, U_8 ≅ G_m and H^1(Q, G_m) = 0, so C' has a single object up to isomorphism.
  - In PGL_2(Q) take (t_0, t_1) = (diag(1, −1), [[1, 1], [−2, −1]]) and (t_0', t_1') = ([[0, 1], [−1, 0]], [[1, 0], [2, −1]]). These are pairs of involutions (trace 0).
  - Their products u = [[1, 1], [2, 1]] and u' = [[2, −1], [−1, 0]] both have trace 2 and determinant −1, so α = 4/(−1) − 2 = −6, and u², u'² are not scalar.
  - det t_0 = −1 and det t_0' = 1 differ by a non-square. Conjugation in PGL_2(Q) changes determinants by squares, and Aut(PGL_2) = PGL_2. So the two pairs are non-isomorphic objects of C with the same α, and C is not equivalent to C'.
  - This is Michel Hua's project's example, recomputed here.
- **The automorphisms say the same.**
  - Aut(α, R) = U_{2−α}(S) is infinite here.
  - The centralizer of φ(D_∞) is ₂U_{2−α}. Cent(u) is the image of U_{2−α}: the torus, or the unipotent group when α = 2. Since t_0ut_0 = u^{−1}, t_0 acts on Cent(u) by inversion, and the elements it fixes are those with x² = 1.
- **The corrected statement.** By his own reduction on 018, every pair is locally fppf isomorphic to the regular-polygon model of the same α. So the pairs with invariant α form a neutral gerbe, banded by the commutative group ₂U_{2−α}. Hence C is equivalent to the category of pairs (α, R) with α + 2 invertible and R a ₂U_{2−α}-torsor.
  - Over a field K with 2 − α ≠ 0 the classes form H^1(K, μ_2) = K^*/K^{*2}. For the split group the class is read off from det t_0 mod squares.
- **One more point.** "u_s² ≠ 1" implies "α + 2 invertible", but not conversely: t_0 = t_1 gives u = 1 and α = 2 (Michel Hua's project).

### 022-029: D_i × Z/2 in GP(1, k); the invariant A of a section of a form of GP(1) or SL(2): unipotent elements, conjugacy, the failure at α = ±2, the polynomials G_n

**What he does.**
- **022, Corollary.** Let k be algebraically closed, i even ≥ 0, and (∗) the existence of an injective D_i × Z/2 → GP(1, k).
  - a) "Si i ≠ 0, donc i ≥ 2, la condition (∗) est vérifiée sss car. k = 2". His margin: "distinguer le cas i = 2 dans dém."
  - b) For i = 0, (∗) holds iff char k = 0, or char k > 0 and k is not algebraic over the prime field.
  - Proof of a) for i = 2i' ≥ 4: D_i embeds iff p ∤ i or i = p. In the first case α ≠ 2, so Aut(G, φ|D_i) ≅ μ_2, and the generator σ of Z/2 goes to 1 or to u^{i'}.
- **023.** A title leaf: "(9 p) Invariants des sections des formes de GP(1) etc".
- **024.**
  - For G a form of GP(1) or SL(2), the class functions I(G) = Hom_sch(G, E^1_S)^G form a representable functor. There is a canonical isomorphism A: I(G) ≅ E^1_S, characterized by A(i(λ)) = λ + λ^{−1} for every monomorphism i: G_m ↪ G, after any base change. So A(1) = 2.
  - An involution σ (σ² = 1, σ_s ≠ 1) has A(σ) = −2. This is clear when 2 is invertible (σ lies in a maximal torus, with λ = −1); in general by "un argument de coeff universels". His margin: for GP(1), σ is a "réflexion"; for SL(2) in residue characteristic ≠ 2, it generates the centre.
- **024-025.**
  - A unipotent u (locally fpqc u = i(t) for a monomorphism i: Aff(1) = G_m ⋉ G_a → G) has A(u) = 2. More generally A(i(λ, t)) = λ + λ^{−1}.
  - The proof: f(λ, t) = A(i(λ, t)) has f(λ, 0) = λ + λ^{−1} and is invariant under conjugation, and (0, t)(λ, 0)(0, −t) = (λ, λ^{−1}t − t). So f = λ + λ^{−1} wherever λ^{−1} − 1 is invertible, and everywhere "par prolongement".
  - Then: "Une condition nécessaire pour que u soit unipotent est donc que A(u) = 1" (sic). The condition is sufficient over a field, since over an algebraically closed field every element lies in a Borel. "J'ignore ce qui en est dans le cas général."
- **026, Proposition.**
  - Let u, u' have A(u) − 2 and A(u) + 2 invertible ("u_s² non unipotent"). Then u and u' are conjugate locally fpqc "(ou encore, conjugués si G forme de GP(1))" iff A(u) = A(u'). His margin: over a field this holds without restriction on A, for non-central u.
  - Proof: each lies in a unique maximal torus. By the conjugacy theorem and localization the torus is G_m, and u, u' are roots λ, λ' of t² − αt + 1 = 0. Its discriminant (α − 2)(α + 2) is invertible, so it defines an étale double cover, and locally λ' = λ or λ^{−1}, which are exchanged by the Weyl element.
- **026-027, the points where α(s) = ±2.**
  - Over an Artinian base with λ' = λ + μ and 𝔪μ = 0, the equation λ' + λ'^{−1} = λ + λ^{−1} holds automatically. But λ' = λ or λ' = λ^{−1} pins μ to at most two values, so the statement fails "si k n'est pas réduit à 2 él".
  - His margin: "une propriété générale des morphismes « ramifiés » (non nets)", a continuum of infinitesimal solutions from the first order on.
- **028, Remark.**
  - A homomorphism j: G_m → G with flat kernel factors as λ ↦ λ^n followed by a monomorphism. So A(j(λ)) = λ^n + λ^{−n} = G_n(λ + λ^{−1}), where G_n ∈ Z[U] is the universal monic polynomial of degree n expressing T^n + T^{−n} in Z[T, T^{−1}]^σ = Z[U].
  - Example 1: for p: G̃ → G = G̃/μ_2, with G̃ a form of SL(2), A(p(u)) = A(u)² − 2, and A(u) = Tr u on G̃.
  - Example 2: for V locally free of rank 2 and u ∈ Aut(V), A(u_C) = (Tr u)²/det u − 2, by writing u = tv locally with v ∈ SL(V).
- **029.**
  - With eigenvalues λ_1, λ_2: A = λ_1/λ_2 + λ_2/λ_1. A pseudo-reflection with parameter λ = det u gives λ + λ^{−1}.
  - Proposition: if u² = 1 and u_s ≠ 1 everywhere (with residue characteristic ≠ 2 for forms of SL(2)), then A(u) = −2, and "la réciproque [est] vraie si S est réduit".
  - The proof with 2 invertible: u lies in a unique maximal torus (for GP(1)), or generates the centre μ_2 (for SL(2)). So locally u is the section −1 of G_m. It continues on 030.

**Checked (SA04-R85-09).**
- **022, with its corrections (SA04-K85-03).**
  - i = 2: (Z/2)³ embeds iff char k = 2. In characteristic 2 it lies in G_a(k) = k; in other characteristics the elementary abelian 2-subgroups of PGL_2(k) have order at most 4.
  - i = 2i' ≥ 4: in characteristic 2, GP(1, k) has no element of even order > 2, so D_i does not embed at all. In other characteristics his proof applies: the centralizer of D_i is {1, u^{i'}} ⊂ D_i. So (∗) never holds for i ≥ 4, and "sss car. k = 2" is right only for i = 2, the case his margin sets apart.
  - i = 0: in characteristic 2, an element u of infinite order is semisimple and its centralizer is a torus T. The elements of T fixed by the inversion that t_0 induces satisfy x² = 1, hence x = 1, so the factor Z/2 has nowhere to go and characteristic 2 must be excluded from b). In characteristic 0, or p > 2 with k transcendental, u = diag(λ, 1) with λ of infinite order, t_0 antidiagonal and σ = diag(−1, 1) give an embedding.
  - Michel Hua's project states the same three conclusions.
- **024.**
  - For PGL_2, A is Tr²/det − 2 on a lift (for diag(λ, 1) this is λ + λ^{−1}); for SL_2, A = Tr.
  - An involution of PGL_2 has trace 0, so A = −2, in every characteristic: in characteristic 2 it is unipotent, and −2 = 2.
- **025.**
  - With the action x ↦ λx + t, conjugating (λ, 0) by (1, t) gives (λ, (1 − λ)t); his convention gives (λ, (λ^{−1} − 1)t). Either way the conjugates of (λ, 0) cover the locus where λ − 1 is a unit, which is schematically dense in G_m × G_a. So A(i(λ, t)) = λ + λ^{−1}, and a unipotent u has A(u) = 2, not 1 (SA04-K85-04).
  - Over a field, A(u) = 2 gives (λ − 1)² = 0, so λ = 1: the condition is sufficient there, as he says.
- **His "J'ignore" on 025 has a negative answer.**
  - Over k[ε]/(ε²), every u = 1 + εX ∈ PGL_2 has Tr² = 4 + 4εTr X and det = 1 + εTr X, hence A(u) = 2.
  - Conjugation acts on the first-order part X by the adjoint action of PGL_2(k), so u is unipotent only if X is ad-nilpotent modulo scalars.
  - So u = diag(1 + ε, 1) has A(u) = 2 and is not unipotent.
- **026.**
  - The étale double cover gives local conjugacy, as he says. "Conjugués si G forme de GP(1)" holds over a field: lifts with the same characteristic polynomial up to a scalar are conjugate in GL_2(K), or by Skolem-Noether in a quaternion algebra.
  - It fails over a general base (SA04-K85-05). On a smooth affine complex curve S with a line bundle L of order 3, O² ≅ L ⊕ L^{−1}. Take u = diag(2, 1) on O ⊕ O, and u' acting as 2 on L and as 1 on L^{−1}. They have the same A = 5/2, with A ± 2 invertible, and they are locally conjugate.
  - But a g ∈ PGL_2(S) with gug^{−1} = u' would carry the eigenline bundles to the eigenline bundles up to one twist N: O ≅ L ⊗ N and O ≅ L^{−1} ⊗ N. So L² ≅ O, which contradicts order 3.
  - Michel Hua's project gives an example of the same kind, over a Dedekind base.
- **027.** With λ = ±1 and λ' = λ(1 + aε) over k[ε], λ'^{−1} = λ(1 − aε) and λ' + λ'^{−1} = λ + λ^{−1}. But λ' ∈ {λ, λ^{−1}} only for a = 0. So the statement fails at α = ±2 over every field, F_2 included; his "si k n'est pas réduit à 2 él" is a safe sufficient condition. The pair u = 1, u' = diag(1 + ε, 1) shows it on the group.
- **028.**
  - G_1 = U, G_2 = U² − 2, G_3 = U³ − 3U and G_{n+1} = UG_n − G_{n−1}, so G_n is monic of degree n.
  - Example 1: A(p(u)) = Tr(u)² − 2 when det u = 1.
  - Example 2 and 029: (λ_1 + λ_2)²/(λ_1λ_2) − 2 = λ_1/λ_2 + λ_2/λ_1, and a pseudo-reflection (eigenvalues λ, 1) gives λ + λ^{−1}.
- **029: the converse needs S reduced.** Over k[ε], ũ = [[ε, 1], [1, 0]] has Tr² = ε² = 0, hence A = −2, but ũ² = [[1, ε], [ε, 1]] is not scalar.

### 030-034: involutions (end); the order of u read on α through F_n and Ψ_n; the theorem for forms of SL(2); finite subgroups of GP(1) (start)

**What he does.**
- **030, the involution proposition (end).**
  - For forms of GP(1) it holds without restriction on residue characteristics, "car le schéma des « réflexions » dans GP(1)_Z est lisse sur Spec Z".
  - For SL(V): Cayley-Hamilton gives u² = id ⟺ (Tr u)u = 2·id, from which "Tr u = −2" is to be concluded. An infinitesimal induction Tr u_n = −2 ⟹ Tr u_{n+1} = −2 is begun, with the margin "bien peu clair".
- **030, Proposition.** Let G be a form of GP(1) or SL(2), u a section, α = A(u), (α + 2)(α − 2) invertible, n ≥ 3.
  - F_n and Ψ_n ∈ Z[U] are the monic polynomials with distinct roots ζ + ζ^{−1}, where ζ runs over the n-th roots of 1 other than ±1 (for F_n), resp. the primitive n-th roots (for Ψ_n).
  - The claims: u^n = id ⟺ "F_n(α) = 1" (sic, for = 0); and u^n = id with every u_s of exact order n ⟺ Ψ_n(α) = 0.
  - His margin, without the hypothesis on α: [u^n = id, the u_s of exact order n, n prime to the residue characteristics] ⟺ [Ψ_n(α) = 0 and α² − 4 invertible].
  - Proof: u lies in a unique maximal torus ≅ G_m, as a section λ with α = λ + λ^{−1}, and the rest is "calcul standart".
- **031.**
  - Cor. 1 (residue characteristics ≠ 3): u³ = id with all orders 3 ⟺ α = −1; "resp." u⁶ = id with all orders 6 ⟺ α = +1.
  - Cor. 2 (≠ 2): order 4 ⟺ α = 0.
  - Cor. 3 (≠ 5): "u^5 = 0" (sic, for u^5 = id) with order 5 ⟺ α² + α − 1 = 0.
  - NB: the order of an element of SL(2, k) is infinite, prime to p, 2p (p odd) or p. Leaving out the central ±1, α determines the conjugacy class locally fppf.
- **032.**
  - For u non-central and ζ a root of ζ² − αζ + 1: in characteristic 0 the order is finite iff Ψ_n(α) = 0 for some n ≥ 3; in characteristic p, iff α is algebraic, iff ζ has finite order.
  - **Theorem** (forms G̃ of SL(2), n ≥ 3; (∗): u^n = id and every u_s of exact order n):
    - A) n neither p nor 2p (p an odd prime): (∗) ⟺ Ψ_n(α) = 0 and n invertible on S. His margin: n = 4 is not excluded, and A) should work in the same way for G = G̃/μ_2.
    - B) n = 2p: (∗) ⟺ Ψ_n(α) = 0 and 2 invertible on S. His margin: "à vérifier … Peut-être faux".
    - C) n = p: (∗) ⟺ Ψ_n(α) = 0.
  - NB: only in case A do these force (α + 2)(α − 2) invertible. In B and C, α_s² = 4 exactly at the points of characteristic p, with α_s = −2 (B) or +2 (C).
- **033.** A title leaf: "(8 p) Sous-groupes finis de GP(1)".
- **034.** Finite subgroups of GP(1, k), SL(2, k) and GL(2, k), with k algebraically closed of characteristic 0.
  - Theorem: a) two finite subgroups of GP(1, k) are conjugate iff they are isomorphic.
  - b) The types are Z/n, D_n (n ≥ 2), A_4, 𝔖_4 and A_5, "exactmt les types des groupes d'isom. des cartes orientées régulières sphériques".

**Checked (SA04-R85-10).**
- **The polynomials.**
  - For u ∈ SL_2 over any ring, Cayley-Hamilton gives u^n = U_{n−1}(α)u − U_{n−2}(α), with U_{m}(T + T^{−1}) = (T^{m+1} − T^{−m−1})/(T − T^{−1}).
  - At a primitive n-th root ζ, T^{n−1} = T^{−1}, so U_{n−1} and U_{n−2} + 1 both vanish at ζ + ζ^{−1}. Hence the monic separable Ψ_n (and F_n) divides both in Z[U]. So Ψ_n(α) = 0 implies u^n = 1 over every base.
- **The Proposition of 030 lacks "n invertible" (SA04-K85-06).** Mod 5, Φ_15 ≡ Φ_3^4, so over F_5 an element of order 3 has α = −1, with (α + 2)(α − 2) = −3 invertible and Ψ_15(−1) = 0. Yet its order is 3, not 15. The same example breaks the "⟸" of his margin. The Theorem of 032 carries the condition.
- **Cor. 1 of 031, "resp. 6", also needs residue characteristic ≠ 2 (SA04-K85-06).** There α = 1 gives λ² + λ + 1 = 0, an element of order 3; GP(1) and SL(2) have no elements of order 6 in characteristic 2. This is what Theorem B) has. Cor. 2 and 3 are right (SA04-R85-05).
- **B), which he doubts, holds for u non-central in every fibre (the margin's hypothesis).**
  - At a point of characteristic p, Φ_{2p}(T) = Φ_p(−T) ≡ (T + 1)^{p−1}, so α_s = −2. A non-central element of SL_2 with trace −2 is −1 times a unipotent ≠ 1, of order exactly 2p.
  - At characteristic 2 there is no element of order 2p. At the other points ζ is a primitive 2p-th root.
  - Example n = 6: Tr u = 1 gives u² = u − 1, u³ = −1 and u⁶ = 1 over any ring.
- **C):** Ψ_p ≡ (U − 2)^{(p−1)/2} mod p, and a non-central element with trace 2 is unipotent of order p.
- **A) needs "n invertible":**
  - n = 4 at characteristic 2: Ψ_4 = U, and trace 0 = 2 gives a unipotent of order 2;
  - n = 9 at 3: Ψ_9 ≡ (U − 2)^3;
  - n = 15 at 5, as above.
- **The extent of these checks.** The direction ⟸ holds over every base; the direction ⟹ is checked fibre by fibre, which suffices over a reduced base. Michel Hua's project reaches the same conclusions for 030-032, with the same F_15 example and the same remarks on "F_n(α) = 1" and "u^5 = 0".
- **034.** This is Klein's classification (F. Klein, *Vorlesungen über das Ikosaeder*, 1884, Part I, ch. 1; locator to be checked).

### 035-037: centralizers and normalizers of the finite subgroups of GP(1) in characteristic 0, the categories of pairs (G, Γ), and models over Q

**What he does.**
- **035, 1) Γ ≅ Z/n, n ≥ 2.**
  - T = Z(Γ) is the unique maximal torus containing Γ, and Γ = ₙT. So Γ ↦ T and T ↦ ₙT are inverse bijections between the maximal tori and the cyclic subgroups of order n.
  - Aut(G, Γ) = N(Γ) = N(T), with N(Γ)/Z(Γ) ≅ Z/2 ↪ Aut Γ.
  - Corollary: over S of characteristic 0, a form G of GP(1) with a finite étale cyclic subgroup of order n "équivaut à" a smooth quadratic Module of rank 2. His margin: "expliciter les foncteurs".
- **035, 3) Γ = D_2.**
  - Z(Γ) = Γ and N(Γ) ≅ 𝔖_4. Γ ↦ N(Γ), and N ↦ the unique normal subgroup of N of type D_2 (index 6), are inverse bijections between the subgroups of type D_2 and those of type 𝔖_4.
  - The text also calls N(Γ) "l'unique ss-gpe de type A_4 qui contienne Γ". The unique A_4 containing Γ is [N(Γ), N(Γ)].
  - His margin: here N(Γ) → Aut(Γ) is not injective.
  - Corollary: over S of characteristic 0, the pairs (G, Γ), Γ a form of D_2, are the pairs (G, Γ̃), Γ̃ a form of 𝔖_4. Equivalently they are 𝔖_4-torsors, étale covers of degree 4, or tetrahedra over S; his margin adds "octaèdres orientés".
- **036, 2) Γ = D_n, n ≥ 3.**
  - Γ^+ ≅ Z/n, T = Z(Γ^+), and Z(Γ) = ₂T.
  - "Aut(G, Γ) = N(Γ) = Γ si n pair, Γ·₂T si n impair", with N(Γ)/Z(Γ) ≅ Γ/₂Γ^+ ⊂ Aut(Γ). His margin: "vérifier".
  - Corollary: for n even, the pairs (G, Γ) are the principal D_n-covers, or the regular n-gons over S. For n odd one must take products with the quadratic covers, "la même description que pour Γ = D_{2n}".
- **036, 4 & 5) Γ = A_4 or 𝔖_4.**
  - Z(Γ) = 1 and N(Γ) ≅ 𝔖_4 ≅ Aut(Γ).
  - The forms of D_2, A_4 and 𝔖_4 in a fixed G correspond one to one.
  - Corollary: all these pairs are equivalent to 𝔖_4-torsors, étale covers of degree 4, tetrahedra, octahedra, or forms of A_4 or of 𝔖_4 over S.
- **037, models over Q.**
  - μ_n acts on G_m and hence on P^1_Q. The same action comes from μ_{2n} acting on O² by λ and λ^{−1}, through μ_{2n} → μ_n.
  - Z/2 ⋉ μ_n ⊂ Z/2 ⋉ G_m = N(T) gives the dihedral cases. For 𝔖_4, he takes the normalizer of the standard D_2, "une forme (tordue ?) de 𝔖_4 … il faudrait regarder de plus près".
  - His margin: over Q, an untwisted Z/n lies in a form of GP(1) only if Ψ_n has degree 1, i.e. n ∈ {2, 3, 4, 6}.
  - A second margin: over a field k, these are equivalent: a) Ψ_n(α) = 0 has a root in k; b) an untwisted Z/n lies in a form G of GP(1) "(alors G est néc. non tordue)"; c) the same for D_n.

**Checked (SA04-R85-11).**
- **1) needs n ≥ 3 for Z(Γ) = T (SA04-K85-08).** The centralizer of an involution is all of N(T): diag(1, −1) commutes with the antidiagonal in PGL_2. So for n = 2, Z(Γ) = N(Γ) = N(T) and N/Z is trivial. The bijection T ↔ ₂T still holds, since an involution lies in a unique torus.
- **3).** The normalizer of a Klein group in SO(3) is the octahedral group, with kernel Γ on Aut(Γ) ≅ 𝔖_3.
  - Γ lies in other octahedral groups as a non-normal Klein subgroup. For example, take the cube turned by 45° about one of Γ's axes: two of Γ's rotations then become edge rotations. So "unique" holds for the A_4 and for the 𝔖_4 in which Γ is normal.
  - The corollary is a neutral gerbe: Aut of the standard pair is N(𝔖_4) = 𝔖_4, so the classes are H^1(S, 𝔖_4).
- **2): N(D_n) = D_{2n} for every n ≥ 3 (SA04-K85-09).**
  - t ∈ T normalizes Γ iff tst^{−1} = t²s ∈ Γ, iff t ∈ ₂ₙT. So N(Γ) = ₂ₙT ⋊ ⟨s⟩ ≅ D_{2n}.
  - For n odd this is his Γ·₂T. For n even it is not Γ: diag(ζ_8, 1) normalizes the D_4 = ⟨diag(i, 1), antidiagonal⟩ without lying in it.
  - So the pairs (G, D_n) correspond to D_{2n}-torsors for every n ≥ 3 (for n odd, D_{2n} ≅ D_n × Z/2, his product description), and N/Z ≅ D_n.
- **4 & 5).** Aut(A_4) ≅ Aut(𝔖_4) ≅ 𝔖_4 = N, and N(𝔖_4) = 𝔖_4.
- **037, the first margin.** For n ≥ 3, an element of order n in G(Q) has α = ζ + ζ^{−1} ∈ Q, so deg Ψ_n = φ(n)/2 = 1, i.e. n ∈ {3, 4, 6}, besides n = 2: the crystallographic restriction.
- **037, "(alors G est néc. non tordue)" is false (SA04-K85-10).**
  - SO(3) = PGL_1(H) over R is a twisted form, and it contains rotations of every order.
  - Over Q, the quaternion algebra ramified at 3 and ∞ contains Q(√−3), so its PGL_1 contains the order-3 image of a primitive sixth root of unity.
  - a) ⟹ b) holds in the split group: the companion matrix of t² − (α + 2)t + (α + 2) has Tr²/det − 2 = α.
- Michel Hua's project makes the same four corrections (n = 2, N(D_n), the "unique", and SO(3)).

### 038-041: A_5 in forms of GP(1); forms of D_n as affine lines over Z/n; the theorem: embeddings of A_5 are classified by a root of T² + T − 1 over any base

**What he does.**
- **038, 6) Γ ≅ A_5.**
  - Z(Γ) = 1 and N(Γ) = Γ.
  - Once a reference (G_0, Γ_0) over Q is chosen, over S of characteristic 0 a pair (G ⊃ Γ) amounts to an inner form of Γ_0, i.e. a Γ_0-torsor. For Γ_0 = A_5 constant, that is a degree-5 cover with a trivialization of the quadratic cover of its orientations.
  - Over k, an untwisted A_5 lies in some form of GP(1) iff α² + α − 1 = 0 has its roots in k. "Pour que de plus G soit non tordu, il f et s. que k contienne les racines cinquièmes de 1" (margin: "vérifier", underlined twice).
  - Over k_0 = Q[T]/(T² + T − 1), an embedding is fixed up to unique isomorphism by asking that the invariant of a standard 5-cycle be α_0. Then the pairs over k_0-schemes are the A_5-torsors.
- **039-040, forms of D_n.**
  - Γ has a subgroup Γ^+ of index 2 that is abelian and acted on by −1, with a split extension and with e) Γ^+ ∖ ₂Γ^+ generating Γ^+. His NB says that for cyclic Γ^+ of order n this means "n ≠ 1".
  - Then Γ^− = Γ ∖ Γ^+ consists of involutions, ₂Γ = Γ^− ⊔ ₂Γ^+, and Γ^+ is the subgroup generated by Γ ∖ ₂Γ (∗). So Γ^+ is unique, Γ^− is a Γ^+-torsor, and the group law is rebuilt from Γ^+ and the torsor.
  - Conversely, every torsor under an abelian group gives such a "dièdrale" extension: an equivalence of categories, fully faithful on the pairs satisfying e).
  - Prop. (n ≥ 3): the groupoid of forms of D_n is that of the affine lines over Z/n, and Aut(D_n) ≅ Aff(1, Z/n) = (Z/n)^* ⋉ Z/n.
- **041, Theorem (any scheme S).**
  - For a form G of GP(1)_S and a monomorphism φ: A_{5,S} ↪ G (his margin: non-trivial on every fibre suffices), set α(φ) = A(φ(π)), with π the standard 5-cycle.
  - Then (G, φ) ↦ α(φ) is an equivalence onto the discrete category of the α ∈ Γ(S, O_S) with α² + α − 1 = 0. The groupoid is rigid, and the functor of isomorphism classes is represented by M = Spec Z[T]/(T² + T − 1).
  - His margin: α' = −1 − α = −1/α.
  - Corollary: α(φ∘u) = α(φ) for u inner, and α(φ∘u) = α'(φ) for u inner on no fibre.

**Checked (SA04-R85-12).**
- **038.**
  - N(A_5) = A_5 in PGL_2(C): the outer automorphism exchanges the two classes of 5-cycles, which have different invariants (ζ + ζ^{−1} against ζ² + ζ^{−2}), so it is not induced by conjugation. Hence the pairs form a neutral gerbe with group Γ_0, i.e. Γ_0-torsors, as he says.
  - "A_5 ⊂ G(k) ⟹ α ∈ k" is right: a 5-cycle has Ψ_5(A) = 0.
- **His "racines cinquièmes" for split G is wrong (SA04-K85-11).** A_5 ⊂ PGL_2(k), in characteristic 0, iff √5 ∈ k and −1 is a sum of two squares in k (A. Beauville, "Finite subgroups of PGL_2(K)", Contemp. Math. 522, 2010; locator to be checked).
  - k = Q(√5, i) satisfies this without containing μ_5.
  - Over R, √5 ∈ R but −1 is not a sum of two squares: A_5 lies in SO(3) = PGL_1(H) and not in PGL_2(R).
  - Michel Hua's project makes the same correction with the same field.
- **039.**
  - For σ = sx with x ∈ Γ^+, σ² = sxsx = x^{−1}x = 1, so Γ^− ⊂ ₂Γ.
  - For Γ^+ = Z/n, e) fails for n = 2 as well: Z/2 ∖ ₂(Z/2) = ∅. So e) means n ≥ 3, not "n ≠ 1". This matches D_2 having three subgroups of index 2.
  - Aut(D_n) ≅ Aff(1, Z/n) for n ≥ 3, and its torsors are the affine lines over Z/n.
- **041.**
  - α' = −1 − α = −1/α, since α + α' = −1 and αα' = −1.
  - The outer automorphism sends the class of π to that of π², whose invariant is ζ² + ζ^{−2} = α'.
  - A_5 lies in PGL_2 of an algebraically closed field of every characteristic (PGL_2(F_4) ≅ A_5, PSL_2(F_5) ≅ A_5, A_5 ⊂ PSL_2(F_9)). At 5, T² + T − 1 ≡ (T − 2)² and the 5-cycle is unipotent (α = 2), and the two classes of embeddings merge, since PGL_2(F_5) ≅ 𝔖_5 induces the outer automorphism. So the theorem is consistent with M having a single, non-reduced point over F_5. Whether the infinitesimal part of M at 5 matches the deformations of PSL_2(F_5) ⊂ PGL_2 is not checked here (see hunch H85-2).

### 042-046: Schwarz systems in A_4, 𝔖_4 and A_5; forms of A_4 and 𝔖_4 as 4-element sets; rigidity of the systems

**What he does.**
- **042.** A title leaf: "(14 p) Systèmes de Schwartz dans A_4, 𝔖_4, A_5, et classification des hyperpolygônes réguliers en car. zéro".
- **043, the table of types of Schwarz systems (ρ, ρ', ρ''), with ρρ'ρ'' = 1 and the three generating.** The classes are written 3, 3' (A_4) and 5, 5' (A_5).
  - A_4, "4": (3, 3', 2) with its cyclic permutations, the reversed ones in brackets, and (3, 3, 3) [(3', 3', 3')].
  - 𝔖_4, "9": (4, 3, 2) and its six permutations ("standart"), and (4, 4, 3) with its three cyclic ones.
  - A_5, "32": (5, 3, 2) ×6 ("standart α"), (5', 3, 2) ×6 ("α'"), (5, 5, 3) ×3, (5', 5', 3) ×3, (5, 5', 3) ×6, (5, 5', 2) ×6, (5, 5, 5) and (5', 5', 5').
  - Total 45; his margin: "(ou 16 si on regarde mod action de 𝔖_5)".
  - His question: is a Schwarz system known up to conjugacy once each of its three components is? "OK dans A_4, 𝔖_4, A_5 — regarder groupes diédraux, et 𝔖_5...".
- **044.**
  - In Aut X (char 0), the forms Γ^+ of A_4 and Γ of 𝔖_4 correspond by Γ = Norm(Γ^+) and Γ^+ = [Γ, Γ].
  - Aut(A_4) ← Aut(𝔖_4) ← 𝔖_4 are isomorphisms. So 4-element sets, forms of A_4 and forms of 𝔖_4 are equivalent categories: E is the set of subgroups of index 4.
  - Hence Rev_4(S) ≅ F(S, 𝔖_4) ≅ F(S, A_4) ≅ Tors(𝔖_{4S}) ≅ oriented cubes over S.
  - Since every automorphism of (X, Γ) or (X, Γ^+) comes from Γ, the pairs are again the 𝔖_4-torsors, oriented cubes or (unoriented) tetrahedra.
- **045.**
  - Γ is the automorphism group of the tetrahedron (or of the oriented cube), and Γ^+ that of the oriented tetrahedron (or the "biorientés" automorphisms of the cube).
  - Then the systems (X, H, ρ, ρ', ρ'') generating a non-abelian, non-dihedral finite H. Their automorphisms centralize H, so they are trivial: a rigid category.
- **046.**
  - The first invariant is the triple of orders. In case I (A_4) it contains 3, in case II (𝔖_4) it contains 4, in case III (A_5) it contains 5.
  - In I and II the numerical type determines the system up to isomorphism. In III it does not, "pas même pour l'équivalence modulo 𝔖_5": the two classes of 5-cycles must be told apart.

**Checked (SA04-R85-13): exhaustive count (script `schwarz.py`).** For each ordered triple of conjugacy classes, I counted the generating triples (a, b, c) with abc = 1 and divided by |Inn G|, which acts freely on them.
- **A_4.** 8 class triples, each carrying exactly one system: (2, 3, 3'), (2, 3', 3), (3, 2, 3'), (3', 2, 3), (3, 3', 2), (3', 3, 2), (3, 3, 3) and (3', 3', 3'). That is his 6 + 2, i.e. 4 modulo the outer automorphism, which exchanges 3 and 3'.
- **𝔖_4.** 9, each unique, as he says. The involution in (4, 3, 2) is a transposition, for parity.
- **A_5.** 38 class triples, each unique, not 32. His table omits the six of types (3, 3, 5) and (3, 3, 5') (SA04-K85-12), so the total is 51, not 45. Modulo 𝔖_5 the count is 19, not 16: his 16 is the count of his own table.
- **His question.** Within A_4, 𝔖_4 and A_5, every class triple carries at most one system up to conjugacy, so the answer there is yes.
- **046.** Up to PGL_2-conjugation, which induces Aut(A_4) = 𝔖_4 on A_4, the A_4 systems are fixed by their numerical type (4 types), and the 𝔖_4 ones by theirs (9). In A_5 the types (5, 3, 2) and (5', 3, 2) share a numerical type and are not exchanged by PGL_2, since N(A_5) = A_5.
- **044.** The subgroups of index 4 are the four subgroups of order 3 of A_4 and the four point stabilizers 𝔖_3 of 𝔖_4, and N(A_4) = N(𝔖_4) = 𝔖_4 in PGL_2.
- Michel Hua's project gives the same counts: A_5 has 2280 generating triples in 38 classes, 19 under Aut.

### 047-051: the 𝔖_3-action on Schwarz systems; canonical systems of a regular polyhedron; the 96 Schwarz systems of the tetrahedral group

**What he does.**
- **047.**
  - Tr(H) is the set of triples (ρ, ρ', ρ'') with ρρ'ρ'' = 1. 𝔖_3 acts on it by the cyclic permutations and the three reversals (ρ''^{−1}, ρ'^{−1}, ρ^{−1}), etc.
  - Isomorphism of systems means conjugation in the ambient group scheme: a) for A_4, by 𝔖_4 ("pas A_4"); b) for 𝔖_4, inner automorphisms; c) for A_5, inner automorphisms, with a coarser classification modulo 𝔖_5 giving "moitié moins" of classes.
- **048-049.**
  - For a regular orientable combinatorial polyhedron Π with H = Aut^+(Π), each facet φ ∈ S ⊔ A ⊔ F gets a ρ_φ ∈ H. For every direct flag r = (s, a, f), Σ_r = (ρ_f, ρ_s, ρ_a) has ρ_fρ_sρ_a = 1 and ρ_a² = 1. His margin: ρ_f = ρ_s^{−1} when s and f are opposite.
  - Indirect flags give Σ_{r'} = (ρ_f^{−1}, ρ_s^{−1}, ρ_a). The two families are conjugate under Aut Π but not necessarily under H, "cf icosaèdre": these are the canonical and anticanonical systems.
  - Σ_{r_1} = Σ_{r_2} iff the g with r_2 = g·r_1 centralizes Aut^+ Π in Aut Π. When Aut Π = Z·Aut^+(Π) (cases II, III), the direct and indirect Σ_r are conjugate under Aut^+(Π).
- **050, Proposition (oriented tetrahedron, H = Aut^+ Π ≅ A_4, H̃ = Aut Π ≅ 𝔖_4).**
  - a) φ ↦ ρ_φ is injective on S ⊔ F, with image the 8 elements of order 3, and ρ_sρ_f = 1 for s, f opposite.
  - b) a ↦ ρ_a is of degree 2 from A onto "l'ens ₃H des él. d'ordre 3" (sic), opposite edges having the same image.
  - c) r ↦ Σ_r is injective (the centralizer of H in H̃ is 1). Its image is one H̃-torsor and two H-classes, of numerical type (3, 3, 2). His margins: "24 = 12 + 12" systems, and "72 = 36 + 36" after 𝔖_3.
  - d) Σ_r and Σ_{r'}, for r' the opposite flag, are conjugate under H.
- **051.**
  - e) The three vertices of a face, in the order opposite to Π's orientation, give a system (ρ_s, ρ_{s'}, ρ_{s''}) of type (3, 3, 3), and the opposite faces give another. These are two packets of 12, each an H-torsor, whose union is an H̃-torsor. 𝔖_3^+ keeps the packets and 𝔖_3^− exchanges them.
  - f) "Les 72 + 24 = 96 systèmes de Schwartz précédents de H sont les seuls." The proof begins: the involutions lie in the normal subgroup V, "d'indice 2" (sic), so a system contains at most one involution.

**Checked (SA04-R85-14).**
- **The count.** By SA04-R85-13, A_4 has 8 class triples with one system each, i.e. 8 × 12 = 96 generating triples with product 1: 72 of type {2, 3, 3'} and 24 of types (3, 3, 3) and (3', 3', 3'). This is his 72 + 24 = 96, and f) holds.
- **b).** The six edges map 2:1 onto the three involutions of A_4, the half-turns about the axes through midpoints of opposite edges. So "₃H des él. d'ordre 3" must read ₂H, the involutions (SA04-K85-14).
- **f).** V ≅ D_2 has index 3 in A_4, not 2 (SA04-K85-14). The argument stands: if two members of a triple lie in the proper normal subgroup V, so does the third, and they cannot generate H.
- **049.** For the octahedron and the icosahedron, Aut Π = Aut^+ Π × {±1}, the central inversion. For the tetrahedron the centralizer of A_4 in 𝔖_4 is trivial, so Aut Π ≠ Z·Aut^+ Π there, as he excludes.
- **047, c).** The outer automorphism of A_5 acts freely on the 38 classes, since every class triple contains a 5-class element (SA04-R85-13). This gives exactly half, 19, as he says.
- Michel Hua's project notes both slips of 050-051. Where it reads "3 · Aut^+" on 049, the Codex-web text has Z·Aut^+, which is correct as it stands.

### 052-056: the Schwarz systems of A_4 (end) and of 𝔖_4, the octahedral group

**What he does.**
- **052.**
  - Up to 𝔖_3, ρ and ρ' have order 3, so each is a ρ_s or a ρ_f. Four cases of 12 systems each:
    - 1) ρ = ρ_f, ρ' = ρ_s with s ≺ f (canonical);
    - 2) the anticanonical case;
    - 3) two vertices;
    - 4) two faces (the last two are the cases of e)).
  - Corollary: for A_4 the numerical types are (3, 3, 2), (3, 2, 3), (2, 3, 3) and (3, 3, 3). The class under H̃ = Aut(H) ≅ 𝔖_4 is determined by the type.
  - Every system is either a Σ_r for a unique flag (canonical case) or comes from a well-defined sequence (s, s', s'') of distinct vertices.
- **053-054, Proposition (oriented octahedron Π, H = Aut^+ Π ≅ 𝔖_4).**
  - a) The Σ_r, of type (3, 4, 2), satisfy Σ_r = Σ_{r'} iff r and r' are antipodal. They form an H-torsor in bijection with R^+. His margin: "24 d'où 6×24 = 144".
  - b) s ↦ ρ_s is a bijection S ≅ ₄H, and f ↦ ρ_f a bijection F ≅ ₃H. a ↦ ρ_a makes A a double cover of ₂H ∖ ₂H^+ (H^+ = [H, H] ≅ A_4), with antipodal edges identified. Antipodism becomes inversion.
  - c) For an arc (s, t) and the face f with (s, {s, t}, f) ∈ R^+, (ρ_s, ρ_t, ρ_{f'}) is a system of type (4, 4, 3), with f' the antipode of f. These form an H-torsor; his margin: "24 d'où 24×3 = 72".
  - His margin NB: a subgroup of order divisible by 3 and 4 is "H^+ = A_5" (sic, for A_4) or H.
  - d) These are all.
- **055.**
  - Corollary: the types are (4, 3, 2) with its 6 permutations and (4, 4, 3) with its 3 cyclic ones. The type determines the system up to conjugacy: either Σ = σ·Σ_r for a unique r ∈ R^+ and σ ∈ 𝔖_3, or Σ = σ·(ρ_s, ρ_t, ρ_f) for a unique r and σ ∈ 𝔖_3^+.
  - The proof of d) begins: the orders are 2, 3, 4, and a system contains an element of order 4 and one of order 3.
- **056.** The proof of d) ends: a non-commuting pair of an element of order 4 and one of order 3 is in position a) or c).

**Checked (SA04-R85-15).**
- **The counts.**
  - 𝔖_4 has 9 class triples with one system each (SA04-R85-13). So there are 9 × 24 = 216 generating triples with product 1: 6 × 24 = 144 of type {4, 3, 2} and 3 × 24 = 72 of type {4, 4, 3}, his 144 + 72.
  - For A_4, the 4 × 12 of 052 together with the 𝔖_3-transforms give the 96 of 051.
- **054 b).** 𝔖_4 has 6 elements of order 4, 8 of order 3 and 6 transpositions, against 6 vertices, 8 faces and 12 edges of the octahedron, with the edges 2:1 onto the transpositions.
- **054, the margin.** A subgroup of 𝔖_4 of order divisible by 12 is A_4 or 𝔖_4, so "A_5" is a slip for A_4 (noted with SA04-K85-14).
- **c).** The two 4-cycles at the ends of an edge generate 𝔖_4, since neither lies in A_4.

### 057-061: the proof for 𝔖_4 (end); regular hyperpolygons with n = 1 over a field of characteristic 0: the dihedral case and the polyhedral case

**What he does.**
- **057.** The proof of d) for 𝔖_4.
  - 1) A system contains an element of order 4. It cannot contain two involutions (the group they generate is dihedral), and two elements of order 3 lie in H^+ = A_4.
  - 2) It contains an element of order 3. Otherwise there are two elements of order 4, ρ_s and ρ_t, with t ≠ s and t not the antipode s'. Then (s, t) is an arc, which is case c).
  - 3) The case of one element of order 4 and one of order 3 is finished on 056.
- **058.** A title leaf: "(16 p) hyperpolygônes réguliers".
- **059.** The case n = 1, over k of characteristic 0, with G_0 finite.
  - The invariants are μ_i = λ_i − 1 and β = α + 2. The τ_i have finite order, so the λ_i are roots of unity of orders ν_i ≥ 2. ρ = μ_0μ_1 − β ≠ 0 reduces the problem to V of dimension 2: two strict pseudo-reflections τ_0, τ_1 with ⟨a_0, a'_1⟩ ≠ 0 and a_0, a_1 independent.
  - I) Suppose C = P̌(V) has an invariant divisor of degree 2. It is not a double point: an invariant line has an invariant complement (Maschke), which would make G_0 commutative. So V = D ⊕ D'.
  - If τ_i keeps D, one may take D = ka_i and D' = Ker a'_i. Then τ_j exchanging D and D' gives μ_i + β = 0, say β = −μ_0.
  - τ_1² = id + (2 + μ_1)a'_1 ⊗ a_1 keeping D then gives μ_0 + (2 + μ_1)β = 0, i.e. (1 + μ_1)β = 0, i.e. λ_1 = 0: absurd.
- **060.**
  - So τ_0 and τ_1 both exchange D and D'. In an adapted basis, τ_0 = [[0, ζ], [1, 0]] and τ_1 = [[0, ξ], [η, 0]], with "équations aux valeurs propres λ² + ζ = 0, λ² + ξη = 0". Since 1 is an eigenvalue, the other is −1: the τ_i are reflections, the ordinary regular polygons.
  - II) With no invariant degree-2 divisor, the image of G_0 in PGL_2 is A_4, 𝔖_4 or A_5. Then G_0 ⊂ G̃_0·k^×, with G̃_0 the inverse image in SL(V).
- **061.** ⟨τ_i⟩ ∩ k^× = 1, so ⟨τ_i⟩ embeds in Aut(C) and 2 ≤ ν_0, ν_1 ≤ 5. The same holds for every strict pseudo-reflection of G_0.

**Checked (SA04-R85-16).**
- **057.** Two involutions generate a dihedral group, and 𝔖_4 is not dihedral. If t = s, the group generated is cyclic; if t = s', then ρ_t = ρ_s^{−1} and ρ'' = 1. So the case analysis is complete.
- **059.**
  - For τ_1 = id + a'_1 ⊗ a_1 with ⟨a_1, a'_1⟩ = μ_1, τ_1a_1 = (1 + μ_1)a_1, so λ_1 = 1 + μ_1, and τ_1² = id + (2 + μ_1)a'_1 ⊗ a_1.
  - Then a_0 + (2 + μ_1)⟨a_0, a'_1⟩a_1 ∈ Ker a'_0 gives μ_0 + (2 + μ_1)β = 0. With β = −μ_0 this is (1 + μ_1)β = 0, as he says.
- **060.** The characteristic polynomial of [[0, ζ], [1, 0]] is λ² − ζ, not λ² + ζ, and that of τ_1 is λ² − ξη. Michel Hua's project notes this too. The conclusion is unaffected: one eigenvalue is 1, so ζ = 1 and the other eigenvalue is −1.
- **061.** The powers of a pseudo-reflection have eigenvalues (λ^k, 1), so they are scalar only when trivial. The element orders of A_4, 𝔖_4 and A_5 are 2, 3, 4 and 5.

### 062-068: the equation (E) for ζ, criteria of elimination, normalization, and the table of Pythagorean regular hyperpolygons

**What he does.**
- **062.**
  - β = ζ(λ_0 − 1)(λ_1 − 1) with ζ real. u = τ_0τ_1 has trace λ_0 + λ_1 + β and determinant λ_0λ_1, and K = (Tr u)²/det u − 2.
  - So ζ satisfies (E): (λ_0 − 1)²(λ_1 − 1)²/(λ_0λ_1) · (ζ² + 2(λ_0 + λ_1)ζ/((λ_0 − 1)(λ_1 − 1)) + (λ_0² + λ_1²)/((λ_0 − 1)²(λ_1 − 1)²)) = K ∈ {−2, −1, 0, α, α'}, i.e. τ_0^Cτ_1^C of order 2, 3, 4 or 5.
  - With λ = e^{iθ}, (E) becomes ζ² − cos((θ_1 − θ_0)/2)/(sin(θ_0/2)sin(θ_1/2))·ζ + (1/16)(2cos(θ_1 − θ_0) − K)/(sin²(θ_0/2)sin²(θ_1/2)) = 0.
  - Its discriminant is Δ(K) = (1/2)(1 + K/2)/(sin² sin²) ≥ 0, and ζ = [cos((θ_1 − θ_0)/2) ± cos(θ/2)]/(2 sin(θ_0/2) sin(θ_1/2)). Δ vanishes only for K = −2.
  - With 2 ≤ ν_i ≤ 5 and (ν_0, ν_1) ≠ (2, 2) this gives 15 possibilities.
- **063.**
  - For the four other K, a priori 8·15 = 120 more, "mais il faut en exclure un bon paquet".
  - Criteria: a) 0 < ζ < 1, the definiteness of the invariant hermitian form; b) the Galois conjugates (θ_0 → iθ_0, θ_1 → jθ_1) must again give values in {−2, −1, 0, α, α'}.
  - The projective situation is fixed by K_0, K_1 and K, i.e. by the Schwarz system (up to Aut(H) in the tetrahedral case).
- **064.** Four hyperpolygonal situations sit over each projective one (the choice of the fixed point of each τ_i, i.e. τ_i ↦ τ_i/λ_i), and they give four value systems when ν_0, ν_1 ≠ 2.
- **065.** The dictionary: Pythagorean polygons ↔ (λ_0, λ_1, β) ↔ pinned pairs of pseudo-reflections ↔ (K_0, K_1, K) with the fixed points a_0, a_1. λ_i is a root of λ² − K_iλ + 1 (the Codex-web text marks the sign as doubtful), and the choice of λ_i is the choice of a_i when ν_i ≠ 2. Scratch computations follow.
- **066.**
  - a) When ν_0, ν_1 ≠ 2, (λ_0, λ_1, K) does not determine ζ.
  - b) When ν_0 or ν_1 = 2, two non-isomorphic hyperpolygons sit over each admissible (λ_0, λ_1, K), the two roots of (E). "[NB on sait par ailleurs que l'on aura alors K = −2 i.e. … 2 racines distinctes]" (sic, for K ≠ −2).
  - So ν_0, ν_1, ν do not determine the hyperpolygon.
- **067.** He normalizes λ_i = exp(2iπ/ν_i). Two sources of ambiguity remain: ν_i = 2 (the tetrahedral, octahedral and icosahedral types listed), and the choice K = α or α' when ν = 5.
- **068, the table.**
  - The entries are given with the number φ(ν_0)φ(ν_1) of non-normalized hyperpolygons under each, and the types that carry two hyperpolygons underlined.
  - Tetrahedral 6, octahedral 13, icosahedral 25 ("10 + 4", "+4", "2", "4", "1"), "44 cas au total".
  - His margins: "14 cas sur les 44" where the type does not determine the hyperpolygon, and the check "4·45 = 180", with each of the 45 Schwarz systems of 043 giving 2 × 2 = 4 Pythagorean systems.

**Checked (SA04-R85-17).**
- **(E).** In dimension 2, Tr(τ_0τ_1) = 2 + μ_0 + μ_1 + ⟨a_1, a'_0⟩⟨a_0, a'_1⟩ = λ_0 + λ_1 + β. Expanding (λ_0 + λ_1 + ζ(λ_0 − 1)(λ_1 − 1))²/(λ_0λ_1) − 2 gives his bracket, the −2 absorbed into (λ_0² + λ_1²)/(λ_0λ_1).
- **The trigonometric form.**
  - λ − 1 = 2i e^{iθ/2} sin(θ/2), so (λ_0 − 1)²(λ_1 − 1)²/(λ_0λ_1) = 16 sin²(θ_0/2)sin²(θ_1/2).
  - 2(λ + λ')/((λ − 1)(λ' − 1)) = −cos((θ' − θ)/2)/(sin(θ/2)sin(θ'/2)), and (λ² + λ'²)/((λ − 1)²(λ' − 1)²) = (1/8)cos(θ' − θ)/(sin² sin²).
  - So the "= 0" form has the constant (1/16)(2cos(θ_1 − θ_0) − K)/(sin² sin²), as 062 writes, and the "= K" form of 063 b) has (1/8)cos(θ' − θ)/(sin² sin²). The two are consistent in the Codex-web text. Michel Hua's project corrects a "1/8" in its own reading of 061-062.
- **The discriminant.** It is (2 + K)/(4 sin² sin²), since 2cos²(x/2) − cos x = 1. With K + 2 = 4cos²(θ/2), the roots are his. A double root occurs iff K = −2.
- **Criterion a).** For unitary reflections τ_i x = x + (λ_i − 1)h(x, a_i)a_i with h(a_i, a_i) = 1, β = (λ_0 − 1)(λ_1 − 1)|h(a_0, a_1)|². So ζ = |h(a_0, a_1)|², and the Gram matrix [[1, c], [c̄, 1]] is definite with c ≠ 0 iff 0 < ζ < 1.
- **066 b).** "K = −2" is a slip for K ≠ −2. A system (2, ν_1, 2) generates a dihedral group, so K ≠ −2 and the two roots are distinct, which is his conclusion.
- **068.** The multiplicities under the entries are φ(ν_0)φ(ν_1): 8 for (5, 3, 2), 16 for (5, 5, 3) and (5, 5, 5), 4 for (4, 3, 2), and so on.
- **068 omits the systems with two elements of order 3 and one of order 5, as 043 does (SA04-K85-12).** By SA04-R85-13, (3, 3, 5) and (3, 3, 5') generate A_5. They are realized by finite unitary reflection groups: the regular complex polygon 3{5}3, whose group is Shephard-Todd G_20 of order 360 with projective image A_5 (hunch H85-1).
  - So the icosahedral list lacks (3, 3, 5), (3, 3, 5'), (3, 5, 3) and (5, 3, 3), and the totals 25, 44 and 180 = 4·45 must be recomputed with 51 Schwarz systems.
  - Michel Hua's project notes the omission here as on 043, and reads the "+4" of the row (5, 5, 3), (5, 3, 5), (3, 5, 5) as 3. With 3 the totals become 6 + 13 + 24 = 43, which fits his "14 cas" underlined among 29 entries. The underlines are not visible in the Codex-web text, so this count is not rechecked here.

## Full pass (lead's message of 19 Nov ~15:5x UTC, step 2): progress and what is still unread

The sections above are the survey. The lead asked for a full reading of cotes 80, 82 and 85-89; cotes 83-84 stay out (SA01, SA02), and the K161 folders other than 161-5 and 161-6 stay at survey level (SA23). After a compaction, continue from the first item not marked done.

- [done] Cote 80 in full (K80-01 to -04, scans 3-73; sections "Full pass, cote 80"; SA04-R80-02 to -10; SA04-K80-02). The K80 math notes are still to be read. The ends of 037, 043, 053, 062 and 073, first cut at a fixed width, were read afterwards (addendum; SA04-R80-11, -12; SA04-K80-03).
- [done] Cote 82 in full (K82-01 to -05, scans 2-79; sections "Full pass, cote 82"; SA04-R82-04 to -15). The K82 math notes are still to be read. Scan 031 and the ends of 058-079, first missed or cut, were read afterwards (addendum; SA04-R82-16, -17; SA04-K82-01).
- [ ] Cote 85 in full (K85-01 to -07, scans 2-98). Done so far: 002-029 (SA04-R85-04 to -09; SA04-K85-01 to -05). Next: 030-045 (K85-03), then K85-02 (16-29) to K85-07 (86-98).
- [ ] Cote 86 in full (K86-01, -02, scans 2-33).
- [ ] Cote 87 in full (K87-01 to -03, scans 3-41).
- [ ] Cote 88 in full (K88-01, scans 2-16).
- [ ] Cote 89 in full (K89-01, -02, scans 2-21).
- Then the INTEGRATION and DELIVERABLES updates, and a reply to the lead in under 150 words.

Tools (reader's scratchpad r1sa04): `python -I -B rd.py c80/k80.txt <first> <last> <width>` prints every line of a scan range (also k82.txt, k85.txt to k89.txt); `ins.py` inserts a section before this heading (pass this heading as the marker), `addrows.py` appends TSV rows.
