# Building the paper

Engine: pdfLaTeX, verified with pdfTeX1.40.26, TeXLive2025/dev/Debian. Every local input is included.

On standard TeXLive:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The current 118-page PDF was rebuilt in a fresh directory with three passes. This container required rebuilding the absent pdfLaTeX format and explicitly loading its installed cm,symbols,euler,lm font maps. The paper uses standard packages. The expanded standalone TeX is included. Full final visual and two-reading review remains pending.
