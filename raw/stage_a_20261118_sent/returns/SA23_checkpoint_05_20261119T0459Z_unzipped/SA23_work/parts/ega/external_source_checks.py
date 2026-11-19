#!/usr/bin/env python3
"""Reproduce original-source text extraction and visual-check page images.
The PDF/text/image cache is internal evidence and excluded from the deliverable ZIP.
"""
from pathlib import Path
import fitz,json,hashlib
ROOT=Path('/workspace/scratch/0394364129a2')
E=ROOT/'sources/external/ega';E.mkdir(exist_ok=True,parents=True)
specs=[
 ('EGAIII1',E/'EGAIII1.pdf',[130]),
 ('EGAIV1',E/'EGAIV1.pdf',[23,84,85,109,110,124,126,130,146,147,203]),
 ('EGAIV4',ROOT/'SA23_work/external/bt/EGA_IV4.pdf',[5,6,205,206,207,208,226,227,260,346,347]),
 ('SGA4_2',ROOT/'SA23_work/parts/root/external/SGA4_2.pdf',[400,401,402,403,412,413,414]),
 ('SGA4_3',E/'SGA4_3.pdf',[4,26,82,101,102,103,104,105]),
 ('SGA6',ROOT/'SA23_work/parts/root/external/SGA6.pdf',[423,424,425,426,427,428]),
 ('SGA2',E/'SGA2_2005.pdf',[113])]
out=[]
for name,path,pages in specs:
 if not path.exists():out.append(dict(name=name,status='shared source unavailable'));continue
 d=fitz.open(path)
 for page in pages:d[page-1].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(E/f'{name}_audit_pdf{page}.png')
 if name=='EGAIII1':(E/'EGAIII1.txt').write_text('\n'.join(p.get_text() for p in d))
 out.append(dict(name=name,pdf_pages=len(d),physical_pages_rendered=pages,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
print(json.dumps(out,indent=2))
