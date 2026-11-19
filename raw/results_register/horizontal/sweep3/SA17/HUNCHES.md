# SA17 hunches (sweep 3)

Written by Claude Opus 5.5 at effort max (a34c04448e8299803), 18 Nov 2026. Each hunch gives three things:
- what may be true;
- its grounds: the pages, and the derivations in STUDY.md;
- where it leads.

Literature locators are from memory under the context guard and are marked "to verify".

## Cote 129

**H1. His Δ*(G) exists over every base, and the co-Lie complex is its Frobenius cokernel (scan 94).**
- **On the page:** "Δ*(G) d'ampl. parfaite ⊂ [0,1] devrait exister sur toute base", next to ℓ^G ≃ D/DF ⊗^L M over a
  perfect field.
- **Grounds:**
  - Over a perfect field the formula gives ω_G = M/FM and n_G = ker F with equal ranks. I checked it on μ_p, Z/p and
    α_p.
  - BBM (LNM 930) attach to a finite locally free G a Dieudonné object through Ext's on the crystalline site. Prismatic
    Dieudonné theory (Anschütz-Le Bras) attaches a perfect complex over quasisyntomic bases. Both are to verify.
- **Hunch:** in the prismatic or crystalline theory, ℓ^G is recovered from the Dieudonné complex as a "D/DF ⊗^L"
  base change, that is, as the cone of the linearized Frobenius. That would make his scan-94 sentence a theorem over
  quasisyntomic bases.
- **Leads to:** package SA17-RP2(b).

**H2. The alternative hypotheses in IV anticipate display theory (scan 115).**
- **On the page:** "nilpotent divided powers, or the fibres of G_o have no toroidal component, or they are connected".
  The negation is in the ink; Michel Hua's paraphrase lacks it (credited).
- **Grounds:**
  - Grothendieck-Messing needs nilpotent divided powers (Messing V 1.6, to verify).
  - Zink's displays classify formal p-divisible groups with a nilpotence condition. Their deformation theory works
    along divided powers that are not nilpotent (Zink, Astérisque 278, to verify).
  - Lau's frames handle p = 2 under connectedness or unipotence conditions (to verify).
- **Hunch:** his two alternatives are, up to duality, the conditions under which those theories lift along
  non-nilpotent divided powers. Exactly one of "no toroidal component" (no multiplicative part) and "connected
  fibres" (no étale part) may be needed for each direction of the Hodge filtration.
- **Leads to:** package SA17-RP1(b).

**H3. V holds integrally for p ≥ 3, and for p = 2 the isogeny is what saves it (scan 115).**
- **Grounds (my derivation, CHECK_EVENTS SA17-13):**
  - pA is PD-nilpotent modulo p^N for p ≥ 3, so Grothendieck-Messing along A/p^N → A/p gives the integral statement.
  - For p = 2, 4A is PD-nilpotent modulo 2^N, because v_2(4^m/m!) ≥ m + 1. So the integral statement holds relative
    to A/4. What is left is the step A/4 → A/2, where the divided powers of 2 are not nilpotent.
- **Hunch:** the obstruction in that last step is killed by a bounded power of 2, which gives V up to isogeny for
  p = 2. His "à isogénie près" was the device for p = 2.
- **Leads to:** package SA17-RP1(a).

**H4. The scan-114 conjecture is a theorem over large classes of bases; the open part is the essential image.**
- **On the page:** "Il se pourrait que le foncteur BT(S)° → Cris Dieud(S) soit pl. fidèle, et j'ai une idée de ce qui
  pourrait être l'image essentielle". The idea is not on the sheet.
- **Grounds, all to verify:** full faithfulness is proved for several classes of bases by Berthelot-Messing III
  (1990), de Jong (Publ. IHÉS 82, 1995), de Jong-Messing (1999) and Anschütz-Le Bras.
