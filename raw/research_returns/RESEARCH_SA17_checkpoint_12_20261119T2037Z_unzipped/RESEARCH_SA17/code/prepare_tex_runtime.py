"""Fetch missing official TeX Live runtime files into an isolated TEXMF tree.

This repairs the local compiler only. It is not part of any mathematical proof.
Run with one scratch destination argument, then set TEXMFHOME to that directory.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
import hashlib, json, sys, tarfile, time, shutil
root=Path(__file__).resolve().parents[1]
dest=Path(sys.argv[1]).resolve()
dest.mkdir(parents=True,exist_ok=True)
start=time.perf_counter()
def fetch(package):
    url=f'https://mirrors.ctan.org/systems/texlive/tlnet/archive/{package}.tar.xz'
    t=time.perf_counter()
    try:
        with urlopen(url,timeout=40) as r:data=r.read()
        path=dest/(package+'.tar.xz');path.write_bytes(data)
        with tarfile.open(path) as tar:tar.extractall(dest,filter='data')
        return dict(package=package,url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),seconds=time.perf_counter()-t,status='saved')
    except Exception as e:return dict(package=package,url=url,status='failed',error=str(e),seconds=time.perf_counter()-t)
with ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(fetch,sys.argv[2:] or ['luaotfload','lualibs','luatexbase','lua-uni-algos']))
if (dest/'texmf-dist').exists():
    for path in (dest/'texmf-dist').iterdir():
        if path.is_dir():shutil.copytree(path,dest/path.name,dirs_exist_ok=True)
        else:shutil.copy2(path,dest/path.name)
result={'scope':'compiler dependency recovery','seconds':time.perf_counter()-start,'packages':results}
(root/'logs'/('tex_runtime_fetch_'+str(int(time.time()))+'.json')).write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
