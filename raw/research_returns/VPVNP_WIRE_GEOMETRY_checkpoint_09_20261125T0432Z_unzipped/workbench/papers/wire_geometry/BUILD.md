# Build

Engine: pdfLaTeX (TeX Live), standard packages only.

From this directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The main TeX file, all local inputs, inline bibliography, and resulting PDF
form a standalone editable paper. Final verification uses a fresh copy.

The original vector figure is included as `wire_networks.pdf`, beside
its own standalone TikZ source. To edit or reproduce it, run:

    pdflatex -interaction=nonstopmode -halt-on-error wire_networks.tex

The earlier Matplotlib generator is also included as editable original
figure code. To reproduce that alternative rendering, run:

    python draw_wire_networks.py --output wire_networks.pdf
