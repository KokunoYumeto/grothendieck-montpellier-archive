#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
# A standard LuaLaTeX installation with lmodern, amsmath and hyperref is sufficient.
# This session used TEXINPUTS/LUAINPUTS for a locally unpacked texlive-luatex package;
# those environment overrides are optional on a complete TeX installation.
python3 code/consolidate_records.py
lualatex --interaction=nonstopmode --halt-on-error RESEARCH_SA08_C3_D031_paper.tex
bibtex RESEARCH_SA08_C3_D031_paper
lualatex --interaction=nonstopmode --halt-on-error RESEARCH_SA08_C3_D031_paper.tex
lualatex --interaction=nonstopmode --halt-on-error RESEARCH_SA08_C3_D031_paper.tex
