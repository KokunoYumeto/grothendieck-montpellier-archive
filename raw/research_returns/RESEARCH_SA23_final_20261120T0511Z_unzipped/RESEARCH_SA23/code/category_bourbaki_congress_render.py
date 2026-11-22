from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,hashlib,os,sys,time
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
number=sys.argv[1]
pdf=r/f'sources/category_bourbaki_congress_{number}_pdf0_1.pdf'
assert pdf.exists()
source_dir=r/f'sources/category_bourbaki_congress_{number}_pages';source_dir.mkdir(exist_ok=True)
note_dir=r/f'notes/category_bourbaki_congress_{number}_pages';note_dir.mkdir(exist_ok=True)
def page(p):
    start=time.monotonic();stem=source_dir/f'page_{p:03d}';out=note_dir/f'page_{p:03d}';records=[]
    for cmd in [['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','2400','-png',str(pdf),str(stem)],['tesseract',str(stem)+'.png',str(out),'-l','eng']]:
        proc=subprocess.run(cmd,capture_output=True,timeout=90,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
        records.append({'command':cmd,'status':proc.returncode,'stdout':proc.stdout.decode(errors='replace'),'stderr':proc.stderr.decode(errors='replace')})
        if proc.returncode:break
    result={'record':number,'physical_page':p,'seconds':time.monotonic()-start,'commands':records}
    if stem.with_suffix('.png').exists():result['sha256_png']=hashlib.sha256(stem.with_suffix('.png').read_bytes()).hexdigest()
    out.with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False),flush=True)
with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(page,range(1,8)))
full='\n\n'.join(f'=== PHYSICAL PAGE {p} ===\n'+(note_dir/f'page_{p:03d}.txt').read_text() for p in range(1,8))
(r/f'notes/category_bourbaki_congress_{number}_main_full.txt').write_text(full)
print(json.dumps({'record':number,'main_pages':7,'characters':len(full)}),flush=True)
