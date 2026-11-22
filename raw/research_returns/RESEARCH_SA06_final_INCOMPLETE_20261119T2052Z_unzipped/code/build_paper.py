#!/usr/bin/env python3
"""Build the LuaLaTeX manuscript and record exact layout diagnostics."""
from pathlib import Path
import subprocess,os,re,json,datetime
ROOT=Path(__file__).resolve().parents[1]
env=os.environ.copy()
local_texmf=ROOT.parent/'texmf'
if local_texmf.is_dir():env['TEXMFHOME']=str(local_texmf)
logs=ROOT/'logs';logs.mkdir(exist_ok=True)
subprocess.run(['python3',str(ROOT/'code/assemble.py')],check=True)
aux=ROOT/'RESEARCH_SA06_paper.aux'
complete_aux=aux.exists() and '\\bibdata' in aux.read_text(errors='replace')
commands=([['bibtex','RESEARCH_SA06_paper']] if complete_aux else [])+[['lualatex','-interaction=nonstopmode','-halt-on-error','RESEARCH_SA06_paper.tex'],
          ['bibtex','RESEARCH_SA06_paper'],
          ['lualatex','-interaction=nonstopmode','-halt-on-error','RESEARCH_SA06_paper.tex'],
          ['lualatex','-interaction=nonstopmode','-halt-on-error','RESEARCH_SA06_paper.tex']]
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
for i,cmd in enumerate(commands,1):
    result=subprocess.run(cmd,cwd=ROOT,env=env,capture_output=True,text=True)
    (logs/f'{stamp}_pass{i}.txt').write_text(result.stdout+result.stderr)
    if result.returncode:
        print('Build failed:',cmd,'code',result.returncode)
        print((result.stdout+result.stderr)[-3500:])
        raise SystemExit(result.returncode)
log=(ROOT/'RESEARCH_SA06_paper.log').read_text(errors='replace')
over=[float(x) for x in re.findall(r'Overfull \\[hv]box \(([0-9.]+)pt too (?:wide|high)\)',log)]
summary={'utc':stamp,'overfull_count':len(over),'overfull_gt_2pt':sum(x>2 for x in over),
         'maximum_overfull_pt':max(over,default=0),'undefined_citations':'Citation' in log and 'undefined' in log,
         'missing_characters':len(re.findall('Missing character:',log)),
         'pdf_bytes':(ROOT/'RESEARCH_SA06_paper.pdf').stat().st_size}
(logs/f'{stamp}_layout.json').write_text(json.dumps(summary,indent=2)+'\n')
(logs/'latest_layout.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
