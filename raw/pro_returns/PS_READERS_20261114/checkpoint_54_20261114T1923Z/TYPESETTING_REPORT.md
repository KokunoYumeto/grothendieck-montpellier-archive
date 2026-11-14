# Typesetting report

Work in progress. No final reader has yet passed the requested compile, overflow, link and visual checks.

## Latest whole-working-set apparatus proof

The 364-source-page apparatus proof (`logs/PS_EN_corrected_apparatus_readers_run006.log`) compiles successfully to 609 PDF pages. It has no missing characters and five overfull hboxes, widest 9.24255 pt. Three are below 2 pt; the two larger boxes are the reconstructed marginal corner/rule marks on cote 134-5/site 84. Their 30 mm rules are being shortened locally to 25 mm so that the complete mark fits the 28 mm margin; no mathematical diagram is rescaled. The PDF contains 1,988 archive-link annotations covering all 364 distinct checked source pages. The 364 scan, 1,215 doubt and 387 illegibility logical marks match the source exactly, including six nested marks sharing an outer link. This proof remains incomplete in scope and is not a final reader.

The separate 82-page cote 134-5 apparatus proof has one 1.38246 pt box and no missing glyphs; the repaired site 64 line and its apparatus continuation have been rendered and inspected. The separate 44-page cote 134-2 apparatus proof has one 1.91537 pt box and no missing glyphs. Their link counts match their respective sources. The guide proof through 322 checked pages compiled without overflows or missing characters; its expanded source is being built as additional sections finish.

## First successful whole-working-set proof

`logs/PS_EN_diplomatic_readers_run006.log` documents the 154-source-page diplomatic proof: LuaLaTeX exit 0, 157 PDF pages, five overfull hboxes, widest 18.79446 pt, no missing-character messages. The source pages with overflows were 134-5/2 and 134-7/52, /53, /63, /64. The 0.18546 pt excess on /52 is within the numerical limit but remains in the visual-review queue. The four larger-overflow pages were rendered and actually inspected; their observations are in `records/VISUAL_QA.json`. Local discretionary or zero-width breaks were added at the offending words and adjoining revision marks. The subsequent 134-7 proof passed those repaired paragraphs, with only the 0.18546 pt box remaining before it encountered an undefined wavy-underline macro on newly included page /66. That macro is now implemented with a breakable lua-ul underline pattern and is being checked.

The corrected-apparatus working proof reached the end of its 154 source pages, but its PDF export failed before the font-map repair. Its log recorded 12 overfull boxes, widest 18.79446 pt, and no missing-character messages. It has not yet passed final compilation or visual inspection.

## Repairs already made

The build removes redundant nested math delimiters, escapes TikZ matrix separators when a diagram is tokenized inside a macro argument, renders diagram labels in their proper context, preserves the separate lines of the front-matter contents, provides break opportunities in long runs of typewriter x overstrikes, and applies individually specified paragraph repairs. Mathematical content is unchanged by these mechanical operations. Explicit changes of reading and handwriting provenance are recorded separately in `CHECK_DECISIONS.tsv`.

All marginal notes carry calls. Notes exceeding three footnote-size lines of margin height are set in labelled ruled blocks; short notes remain in the margin. Math-mode marginal notes are queued until a safe text boundary, with a call at their original position. Their final placement is still subject to page-by-page inspection.

No global scaling pass, scaling below 70 percent, raised `hfuzz`, or deliberate suppression of overfull diagnostics has been used. Ink bounds, all landscape pages, the complete spread of reader samples, and PDF link counts remain pending.

## Evidence and final acceptance

`records/OVERFLOW_HISTORY.tsv` preserves overflows from every retained build, including failed or superseded builds. Final visual checks must cover the corresponding source pages even when repagination changes their physical page number. `records/VISUAL_QA.json` distinguishes actual inspections from images merely rendered. The final report will replace this progress report only after all five complete PDFs meet the stated requirements.

No working file has yet been intentionally omitted from the checkpoint collection. If intermediate proofs or redundant logs are excluded from the final packages, they will be listed here with their replacement and reason. Older compile logs still require a final privacy pass for wrapped system paths; current logs are sanitized by the compile wrapper.
