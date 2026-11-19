# Cote 150, scans 17-30: integration into the SA10 study

Claude Opus 5.5 at effort max, sub-agent of a6d42bf6fe2b0d8a8 (reading 150_017-030), horizontal sweep 3, 19 Nov 2026.

## STUDY

**Cote 150, scans 17-30 (manuscript pages 3-9 and the §7 sheet), read in full, with the second pass of 17 Nov as
text.** On 012-016 the conical neighbourhood is the cone C(f) of f = 0·(−): Ṫ → Y, a mapping cylinder with its
[0,1]-action.

**The two compatibility notions and equisingularity (017-020).**
- Compatibility of a closed part with a collar is conical compatibility plus purity, T'∩Y = 0·Ṫ' (re-proved).
- Equisingularity is strengthened from separate local triviality to that of the whole family. A crossing pair of
  sections shows why.
- The alternative (14) and strict equisingularity after shrinking are re-proved.
- The Proposition of 020 is false for merely compatible parts; it holds for parts pure in the sense of the 018 margin.

**Germs and the découpage cônique (022-024).**
- The germ relation is an equivalence; his margin gives the step for transitivity.
- The Theorem of 023, an equivalence for isomorphisms between conical germs and data (X̃^*, Ẋ, ℰ, Y, f), is re-proved.
  Its inverse is the **deployment** of X along Y, the real blow-up in the conical setting: Y is replaced by the
  collared link Ṫ. This is the folder's second title.
- The closed-subset Corollary is re-proved; it keeps the extra base points in Y'.

**Collars against cones, and corners (024-029).**
- The product Condition of 025 is re-proved, with one precision: his b) is what stops the cone from rescaling the
  collar coordinate.
- Transversal families of collars, E_J ≃ B_J × I^J (027, canonical), are the compatible collars of a manifold with
  corners.
- Precylindrical stratifications (028) are its face stratifications: bordering faces, transversal collars, Boolean
  intervals. Their local structure is a cube corner (029), checked.
- The infimum claim of 029 holds inside I_{i,j}, where his proof works, and fails read in I. The lens (a disc bounded by
  two arcs meeting at two corners) is precylindrical, satisfies (14) and has no infimum of its two arcs.

**The step of the induction (030).**
- The intersection axiom (14) a) X_i ∩ X_j = ⋃_{α≤i,j} X_α, which he says on 031 he had forgotten, holds; its
  extension to finite intersections is re-proved.
- The germ form of the disjoint-neighbourhood statement needs compactness (a line and an exponentially close curve).

**Slips corrected:** "parties fermées de X" (X^*); Y_i for T̄_i; Ė_J for E_J; X_0 for Ẋ_0; the circular s_k; the
bordering arrows called "verticales"; "k ∈ j".

**Readings decided on the native scan:** Y_i; "globalement" struck; "des récurrences" (021: the boundary datum is
introduced "pour faire des récurrences"); the insertion arrow on 022; Ė_J.

**Open readings:** maximaux|minimaux (028), dans X|des X_i (030), the verb on 025, alors|et (019), 1°|a), σ|F (029).

**EXIT_TOWER (folio 9 = scan 028).**
- A.1 (Boolean intervals only for g = 0 and (1,1)) means that M̄_{g,n}, stratified by isomorphism classes, is not
  precylindrical.
- A.3 (Boolean factorizations of a fixed contraction, and the intersection axiom) means that its deployment is.
- Our register summary of A.1 misstates it (SA10-K150b-13).

## HUNCHES

**H150b-1. Précylindrique means a manifold with embedded corners, and déploiement means the iterated real blow-up
(sharpens H1).**
- The Theorem of 023 is the one-stratum deployment.
- Iterating it stratum by stratum, keeping the boundaries as the cancelled 021 asks ("pour faire des récurrences"),
  should yield a precylindrical stratification. That would be his "déploiement des espaces stratifiés" and the
  1981-82 form of the unzipping of Ayala-Francis-Tanaka.
