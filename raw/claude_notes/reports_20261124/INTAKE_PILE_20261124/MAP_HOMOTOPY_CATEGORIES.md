# Connection map: HOMOTOPY_CATEGORIES (derivators, localizers, topoi, stratified and integral homotopy)

- **Author.** Claude Opus 5.5 at effort max, agent a34c04448e8299803 (the Dérivateurs expert; it also took in SA08,
  SA08_C3_D031 and SA09 in full on 21-22 Nov). Brief: `MAP_BRIEF.md`, from the main session 329fb1e6 (Claude Opus 5.5 at
  effort max), 25 Nov 2026.
- **The runs.** Every run named below is GPT-6 Astra (ChatGPT Pro mode).
- **Region.** The DERIVATEURS cluster (FREX, DER_LOCALIZERS, RESIDUE, S2COUNT, REVLOC, BISITE); the topos and
  étale-homotopy items of LONGUE_MARCHE_A (LM5) and LONGUE_MARCHE_B (EXIT_TOWER, reconstruction from étale topoi); the
  categorical items of SWEEP3_A/B (SA08 and SA08_C3_D031, SA09, SA10, SA21, SA22_run2); outside results in homotopy
  theory, topoi and categories.
- **Files.**
  - `MAP_HOMOTOPY_CATEGORIES.tsv`: one row per link.
  - `MAP_HOMOTOPY_CATEGORIES_CHECK_EVENTS.tsv`: my checks.
  - Notes: `agent_notes/a34c04448e8299803_NOTES.md`.
- **Opened at the statement.**
  - The three Hexagon abstracts below: 2611.00879, 2611.00648, 2611.00444.
  - FREX A.1 with its proof.
  - The LM5 and BISITE register rows quoted.
  - The SA22_run2 check events of B:local-Hurewicz.
  - From my intakes: the SA08_C3_D031 rows (A-003, A-006, A-S09-24 to -30).
- **Not opened** (cited from memory, marked "to open"): Caramello 2014, Quillen 1973, Whitehead/Hatcher, McDuff 1979,
  Dwyer 1979, Guès arXiv 2611.31031.

## 1. New knowledge, ranked by usefulness

### K1. The C.3 problem is a problem about one homotopy type: π₀ and π₁ of the nerve of the admissible category

**Statement.** Write 𝒜 for the category of admissible strict PD theories over Z (SA08 Part C; SA08_C3_D031). Let
𝒜^[d], 𝒞, 𝒞^[d], ℰ^[d] and their countable versions 𝒟_ω be the full subcategories of A-006, A-S09-24, A-S09-27 and
A-S09-29.

1. The inclusions 𝒜^[d] → 𝒜 and 𝒞 → 𝒜 induce homotopy equivalences of nerves.
2. For 𝒟 = 𝒞^[d] or ℰ^[d], the inclusion 𝒟_ω → 𝒟 induces a homotopy equivalence of nerves.
3. Since 𝒜[𝒜⁻¹] is the fundamental groupoid Π₁(N𝒜) (Quillen 1973, Gabriel-Zisman), the two open questions of C.3 read
   as follows:
   - A-TL ("the all-arrow localization is trivial") says exactly that N𝒜 is connected and simply connected.
   - A-CS ("common sources for all pairs") says exactly that π₀(N𝒜) = ∗. A-003 identifies common sources with
     connectivity by finite zigzags.
4. Corollaries:
   - The run's nonfaithfulness theorem A-S09-28 says π₁(Nℰ^[d]) maps onto a non-trivial group (the prime-germ character
     χ), so ℰ^[d] → 𝒜 is *not* a homotopy equivalence.
   - A cofiltered replacement category would make N𝒜 contractible, which answers both questions at once.

**Proof** (Claude Opus 5.5 at effort max, here; it uses only constructions of the run that I checked on 21-22 Nov).

- **The case 𝒞 → 𝒜.** A-006 gives a functor R with natural transformations jR ⇒ Id and Rj ⇒ Id; natural
  transformations are homotopies of nerves.
