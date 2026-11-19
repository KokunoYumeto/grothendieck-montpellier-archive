## STUDY

**Cote 151, scans 18-31, read in full** in my second-pass text of 17 Nov (Claude Opus 5.5 at effort max, 19 Nov);
native images checked on 020, 023, 025. Full working: `readings/151_018-031.md`.

**018** is a cancelled draft of the product step of "Hyperrecouvrements" (014-015): φ_! preserves products if it does
so on representables, by universal colimits (re-proved).

**019-025 (his pages ② to ⑦): the finite-set system of 017 in degree 3.**
- 019 lists five types of condition (I concatenation, II-V squares of δ's and K's), with consistent counts per degree.
- 020 writes out the degree-3 conditions, épi maps and two "cart" squares, and asks "iso ???" of X_2 → X_1 × X_1.
- **Decided on the native image:** the top arrows of the first square (020) and of (*) (025) are the degeneracy
  X_2 ↪ X_3, not maps X_3 → X_2, so the squares are the images of the E-squares beside them (E04 withdrawn).
- **With X_1 a point, re-proved:**
  - the five relations, pρd = c being the pointed form of pρd = δ_0p_1;
  - the lemma on the translates ρ^i d(ζ);
  - the orbit decomposition X'_3 = {e_3} ⊔ 𝔖_3 ∧_{1,σ_1} X_2^*;
  - the image Σ of (p, pρ), and the criterion |X_2| ≤ 2.
- **The two squares:**
  - (*) is cartesian for every system (an Eilenberg-Zilber-type identity), not only for card X_1 = 1.
  - (**) is a real axiom; it forces p^*(X_3^*) ⊂ X_2^*, so p^* is never onto (the single arrowhead).
- **Slips:**
  - ρσ_iρ^{-1} = σ_{i−1} under his composition, not σ_{i+1};
  - the second case on 025 reads "i=1" in the ink; 2 is meant.
- **What the system is:**
  - "iso ???" is answered in the negative by the nerve of ℤ/2, the page's own case.
  - A 3-sheeted cover with monodromy 𝔖_3 shows that |X_2| = 2 does not force X_3 = X'_3.
  - With 009's group relations, the system reads as the π₀ shadow of a Čech or hypercovering nerve.

**027-031: "Structures stratifiées" §1, pp. 1-3.**
- **The provisional germ collapses for paracompact X.** The topos limit of the open neighbourhoods is Sh(Y), and the
  punctured germ is empty. The pro-object (cote 150 §15) or a non-T₁ site (Zariski, étale) keeps the content.
- **His margin Y ≃ 𝒱** holds in shape, and as a homotopy equivalence for tame Y.
- **"Z^* a manifold" fails in Top** (Bing's dogbone) and holds in PL and smoothly, under the moderation he names.
- **The span (7)** glues X back for honest neighbourhoods.
- **Van Kampen:**
  - (8) holds without connectivity (Brown).
  - (9) needs 𝒱^* connected (X = S¹ with a point refutes it as stated); 151/33's connected link supplies it.
  - "extérieurement" and the path-class margin are right.
- **Into 032:** local triviality makes 𝒱^* → Y a fibration with fibre the link, which is (11) of 151/32.

**Counts:**
- 32 check events (SA10-R151b-01 to 32) and 11 corrections (SA10-K151b-01 to 11);
- doubt marks 192 → 191 after the fold-in.

## HUNCHES

**H151b-1. The finite-set system of 151/003-025 is the π₀ of a hypercovering indexed by finite sets.** This is new,
and links SA10-8 and the "techniques bisimpliciales" of 151/43.
- **The hunch:**
  - Take a functor X on the nonempty finite sets [1,n] (017) satisfying the concatenation surjectivity (**) and the
    conditions I-V of 019. It is the π₀ of a Čech-type nerve, U^{×n}, of a covering in a topos.
  - Its axioms are Hyp 1-2' of "Hyperrecouvrements" (011-013) for that index category.
  - Groups and Galois covers give the bijective case, where the bound of B11 is attained. Non-Galois covers give
    X_3^* ≠ ∅.
- **Grounds:**
  - the group relations σ(x)·x = 1 and p_12 p_23 p_31 = 1 on 009;
  - the parallel of (**) with Hyp 2, which Michel Hua's project also notes;
  - the three examples of SA10-R151b-17;
  - "iso ???" answered (R151b-18).
- **To test:**
  - whether the degree-3 conditions of 020 characterize the π₀ of 2-coskeletal Čech nerves;
  - what "épi" rather than "bijective" adds, which is the hypergroupoid direction.
- **Literature:** M. Artin and B. Mazur, *Etale homotopy*, LNM 100 (1969); SGA 4 V §7 (hypercoverings). Locators to be
  checked.

**H151b-2. The tube of 151/028 should be a pro-object or an oriented product, not a topos limit.** This sharpens H150f-2
and H150b-4.
- **The hunch:**
  - For Hausdorff X, the right punctured germ is the pro-space of the U ∖ Y, whose homotopy type is Quinn's homotopy
    link.
  - On étale sites the limit topos is the henselized neighbourhood, and the punctured germ is Deligne's oriented
    product Y ×← X^* (the vanishing topos).
  - Artin gluing is the sheaf form of the span (7).
- **Grounds:**
  - SA10-R151b-25: the topos limit collapses for regular X;
  - 151/32 names the étale setting;
  - cote 150 §15 switches to pro-neighbourhoods.
- **Literature:** F. Quinn, J. Amer. Math. Soc. 1 (1988), 441-499; L. Illusie et al., *Travaux de Gabber*, Astérisque
  363-364 (2014), exposé XI; SGA 4 IV 9.5. Locators to be checked.

**H151b-3. (8)-(9) with (11) is the two-stratum case of a homotopically stratified set.** This sharpens H2.
- **The hunch:**
  - (11) of 151/32 is Quinn's holink-fibration condition for two strata.
  - (9), with 𝒱^* connected, is the π₁ shadow of X ≃ hocolim(X^* ← holink → Y).
- **Grounds:**
  - SA10-R151b-29, R151b-30 and R151b-32;
  - the S¹ counterexample shows that the pointed form needs the link connected, which 151/33 assumes.

## PACKAGES

**P151b-1, joined to P150f-1 (one cluster, one prompt): the punctured tubular germ as a topos.**
- **The question:** which object should 𝒱^*_{Y,X} be, so that (7) recovers X, (8)-(9) hold and (11) makes sense? The
  candidates are:
  - (a) the topos limit, which collapses for T₁ spaces X and is right for schemes with the étale topology;
  - (b) the pro-topos of punctured neighbourhoods;
  - (c) the oriented product Y ×← X^*.

  The package asks for the comparison maps between them where they are defined, and for the gluing, van Kampen and
  fibration statements for each.
- **Why it matters:** 151/32-44, the homotopy type of a stratified space from its pieces, rests on this object. With
  the topos limit, (5)-(10) are empty for Hausdorff X.
- **What it rests on:** SA10-R151b-25 and R151b-28 to R151b-32; STUDY §1; reading 150_072-084 (§15, the
  pro-neighbourhoods).
- **The strongest known reduction:**
  - For honest open neighbourhoods, and pro-systems of them, (7) and (8) are classical: open covers and Brown's
    groupoid van Kampen theorem.
  - The étale case is Artin gluing together with the description of i^*j_* by the henselized punctured neighbourhood.
- **Material:**
  - 151/027-044 and 150/077-084;
  - SGA 4 IV 9.5;
  - Illusie et al. 2014, exposé XI;
  - Quinn 1988.
