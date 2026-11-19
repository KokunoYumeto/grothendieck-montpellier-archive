"""Reproducible LuaLaTeX/BibTeX build in the supplied TeX environment."""
from pathlib import Path
import os, subprocess, json, re, time
ROOT=Path(__file__).resolve().parents[1]
env=os.environ.copy()
env['TEXMF']='{/usr/share/texlive/texmf-dist,/usr/share/texmf}'
env['TEXINPUTS']=f'.:{ROOT}/build//:'
env['BIBINPUTS']=f'.:{ROOT}:'
env['LUAINPUTS']=f'{ROOT}/build/texdeps//:'
env['TEXMFCACHE']='build/texcache'
(ROOT/'build/texcache').mkdir(parents=True,exist_ok=True)
fmt=ROOT/'build/texmfvar/web2c/luahbtex/lualatex.fmt'
log=[]
def run(argv,cwd=ROOT):
 start=time.monotonic(); p=subprocess.run(argv,cwd=cwd,env=env,capture_output=True,text=True)
 log.append({'command':argv,'exit_code':p.returncode,'seconds':round(time.monotonic()-start,3)})
 (ROOT/'build'/('build_step_%02d.txt'%len(log))).write_text(p.stdout+'\n'+p.stderr)
 print('Step',len(log),'exit',p.returncode,'seconds',log[-1]['seconds'])
 if p.returncode: print((p.stdout+'\n'+p.stderr)[-6000:]); raise SystemExit(p.returncode)
for package,generated,source in [
 ('lualibs','lualibs.lua','lualibs.dtx'),
 ('luatexbase','luatexbase.sty','luatexbase.ins')]:
 directory=ROOT/'build/texdeps'/package
 if directory.exists() and not (directory/generated).exists():
  run(['luatex','-ini','-interaction=nonstopmode','-halt-on-error',
       '\\input plain \\input '+source],cwd=directory)
compat=ROOT/'build/texcompat.lua'
if not compat.exists():
 compat.write_text('lfs.iswritablefile=nil\nlfs.isreadablefile=nil\n')
if not fmt.exists():
 fmt.parent.mkdir(parents=True,exist_ok=True)
 run(['luahbtex','-ini','-interaction=nonstopmode','-halt-on-error','-jobname=lualatex','-progname=lualatex',f'-output-directory={fmt.parent}','lualatex.ini'])
args=['lualatex',f'--lua={ROOT}/build/texcompat.lua',f'-fmt={fmt}','-interaction=nonstopmode','-halt-on-error','-output-directory=build','RESEARCH_SA05_paper.tex']
run(args)
run(['bibtex','build/RESEARCH_SA05_paper'])
run(args);run(args)
s=(ROOT/'build/RESEARCH_SA05_paper.log').read_text(errors='replace')
ows=re.findall(r'Overfull \\[hv]box \(([^)]+)\)',s)
res={'steps':log,'overfull_boxes':ows,'over_2pt':[v for v in ows if float(re.search(r'[0-9.]+',v).group())>2]}
(ROOT/'code/build_paper_output.json').write_text(json.dumps(res,indent=2))
(ROOT/'RESEARCH_SA05_paper.pdf').write_bytes((ROOT/'build/RESEARCH_SA05_paper.pdf').read_bytes())
print(json.dumps(res,indent=2))
