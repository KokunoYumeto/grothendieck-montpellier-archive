"""Render previously uninspected archival-method slide images for reading."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, subprocess, time

root=Path(__file__).resolve().parents[1]
source=root/'sources/algebra_history_cirm_inventory.pdf'
folder=root/'sources/geometry_cirm_folders'
folder.mkdir(exist_ok=True)
pages=[6,7,8,11,12,14,15,17,18,19,20,21,22,23]
def render(page):
 dest=folder/f'page_{page:02}'
 argv=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2400','-png',str(source),str(dest)]
 start=time.perf_counter()
 run=subprocess.run(argv,capture_output=True,text=True)
 record={'page':page,'argv':argv,'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr,'elapsed_seconds':time.perf_counter()-start}
 p=dest.with_suffix('.png')
 if p.exists():
  record.update(path=str(p.relative_to(root)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
 return record
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 records=list(pool.map(render,pages))
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source':str(source.relative_to(root)),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'pages':records,'total_elapsed_seconds':time.perf_counter()-start,'scope':'Images rendered here are not claimed read until separately displayed; slides9,13,16 were already inspected by algebra.'}
(root/'logs/geometry_folders_render.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps({'pages':len(records),'failed':[r['page'] for r in records if r['returncode']],'elapsed_seconds':out['total_elapsed_seconds']},ensure_ascii=False))
