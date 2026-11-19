# Cotes 71 and 75 (topic SA01, "Géométrie et topologie combinatoire", part 1): the reading

- **Who:** Claude Opus 5.5 at effort max, reader R3 of the deep-sweep agent a6d42bf6fe2b0d8a8 (Claude Opus 5.5 at effort max), horizontal sweep 3, topic SA01.
- **Date:** 19 Nov 2026.
- **What was read, and how:**
  - The Codex-web transcriptions `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/J71-01..06` and `J75-01..04` (`out/*_transcription.tex`), every transcribed scan, through the cleaner used for cotes 69-74 (deletions dropped, `\unsure{a|b}` as a[?b]); the folder notes (`*_notes.md`) of J71; the doubts files only for counts.
  - Scans: `grothendieck_archive_montpellier/11_geometrie_et_topologie_combinatoire/71.pdf` and `75.pdf`, scan N = PDF page N. Viewed:
    - cote 71: 71/12, 30, 32 and 36 at 70-80 dpi; the title and byline of 71/21 at 130 dpi; on 71/36 the line of Lemma XI at 250 dpi and the lower half with its margins at 200 dpi; the signature of 71/48 at 300 dpi; the foot of 71/35 at 200 dpi; the cover 71/1 at 110-150 dpi; 71/2, 5, 16, 18 and 20 at 22 dpi;
    - cote 75: the transitivity line of 75/9 at 300 dpi; the cover 75/1 at 110 dpi; 75/29 at 22 dpi.
  - Computations: `chk71.py` (good vertices of random simple polygons) and `chk75.py` (the small exceptional isomorphisms) in the reader's scratchpad.
  - Not used: Michel Hua's project, the Work math notes.
- **Coverage:** see "What was not reached" at the end.

Ids: check events SA01-R71-nn and SA01-R75-nn, corrections SA01-K71-nn and SA01-K75-nn.

---

## Cote 71: the Jordan theorem and three good vertices for plane polygons (SA01-40, SA01-43)

