# Reproduction environment

The build uses LuaHBTeX 1.18.0, reporting TeX Live 2025/dev/Debian, with the
installed LaTeX2e 2024-11-01 patch level 2 kernel and L3 programming layer dated
2025-01-18. LuaLaTeX compiles the standalone sources directly.

The execution installation lacked its file databases, font-loading support and
French language files. `bootstrap_tex.py` provides an isolated support tree and
format, using the archived TeX Live 2024 final repository. The requested packages
are recorded in that script; the helper derives installation locations at run
time and changes no system installation. It removes no supplied source file.

The edition’s main font is Latin Modern Roman, with Latin Modern Sans for source
marks. `fontspec` is loaded with `no-math`, leaving the established Computer Modern
math font encodings intact, including Greek characters inside `\mathrm`. The
formula strings are unchanged by that setting.

The renderer uses LuaLaTeX's own node inspection to count the actual lines in a
footnote-size marginal-note box. This is embedded in each standalone source and
requires no external Lua file. Its three-/four-line boundary and deferred notes
inside groups are exercised by `python scripts/probe_rendering.py`.

`compile_readers.py` uses PyMuPDF for PDF link and geometry measurements. The
PDFs are rendered for visual inspection with PyMuPDF or Poppler. Python 3 and
standard-library modules provide source, TSV, JSON and archive processing.
`compile_readers.py` fixes `SOURCE_DATE_EPOCH` to 14 November 2026 at 00:00 UTC
unless the caller supplies another value, and enables `FORCE_SOURCE_DATE`, so
wall-clock compile time does not change the PDF creation date. Successful output
PDF hashes are recorded separately from the standalone source hashes.

The raw runtime format log, download caches, font cache and temporary compilation
folders are reproducible intermediates. Publication records contain sanitized
build logs, measured outputs, source hashes and visual-review observations.

The optional source-glyph tracing script uses Pillow, NumPy and Matplotlib to
record the contour transformation. Its output is ordinary embedded TikZ; none of
those Python dependencies is needed to compile a reader.
