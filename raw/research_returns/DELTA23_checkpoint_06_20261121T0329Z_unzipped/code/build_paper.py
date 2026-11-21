#!/usr/bin/env python3
"""Compile the working paper twice; use local fallback format only when present."""
from pathlib import Path
import os,subprocess,shutil,json
ROOT=Path(__file__).resolve().parents[2]
work=ROOT/'work';out=work/'package';env=os.environ.copy()
fmt=work/'private/pdflatex.fmt'
if fmt.exists():
 font_map=work/'private/pdftex.map'
 euler_map=Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/euler.map')
 if font_map.exists() and euler_map.exists() and 'eufm10 ' not in font_map.read_text():
  with font_map.open('a') as f:f.write('\n'+euler_map.read_text())
 env.update({
 'TEXINPUTS':'.:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex//:',
 'TFMFONTS':'/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//:',
 'T1FONTS':'/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//:',
 'ENCFONTS':'/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//:',
 'TEXFONTMAPS':str(work/'private')+':/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:'})
 cmd=['pdftex','-fmt='+str(fmt.with_suffix(''))]
else:cmd=['pdflatex']
cmd+=['-interaction=batchmode','-halt-on-error','DELTA23.tex']
for i in range(2):
 r=subprocess.run(cmd,cwd=out,env=env,capture_output=True,text=True)
 if r.returncode:
  print(r.stdout[-1500:]);print((out/'DELTA23.log').read_text(errors='replace')[-5000:]);raise SystemExit(r.returncode)
log=(out/'DELTA23.log').read_text(errors='replace')
problems=[x for x in log.splitlines() if 'Overfull' in x or 'undefined' in x or 'LaTeX Warning' in x]
import fitz
doc=fitz.open(out/'DELTA23.pdf')
print(json.dumps({'passes':2,'pages':len(doc),'bytes':(out/'DELTA23.pdf').stat().st_size,'warnings':problems},indent=2))
