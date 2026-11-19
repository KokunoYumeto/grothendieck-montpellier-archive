"""Render and OCR the scanned primary-source final section; text is a locator aid.
No mathematical verdict is inferred automatically from OCR.
"""
from pathlib import Path
import subprocess
B=Path(__file__).resolve().parents[1]
D=B/'research'/'ArtinMilne_pages';D.mkdir(exist_ok=True)
for page in range(11,20):
 stem=D/f'page{page:02d}'
 if stem.with_suffix('.txt').exists():
  print('reuse',page)
  continue
 a=subprocess.run(['pdftoppm','-f',str(page),'-singlefile','-scale-to','2100','-png',str(B/'research'/'ArtinMilne1976.pdf'),str(stem)],capture_output=True,text=True)
 print('render',page,a.returncode,a.stderr.strip())
 b=subprocess.run(['tesseract',str(stem)+'.png',str(stem),'-l','eng'],capture_output=True,text=True)
 print('ocr',page,b.returncode,b.stderr.strip())
with (D/'combined.txt').open('w') as out:
 for p in sorted(D.glob('page*.txt')):
  out.write('\n===== PDF '+p.stem+' =====\n'+p.read_text())
