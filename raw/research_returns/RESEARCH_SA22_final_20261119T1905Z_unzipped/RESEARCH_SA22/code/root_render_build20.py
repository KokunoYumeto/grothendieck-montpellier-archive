"""Render distributed and changed pages of build20 for actual visual inspection."""
from pathlib import Path
import concurrent.futures,hashlib,json,subprocess,time

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
pdf=ROOT/'RESEARCH_SA22_paper.pdf'
pages=[1,4,19,20,30,35,55,60,65,66,71,76,77,79,80,81,90,106,107,116,123]
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
def render(page):
    start=time.perf_counter()
    target=ROOT/'qa'/f'paper_build20_{page:03d}'
    result=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','110','-singlefile','-png',str(pdf),str(target)],capture_output=True,text=True)
    return dict(page=page,exit_code=result.returncode,stderr=result.stderr,seconds=time.perf_counter()-start,path=str(target.with_suffix('.png').relative_to(ROOT)))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(render,pages))
out=dict(build=20,pdf_bytes=pdf.stat().st_size,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),pdfinfo=info,rendered_pages=pages,results=rows,seconds=time.perf_counter()-START,scope='Rendering only. Actual image inspection is recorded separately after viewing.')
(ROOT/'code/root_render_build20_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('results','pdfinfo')},indent=2))
