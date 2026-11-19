# SA12 (Séminaire de Géométrie Algébrique), sweep 3: the fundamental group (cote 29) and cohomological dimension (cote 31)

Lead: agent a65dbdc241d1a129a (Claude Opus 5.5 at effort max), 19 Nov 2026, with two readers, both Claude Opus 5.5 at effort max:
- reader A, agent a203d72bad105bea5;
- reader B, agent a3c8d7ded052a745e. It was interrupted at 29/187, then resumed by the coordinator, and it finished cote 29 to scan 217.

The details, item by item, are in `readings/`:
- `c29a.md`: cote 29, scans 2-140 (reader A);
- `c29b_c31.md`: cote 29, scans 141-217 (reader B; despite its name it holds no cote 31);
- `c31_lead.md`: cote 31, scans 2-102 (the lead).

Their check events and corrections are merged into CHECK_EVENTS.tsv (106) and CORRECTIONS.tsv (24).

**Read in sweep 3, in full: 306 of the 469 transcribed pages.**
- Cote 29, scans 2-217: all 213 transcribed pages. Scan 7 has no transcription anywhere; 190 and 208 are blank (decided on the scans).
- Cote 31, scans 2-102: 93 pages. Scans 34, 40, 41, 46, 53, 64, 73 and 89 have no transcription.

**Not read in sweep 3: 163 pages, none of them in cotes 29 or 31.** They were placed in sweeps 1-2 and are listed in DELIVERABLES.tsv.
- **Cote 33** (96 pages, Pro MPL_33_002-049 with its parallel chat, and MPL_33_050-097): the 1965 SGA 5 duality draft (SA12-52 to SA12-61), with reused typescripts.
- **Cote 37** (55 pages, B37-01..05, H37-01): the SGA and EGA re-editions of 1967-71, and the letters. They include Grothendieck to Dieudonné, 22.8.1967, on whether formal smoothness is local (F31), and Hartshorne's letter of 4.8.1969.
- **Cote 32** (8 pages, C32-01): the Gysin map and the local fundamental class.
- **Cote 35** (4 pages, H35-01): the plan of SGA 7.

Item ids are SA12-n of `sweep2/SA12/OBJECTS.tsv`; flags Fn are those of `sweep2/SA12/FLAGS.tsv`. Hua = Michel Hua's project, a credited witness.

## Cote 29: the fundamental group

### 1. Tame ramification: the Grothendieck-Murre dossier of 1967 (29/002-039) — SA12-11, SA12-30, SA12-31
- **The order of the letters**, read by their dates:
  1. 29/005-006: Murre to Grothendieck, 29.3.67.
  2. 29/008-009: Grothendieck to Murre, 11.4.67.
  3. 29/010-012: Grothendieck to Murre, 24.4.67.
  4. 29/003-004: Murre to Grothendieck, 16.5.67.
  5. 29/035-039: Grothendieck's reply of late May 1967, written between 16 May and 2 June.

  This is the genesis of Grothendieck-Murre, LNM 208 (1971).
- **The typescript "Données de ramification"** (29/013-034) is the sketch enclosed with the letter of 24.4.67 (identified by reader A, new). Murre quotes it word for word on 29/003.
- **Checked:**
  - His counterexample to Murre's 1.16.
  - The exact condition n_i | n'_i for maps of Kummer covers. Murre's "n' = m.n" is right, and Grothendieck's "n' ≥ n" means divisibility (his own reply says so).
  - The regularity of A[T]/(T_i^{n_i} − x_i), in every characteristic.
  - The full-faithfulness criterion for Kummer data a), whose hypothesis "no common components" is needed.
  - "r ne commute pas aux produits".
  - The Galois criterion of §4 for Kummer data.
  - The classification Hom(G_i, H)/H of the reply.
- **Wrong or loose:**
  - In case b) (29/021-022), "deux à deux disjointes" (on the ink) excludes crossings. The working condition is "no common component"; he calls it himself "la condition canularesque".
  - The section "Cas des revêtements galoisiens" is §4: the digits 3 and 4 are overtyped (29/031).
