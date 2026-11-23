# ARCH_ALG final return

Status: **INCOMPLETE**, under the prompt’s stopping rule after two consecutive scheduled reviews without qualifying movement. Start with `FINAL_STATUS.md` and the last review in `LEDGER.md`.

- `ARCH_ALG.pdf` is the compiled 246-page paper.
- `ARCH_ALG.tex` includes the 81 proof modules under `research/`. Checked findings and open gates occupy separate parts.
- `QUESTIONS.tsv`, `CHECK_EVENTS.tsv`, and `IMPLICATIONS.md` give the exact attained states, actual verification events, and consequences.
- `research/` retains the proof sources, failed-route notes, source locators, movement-review snapshots and computation scripts.
- `FINAL_MANIFEST.json` records every archived file’s size and SHA-256 digest.

To rebuild the paper with an installed TeX distribution, run `xelatex ARCH_ALG.tex` twice from this directory; fontspec and Latin Modern fonts are required. The session’s build scripts are retained for provenance, but their absolute paths and locally rebuilt format are specific to that execution environment.

The package can be resumed with the original supplied archive and prompt. The original archive is not nested here, and no earlier checkpoint ZIP is included.
