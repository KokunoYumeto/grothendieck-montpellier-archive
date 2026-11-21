# Final PDF visual review — build 23

Run: TRACE_DET_20261121. Date: 21 November 2026. Reviewer: `/root`,
GPT-6 Astra Pro; effort setting not exposed. This record was written after
the review, during final release preparation.

## Reviewed artifact

- PDF: `TRACE_DET.pdf`, 81 pages, 1,007,106 bytes.
- PDF SHA256: `3def7f81cdc8fe4da551a4bdb2ead726b956071047400bf6c564409e2e51fe7e`.
- Standalone TeX SHA256: `e059ae1ec4061ebce92588dc8245b964ccb32581cf1ba02da9b3d623e71e2e60`.
- Successful compilation log: `work/latex_build_23.log`.
- Renderer: `work/render_final_qa.py`, using PyMuPDF at scale 1.25 and
  Pillow contact sheets. All 81 page images and seven contact sheets are
  retained in `work/pdf_qa_build23/`.

## Actual inspection scope

All seven contact sheets were viewed individually: pages 1–12, 13–24,
25–36, 37–48, 49–60, 61–72 and 73–81. The title and one-page contents were
also inspected at full rendered size in `work/pdf_qa_current/page_01.png`
and `page_02.png`; the full-size page 35 in the build-23 render was
inspected for the weighted-endpoint Mellin formula and script-font glyphs.
An attempted extra full-size view of page 65 was truncated by the display
context and is **not** counted as a completed inspection. Page 65 was
covered by the successfully viewed pages 61–72 contact sheet.

The review covered the title and abstract, contents, all proof sections,
long mathematical displays and source identifiers, conditional statement
table, framework table, Part II and bibliography. No clipped formula,
overlap, missing glyph, missing page or broken table was observed. The
framework table continues across pages 75–76 with a repeated header.
The ordinary bibliography continuation across pages 79–81 is legible.

The build has no unresolved reference, missing citation or overfull box.
Its single underfull paragraph warning (badness 1199, source lines
1402–1410, page 26) concerns long formal-source identifiers. The rendered
paragraph is readable and stays within the margins; it requires no
mathematical or layout repair.

## Result and limits

PASS for the final 81-page layout. The final TeX and PDF were not changed
after this review. This is a render-and-inspect layout check, not an
additional mathematical proof certificate. Whole-proof readings are
recorded separately in `CHECK_EVENTS.tsv`.

Earlier render folders and `work/pdf_qa_build16.md` document older
checkpoints; their 43-page review is not the final review.
