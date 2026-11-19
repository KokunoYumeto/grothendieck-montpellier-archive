# LuaLaTeX build reproduction

The environment initially had the LuaLaTeX executable but no format or usable
Lua font-loading runtime. We generated the format with:

```
luahbtex --ini --interaction=nonstopmode --halt-on-error --jobname=lualatex lualatex.ini
```

The `code/prepare_tex_runtime.py` script fetched the missing official TeX Live
packages into an isolated scratch `texenv` tree. The exact URLs, hashes, sizes,
times and outcomes are in the `logs/tex_runtime_fetch*.json` files. Its handling
of the mixed archive layouts was corrected after the first unsuccessful build.

The scratch font maps concatenated the installed maps `lm.map`, `cm.map`,
`cmextra.map`, `latxfont.map`, `symbols.map`, `rsfs.map`, and `euler.map`, with
the resulting text placed in `pdftex.map`, `psfonts.map`, and `psfonts_t1.map`.
No fonts were modified. The last addition fixed a missing Euler Fraktur font.

The reproducible final invocation was:

```
python code/build_paper.py --format /workspace/scratch/b00be283d10d/lualatex.fmt --texmf /workspace/scratch/b00be283d10d/texenv
```

On a complete TeX Live installation, `python code/build_paper.py` suffices.
The script makes three LuaLaTeX passes and one BibTeX pass, checks the final
log, and records a PDF hash. `code/render_pdf_qa.py` reproduces the rendered
pages; a human/model visual check is separately recorded, never inferred from
rendering. Runtime dependency trees and original sources are not deliverables.
