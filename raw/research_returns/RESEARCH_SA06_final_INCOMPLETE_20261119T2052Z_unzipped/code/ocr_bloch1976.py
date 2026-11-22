#!/usr/bin/env python3
"""OCR the retrieved primary scan for locating passages; verify formulas visually."""
from pathlib import Path
import concurrent.futures, subprocess, time, json
import fitz
R=Path(__file__).resolve().parents[1];src=R/'sources'/'bloch_gdz';out=src/'ocr';out.mkdir(exist_ok=True)
t=time.perf_counter();doc=fitz.open(src/'bloch1976.pdf')
for i in range(1,len(doc)):
 doc[i].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(out/f'page_{i:02}.png')
def ocr(i):
 p=out/f'page_{i:02}';r=subprocess.run(['tesseract',str(p)+'.png',str(p),'--psm','3'],capture_output=True,text=True)
 return {'page':i+1,'printed_page':214+i,'returncode':r.returncode}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rs=list(pool.map(ocr,range(1,len(doc))))
text='\n'.join(f'\n=== Printed page {214+i} ===\n'+(out/f'page_{i:02}.txt').read_text() for i in range(1,len(doc)))
(src/'bloch1976_ocr.txt').write_text(text)
rec={'pages':rs,'runtime_seconds':time.perf_counter()-t,'scope':'OCR for source location only; mathematical formulas require visual inspection.'}
(R/'code'/'ocr_bloch1976_output.json').write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec))
