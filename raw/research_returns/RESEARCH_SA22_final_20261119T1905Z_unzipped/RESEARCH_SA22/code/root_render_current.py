"""Render a specified current build and page sample; visual reading is separate."""
from pathlib import Path
from datetime import datetime,timezone
import concurrent.futures,hashlib,json,subprocess,time,sys

R=Path(__file__).resolve().parents[1]
build=int(sys.argv[1]);pages=sorted(set(map(int,sys.argv[2].split(','))))
target=R/'code'/f'root_render_current_{build:02d}_output.json'
assert not target.exists(),'Render records are immutable.'
started=time.perf_counter();stamp=datetime.now(timezone.utc).isoformat()
pdf=R/'RESEARCH_SA22_paper.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
def render(page):
 before=time.perf_counter();dest=R/'qa'/f'paper_build{build}_{page:03d}'
 p=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','110','-singlefile','-png',str(pdf),str(dest)],capture_output=True,text=True)
 return dict(page=page,exit_code=p.returncode,stderr=p.stderr,seconds=time.perf_counter()-before,path=str(dest.with_suffix('.png').relative_to(R)))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(render,pages))
out=dict(build=build,started_utc=stamp,pdf_bytes=pdf.stat().st_size,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pdfinfo=info,rendered_pages=pages,results=results,seconds=time.perf_counter()-started,scope='Rendering only. Actual image inspection is recorded after viewing.')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['pdfinfo','results']},indent=2))
sys.exit(0 if all(x['exit_code']==0 for x in results) else 1)
