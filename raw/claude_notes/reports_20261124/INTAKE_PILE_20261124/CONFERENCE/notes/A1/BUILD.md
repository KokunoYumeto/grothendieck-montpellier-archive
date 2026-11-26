# Build

Engine: pdfLaTeX (MiKTeX on this machine; any TeX Live with amsart, amsmath, amssymb, amsthm, mathtools, lmodern,
microtype, geometry, xcolor, hyperref, xurl). No BibTeX: the bibliography is inline.

    pdflatex -interaction=nonstopmode gt_monoid_note.tex
    pdflatex -interaction=nonstopmode gt_monoid_note.tex
    pdflatex -interaction=nonstopmode gt_monoid_note.tex

State of the build of 25 Nov 2026 (Claude Fable 5.2 at effort max, the conference convener): 8 pages, 0 overfull boxes,
0 underfull boxes, 0 undefined references (`gt_monoid_note.log`; `build_1.log` to `build_3.log` are the three passes).

Pages looked at: all eight pages of the first clean build were rendered at 88 dpi and read. After the last edits (one
word in the abstract, the lead sentence of Corollary D, the locator of the Lochak-Schneps definition in section 1.1 and
in the bibliography; one item removed from a list in the note on method) the note was rebuilt with three passes. Pages 1, 2, 7 and 8, which the edits touch, were rendered and
read again. Pages 3 to 6 begin and end with the same lines as the pages read before (first and last text lines of each
page compared with `pdftotext`). Images of the final build: `pages/p-1.png` to `pages/p-8.png`.

One mishap, repaired: a shell heredoc turned `\ref` into a carriage return in two places. Both were restored, the file
was checked to contain no carriage return, and the note was rebuilt.
