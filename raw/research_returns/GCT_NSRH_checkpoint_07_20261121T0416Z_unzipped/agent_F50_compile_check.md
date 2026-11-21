# F50 isolated LaTeX check

Author-side syntax check; this is not an independent mathematical review or a whole-paper layout review.

- Checked at UTC: 2026-11-21T02:11:39.276026+00:00
- Fragment: `finding_F50.tex`
- Fragment SHA256: `1baea8ce4b1f12edaf7f7fc59517ecb78ef9cc0e5b80175353c58626b7b49faf`
- Wrapper: `tex_check/theta_F50.tex`, using the current main-paper preamble.
- Command: `env TEXMF=/usr/share/texlive/texmf-dist pdflatex -fmt=/workspace/scratch/b5024d19aacd/GCT_NSRH_work/tex_check/pdflatex.fmt -interaction=nonstopmode -halt-on-error -output-directory=/workspace/scratch/b5024d19aacd/GCT_NSRH_work/tex_check /workspace/scratch/b5024d19aacd/GCT_NSRH_work/tex_check/theta_F50.tex`
- Result: exit status 0; PDF produced, 7 pages, 255811 bytes.
- No undefined-control-sequence, fatal-error, or overfull-box diagnostic occurred.
- Expected standalone warnings: bibliography entries absent from this isolated wrapper, first-pass equation references, and the environment's missing default `pdftex.map` (the explicit main-preamble font maps loaded successfully).
- A full independent report review is recorded separately in `agent_F50_fresh_review.md`; final fragment match has been requested.
