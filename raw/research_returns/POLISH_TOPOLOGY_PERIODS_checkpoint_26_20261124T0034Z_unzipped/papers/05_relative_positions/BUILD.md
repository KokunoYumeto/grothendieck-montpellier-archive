# Build the standalone paper

Run in this directory with a normal TeX Live or MiKTeX installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Keep `main.tex`, `extension_comparison.tex`, and `polygon_invariant.tex` together. The latter two files are local mathematical sections. The bibliography is in `main.tex`; BibTeX and downloaded references are not required. The standard packages are geometry, fontenc, lmodern, amsmath, amssymb, amsthm, mathtools, microtype, booktabs, array, longtable, xurl, and hyperref. No shell escape, network access, nonstandard class, image, or source appendix is required.

The checked build used pdfTeX 1.40.26 and LaTeX2e 2024-11-01. A normal installation supplies its own format and font maps. Temporary runtime paths used by the preparation environment are not part of the paper.

## Numerical checks

From the containing deliverables directory, follow `checks/paper5/README.md`. The fifteen-matching theorem also has its complete proof and all fifteen cases in the paper itself.

## Preceding reviewed revision (10:01 UTC)

The 41-page revision was built from a fresh copy of all three TeX inputs on 2026-11-23T10:01:51.404504+00:00. Three final pdfLaTeX passes have no warnings, undefined references/citations, or overfull/underfull boxes. Root actually viewed all changed pages: 7 and19–41. Pages1–6 and8–18 are pixel-identical to the preceding reviewed39-page PDF at108dpi. The final method-note layout changes only pages40–41, both re-viewed; pages1–39 were compared again and are pixel-identical to the staged reviewed pages. The changed mathematical text was read for proof validity and newcomer clarity. Full hashes and page comparisons are in notes/paper05_scope_reconciliation_release.json.

Preceding main.tex SHA256: `641f731dcd170b1324acc4beac226a8fdae64e41b3b05961b9970337f3083fbb`. Preceding main.pdf SHA256: `662957ecaa45eb3bd37cce399cd96389dcf09665288cabd4ada3b67cfc0950a3`.


## 2026-11-23T10:35:52.656355+00:00: independent incidence release

The current synchronized PDF remains41pages. Only page20 changed and was actually inspected; the other40pages have identical pixels to the preceding reviewed pair. Three pdfLaTeX passes succeeded, final log clean. The new named program **Incidence polygon gluing** independently reconstructs every finite endpoint pairing from extension incidences. All721faces,1592paired sides and6368endpoint flags agree; independent homology now uses these new pairings. Records: `../../notes/paper05_incidence_gluing_audit.md` and `../../notes/paper05_incidence_release.json`. Seven exact source scopes are accepted; C06 identification and the signed-polygon main gate remain separate.

Current source SHA256: `8a386a192b197e3a2465ece5153e1cf60741fd77b05000f6e86b04c77863dbc7`. Current PDF SHA256: `79c2a88b5188c6394166cac98223dc3557e5b21a170ff9c0e8a1b8ffb3d9f61c`. No external deposit.
