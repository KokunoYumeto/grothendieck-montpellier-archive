from pathlib import Path
import os, subprocess
base=Path(__file__).resolve().parent.parent
env=os.environ.copy()
for key,leaf in [('TEXINPUTS','tex'),('TFMFONTS','fonts/tfm'),('VFFONTS','fonts/vf'),('T1FONTS','fonts/type1'),('ENCFONTS','fonts/enc'),('TEXFONTMAPS','fonts/map')]:
    env[key]=':'.join('/usr/share/'+p+'/'+leaf+'//' for p in ['texlive/texmf-dist','texmf'])+':'
fmt=base/'work/texcache/pdflatex.fmt'
if not fmt.exists():
    fmt.parent.mkdir(parents=True,exist_ok=True)
    subprocess.run(['pdftex','-ini','-etex','-interaction=nonstopmode','-halt-on-error','-jobname=pdflatex','-output-directory='+str(fmt.parent),'/usr/share/texlive/texmf-dist/tex/latex/tex-ini-files/pdflatex.ini'],env=env,cwd=base,check=True)
for n in range(2):
    with (base/f'work/texcache/build_pass{n+1}.log').open('w') as f:
        subprocess.run(['pdflatex','-fmt='+str(fmt),'-interaction=nonstopmode','-halt-on-error','-output-directory='+str(base/'K17_package'),str(base/'K17_package/K17.tex')],env=env,cwd=base,stdout=f,stderr=subprocess.STDOUT,check=True)
print('PDF built in two passes')
