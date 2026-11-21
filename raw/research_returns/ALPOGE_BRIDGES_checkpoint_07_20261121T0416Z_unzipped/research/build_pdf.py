"""Build only; visual QA is separate and never inferred from compiler success."""
from pathlib import Path
import os, subprocess
r=Path(__file__).resolve().parents[1];d=r/'deliverables'
env=os.environ.copy()
paths={
'TEXINPUTS':'/usr/share/texlive/texmf-dist/tex//:',
'TFMFONTS':'/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm//:',
'TEXFORMATS':str(r/'research/tex_build')+':',
'OPENTYPEFONTS':'/usr/share/texmf/fonts/opentype//:/usr/share/texlive/texmf-dist/fonts/opentype//:',
'TTFONTS':'/usr/share/fonts//:',
'T1FONTS':'/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1//:',
'VFFONTS':'/usr/share/texlive/texmf-dist/fonts/vf//:/usr/share/texmf/fonts/vf//:',
'TEXFONTMAPS':'/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map//:',
'ENCFONTS':'/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc//:'}
env.update(paths)
for i in range(2):
 with (r/'research/tex_build'/f'pass{i+1}.log').open('w') as f:
  subprocess.run(['xelatex','-no-pdf','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(d),str(d/'ALPOGE_BRIDGES.tex')],env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
args=['xdvipdfmx','-q']
for f in ['cm.map','cmextra.map','symbols.map']:args+=['-f','/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts/'+f]
args+=['-o',str(d/'ALPOGE_BRIDGES.pdf'),str(d/'ALPOGE_BRIDGES.xdv')]
with (r/'research/tex_build'/'convert.log').open('w') as f:subprocess.run(args,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
print('PDF built; visual QA pending',flush=True)
