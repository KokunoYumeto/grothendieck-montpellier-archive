#!/usr/bin/env python3
"""Use the installed TeX sources/fonts and the locally built LaTeX format."""
import os
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
env = os.environ.copy()
env.update({
    "TEXINPUTS": ".:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:",
    "TFMFONTS": "/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//:",
    "TEXFONTMAPS": str(HERE) + ":/var/lib/texmf/fonts/map//:/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:",
    "T1FONTS": "/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//:",
    "ENCFONTS": "/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//:",
})
sys.exit(subprocess.call([
    "pdftex", "-fmt=" + str(HERE / "pdflatex.fmt"),
    "-interaction=nonstopmode", "-halt-on-error", *sys.argv[1:]
], env=env))
