# SA04: Géométrie et topologie combinatoire, part 2 (cotes 69-102, 161): sweep 3, wave 1: research packages

<!-- reading:cote93_crystals -->
### From the reading cote93_crystals

- **P93-1: χ and χ_! on locally conical spaces.**
  - *Question:* write the complete theorem of 93/066 on E_∞, with both of his "j'ignore" questions resolved, and determine whether his χ_! is the o-minimal Euler characteristic on definable sets.
  - *Why:* it completes his own axiomatics and connects cote 93 to the tame programme of cote 156.
  - *Rests on:* Hanner (1951), West (1977), the Leray and Serre spectral sequences, van den Dries (1998).
  - *Strongest reduction:* proofs SA04-R93-11, -12 in this reading, and Pro EC21, EC27-EC39.
  - *Material:* 93/055-066 (Pro text with the corrections SA04-K93-01 to -08), Pro notes EC01-EC46.
- **P93-2: the projective invariant in characteristic p.**
  - *Question:* over F_p, classify the differential operators G(f, g) in Hasse derivatives of any order, with values in ω^{⊗2}, satisfying the cocycle condition b), PGL₂-invariance c) and non-vanishing. Is every such G equal to c·G_0 with c ∈ F_p^*, as his Remark 3 on 93/074 claims, or does the uniqueness hold only up to order 3, as his margin "faux?" suggests?
  - *Why:* it decides his own doubt, and it bears on projective structures and opers in characteristic p (SA04-9, SA01).
  - *Rests on:* 93/072-074, the uniqueness of the Schwarzian in characteristic 0 (Ovsienko-Tabachnikov 2005, ch. 1, locator to be checked), and p-curvature of opers (Y. Ihara; S. Mochizuki, *Foundations of p-adic Teichmüller theory*, AMS/IP 1999, locator to be checked).
  - *Strongest reduction:* his statement for order ≤ 3 and SA04-R93-15.
  - *Material:* 93/072-084.
- **P1615-1: the Tannakian mysterious functor of 161-5/23-29.**
  - *Question:* state his torsor data (ρ, j, Q_L, R_L, the descent and Frobenius data, the extension E of Γ) precisely. Prove that the extensions of α₀ are classified by the slopes, and that fixing them, or imposing weak admissibility, makes the solution unique up to G'_L(L).
  - *Why:* it is the most developed form of the "foncteur mystérieux" in the archive, and it predates Fontaine's period rings.
  - *Rests on:* Fontaine (1982); Colmez-Fontaine (2000); Kisin (2006); the rank-one computation SA04-R1615-03.
  - *Strongest reduction:* rank one, settled.
  - *Material:* 161-5/023-029 after a reading on the scans; 93/049-054.
<!-- /reading:cote93_crystals -->

<!-- reading:cotes69-74 -->
### From the reading cotes69-74

- **P3-1: GQ(2, t) by torsors.** Question: does his pinning argument (69/3-19, 74/93-116) prove, uniformly, that a graph with unique triangles on edges and equality in |S| ≥ 3(ν - 1) is GQ(2, t) with t ∈ {1, 2, 4}, each unique, with a torsor model? Why: it turns cotes 69 and 74 into a classification and tests H3-1. Rests on: 69/3-19, 74/19, 74/93-116 (read and checked here); Payne-Thas, *Finite generalized quadrangles*, 1984, §§1.2, 5.3, 6.1 (locators to be checked). Strongest reduction on the pages: 74/103-104 reduces the classification to two questions (systems of quotients with φ_αβ bijective; their double covers with axiom (**)); 74/128-130 gives the map u at a vertex, and with φ injective the orbit count leaves only c ∈ {0, 1, 2, 4} (SA04-R74-07). Material: `cotes69-74.md`, `chk69.py`, `chk69b.py`, `chk74b.py`, `chk74c.py`.
- **P3-2: bad primes of pinned regular realizations.** Question: for [p1, ..., pn], compute the invariant form, its discriminants and Stiefel-Whitney classes in general, and prove that the degenerate characteristics are those dividing the Coxeter discriminant and the Gram entries. Why: unifies 70/68-72 and 72/45-113. Rests on: cote 72's continuants (verified n ≤ 5) and 70/68-70. Strongest reduction on the pages: δ_V = β_0^n···β_{n-1}·L_{n+1}(β), δ_E = β_0^n···β_{n-1}·L_n(β_1..β_{n-1}) (72/53). Material: `chk70.py`, `chk72.py`, K70-05..07, K72-03..07, MPL_72_035-081.
- **P3-3: which loops satisfy his closure condition?** Question: characterize the 3-nets satisfying (f_3f_2f_1)² = id at every point (74/14-16): Moufang loops exactly? Why: answers his question "le foncteur φ est-il une équivalence ?" on the subcategory he singles out. Rests on: 74/2-16, 69/101-119; Blaschke-Bol, *Geometrie der Gewebe*, 1938 (locator to be checked). Strongest reduction: his derivation of the left Bol identity (74/16); computed on M(S3,2). Material: `chk74a.py`.
<!-- /reading:cotes69-74 -->

<!-- reading:cotes76-79 -->
### From the reading cotes76-79

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
<!-- /reading:cotes76-79 -->

<!-- reading:cotes80-89 -->
### From the reading cotes80-89

none (survey reading; the packages of SA04 come from the full readings of cotes 93 and 94-102).
<!-- /reading:cotes80-89 -->

<!-- reading:cotes94-102 -->
### From the reading cotes94-102

- **P101-1: his 1958 Gorenstein and canonical-module characterizations, set against the literature.**
  - *Question:* state each characterization of 101/031-043 precisely (Propositions 13-16, the closing theorem, Problem C, and the margin that two of the three Ext conditions do not suffice). Prove or refute each, and give counterexamples for the pairs.
  - *Why:* it is the earliest dated form of this theory in the archive, and his own questions there remain open.
  - *Rests on:* Bass (1963); Roberts (1983); Bruns-Herzog, ch. 3.
  - *Strongest reduction:* SA04-R101-01 to -03.
  - *Material:* 101/017-043 after a reading on the scans.
- **P100-1: the good-reduction theorem of 100/003 in full.**
  - *Question:* prove the theorem as stated (full faithfulness, and the equivalence under étale depth ≥ 2 with a geometrically unibranch finite cover, or his simplicial condition), or find the hypothesis it needs. Compare it with the published extension theorems.
  - *Why:* it is the arithmetic outcome of the Barsotti-Tate programme of cote 93.
  - *Rests on:* Grothendieck (Invent. Math. 1966); Serre-Tate; Raynaud's descent for abelian schemes; Faltings-Chai ch. V; the Baire argument checked here.
  - *Material:* 100/002-045 after the divergent pages are decided on the scans.
<!-- /reading:cotes94-102 -->