- **Open on the pages, settled later:**
  - case 2° as a full subcategory;
  - transitivity;
  - fpqc descent for coverings of type R;
  - the a posteriori tameness (29/011, 29/100).

  All are in LNM 208 (locators unverified).

### 2. "Finitudes (Pbs et conjectures)" (29/040-046) — SA12-32, SA12-3
The programme, over a separably closed k:
- π₁ of a proper scheme is of finite type ("démontré").
- π'₁ (the prime-to-p part) of a scheme of finite type is of finite presentation. "Le cas 'type fini' est prouvé" (the ink, sweep 2): only finite generation is proved.
- π₁^t is of finite type, "Prouvé Modulo conjecture d'invariance birationnelle de la ramification modérée". Its "N.B. c) plus général que a)" is right.
- Local and uniform versions.

Item 3) b), the constructibility of π'₁ of the geometric fibres, is Orgogozo (2003, locator unverified).

The finite presentation of π'₁ without resolution is not settled on the pages (Esnault-Schusterman-Srinivas for good compactifications; locator unverified).

### 3. Relative finiteness for π₁ (29/047-058) — SA12-1, SA12-2
**Lemma 1 (descent of a generically defined isomorphism).** The hypothesis on the ink is "réduit", not "biréduit" (decided on the scan, 29/048).
- Reader A's counterexample with a non-reduced fibre shows the hypothesis is needed: X = Spec R[x,x⁻¹,z]/(z² − tx) over a DVR.
- The steps with "réduit" were checked, except his "considérations de profondeur".

**Lemmas 3-4** were re-derived.

**The "Prop" of 29/058** (finitely many étale covers of each degree for curves implies the same for all X of finite type, his margin "?"):
- its hypothesis forces char k = 0, because of the Artin-Schreier covers of A¹;
- it is correct as stated;
- the induction uses more than curves over k, which may be what his "?" asks.

### 4. π₁ and Pic^τ birational (29/060-065) — SA12-3, SA12-4, SA12-6
- **F5, decided on the scan.** The cover reads "π₁ et Pic^τ birationnels".
- **Checked:**
  - finite generation of π'₁ by van Kampen and a generic curve (Bertini, Jouanolou 6.3, locator unverified);
  - the product formula, checked on Kummer covers. It fails for the full π₁ in characteristic p (z^p − z = xy), which is why Γ is prime to p.
- **Open (his):** is π₁(X − Y) modulo the wild inertia at the codimension-1 components of Y topologically of finite type? (29/061)

### 5. π₁ of a proper scheme minus codimension ≥ 2; the birational π₁ (29/066-070) — SA12-5, SA12-7, SA12-8
**The Chow step of 29/066 is false for proper surjective maps** (Bl_p P² → P²; F12 confirmed). The gap is confined to proper non-projective Z:
- for projective Z the theorem is proved on these pages;
- the finite generation of the birational π₁ (29/070) survives in full, since it needs only the projective case (reader A, new).

**His question on 29/070 has the answer no** (Pro BR13, re-derived): is π₁(U; Ω) → π₁(K/k; Ω) bijective for U the regular locus of a normal model?
- X = (P¹ × P¹)/±1 has four A₁ points; U is the complement of those points.
- U has the double cover from P¹ × P¹, while π₁(K/k) = 1.

**Open (his):**
- the margin question whether π₁(X − Y) → π₁(X) has a kernel of finite type for Y of codimension ≥ 2;
- the proper non-projective case in characteristic p.

### 6. Birational invariance of Pic^τ (29/071-077) — SA12-9, SA12-10
**The theorem (29/071).** f: X → Y is a birational morphism of normal proper k-schemes with Y regular. Then Pic^τ_Y → Pic^τ_X is an isomorphism.

**What the page proves** (checked step by step by reader A):
- the monomorphism;
- the bijection on points, through the negativity lemma (Kollár-Mori 3.39, locator unverified);
- the bijection H¹(Y,O) ≅ H¹(X,O), without resolution:
  - in characteristic p, by splitting off the F-bijective part (via π₁ and H¹(Z/p)) and the F-nilpotent part (via Kunz on the regular Y);
  - in characteristic 0, by reduction mod p.

