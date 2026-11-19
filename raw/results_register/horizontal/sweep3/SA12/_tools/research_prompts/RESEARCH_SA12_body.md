# RESEARCH_SA12: Grothendieck's conjectures on the cohomological dimension of affine schemes (cote 31), with Pic^τ in characteristic p, his pointed torsors, and his open questions on π₁ (cote 29)

**To be settled, in four Parts:**
- **A.** His "Conjectures sur la cohomologie des schémas affines" (31/085), his question of 31/082, the open "Th" of 31/080, and the bounds for henselian local domains of 31/023 and 31/070. A.1 is the main question.
- **B.** The birational invariance of Pic^τ (29/071-077) in characteristic p, where his proof has a gap at the infinitesimal step, and his Question on normal models.
- **C.** His pointed torsors of 1959-60: Proposition 4 (29/139-142), false as stated, in its exact true form; the relative representability question of 29/131.
- **D.** His other open questions on the fundamental group (29/061, 29/066, 29/098, 29/116, 29/180, 29/041), the proof missing at 29/207 ("Prouvons que α est essentiellement surjectif"), the axiom G5 of 29/212, and two local questions of cote 31 (31/044, 31/101).

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA12`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a65dbdc241d1a129a, the lead of this topic in sweep 3 of our horizontal reading, on 19 Nov 2026, at the word of the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA12_study.zip`: our study of the topic.**
  - `study/STUDY.md`: what his pages contain and establish, item by item: §§1-15B for cote 29, §§16-27 for cote 31. It also lists the stretches not read in sweep 3: cotes 33, 37, 32 and 35. Cotes 29 and 31 were read in full.
  - `study/HUNCHES.md` (H1-H23) and `study/RESEARCH_PACKAGES.md` (the four packages behind Parts A-D).
  - The tables `CHECK_EVENTS.tsv` (106 events), `CORRECTIONS.tsv` (24), `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`, the full readings with their tables:
    - `c29a.md` (cote 29, scans 2-140);
    - `c29b_c31.md` (cote 29, scans 141-217);
    - `c31_lead.md` (cote 31, scans 2-102).
  - `study/sweep2/`: the item map `OBJECTS.tsv` (SA12-1 to SA12-70), `FLAGS.tsv`, `TOPIC_NOTES.md`, and `SA12_scan_readings.md` (ten readings decided on the scan images).
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic), on 18-19 Nov 2026. It was checked as recorded in `CHECK_EVENTS.tsv` and nowhere else.
- **`RESEARCH_SA12_transcriptions.zip`: the AI transcriptions (LaTeX) of the topic's pages, with their notes and doubts.**
  - The Pro packages are MPL_29_049-094, MPL_29_095-140, MPL_29_141-187, MPL_31_002-051, MPL_33_002-049 and MPL_33_050-097, by GPT-6 Astra (ChatGPT Pro mode).
  - The Codex folders:
    - A29-01, C29-01..07, B37-01..05, C32-01, H35-01 and H37-01, by GPT-6 Astra at reasoning effort max in Codex web;
    - K29-01..11 and K31-01..03 (with math notes), by GPT-6.2 Astra at reasoning effort max (ChatGPT Work), as K29-04..08 record.
  - `\scanpage{N}` marks scan N of the cote's PDF; the archive's sheet number is N−1. The transcriptions carry `\unsure{a|b}` marks. The readings decided some readings on the scan images, and `CORRECTIONS.tsv` gives them.
  - Where a step of yours depends on a doubtful reading, say so and treat each reading.
- **`RESEARCH_SA12_broad.zip`: the sweep-3 study files of neighbouring topics,** for the connections: SGA (SA13), Picard (SA14), crystals (SA15), descent (SA17) and EGA (SA23), where they exist.
- No literature is attached. Fetch the sources yourself (list below), preferring the arXiv LaTeX source.

## Where this comes from

**The pages.** Cotes 29 and 31 of the Grothendieck archive at the University of Montpellier, in the section "Séminaire de Géométrie Algébrique".

