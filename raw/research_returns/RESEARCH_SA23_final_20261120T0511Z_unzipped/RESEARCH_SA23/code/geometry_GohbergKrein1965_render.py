from pathlib import Path
import os,subprocess,json,time
from PIL import Image
base=Path("/workspace/scratch/a7ef7e55112c/RESEARCH_SA23")
runtime=Path("/tmp/geometry_djvu_runtime")
env=os.environ.copy();env["LD_LIBRARY_PATH"]=str(runtime/"usr/lib/x86_64-linux-gnu")
dest=base/"notes/geometry_GohbergKrein1965_pages";dest.mkdir(exist_ok=True)
pages=[1,2,7,131,132,199,427,428,431]
texts=(base/"notes/geometry_GohbergKrein1965_full.txt").read_text().split("\f")
results=[];started=time.time()
for n in pages:
    ppm=runtime/f"geometry_GK_page_{n:03}.ppm"
    p=subprocess.run([str(runtime/"usr/bin/ddjvu"),"-format=ppm",f"-page={n}","-scale=400",str(base/"sources/geometry_GohbergKrein1965.djvu"),str(ppm)],capture_output=True,text=True,env=env)
    record={"one_based_djvu_page":n,"returncode":p.returncode,"stdout":p.stdout,"stderr":p.stderr}
    if p.returncode==0:
        im=Image.open(ppm);record["pixels"]=list(im.size)
        im.save(dest/f"page_{n:03}.png");ppm.unlink()
        (dest/f"page_{n:03}.txt").write_text(texts[n-1])
    results.append(record)
log={"elapsed_seconds":time.time()-started,"pages":results}
(base/"logs/geometry_GohbergKrein1965_render.json").write_text(json.dumps(log,ensure_ascii=False,indent=2))
print(json.dumps(log))

