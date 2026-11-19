## STUDY

**Cote 150, scans 72-84 (his sheets 31v-38), read in full on the second-pass text of 17 Nov; full reading
`readings/150_072-084.md`.**

**The Remarque (072).** The first "déploiement", Σ = ∐X_i with arrows ∐_{X_i⊂X_j} X_i, is 151's half-simplicial space
(s étale, b a closed immersion), re-proved; the second is the deployment of cote 150 (b bordant). The margin's "c) follows
from a), b)" needs manifold components and s locally trivial.

**§14, the deployed strata cut out by tubes (073-076).** Σ_i = X_i ∖ T̊_{<i}, Σ_{ij} = Ṫ_i ∩ Σ_j, and over flags
Σ_{i_0…i_n} = Ṫ_{i_0} ∩ … ∩ Ṫ_{i_{n−1}} ∩ Σ_{i_n}, made coherent by a dimension function and the filtration
X^{(d)} = X − ⋃_{α<d} T̊_α.
- Cofinal deletions are inclusions and the other deletions go through retractions: 039's standard presentation, built
  concretely.
- With Mather's control on the retractions, the cartesian square (3) of 040 is re-proved.
- Refined: Σ_{ij} ⊂ Σ_j needs T'_{ij} to be the trace of T_i (a smaller tube fails); (49) has the slip X_{(d)} for
  X^{(d)} and needs admissible tubes; closedness needs T̊ open (H150a-3).

**§15, pro-neighbourhoods (077-084).** V_i ≃ X_i^*; V_i ∩ V_j = ∅ for incomparable strata exactly under his "ouverts
normaux" (hereditary normality); X is the colimit of the V_i along the V_{ij} level by level, and of the V_d over
Drap(I)^op, so the corner pieces that refute 151/069 are present.
- Relative versions need Z a union of strata (counterexample Z = {0} ∪ {1/n}).
- Ideals and bands are the closed and locally closed subsets of Esp(I); V_J and the raccords V_J^L = V_J ∩ X_L^* reduce to
  J ≺ L.
- The band Lemma is re-proved, its struck 3° shown redundant.
- In X' = X^*_{I'}, X'_J is closed and X'_L open. The margin (69), V_J^L ↪ V_J ∩ V_L an equivalence for J ≺ L, is
  re-proved under control and fails without domination. With J = {i}, L = {j} it answers his question of 077.
- (70) row 2 is exact only for J ∩ L = ∅; (71)-(72) are a correct intersection-stable cover, and (73) its spectral
  sequence for I finite.

**H4 refuted.** "Str_∞ p. 84" (151/059) is "Structure à l'infini des M_{g,ν}" (cote 147), his p. 84 = scan 147/177, with
(292)-(294) on 147/176 (scans viewed). Cote 150 §15 is the general form of those normal-crossings pieces, and its
comparison map is canonical where (294)'s is not.

**Counts:** 36 check events (SA10-R150f-01 to 36), 15 corrections (SA10-K150f-01 to 15), 125 \unsure marks; five
consequential readings open.

## HUNCHES

**H150f-1. Cote 150 §15 makes the Longue Marche's (294) canonical** (refutes H4 as stated; sharpens H1, H150a-1 and P1).
- *Grounds:* 151/059 cites 147/176-177. The pieces 𝒱^{d'}_{d,d''} are V_J^L with J = {d}, L = {d'} inside X' = D_{d''}.
  The margin (69) and V_{ij} ≃ Σ_{ij} (R150f-29, 36) give their homotopy type through a canonical inclusion of
  pro-spaces. In (294) the defect is "ne pas correspondre à une flèche canonique"; only the identification with the
  normal bundle stays non-canonical.
- *Test:* for a normal-crossings divisor, compute V_J^L and E_2 of (73), and compare with 147/177's Scholie.

**H150f-2. The raccord V_J^L is the homotopy link of X_J^* in X_L^*** (sharpens H150b-4, H150c-2 and the first-pass note
N23).
- *Grounds:* V_J^L = V_J ∩ X_L^*, the germ of X_L^* near X_J^*; (69) and the hocolim over Drap(I)^op (R150f-17).
- *Statement to test:* in a homotopically stratified space, V_J^L ≃ holink(X_J^* ∪ X_L^*; X_J^*), for J ≺ L. Literature:
  F. Quinn, "Homotopically stratified sets", J. Amer. Math. Soc. 1 (1988), 441-499 (locator to be checked).
- *Consequence:* the V_d over Drap(I) are a pro-space form of the exit-path data. (73) is then a descent spectral sequence
  for constructible cohomology, the sheaf-level form of 151/043's van Kampen principle.

**H150f-3. The band calculus is the recollement calculus of Esp(I)** (sharpens H150a-4 and SA10's question P1).
- *Grounds:* ideals and bands are the closed and locally closed subsets of Esp(I) (R150f-20). The band Lemma gives the
  smallest locally closed piece X' = φ^{-1}(I') in which J is closed and L open (R150f-26, 28).
- *Consequence:* V_J^L is the deleted germ of a closed part in an open one, the datum of SGA 4 IV 9.5 (locator to be
  checked), when I' = J ⊔ L; otherwise the middle strata intervene (first-pass N22).
- *Test:* the 2-functor J ↦ Sh(X_J^*) on the bands of I should be glued from the V_J^L. This is P1 with the right stones.

## PACKAGES

**P150f-1. The pro-space model of a stratified space, and the Longue Marche's pieces made canonical.**
- *The question:* for Whitney (or Thom-Mather, or homotopically stratified) spaces, prove (51), (56)-(57) for unions of
  strata, the margin (69) for J ≺ L, the agreement V_d ≃ Σ_d, and (73). Identify V_J^L with the homotopy link, and derive
  147/176's (294) canonically for normal crossings.
- *Why it matters:*
  - it is the gluing theorem of P1 done with the right pieces (all flags), and it repairs 151/069;
  - it supplies the canonical arrow that 147/176 lacks;
  - it joins cote 150 to La Longue Marche's structure at infinity of M_{g,ν}.
- *What it rests on:* 150/073-084 (read in full here), 150/031-043 (standard presentation), 151/057-069, and
  147/160-177.
- *Strongest reduction on the page:*
  - (53) holds level by level;
  - (69) reduces to (57) in X' and to X'_L being open;
  - (57) reduces to a control condition on the retractions (R150f-19);
  - (73) is the cover spectral sequence, for I finite.
- *Material:* the second-pass `.tex` of MPL_150_044-084 and MPL_151_032-075; the first-pass `.tex` of MPL_147_138-190;
  J. Mather, "Notes on topological stability" (control data); F. Quinn 1988; J. Lurie, *Higher Algebra*, App. A;
  D. Dugger and D. Isaksen, Math. Z. 246 (2004); SGA 4 IV §9. Locators to be checked.
