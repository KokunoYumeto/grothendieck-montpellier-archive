## STUDY

Scans 085-099 of cote 150 are two pieces of his 1981-82 notes on stratified spaces, sheets 39-46 of his numbering.

**§16 (085-088) builds the deployed side of §15's pro-neighbourhoods.** For a band J:
- Σ_J is X_J^* minus the open tubes of the strata below J (70). It is closed in X, a homotopy model of X_J^* (73), and
  glued from the Σ_j along the Σ_ij (72).
- Its boundary is Σ̇_J (74).
- The tube of Σ_J in a larger band Σ_{I'} is (75)-(76).
- The band pieces Σ^♭_{J,L} = Ṫ ∩ Σ_L have their flag colimit (77)-(78) and the span Σ_J ← Σ^♭_{J,L} → Σ_L (79).

A margin proposes the "éclatés orientés", with Σ_i ⊃ X_i^*. The Remarque of 088 claims that Σ_{J,L} ↪ Σ_L is intrinsic up
to isotopy in tame topology.

**§17 (089-099) is a clean restart.**
- It puts the Alexandrov topology on I (closed = down-sets). Bands are its locally closed parts (= order-convex), with the
  domination J ≺ K.
- It states (Strat 1)-(Strat 5).
- It proves:
  - the open strata partition X;
  - the spectral sequence of the closed cover (89);
  - the criteria (95)-(96) for neighbourhoods of strata to meet.
- It sets out V_i, V_d, V^Z, V_J, V_{J,L}, V_J^L and V_{J_0…J_n} with their union and colimit formulas.

**The reading re-derived 44 steps (SA10-R150g-01 to -44).**
- "Rare" in (Strat 5) means nowhere dense, as on 004. The dense faithful stratifications are exactly the locally finite
  partitions with the frontier condition, I being the closure order (R150g-22 to -27).
- For a chain I, the bands under ≺ are the arrow poset Ar(I) (R150g-19).
- **His "? à vérifier!" on (100) is justified.** Z = {0} ∪ {1/n} in ℝ refutes it, and the same Z refutes (104).
  - Both hold for Z a locally closed union of strata, under control.
  - (110) needs that form; (111), with Z = X_L^*, holds (K150g-08, -11).
- (74)'s second and third lines index the interior seams, not the boundary (K150g-01).
- The parenthetical of (75) is false, as his own margin says (K150g-03).
- (96) ⟸ needs density (K150g-07).
- (103) holds for bands only (K150g-10).

**Corrections (K150g-01 to -16), 16 in all:**
- four refutations or confirmed self-doubts, each with its refined statement;
- three precisions of hypotheses;
- three readings decided by the mathematics;
- three slips;
- one notation proposal (♭ = the trace on the top open stratum);
- one immaterial reading;
- one typesetting error in the 17 Nov second-pass file. 087 l.5 reads "\qquadT", which does not compile; it must be fixed
  in the second-pass folder before any build.

**Open:**
- (100)/(110) in the control-free tame setting;
- the Remarque's isotopy invariance;
- five readings for the native scans:
  - 085 l.52;
  - the 086 margin's subscript;
  - the ♭ glyphs;
  - 085's head line;
  - 088's "le cas équisingulier".

## HUNCHES

**H150g-1. ♭ is one notation, the trace on the top open stratum, on the V-side and on the Σ-side** (new; notation).
- *Grounds:*
  - the 077 margin, V_{ij}^b = V_i ∩ X_j^*;
  - 087's Σ^♭_{J,L} = Ṫ ∩ Σ_L (77);
  - 098's "Suggestion": V^♭_{J,L} for V_J^L = V_J ∩ X_L^*, and V^♭_{i_0…i_n} = V_{i_0…i_n} ∩ X^*_{i_n} (K150g-15).
- *Statement to test:*
  - V^♭_{J,L} ≃ Σ^♭_{J,L} for bands J ≺ L. This is the band form of V_{ij} ≃ Σ_{ij} (R150f-29, 36).
  - With (111) and (78) it gives V_{J,L} ≃ the colimit of the Σ_d over the flags from J to L.
- *Test:*
  - the three glyphs side by side on the native scans of 077, 087 and 098;
  - the statement for a normal-crossings divisor.

**H150g-2. (111) is the band form of "deleted neighbourhood ≃ homotopy link"** (sharpens H150f-2).
- *Grounds:*
  - (111), V_J^L ↪ V_{J,L} for bands J ≺ L, holds because Z = X_L^* is a union of strata (R150g-43).
  - The general (110) needs the refined hypothesis (K150g-08).
  - H150f-2 identifies V_J^L with the homotopy link.
- *Statement to test:* for a homotopically stratified space and bands J ≺ L,
  V_J ∩ V_L ≃ V_J ∩ X_L^* ≃ holink(X_J^* ∪ X_L^*, X_J^*). Literature: F. Quinn, J. Amer. Math. Soc. 1 (1988) (locator
  to be checked).
- *Consequence:*
  - The V_{J_0…J_n} of (112)-(113), over chains J_0 ≺ ⋯ ≺ J_n, are iterated homotopy links.
  - Since i ≤ j ⟺ {i} ≺ {j}, the flag presentation by the V_d is the case of singletons.
  - For a chain I, the indexing poset is Ar(I) (R150g-19).

**H150g-3. The "éclatés orientés" of 085 confirm H150b-1** (sharpens H150b-1).
- *Grounds:*
  - The 085 margin gives Σ_i ⊃ X_i^*, X_J^* = Σ_J ∖ Σ̇_J and X = lim→ Σ_d over Drap(I), as "plus commode".
  - The Σ_i of §14 lies inside X_i^*, the complement of open tubes. The blown-up Σ_i contains X_i^* as its interior. Up
    to collars they are the same manifold with corners.
- *Consequence:*
  - The deployment has two models: inward (§14, §16) and outward (the oriented real blow-up).
  - The outward one is the resolution of a Thom-Mather space by manifolds with corners in the later literature:
    A. Verona (LNM 1102); J.-P. Brasselet, G. Hector and M. Saralegi's "dépliage"; P. Albin, É. Leichtnam, R. Mazzeo and
    P. Piazza. Locators to be checked.
- *Test:* for a normal-crossings divisor, the outward Σ_d should be the real oriented blow-ups, and their colimit over
  Drap(I) should give X back.

**H150g-4. §17's stratifications of type I are continuous maps to I with its Alexandrov topology** (sharpens H150f-3).
- *Grounds:*
  - (82)-(83) are the Alexandrov topology: closed = down-sets (R150g-14).
  - The open strata partition X (R150g-20, -21), so (Strat 1)-(Strat 3) amount to a map φ: X → I with φ^{-1}(↓i) = X_i
    closed and the X_i a locally finite cover.
  - Density and fidelity make I the closure order, with the frontier condition (R150g-27).
- *Consequence:*
  - His "type I" is the I-stratified space of J. Lurie, *Higher Algebra*, App. A (locator to be checked), with local
    finiteness.
  - His bands are the locally closed parts of I, so X_J^* = φ^{-1}(J) is locally closed exactly for bands (R150g-28, -31).
  - The exit-path ∞-category is then the natural receiver of the V-calculus.
- *Test:* do his conical structures (073-076) give Lurie's "conically stratified" condition? That condition is what makes
  the exit paths an ∞-category.

## PACKAGES

**P150g-1, joined to P150f-1 (one cluster, one prompt): the band form of the pro-space model, with the hypotheses that
make it true.**
- *The question:* in P150f-1's setting (Whitney, Thom-Mather or homotopically stratified spaces), prove for bands J ≺ L:
  - (100) and (104) for Z a locally closed union of strata, and (110) from them;
  - (111), V_J^L ≃ V_{J,L};
  - V_J ≃ Σ_J ((73) with (103)) and V_J^L ≃ Σ^♭_{J,L} (H150g-1);
  - (72); (78) with L = I'∖J; (74) in its corrected form (K150g-01);
  - the colimit formulas (101), (108) and (113) for the band presentation V_{J_0…J_n};
  - the Remarque of 088: Σ_{J,L} ↪ Σ_L is independent of the conical structure up to isotopy, in o-minimal (tame)
    topology.
- *Why it matters:*
  - it is P150f-1's gluing theorem along bands instead of strata, the form that a recollement (H150f-3) and the Longue
    Marche's pieces need;
  - it puts the self-flagged (100) on its true hypothesis.
- *Refuted forms, to be stated in the prompt so that no time goes into them:*
  - (100) and (104) for arbitrary locally closed Z (R150g-36, -40);
  - (103) for non-bands (R150g-39);
  - (96) ⟸ without density (R150g-34).
- *Strongest reduction on the page:*
  - (110) ⟸ (100), through the homotopy colimit of the open cover by the V_d (R150g-43);
  - (100) for a union of strata ⟸ control on the retractions (R150f-19);
  - (111) is (110) with Z = X_L^*;
  - (78) ⟸ the corner structure of the deployment (R150g-12).
- *Material:*
  - the second-pass `.tex` of MPL_150_085-099+151_001-031, scans 085-099, with K150g-04 fixed;
  - this reading's four files;
  - P150f-1's material;
  - for the Remarque: L. van den Dries, *Tame topology and o-minimal structures* (1998), triangulation and Hardt
    triviality (locators to be checked).
