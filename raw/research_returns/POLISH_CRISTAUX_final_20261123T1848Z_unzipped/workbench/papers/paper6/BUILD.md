# Build

This standalone LaTeX project has one source file, `main.tex`, containing all mathematics and its bibliography. No external input, figure, or data file is required.

With pdfLaTeX and the standard TeX Live packages named in the preamble, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Without latexmk, run `pdflatex -interaction=nonstopmode -halt-on-error main.tex` twice. The result is `main.pdf`; BibTeX is not required. The document uses T1 Latin Modern fonts and author–date citations.

The optional exact algebra certificate `../../code/principal_theta_fraction_free.py` requires Python 3 and SymPy. It prints JSON and has no role in the LaTeX build. It uses fraction-free polynomial elimination over F2, independently of the earlier perfect-matching expansion. Its expected output is alongside the program. The companion `principal_theta_character_certificate.py` uses sparse linear constraints, saturated polynomial ideals and character orthogonality to verify the tensor dimensions, exceptional parameters and Fourier transformation; its expected JSON is also alongside it.

The final build and the page-by-page and two text readings are recorded separately in the audit. This text and code are CC0 1.0.
