# SA17, Descentes (cotes 126-133): sweep 3, the topic worked through

Written by Claude Opus 5.5 at effort max (agent a34c04448e8299803), horizontal sweep 3, 18 Nov 2026 from 22:35 UTC.
Brief: the main session's message of 18 Nov ~22:2x UTC ("Sweep 3 starts now"): read every transcribed page in full,
work through the mathematics, close the dependencies by reading, write the hunches and the research packages in
concept, and record the deliverables per cote and scan range.

How to read this file:
- **On the page** is what he writes.
- **Checked** is a re-derivation of mine; each one is a row in CHECK_EVENTS.tsv.
- **Known** cites the literature. Locators marked "(to verify)" were given from memory under the context guard,
  which forbids reading literature now; they must be checked before any public use.
- **Wrong** and **open** are as defined in the brief.
- **Readings decided on the image** were decided at 300 dpi crops of the scans in `grothendieck_archive_montpellier/14_descentes/129.pdf`
  (page number = scan number). They are listed in CORRECTIONS.tsv.

What this study covers:
- **Cote 129, scans 77-115** (Pro package MPL_129_077-115): read in full and worked through, below.
  - Scans 79 and 89 are absent from the package.
  - Scan 112 is blank.
  - Scans 99, 101, 103, 105, 109 and 111 are reused printed pages (SA17-10).
- **Cote 129, scans 1-76:** the typescript of the course text (the Witt vector chapter and onward;
  `inputs/SA17/api/montreal_seminar_129_combined.tex`). It is placed only. The transcribed pages do not name its
  writer, and that remains to be established.
- **Cotes 131 and 133 and the Work folders K126-K132:** see their sections. Each section says how far it was read.

## Cote 129, scans 77-115: his notes for the 1970 Barsotti-Tate course and the "Conférence à Nice"

Scan 78 gives the plan of the course:
- I. Witt vectors;
- II. Dieudonné theory;
- III. generalities on BT groups;
- IV. divided powers and crystals;
- V. the Dieudonné functor over a general base (programme and problems);
- VI. F-crystals and a specialization theorem.

The sheets that follow carry out I-V in note form. On scan 113 a new set of sheets starts, headed "Conférence à Nice".

Context (to verify):
- The course is the Montréal summer school of 1970, published as *Groupes de Barsotti-Tate et cristaux de
  Dieudonné*, Sém. Math. Sup. 45, Presses de l'Université de Montréal, 1974.
- The talk is "Groupes de Barsotti-Tate et cristaux", Actes du Congrès international des mathématiciens (Nice
  1970), t. 1.

