# Frozen A01–A25 compilation and visual review

Date: 21 November 2026. Reviewer: GPT-6 Astra Pro; reasoning effort not exposed; `/root/effective_galois`.

## Result

PASS. The frozen standalone source compiled in three stable XeLaTeX passes to 74 pages. No source or layout modification was needed.

- Source SHA256: `33ea6de69f9a3a366c7fa1fe49b286abf854a69f118ad77fba7b2cb6abd61b75`.
- PDF SHA256: `45aeabe56bed6225c7f2eed7915de3591df3899489fdad031c3443e044dfa6f7`.
- Zero overfull boxes, undefined references, missing-character notices, or remaining rerun requests.
- Remaining log notices concern underfull spacing and a legacy amsmath `over` command.

## Visual scope

All 74 pages were rendered at a 1600-pixel long edge. I visually inspected every page in nine contact sheets. I additionally inspected full-size pages 8, 10, 12, 23, 29, 35, 37, 48, 51, 54, 60–65, 72 and 74. The independent agent `/root/gt_certificates` inspected every full-size page 38–49, including the new A21–A25 proofs, tables and equation labels; its signed-scope audit is retained in `qa/INDEPENDENT_PAGES38_49_VISUAL_QA.md`.

Neither reviewer found clipping, overlap, broken glyphs, equation-label collisions, malformed table boundaries or margin overflow. The evidence retains all nine contact sheets and all 29 distinct full-size reviewed pages, together with hashes of all 74 generated page images. The remaining images can be reproduced from the retained PDF and render script.

## Reproduction

The actual build command was:

```sh
python final/reproduce/compile_standalone_tex.py --source final/AN_GRH.tex --build-dir work/effective_galois/tex_build/a01_a25 --format-dir work/row_audit/tex_build
```

The render command was:

```sh
python work/row_audit/tex_build/render_qa.py work/effective_galois/tex_build/a01_a25/AN_GRH.pdf work/effective_galois/tex_build/a01_a25/qa
```

Exact compiler commands, environment overrides, pass logs and PDF metadata are retained. The render script is copied into the snapshot. The current reading copy and manifest were installed only after both visual reviews passed. The previous 62-page PDF, source, logs and visual evidence remain under `evidence/build/a01_a20/`; its previous canonical manifest was also preserved there.

The exact `validate_build_manifest` function from the packaged validator was executed in isolation against the installed artifacts and passed. This validates the source/PDF hashes and recorded build/visual scope. It does not claim a full package/ledger validation, a new mathematical proof reread, or formal proof-assistant verification. The manifest explicitly records `formally_verified: false`.
