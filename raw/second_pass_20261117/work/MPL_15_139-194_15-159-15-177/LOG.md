# Work log, block MPL_15_139-194_15-159-15-177 (agent a28ea31fa17dd65e1, Claude Opus 5.5 at effort max)

One entry per scan as it is checked: the changes (place | first pass | corrected | evidence | confidence), what is unresolved, and the notes.

## scan 159: no change
- The ink agrees with the first pass line by line. Crops are in s159_crops.png.
- Kept as unsure:
  - "unités \unsure{absolues}": the shape fits "absolues" with "ab" run together, but the first letters are not distinct;
  - the struck cluster before "Z×R*" (first pass: A_Q, unsure);
  - the symbol ℛ|𝔑 (a calligraphic R with a loop).
- The display reads "A*(... Z×R*)" with a plain Z; no hat is visible.
- "l'union des sections": the word is not struck, only heavily inked.
- Note (sweep-3 reader, mathematical, not a reading): the abelianized Galois group is an extension of the narrow
  class group Pic^+(A) by Ohat*/closure(E^0). With his second formula it is an extension of Pic(A) by
  (Ohat* x pi_0(K_R*))/closure(E).

## scan 160: no change
- A reused Bourbaki typescript (n° 413, p. 1-41), upside down on the sheet. Read upside down; every line agrees.
- The typewriter writes "T^{(o)}" and "T_o" with the letter o where the first pass has 0. This is not
  consequential, and the first pass's "\unsure{o|0}" already lists the ink's "o" first.

## scan 161: 2 changes (in edits.py)
- Diagram, superscript of Pic(A): \unsure{abs|ab} becomes "abs". The crop shows three letters, a, b, s. High.
- Both diagrams: \unsure{réseaux} de Hodge becomes "réseaux de Hodge"; the word is clear in both nodes. Medium.
- Kept as unsure:
  - Γ|γ: a cursive Γ looks like "r";
  - "on \unsure{donne}";
  - "\unsure{le tout}";
  - the last line's "\unsure{réseau}".
- Checked and agreeing with the first pass: "de" before K is struck; "K, est associé des foncteurs" (faint "associé");
  the margin "K̃ = corps de classes absolu", with "absolu" underlined.

## scan 162: no change
- Bourbaki typescript n° 413, p. 1-38, upside down. Every line agrees, including the underlines and the formula (23).
- The ϑ is drawn by hand; the first pass's \unsure{\vartheta|\theta} is kept.
- "Si r ⩾ ∞" is typed as the first pass has it.

## scan 163: 3 changes (in edits.py)
- Line 1: "Si ξ̃ est réelle" becomes "Si ξ̃ \deleted{est} réelle". A horizontal stroke crosses "est" (crop). Medium.
- Diagram: the struck word before "G⁰-Modules" reads "Vectori(el)s" (an l near its end), not "Vecteurs".
  It becomes \deleted{\unsure{Vectoriels|Vecteurs}}. Medium.
- Crossed-out block, "V ⊗_Q C muni de \deleted{une}" becomes "muni des \deleted{\unsure{une}}": the ink reads "des". Medium.
- Unresolved: the struck "NB Le \unsure{degré} de ξ". The struck word is longer than "degré" (perhaps "domaine");
  it is kept as is.
- Checked: the crossed-out NB block, the two fibre functors ξ̃, ξ̃', and Φ under the plain right-hand line.

## scan 164: no change
Bourbaki typescript n° 413, p. 1-37, upside down. Every line, the underlines, Proposition 20 (i) and (ii), and the
tildes under R and C agree with the first pass.

