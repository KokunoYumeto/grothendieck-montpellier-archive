"""Build LuaLaTeX using a workspace-local format/cache if distro caches are absent."""
from pathlib import Path
import os, subprocess, sys, json, time

root=Path(__file__).resolve().parents[1]
cache=root.parent/'tex_runtime_sa08'
for folder in ['web2c','cache','config','var']:(cache/folder).mkdir(parents=True,exist_ok=True)
(root/'tex-cache').mkdir(exist_ok=True)
env=os.environ.copy()
env.update({
 'TEXMF':'{'+str(cache) + ',/usr/share/texmf,/usr/share/texlive/texmf-dist}',
 'TEXMFVAR':str(cache/'var'), 'TEXMFCONFIG':str(cache/'config'),
 # A relative cache lies inside the document directory and is accepted by
 # TeX's restrictive output-file policy as well as the workspace sandbox.
 'TEXMFCACHE':'tex-cache',
 'TEXFORMATS':str(cache/'web2c')+'//:',
})

def run(cmd,work,log):
    start=time.monotonic()
    with (root/'logs'/log).open('w') as f:
        result=subprocess.run(cmd,cwd=work,env=env,stdout=f,stderr=subprocess.STDOUT)
    print(json.dumps({'command':cmd,'code':result.returncode,'seconds':time.monotonic()-start,'log':log}),flush=True)
    if result.returncode:sys.exit(result.returncode)

if not (cache/'web2c/lualatex.fmt').exists():
    run(['luahbtex','--ini','--etex','--jobname=lualatex','--progname=lualatex','lualatex.ini'],cache/'web2c','typeset_format.txt')
name=next((a for a in sys.argv[1:] if not a.startswith('--')),'typeset_current.txt')
aux = root/'RESEARCH_SA08_paper.aux'
if ('--bibliography' in sys.argv and aux.exists()
        and '\\bibdata{' in aux.read_text()
        and '\\bibstyle{' in aux.read_text()):
    # Rebuild an existing bibliography before TeX reads it. This also recovers
    # when a corrected .bib entry left an invalid generated .bbl behind.
    # A failed TeX pass can leave a truncated .aux without bibliography data;
    # in that case the first TeX pass must restore it before BibTeX runs.
    run(['bibtex','RESEARCH_SA08_paper'],root,Path(name).stem+'_bibtex_preflight.txt')
run(['lualatex','-interaction=nonstopmode','-halt-on-error','RESEARCH_SA08_paper.tex'],root,name)
if '--bibliography' in sys.argv:
    prefix=Path(name).stem
    run(['bibtex','RESEARCH_SA08_paper'],root,prefix+'_bibtex.txt')
    for pass_number in (2,3):
        run(['lualatex','-interaction=nonstopmode','-halt-on-error','RESEARCH_SA08_paper.tex'],root,prefix+'_pass'+str(pass_number)+'.txt')
