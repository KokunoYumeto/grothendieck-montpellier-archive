"""Reproduce the repair for the container's incomplete TeX installation.

A normal TeX Live installation does not need this. This downloads only
public TeX runtime dependencies and creates a local LuaLaTeX format.
"""
from pathlib import Path
import hashlib,json,os,subprocess,tarfile,time,urllib.request
ROOT=Path(__file__).resolve().parents[1]
RUNTIME=ROOT/'logs'/'tex-runtime'
RUNTIME.mkdir(parents=True,exist_ok=True)
records=[]
for name in ['luaotfload','lualibs','luatexbase','lua-uni-algos','lualatex-math']:
    p=RUNTIME/(name+'.tar.xz')
    url='https://mirrors.ctan.org/systems/texlive/tlnet/archive/'+name+'.tar.xz'
    before=time.monotonic()
    if not p.exists():p.write_bytes(urllib.request.urlopen(url,timeout=45).read())
    with tarfile.open(p) as a:a.extractall(RUNTIME/'texmf',filter='data')
    records.append(dict(package=name,url=url,bytes=p.stat().st_size,
                        sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                        seconds=time.monotonic()-before))
env=os.environ.copy()
env.update(TEXMF='/usr/share/texlive/texmf-dist',TEXMFVAR=str(RUNTIME),TEXMFCACHE=str(RUNTIME))
if not (RUNTIME/'lualatex.fmt').exists():
    with (ROOT/'logs'/'format_build.out').open('w') as f:
        subprocess.run(['luahbtex','--ini','--jobname=lualatex','--progname=lualatex',
                        '--output-directory='+str(RUNTIME),'lualatex.ini'],env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
(ROOT/'logs'/'tex_runtime_manifest.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
