"""Targeted OCR of specified source PDF pages; run alongside sequential source OCR."""
import pathlib, subprocess, concurrent.futures, json, os, time
import fitz
root=pathlib.Path(__file__).resolve().parents[1]
src=root/'work/reference_pdfs/sga7-1.pdf'
out=src.with_suffix('')
pages=[356,357,358,399,403,404,405,406,407,417,422,423,424,425,426,431,450,483,505,508,509,511]
def one(n):
    txt=out/f'page_{n:03d}.txt'
    if txt.exists() and txt.stat().st_size>20:return n
    png=out/f'priority_{n:03d}.png'
    doc=fitz.open(src);doc[n-1].get_pixmap(dpi=150).save(png)
    target=out/f'priority_{n:03d}'
    r=subprocess.run(['tesseract',str(png),str(target),'--psm','3'],capture_output=True,text=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
    if r.returncode:raise RuntimeError(r.stderr)
    txt.write_text(target.with_suffix('.txt').read_text())
    print(json.dumps({'page':n,'status':'readable OCR ready'}),flush=True)
    return n
start=time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: results=list(pool.map(one,pages))
print(json.dumps({'pages':results,'seconds':round(time.time()-start,2)}))
