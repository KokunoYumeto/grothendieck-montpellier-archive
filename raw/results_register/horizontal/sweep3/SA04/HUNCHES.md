# SA04: Géométrie et topologie combinatoire, part 2 (cotes 69-102, 161): sweep 3, wave 1: hunches

<!-- reading:cote93_crystals -->
### From the reading cote93_crystals

- **H93-1 (Euler characteristics: settled here; a link).** The theorem of 93/066 holds on E_∞ without either of his two restrictions. Grounds: proofs SA04-R93-11, -12. Further, his χ_! on E_∞ should agree with the o-minimal Euler characteristic on locally closed definable sets, whose one-point compactifications are locally conical by definable triangulation (L. van den Dries, *Tame topology and o-minimal structures*, LMS Lecture Note Series 248, CUP 1998, ch. 4 and 8, locator to be checked). That would make 93/55-66 the first written form of the tame programme of cote 156 (SA21). It sharpens the SA21 hunches on χ in tame topology; I did not read H1-H12 of SA21.
- **H93-2 (characteristic p Schwarzian).** His margin on 93/074, "faux? pour un op. diff. d'ordre ≤ 3", is likely right in the other direction. In characteristic p, cocycles invariant under PGL₂ and built from Hasse derivatives of unbounded order may not all be multiples of G_0, because D^{(p^k)} gives new invariants of the étale coordinate. Grounds: in characteristic p the étale maps f and f + h^p (h a function) share all Hasse derivatives below order p. Untested.
- **H93-3 (the cancelled first value on 93/073).** The heavily cancelled value before "1/(2t)" may be the correct 1/(4t²). That would make the printed value a late slip. This is a reading question for the edition, at 400-600 dpi.
- **H93-4 (the torsor-extension device).** The construction of 93/234-236 is the device that Deligne-Illusie (1987) use for liftings mod p². His version is general: any torsor under an abelian sheaf with an affine map into Z⁰Hom•. The other parts of cote 93 (135-220, SA01) may use it for the canonical projective connection over a base, which would join SA04-9 and SA04-13.
- **H1615-1 (the slope as the missing condition).** The non-uniqueness on 161-5/029 is exactly the slope (Newton) data, and the Néron-model computation at the foot of the page shows he was computing it. The natural completion of his torsor description replaces "all extensions conjugate" by "conjugate once the slopes (equivalently weak admissibility) are fixed". This would make 161-5/23-29 a Tannakian precursor of Colmez-Fontaine. It needs a careful reading of 25-29 on the scans before it can be stated.
<!-- /reading:cote93_crystals -->

<!-- reading:cotes69-74 -->
### From the reading cotes69-74

