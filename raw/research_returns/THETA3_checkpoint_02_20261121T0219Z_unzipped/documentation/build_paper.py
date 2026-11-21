"""Build the standalone paper with explicit installed font maps."""
from pathlib import Path
import os,subprocess,sys
root=Path(__file__).resolve().parent.parent
out=root/'work/texqa';out.mkdir(exist_ok=True)
env=dict(os.environ,TEXMF='{/usr/share/texlive/texmf-dist,/usr/share/texmf}',TEXFORMATS=str(root/'work/texruntime'))
source=r'\pdfmapfile{+lm.map}\pdfmapfile{+cm.map}\pdfmapfile{+symbols.map}\pdfmapfile{+euler.map}\input{deliverables/THETA3.tex}'
for passnum in range(1,3):
 result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','-output-directory='+str(out),source],cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
 (out/f'build_pass{passnum}.txt').write_text(result.stdout)
 print('pass',passnum,'return',result.returncode)
 if result.returncode:
  print(result.stdout[-3500:]);sys.exit(result.returncode)
print('Built',out/'THETA3.pdf')
