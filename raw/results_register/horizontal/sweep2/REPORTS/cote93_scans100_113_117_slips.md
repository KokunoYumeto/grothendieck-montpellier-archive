# Cote 93, scans 100, 113 and 117: three slips in the uniformization notes

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 18 Nov 2026.

**Verdict:** all three are his slips, not misreadings. The ink says what the frozen transcription says. The mathematics needs another sign, factor or word, and his own next lines use the right form.

## Where

| What | Where |
|---|---|
| His pages | Cote 93, scans 92-134: projective connections, the Schwarzian and uniformization |
| Scan images | `grothendieck_archive_montpellier/11_geometrie_et_topologie_combinatoire/93.pdf`, PDF pages 100, 113 and 117. A scan number is the PDF page; the archive's pencil number is one less (99, 112, 116). |
| Transcription and notes | Pro package MPL_93_092-134 (GPT-6 Astra, ChatGPT Pro mode): `grothendieck_archive_transcription_20261110/returns/MPL_93_092-134_unzipped/MPL_93_092-134/` (`_transcription.tex`, `_notes.md`) |
| The notes that raise them | A09 (entry #11) on 100; B11 (#28) on 113; C03 (#39) on 117; the list of open readings (#90) |
| Items | SA01-31: projective connections (= H03F, with SA04-9). SA01-32: the Schwarzian and G_0 (= H03D, with SA04-7). |

## The readings, decided on the scan images

I read each line on the PDF page at 300 dpi.

| Scan | The ink | Frozen transcription | Notes | Verdict |
|---|---|---|---|---|
| 100 | D(f dt) = a df/dt + b. There is no f after b. | The same | A09: a linear operator needs + b f, and Hua's modernization writes a f' + b f. | His slip: he left out the f. |
| 113 | log s' = −Λ(t) + cte; then s' = cte exp Λ(t), with no minus; then s = cte ∫ exp −Λ(t) dt + cte | The same | B11: the middle exponent must be −Λ, and scan 114 uses −Λ. | His slip: he dropped the minus sign. |
| 117 | H = Aut_C P¹(C) ≃ GP(1, C) = {(a b; c d) : ad − bc ∈ C*} "mod. matrices diagonales" | The same words | C03: the quotient is by scalar matrices; diag(2,1) acts by t ↦ 2t. | His slip of wording: "diagonales" where scalar matrices are meant. |

## The mathematics around them

What each line feeds, and why none of the slips spreads:
- **Scan 100.** In a local coordinate the operator is D(f dt) = a f' + b f, and λ_t = b/a is "la coordonnée principale". His pole conditions follow: simple poles, residue 2, no constant term (note A10). The polar-part criterion (A10, A14), the contact-element question (A15) and the Riccati coordinate of SA01-31 all use this. His next lines treat D as linear (λ = b/a, "a et b ne doivent pas être nuls simultanément"), so the missing f does not propagate.
- **Scan 113.** This is the developing map: s''/s' = −λ, so log s' = −Λ + c, s' = c·exp(−Λ), and s = c ∫ exp(−Λ) dt + c'. The solutions form a torsor under the affine group. The three equations of B12 (λ = −s''/s', G_t(s) = μ) and the linearization u'' = (μ/4)u of B13 use it, and so does the uniformizing equation (F01). The next line, and scan 114, use exp(−Λ).
- **Scan 117.** H = PGL₂(C) acts on P¹. The Schwarzian cocycle G is H × H-invariant (his I) and satisfies the chain law (his II); notes C01-C05 cover this. The torsor construction (C09), the canonical projective connection on P¹-bundles (C06) and the algebraic extension (C05) use it. Every later use takes H as the Möbius group.

I checked two consequences by hand in sweep 2 part 1, and both agree: B12, where α = s', λ = −s''/s' and 2λ' + λ² = G_t(s); and B13, where λ = 2u'/u gives u'' = (μ/4)u.

## What agrees and what conflicts

- The ink, the frozen transcription, the Pro notes (A09, B11, C03) and Hua's modernization (on 100) agree on what is written. The question was never what the ink says but whether he meant it, and the mathematics settles that.
- No two notes conflict.

## Corrections

These belong in the commentary; the transcription stays as the ink is.

| Scan | Read as |
|---|---|
| 93/100 | D(f dt) = a df/dt + b f |
| 93/113 | s' = c · exp(−Λ(t)) |
| 93/117 | H = invertible matrices modulo scalar matrices (PGL₂(C)) |

## Check events

Recorded in `sweep2/SA01/CHECK_EVENTS.tsv`: three readings checked on the scan image.