- **A check of my own reasoning:** I first thought the crystal of G over k[ε]/(ε²) depends only on G mod ε, which
  would refute full faithfulness there. That is wrong. The ideal (ε) is not inside the divided-power ideal of the
  base, so crystals on S and on S_o differ. For the Serre-Tate deformation q = 1 + aε, log q̃ does not lie in the
  divided-power envelope of (p, x²). So no counterexample comes from this, and none is recorded.
- **Hunch:** what he meant by the essential image is the category of Dieudonné crystals (locally free, with F and V,
  FV = VF = p). The published course (SMS 45) is where to look for his formulation.
- **Leads to:** package SA17-RP2(a).

**H5. The closure sheets aim at Tate's extension theorem through finite levels (scans 106-110).**
- **Grounds:**
  - closures of generic-fibre subgroups over a trait;
  - flatness of intersections;
  - an epimorphism criterion for "divided groups";
  - Φ conservative, and Φ(u) not surjective unless u is formally smooth.

  These are the steps of Tate's proof that Hom(G, H) = Hom(G_η, H_η) for p-divisible groups over an integrally
  closed noetherian domain of generic characteristic 0 (Tate, Driebergen 1967, Thm 4, to verify). They also connect
  to Raynaud's prolongation results (Bull. SMF 102, 1974, to verify).
- **Weak ground:** the "1st conj." of scan 107 is not stated in this package. To be found in the Work folders or in
  cote 131 or 133.
- **Leads to:** no package until the conjecture is found.

**H6. The typescript of scans 1-76 is the course text of 1970, possibly the typescript of SMS 45.**
- **Grounds:**
  - The typescript's §2 (W_n, V_n, F, T_n with T_nF_n = F_{n+1}T_n, and λ acting through F^{1-n}(λ)) follows the
    plan of scan 78.
  - Its relations agree with the sheet of scan 81.
- **Leads to:** a collation with SMS 45, which decides whether the typescript is known material (place only) or a
  variant (edit). This is a deliverables question, not a research question.

## Cote 131

**H7. Generic modularity (8°) gives the constructibility that Prop. 3 needs, by noetherian induction.**
- **Grounds:**
  - Scan 6 reduces the theorem to "la condition de constructibilité de loc. cit.".
  - Next to Prop. 3, hypothesis 2, the margin says "Transformer en une condition de modularité 'générique'".
  - 8° is that condition.
- **Hunch:** for T of finite type and η ∈ F(T), 8° applied on the irreducible components of T and of the closed
  complements gives, by noetherian induction, that M(T, η) is a finite union of locally closed sets. This would close
  the main gap of cote 131.
- **Weak point:** 8° is stated for Z finite over S'. The induction needs it for T locally of finite type, through
  5° and quasi-finiteness.
- **Leads to:** package SA17-RP3.

**H8. 7° is superfluous under the strengthened 4°, by Krull and the argument of scan 20.**
- **Grounds:**
  - the margin of scan 14;
  - the scan-20 argument shows that formal coincidence plus finiteness over a local base forces equality.
- **Hunch:** with 4° for noetherian adic rings, modularity at the closed point propagates to all points of a finite Z
  over a complete local S'. A complete local ring is determined by its adic quotients, and the modular locus is
  stable under generization once the formal neighbourhoods agree.
- **Leads to:** package SA17-RP3 (ii).

**H9. The application "abelian schemes over a normal base are projective" (scan 17) may need a correction.**
- **Grounds:** I recall that Raynaud's LNM 119 (1970) treats exactly this question and gives limits and
  counterexamples. I cannot check now.
- **Hunch:** the sheet's statement is stronger than what is true, or true only locally over S.
- **Leads to:** a literature check inside SA17-RP3 before the statement is used anywhere.

## Cote 133 (scans 19-29 only)

**H10. Scans 24-27 anticipate FI-sets and representation stability.**
- **Grounds:**
  - functors on the category of finite sets and injections;
  - "equivalence" meaning bijective for |E| ≥ n, with 2-out-of-3 and base change;
  - the "distinguished" functors E ↦ ⊔_n Mon(I_n, E) ∧_{S_n} X_n.
