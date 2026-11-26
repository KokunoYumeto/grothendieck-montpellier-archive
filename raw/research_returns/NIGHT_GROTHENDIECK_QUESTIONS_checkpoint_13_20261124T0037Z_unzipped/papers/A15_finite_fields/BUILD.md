# Build

This is a standalone LaTeX project. Its sources are `main.tex`, `central_cm.tex`, and `companion.tex`; the bibliography is inline in `main.tex`. No local style files, figures, or external bibliography files are required.

Engine checked: pdfTeX 3.141592653-2.6-1.40.26, TeX Live 2025/dev (Debian), LaTeX2e 2024-11-01 patch level 2. Standard packages used: `lmodern`, `geometry`, `amsmath`, `amssymb`, `amsthm`, `mathtools`, `microtype`, `enumitem`, `natbib`, `xurl`, and `hyperref`.

From this directory:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. The verified draft has nineteen pages. The final build is made from a fresh copy of this returned source, and the resulting log is checked for undefined references and overfull boxes. Every PDF page is rendered and visually inspected.

## Recovery for an uninitialized TeX installation

The execution environment initially contained the TeX files but lacked the `pdflatex` format and font maps. No package installation was needed. A format was generated in a temporary directory with:

```sh
pdftex -ini -etex -interaction=nonstopmode -halt-on-error -jobname=pdflatex -progname=pdflatex pdflatex.ini
```

The resulting `pdflatex.fmt` was placed in the user's TeX variable tree under `web2c/pdftex/`, and `mktexlsr` was run on that tree. The following command generated the necessary maps from installed font files:

```sh
updmap-user --enable Map=lm.map --enable Map=cm.map --enable Map=cmextra.map --enable Map=symbols.map --enable Map=latxfont.map --enable Map=euler.map
```

These recovery steps are unnecessary on an ordinary configured TeX Live installation. The project itself uses only the two build commands above.

## Rights and scope

The paper's original text is dedicated to the public domain under CC0 1.0. Other authors' works are cited and linked, not included. The endomorphism invariants use Tate's positive-sign convention for abelian-variety endomorphisms.
