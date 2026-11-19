# SA04: Géométrie et topologie combinatoire, part 2 (cotes 69-102, 161): sweep 3, wave 1

**Lead:** Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026, by sweep3/WAVE1_LEAD_BRIEF_20261119.md.

**Readers** (all Claude Opus 5.5 at effort max; method: _tools_a6d42bf6/READER_BRIEF.md):
- R1, agent a0399c97cde963d2d:
  - cote 93 (the crystals strand, scans 47-91 and 221-236) and cote 161-5 (`readings/cote93_crystals*`);
  - cotes 94-102, with the six divergent scans of cote 100 decided on the images (`readings/cotes94-102*`);
  - cotes 80, 82 and 85-89, and the K161 folders 161-1 to -4 and 161-6, as a survey (`readings/cotes80-89*`).
- R3, agent a5723c09c05df9eda: cotes 69, 70, 72, 73 and 74 in full, with K72 compared against the Pro package MPL_72_035-081 scan by scan (`readings/cotes69-74*`).
- R4, agent a774f5c4e87a59ea4: cotes 76, 77, 78 and 79 in full (`readings/cotes76-79*`).

**Sources:**
- the Pro packages in `inputs/SA04/pro/` and `inputs/SA01/pro/MPL_72_035-081*`;
- the Codex-web K-folders in `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K<cote>-*/out/`;
- the scans in `grothendieck_archive_montpellier/`;
- the maps in `sweep2/SA04/WHAT_IS_WHERE.md` and `TOPIC_NOTES.md`.

**Not yet read in full** (to be read):
- cotes 80, 82 and 85-89, and 161-6: a survey only (the first lines of each scan, no image). The full reading is assigned to R1 after its SA01 stretch.
- the K161 folders 161-1 to -4: a survey only. They are SA23's, whose sweep-3 study reads them.
- cotes 94-102: the ends of long paragraphs past the reader's cut and most TikZ diagrams; the Pro and Work notes were not opened; the rest of cote 100 needs a second pass on the scans.
- drawings (TikZ) in cotes 76-79; scans 79/272, 275 and 282, which have no inventory row.
- the scans that no folder transcribes, listed in each reading.

**Ink still to decide on the scans:** the corrections marked "no scan viewed" in CORRECTIONS.tsv. The readers viewed 69/14 and 21, 70/120-121, 72/35-36, 74/120-121, 76/7, 79/37, 143, 240 and 273, 93/56-73 (seven readings), 97/005, and cote 100, scans 3, 9, 27, 30, 46 and 51.

**Asked in other prompts:** cote 100 (RESEARCH_SA15, Part C), 161-5 (RESEARCH_SA23, Part J), cotes 94, 97 and 98 (the working-through objects H035, H036, H02M). The characteristic-p questions of cote 93 (P93-2, H93-4) go into RESEARCH_SA03 with the rest of cote 93.

The items below are the readers' integration blocks, one per stretch.

<!-- reading:cote93_crystals -->
### From the reading cote93_crystals

Cote 93 (scans 47-91, 221-236) and cote 161-5, read in full by reader R1 (Claude Opus 5.5 at effort max), 19 Nov 2026: the Pro text (GPT-6 Astra, ChatGPT Pro mode) page by page, the Codex-web folders compared word by word, scans of 93 viewed where a reading mattered. Full reading: `cote93_crystals.md`.

**The Barsotti-Tate programme (93/47-54; SA04-1, SA04-3).** 47-48 are a typed draft of ch. V of the Montréal notes (the crystalline comparison for abelian schemes, deformations, Serre-Tate after Messing). The typed "Rabiots" (49, 51) and "Sur un théorème de Tate" (53-54) pose Problems 4-6, the "foncteur mystérieux" from filtered F-crystals to Galois representations. They guess that it is fully faithful with a quasi-inverse on a subcategory of Hodge-Tate modules, and that Tate's theorem holds without characteristic 0. All of this was later proved: Fontaine (1982), Colmez-Fontaine (2000), Kisin (2006), de Jong (1998). The Proposition of 49 (isogroups are insensitive to nilpotent thickenings) agrees with Drinfeld's rigidity. Two reused typed leaves (50, 52) carry exercises on pseudo-resolvents and Cohen's factorization (SA04-2, decided in sweep 2).

