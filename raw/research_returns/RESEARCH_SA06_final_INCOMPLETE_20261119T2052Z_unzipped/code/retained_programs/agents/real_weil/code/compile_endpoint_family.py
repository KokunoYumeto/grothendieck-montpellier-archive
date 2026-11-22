#!/usr/bin/env python3
"""Four-pass standalone formatting check for the full endpoint proof."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json, os, subprocess

started=perf_counter()
base=Path(__file__).resolve().parents[1]
research=base.parents[1]
out=base/'output'
name='endpoint_family_check'
tex=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=27mm]{geometry}
\usepackage{amsmath,amsthm,amssymb,mathtools,natbib,longtable,booktabs,hyperref}
\setlength{\emergencystretch}{2em}
\begin{document}
\input{agents/real_weil/C3_endpoint_family_lifting.tex}
\input{agents/real_weil/C3_exceptional_ordinary_presentation.tex}
\bibliographystyle{plainnat}
\bibliography{agents/real_weil/SEMIPURITY_references,agents/frobenius/C3_smooth_exceptional_references,agents/frobenius/C3_fixed_family_negative_K_references,sources/root_references}
\end{document}
'''
(out/f'{name}.tex').write_text(tex)
latex=['lualatex','-interaction=nonstopmode','-halt-on-error','-output-directory=agents/real_weil/output',f'agents/real_weil/output/{name}.tex']
env=os.environ.copy()
env['TEXMFHOME']=str(research.parent/'texmf')
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
runs=[]
for index,command in enumerate([latex,['bibtex',f'agents/real_weil/output/{name}'],latex,latex],1):
    t=perf_counter()
    r=subprocess.run(command,cwd=research,env=env,capture_output=True,text=True)
    path=out/f'{stamp}_{name}_{index}.txt'
    path.write_text(r.stdout+r.stderr)
    runs.append({'command':command,'returncode':r.returncode,'runtime_seconds':perf_counter()-t,'output':str(path)})
    if r.returncode:
        break
log=(out/f'{name}.log').read_text(errors='replace')
record={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':perf_counter()-started,'runs':runs,
        'diagnostics':[line for line in log.splitlines() if 'Overfull' in line or 'undefined' in line or line.startswith('!')]}
(out/'compile_endpoint_family.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
if any(run['returncode'] for run in runs):
    raise SystemExit(1)
