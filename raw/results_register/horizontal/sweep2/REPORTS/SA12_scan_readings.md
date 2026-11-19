# SA12: ten readings decided on the scans

18 Nov 2026, about 22:05 UTC. Written by Claude Opus 5.5 at effort max, a sub-agent of the broad agent a0c4bb37 (Claude Opus 5.5 at effort max), in horizontal sweep 2 for topic SA12 (Séminaire de Géométrie Algébrique).

## Summary
| # | Place | Decision |
|---|---|---|
| 1 | 29/139 | "Sans rigueur" confirmed. He marked Proposition 4 himself. |
| 2 | 29/142 | His warning that reducedness is lost: confirmed. |
| 3 | 29/183 and 181 | The "?" under ≃, "néc et suffisantes" and "[compact ?]": confirmed. |
| 4 | 29/041 | "prouvé", not "présumé". |
| 5 | 31/020 | The "<" is in the ink: his slip for ≤. **New:** the transcription misreads "cd(X_Q) ≤ 2 dim X_Q + 2" as "+1". |
| 6 | 33/023 | "(12 + 1)" is typed: a slip of the reused typescript, which should have 11. |
| 7 | 33/075 | "α1 + α2" and "(3 ≤ i ≤ 8)" are typed: slips of the reused typescript. |
| 8 | 33/090 | Both projection displays are as transcribed: one slip (F inside R^!f) and one shorthand (no f^*). |
| 9 | 37/094 | "J'ignore donc si la notion 'formellement lisse' est vraiment locale en haut !": confirmed. |
| 10 | 29/125 | The month in "18.?.1959" is not decided on the ink. The shape leans to 6; Hua reads août (8). |

## How the scans were read
- The scans are the archive PDFs `grothendieck_archive_montpellier\05_seminaire_de_geometrie_algebrique_sga\<cote>.pdf`.
- Each page was rendered with `pdftoppm` at 130-300 dpi and cropped with `magick`. The PDF of 29/125 embeds its image at 229 dpi, so higher renderings add no detail.
- **Scan number = PDF page number.** PDF page 139 of 29.pdf carries Proposition 4, exactly as the transcription's `\scanpage{139}`, and its footer shows the archive foliation 138. The same offset holds for every page used below.
- Each decision is a check event in `sweep2\SA12\CHECK_EVENTS.tsv` and is noted in `sweep2\SA12\FLAGS.tsv`.

