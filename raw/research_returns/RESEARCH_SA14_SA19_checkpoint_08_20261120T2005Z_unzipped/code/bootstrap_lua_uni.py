"""Install lua-uni-algos from its source ZIP when the TDS endpoint is unavailable."""
from pathlib import Path
import urllib.request,zipfile,io,hashlib,json,time
root=Path(__file__).resolve().parents[1]
url='https://mirrors.ctan.org/macros/luatex/generic/lua-uni-algos.zip'
start=time.monotonic();data=urllib.request.urlopen(url,timeout=45).read()
target=root/'tmp/tex_runtime/texmf/tex/luatex/lua-uni-algos';target.mkdir(parents=True,exist_ok=True)
files=[]
with zipfile.ZipFile(io.BytesIO(data)) as z:
    for name in z.namelist():
        if name.endswith('.lua'):
            out=target/Path(name).name;out.write_bytes(z.read(name));files.append(out.name)
report=dict(url=url,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),seconds=round(time.monotonic()-start,3),files=files,status='success')
(root/'code/bootstrap_lua_uni_repro_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
