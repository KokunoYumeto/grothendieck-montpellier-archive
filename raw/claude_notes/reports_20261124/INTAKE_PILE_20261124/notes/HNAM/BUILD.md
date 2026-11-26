# Build

Engine: pdfLaTeX (MiKTeX on this machine; any TeX Live with amsart, amsmath, amssymb, mathtools, lmodern, microtype,
geometry, xcolor, hyperref, xurl). No BibTeX: the bibliography is inline.

    pdflatex -interaction=nonstopmode hnam_note.tex
    pdflatex -interaction=nonstopmode hnam_note.tex
    pdflatex -interaction=nonstopmode hnam_note.tex

State of the build of 24 Nov 2026, 23:5x UTC (Claude Fable 5.2 at effort max): 10 pages, 0 overfull boxes, 0 underfull
boxes, 0 undefined references (`hnam_note.log`; `build_1.log` to `build_3.log` are the three passes).

Pages looked at: all ten pages of the first clean build were rendered and read; after the last edits (the display in
Proposition 3.2, three sentences in §1.4, §1.7 and the note on method) pages 3, 4, 6 and 9 were rendered again at
95 dpi and read. The other pages have the same source text as when they were read. Images of the final build:
`pages/p01.png` to `pages/p10.png`.

One display was too wide in the first build (5.5pt, proof of Theorem 4.1); it is now two aligned lines.

Last edit (24 Nov 2026, about 23:10 UTC): Theorem A now says "for some eta in [1/2,1)" (one phrase on page 2). Rebuilt
with three passes: 10 pages, 0 overfull boxes, 0 undefined references, the same page breaks (first lines of every page
compared with the pages read).

Recheck rebuild (25 Nov 2026, Claude Opus 5.5 at effort high, agent a25c2acbb3a6f11f7): after the edits listed in its report (Toda wording p.4, zero-count attribution p.5, recheck sentence p.9, Table 1 locator p.10), three passes: 10 pages, 0 overfull, 0 undefined references. Pages 5, 9, 10 rendered at 80 dpi (pages_recheck/) and read.
