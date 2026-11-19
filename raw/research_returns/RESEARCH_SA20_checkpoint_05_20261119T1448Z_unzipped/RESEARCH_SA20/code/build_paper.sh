#!/usr/bin/env bash
set -euo pipefail
research_root="$(cd -- "$(dirname -- "$0")/.." && pwd)"
workspace_root="$(dirname -- "$research_root")"
cd -- "$research_root"
if [[ -d "$workspace_root/.tex_formats/texmf" ]]; then
  export TEXMFHOME="$workspace_root/.tex_formats/texmf"
  export TEXFORMATS="$workspace_root/.tex_formats:"
  export TEXFONTMAPS="$workspace_root/.tex_formats/maps:"
fi
python3 code/assemble_records.py
lualatex -interaction=nonstopmode -halt-on-error '\tracinglostchars=3\errorcontextlines=999\input{RESEARCH_SA20_paper.tex}'
bibtex RESEARCH_SA20_paper
lualatex -interaction=nonstopmode -halt-on-error '\tracinglostchars=3\errorcontextlines=999\input{RESEARCH_SA20_paper.tex}'
lualatex -interaction=nonstopmode -halt-on-error '\tracinglostchars=3\errorcontextlines=999\input{RESEARCH_SA20_paper.tex}'