His references on the sheets are "lettre Illusie 5.3 / 6.4" and "Notes I". Illusie's exposé "Déformations de groupes
de Barsotti-Tate (d'après A. Grothendieck)", Astérisque 127 (1985), is built on those letters.

### SA17-2 · Witt vectors (scans 80-81)

**On the page:**
- The ghost components φ_i = x_1^{p^{i-1}} + p x_2^{p^{i-2}} + … + p^{i-1} x_i.
- The maps V (shift), R (restriction W_{n+1} → W_n) and a map W_n → W_{n+1}, read T by the transcription.
  Whether the letter is T, Π or D is open, and so is "type D".
- The relations R_n T_n = V_n and T_n R_n = V_{n+1}.
- F with FV = VF = p in characteristic p.
- The colimit of the W_n.
- In characteristic p: T∘F = p and p∘F^{n-1} = F^n∘T.
- The map u: lim→ W_n(k) ≅ K/W for k perfect.

**Checked:**
- R_nT_n = V_n and T_nR_n = V_{n+1} hold by a computation on the components, with T the injective shift
  W_n → W_{n+1}.
- In characteristic p, T∘F = VF = p as maps W_n → W_{n+1}. Since T commutes with F (the typescript of scans 1-76
  writes T_nF_n = F_{n+1}T_n), F^n∘T = T∘F^n = p∘F^{n-1}.
- These identities are what makes the colimit along T agree with the colimit along multiplication by p, which is
  K/W. The identification needs a Frobenius twist, u_n(x) = p^{-n}F^n(x̃). The typescript does the same when it
  makes λ ∈ W act on (W_n)_k by multiplication by F^{1-n}(λ).

**Status:** the definitions and the identities are correct. The sheet stops before the W-module structure, which
the typescript supplies.

### SA17-3 · Dieudonné theory over a perfect field (scan 82)

**On the page:**
- G ≅ G_et × G_mult × G_bi.
- The anti-equivalence G ↦ D*(G) with W-modules of finite length carrying F and V (Fλ = λ^σF, λV = Vλ^σ).
- The dictionary:
  - G unipotent ⟺ V_M nilpotent;
  - G* unipotent ⟺ F_M (word discussed below);
  - G étale ⟺ F_M iso;
  - G* étale ⟺ V_M iso.
- On the left margin: F nilpotent ⟺ G_et = 0, and V nilpotent ⟺ G_mult = 0.

**Readings decided on the image:**
- The ink has "FV = p.id , FV = p.id": he wrote FV twice. The second should be VF = p·id. This is his slip, and the
  transcription is faithful to it.
- The word after F_M is closest in the ink to "unipotent", the same shape as the word after G*. The mathematics
  requires "nilpotent": F_M is an endomorphism, and G* unipotent ⟺ G connected ⟺ F_M nilpotent. The reading stays
  marked; the edition notes the correction.

**Checked:** with those two corrections, the dictionary agrees with the contravariant theory.

**Known (to verify):** Demazure-Gabriel, *Groupes algébriques* I, ch. V; Fontaine, Astérisque 47-48 (1977).

### SA17-4 · Barsotti-Tate groups (scans 84-88)

**On the page:**
- **Example (a):** an extension of an abelian scheme of dimension a by a torus of dimension m gives a BT group of
  height 2a + m.
- **Example (b):** formal Lie groups on which p is an epimorphism. "Il devrait être vrai" that G(1) is finite
  locally free, with the margin "(†) fibres de hauteur localement constante".
- Ind-étale and toroidal BT groups, and the filtration G^tm ⊂ G^o ⊂ G.
- A counterexample over a trait: the modular elliptic curve at the points where the Hasse invariant vanishes. The
  generic fibre is ordinary and the special fibre supersingular, so the separable rank jumps and G^o is not a BT
  group over the trait.
- A proposition (i)-(iv) with a "Lemme (EGA IV ?)": the étale-radicial factorization exists iff the separable rank of
  the fibres is locally constant.
- Scan 88: extensions of BT groups and cokernels of monomorphisms of BT groups are BT. The height is r, and G(n) has
  rank p^{rn}.

**Checked:**
- **Height 2a + m:** p^n is an epimorphism on the torus, so 0 → T[p^n] → E[p^n] → A[p^n] → 0 is exact. The ranks
  are p^{nm}·p^{2an}.
- **Scan 88:** the snake lemma for p gives 0 → G'(1) → G(1) → G''(1) → G'/pG' = 0.
  - G(1) is a G'(1)-torsor over G''(1), hence finite locally free.
  - For a cokernel, G''(1) = G(1)/G'(1) is the quotient by a closed flat subgroup.
  - p is an epimorphism on G'' because it is one on G.

**Known (to verify):** the expectation of example (b) holds under his hypothesis (†): Messing, LNM 264, ch. II §3;
Tate, "p-divisible groups" (Driebergen 1967), §2, over complete local noetherian rings.

**Open:** where his "Lemme (EGA IV ?)" stands in the literature (EGA IV_4 §18.5; to verify).

### SA17-6 · cotangent complex and co-Lie complex (scans 92-94)

**On the page (scan 93):**
- ℓ^{G/S} = Le*(L^{G/S}), the co-Lie complex. The margin says it was introduced by "Mazur-Roberts" (the
  transcription reads "Mazur-Robert"; Mazur-Roberts, Invent. Math. 9 (1970), to verify).
- ℓ̌ = RHom(ℓ, O_S), the Lie complex. For G locally of finite presentation and complete intersection, ℓ has perfect
  amplitude in [-1,0] and ℓ̌ in [0,1].
- Notation: ω_G = H_0, n_G = H_1, t_G = H^0(ℓ̌), ν_G = H^1(ℓ̌), with t = ω̌ and n = ν̌.
- rg ℓ^G = dim G (= rg ω_G − rg n_G when both are locally free).
- The transitivity triangle ℓ^{G''} → ℓ^G → ℓ^{G'} →(+1) for an exact sequence 0 → G' → G → G'' → 0 of flat
  groups.
- The resulting exact sequence when G' is locally of finite presentation.
- The "Formule remarquable": RHom(ℓ^G, J) ≃ τ_{≤1} RHom(G*, J). On scan 92 it carries "à vérifier !".

**Checked:**
- **Transitivity:** the triangle follows from the transitivity triangle of G → G'' → S, restricted along the unit
  section, with G ×_{G''} S ≅ G' (flat base change). The long sequence is
  0 → n_{G''} → n_G → n_{G'} → ω_{G''} → ω_G → ω_{G'} → 0.
  His own triangle on the same page forces this order. In the ink the n-subscripts are not legible with certainty:
  the second is written over. The reading stays open, and the apparatus gives the forced sequence.
- **The Formule remarquable, H^0 tested** over a base of characteristic p:
  - Hom(Z/p, G_a) = G_a = Lie μ_p;
  - Hom(μ_p, G_a) = 0 = Lie Z/p.

  It is consistent on both. The general statement is known (Illusie, *Complexe cotangent et déformations* II,
  LNM 283, ch. VII §3, to verify) and is not re-proved here.
- **Scan 94: ℓ^G ≃ D/DF ⊗^L M over a perfect field,** with M the Dieudonné module. It gives ω_G = M/FM, n_G = ker F
  and equal ranks. Tested on μ_p, Z/p and α_p: consistent.

**Open, his:** "Δ*(G) d'ampl. parfaite ⊂ [0,1] devrait exister sur toute base". See HUNCHES H1.

### SA17-5 · deformations of BT groups (scans 91, 95)

**On the page:**
- Théorème 4.1 (a)-(d): existence of deformations of BT groups and of truncated BT groups along nilpotent
  immersions, surjectivity at finite level, and the torsor of deformations.
- The pointers "cf lettre Illusie 6.4" and "je ne sais pas procéder directement !".
- Scan 95: Deligne-Illusie on deformations of flat groups, and truncated BT groups ("Lettre Illusie 5.3").

**Status:** announced, with the proof in the letters to Illusie.

**Known (to verify):** Illusie, Astérisque 127 (1985), §4 (Théorème 4.4 and its corollaries). Nothing is
re-derived here: the page has no argument.

### SA17-7 · truncated BT groups and the Ext comparison (scans 95-96)

**On the page:**
- Ext¹_{Λ_n}(G, M) = 0 and Ext²_{Λ_n} ≅ Ext²_Z.
- NB: Ext²_Z(G, M) = 0 if 2 is invertible.

**Known:** the Pro notes of this package found the locator (notes lines 530-541):
- Illusie, Astérisque 127, Remarque 4.6(a), p. 178. It cites Breen for the vanishing at odd p with additive
  coefficients, and gives a characteristic-2 example.
- Breen, Ann. Sci. ÉNS 8 (1975), 339-352, the theorem and Remarks 1-3, pp. 339-340.

The notes also show that the statement must be read as a sheaf Ext. Globally, G = Z/p and M = O give
Ext² ≅ H²(O) ⊕ H¹(O). This is the notes' finding, not mine.

### SA17-12 · Serre-Tate and the Nice definition (scan 113)

**On the page:** the definition of BT groups, and the Serre-Tate theorem (deformations of an abelian scheme equal the
deformations of its BT group).

**Known (to verify):** Katz, "Serre-Tate local moduli", LNM 868 (1981); Messing LNM 264, ch. V. The hypotheses on the
sheet are incomplete (sweep 2): p must be locally nilpotent, and the immersion nilpotent.

### SA17-11 · divided powers and the crystalline site (scans 113-114)

**On the page:** divided powers, exp and log, and the crystalline site, with the margin "Berthelot (et Illusie)".

**Known (to verify):** Berthelot, LNM 407 (1974). The formula conflicts recorded in the notes (N74, N79) stand as in
sweep 2. I did not re-derive them in this pass.

### SA17-13 · crystals and the Dieudonné functor (scans 114-115)

**On the page (scan 114):**
- **Ex. 1:** crystals over a perfect ring A_o of characteristic p are W(A_o)-modules.
- **Ex. 2:** on a smooth base, crystals are modules with an integrable connection, with a nilpotence condition, and
  the "germes d'animaux … Dwork, Katz".
- The Dieudonné functor D(G).
- His conjecture: "Il se pourrait que le foncteur BT(S)° → Cris Dieud(S) soit pl. fidèle, et j'ai une idée de ce qui
  pourrait être l'image essentielle". The idea itself is not on the sheet.

**On the page (scan 115):**
- **III:** for S = Spec k, k perfect of characteristic p > 0, one gets back the usual Dieudonné functor.
- **IV (decided on the image):** D(G)_S is filtered by **0 → ω_G → D(G)_S → ω̌_{G*} → 0**.
  - The ∨ above the first ω and the * of its subscript are written over in the same way, so the transcription's
    "ω_{G*}" should read ω_G.
  - The rank count confirms it: rk ω_G + rk ω̌_{G*} = d + d* = h = rk D(G), as in his margin "d + d* = h" on
    scan 90. With ω_{G*} the ranks would sum to 2d*.
- **IV, deformations:** for S_o ⊂ S a thickening with divided powers ("ép. à p. div."), assume one of the following:
  - the divided powers are nilpotent;
  - the fibres of G_o have no toroidal component (the negation is in the ink; Michel Hua's paraphrase lacks it, as
    found in sweep 1, credited);
  - the fibres of G_o are connected.

  Then lifting G_o is "la même chose" as lifting the filtration of D(G_o)_{S_o} to D(G_o)_S.
- **V:** BT groups up to isogeny over A, separated and complete for the p-adic topology, with A_o = A/pA. The functor
  G ↦ (G_o, filtration on D(G_o)_A) is fully faithful.
- **V, the complete local case:** for A complete local noetherian with perfect residue field k, a BT group up to
  isogeny is known once one knows G_o over k (its Dieudonné module M) and a filtration on (M ⊗_W A)_{p|Q}. The
  index is read uncertainly; it is probably ⊗Q.

**Known (to verify):**
- **IV under nilpotent divided powers** is the Grothendieck-Messing theorem, Messing LNM 264, ch. V, Thm 1.6.
- **V over the ring of integers of a p-adic field** is the classification of p-divisible groups up to isogeny by
  filtered Dieudonné modules:
  - Fontaine, Astérisque 47-48;
  - for the essential image, Breuil (p > 2) and Kisin (all p).

  This is the "foncteur mystérieux" programme.

**Checked, my derivation (a reduction, not checked by a second party):** for p ≥ 3, V holds integrally, and with
filtrations on D(G_o)_A itself.
- The ideal pA always carries divided powers (γ_m(pa) = (p^m/m!)a^m). It is PD-nilpotent modulo p^N when p ≥ 3,
  because v_p(p^m/m!) ≥ (m(p−2)+1)/(p−1) → ∞.
- So Grothendieck-Messing applies along every A/p^N → A/p.
- BT groups over a p-adically complete A are the compatible systems over the A/p^N (de Jong, Publ. IHÉS 82 (1995),
  2.4.4; to verify).

For p = 2 the divided powers on 2A are never nilpotent: γ_{2^k}(2) has 2-adic valuation 1. That is the case his "à
isogénie près" and his alternative conditions in IV have to cover. See HUNCHES H2-H3 and package SA17-RP1.

### SA17-8 · Tate objects, "Sottises sur groupes p-divisibles" (scans 97-104)

**On the page:**
- An object A with an endomorphism f, f^n = 0, and conditions (i)-(iv). The rank identity rg(A) = n·rg(A/fA)
  characterizes the "Tate" objects: locally free over O[f]/(f^n), the model being G(n) with f = p.
- A morphism criterion and the uniqueness of Tate sub-objects (scan 102).
- The group-scheme version (scan 104).

**Checked:**
- (ii bis) ⇒ (iii) (scan 98).
- S_j ⇒ S_{j-1} and A/f^{n-1}A ≅ fA (scan 100).
- The morphism criterion and the uniqueness corollary (scan 102).
- (ii) ⇒ (i) for group schemes, through the fibrewise flatness criterion (scan 104).

All agree.

**Open readings:** a bound on scan 100 and the title word "Sottises" (scan 97).

### SA17-9 · closures over a trait and a Galois dévissage (scans 106-110)

**On the page:**
- Schematic closures of subgroups of the generic fibre: G'_1 = G'_2 ∩ G_1 iff flat, and "the question is Ker α''".
- Scan 107, in English: "? Proof of 1st conj." by Galois dévissage.
- Scan 108: conditions a)-f), and the example (Z/p² × Z/p²)_η with u, F and V.
- Scan 110: an epimorphism criterion for "divided groups" over a trait. Φ is conservative, and Φ(u) is not surjective
  if u is not formally smooth.

