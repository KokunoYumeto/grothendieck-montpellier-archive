#!/usr/bin/env python3
"""Compile with LuaLaTeX, including a local format when system caches are absent."""
import os
from pathlib import Path
import subprocess
import sys

paper = Path(__file__).resolve().parent.parent
taskroot = paper.parent.parent
texroot = taskroot / 'tmp' / 'texmf'
formats = texroot / 'web2c' / 'luahbtex'
formats.mkdir(parents=True, exist_ok=True)
env = os.environ.copy()
env['TEXMF'] = '{' + ','.join(map(str, [texroot, Path('/usr/share/texmf'), Path('/usr/share/texlive/texmf-dist')])) + '}'
env['TEXMFVAR'] = str(texroot)
env['TEXMFCACHE'] = str(texroot / 'cache')
env['TEXFORMATS'] = str(formats) + '//:'
(texroot / 'cache').mkdir(parents=True,exist_ok=True)
fmt = formats / 'lualatex.fmt'
if not fmt.exists():
    p = subprocess.run(['luahbtex','--ini','--jobname=lualatex','--progname=lualatex',
                        '-interaction=nonstopmode','-halt-on-error','lualatex.ini'],
                       cwd=formats,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (paper/'code'/'format_build.out').write_text(p.stdout)
    print('Local LuaLaTeX format build:',p.returncode,flush=True)
    if p.returncode:
        print(p.stdout[-10000:])
        raise SystemExit(p.returncode)
p = subprocess.run(['latexmk','-g','-lualatex','-interaction=nonstopmode','-halt-on-error',
                    'RESEARCH_SA07_paper.tex'],cwd=paper,env=env,text=True,
                   stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
(paper/'code'/'paper_build.out').write_text(p.stdout)
print('LuaLaTeX paper build:',p.returncode,flush=True)
print(p.stdout[-5000:])
raise SystemExit(p.returncode)
