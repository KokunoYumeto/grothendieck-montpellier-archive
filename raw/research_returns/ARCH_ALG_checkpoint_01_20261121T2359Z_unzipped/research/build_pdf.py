#!/usr/bin/env python3
"""Compile the current paper using this session's rebuilt XeLaTeX format."""
import os, subprocess, shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BUILD=ROOT/'work/tex_build'
ENV=os.environ.copy()
ENV.update(TEXMF='{/usr/share/texmf,/usr/share/texlive/texmf-dist}',
 TEXMFCNF='/usr/share/texlive/texmf-dist/web2c',
 TEXINPUTS='.:/usr/share/texmf/tex//:/usr/share/texlive/texmf-dist/tex//:',
 TFMFONTS='/usr/share/texmf/fonts/tfm//:/usr/share/texlive/texmf-dist/fonts/tfm//:',
 OPENTYPEFONTS='/usr/share/texmf/fonts/opentype//:/usr/share/texlive/texmf-dist/fonts/opentype//:')
command=['xetex','-fmt='+str(BUILD/'xelatex.fmt'),'-interaction=nonstopmode',
 '-halt-on-error','-output-directory='+str(BUILD),str(ROOT/'deliverable/ARCH_ALG.tex')]
run=subprocess.run(command,cwd=ROOT/'deliverable',env=ENV,capture_output=True,text=True)
(BUILD/'build_output.txt').write_text(run.stdout+'\n'+run.stderr)
print(run.stdout[-4500:]); print('exit',run.returncode)
if run.returncode: raise SystemExit(run.returncode)
if (BUILD/'ARCH_ALG.pdf').exists():
 shutil.copy2(BUILD/'ARCH_ALG.pdf',ROOT/'deliverable/ARCH_ALG.pdf')
 print('PDF copied from XeTeX output.')
 raise SystemExit(0)
driver=subprocess.run(['xdvipdfmx','-o',str(ROOT/'deliverable/ARCH_ALG.pdf'),str(BUILD/'ARCH_ALG.xdv')],cwd=ROOT/'deliverable',env=ENV,capture_output=True,text=True)
print(driver.stdout[-2000:]);print(driver.stderr[-2000:])
raise SystemExit(driver.returncode)
