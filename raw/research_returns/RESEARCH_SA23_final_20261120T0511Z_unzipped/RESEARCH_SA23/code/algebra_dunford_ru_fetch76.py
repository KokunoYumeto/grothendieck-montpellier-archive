from pathlib import Path
import urllib.request, hashlib, json, time, datetime, subprocess, os, re
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
runtime=Path('/tmp/geometry_djvu_runtime')
env=os.environ.copy();env['LD_LIBRARY_PATH']=str(runtime/'usr/lib/x86_64-linux-gnu')
url='https://eqworld.ipmnet.ru/ru/library/books/DanfordShvarc_t2_1966ru.djvu'
dest=ROOT/'sources'/'algebra_dunford_ru1966.djvu'
start=time.monotonic();rec={'url':url,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
try:
 with urllib.request.urlopen(url, timeout=25) as r:
  b=r.read();rec.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'))
 dest.write_bytes(b)
 rec.update(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),path=str(dest.relative_to(ROOT)))
 tx=dest.with_suffix('.txt')
 run=subprocess.run([str(runtime/'usr/bin/djvutxt'),str(dest),str(tx)],capture_output=True,text=True,env=env)
 rec['extract']={'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr}
 if run.returncode==0:
  pages=tx.read_text().split('\f');rec['text_page_segments']=len(pages)
  patterns={'groth':'groth|гротен','lidskii':'lids|лидск','letters':'письм|letter|unpublish|неопубли','history':'историческ|historical','notes':'примечания|комментар','preface':'предисловие','contents':'оглавление|содержание'}
  rec['hits']={k:[i+1 for i,p in enumerate(pages) if re.search(pat,p,re.I)] for k,pat in patterns.items()}
  for i,p in enumerate(pages):
   if re.search(patterns['groth']+'|'+patterns['lidskii'],p,re.I):
    print('PAGE',i+1)
    for m in re.finditer(patterns['groth']+'|'+patterns['lidskii'],p,re.I):print(p[max(0,m.start()-160):m.end()+220].replace('\n',' '))
  rec['initial_renders']=[]
  out=ROOT/'notes'/'algebra_dunford_ru1966_pages';out.mkdir(exist_ok=True)
  for n in [1,2,3,4,5,6,7,8]:
   ppm=out/f'page_{n:03d}.ppm'
   z=subprocess.run([str(runtime/'usr/bin/ddjvu'),'-format=ppm',f'-page={n}','-scale=400',str(dest),str(ppm)],capture_output=True,text=True,env=env)
   d={'page':n,'returncode':z.returncode,'stderr':z.stderr}
   if z.returncode==0:
    im=Image.open(ppm);p=ppm.with_suffix('.png');im.save(p);ppm.unlink();d.update(path=str(p.relative_to(ROOT)),pixels=list(im.size))
    (out/f'page_{n:03d}.txt').write_text(pages[n-1])
   rec['initial_renders'].append(d)
except Exception as e:rec['error']=repr(e)
rec.update(ended_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=round(time.monotonic()-start,3))
(ROOT/'logs'/'algebra_dunford_ru_fetch76.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2))
print(json.dumps(rec,ensure_ascii=False,indent=2))