**Cote 29 (213 transcribed pages)** is his working file on the fundamental group, from 1959 to 1969:
- the letter to Serre of 1959 on the "vrai" fundamental group (pointed torsors under finite group schemes, before Nori);
- the "Compléments SGA 1960";
- the 1967 correspondence with J. P. Murre on tame ramification, with the typescript "Données de ramification" (the genesis of Grothendieck-Murre, LNM 208);
- his comments on Murre's 1969 draft;
- the formal tame π₁ along a divisor;
- "Finitudes (Pbs et conjectures)";
- "π₁ et Pic^τ birationnels";
- Bertini and inertia, notes for SGA 7.

**Cote 31 (93 pages)** is his working file on cohomological dimension:
- the flat cd_p of fields of characteristic p;
- M. Artin's theorems on cd and real fields;
- Cartan's lemma;
- "cd des affines" (17 pages), with his sequence of theorems on affine vanishing;
- the "Conjectures sur la cohomologie des schémas affines";
- Lefschetz for hyperplane sections;
- the "Théorème de Spécialisation" (local 1-asphericity of smooth morphisms).

Both cotes carry reused typescripts (SGA 2, SGA 3, EGA, Bourbaki-type rédactions), identified in the study and not to be studied.

**Our reading of them.** Sweep 3 (19 Nov 2026) read 306 of the topic's 469 transcribed pages in full and worked them through: all of cotes 29 and 31. Cote 29, scans 2-217, was read by two readers; cote 31, scans 2-102, by the lead. All three are Claude Opus 5.5 at effort max. Sweeps 1-2 (18 Nov) placed every note entry and decided ten readings on the scan images.

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of some of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages. We know of no published study of cote 31's conjectures; check this.

## Results this prompt builds on (status on 19 Nov 2026)

Each result names the check events of `CHECK_EVENTS.tsv` (by the page in the id column). Recheck every result you use (Rules of proof, 7).

**Cote 31.**
1. **The refutation on 31/082 does not apply.** His "Mais c'est faux déjà pour l'anneau des entiers d'un corps de nbres … n = 2 … cd(X) = 3 !" does not satisfy his own hypothesis that ℓ is prime to the residue characteristics.
   - For ℓ invertible the test is U = Spec O_K[1/ℓ], K totally imaginary. There n = 2 and cd_ℓ(U) = 2 (literature, locator unverified).
   - The question of 31/082 is therefore open. Computation, refuted with the refined statement, check event at 31:82.
2. **Conjectures 2° and 3° of 31/085 fit Artin-Verdier exactly** (computation, 31:85).
   - Spec O_K (K totally imaginary) has cd 3 for all torsion sheaves, and 3 = δ(V(ℓ)) + 3.
   - Every proper open U of Spec O_K has H³(U,F) = 0 for every torsion constructible F, because ⊕_{v∉U} H²(K_v,F) → H³_c(U,F) is onto by duality. So cd(U) = 2 = cd K.
3. **Conjecture 1° holds in the test cases** (computations recorded in readings/c31_lead.md item 14):
   - affine varieties over algebraically closed and finite fields;
   - Spec O_K[1/ℓ];
   - strictly local rings.
