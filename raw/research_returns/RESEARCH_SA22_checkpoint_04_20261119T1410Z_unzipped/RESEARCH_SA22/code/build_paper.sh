#!/usr/bin/env bash
set -eu
cd "$(dirname "$0")/.."
SA22_ROOT=$(pwd)
export TEXMF="{$SA22_ROOT/logs/tex-runtime/texmf/texmf-dist,$SA22_ROOT/logs/tex-runtime/texmf,/usr/share/texmf,/usr/share/texlive/texmf-dist}"
export TEXFORMATS="$SA22_ROOT/logs/tex-runtime"
export TEXMFVAR="$SA22_ROOT/logs/tex-runtime"
export TEXMFCACHE="$SA22_ROOT/logs/tex-runtime"
lualatex -interaction=nonstopmode -halt-on-error -output-directory=logs RESEARCH_SA22_paper.tex
BIBINPUTS="$SA22_ROOT:" bibtex logs/RESEARCH_SA22_paper
lualatex -interaction=nonstopmode -halt-on-error -output-directory=logs RESEARCH_SA22_paper.tex
lualatex -interaction=nonstopmode -halt-on-error -output-directory=logs RESEARCH_SA22_paper.tex
cp logs/RESEARCH_SA22_paper.pdf RESEARCH_SA22_paper.pdf