- **H3-1 (sharpened; confirmed on his page 74/19 and 74/60).** His "graphes trialitaires" are the GQ(2,t) with t ∈ {1,2,4} (9, 15, 27 points; with t = 0 the triangle). He states the restriction c_ν = 2^ν himself. Hunch: the torsor route of 69/18-19 and 74/93-105 proves "t is a power of 2" directly (the image of the non-neighbours is a torsor under a subgroup), Higman's bound then gives t ≤ 4. Sharpened by 74/124 and 74/128-130 (third pass): at a vertex, u = id + δη on F2^{c+1} has |im u| = 2^c (c even) or 2^{c+1} (c odd), and if φ: Y → E is injective then |im u| divides |Y| = 4c, which leaves exactly c ∈ {0, 1, 2, 4}, without Higman (SA04-R74-07). The open step is the injectivity of φ, which the pages state for ν = 0 only. The dimensions 9, 15, 27 are those of H3(C), H3(H), H3(O) (minuscule representations of A2×A2, A5, E6).
- **H3-2.** Cote 69 is a "graph-first" construction of E6; with 69/96-99 it is the germ of the root-system functor of cote 88 (SA04-34).
- **H3-3 (precise).** δ' = 4(α+2)(β+2)²·det Gram[p,q]; the bad primes of a pinned realization are those dividing the Coxeter discriminant, the squared Gram entries α + 2, β + 2, and α - 2; cote 72 gives the general n: δ_V = Bρ with ρ = L_{n+1}, a continuant in the β_i.
- **H3-4.** The icosahedron mod 5 = P²(F5) with its conic gives a concrete model for the bi-icosahedra at p = 5 (SA01-16): the two icosahedra are the halves of the 24 isotropic vectors.
- **H3-5 (new, cote 74/2-16).** His closure condition (f_3f_2f_1)² = id at every point holds for Moufang loops (computed on M(S3,2)) and gives the left Bol identity; being symmetric in the three directions, it should give both Bol identities, i.e. characterize the 3-nets of Moufang loops (Bol's Moufang closure condition), not the group nets. Grounds: the computation and his derivation on 74/16.
- **H3-6 (new).** The "ombre" of cote 73 (a configuration's fibre under an operation, in a theory of identification by tests) and of cote 74 (the shadow of a point on a pavé) is the word of 156-4 (SA21): the shadows in cotes 73-74 are finite combinatorial models of the same notion. Link by our inference; to be checked against the SA21 reading.
- **H3-7 (new, cote 73).** For n = 5 the critical pentagons lie over the zero set of Gauss's discriminant (Σf)² - 4Σf_if_{i+1}; for general n the critical locus of the area map M_n → P^{n-1} is cut out by his λ-system, with the hyperspecial component (triangles run n/3 times) where dim N = 2.
<!-- /reading:cotes69-74 -->

<!-- reading:cotes76-79 -->
### From the reading cotes76-79

- **H76-1 (sharpens his 76/43).** The essential image of finite n-manifolds with regular filtrations in the free G_n-sets is the set of G_n-sets whose ⟨σ_0..σ_{n-1}⟩- and ⟨σ_1..σ_n⟩-orbits realize spheres, as a recursive condition.
  - For n = 3 it is decidable by Euler characteristics, as in crystallization theory (Ferri-Gagliardi-Grasselli; locator to be checked).
  - For n = 4 it needs 3-sphere recognition, which is decidable (Rubinstein 1995, Thompson 1994; locators to be checked).
  - For large n it is undecidable (Novikov).
  - So his hope of a combinatorial characterization can be effective only in low dimension.
  - Link: SA21 (formes, strata).
- **H77-1.** The mixed-characteristic classification of quadratic covers by (L, D, b_0), with b_0² = D mod 2 and the mod-4 condition D_1 = γ(b_0) (77/53-64, 77/74-86), describes the stack of quadratic algebras [A²/(G_a ⋊ G_m)] through the discriminant.
  - I have not seen it stated in this form.
  - To check against Knus (1991) Ch. I-III, Loos (Math. Z. 2007), Voight, "Characterizing quaternion rings over an arbitrary base" (J. reine angew. Math. 2011), and Wood, "Gauss composition over an arbitrary base" (Adv. Math. 2011). All locators to be checked.
- **H77-2.** 77/90-117 is the algebraic form of "complex structures on a real plane ↔ P^1(C) - P^1(R)".
  - Over R, {u ∈ sl_2 : u² = -1} is the two-sheeted hyperboloid, i.e. the two half-planes.
  - Over a base, the Weil restriction along S[i] gives a model of the upper half-plane that works over Z[1/2].
  - It may be the scheme-theoretic starting point of his uniformization notes (SA01-33, cote 93).
- **H78-1 (answers his questions b), c) on 78/48-49; argument, not fully checked).**
  - A regular system of p vertices over Z, with a genuine (étale) regular p-gon at p, does not exist for p ≥ 5. The rotation group is a ±1-twist of μ_p, whose Galois module χ_cyc·ε cannot be unramified at p unless p - 1 | 2.
  - Likewise there is no SR(2p)S over Z[1/2] for p ≥ 5.
  - n = 3, 4 over Z and n = 6 over Z[1/2] exist, with explicit integral examples given in the reading.
