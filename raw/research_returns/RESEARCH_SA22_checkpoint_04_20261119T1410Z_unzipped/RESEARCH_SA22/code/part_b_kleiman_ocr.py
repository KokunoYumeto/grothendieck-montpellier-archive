#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import fitz,subprocess,json,time
root=Path(__file__).resolve().parents[1];pdf=root/'sources/kleiman1994.pdf';t=time.perf_counter()
def ocr(i):
 d=fitz.open(pdf);p=d[i];raw=p.get_pixmap(matrix=fitz.Matrix(2,2)).tobytes('png')
 if i>=12:(root/f'qa/kleiman1994_pdf{i+1}.png').write_bytes(raw)
 r=subprocess.run(['tesseract','stdin','stdout','-l','eng'],input=raw,stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
 return i,r.stdout.decode()
with ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(ocr,range(18)))
(root/'sources/kleiman1994.txt').write_text('\n\n'.join(f'PDF PAGE {i+1}; PRINTED PAGE {i+3}\n'+s for i,s in out)+'\n')
summary={'pages_ocr':18,'elapsed_seconds':time.perf_counter()-t};(root/'code/part_b_kleiman_ocr_output.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary)
