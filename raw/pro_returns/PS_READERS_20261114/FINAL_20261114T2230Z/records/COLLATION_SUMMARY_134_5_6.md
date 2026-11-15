# Collation and guide handoff: reviewer 134-5/134-6

## Frozen scope

The assigned review comprises all 132 pages of cote 134-5, cote 134-6 sites 61–74, and cote 134-6 sites 81–124: 190 source pages in total. Each per-page record attests that both supplied original image halves were opened and inspected. The page-specific evidence is in `review_notes/134_5_6.jsonl`; `records/PAGE_REVIEW_134_5_6.tsv` indexes the completed reviews. No review is claimed for cote 134-6 sites 1–60 or 75–80, which belong to other reviewers.

The source/guide freeze contains 6,695 decision rows:

| Source identifier type | Rows |
|---|---:|
| Required witness-difference decisions, `DIFF` | 608 |
| Original doubtful-reading decisions, `UNSURE` | 696 |
| Original illegibility decisions, `ILLEGIBLE` | 167 |
| Per-page supplied-note decisions, `NOTE` | 1,278 |
| Recorded textual, provenance, graphic and mechanical changes, `CHANGE` | 3,756 |
| Reviewed-header metadata corrections, `META` | 190 |

The 863 original doubt macros receive 375 image-resolved decisions, 355 retained-doubt decisions, and 133 refined readings that retain residual doubt. The checked pages contain 508 `unsure` and 267 `illegible` macros, totaling 775. These counts include previously omitted obscured underletters, cancelled fragments, clipped readings and uncertain provenance now explicitly represented; they are counts of macros, not a count of distinct words. The records preserve the meaning of the original illegibility groups when a reading remains unresolved. Every retained `illegible` uses its required braced count.

`records/MASTER_VARIANTS_134_5_6.json` supplies 63 explicit variants in addition to the regular transformations of deletion, insertion and writing-over macros performed by the common builder. At freeze, every explicit before-span was present in its checked source. The helper rebuild assertions account for every required DIFF row, every original doubt macro and every supplied note field. All assigned keys are present, with no extra pages in this review file and no stale unreviewed header.

## Editorial handling

The scan governs all readings. The comparison witness does not settle a reading that remains obscured on the image. Author spelling, notation, literal indices, blank formula positions and unproved mathematical assertions remain in the checked text. The guide identifies mathematical discrepancies rather than repairing them in the source. Typed interlinear insertions and typewriter overprints retain explicit typed provenance. Mixed diagrams distinguish handwritten arrows from typed objects, and the recurring circled-star symbol distinguishes a typed star from its pen circle. Placement hooks and encircling strokes are represented as placement or graphics, without introducing editorial descriptions as manuscript words. Handwritten transpositions and reinstatements use explicit variants where the source order differs from the corrected reading.

The restored checkpoint and the reconstruction of the missing 61–65 work are documented by `scripts/recover_061_065_134_5_6.py`. That reconstruction used the earlier actual image observations and authored decisions, not a fresh claim of inspection from filenames. The immutable supplied inputs were restored and verified centrally before work resumed.

## Section guide

The completed guide contribution has 33 section entries, each with one body paragraph:

| File | Sections |
|---|---|
| `guide_sections/134_5_6.tex` | 67–91 |
| `guide_sections/134_6_middle_by_134_5_6.tex` | 102–104 |
| `guide_sections/134_6_tail_by_134_5_6.tex` | 105–109 |

Section 102 combines the other reviewer's page 378 evidence with this reviewer's pages 379–381. Section 104 combines this reviewer's pages 384–392 with the closing-page evidence for 393. Section 105 combines the reviewed handoff for 394–398 with this reviewer's 399–406; there is one complete entry, not separate opening and continuation entries. The shared evidence is indexed in `records/GUIDE_COVERAGE_134_5_6.json` and `records/HANDOFF_104_105_tail_134_3_4.md`. Previously verified local heading breaks remain in sections 90, 108 and 109.

The final middle-section paragraphs specifically distinguish the cancelled infinite additive-envelope duality on page 378 from its live finite counterpart; the tentative exactness-to-projectivity converse on page 381 from its rejection by flatness on page 410; the pseudo-topos/pseudocotopos hypotheses lost by the witness; the literal direct-limit wording on pages 386 and 389 from the projective-limit argument; the misplaced N naming the topos on page 390; the K/L differences in the exterior Hom formulas on page 392; the N/M shift at the 392–393 boundary; and the missing opposite in formula (37), given the explicit variance convention on page 385. Section 105 also separates the established presheaf duality from the tentative additive and reflexive generalizations.

## Local proof evidence and final-reader QA

The source-local diplomatic repairs for cote 134-6 sites 106, 110 and 113 have retained proofs, logs, images and actual visual observations in `records/VISUAL_QA_134_5_6.json`. The final source-local proofs recorded there compiled without overfull boxes or missing characters. Common full-reader builds and subsequent central normalization remain the root reviewer's responsibility.

The final corrected-apparatus PDF review is a separate stage. `scripts/record_final_app_qa_134_5_6.py` records only explicitly authored observations after selected page images have actually been opened, and checks the final PDF hash against the common selection manifest. Its output is `records/FINAL_VISUAL_QA_corrected_apparatus_134_5_6.json`. A selection or a prepared image is never itself a certification of visual inspection.
