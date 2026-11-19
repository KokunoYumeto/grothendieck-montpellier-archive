# H0HW, the five-point object: what my topics hold

For the broad agent a0c4bb37f14505b26 (Claude Opus 5.5 at effort max), from agent ae4ae3dc (Claude Opus 5.5 at effort
max), horizontal sweep 2, part 2, 18 Nov 2026. Topics SA29, SA30, SA31, SA22, plus the control runs filed in SA28.

## The diagram and the problem (SA31-5, SA31-Q1; cote 148, scans 029–040)

- **The objects.** On 148/031 there are nine object orbits under Aut⁺ (order 120), of sizes 120/i:
  62 + 240 + 240 = 542. Checked in sweep 1.
  - The first row, 12 + 20 + 30 = 62, is the cell count of the dodecahedron of 146/077.
- **The arrows** (148/033, decided on the scan image; `img/148_033_table.png`, `img/148_033_sum.png`,
  `img/148_033_prog.png`).
  - The left-margin table lists fourteen named families in three blocks: 180 + 420 + 1020 = 1620.
  - Its sum reads 1620 = 5×60 + 11×120, corrected from an earlier 1500. That is sixteen S₅-orbits: five of size 60 and
    eleven of size 120. The family σ_r^{1′} counts 3×120.
  - The programme reads "1) déterminer un syst. fondamental de relations entre les 1620 flèches du diagramme, se
    partageant [entre, struck] 14 … sous 𝔖_K (aux 542 sommets, se partageant entre 9 orbites)".
  - So the page has fourteen families and sixteen orbits. Pro's note `MPL_148_029-072#1` ("fourteen stated arrow
    orbits") counts the families as orbits; corrected in `SA31/CORRECTIONS.tsv`.
- **The register.**

| Register statement | Status | Content |
|---|---|---|
| EXIT_TOWER B.12 | Proved | the nine vertex orbits and the corrected sixteen arrow orbits |
| EXIT_TOWER B.13 | Proved | the relations required by the diagram |
| EXIT_TOWER B.15, B.25 | Proved | a realization of all 542 objects and 1620 arrows |
| GT_TOWER_CHECK B.5 | Proved | rechecks B.25 |
| EXIT_TOWER B.31 | Proved | path choices; a nonuniqueness certificate |
| LM4_SUCCESSOR E.37 | Proved | the 542 objects |
| LM4_SUCCESSOR E.38 | Refuted | "fourteen S₅-orbits" |
| DELTA_ON_GT B.33 | Open | "the 1620 geometric arrows" |
| LM4_SUCCESSOR E.32 | Refuted | his inference on 148/035 that every finite antiholomorphic automorphism preserving five marks has order two |

## The boundary and the cells (SA30-6, SA30-7)

- **147/066–068 (SA30-6).** The boundary of the moduli of five points over Spec Z is a split stable curve with 10
  rational components and 15 nodes. Its graph is the "dodécaèdre gauche", the Petersen graph, of genus 6 (checked in
  sweep 1). The incidences on 147/070 disagree with it (flag).
- **146/077 (SA30-7).** 120 frames and 62 = 2(6 + 15 + 10) cells (checked in sweep 1).

## Around it

| Item | What it holds |
|---|---|
| SA29-18 (148/024) | canonical configurations and covering counts |
| SA29-Q1 | the order-five relation is not written on 144, 145 or 148/001–028; the notes of 143 (SA28) record the same absence |
| SA31-6 (148/041–072) | the operations on marks the arrows need: erasure, surmarking, cutting, and contracting cutting edges, called a "morphisme de générisation" on 148/054 |
| Control runs CTRL-148 and CTRL-148_2 (148/044–058) | they agree on his slips (A = A₀ for A_ℓ, r(ω) for r(a)) and on the total-genus formula of 049, which is checked |
| SA22-7 (67/076–085, B11) | in the 1984 welding notes, a "five-point coherence test" follows the four-holed-sphere comparison (B10): a return to the five-point case in January 1984 |

**Where the control runs differ:** on the margins of 148/053.
- CTRL-148 cannot read them.
- CTRL-148_2 reads "sont inverses l'une de l'autre, et sont des équivalences de groupoïdes".
- Pro's transcription has no such sentence. To decide on the scan.

## Still to decide

- **148/033:** which word after "14" is struck. The counts do not depend on it.
- **148/053:** the margins.
- **147/070:** the incidences.
