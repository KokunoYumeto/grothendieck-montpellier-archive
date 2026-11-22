from pathlib import Path
import os, subprocess, json, time, datetime, hashlib
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
runtime=Path('/tmp/geometry_djvu_runtime')
env=os.environ.copy();env['LD_LIBRARY_PATH']=str(runtime/'usr/lib/x86_64-linux-gnu')
src=ROOT/'sources'/'algebra_dunford_ru1966.djvu'
out=ROOT/'notes'/'algebra_dunford_ru1966_pages'
start=time.monotonic()
count=subprocess.run([str(runtime/'usr/bin/djvused'),str(src),'-e','n'],capture_output=True,text=True,env=env)
pages=[1,2,3,4,5,6,7,8,328,329,330,753,755,970,971,993,994,1045,1047,1061,1062,1064]
rows=[]
for n in pages:
 r={'physical_page':n}
 tx=subprocess.run([str(runtime/'usr/bin/djvutxt'),f'-page={n}',str(src)],capture_output=True,text=True,env=env)
 r['text_returncode']=tx.returncode;r['text_first_line']=tx.stdout.strip().splitlines()[0] if tx.stdout.strip() else ''
 (out/f'page_{n:03d}.txt').write_text(tx.stdout)
 png=out/f'page_{n:03d}.png'
 if not png.exists():
  ppm=out/f'page_{n:03d}.ppm'
  z=subprocess.run([str(runtime/'usr/bin/ddjvu'),'-format=ppm',f'-page={n}','-scale=400',str(src),str(ppm)],capture_output=True,text=True,env=env)
  r.update(render_returncode=z.returncode,render_stderr=z.stderr)
  if z.returncode==0:
   im=Image.open(ppm);im.save(png);ppm.unlink()
 if png.exists():r.update(image=str(png.relative_to(ROOT)),image_sha256=hashlib.sha256(png.read_bytes()).hexdigest())
 rows.append(r)
rec={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':round(time.monotonic()-start,3),'physical_page_count':count.stdout.strip(),'pages':rows,'index_correction':'Whole-file djvutxt skips the cover text segment. The numbered search hits in fetch76 are text-segment ordinals, not physical page numbers. The cover is physical1; English-title text is physical2. Here all selected text files are regenerated with explicit -page=n, and original-page labels are to be verified visually. Initial images were always correctly indexed by physical page.'}
(ROOT/'logs'/'algebra_dunford_ru_render77.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2))
print(json.dumps(rec,ensure_ascii=False,indent=2))