**Status:** self-flagged, unfinished.

**Open reading:** α_p^{2?} and the group orders on scan 108. They differ from Michel Hua's reading (sweep 1,
credited).

**Not re-derived:** the "1st conj." itself is stated on a sheet outside this package or not at all. See HUNCHES H5.

### SA17-10 · reused printed pages (scans 99, 101, 103, 105, 109, 111)

These are printed rédaction pages numbered n° 380 and n° 382: §4 "Algèbres de fonctions" (Stone-Čech, closed
equivalence relations), and "3.6 Critères d'analyticité". He wrote nothing on them. The author is not identified on
the page. They are placed only.

### SA17-1 · codicology

- The plan is on scan 78.
- Scan 79 is absent from the package, and so is scan 89.
- Scan 112 is blank.
- Scans 113-115 are the Nice sheets.
- The archive foliation runs 1 ahead of the scan number: scan 82 is folio 83, scan 93 is folio 94, and scan 115 is
  folio 116.

### How cote 129 connects

The order of dependence is:
- Witt vectors (SA17-2) → Dieudonné theory (SA17-3) → BT groups (SA17-4);
- the co-Lie complex (SA17-6) → deformations (SA17-5) → Serre-Tate (SA17-12);
- divided powers (SA17-11) → crystals and the Dieudonné functor (SA17-13), which collects all of them;
- the Tate-object sheets (SA17-8, SA17-9) are a side line on the structure of G(n) and on closures over a trait.

