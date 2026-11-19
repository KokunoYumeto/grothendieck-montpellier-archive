#!/usr/bin/env python3
import argparse,json,fitz
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('pdf');p.add_argument('pages',help='one-based PDF pages, comma separated');a=p.parse_args()
src=Path(a.pdf);d=fitz.open(src)
out=[]
for s in a.pages.split(','):
    i=int(s)-1;dest=src.parent/(src.stem+f'_pdfpage_{i+1}.png')
    d[i].get_pixmap(matrix=fitz.Matrix(1.45,1.45)).save(dest)
    out.append({'pdf_page':i+1,'path':str(dest)})
print(json.dumps(out))
