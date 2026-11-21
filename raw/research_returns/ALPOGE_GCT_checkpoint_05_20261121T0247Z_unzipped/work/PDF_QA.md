# PDF verification record

2026-11-21, root: the 68-page checkpoint02 PDF was rendered and inspected in five contact sheets. All pages were reviewed for layout, clipping, overlap and gross rendering errors. A mostly empty third contents page motivated a compact contents layout.

2026-11-21 around 01:13 UTC, root: the expanded 89-page PDF through the initial P-F27 proof was compiled twice, rendered with PyMuPDF, and every page inspected in six contact sheets. No clipping or overlap was observed. A TeX-detected 13.6pt overflow in the run-in heading paragraph preceding P-F23 was removed by replacing the unbreakable Markov/Fibonacci expression with words. The final compile had no overfull warning. This is visual layout QA, separate from the full mathematical proof readings recorded in CHECK_EVENTS.tsv. The subsequent P-F27 connected extension and P-F28/P-F29 additions require a new render check.

2026-11-21 around 01:15 UTC, root: the final 94-page checkpoint03 PDF compiles twice without overfull boxes. Revised frontmatter pages1–3 and the added/refined sections on pages52–61 were rendered at increased scale and visually inspected in two contact sheets; equations, headings and body text are clear with no overlap or clipping. Other body sections retain their already reviewed layout, with pagination shifted.

2026-11-21 01:39UTC, root: the 103-page paper throughP-F32 compiled successfully in three passes. Updated opening, P-F30-P-F32 and open-gate sections were rendered (pages1,4,5,62-70,98-100) and every rendered page inspected in two contact sheets. No clipping, overlap or equation overflow was seen. The abstract wording was subsequently clarified to distinguish simple pole order from the exponential order of the root of unity.

## 2026-11-21T01:59:40.963803+00:00 — fourth-checkpoint expansion

Compiled the120-page paper twice without overfull boxes, undefined references, or rerun warnings. Rendered and visually inspected pages1 and70–91, covering P-F33–P-F38 and their surrounding transitions, in contact_03–05. No clipped formulas, overlapping text, or broken page layout was observed. The earlier reviewed pages and source-image correction remain documented above. A subsequent short P-F38q addition is being recompiled and its affected pages will be inspected separately.

2026-11-21T02:01:12.876561+00:00: Recompiled the final checkpoint text through P-F38q; no layout/reference warnings. Inspected the affected pages85–87 and later section/reference transitions on contact_06, and updated open-gate pages114–115 on contact_07. No clipping, overlap, or formula overflow observed. The final checkpoint PDF has120pages.


## 147-page build through P-F45 — 2026-11-21T02:36:26.992994+00:00

Three TeX passes completed successfully. The third log has no overfull boxes, undefined controls, undefined references or rerun warning. The initial build exposed a missing mathrsfs package declaration and one overlong P39 normalization display; both were corrected before the successful build. Root visually inspected contact08–13, covering pages1–3,85–115,140–147, including every newly integrated proof P39–P45, the64-entry cyclotomic certificate, the Hodge table, revised gates and references. Formulas, tables, tags and margins are clear and unclipped. P40's forward reference to the new global comparison was then updated; P46 will be rendered in the next build.


## 152-page build through P-F46 core — 2026-11-21T02:39:48.720588+00:00

Two TeX passes completed; the second log has no overfull boxes, undefined controls/references or rerun warning. Root visually inspected contact14–15 (pages95,113–119,145–148), including the updated P40 forward reference, every P46 formula and lattice/counting argument, the current disposition, revised open gates and their transitions. All inspected content fits without clipping. The optional unitary-lift interpretation is not yet in this compiled version.


## Final153-page checkpoint05 build through P-F46 — 2026-11-21T02:45:43.207563+00:00

The frozen P46 fragment matches the standalone source exactly. Two final passes compile without overfull boxes, undefined commands/references or rerun warnings. Root inspected contact16 (pages116–120,146–148) and contact17 (pages116–118,147 after the deck-embedding clarification): the full unitary lattice proof, formulas, source locators, section transitions and remaining gates are clean. The added deck-generator sentence is a convention clarification consistent with the whole proof.
