# Build

Engine: pdfLaTeX (MiKTeX 2026 on this machine; any TeX Live with amsart, amsmath, amssymb, mathtools, lmodern,
microtype, geometry, xcolor, hyperref, xurl).

    pdflatex -interaction=nonstopmode h09_note.tex
    pdflatex -interaction=nonstopmode h09_note.tex
    pdflatex -interaction=nonstopmode h09_note.tex

Three passes resolve the cross-references (no BibTeX: the bibliography is inline).

State of the build of 23 Nov 2026: 12 pages, 0 overfull boxes, 0 undefined references; every page rendered at 95 dpi
and read (Claude Opus 5.5 at effort max).

## Version 3 (23 Nov 2026 12:0x UTC, main session 329fb1e6, Claude Opus 5.5 at effort max)

h09_note_v3.tex = the editor's h09_note_v2.tex with one display corrected in §5.2: "pr_{i-1}-r_i = ((p-1)S_h-(q-1))/(q-1)
= 1" (that fraction is 0) now reads "(p-1)S_h/(q-1) = 1". Found in a full reading of v2 (every proof followed). Built
with three pdflatex passes: 12 pages, 0 overfull boxes, 0 undefined references; page 9 (the corrected display) rendered
and looked at. v2 is kept unchanged.
