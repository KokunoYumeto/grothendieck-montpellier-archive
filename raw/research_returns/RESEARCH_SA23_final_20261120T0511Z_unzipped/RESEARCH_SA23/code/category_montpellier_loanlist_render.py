from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,hashlib,os,re,time
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
pdf=r/'sources/category_montpellier_162-1.pdf'
info=subprocess.run(['pdfinfo',str(pdf)],capture_output=True,text=True)
print(json.dumps({'command':['pdfinfo',str(pdf)],'status':info.returncode,'stdout':info.stdout,'stderr':info.stderr}),flush=True)
assert info.returncode==0
pages=int(re.search(r'^Pages:\s+(\d+)',info.stdout,re.M).group(1))
assert pages<=12, 'Catalogue has nine original pages; inspect unexpected count before broad rendering.'
source=r/'sources/category_montpellier_162-1_pages';source.mkdir(exist_ok=True)
notes=r/'notes/category_montpellier_162-1_pages';notes.mkdir(exist_ok=True)
def render(p):
    stem=source/f'page_{p:03d}';out=notes/f'page_{p:03d}';commands=[];start=time.monotonic()
    for cmd in [['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','2400','-png',str(pdf),str(stem)],['tesseract',str(stem)+'.png',str(out),'-l','eng']]:
        result=subprocess.run(cmd,capture_output=True,text=True,timeout=90,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
        commands.append({'command':cmd,'status':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
        if result.returncode:break
    log={'physical_page':p,'elapsed':time.monotonic()-start,'commands':commands}
    if stem.with_suffix('.png').exists():log['sha256_png']=hashlib.sha256(stem.with_suffix('.png').read_bytes()).hexdigest()
    out.with_suffix('.json').write_text(json.dumps(log,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(log,ensure_ascii=False),flush=True)
with ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(render,range(1,pages+1)))
full='\n\n'.join(f'PHYSICAL PAGE {p}\n'+(notes/f'page_{p:03d}.txt').read_text() for p in range(1,pages+1))
(r/'notes/category_montpellier_162-1_ocr.txt').write_text(full,encoding='utf-8')
print(json.dumps({'pages':pages,'ocr_characters':len(full)}),flush=True)
