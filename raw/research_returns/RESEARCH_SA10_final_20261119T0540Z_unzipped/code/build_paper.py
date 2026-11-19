"""Compile with LuaLaTeX; repair only missing task-local TeX runtime caches."""
from pathlib import Path
import os, subprocess, time, re, shutil, json
from datetime import datetime, timezone

start=time.perf_counter()
root=Path(__file__).resolve().parents[1]
(root/'logs').mkdir(exist_ok=True)
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
history=root/'logs'/'build_history'/stamp
history.mkdir(parents=True,exist_ok=False)
for old in list((root/'logs').glob('build_*.out'))+[root/'RESEARCH_SA10_paper.log']:
    if old.exists():shutil.copy2(old,history/old.name)
env=os.environ.copy()
support=root.parent/'texmf'
# This engine's lfs.iswritablefile returns nil for directories. Use the
# package's own io.open-based directory check, which respects actual access.
for source in (support/'tex'/'luatex').glob('*/*.lua'):
    original=source.read_text()
    repaired=original.replace('if lfs.isreadablefile and lfs.iswritablefile then','if false then -- use the upstream directory-aware fallback')
    repaired=repaired.replace('if lfs.isreadablefile and lfs.iswritablefile then','if false then')
    if repaired!=original: source.write_text(repaired)
env['TEXMF']='{'+str(support)+',/usr/share/texlive/texmf-dist,/usr/share/texmf}'
env['TEXMFCACHE']='tex_cache'
(root/'tex_cache').mkdir(exist_ok=True)
maps=[Path('/usr/share/texmf/fonts/map/dvips/lm/lm.map')]
maps+=sorted(Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/amsfonts').glob('*.map'))
maps+=[Path('/usr/share/texlive/texmf-dist/fonts/map/dvips/rsfs/rsfs.map')]
lines=[]; names=set()
for p in maps:
    for line in p.read_text().splitlines():
        if not line.strip() or line.startswith('%'): continue
        name=line.split()[0]
        if name not in names: names.add(name); lines.append(line)
(root/'pdftex.map').write_text('\n'.join(lines)+'\n')
if not (root/'lualatex.fmt').exists():
    with (root/'logs/build_format.out').open('w') as f:
        subprocess.run(['luahbtex','--ini','--interaction=nonstopmode','--halt-on-error','--jobname=lualatex','--progname=lualatex','/usr/share/texlive/texmf-dist/tex/latex/tex-ini-files/lualatex.ini'],cwd=root,env=env,stdout=f,stderr=subprocess.STDOUT,check=True)
passes=[]
if (root/'RESEARCH_SA10_paper.aux').exists():
    # Refresh an older bibliography before TeX can read stale unsafe text.
    passes.append(('build_bibtex_pre.out',['bibtex','RESEARCH_SA10_paper']))
passes += [
 ('build_pass1.out',['lualatex','--interaction=nonstopmode','--halt-on-error','RESEARCH_SA10_paper.tex']),
 ('build_bibtex.out',['bibtex','RESEARCH_SA10_paper']),
 ('build_pass2.out',['lualatex','--interaction=nonstopmode','--halt-on-error','RESEARCH_SA10_paper.tex']),
 ('build_pass3.out',['lualatex','--interaction=nonstopmode','--halt-on-error','RESEARCH_SA10_paper.tex'])]
for name,cmd in passes:
    with (root/'logs'/name).open('w') as f:
        result=subprocess.run(cmd,cwd=root,env=env,stdout=f,stderr=subprocess.STDOUT)
    print(name, result.returncode, flush=True)
    if result.returncode:
        print((root/'logs'/name).read_text()[-2500:]); raise SystemExit(result.returncode)
log=(root/'RESEARCH_SA10_paper.log').read_text()
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too',log)]
print('Overfull boxes:',over)
print('Overfull boxes exceeding 2pt:',sum(x>2 for x in over))
elapsed=time.perf_counter()-start
print('Runtime:',f'{elapsed:.6f}','seconds')
summary={'build_started_utc':stamp,'complete':True,'overfull_pt':over,
         'overfull_exceeding_2pt':sum(x>2 for x in over),'runtime_seconds':elapsed,
         'missing_characters':len(re.findall(r'Missing character:',log)),
         'undefined_citations':len(re.findall(r'Citation .* undefined',log))}
(root/'logs'/'build_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
