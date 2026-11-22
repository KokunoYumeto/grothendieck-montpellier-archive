"""Compile the current TeX only; never invokes Lean."""
from pathlib import Path
import argparse
import os
import subprocess

B=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('prefix');p.add_argument('--passes',type=int,default=3)
a=p.parse_args()
env=os.environ.copy()
env['TEXMF']='{/etc/texmf,/usr/share/texlive/texmf-dist,/usr/share/texmf}'
for n in range(1,a.passes+1):
 log=B/(a.prefix+f'_pass{n}.log')
 with log.open('w') as out:
  r=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','KTOWER.tex'],cwd=B,env=env,stdout=out,stderr=subprocess.STDOUT)
 lines=log.read_text(errors='replace').splitlines()
 issues=[s for s in lines if any(t in s for t in ['Warning','Overfull','Undefined','! '])]
 print({'pass':n,'exit':r.returncode,'issues':issues,'end':lines[-3:]},flush=True)
 if r.returncode:raise SystemExit(r.returncode)
