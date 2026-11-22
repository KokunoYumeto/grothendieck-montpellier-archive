"""Install missing public CTAN font-loader dependencies in a private TeX tree."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request,zipfile,io,time,json,hashlib
root=Path(__file__).resolve().parents[1]
target=root/'tmp'/'tex_runtime'/'texmf';target.mkdir(parents=True,exist_ok=True)
names=['lualibs','luaotfload','lua-uni-algos']
def fetch(name):
    start=time.monotonic()
    url=f'https://mirrors.ctan.org/install/macros/luatex/generic/{name}.tds.zip'
    try:
        with urllib.request.urlopen(url,timeout=40) as f:data=f.read()
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for member in z.infolist():
                if member.is_dir():continue
                dest=(target/member.filename).resolve()
                if not dest.is_relative_to(target.resolve()):raise ValueError('unsafe archive path')
                dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(z.read(member))
        return dict(name=name,url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),seconds=round(time.monotonic()-start,3),status='installed privately')
    except Exception as e:return dict(name=name,url=url,status='failed',error=str(e),seconds=round(time.monotonic()-start,3))
with ThreadPoolExecutor(max_workers=2) as pool:out=list(pool.map(fetch,names))
report=json.dumps(out,indent=2)
(root/'code'/'bootstrap_luatex_output.json').write_text(report+'\n')
print(report)
