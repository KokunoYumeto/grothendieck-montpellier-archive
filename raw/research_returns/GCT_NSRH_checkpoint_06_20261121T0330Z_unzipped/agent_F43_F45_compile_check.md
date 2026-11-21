# F43/F45 fragment compilation check

Date: 2026-11-21, 01:42 UTC.
Checker: `/root/rectangular_and_theta` (fragment author; this is a syntax check, not an independent mathematical review).

## Exact inputs

- `finding_F43.tex`: SHA256 `e9b810cd54934edbb0a7c8d7b31b0763de041021b56595fba6d3a4894a97fcb2`.
- `finding_F45.tex`: SHA256 `763592f7e06e94366e8831a88174ae1a91d0ddd2ec2d7d8f983ff6dbbb9188f7`.
- Wrapper: `tex_check/theta_F43_F45.tex`, using the current main paper's preamble and these two fragments as inputs. The main paper was not changed by this check.

## Procedure and result

Ran `pdflatex` with the existing `tex_check/pdflatex.fmt`, `TEXMF=/usr/share/texlive/texmf-dist`, `-interaction=nonstopmode`, and `-halt-on-error`.

**PASS:** exit code 0, eight-page PDF produced at `tex_check/theta_F43_F45.pdf`; log at `tex_check/theta_F43_F45.log`. No undefined control sequence or fatal TeX error. The first standalone pass has expected undefined references and citations because it lacks the main bibliography and has not had a second cross-reference pass. A missing default `pdftex.map` warning is followed by the explicitly loaded font maps, and the PDF is produced with Type 1 fonts.

This check does not claim final-paper layout inspection, reference resolution, or independent proof verification. The independent mathematical reviews are recorded separately in `REVIEW_POSITIVE_RANK3_GCT.md` and `agent_F45_fresh_review.md`.
