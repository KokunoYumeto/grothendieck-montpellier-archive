#!/usr/bin/env python3
"""Compile with LuaLaTeX and BibTeX through latexmk.

On a standard TeX Live installation only latexmk, LuaLaTeX and the packages
named in the paper are required. The optional task-local runtime is used only
when its already-built format is present; it is not needed for reproduction.
"""
import os
from pathlib import Path
import subprocess
import sys

paper = Path(__file__).resolve().parent.parent
taskroot = paper.parent.parent
texroot = taskroot / 'tmp' / 'texmf'
formats = texroot / 'web2c' / 'luahbtex'
env = os.environ.copy()
fmt = formats / 'lualatex.fmt'
if fmt.exists():
    env['TEXMF'] = '{' + ','.join(map(str, [texroot, Path('/usr/share/texmf'), Path('/usr/share/texlive/texmf-dist')])) + '}'
    env['TEXMFVAR'] = str(texroot)
    env['TEXMFCACHE'] = str(texroot / 'cache')
    env['TEXFORMATS'] = str(formats) + '//:'
p = subprocess.run(['latexmk','-g','-lualatex','-interaction=nonstopmode','-halt-on-error',
                    'RESEARCH_SA07_paper.tex'],cwd=paper,env=env,text=True,
                   stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(paper/'code'/'paper_build.out').write_text(p.stdout)
print('LuaLaTeX paper build:',p.returncode,flush=True)
print(p.stdout[-5000:])
raise SystemExit(p.returncode)
