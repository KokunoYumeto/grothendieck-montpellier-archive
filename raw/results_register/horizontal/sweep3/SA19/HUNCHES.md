# SA19: hunches (sweep 3, wave 1)

Merged by Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3 wave 1 (merge) from the readers' files in readings/. Each section is the reader's text, unchanged.

## From readings/c43_c44.md (5. Hunches (the whole stretch))

- **H1. An early statement of Grothendieck's pairing on component groups (43:117).** Boxed beside the duality
  H^1(K,A) = Ext^1_{k-gr}(ℬ, Q/Z) is "(2) π_0(A) et π_0(B) duaux (à valeurs dans Q/Z)", for dual abelian varieties
  over a complete field with algebraically closed residue field. The dossier's dated leaves (Shatz's thesis of June 1962
  on 144, a September-1963 list on 118, "mai 1964" on 87) place it years before SGA 7 IX 1.3 (1967-69), where the
  pairing is a conjecture; it was proved for perfect residue fields by Bégueri (algebraically closed, mixed
  characteristic), McCallum, Bertapelle and Suzuki, and fails for some imperfect ones (Bertapelle-Bosch). Suzuki's proof
  runs through exactly the programme of these pages: Serre duality of Néron models as group objects over the residue
  field, on a perfect site. Links: SA18-11 (integral models and local duality), SA19-2.
- **H2. Biextensions before SGA 7 VII (43:16, 43:21).** The three-argument notation Ext^1(A, B; C) appears twice: for
  "l'accouplement de Lang" (a biextension of Ext^1(J,G) x J'(k) by G(k)) and for Tate's pairing of dual abelian
  varieties over a Galois extension (Ext_{Z(Γ)}(A_L, A'_L; L^*), with a cup product built from resolutions). The pairing
  of 204-205 is built from Pic of a torsor. These are the biextension constructions of SGA 7 I, VII-VIII (1967-68) and
  Mumford's (1969), in a 1962-64 dossier. Links: SA18-14 (duality of abelian varieties), SA19-1.
- **H3. Higher adèles and the residue complex through chain completions (43:45-69).** He writes (a) the recursive
  adèles over chains of points, 𝒜^{n+1} = ∏_a lim_k 𝒜^n ⊗ O_a/m_a^k, with "l'inclusion étant fidèlement plate" (Parshin
  1976, Beilinson 1980, Huber 1991); (b) the rings A_{[p_1..p_n]} by iterated completion and Hom(K_p, K_q) = A_{q,p} for
  the injective hulls K_p = E(A/p); (c) the endomorphism algebra of the residual complex, End^0 = ∏ Ô_x, the differential
  θ ∈ ∏ Hom(K(x), ⊕ K(x')) ≅ ∏' Ô_{x,x'}, θ^2 = 0, and "𝒜 libre pour ces propriétés". Item (c) is Yekutieli's explicit
  construction of the Grothendieck residue complex from Beilinson completion algebras (Astérisque 208, 1992), here as
  a presentation of End(K^•) by generators and relations, which is the precise new question (research package RP1).
  Links: SA19-5; the duality theory of Residues and Duality.
- **H4. Local cohomology of algebraic groups and local Jacobians (43:70-76, 43:80).** For A regular local of dimension
  d >= 2, H^i_A(G) vanishes except in degree d and sees only the unipotent part (checked here), so the local Jacobian
  J_{A/k} is pro-unipotent and projective; for d = 1 it is linear with multiplicative part G_m; for d = 0 it is the
  generalized Albanese of the function field, and Ext^*(J_{K/k}, G) = H^*(K, G) is his boxed derived form of geometric
  class field theory. The degree >= 2 part is open in characteristic p (research package RP3). This is a geometric
  analogue of higher local class field theory (Parshin, Kato): for d = 2, J_{A/k} is the object whose Hom into G_a is
  H^2_m(A). Links: SA19-1, SA19-5, SA19-6 (Witt and Dieudonné rings of 181-202).
- **H5. Cote 44: the programme is half known, half false, half open.** Th. 1-2 and the endpoints of Th. 3 are the
  existence of algebraic representatives (known for codimensions 1, 2 and n); Th. 7 is false (Griffiths); Th. 3's duality
  P^i ~ P^{n+1-i} for 2 <= i <= n-1 and Th. 4's positivity in characteristic p are open as far as the pages and the
  checked literature go; Th. 5 holds for surfaces with integral fibres (checked) and is a version of the comparison
  between the height on the generic member of a pencil and the intersection pairing on the total space (Néron, Tate,
  Shioda; for higher codimension Beilinson-Bloch heights). Links: SA18-14, SA18-12 (standard conjectures), SA16.
- **H6. The "1983 bridge" planning question.** The Pro package was asked whether these leaves contain the
  point-to-section injectivity argument; they do not (Pro's finding, confirmed on 1-93 and 143-208 too: no Abel map from
  an open curve into a generalized Jacobian together with an injectivity statement on points). What the leaves give is
  the derived form H^*(X - S, G) = Ext^*(P_S, G) (43:28-34) from which an injectivity statement for the Abel map on
  π_1^ab follows (Cor. 3 and its "il semble ... bijectif"), the input ANABELIAN_A1_SUCCESSOR's B.68 needs.
