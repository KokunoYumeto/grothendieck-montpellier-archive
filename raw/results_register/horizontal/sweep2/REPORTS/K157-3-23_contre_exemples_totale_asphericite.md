# His "Contre-exemples pour la totale asphéricité" (Les Dérivateurs, cote 157-3, scans 342-356)

Claude Opus 5.5 at effort max (agent a34c04448e8299803), horizontal sweep 2 part 2, 18 Nov 2026. Item SA32-33. Global
concepts HTA1/HTA2 (`sweep1/GLOBAL/CONCEPTS.tsv`). Each passage was read in the transcription; the readings marked
"image" were decided on the scan image (`grothendieck_archive_montpellier/21_derivateurs/157-3.pdf`, page = scan).

## Where
| what | where |
|---|---|
| his pages | cote 157-3, scans 343-353 (his local pages 9-17), scan 355 (p. 18) |
| other paper in the folder | scans 342, 344: reused typescript (pp. 41, 44 of another text); scans 354, 356: a blank form of the Inspection académique de Vaucluse (Avignon) |
| transcription | `grothendieck_archive_transcription_20261110/codex_web_20261113/returns/K157-3-23/out/K157-3-23_transcription.tex` |
| notes | the same folder: `K157-3-23_mathnotes.md` (Work, six units), `K157-3-23_notes.md` (Codex, two tables) |
| research | REGISTER.tsv: DER_FOLLOWUP A.11, C.7, F.1; POLES G.4, B.8, G.2; TOTAL_ASPHERICITY A.13, A.14 |

## What his pages contain
1. **p. 9 (scan 343).** A category V = (0 ⇉ a, then a → b, a → c) with βλ = βμ and γλ = γμ. He finds b ⊔_a c ≅ e_V in V^∧,
   "pourtant V n'est pas asphérique, ni même 1-connexe": he says V is homotopic to V₀ = (0 ⇉ a) through a retraction.
2. **p. 10 (scan 345), §2.6.**
   - He states: "Je me suis finalement convaincu que Υ = {a₀ → b₀, a₀ → c₀} n'est pas totalement asphérique (pour le
     localiseur W∞ ...)".
   - He gives an equivalent form: there is a diagram of type Υ in some Z whose colimit b ⊔_a c in Z^∧ is the final
     presheaf e_Z, "sans que pour autant Z soit asphérique, ni même 1-connexe*".
   - Margin: "*faux -- il est 1-connexe forcément, mais non 2-connexe (cf commentaire XII p. 101)". On the image, "faux",
     "XII" and "101" are legible.
3. **p. 11 (scan 346).** The "universal" example Z: Υ plus an object o₀ with two arrows λ₀, μ₀ to a₀, equalized by β₀ and
   γ₀; six non-identity arrows in all. He first claims a retraction of Z onto Z₀ = (o₀ ⇉ a₀). Margin: "faux, il n'y a pas de
   rétraction du tout ! En fait, Z est la suspension de [o₀ ⇉ a₀], qui a le type d'homotopie du cercle, [donc Z a] le type
   d'homotopie de la 2-sphère."
4. **pp. 12-16 (scans 347-352).**
   - "b₀ ⊔_{a₀} c₀ = e_Z est immédiate."
   - Aim: finite "déchirants" pushouts in Cat with an aspheric open immersion i: U → Ū (so i ∈ W) but i' ∉ W, and with
     p ∈ W but q ∉ W. Unlike "prop. 10, 11 (p. 101-107)", these use finite categories.
   - **Proposition (p. 13):** for n, m ≥ 2, the inclusion of the boundary U = ∂X into X = Φ_n × Φ_m is a W-aspheric
     open immersion. It is not a Dwyer immersion, because of the four corners. The proof shows that U → X is not a
     W-cofibration.
   - The proof: the corner category ≅ Υ is a closed Dwyer immersion; it uses V̄ = Δ¹ × Δ¹, and V' (V'₀ plus a final
     object). The step "i' ∈ W équivaut à V'/t W-asph." cites "cor. 4, p. 149 dans (XII)". On the image, the digit is
     the 4 of "149"; the chapter mark could be read XII or XIb.
   - The margin there reads "moyennant (W 7 bis)" (image: barred 7). V'/t ≃ V'₀ has π₁ = Z, so it is not W-aspheric
     "dans le cas, disons, où W = W∞" (image: subscript ∞; W₁ is less likely). "qed."
