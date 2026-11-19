# SA14: research packages (concepts) (sweep 3, wave 1)

Merged by Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3 wave 1 (merge) from the readers' files in readings/. Each section is the reader's text, unchanged.

## From readings/c57.md (9. Research packages (concepts))

- **P1. Grothendieck-Lefschetz for Pic in characteristic p without vanishing hypotheses (57:97, H3, H4).**
  - *Question:* for X smooth projective of dimension n >= 4 over an algebraically closed field of characteristic p and
    Y a smooth hyperplane section, prove or refute that Pic(X) -> Pic(Y) is an isomorphism (no condition on
    H^i(Y, O_Y(-m))). Also prove or refute injectivity for n >= 4 (his boxed "noyau nul").
  - *Why it matters:* it is his explicit question; the page reduces it to p-parts.
  - *Rests on:* 57:97, 57:99-101; SA14-3.
  - *Strongest reduction:* the cokernel (n >= 4) and the kernel (n >= 3) are finite p-groups of bounded exponent,
    built from the layers H^2(Y, O_Y(-m)) and H^1(Y, O_Y(-m)) for small m (checked here).
  - *Needs:* SGA 2 XI-XII; Hartshorne, Ample subvarieties, ch. IV; Bhatt-de Jong (local Picard); Raynaud's and
    Lauritzen-Rao's counterexamples to Kodaira vanishing.
- **P2. The infinitesimal kernel on the generic hyperplane section (57:100, H1).**
  - *Question:* prove or refute that there is a smooth projective X of dimension >= 2 over an algebraically closed
    field of characteristic p, with a very ample O_X(1), such that H^1(X, O_X(-1)) != 0. Such an X is exactly a case
    where the kernel of Pic^tau_X (x) Kbar -> Pic^tau_{Y_Kbar} is nonzero.
  - *Why it matters:* it decides whether his corollary's "purement infinitésimal" kernel is ever nonzero; it is a
    Kodaira-vanishing question for very ample sheaves.
  - *Rests on:* 57:99-100; the computation Lie K = h.H^1(X, O_X(-1)).
  - *Strongest reduction:* K = 0 iff H^1(X, O_X(-1)) = 0; for a surface this means H^1(O_X) -> H^1(O_C) is not
    injective for a smooth hyperplane curve C.
  - *Needs:* Raynaud (1978) on Kodaira vanishing; Mumford's pathologies; Lauritzen-Rao (1997).
- **P3. Seshadri's theorem without Pic, and the relative-complete-intersection question (57:105-111, H2, H13).**
  - *Question:* for f: X -> S proper flat with geometrically integral (S_2) fibres over a normal noetherian S, prove or
    refute that a Weil divisor on X with no vertical component and Cartier on the generic fibre is Cartier; and
    determine the exact fibre condition (R_2 sufficient over regular S by the argument here) under which Question 2 holds.
  - *Why it matters:* his two questions on 110-111; Question 2 is refuted here as stated.
  - *Rests on:* 57:104-114; SA14-4, SA14-18.
  - *Strongest reduction:* the smooth case (Ramanujam-Samuel); the counterexample xy - z^2 - t^2 (relative dimension 3,
    normal fibres); the positive refinement with regular S and R_2 fibres (SGA 2 XI parafactoriality).
  - *Needs:* EGA IV 21.14; SGA 2 XI; Kleiman 2005.
- **P4. The henselian questions of 1962 (57:227-231, 272, 193-194, H5, H12).**
  - *Question:* for A the henselization of a local ring of finite type over a field of characteristic 0 (and over
    excellent DVRs), prove or refute (i) X^/Y^ projective => X/Y projective; (ii) Pic(X) = Pic(X^) when R^1 f_* O_X has
    finite length; (iii) Pic(Y - y) = Pic(Y^ - y^) at isolated singularities. In characteristic p, prove or refute the
    agreement of the local NS groups of S, S~ and S^ modulo p-groups.
  - *Why it matters:* these questions are the origin of SGA 2 XIII and of approximation theory; the page proves the
    analytic case.
  - *Rests on:* 57:227-272; SA14-5, SA14-6.
  - *Strongest reduction:* the analytic theorem (Th. 1.7, Th. 2.1, Cor. 2.4, proved on the pages); the cone computation
    (bijectivity iff H^1(X, O_X(n)) = 0 for n >= 1; Pic(S~ - a) = Pic(S^ - a) for cones over curves).
  - *Needs:* Artin, Publ. IHES 36 (1969); Boutot, LNM 632; Danilov (1968); SGA 2 XII-XIII.
