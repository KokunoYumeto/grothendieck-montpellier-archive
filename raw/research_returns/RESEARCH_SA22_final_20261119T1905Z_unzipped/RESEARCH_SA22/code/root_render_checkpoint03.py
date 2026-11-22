from pathlib import Path
import concurrent.futures,subprocess,time,json
R=Path(__file__).resolve().parents[1];T=time.perf_counter();pages=[4,16,29,30,31,39,85,97,99,110]
def render(p):
 t=time.perf_counter();q=R/'qa'/f'paper_cp03_{p:03d}'
 r=subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-r','85','-singlefile','-png',str(R/'RESEARCH_SA22_paper.pdf'),str(q)],capture_output=True,text=True)
 return {'page':p,'exit_code':r.returncode,'seconds':time.perf_counter()-t,'stderr':r.stderr,'path':str(q)+'.png'}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(render,pages))
s={'pages':len(pages),'seconds':time.perf_counter()-T,'renders':out}
(R/'code/root_render_checkpoint03_output.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s))
