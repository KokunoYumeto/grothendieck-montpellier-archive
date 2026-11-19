"""Compile the independently audited E.3s--u fragments and retain diagnostics."""
from pathlib import Path
from datetime import datetime, timezone
import json, os, subprocess, time

ROOT=Path(__file__).resolve().parents[1]
RESEARCH=ROOT.parents[1]
OUT=ROOT/'output'
base='E3_morphic_check'
tex=f'agents/cycles/output/{base}.tex'
commands=[
 ['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/cycles/output',tex],
 ['bibtex',f'agents/cycles/output/{base}'],
 ['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/cycles/output',tex],
 ['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/cycles/output',tex],
]
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
environment=os.environ.copy()
environment['TEXMFHOME']=str(RESEARCH.parent/'texmf')
records=[]
start=time.perf_counter()
for i,cmd in enumerate(commands,1):
 run=subprocess.run(cmd,cwd=RESEARCH,env=environment,capture_output=True,text=True)
 output=OUT/f'{stamp}_{base}_compile_{i}.txt'
 output.write_text(run.stdout+run.stderr)
 records.append({'command':cmd,'exit':run.returncode,'output':str(output)})
 if run.returncode: break
log=(OUT/f'{base}.log').read_text(errors='replace') if (OUT/f'{base}.log').exists() else ''
diagnostics=[line for line in log.splitlines() if 'Overfull' in line or 'undefined' in line or line.startswith('!')]
result={'utc':datetime.now(timezone.utc).isoformat(),'seconds':time.perf_counter()-start,'commands':records,'diagnostics':diagnostics}
(OUT/'compile_morphic.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/f'{stamp}_compile_morphic.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
