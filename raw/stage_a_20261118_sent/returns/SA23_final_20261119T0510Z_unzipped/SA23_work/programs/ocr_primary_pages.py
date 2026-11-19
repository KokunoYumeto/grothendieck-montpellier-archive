#!/usr/bin/env python3
"""OCR selected pages of an explicitly retrieved published source; never manuscript inputs."""
import argparse, concurrent.futures, json, subprocess, os
from pathlib import Path
import fitz
p=argparse.ArgumentParser(); p.add_argument('pdf'); p.add_argument('pages',help='one-based comma/range list'); a=p.parse_args()
pdf=Path(a.pdf); out=pdf.parent/(pdf.stem+'_ocr'); out.mkdir(exist_ok=True)
pages=[]
for part in a.pages.split(','):
 if '-' in part:
  x,y=map(int,part.split('-')); pages.extend(range(x,y+1))
 else: pages.append(int(part))
def run(n):
 doc=fitz.open(pdf); png=out/f'p{n:03}.png'; doc[n-1].get_pixmap(matrix=fitz.Matrix(2,2)).save(png)
 env=dict(os.environ); env['OMP_THREAD_LIMIT']='1'
 r=subprocess.run(['tesseract',str(png),'stdout','-l','eng','--psm','6'],capture_output=True,text=True,check=True,env=env,timeout=90)
 (out/f'p{n:03}.txt').write_text(r.stdout); return {'physical_page':n,'text':str(out/f'p{n:03}.txt'),'image':str(png)}
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex: results=list(ex.map(run,pages))
print(json.dumps({'pdf':str(pdf),'pages':results},indent=2))
