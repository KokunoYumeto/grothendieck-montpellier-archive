# Standalone build

Engine: pdfLaTeX (TeX Live with standard packages). Keep these twelve source files together: `main.tex`, `opening_supports.tex`, `opening_topology.tex`, `support_comparisons.tex`, `poset_topology.tex`, `lowdim_incidence.tex`, `event_domains.tex`, `opening_atlases.tex`, `atlas_representations.tex`, `support_distinctions.tex`, `optional_criteria.tex`, and `restricted_intersections.tex`. The bibliography is inline.

From a fresh copy of this directory run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No downloads are required. The resulting deliverable is `main.pdf`. Check `main.log` for unresolved references and overfull boxes. `SOURCE_MANIFEST.json` records the current input and PDF hashes. The reviewed build is 45 pages with no warnings.
