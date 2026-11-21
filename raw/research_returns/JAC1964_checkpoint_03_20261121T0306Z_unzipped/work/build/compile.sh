#!/usr/bin/env bash
set -euo pipefail
task_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
task_format="$task_root/work/build/pdflatex.fmt"
if [[ ! -f "$task_format" ]]; then
  cd "$task_root/work/build"
  TEXINPUTS=/usr/share/texlive/texmf-dist/tex//: \
  TFMFONTS=/usr/share/texlive/texmf-dist/fonts/tfm//: \
  pdftex -ini -etex -jobname=pdflatex -progname=pdflatex \
    /usr/share/texlive/texmf-dist/tex/latex/tex-ini-files/pdflatex.ini \
    > format-build.log
fi
cd "$task_root/deliverables"
for task_pass in 1 2; do
  TEXMF='{.,/usr/share/texmf,/usr/share/texlive/texmf-dist}' \
  pdftex -interaction=nonstopmode -halt-on-error -fmt="$task_format" \
    -progname=pdflatex \
    '\pdfmapfile{+lm.map}\pdfmapfile{+euler.map}\pdfmapfile{+symbols.map}\input JAC1964.tex' \
    > JAC1964.compile.txt
done
rg 'Overfull|undefined|^!|Output written' JAC1964.compile.txt || true
