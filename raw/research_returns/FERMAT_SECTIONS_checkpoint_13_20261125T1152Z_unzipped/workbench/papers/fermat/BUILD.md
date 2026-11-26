# Build

Engine: pdfLaTeX (TeX Live, standard packages only).

From a fresh copy of this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Equivalent without latexmk:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is inline in `main.tex`; there are no local style files or figures.
The PDF is `main.pdf`. Mathematical checks are independent of TeX compilation.

The optional local input `identity.tex` is generated from the frozen editable
project by `tools/paper_identity.py` in the enclosing workbench. To create or
verify that identity from the workbench root:

```bash
python3 tools/paper_identity.py papers/fermat --create --utc YYYY-MM-DDTHH:MM:SSZ
python3 tools/paper_identity.py papers/fermat
```

Substitute the actual UTC freeze time in the creation command. Create the
identity after the final source edit and before the fresh PDF build. The
corresponding source manifest excludes the generated identity files and PDF;
the detached workbench manifest covers the final delivered files. A source edit
requires a new identity and a fresh build. Compilation also works before the
identity is created.