4. **The Lemma of 31/067-068** (cd_ℓ bounded by a function φ satisfying his conditions (a), (b)) is correct, with "p + q ≥ φ(x)" in place of the page's "p − q" (targeted proof check, 31:68). The Corollary of 31/070 is therefore proved on the page, modulo its hypothesis cd_ℓ K_{Y,ȳ} ≤ dim O_{Y,ȳ}.
5. **Lemma 1 of 31/074-075** (2'_{n+1} ⇒ 1_n) was checked (31:74-75). His Th. 2_n is proved on his pages for rings essentially of finite type over a field or over a noetherian ring of dimension ≤ 1.
6. **The Corollary of 31/023.** His marginal example A = ℝ[x,y]/(x² + y²), localized, gives K = ℂ(x), cd₂ K = 1 < cd₂ ℝ + dim A (computation, 31:23). So exception (b) occurs.
7. **31/020: cd(X_ℚ) ≤ 2 dim X_ℚ + 2** (ink, decided on the scan in sweep 2; the transcription has + 1).
8. **31/049.** The reason "H¹(k, GL(n)) = 0" does not give G ≅ G_a^n over k in characteristic p. The conclusion holds over perfect k (refuted with the refined statement, 31:49).
9. **31/038.** Lemma 3 ("g transforme tout simplexe en un simplexe disjoint") is false as stated and not needed (refuted, 31:38).
10. **31/044.** H¹(G,O*) → H¹(G_i,(O/m)*) is bijective for a tame, totally ramified extension of a DVR (computation, 31:44).
11. **31/090-091** (Lefschetz) and **31/096-097** (Lemma 3 by Abhyankar) were checked (31:90-91, 31:96-97).

**Cote 29.**
12. **Pic^τ (29/071-075),** checked step by step (check events at 29:71-75).
    - The monomorphism, the bijection on points (negativity lemma) and H¹(Y,O) ≅ H¹(X,O) are proved on the page without resolution:
      - in characteristic p, by the F-bijective/F-nilpotent split;
      - in characteristic 0, by reduction mod p.
    - The final step "closed immersion, bijective, iso on tangent spaces ⇒ iso" is false for non-smooth group schemes (α_p ⊂ α_{p²}). The theorem is proved in characteristic 0 and has a gap in characteristic p.
    - The rank formula of 29/076 needs l ≠ p (a supersingular elliptic curve).
13. **Proposition 4 (29/139),** "si α est minimal, u ↦ u_*(α) est injective", is false as stated.
    - The counterexample is the cusp A = k[x,y]/(y^p − x^{p+1}), with α the class of z^p = x in H¹(A, α_p), u = 0 and v = [x] (re-derived in full, 29:139).
    - Reader B (29:141-142): in the proof as written minimality is idle. The diagonal claim is equivalent to u = v, and the final "unicité" fails without minimality: take G = ℤ/2 constant, α trivial.
    - Proposition 4 holds for étale groups, and for u, v whose equalizer is admissible, which covers constant groups (re-proved). Otherwise it is open. Given Prop. 4, the pro-object π₁^C of 29/143 is formal (29:143).
    - 29/143, Exemple II, reads on the ink "ce qui semble raisonnable surtout si k sep. clos". The Pro reading "rend vraisemblt inutiles les hyp." is a misreading, and Pro note N143.2 rests on it (reading decided on the scan image, 29:143).
14. **29/066, the Chow step** ("Z' → Z propre surjectif ⇒ Y' de codim ≥ 2") is false for proper maps (Bl_p P² → P²) and true for finite maps.
    - The theorem (π₁ of a proper scheme minus codimension ≥ 2 is of finite type) is proved for projective Z.
    - 29/070 (the birational π₁ is of finite type) survives in full (29:66, 29:70).
15. **29/070.** His question whether π₁(U;Ω) → π₁(K/k;Ω) is bijective, for U the regular locus of a normal model, has the answer no: X = (P¹ × P¹)/±1 (29:70).
16. **29/094.** The Picard lifting is false without properness and true for X₀ proper over a field (re-proved, 29:94).
17. **29/096.** "Extension triviale" is false for a complete curve of genus ≥ 1 with nonzero self-intersection and D'₀ = ∅ (29:96).
18. **29/048.** Lemma 1 needs "réduit" (the ink; a counterexample with a non-reduced fibre, 29:48).
19. **29/149.** "[par exemple fini / S' étale sur S]" (ink): "fini" is needed (29:149).
20. **29/183.** "Ces conditions sont néc et suffisantes" is false without compactness (K = ℕ^ℕ, φ(x) = x_{x₀+1}). It is true when every π₀ᵢ is finite (29:183).
21. **29/187.** The proof step "il y a un X'-morphisme X̃' → X''" fails. The proposition holds by Zariski's main theorem on the normalization (29:187).
22. **29/180.** For S' → S fpqc, every descent datum on G_{S'} is effective by Gabber's descent for ind-quasi-affine morphisms (Stacks 0APK, locator unverified). The proper surjective case is open; Rydh's theorem on effective descent of étale morphisms along universally subtrusive morphisms may settle it (29:179-180).
23. **29/212, "Remarque : il se pourrait que G5 soit surabondant", is refuted** (refuted with the refined statement, 29:212).
    - The countable ℤ-sets satisfy G0-G4 and fail G5: Z × Z ≅ ⊔_ℤ Z contains Z × [1, N+1] as a summand for every N.
    - They also fail G5', his replacement: an exact F with F(pt) = pt would make the translation act on the finite F(Z) with some order m, while the equalizer of τ^m and id is ∅.
    - So B(ii) of 29/209-212 needs G5 or G5'.
