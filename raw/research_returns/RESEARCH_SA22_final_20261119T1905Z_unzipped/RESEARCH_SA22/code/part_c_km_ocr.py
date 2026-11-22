#!/usr/bin/env python3
"""Render/OCR the original determinant section for source inspection."""
from pathlib import Path
import concurrent.futures, datetime, json, subprocess, time
ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'sources/knudsen_mumford1976.pdf'
OUT=ROOT/'sources/knudsen_mumford1976_pages'
OUT.mkdir(exist_ok=True)
start=time.perf_counter()
render=subprocess.run(['pdftoppm','-f','1','-l','14','-r','160','-png',str(PDF),str(OUT/'page')],capture_output=True,text=True)
images=sorted(OUT.glob('page-*.png'))
def one(p):
    base=p.with_suffix('')
    r=subprocess.run(['tesseract',str(p),str(base),'--psm','3'],capture_output=True,text=True)
    return {'file':p.name,'returncode':r.returncode}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records=list(pool.map(one,images))
text='\n'.join('\n=== PDF PAGE '+p.stem.split('-')[-1]+' ===\n'+p.with_suffix('.txt').read_text() for p in images)
(ROOT/'sources/knudsen_mumford1976_section1_ocr.txt').write_text(text)
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'render_returncode':render.returncode,'pages':records,'seconds':time.perf_counter()-start,'scope':'Source rendering and OCR, not a mathematical test; equations must be visually verified.'}
(ROOT/'code/part_c_km_ocr_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