**Euler characteristics (93/55-66; SA04-4).** His axioms (a)-(h) for χ and χ_! were re-derived. The theorem of 66 lives on E_∞, the locally compact spaces whose one-point compactification is locally conical. He leaves two questions there: whether (g) holds without the restriction to relative polyhedra, and whether (a)-(e) characterize χ and χ_! on all of E_∞. **Both have affirmative answers:**
- compact members of C_∞ are ANRs (Hanner), hence of finite CW homotopy type (West);
- cutting at infinity reduces the non-compact case to the compact one;
- the Leray and Serre spectral sequences then give the product formulas;
- homotopy models give uniqueness.

The Pro notes left the first open (EC37) and the second conditional (EC39); the condition falls away, since the doubtful letter in the definition of C_n does not change the class. His doubt about compact triangulability is right from dimension 4 on (Freedman-Casson; Manolescu). Seven readings were decided on the scans, among them the swapped arrows of 56 (d) and the cancelled E_3 bracket of 62.

**The Schwarzian and the écarts (93/72-84; SA04-7, -8).** G = −2(S(g) − S(f)) dt² and G = 12 G_0 hold. The ink of 73 has the wrong test value dt²/(2t); it is not a misreading, and the right value is dt²/(4t²). The n-differential formulas of 80/82 check, up to two slips. An open point: his "faux?" on the uniqueness of G_0 in characteristic p for operators of order above 3.

**Projective bundles and opers (93/86-91; SA04-9).** The relation c₁₂ = −2c₂₃ and the canonical triple (g, L, c_Ω) with L ≅ P¹(ω) ⊗ ω⁻¹ (the Atiyah extension) check. This is the Borel reduction of the canonical PGL₂-oper. It needs 2 invertible, as he says, and continues on 93/135 (SA01).

**Periods and the torsor-extension construction (93/221-236; SA04-11 to -13).** These pages hold:
- Picard-Fuchs expressions and periods ∫_a^b ω;
- the Gauss-Manin connection on f_*(ZΩ¹)/df_*O, with a correct Stein restriction;
- differential operators with constant coefficients on stratified modules (characteristic 0);
- a general device on 234-236: a torsor under an abelian sheaf, with affine maps into Hom•, gives a morphism in the derived category through the extension of Z by the torsor.

Read additively, the device is sound: it compares de Rham complexes of local liftings without a global lifting, the step 48 postulates.

**Cote 161-5 (SA04-14 to -16).** Scans 3-22 are printed text by Serre: the Driebergen paper of 1967 and the course résumé of 1968-69. His marginal notes cite Sen (1973). His notes (23-29) put the mysterious functor in Tannakian form, with torsors for the algebraic envelope G. They ask two questions:
- whether the crystalline data extend as ⊗-functors to the category generated by Barsotti-Tate representations: yes, by Fontaine's D_cris;
- whether all extensions of a section over π are conjugate: no, already in rank one. The kernel of H¹(Γ, G_m) → H¹(π, G_m) maps onto Z by the valuation (the slopes), as Michel Hua's project found; my re-proof confirms it.

**Deliverables.** Nothing is ready for an edition; 93/221-236 is closest. 161-5/3-22 is Serre's print, to be cited. 93/47-91 (394 unsure marks) and 161-5/23-29 (18 per scan) need a pass on the scans.
<!-- /reading:cote93_crystals -->

<!-- reading:cotes69-74 -->
### From the reading cotes69-74

Reader R3 (Claude Opus 5.5 at effort max) of a6d42bf6fe2b0d8a8, 19 Nov 2026, three passes. Read: every transcribed scan of cotes 69, 70, 72, 73 and 74; K72 compared with the Pro package MPL_72_035-081. 46 check events, 36 corrections.