Scans 1-48: 41 transcribed in six Codex-web folders (J71-01 to J71-06). 71/1 is the archive's cover sheet (viewed at 110-150 dpi): "Théorème de Jordan*: notes manuscrites (1976, s.d.). Cote n° 71, 47 pages". Its footnotes read "*Comprend un manuscrit de Carlos Contou-Carrère" and "†Versos: lettres (1977-1978)". 71/2, 5, 16, 18 and 20 are blank. 71/35 holds one line, upside down, in hand A (described below): "Montrons que ]s, s'[ ⊂ ext Γ", a discarded start of a sentence that 71/33 carries.

The cote holds two kinds of writing:
- a manuscript with the byline "Carlos C. Contou-Carrère" (71/21), folios I-XIX on scans 21-48, dated at the end "le 15 juillet 1976, Montpellier";
- notes in another hand on 71/3-19 and on unnumbered sheets among the folios (71/30 and 71/32 viewed).

### The hands: what the ink shows

**Hand A.** An upright, rounded script in black ink. It writes the title and the byline of 71/21 and the whole text of the numbered folios I-XIX. It also writes the date line of 71/48 and the paraph or signature under it.
- The signature is a cursive flourish ending in a long descender and a point (300 dpi).
- Its letters do not read "Contou-Carrère". The transcription's "Mauré" (with the alternatives Mouré, Maury, Maurice) is a guess at a flourish.
- The author is the one named by the byline of 71/21 and by the archive's cover note on 71/1.
- Some interlinear corrections are in hand A: "adjacents" written over a struck "consécutifs" on 71/36; "]s',s''[ ⊂" inserted on 71/36; "int" written over "ext" in the first case of Lemma XI.

**Hand B.** A fast, slanted cursive, full of abbreviations. On 71/12 it is in blue ink (viewed); on the versos 71/30 and 71/32 it is in black, with polygon drawings on 71/30.

**The margins of the manuscript.** They are in a slanted cursive unlike hand A, in two media.
- **Black ink**, on 71/36: "lemme X", "ambigu", "faux" with a cross, "!", and a circled "non vide ?".
- **Grey pencil:**
  - on 71/21: the circle round "de ℝ²" in the title, and "plan" added after it;
  - on 71/36: "faux pour n = 3!"; "OPS Γ non convexe (sinon c'est clair grâce à --)"; "il faut prendre s comme dans la dém. du lemme VIII (pas son énoncé !)"; "dire avant ! (et tu auras lemme VIII)";
  - not viewed by us: the J71 folder notes call pencil the objection "ce n'est pas une env. conv. !" (71/37), the groups "a = s", "b = s'" (71/38), a struck word on 71/47 and the comment "faux, si on ne choisit pas bien ses notations" (71/48). They do not state the medium of "compliqué, prendre le sommet ..." (71/37), "so what" (71/47) or "douteux" (71/48).
- **Comparison with hand B.** The slant and the letter forms of these margins (f, x, p, d, the abbreviations "dém.", "OPS") match the cursive of hand B on 71/12, 30 and 32.
- **The addressee.** The pencil note on 71/36 addresses the author as "tu".
- **The side count of Lemma XI.** The insertion "à n ⩾ 3 côtés" above the statement of Lemma XI on 71/36 is in the same grey medium. Its relation sign is overwritten by a blot (250 dpi), so the ink does not settle "⩾" against ">".

### 71/21-48: the manuscript

**Plan (71/21).**
- *Théorème 1 (Jordan):* every polygon is a J-polygon.
- *Théorème 2 ("Dehn (?) non-publié"):* every polygon has at least three good vertices, and for at least two of them the triangle is interior.
- Section 1: preliminaries. Polygons are the geometric realizations in ℝ² of connected abstract polygons; arcs; Remarque 1 (two vertices cut a polygon into two arcs).

**Definitions (71/23).**
- *Definition 1, J-polygon:* ℝ² - Γ = U ∪ V with U and V connected, U relatively compact and V̄ non-compact; and local two-sidedness at every point of Γ. Margins: "V ! non rel. compact", "non vides !".
- *Definition 2, good vertex:* s is not collinear with its two neighbours s', s'', and the triangle s s' s'' contains no vertex of Γ in its interior. Margin: "vague".
- *Definition 3:* visibility.

**Lemma I (71/25).** An arc of Γ has a neighbourhood V with V ∩ int Γ and V ∩ ext Γ connected. Right; the proof is a finite cover by disks. Its appeal to "l'axiome du choix" is superfluous (margin "!").

**Convex sets (71/27-31).**
- Lemma II: the boundary of the convex hull of a finite set is a polygon.
- Lemma III: an edge has a supporting line.
- Lemma IV: from a point outside a convex set some non-vertex point is visible.
- Lemma V: if y ∈ ]s, s'[ is visible from x, every point of the line ss' is visible from x. The proof actually shows that the convex set lies in the closed half-plane opposite x, which is what the margin's NB says.
- Lemma VI: convex polygons are J-polygons, and their non-flat vertices are good.
- All checked (SA01-R71-05).