**The gap.** The last step, "closed immersion, bijective on points, iso on tangent spaces ⇒ iso", fails for non-smooth group schemes: α_p ⊂ α_{p²}.
- So the theorem is proved in characteristic 0, and has a gap in characteristic p when Pic^τ_Y is not reduced.
- What closes it: injectivity of H²(Y,O) → H²(X,O), which holds when R¹f_*O_X = 0 (Chatzistamatiou-Rülling for smooth X; locator unverified).

**The rank formula of 29/076** needs l ≠ p: a supersingular elliptic curve has p-rank 0. With l ≠ p, the uniform bound n(K/k) on normal models was re-derived.

**Open (his):**
- the Question of 29/075: is the system of Pic^τ essentially constant on normal models without a smooth model? It is equivalent to the boundedness of dim H¹(O).
- a proof of the bound without π₁ (29/077).

### 7. Murre's 1969 draft and Grothendieck's comments (29/078-086) — SA12-11, SA12-17
- **29/079-081.** Murre's letter of 30.4.69: the draft on "formal tamely ramified coverings" and "plumbing", chapters I-X, with "The chapter on the analogue of the theorem of Mumford has still to be written".
- **29/082-086.** Grothendieck's comment sheets on it (F17 settled: by the item numbers they answer Murre's typed comments).
  - F6, decided on the scan: "Normality-assumption more natural".
  - The circled line "where is the 'Abhyankar lemma'?" is kept in a figure node by the Pro page. An edition must print it as text.

### 8. The formal tame π₁ along a divisor (29/088-103) — SA12-16, SA12-17, SA12-18, SA12-19
**Setting.** The inertia extension μ → π₁^t(X^/D) → π₁^t(U) → e, with its class α. The class is the self-intersection class (Lemma 2); the topological model is the Euler class of a circle bundle.

