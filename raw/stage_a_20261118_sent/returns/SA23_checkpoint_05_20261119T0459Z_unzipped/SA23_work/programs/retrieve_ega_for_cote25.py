#!/usr/bin/env python3
"""Fetch primary publications explicitly identified in the cote25 reference audit."""
import concurrent.futures,urllib.request,json
from pathlib import Path
import fitz
P=Path('SA23_work/external');P.mkdir(exist_ok=True)
data=[('EGAIII2','https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf'),('EGAIV2','https://www.numdam.org/item/PMIHES_1965__24__5_0.pdf'),('EGAIV3','https://www.numdam.org/item/PMIHES_1966__28__5_0.pdf')]
def run(t):
 k,u=t;p=P/(k+'.pdf')
 if not p.exists():
  with urllib.request.urlopen(u,timeout=55) as r:p.write_bytes(r.read())
 d=fitz.open(p);text='\n'.join(f'\n[PHYSICAL {i+1}]\n'+page.get_text() for i,page in enumerate(d));(P/(k+'.txt')).write_text(text)
 return dict(key=k,url=u,path=str(p),bytes=p.stat().st_size,pages=len(d),text_chars=len(text))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(run,data))
print(json.dumps(results,indent=2))
