# Standalone build

Engine: pdfLaTeX with ordinary TeX Live packages. From a fresh copy of this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is inline. The five local TeX inputs must accompany main.tex. No downloads, shell escape, or bibliography processor are required. The resulting deliverable is `main.pdf`. Check `main.log` for unresolved references and overfull boxes. The current expanded 31-page draft was built with this three-pass sequence from a clean directory and every page was visually reviewed; environment-specific font-format setup is recorded only in the session build record.
