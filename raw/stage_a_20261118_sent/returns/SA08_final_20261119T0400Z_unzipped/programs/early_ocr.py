"""OCR selected already-downloaded reference pages; never manuscript scans."""
from pathlib import Path
import subprocess,sys,json,concurrent.futures,os
R=Path(__file__).resolve().parents[1]
name=sys.argv[1]; pages=list(map(int,sys.argv[2:]));pdf=R/'work/early/references'/f'{name}.pdf';out=pdf.with_suffix('');out.mkdir(exist_ok=True)
def job(p):
 base=out/f'page_{p:03}'
 a=subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-scale-to','2200','-png','-singlefile',str(pdf),str(base)],capture_output=True,text=True)
 b=subprocess.run(['tesseract',str(base)+'.png',str(base),'-l','eng'],capture_output=True,text=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
 return {'reference':name,'pdf_page':p,'render_returncode':a.returncode,'ocr_returncode':b.returncode,'stderr':a.stderr+b.stderr}
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 for r in pool.map(job,pages): print(json.dumps(r),flush=True)
