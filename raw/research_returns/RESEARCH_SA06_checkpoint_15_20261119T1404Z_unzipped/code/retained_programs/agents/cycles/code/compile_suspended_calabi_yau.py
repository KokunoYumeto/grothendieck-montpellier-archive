"""Retained four-pass C.3ai wrapper build."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import time

base=Path(__file__).resolve().parents[1]
research=base.parents[1]
out=base/'output'
name='C3ai_check'
latex=['lualatex','-interaction=nonstopmode','-halt-on-error',
       '-output-directory=agents/cycles/output',f'agents/cycles/output/{name}.tex']
commands=[latex,['bibtex',f'agents/cycles/output/{name}'],latex,latex]
env=os.environ.copy();env['TEXMFHOME']=str(research.parent/'texmf')
started=time.perf_counter()
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
runs=[]
for index,command in enumerate(commands,1):
    result=subprocess.run(command,cwd=research,env=env,capture_output=True,text=True)
    path=out/f'{stamp}_C3ai_compile_{index}.txt'
    path.write_text(result.stdout+result.stderr)
    runs.append({'command':command,'returncode':result.returncode,'output':str(path)})
    if result.returncode:break
log=(out/f'{name}.log').read_text(errors='replace')
record={'utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-started,'runs':runs,
        'diagnostics':[line for line in log.splitlines() if 'Overfull' in line or 'undefined' in line or line.startswith('!')]}
(out/'compile_suspended_calabi_yau.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
