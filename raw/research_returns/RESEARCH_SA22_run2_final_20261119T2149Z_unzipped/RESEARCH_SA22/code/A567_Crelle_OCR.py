#!/usr/bin/env python3
"""Render and OCR acquired original scans; OCR is a finding aid, not a proof."""
import concurrent.futures,hashlib,json,os,subprocess,time
from datetime import datetime,timezone
from pathlib import Path
import fitz
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'qa/A567_Crelle';OUT.mkdir(exist_ok=True)
specs=[('A567_Nakamura1990_405',117),('A567_Nakamura1990_411',205),('A567_IharaNakamura1997',125)]
def render(spec):
 name,start=spec;p=ROOT/'literature'/(name+'.pdf')
 subprocess.run(['pdftoppm','-f','2','-r','160','-png',str(p),str(OUT/name)],check=True,capture_output=True)
 return name,start,sorted(OUT.glob(name+'-*.png'))
def ocr(p):
 dest=p.with_suffix('');env=dict(os.environ);env['OMP_THREAD_LIMIT']='1'
 subprocess.run(['tesseract',str(p),str(dest),'--psm','3'],check=True,capture_output=True,env=env)
 return {'image':str(p.relative_to(ROOT)),'text':str(p.with_suffix('.txt').relative_to(ROOT)),'image_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
begin=datetime.now(timezone.utc).isoformat();t=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:papers=list(pool.map(render,specs))
allpages=[p for _,_,ps in papers for p in ps]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(ocr,allpages))
for name,start,ps in papers:
 text='\n\n'.join(f'PRINTED PAGE {start+i} / PDF PAGE {i+2}\n'+p.with_suffix('.txt').read_text() for i,p in enumerate(ps))
 (ROOT/'literature'/(name+'_OCR.txt')).write_text(text)
 print(name,len(ps),'original scan pages OCRed',flush=True)
out={'started_at_utc':begin,'finished_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'54 original scan canvases including any blank ending page; covers excluded; OCR must be checked against page images for mathematical symbols','pages_count':len(rows),'elapsed_seconds':time.perf_counter()-t,'rows':rows}
(ROOT/'logs/A567_Crelle_OCR.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