- **H79-1 (now with evidence).** §§VII-XI axiomatize the congruence regular triangulations SP_{M,i} among the regular maps of type {3, n}. The decisive axioms are To 6-To 7 (Z ≅ Z'_n acting on every star by ω ↦ ω^ν) together with (H1).
  - Both hold for SP_M: his identity of 79/295, and Klein's map.
  - The star-power operation fails on a non-congruence PSL(2,13) Hurwitz map, and (H1) fails on one (SA04-R79-09, -13).
  - T_0 4 alone does not single SP_M out (the torus {3,6}_(3,0), SA04-R79-06).
  - Conjecture: a connected regular orientable triangulation with all vertex orders n is some SP_{M,i} (M = (Z/n)²) when its commutant Z acts on the stars through an isomorphism Z → Z'_n and every element of Z satisfies (H1).
  - In the classical language, regular maps of type {3, n} correspond to normal subgroups N of PSL(2,Z) containing the n-th power of the parabolic, and the Farey map of level n is N = Γ(n) (Lehner-Newman 1964; Jones-Singerman 1978; locators to be checked). The conjecture would characterize N = Γ(n) by the commutant's action on stars.
- **H79-2.** M is the "enveloping group" of the partial addition of SP_M, i.e. Z^(M^*)/⟨[x+y]-[x]-[y] (x∧y a unit), [-x]+[x]⟩ ≅ M, for every n ≥ 3 and for Λ = Z. This is his exactness question of 79/83; I computed it for n = 3..8 (SA04-R79-07).
  - With the incidence formula ζ' = λ²ζ ± λ of 79/293-295, it would recover the module M, and the homotheties as scalars, from the graph with homotheties alone.
  - That reconstruction is what §XI aims at.
<!-- /reading:cotes76-79 -->

<!-- reading:cotes80-89 -->
### From the reading cotes80-89

- **H85-1 (operations on maps).** The "Opérations sur systèmes de Schwartz" (85/082-094), with S_3 and Ẑ^× acting on triples (h_0, h_1, h_2) with h_0h_1h_2 = 1, are the operations on regular maps and hypermaps of Jones and Thornton (1983), and an early form of the Galois-type action of the Esquisse. Grounds: the groups acting and the free group ⟨h_0, h_1, h_2 | h_0h_1h_2 = 1⟩. A full reading of these 12 pages should state what he proves.
- **H80-1 (pseudoline classification).** His counts "n = 4: 1, n = 5: 6" for affine arrangements should match the known enumeration of simple arrangements, once his C_aff and "stable" are pinned to the scan; to be checked against D. Knuth, *Axioms and hulls*, LNCS 606 (1992), locator to be checked. He also uniquely reconstructs the map from the oriented 1-skeleton when no line is a monogon or bigon (80/071). That is a combinatorial rigidity statement worth stating precisely.
- **H82-1 (characteristic 2).** The characteristic-2 dictionary of cote 82 (forms of sl(2) and gp(1) as affine symplectic planes) is the algebra behind his "2 inv." in the opers of 93/086-091. Reading the two together would give the characteristic-2 theory of projective structures that the cote 93 pages leave open.
<!-- /reading:cotes80-89 -->

<!-- reading:cotes94-102 -->
### From the reading cotes94-102

- **H94-1 (one programme for EGA V-VI).** Cotes 94, 98 and 102 are three drafts of one book plan: representability of linear functors (94), finiteness and bounded families (98), gluing and properties of morphisms of functors (102). Grounds: the cross-references to EGA III 7.7, SGA 4 XVII and SGA 6 XIII, the shared methods (generic flatness, noetherian induction), and the EGA VI plan of cote 26 (SA23-28).
- **H100-1 (the source of a known extension theorem).** The theorem of 100/003 is likely the unpublished source of the extension results for abelian schemes via p-divisible groups later cited in the literature (Faltings-Chai, ch. V). Grounds: the hypotheses (étale depth ≥ 2, geometric unibranchness) and the method (moduli with level structure, descent). This is a historical question, to be checked against Faltings-Chai's attributions.
- **H101-1 (priority of the canonical module).** The 1958 notes define the canonical module and characterize Gorenstein rings by Ext(k, A) five years before Bass. Grounds: the dated title "Notes antiques 1958" and the content of 101/017-043. It would be worth a historical note, with care about what Serre and others had at the time.
- **H101-2 (his Problem C and the margins on 101/041-042).** His claim that no two of the three conditions on Ext^{n−1}, Ext^n and Ext^{n+1}(k, M) suffice is a precise statement about modules. Roberts' theorem (rings of type 1 are Gorenstein) bears on a neighbouring statement for rings (P. Roberts, "Rings of type 1 are Gorenstein", Bull. London Math. Soc. 15 (1983), locator to be checked).
<!-- /reading:cotes94-102 -->