24. **29/202-207.** For a generating cartesian φ: C → 𝓡, C locally filtering and φ fully faithful, the functor α of 29/204 is faithful and full: the page proves it, checked at 29:205-207.
    - The page then stops at "Prouvons que α est essentiellement surjectif." (ms. p. 16). The next leaf, 208, is blank (decided on the scan), and 209 starts a new sequence.
25. **29/199-201.** Ex. 2 of the Kummer data is the μ_n-gerbe of n-th roots of O(D_i), with class the Kummer coboundary of [O(D_i)] (29:201). His "H²(X, μ_n)" is a slip for H²(S, μ_n).
26. **29/217.** The Proposition on exact functors between multi-Galois categories was re-proved (29:217).
    - In (ii) the ink reads "ss-objets de Y", his slip for u(X).
    - In (iii) the ink reads "(cf (ii))".
27. **29/191-198 and 29/213-215** were checked: the topology of r-surjective families, Prop. 2, Prop. 6 with its Corollary (homomorphisms of ramification data are fully faithful), and the degree conditions ⓪-③ ⇒ A(iii).

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1 (H1).** Conjecture 1° may follow, for quasi-excellent X, from two inputs and a fibration argument:
  - Gabber's affine Lefschetz theorem (Illusie-Laszlo-Orgogozo, Travaux de Gabber, Exp. XV);
  - his bound for fields (Exp. XVIII-A), with Serre's formula cd_ℓ(k') = cd_ℓ(k) + tr.deg (Cohomologie galoisienne II.4.2).

  The step to check is the passage from strictly local bases to arbitrary ones, through Hochschild-Serre on strict localizations. Excellence may be needed.
- **L2 (H2).** 1° implies the bound of 31/082, since the generic point alone gives n ≥ cd_ℓ k(x). That n is attained by an affine open may follow from local purity at a regular point.
- **L3 (H3).** 2° and 4° look like the scheme forms of the field bounds of Gabber-Orgogozo, "Sur la p-dimension des corps" (Invent. Math. 174, 2008). The method may be Gabber's affine Lefschetz for p-torsion, through the comparison for henselian pairs.
- **L4 (H4).** Equality on small opens. For A = k{x,y} strictly henselian, (x) ∪ (y) ≠ 0 in H²(Spec A[1/xy], μ_ℓ^{⊗2}). For Spec A[1/x], the sheaves we tried give only degree 1. Hunch: complements of normal-crossings divisors with dim A branches at the closed point attain cd_ℓ K. See also Achinger's K(π,1) neighbourhoods.
- **L5 (H5, H6).** 31/070 (i) is Gabber's theorem for quasi-excellent strictly henselian local domains. The henselian lower bound may hold without regularity, through normalization and a regular alteration of degree prime to ℓ (Gabber).
- **L6 (H10).** Pic^τ: the theorem holds when H²(Y,O_Y) → H²(X,O_X) is injective. Then the deformation functors of the trivial bundle agree: bijective on tangent spaces, injective on obstruction spaces.
  - For X smooth, Rf_*O_X = O_Y in every characteristic (Chatzistamatiou-Rülling).
  - In dimension 2, X normal between a resolution and the regular Y has only sandwiched, hence rational, singularities, so R¹f_*O_X = 0. Check this, and its characteristic p form.
  - A counterexample would need dimension ≥ 3, R¹f_*O_X ≠ 0 and Pic^τ_Y non-reduced.
