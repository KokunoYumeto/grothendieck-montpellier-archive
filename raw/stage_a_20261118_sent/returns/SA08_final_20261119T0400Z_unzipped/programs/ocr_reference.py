"""OCR requested PDF pages for source lookup. Formula conclusions require image review."""
import argparse, pathlib, subprocess, concurrent.futures, json, time, os
import fitz
p=argparse.ArgumentParser();p.add_argument('pdf');p.add_argument('first',type=int);p.add_argument('last',type=int);p.add_argument('--workers',type=int,default=6);a=p.parse_args()
src=pathlib.Path(a.pdf); out=src.with_suffix('')
out.mkdir(exist_ok=True)
def one(n):
    doc=fitz.open(src);page=doc[n-1]
    png=out/f'page_{n:03d}.png';txt=out/f'page_{n:03d}'
    if not txt.with_suffix('.txt').exists() or txt.with_suffix('.txt').stat().st_size < 20:
        page.get_pixmap(dpi=150).save(png)
        r=subprocess.run(['tesseract',str(png),str(txt),'--psm','3'],capture_output=True,text=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
        if r.returncode:raise RuntimeError(r.stderr)
    return n,txt.with_suffix('.txt').read_text()
start=time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
    results=list(pool.map(one,range(a.first,a.last+1)))
combined=out/'combined.txt'
combined.write_text(''.join(f'\n=== PDF PAGE {n} ===\n{t}' for n,t in sorted(results)))
print(json.dumps({'pdf':str(src),'first':a.first,'last':a.last,'pages':len(results),'seconds':round(time.time()-start,2),'text':str(combined)}))
