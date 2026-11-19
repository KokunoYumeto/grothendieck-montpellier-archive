#!/usr/bin/env python3
"""Install the missing LuaLaTeX data packages into this workspace only.

Primary package pages: ctan.org/pkg/{luaotfload,lualibs,luatexbase}.
No binaries are downloaded and no system files are changed.
"""
from pathlib import Path
import urllib.request
import zipfile
import json
import time
from tex_runtime import ROOT,RUNTIME,environment

environment()
downloads=RUNTIME/'downloads'
downloads.mkdir(exist_ok=True)
results=[]
for name in ['luaotfload','lualibs','luatexbase']:
    url=f'https://mirror.math.princeton.edu/pub/CTAN/install/macros/luatex/generic/{name}.tds.zip'
    p=downloads/f'{name}.tds.zip'
    start=time.perf_counter()
    try:
        if not p.exists():
            with urllib.request.urlopen(url,timeout=45) as r:
                p.write_bytes(r.read())
        with zipfile.ZipFile(p) as z:
            for entry in z.infolist():
                if not (RUNTIME/'texmf'/entry.filename).resolve().is_relative_to((RUNTIME/'texmf').resolve()):
                    raise ValueError('Unsafe archive entry '+entry.filename)
            z.extractall(RUNTIME/'texmf')
            n=len(z.infolist())
        results.append({'package':name,'url':url,'status':'installed locally','bytes':p.stat().st_size,'entries':n,'seconds':time.perf_counter()-start})
    except Exception as exc:
        results.append({'package':name,'url':url,'status':'failed','error':str(exc),'seconds':time.perf_counter()-start})
name='lua-uni-algos'
url='https://mirror.math.princeton.edu/pub/CTAN/macros/luatex/generic/lua-uni-algos.zip'
p=downloads/'lua-uni-algos.zip'
start=time.perf_counter()
try:
    if not p.exists():
        with urllib.request.urlopen(url,timeout=45) as r:
            p.write_bytes(r.read())
    target=RUNTIME/'texmf/tex/luatex/lua-uni-algos'
    target.mkdir(parents=True,exist_ok=True)
    n=0
    with zipfile.ZipFile(p) as z:
        for entry in z.infolist():
            if entry.filename.endswith('.lua'):
                (target/Path(entry.filename).name).write_bytes(z.read(entry))
                n+=1
    results.append({'package':name,'url':url,'status':'installed local Lua modules','bytes':p.stat().st_size,'entries':n,'seconds':time.perf_counter()-start})
except Exception as exc:
    results.append({'package':name,'url':url,'status':'failed','error':str(exc),'seconds':time.perf_counter()-start})
map_sources=[Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')]
map_sources+=sorted(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts').glob('*.map'))
map_sources.append(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/rsfs/rsfs.map'))
map_entries={}
for map_path in map_sources:
    if map_path.exists():
        for line in map_path.read_text().splitlines():
            if line.strip() and not line.startswith('%'):
                map_entries.setdefault(line.split()[0],line)
map_dest=RUNTIME/'texmf/fonts/map/pdftex/local/pdftex.map'
map_dest.parent.mkdir(parents=True,exist_ok=True)
map_dest.write_text('\n'.join(map_entries.values())+'\n')
results.append({'package':'workspace font map','status':'built from installed maps',
                'sources':[str(p) for p in map_sources],'entries':len(map_entries),'destination':str(map_dest.relative_to(ROOT))})
print(json.dumps(results,indent=2))
