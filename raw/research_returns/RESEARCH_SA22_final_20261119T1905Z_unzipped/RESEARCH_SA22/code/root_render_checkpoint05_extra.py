"""Render the new Alling comparison table and expanded source-status pages."""
from pathlib import Path
import concurrent.futures,json,subprocess,time
ROOT=Path(__file__).resolve().parents[1]
started=time.perf_counter()
def render(page):
    t=time.perf_counter();prefix=ROOT/'qa'/f'paper_cp05_{page:03d}'
    result=subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','85','-singlefile','-png',str(ROOT/'RESEARCH_SA22_paper.pdf'),str(prefix)],capture_output=True,text=True)
    return dict(page=page,exit_code=result.returncode,seconds=time.perf_counter()-t,stderr=result.stderr,path=str(prefix)+'.png')
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    rows=list(pool.map(render,[65,108,116]))
out=dict(pages=3,seconds=time.perf_counter()-started,renders=rows)
(ROOT/'code/root_render_checkpoint05_extra_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
