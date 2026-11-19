# Les Dérivateurs XII, Théorème 2 (ms. p. 78), against the finding that it fails

Claude Opus 5.5 at effort max (agent a34c04448e8299803), horizontal sweep 2 part 2, 18 Nov 2026. Item SA32-31 (chapter
XII ms. 63-171, which holds Théorème 2). Item SA32-30 is chapter XII ms. 1-62. Image:
`grothendieck_archive_montpellier/21_derivateurs/157-3.pdf`, page 129.

## Where
| what | where |
|---|---|
| chapter XII in round D | cote 157-3 from scan 50 (ms. p. 1). K157-3-04 holds ms. 1-14; -05 ms. 15-30; -06 ms. 31-46; -07 ms. 47-62; -08 ms. 63-78; -09 ms. 79-94; -10 ms. 95-110; -11 ms. 111-125; -12 ms. 126-140; -13 ms. 141-155; -14 ms. 156-171 (scan = ms. + 51 in K157-3-08 to -09) |
| W(7) ("axiome du cube, ou lemme des cinq") and W(7 bis) ("axiome du carré cocartésien") | ms. 75-77, scans 126-128 (`K157-3-08_transcription.tex` L677-L700) |
| Proposition 6 and Théorème 2 | ms. 78, scan 129 (L838-L871) |
| his remark on the reverse implication | ms. 79-80, scans 130-131 (`K157-3-09_transcription.tex` L1-L45) |
| notes | `K157-3-08_mathnotes.md` U12, P6, Q5; `K157-3-08_notes.md` (row 129 (78)) |
| research | POLES B.8, G.2, B.7, A.10, G.4, G.8, G.9, G.15; DER_LOCALIZERS A.8; TOTAL_ASPHERICITY A.9, A.13, A.14 |

## What his pages contain (scan 129, decided on the image)
- "Proposition 6. L'axiome W(7) (lemme des cinq) implique W(7bis) (axiome du carré cocartésien)." The transcription marked
  the digit 7|8. On the image it is the same barred seven as in "l'axiome W(7)" two lines below.
- "Théorème 2. Le localiseur fond. W∞ satisfait à l'axiome W(7)."
- "C'est sûrement une conséquence du critère cohomologique d'Artin-Mazur, compte tenu des suites exactes de
  Mayer-Vietoris pour l'un et l'autre des deux carrés cocartésiens, et les variantes non commutatives de Mayer-Vietoris.
  Je n'ai pas fait la vérification en forme -- et devrais sans doute réparer cette omission."
  - On the image, "sûrement" and "du critère cohomologique d'Artin-Mazur, compte tenu" are inserted above the line.
  - "cohomologique" is my reading; the transcription offered cohomologique | homotopique.
- **ms. 79-80 (scan 130), his remark.**
  - The dual (cartesian) form of W(7 bis) fails for W∞.
  - The forward implication i₀ ∈ W ⇒ i ∈ W "doit être considéré comme allant de soi".
  - "Par contre l'implication inverse ... m'apparaît comme un trait très particulier du dérivateur HOT_W (quand il le
    possède), et notamment de HOT = HOT_{W∞}."

## What the notes say
- The Work and Codex notes record Théorème 2 as stated without verification: "Je n'ai pas fait la vérification en
  forme" (P6) and "devrais sans doute réparer cette omission" (Q5).
- They do not say whether it is true.

## Against the research runs: Théorème 2 is false as stated
- **Refuted.**
  - POLES:G.2: "XII Théorème 2, manuscript p. 78, and its interpretation of reverse excision as a property of ordinary HOT
    at pp. 79-80 are false. The forward clauses of W(7) and W(7 bis) hold for W∞."
  - POLES:B.8: W∞ satisfies none of W(7), W(7 bis), Loc (6 b) and Loc (6 c). It also refutes XVI Theorem 5.4 as far as it
    includes Loc (6).
  - DER_LOCALIZERS:A.8 ("XII Theorem 2 claims W∞ satisfies reverse cube excision": refuted).
  - TOTAL_ASPHERICITY:A.13: a finite sieve inclusion with a one-object complement.
- **Witness.** POLES:B.7: a finite category with 35 objects and 159 arrows whose classifying space is connected and
  integrally acyclic with π₁ ≠ 1. Homology, and so the Artin-Mazur cohomological criterion he invokes, cannot see this
  π₁. His suggested route through the cohomological criterion and Mayer-Vietoris is where the argument breaks.
- **What survives.**
  - Proposition 6, W(7) ⇒ W(7 bis): POLES:A.10.
  - The forward clauses for W∞: POLES:G.2.
  - For W_R (homology with coefficients R) both axioms hold: TOTAL_ASPHERICITY:A.14.
- **What depends on Théorème 2 (or on W(7 bis) for W∞) in chapter XII**, per POLES and its round-D folder:
  - Proposition 7 and the one-point-complement equivalence, ms. 84-85 (K157-3-09); Corollaries 4-5, ms. 149-151 (K157-3-13):
    POLES:G.4.
  - The reverse direction of Théorème 4(a), ms. 146-147 (K157-3-13), and Corollary 6(b), ms. 157 (K157-3-14): POLES:G.8.
  - The converses of Théorème 5, ms. 168 (K157-3-14): POLES:G.9.
  - The opening of §8, ms. 265, which reverses Proposition 6: POLES:G.15.
  - Outside XII: his §2.6 Proposition (K157-3-23) cites Cor. 4, p. 149 "moyennant (W 7 bis)". See
    `K157-3-23_contre_exemples_totale_asphericite.md`.

## Corrections and refinements (also in SA32/CORRECTIONS.tsv)
1. Status of XII Théorème 2: stated without proof by him ("pas fait la vérification en forme"); refuted.
2. Status of the remark of ms. 79-80: his interpretation of the reverse implication as a feature of HOT is refuted. The
   forward implication, which he calls "allant de soi", holds.
3. Reading: Proposition 6 is about W(7), not W(8) (image).
4. Status of the chapter-XII statements that use W(7 bis) for W∞: each must carry the hypothesis W(7 bis) (POLES:G.4,
   G.8, G.9, G.15).

## For sweep 3
- Read the round-D units of K157-3-09 to -14 at the places listed, and record each dependent statement with its
  hypothesis restored.