- **L7 (H12, H19).** Proposition 4: the weight lies on the uniqueness of pointed maps from a minimal P. In Nori's setting (Hom over k; S proper, reduced, connected, H⁰(S,O_S) = k) pointed torsors are rigid, and Prop. 4 should hold there. The candidates for a true general form:
  - minimality among all closed subgroup schemes, flat or not;
  - normal S;
  - morphisms over the base field only.
- **L8 (H13, H14, H18, H7, H9).**
  - π₁(Z − Y), Z proper non-projective in characteristic p, is probably of finite type.
  - Π₂^t(Spec ℤ − S) is governed by A. Schmidt's K(π,1) results.
  - Effective descent along proper surjective maps (29/180) probably holds: Rydh's theorem, if the non-quasi-compact G_{S'} is within its hypotheses. The test case, the normalization of a nodal curve, is effective.
  - 31/044 probably fails in the wild case.
  - 31/101 is governed by Swan conductors (Deligne-Laumon semicontinuity).

- **L9 (H20).** Ramification data are the finite étale sites of root stacks: Ex. 2 of 29/201 is the gerbe of n-th roots of O(D_i), and the tame Kummer data are the theory of LNM 208 and the later logarithmic Kummer-étale theory. The missing essential surjectivity of 29/207 should follow by effective descent of finite étale covers along Kummer covers, with C locally filtering.
- **L10 (H23).** The countable ℤ-sets fail G5 because their Hom sets are infinite. Finiteness of Hom between connected objects is the candidate for the condition that gives G5 from G0-G4.

## What the outcome must be

{{OUTCOME}}

## Parts

**Conventions.** cd_ℓ(X) is the étale ℓ-cohomological dimension: the least n such that H^q(X_ét, F) = 0 for every q > n and every ℓ-torsion sheaf F. For a field it is cd_ℓ of its absolute Galois group.

"Bon" is his word, undefined on these pages. In every item of Part A, decide the statement first for quasi-excellent schemes, then for noetherian schemes without that hypothesis, with a counterexample where it fails.

δ is his p-degree: for a field k of characteristic ℓ, ℓ^{δ(k)} = [k : k^ℓ]. For a scheme Z of characteristic ℓ, δ(Z) is the sup of δ(k(z)) over the maximal points z of Z.

**A. The cohomological dimension of affine schemes. The main question is A.1.**

