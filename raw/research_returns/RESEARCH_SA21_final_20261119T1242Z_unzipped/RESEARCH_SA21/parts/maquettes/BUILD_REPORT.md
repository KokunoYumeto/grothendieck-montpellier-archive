# Part C preflight build

The user-facing master is to be built by the root in LuaLaTeX. The local `build/maquettes_check.pdf` is a preflight check of the Part C fragment only, not the master deliverable.

Initial invocation failed before reading the fragment because pdflatex.fmt was absent. A local format was built with `pdftex -ini -jobname=pdflatex -progname=pdflatex '*pdflatex.ini'`; local map registrations for lm, cm, cmextra and symbols resolved the environment's missing default font map. No global configuration was changed. Logs are in `build/`.

The successful eight-page build had zero overfull boxes and zero underfull boxes, and no undefined citations or references. Zero boxes exceeded 2pt both before and after the successful source build; environment failures produced no usable layout. Pages1,3,5,8 were rendered and visually inspected, including the proof body and references. No clipping, collision or margin overflow was seen. A subsequent small explicit definition of incidence signs and dimension-rank wording was added to the fragment and is to be included in the root's final LuaLaTeX verification.

## Lua font-map diagnostic

The root master later reached all content pages but failed to embed msbm10 because the default font map was absent. The isolated `build/lua_font_check.tex` harness was compiled using the root's existing local LuaLaTeX format, without editing it. Direct registrations `\pdfextension mapfile {+lm.map}`, `+cm.map`, `+cmextra.map`, and `+symbols.map` produced a successful one-page diagnostic containing blackboard-bold R and C. The successful log embeds msbm10.pfb. The corresponding PFB is `/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/symbols/msbm10.pfb`. The root was also given the existing `rsfs.map` for its additional mathrsfs package. These are environment diagnostics; the transient diagnostic PDF is excluded from the deliverable package and is not the published research PDF. No aggregate diagnostic runtime was recorded.
