"""Fetch unmodified CTAN LuaLaTeX support into a task-local texmf tree."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, zipfile, io, time, os, subprocess

start=time.perf_counter()
target=Path(__file__).resolve().parents[2]/'texmf'
target.mkdir(exist_ok=True)
packages={'luaotfload':'https://mirrors.ctan.org/macros/luatex/generic/luaotfload.zip',
          'lualibs':'https://mirrors.ctan.org/macros/luatex/generic/lualibs.zip',
          'lua-uni-algos':'https://mirrors.ctan.org/macros/luatex/generic/lua-uni-algos.zip'}
def get(item):
    name,url=item
    try:
        data=urllib.request.urlopen(url,timeout=30).read()
        z=zipfile.ZipFile(io.BytesIO(data))
        out=target/'tex'/'luatex'/name
        out.mkdir(parents=True,exist_ok=True)
        n=0
        for member in z.infolist():
            path=Path(member.filename)
            if path.suffix in ('.lua','.sty','.tex','.ins','.dtx'):
                (out/path.name).write_bytes(z.read(member)); n+=1
        if name=='lualibs' and not (out/'lualibs.lua').exists():
            env=os.environ.copy()
            env['TEXMF']='{'+str(target)+',/usr/share/texlive/texmf-dist,/usr/share/texmf}'
            with (out/'generate.out').open('w') as log:
                result=subprocess.run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error',r'\input plain \let\install=y \input lualibs.dtx'],cwd=out,env=env,stdout=log,stderr=subprocess.STDOUT)
            if result.returncode:
                return f'{name}: docstrip failed; see {out}/generate.out'
        return f'{name}: {len(data)} archive bytes, {n} runtime files, URL {url}'
    except Exception as e:
        return f'{name}: FAILED {type(e).__name__}: {e}'
with ThreadPoolExecutor(max_workers=2) as pool:
    for result in pool.map(get,packages.items()): print(result)
print(f'Runtime {time.perf_counter()-start:.6f} seconds')
