# Visual PDF verification

Second scheduled checkpoint, 20 November 2026. We rendered and visually inspected pages 1, 20, 40, 60, 76 of the 76-page current PDF. Body text, formulas, headings and bibliography fit the page; no clipping or overlaps were found. The final build had zero warnings and zero overfull boxes (0 exceeding 2pt, maximum 0pt). Before/after counts in both checkpoint builds were 0/0; no overflow pages required separate rendering.

PDF SHA256: 3c1ae59fcdbbd1e28f9a3f37b513d40a99f428412abc0464503999de39c570ca

Inspection completed 2026-11-20T01:42:41.953890+00:00.


## Third scheduled checkpoint

Completed 2026-11-20T02:27:10.155221+00:00. We rendered and directly inspected pages 1, 20, 40,
60 and 82 of the 82-page PDF. Headings, body text, mathematical displays,
footers and bibliography fit their pages, without clipping or overlap.
PDF SHA256: 4fa8689f698d0f8f45bc62834c2164860bcd07bda491f541473a733eb29b9af9.

The first attempt had one fatal bibliography typesetting error from two
unescaped underscores in agent names, and zero overfull boxes. We replaced
those metadata names by plain prose and rebuilt through LuaLaTeX/BibTeX/
LuaLaTeX/LuaLaTeX. All four commands returned zero. The successful build
had zero warnings, zero overfull boxes, zero overflows above 2pt, and a
maximum overflow of 0pt. Thus overfull counts before/after were 0/0;
there were no overflow pages requiring separate inspection. The failed
attempt's diagnostic and log are preserved under distinct names.


## Fourth scheduled checkpoint

Inspection completed 2026-11-20T02:59:18.299089+00:00. We directly displayed and inspected pages
1, 20, 40, 45, 46, 47, 60, 67, 78, 79 and 86 of the 86-page PDF. The
sample includes the new 1956 reconstruction, the expanded stack descent
argument, the remaining documentary gate and the final bibliography.
No clipping, overlaps, missing symbols or margin overflow was observed.
PDF SHA256: 05b380b1fec5c8d88b40fa9ebcddc7c6d0f76e7a4a576513468956ee9b3ded54.

The first preparation attempt stopped on an unescaped underscore in a
bibliography note, before producing a usable new PDF. The exact failed
logs are retained. We changed the plain-text metadata to k(n)=1 and ran
LuaLaTeX/BibTeX/LuaLaTeX/LuaLaTeX again; all four commands returned zero.
The successful build has zero warnings and zero overfull boxes, including
zero above 2pt, with maximum overflow 0pt. Overfull counts before/after
were 0/0. There were no overflow pages requiring a further separate sample.
The successful build took 21.324422570 seconds; rendering took
0.555323437 seconds. The earlier truncated image batch
was not counted as visual inspection: all eleven pages were subsequently
displayed one at a time and read.


### Fourth checkpoint: final bibliography build

The preparation PDF was subsequently rebuilt to include three additional
documentary bibliography entries and to repair observed spacing in notes.
Its 86-page visual record above is retained and is not substituted for this
new inspection. The delivered checkpoint PDF has **87 pages** and SHA256
**dfb88c55f097d18512bbccbb29882f86cf74b6c12e893b6ad9897a643c31afa4**. Inspection completed 2026-11-20T03:07:28.585176+00:00.

We displayed and inspected pages 1, 20, 40, 45, 46, 47, 60, 67, 78, 79 and
87 one at a time. No clipping, overlaps, missing symbols or margin overflow
was observed. All four compilation commands returned zero; warnings 0,
overfull boxes 0, overflows above 2pt 0, maximum overflow 0pt. Counts
before/after remain 0/0. There were no overflow pages requiring inspection.
Build time: 21.374059133 seconds. Render time:
0.487012971 seconds. All 85 bibliography entries have
an explicit opened or not-opened statement, qualified where only metadata
or a later source was inspected.


### Fifth checkpoint: final 96-entry bibliography build

The delivered paper has **90 pages**, SHA256 **f4c32598c77805631fcecf7fce909411c53583f2bffd7f0c14fa58d5fc5edab7**. Inspection
completed 2026-11-20T03:52:35.390252+00:00. We directly displayed fifteen page images individually:
root inspected pages 45, 46, 47, 49, 68, 79, 80, 81, 82 and 84; the algebra
agent inspected pages 1, 20, 40, 60 and 90. Its independent image-review
record is `notes/algebra_checkpoint05_visual_QA.md`. No clipping, overlaps,
missing symbols or margin overflow was observed. Page 81 carries the short
final scope paragraph before the bibliography break.

All four compilation commands returned zero. Warnings: 0. Overfull boxes:
0. Boxes above 2pt: 0. Maximum overflow: 0pt. Before/after counts remain
0/0, and no overflow pages required additional inspection. Build time:
21.216543657 seconds. Render time: 0.557759564
seconds. All 96 bibliography entries explicitly identify their access
status, with qualifications where only metadata or a later source was read.

The earlier preparation renders were not certified as viewed. An initial
final-tag render occurred before the last build finished; it was replaced
by the post-build render at 03:50:25 UTC before any inspection certification.
Only the final PDF hash above is covered by this record.


### Sixth checkpoint: 1951 notice and later documentary checks

The paper has **91 pages**, SHA256 **2a01da209cd326f1749883b29a1e00e8f0b5eb404f1cb17405b11881d5a7b906**. Actual inspection completed
2026-11-20T04:34:04.158144+00:00. Root individually displayed and inspected pages
45, 46, 47, 48, 49, 50, 68, 79, 80, 81, 82 and 85. The category agent
individually displayed and inspected pages 1, 20, 40, 60 and 91, with the
PDF, render-manifest and image hashes checked before and after its review.
Its exact record is `notes/category_checkpoint06_visual_QA.md`.

No clipping, overlap, missing glyph, illegible formula or margin defect
was observed. Page 81 carries the final scope discussion before the
bibliography page break. The changed historical comparison explicitly
includes the original 1951 announcement without identifying it as a proof
or assigning its date to the Montpellier sheets.

All four build commands returned zero. Warnings: 0. Overfull boxes: 0.
Boxes exceeding 2pt: 0. Maximum overflow: 0pt. Before/after counts are
0/0, so no overflow page required additional inspection. Build time:
21.513680344 seconds; rendering time:
0.689080408 seconds. All 103 bibliography entries
state their actual access status. This record applies only to the PDF
hash above and does not inherit an inspection from an earlier build.
