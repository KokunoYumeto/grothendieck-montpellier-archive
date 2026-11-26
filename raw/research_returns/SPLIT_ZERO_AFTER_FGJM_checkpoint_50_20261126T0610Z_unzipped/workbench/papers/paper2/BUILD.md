# Build and verification

Run from this directory with a standard TeX Live installation:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The tested engine is pdfTeX1.40.26 (TeX Live2025/dev). The preamble lists all standard package dependencies; bibliography entries are embedded. Include every local TeX input and the figures directory where present. No source download is required to build.

The current fresh build has 25 pages, zero overfull boxes, and no undefined references or citations. All pages have been inspected. Expert and newcomer readings are documented in the review record; independent theorem checks remain separately typed. The original execution environment required regeneration of its absent pdflatex format and explicit TeX/font-map roots, an environment repair that is not a manuscript dependency.

Current PDF SHA-256: 09fc5ae53d56ea42275296052cf74325e87d681517124216328daf38bf84e12c. Current all-input hashes and fresh-build location are recorded in checks/paper2_checkpoint7_build.json.

## Current verified build (2026-11-24T19:25:18.288078+00:00)

25pages, fresh three-pass build, no overfull boxes and no undefined references or citations. MainTeX SHA256 `547f47008ebbaf647af81c74bff1854f3751d774d671098d3426388a5a4d6fb4`; PDF SHA256 `826c177459e0bcf07728b7a87e330538c85c053433c2bc9c7082d3b7f99653cd`. The final section now explicitly separates unconstructed arithmetic support lifts from the scalar identities. Changedpages24–25 were inspected individually; other23rasters are byte-identical to the preceding fully inspected PDF. Expert/newcomer revision readings are recorded in checks/paper2_checkpoint8_build.json.

## Current verified build (2026-11-24T20:26:52.395567+00:00)

25 pages, fresh three-pass build, no overfull boxes and no undefined references or citations. Main TeX SHA256 `abaee615652883c59a464877d51b3fcd19f694bb50ba7728a939a744a1de8cab`; PDF SHA256 `e01e1cb41745bf06b45f75b8300435562cccee7d6daa49da9ad8b8109dde08c2`. All25pages were visually inspected after adding the public foundation citation. Expert reading verified the source-credit correction and its exact locators; newcomer reading verified the distinction between the known unweighted formula and the weighted extension. No mathematical claim was changed. Full current hashes and review evidence: checks/paper2_checkpoint9_build.json.
