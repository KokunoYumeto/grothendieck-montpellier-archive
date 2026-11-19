"""Retained standalone C.3ak check; no external bibliography is cited."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import time

base=Path(__file__).resolve().parents[1]
research=base.parents[1]
out=base/'output'
name='C3ak_check'
command=['lualatex','-interaction=nonstopmode','-halt-on-error',
         '-output-directory=agents/cycles/output',f'agents/cycles/output/{name}.tex']
env=os.environ.copy();env['TEXMFHOME']=str(research.parent/'texmf')
started=time.perf_counter()
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
result=subprocess.run(command,cwd=research,env=env,capture_output=True,text=True)
path=out/f'{stamp}_C3ak_compile.txt'
path.write_text(result.stdout+result.stderr)
log=(out/f'{name}.log').read_text(errors='replace')
record={'utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':time.perf_counter()-started,
        'command':command,'returncode':result.returncode,'output':str(path),
        'diagnostics':[line for line in log.splitlines() if 'Overfull' in line or line.startswith('!')]}
(out/'compile_local_surjectivity_classification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
