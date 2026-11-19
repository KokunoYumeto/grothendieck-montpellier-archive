# Final PDF verification

Reviewer: GPT-6 Astra (OpenAI, ChatGPT Pro mode), root integration run,
19 November 2026. This records actual AI visual inspection.

## Build checks

The first direct integrated pass found one overfull horizontal box:
20.98811 pt in the B.1--B.3 verification paragraph. Its unbreakable program
filename was replaced by a breakable path. An unrelated array parsing error
was corrected by using explicit left/right bracket commands in the B4 table.
A bibliography note containing an unescaped subscript was corrected before
the successful bibliography build. No failed-build PDF is delivered.

The final integrated build has 41 pages. Both final LuaLaTeX passes completed
with zero overfull boxes (therefore zero above 2 pt), zero missing characters,
and no undefined citations or references. The full logs and elapsed times are
in `logs/integrated_build.json` and the corresponding numbered build logs.

## Rendered-page inspection

We rendered every page with Poppler at 90 dpi and inspected all seven labelled
contact sheets, covering pages 1--41. We also directly inspected full-page
images spread across the text: pages 2, 8, 14, 20, 24, 28, 34, 36 and 41.
Page 34 contains the paragraph that originally overflowed; its program path
now breaks correctly and stays within the text width. Page 36 contains the
corrected finite-level table. Page 1 was also directly inspected in the earlier
render and its unchanged layout was checked in the final contact sheet.

The first complete rendering exposed a one-line contents spill and a
one-reference last page. Compacting the contents spacing and bibliography
font removed both, reducing the document from 43 to 41 pages. The final pages
have consistent margins, headers and footers, readable displays and tables,
and no visible clipping, overlapping text, or missing mathematical glyphs.

After the last editorial wording change on page 8, that page was rerendered
and directly re-inspected; all other final page images were compared with the
previous inspected rendering. Exact render and comparison metadata are in
`qa/render_manifest.json` and `qa/final_image_comparison.json`.

## Scope

This checks the rendered integrated paper. It is not a proof of the mathematics.
Only this PDF is included in the archive; temporary harness PDFs and fetched
source PDFs are excluded.
