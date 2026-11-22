"""Obtain missing TeX runtime packages locally, without changing system files.

The execution environment had LuaHBTeX but no lualatex format or font loader.
These are build dependencies, not mathematical evidence. Third-party package
archives are not included in the research deliverable.
"""
import pathlib, urllib.request, tarfile, concurrent.futures, time
root=pathlib.Path(__file__).resolve().parents[2]/'.tex-runtime'
root.mkdir(exist_ok=True)
def fetch(name):
    out=root/(name+'.tar.xz'); start=time.monotonic()
    if out.exists(): return f'{name}: cached {out.stat().st_size} bytes'
    errors=[]
    for base in ['https://ctan.math.illinois.edu/systems/texlive/tlnet/archive/',
                 'https://mirrors.ctan.org/systems/texlive/tlnet/archive/']:
        try:
            with urllib.request.urlopen(base+out.name,timeout=30) as response:
                data=response.read()
            out.write_bytes(data)
            with tarfile.open(out) as archive: archive.extractall(root,filter='data')
            return f'{name}: {len(data)} bytes; {time.monotonic()-start:.3f}s; {base}'
        except Exception as exc:
            errors.append(str(exc))
    return f'{name}: FAILED {errors}'
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    lines=list(pool.map(fetch,['luaotfload','lualibs','luatexbase','lua-uni-algos']))
text='\n'.join(lines)
print(text)
(pathlib.Path(__file__).resolve().parents[1]/'outputs'/'tex_runtime.txt').write_text(text+'\n')