**Checked:**
- Lemma 1 (H¹ of the universal tame cover).
- The Picard lifting of 29/094 (F13). It is false as written, without properness: the kernels of Pic(X_m) → Pic(X₀) acquire n-torsion when a unit of X₀ does not lift. It is true for X₀ proper over a field, the intended setting ("th. de Mumford"; re-proved).
- **Example I, "extension triviale" (29/096, F1).** It is right when D'₀ ≠ ∅. It is false for a complete curve of genus ≥ 1 with nonzero self-intersection, where the extension is of Heisenberg type.
- Example I 2°: the lens-space case, μ_{d'}.
- **Example II** (X₀ = Spec ℤ): the tame π₁^t(Spec ℤ − S) is in general non-abelian. Example: the S₃ field of x³ − x − 1, ramified only at 23.
- 29/101-103: the class equals c(O(D)), checked in two cases.

**Open (his):**
- "Mais qu'est Π₂^t(X₀/D'₀) ???" (29/098);
- the a posteriori tameness on 29/100;
- the hypothesis "D_i disjoints" of 29/092.

### 9. Quasi-unipotence, Π₂, local algebra (29/104-112) — SA12-20, SA12-21, SA12-23, SA12-24
These were checked:
- Lemma 6.5 (F G F⁻¹ = G^q ⇒ G quasi-unipotent, cancelled);
- H²(X,M) = Hom(Π₂(X), M) for X simply connected;
- the Chinese remainder theorem and the monic factorizations.

29/112 is the title "Notes pour SGA 7".

### 10. Bertini and the functorial behaviour of inertia (29/113-123) — SA12-6, SA12-16
Checked:
- Bertini 1 and its corollaries.
- His reservation that π₁(Y_t̄) → π₁(X_t̄) need not be onto without properness is justified: an Artin-Schreier cover on A² splits on the generic line.
- Th. 6 (non-generic sections), given the tame specialization theorem.
- The inertia matrix N is an isomorphism iff det N = ±p^r (29/121).
- The conjugacy of inertia along a transversal divisor (29/122).

**Open (his, 29/116):** conjugacy of the vanishing cycles under π₁(D − D^v) for a general (not generic) Lefschetz pencil when char k = 2 and dim X is odd.

### 11. The "vrai" fundamental group: the letter to Serre of 1959 (29/124-130) — SA12-22
- **F19, decided on the scan:** "[pour les ensembles]".
- **F16 stays open:** the month is 6 or 8, and the place "Vallou…" is not read.
- **The letter.** A category of finite group schemes with conditions (i)-(vi), including "special" groups and S reduced.
- **Re-proved:**
  - the rigidity lemma (29/126). Its hypothesis (vi), S reduced, is needed: α_p over k[ε];
  - the pro-representability by minimal pairs (29/127-128).

  This is the construction published later by Nori (1976/1982).
- **The p-part as a "module de Weil"** with Witt-vector coefficients and three pieces (29/129-130) is the Dieudonné-module programme, seven years before crystals.

### 12. Pointed torsors and Proposition 4 (29/131-143) — SA12-22, SA12-25, SA12-26, SA12-35; F7, F23, F10
**Proposition 4 (29/139, 141).** "Si α est minimal, alors u ↦ u_*(α) est injective." It is **false as stated**: the cusp A = k[x,y]/(y^p − x^{p+1}) and α_p (Pro N033, re-derived in full by reader A):
- the torsor z^p = x is minimal;
- u = 0 and v = [x] have u_*α = v_*α;
- the equalizer is not flat.

**Reader B (new): the proof as written never uses minimality.**
- The diagonal claim c ≡ 1 is equivalent to u = v.
- The final "unicité" of pointed maps fails without minimality: take G = ℤ/2 constant and α trivial.

**What is true** (re-proved):
- Proposition 4 holds in the étale case: minimal ⇔ P connected, and pointed maps from a connected P to a finite étale scheme are unique.
- It holds for u, v whose equalizer is admissible. This covers the letter's setting of constant groups.
- Given Prop. 4, the pro-object π₁^C of 29/143 is formal.

**Other points.**
- Uniqueness of U (29/137) does not need S reduced.
- Exemple II on the ink reads "ce qui semble raisonnable surtout si k sep. clos". The Pro reading "rend vraisemblt inutiles les hyp." is a misreading, and Pro note N143.2 rests on it.

**Open:**
- Proposition 4 for finite flat non-étale G with S-morphisms varying along S;
- the representability of pointed G-torsors on X_T for f proper flat (29/131).

### 13. "Compléments SGA 1960" (29/144-163) — SA12-33, SA12-34, SA12-35, SA12-37
**The π₁ of a fibre product (29/149-151).** π₁(X ×_S Y) → π₁(X) ×_{π₁(S)} π₁(Y), re-proved.
- The ink reads "[par exemple fini / S' étale sur S]" (the Pro has "si(?)").
- "Fini" is needed: for S' étale and not finite the clause is false (G_m → A¹).

**Finite étale covers of rank n (29/153-157).**
- Serre's G_n-torsor argument was re-proved.
- Prop. 3.1 needs X separated over Y (the doubled origin).

**Galois categories (29/158-161).**
- "[implique F(X) = ∅ → X = 0]" holds.
- The margin axioms need X ≠ 0.
- The descent example needs "fidèlement plats".

**Proper dominant f to a normal Y has finite cokernel on π₁ (29/162), re-proved.** His N.B. (non-normal Y) works for every integral nodal curve, not only rational ones.
- "[p. ex. Y normale]" does not give universal openness (the blow-up of A²).
- The construction of f_*(X₁) for universally open f (29/163) is his conjecture, left open.

### 14. The progroupe fondamental for infinite principal covers (29/164-172) — SA12-22, SA12-37
- Left exactness and minimal elements for pointed π-bundles with constant group π were re-proved. The fibres of S' → S are nonempty, which he only asserts.
- This gives a pro-group "qui ne peut plus être interprété comme un simple groupe topologique": the "π₁ élargi" of SGA 3 X §6. Its modern form is the pro-étale π₁ of Bhatt-Scholze (locators unverified).
- The comparisons H¹_{C_i} were checked for finite G. The Dedekind and local cases of 29/172 were not rechecked.

### 15. π₀, π₁ and the simplicial formalism; F(I) ≃? C(K,I); a finiteness proposition (29/173-187) — SA12-37, SA12-26; F22, F26
**The plan "Groupe fondamental" (29/174)** is the plan of SGA 1 X and of cd material.

**Descent data relative to S'/S (29/179).** π₁(S'/S) is generated by n'' − n' elements; killing a spanning tree gives the sharper n'' − 2n' + 1 (computation).

