from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,os,time,hashlib
r=Path('/workspace/scratch/a7ef7e55112c/RESEARCH_SA23')
images=r/'sources/category_bourbaki_r230_pages';images.mkdir(exist_ok=True)
notes=r/'notes/category_bourbaki_r230_fredholm_pages';notes.mkdir(exist_ok=True)
pdf=r/'sources/category_bourbaki_r230_original_1.pdf'
def one(page):
    records=[];s=time.monotonic();stem=images/f'page_{page:03d}'
    commands=[['pdftoppm','-f',str(page),'-l',str(page),'-singlefile','-scale-to','2500','-png',str(pdf),str(stem)],['tesseract',str(stem.with_suffix('.png')),str(notes/f'page_{page:03d}'),'-l','eng']]
    for cmd in commands:
        p=subprocess.run(cmd,capture_output=True,timeout=60,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
        records.append({'command':cmd,'status':p.returncode,'stdout':p.stdout.decode(errors='replace'),'stderr':p.stderr.decode(errors='replace')})
        if p.returncode:break
    png=stem.with_suffix('.png')
    result={'physical_page':page,'expected_typed_page':page+86,'seconds':time.monotonic()-s,'sha256_png':hashlib.sha256(png.read_bytes()).hexdigest() if png.exists() else None,'commands':records}
    (notes/f'page_{page:03d}.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)
with ThreadPoolExecutor(max_workers=6) as pool:list(pool.map(one,range(118,136)))
full='\n'.join(f'\n=== PHYSICAL {p}; EXPECTED TYPED {p+86} ===\n'+(notes/f'page_{p:03d}.txt').read_text() for p in range(118,136))
(r/'notes/category_bourbaki_r230_fredholm_full.txt').write_text(full)
print(json.dumps({'all_pages':18,'characters':len(full),'fulltext':'notes/category_bourbaki_r230_fredholm_full.txt'}),flush=True)
