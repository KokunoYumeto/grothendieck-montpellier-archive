"""Render build21, including both pages of the clarified B1b scope argument."""
from pathlib import Path
import concurrent.futures, hashlib, json, subprocess, time

R=Path(__file__).resolve().parents[1]
started=time.perf_counter()
pdf=R/'RESEARCH_SA22_paper.pdf'
pages=[1,4,19,20,30,35,55,60,65,66,68,69,71,76,77,79,80,81,90,106,107,116,123]
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True,check=True).stdout
def render(page):
    before=time.perf_counter()
    target=R/'qa'/f'paper_build21_{page:03d}'
    p=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','110','-singlefile','-png',str(pdf),str(target)],capture_output=True,text=True)
    return dict(page=page,exit_code=p.returncode,stderr=p.stderr,seconds=time.perf_counter()-before,path=str(target.with_suffix('.png').relative_to(R)))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(render,pages))
out=dict(build=21,pdf_bytes=pdf.stat().st_size,pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
         pdfinfo=info,rendered_pages=pages,results=results,seconds=time.perf_counter()-started,
         scope='Rendering only. Actual page inspection is recorded separately after viewing.')
(R/'code/root_render_build21_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('pdfinfo','results')},indent=2))