Every dependency row is read from the pages in DEPENDS.tsv.

Across topics:
- The divided powers and crystals of scan 113-114 meet the de Rham notes (SA08, SA09).
- The "Notes I" references point to an earlier sheet set, not in this package.

## Cote 131, scans 2-42: representability by locally quasi-finite separated schemes

Package MPL_131 (38 scans; scans 11, 19 and 22 absent). Read in full on 18 Nov at about 22:45 UTC.

**His sheets** are the odd and low scans: 2-7, 9, 12, 14-17, 20, 23, 25, 27, 29, 31, 33, 35, 37, 39 and 41.

**Reused printed rédaction pages** are interleaved. They are placed only (SA17-19), and their author is not identified
on the page:
- n° 392 (scans 8, 10, 21): divisor classes attached to modules of finite type; the relative invariant of two lattices.
- n° 371 (scans 13, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42): tensor products of algebras; the large algebra of a
  monoid; free-monoid operators.

### SA17-14 · the conditions (scans 2-4, 12, 14)

**On the page.** For F: (Sch/S)° → Ens, S locally noetherian, the conditions are:
- **1°** F is an fpqc sheaf: (a) Zariski local; (b) compatible with faithfully flat quasi-compact descent. It is
  enough for B → B̂.
- **2°** F commutes with filtered colimits of rings.
- **3°** F commutes with adic limits of artinian rings.
- **4°** Exactness on finite algebras over artinian local A: F(A) → F(A') ⇉ F(A'') with trivial residue extension
  and long_A A'/A = 1. This is a Schlessinger-type condition.
- **5°** At every point with values in an algebraically closed field, the prorepresenting ring is finite.
- **6°** Separation (valuative criterion).
- **7°** Local modularity: over a complete local noetherian S', if η: Z → F_{S'} is modular at the closed point, it is
  modular (or at least étale) everywhere.
- **8°** Generic modularity: modular at the generic point implies modular on an open neighbourhood.

On scan 4 he notes that the conditions are stable under base change, and that all except 2°, 5° and 6° are absolute
conditions on F.

**The Théorème (scan 14):** F is representable by an X that is locally quasi-finite and separated over S iff 1°-8°
hold.
- **Corollaire 1:** X étale and separated iff 1°-4°, 6°, and F étale on artinian arguments.
- **Corollaire 2:** X unramified and separated, with an extra condition (NR b) on complete local domains of
  dimension 1.