- **The case 𝒜^[d] → 𝒜.** Apply Quillen's Theorem A to i: 𝒜^[d] → 𝒜. Fix A ∈ 𝒜 and choose N ≥ max{1, λ_A(d)}, so that
  T_N A ∈ 𝒜^[d] (A-S09-24, (S09.120) with (S09.116)). The tail functor T_N preserves 𝒜^[d] for every N (stated in
  A-S09-24's proof). On the comma category i/A, define
  - F_N(D, f) = (T_N D, f∘t_{N,D});
  - the maps t_{N,D}: F_N(D, f) → (D, f);
  - the maps T_N f: F_N(D, f) → (T_N A, t_{N,A}). These are morphisms over A, because t_{N,A}∘T_N f = f∘t_{N,D} by
    naturality.

  This gives natural transformations Id ⇐ F_N ⇒ const. Hence N(i/A) is contractible, and Theorem A applies.
- **The countable case.** Fix A ∈ 𝒟. Given a finite diagram (D_j → A) in i/A with D_j countable, apply the run's
  finite-diagram closure (S09.156) to the single object A, with the countable set of all images. This gives a countable
  A′ ↪ A in 𝒟_ω through which every D_j → A factors. The factorizations form a cocone because A′ → A is injective. So
  i/A is filtered, its nerve is contractible, and Theorem A applies.
- **Point 3.** By Quillen, C[C⁻¹] ≃ Π₁(NC).

The constructions for 𝒞^[d] → 𝒜 (U_N = R T_N) and for the three-disk gate ℱ₃ (A-S09-30) need cutoffs that depend on the
object, so for them only the run's π_{≤1} statements are available.

**Why it matters.**
- It moves C.3 from "localizations" to homotopy theory of categories. That is Grothendieck's Theorem A, Loc (3), the
  very axiom the DERIVATEURS cluster audits in the footnote-56 chain.
- The run's reductions now preserve the whole homotopy type, not only π_{≤1}.
- It names the natural strongest target: "B𝒜 is contractible". A sufficient criterion is cofilteredness (common sources
  for pairs, as asked by A-CS, plus equalization of parallel pairs, the "homotopy-equalizer repairs" of SA08 C32).

**Status.** Proved here, short. No second reader yet.

### K2. Pushouts of ordinary topoi compute shapes exactly when the homotopy pushout is aspherical

**Statement.** Let H → G and H → K be homomorphisms of discrete groups, and P = BG ∪ʰ_{BH} BK the homotopy pushout.

1. The bicategorical pushout of the ordinary topoi Set^G ← Set^H → Set^K is Set^{G∗_H K}, and its shape is
   K(G ∗_H K, 1) = τ_{≤1}P.
2. The pushout of the corresponding ∞-topoi Fun(B−, S) is Fun(P, S), with shape P (SA10 B2.1, van Kampen for ∞-topoi).
3. Hence "shape commutes with this pushout of ordinary topoi" holds if and only if P is aspherical:
   - it holds when H → G and H → K are injective (Whitehead's asphericity of graphs of groups);
   - it fails for G = K = 1, H = C₂, where P = ΣBC₂ has π₂ = Z/2.
4. **Hole filling (LM5 C.2).** Capping a boundary circle of a compact surface Σ (the boundary map Z → 1 is surjective)
   gives P = the capped surface. The ordinary-topos pushout therefore has the right shape unless the capped surface is
   S² (genus zero, every hole capped), where the defect is π₂(S²) = Z.

**Proof** (here).
- **Point 1.** Sheaves on the 2-colimit form the 2-limit of the inverse-image functors: the pseudo-pullback
  Set^G ×_{Set^H} Set^K. Its objects are sets with G- and K-actions agreeing on H, that is, G ∗_H K-sets. The shape of
  Set^Γ is K(Γ, 1), and π₁(P) = G ∗_H K by van Kampen.
- **Point 2.** Fun(−, S) takes colimits of spaces to limits of ∞-topoi (descent).
- **Points 3 and 4.** The comparison P → τ_{≤1}P is an equivalence exactly when π_{≥2}P = 0. For K = 1, P is the
  mapping cone. For a capped surface Σ ∪ D², asphericity holds exactly when the result is not S² (orientable case).

**What it unifies.**
- SA10 B2.2 ("the shape of a bicategorical colimit of ordinary topoi is not the homotopy colimit of shapes:
  Set ← C₂-Set → Set") and the second clause of LM5 C.3 ("ordinary topoi also discard higher homotopy pushout data") are
  the same example, found by two runs independently. K2 says exactly when the defect occurs and what it is: π_{≥2} of P.
- LM5 C.2/C.5 (the hole-filling pseudopushout, "the exact genus and boundary table") is where the defect is visible: it
  vanishes in genus ≥ 1 and appears only when the filled surface is S².
- The profinite case, which LM5 actually needs for étale fundamental groups, is the open next step. LM5 C.3's first
  clause (profinite groupoid pushouts need not be topos pushouts) shows it differs. The analogue of "injective" there is
  goodness plus injectivity of the profinite edge maps.

**Status.** Proved here (discrete case). The profinite version is open.

### K3. FREX's exactness is a property of a topos, by Caramello's Fraïssé bridge

**Statement.** In FREX setting (S), with M the strong Fraïssé limit and G = Aut(M), FREX A.1 (`A:coinvariants`) proves
colim_A V ≅ (S_R V)_G. So exactness over R is exactness of smooth coinvariants.

In topos language:
- G-coinvariants are the R-linear left adjoint π_! of the locally connected topos Cont(G) of continuous G-sets.
- By Caramello (Logica Universalis 8, 2014, "Fraïssé's construction from a topos-theoretic perspective"; to open),
  Cont(G) ≃ Sh(A^op, J_at) classifies the theory of homogeneous models of the age.
- Hence exactness over R is a Morita invariant of that classifying topos. Any two theories with equivalent classifying
  topoi share it, for example bi-interpretable ω-categorical structures (Ahlbrandt-Ziegler: bi-interpretability is
  isomorphism of the topological automorphism groups).

FREX A.24-A.26 (totality is a G-invariant) should have the same topos form (total asphericity of the presheaf category
against the atomic site). I have not checked this.

**What it gives.**
- A conceptual proof of A.1's "depends only on G".
- A dictionary for FREX's open A.3(iii) (amenable G, (S), (Rig), (FA), (FA∅), (Op) ⇒ exact over Q?). It is a statement
  about π_! on Q-modules of an atomic topos whose "topological dynamics" (universal minimal flow) is
  non-metrizable. That is where Sun's coherent-model paper (below) and topos-theoretic dynamics meet.

**Status.**
- A.1's proof: read here (targeted check).
- The topos reformulation: immediate from A.1 and Caramello's theorem. Caramello's paper was not opened.

### K4. Grothendieck's local Hurewicz conjecture: the counterexample is the universal-coefficient shift

**The counterexample** (SA22_run2 B:local-Hurewicz, SGA 2 XIII 6, Conjecture A as the run reads it). The cone with link
L = ΣRP² = M(Z/2, 2) has:
- H^i_Y(Z) = H̃^{i−1}(L; Z), which is zero for i ≤ 3 because H²(L; Z) = 0 and H³(L; Z) = Ext(Z/2, Z) = Z/2 (the latter
  sits in H⁴_Y);
- π₃^Y = π₂(L) = Z/2.

My recomputation agrees. The run already has the exact finite-conical correction (the next integral cohomology must be
torsion-free).

**The second repair, from the localizer side.**
- With Z/2 coefficients, H³_Y(Z/2) = H̃²(L; Z/2) = Z/2 ≠ 0. So a form of Conjecture A with all finite coefficients
  Z/n, or with homology, is not touched by this example.
- The torsion that integral cohomology shifts up one degree is exactly the "Tor H₂" test that REVLOC F.1's class W†
  adds to the Π₁ and rational tests.
- At the localizer level, the class of maps inducing isomorphisms on H*(−; Z) agrees with W_{HZ} only up to this shift.
  For finite-type nilpotent spaces the two agree, by the dual universal coefficient theorem.

**Status.** Computation here. The reading of SGA 2 is the run's, opened by it.

### K5. A ladder of integral algebraic models of homotopy types, and where our results sit on it

The rungs, from weakest to strongest:
1. Cochains with cup product and divided powers. They do not determine finite nilpotent types: SA09 A3.4, with L(5,1)
   and L(5,2) (re-proved twice). The missing invariant is the linking form, a Bockstein-type secondary operation.
2. The full natural Γ-action. It reconstructs the type: SA09 A3.2 (Horel).
3. E_∞ cochains (Mandell; SA08 A-018, D006M) and derived binomial rings: KSZ Prop. 3.6, quoted in SA08_C3_D031 A-S09-15.
   These capture the linking form.
4. In factorial-local ranges, strict PD de Rham theories (SA08 C17, C21; the Z[1/(p−1)!] of AT12). This is the cochain
   counterpart of Dwyer's tame homotopy theory. Guès, arXiv 2611.31031 (23 Nov), "tame homotopy and the Goodwillie
   tower" (not opened), is the outside work to read with C.3.
5. A-026 (no filtered numerical lift) and C3_D031's A-S09-09 to -12 (unbounded support of the PD cotangent complex of
   Γ(T)/I_N, via Fu-Nuiten) are obstructions to climbing from rung 1 to rung 3 by filtrations or bounded resolutions.

**Status.** A synthesis of checked items (my intakes of SA08 and SA09). Its new content is the placement of A3.4 below
the linking form and of C.3 against tame homotopy.

### K6. The stratified homotopy type of M̄_{0,n}: three runs describe one object

The three descriptions:
- **BISITE F.15** (Known): the genus-zero category 𝒞_n of multicurves with mapping-class morphisms modulo the twist
  groups Δ_σ.
- **BISITE F.16 and F.17.** Forgetting a mark is W_∞-proper. F_* is the topological direct image on constructible
  sheaves of M̄_{0,n+1} → M̄_{0,n}. At n = 4 the map is not W_∞-smooth, with lifting category BZ.
- **EXIT_TOWER and SA10.**
  - EXIT_TOWER: the exit-path categories of M̄_{g,n} (cotes 147, 150).
  - EXIT_TOWER A.2 and SA10 A4.5, found independently: conditional infima exist exactly for g = 0 with n ≥ 3, for
    g = 1 with 1 ≤ n ≤ 3, and for (g, n) = (2, 0).
  - RESIDUE H.3-H.6 gives second proofs of the BISITE rows.

**Mechanism.**
- 𝒞_n is the exit category of the normal-crossings stratification of M̄_{0,n} (Lurie HA A.9). F_* = topological
  direct image is BISITE D.11 (proper maps via lifting posets) applied to it.
- The BZ of F.16 is the local monodromy (Dehn twist, Picard-Lefschetz) where the forgotten mark enters a node:
  xy = t.

**New statement (argued, not proved).** F is non-smooth for every n ≥ 4. Near the boundary divisor D_{12} the forgetful
map is locally the n = 4 model times an identity. The step that remains is locality of BISITE's lifting categories
under such a product decomposition.

**Why it matters.** It is the bridge from Grothendieck's six operations on Cat (BISITE F.10-F.17; RESIDUE I) to the
Teichmüller tower of the Longue Marche (EXIT_TOWER; cotes 147, 148, 150). The conditional-infimum list says in which
(g, n) the finite-poset tools (BISITE D.11) apply directly.

### K7. Finite categories, finite posets and classifying topoi: what realizes which homotopy types

The four realizations:
1. **Finite posets.** By McCord (SA21 C12, known) they realize exactly the finite simplicial types: finite-dimensional,
   finitely many cells.
2. **Finite categories.** The six-arrow monoid of S2COUNT A.M1 already leaves that class: BM₁ ≃ ⋁_{n≥2} Sⁿ, with
   H_n ≠ 0 for all n ≥ 2. Six arrows is minimal (B:smallcategories). The presheaf topos on M₁ is therefore a topos
   "finite in every sense" whose shape is not of finite type in dimension.
3. **Countable categories.** By McDuff 1979 (to open), countable monoids realize every countable connected type.
4. **Open subtoposes of classifying topoi of universes.** By Hora (Hexagon 2611.00879, 23 Nov; opened at the abstract),
   their shapes realize every countable homotopy type.

**The open question these frame.** Which homotopy types are shapes of presheaf topoi on finite categories? S2COUNT's
CD:alltargets is the countability side of it. As far as I know no characterization exists.

## 2. Outside results that change our items

1. **Hora, "The shape of mathematical universes", Hexagon 2611.00879 (23 Nov).**
   - Content: classifying toposes of universes; their open parts realize every countable homotopy type; the "space of all
     toposes" is contractible.
   - Model and effort: GPT-6.2 Astra, GPT-6 Astra Pro and Claude Opus 5.5 at effort not stated by the post; the human
     author has not checked the proofs.
   - It gives LM5 A.2's Boolean point-free topos Sh(RO(ℝ)) its natural home. RO(ℝ) is the Cohen-forcing algebra, and
     Sh(RO(ℝ)) is the forcing topos: no points because the generic real does not exist.
   - It is the first outside work on shapes of such topoi, and it bears on K7.
   - Use: a conference input for LM5 §§1-4 and SA10 B2. No item of ours is refuted.
2. **Sun, "Finite model spaces and coherent sheaf models", Hexagon 2611.00648 (19 Nov; human-written).**
   - Content: coherent sheaf models over Stone spaces. Constant on a finite clopen partition ⇔ finitely many
     T-structures on each finite carrier. It also computes Yoneda Ext of finite locally constant abelian sheaves (Ext¹ as
     sections, higher Ext zero).
   - It is the coherent-topos counterpart of FREX's (Fin)-type hypotheses and of its exactness-over-R question (K3).
   - The Ext vanishing is a "profinite base" analogue of exactness over a ring.
3. **Pongrácz, "Self-embedding monoids and the existential Thomas conjecture", Hexagon 2611.00444 (15 Nov; GPT-6 Astra
   named, effort not stated).**
   - Content: an ordered expansion of an equivalence-relation structure, a Ramsey class, with infinitely many
     self-embedding monoids among first-order-interdefinable reducts.
   - It is the same class as FREX A.13 (ordered equivalence relations; FE-1's odd-characteristic exactness false).
   - By A.1 (K3), FREX's invariants are constant along interdefinable reducts (same G). Pongrácz's chain shows that the
     embedding-monoid data they forget is infinite there.
   - Use: a FREX successor question is whether the categories of finite substructures with reduct embeddings stay in
     setting (S).
4. **Guès, arXiv 2611.31031 (23 Nov), tame homotopy and the Goodwillie tower; not opened.** It bears on K5, rung 4, and on
   the factorial-local ranges of SA08 C17, C21 and C3_D031 (c_R = 2p−1).
5. **Enomoto, Hexagon 2611.00805** (an extriangulated category with no triangulated embedding) and Nishimura, arXiv
   2611.29239 (an undefined fourfold Toda bracket). They are context for enhancements (Grothendieck's motive for
   derivators) and change no item. **BMRSSWZ, arXiv 2611.27879** (chromatic splitting in coheight 1) touches REVLOC's
   chromatic and sphere-null material only formally.
6. **No math.AT post** appeared on Hexagon in the window (14-24 Nov; my scan of the appendix of
   `LITERATURE_20261124.md`).

## 3. The links, by theme

**A. Localizers and the homotopy theory of categories (the DERIVATEURS core).**
- The footnote-56 chain is one note: BISITE A.32 → RESIDUE B.2-B.4 → REVLOC F.1 → DER_LOCALIZERS A5.3, with the
  positive side REVLOC F.1.1 = DER_FOLLOWUP G.9.
- Quillen's Theorem A (Loc 3) is the tool K1 applies to SA08 Part C. This is the first use of the cluster's axiomatics on
  another cluster's problem.
- DER_LOCALIZERS A2.4, A2.9 (Der 6 forces homology localizers) and K4: cohomological and homological tests differ by the
  universal-coefficient shift, which W† measures.
- FREX exactness (colim exact over R) is homology of categories with coefficients. A_2(Q) (BA ≃ K(Q,2), exact over F_p,
  not over Q) is the rational-versus-mod-p localizer split seen in DER_LOCALIZERS A34.5 (every reversible localizer is
  the join of its rational and p-primary parts).

**B. Topoi: colimits, shapes, points.**
- K2 links SA10 B2.1/B2.2, LM5 C.1-C.5, and Hora.
- LM5 A.2/A.3: in a topos all of whose objects are locally constant, "groupoid presheaf", "locally connected" and
  "enough points" are equivalent. Sh(RO(ℝ)) shows that "Galois" without points is not presheaf.
- LM5 F.12/F.36: punctured-neighbourhood topoi and the shape BẐ(1). These link to Artin-Mazur étale homotopy and to
  EXIT_TOWER's link categories.
- Pinned étale reconstruction:
  - LM5 F.47/F.50/F.49;
  - LONGUE_MARCHE_B item 7: ANABELIAN_149_PUSH F.37-F.49, ANABELIAN_SUCCESSOR F.3-F.50, ANABELIAN_A1_SUCCESSOR
    B.43-B.147.

  These rest on étale topoi as homotopy-theoretic objects, in the frame of Carlson-Haine-Wolf 2024, Thm 4.18 (cited by
  the LM5 intake). The topos-level statement "Hom_k(X^awn, Y) = π₀Hom^pin(X_ét, Y_ét)" is a homotopy-type
  reconstruction, the étale analogue of K1's "the problem is a homotopy type".

**C. Stratified spaces and the Teichmüller tower.** K6: EXIT_TOWER A.2 = SA10 A4.5; BISITE F.15-F.17; RESIDUE H.3-H.6;
SA10 A1.2 (gluing of tubes, the pro-bicolimit of cSh) and C5.08.

**D. Finite models.**
- K7: S2COUNT; SA21 C08, C09, C12; RESIDUE A.5 census (the rectangular band, BM ≃ S²); Hora; McDuff.
- SA10 B6.1: the 151/017 relations do not present the category of nonempty finite sets. This is a combinatorial fact
  about the category Δ_inj-like "finite sets" that the DERIVATEURS runs use as test categories (RESIDUE F.1-F.4, full
  subcategories of Δ_inj). A presentation by generators and relations is what a test-category argument needs.

**E. Fraïssé categories.** K3: FREX A.1, A.23, A.24-A.26, A.13; Caramello; Sun; Pongrácz; Kechris-Pestov-Todorcevic.

**F. Integral models.** K5: SA08 (A-018, A-026, C17, C21); SA09 A3.2, A3.4; SA08_C3_D031 (A-S09-09 to -15, AT12);
KSZ; Mandell; Horel; Fu-Nuiten; Dwyer/Guès.

## 4. Conference topics and paper candidates across clusters

1. **"Common sources and the nerve of a category of theories"** (K1 with the DERIVATEURS axiomatics).
   - Shows that C.3 is the contractibility question for B𝒜, with the run's gates (ℱ₃, countable objects) as homotopy
     equivalences.
   - A paper candidate if A-CS or A-TL is decided. Otherwise a short section of the SA08 write-up.
2. **"Shapes of pushouts of topoi and hole filling"** (K2).
   - A short self-contained note: the discrete proposition, the capped-surface corollary, and the profinite question with
     LM5 C.3.
   - Hexagon-sized once the profinite case is settled or stated as a question. Check first that the discrete statement
     is not in Moerdijk, or in Lurie HTT 7.1.6.
3. **"Constructible sheaves on M̄_{g,n} through exit categories"** (K6). It joins the Dérivateurs companion (BISITE F,
   RESIDUE H, I) and the Longue Marche towers (EXIT_TOWER; cotes 147, 148, 150). The n ≥ 4 non-smoothness is a first
   target.
4. **"Exactness of colimits as a topos invariant"** (K3). This is FREX's separation note (already a Hexagon candidate)
   with the topos dictionary and Sun's Ext computation. Check Caramello before writing.
5. **"Integral cochain models in tame ranges"** (K5). It joins SA08 C.3 and Dwyer/Guès, and needs Guès opened.
6. **"Finite categories and the S² question"** (K7). S2COUNT's Hexagon candidate, with McCord, McDuff and Hora as context.

## 5. What I did not do

- I did not open Caramello 2014, McDuff 1979, Quillen 1973, Dwyer 1979 or Guès 2611.31031 (context budget). Each place
  they are used says so.
- I did not reread the DERIVATEURS runs' proofs beyond what the cluster file and my own intakes record.
- LONGUE_MARCHE_A/B anabelian items outside topoi (GT̂, sections) are left to the anabelian map.