**The question of 29/180:** is every descent datum on G_{S'} effective?
- For S' → S fpqc it is answered by Gabber's descent for ind-quasi-affine morphisms (Stacks 0APK, locator unverified).
- For S' → S proper surjective it stays open on the pages. Rydh's theorem may settle it: universally subtrusive morphisms of finite presentation are of effective descent for étale morphisms (Bull. SMF 2010, locator unverified). It remains to check whether the non-quasi-compact G_{S'} is within Rydh's hypotheses (reader B).

**F(I) ≃? C(K,I) (29/183).** "Néc et suffisantes" is false without compactness:
- the counterexample is K = ℕ^ℕ with φ(x) = x_{x₀+1};
- with all π₀ᵢ finite (K profinite) the conditions are necessary and sufficient, and his own "[compact?]" (29/181) answers itself "yes";
- in the NB, "ni surjectif" is right: L = ω₁.

**The proposition of 29/187** (quasi-finite separated and locally of finite type over a universally japanese base is of finite type) is true. Its proof step "il y a un X'-morphisme X̃' → X''" fails. The repair is Zariski's main theorem on the normalization.

### 15A. Ramification data as stacks of multi-Galois categories (29/188-207) — SA12-30, SA12-33, SA12-70; F18
Codex/Work K29-02 and K29-03 only, with no Pro pass. Read by reader B.

- **188 (cancelled): "Opérateur d'homotopie pour d''".**
  - Cauchy operators U_j, T_j and a weight φ_n give P d''f = f − U₁…U_n f.
  - Checked: Cauchy-Pompeiu in each variable, telescoped. φ_n is the average over the n! orders of the variables.
  - It is the handwritten form of the ∂̄-homotopy formula of the reused typescript SA12-70 (33/095, 097). Whether that typescript is his own is not decided.
- **189 is the cover** "Données de ramification / Catégories multigaloisiennes". Manuscript pages 1-16 follow on 191-207.
- **191-197: the definition.** A ramification datum on S is a stack 𝓡 of multi-Galois categories on Et(S) with a cartesian geometric realization r: 𝓡 → Fl_S, under axioms R1-R4.
  - The r-surjective families form a topology. Checked: base change along summands, his "(mettre en lemme)".
  - Prop. 2 (X = ∅ ⇔ r(X) = ∅; connectedness): checked.
  - Prop. 3 and Th. 1: objects subordinate to a Galois P are étale covers of r(P) with a compatible G-action, by descent.
  - Prop. 4: an admissible action (Z, G) gives a ramification datum.
  - "Prop 5 ….." is left unwritten (197).
- **198, Prop. 6 and its Corollary.** A homomorphism of ramification data is necessarily fully faithful. Re-proved through R2 on both sides.
- **199-201: Kummer data.**
  - Ex. 2 is a μ_n-gerbe: the gerbe of n-th roots of O(D_i), whose class is the Kummer coboundary of [O(D_i)]. Checked.
  - "H²(X, μ_n)" is his slip for H²(S, μ_n).
  - His remark "Ces exemples boitent un tout petit peu" means n_i need be prime only to the residue characteristics of D_i, which is the tame condition.
- **202-207: reconstruction.** For a generating cartesian φ: C → 𝓡 and C locally filtering, the functor α of (*) (204) is claimed to be an equivalence once φ is fully faithful.
  - Faithfulness and fullness are proved on the page (checked by reader B).
  - **Open: the proof stops at "Prouvons que α est essentiellement surjectif."** (207, ms. p. 16). The next leaf (208) is blank and 209 starts a new sequence, so the essential surjectivity is not on the pages.

### 15B. "Catégories multigaloisiennes" (29/209-217) — SA12-33; F18
K29-03 only. Read by reader B.
- **A (209-211).** Characterizations of C ≃ 𝒯_revf, the locally constant finite objects of a topos. (i) ⇒ (iii) was checked through the frame torsors Isom([1,i], X), as in Serre's argument of 29/153.
- **B (209-212).** C is a product of Galois categories ⇔ axioms G0-G5, where G5 bounds the degree.
  - **His remark "il se pourrait que G5 soit surabondant" is refuted** (reader B). The countable ℤ-sets satisfy G0-G4 and fail G5: Z × Z contains Z × [1, N+1] as a summand for every N.
  - They also fail G5', his exact-functor replacement for G5. So B(ii) needs G5 or G5', and his induction on N is where it is used.
  - Michel Hua's project presents G5' as a route to redundancy. On the page, G5' is an equivalent replacement.
- **213, 215 (sheets 1 bis, 1 ter).** Conditions ⓪-③ (degree classes) imply A(iii), re-proved by induction on the degree through the diagonal summand. The Corollary that the degree is unique follows.
- **214 (largely cancelled).** Multiple points of f: X → Y of codimension d.
  - For f unramified the boxed ∅ holds.
  - The bound "n − card(E)d, égalité pour P = P₀" needs n − (card E − 1)d (his slip or a dropped −1; not checked on the ink).
  - His question on the closure of the double points at triple points is open.
- **216.** The Corollary for a connected final object (vi: C ≃ C(π), π profinite) is SGA 1 V 4. The sufficiency of (v) without finite colimits is not checked.
- **217.** The Proposition on exact functors between multi-Galois categories was re-proved: faithful ⇔ conservative ⇔ reflects ∅; fully faithful ⇔ bijection on subobjects; equivalence.
  - On the ink, (ii) ends "ss-objets de Y": his slip for u(X).
  - (iii) reads "(cf (ii))".

## Cote 31: cohomological dimension ("SGA A, résidus de rédaction")

### 16. Flat cd_p of a field of characteristic p (31/002-009) — SA12-41
- **The results.** Lemma 1 is the dévissage. Lemma 2 says cd^{t.m.}_p ≤ n iff the H^i(k',G_m) vanish for i > n and H^n(k',G_m) is p-divisible.
- **Checked.**
  - "Degree prime to p suffices" in Lemma 2.
  - Lemma 3, re-proved: cd^{rad add}_p is 0 or 1 as k is perfect or not.
- **Reused.** The even scans 4-8 are an SGA 3 IX typescript.

### 17. A counterexample on cofiniteness (31/010-017) — SA12-43
- **The construction.** A module M = lim E_n that is "fA-cofini" while M/fM ≅ (B/gB)^{(ℕ)} is not.
- **Checked.** The computation (c_{n+1}) and the regularity needed in (b_{n+1}), which holds when B is a domain.
- **Link (mine).** It bears on Hartshorne's cofiniteness question, whose letter of 4.8.1969 is in cote 37 (unread).

### 18. Artin's theorems on cd and real fields (31/019-023) — SA12-44
**Theorem 1 and Corollaries 1-3**, with his margin "suffit-il de degré de transcendance fini ??".

**Corrections:**
- cd(X_ℚ) ≤ 2 dim X_ℚ + **2**. The ink has 2; the transcription has 1 (F32, decided in sweep 2).
- "cd(X) < 2 dim X + 1" is his slip for ≤.

**The Corollary of 31/023.** A noetherian local domain A has cd_r(K) ≥ cd_r(k) + dim A, except possibly:
- (a) r = char K > 0;
- (b) r = 2 with an orderable residue field.

His margin example ℝ[x,y]/(x² + y²) was computed: cd 1 < ∞. So exception (b) is needed. "Corps réel coulant(?)" is probably "clos" (not checked on the scan). His margin "cette restriction est-elle inutile ???" (the regular case) is open.

### 19. Cartan's lemma; SGA 2 leaves (31/024-033) — SA12-45, SA12-46
- **Cartan's lemma** for sites (31/025-027) was checked. In the H̄-variant (31/029-031), the boundary n / n+1 stays a reading question.
- **The SGA 2 typescript** (Th. 2.1-2.4, the condition (Lef), Remarques 5.10) carries his instruction to correct EGA 0_III 13.7.7, p. 78: delete three phrases (31/028).

### 20. π₁ of an orbit space (31/035-039) — SA12-47
- **The page.** Armstrong's theorem for simplicial sets, on ENS paper, in a hand not identified.
- **Lemma 3 (31/038) is false as stated.** "g transforme tout simplexe en un simplexe disjoint" fails for an edge [x, gx], and the claim is not needed.
- **Checked.** Th. 2 (transfer) was re-proved; Th. 3 (torsion of π_i) was checked.

### 21. Trace and inertia; the local norm criterion (31/042-045) — SA12-48
- **Checked.** The equivalences (trace onto, Tate cohomology vanishing) and the tame corollary.
- **The question.** H¹(G,O*) → H¹(G_i,(O/m)*) is bijective in the tame case (checked); the wild case and GL(n) are open.
- **Reading.** "Doute(?)" on 31/044 is probably "Donc" (not checked on the scan).

### 22. cd of a field for algebraic groups; Tsen (31/047-052) — SA12-49, SA12-50
- **The page.** The five equivalent conditions.
- **The unipotent step in characteristic p (31/049).** It argues "H¹(k,GL(n)) = 0", which does not suffice, since Aut(G_a^n) contains the additive polynomials. The conclusion still holds over perfect k, where unipotent groups split.
- **Unwritten.** The arbitrary-field branch is not written.
- **The rest.** Tsen and the transcendence-degree bound are standard.

### 23. Injective sheaves restricted to closed subsets (31/054-062) — SA12-38
- **His answer is "Réponse négative".** Example 4 (two curves meeting in two points) was checked.
- **The Proposition** (H¹(U,F) = 0 for all open U ⇒ all H^i vanish) was re-proved.

### 24. "cd des affines": the φ-criterion and a general bound (31/063-071) — SA12-38
- **The Lemma of 31/067-068** was checked through the Leray spectral sequence. The page's "p − q ≥ φ(x)" must be p + q.
- **The Corollary of 31/070** is cd_ℓ(X) ≤ φ(X), under the hypothesis cd_ℓ K_{Y,ȳ} ≤ dim O_{Y,ȳ}. He writes of that hypothesis: "probablement tjrs. le cas, du moins si X est 'bon'" (Gabber's bound for quasi-excellent rings, locator unverified).
- **His henselian question (31/070, margin).** Is cd_ℓ K ≥ dim A + cd_ℓ k for A henselian local integral with cd_ℓ k < ∞?

### 25. Artin's affine Lefschetz in his own sequence (31/074-083) — SA12-39
- **His sequence.** He proves Th. 2_n (cd_ℓ (Spec A)_f ≤ n for A strictly local of dimension n) for rings essentially of finite type over a field or a ring of dimension ≤ 1.
- **The open "Th" of 31/080.** X affine of finite type over a strictly local Y: is cd_ℓ(X) ≤ sup(dim X₀, dim X' + 1)?
  - X₀ is the closed fibre and X' = X ×_Y (Y − {m}).
  - In the non-affine variant the bound is sup(2 dim X₀, 2 dim X' + 1).
  - The induction of 31/081 breaks off.
- **The question of 31/082.** For X noetherian affine with ℓ prime to the residue characteristics, is cd_ℓ(X) ≤ n := sup_x [cd_ℓ k(x) + dim O_{X,x}]? And is n the sup over the affine opens?
  - His refutation, "faux déjà pour l'anneau des entiers d'un corps de nbres … cd(X) = 3", does not satisfy his own hypothesis on ℓ. For ℓ invertible, Spec O_K[1/ℓ] has cd_ℓ 2 = n.
  - So the question is open.
- **31/083.** cd_ℓ(X) ≤ dim X + 1 for affine X of finite type over ℤ. It agrees with the question.

### 26. His conjectures on the cohomology of affine schemes (31/085-087) — SA12-39
X is a "bon" affine integral scheme with generic point x.
- **1°.** If ℓ is invertible on X, then cd_ℓ(X) ≤ cd_ℓ(k(x)). His margin asks: "et cela devient une égalité pour les ouverts assez petits ?"
- **2°.** If ℓ is neither invertible nor nilpotent, then cd_ℓ(X) ≤ sup(cd_ℓ k(x), δ(V(ℓ)) + 3), with ℓ^{δ(k)} = [k : k^ℓ], δ(Z) the sup over the maximal points of Z.
- **3° (unnumbered).** If some prime ℓ' is invertible on X, then cd_ℓ(X) ≤ cd_ℓ(k(x)) for every ℓ.
- **4°.** A is a good henselian local integral ring with char K = 0, and U an affine open of Spec A. Then cd_ℓ(U) ≤ dim A + δ(k) + cd_ℓ(k).
- **31/087.** "Pour les bons anneaux locaux henséliens de car. résiduelle nulle, tout est vérifié grâce à Artin."

**Checked on test cases.**
- 1° holds for:
  - affine varieties over algebraically closed and finite fields;
  - Spec O_K[1/ℓ];
  - strictly local rings.
- 2° and 3° fit Artin-Verdier exactly:
  - Spec O_K has cd 3 = 0 + 3;
  - every proper open of Spec O_K has cd 2 = cd K (computation, check event of 31/085).

**Status: open on the pages.** These are the main research questions of the topic (RESEARCH_PACKAGES.md).

### 27. Lefschetz for hyperplane sections; the specialization theorem (31/090-101) — SA12-40
- **Lefschetz (31/090-091).** Checked through the Gysin sequence: surjective for i ≥ n+1, bijective for i ≥ n+2.
- **The "Théorème de Spécialisation" (31/092-099).** Smooth morphisms are locally 1-aspherical for groups prime to the residue characteristics. Lemma 3 was checked through Abhyankar.
- **The applications.** Smooth base change, invariance under extension of separably closed fields, relative purity.
- **Open (his, 31/101).** Local constancy of R^i h_* G for G given only on the complement V of a divisor: "Le Pb. ne semble pas facile … wild ramification".

## How it connects
- **Cote 29.** It is the working file behind SGA 1 X and XIII, and LNM 208: the tame π₁, the specialization theorems, finiteness. Behind the 1959 letter it leads to Nori's fundamental group scheme; behind 29/164-172, to the pro-étale π₁.
- **Cote 31.** It is the working file behind SGA 4 X (cd of fields and schemes, Artin's theorems), SGA 4 XIV-XVI (affine Lefschetz, specialization) and SGA 2 (Lefschetz conditions). His conjectures of 31/085 point to Gabber's affine Lefschetz theorem and to the p-dimension of fields (Gabber-Orgogozo 2008; locators unverified).
- **Cross-topic.** SA12-22 (pointed torsors) meets the crystals topics (the "module de Weil" of 29/129-130). SA12-41 (flat cd_p) meets SA15. SA12-16 (inertia extension) meets SGA 7 (SA12-69, cote 35).
- **Wrong, with corrections** (CORRECTIONS.tsv):
  - Proposition 4 (29/139), with its proof (29/141-142);
  - the Chow step (29/066);
  - the char-p step of Pic^τ (29/074-075);
  - the rank formula (29/076);
  - "extension triviale" (29/096);
  - the Picard lifting without properness (29/094);
  - F(I) ≃ C(K,I) without compactness (29/183);
  - the step of 29/187;
  - Lemma 3 of 31/038;
  - the unipotent step of 31/049;
  - the refutation of 31/082;
  - his remark "G5 surabondant" (29/212);
  - the slips of 29/201 (H²(X, μ_n) for H²(S, μ_n)), 29/214 (the multiple-point bound) and 29/217 (ii) ("de Y" for u(X));
  - the readings 29/031, 29/143 (Pro note N143.2 rests on the misreading), 29/149, 29/217 (iii), 31/020, 31/068.
