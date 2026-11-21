#!/usr/bin/env python3
"""Build the self-contained paper, repairing only missing local TeX caches.

A normal TeX installation can simply run pdflatex HODGE_SIGN.tex twice.
This workspace's distribution files existed but its format/font-map caches
were absent; the optional local cache below avoids changing system files.
"""
from pathlib import Path
import os, subprocess, sys

r=Path(__file__).resolve().parent
cache=r/'tex_build'; cache.mkdir(exist_ok=True)
qa=r/'verification'; qa.mkdir(exist_ok=True)
env=os.environ.copy()
roots=[Path('/usr/share/texlive/texmf-dist'),Path('/usr/share/texmf')]
if all(p.exists() for p in roots):
    env['TEXMF']='{'+','.join(map(str,roots))+'}'
    env['TEXFORMATS']=str(cache)+':'
    env['TEXFONTMAPS']=str(cache)+':'
    if not (cache/'pdflatex.fmt').exists():
        p=subprocess.run(['pdftex','-ini','-etex','-jobname=pdflatex','-progname=pdflatex',
                          '-output-directory='+str(cache),'pdflatex.ini'],cwd=r,env=env,
                         stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
        (qa/'format-build.log').write_text(p.stdout)
        if p.returncode:raise SystemExit(p.stdout[-4000:])
    maps=[roots[1]/'fonts/map/dvips/lm/lm.map']+list((roots[0]/'fonts/map/dvips/amsfonts').glob('*.map'))
    (cache/'pdftex.map').write_text('\n'.join(p.read_text() for p in maps if p.exists()))

for iteration in range(1,4):
    p=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',
                      '-output-directory='+str(r),str(r/'HODGE_SIGN.tex')],cwd=r,env=env,
                     stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    (qa/f'latex-pass-{iteration}.log').write_text(p.stdout)
    if p.returncode:raise SystemExit(p.stdout[-5000:])
    if iteration>=2 and 'Rerun to get cross-references right' not in p.stdout:
        break
log=(r/'HODGE_SIGN.log').read_text(errors='replace')
for line in log.splitlines():
    if any(x in line for x in ['Overfull','undefined','Output written']):print(line)
print('PDF build completed; inspect rendered pages and the full logs.')
