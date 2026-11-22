"""Render the assigned R230 Hilbert pages; OCR is only a finding aid."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,time,json,hashlib
from datetime import datetime,timezone
b=Path(__file__).resolve().parents[1]
src=b/'sources/category_bourbaki_r230_original_1.pdf'
out=b/'sources/geometry_r230_hilbert';out.mkdir(exist_ok=True)
texts=b/'notes/geometry_r230_hilbert_ocr';texts.mkdir(exist_ok=True)
def run(argv):
 t=time.perf_counter();r=subprocess.run(argv,capture_output=True,text=True)
 return {'argv':argv,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'elapsed_seconds':time.perf_counter()-t}
def one(n):
 prefix=out/f'physical_{n:03d}'
 a=run(['pdftoppm','-f',str(n),'-l',str(n),'-singlefile','-scale-to','2300','-png',str(src),str(prefix)])
 image=prefix.with_suffix('.png')
 z={'physical_page':n,'expected_typed_page':n+86,'render':a}
 if image.exists():
  z.update(path=str(image.relative_to(b)),bytes=image.stat().st_size,sha256=hashlib.sha256(image.read_bytes()).hexdigest())
  z['ocr']=run(['tesseract',str(image),str(texts/f'physical_{n:03d}'),'-l','eng','--psm','3'])
 return z
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool: rows=list(pool.map(one,range(102,118)))
log={'utc':datetime.now(timezone.utc).isoformat(),'source':str(src.relative_to(b)),'source_bytes':src.stat().st_size,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'pages':rows,'elapsed_seconds':time.perf_counter()-start,'scope':'Rendering/OCR does not certify visual reading. Assigned physical102-117, typed188-203.'}
(b/'logs/geometry_r230_hilbert_render.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps({k:v for k,v in log.items() if k!='pages'},indent=2))
print('Failures:',[(r['physical_page'],r['render']['exit_code'],r.get('ocr',{}).get('exit_code')) for r in rows if r['render']['exit_code'] or r.get('ocr',{}).get('exit_code')])