Short names used below:
- `pro\`: `results_register\horizontal\inputs\SA12\pro\`
- `codex\`: `results_register\horizontal\inputs\SA12\codex\`
- `returns\`: `grothendieck_archive_transcription_20261110\returns\`

---

## 1. Cote 29, scan 139: the margin at Proposition 4 (F7)
- **Transcription:** `pro\MPL_29_095-140_transcription.tex`, line 855: `\margin{\unsure{Sans rigueur} …}`.
- **The proposition:** "Si α ∈ Z(a,G) est minimal, alors u ↦ u_*(α) de Hom_S(G,G') dans Z(a,G') est injective."
- **What the notes said:**
  - Work K29-08 and the Codex notes K29-08 leave open "Sans rigueur" or "Sens rigoureux".
  - Pro note N033 (package MPL_29_095-140) refutes the proposition in its repaired form over the cusp y^p = x^(p+1) in characteristic p.
- **What the ink shows:** two words written slanting in the left margin, beside a vertical bar that marks the statement.
  - The first word has four letters, S·n·s ("Sans" or "Sens").
  - The second begins "rig" and has four more elements after the g. That fits "rigueur" (7 letters), not "rigoureux" (9 letters).
- **Decision:** reading confirmed, "Sans rigueur".
- **What it changes:** he flagged Proposition 4 as not rigorous himself. This agrees with his warning on 29/142 (reading 2) and with the cusp counterexample to the repaired statement. Proposition 4 should be recorded as a statement he marked himself, and not as an error discovered against him.

## 2. Cote 29, scan 142: the warning on reducedness (F23)
- **Transcription:** `returns\MPL_29_141-187_unzipped\MPL_29_141-187\MPL_29_141-187_transcription.tex`, line 78.
- **What the notes said:** Pro note N142.1 (package MPL_29_141-187) cites the warning and says that Hua's modernised reading omits it.
- **What the ink shows:** "[Attention, on perd le fait que S est réduit, S₁ ne l'est plus]." The script is abbreviated, but every word is accounted for.
- **Decision:** reading confirmed.
- **What it changes:** the proof of Proposition 4 passes to S₁ = P, which is not reduced, and he says so. Together with reading 1, his own pages carry two warnings at the step where the cusp counterexample bites.

## 3. Cote 29, scans 183 and 181: reconstruction of a pro-object (F26)
- **Transcription:** `MPL_29_141-187_transcription.tex`, line 1369 ("F(I) \underset{?}{\simeq} C(K,I)"), line 1396 ("Ces conditions sont néc et suffisantes") and line 1264 (on 181: "espace [compact?]").
- **What the notes said:** Pro note N183.1 refutes "suffisantes" when K is not compact. Its counterexample is K = ℕ^ℕ with the continuous map x ↦ x_{x₀+1}, which factors through no finite stage. N183.3 repairs the statement with finite stages.
- **What the ink shows:**
  - On 183, "F(I) ≃ C(K,I)" has a "?" written under the ≃, and "K espace top. tot. discontinu" stands beside it. Lower down: "Ces conditions sont néc et suffisantes, et on pourra prendre K = lim π₀ᵢ".
  - On 181, "π₀(K) = espace [~~~?]": a bracketed word ending in a clear "?". "compact" fits the strokes.
- **Decision:** reading confirmed.
- **What it changes:** his own question marks sit exactly where the claim fails. The comparison F(I) ≃ C(K,I) needs K compact, and with finite stages it is right. The refutation in N183.1 is of the unqualified wording, which he had already queried.

## 4. Cote 29, scan 041: "prouvé" or "présumé" (F20)
- **Transcription:** `codex\K29-01_transcription.tex`, line 99: "b) Le cas ``type fini'' est \unsure{prouvé|présumé} [réduction au cas normal …".
- **What the notes said:** the Codex notes K29-01 leave the status word open, and the two readings give opposite statuses.
- **What the ink shows:** "p-r-o-u-v-é", with the closing accent. There is no tall s and no three-humped m, which "présumé" would need. The cancelled earlier line above also reads "le type fini est prouvé".
- **Decision:** "prouvé"; the first reading is confirmed.
- **What it changes:** on this "Finitudes" sheet he records case b) "type fini" (finite generation of the prime-to-p π₁ for X of finite type over k) as proved. The proof sketch follows in brackets: descent, the nonsingular case "joli au sens d'Artin", the homotopy exact sequence, and reduction to a normal curve. The stronger "présentation finie" is not claimed.

## 5. Cote 31, scan 020: "cd(X) < 2 dim X + 1" (F4), and a misreading found on the same line (F32)
- **Transcription:** `pro\MPL_31_002-051_transcription.tex`, line 609: "\mathrm{cd}(X)<2\dim X+1,\ \mathrm{cd}(X_{\mathbb Q})\leq2\dim X_{\mathbb Q}+1,\ \mathrm{cd}(X_{\mathbb R})\leq2\dim X".
- **What the notes said:** Pro note N030 shows that the strict "<" fails for X = Spec 𝔽₃, where cd = 1 and dim X = 0, and asks whether the sign is a slip.
- **What the ink shows:**
  - "cd(X) < 2 dim X + 1" has a plain "<". The neighbouring "≤" signs on the same line carry a clear bar.
  - The second bound reads "cd(X_Q) ≤ 2 dim X_Q + 2". Its final figure is a 2, written like the other 2s on the line, and is not the short vertical stroke of the 1 in "X + 1".
- **Decision:**
  - The "<" is in the ink: the transcription is right, and the "<" is his slip for ≤. The deleted line (ii bis) above it has "≤ 2 dim X + 1 (resp. ≤ 2 dim X + 2)", and SGA 4 X 6.2 has ≤.
  - The X_Q bound is a **misreading in the transcription**: the ink has "+2", the transcription "+1".
- **What it changes:**
  - The theorem on this page should read cd(X) ≤ 2 dim X + 1 and cd(X_Q) ≤ 2 dim X_Q + 2.
  - "+2" is the correct bound: a number field has cd 2 when X(ℝ) = ∅. "+1" would be false; X_Q = Spec ℚ(i) already gives cd 2 > 1.
  - The transcription of 31/020 should be corrected to "+2" (F32).

## 6. Cote 33, scan 023: the E6 exponent product (F2)
- **Transcription:** `pro\MPL_33_002-049_transcription.tex`, line 622: "(m+1)(m'+1)(1+1)(5+1)(7+1)(12+1)=2^7.3^4.5".
- **What the notes said:** Pro note N53 shows the equation is impossible mod 13 and points to the exponent 11.
- **What the ink shows:**
  - A reused typescript, page "- 218 -", numbered "n° 391".
  - "(m + 1)(m' + 1)(1 + 1)(5 + 1)(7 + 1)(12 + 1) = 2⁷.3⁴.5" is clearly typed with "12".
  - The line above reads "m + m' = 12".
- **Decision:** reading confirmed. The 12 is a typing slip of the source, not a misreading.
- **What it changes:** nothing in the transcription. With (11 + 1), the two equations m + m' = 12 and (m+1)(m'+1) = 45 give m, m' = 4, 8, so the E6 exponents are 1, 4, 5, 7, 8, 11. The slip belongs to the reused typescript, a Bourbaki-type draft numbered n° 391 (my inference), not to Grothendieck.

## 7. Cote 33, scan 075: the E8 plate (F24)
- **Transcription:** `returns\MPL_33_050-097_unzipped\MPL_33_050-097\MPL_33_050-097_transcription.tex`, line 802 (the paragraph after `\scanpage{75}` at line 787).
- **What the notes said:**
  - Pro note N44 (package MPL_33_050-097) says "α1+α2" should be "α1+α3".
  - Pro note N70 says the range "(3≤i≤8)" invokes an undefined α9.
- **What the ink shows:** the same typescript, page "- 210 -", "n° 391".
  - "… enfin, α₁ + α₂ a la même forme que α₁ sauf qu'on y a permuté ε₁ et ε₂ …" is typed with α₂.
  - "(α_i|α_{i+1}) = (α₂|α₄) = (α₁|α₃) = −1, (3 ≤ i ≤ 8)" is typed with 8.
- **Decision:** both readings confirmed. Both are slips of the source typescript.
- **What it changes:**
  - Nothing in the transcription.
  - Mathematically, α₁ + α₃ = ½(ε₂+ε₈) − ½(ε₁+ε₃+…+ε₇) is α₁ with ε₁ and ε₂ permuted (recomputed here). α₁ + α₂ has coefficient 3/2 at ε₁. The range ends at 7.
  - With reading 6, the n° 391 typescript (pages 210 and 218) carries three such slips.

## 8. Cote 33, scan 090: the projection formulas (F25)
- **Transcription:** `MPL_33_050-097_transcription.tex`, lines 1457-1470.
- **What the notes said:**
  - Pro note N24: the first display "places R^!f(F•) inside the right-hand internal Hom" and is ill-typed.
  - Pro note N25: the tensor display "G•⊗^L F•" under a direct image omits the pullback of G•.
- **What the ink shows:**
  - First box: "ℝHom(ℝ_!f(F.), G.) ≃ ℝf_*(ℝHom(ℝ^!f(F.), G.))". The letter inside ℝ^!f is the same F as on the left.
  - Third box: "G. ⊗^L ℝf(F.) ≃ ℝf_*(G. ⊗^L F.)", with an overwritten shriek or star, and the margin "si G. loc. libre (peut se généraliser à G. loc. constant …)".
- **Decision:** both readings confirmed.
  - The first is his slip. The intended right side is ℝf_* ℝHom(F., ℝ^!f G.), the sheafified global duality.
  - The second is his shorthand: G. stands for f^*G..
- **What it changes:** nothing in the transcription. A reconstruction states the duality isomorphism with the arguments in place, and the projection formula with f^*.

## 9. Cote 37, scan 094: the formal-smoothness question (F31)
- **Transcription:** `grothendieck_archive_transcription_20261110\codex_web_20261113\returns\B37-05\out\B37-05_transcription.tex`, line 263.
- **What the notes said:** the Codex notes B37-05 quote the sentence.
- **What the ink shows:** a typed letter to Dieudonné (the letter opens on 37/093, dated 22.8.1967). It reads:
  - "J'ai découvert un canular ennuyeux dans EGA IV 17.1.6 (i) … la démonstration via (16.5.17) ne marche que si on suppose ¹_{X/Y} de présentation finie …"
  - "J'ignore donc si la notion 'formellement lisse' est vraiment locale en haut !"
  - The question is reduced to whether a module that is locally projective on Spec(A) is projective, a question he had put to D. Lazard.
  - The Ω before ¹_{X/Y} is left blank by the typist.
- **Decision:** reading confirmed.
- **What it changes:** it is his own open question of 1967, recorded as item SA12-68. A literature lead, not checked here, is Raynaud-Gruson on the descent of projectivity.

## 10. Cote 29, scan 125: the date of the letter to Serre (F16)
- **Transcription:** `codex\C29-06_transcription.tex`, line 106: "\unsure{Vallouin|Valloire|Vallouise} 18.\unsure{6|8}.1959".
- **What the notes said:**
  - The Codex notes C29-06 leave the place and the month open.
  - Hua's modernised reading heads the letter "Lettre à Serre, 18 août 1959", as cited by the Pro note N143.3 of MPL_29_141-187.
- **What the ink shows:**
  - A handwritten dateline above the typed "Mon cher Serre;": "V·llou·i· 18.?.1959".
  - The month digit is shorter than the 8 of "18". It has an open, hooked top and a closed lower loop, while the 8 of "18" has two closed loops. By shape it leans to 6, but an 8 with an open upper loop cannot be excluded.
  - The place word begins "Vallou"; its ending is too compressed to decide.
- **Decision:** not decided on the ink. The double reading "18.6|8.1959" is kept, with the ink leaning to 6 and Hua reading 8.
- **What it changes:** the letter is of 1959 in either case, June or August, and that date is secure. To settle the month, compare the printed Grothendieck-Serre correspondence (not checked here).