## scan 165: 3 changes (in edits.py), one consequential
- "filtré par des H_ξ(\unsure{W|V})^{(p)}" becomes "H_ξ(W)^{(p)}"; the crop shows "(W)". Medium.
- Margin \unsure{coh. de De Rham} becomes "coh. de De Rham" ("DeRham" is legible). Medium.
- CONSEQUENTIAL: "prolongeant frob_ξ de façon \uline{K_ξ-linéaire} à V̄_ξ" becomes "de façon \uline{½-linéaire}",
  his abbreviation for semi-linéaire.
  - Evidence: the crop shows the sign ½ before "linéaire".
  - Confidence: high.
  - Meaning: frob_ξ (complex conjugation for a real place) is extended semi-linearly to V ⊗ K̄_ξ = V ⊗ C, not
    K_ξ-linearly. Only then can "frob'_ξ soit l'identité sur H_ξ(V)" make H_ξ(V) a real structure.
- Kept: G^{0|*} (the superscript is struck or scribbled), "\unsure{norme}", p|ρ, K̃|K̄, G|C, ξ_{m|∞}.

## scan 166: 1 change (in edits.py)
- Bourbaki typescript n° 413, p. 1-36, upside down.
- (21), index: "(1≤i≤m, \unsure{≤}1≤j≤n_i)" becomes "(1≤i≤m, ≤1≤j≤n_i)". The stray "⩽" after the comma is
  in the typescript, so it is kept as typed. Medium.
- Everything else agrees: Proposition 19, its Corollary and (22).

## scan 168 (another hand, blue ink on squared paper): 1 change (in edits.py)
- "Q(\unsure{ζ})" becomes "Q(ζ)": the same glyph as the clear "ζ^m = 1" that follows. Medium.
- "[K:K'] = 2" reads 2 in the ink, so there is no reading change. The sweep-3 reader's "[K:K'] = p" is a mathematical
  correction, not a reading. The writer changed "quadratique" into "de degré p ≥ 2" and changed "= p(r'_1 + 2r'_2)"
  (overwritten in darker ink), but left "[K:K'] = 2". Their "0 ≥ r_1 + 2r'_2" is right for general p: it follows
  from 0 = r_1 + (p-2)r'_1 + 2(p-1)r'_2.
- The struck "K⊂R, ou" after b) and the struck "r_1+r_2" are confirmed.

## scan 172 (cover): no change
"Calculs de cohomologie / absolue des Motifs / de Tate Z(n)." agrees. The first word's ending is a flourish, so
\unsure{Calculs|Calcul} is kept. The sheet number is 171.

## scan 173: 4 changes (in edits.py), one consequential
- CONSEQUENTIAL (medium): the two displays over Spec Z use the doubled ℍ of his absolute cohomology, as on the
  lines for 𝐇^i(F_q, ...) above. "H^i(Spec Z, Z(1))" becomes "\mathbb H^i(Spec Z, Z(1))", and
  "\unsure{\mathbb H|H}^i(Spec Z, Z)" becomes "\mathbb H^i". Evidence: the crop shows a doubled left stroke in both.
  This makes "H^3(Spec Z, Z(1)) = Z" a statement about his absolute cohomology, which the sweep-3 reader identifies
  as Weil-étale cohomology.
- Line "𝐇^i(F_q, Q(n)) = 0 si n ≠ 0, \text{pour tous} i": the ink begins "quel que" as in the line above, but the
  third word is unclear. It becomes \unsure{quel que soit|pour tous}. Low to medium.
- "l^{\unsure{v_l|ν_l}(1-q^n)}" becomes "v_l". Medium.
- Margin "... et n ≠ 0 (tout i)": the ink reads n ≠ 0. The sweep-3 reader's "n ≠ 1" is a mathematical correction:
  the localization terms H^{i-2}(points, Q(n-1)) vanish for n ≠ 1, and at n = 1 the units of U enter.
- Kept: M'_π|M_π, the "\unsure{!}" after Q_l, "(mod \unsure{p-prim|p-près}?)", and the struck Q under the first Z.

## scan 174: 3 changes (in edits.py)
- Margin "\unsure{pas de miracle}, car si i ≥ 4, les deux \unsure{mbs} doivent être = 0" is settled as "pas de miracle"
  and "mbs" (= membres); both are legible in the crop. Medium.