**Hull and visibility (71/31-34).**
- E(Γ) = E(S(Γ)).
- Lemma VII: ext ∂E(Γ) ⊂ ext Γ. Margin: "inutile".
- A second "Lemme VII", in fact VIII (SA01-K71-02): a non-convex polygon has two vertices s, s' with ]s, s'[ ⊂ ∂E(Γ) ∩ ext Γ.
- Lemma IX: a convex polygon has interior angles ≤ π.
- Lemma X: every polygon has at least three vertices with interior angle < π, namely the hull vertices.
- Right (SA01-R71-05).

**Lemma XI (71/36-37): an interior diagonal.**
- **The statement.** As first written it is false for n = 3: a triangle has no diagonal. The margin "faux pour n = 3!" is right. With the inserted side count (n ≥ 4) it is the classical lemma (SA01-K71-01).
- **Case 1** (T minus its two edges does not meet Γ). Here the margin says "faux" beside the conclusion, where the ink shows "ext" struck and "int" written. As it now stands the case is right with s taken from Lemma X: the convex sector at s is the interior one, so the connected set T - ([s,s'] ∪ [s,s'']) lies in int Γ.
- **Case 2a** (Γ meets T only on ]s', s''[). A vertex z of Γ on ]s', s''[ gives ]s, z[ ⊂ T̊ ⊂ int Γ. Right. In the ink (200 dpi) a slash stands before "⊂" (transcribed "/ ⊂" or "⊄"); only "⊂" makes the case coherent.
- **Case 2b** (71/37, T̊ meets Γ). The manuscript takes the convex hull C of (T̊ ∪ ]s',s''[) ∩ Γ and a vertex of ∂C visible from s (Lemmas IV-V).
  - The margin objects that C is not a "convex set" in the manuscript's own convention (the hull of a finite set). The objection is right as to the convention, and repairable: that set is a finite union of segments, so its hull is the hull of finitely many points.
  - The margin proposes the standard shortcut, the vertex of Γ in T farthest from the line s's''.
- Checked (SA01-R71-03).

**Section 3: Theorem 1 (71/38-44).**
- Take a hull chord [s, s'] with ]s, s'[ ⊂ ∂E(Γ) ∩ ext Γ (corollary to Lemma VIII). Glue it to the two arcs of Γ to get Λ¹ and Λ², and argue by induction on card S(Γ) - 2.
- Lemmas XII-XV place Λ² inside Λ¹ (after labelling). Then V = ext Λ¹ ∪ int Λ² ∪ ]s, s'[ and U = int Λ¹ - R_{Λ²} are the two components of ℝ² - Γ (Lemma XVI), and Lemma XVII gives the local two-sidedness.
- The carrying step, that the pocket int Λ² is part of the exterior of Γ and the chord joins it to ext Λ¹, is right (SA01-R71-04).
- Slips in the proof of Lemma XVI on 71/43 (SA01-K71-03):
  - "Soient x, y ∈ U = ext Λ¹ ∪ ..." should read V;
  - in the second case, "Λ_xy ⊂ ext Λ¹" should read ⊂ int Λ² ∪ ]s, s'[.

**Section 4: Theorem 2 (71/44-48).**
- Cut Γ along the interior diagonal of Lemma XI.
- Lemma XVIII: Λ² - {s, s'} ⊂ ext Λ¹. In its proof, "Λ¹ - ]s, s'[ ⊂ ext Λ¹" should read ext Λ² (SA01-K71-04).
- Lemma XIX: int Λ¹ ⊂ ext Λ².
- **Lemma XX:** two good vertices with interior triangles, non-consecutive when n ≥ 4. This is Meisters' two-ears theorem (G. H. Meisters, "Polygons have ears", Amer. Math. Monthly 82 (1975), 648-651; locator to be checked).
  - The manuscript's proof iterates a re-gluing (Λ^{1(n)}) when the ear found in Λ¹ is an endpoint of the diagonal. The margins question it ("?", "!", "so what").
  - The iteration is not needed. Taking the lemma itself as the induction hypothesis (two non-consecutive ears in each Λ^i, or the apex when Λ^i is a triangle) gives in each Λ^i an ear outside {s, s'}, which is an ear of Γ. The two ears lie on different open arcs, so they are not consecutive.
  - The conclusion is right (SA01-R71-02). The iteration was not checked line by line.
- **Lemma XXI:** a non-convex polygon has a good vertex whose triangle is exterior (a "mouth").
  - The proof applies Lemma XX to the pocket Λ² cut off by a hull chord. Since the two ears of the pocket are not consecutive, one of them is not an endpoint of the chord; its two edges are edges of Γ, and its triangle lies in the pocket, hence in ext Γ.
  - The proof is right, provided Λ² is the inner polygon as labelled in section 3. This is the content of the pencil "faux, si on ne choisit pas bien ses notations"; the margin's "douteux" is answered by the non-consecutiveness.
  - The statement and this argument are the "one-mouth theorem" of G. T. Toussaint, "Anthropomorphic polygons", Amer. Math. Monthly 98 (1991), 31-35 (locator to be checked).
- **Theorem 2 follows.** A convex polygon has at least three good vertices, all ears. A non-convex one has two ears (XX) and a mouth (XXI).
- **Checks (SA01-R71-02).**
  - Re-proved by the pocket argument.
  - Computed: 17,593 random simple polygons with 5 to 12 vertices. Every non-convex one has a mouth; none has fewer than three good vertices or fewer than two ears.
- **"Dehn (?) non-publié".** Dehn's unpublished proof of the polygonal Jordan theorem was described by H. Guggenheimer, "The Jordan curve theorem and an unpublished manuscript by Max Dehn", Arch. Hist. Exact Sci. 17 (1977), 193-200 (locator to be checked). The manuscript's attribution carries its own question mark.

### 71/3-19 and the versos: notes in hand B

- **71/10-12: pairs of open sets and pseudopartitions.**
  - For open U, V the conditions a) U = ∁V̄, V = ∁Ū; b) U ∩ V = ∅ and ∁(U ∪ V) ⊂ Ū ∩ V̄; c) U ∩ V = ∅, X = closure(U ∪ V), U̇ = V̇ are equivalent. d) Ū ∩ V̄ = U̇ = V̇ is a consequence only: U = V = ∅ satisfies d) and not a). The transcription's arrow "⇐" for d) fits this.
  - U admits such a V iff U is regular open, i.e. ∁Ū is dense in ∁U, as he says.
  - For a closed K with complementary regular opens U_K, U'_K of K and B = U_K ∩ K̇, the formulas for Int, closure and frontier hold when B ∩ C = ∅. His corollary is right: X_1 = ∁U_K is locally closed iff B̄ ∩ C = ∅ iff B is closed in X. The reading "fermé dans X" is the right one, not "X_1"; B does not meet X_1 (SA01-K71-05).
  - The six-set pseudopartition U, U', W, B, B', C of 71/12 checks.
  - All in SA01-R71-06.
- **71/6-8: cutting X along K.** The amalgamated sum 𝒳 of the X_i over W; 𝒳 → X is étale off ∐C_i and a closed immersion on ∐C_i. His own pencil asks "vérifier l'énoncé précis". Not checked.
- **71/7 and 71/13:** flags Drap(I), strata Σ_d(𝒳), Δ_{i_0..i_k}, and a cancelled comparison |Δ̃| →? Σ(|K|, |L|). These are the "simplicial realizations (|K|, |L|)" of SA01-40. Too sketchy to check.
- **71/11: a braid computation.** For a triple with λ_0λ_1λ_2 = 1, the half-twist t: (λ_0, λ_1, λ_2) ↦ (λ_0, λ_1λ_2λ_1^{-1}, λ_1) satisfies t(λ_1) = λ_0^{-1}λ_2λ_0 and t² = conjugation by λ_0^{-1}. This is his "int(λ_0^{-1})"; the "t² = int(λ_0)" at the head uses the other convention for int (checked, SA01-R71-06). Below it: induced bundles G ∧_H E, f_! f^*.
- **71/14:** the theta-curve. Three arcs Γ'_1, Γ'_2, Γ'_3 join x and y, and Γ_i is the union of the other two. "v_1, v_2, v_3 in distinct regions" ⇔ "E - Γ has three regions"; "Γ_1, Γ_2 Jordan curves" ⇒ a) ⇒ "all three Γ_i are Jordan curves". These are the statements of the theta-curve lemma; the proofs are sketched.
- **71/17:** for a simple closed curve C in a connected surface, card π_0(E - C) ≤ 2, and three equivalent forms of "C separates".
- **71/19:** two J-polygons meeting in a polygonal arc I are either side by side or nested, and Γ'' = (Γ ∪ Γ') - (I - ∂I) is a J-polygon with the stated interior and exterior. This is the compact form of the manuscript's Lemmas XII-XVI. Right (SA01-R71-04).
- **71/30 (verso, hand B):**
  - many polygon sketches;
  - a lemma: every polygon has a non-flat vertex whose exterior sector exceeds π;
  - for n ≥ 4, cases (i)-(ii) of the interior diagonal;
  - a corollary: either ]s', s''[ ⊂ Int Γ, or some t ∈ S(Γ) has ]s, t[ ⊂ Int Γ, with t the vertex of T farthest from s's''.

  This is the shortcut proposed in the margin of 71/37.
- **71/32 (verso, hand B):**
  - two distinct polygons meet in finitely many arcs;
  - for Γ' = ∂E(Γ), each endpoint s of a component of Γ ∩ Γ' has a t with ]s, t[ ⊂ Γ' ∩ ∁Γ ⊂ Ext Γ;
  - Cor: a non-convex polygon has a hull chord in Ext Γ;
  - "NB Ext(Γ) est défini pour tt polygône".

  This is the manuscript's Lemma VIII in compact form.

### Reused sheets (SA01-43)

- 71/4 and 71/15: Montpellier thesis-defence notices of 19 April 1977 (Sciences de la Terre, géologie appliquée; chimie-physique). The transcription has their full text; we reproduce nothing beyond the type and date.
- 71/9: a printed bank circular of January 1978 with a payment-authorization form; not reproduced.

These sheets are among the notes of 71/3-19, and the archive's cover lists "Versos: lettres (1977-1978)". The hand-B notes written on such sheets therefore date from after April 1977, and after January 1978 for the leaf of 71/9. The pairing of each note with its verso was not checked on the physical leaves.

### Cote 71: state and links

**State.**
- Every transcribed scan is read.
- Corrections: Lemma XI as first written (SA01-K71-01); the double "Lemme VII" (SA01-K71-02); slips on 71/43 and 71/45 (SA01-K71-03, -04); the reading "X" on 71/10 (SA01-K71-05); the signature reading of 71/48 (SA01-K71-06).

**Links.**
- SA04-22 (cote 73), our note: the triangles of the good vertices are the "ear" triangles whose areas cote 73 uses to recover a pentagon (73/20).
- SA01-41 (cote 75): combinatorial polygons and their orientation.
- SA01's plane-topology items (cotes 81, 154), as the sweep-2 map groups them.
- Literature: Meisters 1975, Toussaint 1991, Guggenheimer 1977 (above).

---

## Cote 75: the DEA course "Géométries combinatoires", 1977-78 (SA01-41)

Scans 1-33: 31 transcribed in four Codex-web folders (J75-01 to J75-04). 75/1 is the archive's cover sheet (viewed at 110 dpi): "Cours C4, DEA : notes manuscrites (s.d.), lettre (1978), tapuscrit (1977-1978). Cote n° 75, 32 pages". 75/29 is blank.

**75/2: the head of the notes.** "C4 DEA / Géométries Combinatoires", with "(24 p)" in the margin.

### 75/3-17: groups, graphs, contours, small groups, torsors

**Groups and homogeneous spaces (75/3).**
- Pointed homogeneous spaces ⇔ subgroups (an equivalence of categories); isomorphism classes ⇔ conjugacy classes.
- Torsors are the largest homogeneous spaces.
- Aut_G(P) ≅ G non-canonically, with u_{gx} = u_x ∘ int(g^{-1}). His boxed "u_y = u_x ∘ int(s^{-1})" for y = sx is checked by his own lines.

**Graphs (75/4-5).**
- Graphs as (S, A, R); strict graphs; the topological realization by gluing segments.
- A finite graph has a rectilinear realization iff it is strict, and then one in ℝ³: points with no three collinear and disjoint segments for disjoint pairs. Right: points on the moment curve do it (SA01-R75-04).

**Contours: 2-regular graphs (75/5-8).**
- The connected ones are classified by c = card S, any cardinal with 2 ≤ c ≤ ℵ_0, strict iff c ≥ 3. They correspond to the subgroups H ≠ ℤ of ℤ.
- Orientations: two for a strict contour.
- Aut(X) ≅ ℤ/2 · ℤ/H (semidirect product), with Aut⁺ cyclic and generated by either orientation.
- A connected oriented contour is a torsor under ℤ/n, i.e. a set with a circular order.
- All right (SA01-R75-03).

**Sets with a permutation, ℤ-sets (75/9).**
- Classification by the numbers n_i of orbits of each type, and the finiteness criterion.
- **The transitivity line.** "u transitif (⇔ u définit sur E un ordre circulaire) ⇔ tous les n_i sauf un au plus sont nuls". The arrow is "⇔" in the ink (viewed at 300 dpi). The condition is necessary only: (12)(34) has n_2 = 2 and is not transitive. Right: u is transitive iff Σ n_i = 1 (SA01-K75-01).
- Conjugacy classes of S_n ⇔ partitions of n. His table: S_2: 2, S_3: 3, S_4: 5, A_3: 3. It leaves S_5 ("?") and A_4 blank: they have 7 and 4 classes (computed, SA01-R75-02).
- The semidirect product as a split extension, with the margin "Parler ici d'un gr. inverseur d'extensions ... Aff(Z) ≃ Z·Aut Z".

**Affine groups (75/10-12).**
- Aff(Z) ≅ Z · Aut(Z); Aff_R(V) ≅ V · Aut_R(V); Depl(V, Q) ≅ V · O(V, Q).
- The splittings q_t of a torsor: q_{tg} = int(i(g)) ∘ q_t (checked on the page).
- Aff^{±1}(ℤ_n) is the dihedral group D_n.
- On 75/12, the reflection fixing a vertex: σ_{tg} = g²σ_t = σ_t g^{-2}. For n odd, t ↦ σ_t is a bijection onto the reflections; for n even its fibres have 0 or 2 elements. Checked (SA01-R75-03).
- Fibre products of sets and groups; pulling back an extension.

**Small sets (75/13-14).**
- S_3 ≅ Aff(1, F_3) ≅ GL(2, F_2) ≅ GP(1, F_2); A_3 ≅ F_3⁺.
- S_4 ≅ Aff(2, F_2) ≅ GP(1, F_3); A_4 ≅ Aff(1, F_4), which he marks "?" and which is true.
- S_5 ≅ GP(1, F_5); A_5 ≅ GP(1, F_4).
- All computed as faithful permutation groups with matching orders and element-order profiles (SA01-R75-02).

**Classical groups and the structures they define (75/14).**
- Vector, affine and projective structures as elements of Isom_ens(k^n, -)/G.
- In the affine line, "Isom_ens(k^n, V)/Aff(n, k)" should read Isom_ens(k^n, E) (SA01-K75-02).

**Regular realization of a polygon (75/15-16, an exercise).**
- Existence from z^n = 1; uniqueness up to similitude, every combinatorial isomorphism being induced by a unique similitude.
- The affine or vector envelope of a combinatorial polygon.

**Contracted products (75/16-17).**
- ^P E = P ×_G E, P → Bij(E, F).
- Injectivity holds exactly when G acts faithfully on E (right).
- Transport of every G-invariant structure.

### 75/18-28: torsors at work

- **75/18-20.**
  - (G, E)-structures; Isom(P_n, P) is a D_n-torsor, so a combinatorial polygon with n sides is a D_n-torsor T, with P = ^T P_n.
  - Its envelope Env(P) = ^T E, with D_n acting on ℂ by ζ^i and complex conjugation.
  - Functors on a connected groupoid C_E ≃ G-objects (right).
  - Extension of the group of operators: E ×_G G'.
- **75/21: torsors under a commutative group.** X ∧ Y = X ×_G Y is associative and commutative with unit G_s, and every torsor has an inverse.
- **75/22: "structures cubiques".**
  - Over a ring with 2 ≠ 0: free modules with n free rank-1 summands, each with a bi-base {e_i, f_i = -e_i}, are equivalent to 2n-sets with a fixed-point-free involution.
  - The automorphism group is (±1)^n · S_n = W(B_n). For n = 4 this is the torsor category of 74/134 ("8-sets with an involution ≃ 4-cubes ≃ W(B4)-torsors"; SA04 reading, cote 74).
- **75/23-24.**
  - A connected contour C gives ω(C), its two orientations, and G⁺ = Aut⁺(C) ≅ ω ∧_{±1} ℤ_n. Conversely (ω, T) gives a contour.
  - Exercise: a torsor under Z · Γ ⇔ a Γ-torsor ω together with a torsor under ω ∧_Γ Z. Right.
- **75/25-28: orientations.**
  - Of a real vector space: ω_E = P ×_G {±1}. Of a free quadratic module with 2 invertible: through O(n) → {±1}. Of a finite set: through the signature.
  - Compatibilities through S_n → O(n, k) → {±1}: permutation matrices have determinant equal to the signature.
  - The associativity formula ω_E ≅ ω_{I⁻} ∧ ⋀_i ω_{E_i}, I⁻ being the summands of odd dimension, is right: exchanging two summands changes the orientation by (-1)^{d_i d_j} (SA01-R75-03). The same holds for a map J → I of finite sets with odd fibres I⁻.
  - Filtrations: ω_E ≅ ⋀ ω_{E_i/E_{i-1}}.

### 75/30-33: a letter head and the two course announcements

- **75/30.** The letterhead of the Institut de Mathématiques (USTL), "Villecun le 30.01.78", from "Monsieur Alexandre Grothendieck, Professeur", to the Minister of Education, with the salutation and the signature. Nothing more is transcribed; we reproduce nothing further.
- **75/31-32, typed: "Cours C4 1977-78 de A. Grothendieck: Géométrie de l'icosaèdre".**
  - The programme: the combinatorial icosahedron and the oriented 5-set ("les cinq couleurs coloriant les arêtes"), with group A_5, and realizations over all fields and rings.
  - Characteristics 2 and 5 are special, through A_5 ≅ SL(2, F_4) (≅ GP(1, F_4) ≅ SO(3, F_4)) and S_5 ≅ GP(1, F_5) (≅ SO(3, F_5)).
  - All four isomorphisms are right: SL(2, 4) = PSL(2, 4) = PGL(2, 4), O(3, q) ≅ Sp(2, q) for q even, and SO(3, q) ≅ PGL(2, q) for q odd. The A_5 and S_5 cases were computed (SA01-R75-02).
- **75/33: "Cours DEA 1977/78 de A. Grothendieck: Géométrie arithmétique des polygônes réguliers".**
  - The programme: regular polygons over a field, then over any base ring, "le n-polygône régulier 'le plus général'", and the general regular icosahedron over a ring finite over ℤ with residue fields of every characteristic ("la caractéristique deux donnera sans doute du fil à retordre !").
  - This is the programme of cotes 70 and 72 (SA04-21, SA01-1) and of SA04 hunch H3-4 (the icosahedron mod 5).
  - Computed for the hunches H75-1 and H75-2 (SA01-R75-05):
    - the general regular p-gon over ℤ[2cos(2π/p)] degenerates exactly above q when p = q^k or 2q^k (p = 3..30);
    - at {3,5} the discriminant δ' of 70/69 is a unit (φ²) and δ = -3φ⁴;
    - at {5,3}, δ' = 1 and δ has norm 5.

### Cote 75: state and links

**State.**
- Every transcribed scan is read.
- Corrections: the transitivity criterion of 75/9 (SA01-K75-01, decided on the scan); the slip V for E on 75/14 (SA01-K75-02).

**Links.**
- SA01-1 and SA04-21: the announcement of 75/33 is the programme of cotes 70 and 72.
- SA01-16 and SA04 H3-4: 75/31-32 (A_5, S_5 and characteristics 2 and 5).
- SA04-23: 75/22 and 74/134.
- SA01-40: polygons.

---

## What was not reached

Every transcribed scan of cotes 71 (41 scans) and 75 (31 scans) is read. The untranscribed scans were viewed: 71/1 and 75/1 (archive covers); 71/2, 5, 16, 18, 20 and 75/29 (blank); 71/35 (one line, given above). Not reached:
- **Readings not viewed on the scan:**
  - 71/10 "X_1" or "X";
  - the slips of 71/43 and 71/45;
  - 75/14 "V";
  - the margins of 71/23, 25, 27, 37, 38, 47 and 48 beyond what the J71 notes say of their medium.
- **Hand B's notes on 71/6-8 and 71/7, 13** (cutting along K, flags and strata): read, not checked.
- **Lemma XX:** the manuscript's iteration (71/47-48) was not checked line by line; the lemma is checked by the simpler route.
- **Not used:** Michel Hua's project, the Work math notes.
