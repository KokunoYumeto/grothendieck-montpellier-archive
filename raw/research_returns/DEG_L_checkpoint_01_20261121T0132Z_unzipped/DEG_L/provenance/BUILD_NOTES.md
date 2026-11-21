# Build notes

The manuscript source is complete enough for checkpoint review but is still being updated during active research. It is assembled by `code/build_paper.py`; the component reports retain detailed source and check commentary.

Tectonic could not fetch its uncached default bundle (HTTP403). A local pdfTeX format was successfully built using the installed TeX tree with explicit TEXINPUTS and TFMFONTS. Normal filename-database lookup was not finding installed files. The first full build reached a missing `lmodern.sty` path; the next build should add `/usr/share/texmf/tex//` to TEXINPUTS and matching font paths, or use an available font family. No successful PDF compile or visual verification has yet been recorded.

The source TeX is the requested deliverable; an optional PDF will be provided only after successful rendering and inspection.
