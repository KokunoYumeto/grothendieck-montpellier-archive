#!/usr/bin/env python3
"""Reproduce the primary published-page retrieval and render used in the tangent check."""
import urllib.request,fitz,json,hashlib
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'external/GrothHilbert1961.pdf'
url='https://www.numdam.org/article/SB_1960-1961__6__249_0.pdf'
if not p.exists():p.write_bytes(urllib.request.urlopen(url,timeout=60).read())
d=fitz.open(p)
for n in [22,23]:d[n].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(p.with_name(f'GrothHilbert1961_p{n+1}.png'))
out={'url':url,'pages':len(d),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'physical_pages_rendered':[23,24],'printed_pages_read':[270,271],'read':'5.3, Corollary5.4, Remark5.5; formulas visually checked on published PDF, not manuscript scans'}
print(json.dumps(out,indent=2))
