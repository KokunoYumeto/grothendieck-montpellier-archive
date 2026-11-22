from pathlib import Path
import concurrent.futures, datetime, hashlib, json, subprocess, time
base=Path(__file__).resolve().parents[1]
source=base/'sources/algebra_history_cirm_inventory.pdf'
dest=base/'sources/geometry_cirm_folders'
pages=[1,2,3,4,5,10,24,25,26]
def render(page):
 prefix=dest/f'page_{page:02}'
 argv=['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','1600','-png',str(source),str(prefix)]
 start=time.perf_counter();run=subprocess.run(argv,capture_output=True,text=True)
 p=prefix.with_suffix('.png')
 return {'page':page,'argv':argv,'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr,'elapsed_seconds':time.perf_counter()-start,'path':str(p.relative_to(base)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None}
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rows=list(pool.map(render,pages))
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'rows':rows,'elapsed_seconds':time.perf_counter()-start,'scope':'Remaining slides excluding the three already visually inspected by algebra; rendering does not itself certify visual inspection.'}
(base/'logs/geometry_folders_remaining.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps({'pages':len(rows),'failed':[r['page'] for r in rows if r['returncode']],'elapsed_seconds':out['elapsed_seconds']}))