- Grounds:
  - 023 re-proved;
  - the collars of 027 are those of Jänich's ⟨n⟩-manifolds and Laures's compatible collars;
  - 029's cube corners.
- Literature: K. Jänich, Math. Ann. 176 (1968), 53-76; G. Laures, Trans. Amer. Math. Soc. 352 (2000), 5667-5688; D.
  Ayala, J. Francis, H. L. Tanaka, Adv. Math. 307 (2017), 903-1028. Locators to be checked.
- The gluing theorem of P1 is the inverse operation: gluing back what the deployment cut.

**H150b-2. The flags of 039-043 deploy the index poset (sharpens H3 and H5).**
- When a space fails c) because faces meet themselves or an automorphism identifies two factorizations, as M̄_{g,n}
  does (EXIT_TOWER A.1), indexing by flags or fixed contractions restores Boolean intervals (A.3).
- So the passage to Drap(I) on 039-043 is forced by his own Teichmüller example, as his refusal of infima on 151/54 is.
- To be checked on the next block.

**H150b-3. Relative infima are his consistent position from 1981 to 1986 (sharpens H3).**
- 029 proves the infimum inside I_{i,j}, and its global reading fails for the lens.
- 151/54 rejects global infima as an axiom, and 156-7/14 keeps them for the "polyédral" case only.
- The geometric content is the intersection axiom (14) a), a union over the maximal common lower bounds. It holds for
  M̄_{g,n} (EXIT_TOWER A.3).

**H150b-4. The découpage cônique is the cone-like case of the neighbourhood-germ classification (sharpens H2).**
- Quinn's homotopically stratified sets and Hughes-Taylor-Weinberger-Williams (Topology 39 (2000), 873-919)
  classify neighbourhood germs of a stratum by holink data. His (X̃^*, Ẋ, ℰ, Y, f) is the strict version, with f in
  place of the holink fibration.
- The deployment data are therefore the input of the exit-path picture of 151/32-43 at the level of spaces, before the
  topos is taken.
- Locators to be checked.

## PACKAGES

**P150b-1. The deployment of a conically stratified space (companion to P1 of the SA10 study).**
- **The question:**
  - When does iterating the découpage cônique of 023, keeping the boundaries (021, 030), produce a precylindrical
    stratification (028 a)-c), (14))?
  - What indexes its faces: the poset of strata, its flags (039-043), or the category of strata and incidences?
  - For M̄_{g,n}: is the real oriented blow-up of the boundary a precylindrical stratification once indexed by fixed
    contractions?
- **Why it matters:**
  - it is the folder's programme, its second title;
  - it is the inverse of the gluing theorem of 151/69, which is refuted as stated (P1);
  - it is the geometric input of the stratified homotopy type of 151/32-44.
- **What it rests on:** 150/012-033 (second pass of 17 Nov; read here 017-030); 150/039-043; 151/32-75 (the SA10
  study); EXIT_TOWER A.1-A.3, A.12.
- **Strongest known reduction:**
  - the one-stratum case is the Theorem of 023, re-proved for isomorphisms;
  - corner structure follows from compatible collars and (14) (029, checked);
  - for M̄_{g,n} the fixed-contraction intervals are Boolean (A.3) and the deployed family is locally trivial (A.12);
  - the lens shows that global infima are not to be expected.
- **Material:**
  - the corrected `.tex` of MPL_150_001-043 with the scans;
  - the EXIT_TOWER return;
  - Douady 1961, Jänich 1968, Laures 2000, Ayala-Francis-Tanaka 2017, Quinn 1988, HTWW 2000 (locators to be checked);
  - for M̄_{g,n}, T. Kimura, J. Stasheff, A. Voronov, "On operad structures of moduli spaces and string theory",
    Comm. Math. Phys. 171 (1995), 1-25 (real blow-up along the boundary; locator to be checked).
