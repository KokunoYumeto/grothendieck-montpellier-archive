from pathlib import Path
from urllib.request import Request,urlopen
from zipfile import ZipFile
from io import BytesIO
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[1]
dest=ROOT/'build/texdeps'
dest.mkdir(parents=True,exist_ok=True)
records=[]
for name,url in [
 ('luaotfload','https://mirrors.ctan.org/macros/luatex/generic/luaotfload.zip'),
 ('lualibs','https://mirrors.ctan.org/macros/luatex/generic/lualibs.zip'),
 ('luatexbase','https://mirrors.ctan.org/macros/luatex/generic/luatexbase.zip'),
 ('lua-uni-algos','https://mirrors.ctan.org/macros/luatex/generic/lua-uni-algos.zip')]:
 start=time.monotonic(); rec={'name':name,'url':url}
 try:
  b=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read()
  with ZipFile(BytesIO(b)) as z:
   for f in z.infolist():
    p=(dest/f.filename).resolve()
    if not p.is_relative_to(dest.resolve()): raise ValueError('unsafe archive path')
   z.extractall(dest)
  rec.update(status='downloaded',bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
 except Exception as e: rec.update(status='failed',error=str(e))
 rec['seconds']=time.monotonic()-start;records.append(rec);print(rec,flush=True)
(ROOT/'code/fetch_tex_dependencies_output.json').write_text(json.dumps(records,indent=2))