**Checked:**
- The necessity of 1°-8° for F = h_X holds with the standard facts for X locally of finite type over a locally
  noetherian S: fpqc descent, limits, Hom(Spec B̂, X) = lim Hom(B_n, X), quasi-finiteness, and the openness of the
  locus of local isomorphisms.
- His remark (scans 7, 9) that 7° (in its form C_1) is "vide" when F → S is étale: formal étaleness lifts η_o
  uniquely along the nilpotent thickening.

**Open, his own (margin of scan 14):**
- "Donner l'exemple-type (S de dim 1) montrant que (8°) n'est pas surabondant".
- "Est-ce que 7° est surabondant? Non, si on renforce aussi 4° au cas adique noeth." In other words, 7° should follow
  once 4° is strengthened to noetherian adic rings.

Neither is proved on the sheets. See package SA17-RP3.

### SA17-15 · the proof by induction on dim S (scans 4-6) and the formal propositions (scans 23-33)

**The plan (scans 4-6).** The proof runs by induction on dim S:
1. dim S = 0: build X from 4° and 5°, and represent F by 1°a, 2° and 3° ("cor 2 à prop 1" of the attached notes).
2. S complete local of dimension n: F_U is representable by induction, with U = S − s. Build finite X_i from the
   points of F_o, and reduce through Prop. 2 to the X_{iU} → X_U being disjoint open immersions, which comes from 6°
   and 7°.
3. S local: descent from Ŝ.
4. S arbitrary: the Lemma (representable over every S^a = Spec O_{S,a} ⇒ representable) through Prop. 3, "on est
   ramené à vérifier la condition de constructibilité de loc. cit.". **That condition is not verified on the sheets.**

**The formal propositions (scans 23-33).**
- **Proposition 1 (scans 23-25):** if (X, ξ) represents F on local arguments essentially of finite type with finite
  residue extension, and F is Zariski local and commutes with colimits, then (X, ξ) represents F.
  - **Checked.** The proof is right. One step is implicit: the opens U_t (t with finite residue extension) cover T,
    because every point of T generizes a closed point of its fibre.
- **Corollaire 1 (scans 25-29):** the representing property on artinian arguments, together with the injectivity of
  F(B) → F(B̂) and of F(B̂) → lim F(B_n), suffices.
  - **Checked, with a gap filled.** The page proves u'p_1 = u'p_2 on T' ×_T T' = Spec(B̂ ⊗_B B̂) "en vertu de 1°)".
    But 1°) was proved only for local arguments essentially of finite type, and B̂ ⊗_B B̂ is neither local nor
    noetherian.
  - The step holds after one more argument. For T of finite presentation, the equalizer of u and v is a locally
    closed subscheme. It contains the local schemes at all points with finite residue extension, so it is all of T.
    Condition L2 then carries injectivity to every affine argument.
  - With this, fpqc descent of morphisms into the scheme X finishes the proof as on the page.
- **Corollaire 2** (S artinian) and **Proposition 2** (S complete local, gluing X_1 to X' along an open immersion,
  scans 29-33) follow from Cor. 1 as written. His margin asks to "Transformer 4°) sous une forme plus facile à
  vérifier".

### SA17-17 · Proposition 3: local representability plus constructible modularity ⇒ representability (scans 33-41)

**On the page.**
- The hypotheses:
  1. F_a is representable for every a;
  2. for T locally of finite type and η ∈ F(T), the locus M(T, η) of local modularity is constructible;
  3. L1 and L2.
- The definition of "modulaire local" (scan 35), with condition 2°, which says that L is a field of definition of β.
- The uniqueness remark (scan 37).
- The proof (scans 37-41): M(T, η) is open. Affine X^{(x)} are modular at all points. A lemma: if η_z is modular for
  all z ∈ Z, then h_Z ×_F h_Z is represented by Z' ⊂ Z × Z with both projections local isomorphisms. Over S_a, Z'
  is the trivial relation, hence trivial over a neighbourhood U of a. The X^{(x)} are "quasi-modular", and a further
  "formal proposition" glues them.

**Checked:**
- M(T, η) is open: a constructible set stable under generization in a noetherian space is open.
- "Z' trivial over S_a ⇒ trivial over a neighbourhood": the image E of Z' − Δ in S is constructible and contains no
  generization of a. So a is not in the closure of E, which is the set of specializations of E. This needs Z' of
  finite type over S, which is implicit on the page.
- The uniqueness remark of scan 37: the standard universal-object argument.

**Open on the page:**
- the meaning of "quasi-modulaire" ("Préciser la signification de ce terme");
- the gluing proposition, which is not written;
- above all, the verification of hypothesis 2 (constructibility) from 1°-8° in the main theorem. 8° (generic
  modularity) is clearly meant to give it, and his margin says "Transformer en une condition de modularité
  'générique'".

### SA17-16 · non-ramification, the diagonal, the infinitesimally étale locus (scans 7, 9, 12, 15-16, 20)

