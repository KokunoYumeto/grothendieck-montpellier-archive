# Cote 93, scan 52: exercise 22 a), a misreading in both transcriptions

Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, horizontal sweep 2 part 2, 18 Nov 2026.

**Verdict:**
- The typescript reads ‖yw − w‖ < ε.
- Both transcriptions read ‖yw − u‖ < ε: the Pro stage-A one (MPL_93_047-091) and the Work one (K93-07). This is a misreading.
- As typed, the exercise is true, and the proof is a few lines. It is the lemma behind Cohen's factorization theorem, and part b) is the theorem itself.
- The Work notes' "refutation" (M52) refutes the misreading. Their proposed intended reading (S52) is what the type says.

## Where

| What | Where |
|---|---|
| The page | Cote 93, scan 52: a reused typed leaf, upside down, numbered "− 35 −" and "n° 393". It holds exercise 21 (pseudo-resolvents) and exercise 22 (Banach algebras); the whole block is struck through by diagonal lines. |
| Scan image | `grothendieck_archive_montpellier/11_geometrie_et_topologie_combinatoire/93.pdf`, PDF page 52 (archive pencil 51), rendered at 400 dpi and rotated 180° |
| Transcriptions | Pro MPL_93_047-091 (`inputs/SA04/pro/MPL_93_047-091_transcription.tex`, and checkpoint 01) and Work K93-07 (`codex_web_20261113/returns/K93-07/out/K93-07_transcription.tex`) |
| Notes | Work K93-07: S52 (Slips) and M52 (Remarks of the model). Pro MPL_93_047-091: BT28-BT29 and BT51-BT53, which discuss 22 b) and its continuation on 050. |
| Items | SA03-21 (K93-07's remarks); SA04-2, the pseudo-resolvent and Banach-algebra exercises (= H02N) |

## The reading, decided on the scan image

The typescript reads:

> 22) a) Soient B une algèbre de Banach unipollente [sic, as typed], w ∈ B, C > 1 et ε > 0. Il existe η > 0 tel que les conditions u ∈ B, ‖u‖ < C, ‖uw − w‖ < η, 0 ≤ γ ≤ 1/4C impliquent ‖yw − w‖ < ε, où y = [(1 − γ)e + γu]⁻¹.

The letter after the minus in the conclusion was compared glyph by glyph, at 400 dpi:
- In this typeface w has a middle stroke, as in "uw − w" one line up.
- Its u has none, as in "‖u‖ < C".
- The disputed letter has the middle stroke: it is w.

## The mathematics: as typed, the exercise is true

My proof, using ‖e‖ = 1:
1. Put v = (1 − γ)e + γu = e + γ(u − e). Then ‖v − e‖ ≤ γ(‖u‖ + 1) < (C + 1)/(4C) < 1/2, since C > 1.
2. So v is invertible, with ‖v⁻¹‖ < 2.
3. Then yw − w = v⁻¹(w − vw) = −γ v⁻¹(uw − w).
4. Hence ‖yw − w‖ < 2γη ≤ η/(2C) < η, and η = ε will do.

With the misread conclusion ‖yw − u‖ the statement is false. Take B = C, u = 1, w = 0, γ = 0: then y = 1 and ‖yw − u‖ = 1. That is the Work notes' M52, and it refutes only the misreading.

**What the exercise is (my identification, from the statements):** 22 b) asks that, when A has elements u with ‖u‖ < C and ‖ux_i − x_i‖ < ε for any finitely many x_i (a bounded approximate identity), every z ∈ A factor as z = xy with y in the closure of Az and ‖z − y‖ < δ. That is Cohen's factorization theorem (P. J. Cohen, 1959), and 22 a), with γ = 1/(4C), is the step of its standard proof.

## What depends on what

- 22 b) uses 22 a) in its induction: "Appliquant a) dans Ã, déterminer par récurrence ...".
- The Pro notes (BT28-BT29, BT51-BT53) find two literal defects in the proof of 22 b) continued on 050. I have not checked those.

## What agrees and what conflicts

- The scan and Work S52 agree: S52 proposes ‖yw − w‖ as the intended reading.
- Both transcriptions and Work M52 disagree with the scan: the transcriptions read u, and M52 refutes that reading.

## Corrections

- **The transcriptions** of 93/052 (Pro MPL_93_047-091 and Work K93-07): read ‖yw − w‖ < ε.
- **SA03-21's flag from part 1** ("an error of the typed exercise or of the reading") is decided: it is a misreading.
- **M52's refutation** is withdrawn: it applies to the misreading.
- **The exercise as typed** is proved above.

The leaf's typed numbering ("n° 393", "− 35 −") belongs with the numbered typescripts found on cote 91 (n° 285, 316, 371) and cote 102 (n° 387). That they are Bourbaki rédactions is my inference, not checked.

## Check events

- **In `sweep2/SA03/CHECK_EVENTS.tsv`, for work:K93-07#6:** the reading checked on the scan image; the exercise as typed proved.
- **In `sweep2/SA04/CHECK_EVENTS.tsv`:** the Pro transcription of 93/052 checked against the scan, which it misreads.