5. **p. 17 (scan 353).** "Recollement dans Cat d'un ouvert et d'un fermé complémentaire": is the gluing square
   W-cocartesian (assuming Loc(6))? For a variant: "chose fausse (sauf si i ou j ∈ W = W∞)".
6. **p. 18 (scan 355).** The situation is "tout à fait spéciale à la catégorie des modèles Cat". Margin: "une esquisse de
   vérification pour n = 2" convinces him that φ ∈ W₂.

## Which "totally aspheric"
- **HTA2.** §2.6 states total asphericity through final images: a Υ-diagram whose colimit in Z^∧ is the final presheaf
  must force Z to be aspheric. This is the Les Dérivateurs XII notion, and he cites "commentaire XII p. 101".
- **Not HTA1** (products of representables, Pursuing Stacks §65 A). Υ has the initial object a₀, so its products of
  representables are not at issue.

## Against the research runs
- **Agrees: Υ is not totally W∞-aspheric.**
  - DER_FOLLOWUP:A.11 (proved; XII ms. 88-89): A is total for W iff BA is W-aspheric and every action component has a
    W-aspheric unreduced suspension.
  - For Υ: BΥ is contractible (a₀ is initial). The action with two points over a₀ and one over each of b₀ and c₀ has a
    component equal to the poset K_{2,2} ≃ S¹; its unreduced suspension is S², which is not W∞-aspheric. (My computation.)
  - DER_FOLLOWUP:C.7 (proved; XII ms. 101-103, 109): W₀ needs 1-connected, W₁ needs 2-connected. This matches his
    corrected margin, "1-connexe forcément, mais non 2-connexe (cf commentaire XII p. 101)".
- **His example Z checked by hand (agrees with his margins, not with his first text).**
  - b₀ ⊔_{a₀} c₀ is the final presheaf objectwise: at o₀ it is 1 ⊔_2 1 = 1; at a₀, b₀ and c₀ it is 1.
  - Z is covered by the sieves {o₀, a₀, b₀} and {o₀, a₀, c₀}. Each has a final object, and they meet in the circle
    category o₀ ⇉ a₀. The forward excision clause holds for W∞ (POLES:G.2), so BZ ≃ ΣS¹ = S²: 1-connected, not
    2-connected.
  - His first claims (V and Z not 1-connected; a retraction) are false, and he crossed them out in the margins himself.
- **The Proposition of p. 13 depends on a step that fails for W∞.**
  - Its proof passes through XII Cor. 4 (ms. 149) "moyennant (W 7 bis)".
  - POLES:G.4 (refuted): the one-point-complement equivalence (XII ms. 85) and Corollaries 4-5 (ms. 149-151) "are valid
    under W(7 bis), but false for W∞".
  - POLES:B.8, POLES:G.2 and TOTAL_ASPHERICITY:A.13: W∞ fails W(7 bis).
  - So, as written, the proof stands for a localizer with W(7 bis). TOTAL_ASPHERICITY:A.14 gives W_R, for which V'₀ is
    not aspheric either, since H₁ = R. For W∞, which is the case he names, the proof does not stand. Whether ∂X → X fails
    to be a W∞-cofibration is open from this argument. (My reading of the dependency, not re-proved.)
- DER_FOLLOWUP:F.1 (filtered ⊊ exact ⊊ total ⊊ quasi-filtered; witnesses Δ_inj, C_δ, repaired K*) concerns other
  examples. Υ adds a small non-total category with an initial object.

## What our notes say
- The Work notes (`K157-3-23_mathnotes.md`, lines 9, 24, 62) describe Υ and Z and record the margins "faux", "il n'y a
  pas de rétraction du tout !", "Z est la suspension de". They also record "moyennant (W 7 bis)" and the citation, read
  as "cf … 9, p. 149 dans (XII)".
- They do not say that the cited corollary fails for W∞. The image favours "cor. 4", the corollary that POLES:G.4
  refutes.

## Corrections and refinements (also in SA32/CORRECTIONS.tsv)
1. Status of "Υ is not totally W∞-aspheric": stated by him, true. He corrected his first reason; the reason now is Z ≃ S².
2. Status of the p. 13 Proposition: proved by him modulo W(7 bis) and XII Cor. 4, which are false for W∞. It stands for
   localizers satisfying W(7 bis); for W∞ it is not established.
3. Reading: "cor. 4" (image), not 9; the chapter mark is undecided between XII and XIb.

## For sweep 3
- Is ∂(Φ_n × Φ_m) → Φ_n × Φ_m a W∞-cofibration?
- The "Recollement" question of p. 17 against STRATA C and POLES G.19 (gluing).
