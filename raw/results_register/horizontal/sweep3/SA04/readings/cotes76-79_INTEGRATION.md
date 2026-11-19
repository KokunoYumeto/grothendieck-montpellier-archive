# Cotes 76-79: integration (reader R4, Claude Opus 5.5 at effort max, 19 Nov 2026)

## STUDY

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

## HUNCHES

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

## PACKAGES

- **P-R4-1. Quadratic algebras over a base where 2 is regular (cote 77).**
  - Question: are Th. 77/57, Th. 77/59 and Props 77/78-86 (quadratic covers ↔ (L, D, b_0); Δ = b² - 4c iff the étale algebra A_{2Δ}[√Δ] extends over A_Δ) known, and in what generality are they true?
  - Why it matters: it is a complete description of quadratic covers through the discriminant at 2, with an arithmetic criterion (the scheme form of "Q(√d) unramified at 2 iff d ≡ 1 mod 4").
  - It rests on 77/21-64 and 77/74-86, with checks SA04-R77-04 to -06.
  - Strongest reduction on the page: the uniqueness argument (4 regular) and the torsor of lifts under 2L.
  - Material: K77-02 to K77-06; Knus 1991; Loos 2007; Voight 2011; Wood 2011.
- **P-R4-2. Cote 79, §§VII-XI: do his axioms characterize the congruence maps?**
  - Questions:
    - (a) H79-1: do To 1-To 8 with (H1) for every element of Z, or the multigraph axioms of §XI with the isomorphy and homogeneity conditions, characterize the SP_{M,i} (Λ = Z/nZ) among the regular triangulations of type {3, n}?
    - (b) H79-2, the enveloping group, for all n and for Λ = Z.
    - (c) The bound "distance 0, 2 or 3" of §X.1.
  - Why it matters: it would characterize the congruence (level-n) regular maps combinatorially. That is the map form of the congruence question for subgroups of PSL(2,Z), which the Esquisse's dessins pose for the cartographic group. It continues SA01-2 on his own pages.
  - Strongest reduction on the page: §XI.3 turns a homogeneous graph with homotheties into pinned group data (H, U_0, T_H, N_H) with conditions a)-d) (163), and (164) is now proved (SA04-R79-17). So (a) becomes a question about these data for H = PSL(2,Z/n) against the other quotients of the (2,3,n) triangle group.
  - Evidence so far: SA04-R79-05, -06, -09 and -13.
  - Material:
    - the K79 folders from scan 103 on (§§VII-XI);
    - `c79b.py`, `nu_op.py` and `h1_test.py` in reader R4's scratchpad;
    - a census of regular maps (Conder), Lehner-Newman 1964, Jones-Singerman 1978 and Coxeter-Moser §8, all locators to be checked.
- **P-R4-3. Regular systems of vertices over Z (78/45-49).**
  - Question: his b) and c), with H78-1's negative answer for p ≥ 5 to be proved in full: finite flat group schemes of order p over Z_(p) (Oort-Tate), and the regular p-gon in characteristic p.
  - Why it matters: it decides whether the "modular" description of regular polygons extends over Z.
  - Material: cote 78/41-49 and 78/113-120.