- **P5. Hodge asymmetry and jumps from quotients (A x B)/Gamma (57:283-288, 297).**
  - *Question:* construct, or prove impossible within this family, (A, B, Gamma) with Gamma finite acting on an abelian
    scheme A and freely on B, such that dim (t_{A'})^Gamma - dim (t_A)_Gamma is > 0, < 0, or varies in a family. This is
    the asymmetry h^{01} - h^{10} of X = (A x B)/Gamma. Settle also whether A'^Gamma can fail to be flat, with the
    consequences he lists (Pic^tau not flat; the Picard variety not compatible with specialization).
  - *Why it matters:* it is his plan for systematic pathologies of Pic in characteristic p; Igusa's own example gives
    difference 0 (checked here).
  - *Rests on:* 57:283-288, 297, 311 ("étudier la famille modulaire de la surface de Igusa").
  - *Strongest reduction:* Pic_X = Pic_Y x Pic_A^Gamma and Pic^tau_X = Pic^tau_Y x A'^Gamma (286, checked); the formula
    for h^1(O) - h^0(Omega^1) (287).
  - *Needs:* Igusa (1955); Mumford's pathologies; W. Lang's examples; Oort on group schemes.
- **P6. Properness of Pic^0 for normal families and separatedness of Corr (57:314-315, 22, 32; H7, H9).**
  - *Question:* for X normal and proper over a trait with a section, prove or refute that every L on the generic fibre
    algebraically equivalent to 0 extends to X with special fibre algebraically equivalent to 0. Prove or refute that
    Corr_S(X, Y) is separated for X, Y proper flat with f_* O = O universally.
  - *Why it matters:* his questions on 314-315 and in the letter to Murre; the properness of Pic^0 for normal
    degenerations.
  - *Rests on:* 57:21-22, 30-32, 309-315; SA14-4, SA14-9.
  - *Strongest reduction:* both hold when Pic_{X/S} is representable (projective X); Corr is separated if Pic of a
    factor is separated (integral geometric fibres).
  - *Needs:* Raynaud, Publ. IHES 38 (1970); Artin's algebraic spaces; Kleiman 2005.

## From readings/c58_c60.md (7. Research packages (concepts))

RP-S1, planned at first for 60:53, is settled in §2.5(d): μ_x(E) = 0 for every E, and the answer to "δ^♮(E)^2 =
q^{χ^♮(E)} ??" is yes. It is not a research package.

### RP-S2. Finite generation of the local étale fundamental group (58:19)

- **Question** (settled by a proof or a counterexample). Let A be a complete noetherian normal local ring of dimension 2
  with algebraically closed residue field, and U = Spec A − {m}. Is π_1^ét(U) topologically finitely generated?
- **Why it matters.** With 58:19 and its "Conséquence", a positive answer gives the topological finite generation of π_1
  of the punctured spectrum of every complete local ring with algebraically closed residue field: this is Grothendieck's
  "Conjecture". A negative answer bounds what the local Lefschetz theorem can transport.
- **What it rests on.**
  - 58:9-13 (the connectedness theorem, §3.2);
  - 58:19 (the local Lefschetz theorem for π_1, re-proved in §3.4);
  - the dévissage to normal rings of dimension 2. It is not written on the page; normalization is finite and local for
    complete rings.
- **Strongest reduction known.**
  - On the page: to normal A of dimension 2.
  - In characteristic 0: π_1(U) is the profinite completion of the fundamental group of the link, a finitely presented
    3-manifold group (Mumford, Publ. IHES 9, 1961; locator unverified).
  - In characteristic p:
    - the tame quotient is topologically finitely generated (Grothendieck-Murre, LNM 208, 1971; locator unverified);
    - for strongly F-regular A, π_1(U) is finite (Carvajal-Rojas, Schwede, Tucker; locator unverified).
  - Derived here: H^1(U_1, Z/p) is finite for every connected finite étale U_1 -> U.
    - U_1 is the punctured spectrum of a normal 2-dimensional A_1, and F − 1 is onto on A_1 (Hensel, k algebraically
      closed). So H^1(U_1, Z/p) = ker(F − 1 | H^2_m(A_1)).
    - That kernel is finite by the Hartshorne-Speiser-Lyubeznik theorem (locator unverified).
    - For ℓ ≠ p, H^1(U_1, Z/ℓ) is finite through Kummer theory and the finite ℓ-torsion of Cl(A_1) (Lipman, Publ. IHES
      36, 1969; locator unverified).
  - What remains: finite H^1 of every open subgroup does not imply topological finite generation (∏ A_5 is a
    counterexample to that implication). The open part is the non-abelian wild ramification along the exceptional
    curves of a resolution.
- **Material a run needs.**
  - 58:3-19 (this reading, §3);
  - SGA 1 X and XIII; SGA 2 X and XIII; Grothendieck-Murre (LNM 208); Mumford 1961; Lipman 1969;
  - Hartshorne-Speiser (Ann. Math. 1977) and Lyubeznik (Crelle 1997) on Frobenius actions;
  - Carvajal-Rojas-Schwede-Tucker on fundamental groups of F-regular singularities;
  - the literature on wild Z/p-quotient singularities of surfaces (Artin; Peskin);
  - all locators unverified. The run first establishes the state of the question in the literature.

### RP-S3. Canonical points of the torsors Pic^δ (59:10-14, 59:26-28)

- **Question** (settled for each type by a proof or a refutation). For which types D = (d_1 | ... | d_n) does the torsor
  Pic^δ_{A/S} have a section over the moduli stack of abelian schemes with a polarization of type D over Z[1/2], that
  is, a line bundle in the class δ chosen compatibly with base change? Do the trivializations of his page coincide with
  the canonical ones?
- **Why it matters.**
  - Cote 59 constructs canonical trivializations of (Pic^δ)^{⊗2χ(δ)^{n−2}} and, for χ(δ) even, of
    (Pic^δ)^{⊗χ(δ)^{n−2}}, and asks whether they are the canonical sections ("à vérifier"). The exact answer fixes what
    the determinant construction gives.
  - It joins his theta divisor (59:26-28) to the determinant of cohomology.
- **What it rests on.** 59:10-14 and 59:26-28 (§4.3, §4.4, §4.8); the boxed relation re-proved in §4.3(a).
- **Strongest reduction known.**
  - Existence:
    - when at most one d_i is odd, by Mumford's e_*^L (§4.4(c), derived here for n = 2; the same argument works for every
      n, since the polar form on A[2]/R is nondegenerate of rank 2·#{i : d_i odd} and a unique refinement is
      distinguished only in ranks 0 and 2);
    - (Pic^δ)^{⊗2} always (the point (1, δ̃)^*P_A);
    - for n = 2 the page's answer (χ even) matches.
  - Open: non-existence when two or more d_i are odd. This needs the monodromy of the moduli stack to act on the
    refinements with only the two Arf orbits, as for the 10 even and 6 odd theta characteristics in genus 2. Also open:
    whether his determinant trivializations equal these.
  - Probably in the literature on the characteristics of line bundles (Birkenhake-Lange, "Complex Abelian Varieties",
    ch. 4; locator unverified); a run first searches there.
- **Material a run needs.**
  - pages 59:2-28 (this reading, §4);
  - Mumford, "On the equations defining abelian varieties I" (Invent. Math. 1, 1966);
  - Birkenhake-Lange ch. 4 and 8;
  - Moret-Bailly, Astérisque 129;
  - Faltings-Chai ch. I;
  - Mukai, Nagoya Math. J. 81 (1981);
  - Knudsen-Mumford (Math. Scand. 39, 1976);
  - all locators unverified.
