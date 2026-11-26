# Build

This project is self-contained. `main.tex` contains its bibliography and uses only standard LaTeX packages. There are no local inputs, custom styles, figures, downloaded papers, or dependencies on another article in this workbench.

Engine used: pdfTeX 3.141592653-2.6-1.40.26, TeX Live 2025/dev/Debian, in pdfLaTeX mode.

From this directory, run three times:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The resulting file is `main.pdf`. Every delivered PDF is built from a fresh copy of this returned project. The build check rejects undefined references and overfull boxes above 2 pt; rendered pages are separately inspected.

The optional exact arithmetic certificate is independent of typesetting. From the workbench directory:

```bash
python programs/lifting_arithmetic.py --output lifting_arithmetic_result.json
```

It requires Python 3 and SymPy (checked with 1.14.0). Expected identities: all three involution differences are zero; the three characteristic-two minors are `x1*x2*x3`, `x2*x3**2`, and `x3**3`; the projective elliptic residual is `-8*(u**3+u**2+64)`; the discriminant is `-433`; the unique odd root modulo `2**64` is `1678045356210003903`. This verifies the explicit ingredients, not the existence of a particular final hypersurface or any comparison theorem.
