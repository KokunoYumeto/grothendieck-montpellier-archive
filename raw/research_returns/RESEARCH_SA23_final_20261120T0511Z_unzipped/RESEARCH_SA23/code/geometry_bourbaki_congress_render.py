"""Render explicitly selected original congress pages; preserve commands and hashes."""
from pathlib import Path
import argparse,subprocess,time,json,hashlib
from datetime import datetime,timezone
b=Path(__file__).resolve().parents[1]
a=argparse.ArgumentParser();a.add_argument('record',type=int);a.add_argument('first',type=int);a.add_argument('last',type=int);o=a.parse_args()
src=b/f'sources/geometry_bourbaki_congress_{o.record}_1.pdf'
dest=b/f'sources/geometry_bourbaki_congress_{o.record}_pages';dest.mkdir(exist_ok=True)
argv=['pdftoppm','-f',str(o.first),'-l',str(o.last),'-scale-to','2200','-png',str(src),str(dest/'page')]
t=time.perf_counter();r=subprocess.run(argv,capture_output=True,text=True);elapsed=time.perf_counter()-t
rows=[]
for p in sorted(dest.glob('page-*.png')):
 rows.append({'path':str(p.relative_to(b)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
log={'utc':datetime.now(timezone.utc).isoformat(),'record':o.record,'first':o.first,'last':o.last,'argv':argv,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'elapsed_seconds':elapsed,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'pages':rows,'rendering_is_not_reading':True}
(b/f'logs/geometry_bourbaki_congress_render_{o.record}_{o.first}_{o.last}.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps({k:v for k,v in log.items() if k not in ['pages','stdout']},indent=2));print('Image files',len(rows))