**On the page:**
- (A) and (B), and their replacement (C)/(D_1): the infinitesimally étale locus of η: Z → F_{S'} is open.
- (C_1), stability under generization, is equivalent to A and automatic when F is étale.
- The case "immersion ouverte": F → S a monomorphism, étale on artinian arguments.
- The reduction of the general case to the unramified one through the diagonal F → F ×_S F (scan 20). The diagonal
  is representable by the unramified case and is a closed immersion by 6°. So X ×_{F_{S'}} X is a closed subscheme
  of X ×_S X that coincides formally with the diagonal, hence equals it, and X → F is a monomorphism and étale, hence
  an open immersion.

**Checked:** the scan-20 argument agrees, once "coincides formally ⇒ equal" is spelled out for W = X ×_{F_{S'}} X:
1. Krull's intersection theorem, applied at each point of the diagonal Δ, makes Δ open in W.
2. Δ is closed, being a section of the finite map p_1.
3. The rest, W − Δ, is finite over the local base S'. Its closed fibre is empty because X_o → F_o is a monomorphism,
   so it is empty.

The page leaves step 3 implicit.

### SA17-18 · applications in view (scan 17)

**On the page:**
- **Unramified functors:**
  - mono-finiteness, and G/H with H open and closed and flat;
  - classes of divisorial correspondences;
  - pointed Hom into a commutative group;
  - Hom of abelian varieties;
  - immersions, the diagonal, and "foncteurs platificateurs";
  - the decomposition of fibres into connected (or irreducible) components, where the functors are even étale.
- **Applications:**
  - "Un schéma abélien sur S loc. noeth. normal est projectif sur S", through the scheme of divisorial correspondences
    on X ×_S X;
  - the existence of the Picard scheme of a proper scheme over a field ("Chevalley-Seshadri-Grothendieck-Murre"),
    and over a dense open of a base.

**Known (to verify):**
- The modern form of the whole programme is Artin's criterion (Artin 1969, 1974) together with "a separated, locally
  quasi-finite algebraic space is a scheme" (Knutson; Stacks Project).
- The universal flattening is representable by a monomorphism of finite presentation (Raynaud-Gruson 1971, and the
  Stacks Project).
- On the projectivity of abelian schemes over normal bases, Raynaud's LNM 119 (1970) gives the exact status: whether
  it holds globally or locally on S, and the counterexamples over non-normal bases. **His statement must be checked
  against it before any use.**
- Picard over a field: Murre (Publ. IHÉS 23, 1964), Oort (1962).

### How cote 131 connects

- It is a complete programme: conditions, a theorem, corollaries for the étale and unramified cases, a proof by
  induction with three formal propositions, and applications.
- Missing on the sheets:
  - the constructibility input;
  - the gluing proposition;
  - the two redundancy questions.
- It stands apart from the BT material of cote 129. It meets the descent notes of cotes 126-128 (Work folders
  K126-K128: faithfully flat and non-flat descent) through 1°b and Prop. 3.

## Cote 133, scans 19-29: finite-set operations, the category of finite sets and injections, and the Cauchy formula
> [19 Nov 2026, sweep 3.5] Bears on line 473: C:local_charzero_counterexample (133 scan 29) (SA17 intake, confirmed; PROPAGATION.tsv n=502). See results_register/horizontal/sweep3_5/SUMMARY.md.

Package MPL_133 has 50 scans; scans 5, 10 and 41 are absent.

**What was read in sweep 3:** scans 19-29 only, in full, on 18 Nov at about 22:50 UTC. The budget ran out before scans
2-18 and 30-54. For those, the sweep-2 map and the Pro notes are the current record:
- the quadratic Witt-group sheets (notes W01-W16, scans 3-9);
- the printed offprints of scans 11-17, which the notes attribute to Laborde (P01), credited to him;
- the remaining sheets after scan 29.

**Correction to sweep 2.** SA17-23 was labelled "formal groups and their decompositions (scans 19-29)". That is wrong.
The pages are the notes' section "Finite-set operations and representation rings" (F01-F12): I misread their "F"
codes. The label should be "finite-set operations, finite sets with injections, and representation rings of the
symmetric groups".

### Scan 19: λ- and σ-operations

**On the page:**
- λ_t, σ_t and the boxed identity σ_t(E)λ_{-t}(E) = 1, with σ² = E² − λ².
- For finite G-sets: σ²(E) = λ²(E) + E and the boxed 2λ²(E) + E = E², with the count 2·d(d−1)/2 + d = d².
- The open question "λ^i(xy) = ?".

**Checked:** at order 2 the two descriptions agree. With λ² = 2-subsets and σ² = 2-multisets, E² − λ² = λ² + E = σ².

### Scans 20-23: the injection powers τ^n and the map powers T^n on the Burnside ring

**On the page:**
- k_*(G) = ⊕ k(G × S_n) with the induction product.
- τ^n(E) = cl_n(Mon(I_n, E)).
- The Prop.: τ*(E ⊔ F) = τ*(E)τ*(F).
- The corollary: τ* is a homomorphism k_0(G) → 1 + k̂_*(G)^+.
- The operations q_H^n.
- T^n(E) = cl_n(Hom(I_n, E)), and the decomposition of Hom(I_n, E) by the quotients of I_n.

**Checked:**
- The Prop. holds, because S_n/(S_i × S_j) = P_i(I_n).
- The number of quotients of type α is n!/∏ α_i!(i!)^{α_i}.
- **His deletion is right.** He crossed out the formula T^n = Σ_i φ_{n,i}(τ^i) with φ_{n,i} = induction from S_i.
  For n = 2 the diagonal part of Hom(I_2, E) is E with trivial S_2-action, but φ_{2,1}(cl_1 E) = E ∧_{S_1} S_2 has
  free action.
- The surviving sum over types α is the right shape. Its terms must be φ_α = Ind_{W_α}^{S_n} ∘ Infl, along
  W_α = ∏ S_i ≀ S_{α_i} → ∏ S_{α_i} ⊂ S_{μ(α)}. They depend on α, not only on (ν(α), μ(α)) as his notation suggests.

### Scans 24-27: functors on finite sets and injections

**On the page:**
- The category ℰ of finite sets with injections, and functors ℰ → Ens_f, which he calls a "para-topos".
- The representables h_I = Mon(I, −), which are connected and are the components of the H_J = Hom(J, −).
- "Foncteurs spéciaux": finite sums of h_I, equivalently direct summands of H_I. They are stable under finite limits
  and composition.
- "Foncteurs distingués": finite sums of Mon(I, −)/H, equivalently E ↦ ⊔_n Mon(I_n, E) ∧_{S_n} X_n.
- "Équivalences": maps bijective for |E| ≥ n. They satisfy 2-out-of-3 and are stable under base change.
- The subcategory of functors with injective transition maps, with ⊔, × and ∘.

**Checked:**
- 2-out-of-3: take the larger of the two thresholds.
- The connectedness of h_I: any two elements of Mon(I, E) are related through the identity of I and morphisms of ℰ.

The rest are definitions. See HUNCHES H10.

### Scans 28-29: tensor powers and the Cauchy formula

**On the page:**
- Over a ringed topos, K(X, *) = ⊕ K(B_{S_n X}), with τ^n(cl E) = cl(E^{⊗n}).
- The formula τ^n(ξ) = Σ_α Σ_α(λ^1ξ, …, λ^nξ) ρ_1^{α_1}⋯ρ_n^{α_n}, where:
  - Σ_α is the monomial symmetric function of type α written in the elementary ones;
  - ρ_i is the class of the trivial representation of S_i, placed in degree i.
- The margin: "Relation avec le th. de commutation à la H. Weyl".
- The corollary: λ^n(ξ) is the coefficient of ρ_1^n, and the Adams operation ("S^n") is the coefficient of ρ_n.
- The question: for which k is ⊕ R_k(S_n) the polynomial ring on the ρ_i? "Est-ce vrai si k est un anneau local?"

**Checked:**
- **Over a field of characteristic 0** the formula is the Cauchy identity Σ_λ s_λ(x)s_λ(y) = Σ_ν m_ν(x)h_ν(y),
  read through the Frobenius characteristic (ρ^α ↦ h_α) and the splitting principle. It is Schur-Weyl duality, as his
  margin says.
- The corollary follows: m_{(1^n)} = e_n and m_{(n)} = p_n.
- **His question, answered in the negative for local rings:**
  - k = F_2: ρ_1² = [F_2[S_2]] = 2ρ_2.
  - k = F_p: R_{F_p}(S_p) has rank p(p) − 1 (the p-regular classes), fewer than the p(p) monomials ρ^α of degree p.
  - The F_2 example is the Pro notes' F11, credited; I re-derived it and added the F_p rank count.
  - The characteristic-0 case is the notes' F12 (Λ = Z[h_1, h_2, …]).
- **Open:** the exact class of rings k for which the answer is yes. Characteristic 0 is necessary for the argument
  above. Whether Z_p-lattices give the polynomial ring is not settled here.

## Cote 133, scans 2-18 and 30-54 (wave 2)

**Who:** the reader a598c2dff473d448c (Claude Opus 5.5 at effort max), launched by a34c04448e8299803 on 19 Nov 2026.
It read the transcription, the Pro notes and the doubts in full, and used Michel Hua's reading as a credited witness.
Its full reading is `readings/133_002-018_030-054.md`: 59 check events, 33 corrections, 9 readings decided on the
image. Integrated here on 19 Nov.

**Placed only:**
- Laborde's printed offprints (scans 11-17), credited to him;
- the computer listing of scan 18, with his one formula;
- the thesis notices (48, 50).

Scans 5, 10 and 41 are blank leaves (per Michel Hua's project).

### SA17-21 · Witt groups of quadratic forms (scans 2-9)

**His question on scan 4, "c₁ ?", settled: yes.** w₂(H(L)) = c₁(L) mod 2 in étale cohomology, and more generally
w(H(E)) = Σ (1+α)^{r−k} c̄_k(E). This explains why "w∘α = 1" is struck on scan 9. The result is new in this reading.

**Wrong:**
- **Scan 6.** "WG(S) is a pre-λ-ring augmented to H⁰(S, Z)" fails where 2 is not invertible: λ² of the hyperbolic
  plane has rank 1, which his own even-rank statement forbids. New in this reading.
- **Scan 6.** The ink stops P_i at λ^{i−1}; the universal formula needs λ^i. Michel Hua's project corrects the same.

**Decided on the image at 600 dpi (scan 8):** the name in "dixit" is **Lazard**, not Laborde. The Pro transcription
and Michel Hua's project both read Laborde.

**Open:** the λ-ring question for his split WG(S). See H-133-1 and package SA17-RP5.

### SA17-26 · the game of go (scans 30-34)

- His scoring identity D = 2(P + T) − ν² − ε. The slip "ν² − D'" is decided on the image, and the signs before ε are
  minus.
- His last-move rule holds if each side fills only its own territory.
- His question gets a no: the last-move term ε depends on play, through sacrifices.
- **Open:** the rule under his literal no-pass rules.

### SA17-25 · formal groups, algebraic groups, crossed modules (scans 35-54)

**Scan 36:**
- The heading is "Solution", not "Structure".
- The labels L₀ and D₀ are swapped. This is Michel Hua's correction; both are written over in the ink.
- **The splitting statement (I) is false** without "up to isogeny" in the formal category. The universal vector
  extension of a supersingular formal group is a counterexample. Up to isogeny it holds.
- **Open:** statement (II) and the other formal-group claims.

**Scans 42-44:**
- Pic must be Pic⁰, and φ₀ must start from the dual of t (both Michel Hua's corrections).
- "Γ libre" is too strict: torsion is allowed, and the restriction is in his ink.
- The note "iff 𝔷_u finite" fails over F̄_p (Michel Hua's project).
- The equal-characteristic constructibility claim fails for the multiplicative part (the Pro notes G13).

**Scans 46-54, the "Fourbis" pp. 1-7: one group G for two crossed modules.**
- The centre and derived-group tests, the twist formulas and his "Vérifier" are all re-derived for ordinary groups,
  with the sign fixed.
- The cancelled "N' = Cent(H)" should read N' = H ∩ Z(G).
- **Open:** which central extensions E satisfy both tests.
- See H-133-2 (P. Hall's isoclinism) and package SA17-RP6.

## Cotes 126, 127, 128, 130, 132: the Work folders (wave 2)

**Who:** the reader ac8bd2a26d00b4f37 (Claude Opus 5.5 at effort max), launched by a34c04448e8299803 on 19 Nov 2026.
It read every handwritten page and the notes files in full; it used the doubts registers and Michel Hua's readings by
search. Its full reading is `readings/K126-K132.md`: 50 check events and 22 corrections.

**Placed only:**
- Ladegaillerie's two CRAS Notes (cote 132, scans 26-32), credited to him;
- the Bourbaki typescripts n°383 and n°357 (cote 130);
- an EGA IV typescript leaf (cote 127, scan 9).

### SA17-28 · cote 126: faithfully flat descent and miscellany

**Wrong:**
- **Scans 4-8.** The equivalence-relation proposition silently needs R → X flat; the page itself later says "Comme
  R → X est plat".
- **Scan 20.** "Y irréductible ⇒ composantes irréductibles disjointes" is false: the étale double cover of the nodal
  cubic is a counterexample. The lemma it serves is still true, by another proof.
- **Scan 28.** The late fifth triple "(t''', t_1, t_2) ∈ V" is in the ink and makes the claimed surjectivity false. It
  must be deleted.
- **Scan 29.** Primes are slipped (t''' for t''). Michel Hua's project notes the same.

**Closed:** Remarque 2, the vanishing he marked "?", is true for quasi-compact quasi-separated maps.

**Open:** effectivity in the quasi-projective case (scan 35).

**The link to cote 131:**
- Prop. 2 (ii) is the form of condition 1° of cote 131.
- Scans 32-35 pose the question that step 3 of cote 131 needs: descent along Spec Ô → Spec O. See package SA17-RP7.

### SA17-29 · cote 127: non-flat descent

- Théorème 1.4 rests on Lemma 1.3, which has no proof. It is open.
- Th. 1.8 ("lemme de Hironaka") is read through the valuative criterion.
- **Open:** the factorisation of epimorphisms into effective ones.
- Scans 22-24 (unramified functors, descent along all epimorphisms) supply the type of argument that cote 131's
  applications use.

### SA17-30 · cote 128: non-flat descent through the conductor

- **Closed:** the k[ε] case, "J nilpotent", and "V est de dim 1".
- **Lemma 1** (G_m against G_a) has a gap: the multiplicative and additive connecting maps differ by a factor c⁻¹. It
  is fine in odd characteristic; characteristic 2 is open. See package SA17-RP8.
- **Open:** the limit lemma of the Théorème.

### SA17-31 · cote 130: heights and local symbols

**Decided on the image (scan 14):** the ink reads ρ(X̃) − 2, not −1. And z is the number of base points, not of
"sections singulières".

**Closed:**
- Bounded M_K-sets have bounded height.
- "Admettons ce point", the sheaf property.

**Scan 15:** the formula holds; it is Shioda's height formula. Read with the local correction terms in (1/m)Z of
scans 4-6, cote 130 contains the structure of the Mordell-Weil lattice formula, with the component-group pairing of
SGA 7 IX. See H-K-5 and package SA17-RP9.

### SA17-32 · cote 132: embeddings in surfaces, Teichmüller groups with holes, extensions of topological groups

- **Closed:** the H³ obstruction ("sauf erreur") is Taylor's theorem of 1954.
- **Open:** case B', which he marks "faux"; H-K-7 proposes a repair through the 2-type of BH.
- Ribbon graphs, the groups T_{g,n} with holes, boundary twists and Ladegaillerie's classification of embeddings are
  the germ of the Teichmüller tower of the Esquisse (H-K-6).

### Readiness

The reader judges every handwritten scan range of K126-K132 ready to edit and translate, with its corrections as notes.
The offprints and typescripts are placed only. For cote 133, no range is edition-ready before an image pass over the
remaining marks. DELIVERABLES.tsv has the details.