**Cotes 69 and 74 (SA04-20, SA04-23): the 27 lines as a graph.**
- A 27-vertex, 10-regular graph with every edge in exactly one triangle is the cubic graph (69/3-11): the uniqueness of GQ(2,4), proved by pinning a triangle and describing the rest by F2-torsors.
- Every pinned configuration is counted against |W(E6)| = 51840; E6 and W are rebuilt from the graph (69/42-58); "minuscule-type" vectors (69/96-99); 3-nets and loops (69/101-119, 74/2-16).
- Cote 74 names the series 𝒯_{-1}, 𝒯_0, 𝒯_1, 𝒯_2 (triangle, bitriangle, the 15 duads of a 6-set, the 27): the GQ(2,t), with his own claim that only c = 1, 2, 4 occur (74/19).
- He studies triads, hexagons, bitriangles ("pavés") and their shadows, decompositions into three bitriangles (group of order 1296), the symmetries σ_t of triangles (generating the index-2 subgroup of W(E6), transitive on arcs), and answers his own open question of 69/40 (five relative positions of two bitriangles, 74/63).
- 74/119-136: the counting tables of the series (every value right; three closed formulas slipped, and the pinned bitriangle cells corrected in the ink by overwritten exponents, decimals left standing); the torsor at a vertex for every ν (74/128-130: u = id + δη is bijective iff c + 1 is even, else im u = Ker η); the self-dual "cour" (74/131-132); the diagrams A_2-A_5, prisms and bisquares as torsor categories (74/133-136; no induced prism over a pentagon or hexagon, computed).
- All counts and models computed; corrections: 16 sixes per line (ink 18, 69/21), i(δ)·i(δ') = 6 (ink 9, 69/57), the weight table of 69/93, the B_r case of 69/97, scratch counts on 74/67 and 74/78, the formulas of 74/120-121.

**Cotes 70 and 72 (SA04-21, SA01-1/3/4/6): pinned regular realizations over rings.**
- Reflection conditions leave one modular invariant α_i per adjacent pair (the trace of σ_iσ_{i+1}); 2n+1 parameters without σ_i² = 1 (70/34 = 72/14).
- The invariant quadric of {p, q}: δ' = -(α+2)(α+β)(β+2)² = 4(α+2)(β+2)²·det(Gram), δ = (α-2)(α+2)(β+2)² (70/68-70, verified); bad characteristics of the five solids; the icosahedron mod 5 fills P²(F5).
- Cote 72 does it for all n: continuants L_n with δ_n = β_0^n···β_{n-1}L_n, ρ = L_{n+1}, σ = L_n, σσ' = β + γρ (computed n ≤ 5); invariant subspaces; groups generated by pseudo-reflections; Stiefel-Whitney and Brauer classes of the invariant form (72/107-113: formulas right, but η_i² = εη_i refutes his "10 classes independent", and H¹ needs ∂(2)).
- Decided on the scan: 72/36 (SA01-C3) is his slip ("+1" is the ink; the coherent statement is β_i = 4cos²θ_i, α_i = 2cos 2θ_i); 72/35 the Pro misread "Peut-être faux"; it reads "Peut-être faut-il se donner au préalable ...".
- Programme on 70/122-123: an arithmetic theory of regular polytopes (moduli of k-realizations).

**Cote 73 (SA04-22): polygons over a base.** The area map u ↦ (u_{i-1} ∧ u_i): M_4 ≅ P² (73/6), the pentagon recovered from its five ear areas by a quadratic whose discriminant is Gauss's pentagon discriminant (73/20, computed), critical polygons and the theorem dim N(u_*) ∈ {0,1,2} (dim 2 iff a triangle run n/3 times); a theory of identification by tests ("crible", "ombre", 73/9-11).

**Dating:** reused sheets of June 1976 to July 1978 (Bourbaki seminar June 1976, IPES jury June 1976, USTL statutes June 1977, PCF leaflet December 1977, thesis notices June-July 1978).
<!-- /reading:cotes69-74 -->

<!-- reading:cotes76-79 -->
### From the reading cotes76-79

**Extent.**
- Every transcribed scan of cotes 76-79 was read: 635 scans (76: 55, 77: 157, 78: 129, 79: 294).
- The texts are the Codex-web transcriptions K76-K79. Five scans were viewed: 76/7, 79/37, 143, 240 and 273.
- The checks are 51 check events (re-proofs, sympy and brute-force computations, scan readings) and 29 corrections.

**Cote 76 (SA04-24), the combinatorial frame.**
- Incidence complexes with the diamond axiom, flags and involutions σ_i. G_n (σ_i² = 1, non-consecutive σ_i commuting) is his "groupe n-cartographique", and G_2 is the cartographic group of the Esquisse. These are today's abstract polytopes and maps.
- Flag geometries ↔ quasi-simplicial sets. The combinatorial cube and the hemicubes were checked by brute force.
- Two statements are wrong as written:
  - the manifold criterion of 76/7 (decided on the scan; counterexample: the suspension of a torus);
  - the essential image in Th. 1 (76/39) for n ≥ 3.
- Two of his open questions are answered: δ-connectivity under heredity, and the hemicube automorphisms for n even.

**Cote 77 (SA04-25), quadratic forms over a base.**
- Rank-2 data (O(2)-torsors).
- The circumscribed conics of the pinned polygon. His open question is answered: Δ = α(α+1)²(α-2)^5(α+2)².
- Quadratic covers ↔ (L, D) when 2 is invertible, and ↔ (L, D, b_0) with a mod-4 condition when 2 is regular. B² ≡ (-1)^m Δ mod 4.
- The affine quadric det u = 1 as a Weil restriction along S[i]/S; orthogonal group schemes; the Arf cover.
- Wrong: μ = 2, not 1/2, on 77/101; two signs on 77/117; the simplicity of SO(2ν+1); Aut of a rank-2 quadric.

**Cote 78 (SA04-26), a course on regular polygons, Nov-Dec 1977.**
- Regular polygons ↔ affine D_n-representations; universal pinned coordinates.
- The vertex polynomials F_n, with u_α^n = id ⇔ F_n(α) = 0 over any ring. His Bezout pair is wrong; the theorem stands.
- Semi-cyclotomic polynomials mod p:
  - the order statement fails for p = 2;
  - one congruence should read (T-2)^{p'}, not (T-1)^{p'}.
- Regular systems of vertices over Z: hunch H78-1.

**Cote 79 (SA04-27), regular triangulated 2-polyhedra and their axiomatics.**
- §I-II: SP_M for M free of rank 2 over Z/nZ or Z.
  - Aut^+ = PSL_2(Λ), and the genus is 1 + N'(n-6)/(12n). These are the Farey maps of X(n) (checked for n = 3..12).
  - G_{3,∞} ≅ PGL_2(Z).
  - This puts SA01-2 on his pages.
- §VI-VIII:
  - the commutant of Sl_Λ(M): Λ^* on M^*, Z'_n on S_M, with the octahedron's antipodism when 2Λ = {0,2};
  - the axioms T_0 1-7 and To 1-8 of "structures triangulaires congruentielles";
  - Z'_n acts on stars by ω ↦ ω^ν.
- §IX-XI:
  - graphs and multigraphs "à homothéties", generalized antipodisms, prégraphes and jauges;
  - homogeneity as pinned group data (H, U_0, T_H, N_H);
  - a vertex is determined by its star, except on bipyramids, and over a semi-local Λ except when 2Λ = {0,2}.
- His questions answered:
  - T_0 4 is a genuine axiom (the torus {3,6}_(3,0));
  - the star-power operation fails on the PSL(2,13) Hurwitz maps (79/143);
  - to "J'ignore si cette condition est tjrs satisfaite !" (79/184) the answer is no: on one PSL(2,13) Hurwitz map an antipodism fails (H1);
  - (164) B_H ∩ N_H = T_H holds, as he proves.
- Errors:
  - the orders of Z'_n on 79/143 (his, as the scan shows);
  - GP(1,Z/5Z) is A_5 × {±1}, not "S_5 ?" (79/273);
  - slips on 79/37 (one of them the transcription's), 79/240, 79/250 (94) and 79/277.
- 79/283-297 are 1980 notices used as scrap; §II dates from 1982 or later.

**Links.**
- 76 → 77 → 78 → 79 is one programme: combinatorial frame, quadratic forms, polygons, polyhedra.
- SA01: SA01-1, SA01-2 (his pages, and the homothety axioms), SA01-3, SA01-6, SA01-16, SA01-28 and SA01-41.
- SA04: SA04-21, SA04-30 and SA04-41.
- See DEPENDS.
<!-- /reading:cotes76-79 -->

<!-- reading:cotes80-89 -->
### From the reading cotes80-89

Cotes 80, 82 and 85-89, and cote 161 parts 1-4 and 6. Survey reading by reader R1 (Claude Opus 5.5 at effort max), 19 Nov 2026: every scan seen through the first lines of the cleaned Codex-web text; no scan image; full reading: `cotes80-89.md`. Cotes 83 and 84 are SA01's and SA02's by the sweep-2 placements and were not read.

**Cote 80 (SA04-28): pseudoline systems.**
- Classification of systems of pseudolines: affine arrangements of n pseudolines correspond to projective ones of n+1 with a marked line; counts of the fibres of the passage.
- Real hyperplane arrangements as stratified spheres.
- The "crucial cases" of 1-dimensional arrangements: pencils, I_N, I_pq, II_pq, II_4, II_5, III_6 (complete quadrangle), IV_7 (quadrilateral with its diagonals).
- The combinatorial and "gauche" cube and octahedron with their orientations; reconstruction of the map from the oriented arrangement (a uniqueness theorem when there are no monogons or bigons).
- His vertex counts check, except the margin "N+1 sommets" on I_N, which has N.
- Reused sheets: his German autobiographical typescript and a notice of 13 May 1981.

**Cote 82 (SA04-30): rank-3 quadratic modules and Lie algebras over a base.**
- The bracket attached to a symmetric bilinear form of rank 3; Cramer's identities f'f = Δ; sl(2) from q = xy + z²; Casimir forms.
- Characteristic 2: forms of sl(2) and gp(1) as affine symplectic plane bundles; centralizers of finite étale subgroups.
- A "dictionary" of eleven fibred categories equivalent to GP(1) = SO(3)-torsors, three of them only over S − {2}.
- Discriminants and brackets check.

**Cote 85 (SA04-31): eight dossiers.**
- Triangle groups and pinned regular 2-polyhedra in forms of GP(1) over a base, with the invariants α = ζ + ζ^{−1}.
- Representations of the infinite dihedral group; invariants of automorphisms of P¹; finite subgroups of PGL₂.
- "Systèmes de Schwartz" in A_4, S_4 and A_5; regular hyperpolygons; the classification of finite regular 2-polyhedra in characteristic 0.
- "Opérations sur systèmes de Schwartz" by S_3 and Ẑ^×: the operations on maps later published by Jones and Thornton, in the setting of the dessins.
- Classes of subgroups of S_5.
- The unit N(α + 2) = 1 and the flag counts check.

**Cote 86 (SA04-32):** incidence geometries as sets with three involutions on flags (a fully faithful functor), and the combinatorial and hemi-icosahedron through its 5 orthogonal triples, G^+ = Alt_5.
**Cote 87 (SA04-33):** convex polyhedra, polarity, and finite posets with the diamond property: the abstract-polytope axioms.
**Cote 88 (SA04-34):** maps from Coxeter data; regular maps as quotients of the universal maps C_{p,q}, the spherical ones being the Platonic solids.
**Cote 89 (SA04-35):** 3-3 sets, the combinatorial hexagon, squares through F_3-planes, and rank-2 modules over rings.

**Cote 161, parts 1-4 and 6 (SA23 in sweep 2).**
- Adjoint functors and finite theories (161-1). It also holds a stray page in the notation of the 161-5 crystal notes.
- δ-exact envelopes, classifying topoi of algebraic structures, accessible categories (161-2).
- Products of topoi and English lecture notes on topoi (161-3); flat descent and an introductory course in algebraic geometry (161-4).
- The Euclidean icosahedron, and embeddings of graphs in surfaces (161-6). His margin question "b_1(X) + 1 components?" has the answer b_1(X) + 1 − 2g(U): his guess holds exactly in genus 0.

**Deliverables.** Nothing is ready for an edition. Each part has one Codex-web pass, with 6-15 unsure marks per scan, and needs a full reading on the scans. This survey gives the map for it.
<!-- /reading:cotes80-89 -->

<!-- reading:cotes94-102 -->
### From the reading cotes94-102

Read in full by reader R1 (Claude Opus 5.5 at effort max), 19 Nov 2026: Pro text (GPT-6 Astra, ChatGPT Pro mode) for 98 and 100, Codex-web otherwise; one scan viewed (97/005). Full reading: `cotes94-102.md`.

**Cote 94 (SA04-36): representing functors on modules.** Criteria for a functor Mod(A) → Ens to be representable by a module of finite type:
- faithfully flat descent (Lemma 1);
- f-adic gluing (Lemma 2);
- noetherian induction (Prop. 3), the local case through injective hulls (Prop. 4), constructibility of ranks (Remark 5 bis);
- generic base change along regular sequences (Lemma 6, Cor. 7), dualizing modules on a dense open, Theorem 12.

Two theorems follow. Theorem 14 is EGA III 7.7.6 (the module H(F, G) for G flat and f proper), here with a new proof. Theorem 19: Weil restriction of affine schemes along proper flat morphisms is affine. Checked: Lemmas 1-2, Prop. 3, and Lemma 6 b), whose "trivial" step needs the remark that a regular sequence stays regular modulo the nilradical when gr_J is free. Cor. 7 and Lemma 16 have slips.

**Cote 97 (SA04-37): Chern classes and Fuchsian groups.**
- The Chern classes of the regular representation of Z/p: the ink has c_{p−1}(r_G) = ξ₀^{p−1}. Wilson's theorem gives −ξ₀^{p−1}, so c(r_G) = 1 − ξ₀^{p−1}. His conclusion H^{Nk}(G)(p) ≠ 0 stands.
- A cocompact torsion-free Fuchsian group always lifts to SL₂(R): the obstruction is the Euler number 2 − 2g mod 2. This is a spin structure, with E₀ ⊗ E₀ = T_X ⊕ 2.
- The cohomology of B_G, and torsion primes of reductive groups (the matter of his Séminaire Chevalley exposé of 1958).

**Cote 98 (SA04-17): norms and bounded families.**
- An axiomatic theory of norms Y → Σ^r(X/Y) for "normed" morphisms (cf. SGA 4 XVII). Its degree axiom (v bis) holds for finite locally free morphisms, since invariants of a permutation basis are free on the orbit sums.
- Hypersheaves on G-sets and Leray-Čech spectral sequences.
- "Familles limitées" (cf. SGA 6 XIII): a refined Chow lemma; stability of bounded families under ⊗, Hom, Tor and Ext; base-change lemmas for Tor and Ext under flatness of the Tor and Ext sheaves. Both lemmas were checked.
- Reused leaves: Bourbaki *Topologie générale*, and a typescript on abelian varieties carrying his margins.

**Cote 100 (SA04-38): good reduction via p-divisible groups.**
- The theorem: abelian schemes over S are the same as pairs of an abelian scheme over U and a p-divisible group over S. The functor is fully faithful when U meets every component, and an equivalence when the étale depth along T is at least 2 and S has a geometrically unibranch finite cover.
- The proof: Grothendieck's Inventiones 1966 rigidity theorem, Serre-Tate, level structures and Mumford's moduli (the GIT sheets are in the folder), descent along proper epimorphisms, and algebraization of formal abelian schemes.
- The algebraization rests on a Baire-category argument over complete local rings. It was checked, with one qualification: V must be a complete discrete valuation ring.
- The reused EGA IV₄ proofs (14 March 1967) date the folder to after March 1967.
- Pro and K100 diverge strongly on six pages.

**Cote 101 (SA04-39): local cohomology, "Notes antiques 1958".**
- Cones and Proj; local duality for non-quasi-coherent modules, worked out with adèles for n = 2.
- The 1958 notes: the canonical module as "module fondamental", local duality in degrees ≥ k iff H^i(A) = 0 for k ≤ i < n, deficiency modules Ω^{(i)}, and characterizations of Gorenstein rings by Ext^{n−1}, Ext^n and Ext^{n+1}(k, ·). They come before Bass (1963) and the 1961 Harvard seminar.
- His question "Ext^i(K, A) = 0 for all i?" has a positive answer for every complete local noetherian domain: A is pure-injective, hence cotorsion.

**Cote 102 (SA04-40): "Pour EGA VI".** As in the sweep-2 report: gluing of objects of a site along a class M, the "Questions pour Artin", and a plan for properties of morphisms of functors.

**Deliverables.** Nothing is ready for an edition: one transcription pass per cote (two for 100), 8 to 14 unsure marks per scan. Cote 100's divergent pages and the 1958 notes come first.
<!-- /reading:cotes94-102 -->
