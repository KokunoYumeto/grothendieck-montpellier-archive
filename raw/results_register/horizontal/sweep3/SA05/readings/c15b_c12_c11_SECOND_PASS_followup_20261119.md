# Follow-up readings on the scans for the RESEARCH_SA05 intake (12:120, 15:3, 15:5, 15:11)

Claude Opus 5.5 at effort max (agent a7b7747fd6dd29f87), 19 Nov 2026. These places were read on the scans at the
coordinator's word, after the intake of the RESEARCH_SA05 final (`../INTAKE_RESEARCH_SA05_20261119.md`, §6).

The transcriptions checked:
- 12:120: `returns/MPL_12_099-149_unzipped/pages/MPL_12_099-149_12_scan120.tex`, the GPT-6 Astra (ChatGPT Pro mode) first
  pass, against `packages_done/P131_87_MPL_12_099-149/MPL_12_099-149_scans.zip`, image `..._12_scan120_b.jpg`;
- 15:3, 15:5 and 15:11: `returns/MPL_12_150-168+15_002-033_unzipped/MPL_12_150-168+15_002-033/pages/`, against
  `second_pass/img/MPL_12_150-168+15_002-033/`.

The crops are in `grothendieck_archive_transcription_20261110/second_pass/work/SA05_followup/`.

## Changes, in the second-pass form

| scan | place | first-pass reading | corrected reading | evidence (what the image shows) | confidence |
|---|---|---|---|---|---|
| 12:120 | final box, "Cas général relatif", second line | `\text{niveaux}&\le\operatorname{Inf}(i,\unsure{n})+j` | `\text{niveaux}&\le\operatorname{Inf}(i,n)+j` | a heavy, retraced n (a short stroke below it, perhaps the remains of an earlier sign); the first line of the box reads 2 Inf(i, n) + j, followed by a "?". The margin lasso asks "peut on remplacer par n − 1 si f est de dim ≤ n − 1 ?", with struck words about the fibres. So n stands in the box, and n − 1 is the improvement he asks about (crop c120) | medium |
| 15:3 | the band of the subgerbe | `H=\operatorname{Ker}(G^0\xrightarrow{\unsure{\epsilon\|e}}G_m)` | `H=\operatorname{Ker}(G^0\xrightarrow{\epsilon}G_m)` | the label over the arrow is ε, the letter of the augmentation ε: G → G_m (image s3b) | high |
| 15:11 | NB, first argument | `\unsure{U\|H} est disconnexe` | `U est disconnexe` | a script capital U with a hook at the top left and no crossbar. His H on 15:3, "H = Ker", has a crossbar (zoom c11). The sense (a polarizable category whose group is disconnected) points to his group H = H⁰ × μ₂ or to a group named U nearby; the reading is U | medium |

## Readings confirmed, without change

- **12:120: what n denotes.** Above the final box, beside the diagram X → Y ∋ y, he defines
  "n = d_y(f) = Sup_{x ∈ X} [deg tr k(x) : k(f(x)) + dim of the closure of f(x) at y]". This is a local relative
  dimension at y, with "au voisinage de y". With n = d_y(f), his box gives level ≤ Inf(1, 1) + 0 = 1 for H¹ of an
  elliptic curve over F₅, which is right. The RESEARCH_SA05 counterexample refutes only our prompt's n − 1 form (prompt
  C.4). The fine reading of the bracket in the definition of n (the dimension term) is medium.
- **15:3: the augmentation.** The word "augmentation" does not occur on 15:3. The Tate rigidification is on the page in
  another form: right after "F⁰(H*(X)) = f_*(Q_X) si X fini sur k — cela définit F⁰ sur Niv⁰(M)⁰", he writes
  "F⁰(Q(1)) = Q".
  - So F⁰ includes the Tate object, and the band H he names for the subgerbe "des foncteurs fibres de M prolongeant
    F⁰" is right as written.
  - Our STUDY.md §1 glossed Niv⁰(M)⁰ as "the motives of level 0 and weight 0 (the Artin motives)" and left out
    F⁰(Q(1)) = Q.
  - The transcription has the line.
- **15:5: the weights.** "le sous-groupe Γ ⊂ Q̄* formé des λ tels que l'on ait: λ entiers algébriques; λ unité
  ℓ-adique pour ℓ ≠ p; |λ_i| = p^{ν/2} pour ~~∃~~ ν ∈ Z⁺ convenable, pour tt conjugué λ_i de λ."
  - These conditions define the monoid of effective Weil numbers (ν ≥ 0, algebraic integers), while he calls Γ a
    subgroup.
  - The group he uses is the group they generate: all weights ν ∈ Z.
  - The RESEARCH_SA05 correction ("literal monoid reading") stands as a correction of his text. The transcription is
    right.
- **15:11: the ground field of Serre's argument.** The paragraph ends "soit par l'argument de Serre sur la courbe
  elliptique d'inv. de Hasse nul" and names no field. Over F_p the argument needs the repair the run gives:
  End⁰(E) = Q(√−p) is a field, while the quaternion algebra is End⁰ over F_{p²}. The transcription is right.