- **A.1 (Conjecture 1°, 31/085).** X is an affine noetherian integral scheme with generic point x, and ℓ is a prime invertible on X. Prove or refute: cd_ℓ(X) ≤ cd_ℓ(k(x)).
- **A.2 (his margin on 1°: "et cela devient une égalité pour les ouverts assez petits ?").** For X as in A.1 with cd_ℓ(k(x)) < ∞: does every nonempty open of X contain a nonempty affine open U with cd_ℓ(U') = cd_ℓ(k(x)) for every nonempty affine open U' ⊂ U? Prove or refute.
- **A.3 (the unnumbered conjecture between 2° and 4° on 31/085).** If some prime ℓ' is invertible on X, is cd_ℓ(X) ≤ cd_ℓ(k(x)) for every prime ℓ, including the residue characteristics? Prove or refute.
- **A.4 (Conjecture 2°).** If ℓ is neither invertible nor nilpotent on X, is cd_ℓ(X) ≤ sup(cd_ℓ k(x), δ(V(ℓ)) + 3)? Prove or refute.
  - Also decide his cancelled margin question: is cd_ℓ(k(x)) ≥ δ(V(ℓ)) + 1 always?
- **A.5 (Conjecture 4°, and 31/087).** A is a henselian local integral ring with fraction field K of characteristic 0 and residue field k, and U is an affine open of Spec A. Is cd_ℓ(U) ≤ dim A + δ(k) + cd_ℓ(k) for every prime ℓ? Here δ(k) = 0 unless ℓ = char k. Prove or refute.
  - Then derive his N.B. of 31/087, "Pour les bons anneaux locaux henséliens de car. résiduelle nulle, tout est vérifié grâce à Artin", from Artin's theorems, with exact locators.
- **A.6 (31/082).** X is noetherian affine, ℓ is prime to every residue characteristic of X, and n = sup_{x∈X} [cd_ℓ k(x) + dim O_{X,x}]. Prove or refute each:
  - (i) cd_ℓ(X) ≤ n;
  - (ii) n is the sup of cd_ℓ(U) over the affine opens U of X.

  Check our result 1 (his number-ring refutation does not meet his hypothesis) and say plainly whether it stands.
- **A.7 (the "Th" of 31/080).** A is strictly local noetherian, Y = Spec A with closed point m, X is of finite type over Y, X₀ = X ×_Y {m}, X' = X ×_Y (Y − {m}), and ℓ is prime to the residue characteristic. Prove or refute each:
  - (i) for X affine, cd_ℓ(X) ≤ sup(dim X₀, dim X' + 1);
  - (ii) for X not affine, cd_ℓ(X) ≤ sup(2 dim X₀, 2 dim X' + 1);
  - (iii) his N.B.s for X integral dominating Y, with d the dimension of the generic fibre: cd_ℓ(X) ≤ dim Y + d in the affine case, and cd_ℓ(X) ≤ 2 dim Y − 1 + 2d otherwise (dim Y ≠ 0).

  His pages prove (i) for rings essentially of finite type over a noetherian ring of dimension ≤ 1, by an induction that breaks off on 31/081. Complete it in general or refute it.
- **A.8 (31/070).** Prove or refute each:
  - (i) "probablement tjrs. le cas, du moins si X est 'bon'": for every noetherian strictly henselian local domain B with fraction field K and ℓ invertible in B, cd_ℓ(K) ≤ dim B;
  - (ii) his margin question: for A a noetherian henselian local domain with residue field k, cd_ℓ(k) < ∞ and ℓ ≠ char K, is cd_ℓ(K) ≥ dim A + cd_ℓ(k)?
- **A.9 (31/023).** Take the Corollary of 31/023. A is a noetherian local domain and r a prime: cd_r(K) ≥ cd_r(k) + dim A, except possibly
  - (a) r = char K > 0, and
  - (b) r = 2 with some κ(x) orderable and cd₂ κ(x)(√−1) finite.

  Prove the Corollary from Artin's theorems as the page intends. Then settle three things:
  - his N.B. that for A catenary and universally japanese, exception (b) can occur only when k itself is real closed (the transcription reads "corps réel coulant(?)"; determine the condition that makes the statement true);
  - his claim that for A regular the inequality holds outside case (a);
  - his margin "cette restriction est-elle inutile ???", read both ways: is regularity needed, and is the exclusion of case (a) needed? For each, give a proof or a counterexample.

**B. Birational invariance of Pic^τ in characteristic p (29/071-077).**

- **B.1.** k is algebraically closed of characteristic p > 0. f: X → Y is a dominant birational morphism of integral proper k-schemes, X normal and Y regular. Prove or refute: f^*: Pic^τ_{Y/k} → Pic^τ_{X/k} is an isomorphism of group schemes.
  - Then decide it under each of his margin variants: X normal "sur k" (geometrically normal), Y projective, and Y smooth over k ("Y lisse sur k (!)").
  - Begin from the page's proof (study §6, readings/c29a.md, 29/071-077), which settles everything except the infinitesimal step.
- **B.2 (his Question, 29/075).** For K/k finitely generated of characteristic p, is dim H¹(X, O_X) bounded as X runs over the proper models of K normal over k? Equivalently, by his N.B., is the inductive system of the Pic^τ over these models essentially constant? Prove or refute.
- **B.3 (29/077).** Prove the bound dim Pic_{X/k} ≤ n(K/k) for every proper model X of K normal over k by a proof that does not use the fundamental group, as he asks ("Y-a-t-il une démonstration … n'utilisant pas la théorie du groupe fondamental"). Correct the rank formula to l ≠ p where it is used.

**C. Pointed torsors and the fundamental group scheme (29/124-143).**

- **C.1 (Proposition 4).** Take the setting of 29/141.
  - S is connected, reduced and noetherian, with a point a.
  - C is a category of finite flat S-groups stable under products, kernels of pairs and images.
  - Z(G) is the set of classes of a-pointed torsors, and minimality is as on 29/141.

  Determine the exact class of (S, C, allowed morphisms) for which Proposition 4 holds, with a proof that it is the whole answer. In particular, decide each of these, each with a proof or a counterexample:
  - (i) S normal, C all finite flat S-groups, all S-group morphisms;
  - (ii) S reduced and not normal, C = {G₀ ×_k S : G₀ a finite k-group}, morphisms defined over k;
  - (iii) the same C with all S-group morphisms. The cusp refutes this for one S; decide for every non-normal S.

  Then decide whether the pro-object π₁^C of 29/143, in case (ii), is Nori's fundamental group scheme when S is of finite type over a perfect field k with a in S(k).
- **C.2 (29/131).** f: X → S is proper flat with a section, f_*O_X = O_S universally, and G is a finite étale S-group. Is the functor T ↦ {pointed G_T-torsors on X_T} representable by an étale, quasi-finite, separated S-scheme? Decide it. Then decide the same for G finite flat, not étale, with the representing object you find.

**D. His other open questions on the fundamental group, and two local questions of cote 31.** Each is to be proved or refuted.

- **D.1 (29/061).** X is normal and complete over an algebraically closed field, and Y ⊂ X is closed. Is π₁(X − Y), modulo the closed normal subgroup generated by the wild inertia groups at the codimension-1 components of Y (in the normalization), topologically of finite type?
- **D.2 (29/066).**
  - (i) His margin question: X is connected and normal of finite type over an algebraically closed field, and Y ⊂ X closed of codimension ≥ 2. Is Ker(π₁(X − Y) → π₁(X)) topologically of finite type?
  - (ii) The case his proof leaves: is π₁(Z − Y) topologically of finite type for Z proper and not projective, of characteristic p, with Y of codimension ≥ 2?
- **D.3 (29/098, "Mais qu'est Π₂^t(X₀/D'₀) ???").** Determine Π₂^t(Spec ℤ − S) for every finite set of primes S. More generally, determine it for X₀ = Spec O_K − S. Decide for which (K, S) these schemes are of type K(π,1) for tame coefficients prime to the residue characteristics.
- **D.4 (29/116).** char k = 2, X is of odd dimension, and the Lefschetz pencil is general but not generic. Are the vanishing cycles conjugate under π₁(D − D^v)?
- **D.5 (29/180).** S, S' are noetherian and S' → S is proper and surjective, not flat. Is every descent datum on a constant group G_{S'} effective? Decide also when G is residually finite.
- **D.6 (29/041, 1 b)).** For X of finite type over an algebraically closed field of characteristic p, is π'₁(X) (the maximal prime-to-p quotient) of finite presentation, with no resolution of singularities assumed?
- **D.7 (29/202-207, "Prouvons que α est essentiellement surjectif.").** Take the setting of 29/202-204: a ramification datum (𝓡, r) on S with axioms R1-R4 (29/191-192), a generating cartesian φ: C → 𝓡 with C locally filtering and φ fully faithful, and the functor α of (*) on 29/204. Prove that α is essentially surjective, so that α is an equivalence as he claims; or refute it with a counterexample, and prove the strongest true statement in its place.
  - Then decide Prop. 5, left unwritten on 29/197.
  - Also decide whether the ramification data of Ex. 2 (29/199-201) are equivalent to the finite étale sites of the root stacks of the D_i.
- **D.8 (29/209-212, G5).** Recheck our refutation of "G5 surabondant" (result 23). Then determine a condition added to G0-G4 that implies G5, with a proof, and a counterexample showing that it cannot be weakened to G0-G4 alone. Test finiteness of Hom between connected objects first (lead L10).
- **D.9 (31/044).** O is semi-local with a finite group G of automorphisms, and G_i is the inertia as on 31/044. Is H¹(G, O*) → H¹(G_i, (O/m)*) bijective when the order of G_i is divisible by the residue characteristic? And his question: "Qu'en est-il dans le cas des Gl(n, O) au lieu de O* ?"
- **D.10 (31/101).** f: X → S is proper and smooth, Y ⊂ X is a relative divisor with normal crossings over S, V = X − Y, h: V → S, and G is a locally constant constructible sheaf on V of order invertible on S. Determine a necessary and sufficient condition for the R^i h_* G to be locally constant, with a proof that it is the whole answer.
  - First do this for X/S a relative curve, then in every relative dimension.
  - Decide whether tame ramification of G along Y is a sufficient condition.

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

Locators are unverified; check each.
- **SGA.**
  - SGA 1 (exposés V, IX, X, XIII);
  - SGA 2 (exposés X-XIII);
  - SGA 3 (exposé X §6);
  - SGA 4 (exposés IV, V, X, XIV, XV, XVI, XVIII);
  - SGA 4½ (Arcata; Th. finitude);
  - SGA 7 (exposés I, XIII, XV-XVIII).
- **Fundamental groups.**
  - A. Grothendieck, J. P. Murre, The tame fundamental group of a formal neighbourhood of a divisor with normal crossings on a scheme, LNM 208 (1971).
  - M. Nori, On the representations of the fundamental group (Compositio 1976) and The fundamental group-scheme (Proc. Indian Acad. Sci. 1982).
  - M. Antei, M. Emsalem, C. Gasbarri, Sur l'existence du schéma en groupes fondamental (and the related work on bases of dimension 1).
- **Cohomological dimension.**
  - L. Illusie, Y. Laszlo, F. Orgogozo (eds.), Travaux de Gabber sur l'uniformisation locale et la cohomologie étale des schémas quasi-excellents, Astérisque 363-364 (2014), arXiv:1207.3648. Exposés XV and XVIII-A above all.
  - O. Gabber, F. Orgogozo, Sur la p-dimension des corps, Invent. Math. 174 (2008).
  - J.-P. Serre, Cohomologie galoisienne.
  - J. S. Milne, Arithmetic Duality Theorems, chapter II.
  - A. Schmidt, his papers on K(π,1) arithmetic schemes (Crelle, Duke).
  - P. Achinger, K(π,1)-neighborhoods and comparison theorems (Compositio 2015) and Wild ramification and K(π,1) spaces (Invent. Math. 2017).
- **Other.**
  - A. Chatzistamatiou, K. Rülling, Higher direct images of the structure sheaf in positive characteristic (Algebra Number Theory 2011).
  - J. Kollár, S. Mori, Birational geometry of algebraic varieties.
  - F. Orgogozo, Altérations et groupe fondamental premier à p (Bull. SMF 2003).
  - H. Esnault, M. Schusterman, V. Srinivas, on finite presentation of the tame fundamental group.
  - G. Laumon, Semi-continuité du conducteur de Swan (d'après P. Deligne) (Astérisque 82-83).
  - R. Hartshorne, Affine duality and cofiniteness (Invent. Math. 1970).
  - B. Bhatt, P. Scholze, The pro-étale topology for schemes.
  - D. Rydh, Submersions and effective descent of étale morphisms, Bull. SMF 138 (2010).
  - N. Borne, A. Vistoli, Parabolic sheaves on logarithmic schemes (Adv. Math. 2012), and L. Illusie, An overview of the work of K. Fujiwara, K. Kato and C. Nakayama on logarithmic étale cohomology (Astérisque 279, 2002).
  - The Stacks Project.

{{RULES}}

{{DELIVER}}
