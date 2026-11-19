# SA18: hunches (sweep 3, wave 1)

Merged by Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3 wave 1 (merge) from the readers' files in readings/. Each section is the reader's text, unchanged.

## From readings/c45_c56.md (Hunches (with grounds))

- **H1 (45:38 margin, 45:42).** Constructing the Chevalley groups over Z as Aut^0 of the Chevalley Lie algebra works over
  Z[1/N] exactly where H^0 = H^1 = H^2 (𝔤_{F_p}, 𝔤_{F_p}) = 0, and fails at small primes.
  - Grounds: his (1)-(3); my dim H^1 = 3 for pgl_2 in characteristic 2.
  - Expected bad primes: 2 for A_1, B, C, F_4; 2 and 3 for G_2; perhaps p | n+1 for A_n.
  - Literature: Hogeweij on Chevalley Lie algebras in bad characteristic, Hiss on H^1(G, 𝔤) (locators unverified).
  - Package R1.
- **H2 (45:55, Question 1).** For non-split ρ, a maximal torus T ≅ T_1 need not lie in a Borel.
  - Grounds: his N.B. covers only split T_1. Over F_q the question is whether wτ conjugate to τ in GL(X) forces w
    τ-conjugate to 1 in W. Over U_3 this holds (checked). Triality ^3D_4 is the natural candidate for failure.
  - Package R7.
- **H3 (45:59).** In "vrai pour les formes intérieures" he was thinking of inner forms with a Killing couple. The real
  obstruction to Aut(G) → Out(G) being onto, for inner forms of SL_n, is [D] ≠ [D^op] (the Tits class).
- **H4 (46:9).** The Fitting-ideal argument makes every finitely presented unit F-module locally free on any base. The
  infinite-type counterexample shows the Katz equivalence needs finiteness. This links to the mod-p Riemann-Hilbert
  correspondence for unit F-crystals (Emerton-Kisin; Böckle-Pink) (locators unverified).
- **H5 (46:19).** The object he means is the Frobenius neighbourhood V(I^[p^ν]). His margin ("ne fait intervenir que la
  section marquée") is exactly true for it.
- **H6 (47:10-11).** Over a base, the Chow-theoretic Fourier transform satisfies F(ab) = (-1)^g F(a)*F(b) with no Todd
  factor iff Todd(H^1_dR(A/S)) = 1 in CH_Q(S).
  - In characteristic 0 this holds by Esnault-Viehweg. In characteristic p, van der Geer's relation c(E)c(E^∨) = 1 on
    A_g suggests it too.
  - His pages anticipate the Deninger-Murre decomposition (Crelle 422, 1991), which needs this identity. Links SA07.
  - Package R2.
- **H7 (54:7, SA15).** Oda's theorem answers his question. The full Hodge-de Rham structure of an abelian scheme in
  characteristic p is determined by the BT_1 A[p] through its Dieudonné crystal. This is the bridge to SA15-16
  (`sweep3/SA15/STUDY.md` §2), where 2.7 shows why divided powers are needed for the crystal.
- **H8 (51:19-22).** The abelian subscheme of Pic_{X/S} should exist for X/S smooth projective over a reduced S in every
  characteristic, since the Picard variety of the fibres has constant dimension b_1/2. Over non-normal bases a
  non-reduced Pic^0 (Igusa) could break uniqueness. Package R4.
- **H9 (51:23).** His "analogue th. de pureté pour la bonne réduction" is the purity question for abelian schemes.
  - Mixed characteristic with small ramification: yes (Vasiu-Zink).
  - Otherwise there are counterexamples.
  - The torsor version d) should hold over regular bases where purity holds for the abelian scheme.
  - Links SA15-19 (Néron models and p-divisible groups, 100:48-53). Package R5.
- **H10 (52:10).** His "conoyau de dim 1, fibre Spec k[t]/t^2" is the genus-3 case. He probably had the
  quartic/hyperelliptic dichotomy of genus 3 in mind.
- **H11 (55:8).** His question (is the contraction J ∩ A of a finitely generated ideal of A[T] finitely generated, for A
  coherent) has a negative answer. A counterexample should exist in Soublin's coherent ring with A[T] not coherent.
  Package R6.
- **H12 (45:4-15).** Over imperfect fields of dimension ≤ 1 (F̄_p(t)), extensions by non-solvable infinitesimal
  kernels are the only open case of his surjectivity and H^2 theorems. The Cartan-subalgebra route cannot work, and a
  different argument, perhaps by Weil restriction or by passing to G/G_1, is needed. Package R3.
- **H13 (56:15).** Both degree slips on 56:15 shift by the same amount (2ν-2 for 2ν, 2ν-1 for 2ν). This fits an
  indexing of the cone over Q^n with the cone over Q^{n-1} mixed up. The other rows were computed correctly.
- **H14 (dating, SA18-19).** These are new datings, drawn from the pages:
  - 46:3, an EGA plan earlier than EGA I (about 1959);
  - 45:72-75, his comments to Delzant, 22 July 1961, preceding the CRAS note of 10 September 1962;
  - 48:2-5, an EGA VII plan citing SGAD and Mumford's book(s), 1965 or later;
  - 53, a course on algebraic groups with a participant's letter of 15 June 1973 and his rectification. This places a
    group-scheme course in spring 1973.