- **Where this sits (to verify):** this is the setting of FI-modules (Church-Ellenberg-Farb, Duke Math. J. 2015) and
  of species (Joyal 1986, which the Pro notes cite).
- **Hunch:** his ring of distinguished functors modulo equivalence, with ⊔, × and composition, is a λ-ring with
  plethysm. It is the structure he looks for on scan 19 ("λ^i(xy) = ?"). The sheets of scan 28 (tensor powers in
  K(B_{S_n})) are his linear version of it.
- **Leads to:** package SA17-RP4.

## Cote 133, scans 2-18 and 30-54

From the reader a598c2dff473d448c (Claude Opus 5.5 at effort max), `readings/133_002-018_030-054.md`.

**H-133-1. His λ-ring question for the split WG(S) has a positive answer over a field of characteristic 0.**
- **Grounds:**
  - his reduction to B_{O(m)×O(n)} (scan 6);
  - complete reducibility of representations of O(m) × O(n), so that split and metabolic Grothendieck-Witt groups agree
    on B_G;
  - Zibrowius's λ-ring theorem for symmetric representation rings (2015; to verify).
- **Open part:** characteristic p > 2.

**H-133-2. Scans 36 and 46-54 are a crossed-module form of P. Hall's isoclinism.**
- **Grounds:** a group seen through G/Z(G), G' and the commutator map.
- **Literature (to verify):** P. Hall 1940; Beyl-Tappe, LNM 958; Aldrovandi-Noohi 2009.

**H-133-3. Scan 36 is a formal, characteristic-p counterpart of Rosenlicht's theorem.** The statements hold up to
isogeny, and the universal vector extension is the exact obstruction.

**H-133-4. The go identity is the territory-versus-area relation of the rule books.** Low priority.

## Cotes 126-132 (Work folders)

From the reader ac8bd2a26d00b4f37 (Claude Opus 5.5 at effort max), `readings/K126-K132.md`.

**H-K-1. Step 3 of cote 131 (descent from Ŝ to S) is settled for quasi-compact pieces; the locally quasi-finite case
needs one more idea.**
- **Grounds:**
  - X separated and quasi-finite over Ŝ is quasi-affine (EGA IV 18.12.12);
  - fpqc descent is effective for quasi-affine X (SGA 1 VIII 7.9; to verify).
- **For the locally quasi-finite case:** glue as an algebraic space, then use "separated, locally quasi-finite algebraic
  spaces are schemes".

**H-K-2. The type case of 126 scan 35 is a Nisnevich gluing question.**
- It is effective for quasi-affine X.
- Counterexamples are expected among algebraic spaces glued along an elementary distinguished square.

**H-K-3. Lemma 1.3 of cote 127 is true and provable with cote 128's conductor machinery.**

**H-K-4. Lemma 1 of cote 128 fails in characteristic 2 without an extra hypothesis.**
- **Grounds:** the factor c⁻¹ between the connecting maps; the model k[s]/(s²).

**H-K-5. Cote 130 contains the structure of Shioda's height formula two decades early.**
- **Grounds:**
  - the local corrections in (1/m)Z;
  - the formula Q(i(ξ), i(η)) = −ξ·η when all fibres are irreducible;
  - the Z/mZ pairing, which is Grothendieck's component-group pairing of SGA 7 IX.
- **Literature (to verify):** Shioda 1990.

**H-K-6. Cote 132 is the combinatorial start of the Teichmüller tower of the Esquisse (1984).**
- **Grounds:**
  - ribbon graphs;
  - T_{g,n} with holes and the boundary twists Z^I;
  - Ladegaillerie's embeddings;
  - scan 19's map Aut_circ(K) → T_{g,n}, which is the stabilizer of a dessin.
- **Links:** SA09 H4 (cote 138 as La Longue Marche Part I in draft).

**H-K-7. The B' identification of 132 scan 22 ("faux") is repaired by the 2-type of BH.** Extensions of H by a
discrete N are maps of 2-types, with Taylor's k-invariant in H³(π_0H, π_1H).
