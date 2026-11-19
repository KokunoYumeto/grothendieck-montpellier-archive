"""Fetch missing official CTAN LuaLaTeX runtime packages into a private tree."""
import concurrent.futures
import sys
import urllib.request
import zipfile
from pathlib import Path
from time import perf_counter

root=Path(__file__).resolve().parents[2]/'SA21_sources/tex_dependencies'
root.mkdir(parents=True,exist_ok=True)
def fetch(name):
 t=perf_counter();url=f'https://ctan.math.illinois.edu/macros/luatex/generic/{name}.zip'
 p=root/f'{name}.zip'
 try:
  with urllib.request.urlopen(url,timeout=30) as src,p.open('wb') as dst:
   while block:=src.read(1<<20):dst.write(block)
  with zipfile.ZipFile(p) as z:
   for info in z.infolist():
    dest=(root/info.filename).resolve()
    assert dest.is_relative_to(root.resolve())
   z.extractall(root)
  return dict(package=name,bytes=p.stat().st_size,seconds=perf_counter()-t,result='downloaded')
 except Exception as e:return dict(package=name,seconds=perf_counter()-t,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
 for result in ex.map(fetch,sys.argv[1:] or ['lualibs','luaotfload']):print(result,flush=True)
