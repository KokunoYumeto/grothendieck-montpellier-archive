# A01--A35 compilation and visual review

Date: 2026-11-21. Build owner and primary layout reviewer: GPT-6 Astra Pro, effort not exposed, `/root/effective_galois`. Independent new-page layout reviewer: GPT-6 Astra Pro, effort not exposed, `/root/gt_certificates`.

**PASS.** This audit records compilation, layout review, artifact hashes and structural package validation. It is not a new mathematical proof reading or a claim of formal verification.

## Frozen source and compiled reading copy

- Source: `final/AN_GRH.tex`, SHA256 `28f6eea75623e702cc9b3a76edab3334cdcea1356a6a0ec814c3ad9415f34ec7`.
- PDF: `final/AN_GRH.pdf`, SHA256 `4d7f909477553080831e2df00e0a427803f67311e8886b8a078b7436f1d913ad`.
- Length: 102 pages.
- Three successful, stable XeLaTeX passes, with process-local TeX filesystem roots and shell escape disabled, using the retained format.
- Zero overfull boxes, unresolved references, missing-character notices or remaining rerun requests. The retained log has only underfull-spacing warnings and the existing amsmath notice concerning the legacy `over` command.
- **No source or layout changes were made during this freeze.**

Reproduction command:

```sh
python final/reproduce/compile_standalone_tex.py --source final/AN_GRH.tex --build-dir work/effective_galois/tex_build/a01_a35 --format-dir work/row_audit/tex_build
```

Render command:

```sh
python work/row_audit/tex_build/render_qa.py work/effective_galois/tex_build/a01_a35/AN_GRH.pdf work/effective_galois/tex_build/a01_a35/qa
```

## Actual visual review

Rendered every page with `pdftoppm -scale-to 1600 -png`. I inspected every one of the 102 pages in twelve contact sheets. I additionally inspected these 23 pages individually at full rendered size:

1, 6, 10, 12, 49, 78, 79, 81, 82, 88, 89, 90, 91, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102.

The separate GT reviewer inspected all fifteen new pages 63--77 individually at full rendered size. Their audit is `work/gt_certificates/positive_rank_theta/PDF_A32_A35_PAGES63_77_VISUAL_QA.md`, SHA256 `86a2c2d349cf02a96ddf0feb044a67557979969e4e9c525be77f5677898e28ac`. Both reviewers recomputed or checked the exact source and PDF hashes.

Neither reviewer observed clipping, overlapping text or mathematics, missing glyphs, equation-tag collisions, broken table boundaries or margin overflow. The dense OR/DR/BE/TF displays, long source-name tables and multi-page bibliography are legible. This combines all-page contact-sheet coverage with 38 distinct full-size page inspections; it does **not** claim that all 102 pages were inspected at full size.

## Installation and preserved history

Installed only after both visual reviews passed, using `work/effective_galois/install_a01_a35_build.py`. The current manifest is `final/evidence/build/manifest.json`; the matched source, PDF, compilation record, all three pass logs, page map, rendering record, every page-render hash, all twelve contact sheets, all 38 full-size reviewed page images, independent audit, and layout-change record are retained under `final/evidence/build/a01_a35/`.

The earlier matched 88-page A01--A31 source/PDF and evidence remain intact under `final/evidence/build/a01_a31/`. The former canonical manifest was additionally copied to `canonical_manifest_before_a01_a35.json` in that directory. The still earlier A25 and A20 snapshots were not modified.

## Executed package validation

After installing the PDF and matching manifest, executed:

```sh
python final/reproduce/validate_package.py
```

Exit status zero, PASS. At that execution the package contained 1375 question rows, 1093 normalized check events, 45 citation keys and 124 verified retained source hashes. Table cardinalities were 800, 575, 525, 97, 108, 53 and 4825 for the respective audited register/flag/unique/excerpt/analytic/GT-certificate/GT-word tables. The validator checked proof-check event coverage and exact current source/PDF/visual-QA hash matching. It explicitly retained `formally_verified=false`.

The validation output is copied to `final/evidence/build/a01_a35/PACKAGE_VALIDATION_SNAPSHOT.json`. The build/hash gate was exercised as part of this full validator run; it is not represented as a separate unperformed execution. Later ledger-only merges may change event counts and should be followed by the parent's normal final validator run; they do not change this frozen source/PDF pair.