- "[\unsure{est-on|est-ce} nul ??]" becomes "[\unsure{est-ce|est-on} nul ??]". The word after "est-" is one short
  stroke, more like "ce" than "on", which agrees with the sweep-3 reader's "[est-ce nul ??]". "nul" has no visible
  ascender (it could be "vrai") but is kept. Low.
- "\unsure{où on trouve} Q !" becomes "où on trouve Q !". Medium.
- Checked: the localization sequence, i_x^!(M) = \unsure{R} i_x^*(M)(-1)[-2] (the mark before i_x^* is a small
  stroke, kept unsure), the n ≠ 1 and n = 1 cases, and "H^i(X,Q(1)) = 0 sauf pour i = 3, où on trouve Q !".

## scan 175 (the whole page crossed out): no change
- The cocycle computations, the diagram for H^1(π,M) and M finite, φ(x^n), φ(x^{-n}), Z^1, B^1, H^1(Z,M) and
  "(1-f^n)/(1-f) φ(f)" agree with the first pass.
- Kept as unsure: "1\unsure{-}x^n" (the operator is a blot), "\unsure{pti}", B|𝔹 (a doubled stroke), α|x.

## scan 176: 5 changes (in edits.py), one consequential
- "les anneaux \unsure{localisés|locaux} stricts" becomes "localisés"; the crop reads l-o-c-a-l-i-s-é-s. Medium-high.
- CONSEQUENTIAL (medium): "H^1(X, \uline{\unsure{D|Z}^0}_X) = 0" becomes "H^1(X, \uline{\unsure{Div|D^0}}_X) = 0".
  - Evidence: the underlined sheaf symbol is a D followed by a compressed small group, consistent with his "Div".
  - Mathematics: Proposition 5.4 needs H^1(X, Div_X) = 0. The exact sequence 0 → G_m → R_X^* → Div_X → 0 gives
    H^1(Div) → H^2(G_m) → H^2(R^*). With factorial strict local rings, Div_X is a sum of i_{x*}Z over the
    codimension-1 points, and H^1(x, Z) = Hom(Gal, Z) = 0.
- Theorem 5.6 a): "Si X est un schéma \unsure{loc|local}, \unsure{et}" becomes "local, et"; both are legible. Medium.
- "il existe \unsure{un|une} \deleted{extension} morphisme" becomes "\deleted{une extension} morphisme": the strike
  starts under "une". Medium.
- "\deleted{\unsure{splitte} ξ}" becomes "\deleted{splitte ξ}"; "splitte" is legible. Medium.
- Kept: "Sous les \unsure{=^s|=} conditions" (his abbreviation for mêmes) and the struck "tel que ξ|X' \unsure{=0|→0}".

## scan 177: 1 change (in edits.py)
- Margin "\unsure{pas de miracle}, car les deux sont nuls." is settled as "pas de miracle", the same words as on 174.
  Medium.
- Kept: the superscript H^{\unsure{i+1|i-1}}_S (the sign is not distinct; the sequence needs i+1), the smudged
  "\unsure{⋯}", the blot "\unsure{0}" for i = 0, and the overwritten X̄ in H^2.
- Checked: both diagrams over Spec Z and S, with "Z* = {+1,-1}", "(Q/Z)^S —somme des inv.→ Q/Z" and "H^3(Ū,G_m) =? 0".

## BLOCK DONE (outputs written once to second_pass/out/MPL_15_139-194/)
Final message for block 1:
- 15 scans; changes 23 (high 3, medium 18, low 2); 32 places unresolved.
- Consequential corrections:
  - 15:165 "prolongeant frob_ξ de façon K_ξ-linéaire" → "½-linéaire" (semi-linear extension of the real Frobenius);
  - 15:173 the Spec Z displays carry his absolute ℍ, not H ("ℍ^i(Spec Z, Z(1)) = Z for i = 3; ℍ^i(Spec Z, Z) = Z
    for i = 0");
  - 15:176 "H^1(X, D^0_X) = 0" → "H^1(X, Div_X) = 0" (the vanishing behind Proposition 5.4, Br(X) ↪ Br(K)).
